# Chat tells (dated)

last_verified: 2026-10-22 for word lists (owner's `ai-auditor` list). Structure section cross-checked against `research_notes/` on 2026-11-17.
Re-check: word and punctuation tells monthly, structure tells every 6 months, everything after a major model release.

A tell is a reason to rework the reply. It is never proof of who or what wrote it. One tell means nothing; several kinds together mean the reply is running on defaults.

## Structure (strongest, slowest to expire)

| Tell | Fix |
|---|---|
| Praise or "You're absolutely right" before any content | Delete it. Start with the answer, or with the specific thing you noticed |
| Restating the question, or announcing the plan ("Let's break this down", "Here's a step-by-step") | Start on the first step or the answer |
| Praise sandwich: compliment, critique, compliment | Lead with the biggest problem and the fix. Keep praise only if specific and true |
| Reversing a correct answer after pushback ("You're right, I apologize") | Re-check. If it held, say "I checked, it holds, here is why". If wrong, name the error once |
| No checkable specifics: no number, name, example or line pointed at | Add a real one from the user's message, or ask for it |
| Bullets and bold labels on a short answer ("**Key takeaways:**", "**Pros:**") | Prose. One list only if the items are truly parallel |
| Headings in a reply under about 300 words | Remove them |
| "It's not X, it's Y"; triplets on every list | State Y. Give the real count of items |
| Closing recap, "I hope this helps", or a menu of offers | End when the content ends. One concrete next step at most |
| Hedge on every line ("may potentially", "it depends" with no follow-through) | Say your confidence once, with the reason. Then commit |
| Over-apology ("I apologize for any confusion") | Apologize only for a real error, in one clause, then fix it |
| Analogy that would fit any topic | Replace with one from this topic's mechanism, or drop it |
| Explanation with steps and no reason, or a rule with no worked example | Add the why. Put one example with numbers first |
| "Studies show", "experts say" with no name | Name the source or drop the claim |

## Words and punctuation (expire fast)

Count these only in clusters of three or more.

- **Chat openers:** "Great question", "Absolutely!", "Certainly!", "That's a fascinating idea", "What a great".
- **Plan announcements:** "Let's break this down", "Let's dive in", "Here's a breakdown".
- **Stock phrases:** "it's important to note", "it's worth mentioning", "when it comes to", "at the end of the day".
- **Current words:** crucial, pivotal, significant, seamless, robust, underscore, leverage, landscape (abstract use).
- **Newer, Claude-leaning (weak):** genuinely, quietly, honestly, load-bearing, "doing real work", "stated plainly".
- **Expired (do not use as a signal):** delve, tapestry, intricate, showcasing.
- **Em dashes:** about 3 per 1,000 words or more is a reason to re-read. Weak alone; humans use them. Use a full stop or comma.
- **Exclamation marks and emoji:** one in a casual reply is fine. A string of them in advice or feedback reads as performed warmth.

## Guards

- Formal, simple or non-native English is not a tell. Lower confidence for these.
- A quote, a title, or a reply that discusses a phrase is exempt.
- A user who asks for warmth, emoji, a list or a long answer gets it. Their request overrides style tells.
- Support and customer chat may need one acknowledgement of the problem. One, not a paragraph.
- The tells "I hope this helps" and menus of follow-up offers are widely reported but have no opened primary source in `research_notes/`. Treat as unverified common patterns.
- Judge the reply, never the writer. People score near chance at spotting AI text by feel.
- English lists do not transfer to other languages.

## Sources

Owner's `ai-auditor` list (2026-10-22). Sharma et al., Anthropic, Oct 2023 (models drift toward agreeing with users; possibly outdated for current models). ELEPHANT benchmark, arXiv:2505.13995, v2 Sep 2025 (11 models preserved user "face" about 45 percentage points more than humans). Wikipedia "Signs of AI writing" (opened, partial). Kobak et al., Science Advances, July 2025 (excess vocabulary in PubMed abstracts). Notes with caveats: `research_notes/AI tells and craft across media/chat_explanations.md`.
