# AI tells and craft in writing

Scope: how AI-made prose is recognized, and what skilled writers do instead. Craft quality, not detector evasion. Sources are dated; "possibly outdated" means pre-2025 or a model era that has since changed.

## Part 1: Tells

### Word choice

**Tell: "AI vocabulary" cluster** (delve, tapestry, testament, pivotal, crucial, underscore as a verb, showcase, intricate, valuable, landscape)
- Why it reads as AI: these words rose sharply after 2022. Kobak et al. found excess use in 15M+ PubMed abstracts (2010–2024), with "delve" the best-known example. Estimated at least 13.5% of 2024 abstracts were LLM-processed, up to 40% in some subcorpora. Excess words also include "potential", "findings" and "crucial".
- Fix: say the specific thing. "Delve into the causes" becomes "look at why it failed". "Crucial" becomes the reason it matters.
- Source: Kobak et al., Science Advances, 2 Jul 2025, https://www.science.org/doi/10.1126/sciadv.adt3813 (data to 2024, GPT-3.5/4 era). Word list: https://github.com/berenslab/llm-excess-vocab (2024 values in `results/excess_words.csv`; not read in full).
- Caveat: the method can't separate direct LLM use from people copying LLM-favoured words. Words alone prove nothing.

**Tell: copula avoidance** ("serves as", "stands as", "features", "boasts", "refers to" in place of "is/has")
- Why: a fancier verb sounds like writing and hides the plain fact.
- Fix: use "is" or "has". Plain verbs are usually right.
- Source: WikiProject AI Cleanup, "Signs of AI writing", https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing (cited for a decline in "is/are" in academic writing after 2023; current as of the page's own date, verified only via a fetched summary).

**Tell: significance inflation** ("marks a pivotal moment", "underscores its importance", "a testament to")
- Why: asserts importance instead of showing it. Readers skip it.
- Fix: state the fact, or its consequence. Cut the sentence if the consequence is nothing.
- Source: Wikipedia guide (above).

**Tell: vague attribution** ("Experts argue", "Industry reports suggest", "Observers have cited")
- Why: names no one. Often invented.
- Fix: name the source with a link, or delete the claim.
- Source: Wikipedia guide (above). The guide flags this section as partly outdated.

**Tell: generic praise** ("a revolutionary titan", "captivates residents and visitors")
- Why: statistical smoothing toward the most common positive adjective. No information.
- Fix: swap the adjective for one fact, price, date, number or named detail.
- Source: Wikipedia guide (above).

**Tell: hedging preambles** ("While X is true, it's important to consider nuance")
- Why: concedes a point and then asserts the same claim anyway.
- Fix: make the claim, then one real limit with a specific condition.
- Source: Wikipedia guide (above), flagged as a 2026 pattern.

### Sentence and paragraph structure

**Tell: negative parallelism** ("It's not just X, it's Y"; "not only X, but also Y"; "not X, but Y")
- Why: often corrects a misconception nobody held. Heavily overrepresented in model output. A 2026 TechCrunch piece quotes a detection vendor's CEO calling it a strong but not conclusive pattern. An editor's guide calls "not only… but also" once-per-article fine and every-paragraph a tell.
- Fix: state the claim directly. Keep the contrast only where a reader really holds the wrong view.
- Source: TechCrunch, 20 Apr 2026, https://techcrunch.com/2026/04/20/ai-writing-its-not-just-this-its-that-barrons/ ; Wikipedia guide (named "negative parallelisms").

**Tell: reflexive rule of three**
- Why: lists come in threes because that sounds complete. Often the third item is filler.
- Fix: list what you actually have. One specific example beats three vague ones.
- Source: Wikipedia guide (rule-of-three in influence claims).

**Tell: empty opener and tidy closer** (summary at the end; "In conclusion"; "Ultimately"; "Future outlook")
- Why: NN/G found AI puts the summary in the conclusion, so users must read to the end for the answer. Human editors lead with it.
- Fix: lead with the answer. End when the last point lands. Cut the recap.
- Source: NN/G, "Product-Specific GenAI Needs to Write for the Web", 4 Apr 2025, https://www.nngroup.com/articles/genai-write-for-the-web/

**Tell: formulaic challenges section** ("Despite its success, X faces several challenges…" then a positive close)
- Fix: name one real challenge, with its cost to a real person or number.
- Source: Wikipedia guide.

**Tell: uniform rhythm**
- Why: paragraphs and sentences of similar length, each with the same shape. The Wikipedia guide reports 8–20-word sentences as a later-model pattern. That is a secondhand summary; I did not verify the figure.
- Fix: read it aloud. Put a short sentence after a long one. Break the pattern on purpose once a paragraph.
- Source: Wikipedia guide (model-era claims unverified).

**Tell: em-dash overuse**
- Why: listed as a common sign in the Wikipedia guide. NPR (Nov 2025) reports writers now avoid em dashes for fear of looking AI-made. A July 2025 study (reported by The Conversation) found readers name em dashes as a chatbot marker, yet their detection was only slightly better than chance.
- Fix: use a comma, a period, or parentheses. Do not remove a dash the sentence needs. One em dash is not evidence of anything.
- Source: The Conversation, Jul 2025, https://theconversation.com/too-many-em-dashes-weird-words-like-delves-spotting-text-written-by-chatgpt-is-still-more-art-than-science-259629 ; NPR, 10 Nov 2025, https://www.npr.org/2025/11/10/nx-s1-5596088/inside-the-unofficial-movement-to-save-the-em-dash-from-a-i
- Note for this project: CLAUDE.md bans nothing here, but em dashes in UI copy are on the "looks vibecoded" list (rule 16). Ask the owner first.

### Length, format, reading level

**Tell: padding and over-length**
- Why: NN/G's test found AI answers longer than the question needed. Participants said a yes/no question got "a lot of info". Sales pitch and tangents crept in.
- Fix: answer first, then only what the reader needs to act. Cut anything that does not change their decision.
- Source: NN/G, 4 Apr 2025 (above).

**Tell: formatting as decoration** (bold on every term, bullets for prose, headers on short text, "Key takeaways" box, emoji headers)
- Why: formatting used where prose would do looks like a slide. Wikipedia lists emoji headers, curly quotes and excessive boldface as signs.
- Fix: use lists only when the content is a list. Bold one or two key terms, not everything. Use real list markup.
- Source: NN/G (2025), Wikipedia guide.

**Tell: jargon for a basic question** (technical terms the reader was not asked about)
- Fix: write for about a 6th–8th grade reading level for web copy. Replace the term with what it does ("gears for specific terrains" for "drivetrain" and "torque").
- Source: NN/G, 4 Apr 2025.

**Tell: chatbot residue** ("Here are several neutral paraphrases", "I hope this helps", knowledge-cutoff disclaimers, prompt refusals left in the text)
- Fix: delete. Read the first and last line of every draft.
- Source: Wikipedia guide.

### Sourcing and facts (matters most for SEO, marketing, academic)

**Tell: invented or decorative citations** (dead links, DOIs that resolve to unrelated papers, references that do not exist, utm_source parameters, named references never used)
- Fix: check every link and statistic before publishing. If you cannot find a source, delete the claim. Do not write "studies show".
- Source: Wikipedia guide, citations section.

**Tell: generic statistics with no source**
- Fix: keep the number only with its source and date. Otherwise write the observation you actually made.
- Source: general; see gaps below.

## Part 2: Craft principles

These are from older, mostly pre-2025 sources read secondhand. Treat as principles, not verified quotes.

1. **Cut clutter.** Zinsser (*On Writing Well*, original 1976, possibly outdated on examples): "Writing improves in direct ratio to the number of things we can keep out of it that shouldn't be there." Drop qualifiers (very, quite, a bit, sort of), and "currently" when "now" does the job. Check each word for a job. Secondary sources: https://www.litcharts.com/lit/on-writing-well/summary (summary only; check the book's Simplicity and Clutter chapters before quoting).
2. **Rules for when instinct fails.** Orwell, "Politics and the English Language" (1946, possibly outdated on tone, principles hold): cut any word that can go; prefer the short word; prefer the active voice; avoid the figure of speech you have seen in print many times; use an everyday word over jargon. Orwell also says to break any rule rather than write something barbarous. Secondary sources: https://en.wikipedia.org/wiki/Politics_and_the_English_Language
3. **Know what you think first.** Zinsser ties clear writing to clear thinking. Generic prose usually comes from a writer who has not decided their claim. Fix the thesis before the sentences. An editor's guide (CapX, Aug 2026, https://capx.co/an-editors-guide-to-spotting-ai-writing) argues AI is weak at original opinion because it aggregates. Secondhand, but consistent with the Wikipedia guide's "generic" tells.
4. **Be specific.** Name the person, the number, the place, the price, the date. A concrete detail is the most reliable thing a human adds. Replace each adjective that could describe anything.
5. **Put the answer first.** NN/G's inverted pyramid: the main point, then support, then detail. Readers on the web scan.
6. **Write for one reader.** NN/G's fix for AI copy is matching length and detail to the question. Decide who the reader is before drafting; the detail level follows.
7. **Rewrite.** Zinsser calls rewriting where the game is won or lost. A first AI draft is raw material. Cut the first paragraph and the last paragraph and see whether anything is lost.
8. **Use your voice.** Read it aloud. If you would not say the sentence to a colleague, rewrite it. Vary length on purpose.
9. **Show, do not announce.** "This matters because" and "it's important to note" are announcements. Put the fact there instead.

## Part 3: How each medium goes wrong with AI

- **Marketing and product copy:** the failure is generic praise, negative parallelism and vague benefits ("seamless", "revolutionary"). The NN/G product-embedded example shows tools that answer a simple product question with an irrelevant guide. Good copy names the feature, the buyer, and what changes for them.
- **SEO content:** the failure is padding to a word count, a summary at the end, and headings that repeat the query. Good SEO pages answer the query in the first lines, then add detail the reader does not already have. Gap: I found no 2025–2026 source with measured SEO outcomes.
- **Academic prose:** the failure is hedged, vague attribution and the "AI vocabulary" set, now measured in 2024 abstracts (Kobak et al.). Good academic writing states the claim, the evidence, and the limit, and cites specific papers.
- **Emails to customers:** not researched in depth. The same tells apply: preambles, generic praise, a tidy close. Lead with the reason for writing.

## Gaps and caveats

- No primary source found for marketing copy or SEO quality beyond NN/G product-tool testing (2025).
- Wikipedia guide: the fetched summary gave model-era date ranges (GPT-4 through GPT-6) I could not verify against the page. Use the tell list, not the dates.
- Orwell and Zinsser: read via secondary summaries, not the books.
- Kobak et al. is a word-frequency study on biomedical abstracts, not general prose. Its word list may not transfer.
- The "readers can't tell" finding (The Conversation, Jul 2025; Wikipedia guide citing a 2025 study) suggests that tells are weak evidence on their own. A tell is a prompt to look closer, not a verdict.
- Not researched: writing communities' current consensus, linguistics corpus papers beyond Kobak, and GitHub anti-AI-writing skill repos.
