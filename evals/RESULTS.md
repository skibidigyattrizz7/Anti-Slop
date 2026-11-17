# Eval summary, 2026-11-17

Each row is one task, written once with the skill and once without (writer: Haiku), then scored by a judge in a fresh context that did not know which was which (judge: Sonnet). Full reports are in each `evals/<skill>/runs/2026-11-17/` folder.

| Skill | Without skill | With skill | Judge preferred |
|---|---|---|---|
| human-writing (3 tasks, first version) | 5.0/8 mean | 6.3/8 mean | With skill, 2 of 3 |
| human-writing (2 tasks, after fixes) | 4.5/8 mean | 7.0/8 mean | With skill, 2 of 2 |
| human-chat | 5/7 | 7/7 | With skill |
| human-code | 6/7 | 7/7 | With skill |
| human-ui | 4/8 | 8/8 | With skill |
| human-media | 1/7 | 7/7 | With skill |
| human-games | 1/1 | 2/2 | With skill, but most of the rubric did not apply |
| human-fiction | 8/8 | 7/8 | Judge liked the skill scene more as prose, but it dropped a supplied detail and failed the must-pass check |
| real-reports | 6/7 | 6/7 | Without skill, narrowly |
| human-fiction (after fixes) | 4/8 | 8/8 | With skill |
| real-reports (after fixes) | 5/7 | 6/7 | With skill |

## What to take from it

- The skills changed the output in every category, and usually for the better.
- Two did not win cleanly. The fiction skill dropped a detail from the brief. The reports skill computed a number on an assumption it had not checked and left blanks in its recommendation. Both skills and their rubrics were changed after the run and re-tested the same day, and the skill version was then preferred in both. The rubrics changed too, so part of that gain comes from stricter checks.
- Every rubric was reworded where a judge found a check unclear, and each now has an edge-case section.

## Limits

- One run per arm, one task per category (writing had three). That is far too few to call any difference proven.
- Two judges gave the same file scores a point or two apart, so small gaps mean little.
- Writer and judge are both Claude models. No human rated anything.
- `own-voice`, `build-logs`, `unslop-prompting` and `see-it-run` have no eval run. `see-it-run` was used by the UI judge and its script passes its self-test.
