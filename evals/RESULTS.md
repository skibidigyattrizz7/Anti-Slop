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

## Agent tests (2026-11-18)

Two agents that had never run were tested once each, on Sonnet, following their own files.

**Viewer** opened the no-skill bike shop page (`human-ui/runs/2026-11-17/t-b.html`) with the bundled screenshot script and a keyboard walk-through. It found, unprompted, the spacing bug the UI judge had seen: headings tight against the divider lines and hero text flush to the screen edge on phone. It also found two things the judge missed: a phone link under the 24 px tap size, and a 1 px default focus ring on that link. 0 console errors. It did not edit any file.

**Writing specialist** fixed the weakest writing sample (`human-writing/runs/2026-11-17/p3-a.md`) using the judge's report. A fresh judge scored the result (`JUDGE-fixed.md`).

| Before fix | After fix |
|---|---|
| 4/8, Fix first | 6/8, Fix first |

It removed every invented event the judge had listed. It still failed the must-pass fidelity check: it kept a cause the brief never gave ("A part that small was behind the drops"), which it had noticed and listed under "Left alone", and it added "pit kit". It also came out 28 percent short. The test prompt told it not to load skills, and it read that as not reading the skill files, so it worked without the rubric. The agent file now says that an unstated cause or motive counts as new, that fidelity problems are never left alone, that a short result lists the missing details in place of padding, and that it checks W3 and W8 before it reports.

Rerun with the changed agent file and full access to the skill folder (`p3-a-fixed2.md`, judged in `JUDGE-fixed2.md`): 6/8, Fix first. The must-pass fidelity check now passes: every supplied fact kept, no cause or place added. It fails W8 because it came out at 100 words against about 200, and it listed the five details it would need from the user to fill that out, in place of padding. That "Fix first" is the right result: the post cannot reach 200 honest words without facts nobody supplied. It also fails W2 on one 40-word paragraph with nothing checkable in it. No tool call was denied.

## Limits

- One run per arm, one task per category (writing had three). That is far too few to call any difference proven.
- Two judges gave the same file scores a point or two apart, so small gaps mean little.
- Writer and judge are both Claude models. No human rated anything.
- `own-voice`, `build-logs`, `unslop-prompting` and `see-it-run` have no eval run. `see-it-run` was used by the UI judge and its script passes its self-test.
