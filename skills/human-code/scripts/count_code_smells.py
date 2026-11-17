#!/usr/bin/env python3
"""Count measurable code smells in one source file. Evidence for a reviewer, never a verdict.

Usage:
  python3 count_code_smells.py FILE          human-readable report
  python3 count_code_smells.py --json FILE   JSON report
  python3 count_code_smells.py --selftest

Exit codes: 0 no flags, 1 one or more flags, 2 usage error.
Lists last_verified: 2026-11-17 (see references/tells.md).

Counts: error-swallowing blocks (bare except, empty catch, catch or except that only
logs a fixed message), comment-to-code ratio, comments that restate their line,
TODO and placeholder stubs, generic names, banner comments, secret-looking strings.

What it cannot see: it is regex-based and reads one file. It does not parse code, so
it can miss swallowing hidden in helpers, Go `if err != nil {}`, Lua `pcall`, or Rust
`let _ =`. It mistakes comment markers inside multi-line strings, and braces inside
strings can skew catch-body matching. "Restates" is word overlap, not meaning. It
cannot tell whether code runs, reuses a helper that exists elsewhere, or is correct.
Generated, vendored and fixture files will trip it legitimately.
"""
import json, re, sys, os

HASH_EXT = {".py", ".sh", ".bash", ".rb", ".pl", ".r", ".yml", ".yaml", ".toml", ".ps1"}
DASH_EXT = {".lua", ".luau", ".sql", ".hs"}
GENERIC = {"data", "result", "results", "handler", "temp", "tmp", "utils", "util", "helper",
           "helpers", "obj", "item", "items", "stuff", "thing", "value", "val", "res", "ret", "info"}
FILLER = {"process", "handle", "do", "my", "the", "new", "get", "run", "manager"}
STOP = {"the", "a", "an", "to", "of", "and", "or", "for", "in", "on", "is", "if", "it", "this", "that",
        "we", "with", "from", "be", "are", "as"}
GENERIC_VERBS = {"increment", "decrement", "loop", "iterate", "check", "set", "return", "initialize",
                 "init", "get", "call", "create", "define", "declare", "add", "print", "update"}
KEYWORDS = {"def", "function", "class", "local", "let", "const", "var", "return", "import", "from",
            "self", "this", "end", "then", "else", "elif", "while", "for", "not", "and", "or", "true",
            "false", "none", "null", "nil", "if", "in", "do", "new", "print", "pass"}
SECRET_RES = [
    re.compile(r"""(?i)\b\w*(?:api[_-]?key|secret|token|passwd|password|pwd|private[_-]?key)\w*\s*[:=]\s*["'][^"'\s]{8,}["']"""),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]
PLACEHOLDER_VAL = re.compile(r"(?i)(your[_-]|<.+>|xxxx|changeme|example|placeholder|\$\{|%\()")
STUB_RES = [
    re.compile(r"\b(?:TODO|FIXME|XXX)\b"),
    re.compile(r"^\s*pass\s*(?:#.*)?$"),
    re.compile(r"NotImplemented(?:Error)?|not implemented|unimplemented!?\(", re.I),
    re.compile(r"(?i)\b(?:implement (?:this|me)|rest of (?:the )?code|add your code here|your code here)\b"),
]
LOG_ONLY = re.compile(
    r"""^(?:print|println|printf|console\.\w+|logger?\.\w+|logging\.\w+|log\.\w+|System\.out\.println|fmt\.Print(?:ln|f)?|echo)"""
    r"""\s*\(?\s*(["'`])[^"'`$+%{]*\1\s*\)?\s*;?$""")
BANNER = re.compile(r"^[\W_]*(?:[=\-*#~_/+]{4,})|^\W*[=\-*#~]{2,}\s*\w[\w \-]*\s*[=\-*#~]{2,}\W*$")


def comment_marker(ext):
    if ext in HASH_EXT: return "#"
    if ext in DASH_EXT: return "--"
    return "//"


