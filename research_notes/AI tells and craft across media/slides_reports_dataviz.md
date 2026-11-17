# AI tells and craft: slides, reports, dataviz, spreadsheets

**Status note (read first):** Web search hit rate limits after 5 queries and two page fetches returned 404/blocked. Entries marked **[verified]** were read in a fetched page or a search snippet from the cited URL. Entries marked **[unverified, from memory]** must be checked before they go into a skill. Nothing here is invented; gaps are listed at the end.

---

## A. Tells and failure patterns

### A1. Reports with fabricated references (Deloitte Australia)
- **Tell:** A government-commissioned report with citations to sources that do not exist and a misquoted court judgment.
- **Why it reads as AI:** Generative models produce plausible references and quotes that look right and are never checked. The reader trusts the formatting. Nobody in the review chain verified the citations.
- **Fix / craft move:** Every cited source gets a link, and a named person checks each one against the original before sign-off. Quotes are copied from the source text, never regenerated. Disclose AI use in the document.
- **Source:** Reported in late 2025 by Australian media, as a summary from search; the primary article was not retrieved. [unverified, from memory] Contract value about A$440k; Deloitte reportedly refunded part or all of the final payment and reissued a version disclosing generative-AI use. Check exact figures in the original AFR or Guardian coverage before citing. Publish date: late 2025.

### A2. "Workslop": polished output that moves work to the recipient
- **Tell:** Documents, decks or memos that look finished but lack substance, so the recipient has to rework or decode them.
- **Why it reads as AI:** Length and polish are cheap with AI; the decision, the evidence and the specifics are missing. The effort is shifted to the reader.
- **Fix / craft move:** Before sending, state the one decision or conclusion the reader needs, then check that every section supports it. Cut any section that a reader could not act on.
- **Source:** Harvard Business Review, "AI-Generated 'Workslop' Is Destroying Productivity," by BetterUp Labs and the Stanford Social Media Lab. Published 22 Sep 2025, updated 25 Sep 2025. [verified: date and premise from fetched page; the page text returned was only the intro] The survey figures I recall (about 1,150 US employees; about 40% received workslop in the prior month; a per-employee cost estimate) are [unverified, from memory]. Re-check them in the full article before quoting.

### A3. Every slide titled with a noun phrase ("Market overview", "Key takeaways")
- **Tell:** Slide titles are topic labels. The message has to be found in the chart.
- **Why it reads as AI:** Topic labels are the default for a model asked to "make slides about X." They describe the content rather than claim something about it.
- **Fix / craft move:** Make each title a full-sentence claim, the conclusion of the slide ("Churn fell 3 points after onboarding changed"). Check the deck by reading only the titles: they should tell the story.
- **Source:** Knaflic's Storytelling with Data blog says she sets each slide title to the main point or takeaway, not a descriptive label. [verified: search snippet from storytellingwithdata.com, "a quick presentation makeover" and "structure your slides"; the think-cell guide "How to tell a better data story one slide at a time" (2025 or later, undated in snippet) states the same split: chart title describes, action title tells the story.] Publish date: blog posts undated in snippets; treat as 2016-2025.

### A4. Wall of bullets
- **Tell:** Four to seven bullets per slide, each 8-15 words, same weight.
- **Why it reads as AI:** The model lists everything it found; nothing is ranked or cut.
- **Fix / craft move:** One message per slide. If the slide needs "and" to describe what it shows, it has two messages and needs two slides (secondary consultant heuristic, Deckary blog, undated). Put the number or the image in the centre and the explanation in one line beneath.
- **Source:** Knaflic, "one thing on stage" blog post (2016) [verified snippet]. Consultant heuristic [unverified source date].

### A5. Filler claims without numbers
- **Tell:** "Significant growth," "best-in-class," "enables transformation," no figure, no baseline, no source.
- **Why it reads as AI:** Generic buzzwords are the statistically likely continuation. They sound like a claim but cannot be checked.
- **Fix / craft move:** Replace each adjective with a number, its baseline and its date, or delete the sentence. If the number is unknown, write "not measured" and say what would measure it.
- **Source:** Craft principle, no single source. [unverified, from memory] Standard consultant editing practice (McKinsey-style "so what" test).

### A6. Key takeaways / summary slide that repeats the deck
- **Tell:** A closing slide with three generic bullets that restate earlier slides.
- **Why it reads as AI:** Summaries are trained-in habit. They add length without a decision.
- **Fix / craft move:** End with the recommendation and the decision needed, with owner and date. Cut the recap.
- **Source:** Craft principle, [unverified, from memory].

### A7. Stock-template visuals: gradient backgrounds, icon rows, symmetric three-column cards
- **Tell:** Three icon boxes, each with a heading and a two-line blurb; purple-to-blue gradient background.
- **Why it reads as AI:** These are the most common layouts in the training data. Their symmetry carries no information about the content.
- **Fix / craft move:** Let the layout follow the content: a comparison is a table or a paired bar; a process is a numbered sequence. Use the house template colours with a single accent for the one point. Check against the banned list in `/home/user/Claude-Mode/CLAUDE.md` (gradients, icon rows, Inter, em dashes in UI copy) and ask the owner before using any of them.
- **Source:** Project list in `/home/user/Claude-Mode/CLAUDE.md` (items 1, 3, 8, 10, 16, 19). This is the owner's list, not a published study. [verified: file read in session]

