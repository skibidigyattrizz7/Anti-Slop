# Fiction rubric

Used by the judge agent and for self-checks. Each check is PASS, FAIL or N/A. A FAIL needs a quoted line as evidence. Check in this order, every time.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| F1 | Fidelity | Every fact from the brief is kept (counts, ages, times, places, roles, what is owed), shown or stated, the length is within 10% of the ask, and nothing is presented as real that the brief did not give | A real fact, quote, source or event is invented, a brief fact is changed or dropped, or the length is over 10% off (must-pass) |
| F2 | Specific start | It opens on a concrete thing or scene, with names and places chosen for the setting | Weather, a sky or light described as if it has moods, "in a small town", or a stock name, job or place leads |
| F3 | Wants and cost | At least two characters want conflicting things and a choice costs someone | No conflict, or the hero is plainly right and nothing is lost |
| F4 | Dialogue | Lines want, dodge or interrupt, and speakers are not interchangeable | Speeches explain plot or theme, or all speakers sound alike |
| F5 | Subtext | Theme and feelings are carried by action or detail, with some feelings named plainly. Narration that adds something new passes | A line states the lesson, or narration or interior thought restates a feeling a line or detail already showed ("she could see him knowing it"), or every emotion is a body sensation |
| F6 | Shape | A second thread, time jump or escalation changes what is at stake by the last third (a deadline, an offer, a new person who wants something) | One flat line at one pitch, or the extra material is only background (noise, weather, bystanders) |
| F7 | Ending | It ends unresolved on a concrete pending act or object (a pen over a signature line), or ironic, or with a consequence | Quiet acceptance, a realization, a tidy moral, or it ends on stasis or mood ("neither of them moved", grey light) |
| F8 | Phrases | No stock phrases or triplet habit (list in `tells.md`); script shows no clusters | Any stock phrase, or 3+ stock-name or body-sensation hits |

For games and NPCs, F4 means short in-character lines and F6 means the player's choice changes something visible. For poems, F2 to F5 apply to images and the last stanza; F3, F4 and F6 are N/A.

## How to read the edge cases

- **F1, facts and shown details:** a detail from the brief counts as kept if a reader can tell it from the page. Age shown by a concrete detail ("pencil behind his ear since before the girl was born", "thirty years on this gate") passes only if the number is clear. A bare name with no hint of 52 fails. An implied time (5 a.m. by dark yard and a 6 o'clock deadline) passes.
- **F1, length:** count the words. Within 10% either way passes (360 to 440 for a 400 ask). A character, place or event the writer invents inside the story is fine; presented as real, it fails.
- **F2, openers:** a concrete image first, then sky or light, passes. Sky or dawn with a mood or decision ("had not decided what colour") leading fails.
- **F5, narration:** quote the narration and the line it repeats. Narration that gives new information ("the old voice... did not arrive") passes. A line that explains the shoulders just shown fails. Interior thought that only names a detail without using it ("thought of her daughter's school fees, did not say it") is a fail when the detail never reaches the page as speech or action.
- **F6, bystanders:** a conductor or horn that only reacts is texture. It passes if it changes what a character does or risks.
- **F7, open endings:** open is not enough. The ending has to leave something concrete pending.

## Verdict

- **Ship:** F1 passes and at most one other check fails.
- **Fix first:** anything else. F1 failing is always "Fix first".

Report the score (passes out of applicable checks) with the verdict, never alone. Top fixes go in order of check ID.

## Guards

- Judge the text, never who or what wrote it. Do not say "AI-written" or "proves".
- Script counts are evidence only. A stock name inside a parody or a quotation is exempt.
- A brief or the user's own style can override F2 (e.g. a requested setting) and F7 (a requested happy ending). It never overrides F1.
- Genre convention is not a fail: a lighthouse in a lighthouse-themed brief is fine.

## Senior checks

Apply only when the brief is a full project or the user asks for a senior review. They never change the verdict rule for ordinary work. Sourcing is thin, so treat a miss as a prompt to look, not proof.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| S1 | Distance | Distance fits the scene and holds within a paragraph unless the shift is deliberate | An unmotivated jump between far and close in one paragraph |
| S2 | Scene function | Each scene has a goal, opposition and a change, or is a sequel ending in a decision | A scene where nothing is wanted, opposed or changed |
| S3 | Want and need | The lead's want and need can be stated and differ, and the want costs something | They are the same, or no cost lands |
| S4 | Subtext | At least one spoken line differs from what the speaker wants, and no line explains it | Every line says what the speaker feels |
| S5 | Revision | Passes were run in order (structure, want, dialogue, distance, rhythm, cut, proof) | Tells were polished before the shape was fixed |
