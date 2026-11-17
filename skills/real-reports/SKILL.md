---
name: real-reports
description: Use when writing or checking a report, research summary, literature review, data analysis, slide deck, chart, citations or statistics. Also use when the user says "add sources", "check these numbers", "make a deck", "summarize this research" or "this report sounds vague". Not for general prose (human-writing), chat replies (human-chat) or spreadsheets and code.
---

# Real Reports

A model writes the most plausible next sentence, so a report comes out confident, vague and neat: "studies show", round statistics, a source that looks right and was never opened. Some of those sources do not exist, or do not say what they are cited for. A skilled analyst opens every source, checks every number and says what is still unknown.

## Top rules

1. **Open the source before keeping the claim.** Search, open the page, find the passage. Memory is not a source.
2. **Cite only what you read.** Each citation gets a link, and the page says what you cite it for.
3. **Match the claim to the evidence.** Give the sample, scope and date. "One small study" stays "one small study".
4. **Lead with the finding.** Start the report, section and slide with the conclusion, then the proof. Slide titles are sentences that claim something.
5. **Replace adjectives with numbers.** Give figure, unit, baseline, date. With no figure, write "not measured".
6. **Read the data yourself.** Check axes, units and columns. Recompute each figure from source rows, in code when you can.
7. **End on a decision.** Recommendation, options, cost, owner, date. Then a Sources list.

## Never

- Invent a citation, statistic, quote, study or framework name.
- Cite a page you did not open, or one that does not say it.
- Present an unverified claim as checked. Label it "unverified" or cut it.

## Defaults

- Prefer primary sources (paper, dataset, official page) over summaries of them.
- Mark claims strong, moderate or weak when stakes are high.
- Put source, date and unit under every chart.
- Say once, clearly, what is uncertain or missing.

## Read when

| When | Read |
|---|---|
| Writing a report, memo or research summary | `references/craft-reports.md` |
| Building a deck | `references/craft-slides.md` |
| Making or reading a chart | `references/craft-charts.md` |
| Scanning a draft for tells | `references/tells.md` |
| Checking a finished piece | `references/rubric.md` |
| You can run code | `python3 scripts/check_report.py FILE` |

## Before and after

**Before:** "Remote work has become increasingly important, and experts agree it boosts productivity."

**After:** "A 2024 survey of 800 staff at one logistics firm found self-reported output rose for 60% of remote workers. [link] It is self-reported and from one firm, so it does not show a general effect."

(Invented numbers to show the format. A real report uses verified figures.)

**Before:** Slide title "Q3 overview".

**After:** "Q3 refunds fell 18% after the checkout fix" (invented numbers, form only).

## Final check

- Did you open every source, and does each say what you cite it for?
- Can every number be traced to a row, page or dataset?
- Does it end on what to do next, with the unknowns named?
