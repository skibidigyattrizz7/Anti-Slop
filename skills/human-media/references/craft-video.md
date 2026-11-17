# Video and motion craft

Evidence is thin. The one study found, Physion-Eval (arXiv, 2026-03-20), reports at least one human-visible physics glitch in 83.3% of exocentric and 93.5% of egocentric physics-critical videos across five unnamed models. Most other claims are vendor blogs. Treat them as advice.

## Plan before you generate

- **Storyboard first.** One sentence per shot, each with a purpose. Google's Veo 3.1 guide (2025-10-16) orders a prompt as cinematography, subject, action, context, style.
- **Short shots, one subject, one action.** Build scenes in the edit, not in the generator.
- **Reference frames.** One locked still per character and per place, used as the start frame.
- **Fewer, longer shots** reduce identity drift. Avoid cutting between two generations of one person unless a reaction motivates it.

## Camera

- Give every shot a reason: a dolly that follows a reveal, a static hold for a reaction, handheld for tension.
- Vary move type and speed across the cut. Hold still when there is nothing to reveal.
- Vocabulary that works: dolly, tracking, crane, slow pan, POV; wide, close-up, low angle; shallow depth of field, rack focus.

## What still breaks (2026, secondary sources)

- Hands, small-object handling, liquids, cloth, state changes mid-shot. Keep these brief and wide, or cut before the grip resolves.
- Text in frame. Add titles and signs in an editor, in a real font.
- Faces in close-up. Use medium or wide, or keep the face off screen. Record the voice first and cut to reactions.
- Identity across shots and sequences over about 20 s. A 70 to 80% consistency figure comes from one secondary blog and is unverified, so it is left out.
- Model rankings conflict across blogs and versions. Check the version before quoting one.

## Editing

- **Edit in a real editor.** Titles, captions, retimes and grade belong outside the generator.
- **Grade all clips together.** One LUT, one black level, one white point. Clips of 4 to 8 s have separate exposure and look like splices.
- **Cut on motion or on a reaction.** Emotion decides the cut first (Walter Murch's Rule of Six: emotion, story, rhythm, eye trace, 2D plane, 3D space). The percentage weights often quoted are from secondary blogs, so ignore them.
- **Let the key detail land, then cut.**
- **Sound bridges cuts.** An L-cut or J-cut carries the viewer across. Run one continuous audio bed under the joins.
- **Retime in the editor** if motion feels off. Keep motion blur consistent.
- **Mix real and generated.** Shoot or source the specific objects and places the story needs. Beauty establishing shots with no subject read as stock.
- **Short form:** lead with the most specific image or claim, not a logo. This is practice, not a sourced rule.

## Motion design and UI animation

- Give each motion a job: entrance for new content, feedback for a tap, exit for dismiss.
- Vary duration by distance and importance. UI motion often sits roughly 200 to 500 ms (secondary source).
- Do not fade up everything on scroll or use one spring everywhere. Overshoot for a settle on success; firm, no overshoot for errors.
- Slow in, slow out. Add anticipation before a big start and follow-through after a stop (Thomas and Johnston, *The Illusion of Life*, 1981). For game effects timing see human-games.

## Longer before and after

**Before:** "Cinematic slow-motion shot of a chef cooking, 4K, epic."

**After shot list (20 s):**
1. Wide, static, 3 s: a kitchen at 6 a.m., one chef, window light from the right.
2. Insert, 2 s: hands cracking an egg (real footage, not generated).
3. Medium, handheld, 4 s: she tastes, looks off frame left.
4. Generated, 3 s: steam over a pan, no hands, no text.
5. Close on the plate, rack focus, 3 s.
Voiceover recorded first. Titles added in the editor. One grade across all five.

## Check without watching

You cannot watch the video. Read the shot list and prompts, and ask the user to check motion, faces and audio sync.
