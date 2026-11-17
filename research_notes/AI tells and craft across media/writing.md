# AI tells and craft in writing

## Part 1: Tells

### Word choice

- **Tell:** "AI vocabulary" cluster: delve, tapestry, testament, pivotal, crucial, underscore (verb), showcase, valuable, potential, findings.
- **Why it reads as AI:** Excess use of these words rose sharply after 2022. Kobak et al. estimated at least 13.5% of 2024 PubMed abstracts were LLM-processed, up to 40% in some subcorpora. Excess words include "potential", "findings" and "crucial".
- **Fix / craft move:** Say the specific thing. "Delve into the causes" becomes "look at why it failed". "Crucial" becomes the reason it matters.
- **Source:** Kobak et al., Science Advances, 2 Jul 2025, https://www.science.org/doi/10.1126/sciadv.adt3813 (data to 2024; GPT-3.5/4 era). Word list: https://github.com/berenslab/llm-excess-vocab (2024 values in `results/excess_words.csv`, not read in full). Caveat: the method cannot separate direct LLM use from people adopting LLM-favoured words. A word alone proves nothing.

- **Tell:** Copula avoidance: "serves as", "stands as", "features", "boasts", "refers to" in place of "is" or "has".
- **Why it reads as AI:** A fancier verb sounds like writing and hides the plain fact. The Wikipedia guide marks this pattern as outdated for current models.
- **Fix / craft move:** Use "is" or "has".
- **Source:** WikiProject AI Cleanup, "Signs of AI writing", https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing (page fetched 2026-11-17; the guide says it is current as of Oct 2026).

- **Tell:** Significance inflation: "marks a pivotal moment", "underscores its importance", "a testament to".
- **Why it reads as AI:** Asserts importance instead of showing it. Readers skip it.
- **Fix / craft move:** State the fact or its consequence. Cut the sentence if there is no consequence.
- **Source:** Wikipedia guide (above). Tagged 2023–2025 in the guide's promotional-language section.

- **Tell:** Vague attribution: "Experts argue", "Industry reports suggest", "Observers have cited".
- **Why it reads as AI:** Names no one, and is often invented. The guide marks this section as partly outdated.
- **Fix / craft move:** Name the source with a link, or delete the claim.
- **Source:** Wikipedia guide (above).

- **Tell:** Generic praise: "a revolutionary titan", "captivates residents and visitors", "vibrant", "nestled", "groundbreaking".
- **Why it reads as AI:** Smoothing toward the most common positive adjective. No information. The guide tags this 2023–2025.
- **Fix / craft move:** Replace each adjective with one fact: a price, date, number or named detail.
- **Source:** Wikipedia guide (above).

### Structure

- **Tell:** Negative parallelism: "It's not just X, it's Y", "not only X, but also Y", "Y rather than X".
- **Why it reads as AI:** Often corrects a misconception nobody held. The Wikipedia guide calls "rather than" "particularly common in recent LLM output". A TechCrunch piece (20 Apr 2026) quotes a detection-vendor CEO calling it a strong but non-conclusive pattern.
- **Fix / craft move:** State the claim directly. Keep a contrast only where a reader really holds the wrong view.
- **Source:** TechCrunch, https://techcrunch.com/2026/04/20/ai-writing-its-not-just-this-its-that-barrons/ ; Wikipedia guide (above).

- **Tell:** Reflexive rule of three.
- **Why it reads as AI:** Threes sound complete. The third item is often filler.
- **Fix / craft move:** List what you have. One specific example beats three vague ones.
- **Source:** Wikipedia guide (above), listed without an era tag; the guide notes it is stronger in some contexts.

- **Tell:** Empty opener and tidy closer: a summary at the end, "In conclusion", "Ultimately", "Future outlook".
- **Why it reads as AI:** NN/G found AI puts the summary at the end, so readers must read to the bottom for the answer.
- **Fix / craft move:** Lead with the answer. End when the last point lands. Cut the recap.
- **Source:** NN/G, "Product-Specific GenAI Needs to Write for the Web", 4 Apr 2025, https://www.nngroup.com/articles/genai-write-for-the-web/ (2025, model era not stated).

