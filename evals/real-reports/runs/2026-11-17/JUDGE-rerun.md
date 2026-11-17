# Judge report: t-a.md and t-c.md

Context used: board brief on monthly vs annual billing. Source facts: 4,200 customers, 31% annual, churn 6.8% monthly vs 2.1% annual, billing export Oct 2026. Script check_report.py was run on both (counts are evidence only, no links to open in either file).

## t-a.md

```
Verdict: Fix first      Score: 5/7 checks pass
Category: reports   Rubric: /home/user/anti-slop/skills/real-reports/references/rubric.md

Checks:
R1 PASS  "Company billing export, October 2026: customer count, billing mix (31% annual), and last year's churn by billing plan" (cited as the company's own data, dated, not called verified; no invented number or source)
R2 PASS  "Part of the gap may come from who picks annual, not from annual billing itself." (correlation not stated as cause)
R3 FAIL  "Annual customers left at about a third of the rate of monthly customers (2.1% vs 6.8%)." and "The monthly figure is a monthly rate. The annual figure may be a yearly rate." (a derived ratio rests on an unconfirmed period; the brief never says the monthly figure is a monthly rate)
R4 PASS  "Decision requested: Approve a test of moving customers toward annual billing, with a full switch to follow only if the test supports it."
R5 PASS  figures used throughout; no trend filler (script: 0 vague, 0 trend)
R6 N/A   no charts
R7 FAIL  "Annual customers left at about a third of the rate of monthly customers" (stated as settled, then the next lines list the period as unconfirmed: "We need to confirm both are measured the same way.")
R8 PASS  "Board ask: Approve the test and a discount budget." and Sources line "Company billing export, October 2026" (no link exists for user data; no placeholders)

Top fixes (most important first, 5 at most):
1. "Why it matters" paragraph "Annual customers left at about a third of the rate of monthly customers (2.1% vs 6.8%)." -> compares two rates whose period the brief does not state -> say "the export shows 2.1% for annual and 6.8% for monthly; the period is not stated" and drop "about a third".
2. "Why it matters" caution "The monthly figure is a monthly rate. The annual figure may be a yearly rate." -> invents a unit for the monthly figure and contradicts "last year's churn" -> say neither unit is confirmed, and list it as an open question.
3. "Why it matters" "Every customer we keep is revenue we do not have to replace, and annual contracts make revenue more predictable." -> generic claim with no figure and no source -> cut it or tie it to a figure the brief supplies.
4. Recommendation step 1 "a modest discount" -> vague; the brief gives no price -> state that price and discount are unknown and that the test sets them.

Could not check: nothing beyond what is on the page; there are no links to open. Real truth of the export figures cannot be checked.
```

## t-c.md

```
Verdict: Ship      Score: 6/7 checks pass
Category: reports   Rubric: /home/user/anti-slop/skills/real-reports/references/rubric.md

Checks:
R1 PASS  "[source: your billing export, Oct 2026]" and "Your data, not independently verified; no link." (user's data, dated, not called verified; no invented number or source)
R2 PASS  "Our data shows a large churn gap, but it does not yet show that annual billing causes lower churn."
R3 FAIL  "Arithmetic: 0.31 × 4,200 = 1,302 annual; 4,200 − 1,302 = 2,898 monthly." (arithmetic is shown, but 1,302 and 2,898 are four digits from a two-digit percentage, so precision exceeds the source; rounded 31% could be about 1,280 to 1,320)
R4 PASS  "Recommendation: Test annual billing before switching everyone." opens the report
R5 PASS  figures and named unknowns instead of adjectives; script 0 vague, 0 trend
R6 N/A   no charts
R7 PASS  "I have not converted either figure, because the period is not stated." and "What would change the recommendation" section (period named once as unknown and not used as settled)
R8 PASS  "Approve a two-quarter test of annual billing, with the test design, discount level and success measure to come back to the board." and Sources line naming the export and date (no placeholders)

Top fixes (most important first, 5 at most):
1. "The evidence" first bullet "0.31 × 4,200 = 1,302 annual; 4,200 − 1,302 = 2,898 monthly." -> false precision from a rounded percentage -> write "about 1,300 annual and about 2,900 monthly" or drop the counts.
2. Opening "Our data shows a large churn gap" -> calls the gap large while the period is unknown -> say "the export shows a gap (6.8% vs 2.1%); the period is not confirmed".
3. "Open questions" and evidence bullets use "your billing export" -> a board brief should not address the reader as "your" -> name it "the company billing export".
4. "Proposed owner: finance lead (proposed, not yet agreed)" -> a name for the owner not supplied in the brief; it is flagged as proposed, but a board may read it as decided -> keep it labelled as a proposal or move it to Open questions.

Could not check: nothing beyond what is on the page; there are no links to open. Real truth of the export figures cannot be checked.
```

## Which is better

t-c.md is better: it leaves the period of the churn figures unknown and does not compute on it, while t-a.md invents a unit ("The monthly figure is a monthly rate") and states "about a third" as settled.

## Rubric notes

- R3 "precision exceeds the source" is unclear for counts derived from a rounded percentage. A strict reading fails t-c (1,302); a lenient reading passes it. The rubric should say whether a derived count from a rounded percentage must be shown as approximate.
- R3 and R7 overlap on the unit problem. t-a failed both for one defect (the ratio treated as settled). The rubric should say whether the same defect is counted twice.
- R7 "uses as settled something it lists as unknown" depends on order: t-a states the ratio first, then adds the caution. The rubric does not say whether a caution immediately after is enough.
- R1 "not called verified" passed both files; it cannot separate them. t-c adds "not independently verified", t-a says nothing either way, and the rubric treats both as PASS.
- R8 "no placeholders" does not say whether a deferral ("discount level ... to come back to the board", "Set the discount level in the test") is a placeholder. I treated both as PASS because each recommendation is still complete.
- R2 "scope, sample and date are stated" is hard to apply when the brief gives "last year" and no range. Neither file defines it as a fact; t-c asks, t-a ignores it, and both PASS.
- R5 passed both; it did not separate them. The generic sentence in t-a ("Every customer we keep is revenue we do not have to replace") is not in the R5 fail list.
- Script flag "paragraphs_with_numbers_but_no_citation" fired for t-a (3) and not t-c (0) because t-c repeats a source tag in every bullet. The rubric says one source line per section is enough, so this count should not be read as a fail.
- Verdict rule gives Ship for t-c on one fail, though that fail is the weaker one. A single-check threshold makes the gap between the two files (Fix first vs Ship) depend on whether R3 is read strictly.
