# Own voice rubric

Used by the judge agent and for self-checks. Each check is PASS, FAIL or N/A. A FAIL needs a quoted line as evidence.

Check in this order, every time.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| V1 | Fidelity (must pass) | Every experience, number, name, award, grade and feeling traces to what the user gave, with its meaning unchanged | A personal detail appears from nowhere, or a supplied one is inflated, softened or dropped |
| V2 | Scene | Each claim about the person is backed by a specific moment, number or name they supplied | A trait is asserted ("I am resilient") with no scene behind it |
| V3 | Voice match | Sentence length, word choice and quirks match the sample or the way the user wrote in the chat | Vocabulary or polish the user never shows, or a smooth tone that matches nothing in the sample |
| V4 | Stock lines | No lesson-of-life lines or grand claims ("shaped who I am today", "changed my life", "passion for") | One or more appear |
| V5 | Rhythm | Short and long sentences mix, and at least one line is plainly spoken | Every sentence runs the same length and shape |
| V6 | Ending | Ends on a detail, decision or next step | Ends on a moral, a summary or a restated thesis |
| V7 | Authorship | For high-stakes or graded work, the response coaches or edits the user's own draft, or the user wrote the core | The response ghostwrites a full application or graded piece where the user has not drafted, or helps hide AI use against a stated rule |
| V8 | Format | The form fits the genre: short email, verb-plus-result resume line, spoken speech | Resume filler ("responsible for"), a cover letter that repeats the resume, an email that opens with pleasantries |

## How to read the edge cases

- **V1, gaps:** `[detail needed: ...]` or a question to the user passes. A plausible filler detail fails, even a small one.
- **V1, tone words:** a feeling the user hinted at passes if stated as they said it. Turning "annoyed" into "devastated" fails.
- **V3, no sample:** with no sample, judge only that the text is plain and uses the user's own supplied words.
- **V4, quotes:** a stock line the user wrote themselves, kept in an edit, is theirs. Flag it to them; do not count it against the edit.
- **V7, N/A:** N/A for a casual message the user asked you to write for them.

## Verdict

- **Ship:** V1 passes and at most one other check fails.
- **Fix first:** anything else. V1 failing is always "Fix first".

Score is passes out of applicable checks. Report the score with the verdict, never alone.

## Guards

- Judge the text, never who or what wrote it. Do not say "AI-written" or "proves".
- Formal, simple or non-native English is a voice, not a failure.
- A brief or the user's sample overrides V5 and V8 defaults. It never overrides V1 or V7.
