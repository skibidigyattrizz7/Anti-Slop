# Build log rubric

Used by the judge agent and for self-checks. Each check is PASS, FAIL or N/A. A FAIL needs a quoted line as evidence.

Check in this order, every time.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| B1 | Fidelity (must pass) | Every measurement, reading, part number, date and result traces to what the user gave, with units and meaning unchanged. Gaps are blank placeholders or questions | A number, model, date or test result appears from nowhere, or a supplied one is rounded, converted or improved |
| B2 | Exact parts | Parts carry model numbers, pins, and software or firmware versions where the user supplied them | Parts are named only by type ("an ultrasonic sensor") when a model was supplied |
| B3 | Measurements | Numbers carry units and the conditions they were taken under | A number has no unit, or a claim like "reliable" or "fast" has no figure behind it |
| B4 | Failures | At least one problem is recorded with its cause and the change made, when the user supplied one | The story has no problem, or a failure is smoothed into a success |
| B5 | Entry shape | Entries are dated and follow goal, tried, result, changed, next | Undated, or a narrative with no result and no next step |
| B6 | Wiring and structure | Wiring and parts are in tables or a diagram reference; code values have a reason | Wiring only in prose, or magic numbers with no why |
| B7 | Ending and safety | Ends on a next step or known issue; specific safety notes where hazards exist | A conclusion that repeats the intro, or a LiPo, stall or fuse hazard goes unmentioned |
| B8 | Plain words | No hype words (seamless, robust, innovative, leverages, cutting-edge) | Two or more appear, or the opener announces the project |

## How to read the edge cases

- **B1, placeholders:** `[measure: ...]` passes. A believable number in its place fails, even if labelled "approx".
- **B1, illustrative values:** an example inside a skill file is fine. In a user's log, any unsupplied value fails.
- **B3, no data:** if the user gave no measurements, a log that says what to measure and leaves blanks passes.
- **B4, no failures supplied:** do not invent one. Ask "did anything break or surprise you?" A log that records none and asks passes.
- **B5, notebooks:** if the team's notebook uses its own format, that overrides B5 order.

## Verdict

- **Ship:** B1 passes and at most one other check fails.
- **Fix first:** anything else. B1 failing is always "Fix first".

Score is passes out of applicable checks. Report the score with the verdict, never alone.

## Guards

- Judge the text, never who or what wrote it. Do not say "AI-written" or "proves".
- Young builders' short or informal logs are not a failure. Judge detail, not polish.
- A brief or the team's format overrides B5 and B8 defaults. It never overrides B1.
