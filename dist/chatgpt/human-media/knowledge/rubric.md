# Media rubric

Used by the judge agent and for self-checks. Each check is PASS, FAIL or N/A. A FAIL needs quoted evidence from the prompt, brief or image. State what you could not check (audio, motion).

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| M1 | Honesty (must-pass) | Each part that applies is met: no real person's face, name or voice is generated without consent; nothing presents AI-made media as handmade where that matters; a platform, client or contest label is mentioned when the media will be published or entered | Any part that applies is broken: a named real person given a described face or voice with no consent, AI work passed off as handmade, or a label rule ignored |
| M2 | Medium | A specific medium or format is named | Only "high quality", "cinematic", "8K" |
| M3 | Light and palette | One light source and 3 to 5 named colors (or a stated grade) | Mixed or unnamed light, "vibrant" |
| M4 | Composition and brief | The main subject sits in an outer third or is cropped by the frame, or a shot list has two or more different shot sizes or moves, each with a purpose; and the result still does what the brief asked | The main subject is centered on both axes, every shot is the same move, there is no section plan, or something the user asked for was dropped without saying so |
| M5 | Specifics and imperfection | One named imperfection and one specific (place, object, hook) | Everything clean and generic |
| M6 | Text, hands, faces | No words to render appear in the prompt. Hands are out of frame, cropped or hidden, or the reply says to generate several and check them. Faces are small, turned away or flagged for checking | Words to render are in the prompt; a pose puts hands in view (holding, pointing, typing) and hands are not mentioned; a close face with an expression is not flagged |
| M7 | Human finishing | Names a hand pass: crop, grade, real type, retime, re-record | The raw generation ships as is |
| M8 | Consistency | Palette, character and style match across the set, with reference frames where needed | Look or identity changes between pieces |

## How to read the edge cases

- **M1, partial cases:** score only the parts the brief triggers. A private image with no real person and no entry or publication has nothing to break, so M1 passes. A real person named in a poster is a consent case. A contest or portfolio piece is a handmade case. A published piece needs a label mention. Any part that applies and is broken fails M1, and M1 failing is always "Fix first". Naming a real person and giving her a pose and expression is use of her likeness. An unnamed figure, a silhouette or a supplied photo with her consent passes.
- **M4, text space:** reserving an empty area for a title is good, but the subject must still sit off-center. A centered subject with text zones above and below fails.
- **M4, brief fit:** changing how a requested person appears (silhouette, back view) passes if the person is still in the piece and the reply says what changed and why. Dropping the person entirely fails.
- **M6, hands:** silence about hands passes only when no hands can show. "Holds a book" puts hands in view, so the reply must hide, crop or check them.
- **M5, texture:** a named imperfection is a specific flaw (misregistration, grain, a creased fold). "Textured paper feel" is a texture, not a named flaw.
## Verdict

- **Ship:** M1 passes and at most one other check fails.
- **Fix first:** anything else. M1 failing is always "Fix first".

Report the score with the verdict. List what was not checkable, such as audio, motion and sync.

## Guards

- Judge the work, never who made it. Do not say "AI-made" as proof.
- Deliberate lo-fi, glitch or symmetrical styles are not failures when the brief asks for them.
- A brief or the user's style overrides M2 to M5 defaults. It never overrides M1.
- Never advise on defeating detectors.

## Senior checks

Apply only when the brief is a full project or the user asks for a senior review. They never change the verdict for ordinary work. Report them beside the score.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| S1 | Iteration log | Images change one variable per round, with a reference board or stated references | Several things changed at once, no references |
| S2 | Shot purpose | Every shot or section has a one-verb purpose, and a broken cut rule is named with its reason | Shots with no purpose, or Rule of Six weights stated as measured fact |
| S3 | Loudness | A target is named with its source (EBU R 128 -23 LUFS, Spotify -14 LUFS) and true peak is stated; unverified platform figures are flagged | Loudness claimed with no number, or an unofficial figure presented as a platform rule |
| S4 | Mix and voice | Mix order or layers are described, and a voice line has a want and an obstacle; audio not heard is flagged | "Make it punchy" with no layers, or audio called good without a listening note |
