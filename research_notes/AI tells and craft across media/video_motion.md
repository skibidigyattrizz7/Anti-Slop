# AI-made video, animation and motion: tells, fixes, craft

Scope: craft quality only. Detector internals excluded. Evidence is thin: most 2026 tell claims come from vendor or SEO blogs. The only study found is Physion-Eval (arXiv, March 2026). Today is 2026-11-17. "Snippet only" means the claim came from a search summary, not a fetched page.

## 1. Tells in AI-generated video

### Physics and object interaction
- **Tell:** Objects pass through each other, liquids and cloth move wrong, an object changes state mid-shot.
- **Why it reads as AI:** The model learns appearance more than causal motion, so single frames look fine and motion looks wrong.
- **Fix / craft move:** Keep physical interactions brief and on wide shots. Show cause and effect, not the mechanics. Prefer simple motion (a walk, a pour from a distance) over small-object manipulation.
- **Source:** Physion-Eval, submitted 2026-03-20: 83.3% of exocentric and 93.5% of egocentric physics-critical videos show at least one human-visible glitch. Five models, not named on the abstract page. https://arxiv.org/abs/2603.19607 (fetched). A CapCut guide (Aug 2026, vendor) says hands, object interaction and state changes still break: https://www.capcut.com/create/ai-video-physics-realism-whats-fixed-and-whats-broken (snippet only).

### Hands
- **Tell:** Extra or fused fingers, hands that slide off objects, hands that change shape between frames.
- **Why it reads as AI:** Hands are small and heavily articulated; errors show at normal viewing size.
- **Fix / craft move:** Frame hands out of shot, hide them (pockets, props), or cut before a grip resolves. Use practical footage for hand close-ups.
- **Source:** Hands named as a weak point in 2026 comparisons (secondary, date not shown): https://tools-3hx.pages.dev/en/sora-vs-runway-gen4-vs-kling-ai-video-generation-comparison-2026-en/. No primary benchmark retrieved; see Gaps.

### Morphing and identity drift
- **Tell:** Background objects reshape, a character's face, clothes or hair change between shots, lighting drifts.
- **Why it reads as AI:** Each generation holds no persistent state for identity or scene, so the same person or place differs across cuts.
- **Fix / craft move:** Fewer, longer shots. Use one reference image per character and per location as the start frame. One subject per shot. Avoid cutting between two generations of one person unless a reaction motivates the cut.
- **Source:** Kling's own blog lists visual consistency, physics, text and long-form storytelling as open limitations (date not shown): https://kling.ai/blog/limitations-of-current-ai-video-generation-technology. Consistency claims for sequences over ~20 s and a 70-80% figure come from a secondary blog (unverified): https://budgetpixel.com/blog/why-ai-videos-feel-fakeand-how-consistency-changes-everything (snippet only).

### Text in frame
- **Tell:** Signs, screens and captions wobble, misspell or dissolve.
- **Why it reads as AI:** Glyph shapes are not held stable across frames; text is generated as texture.
- **Fix / craft move:** Never rely on generated text. Add titles, signs and UI in an NLE or motion tool, in a real font.
- **Source:** Text named as the most consistent complaint in 2026 comparisons (secondary, date not shown): https://tools-3hx.pages.dev/en/sora-vs-runway-gen4-vs-kling-ai-video-generation-comparison-2026-en/. Kling's own blog also lists text as a limitation (above).

### Uniform, unmotivated camera drift
- **Tell:** Every shot slides or pushes in at the same speed, with no reveal, follow or reaction behind it.
- **Why it reads as AI:** Without a stated camera intent, prompts produce a generic drift. Shots look chosen by default, not by the filmmaker.
- **Fix / craft move:** Give each shot a purpose: a dolly that follows a reveal, a static hold for a reaction, handheld for tension. Vary move type and speed across the cut. Hold static when there is nothing to reveal.
- **Source:** Google Cloud, "Ultimate prompting guide for Veo 3.1", published 2025-10-16 (Veo 3.1 era). Gives the camera vocabulary: dolly, tracking, crane, aerial, slow pan, POV; wide, close-up, low angle; shallow depth of field, rack focus. https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1 (fetched). Static default without camera instruction: a third-party guide (date not shown), https://www.veed.io/learn/veo-3-1-prompts (snippet only).

