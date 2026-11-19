#!/usr/bin/env python3
"""Run the Anti-Slop evals with headless Claude Code (`claude -p`).

What it does:
  quality   For each held-out task in evals/heldout.json: write it N times with
            the skill and N times without, then a judge scores each pair blind
            (random labels A/B) with agents/judge.md and the skill's rubric.
  triggers  For each phrase in evals/<skill>/prompts.md, check whether a plain
            request loads the right skill when the plugin is installed.

Usage (from anywhere):
  python3 tools/run_evals.py                      everything, 3 runs per side
  python3 tools/run_evals.py --skills human-ui --runs 1
  python3 tools/run_evals.py --only triggers
  python3 tools/run_evals.py --only agents       specialists fix earlier no-skill outputs
  python3 tools/run_evals.py --selftest           no Claude calls

Results go to evals/results/<timestamp>/ (results.json and summary.md).
Writers default to Haiku and the judge to Sonnet. Each run is a real API call.
"""
import argparse, concurrent.futures as cf, json, random, re, shutil, subprocess, sys, tempfile, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# keep the user's own hooks and MCP servers out of every run
BASE = ["claude", "-p", "--no-session-persistence", "--strict-mcp-config",
        "--settings", '{"disableAllHooks":true}']


def claude(args, prompt, cwd, timeout=600):
    r = subprocess.run(BASE + args + [prompt], cwd=cwd, capture_output=True, text=True,
                       timeout=timeout, stdin=subprocess.DEVNULL)
    return r.stdout


def strip_fence(text):
    m = re.fullmatch(r"\s*```[\w-]*\n(.*?)\n```\s*", text, re.S)
    return m.group(1) if m else text.strip() + "\n"


def write(task, with_skill, model, cwd):
    if with_skill:
        skill_dir = ROOT / "skills" / task["skill"]
        prompt = (f"First read {skill_dir}/SKILL.md and follow it. You may read files in that folder.\n\n"
                  f"Task: {task['task']}\n\nReply with only the finished work, nothing before or after it.")
        args = ["--disable-slash-commands", "--tools", "Read,Glob,Grep", "--add-dir", str(skill_dir), "--model", model]
    else:
        prompt = f"Task: {task['task']}\n\nReply with only the finished work, nothing before or after it."
        args = ["--disable-slash-commands", "--tools", "", "--model", model]
    return strip_fence(claude(args, prompt, cwd))


def parse_json(text):
    m = re.search(r"\{.*\}", text, re.S)
    return json.loads(m.group(0)) if m else None


def judge(task, files, model, cwd):
    """files: {"A": path, "B": path}. Returns parsed JSON or None."""
    body = (ROOT / "agents" / "judge.md").read_text(encoding="utf-8").split("---", 2)[2]
    names = ", ".join(f"{k} = {Path(p).name}" for k, p in files.items())
    look = ""
    if task["ext"] == "html":
        look = (f"Open each page for real: run node {ROOT}/skills/see-it-run/scripts/shoot.cjs <file> --out {cwd}/shots-<label> "
                "and look at phone.png and desktop.png with Read before you score.\n")
    prompt = (f"{body}\n\n## This job\n\nCategory skill folder: {task['skill']}. Skills live under {ROOT}/skills/.\n"
              f"Brief: {task['brief']}\nFiles, in {cwd}: {names}. Judge each on its own. You do not know how they were made.\n{look}\n"
              "After judging, reply with ONLY one JSON object and no other text:\n"
              '{"files": {"A": {"passes": 0, "applicable": 0, "verdict": "Ship or Fix first", "must_pass": "PASS or FAIL"}, '
              '"B": {...}}, "better": "A or B or tie", "reason": "one sentence"}')
    args = ["--disable-slash-commands", "--tools", "Read,Glob,Grep,Bash", "--add-dir", str(ROOT),
            "--allowedTools", "Read Glob Grep Bash(python3:*) Bash(node:*)", "--model", model]
    try:
        return parse_json(claude(args, prompt, cwd, timeout=900))
    except (json.JSONDecodeError, subprocess.TimeoutExpired):
        return None


