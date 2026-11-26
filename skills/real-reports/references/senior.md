# Senior layer for reports

Use for a big job, a senior review, or when the user asks for senior-level work. It adds to the other files and removes nothing. Each rule gives the rule, why, a check, and a tag. `[verified: URL]` means the page was opened. `[practice]` means common professional practice with no opened source, so never quote a number from it as fact.

## Frame the question

- **Write the decision first.** One sentence: who decides what, by when, between which options. Why: otherwise the analysis answers a question nobody asked. Check: each possible result maps to a different action. If two results lead to the same action, drop the analysis. [practice]
- **Split the question with an issue tree.** Branches must not overlap and must together cover the parent. Example: margin fell, so price, volume and mix, unit cost. Check: for each level, name anything in the parent that sits in no branch. Minto's Pyramid Principle is the usual source: 3rd ed., Financial Times Prentice Hall, 2002 [verified: https://search.worldcat.org/title/The-pyramid-principle-:-logic-in-writing-and-thinking/oclc/48025624] (edition only; book not opened). The rule itself: [practice]
- **State a hypothesis and its kill criteria before the analysis.** Write the best-guess answer and the result that would overturn it. Why: it stops you reading any result as support. Check: every analysis step names the hypothesis it tests. [practice]

## Analysis

- **Fix the analysis plan before looking.** Many reasonable choices (cut-offs, subgroups, outlier rules) multiply the chances of a chance finding. Check: the plan is written first, and the report lists every comparison made, not only the ones that worked. [practice]
- **Say who is not in the data.** Self-selection, non-response and survivors skew a sample. Check: one line answers "who could not appear here?" [practice]
- **Give the base rate.** Quote the denominator with every "X% of Y". Example: "doubles the risk" from 1 in 10,000 is 2 in 10,000. Check: each percentage has its base next to it. [practice]
- **Re-cut the headline by the likeliest confounders.** An association can vanish or reverse when a population is split into subgroups (Simpson's paradox). Check: two or three plausible splits were tried, and a flip is reported with the split shown. [verified: https://plato.stanford.edu/entries/paradox-simpson/]

## Say how sure you are

- **Use plain words for uncertainty.** "We are 95% sure the true value is between 4 and 7." Why: the reader acts on it. Check: no bare standard error, p-value or "significant" without the plain sentence. [practice]
- **Chart uncertainty only when it changes the reading.** Show ranges (two values), not a single standard error. Skip it when the gaps are clearly large or the trend is clear. Stacked bars cannot show it. Check: remove the range; if the reader's conclusion is unchanged, leave it out. [verified: https://service-manual.ons.gov.uk/data-visualisation/guidance/showing-uncertainty-in-charts]
- **When it does not know, say so in this form.** Name the question, what was tried, why the data cannot answer it, what would (cost, time), and what you advise meanwhile. Example: "The data cannot separate price from season because it has no prior year. A 4-week holdout would. Until then, act on the cheaper option." Check: all five parts present, and the advice is a decision, not a hedge. [practice]

## Charts

- **Pick the chart from the question.** The FT Visual Vocabulary groups types by question: deviation, correlation, ranking, distribution, change over time, magnitude, part-to-whole, spatial, flow. Why: the question decides what the eye must compare. Check: the question is written down before the type is chosen. [verified: https://github.com/Financial-Times/chart-doctor/blob/main/visual-vocabulary/README.md]
- **Title the takeaway and label directly.** Slide title: the finding as a sentence. Chart title: what is plotted. Put names next to lines and bars so a colour key is not needed. Weak: "Revenue by region". Strong: "North revenue fell while the others held (2025 vs 2024)". Check: read only the titles; the story survives. [verified: https://www.storytellingwithdata.com/blog/2020/3/5/transforming-slide-titles] [verified: https://www.datawrapper.de/blog/text-in-data-visualizations]

## Decks

- **Write a ghost deck first.** All titles as sentences in a text outline, each with a sketched empty chart. Agree the story, then build. Why: a wrong story is cheapest to fix before any chart exists. Check: the outline alone reads as the argument. [practice]
- **Run the slide-sorter test.** View all slides as thumbnails. Each shows one title and one visual, and the sequence shows the arc. Check: any slide you cannot summarise from its thumbnail gets split or cut. [practice]

## Spreadsheet models

These are FAST Standard rules (edition 02c, July 2019, CC BY 4.0), the modelling standard; present them as FAST's, not as law. [verified: https://www.stl-training.co.uk/download/forum/40296_FAST-Standard-02c-July-2019.pdf]

- **Separate inputs, workings, presentation and checks.** FAST 1.01-01. Check: no input sits in a workings sheet.
- **No hardcodes in formulas.** FAST 3.04-01. Every number sits in a labelled input cell. Check: search formulas for typed constants.
- **One formula per row across time.** FAST 3.02-01. Check: no row changes formula mid-way.
- **Keep formulas short.** FAST says a formula should take no more than 24 seconds to explain, and avoids nested IFs. Some modellers dispute this, so treat it as FAST's house rule.
- **Show a master error check.** FAST 2.03-05. Check: it reads zero after every scenario.

Give each input a unit, source and date. Every rule in this section is FAST's.

## Build on

- **pptx** and **xlsx** (Apache-2.0): take their file mechanics. From pptx take structure only (layouts, speaker notes, thumbnails for the sorter test), not its design ideas. Without them: edit with any library that writes notes and reads formulas.
- **deep-research** (when present; link by name only): runs the research loop. Without it: split the question, open each source, cite only what you read.
- **dataviz** (when present; link only, no licence copied): use for colour and accessibility checks. Without it: one accent colour on grey, a table twin for every chart.

## Credits

No text here is copied from another skill. FAST rules are paraphrased with their rule numbers.
