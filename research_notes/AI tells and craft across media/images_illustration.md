# AI-made images: tells, fixes and craft (illustration, photo-style, logos, concept art)

Scope: craft quality only. Detector internals are excluded. Dates are as stated by each source; "possibly outdated" marks pre-2025 material. Most 2026 sources are vendor or agency blogs with no benchmarks, so treat their claims as practitioner opinion.

## Tells

**Tell:** Plastic, over-smoothed skin with no pores, blemishes or hair detail.
**Why it reads as AI:** The model averages skin toward a clean, retouched surface, so texture is absent.
**Fix / craft move:** Ask for real texture by name (pores, wrinkles, fabric wear). Avoid "studio polish" and "staging" wording. Add detail in a regional pass rather than the whole frame.
**Source:** [Upsampler, 2026-03-20](https://upsampler.com/blog/make-ai-images-look-real) (lists it as a current tell); [OpenAI cookbook, gpt-image-1.5 guide, undated, marked archived](https://developers.openai.com/cookbook/examples/multimodal/image-gen-1.5-prompting_guide) (recommends explicit texture wording). Improvement claim: [PicassoIA, 2026-06-14](https://blog.picassoia.com/how-ai-image-models-have-changed-in-2026) says 2026 top models render convincing skin, but it is a vendor piece with no benchmark. Status: improved on top models, not solved.

**Tell:** Hands with extra, fused or mis-jointed fingers; thumbs on the wrong side.
**Why it reads as AI:** Hands are many small, occluded, high-variance shapes, and the model has to get all of them right at once.
**Fix / craft move:** Inpaint or regenerate the hands. Pick poses that hide hands (pockets, one hand holding one object, cropped out). Use a reference photo of the pose.
**Source:** [Upsampler, 2026-03-20](https://upsampler.com/blog/make-ai-images-look-real). Status is contested: other 2026 guides say hands are now usually correct, and the PicassoIA piece does not discuss hands. Treat as "less reliable than before, still checked by hand."

**Tell:** Garbled or misspelled text, especially incidental text on signs, labels, book spines.
**Why it reads as AI:** Text is rendered as shapes, not as glyphs, unless the model was trained for it.
**Fix / craft move:** Put the exact words in quotes or ALL CAPS, specify font style, size, colour and placement, and ask for verbatim copy shown once. For dense or print type, set it in a design tool after generation. Keep incidental text out of frame.
**Source:** [OpenAI cookbook, gpt-image-1.5 guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-1.5-prompting_guide) (quoted-text method). Requested short text is now reliable on some models: [PicassoIA, 2026-06-14](https://blog.picassoia.com/how-ai-image-models-have-changed-in-2026) names Ideogram v3 as readable by default. Status: solved for requested headline text, weak for incidental text (one 2026 search summary, not verified against a primary test).

**Tell:** Repeated, copy-pasted elements in crowds, bookshelves, tile floors, windows.
**Why it reads as AI:** The model samples a pattern and tiles it, so no element has its own history.
**Fix / craft move:** Vary elements on purpose (different spines, faces, tile wear). Reduce the count of repeats, put the crowd out of focus, or design the repeat in a layout tool.
**Source:** [Upsampler, 2026-03-20](https://upsampler.com/blog/make-ai-images-look-real).

**Tell:** Shadows going in different directions; eye reflections that do not match the scene.
**Why it reads as AI:** Each region is lit plausibly on its own, but there is no single light source.
**Fix / craft move:** Name one light source and its direction ("soft window light from the left", "overcast afternoon light"). Check the catchlights in the eyes against that source. Upsampler gives no dedicated fix beyond prompting.
**Source:** [Upsampler, 2026-03-20](https://upsampler.com/blog/make-ai-images-look-real); [OpenAI cookbook](https://developers.openai.com/cookbook/examples/multimodal/image-gen-1.5-prompting_guide) (specify lighting and mood). Light-direction example from a vendor guide, [Sozee, undated](https://www.sozee.ai/resources/create-realistic-ai-images-chatgpt/).

**Tell:** The "AI glow": teal-and-orange grade, glossy highlights, over-pushed contrast and colour.
**Why it reads as AI:** Practitioners describe it as the model's averaged default look. It is a learned average, not a choice. Teal-and-orange is also a real film convention, so the palette is fine; the overuse is the tell. The "averaged aesthetic" explanation is a practitioner claim, not a studied finding.
**Fix / craft move:** Name exact colours and a restricted palette instead of "vibrant". Pull saturation down. Grade the final image in an editor, not with the prompt. Choose a grade from a real reference (a film still, a photo) and match it.
**Source:** [Mika Reyes, undated](https://mikareyes.com/ai/how-to-fix-ai-looking-graphic-design-and-posters); [ArtSmart, undated, vendor](https://artsmart.ai/blog/color-theory-in-ai/) (advises naming exact colours to avoid the default palette).

**Tell:** Unnaturally balanced, centred symmetry in faces, buildings and objects.
**Why it reads as AI:** Symmetry is the statistically safe composition. Real scenes are asymmetric and cropped.
**Fix / craft move:** Place the subject off-centre, specify framing and viewpoint (close-up, low angle, wide) and the negative-space side. Break the symmetry with one deliberate asymmetric element.
**Source:** [Upsampler, 2026-03-20](https://upsampler.com/blog/make-ai-images-look-real); [OpenAI cookbook](https://developers.openai.com/cookbook/examples/multimodal/image-gen-1.5-prompting_guide) (place subject with negative space).

**Tell:** Flat materials: fabric with no weave, wood with no grain, polished metal with no scratches.
**Why it reads as AI:** Surfaces are clean because the training average is clean. Real objects carry wear, and the eye expects it.
**Fix / craft move:** Ask for named wear (scratches, fabric weave, grain, dust, fingerprints). Give one object a history: a worn edge, a dent, a mismatched part.
**Source:** [Upsampler, 2026-03-20](https://upsampler.com/blog/make-ai-images-look-real).

**Tell:** Impossible backgrounds: windows opening onto nothing, geometry that does not close.
**Why it reads as AI:** Background detail is generated without a structural model of the room or street.
**Fix / craft move:** Simplify the background or push it out of focus. Specify the architecture and the lens. Crop the frame so the impossible parts are not visible.
**Source:** [Upsampler, 2026-03-20](https://upsampler.com/blog/make-ai-images-look-real).

**Tell:** Misaligned features and gaze; faces where eyes, nose and mouth do not sit as one structure.
**Why it reads as AI:** Faces are generated as a whole, and small misalignments are easy to see on a symmetric face.
**Fix / craft move:** Inpaint the face at higher detail. Check the eye line against the head angle. Use a character reference for consistency across images.
**Source:** [Upsampler, 2026-03-20](https://upsampler.com/blog/make-ai-images-look-real); [PicassoIA, 2026-06-14](https://blog.picassoia.com/how-ai-image-models-have-changed-in-2026) (character reference tools still help on specific poses and characters).

**Tell:** Over-sharpened edges and halo-like micro-contrast.
**Why it reads as AI:** Sharpening is applied globally, so every edge looks equally hard.
**Fix / craft move:** Sharpen selectively, or not at all, in the final pass. Let soft edges stay soft where focus falls off.
**Source:** Practitioner pattern in [Upsampler, 2026-03-20](https://upsampler.com/blog/make-ai-images-look-real) (uses a "Clarity" pass, so it is a tool setting, not a flaw by itself). Treat as a judgement call, not a sourced rule.

**Model-level persistence (2025-2026):** The sources do not agree and none benchmark GPT-image, Midjourney v7, Flux, Imagen, Nano Banana or Sora-image directly. PicassoIA (2026-06) says skin, text and multi-person scenes improved across its named models (Flux 2, Ideogram v3, Recraft v4). Upsampler (2026-03) still lists the full tell set and suggests per-task model picks: Recraft for portraits, GPT Image 1.5 for multi-subject scenes with consistent lighting, Flux 2 Max for detailed environments, Ideogram for text. Neither source names model versions with release dates.

## Prompting and workflow moves

- **Write it as a photo being taken.** Use lens, lighting and framing words; they steer realism better than "8K" or "ultra-detailed" ([OpenAI cookbook](https://developers.openai.com/cookbook/examples/multimodal/image-gen-1.5-prompting_guide)).
- **Order the prompt:** background and scene, subject, key details, then constraints. State the intended use (ad, UI mock, poster) so the polish level is set ([OpenAI cookbook](https://developers.openai.com/cookbook/examples/multimodal/image-gen-1.5-prompting_guide)).
- **Do not mix styles in one prompt.** "Photorealistic cartoon" gives conflicting targets ([fal.ai guide, undated](https://fal.ai/learn/devs/gpt-image-1-5-prompt-guide), via search snippet).
- **Edit with one change per turn.** Use "change only X, keep everything else the same", and repeat the preserve list on every iteration to stop drift ([OpenAI cookbook](https://developers.openai.com/cookbook/examples/multimodal/image-gen-1.5-prompting_guide)).
- **Fix locally, not globally.** Inpaint hands, faces and text; regenerate only the broken region (Upsampler, 2026-03-20).
- **Use reference images** for pose, palette and character, and refer to inputs by index and description.
- **Real-photo mixing:** shoot or find a real photo for lighting and texture and use the model for the rest. This is a common practitioner move; no primary source found in this run.

## Logos and brand marks

**Tell:** Raster-only output (PNG/JPG) that blurs when scaled.
**Why it reads as AI:** Generators produce pixels; a mark must work from 16px to billboard size.
**Fix / craft move:** Redraw as flat vector in a vector tool. Test at favicon size and in one colour. Note: some tools now claim SVG export, but critics report corrupt or unusable vector files.
**Source:** [PixelLogo, undated](https://pixellogo.com/blogs/pixellogo-blog-2/5-reasons-why-ai-logos-dont-work); [GraphicsByte, undated](https://graphicsbyte.com/blog/does-ai-make-a-good-logo/).

**Tell:** Looks like a logo but is generic: shared icons, fonts and layouts.
**Why it reads as AI:** Output draws on common visual vocabulary, so it is hard to own or trademark.
**Fix / craft move:** Start from a one-sentence concept ("what this brand does that no one else does"), sketch 20 thumbnails, then pick one and draw it. Use original or licensed type.
**Source:** [PixelLogo, undated](https://pixellogo.com/blogs/pixellogo-blog-2/5-reasons-why-ai-logos-dont-work) (reused assets); [GraphicsByte, undated](https://graphicsbyte.com/blog/does-ai-make-a-good-logo/).

**Tell:** Decorative effects (gloss, gradient, bevel, texture) that do not reduce to flat vector.
**Why it reads as AI:** Effects are baked into the pixels, so the mark cannot be reproduced cleanly in one colour.
**Fix / craft move:** Design flat from the start. Test the mark in one colour and at small sizes before adding any effect.
**Source:** Search-snippet claim that re-creating an AI logo can cost more than a fresh design ([LogoToUse, undated](https://www.logotouse.com/post/ai-generated-logos-vs-human-designers)); not fetched.

No sourced findings on icon-set craft (grid, stroke consistency). See Gaps.

## Commissioners, studios and pipelines

- **Hooded Horse** bans gen-AI art in its contracts and tells developers not to use it in production, even as placeholders. Reported 2026-01-08. CEO quote: "it's not a PR issue, it's an ethics issue." Source: [Kotaku, 2026-01-08](https://kotaku.com/hooded-horse-gen-ai-art-ban-4x-strategy-steam-2000658179).
- **Epic** reportedly uses gen-AI in Fortnite concept and skin design, with outputs not used as final in-game art. Secondary source only: [SynapseWire, 2026](https://synapsewire.com/en/posts/fortnite-generative-ai-art-pipeline-2026/). Unverified against an Epic statement.
- **Riot** reportedly requires "significant human modification" before AI concepts enter design. Single weak source ([SynapseWire, 2026](https://synapsewire.com/en/posts/fortnite-generative-ai-art-pipeline-2026/)); unverified.
- **Valve** reportedly requires disclosure only for gen-AI content players see, not internal tools. Reported only, not fetched; check Steam's developer documentation.
- **Copyright:** the US Copyright Office reportedly protects AI output only where a human has determined sufficient expressive elements. This is the likely reason for "human modification" rules. Search snippet only, via [Creative Bloq](https://www.creativebloq.com/news/ai-art-banned-in-the-video-games-industry) (page content not extracted).
- **Consensus across sources:** AI is accepted for early exploration and expected to be overpainted or replaced before shipping, with provenance documented. Synthesised from the sources above; no primary policy text found.

## Craft principles

- **Value structure before colour.** Loomis's four basic value plans and restricted four-value scale (*Creative Illustration*, 1947, possibly outdated) are summarised in [Muddy Colors, 2012, possibly outdated](https://muddycolors.com/2012/08/composition-basics-value-structure/). Check the image in greyscale first. Full text: [archive.org](https://archive.org/stream/andrew-loomis-creative-illustration/andrew-loomis-creative-illustration_djvu.txt) (text garbled in our fetch).
- **Visual weight and eye path.** Loomis's fulcrum-lever principle and formal or informal subdivision decide balance; contrast and focal points decide the eye path (same Muddy Colors source, possibly outdated).
- **Read it at thumbnail size.** A distinct silhouette, with the key trait legible from far away, is the first test ([JustSketch, undated](https://justsketch.me/how-to-take-your-character-design-silhouettes-to-thumnbail/)).
- **Observation makes the world believable.** Ian McQue's advice: draw from life as much as possible and keep sketching. Good observation is what makes viewers believe the world presented ([Muddy Colors interview, 2012, possibly outdated](https://muddycolors.com/2012/07/interview-with-ian-mcque/)).
- **One named light source.** Photographers and the OpenAI guide both start from one light, its direction and its quality; mixed light is what reads as fake.
- **Imperfection is information.** Wear, scratches, dust and uneven edges tell the viewer a thing exists in the world (Upsampler; OpenAI cookbook).
- **Restrict the palette.** A few named colours with one accent beats a default "vibrant" grade.
- **Point of view and fit.** Commissioners reject generic output because it has no authored choice. Decide the subject, the viewpoint and the mood first, then choose the tool. Human modification is both the craft step and the reason studios accept the work.
- **Iterate in small steps.** One change per edit, a preserve list, and a final human pass for detail and colour.

## Gaps

- No sourced, model-specific persistence data for GPT-image, Midjourney v7, Flux, Imagen, Nano Banana or Sora-image.
- No sourced findings on the generic fantasy or cyberpunk look; not searched in this run.
- No sourced findings on icon-set craft (grid, stroke, optical sizing) or on art-community (r/Art, r/StableDiffusion) discussions.
- Mike Monaghan's advice not found; search returned a different artist.
- Loomis and McQue sources are possibly outdated (2012 summaries of pre-2025 material).
- Riot, Epic and Valve policy claims are secondary or unverified.
- Teal-and-orange and "averaged aesthetic" explanations come from vendor and practitioner blogs; no study of viewer perception was found.
