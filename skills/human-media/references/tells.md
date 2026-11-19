# Media tells (dated)

last_verified: 2026-11-19 (owner's master list 2026-10-22; audio rows re-checked in the second pass).
Re-check: media tells quarterly, and after any major image, video, music or voice model release.

A tell is a reason to rework something, never proof of who or what made it. Evidence is mostly vendor and practitioner writing. Items without a firm source are labelled.

## Images

| Tell | Strength | Fix |
|---|---|---|
| One lighting setup that is too perfect, or shadows and eye reflections that disagree | moderate | Name one light source and check it |
| Real-world inconsistency: signs, shadows, reflections, geometry that does not close | moderate | Simplify or defocus the background, crop |
| Airbrushed skin with no pores | moderate, improving on top models | Name real texture, inpaint locally |
| Centered symmetry, flat clean materials | practitioner | Off center, add wear to one object |
| Teal-and-orange glow, glossy highlights, over-pushed contrast | practitioner | Named palette, grade by hand |
| Repeated copy-pasted elements in crowds, shelves, tiles | practitioner | Vary them or defocus |
| Hands with wrong fingers | contested, "less reliable than before" | Hide, crop or inpaint |
| Garbled text | expired for requested headline text on frontier models (TextFake, Jun 2026); incidental text still weak | Keep incidental text out; set real type |
| Raster-only logo, generic shared icons | practitioner | Redraw as flat vector, test small and in one color |

Provenance: SynthID or C2PA metadata present is strong evidence of AI origin (Google and OpenAI, May 2026). Absence says nothing.

## Video

| Tell | Strength | Fix |
|---|---|---|
| Events or physics that could not happen; wrong fluids, cloth, particles | moderate (ACL 2026 Findings survey; Physion-Eval 2026-03-20) | Keep interactions short and wide |
| Cuts every 8 to 20 s, flickering backgrounds, odd gaze | anecdotal | Grade clips together, cut on motion |
| Face, clothes or place changes between shots | secondary sources | Reference frames, fewer shots |
| Every shot the same slow push-in | secondary | Give each move a reason |
| Wobbling text | secondary | Add text in an editor |
| Stock-feeling beauty shots, royalty-free swell | secondary | Use specific real places and objects |
| Generic fade-up on every element, one spring everywhere | practitioner | Give each motion a job |

Expired: silent video (Sora 2 and Veo 3 make audio). A missing watermark proves nothing.

## Music and voice

| Tell | Strength | Fix |
|---|---|---|
| Huge catalogue, no live presence or history, generic lyrics, over-smooth vocals | moderate | Real structure, human parts, one distinct hook |
| Little development across the whole song | inference from a detector paper (SONICS, 2025) | Build, break, return |
| Hiss under the voice, stray breath or word, instruments cut off or hollow, mix too slick (Start-Track, 2026-02-15; one author warns tips may expire within a year) | practitioner | Re-record vocal and lead parts, edit by hand, add dynamics |
| Flat pitch movement in cloned voices; 30% less F0 variation rated lower (Interspeech 2025) | study | Direct stress and pitch, reject flat reads |
| Even pacing, no breath | practitioner, unverified | Mark pauses and stress, generate line by line |
| Voice clone sounds real | strong: clones fool listeners about 80% of the time (International AI Safety Report, Feb 2026) | Verify identity another way; never clone without consent |

Direction for TTS (ElevenLabs docs, undated): bracket tags steer delivery, ellipses add pause, capitals add emphasis, v3 and later have no SSML breaks, too many breaks cause artifacts, speed 0.7 to 1.2. Describe voice quality in tags, not sound cues.

Platform rules (checked 2026-11-19):
- Spotify: AI Credits launched April 2026 and show which roles or instruments used AI; AI Personas are labeled and left out of recommendations by default; unauthorized voice clones banned (Spotify newsroom, 2026-10-20).
- YouTube: disclose realistic synthetic content, including AI music that is the main focus. Exempt: unrealistic content, minor edits, script help, audio repair, cloning your own voice.
- Audible/ACX: secondary sources say human narration is required unless authorized (April 2026). Not read at source. Tell the user to check ACX.

Weak: music detector results after pitch or speed changes (ISMIR 2026), so no audio detection claims.
Unverified and left out: chord and lyric tells, cymbal-shimmer (vendor blogs only), Newgrounds guide text, Suno and Deezer figures.

## Guards

- Judge the work, never the maker. Do not say "AI-made" as a verdict.
- Do not use detector output or missing watermarks as proof.
- Stylised, lo-fi or glitch work can be deliberate.
- Never offer tips to beat AI detectors.

## Sources

Owner's `ai-auditor` list (2026-10-22). `research_notes/AI tells and craft across media/` (images_illustration.md, video_motion.md, audio_music_voice.md): Upsampler 2026-03-20, OpenAI image guide, Physion-Eval arXiv 2603.19607, Google Veo 3.1 guide 2025-10-16, SONICS arXiv 2408.14080, TechCrunch 2025-09-25; start-track.com 2026-02-15; isca-archive.org Interspeech 2025 (Bakkouche); elevenlabs.io docs; newsroom.spotify.com 2026-10-20; support.google.com/youtube/answer/14328491.