### A8. Default AI charts
- **Tell:** Rainbow categorical colours, legend far from the lines, gridlines and borders on everything, pie charts with eight slices, 3D effects, bars that do not start at zero, no units or source.
- **Why it reads as AI:** Defaults from charting libraries are used without a decision about what the chart is for.
- **Fix / craft move:** Pick the chart from the question: comparison = bar (zero baseline); change over time = line (labelled endpoints OK off zero); part-to-whole with few parts = bar or labelled segments. Label series directly at the line end. Use grey for context, one saturated colour for the point. Remove gridlines and borders; keep one baseline. Put the unit and source in the subtitle.
- **Source:** Cairo and Tufte principles [unverified, from memory; not fetched]. Datawrapper chart guide fetch returned 404, so no Datawrapper citation is verified here.

### A9. Truncated or misleading axes
- **Tell:** Bar chart starting at 95; dual axes with unrelated scales; cherry-picked start dates.
- **Why it reads as AI:** Models optimise for visible difference, not for the reader's reading of magnitude.
- **Fix / craft move:** Bars start at zero. For lines, show the baseline and the change explicitly. Use the same date range for comparisons; say why if it differs.
- **Source:** [unverified, from memory] Cairo, *How Charts Lie* (2019); Tufte, *The Visual Display of Quantitative Information*.

### A10. Hardcoded numbers in spreadsheets and models
- **Tell:** A cell containing 0.23 inside a formula, or a growth rate typed into forty places.
- **Why it reads as AI:** Models write working formulas with values pasted in, so the numbers cannot be changed or traced.
- **Fix / craft move:** One assumptions sheet, with every driver entered once and labelled with unit and source. Calculations reference it. No hardcodes in calc or output sheets. Protect input cells and use data validation.
- **Source:** FAST Standard (Flexible, Appropriate, Structured, Transparent), edition 02c, July 2019 [verified: search summary; primary PDF not fetched; fast-standard.org is the official site]. Possibly outdated in version; the principles are still the professional reference. Quintedge and Brixx blogs are secondary.

### A11. Unverified statistics
- **Tell:** "Studies show 73% of teams…" with no link, or a link to a homepage.
- **Why it reads as AI:** Plausible numbers are generated without a lookup.
- **Fix / craft move:** Any number in the report links to its primary source with a date. If a source cannot be found, delete the number or mark it "estimate, basis: …". Ask the model to list its sources and check each one; a missing link is a fail.
- **Source:** Same as A1 (Deloitte case) [unverified detail].

---

## B. Craft principles (what skilled humans do)

1. **The answer goes first.** Consultants write the conclusion as the title and the first paragraph (pyramid principle, Barbara Minto, *The Pyramid Principle*, 1987; older source, still the standard). Group supporting points in MECE groups.
2. **SCQA framing for reports.** Situation, complication, question, answer. Use it to open a memo or executive summary. [unverified, from memory]
3. **Horizontal and vertical logic.** Titles alone tell the story (horizontal). Each slide's body proves its title (vertical). Knaflic's checks, verified via her blog snippets.
4. **Decide, don't survey.** A report ends with a recommendation, the options considered, what it costs and the decision needed by when. A research summary without a recommendation is unfinished.
5. **Show the data-ink.** Remove anything that does not carry information (Tufte, data-ink ratio). [unverified, from memory]
6. **Direct labels beat legends.** Label the thing, not the colour. [unverified, from memory]
7. **Name the uncertainty.** Give ranges or confidence, state the date of the data, and say what the analysis cannot show. Confident vagueness is the strongest AI tell in a report.
8. **Source line on every chart.** Source, date, unit, n, and definition of any metric that is not obvious.
9. **Editing pass for filler.** Read aloud. Delete any sentence that does not change what the reader will do or believe.
10. **Check the numbers twice.** Recompute each figure from the source rows, not from the summary text. A second person spot-checks the top five claims.

---

## C. Verification checklist before shipping AI output

- Open every link. Confirm the title, author and date match the claim.
- Find every quote in the source text (not a paraphrase presented as a quote).
- Recompute every number from its source; check units and periods.
- Check each chart's axis, baseline and date range against the claim in its title.
- Check the spreadsheet for hardcodes outside the assumptions sheet and for totals that do not sum.
- Remove any claim you cannot trace.

---

## D. Gaps (not verified in this run)

- Primary Deloitte/DEWR coverage (AFR, Guardian) was not retrieved. Figures in A1 are unverified.
- Survey figures from the workslop study are unverified (full HBR article text not returned).
- Datawrapper, FT and Economist style guides: not retrieved. Their rules are not cited here.
- Tufte, Cairo, Duarte, Garr Reynolds: principles stated from memory; no 2025-2026 source checked.
- No Reddit r/consulting or r/PowerPoint threads reviewed.
- Recommended next step: rerun searches for (1) Deloitte/AFR coverage, (2) Datawrapper "chart design" guide, (3) FT visual vocabulary, (4) FAST standard current version, once the search quota resets.
