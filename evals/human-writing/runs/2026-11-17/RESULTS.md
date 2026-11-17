# human-writing eval, 2026-11-17

One run per arm, 3 tasks, writer model Haiku, judge model Sonnet in a fresh context. The judge did not know which file used the skill.

Key: p1-b, p2-a and p3-b used the skill. p1-a, p2-b and p3-a did not.

| Task | Without skill | With skill | Judge preferred |
|---|---|---|---|
| 1 QuizPaste intro | 7/8 | 5/8 | Without skill |
| 2 Sky is blue | 5/8 | 8/8 | With skill |
| 3 Robotics post | 3/8 | 6/8 | With skill |
| Mean | 5.0/8 | 6.3/8 | With skill, 2 of 3 |

## What it showed

- The skill helped most where the baseline padded: warm-up openers, moral endings and invented events (tasks 2 and 3).
- On task 1 the skill made the result worse. The brief had four facts and the model stretched them: "free for students" became "no fee to pay before your first quiz", and it added a "not generic facts from the internet" contrast.
- The baseline also invented details (a motive in task 1, several events in task 3). Fidelity is the check that fails most in both arms.

## Changes made after this run

- Rule 2 now says to state each supplied fact once, as given. Rule 3 says few facts make a short piece. Rule 4 covers the reversed "Y, not X" contrast.
- Rubric: W1, W2, W4, W7 and W8 were reworded where the judge found them unclear, and an edge-case section was added.
- Script: added a "Y, not X tail" count. It is a prompt to look, never a failure on its own.

## Limits

One run per arm is too few to be sure of anything. These numbers predate the changes above. Rerun with 3 runs per arm before trusting the difference.

## Rerun after the changes (same day)

Tasks 1 and 3 were written again with the changed skill (files p1-c and p3-c) and scored by a new blind judge against the same no-skill files. Report: `JUDGE-rerun.md`.

| Task | Without skill | With changed skill | Judge preferred |
|---|---|---|---|
| 1 QuizPaste intro | 5/8 | 8/8 | With skill |
| 3 Robotics post | 4/8 | 6/8 | With skill |

- Task 1, the one the skill lost before, now passes every check. It came out at 81 words against a brief of about 120, so the skill now asks for a length within about 20 percent, and the rubric checks it.
- Task 3 still failed fidelity: "bent" became "loose" and a checklist was invented. The skill now says to keep the supplied word.
- The two judges scored the same no-skill files differently (7/8 then 5/8 on task 1, 3/8 then 4/8 on task 3). A single judge run moves by a point or two, so small gaps mean little.
