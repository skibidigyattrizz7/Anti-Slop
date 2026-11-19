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

## Held-out run with the eval runner (2026-11-19)

`python3 tools/run_evals.py` now does all of this in one command. These tasks are new (`evals/heldout.json`) and were never used to tune a rubric. Writer: Haiku. Judge: Sonnet, blind, random A/B labels. One run per side so far. Raw outputs and judge reports are in `evals/results/`.

| Skill | With skill | Without | Judge preferred |
|---|---|---|---|
| human-writing | 0.88 | 0.50 | With skill |
| human-chat | 0.86 | 0.57 | With skill |
| human-code | 0.67 | 0.50 | With skill |
| human-fiction | 1.00 | 0.62 | With skill |
| human-games | 1.00 | 0.50 | With skill |
| human-media | 0.86 | 0.57 | With skill |
| human-ui | 0.88 | 0.62 | With skill |
| real-reports | 1.00 | 0.57 | With skill |

Scores are rubric checks passed over checks that apply. The skill version was preferred in 8 of 8 categories on tasks the rubrics never saw. The code skill still let a missing file crash with a raw traceback. The code and UI must-pass checks failed in both arms.

### Trigger test

Does a plain request, with no slash command, load the right skill? 16 phrases per skill, Sonnet, plugin installed.

| Skill | Loaded when it should | Stayed quiet when it should |
|---|---|---|
| human-writing | 6 of 8 (was 1 of 8) | 8 of 8 |
| human-fiction | 8 of 8 | 8 of 8 |
| human-ui | 7 of 8 | 8 of 8 |
| human-media | 6 of 8 | 8 of 8 |
| real-reports | 6 of 8 | 8 of 8 |
| human-games | 5 of 8 | 8 of 8 |
| human-code | 4 of 8 | 8 of 8 |
| human-chat | 1 of 8 | 7 of 8 |

The first trigger run found the writing skill loading only when the request mentioned AI. All 8 descriptions now start "Load before starting, even for a short task", which lifted writing from 1 to 6 of 8. Chat stays low because the model answers a question directly without loading anything. Chat rules probably belong in an always-on output style, not a skill.

## Specialist test with the eval runner (2026-11-19)

`python3 tools/run_evals.py --only agents`: each specialist fixes the no-skill output from the held-out run, then a blind judge scores before against after. Specialists ran on Sonnet.

| Specialist | Before fix | After fix | Must-pass after |
|---|---|---|---|
| chat-specialist | 0.71 Fix first | 1.00 Ship | PASS |
| code-specialist | 0.40 Fix first | 1.00 Ship | PASS |
| fiction-specialist | 0.50 Fix first | 1.00 Ship | PASS |
| games-specialist | 0.00 Fix first | 1.00 Ship | PASS |
| media-specialist | 0.43 Fix first | 1.00 Ship | PASS |
| ui-specialist | 0.62 Fix first | 1.00 Ship | PASS |
| writing-specialist | 0.25 Fix first | 0.75 Fix first | PASS |
| reports-specialist | 0.71 Fix first | 1.00 Ship | PASS |

All 8 raised the score, and 7 of 8 reached Ship. The writing specialist kept every fact but stopped 42 percent short of the asked length, leaving `[detail needed]` notes in place of padding. That is the intended behaviour, so it stays "Fix first" until a person supplies the missing details. The UI result comes from a second run, after the judge was told to open each page with the screenshot script: in the first run neither page was opened, so U1 could not pass.

## Chat rules always on (2026-11-19)

The chat skill loaded for only 1 of 8 plain questions, because the model answers questions without loading anything. The plugin now has a startup hook (`hooks/hooks.json`) that adds a 7-rule chat summary to every session. A test run showed the hook context arriving and the reply opening with the answer. The full `human-chat` skill is still there for deeper work.

## Limits

- One run per arm, one task per category (writing had three). That is far too few to call any difference proven.
- Two judges gave the same file scores a point or two apart, so small gaps mean little.
- Writer and judge are both Claude models. No human rated anything.
- `own-voice`, `build-logs`, `unslop-prompting` and `see-it-run` have no eval run. `see-it-run` was used by the UI judge and its script passes its self-test.