def run_quality(task, runs, writer, judge_model, out):
    rows = []
    for i in range(runs):
        work = Path(tempfile.mkdtemp(prefix="eval-"))
        texts = {"with": write(task, True, writer, work), "without": write(task, False, writer, work)}
        labels = ["A", "B"]
        random.shuffle(labels)
        files = {}
        for arm, label in zip(("with", "without"), labels):
            p = work / f"{label}.{task['ext']}"
            p.write_text(texts[arm], encoding="utf-8")
            files[label] = p
            (out / f"{task['id']}-run{i + 1}-{arm}.{task['ext']}").write_text(texts[arm], encoding="utf-8")
        verdict = judge(task, dict(sorted(files.items())), judge_model, work)
        arm_of = dict(zip(labels, ("with", "without")))
        row = {"task": task["id"], "skill": task["skill"], "run": i + 1, "labels": arm_of, "judge": verdict}
        if verdict and "files" in verdict:
            for label, arm in arm_of.items():
                f = verdict["files"].get(label, {})
                row[arm] = {"score": f.get("passes", 0) / max(f.get("applicable", 1), 1),
                            "verdict": f.get("verdict"), "must_pass": f.get("must_pass")}
            b = verdict.get("better", "tie")
            row["better"] = arm_of.get(b, "tie")
        rows.append(row)
        shutil.rmtree(work, ignore_errors=True)
    return rows


SPECIALIST = {"human-writing": "writing", "human-chat": "chat", "human-code": "code", "human-fiction": "fiction",
              "human-ui": "ui", "human-media": "media", "human-games": "games", "real-reports": "reports"}


def run_agent(task, model, judge_model, out, source):
    """A specialist fixes the no-skill output from an earlier run, then a judge scores before vs after, blind."""
    name = f"{task['id']}-run1-without.{task['ext']}"
    found = [source / name] if source else sorted((ROOT / "evals" / "results").glob(f"*/{name}"))
    before = found[-1] if found else None
    if not before or not before.exists():
        return [{"task": task["id"], "skill": task["skill"], "error": f"no earlier output named {name}"}]
    work = Path(tempfile.mkdtemp(prefix="agent-"))
    shutil.copy(before, work / f"draft.{task['ext']}")
    agent = f"{SPECIALIST[task['skill']]}-specialist"
    body = (ROOT / "agents" / f"{agent}.md").read_text(encoding="utf-8").split("---", 2)[2]
    prompt = (f"{body}\n\n## This job\n\nSkills live under {ROOT}/skills/. Work to fix: {work}/draft.{task['ext']}.\n"
              f"Brief: {task['brief']}\nWrite the fixed version to {work}/fixed.{task['ext']} and leave the draft as it is. "
              "No writing sample from the user. Then give your report.")
    args = ["--disable-slash-commands", "--tools", "Read,Glob,Grep,Write,Edit,Bash", "--add-dir", str(ROOT),
            "--allowedTools", f"Read Glob Grep Write(/{work}/**) Edit(/{work}/**) Bash(python3:*) Bash(node:*)", "--model", model]
    report = claude(args, prompt, work, timeout=900)
    fixed = work / f"fixed.{task['ext']}"
    row = {"task": task["id"], "skill": task["skill"], "agent": agent, "report": report[-1500:]}
    if not fixed.exists():
        row["error"] = "specialist wrote no fixed file"
        return [row]
    shutil.copy(fixed, out / f"{task['id']}-{agent}-fixed.{task['ext']}")
    labels = ["A", "B"]
    random.shuffle(labels)
    files = {}
    for arm, label in zip(("before", "after"), labels):
        p = work / f"{label}.{task['ext']}"
        shutil.copy(before if arm == "before" else fixed, p)
        files[label] = p
    verdict = judge(task, dict(sorted(files.items())), judge_model, work)
    arm_of = dict(zip(labels, ("before", "after")))
    row["judge"] = verdict
    if verdict and "files" in verdict:
        for label, arm in arm_of.items():
            f = verdict["files"].get(label, {})
            row[arm] = {"score": f.get("passes", 0) / max(f.get("applicable", 1), 1),
                        "verdict": f.get("verdict"), "must_pass": f.get("must_pass")}
    shutil.rmtree(work, ignore_errors=True)
    return [row]


