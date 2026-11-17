# Media tells (dated)

last_verified: 2026-10-22 for the owner's master list; research notes cross-checked 2026-11-17.
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
| Even pacing, same stress on every line, no breath | practitioner, unverified here | Mark pauses and stress, generate line by line |
| Voice clone sounds real | strong: clones fool listeners about 80% of the time (International AI Safety Report, Feb 2026) | Verify identity through a second channel; never clone without consent |

Weak: music detector results after pitch or speed changes (ISMIR 2026), so no audio detection claims.
Unverified and left out: chord, lyric and cymbal-shimmer tells; Suno and Deezer figures.

## Guards

- Judge the work, never the maker. Do not say "AI-made" as a verdict.
- Do not use detector output or missing watermarks as proof.
- Stylised, lo-fi or glitch work can be deliberate.
- Never offer tips to beat AI detectors.

## Sources

Owner's `ai-auditor` list (2026-10-22). `research_notes/AI tells and craft across media/` (images_illustration.md, video_motion.md, audio_music_voice.md): Upsampler 2026-03-20, OpenAI image guide, Physion-Eval arXiv 2603.19607, Google Veo 3.1 guide 2025-10-16, SONICS arXiv 2408.14080, TechCrunch 2025-09-25.
