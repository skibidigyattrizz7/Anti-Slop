# Build spec: how every category is built

The writing category is the template. Read these first and copy their shape:

- `skills/human-writing/SKILL.md`
- `skills/human-writing/references/rubric.md`, `tells.md`, `craft.md`
- `skills/human-writing/scripts/count_tells.py`
- `agents/writing-specialist.md`, `agents/judge.md`

## Files for one category

```
skills/<skill-name>/SKILL.md
skills/<skill-name>/references/tells.md     dated tells
skills/<skill-name>/references/craft.md     how skilled people do it, by sub-area
skills/<skill-name>/references/rubric.md    pass/fail checks for the judge
skills/<skill-name>/scripts/<name>.py       only if something can be counted
agents/<category>-specialist.md
evals/<skill-name>/prompts.md
```

## SKILL.md

- Body under 500 words. Section order: one paragraph on why output goes generic here, Top rules, Never, Defaults, Read when, Before and after, Final check.
- Top rules: 7 at most. Each says what to do. Keep "don't" for the Never list.
- Never: 2 to 4 items no brief can override. Always include: never invent facts, results or sources.
- Defaults: items a brief or the user's own style overrides.
- Read when: a table that routes to the reference files and the script.
- Before and after: 2 short pairs. They must differ from the eval prompts.
- Final check: 3 questions.
- Description: triggers only. Starts with "Use when". Everyday words a person would type. Under 600 characters. Names the sibling skills it is not for.

## references/

- Each file under about 900 words. No file links to another level of files.
- `tells.md`: starts with `last_verified:` and a re-check schedule. Structure tells before word-level tells. Each tell has a fix. Ends with Guards and Sources. A tell is a reason to rework something, never proof of who made it.
- `craft.md`: sections by sub-area, plus one longer before/after.
- `rubric.md`: 6 to 8 checks with IDs (one letter prefix, e.g. C1 for code). Columns: ID, Check, PASS when, FAIL when. One check is the must-pass (facts are true, the code runs, the page works). Then a Verdict rule and Guards.

## scripts/

- Python standard library only. Supports `--selftest` and `--json FILE`. Exit codes: 0 no flags, 1 flags, 2 usage error.
- Counts are evidence for a reviewer. The script never gives a verdict.
- Run the selftest before you finish.

## Specialist agent

Same sections as `agents/writing-specialist.md`: frontmatter (name, description with plain trigger words, tools), what it needs from the caller, steps, rules, report format. It finds its skill with Glob, fixes work, keeps every fact, stops after two rounds, and never invents missing details.

## evals/<skill-name>/prompts.md

- 3 task prompts with the facts included, to run with and without the skill.
- 8 phrases that should trigger the skill and 8 near-misses that should not.

## Evidence rules

- Keep the owner's existing content where it is good. Tighten it; do not dilute it.
- A number or study goes in only if it is in the owner's skill or sourced in `research_notes/`. Keep its date. Items the research notes mark unverified stay out of `tells.md` or are labelled "unverified".
- Never add tips for beating AI detectors.

## House style for every file

Plain words. Sentence-case headings. No em dashes, no emoji, no "it's not X, it's Y" sentences, no filler intros or summary endings. Short sentences. Examples beat adjectives.
