#!/usr/bin/env python3
"""Count measurable writing tells in a text file. Evidence for a reviewer, never a verdict.

Usage:
  python3 count_tells.py FILE          human-readable report
  python3 count_tells.py --json FILE   JSON report
  python3 count_tells.py --selftest

Exit codes: 0 no flags, 1 one or more flags, 2 usage error.
Word lists last_verified: 2026-10-22 (see references/tells.md).
"""
import json, re, statistics, sys

CLAUDE_TICS = ["genuinely", "quietly", "honestly", "load-bearing", "doing real work", "stated plainly"]
CLUSTER_WORDS = ["crucial", "pivotal", "underscore", "underscores", "seamless", "seamlessly", "robust", "elevate",
                 "unlock", "testament", "landscape", "leverage", "foster", "vibrant", "transformative", "realm"]
EXPIRED = ["delve", "delves", "tapestry", "intricate", "showcasing"]
PATTERNS = {
    "not X, it's Y": r"(?i)\b(?:it's|it is|this is|that's|isn't|is not) (?:not )?(?:just |only |merely )?[^.,;]{1,40}[,;] (?:it's|it is|but)\b",
    "not only... but also": r"(?i)\bnot only\b[^.]{1,80}\bbut also\b",
    # the reversed contrast: "..., not the night before."
    "Y, not X tail": r"(?i), not (?!only\b)[^.,;!?]{1,40}[.!?]",
    "summary closer": r"(?im)^\s*(?:in conclusion|in summary|overall|ultimately)\b",
    "stock phrase": r"(?i)\b(?:in today's (?:fast-paced|digital)|great question|it'?s (?:important|worth) (?:to note|noting|mentioning)|at the end of the day|when it comes to)",
    "-ing tail": r"(?i), (?:ensuring|highlighting|underscoring|showcasing|reflecting|emphasizing|fostering|enabling)\b",
    "vague attribution": r"(?i)\b(?:studies (?:show|suggest)|experts (?:say|agree|argue)|research (?:shows|suggests)|many believe)\b",
}


def find(words, text):
    return {w: n for w in words if (n := len(re.findall(r"\b" + re.escape(w) + r"\b", text, re.I)))}


def analyze(text):
    words = re.findall(r"[A-Za-z']+", text)
    n = max(len(words), 1)
    sents = [s for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text)) if len(s.split()) > 2]
    lens = [len(s.split()) for s in sents]
    lines = [l for l in text.splitlines() if l.strip()]
    r = {
        "words": len(words),
        "em_dashes_per_1000": round(text.count("—") * 1000 / n, 2),
        "claude_tics": find(CLAUDE_TICS, text),
        "cluster_words": find(CLUSTER_WORDS, text),
        "expired_words": find(EXPIRED, text),
        "patterns": {k: len(re.findall(p, text)) for k, p in PATTERNS.items() if re.search(p, text)},
        # numbers are a rough stand-in for checkable specifics
        "numbers_per_100_words": round(len(re.findall(r"\b\d[\d,.:]*\b", text)) * 100 / n, 2),
        "sentence_len_mean": round(statistics.mean(lens), 1) if lens else 0,
        # low variation = even rhythm
        "sentence_len_variation": round(statistics.pstdev(lens) / statistics.mean(lens), 2) if len(lens) > 1 else None,
        "bullet_line_share": round(sum(bool(re.match(r"\s*(?:[-*•]|\d+\.)\s", l)) for l in lines) / max(len(lines), 1), 2),
        "bold_count": len(re.findall(r"\*\*[^*]+\*\*", text)),
    }
    flags = []
    if r["em_dashes_per_1000"] > 3: flags.append("em dashes above ~3/1000")
    if r["claude_tics"]: flags.append("Claude-leaning tic words present")
    if sum(r["cluster_words"].values()) >= 3: flags.append("3+ cluster words")
    if r["patterns"]: flags.append("formula patterns: " + ", ".join(r["patterns"]))
    v = r["sentence_len_variation"]
    if v is not None and v < 0.35 and r["words"] > 150: flags.append("very even sentence rhythm")
    if r["numbers_per_100_words"] == 0 and r["words"] > 150: flags.append("no numbers in 150+ words")
    r["flags"] = flags
    return r


def report(r):
    out = [f"{k}: {v}" for k, v in r.items() if k != "flags"]
    out.append("flags: " + ("; ".join(r["flags"]) if r["flags"] else "none"))
    out.append("Counts are evidence, not proof. Judge content and specifics too.")
    return "\n".join(out)


def selftest():
    ai = ("In today's fast-paced world, it's important to note that learning is crucial. "
          "It's not just a skill, it's a journey. Genuinely, this pivotal step quietly unlocks growth — seamlessly, "
          "ensuring success. Studies show it works. In conclusion, it is a testament to effort.")
    r = analyze(ai)
    assert r["claude_tics"] and r["cluster_words"], r
    for p in ("not X, it's Y", "stock phrase", "-ing tail", "vague attribution"):
        assert p in r["patterns"], (p, r["patterns"])
    assert r["flags"]
    assert "Y, not X tail" in analyze("Check the hardware a week before, not the night before.")["patterns"]
    clean = analyze("I fixed the bent screw at 11 p.m. The arm held.")
    assert clean["patterns"] == {} and clean["flags"] == [], clean
    print("selftest ok")


def main(argv):
    if argv == ["--selftest"]:
        selftest()
        return 0
    as_json = argv[:1] == ["--json"]
    paths = argv[1:] if as_json else argv
    if len(paths) != 1:
        print(__doc__, file=sys.stderr)
        return 2
    r = analyze(open(paths[0], encoding="utf-8").read())
    print(json.dumps(r, indent=2) if as_json else report(r))
    return 1 if r["flags"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
