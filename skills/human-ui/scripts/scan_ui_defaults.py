#!/usr/bin/env python3
"""Count default-cluster signs in an HTML, CSS, JSX or TSX file. Evidence for a reviewer, never a verdict.

Usage:
  python3 scan_ui_defaults.py FILE          human-readable report
  python3 scan_ui_defaults.py --json FILE   JSON report
  python3 scan_ui_defaults.py --selftest

Exit codes: 0 no flags, 1 one or more flags, 2 usage error.
Lists last_verified: 2026-11-17 (see references/tells.md).

Signs counted: purple or indigo gradients, gradient text, system-only, Inter or Geist as the only fonts,
backdrop-blur or glass, very large radius on most elements, 3-column grids, pill badge above an h1,
emoji in headings, scroll fade-in classes, colored left-border cards, buzzword copy, em dashes.

What it cannot see: it reads source text only. It cannot judge a rendered page, computed styles,
styles set in other files, spacing, hierarchy, contrast, whether the copy is specific, or whether a
choice was made for a reason. A 3-column grid may be right for the content. Inter may be chosen on
purpose. Use the counts to know where to look, then look at the page at 375px and 1280px.
"""
import colorsys, json, re, sys

FLAGS_NOTE = "Counts are evidence, not proof. Open the page at 375px and 1280px and judge it."
KEYWORDS = {"sans-serif", "serif", "monospace", "system-ui", "ui-sans-serif", "ui-serif", "ui-monospace",
            "ui-rounded", "inherit", "initial", "unset", "cursive", "fantasy", "emoji", "math"}
# Fonts every device already has. A stack made only of these, Inter or Geist is the default look.
SYSTEM_FONTS = {"-apple-system", "blinkmacsystemfont", "segoe ui", "helvetica", "helvetica neue", "arial", "roboto",
                "sfmono-regular", "menlo", "consolas", "liberation mono", "courier new", "monaco"}
DEFAULT_FONTS = {"inter", "geist", "geist sans", "geist mono"}
EMOJI = "[\U0001F300-\U0001FAFF☀-⛿✅✨⭐❌❤]"
BUZZ = ["elevate", "unlock", "seamless", "seamlessly", "supercharge", "all-in-one", "revolutionize"]
PURPLE_NAMES = r"(?:purple|indigo|violet|fuchsia)"


def hue_is_purple(hexcolor):
    h = hexcolor.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    hue, light, sat = colorsys.rgb_to_hls(r, g, b)[0] * 360, colorsys.rgb_to_hls(r, g, b)[1], colorsys.rgb_to_hls(r, g, b)[2]
    return 245 <= hue <= 295 and sat > 0.3 and 0.15 < light < 0.85