def trigger_phrases(skill):
    """Return (should, should_not) phrase lists from evals/<skill>/prompts.md."""
    path = ROOT / "evals" / skill / "prompts.md"
    if not path.exists():
        return [], []
    should, should_not, cur = [], [], None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            low = line.lower()
            cur = should_not if ("not" in low or "near" in low) else should if "trigger" in low else None
        elif cur is not None and re.match(r"\s*(?:[-*]|\d+\.)\s", line):
            phrase = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", line)
            phrase = re.sub(r"\s*\((?:[\w-]+)\)\s*$", "", phrase).strip().strip('"')
            if phrase:
                cur.append(phrase)
    return should, should_not


def skills_called(stream):
    called = []
    for line in stream.splitlines():
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        if e.get("type") == "assistant":
            for c in e["message"].get("content", []):
                if c.get("type") == "tool_use" and c.get("name") == "Skill":
                    called.append(str(c.get("input", {}).get("skill", "")))
    return called


def run_trigger(skill, phrase, expected, model, cwd):
    # hooks are off in every run, so add the plugin's startup note the way the real hook would
    note = (ROOT / "hooks" / "chat-rules.md").read_text(encoding="utf-8")
    args = ["--plugin-dir", str(ROOT), "--append-system-prompt", note, "--tools", "Skill", "--model", model,
            "--output-format", "stream-json", "--verbose", "--max-turns", "2"]
    called = skills_called(claude(args, phrase, cwd, timeout=300))
    hit = any(c.split(":")[-1] == skill for c in called)
    return {"skill": skill, "phrase": phrase, "expected": expected, "called": called, "ok": hit == expected}


def summarise(quality, triggers, agents=()):
    lines = ["# Eval run", "", "Scores are passes over applicable rubric checks, averaged over runs.", ""]
    if quality:
        lines += ["| Skill | Runs | With skill | Without | Judge preferred with skill | Must-pass held (with / without) |",
                  "|---|---|---|---|---|---|"]
        by = {}
        for r in quality:
            by.setdefault(r["skill"], []).append(r)
        for skill, rs in sorted(by.items()):
            ok = [r for r in rs if "with" in r and "without" in r]
            if not ok:
                lines.append(f"| {skill} | {len(rs)} | judge failed | | | |")
                continue
            avg = lambda arm: sum(r[arm]["score"] for r in ok) / len(ok)
            spread = lambda arm: max(r[arm]["score"] for r in ok) - min(r[arm]["score"] for r in ok)
            wins = sum(r.get("better") == "with" for r in ok)
            mp = lambda arm: sum(r[arm]["must_pass"] == "PASS" for r in ok)
            lines.append(f"| {skill} | {len(ok)} | {avg('with'):.2f} (spread {spread('with'):.2f}) | "
                         f"{avg('without'):.2f} (spread {spread('without'):.2f}) | {wins} of {len(ok)} | "
                         f"{mp('with')} / {mp('without')} |")
        lines.append("")
    if agents:
        lines += ["| Specialist | Before fix | After fix | Must-pass after |", "|---|---|---|---|"]
        for r in sorted(agents, key=lambda r: r["skill"]):
            if "after" not in r:
                lines.append(f"| {r.get('agent', r['skill'])} | {r.get('error', 'judge failed')} | | |")
                continue
            lines.append(f"| {r['agent']} | {r['before']['score']:.2f} {r['before']['verdict']} | "
                         f"{r['after']['score']:.2f} {r['after']['verdict']} | {r['after']['must_pass']} |")
        lines.append("")
    if triggers:
        lines += ["| Skill | Triggered when it should | Stayed quiet when it should |", "|---|---|---|"]
        by = {}
        for t in triggers:
            by.setdefault(t["skill"], []).append(t)
        for skill, ts in sorted(by.items()):
            pos = [t for t in ts if t["expected"]]
            neg = [t for t in ts if not t["expected"]]
            lines.append(f"| {skill} | {sum(t['ok'] for t in pos)} of {len(pos)} | {sum(t['ok'] for t in neg)} of {len(neg)} |")
        lines.append("")
    return "\n".join(lines)


