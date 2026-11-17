# human-games eval, 2026-11-17

One run per arm, 1 task, judge in a fresh context. The judge did not know which file used the skill.

Task: design a better Roblox grenade explosion under about 60 particles and say how to test it at low graphics quality.

Key: t-a used the skill. t-b did not.

| Task | Without skill | With skill | Judge preferred |
|---|---|---|---|
| Grenade explosion design | 1/1 applicable (7 N/A) | 2/2 applicable (6 N/A) | With skill |

## What it showed

- The skill helped on feedback: layered flash, ring, thump at randomized pitch and shake, plus a rule to keep the crosshair and hitbox readable. The no-skill reply had no sound or readability rule.
- The skill reply was honest about what it did not run and which Roblox caps it did not read.
- The no-skill reply had the stronger test plan: an assert, a 33 ms frame threshold, emit counts scaled by quality level and a cleanup check. The skill reply's count script was muddled and had no thresholds.
- The rubric barely worked for a design: 6 or 7 of 8 checks were N/A, the verdict rule said nothing about G1 being N/A, no check scored how concrete the test plan was, and "not checked" notes earned nothing.

## Changes made after this run

- Rubric: added a "Design or plan" PASS column and a mode choice. G1 now passes a design with a numeric test plan (threshold, count with limit, lowest quality level, cleanup check). G1 cannot be N/A. A plan that passes G1 gets "Ship the plan", never plain "Ship". Honest "not checked" notes earn credit under G1 and G6. Added an edge-case section.
- SKILL.md: rule 1 now says that when you cannot run it, write a test plan with numbers, pass/fail thresholds and a cleanup check. Nothing else changed.

Not changed: craft.md and tells.md. The skill reply's other weaknesses were small and did not trace to a missing rule.

## Limits

One run per arm and one task is too few to be sure of anything. The judge saw the old rubric. The new rubric and rule are untested. Rerun with 3 tasks and 3 runs per arm, including at least one running game, before trusting the difference.
