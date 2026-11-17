#!/usr/bin/env python3
"""Count measurable fiction tells in a text file. Evidence for a reviewer, never a verdict.

Usage:
  python3 count_story_tells.py FILE          human-readable report
  python3 count_story_tells.py --json FILE   JSON report
  python3 count_story_tells.py --selftest

Exit codes: 0 no flags, 1 one or more flags, 2 usage error.
Lists last_verified: 2026-11-17 (see references/tells.md).
"""
import json, re, sys

STOCK_NAMES = ["Elara", "Elias", "Kael", "Lyra", "Thorne", "Mara", "Aria", "Luna", "Seraphina",
               "Elena", "Eldric", "Aurelia", "Finn", "Willow"]
STOCK_PHRASES = ["a shiver ran down", "shiver down", "little did they know", "little did he know",
                 "little did she know", "a testament to", "the air was thick with", "whispers of",
                 "tapestry", "in that moment, they understood", "in that moment, she realized",
                 "in that moment, he realized", "heart pounded", "heart hammered", "breath she didn't know",
                 "breath he didn't know", "let out a breath"]
BODY_EMOTION = [r"heart (?:pounded|raced|hammered|skipped|clenched|sank)", r"pulse (?:raced|quickened)",
                r"(?:chest|throat|stomach) (?:tightened|clenched|knotted|dropped)",
                r"knot in (?:her|his|their|my) (?:stomach|throat|chest)",
                r"(?:shiver|chill) (?:ran|crept|went) (?:down|up)", r"butterflies",
                r"hands (?:trembled|shook)", r"tears (?:pricked|stung|welled)", r"breath (?:caught|hitched)"]
LESSON = [r"\b(?:realized|understood|learned|knew) (?:that )?(?:\w+ ){0,6}?(?:really|truly|always|never|only|is|was) ",
          r"\bin that moment\b", r"\bsome things\b", r"\bthe real (?:treasure|magic|gift|power)\b",
          r"\bwas (?:never|always) about\b", r"\bnot alone\b", r"\bhome (?:all along|at last)\b",
          r"\bfor the first time in (?:years|a long time|her life|his life)\b"]
QUOTE = re.compile(r'"[^"\n]*"|“[^”\n]*”')


def names_found(text):
    return {n: c for n in STOCK_NAMES if (c := len(re.findall(r"\b" + n + r"\b", text)))}


def analyze(text):
    low = text.lower()
    words = re.findall(r"[A-Za-z']+", text)
    n = max(len(words), 1)
    names = names_found(text)
    phrases = {p: low.count(p) for p in STOCK_PHRASES if p in low}
    body = {p: len(re.findall(p, low)) for p in BODY_EMOTION if re.search(p, low)}
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    last = paras[-1] if paras else ""
    lesson = [p for p in LESSON if re.search(p, last.lower())]
    dwords = sum(len(re.findall(r"[A-Za-z']+", q)) for q in QUOTE.findall(text))
    r = {
        "words": len(words),
        "stock_names": names,
        "stock_phrases": phrases,
        "body_sensation_hits": sum(body.values()),
        "body_sensation_per_1000": round(sum(body.values()) * 1000 / n, 2),
        "last_paragraph_lesson_patterns": len(lesson),
        "dialogue_share": round(dwords / n, 2),
        "em_dashes_per_1000": round(text.count(chr(8212)) * 1000 / n, 2),
    }
    flags = []
    if names: flags.append("stock names present")
    if phrases: flags.append("stock phrases present")
    if r["body_sensation_hits"] >= 3 or (r["words"] >= 300 and r["body_sensation_per_1000"] > 5):
        flags.append("many body-sensation emotion phrases")
    if lesson: flags.append("last paragraph may state a lesson")
    if r["words"] >= 300 and r["dialogue_share"] < 0.05: flags.append("almost no dialogue")
    r["flags"] = flags
    return r


def report(r):
    out = [f"{k}: {v}" for k, v in r.items() if k != "flags"]
    out.append("flags: " + ("; ".join(r["flags"]) if r["flags"] else "none"))
    out.append("Counts are evidence, not proof. Judge shape, cost and ending yourself.")
    return "\n".join(out)


def selftest():
    ai = ('In a quiet town, Elias Thorne gazed out. A shiver ran down his spine; his heart pounded and his throat '
          'tightened. Little did he know it was a testament to hope.\n\n'
          'In that moment, he understood that love was always about letting go.')
    r = analyze(ai)
    assert "Elias" in r["stock_names"] and "Thorne" in r["stock_names"], r
    assert r["stock_phrases"] and r["body_sensation_hits"] >= 3, r
    assert r["last_paragraph_lesson_patterns"] >= 1, r
    assert r["flags"], r
    ok = analyze('"You took the umbrella," Ines said.\n\n"I did." Dale did not look up. The bus left.')
    assert ok["flags"] == [] and ok["stock_names"] == {} and ok["dialogue_share"] > 0.3, ok
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
        text = open(paths[0], encoding="utf-8").read()
    except OSError as e:
        print(e, file=sys.stderr)
        return 2
    r = analyze(text)
    print(json.dumps(r, indent=2) if as_json else report(r))
    return 1 if r["flags"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