def purple_gradients(t):
    n = len(re.findall(r"\b(?:from|via|to)-" + PURPLE_NAMES + r"-\d{2,3}\b", t))
    for m in re.finditer(r"(?:linear|radial|conic)-gradient\(([^;{}]*)", t, re.I):
        body = m.group(1)
        if re.search(PURPLE_NAMES, body, re.I) or any(hue_is_purple(c) for c in re.findall(r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b", body)):
            n += 1
    return n


def _split(value):
    return [f.strip(" '\"").lower() for f in value.split(",") if f.strip(" '\"")]


def font_check(t):
    families = []
    for m in re.finditer(r"font-family\s*:\s*([^;}]+)", t, re.I):
        families += _split(m.group(1))
    # custom properties such as --display or --text-font
    for m in re.finditer(r"--[\w-]*(?:font|display|mono|sans|serif|family)[\w-]*\s*:\s*([^;}]+)", t, re.I):
        families += _split(m.group(1))
    # shorthand: font: 400 1rem/1.6 Georgia, serif
    for m in re.finditer(r"(?<![-\w])font\s*:\s*[^;}]*?\d(?:px|rem|em|%|pt)(?:\s*/\s*[\d.]+\w*)?\s+([^;}]+)", t, re.I):
        families += _split(m.group(1))
    for m in re.finditer(r"fontFamily\s*:\s*['\"]([^'\"]+)['\"]", t):
        families += _split(m.group(1))
    for m in re.finditer(r"\b(Inter|Geist|Geist_Mono|Roboto|Lora|Playfair_Display)\s*\(\s*\{", t):  # next/font
        families.append(m.group(1).lower().replace("_", " "))
    for m in re.finditer(r"fonts\.googleapis\.com/css2?\?family=([^\"'&>]+)", t):
        families += [m.group(1).split(":")[0].replace("+", " ").lower()]
    families = [f for f in families if not f.startswith("var(") and not re.match(r"^[\d.]+\w*$", f)]
    named = {f for f in families if f not in KEYWORDS}
    # default_only: every family is a keyword, a system font, Inter or Geist
    default_only = bool(families) and all(f in KEYWORDS | SYSTEM_FONTS | DEFAULT_FONTS for f in families)
    return {"named_fonts": sorted(named), "default_only": default_only}


def analyze(text):
    t = text
    cls = len(re.findall(r"\bclass(?:Name)?\s*=", t))
    big_radius = len(re.findall(r"\brounded-(?:2xl|3xl)\b", t))
    big_radius += len(re.findall(r"border-radius\s*:\s*(?:2[4-9]|[3-9]\d|\d{3,})px", t, re.I))
    pill_h1 = len(re.findall(r"(?:badge|pill|chip|eyebrow|rounded-full)[^>]*>[^<]{0,60}</\w+>\s*(?:</div>\s*)?<h1\b", t, re.I | re.S))
    buzz = {}
    for w in BUZZ:
        n = len(re.findall(r"(?<![-\w])" + re.escape(w) + r"(?![-\w:(])", t, re.I))
        if n:
            buzz[w] = n
    n = len(re.findall(r"(?<![-.\w])Transform(?:s|ing|ation)?\b(?![-:(\s]*[:(;])", t))  # capitalised only: skips CSS transform
    n += len(re.findall(r"\btransform your\b", t, re.I))
    if n:
        buzz["transform"] = n
    font = font_check(t)
    r = {
        "purple_gradients": purple_gradients(t),
        "gradient_text": len(re.findall(r"bg-clip-text|background-clip\s*:\s*text|text-transparent", t, re.I)),
        "fonts": font,
        "glass_blur": len(re.findall(r"backdrop-blur(?:-\w+)?|backdrop-filter\s*:\s*blur", t, re.I)),
        "big_radius": big_radius,
        "big_radius_share_of_classed_elements": round(big_radius / cls, 2) if cls else 0,
        "three_col_grids": len(re.findall(r"(?<![\w-])(?:\w+:)?grid-cols-3\b|repeat\(\s*3\s*,\s*(?:1fr|minmax)|grid-template-columns\s*:\s*1fr\s+1fr\s+1fr", t, re.I)),
        "pill_badge_above_h1": pill_h1,
        "emoji_in_headings": len(re.findall(r"<h[1-6][^>]*>[^<]*" + EMOJI, t, re.I)),
        "scroll_fade_in": len(re.findall(r"data-aos|AOS\.init|whileInView|animate-on-scroll|fade-?in-?up|fade-up|animate-fade-in|\.reveal\b|\breveal-on-scroll", t, re.I)),
        "colored_left_border": len(re.findall(r"\bborder-l-[2-8]\b|border-left\s*:\s*(?:[3-9]|\d{2,})px\s+solid\s+(?!transparent)", t, re.I)),
        "buzzwords": buzz,
        "em_dashes": t.count("\u2014"),
    }
    flags = []
    if r["purple_gradients"]: flags.append("purple or indigo gradient")
    if r["gradient_text"]: flags.append("gradient or transparent text")
    if font["default_only"]: flags.append("default fonts only (system stack, Inter or Geist)")
    if r["glass_blur"]: flags.append("backdrop blur or glass")
    if r["big_radius"] >= 3 and r["big_radius_share_of_classed_elements"] >= 0.3: flags.append("very large radius on many elements")
    if r["three_col_grids"]: flags.append("3-column grid (check whether the cards are equal)")
    if r["pill_badge_above_h1"]: flags.append("pill badge above hero heading")
    if r["emoji_in_headings"]: flags.append("emoji in headings")
    if r["scroll_fade_in"]: flags.append("scroll fade-in")
    if r["colored_left_border"]: flags.append("colored left-border cards")
    if buzz: flags.append("buzzword copy: " + ", ".join(buzz))
    if r["em_dashes"] >= 3: flags.append("3+ em dashes")
    r["flags"] = flags
    return r


def report(r):
    out = [f"{k}: {v}" for k, v in r.items() if k != "flags"]
    out.append("flags: " + ("; ".join(r["flags"]) if r["flags"] else "none"))
    out.append(FLAGS_NOTE)
    return "\n".join(out)


SLOP = """<style>.hero{background:linear-gradient(135deg,#6366f1,#8b5cf6)} body{font-family:'Inter',sans-serif}
.card{border-left:4px solid #3b82f6;backdrop-filter:blur(10px)}</style>
<div class="badge rounded-full">New</div><h1 class="bg-clip-text text-transparent">Unlock seamless work</h1>
<h2>\U0001F680 Fast</h2><div class="grid grid-cols-3 gap-4"><div class="rounded-2xl" data-aos="fade-up"></div>
<div class="rounded-2xl"></div><div class="rounded-3xl"></div></div><p>Supercharge your all-in-one tool \u2014 now \u2014 and \u2014 more</p>"""
CLEAN = """<style>:root{--ink:#1c1b19} body{font-family:'Fraunces',Georgia,serif} h1{font-family:'Work Sans',sans-serif}
.card{border:1px solid var(--ink);transform:translateY(2px)}</style><h1>Bell schedule, printed</h1>
<p>Prints the week's bell times on one page.</p><div class="grid grid-cols-2"></div>"""


def selftest():
    r = analyze(SLOP)
    need = ["purple_gradients", "gradient_text", "glass_blur", "pill_badge_above_h1", "emoji_in_headings",
            "scroll_fade_in", "colored_left_border", "three_col_grids", "em_dashes"]
    for k in need:
        assert r[k], (k, r)
    assert r["fonts"]["default_only"] and r["big_radius"] == 3 and {"unlock", "seamless", "supercharge", "all-in-one"} <= set(r["buzzwords"]), r
    sysonly = analyze("<style>body{font-family:system-ui,-apple-system,'Segoe UI',Roboto,sans-serif}</style>")
    assert sysonly["fonts"]["default_only"] and "segoe ui" in sysonly["fonts"]["named_fonts"], sysonly
    var = analyze("<style>:root{--display:Rockwell,'Roboto Slab',Georgia,serif;--text-font:system-ui,sans-serif}"
                  "body{font:400 1rem/1.6 var(--text-font)}h1{font-family:var(--display)}</style>")
    assert var["fonts"]["named_fonts"] == ["georgia", "roboto slab", "rockwell"] and not var["fonts"]["default_only"], var
    short = analyze("<style>p{font:16px/1.5 Georgia,serif}</style>")
    assert short["fonts"]["named_fonts"] == ["georgia"], short
    c = analyze(CLEAN)
    assert c["flags"] == [] and c["buzzwords"] == {}, c
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
        print(e, file=sys.stderr)
        return 2
    r = analyze(text)
    print(json.dumps(r, indent=2) if as_json else report(r))
    return 1 if r["flags"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
