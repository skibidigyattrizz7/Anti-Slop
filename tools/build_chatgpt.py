#!/usr/bin/env python3
"""Build ChatGPT-ready copies of every skill into dist/chatgpt/.

For each skill:
  dist/chatgpt/<skill>/instructions.md   paste into a Custom GPT or project instructions
  dist/chatgpt/<skill>/knowledge/*.md    upload as knowledge files

Usage: python3 tools/build_chatgpt.py          (run from the repo root)
       python3 tools/build_chatgpt.py --check  (fail if dist/ is out of date)

Custom GPT instructions are limited to 8,000 characters, so the build fails if a
skill goes over. Scripts are not copied: ChatGPT cannot run a skill's scripts.
"""
import re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIMIT = 8000


def build_skill(skill: Path, out: Path):
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not m:
        raise SystemExit(f"{skill.name}: SKILL.md has no frontmatter")
    desc = re.search(r"^description:\s*(.+)$", m.group(1), re.M).group(1).strip()
    body = m.group(2).strip()
    # knowledge files are uploaded flat, so drop the folder from each reference
    body = re.sub(r"`references/([\w.*-]+)`", r"`\1` (knowledge file)", body)
    # table rows and sentences that need a script do not apply in ChatGPT
    body = "\n".join(l for l in body.splitlines() if "scripts/" not in l)
    instructions = f"When to apply this: {desc}\n\n{body}\n"
    if len(instructions) > LIMIT:
        raise SystemExit(f"{skill.name}: instructions are {len(instructions)} chars, limit is {LIMIT}")
    files = {out / "instructions.md": instructions}
    for ref in sorted((skill / "references").glob("*.md")) if (skill / "references").is_dir() else []:
        files[out / "knowledge" / ref.name] = ref.read_text(encoding="utf-8")
    return files


def main(argv):
    check = argv == ["--check"]
    if argv and not check:
        print(__doc__, file=sys.stderr)
        return 2
    dist = ROOT / "dist" / "chatgpt"
    wanted = {}
    for skill in sorted((ROOT / "skills").iterdir()):
        if (skill / "SKILL.md").exists():
            wanted.update(build_skill(skill, dist / skill.name))
    if check:
        have = {p: p.read_text(encoding="utf-8") for p in dist.rglob("*.md")} if dist.exists() else {}
        if have != wanted:
            print("dist/chatgpt is out of date. Run: python3 tools/build_chatgpt.py", file=sys.stderr)
            return 1
        print("dist/chatgpt is up to date")
        return 0
    if dist.exists():
        shutil.rmtree(dist)
    for path, content in wanted.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"built {len(wanted)} files for {len({p.parts[-2] if p.name == 'instructions.md' else p.parts[-3] for p in wanted})} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