### Faces, lip-sync and over-smooth skin
- **Tell:** Skin with no pores, eyes that do not track, speech that drifts from the mouth, dead expressions.
- **Why it reads as AI:** Models smooth detail and approximate micro-expression; sync is inferred, not measured.
- **Fix / craft move:** Use faces in medium or wide framing, or keep them off screen. Record voice first and cut to reactions and off-screen lines. Do not ask the model for a close-up performance.
- **Source:** Google's guide supports quoted dialogue and SFX prompting but makes no sync-quality promise (above). The close-up limit comes from a secondary sound-design blog (date not shown): https://invideo.io/faq/does-sound-design-make-ai-generated-footage-feel-more/ (vendor).

### Motion timing
- **Tell:** Motion reads as slightly off in speed or blur.
- **Why it reads as AI:** Models do not reliably learn physical time or frame rate.
- **Fix / craft move:** Retime in the NLE (speed change, frame-rate conversion) and keep shutter and motion blur consistent across shots.
- **Source:** HackerNoon summary of a 2026 study (secondary; "April 2026" per summary, not verified): viewers preferred clips corrected to a predicted physical frame rate. https://sia.hackernoon.com/the-invisible-broken-clock-in-ai-video-generation (snippet only).

### Seams between 4-8 s clips
- **Tell:** Cuts feel like splices; each clip has its own exposure and grade.
- **Why it reads as AI:** Clips are generated independently, so tone and state jump at the join.
- **Fix / craft move:** Grade all clips to one LUT and one exposure. Run one continuous audio bed under the joins. Cut on motion or on a reaction.
- **Source:** Secondary editing guide (date not shown, vendor): https://www.atlabs.ai/blog/why-your-ai-videos-look-fake-(and-how-to-fix-them-step-by-step). Not a perception study.

### Stock-feeling B-roll and generic music
- **Tell:** Every shot is a beauty establishing shot with no subject; music is a royalty-free swell.
- **Why it reads as AI:** Prompts default to "cinematic" averages with no place or point of view.
- **Fix / craft move:** Shoot or source the specific places and objects the story needs. Mix real footage with generated. Score to the cut, not to a mood tag.
- **Source:** Secondary hybrid-workflow post (date not shown): https://dev.to/q0ago/ai-music-video-editing-the-hybrid-workflow-that-looks-human-47l7 (snippet only).

### Voiceover, subtitles and music in short video
- **Tell:** TTS voice reads every comma at one speed with no breath; subtitles are in a default font, broken mid-phrase; music ignores the cut.
- **Why it reads as AI:** The audio is generated to a script, not timed to picture.
- **Fix / craft move:** Write for speech: short sentences, one point per line. Land pauses on cuts. Subtitles break at phrases, one font, one position, clear of UI. Music rises on the important cut and drops under speech.
- **Source:** Secondary sound-design guides above. No retrieved study on viewer perception of TTS.

