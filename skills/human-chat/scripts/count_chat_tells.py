#!/usr/bin/env python3
"""Count chat-reply habits in a text file. Counts are evidence for a reviewer, never a verdict.

Usage:
  python3 count_chat_tells.py FILE          human-readable report
  python3 count_chat_tells.py --json FILE   JSON report
  python3 count_chat_tells.py --selftest

Exit codes: 0 no flags, 1 one or more flags, 2 usage error.
Word lists last_verified: 2026-10-22 (see references/tells.md).
"""
import json, re, sys

OPENER = r"(?i)^\W*(?:great|good|excellent|fantastic|interesting|wonderful) (?:question|point|idea|catch)\b|^\W*(?:absolutely|certainly|of course|sure thing)\b|^\W*you'?re (?:absolutely|totally|completely) right\b|^\W*what a (?:great|fantastic|wonderful|fascinating)\b|^\W*that'?s a (?:great|fantastic|fascinating|really interesting|excellent)\b"
PLAN = r"(?i)\blet'?s (?:break (?:this|it) down|dive in|walk through|unpack|get started|take a look)\b|\bhere'?s a (?:breakdown|step-by-step|quick overview)\b|\bi'?ll (?:walk you through|break (?:this|it) down)\b|\blet me (?:break|walk|explain)\b"
OFFER = r"(?i)\b(?:would you like|do you want|want me to|let me know if|feel free to|don'?t hesitate to|i can also|happy to help)\b"
HOPE = r"(?i)\b(?:i hope (?:this|that) helps|hope this helps|hope that helps|hope this clarifies)\b"
HEDGE = r"(?i)\b(?:may potentially|might possibly|could potentially|it depends|generally speaking|in some cases|to some extent|perhaps|arguably|somewhat|it'?s possible that|it may be|it might be|tends to)\b"


def paragraphs(text):
    return [p for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]


def analyze(text):
    words = re.findall(r"[A-Za-z']+", text)
    paras = paragraphs(text)
    lines = [l for l in text.splitlines() if l.strip()]
    first = paras[0] if paras else ""
    last = paras[-1] if paras else ""
    n = max(len(words), 1)
    # openers only count at the start of the reply; offers and "hope" only in the last two paragraphs
    tail = "\n\n".join(paras[-2:])
    r = {
        "words": len(words),
        "flattering_openers": len(re.findall(OPENER, first)),
        "plan_announcements": len(re.findall(PLAN, text)),
        "closing_offers": len(re.findall(OFFER, tail)),
        "hope_this_helps": len(re.findall(HOPE, text)),
        "hedges": len(re.findall(HEDGE, text)),
        "hedges_per_100_words": round(len(re.findall(HEDGE, text)) * 100 / n, 2),
        "exclamation_marks": text.count("!"),
        "bullet_line_share": round(sum(bool(re.match(r"\s*(?:[-*•]|\d+[.)])\s", l)) for l in lines) / max(len(lines), 1), 2),
        "heading_count": len([l for l in lines if re.match(r"\s{0,3}#{1,6}\s", l)]),
        "em_dashes": text.count(chr(0x2014)),
        "last_paragraph_words": len(last.split()),
    }
    flags = []
    if r["flattering_openers"]: flags.append("flattering opener")
    if r["plan_announcements"]: flags.append("plan announcement")
    if r["closing_offers"]: flags.append("closing offer")
    if r["hope_this_helps"]: flags.append("hope-this-helps line")
    if r["hedges"] >= 3 or r["hedges_per_100_words"] > 2: flags.append("hedges cluster")
    if r["exclamation_marks"] >= 2: flags.append("2+ exclamation marks")
    if r["bullet_line_share"] > 0.5 and r["words"] < 200: flags.append("mostly bullets in a short reply")
    if r["heading_count"] and r["words"] < 300: flags.append("headings in a short reply")
    r["flags"] = flags
    return r


def report(r):
    out = [f"{k}: {v}" for k, v in r.items() if k != "flags"]
    out.append("flags: " + ("; ".join(r["flags"]) if r["flags"] else "none"))
    out.append("Counts are evidence, not proof. Judge the facts and the fit to the question too.")
    return "\n".join(out)


def selftest():
    bad = ("Great question! Let's break this down. There are many factors that may potentially matter, "
           "and it depends. Generally speaking, results can vary!\n\n## Key points\n\n- Fast\n- Cheap\n- Safe\n\n"
           "I hope this helps! Would you like me to compare more options?")
    r = analyze(bad)
    assert r["flattering_openers"] == 1, r
    assert r["plan_announcements"] == 1, r
    assert r["closing_offers"] >= 1 and r["hope_this_helps"] == 1, r
    assert r["hedges"] >= 3 and r["exclamation_marks"] == 3, r
    assert r["heading_count"] == 1 and r["bullet_line_share"] > 0.2, r
    assert r["flags"], r
    good = analyze("Pick B. It costs 40 less and A's extras do not matter here. Only choose A if you need offline mode.")
    assert good["flags"] == [] and good["hedges"] == 0, good
    # a mid-reply "Sure" or offer-like phrase in the body must not count as an opener or closing offer
    mid = analyze("The fix is one line.\n\nSure enough, it compiles.\n\nChange x to 4.\n\nThen rerun.")
    assert mid["flattering_openers"] == 0 and mid["closing_offers"] == 0, mid
    print("selftest ok")


def main(argv):
    if argv == ["--selftest"]:
        selftest()
        return 0
    as_json = argv[:1] == ["--json"]
    paths = argv[1:] if as_json else argv
    if len(paths) != 1 or paths[0].startswith("--"):
        print(__doc__, file=sys.stderr)
        return 2
    try:
        text = open(paths[0], encoding="utf-8").read()
    except OSError as e:
        print(f"cannot read {paths[0]}: {e}", file=sys.stderr)
        return 2
    r = analyze(text)
    print(json.dumps(r, indent=2) if as_json else report(r))
    return 1 if r["flags"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
