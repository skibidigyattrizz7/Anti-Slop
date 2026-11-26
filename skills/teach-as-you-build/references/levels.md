# Levels: exact output shapes

Level 0 adds nothing. Everything below sits after the finished work, never in place of it.

## Level 1: Why block

Heading `Why`. At most 3 cards, about 120 words in all. Each card is five short parts in this order. Drop the rule of thumb only if it does not transfer to other work.

```
Why

1. Decision: <what you chose>.
   Options: <the other real candidates>.
   Reason: <why this one, here>.
   Trade-off: <what it costs>.
   Rule of thumb: <the general test>.
```

Code gets a one-line comment only where a choice is not obvious.

### Example, code

Task: a function that removes duplicate emails from a list.

Why

1. Decision: used a set to track seen addresses.
   Options: a nested loop, or sorting first.
   Reason: a set lookup does not slow down as the list grows.
   Trade-off: it uses extra memory and needs hashable items.
   Rule of thumb: need "have I seen this?" fast, reach for a set.

### Example, UI or writing

Task: a pricing section for a small app.

Why

1. Decision: put the price in the heading.
   Options: a "See pricing" button, or a table.
   Reason: visitors came to find the number, so it is the first thing they read.
   Trade-off: it leaves less room for selling the features above it.
   Rule of thumb: put the answer to the reader's question where they look first.

## Level 2: lesson

Everything in level 1, plus these, in this order.

1. First line: what the learner now has, and the next action.
2. Up to 5 numbered steps. Each is one action and one "why" line of 40 words or fewer.
3. A pointer to the closest real file or screen as a worked example.
4. A separate file, `lesson.md`, at most 400 words: the 3 to 5 decisions in full five-part form, then a "Try it" step.
5. One optional question at the end, marked skippable.

Never ask the learner to do a step before you have delivered the result.

### Example, code

Task: the same email function.

You now have `dedupe_emails()` and it passes the 3 tests. Next: run `python test_emails.py`.

1. Lowercase each address before checking it. Why: `A@x.com` and `a@x.com` are the same inbox.
2. Keep a set of seen addresses. Why: set lookups stay fast on long lists.
3. Append only unseen ones to the output. Why: this keeps the original order.

Closest example: `utils/strings.py`, `unique_words()`.
Full cards are in `lesson.md`.
Optional: what should happen to `"a@x.com "` with a trailing space? Skip if you like.

### Example, UI or writing

Task: a two-paragraph product update for a newsletter.

You now have the draft below. Next: check the date in paragraph 1.

1. Lead with what changed. Why: readers decide in the first line whether it affects them.
2. Give the date once. Why: a repeated date reads as padding and can drift out of sync.
3. End on what to do. Why: a next step is the one thing the reader cannot guess.

Optional: which line would you cut first if it had to be half as long? Skip if you like.

## Errors

Cause, fix, one-line lesson. Example: "The test failed because the list was empty. I added a guard. Lesson: check the empty case first."

## Credits

The apprenticeship order of show, then fade, and the diagnose-first habit follow the `learn` skill (Apache-2.0, modified). "Step 2 of 4 done" and next action first follow `i-have-adhd` (MIT).
