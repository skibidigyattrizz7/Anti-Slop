## Plan: make the Weaver fun

**Target:** The basic chaser enemy. Call it the **Weaver**. It's the enemy most players meet first and encounter most often, so it has the most effect on how fights feel.

**Problem:** It moves in a straight line, so the player only has to hold still or move in one direction. One hit kills it, so the player never has to think about the fight.

**Change:** Give the Weaver three behaviors that require a response.

1. **Approach on a weave.** Instead of walking straight at the player, it moves toward them along a sine wave: amplitude about 60 px, period about 1.2 s. The player has to track its path and can't just stand still.
2. **Keep distance and shoot.** It stops at a preferred range of about 180 px and fires a single shot. Before firing, it telegraphs for 0.5 s with a flash and an aim line. The player gets a clear window to move out of the line.
3. **Two hits to kill.** HP goes from 1 to 2. The first hit makes it stagger and drop its telegraph. This gives the player a reason to keep shooting at it and makes it a real target instead of a single-tap pickup.

Leave the other enemy types as they are for now. Changing one enemy at a time makes it clear what caused any difference.

**Implementation (about one day):**
- Add a state machine with three states: `approach`, `aim`, `recover`.
- Expose the weave amplitude, period, preferred range, telegraph duration, and HP as constants so you can tune them without code changes.
- Add a placeholder aim line and flash so the telegraph is visible.
- Keep the old chaser available behind a flag so you can A/B test.

**How you'll know it worked:** Run a playtest before and after the change with at least 6 players, each playing the same 3-minute level. Record the following.

| Metric | How to measure | Pass target |
|---|---|---|
| Fun rating | Ask "How fun were the Weaver fights, 1–5?" after the session | Median ≥ 4, up from baseline |
| Dodge rate | Shots the player avoids ÷ total Weaver shots | 35–75% (near 0% means unfair; near 100% means boring) |
| Fight length | Seconds from first Weaver spotted to its death | Roughly 1.5–3 s, up from under 0.5 s |
| Damage taken | Fraction of Weaver encounters where the player takes damage | 40–80% |
| Unprompted feedback | Players mentioning the Weaver without being asked | At least half of players mention it, and most of those comments are positive |

**Decision rule:** Keep the change if the fun median and dodge rate both hit their targets and no more than one playtester calls it unfair. If the dodge rate is too low, lengthen the telegraph to 0.7 s. If the fights are too easy, reduce the preferred range or increase the weave amplitude. Change one value at a time and retest.

**Caveat:** With six players these results are directional, not statistical. Treat a clear miss on any target as a real signal, but treat a near-miss as a reason to test again, not a conclusion.
