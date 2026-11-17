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
