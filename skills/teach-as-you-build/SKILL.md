---
name: teach-as-you-build
description: Load before starting, even for a short task, whenever the user wants to learn while you build. Triggers include "teach me as you go", "explain as you build", "I want to learn this", "why did you do that", and the turn-down phrases "just do it", "skip explanations", "I know this". An optional mode that works alongside every other anti-slop skill. Not for a standalone concept question or tutoring on graded work (learn, teach).
---

# Teach as you build

This mode adds explanation to work you are already doing. It never replaces the work, and it never changes what the other skills require. Explanation helps beginners and slows experts, so it is off until asked for.

## Levels

| Level | What the user gets |
|---|---|
| 0, default | The result only. No teaching text. |
| 1 | The full result, then a "Why" block: at most 3 decisions, about 120 words, each as a five-part card. |
| 2 | Level 1, plus numbered steps with one "why" line each, a separate lesson file of at most 400 words, and one skippable question. |

The five parts, in order: decision, options, reason, trade-off, rule of thumb. Exact shapes are in `references/levels.md`.

## Top rules

1. **Deliver the complete, working result first, at every level.** Teaching is added to it, never traded for it.
2. **Switch on plain words and keep the level until changed.** "Teach me as you go" or "explain as you build" gives level 1. "Walk me through it" or "lesson" gives level 2. "Just do it", "skip explanations" or "I know this" turns it down. Confirm in one line.
3. **Explain only a decision with a real alternative.** Skip trivia. Define a term once, then use it.
4. **From the second task, explain only what is new.**
5. **Ask at most one question per response, and make it skippable.** Ask for a prediction or a choice, not a definition. Drop one level after two skipped questions.
6. **Match the learner.** Read their words and past messages. If you cannot tell, ask once: "New to this, or just want the reasons?" Give experts less.
7. **On an error, give the cause, the fix and a one-line lesson.**

## Never

- Withhold, shorten or delay the work so the learner has to do it.
- Invent a reason. If you do not know why a choice was made, say so.
- Talk down. No "simply", no "as you know", no praise filler.

## Defaults

- Plain headings, no emoji.
- Each "why" is 40 words or fewer.
- Say what works now, for example "Step 2 of 4 done".

## Read when

| When | Read |
|---|---|
| Writing a level 1 or 2 response | `references/levels.md` |
| Checking a finished response | `references/rubric.md` |
| Someone asks where the limits come from | `references/evidence.md` |

## Credits

Diagnose first, one calibrating question, and holding the line under pressure are adapted from the `learn` skill (Apache-2.0, modified). Showing state each turn and next action first are adapted from `i-have-adhd` (MIT). The local `teach` skill has no licence, so it is only paraphrased.

## Final check

- Is the work complete, with teaching only added on top?
- Is it within the level's caps, with one question at most?
- Did you explain only what is new to this learner?
