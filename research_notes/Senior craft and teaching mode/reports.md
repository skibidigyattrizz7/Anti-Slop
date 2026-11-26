# Senior craft for reports, analysis, charts, decks, models

Date 2026-11-26. Source tags: **[opened]** = fetched this session and the passage read. **[search]** = only a search-result summary seen, page not opened. **[memory]** = established practice stated from memory, not opened (unverified, do not quote).

Saved by the coordinator: the researcher's Write call was refused, so its returned text is stored here as given.

## 1. Problem framing

- **Define the decision before the data.** Write one sentence: who decides what, by when, between which options. Why: otherwise the analysis answers a question nobody asked. Check: name the action each possible result would trigger. If two results lead to the same action, the analysis is not needed. [memory]. The local `real-reports/craft-reports.md` already says "write the decision or question".
- **Issue tree, MECE.** Split the question into branches that do not overlap and together cover it. Example: "Why did margin fall?" splits into price, volume/mix and unit cost; then cost into materials, labour and freight. Check: for each level, ask "what is in the parent but in none of these?" Minto's grouping rule per secondary summaries: siblings are the same kind of idea, logically ordered, and sum to the parent [search](https://thinkinsights.net/strategy/pyramid-principle). Minto's book not opened.
- **Hypothesis first.** State a best-guess answer on day one and design the cheapest test that could kill it. Check: every analysis step names the hypothesis it supports or refutes. [memory]
- **Kill criteria in advance.** Write what result would change the recommendation before you see it. [memory]
- **Scope exclusions.** One line stating what you will not do and the known data limits. [memory]

## 2. Analysis rigour

