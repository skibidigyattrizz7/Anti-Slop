## t-a.md

```
Verdict: Ship      Score: 6/7 checks pass
Category: reports   Rubric: /home/user/anti-slop/skills/real-reports/references/rubric.md

Checks:
R1 PASS  "Company billing export, October 2026: customer count, billing mix (31% annual), and last year's churn by billing plan (6.8% monthly, 2.1% annual)." Only source is the one supplied in the brief. Derived figures (69%, "about a third") recompute. No invented study or number.
R2 PASS  "Customers who choose annual may already be more committed. Part of the gap may come from who picks annual, not from annual billing itself." Correlation is not stated as cause; scope and date are in Sources.
R3 FAIL  "Last year's churn was 6.8% for monthly-billed customers and 2.1% for annual-billed customers." The paragraph carries no source marker and no date. Source and date appear only in the Sources list.
R4 PASS  "Decision requested: Approve a test of moving customers toward annual billing, with a full switch to follow only if the test supports it."
R5 PASS  "Annual customers left at about a third of the rate of monthly customers (2.1% vs 6.8%)." Figures, no trend filler (script: 0 filler, 0 vague).
R6 N/A   No chart.
R7 PASS  "The monthly figure is a monthly rate. The annual figure may be a yearly rate. We need to confirm both are measured the same way." Unknowns and the cost gap are named ("This brief does not model that cost").
R8 PASS  "Board ask: Approve the test and a discount budget." followed by a Sources list. The export has no link because none was supplied.

Top fixes (most important first, 5 at most):
1. "Why it matters" / "The monthly figure is a monthly rate." -> treats the monthly reading of 6.8% as settled while doubting the 2.1%, but the brief gave neither period -> say both periods are unconfirmed.
2. "Where we are" bullets -> no source or date in the paragraph -> add "(billing export, Oct 2026)" to the section.
3. "a modest discount" -> no figure, so the board cannot size the ask -> state the range to be tested or say it is not yet set.

Could not check: whether the billing export exists or matches the figures (not supplied to me).
```

## t-b.md

```
Verdict: Ship      Score: 6/7 checks pass
Category: reports   Rubric: /home/user/anti-slop/skills/real-reports/references/rubric.md

Checks:
R1 PASS  "Owner-supplied billing export, October 2026: 4,200 customers, 31% on annual billing, churn last year 6.8% monthly (monthly billing) and 2.1% (annual billing). Status: unverified." Source is the one supplied in the brief, and it is labelled unverified. No invented study. The 1,302 / 2,898 counts recompute.
R2 PASS  "Strength: moderate. It is one company's billing export, and I have not opened that export." Selection effect is named ("customers who pick annual may already be more loyal").
R3 FAIL  "Monthly billing at 6.8% a month compounds to about 57% of monthly customers lost in a year (1 - 0.932^12) [1]." The brief gave "6.8% monthly" with no period. This brief's own "Still unknown" item 1 says the periods are unconfirmed. The 57% rests on an assumption stated as fact, and "[1]" makes it look sourced. The 22% figure has the same problem.
R4 PASS  "Recommendation: Do not switch the whole base yet. Run a 12-month pilot..." opens the report; "Finding" follows.
R5 PASS  "2.1% against 6.8% a month for monthly billing". Figures, no filler (script: 0 filler, 0 vague).
R6 N/A   No chart. The options table is not a chart.
R7 PASS  "Still unknown" list; "Not measured." tags on each caveat; the unit conflict is named.
R8 PASS  Decision is at the top ("Approve the pilot..."); the ending is "Still unknown" plus Sources. The Sources link is "[link needed]". Passes on the rubric's form allowance for briefs.

Top fixes (most important first, 5 at most):
1. "Monthly billing at 6.8% a month compounds to about 57%" -> treats an unconfirmed period as known and builds a derived number on it -> give the 57% and 22% only as "if 6.8% is a per-month rate", or drop them.
2. "Approve the pilot and a discount budget of [figure needed], by [date needed]. Owner: [name needed]." -> unfilled placeholders sit in the decision line of a board brief -> remove them or move to an "open items" note for the sender.
3. "I have not opened that export" -> first-person process note inside a board document -> keep "unverified" in Sources and drop the sentence.
4. "[link needed]" -> placeholder in Sources -> replace with the export's internal location or remove.

Could not check: whether the billing export exists or matches the figures (not supplied to me).
```

A is better. B's 57% and 22% figures treat an unconfirmed period as known, and its decision line carries unfilled placeholders. A has one small slip of the same kind.

## Rubric notes

- R1 says "every citation was opened". The only source was supplied in the brief and neither file could open it, and I could not either. I read it as "traces to the brief, nothing invented". The rubric should say what to do when the brief itself is the only source.
- R1 did not separate the two files. B flags the export as unverified and A does not. A says nothing about verification and B says too much. Both pass.
- R3 asks for source and date in each paragraph. Read literally it fails nearly any short brief with a sources list. It was too strict on A. It was useful on B, where an assumption was presented as a traced number.
- The R3 rule "recomputes from the data" cannot check a number derived on an unstated assumption. The rubric should say to fail a derived number whose assumption the brief did not supply.
- R6 was N/A for both, so it did not help.
- R8 asks for working links. The brief supplied none, so neither file could meet it. It passes on the brief-form allowance. The rubric should say how to treat a source with no link.
- R4 passed both. Both use topic-label headings ("Where we are", "What the numbers mean"). The rubric does not say whether that counts below the opening.
- The rubric has no check for placeholders left in the final text. B's "[figure needed]" and "[date needed]" were caught only through fixes, not scored.
- The rubric also gives no way to score an unfounded assumption that the other file makes only once. Both files read 6.8% as a monthly rate, and B alone compounds it.
- The script flagged both files the same way (3 uncited paragraphs, no links), so it did not separate them.