def split_comment(line, marker):
    """Return (code, comment or None). Skips markers inside simple quoted strings."""
    in_q = None
    i = 0
    while i < len(line):
        c = line[i]
        if in_q:
            if c == "\\": i += 2; continue
            if c == in_q: in_q = None
        elif c in "\"'`":
            in_q = c
        elif line.startswith(marker, i) and (i == 0 or line[i - 1].isspace() or marker == "#"):
            return line[:i], line[i + len(marker):].strip()
        i += 1
    return line, None


def tokens(s):
    s = re.sub(r"([a-z])([A-Z])", r"\1 \2", s)
    return [t for t in re.split(r"[^A-Za-z]+", s.lower()) if len(t) > 2]


def restates(comment, code):
    ct = [t for t in tokens(comment) if t not in STOP]
    kt = set(tokens(code))
    if not ct or len(ct) > 6 or not kt:
        return False
    hit = sum(t in kt for t in ct)
    if hit / len(ct) >= 0.5 and hit >= 1 and len(ct) <= 4:
        return True
    return ct[0] in GENERIC_VERBS and hit >= 1


def find_swallows(lines, text, ext):
    out = []
    if ext in (".py", ".rb"):
        for i, l in enumerate(lines):
            m = re.match(r"^(\s*)(?:except|rescue)\b([^:]*):?\s*(.*)$", l)
            if not m or not (l.lstrip().startswith("except") or l.lstrip().startswith("rescue")):
                continue
            indent, head, rest = len(m.group(1)), m.group(2), m.group(3).strip()
            bare = ext == ".py" and l.strip().rstrip(":").strip() == "except"
            body = [rest] if rest and not rest.startswith("#") else []
            for nl in lines[i + 1:]:
                s = nl.strip()
                if not s or s.startswith("#"): continue
                if len(nl) - len(nl.lstrip()) <= indent: break
                body.append(s)
            only_trivial = all(b in ("pass", "continue", "...") or LOG_ONLY.match(b) for b in body)
            if bare or only_trivial:
                out.append((i + 1, "bare except" if bare else "handler only passes or logs a fixed message"))
        return out
    for m in re.finditer(r"\bcatch\s*(?:\([^)]*\))?\s*\{", text):
        j, depth = m.end(), 1
        while j < len(text) and depth:
            depth += {"{": 1, "}": -1}.get(text[j], 0)
            j += 1
        body = re.sub(r"//[^\n]*|/\*.*?\*/", "", text[m.end():j - 1], flags=re.S).strip()
        stmts = [s.strip() for s in re.split(r"[;\n]", body) if s.strip()]
        line = text.count("\n", 0, m.start()) + 1
        if not stmts:
            out.append((line, "empty catch"))
        elif all(LOG_ONLY.match(s) for s in stmts):
            out.append((line, "catch only logs a fixed message"))
    return out