- **Tell:** Formulaic challenges section: "Despite its success, X faces several challenges", then a positive close.
- **Why it reads as AI:** A template, not a finding.
- **Fix / craft move:** Name one real challenge with its cost to a real person or a number.
- **Source:** Wikipedia guide (above).

- **Tell:** Hedging preamble: "While X is true, it's important to note…" then the same claim asserted.
- **Why it reads as AI:** Concedes a point, then asserts the claim anyway. The guide tags "it's important to note" as 2023–2024 and editorialised nuance as mid-2026.
- **Fix / craft move:** Make the claim, then one real limit with a specific condition.
- **Source:** Wikipedia guide (above).

- **Tell:** Uniform rhythm: similar sentence lengths and paragraph shapes.
- **Why it reads as AI:** The guide reports more periods and commas and sentences of about 8–20 words in the newest model era. That claim is from a fetched summary and I could not confirm the exact figure.
- **Fix / craft move:** Read it aloud. Put a short sentence after a long one. Break the pattern once per paragraph.
- **Source:** Wikipedia guide (above), "newest era" tag; unverified figure.

- **Tell:** Em-dash overuse.
- **Why it reads as AI:** The guide lists it as a sign, and its own section calls it a historical indicator (2022 to Sept 2026), so it is weakening as a tell for the newest models. NPR (10 Nov 2025) reports writers avoiding em dashes for fear of looking AI-made. A July 2025 study (The Conversation) found readers name em dashes as a chatbot marker, yet their detection was only slightly better than chance.
- **Fix / craft move:** Use a comma, period or parentheses where they serve. Keep the dash where the sentence needs it. One em dash is not evidence.
- **Source:** Wikipedia guide (above); The Conversation, Jul 2025, https://theconversation.com/too-many-em-dashes-weird-words-like-delves-spotting-text-written-by-chatgpt-is-still-more-art-than-science-259629 ; NPR, https://www.npr.org/2025/11/10/nx-s1-5596088/inside-the-unofficial-movement-to-save-the-em-dash-from-a-i

### Length, format, reading level

- **Tell:** Padding and over-length.
- **Why it reads as AI:** NN/G's test found AI answers longer than the question needed. Participants said a yes/no question got "a lot of info". Sales pitch and tangents crept in.
- **Fix / craft move:** Answer first, then only what the reader needs to act. Cut anything that does not change their decision.
- **Source:** NN/G, 4 Apr 2025 (above).

- **Tell:** Formatting as decoration: bold on every term, bullets for prose, headers on short text, "Key takeaways" boxes, emoji headers.
- **Why it reads as AI:** Formatting used where prose would do reads like a slide. The Wikipedia guide lists emoji headers, curly quotes and excessive boldface as signs.
- **Fix / craft move:** Use lists only when the content is a list. Bold one or two key terms. Use real list markup.
- **Source:** NN/G, 4 Apr 2025; Wikipedia guide (above).

- **Tell:** Jargon for a basic question.
- **Why it reads as AI:** Technical terms appear where the reader did not ask for them.
- **Fix / craft move:** Aim for about a 6th–8th grade reading level in web copy. Describe what the term does: "gears for specific terrains" for "drivetrain".
- **Source:** NN/G, 4 Apr 2025.

- **Tell:** Chatbot residue: "I hope this helps", "Would you like…", "Here are several neutral paraphrases", knowledge-cutoff disclaimers, placeholder text.
- **Why it reads as AI:** Chatbot correspondence pasted into the text. The guide tags this 2023–early 2026.
- **Fix / craft move:** Delete. Check the first and last line of every draft.
- **Source:** Wikipedia guide (above).

### Sourcing and facts

- **Tell:** Invented or decorative citations: dead links, DOIs resolving to unrelated papers, references that do not exist, `utm_source=openai` or `utm_source=chatgpt.com` tracking tags, unused named references.
- **Why it reads as AI:** Citations look sourced without being checked.
- **Fix / craft move:** Check every link and figure before publishing. If you cannot find a source, delete the claim. Do not write "studies show".
- **Source:** Wikipedia guide (above), citations section (era not stated).

## Part 1b: Current (2025–26) vs outdated (2023–24)

