# AI tells and craft: games, 3D, interactive prototypes

Status: partial. Web search hit rate limits after 6 queries and 3 fetches. Only items with a source below are verified. Everything marked **[unverified]** is from memory and must be checked before use.

## Sourced findings

### Tell: jam output is now mostly multiplayer or idle loops with similar scope
- **Tell:** Vibe Jam 2026 entries cluster in competitive brawlers, arena and .io-style games, plus idle/progression loops. Many titles riff on "vibecoder" themes.
- **Why it reads as AI:** The AI-written rule (90%+ code) favours small, well-known genre templates that a model can produce quickly. Similar scope gives similar games.
- **Fix / craft move:** Pick a genre with a clear, fast core loop and one distinctive rule. Keep the core verb to something a player understands within seconds.
- **Source:** [Colyseus, "Vibe Jam 2026"](https://colyseus.io/blog/vibe-jam-2026/), 2026 (post-jam, vendor promo, pattern read from titles, not stated by the author). Model era: not stated. Rules and counts: 945 submissions, one month, 90%+ AI-written code, browser-playable.

### Tell: polish claims are not the same as game feel
- **Tell:** Entries were described as "more polished than 2025" and with "progression and persistence", but the same source does not report on juice, feedback or edge cases.
- **Why it reads as AI:** Progression systems and menus are cheap to generate. Feel (hit response, feedback, timing) takes tuning by hand, so it is what usually goes missing.
- **Fix / craft move:** Count "fake polish" (menus, shops, save screens) against "feel" (does each action answer back?). Spend time on the second.
- **Source:** [Colyseus, "Vibe Jam 2026"](https://colyseus.io/blog/vibe-jam-2026/), 2026. Note: the post does not report failures, so this tell is an inference, not a finding.

### Tell: jam winners show low-effort art and a single hook
- **Tell:** Idle and tactics games with minimal art win first place.
- **Why it reads as AI:** Judges reward a clear hook over visual craft at this scale, so the AI default (quick placeholder art) is not penalised.
- **Fix / craft move:** Make one visual choice on purpose (one palette, one line weight, one font) and apply it everywhere, including the UI.
- **Source:** [IT Brief, "VibeBlitz game jam crowns Idle Tactics"](https://itbrief.co.uk/story/vibeblitz-game-jam-crowns-idle-tactics-as-first-winner), date not confirmed. VibeBlitz: 72 submissions, 250+ participants. Winning-entry visual quality was not checked.

### Tell: the same "single-screen toy" format keeps coming back
- **Tell:** Short browser games that feel like a prototype with no clear ending.
- **Fix / craft move:** Give the prototype a finish line: a level count, a score target, or a defined end state.
- **Source:** [Summer Engine, "Cursor Vibe Jam 2026 guide"](https://www.summerengine.com/blog/cursor-vibe-jam-2026-guide), 2026. Advice: scope to one core mechanic understood in seconds; keep the build light so it loads fast. Prize and count figures on that page are not verified.

### Game feel / juice: concept sources
- **Claim:** Juice is the tactile response to player input. The "Juice it or Lose it" talk (Martin Jonasson and Petri Purho, GDC Europe 2012) shows that small effects added to a plain game change how satisfying it feels. [GDC Vault](https://gdcvault.com/play/1016487/Juice-It-or-Lose). **Possibly outdated** (2012).
- **Claim:** Folmer Kelly's "Don't Juice It or Lose It" (GDC Europe) argues that too much polish breaks immersion. [GDC Vault](https://gdcvault.com/play/1020937/contactUs). **Possibly outdated** (date not checked).
- **Claim (unverified fetch):** Lisa Brown's "The Nuance of Juice" (2016) argues you should pick juice for the experience you want, not add it everywhere. Seen in search results only; the page was not read. **Possibly outdated.**
- **Attribution warning:** Some sites credit Jan Willem Nijman with "Juice it or Lose it." His talk is "The Art of Screenshake" (GDC 2013). Keep these separate.
- **Gap:** I could not retrieve the screen-shake numbers from "The Art of Screenshake." Do not quote figures from memory.

### Three.js / 3D: default look
- **Tell:** Flat uniform ambient light, no shadows, default colours.
- **Why it reads as AI:** The Three.js manual notes that uniform ambient light does not look like lighting; it only stops darks going fully black. Without shadows, objects float.
- **Fix / craft move:** Use a key, fill and rim light arrangement. Add an HDR environment map for image-based lighting. Turn on shadows and wire them up (they are off by default).
- **Source:** [threejs.org manual, lights](https://threejs.org/manual/en/lights.html), date not stated, **possibly outdated** in parts.
- **Version note:** Physically based light units became the default in r155 and later [unverified version number, check the Three.js changelog]. Old intensity values can look dim or blown out. Colour management changed in r152 ([Three.js forum](https://discourse.threejs.org/tags/lighting)).

## Gaps (could not verify this session)

- **Steam AI disclosure policy:** Could not retrieve current Valve documentation. Search was rate-limited. From memory: disclosure became mandatory in early 2024, with a split between pre-release AI content and live-generated content. **[unverified]** Check the Steamworks documentation directly.
- **Player and reviewer complaints about "AI slop" on Steam or itch.io:** not found.
- **Jam organiser rules on AI disclosure:** only the Vibe Jam rules (90%+ AI code) were found.
- **GDC postmortems and talks on AI-assisted development:** not found.
- **Game Maker's Toolkit, Swink's *Game Feel* (2008), Vlambeer postmortems:** not fetched. Swink's book is widely cited, possibly outdated.
- **Concrete juice numbers** (shake amounts, hit-stop frames, coyote time, input buffer windows): not verified. The gamejuice.pages.dev article is a coming-soon page with no content.

## Craft principles

Sourced:
- Choose one core loop and one distinctive rule before any content. (Vibe Jam: scope rule; Summer Engine guide.)
- Feel comes from response to input, not from features. (Jonasson and Purho, 2012.)
- Use juice selectively, matched to the experience you want. Too much hurts immersion. (Kelly, Brown.)
- Light your 3D scene deliberately: key, fill and rim, environment map, shadows. (Three.js manual.)

Unsourced, from training knowledge **[unverified, check before use]**:
- Give every input an immediate response: visual, audio, and a small camera or scale reaction.
- Telegraph enemy and hazard timing so the player can read it.
- Tune numbers by playtesting, not by reasoning alone.
- Use one palette, one line weight and one icon set across the game and its UI.
- Replace all placeholder art and text before calling the build done.
- Provide an ending or goal so a prototype reads as a game.

## Second pass 2026-11-19

Method: pages opened with WebFetch; snippets not trusted. Format: Tell or fact / Fix / Source.

### Steam AI disclosure (verified)
- **Fact:** The Steamworks Content Survey has an AI section. It covers AI content that ships with the game and that players consume (art, sound, narrative, localization). Efficiency tools are explicitly "not the focus". Two classes: pre-generated (judged like any non-AI content) and live-generated (same, plus the developer must describe guardrails that stop illegal content). Adult-only sexual content with live-generated AI is not allowed "at this time". Page has no date. Survey answers cannot be edited after approval without Steam Support.
- **Fix:** Disclose AI art, audio, text, capsule and marketing images that players see. No need to list code helpers.
- **Source:** https://partner.steamgames.com/doc/gettingstarted/contentsurvey (opened 2026-11-19, undated).
- **Fact:** Valve rewrote the guidance around 2026-01-16 to 2026-01-20, first revision since 2024. Dev-time tools such as code helpers no longer need disclosure; AI-made marketing, concept and in-game content still does. Enforcement is by trust, not moderation. Source: https://gigazine.net/gsc_news/en/20260120-steam-updates-ai-disclosure-guidelines (opened 2026-11-19; secondary, but matches the primary page). The PC Gamer article body did not load, so only its headline was seen.
- **Fact (uncorroborated, not used):** one blog claims mandatory asset-level AI tags from June 2026. No second source found.

### Player and reviewer reaction (2026)
- **Tell:** AI key art and capsule images make players skip a demo. Quotes: "I don't feel very compelled to check out demos with AI art capsules"; Mike Rose: "the amount of AI key art is insane". Players sort by popularity and reviews to avoid the flood. **Fix:** Commission or hand-make the capsule and key art; it is the first thing judged. **Source:** https://kotaku.com/steam-next-fest-feb-2026-gen-ai-art-demos-2000673280 (2026-02-24).
- **Caveat:** Developers report being review-bombed as "AI slop" with no evidence, and the article cites no specific signs players use. So "slop" is often a gut label. **Source:** https://creativebloq.com/ai/ai-slop-has-become-a-harmful-insult-hurled-around-with-no-evidence-game-developers-claim (2026-06-29).
- **Not verified:** sales or review-score studies (Game Oracle, 53% weaker first month) came only from aggregator snippets.

### Game feel numbers (verified from primary code)
- **Fact:** Celeste's coyote window is `JumpGraceTime = 0.1f` (0.1 s, 6 frames at 60 fps). Dash start calls `Celeste.Freeze(.05f)` (0.05 s, 3 frames at 60 fps). Ceiling variable-jump grace .05 s; variable jump time .2 s. Wall hit shake `DirectionalShake(..., .1f)` is 0.1 s. Jump input uses `Input.Jump.ConsumeBuffer()`, but the buffer window value is not in Player.cs, so not verified. **Source:** https://github.com/NoelFB/Celeste/blob/master/Source/Player/Player.cs (raw file read 2026-11-19, grep).
- **Fact:** Maddy Thorson's article names coyote time, jump buffering and lift-momentum storage but gives no frame counts; her numbers are pixels (wall jump from 2 pixels away, 5 for super wall jump, in a 320x180 game). **Source:** https://maddymakesgames.com/articles/celeste_and_forgiveness/index.html (undated).
- **Fact:** A Godot tutorial uses 6 frames (0.1 s) for coyote time with no source. **Source:** https://kidscancode.org/godot_recipes/4.x/2d/coyote_time/index.html. Treat 0.1 s as a starting point, not a standard.
- **Fact:** Vlambeer's Nijman talk adds screen shake opposite to gunfire and a 33% chance enemies explode harmlessly; about 30 tweaks in about 45 minutes. No shake size or hit-pause frames given in the write-up. **Source:** https://gamedeveloper.com/design/vlambeer-co-founder-shares-advice-on-building-better-action-games (2014-01-02).

### Could not verify
- Swink's 100 ms response threshold (secondary sites only; book not read). Hit-stop frame counts from a named talk. Jump buffer window from a named source. GMTK numbers (search returned none). Sales studies on AI games.
