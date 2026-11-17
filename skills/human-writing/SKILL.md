---
name: human-writing
description: Use when writing, rewriting or editing prose, such as essays, articles, posts, captions, emails, product or marketing copy, summaries and scripts. Also use when the user says text sounds robotic, generic, stiff or "like AI", or asks to make it sound human or natural. Not for chat replies (human-chat), stories (human-fiction) or pieces in the user's own voice (own-voice).
---

# Human Writing

A model picks the most likely next phrase, so its prose drifts to the average: safe words, even rhythm, nothing a reader could check. A skilled writer chooses for one reader and one subject. Make those choices. Swapping a flagged word for its synonym only moves the text to the next default.

## Top rules

1. **Write the point in one sentence before drafting.** If you can't, ask what the piece is for.
2. **Put a checkable specific in every paragraph.** A name, number, date, place or real example, taken from the user or from a source you opened. When one is missing, ask for it or leave `[detail needed: ...]`.
3. **Open on the point and stop when it is made.** The first sentence carries content. The last one adds a detail, a consequence or a decision.
4. **State only what is true.** Write "Y". Leave out the "not X" half, whether it comes first ("it's not X, it's Y") or last ("Y, not X"). Name who acts: "we decided".
5. **Vary rhythm on purpose.** Mix short and long sentences and uneven paragraphs. List one item, two or four when the content has that many.
6. **Use the plain word and take a view.** "Use", "help", "said". Say what you think where the genre allows, and state real uncertainty once.
7. **Format for where it will be read.** Prose by default, lists for real lists, markdown only where it renders.

## Never

The brief cannot override these.

- Invent a fact, quote, statistic, source or personal detail.
- Fix a flagged word by swapping in a synonym. Rewrite the sentence.
- Tune text to beat an AI detector, or disguise AI writing where AI is not allowed.

## Defaults

A brief or the user's writing sample overrides these.

- At most about 3 em dashes per 1,000 words.
- Sentence-case headings, and bold only for terms the reader must find again.
- Rewrite sentences where the dated words in `references/tells.md` cluster.

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
- Does every paragraph hold a specific the reader could check, and did all of them come from the user or a source?
- Does the last paragraph add anything new? If not, cut it.