def selftest():
    assert strip_fence("```html\n<p>x</p>\n```\n") == "<p>x</p>"
    assert parse_json('Here: {"files": {}, "better": "A"} done')["better"] == "A"
    s, n = trigger_phrases("human-ui")
    assert len(s) >= 6 and len(n) >= 6, (s, n)
    assert not any(p.endswith(")") for p in n), n
    stream = '{"type":"assistant","message":{"content":[{"type":"tool_use","name":"Skill","input":{"skill":"anti-slop:human-ui"}}]}}'
    assert skills_called(stream) == ["anti-slop:human-ui"]
    rows = [{"skill": "x", "with": {"score": 1, "must_pass": "PASS"}, "without": {"score": 0.5, "must_pass": "FAIL"}, "better": "with"}]
    assert "1 of 1" in summarise(rows, [])
    ag = [{"skill": "x", "agent": "x-specialist", "before": {"score": 0.5, "verdict": "Fix first"},
           "after": {"score": 1.0, "verdict": "Ship", "must_pass": "PASS"}}]
    assert "x-specialist | 0.50 Fix first | 1.00 Ship | PASS" in summarise([], [], ag)
    print("selftest ok")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--skills", help="comma-separated skill names (default: all with tasks or prompts)")
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--writer", default="haiku")
    ap.add_argument("--judge", default="sonnet")
    ap.add_argument("--trigger-model", default="sonnet")
    ap.add_argument("--only", choices=["quality", "triggers", "agents"])
    ap.add_argument("--from-run", help="results folder whose no-skill outputs the specialists fix (default: the latest output for each task)")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return 0
    if not shutil.which("claude"):
        sys.exit("claude CLI not found. Install Claude Code first.")
    tasks = json.loads((ROOT / "evals" / "heldout.json").read_text(encoding="utf-8"))
    wanted = set(a.skills.split(",")) if a.skills else None
    if wanted:
        tasks = [t for t in tasks if t["skill"] in wanted]
    out = ROOT / "evals" / "results" / time.strftime("%Y-%m-%d-%H%M")
    out.mkdir(parents=True, exist_ok=True)
    quality, triggers, agents = [], [], []
    if a.only == "agents":
        source = ROOT / "evals" / "results" / a.from_run if a.from_run else None
        with cf.ThreadPoolExecutor(a.workers) as pool:
            for j in cf.as_completed([pool.submit(run_agent, t, a.judge, a.judge, out, source) for t in tasks]):
                agents.extend(j.result())
                print(".", end="", flush=True)
        print()
        (out / "results.json").write_text(json.dumps({"agents": agents}, indent=2), encoding="utf-8")
        summary = summarise([], [], agents)
        (out / "summary.md").write_text(summary, encoding="utf-8")
        print(summary)
        print(f"Saved to {out.relative_to(ROOT)}")
        return 0
    with cf.ThreadPoolExecutor(a.workers) as pool:
        jobs = []
        if a.only not in ("triggers",):
            jobs += [pool.submit(run_quality, t, a.runs, a.writer, a.judge, out) for t in tasks]
        if a.only != "quality":
            skills = sorted(wanted or {p.name for p in (ROOT / "evals").iterdir() if (p / "prompts.md").exists()})
            cwd = tempfile.mkdtemp(prefix="trig-")
            for s in skills:
                should, should_not = trigger_phrases(s)
                jobs += [pool.submit(run_trigger, s, p, True, a.trigger_model, cwd) for p in should]
                jobs += [pool.submit(run_trigger, s, p, False, a.trigger_model, cwd) for p in should_not]
        for j in cf.as_completed(jobs):
            res = j.result()
            (quality.extend if isinstance(res, list) else triggers.append)(res)
            print(".", end="", flush=True)
    print()
    (out / "results.json").write_text(json.dumps({"quality": quality, "triggers": triggers}, indent=2), encoding="utf-8")
    summary = summarise(quality, triggers)
    (out / "summary.md").write_text(summary, encoding="utf-8")
    print(summary)
    print(f"Saved to {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
