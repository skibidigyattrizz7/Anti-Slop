#!/usr/bin/env python3
"""Count verifiable-looking signals in a text or markdown report. Evidence for a reviewer, never a verdict.

CANNOT open links or verify claims. It cannot tell if a source exists, says what is cited,
or if a number is true. A clean run proves nothing about accuracy: open every source yourself.

Counts: vague attributions, numbers with no link or citation marker in the same paragraph,
links, a Sources section, trend filler, suspiciously round statistics.

Usage:
  python3 check_report.py FILE          human-readable report
  python3 check_report.py --json FILE   JSON report
  python3 check_report.py --selftest

Exit codes: 0 no flags, 1 one or more flags, 2 usage error.
Phrase lists last_verified: 2026-11-17 (see references/tells.md).
"""
import json, re, sys

VAGUE = r"(?i)\b(?:studies (?:show|suggest|have shown)|experts (?:say|agree|argue)|research (?:shows|suggests|indicates)|many believe|it is widely (?:known|believed)|according to (?:experts|studies))\b"
FILLER = r"(?i)\b(?:growing rapidly|rapidly growing|increasingly (?:important|popular|common)|plays? a (?:crucial|vital|key) role|highlights? the importance|in today's (?:fast-paced|digital))"
NUM = r"\b\d[\d,.]*\s?%|\b\d{1,3}(?:,\d{3})+\b|\b\d+(?:\.\d+)?\s?(?:million|billion|trillion)\b|\$\s?\d[\d,.]*"
CITE = r"https?://|\[\d+\]|\[[^\]]+\]\(|\([A-Z][A-Za-z-]+(?: et al\.)?,? \d{4}\)|\[source|\[link"
SOURCES_HEAD = r"(?im)^\s*(?:#+\s*)?(?:\*\*)?(?:sources|references|bibliography|works cited)(?:\*\*)?:?\s*$"


def analyze(text):
    paras = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    uncited = []
    for p in paras:
        if re.match(r"\s*#+\s", p) and len(p.splitlines()) == 1:
            continue
        if re.search(NUM, p) and not re.search(CITE, p):
            uncited.append(p.strip()[:80])
    stats = re.findall(r"(\d+(?:\.\d+)?)\s?%", text)
    round_stats = [s for s in stats if float(s) >= 10 and float(s) % 5 == 0 and "." not in s]
    r = {
        "words": len(re.findall(r"\w+", text)),
        "vague_attributions": len(re.findall(VAGUE, text)),
        "trend_filler": len(re.findall(FILLER, text)),
        "links": len(re.findall(r"https?://[^\s)\]>]+", text)),
        "has_sources_section": bool(re.search(SOURCES_HEAD, text)),
        "paragraphs_with_numbers_but_no_citation": len(uncited),
        "uncited_examples": uncited[:3],
        "round_percentages": round_stats,
    }
    flags = []
    if r["vague_attributions"]: flags.append("vague attributions")
    if r["trend_filler"]: flags.append("trend filler")
    if r["paragraphs_with_numbers_but_no_citation"]: flags.append("numbers with no citation in the same paragraph")
    if r["words"] > 300 and r["links"] == 0: flags.append("no links in 300+ words")
    if r["words"] > 300 and not r["has_sources_section"]: flags.append("no Sources section")
    if len(round_stats) >= 3: flags.append("3+ round percentages")
    r["flags"] = flags
    return r


def report(r):
    out = [f"{k}: {v}" for k, v in r.items() if k != "flags"]
    out.append("flags: " + ("; ".join(r["flags"]) if r["flags"] else "none"))
    out.append("Counts are evidence only. This script cannot open links or verify claims.")
    return "\n".join(out)


def selftest():
    bad = ("Studies show that 73% of teams use it. The market is growing rapidly and 50% of firms agree. "
           "Experts agree it is increasingly important, and 40% plan to adopt it.\n\nAdoption hit 20% in 2024.")
    r = analyze(bad)
    assert r["vague_attributions"] == 2 and r["trend_filler"] == 2, r
    assert r["paragraphs_with_numbers_but_no_citation"] == 2 and len(r["round_percentages"]) == 3, r
    assert r["flags"], r
    good = "Adoption was 23% in 2024 (https://example.org/survey).\n\n## Sources\n"
    g = analyze(good)
    assert g["links"] == 1 and g["paragraphs_with_numbers_but_no_citation"] == 0 and g["flags"] == [], g
    assert g["has_sources_section"], g
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
    try:
        r = analyze(open(paths[0], encoding="utf-8").read())
    except OSError as e:
        print(e, file=sys.stderr)
        return 2
    print(json.dumps(r, indent=2) if as_json else report(r))
    return 1 if r["flags"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