### What has improved and what has not (2025-2026)
- **Improved (per Google's guide and vendor material):** Camera control via prompt vocabulary; dialogue and sound-effect prompting in Veo 3.1 (guide dated 2025-10-16).
- **Still weak (per 2026 secondary sources):** hands, text, multi-shot identity, long sequences, object interaction, close-up acting.
- **Model ranking:** claims that Sora 2 leads on narrative coherence and Kling on human motion conflict across blogs and cite different versions. Check the version before quoting: https://tools-3hx.pages.dev/en/sora-vs-runway-gen4-vs-kling-ai-video-generation-comparison-2026-en/ (secondary).

## 2. Craft principles (video and editing)

Workflow and editing advice without a single tell. Free-form, from editing and direction practice.

1. **Storyboard first.** Write each shot as one sentence with a purpose. Google's five-part prompt order (cinematography, subject, action, context, style) fits that sentence; it does not replace it. Source: Google guide above.
2. **Reference frames.** One locked still per character and location, reused as the start frame.
3. **Shot-by-shot generation.** Short shots, one subject, one action each. Longer scenes come from the edit.
4. **Edit in a real NLE.** Titles, captions, retimes and grade belong outside the generator.
5. **Grade everything together.** One LUT, one black level, one white point, then check that all shots read as one world.
6. **Emotion decides the cut.** Walter Murch's Rule of Six orders cutting criteria: emotion, story, rhythm, eye trace, 2D plane, 3D space. Commonly cited weights (51/23/10/7/5/4%) come from secondary blogs, not checked against his book. Source: https://nofilmschool.com/2016/11/6-rules-good-cutting-according-oscar-winning-editor-walter-murch (2016; the rule comes from *In the Blink of an Eye*, 2001, older than 2025, possibly outdated in detail).
7. **Pacing is about where information lands.** A slow shot feels rushed if the key detail arrives at its end and the cut follows immediately. Let the viewer see the important thing, then cut. Source: secondary editing guide above (inference from its example).
8. **Sound bridges cuts.** J-cuts (audio leads) and L-cuts (audio trails) carry the viewer across a change. Standard grammar, not sourced in this pass; treat as craft knowledge.
9. **Motivated camera.** Every move reveals, follows or reacts. Static holds are valid.
10. **Hook-first short form.** Lead with the most specific visual or claim, not a logo or title card. Not sourced in this pass; treat as practice.

## 3. Motion design and UI animation

- **Tell:** Everything fades up on scroll; one ease-out on every element; uniform durations; everything moves at once.
- **Why it reads as generic:** One curve and one duration everywhere remove weight and hierarchy. Fade-up is the default preset.
- **Fix / craft move:** Give each motion a job: entrance for new content, feedback for taps, exit for dismiss. Vary duration by distance and importance. Stagger only where order carries meaning.
- **Source:** SAP Fiori motion design overview (fetch returned 403; snippet only; date not shown): https://www.sap.com/design-system/fiori-design-web/v1-145/foundations/interaction/motion-design-overview. Madegood Designs (date not shown): UI motion roughly 200-500 ms; overshoot overdone is a common mistake (snippet only): https://madegooddesigns.com/motion-design-principles/.

- **Tell:** "Bouncy" overshoot on every interaction, including errors.
- **Why it reads as AI:** A single spring preset on everything reads as template motion, not as response to a state change.
- **Fix / craft move:** Overshoot for a settle on success or a large entrance; firm, no-overshoot motion for errors. Anticipation (a small wind-up) before a large start.
- **Source:** Figma help article explains easing control points outside 0-1 produce overshoot and wind-up (snippet only, date not shown): https://help.figma.com/hc/en-us/articles/41238219562007. Error-state no-overshoot rule from a secondary agent-skill note (date not shown; not verified).

- **Tell:** Motion that starts and stops at constant speed.
- **Why it reads as generic:** Linear or uniform motion has no weight.
- **Fix / craft move:** Slow in, slow out: start gently, speed up, ease to a stop. Follow-through: secondary parts settle after the primary stops.
- **Source:** Disney's principles, secondary summary (date not shown): https://www.linearity.io/blog/principles-of-animation. Original is Thomas and Johnston, *The Illusion of Life* (1981), older than 2025, possibly outdated as a primary citation, still the base vocabulary.

## 4. Launch and explainer tooling

- **HyperFrames (HeyGen), fetched from its README:** an open-source framework (Apache 2.0) that turns HTML, CSS and seekable animations into deterministic MP4 files by seeking frames in headless Chrome and encoding with FFmpeg. Compositions are HTML files with data attributes; no build step; adapters for GSAP, CSS, Lottie, Three.js, Anime.js, WAAPI. Its frame.md section gives one rule: "Numbers come from the script." https://github.com/heygen-com/hyperframes (fetched, undated). It does not publish default durations or easing.
- **Remotion and After Effects templates:** not checked in this pass. Gap.
- **Material 3 easing and duration tokens:** the fetched page returned only a title; no values. Gap.

## Gaps

- Runway Gen-4 official prompting guidance: not retrieved (search rate limit).
- No independent 2026 study of viewer perception of AI video. All tell claims except Physion-Eval rest on vendor, SEO or secondary sources.
- Physion-Eval does not name its five models on the abstract page.
- Hands: no primary benchmark retrieved; the "anatomy glitch" rate from a May 2026 post could not be traced to a source and is omitted.
- Material 3 easing values, Remotion defaults, hook-first and J/L-cut sources: not retrieved.
- Disney principles and Murch weights: secondary summaries only; primary texts not checked.
- SAP, Figma and Madegood claims: from search snippets; SAP page unreadable.