- **Forking paths.** Many reasonable analysis choices multiply the chances of a "significant" result even when only one analysis is run, because the choices depend on the data. Rule: fix the analysis plan before looking and report every comparison made. Source: Gelman and Loken, American Scientist, Nov-Dec 2014 [search](https://www.americanscientist.org/node/3579). Caution: Gelman says the magazine editors introduced a wrong p-value sentence; the p-value is the probability of data at least this extreme if the null model were true [search](https://andrewgelman.com/2014/10/14/didnt-say-part-2/).
- **Sampling and bias.** Name who is in the data and who is missing (self-selection, non-response, survivorship). Check: "Who could not appear in this dataset?" answered in one line. [memory]
- **Base rates.** Quote the denominator and baseline with every "X% of Y". Example: "doubling the risk" at 1 in 10,000 is 2 in 10,000. [memory]
- **Confounders and Simpson's paradox.** Re-cut the headline by the 2-3 likeliest lurking variables; if direction flips, report the split. [memory]
- **Correlation vs cause.** Say once what the data cannot show, and what design would show cause. [memory]
- **Uncertainty in plain words.** "We are 95% sure the value falls in this range". Show uncertainty only when it changes the reading. Shaded bands on lines, dot-plus-range for categories, avoid error bars on bar charts. Source: ONS service manual [opened](https://service-manual.ons.gov.uk/data-visualisation/guidance/showing-uncertainty-in-charts). EU Data Visualisation Guide warns against bar charts with error bars [search](https://data.europa.eu/apps/data-visualisation-guide/error-bars-and-the-cone-of-uncertainty).
- **Sanity checks.** (a) Recompute the headline from raw rows. (b) Order-of-magnitude check against an outside figure. (c) Parts sum to the total. (d) Row counts logged after each join and filter. (e) Scan for duplicates, nulls, unit or definition changes. [memory]
- **Reproducibility.** Raw data read-only; transformations in a script that runs top to bottom; record data version, extract date and package versions; map each number in the text to the line that produces it. [memory]
- **OWID methodology:** no verifiable page found. Gap.

## 3. Writing findings

- **Pyramid, answer first.** One governing thought on top; at most 3 grouped key lines beneath; each point summarises those below. Check: read only the top line of each section; do they sum to the governing thought? [search](https://thinkinsights.net/strategy/pyramid-principle). Minto edition dates conflict across sources; cite as "Minto, edition not verified".
- **SCQA opening.** Situation, Complication, Question, Answer. Check: the reader could plausibly ask the Question aloud at that point. [search]
- **Action titles.** The title is a sentence stating the takeaway; the chart title says what is plotted. Weak: "Revenue by region". Strong: "North region revenue fell while the others held (2025 vs 2024)". Datawrapper gives the same rule [opened](https://www.datawrapper.de/blog/text-in-data-visualizations).
- **Executive summary.** One page: decision needed, recommendation, 3 reasons with numbers, risk, next step with owner and date. [memory]
- **Body vs appendix.** The body holds only what moves the decision. Check: delete the appendix; does the argument stand? [memory]
- **Saying "we don't know".** Name the question, what was tried, why the data cannot answer it, what would, its cost and time, and what you recommend meanwhile. Form: "Data cannot separate X from Y because it has no pre-period. A 4-week holdout would. Until then we act on Z." [memory]

## 4. Charts

- **Type by question (FT Visual Vocabulary)** [opened](https://github.com/Financial-Times/chart-doctor/blob/main/visual-vocabulary/README.md): deviation (diverging bar, spine), correlation (scatter, bubble, XY heatmap), ranking (ordered bar, dot strip, slope, lollipop), distribution (histogram, boxplot, violin), change over time (line, column, slope, area, fan chart), magnitude (column, bar, paired, isotype), part-to-whole (stacked, treemap, waterfall, pie only for few parts), spatial (choropleth, flow map), flow (Sankey, chord). Check: write the question first, then pick from that column.
- **Honest axes.** Bars start at zero. Lines may not, but state the baseline. Dual axes invent correlation; use two charts, small multiples, or index both to 100. Source: local dataviz `references/anti-patterns.md`.
- **Direct labelling.** Put words next to the element; drop the colour key where you can [opened](https://www.datawrapper.de/blog/text-in-data-visualizations).
- **Annotation.** Annotate outliers and context. Two text sizes only. Left-align anything over about 10 words. [opened, same page]
- **Colour for meaning.** One highlighted hue plus grey beats many hues; sequential for magnitude; diverging with a neutral midpoint; cap categories at about 6-8; colour follows the entity when filtering. Source: local dataviz `choosing-a-form.md`, `anti-patterns.md`.
- **Small multiples** when more than about 4-5 series overlap. [local dataviz]
- **Accessibility.** Colour is never the only encoding; check palettes by script; every value reachable without hover; table twin of each chart; hover targets at least 24 px. [local dataviz]
- **Chart checklist (pass/fail):** 1. Title states the takeaway. 2. Subtitle gives unit and period. 3. Source, date and n under the chart. 4. Bars at zero. 5. Series labelled directly. 6. One accent colour carries the point. 7. Passes greyscale and colour-blind check. 8. No dual axis, 3D, or pie over 6 slices. 9. Uncertainty shown if it changes the reading. 10. Table or alt text exists.
- **Tufte, Cairo, Knaflic:** [memory]. Use as idea names only, not quotes.

## 5. Decks

- **Storyline before slides / ghost deck.** Write all titles as sentences in a text outline, sketch each slide with an empty chart, agree the story before building. [memory]
- **One message per slide.** If it needs "and", split it. [local craft-slides]
- **Slide sorter test.** Thumbnails: each shows a title plus one visual; the sequence shows the arc. [memory]
- **Speaker notes** hold what you say, source detail and caveats. [local pptx: `slide.addNotes`]
- **Consistency.** Same title position per slide type; same chart label style; left-align body; no full stop on titles. [local pptx]
- **Open and end.** Open with the conclusion or the ask. End on decision, owner and date. [local craft-slides]
- **Deck checklist:** 1. Titles-only read tells the story. 2. Each slide proves its title. 3. Every number has a source and date. 4. The last slide asks for a decision. 5. Notes contain no unverified figure. 6. The appendix holds the detail.

## 6. Spreadsheets and models

FAST Standard, edition 02c, July 2019, CC BY 4.0 [opened](https://www.stl-training.co.uk/download/forum/40296_FAST-Standard-02c-July-2019.pdf). Newer edition not checked.

- **Separate by type (FAST 1.01-01):** Foundation (inputs, timing), Workings, Presentation, Control (checks, scenarios, change tracking, table of contents).
- **Structure:** consistent columns (1.01-02), one time ruler (1.01-03), calculate once (1.01-07), flow left to right (1.02-01), hide nothing (2.01-08).
- **Consistent formulas (3.02-01):** one formula along each row; no partial range references (3.02-03).
- **No hardcodes (3.04-01):** every number in a labelled input cell.
- **Short formulas (3.03):** "no longer than your thumb"; "no formula should take more than 24 seconds to explain"; no nested IFs. FAST house rules, some debated, so present them as FAST's rules.
- **Labels and units (3.05-01, 3.05-04).**
- **Checks:** master error check visible (2.03-05); model explains itself (2.05-02); list of limitations (2.06-02).
- **Assumptions sheet:** value, unit, source, date and owner per input; scenario tab changes only inputs.
- **Model checklist (pass/fail):** 1. Inputs only on the inputs sheet. 2. No number typed inside a formula. 3. One formula per row across periods. 4. Units on every line. 5. Totals reconcile, check row shows 0. 6. Master check visible. 7. Scenarios switch from one cell and checks stay 0. 8. Zero errors after recalculation. 9. Source and date beside each input. 10. Limitations list present.

## Build on these local skills

S = `/root/.claude/skills/synced/d13e5c22-fd75-4b81-b6fa-7bbe4432d675_ad4b38a0-ff16-4a31-8117-7e768f4021ea/`, P = `/root/.claude/plugins/synced/d13e5c22-fd75-4b81-b6fa-7bbe4432d675_ad4b38a0-ff16-4a31-8117-7e768f4021ea/`

- **`real-reports` (this repo):** strong on sources, finding first, recompute from rows, decision ending, rubric, script. Missing: issue tree, hypothesis, sampling and base-rate rules, uncertainty wording, "we don't know" template, chart type by question, ghost deck, model rules.
- **dataviz:** found only in a temporary bundle path (`/tmp/claude-0/bundled-skills/.../dataviz/`), no SKILL.md in the copy read, no LICENSE. Reuse ideas from `choosing-a-form.md`, `anti-patterns.md`, `color-formula.md`, `scripts/validate_palette.py`, `interaction.md`. Link, do not copy.
- **`S/xlsx/` (Apache 2.0):** formulas not hardcodes; assumptions with sources; colour coding of inputs; recalc zero-errors gate. Missing FAST structure.
- **`S/pptx/` (Apache 2.0):** layouts, `addNotes`, consistency rules, thumbnails for the slide-sorter test. Its "Design Ideas" section conflicts with the owner's flagged-look list; take structure only.
- **`S/docx/`, `S/pdf/` (Apache 2.0):** document mechanics only.
- **`S/deep-research/` (no LICENSE):** decompose and cite; no rigour layer.
- **`S/theme-factory/` (Apache 2.0):** ask-then-confirm theme choice; presets risk a generic look.
- **`P/marketing/skills/performance-report` (no LICENSE):** KPI table shape; benchmark ranges uncited, do not copy.
- **`P/design/skills/research-synthesis` (no LICENSE):** observation vs interpretation; "7 of 10" not "most".

## Teaching notes

Pattern: state the choice, the rejected alternative, the reader's question it serves, and the check that would prove you wrong. One or two sentences, then show.

- Title: "I wrote the finding as the title because the reader skims titles."
- Chart type: "Your question is a ranking, so ordered bars, not a pie. Eyes compare lengths on one baseline more exactly than angles."
- Axis: "Bars start at zero because length carries the value."
- Colour: "Grey for context, one colour for the point."
- Uncertainty: "I show the range because the groups overlap and the ranking could flip."
- We don't know: "We cannot tell X from Y with this data. This test would. Until then I recommend Z."
- Model: "This number sits on the inputs sheet so a reviewer changes it in one place."
- Forking paths: "I fixed the cut-off before looking and list the other cuts I tried."
- End with one question the junior can answer, such as "What would change the recommendation?"
- One teaching line per non-obvious decision. No lectures on settled rules.

## Gaps

- Not opened: Minto, Knaflic, Tufte, Cairo, Gelman and Loken full text, Simpson's paradox and base-rate sources, OWID methodology.
- Failed fetches: Storytelling with Data (404), Gelman blog (403), OWID (404), Datawrapper bar-chart page (404), fast-standard.org (empty).
- Licences confirmed Apache 2.0: pptx, xlsx, docx, pdf, theme-factory. No licence file: dataviz, real-reports, deep-research, performance-report, research-synthesis.
