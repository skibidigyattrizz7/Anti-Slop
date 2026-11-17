# human-media eval, 2026-11-17

One run per arm, 1 task. The judge ran in a fresh context and did not know which file used the skill.

Key: t-b.md used the skill. t-a.md did not.

| Task | Without skill | With skill | Judge preferred |
|---|---|---|---|
| Library poster image prompt | 1/7 (Fix first) | 7/7 (Ship) | With skill |

M8 was N/A for both (single piece).

## What it showed

- The baseline named a real person (Ms. Okafor) and gave her a smile and a pose, left the poster text in the generation, named no medium or flaw, and named no finishing step. It failed six of seven checks.
- The with-skill reply drew an unnamed librarian instead of her likeness, kept text out, named a riso print with misregistration, and gave a hand pass.
- The rubric did not score whether the with-skill reply still met the brief. The user wanted the librarian in the poster, and a faceless figure is a workaround the judge could not weigh.
- M1 bundles three things, and M4, M5 and M6 left room for judgement.

## Changes made after this run

- M1: stays the must-pass. Only the parts the brief triggers are scored, and any part that applies and is broken fails it.
- M4: now concrete (outer third or cropped, or two or more different shots) and includes a brief-fit test. A changed depiction passes if the person is still there and the change is stated.
- M6: words to render in the prompt fail. A pose that shows hands needs hands hidden, cropped or checked. Silence about hands passes only if none can show.
- Added a "How to read the edge cases" section, including that "textured paper" is not a named flaw (M5).
- SKILL.md unchanged. Its rules already match.

## Limits

One run per arm and one task is too few to be sure of anything. These scores predate the rubric changes above, so the old and new rubrics are not directly comparable. The judge saw no generated image, only prompts, so visual checks were not run. Rerun with 3 runs per arm before trusting the difference.
