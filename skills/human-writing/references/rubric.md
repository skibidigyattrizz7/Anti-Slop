# Writing rubric

Used by the judge agent and for self-checks. Each check is PASS, FAIL or N/A. A FAIL needs a quoted line as evidence. A PASS on W2 needs the specifics quoted.

Check in this order, every time.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| W1 | Point | The point fits in one sentence and the first two sentences deliver content | The opening restates the task, sets a scene of generalities or announces what is coming |
| W2 | Specifics | Every paragraph of 40+ words holds a checkable name, number, date, place or example | A paragraph of 40+ words has none |
| W3 | Fidelity | Every fact traces to the brief, the user or a cited source | A fact, quote, statistic or personal detail appears from nowhere, or a brief fact is changed or dropped |
| W4 | Direct claims | Claims are stated plainly | Any "not X, it's Y" staging, vague attribution ("studies show") or inflated significance |
| W5 | Rhythm | Sentence lengths vary and lists use the real count | Script reports variation under 0.35 on 150+ words, or more than one habitual triad per 300 words |
| W6 | Words | Fewer than 3 cluster words and no stock phrases (lists in `tells.md`) | 3 or more cluster words, or any stock phrase |
| W7 | Ending | The last paragraph adds a detail, consequence, decision or open question | The ending summarises, moralises or offers more help |
| W8 | Format | Formatting fits where the text will be read | Decorative bold, headings on a short piece, bullets for prose, markdown where it won't render |

## Verdict

- **Ship:** W3 passes and at most one other check fails.
- **Fix first:** anything else. W3 failing is always "Fix first".

Score is passes out of applicable checks. Report the score with the verdict, never alone.

## Guards

- Judge the text, never who or what wrote it. Do not say "AI-written" or "proves".
- Formal, simple or non-native English is not a failure.
- A brief or the user's writing sample overrides W5, W6 and W8 defaults. It never overrides W3.
