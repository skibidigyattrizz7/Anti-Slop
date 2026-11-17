# Writing rubric

Used by the judge agent and for self-checks. Each check is PASS, FAIL or N/A. A FAIL needs a quoted line as evidence. A PASS on W2 needs the specifics quoted.

Check in this order, every time.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| W1 | Point | The point fits in one sentence and the first two sentences deliver content | The opening restates the task, asks a warm-up question, announces what is coming or sets a scene before the first fact |
| W2 | Specifics | Every paragraph of 40+ words holds a checkable name, number, date, place or example, and the whole piece has at least one per 100 words | A paragraph of 40+ words has none, or the piece falls under one per 100 words |
| W3 | Fidelity (must pass) | Every event, motive, number, quote and source traces to the brief, the user or a cited source, with its meaning unchanged | One appears from nowhere, or a supplied fact is changed, stretched or dropped |
| W4 | Direct claims | Claims are stated plainly | A "not X" half that nobody claimed, vague attribution ("studies show"), or an ordinary thing called the worst, pivotal or a turning point |
| W5 | Rhythm | Sentence lengths vary and lists use the real count | Script reports variation under 0.35 on 150+ words, or more than one habitual triad per 300 words |
| W6 | Words | Fewer than 3 cluster words and no stock phrases (lists in `tells.md`) | 3 or more cluster words, or any stock phrase |
| W7 | Ending | The last paragraph adds a detail, consequence, decision, open question or a concrete next step | The ending repeats the opening, summarises, or lists general lessons |
| W8 | Format | Formatting fits where the text will be read | Decorative bold, section headings on a piece under 300 words, bullets for prose, markdown where it won't render |

## How to read the edge cases

- **W3, views:** a lesson or opinion drawn from the supplied facts passes when it is stated as a view ("we should check hardware first"). It fails when it is stated as something that happened ("we ran the course again").
- **W4, real contrasts:** a contrast passes when it corrects something the reader believes or compares two real options ("a week before, in place of the night before"). The script's "Y, not X tail" count is a prompt to look. It is never a FAIL on its own.
- **W5, near the line:** a variation score between 0.35 and 0.40 with same-shape sentences is a FAIL. Quote three sentences in a row.
- **W8, titles:** one title is fine on any length.

## Verdict

- **Ship:** W3 passes and at most one other check fails.
- **Fix first:** anything else. W3 failing is always "Fix first".

Score is passes out of applicable checks. Report the score with the verdict, never alone.

## Guards

- Judge the text, never who or what wrote it. Do not say "AI-written" or "proves".
- Formal, simple or non-native English is not a failure.
- A brief or the user's writing sample overrides W5, W6 and W8 defaults. It never overrides W3.