def analyze(text, ext=".py"):
    lines = text.splitlines()
    marker = comment_marker(ext)
    code_lines = comment_lines = 0
    restating, stubs, banners, generic, secrets = [], [], [], {}, []
    for i, raw in enumerate(lines):
        s = raw.strip()
        if not s:
            continue
        code, com = split_comment(raw, marker)
        in_block = s.startswith(("/*", "*", "*/")) and ext not in HASH_EXT | DASH_EXT
        if in_block or (com is not None and not code.strip()):
            comment_lines += 1
            ctext = com if com is not None else s.lstrip("/* ").rstrip("*/ ")
            if BANNER.match(ctext) or BANNER.match(s):
                banners.append(i + 1)
            nxt = next((l for l in lines[i + 1:] if l.strip() and not split_comment(l, marker)[0].strip() == ""), "")
            if com is not None and nxt and restates(ctext, split_comment(nxt, marker)[0]):
                restating.append(i + 1)
            if any(r.search(s) for r in STUB_RES[:1] + STUB_RES[2:]):
                stubs.append(i + 1)
            continue
        code_lines += 1
        if com:
            if restates(com, code):
                restating.append(i + 1)
            if STUB_RES[0].search(com) or STUB_RES[3].search(com):
                stubs.append(i + 1)
        if STUB_RES[1].match(code) or STUB_RES[2].search(code) or STUB_RES[3].search(code):
            stubs.append(i + 1)
        bare_code = re.sub(r"(\"[^\"]*\"|'[^']*'|`[^`]*`)", '""', code)
        for m in re.finditer(r"(?<![.\w])([A-Za-z_]\w*)", bare_code):
            name = m.group(1)
            if name.lower() in KEYWORDS: continue
            parts = tokens(name) or [name.lower()]
            if any(p in GENERIC for p in parts) and all(p in GENERIC or p in FILLER for p in parts):
                generic.setdefault(name, []).append(i + 1)
        for r in SECRET_RES:
            m = r.search(raw)
            if m and not PLACEHOLDER_VAL.search(m.group(0)):
                secrets.append(i + 1)
                break
    swallows = find_swallows(lines, text, ext)
    total = code_lines + comment_lines
    r = {
        "code_lines": code_lines,
        "comment_lines": comment_lines,
        "comment_ratio": round(comment_lines / total, 2) if total else 0,
        "error_swallowing": [{"line": ln, "kind": k} for ln, k in swallows],
        "restating_comments": sorted(set(restating)),
        "stubs": sorted(set(stubs)),
        "generic_names": {k: len(v) for k, v in generic.items()},
        "banner_comments": banners,
        "secret_looking_strings": secrets,
    }
    flags = []
    if swallows: flags.append(f"{len(swallows)} error-swallowing block(s)")
    if r["comment_ratio"] > 0.35 and total >= 20: flags.append("comment ratio above 0.35")
    if len(r["restating_comments"]) >= 2: flags.append("2+ comments restate their line")
    if r["stubs"]: flags.append("TODO or placeholder stubs")
    if sum(r["generic_names"].values()) >= 3: flags.append("3+ uses of generic names")
    if banners: flags.append("banner comments")
    if secrets: flags.append("secret-looking strings")
    r["flags"] = flags
    return r


def report(r):
    out = [f"{k}: {v}" for k, v in r.items() if k != "flags"]
    out.append("flags: " + ("; ".join(r["flags"]) if r["flags"] else "none"))
    out.append("Counts are evidence, not proof. Read the code, and run it.")
    return "\n".join(out)


def selftest():
    py = '\n'.join([
        "# ==== helpers ====",
        "import json",
        "api_key = 'abcd1234efgh5678'",
        "def process_data(data):",
        "    # increment counter",
        "    counter += 1",
        "    try:",
        "        result = json.loads(data)  # parse the data",
        "    except Exception:",
        "        print('An error occurred')",
        "    try:",
        "        x = 1",
        "    except:",
        "        pass",
        "    # TODO: implement",
        "    return result",
    ])
    r = analyze(py, ".py")
    assert len(r["error_swallowing"]) == 2, r
    assert r["banner_comments"] == [1], r
    assert r["secret_looking_strings"] == [3], r
    assert len(r["restating_comments"]) >= 2, r
    assert r["stubs"], r
    assert r["generic_names"].get("data") and r["generic_names"].get("result"), r
    js = "function f(){\n try { go(); } catch (e) {}\n try { go(); } catch (e) { console.log('failed'); }\n try { go(); } catch (e) { throw new Error('go failed: ' + e.message); }\n}\n"
    j = analyze(js, ".js")
    assert [s["kind"] for s in j["error_swallowing"]] == ["empty catch", "catch only logs a fixed message"], j
    clean = analyze("# Mobile caps emitters at 100/s, so we use bigger particles.\n"
                    "def reward_survivors(players):\n"
                    "    for p in players:\n"
                    "        p.coins += 1\n"
                    "api_key = os.environ['API_KEY']\n", ".py")
    assert clean["flags"] == [], clean
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
        text = open(paths[0], encoding="utf-8", errors="replace").read()
    except OSError as e:
        print(e, file=sys.stderr)
        return 2
    r = analyze(text, os.path.splitext(paths[0])[1].lower())
    print(json.dumps(r, indent=2) if as_json else report(r))
    return 1 if r["flags"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
