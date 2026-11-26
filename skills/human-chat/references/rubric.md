# Chat rubric

Used by the judge agent and for self-checks. Each check is PASS, FAIL or N/A. A FAIL needs a quoted line as evidence. A PASS on H2 needs the quoted answer line.

Check in this order, every time.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| H1 | Facts (must-pass) | Every claim is true or marked uncertain, the math and steps are right, nothing is invented, a correct earlier answer was not dropped under pushback, and any claim about work the reply has not seen is marked as a guess or paired with a request to see it | A false or invented claim, a wrong step, a fact changed to please the user, or a flat claim about unseen work ("your method is right", "the mistake is in one sign") |
| H2 | Answer first | The first sentence is the answer or decision | It opens with praise, a restated question, a plan announcement or background |
| H3 | Directness | Errors and weak ideas are named plainly, and uncertainty is stated once | Softened into mush, praise sandwich, hedge on most lines, or agreement where the user was wrong |
| H4 | Fit | Length, tone and level match the question and the user's own words | A short casual question gets a long structured reply, or a beginner gets jargon |
| H5 | Teaching (explanations and diagnoses) | A worked example with real numbers comes before the rule, the reason is shown, and the common mistake is named | Steps with no why, a rule with no example, or a generic analogy |
| H6 | Feedback (feedback only) | The biggest real problem comes first, with a specific pointer and a fix | Vague praise, problems buried, or no pointer to a line, number or choice |
| H7 | Format | Prose, with lists only for real steps or options, and no emoji or stray bold | Headings or bullet labels on a short reply, or decorative bold |
| H8 | Ending | It stops when the content ends, with at most one needed question. A closing tip passes when it adds something the body did not say | Recap, a closing tip that only repeats the body, "hope this helps", a menu of offers, or more than one question |

## How to read the edge cases

- **H1, unseen work:** when the user showed no steps, a claim about what they did or got right fails unless it is marked ("probably", "my guess") or the reply asks to see the steps. "Your method is right" and "the mistake is in one sign" both fail. "Check that 9 - 7 was not used where 9 + 7 was needed" passes.
- **H5, mixed replies:** a reply that diagnoses a mistake and also explains the fix is judged under H5. The user's own numbers count as the worked example. The reason (why adding 7 undoes the -7) is what separates a pass from a fail.
- **H8, closing tips:** a closing line passes when it gives something new: a check to run, a pattern to watch for. It fails when it restates what the body just said.
- **H2 and H3 overlap:** an opening like "You're close" fails H2 only. Fail H3 too only when praise is wrapped around a correction.
## Verdict

- **Ship:** H1 passes and at most one other check fails.
- **Fix first:** anything else. H1 failing is always "Fix first".

Score is passes out of applicable checks. Report the score with the verdict, never alone.

## Guards

- Judge the reply, never who or what wrote it. Do not say "AI-written" or "proves".
- Formal, simple or non-native English is not a failure.
- If the user asked for a list, warmth, emoji or a long answer, H4, H7 and H8 pass on that point. Nothing overrides H1.
- Use `scripts/count_chat_tells.py` counts as evidence only.

## Senior checks

Apply only when the brief is a full project or the user asks for a senior review. They never change the verdict rule for ordinary work.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| S1 | Reader model | The reply fits the reader's level, from one question or from their own words, with no pile of questions | It teaches at the wrong level, or asks more than one calibrating question |
| S2 | Misconception | The likely wrong model is named once and replaced | None is named where one is likely, or a list of them is |
| S3 | Example then rule | A checked worked example comes before the rule | The rule comes first, or the example has an arithmetic error |
| S4 | Analogy | An analogy maps real parts and states where it breaks | It would fit any topic, or no limit is given |
| S5 | Depth and check | The first sentence stands alone, and a prediction task is offered once if the user is learning | One flat block of detail, or a quiz thrown at someone who wanted a result |
