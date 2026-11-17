# Image craft

Covers photo-style images, illustration, thumbnails and logos. Evidence is mostly practitioner and vendor guides (2026); treat it as advice.

## Prompt like a photo being taken or a thing being made

- Use lens, light, framing and material words. They steer better than "8K" or "ultra-detailed".
- Order: scene, subject, key details, then constraints. State the use (poster, thumbnail, UI mock) to set the polish level.
- One style per prompt. "Photorealistic cartoon" gives two conflicting targets.
- Fill in `prompt-brief.md` first.

## Light, color, composition

- **One light.** "Soft window light from the left." Check eye reflections and shadows against it.
- **Named palette.** Three to five exact colors with one accent. "Vibrant" gives the default grade. Teal and orange is a real film convention; the overuse is the tell.
- **Off center.** Name the framing, viewpoint and which side holds negative space. Add one deliberate asymmetry.
- **Value first.** Check the image in greyscale. A clear light, mid and dark structure holds even when color fails.
- **Thumbnail test.** Shrink it. Is the silhouette or the one key trait still readable?

## Texture and wear

- Name real texture: pores, fabric weave, wood grain, dust, scratches.
- Give one object a history: a dent, a mismatched part, a worn edge.
- Sharpen selectively. Global sharpening makes every edge equally hard.

## Hands, faces, text, backgrounds

- **Hands:** choose poses that hide them (pocket, one object, cropped). Inpaint the rest. They are less often wrong than before and still checked by hand.
- **Faces:** inpaint at higher detail. Check eye line against head angle. Use a character reference across a set.
- **Text:** short requested headlines are now often right on some models. Incidental text (signs, spines, labels) is still weak. Keep it out of frame, and set real type afterward.
- **Backgrounds:** simplify or defocus. Windows onto nothing and geometry that does not close give it away.
- **Repeats:** vary crowds, shelves and tiles on purpose.

## Workflow

- One change per edit: "change only X, keep everything else the same". Repeat the preserve list each round.
- Fix locally. Inpaint the broken region, not the whole frame.
- Use reference images for pose, palette and character.
- Mix in a real photo for light and texture where you can.
- Final human pass: crop, levels, grain, paint over problems. This is the biggest jump in quality.
- Keep a set consistent: same palette and style.

## Logos and brand marks

- Generators give pixels. A mark must work from 16 px to a billboard, so redraw it as flat vector.
- Test at favicon size and in one color. Effects (gloss, bevel, gradient) baked in the pixels fail this.
- Output draws on common icons and layouts, so it is hard to own or trademark. Start from one sentence ("what this brand does that no one else does"), sketch 20 thumbnails, pick one and draw it.
- Some tools claim SVG export. Critics report broken files, so open and check it.

## Provenance and rules

- Some commissioners ban gen-AI art outright (Hooded Horse, Kotaku, 2026-01-08). Ask before delivering AI art to a client or contest.
- The US Copyright Office reportedly protects AI output only where a human supplied enough expression. That is a search-snippet claim, so check it before relying on it.
- Tell the user to disclose AI use where a platform, client or contest requires it.

## Longer before and after

**Before (thumbnail for a cooking video):** "Amazing delicious pasta, vibrant colors, cinematic, 8K, text: BEST PASTA EVER."

**After:** "Overhead photo, one window light from the left, a pot of pasta on a scratched steel counter, wooden spoon half in frame, slight steam blur. Palette: cream, tomato red, steel grey. Subject in the lower right, empty space left for a title. No text in the image."

Then: generate four, pick one, crop tighter, lower saturation, add the title in a real bold font, shrink to 200 px and check it reads.
