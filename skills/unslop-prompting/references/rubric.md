# Prompt rubric

Used by the judge agent and for self-checks. Each check is PASS, FAIL or N/A. A FAIL needs a quoted line as evidence.

Check in this order, every time.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| P1 | Fact retention (must pass) | Every fact the user gave (names, numbers, dates, constraints, wording they asked to keep) appears in the prompt with its meaning unchanged, and nothing invented is stated as given | A user fact is dropped, softened, changed, or an invented detail is written as if the user supplied it |
| P2 | Goal and audience | The prompt says what the output is for and who uses it | The task is stated with no purpose or reader |
| P3 | Specifics | 3 to 5 concrete details only this task has | Fewer than 3, or the details are generic ("high quality", "modern") |
| P4 | Direction | One committed style or angle | No direction, or empty adjectives ("professional and engaging") or several clashing styles |
| P5 | Example or contrast | A sample, or a good and a bad example, or a described look | Adjectives only, where an example was available |
| P6 | Avoid with reason | Names the default to avoid and why | No avoid list, or a bare "be original" |
| P7 | Format and length | Exact length and shape stated | Format is absent or vague ("a short piece") |
| P8 | Variety and plain words | Asks for different takes when variety is wanted; no "act as a world-class expert" filler | One-shot request where variety was the point, or filler role lines carry the prompt |

## How to read the edge cases

- **P1, missing info:** `[need: ...]` or a question back to the user passes. A made-up number, name or date fails.
- **P1, merging:** two supplied facts may be combined in one sentence. Dropping either fails.
- **P3, thin brief:** if the user gave under three details, ask for more. A prompt that asks passes P3; padding it fails P1.
- **P5, tools:** image and video prompts may use a described look in place of a pasted sample.
- **P8, N/A:** N/A when the user wants one answer, such as a fact lookup.

## Verdict

- **Ship:** P1 passes and at most one other check fails.
- **Fix first:** anything else. P1 failing is always "Fix first".

Score is passes out of applicable checks. Report the score with the verdict, never alone.

## Guards

- Judge the prompt, not the person. Short prompts from beginners are not failures; ask for what is missing.
- A prompt cannot guarantee diverse output. Do not claim it will.
- A brief or the tool's required format overrides P7 and P8 defaults. It never overrides P1.
