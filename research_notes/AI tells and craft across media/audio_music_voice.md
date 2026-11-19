# AI tells and craft: audio (music, sound, voice)

Status: partial. The search quota ran out after about 13 tool calls. Several planned sources (ElevenLabs direction guide, Audible/ACX policy, arXiv tell studies, producer forums) were not retrieved. Everything below is sourced to a page I opened or a search result I read. Items marked UNVERIFIED need a second pass before the skill library relies on them.

## Key question 1: Tells in AI music (Suno/Udio)

### Takeaway
Little verified here. The one checked academic source says full-song structure over time is the distinguishing signal, which points to arrangement development as the weak spot. Tell-level claims (chords, lyric clichés, vocal breaths, mix shimmer) are not yet sourced.

### Cited Findings
- Spotify's Sept 25, 2025 policy: adopts DDEX AI credits so labels and distributors can disclose AI use for vocals, instrumentation, or post-production; bans unauthorized voice clones; says it will not penalize responsible AI use and targets bad actors. Source: [TechCrunch, 2025-09-25](https://techcrunch.com/2025/09/25/spotify-updates-ai-policy-to-label-tracks-cut-down-on-spam) (fetched).
- Spotify says a missing credit does not mean no AI was used, because disclosure depends on the artist or distributor. Source: [TechCrunch, 2025-09-25](https://techcrunch.com/2025/09/25/spotify-updates-ai-policy-to-label-tracks-cut-down-on-spam) (fetched, "stated limits").
- Spotify AI Credits reportedly entered beta on 2026-04-16. Only one source, a distributor marketing blog: [InterSpace Music](https://interspacemusic.com/blog/?p=3887). UNVERIFIED against Spotify's newsroom.
- Suno added stem separation, an inpainting API for editing sections, and Music Finetunes (March 2026). Source: search-snippet aggregator only, [Opus Pro, April 2026](https://www.opus.pro/blog/ai-music-news-april-2026). UNVERIFIED.
- Deezer reports about 44% of daily uploads are fully AI-generated (about 75,000 tracks/day, April 2026). Source: search-snippet aggregator only, same page as above. UNVERIFIED.
- SONICS (arXiv 2408.14080, v4 Feb 2025): the authors argue that synthetic songs are identified by patterns across the whole song, not by short frames. Source: [arXiv](https://arxiv.org/abs/2408.14080) (fetched). This is a detector paper. It is cited only for the craft implication that whole-song development carries the signal.

### Inferences
- If the discriminating signal sits in whole-song structure, the craft fix is arrangement that develops across the song (new material, removed layers, changes in density), not surface polish.

### Gaps
- No sourced evidence yet on chord-progression or lyric-cliché tells, vocal breath/consonant artifacts, cymbal shimmer or mix mush, or which Suno/Udio versions improved on which tells. Needs Gearspace, r/WeAreTheMusicMakers, or Sound on Sound threads from 2025-2026.
- The US Copyright Office January 2025 ruling on non-human-authored output appeared only in a search summary. Not fetched. Not used here.

## Key question 2: Tells in AI voice/TTS and voiceover

### Takeaway
Only the SSML tag set was verified. Direction-level tells (flat prosody, uniform pacing, missing breath) are unsourced in this pass.

### Cited Findings
- SSML `<prosody>`, `<emphasis>`, and `<break>` (time or strength) control pitch, rate, volume, emphasis, and pauses. `<prosody>` and `<emphasis>` should wrap full sentences, because wrapping single words can cause unwanted pauses. Source: [Google Cloud TTS SSML docs](https://docs.cloud.google.com/text-to-speech/docs/ssml) (fetched). No last-updated date shown; treat the tag set as possibly outdated for newer engines.
- ElevenLabs v3 best-practices guide: fetch returned 403. Not read.
- Audible/ACX AI narration rules: search rate-limited. Not read.

### Inferences
- Flat delivery is most often a script problem (no placed pauses, no emphasis choices). Markup helps only where the writer decided where the stress and breath go.

### Gaps
- No verified source on voice-director practice (breath placement, script-as-performance, read-aloud testing), on laughs or mouth noise, or on current disclosure norms for AI narration on Audible, Spotify or YouTube.

## Key question 3: What separates crafted audio

### Takeaway
Thin. Only one 2018 trade article was reached, and it is largely vendor claims. Flagged possibly outdated.

### Cited Findings
- A Sound on Sound article (dated September 2018, possibly outdated) quotes a mixing researcher estimating AI tools could save 50–70% of routine mixing time. This is a time-saving estimate, not a quality measure. Source: [Sound on Sound](https://www.soundonsound.com/music-business/ai-music) (fetched).
- The same article says LANDR's own claim is that even professionals find it hard to tell whether a song was mastered by a human or by LANDR. This is vendor self-assessment. Source: same page.

### Inferences
- No independent evidence yet that AI mixing or mastering is recognized as AI by engineers. The claim is untested.

### Gaps
- Sound-design layering, foley, room tone, silence, genre idiom, and reference-track practice: no sources retrieved.
- MusicRadar arrangement/dynamics article: fetch returned 404.

## Workflow moves (not yet sourced)
- Stem separation exists in Suno per the UNVERIFIED aggregator above. Re-record, re-arrange in a DAW, and use human vocals or instruments are plausible moves but unsourced here.

## Podcasts and audiobooks
- Gap: no verified platform policy for AI voice disclosure beyond Spotify's DDEX credits above.

## Craft principles
Only three are sourced:
1. Place emphasis and pauses on purpose, at sentence level. Source: [Google SSML docs](https://docs.cloud.google.com/text-to-speech/docs/ssml).
2. Disclosure should describe what was AI-made (vocals, instrumentation, post-production), not just yes or no. Source: [TechCrunch, 2025-09-25](https://techcrunch.com/2025/09/25/spotify-updates-ai-policy-to-label-tracks-cut-down-on-spam).
3. Development across the whole piece is where synthetic output is most distinguishable. Source: [SONICS arXiv](https://arxiv.org/abs/2408.14080). This is an inference from a detector paper.

Everything else about craft (dynamics, space, idiom, performance direction, silence) needs a second research pass before it goes into the library.

## Sources
- [TechCrunch, 2025-09-25](https://techcrunch.com/2025/09/25/spotify-updates-ai-policy-to-label-tracks-cut-down-on-spam)
- [arXiv 2408.14080, v4 2025-02-25](https://arxiv.org/abs/2408.14080)
- [Google Cloud TTS SSML](https://docs.cloud.google.com/text-to-speech/docs/ssml)
- [Sound on Sound, 2018, possibly outdated](https://www.soundonsound.com/music-business/ai-music)
- [InterSpace Music (distributor blog, unverified)](https://interspacemusic.com/blog/?p=3887)
- [Opus Pro, April 2026 (search snippet, unverified)](https://www.opus.pro/blog/ai-music-news-april-2026)

## Second pass 2026-11-19

Method: pages opened with WebFetch. Format: Tell or fact / Fix / Source. Producer-sourced tells are thin and dated; the author of one guide says they may expire within a year.

### AI music tells named by practitioners
- **Tell:** Hiss layered over the voice, stronger in quiet songs; a stray breath or word where it does not belong; vocal transitions too polished or crammed; instruments cut off in odd places; instruments hollow or compressed; whole mix "too slick, too manicured" (musician Dylan Paul Ware, quoted); generic "average of everything" phrasing. **Fix:** Re-record or replace the vocal and lead parts; edit stray breaths and cutoffs by hand; add dynamics and uneven human feel. **Source:** https://www.start-track.com/start-tracks-guide-on-how-to-spot-ai-music/ (Will Sisskind, 2026-02-15). The essay lists no structure or lyric tells.
- **Not opened:** Newgrounds moderation guide (weak attacks on percussion, mixing issues) returned 403; claim seen only in a search snippet. Shimmer on hi-hats and sibilance came from vendor blogs only. Both are unverified.
- **Detector paper (earlier pass):** SONICS, whole-song structure. Still the only structure claim.

### AI voice and TTS
- **Fact:** Interspeech 2025 study: voice clones often fail to reproduce dynamic pitch (F0) variation; a condition with 30% reduced F0 variation was rated lower. ElevenLabs was rated comparable to human speech; StyleTTS-2 and XTTS-v2 lower. **Fix:** Direct pitch and stress variation; do not accept flat reads. **Source:** https://www.isca-archive.org/interspeech_2025/bakkouche25_interspeech.html (Bakkouche et al., 2025).
- **Fact (vendor guidance):** ElevenLabs v3/v4 docs: bracket audio tags (for example `[whispers]`, `[sighs]`) steer delivery; describe voice quality, since sound-cue-like tags can produce sound effects; ellipses add pauses and weight; capitals add emphasis; v3 and v4 do not support SSML break tags (older models allow `<break time="x.xs" />` up to 3 s); too many break tags cause speed-ups, noise or artifacts; explicit dialogue tags beat relying on context; speed range 0.7 to 1.2; extreme values hurt quality; tags that speak out loud can be cut in post. **Source:** https://elevenlabs.io/docs/best-practices/prompting/eleven-v3 (opened 2026-11-19, undated; the page mixes v3 and v4 wording, so check against the engine used).
- **Fact:** Google SSML sentence-level wrapping advice (earlier pass) stands for engines that support SSML.

### Platform disclosure
- **Spotify (verified, primary):** Sept 2025: spam filter, impersonation policy against unauthorized voice clones, DDEX AI credits. Oct 2026 one-year post: AI Credits launched in April 2026 and show which roles and instruments used AI, in Song Credits on mobile; AI Personas are labeled (badge announced 2026-08-11) and excluded from editorial and algorithmic recommendations by default; more than 50 million slop and spam tracks removed from recommendations, over 75 million spam tracks removed (company-reported). This confirms the April 2026 beta date, which the first pass had only from a distributor blog. **Sources:** https://newsroom.spotify.com/2025-09-25/spotify-strengthens-ai-protections/ (search result, body not opened); https://newsroom.spotify.com/2026-10-20/prioritizing-human-artistry/ (opened 2026-11-19).
- **YouTube (verified, primary help page):** Disclose realistic altered or synthetic content: a real person appearing to say or do something they did not, altered real events or places, realistic scenes that never happened, and AI-generated music that is the main focus of the video. Exempt: clearly unrealistic content, minor aesthetic edits, production help (scripts, titles, captions), audio repair, cloning your own voice for voiceovers or dubs, game footage. **Source:** https://support.google.com/youtube/answer/14328491 (opened 2026-11-19, undated).
- **Audible/ACX (secondary only):** several vendor and publisher posts say ACX's 2026-04-15 submission requirements need human narration unless Audible authorizes otherwise, and list unauthorized TTS and AI recordings as prohibited; sanctioned routes are KDP Virtual Voice and ACX Voice Replica. One vendor blog says the opposite, so unreliable. The ACX page is script-rendered and could not be read. **Sources:** search results (inkfluenceai.com, troubador.co.uk, 2026). Treat as unverified; tell the user to read ACX directly.

### Could not verify
- Audible/ACX primary text. Newgrounds guide text. Suno and Udio version-specific tells. Deezer 44% figure. Voice-coaching sources on breath placement. Audio engineers' studies on AI mastering.
