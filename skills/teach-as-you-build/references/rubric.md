# Teaching rubric

Used by the judge agent and for self-checks. Each check is PASS, FAIL or N/A. A FAIL needs a quoted line as evidence. Check in this order, every time. Judge the response at the level the user asked for.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| T1 | Work complete (must pass) | The full result is delivered and works, and nothing was left for the learner to finish | Any part is missing, shortened, deferred or turned into an exercise |
| T2 | Level obeyed | Level 0 has no teaching text. Level 1 has a Why block. Level 2 has steps, a lesson file and the question | Teaching text at level 0, a missing block at the asked level, or a level the user did not ask for |
| T3 | Caps | At most 3 decisions, about 120 words at level 1, each why 40 words or fewer, lesson file 400 words or fewer | Any cap is clearly broken, or a level 1 block runs past about 150 words |
| T4 | Card form | Each decision has decision, options, reason, trade-off and rule of thumb, or says why the last is left out | A card has no real alternative, no trade-off, or is a bare fact |
| T5 | Only what matters | Each explained decision had a real alternative, and a repeat task explains only what is new | Trivia is explained, or an earlier card is repeated |
| T6 | One question | At most one question, skippable, asking for a prediction or choice. Not asked again after a skip | Two or more questions, a question that blocks the work, or a repeated skipped question |
| T7 | True and kind | Every reason is correct for this work, with no invented rationale, and the tone is plain | A false or made-up reason, "simply", "as you know", praise filler, or emoji |
| T8 | Fits the learner | Depth matches the learner's words, and drops after "I know this" or two skips | A beginner gets jargon undefined, or an expert gets a lecture |

## How to read the edge cases

- **T1, a lesson file:** the lesson file is extra. If the learner's deliverable is missing from the reply, T1 fails even when the lesson is good.
- **T3, the question:** the question is not counted in the word caps, but T6 limits it.
- **T4, rule of thumb:** may be left out when it does not transfer. The reason for leaving it out is one clause.
- **T5, first task:** the first task in a session may explain a decision the learner has not met. That is new, so it passes.
- **T8, no level cues:** with no cues, one calibrating question counts as a pass, and it must still come with the work.

## Verdict

- **Ship:** T1 passes and at most one other check fails.
- **Fix first:** anything else. T1 failing is always "Fix first".

Score is passes out of applicable checks. Report the score with the verdict, never alone.

## Guards

- Judge the response, never the learner.
- A user who asked for level 0 and got a bare result passes. Silence is not a failure.
- The user's explicit request for more or less overrides the caps in T3, never T1 or T7.
