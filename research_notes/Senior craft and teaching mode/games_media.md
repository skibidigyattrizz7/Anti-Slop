# Senior craft for human-games and human-media (research notes, 2026-11-26)

Legend: [V] opened and read this session. [L] read in a local skill file. [U] unverified: from memory or a search snippet only, not opened at source. Treat [U] numbers as starting points and say so when you teach them.

Existing coverage (do not repeat): human-games craft.md already has "one core verb + twist", gray-box first, tune by playing, teach/test/twist/retire, 5-8 layered feedback, silhouette test, style bible (4-6 colours), crate ~500 tris, VFX telegraph/impact/fade. human-media already has Rule of Six (no weights), one LUT, L/J cuts, SSML/ElevenLabs notes, Spotify/YouTube disclosure. Audio craft file has NO loudness numbers, NO mix chain, NO sound-design process; video file has NO grading or pacing numbers. Those are the biggest holes below.

## 1. Game design: loop, MDA, prototyping, playtesting

- **Design from the aesthetic backward.** Designers write mechanics; players feel aesthetics; dynamics sit between. Why: you pick the feeling first, then check each mechanic produces it. Check: write "target aesthetic: X" (1-2 of the 8) before any code; cut mechanics that serve none. 8 aesthetics: Sensation, Fantasy, Narrative, Challenge, Fellowship, Discovery, Expression, Submission. Example from the paper: Quake = Challenge, Sensation, Competition, Fantasy. Source: [Hunicke, LeBlanc, Zubek, "MDA"](http://users.cs.northwestern.edu/~hunicke/MDA.pdf) [V]. (Quirk: the paper's own list contains Competition in an example, not in the 8; use the 8.)
- **Core loop contract as one sentence.** "Player does [verb] to get [goal] under [pressure]; success gives [reward], failure costs [cost/retry]." Check: each clause is visible in the first minute; restart takes under ~3 s [U, practice]. Local source: threejs-gameplay-systems SKILL.md [L].
- **Loop cadence layers.** Seconds (action), minutes (encounter/level), session (progression). Design what repeats every 5-30 s, what changes across 1-5 min [L: threejs-gameplay-systems].
- **Prototype for fun, not for look.** Boxes, one verb, 1-2 days. Pass: someone who did not make it wants "one more go" unprompted. Fail: they ask what to do next or stop at first death. [U: standard practice; Schell, *The Art of Game Design*, lens of the toy: "is it fun to play with, ignoring goals?" not opened.]
- **Input-to-response under ~100 ms; fix before any juice.** Check: record at 60 fps, count frames from press to first visible change (<=6 frames). Source: [L] threejs-gameplay-systems references/game-feel.md ("~100ms"). Underlying human-factors figure (Nielsen 0.1 s) [U].
- **Playtest protocol (what to watch).** Watch hands and face, not the screen; mute yourself; do not explain; note first confusion time, first death cause, quit point. Ask only after: "what did you think you were supposed to do?" not "was the jump too floaty?". Why: leading questions plant answers; observed behaviour beats opinion. Pass: 5 testers, count how many failed the same moment; a moment that stops 2 of 5 gets fixed [U: Nielsen's 5-user heuristic, not opened]. Method is craft consensus [U]; no primary source opened for the protocol.
- **Avoid leading:** never say "try the new dash"; give a goal ("get to the flag"). Record screen + face if allowed. Retest after each fix with fresh people.

Gaps: no GDC Vault talk could be opened (the one URL tried returned an unrelated session page). Game Maker's Toolkit and Schell not fetched.

## 2. Difficulty, flow, economy, level pacing, onboarding

- **Teach, test, twist, retire (4 beats) per mechanic; second use confirms, third twists.** Already in human-games; add the check: every new mechanic appears first in a spot where failure is harmless (no death pit) [L: threejs-gameplay-systems genre-design.md; Nintendo pattern in human-games craft.md].
- **Pressure/release rhythm.** Dense group, then a reward/rest window; never two peaks back to back. Check: plot intensity per 30 s on a line; there must be valleys [L: genre-design.md].
- **Difficulty ramp: one new variable at a time.** Raise speed, density or combination count, not all three. Pass: a level's change list has exactly one new variable [L: genre-design.md].
- **Forgiveness is invisible design.** Celeste widens windows in the player's favour: coyote time, jump buffering, corner correction, momentum storage ("everything is fudged a tiny bit in the player's favor"). Numbers from the open source (MIT code, not assets): JumpGraceTime 0.1 s (6 frames at 60 fps), VarJumpTime 0.2 s, Gravity 900, MaxFall 160, FastMaxFall 240, JumpSpeed -105, UpwardCornerCorrection 4 px, DashTime 0.15 s, DashSpeed 240, DashCornerCorrection 4 px. Sources: [Player.cs](https://raw.githubusercontent.com/NoelFB/Celeste/master/Source/Player/Player.cs) [V], [Thorson thread](https://x.com/MaddyThorson/status/1238338574220546049) (snippet only) [U]. Jump buffer: code calls Input.Jump.ConsumeBuffer(); buffer length constant not found in this session, so do not quote 4 vs 5 frames (a third-party page conflicts with itself) [U]. Check for your game: coyote 4-6 frames, buffer 4-6 frames, corner nudge 3-4 px at 1x scale; each is a tunable constant.
- **Flow = challenge tracks skill.** Too hard = anxiety, too easy = boredom [U: Csikszentmihalyi; Jenova Chen "Flow in Games" thesis, not opened]. Practical test: death count per section in playtests; a section with 3x the deaths of its neighbours is a spike, not a ramp.
- **Economy: model before tuning.** Sinks and faucets in a spreadsheet; check the time-to-first-upgrade (a few minutes), and that the best choice is not obvious. Pass: no currency accumulates unspent past ~2 upgrade costs in a normal session [U, practice; no primary source].
- **Onboarding without text.** Safe space + single affordance + the verb forced by geometry (a gap only jumpable). Pass: a tester performs the verb within 60 s with no text on screen. Show before tell; one prompt maximum, shown at the moment of need [U, practice].
- **Landmarks and sightlines** (already in human-games). Add pass/fail: from the start, player can name the next goal without reading a map [U].

Gaps: no primary source for economy numbers, flow chart, or "5 users". Say so when teaching.

## 3. Game feel numbers (with sources)

- **Layer 5-8 responses within ~100 ms of impact.** Sound, particles, hit-stop, flash, knockback, shake, number pop; scale to importance tiers (small/medium/large). Source: [L] game-feel SKILL.md. Origin talks: Nijman, ["The Art of Screenshake"](https://www.youtube.com/watch?v=AJdEqssNZ-U) (INDIGO Classes 2013; talk exists, 30 tips per a blog; specific numbers not verified) [U]; "Juice it or Lose it" (Jonasson, Purho) not opened [U].
- **Hit-stop:** a few tens of ms, 1-3 frames at 60 fps (human-games) [L]. Flash: white tint 1-3 frames [L: game-feel feedback-recipes.md]. Squash ~[1.2, 0.8], stretch ~[0.85, 1.15], impact 2-4 frames (30-65 ms), recovery 4-8 frames (65-130 ms), preserve volume [L: motion-design disney-principles.md].
- **Shake from trauma squared.** offset = maxOffset * trauma^2 * noise; trauma decays linearly. Ship a 0-100% "reduce shake" setting, default ~60-80% [L: game-feel feedback-recipes.md].
- **Fixed timestep for physics, interpolate rendering; CCD for fast bodies.** Check: play at 30 and 144 fps; jump height identical [L: physics-tuning].
- **Camera:** exponential smoothing, not lerp(a,b,0.1) (frame-rate dependent); deadzone; look-ahead; clamp to bounds; follow after movement [L: camera-systems].
- **Pass/fail:** (a) press-to-response <=6 frames, (b) every verb has sound + visual, (c) strongest effect is on rarest event, (d) effect never hides the hitbox, (e) shake has a settings slider.

## 4. Production: scope, vertical slice, art bible, performance budgets

- **Vertical slice = one finished minute at final quality** (art, audio, UI, feel) before building more content. Why: proves the pipeline and kills the "looks like a template" risk early. Check: ~1-5 min playable, with real assets; one representative scene before multiplying levels [L: threejs-game-director "Continuity and early quality"]. General practice [U].
- **Scope rule:** cut to the one mechanic and a finish line (human-games). Add: write non-goals for the slice (design brief field) [L: threejs-gameplay-systems].
- **Art bible one page:** shape language, 4-6 colours, value structure, line weight, 3 do/don't thumbnails, UI icon set (human-games has a text version). Add pass/fail: any new asset checked against it in a side-by-side screenshot.
- **Web/mobile starting budgets (measure, do not assume).** Desktop / mobile worst active-play view: draw calls <=300 / <=150; triangles <=750k / <=300k; geometries <=300 / <=200; textures <=60 / <=40; texture memory <=256 / <=128 MB; shadow lights <=2 / 1; shadow map <=2048 / <=1024; DPR cap 2 / 1.5-2; extra post passes <=2 / 0-1. Source: [L] threejs-aaa-graphics-builder references/technical-art.md (author-chosen starting contracts, not a standard).
- **Frame time:** 60 fps = 16.67 ms, 30 fps = 33.3 ms, 120 fps = 8.33 ms (arithmetic). Budget a target 10-12 ms to leave headroom on low-end phones [U, practice]. Check: report actual diagnostics (`renderer.info.render.calls/triangles`), not guesses.
- **Spend rules:** instance repeats, share materials (material count grows faster than geometry), LOD/impostors behind, real shadows only for hero and grounding [L: technical-art.md].
- **Unity web:** Brotli, strip engine code, managed stripping High, correct `Content-Encoding` and `application/wasm` headers on the host [L: unity optimize-web]. Unity audio: avoid stereo clips with 3D spatial blend, avoid Decompress On Load for clips over 1 MB [L: unity optimize-audio].

## 5. Visual art and art direction

All items in this section are craft consensus; Gurney's *Color and Light* and art-director blogs were not opened [U] unless marked [L].

- **Value before colour.** Block in 3-5 values; if the thumbnail reads in greyscale it will read in colour. Check: desaturate a screenshot; the hero and the hazard must still separate (squint/blur test).
- **Composition:** one focal point, leading lines, rule of thirds only as a start; place the subject off centre; group into 3 masses (foreground/mid/back). Check: thumbnail at 5% size still shows the layout.
- **Colour script:** one swatch strip per scene/beat (a 1-row palette per act), so mood changes are planned. Check: each swatch has one dominant, one accent, neutrals; accent <=10% area.
- **Shape language:** circles = safe/friendly, squares = stable, triangles = danger. Enemy vs ally silhouettes differ in shape, not only colour (colour-blind safe). Check: silhouette test at 64 px.
- **Style guide contents:** shapes, palette hexes, proportions (head:body), material rules, line weight, lighting direction, 3 reference images, 3 "not this" images.
- **Direct AI image tools like an art director:** (1) reference board of 6-12 images with a one-line "what I take from this" each; (2) lock palette and light direction in words; (3) generate thumbnails, pick, then iterate one variable at a time (edit mode / inpaint, not a full reroll); (4) keep a seed or reference image for consistency; (5) fix type, hands, small details by hand. Aligned with human-media prompt-brief.md; see also [L] brandkit and taste-skill imagegen-frontend-web (one image per section, one palette across all images, composition variety).
- **Pass/fail:** one light source, <=5 named colours, one imperfection kept, nothing text-in-image.

## 6. Video and motion: editing, shot lists, pacing, grade, UI motion

- **Murch's Rule of Six, with weights.** Emotion 51%, story 23%, rhythm 10%, eye trace 7%, 2D plane 5%, 3D space 4%; when a cut cannot satisfy all, sacrifice from the bottom up, never emotion first. The percentages are Murch's rough illustration, reproduced by blogs; the existing human-media file deliberately ignored them. Cite as "teaching heuristic, not measurement." Sources: [FilmDaft](https://filmdaft.com/walter-murchs-rule-of-six-the-editors-formula-for-choosing-the-right-cut/), [Grainzilla](https://grainzilla.com/walter-murchs-rule-of-six-puts-emotion-at-51-percent-and-continuity-dead-last/) (search snippets; one source gives story 21%) [U]. Book: Murch, *In the Blink of an Eye* (1995), not opened [U].
- **Shot list columns:** shot #, type (wide/medium/close/insert), subject, action, camera move, length (s), purpose (one verb: establish, reveal, react), audio. Pass: every row has a purpose; no two adjacent shots share type and angle.
- **Short-form pacing:** hook in the first ~1-3 s; a visual change every 2-4 s; one idea per video; end on the payoff, not a logo [U: practice, no primary source]. Check: mute it; can you tell the story from pictures?
- **Colour grading basics:** fix exposure and white balance first (primary), then contrast, then look (secondary/LUT). One LUT across clips (already in human-media). Check with scopes: waveform shows black near 0-5%, white near 90-100% IRE; skin tones on the skin-tone line of the vectorscope [U: standard colourist practice, not opened].
- **12 principles in UI/motion:** squash/stretch, anticipation (100-200 ms, 10-20% of main move), staging (dim others to 40-60%), follow-through offsets 50-150 ms, slow in/out (ease-out for entrances, ease-in for exits), arcs, secondary action, timing, exaggeration, solid drawing, appeal, straight-ahead vs pose-to-pose. Source: [L] motion-design director/disney-principles.md (the 12 principles originate with Thomas and Johnston, *The Illusion of Life*, 1981 [U]).
- **UI motion durations:** tooltip 80-120 ms, button/toggle 120-180, icon 150-250, card enter/exit 200-350, modal 300-400, page transition 400-600, dramatic reveal 600-1200; hover <100 ms; stagger total <500 ms; <20 animated elements per viewport; animate transform + opacity only; prefers-reduced-motion alternative; 1/3 rule (no unbroken motion >1/3 container, max 1/3 elements moving at once). Source: [L] motion-design SKILL.md and reference/quality-checklist.md.
- **Motion personality dial:** playful 150-300 ms with ease-out-back, 10-20% overshoot; premium 350-600 ms, no overshoot; energetic 100-250 ms, 15-30% overshoot [L: motion-design SKILL.md].

## 7. Sound and music: mixing, loudness, layering, voice

- **Loudness targets (verified).**
  - EBU R 128 (2023): programme loudness -23.0 LUFS, tolerance +-0.5 LU (live +-1.0), true peak max -1 dBTP. LUFS = LKFS (ITU-R BS.1770). Source: [EBU R 128](https://tech.ebu.ch/docs/r/r128.pdf) [V].
  - Spotify: default -14 LUFS, Loud setting -11, Quiet -19; true peak below -1 dBTP, below -2 dBTP if the master is louder than -14 LUFS integrated; limiter on Loud engages at -1 dB, 5 ms attack, 100 ms decay. Source: [Spotify Support](https://support.spotify.com/us/artists/article/loudness-normalization/) [V].
  - YouTube: ~-14 LUFS integrated, turns loud material down, does not boost quiet; official help page not opened, figure from vendor blogs and a forum thread [U]. Recommended safe deliverable: -14 LUFS integrated, true peak <= -1 dBTP.
  - Other platforms (Apple -16, Netflix -27 dialogue-gated, TikTok): not checked [U].
- **Gain staging:** keep each channel peaking around -18 dBFS RMS-ish (analog-calibration convention) so master has headroom; fix level with clip gain before inserting compressors [U: practice]. Check: master bus peaks <= -6 dBFS before the final limiter.
- **Mix order:** levels, pan, EQ (cut before boost), dynamics, space (reverb/delay), automation. Reference a commercial track at matched loudness (A/B at equal LUFS, else louder wins). Check on phone speaker and earbuds.
- **Sound design layering:** impact = transient (click) + body (low thump) + tail (air/reverb); randomize pitch +-5-10% and volume on repeats (human-games has the rule, number is practice) [U]. Leave silence before a hit for contrast. Game audio: duck music under voice 3-6 dB [U]; route by group (Music, SFX, UI, Voice) with exposed volume params [L: unity craft-game-floors "MusicVol/SFXVol", audio-setup-mixers].
- **Voice direction:** give the line a want and an obstacle ("say it like you're trying not to wake someone"), mark pauses and stresses, record 3 takes with different intensities, pick the one with a pitch contour that varies. Rationale on pitch variation: Interspeech 2025 (cited in existing craft-audio.md) [V in repo, not reopened].
- **Pass/fail:** integrated LUFS within 1 LU of target; true peak <= -1 dBTP; dialogue intelligible over music at a quiet listening level; no clipping; one stinger/silence moment.

## Build on these local skills

Base: `/root/.claude/skills/synced/d13e5c22-fd75-4b81-b6fa-7bbe4432d675_ad4b38a0-ff16-4a31-8117-7e768f4021ea/`

| Path | Reuse | Weak | License |
|---|---|---|---|
| `game-feel/` | Tiers (small/medium/large), 5-8 layers in 100 ms, trauma^2 shake, hit-stop and flash numbers, reduce-shake setting, "feedback must not hide the next decision", feedback-recipes.md | Engine-neutral, no source citations; no audio numbers | Apache-2.0 [V] |
| `physics-tuning/` | Fixed step plus interpolation, CCD, jitter diagnosis, stress test at low/high fps | Mostly engine mechanics, little "feel" tuning | Apache-2.0 [V] |
| `camera-systems/` | Exponential smoothing vs lerp, deadzone, look-ahead, bounds, late-update | 2D/3D follow only, no cinematic grammar | Apache-2.0 [V] |
| `threejs-game-director/` | Scope ladder (user words set bar), game-progress.md log, vertical-slice-first, asset-recovery | Three.js-specific; heavy for small tasks | MIT, (c) 2026 Majid Manzarpour [V] |
| `threejs-gameplay-systems/` (+ references/game-feel.md, genre-design.md) | Design brief fields, core-loop contract, level plan, per-genre difficulty and fun-factor tests, tween helpers | Three.js-specific code; no playtest protocol | MIT [V] |
| `threejs-aaa-graphics-builder/` (references/technical-art.md, visual-scorecard.md) | Render budget table, material roles, 10-category scorecard, "forms, then materials, then lighting, then effects" | Numbers are the author's contracts, not sourced; mobile-only column thin | MIT [V] |
| `threejs-game-ui-designer/` | HUD hierarchy (survival, objective, feedback, flavour), required states, text-fit and safe-area checks | Short; no numbers | MIT [V] |
| `motion-design/` | 12 principles with ms and % numbers, duration table, quality-checklist with severity tiers, personality dial | Web UI oriented; numbers unsourced | MIT [V] |
| `animation-forge/` | Large GSAP/CSS library (6.4k words) | Too long to load whole; no LICENSE file found, so do not copy text | unknown (no LICENSE; README only) |
| `canvas-design/` | Poster/art philosophy, fonts folder | Philosophy-heavy, few numbers | Apache-2.0 (LICENSE.txt) [V] |
| `brandkit/` | Brand-board prompt structure (logo system, sparse type) | Image-generation oriented | MIT [V] |
| `algorithmic-art/` | p5.js generative templates | Little relevance to craft rules | Apache-2.0 per LICENSE.txt (header not fully read) |
| `blender-image-to-3d/` | Image-to-3D pipeline, evals folder | Heavy; Blender-specific | MIT (header seen) |
| `brag/` | Launch-video flow; SOURCE.md notes bundled audio licence unverified and omitted | Do not reuse its audio | MIT (SOURCE.md) |

Plugin: `/root/.claude/plugins/synced/.../unity/skills/` (names skimmed: 2d-pixel-perfect, audio-setup-mixers, craft-game-floors, optimize-audio, optimize-web, urp-postprocessing, ui, etc.). Read three: `craft-game-floors` (art bible, lighting, juice, sound floors with "floors on unless declined" and look scoring; reuse the "floor" idea and the mixer handshake), `optimize-web` (compression, stripping, server headers), `optimize-audio` (load type, mono for 3D). Licence: Unity Companion License (`unity/LICENSE.md`); Unity-dependent use only, do not copy text into the library. `taste-skill/skills/imagegen-frontend-web/SKILL.md`: reuse "one image per section, one palette across all images, vary hero composition"; web-UI focus, MIT per taste-skill LICENSE (not opened).

## Teaching notes (how a senior explains a choice)

- **Name the feeling, then the knob.** "I want the jump to feel forgiving (Challenge without frustration), so I gave 6 frames of coyote time; try 3 and feel the difference." Always: goal, constant, what changes if you move it.
- **Show the pair.** Before/after screenshot or clip, plus the single changed variable. Never explain two changes at once.
- **Give a test, not an opinion.** "Desaturate it: does the hero still pop?" "Mute it: does the story still read?" "Silhouette at 64 px."
- **Say what was cut and why.** Murch: sacrifice lower criteria, never emotion first. Seniors state the trade-off ("I broke eye trace to keep the reaction").
- **Mark confidence.** "This is Celeste's real value (read from the code)"; "this is a rule of thumb"; "I did not verify this." Matches the library's evidence labels.
- **Invite the junior's next move.** End with one thing to try and what result means pass or fail.
- **Use the reference, not authority.** Point at a shipped game, a spec number (-14 LUFS, -23 LUFS, -1 dBTP) or the local checklist item.
- **Keep it short:** one decision, one reason, one check, one source per beat.

Not opened or failed: GDC Vault talks, Game Maker's Toolkit, Schell's book, Gurney, Murch's book, YouTube official loudness page, Apple/Netflix/TikTok specs, Nielsen/Csikszentmihalyi primary texts.
