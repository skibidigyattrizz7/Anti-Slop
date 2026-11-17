# Anti-Slop plan (draft, not approved yet)

Goal: help people make work a skilled human would be proud of. It is a quality tool, not a way to hide AI use.

## 1. Three layers

| Layer | What it is | Runs when |
|---|---|---|
| Skills | Short craft rules per category. Work alone, in Claude and ChatGPT. | Always, from plain words |
| Category agents | One specialist per category. Checks or fixes work in that category. | "check this", "fix this", big builds |
| Job agents | planner, viewer, judge. | Big builds, or when asked |

Agents cost far more tokens than skills (Anthropic measured about 15x a normal chat for multi-agent work). So skills are the default and agents are opt-in.

## 2. Categories (8)

writing, chat, fiction, code, ui, media (images, video, audio), games, reports (slides, data, research).

Smaller existing skills fold in: `humanizer` becomes writing references, `own-voice` and `build-logs` stay as small add-on skills, `unslop-prompting` stays, `ai-auditor` becomes the judge.

## 3. Job agents (3)

- **planner**: before a big build, picks which skills and specialists to use.
- **viewer**: opens the real page, app or game, takes screenshots at phone and desktop size, clicks through it, and reports what it sees. Uses whatever screen tool exists (browser automation, Claude in Chrome, computer use). Says so when none exists.
- **judge**: fresh context, never the agent that made the work. Scores pass/fail per rule with quoted evidence. Never says "proves".

## 4. Every skill has the same shape

Taken from the owner's existing skills, which already work:

1. One paragraph: why AI output goes generic here.
2. Top rules, 7 at most, written as what to do.
3. Dated tells list (short; long lists go in `references/`).
4. Two or three before/after examples.
5. Final check: 3 questions.

SKILL.md stays under about 500 words. Anything countable gets a script.

## 5. Folder layout

```
skills/<category>/SKILL.md
skills/<category>/references/   tells.md (dated), craft.md, examples.md
skills/<category>/scripts/      only where something can be counted
agents/<name>.md
evals/<category>/               test prompts, run with and without the skill
dist/chatgpt/                   generated, never hand-edited
.claude-plugin/plugin.json
```

## 6. Build order

1. Writing, end to end: skill, specialist, judge, eval. This is the template.
2. Prove it: same prompts with and without the skill. Keep only rules that change the output.
3. Copy the template to the other 7 categories, one at a time, each tested.
4. Viewer and planner.
5. ChatGPT export, README, plugin packaging, Agensi listing.

## 7. Ideas borrowed

- `ai-auditor`: fresh-context check, script counts as evidence, works without subagents too.
- `anti-ui-slop`: agree a contract before building, pass a finish gate after.
- `design-dna`: save a style as a small file so a project stays consistent.
- `fable-playbook`: plan, check, fix loop.
- `skill-creator`, `skill-doctor`: test and score each skill.
- `computer-use`, `browser-use`, `agent-browser`: the viewer uses these instead of reinventing them.
- Deep craft skills (`game-feel`, `motion-design`, `impeccable`): link to them when installed, do not copy them.

## 8. Open decisions

- Which category first (suggested: writing).
- Keep the `human-*` names or rename.
- Public MIT repo with paid extras on Agensi (assumed yes).
