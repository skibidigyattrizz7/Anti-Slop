# real-reports eval, 2026-11-17

One run per arm, 1 task (one-page board brief on moving from monthly to annual billing; supplied facts: 4,200 customers, 31% on annual, churn last year 6.8% monthly vs 2.1% annual, billing export Oct 2026). The judge did not know which file used the skill.

Key: t-b used the skill. t-a did not.

| Task | Without skill | With skill | Judge preferred |
|---|---|---|---|
| 1 Billing brief | 6/7 | 6/7 | Without skill |

## What it showed

- The skill did not win. Scores tied and the judge narrowly preferred the brief written without it.
- The skill brief compounded 6.8% into "about 57% lost per year" although its own unknowns list said the period was unconfirmed. The "[1]" next to it made the figure look sourced.
- It left "[figure needed]", "[date needed]" and "[name needed]" inside the decision line, and "[link needed]" in Sources.
- The brief without the skill made a smaller slip of the same kind: it read 6.8% as monthly and doubted only the 2.1%.
- The skill did help on openness: it labelled the export "unverified" and named the selection effect.
- The rubric was part of the problem. R1 required citations to be "opened" when the only source was the user's own export. R3 (source and date in every paragraph) was too strict for a one-page brief. Nothing scored derived numbers or placeholders.

## Changes made after this run

- SKILL.md: user-supplied data is cited as the user's, with its date, never as verified. A derived number shows its arithmetic and rests only on stated facts; if the period or unit is unknown, ask. Missing inputs go as questions at the top, never as placeholders. A recommendation is never left blank: give what the known facts support and what would change it.
- Rubric: R1 handles user data. R3 needs source and date per section, not per paragraph, and fails a derived number built on an unsupplied assumption. R7 fails treating a listed unknown as settled. R8 fails placeholders in the decision. Still 8 checks. Added an edge-case section.
- Script: counts leftover placeholders ("[figure needed]", "TBD") and flags them, with a selftest case.

## Limits

One run per arm on one task is too few to be sure of anything. These scores predate the changes above, and the rubric changed after judging. Rerun with 3 tasks and 3 runs per arm before trusting the difference.
