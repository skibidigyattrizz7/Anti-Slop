---
name: human-writing
description: Use for any prose writing or editing task, even a short one, before drafting or rewriting. Covers essays, articles, blog posts, newsletters, captions, emails, product and marketing copy, summaries and scripts, and requests like "rewrite this", "edit this", "tighten this", "make this sound natural" or "this sounds robotic". Not for chat replies (human-chat), stories (human-fiction), writing in the user's own voice (own-voice), UI text (human-ui) or research with citations (real-reports).
---

# Human Writing

A model picks the most likely next phrase, so its prose drifts to the average: safe words, even rhythm, nothing a reader could check. A skilled writer chooses for one reader.

## Top rules

1. **Write the point in one sentence before drafting.** If you can't, ask what the piece is for.
2. **Put a checkable specific in every paragraph, from what you were given.** A name, number, date or place, from the user or a source you opened. State each fact once, in the words given (bent stays bent). When one is missing, ask for it or leave `[detail needed: ...]`.
3. **Open on the point and end on something new.** The last sentence adds a detail, a consequence or a decision. Land within about 20 percent of the asked length. If the facts cannot fill it, ask for more.
4. **State only what is true.** Write "Y". Leave out the "not X" half, whether it comes first ("it's not X, it's Y") or last ("Y, not X"). Name who acts: "we decided".
5. **Vary rhythm on purpose.** Mix short and long sentences and uneven paragraphs. Use the real count in lists.
6. **Use the plain word and take a view.** "Use", "help", "said". Give your view where the genre allows. State real doubt once.
7. **Format for where it will be read.** Prose by default, lists for real lists, markdown only where it renders.

## Never

No brief overrides these.

- Invent a fact, quote, statistic, source or personal detail.
- Fix a flagged word by swapping in a synonym. Rewrite the sentence.
- Tune text to beat an AI detector, or disguise AI writing where AI is not allowed.

## Defaults

A brief or the user's writing sample overrides these.

- At most about 3 em dashes per 1,000 words.
- Sentence-case headings, and bold only for terms the reader must find again.

## Read when

| When | Read |
|---|---|
| Rewriting or editing text that already exists | `references/rewrite.md` |
| Scanning a draft for tells | `references/tells.md` |
| Fixing one pattern: staging, rhythm, inflation, formatting, chat leftovers, wrong reader | the matching `references/patterns-*.md` |
| Marketing, product, email, academic or explainer copy | `references/craft.md` |
| Checking a finished piece | `references/rubric.md` |
| You can run code | `python3 scripts/count_tells.py FILE` |

## Before and after

**Before:** "Supercharge your workflow with our seamless, all-in-one invoicing platform."

**After:** "Tracks every invoice and emails you the day one is 7 days late."

**Before:** "Photosynthesis is a fascinating and crucial process that plays a vital role in sustaining life on Earth."

**After:** "Plants make their own food from sunlight. Oxygen is the leftover, and it happens to be what we breathe."

## Final check

- Can you state the point in one sentence?
- Does every paragraph hold a checkable specific that came from the user or a source?
- Does the last paragraph add anything new? If not, cut it.
