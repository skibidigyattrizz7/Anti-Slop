# Road to 10/10

Status on 2026-11-18: 7/10. The library is built and every category was tested once. What holds it back is proof, not content.

## The real problems, worst first

1. **The proof is thin.** One run per side, one task per category. Two judges scored the same file a point or two apart, so most gaps are inside the noise. Writer and judge are both Claude models, and no human rated anything.
2. **Rubrics were tuned on the samples they then scored.** Fiction and reports "won" their re-tests partly because their rubrics changed. That is overfitting. A judge or a hackathon reviewer will spot it.
3. **Most agents have never run.** The planner and 7 of 8 specialists have zero runs. The specialist that did run needed a fix before it kept facts straight.
4. **"Triggers from plain words" is untested.** Every skill has 16 trigger phrases in `evals/*/prompts.md`, and none has ever been run.
5. **Install is untested.** Nobody has installed the plugin from the marketplace, or pasted a `dist/chatgpt` skill into ChatGPT.
6. **Thin research.** The games and audio notes rely on memory in places. Some tells are marked unverified.
7. **No demo.** A reviewer needs to see before and after in 30 seconds. Today that means reading markdown.

## The fix, in order (each step is small)

### 1. One eval runner (fixes 1, 2 and 4). Done 2026-11-19: 3 runs per side for all 11 skills, triggers 80 of 88. Human check still to do

Write `tools/run_evals.py`. It uses `claude -p` (headless Claude Code) to:
- run each task 3 times with the skill and 3 times without, on held-out tasks (new prompts, not the ones the rubrics were tuned on)
- give the outputs random labels so the judge is blind, then score with `agents/judge.md`
- run each trigger phrase and record whether the right skill loaded
- write `evals/results.json` and a table with mean and spread per category

One command reruns everything, so every future change can be checked. Cost: about 8 categories × 6 writes × 2 judges. Run it on Haiku writers and a Sonnet judge, one category at a time.

Then add a human check: you score 5 pairs blind. If your picks agree with the judge's, say so in the README. That is the strongest single proof you can add.

### 2. Test every agent once (fixes 3). Done 2026-11-19: all 8 specialists, the viewer and the planner

Each category already has a failing no-skill sample in `evals/*/runs/`. For each specialist: fix that sample, then a fresh judge scores the fix. Pass bar: the score rises and the must-pass check holds. The planner gets one mixed request ("landing page with copy and a hero image").

### 3. One-command polish loop (the demo feature)

Add a `polish` skill that chains what already exists: judge → specialist → viewer for pages → judge again, two rounds at most. It returns before, after and both scores. This is the thing to show at a hackathon: paste something generic, get it back better with a score that proves it.

### 4. A before/after page (fixes 7)

One page with a row per category: no-skill output, skill output, judge scores, and the UI screenshots that already exist. Build it from `evals/results.json` so it updates itself.

### 5. Install and export check (fixes 5)

- Install from the marketplace on a clean machine and run one trigger phrase.
- Paste `dist/chatgpt/human-writing` into a Custom GPT and run eval task 1.
- Add an icon (`.claude-plugin/icon.png`, 512 px or more), the validator's only warning.

### 6. Research second pass (fixes 6). Done 2026-11-19

Rerun the games and audio research only, with search quota fresh. Move anything still unverified out of `tells.md`.

## What to cut

Nothing new until steps 1 and 2 pass. Non-anti-slop skills wait.

## Cost plan

- Steps 1 and 2 are the big ones. Run them in a fresh chat after the usage reset, one category per run.
- Steps 3 to 5 are mostly small files, and cheap.
- Use Sonnet for building and judging and Haiku for writer runs. No Opus.

## Hackathon pitch, one line

"Skills that make AI output as good as a careful person's, with a blind judge that proves it, and one command that fixes your work in front of you."
