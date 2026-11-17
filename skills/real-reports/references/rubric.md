# Reports rubric

Used by the judge agent and for self-checks. Each check is PASS, FAIL or N/A. A FAIL needs a quoted line as evidence. Check in this order, every time.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| R1 | Sources real and read (must-pass) | Every citation was opened and says what it is cited for. No number or source is invented | Any citation is missing, unopened, does not say the cited thing, or any number or source has no trace |
| R2 | Claims match evidence | Scope, sample and date are stated. Strength fits the source | "Studies show" with no name, one study upgraded to a rule, or a correlation stated as cause |
| R3 | Numbers traceable | Each number has unit, baseline, date and source in its paragraph, and recomputes from the data | A number has no source, or precision exceeds the source, or totals do not sum |
| R4 | Finding first | The conclusion opens the report and each section. Slide titles are claims | The opening is background, or titles are topic labels |
| R5 | Specific, not filler | Adjectives are replaced by figures. No generic trend language | "Growing rapidly", "increasingly important", "highlights the importance of" with no figure |
| R6 | Charts honest | Axes, units and source are shown. Bars start at zero. Text matches the chart | Truncated bars, no unit or source, or text contradicts the chart |
| R7 | Uncertainty and disagreement | Unknowns and conflicts between sources are named once, clearly | Everything sounds equally certain, or conflicts are hidden |
| R8 | Ending and Sources | Ends on a recommendation or decision. A Sources list holds real, working links | A recap ending, no decision, or the list is missing or has dead or invented links |

## Verdict

- **Ship:** R1 passes and at most one other check fails.
- **Fix first:** anything else. R1 failing is always "Fix first".

Report the score (passes out of applicable checks) with the verdict, never alone. Name what you could not verify.

## Guards

- Judge the text, never who or what wrote it.
- The script `check_report.py` cannot open links or verify claims. A clean script run does not pass R1.
- A brief or the user's style can change R4 and R8 form, never R1.
- Formal or non-native English is not a failure.