Built from the Wikipedia guide's own era tags, where it gives them. Verify against the page before relying on dates.

- **Still current or newest:** negative parallelism ("rather than"), editorialised nuance in hedges (mid-2026), corrective framings such as "does not establish" and "should not be confused" (mid-2026 onward, "extremely uncommon" before then), primary-source over-stress ("records that", "identifies him as", 2026 onward), notability by listing media coverage (2025 onward), uniform sentence rhythm (newest era).
- **Outdated per the guide:** copula avoidance, vague attribution, named references, URL and date placeholders, em-dash overuse (as a sole signal), promotional vocabulary (tagged 2023–2025), "it's important to note" (tagged 2023–2024).
- **Caveat:** the guide's model-era names (GPT-4 through GPT-6) are its own labels, not verified against vendor release dates.

## Part 2: Craft principles

These come from older sources read secondhand. Treat them as principles, not verified quotes.

1. **Cut clutter.** Zinsser, *On Writing Well* (original 1976, possibly outdated on examples): "Writing improves in direct ratio to the number of things we can keep out of it that shouldn't be there." Drop qualifiers (very, quite, a bit, sort of) and "currently" where "now" works. Summary: https://www.litcharts.com/lit/on-writing-well/summary (check the book's Simplicity and Clutter chapters before quoting).
2. **Rules for when instinct fails.** Orwell, "Politics and the English Language" (1946, possibly outdated on tone; the principles hold): cut any word that can go; prefer the short word; prefer the active voice; avoid figures of speech seen many times in print; use an everyday word over jargon. He also says to break any rule rather than write something barbarous. Secondary source: https://en.wikipedia.org/wiki/Politics_and_the_English_Language
3. **Know what you think first.** Zinsser ties clear writing to clear thinking. Generic prose usually comes from a writer who has not decided the claim. A CapX editor's guide (Aug 2026, https://capx.co/an-editors-guide-to-spotting-ai-writing) argues AI is weak at original opinion because it aggregates. Secondhand.
4. **Be specific.** Name the person, number, place, price or date. Replace each adjective that could describe anything.
5. **Put the answer first.** NN/G's inverted pyramid: main point, support, then detail. Web readers scan.
6. **Write for one reader.** NN/G's fix is to match length and detail to the question. Decide the reader before drafting.
7. **Rewrite.** Zinsser calls rewriting where the game is won or lost. Treat the first AI draft as raw material. Cut the first and last paragraphs and see whether anything is lost.
8. **Use your voice.** Read it aloud. If you would not say the sentence to a colleague, rewrite it. Vary length on purpose.
9. **Show, do not announce.** "This matters because" and "it's important to note" announce. Put the fact there instead.

## Part 3: How each medium goes wrong with AI

- **Marketing and product copy:** generic praise, negative parallelism, vague benefits ("seamless", "revolutionary"). NN/G's product-embedded test showed tools answering a simple product question with an irrelevant guide. Good copy names the feature, the buyer, and what changes for them.
- **SEO content:** padding to a word count, a summary at the end, headings that repeat the query. Good pages answer the query in the first lines, then add detail the reader does not already have.
- **Academic prose:** hedged, vague attribution and the AI-vocabulary set, now measured in 2024 abstracts (Kobak et al.). Good academic writing states the claim, the evidence and the limit, and cites specific papers.
- **Customer emails:** not researched in depth. The same tells apply: preambles, generic praise, a tidy close. Lead with the reason for writing.

## Gaps and caveats

- No 2025–26 source found on marketing or SEO content quality beyond NN/G's product-tool testing. No measured outcomes.
- Wikipedia guide: fetched via a summarising tool. Era tags are its own. The shorter-sentence figure and GPT-4–6 mapping are unverified.
- Orwell and Zinsser: read via secondary summaries, not the books.
- Kobak et al. covers biomedical abstracts. Its word list may not transfer to other prose.
- Reader studies (The Conversation 2025; NPR 2025) suggest individual tells are weak evidence. A tell prompts a closer look, not a verdict.
- Not researched: writing-community consensus, linguistics corpus papers beyond Kobak, GitHub anti-AI-writing skill repos.
