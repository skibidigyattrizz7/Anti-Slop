# human-chat eval, 2026-11-17

One run per arm, 1 task. The judge ran in a fresh context and did not know which file used the skill.

Key: t-b.md used the skill. t-a.md did not.

| Task | Without skill | With skill | Judge preferred |
|---|---|---|---|
| Algebra answer check | 5/7 (Fix first) | 7/7 (Ship) | With skill |

## What it showed

- The skill helped on two checks. The with-skill reply opened with the answer (H2) and gave the reason for adding 7 (H5). The baseline opened with "You're close" and gave a rule with no reason.
- Both replies guessed the user's slip without seeing any steps. Both marked the guess, but each also made a flat claim about unseen work ("The mistake is in one sign", "Your method is right"). The old H1 did not cover that, so the judge passed both.
- `scripts/count_chat_tells.py` flagged nothing on either file, so it could not separate them.

## Changes made after this run

- H1: a flat claim about work the reply has not seen fails unless it is marked as a guess or the reply asks to see the steps.
- H5: now covers diagnosis replies as well as explanations.
- H8: a closing tip passes when it adds something a recap would not.
- Added a "How to read the edge cases" section (H1, H5, H8, H2 and H3 overlap).
- SKILL.md unchanged. Its rule against stating a guess as certain already matches the new H1.

## Limits

One run per arm and one task is too few to be sure of anything. These scores predate the rubric changes above, so the old and new rubrics are not directly comparable. Rerun with 3 runs per arm before trusting the difference.
