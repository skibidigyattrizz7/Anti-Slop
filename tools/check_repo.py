#!/usr/bin/env python3
"""Check that every skill and agent in the repo follows docs/BUILD_SPEC.md.

Usage: python3 tools/check_repo.py     (run from anywhere)
Exit codes: 0 all good, 1 problems found.

Checks: frontmatter, name matches folder, description length and "Use when",
SKILL.md body size, file references that point nowhere, script self-tests,
agent frontmatter, and that dist/chatgpt is up to date.
"""
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BODY_LIMIT = 500      # words, with a little slack for tables
BODY_SLACK = 20
DESC_LIMIT = 600      # characters
REF_LIMIT = 1150      # words; pattern files from humanizer run a little long
problems = []


def bad(where, what):
    problems.append(f"{where}: {what}")


def frontmatter(path):
    m = re.match(r"---\n(.*?)\n---\n(.*)", path.read_text(encoding="utf-8"), re.S)
    if not m:
        bad(path.relative_to(ROOT), "no frontmatter")
        return {}, ""
    fields = dict(re.findall(r"^([\w-]+):\s*(.+)$", m.group(1), re.M))
    return fields, m.group(2)


def check_skill(skill):
    rel = skill.relative_to(ROOT)
    fields, body = frontmatter(skill / "SKILL.md")
    if fields.get("name") != skill.name:
        bad(rel, f"name {fields.get('name')!r} does not match folder")
    desc = fields.get("description", "").strip("\"'")
    if not desc:
        bad(rel, "no description")
    if len(desc) > DESC_LIMIT:
        bad(rel, f"description is {len(desc)} chars, limit {DESC_LIMIT}")
    if "use when" not in desc.lower() and "use for" not in desc.lower() and "use " not in desc.lower():
        bad(rel, "description does not say when to use the skill")
    words = len(body.split())
    if words > BODY_LIMIT + BODY_SLACK:
        bad(rel, f"SKILL.md body is {words} words, limit {BODY_LIMIT}")
    for md in [skill / "SKILL.md", *sorted(skill.glob("references/*.md"))]:
        text = md.read_text(encoding="utf-8")
        if md.parent.name == "references" and len(text.split()) > REF_LIMIT:
            bad(md.relative_to(ROOT), f"{len(text.split())} words, limit {REF_LIMIT}")
        for ref in set(re.findall(r"`((?:references|scripts)/[\w./*-]+)`", text)):
            if not list(skill.glob(ref)):
                bad(md.relative_to(ROOT), f"points to missing {ref}")
    for script in sorted(skill.glob("scripts/*.py")):
        r = subprocess.run([sys.executable, str(script), "--selftest"], capture_output=True, text=True)
        if r.returncode != 0:
            bad(script.relative_to(ROOT), "selftest failed: " + (r.stderr or r.stdout).strip()[-200:])


def check_agent(agent, skill_names):
    rel = agent.relative_to(ROOT)
    fields, body = frontmatter(agent)
    if fields.get("name") != agent.stem:
        bad(rel, f"name {fields.get('name')!r} does not match file name")
    if not fields.get("description"):
        bad(rel, "no description")
    for section in ("## Rules", "## Report format"):
        if section not in body and "## Safety rules" not in body:
            bad(rel, f"missing section {section}")
    for name, path in re.findall(r"\*\*/skills/([\w-]+)/([\w./-]+)", body):
        if name not in skill_names:
            bad(rel, f"points to unknown skill {name}")
        elif not (ROOT / "skills" / name / path).exists():
            bad(rel, f"points to missing skills/{name}/{path}")


def main():
    skills = sorted(p for p in (ROOT / "skills").iterdir() if (p / "SKILL.md").exists())
    for skill in skills:
        check_skill(skill)
    names = {s.name for s in skills}
    for agent in sorted((ROOT / "agents").glob("*.md")):
        check_agent(agent, names)
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "build_chatgpt.py"), "--check"], capture_output=True, text=True)
    if r.returncode != 0:
        bad("dist/chatgpt", (r.stderr or r.stdout).strip())
    for p in problems:
        print("PROBLEM", p)
    print(f"{len(skills)} skills, {len(list((ROOT / 'agents').glob('*.md')))} agents, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
