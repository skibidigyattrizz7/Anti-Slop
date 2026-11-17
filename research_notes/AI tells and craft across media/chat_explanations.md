# AI tells and craft: chat replies, emails, posts, explanations

Scope: how AI-written conversation and explanation gets read as AI, and what skilled humans do instead. Craft quality, not detector evasion. Sources were checked at search-snippet level unless marked "opened". Dates given where found; anything before 2025 is flagged.

## Tells

### Sycophantic openers and praise
- **Tell:** "Great question!", "What a fantastic idea", "You're absolutely right" before any content.
- **Why it reads as AI:** It is flattery with no information. Research says models drift toward agreeing with and praising the user because human raters often prefer agreeable answers. Sharma et al. (Anthropic) found humans and preference models sometimes prefer convincing sycophantic answers over correct ones. Source: [Towards Understanding Sycophancy in Language Models](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models), Oct 2023 (possibly outdated for model era; the mechanism still matches 2025 work).
- **Fix / craft move:** Start with the answer or the specific thing you actually noticed about their question. Delete the praise line. If the user is wrong, say so plainly with the reason.
- **Source:** ELEPHANT benchmark, [arXiv:2505.13995](https://arxiv.org/abs/2505.13995) (v2 dated 29 Sep 2025, ICLR 2026 poster). Tested 11 models; they preserved user "face" about 45 percentage points more than humans in general-advice and moral-judgment prompts. Social sycophancy is rewarded in preference data and current mitigations are weak.

### Caving to pushback
- **Tell:** "You're right, I apologize" followed by a reversed correct answer when the user just pushed back.
- **Why it reads as AI:** Agreement is cheap and looks polite, but it signals no independent judgment. Sharma et al. report models conceding to mistakes that weren't theirs.
- **Fix / craft move:** Re-check. If the original was right, say "I checked, the original holds, here is why." If it was wrong, name the specific error and correct it once.
- **Source:** [Sharma et al., Anthropic, Oct 2023](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models) (possibly outdated for model era).

### Over-apologizing and over-hedging
- **Tell:** "I apologize for any confusion", "It's important to note", "may potentially", "While there are many factors...".
- **Why it reads as AI:** Hedges and apologies that carry no information. Readers stop trusting the sentence when every claim is wrapped in qualifiers.
- **Fix / craft move:** Say how confident you are once, and why ("I'm fairly sure; I haven't run it"). Delete apologies unless you caused a real error.
- **Source:** Wikipedia's "Signs of AI writing" lists vague hedges and inflated qualifiers. [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), page updated through 2026; opened, partial read.

### Bullet-everything and bolded headers in casual replies
- **Tell:** A two-sentence answer broken into bold labels and five bullets. "**Key takeaways:**", "**Pros:**", "**Cons:**".
- **Why it reads as AI:** Formatting signals a report, not a conversation. Structure is applied to content that does not have that shape. Wikipedia's guide names markdown and bold-label formatting in chat leftovers as a common current sign.
- **Fix / craft move:** Match the shape of the question. Short question, short prose answer. Use a list only when items are truly parallel or the user needs to scan steps. Bold no more than one key term.
- **Source:** [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (opened; markdown named in intro and a dedicated section).

### Rule-of-three and "not X, but Y" constructions
- **Tell:** "It's not just a tool, it's a partner." "Fast, reliable, and secure." Triplets on every list.
- **Why it reads as AI:** The "not X, but Y" frame argues against a misconception the reader never had. Triplets are a rhythm default, not a count of what exists.
- **Fix / craft move:** State the claim. Give the number of items that actually exist, even if it is two or four.
- **Source:** [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (opened; "negative parallelisms" and "rule of three" sections).

### Puffery and vague authority
- **Tell:** "a pivotal moment", "stands as a testament to", "Experts argue", "Industry reports suggest", "plays a vital role".
- **Why it reads as AI:** Inflates importance without a specific fact. Vague attribution implies sources that were never named.
- **Fix / craft move:** Replace with the concrete fact or who said it. If you cannot name the source, cut the claim.
- **Source:** [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (opened).

### Overused vocabulary
- **Tell:** "delve", "tapestry", "underscore", "pivotal", "showcase", "intricate", "landscape", "navigate the complexities".
- **Why it reads as AI:** Kobak et al. estimate that the appearance of LLMs led to an abrupt rise in certain style words in PubMed abstracts from 2024. Their estimate: at least 13.5% of 2024 abstracts were processed with LLMs. Single uses mean nothing; a cluster is the signal.
- **Fix / craft move:** Use the plain verb. "Shows" not "showcases"; "uses" not "leverages"; "is" not "serves as".
- **Source:** Kobak et al., [Science Advances, July 2025](https://arxiv.org/abs/2406.07016) (preprint June 2024, later versions retitled "LLM-assisted writing in biomedical publications"). Secondary summary only; the journal page was not opened.

### Em dashes
- **Tell:** Multiple em dashes per paragraph, especially in "X — a Y — that Z" asides.
- **Why it reads as AI:** Em dashes are used heavily in model output. Humans use them too, so this is weak evidence alone.
- **Fix / craft move:** Use a full stop or a comma. Keep at most one per paragraph when you do use it. Treat as a reason to re-read, not a verdict.
- **Source:** [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (opened; listed as a historical/current sign with a caveat). Dev.to and PCWorld summaries also list it ([Dev.to](https://dev.to/perufitlife/i-built-a-free-ai-tell-detector-after-my-own-reddit-account-got-2-all-comments-are-ai-generated-57ei) is anecdotal and sells a tool; treat cautiously).

### Summary-restating closers
- **Tell:** "In summary, X is important. By following these steps, you can Y. I hope this helps!"
- **Why it reads as AI:** It repeats what was just said and adds a generic warm sign-off.
- **Fix / craft move:** End when the content ends. If a next step matters, state that step only.
- **Source:** Pattern named in the Wikipedia guide's formulaic-section discussion ([Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), opened). "I hope this helps" specifically was not confirmed in an opened source; treat as widely reported, not verified.

### Menus of follow-up offers
- **Tell:** "Would you like me to: (1) ... (2) ... (3) ... Let me know which!"
- **Why it reads as AI:** It hands the work back to the user and pads the reply. It is generic and needs no context.
- **Fix / craft move:** Give one useful next step tied to their situation, or nothing. Ask one question only when you genuinely cannot continue.
- **Source:** Not found in an opened source during this pass. Gap: no research-backed citation for this specific tell. Based on the general pattern in [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) ("Answer: ... numbered options" leaked replies).

### Fake enthusiasm and buzzword copy
- **Tell:** "Exciting news!", "Unlock the power of", "seamless", "robust", "game-changing", "empower your team".
- **Why it reads as AI:** Words that claim value without a claim. The reader cannot act on them.
- **Fix / craft move:** Name the change in numbers or behavior. "Cuts setup from 20 to 5 minutes" beats "seamless onboarding".
- **Source:** Wikipedia's promotional-tone section ([Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), opened). Google's developer voice guide also bans buzzwords ([Google voice and tone](https://developers.google.com/style/tone), search snippet, not opened).

### Chat leftovers in published text
- **Tell:** "Here are several neutral paraphrases:", "Certainly!", "Knowledge cutoff" disclaimers, placeholder text like `[insert date]`, or a pasted reply that starts "Answer:".
- **Why it reads as AI:** The writer did not edit out the conversation wrapper. Wikipedia editors treat such pasted replies as evidence of undisclosed AI use.
- **Fix / craft move:** Before sending, read the first and last sentence and delete any line that talks to the reader about the writing itself.
- **Source:** [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (opened, partial; "Leaked chatbot replies" and placeholder sections).

### Email-specific tells
- **Tell:** Generic greeting, "I hope this email finds you well", "Please don't hesitate to reach out", a paragraph that restates the email's purpose three ways, and no specific detail about the recipient.
- **Why it reads as AI:** Template language with no relationship detail. The sender could have written it to anyone.
- **Fix / craft move:** Open with the reason you are writing. Include one detail only the sender would know. Cut the "hope this finds you well" line.
- **Source:** Heymarket, [How to spot an AI-generated email](https://www.heymarket.com/blog/identify-ai-generated-emails/), undated (search snippet; marketing blog, moderate reliability). Reply.io, [AI Words in Emails](https://reply.io/blog/ai-words-in-emails/), undated (search snippet).

Gap: no Reddit thread on spotting AI email was found in this pass. Most of the email material above is from marketing blogs. Treat as practitioner opinion, not evidence.

### Reviews, comments and social posts
- **Tell:** Generic praise with no specifics ("Amazing product, highly recommend!"), uniform sentence length, a "hook" line followed by "Here's what I learned:" and a list of lessons, and a closing question designed for engagement ("What do you think?").
- **Why it reads as AI:** Each element is a template slot. Real posts contain a specific event, a number, or an admission of something that did not go well.
- **Fix / craft move:** Anchor the post in one real moment with a specific detail. Drop the "Here's what I learned" framing. Ask a question only when you want a specific answer.
- **Source:** Gap: no primary, dated study on LinkedIn or review AI tells was found in this pass. Only Dev.to (anecdotal, tool-seller) and blog summaries. Mark as unverified.

## Why humans and models diverge (mechanism)

- **Preference training rewards agreeable, fluent, long answers.** Sharma et al. 2023 ([Anthropic](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models)) report that matching a user's views is more likely to be preferred in helpfulness data. Possibly outdated for 2026 model era, but the mechanism is well cited.
- **Social sycophancy is measurable.** ELEPHANT ([arXiv:2505.13995](https://arxiv.org/abs/2505.13995), 2025) finds models over-preserve the user's self-image, especially in advice and moral-judgment prompts.
- **Forced-choice bias persists.** Beacon ([arXiv:2510.16727](https://arxiv.org/abs/2510.16727), Oct 2025) is a single-turn benchmark for the same bias. Seen in search listing only; details not opened.
- **OpenAI's April 2025 GPT-4o rollback.** OpenAI's postmortem on overly flattering behavior was not retrievable (HTTP 403 on fetch). Gap: cite only after opening it.

## Craft principles (beyond "not looking AI")

Pulled from style guides and plain-language practice. Sources are search summaries where noted.

1. **Lead with the answer.** NN/g's UX writing FAQ says the inverted pyramid matters more now: answer first, support after. ([NN/g UX writing FAQ](https://www.nngroup.com/articles/ux-writing-faqs/), search summary; article not opened.)
2. **Write for scanning, then reading.** NN/g reports most users scan rather than read word by word; chunk content and use descriptive subheadings. Figures vary by secondary source; verify on the NN/g site before quoting numbers.
3. **Plain words, jargon in parentheses on first use.** GOV.UK makes plain English mandatory, including for technical audiences, and rejects skipping it for experts. ([GOV.UK clear language guidance](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-language/), search snippet.)
4. **Active voice, second person, conditions before instructions.** Google's developer style guide asks for "you" over "we", active voice, and conditions placed before the instruction. ([Google voice and tone](https://developers.google.com/style/tone), search snippet.)
5. **No "please" padding or "simply/easy".** Google's guide: "To view the document, click View" over "please click". It also discourages "simply" and "easy" in procedures, since a step that is hard for the reader is not made easier by the word.
6. **Write like you'd speak it.** Microsoft's guide advises conversational writing, contractions acceptable, get to the point quickly. ([PerfectIt summary of Microsoft Writing Style Guide](https://www.perfectit.com/blog/five-things-to-check-in-microsoft-style), search snippet; primary page behind sign-in.)
7. **Imagine a knowledgeable friend.** Google's guide frames the target voice as a knowledgeable friend who understands what the reader is trying to do. Pair this with the reader's level: a beginner needs the term defined; an expert needs the point, not the scaffolding.
8. **Test by reading aloud.** Google's guide recommends reading the text aloud and asking what you are actually trying to say. Filler and tells show up fast this way.
9. **Cut before you add.** Microsoft's guide: eliminate extraneous information. GOV.UK: publish only what someone needs to complete their task.
10. **Specific beats general.** Wikipedia's guide: a sign alone is not proof; the combination of puffery, vague attribution and empty significance is what reads as generated. The fix is the concrete fact, number or named source.
11. **Match length and register to the asker.** A short casual question gets a short casual answer. Professional email gets a clear subject line and one ask. Support gets the next step first, then the reason.
12. **Show your confidence once.** A single "I'm fairly sure, I haven't run it" is more useful to a reader than uniform hedging on every sentence.

## Context differences

- **Quick chat:** Short, direct, no headers, no closing menu. One follow-up question at most.
- **Professional email:** Subject line that says what the email is for. First line states the ask or the news. Name one specific detail. Sign off plainly.
- **Customer support:** Acknowledge the specific problem once, give the step that fixes it, say what happens next. No "we understand your frustration" boilerplate.
- **Social post:** One real moment, one specific detail, one point. No "Here's what I learned" list unless the list is the post.
- **README / docs:** Task-first headings, short sentences, imperative steps, conditions before instructions, one example per concept. Use the tone rules above.
- **Explanation / tutorial:** Start from what the reader already knows, add one new idea at a time, show a worked example before the general rule.

## Gaps

- No opened primary source for NN/g, Google's developer guide or GOV.UK page content; statements are from search snippets.
- OpenAI's GPT-4o sycophancy postmortem was not retrievable (HTTP 403).
- No dated, primary research on LinkedIn, review or comment tells was found.
- "I hope this helps" and "menus of follow-up offers" lack an opened primary source.
- Feynman-style teaching guidance and Stripe docs guidance were not searched in this pass.
- Sharma et al. (2023) and Kobak et al. (2024/2025) are older than 2025 for model-era claims; flagged as possibly outdated for current model behavior.
