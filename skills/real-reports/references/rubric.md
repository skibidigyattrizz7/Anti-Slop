# Reports rubric

Used by the judge agent and for self-checks. Each check is PASS, FAIL or N/A. A FAIL needs a quoted line as evidence. Check in this order, every time.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| R1 | Sources real and read (must-pass) | Every public source was opened and says what it is cited for. User-supplied data is cited as the user's, with its date, and not called verified. No number or source is invented | A public citation is unopened or does not say the cited thing, or any number or source has no trace to the brief or a source |
| R2 | Claims match evidence | Scope, sample and date are stated. Strength fits the source | "Studies show" with no name, one study upgraded to a rule, or a correlation stated as cause |
| R3 | Numbers traceable | Each number has a unit and baseline, and its source and date appear in its section or a source line. Every derived number shows its arithmetic and rests only on stated facts | A number has no source, precision exceeds the source, totals do not sum, or a derived number rests on an assumption the brief did not supply (an unconfirmed period or unit) |
| R4 | Finding first | The conclusion opens the report and each section. Slide titles are claims | The opening is background, or titles are topic labels |
| R5 | Specific, not filler | Adjectives are replaced by figures. No generic trend language | "Growing rapidly", "increasingly important", "highlights the importance of" with no figure |
| R6 | Charts honest | Axes, units and source are shown. Bars start at zero. Text matches the chart | Truncated bars, no unit or source, or text contradicts the chart |
| R7 | Uncertainty and disagreement | Unknowns and conflicts between sources are named once, clearly, and the text treats them as unknown | Everything sounds equally certain, conflicts are hidden, or the text uses as settled something it lists as unknown |
| R8 | Decision and Sources | Ends on or opens with a complete recommendation, with no placeholders ("[figure needed]") left in the text. A Sources list names each source, with a link where one exists | A recap ending, no decision, a blank or placeholder in the decision, a missing list, or dead or invented links |

## How to read the edge cases

- **Counts from a rounded percentage:** a count worked out from a rounded figure is written as rounded too ("about 1,300 of 4,200", from 31%). An exact-looking count such as "1,302" fails the false-precision check.
- **One finding, one check:** when a derived number rests on an unstated assumption, fail the derived-number check only. Do not fail the precision check for the same line.

- **R1, user data:** when the brief's own data is the only source, PASS if it is cited as the user's with a date and not called verified. Do not require it to be opened. Calling it "verified" is a FAIL.
- **R3, short briefs:** one source and date line per section, or one under the numbers, is enough. Each paragraph need not repeat it.
- **R3, derived numbers:** compounding, annualising or totalling needs the period or unit stated in the brief. If the brief leaves it open, a computed figure is a FAIL, even when the unknown is listed elsewhere. "If 6.8% is monthly, then..." with the arithmetic shown passes.
- **R8, no link:** a source the user supplied has no link. Name it and its date. A placeholder in its place ("[link needed]") is a FAIL.
- **R4, headings:** topic-label headings below the opening do not fail R4 if the opening states the finding.

## Verdict

- **Ship:** R1 passes and at most one other check fails.
- **Fix first:** anything else. R1 failing is always "Fix first".

Report the score (passes out of applicable checks) with the verdict, never alone. Name what you could not verify.

## Senior checks

Apply only when the brief is a full project or the user asks for a senior review. They never change the verdict rule above for ordinary work. Report them beside the score, not inside it.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| S1 | Decision and structure | The decision is stated first, and the sections follow an issue tree with no overlap and no gap | The report starts from the data, or sections overlap or leave out part of the question |
| S2 | Plan and base rates | A hypothesis and what would overturn it are stated. Every comparison made is listed. Each percentage has its base and who is missing from the sample | Only the comparisons that worked are shown, or a percentage has no base |
| S3 | Splits and uncertainty | A likely confounder was checked and a flip is shown. Uncertainty is in plain words and charted only when it changes the reading | One headline cut is treated as settled, or a bare p-value or standard error stands alone |
| S4 | Chart and deck craft | Chart type follows the question, titles state the takeaway, labels are direct. Titles alone tell the story | Topic-label titles, a colour key where direct labels fit, or a slide that fails the sorter test |
| S5 | Models and "we don't know" | Model inputs are separate and labelled, with no typed constants in formulas and a visible check. Open questions use the five-part form | Hardcodes in formulas, no check row, or an unknown hedged instead of answered with a next step |

## Guards

- Judge the text, never who or what wrote it.
- The script `check_report.py` cannot open links or verify claims. A clean script run does not pass R1. Its placeholder count is evidence for R8.
- A brief or the user's style can change R4 and R8 form, never R1.
- Formal or non-native English is not a failure.
