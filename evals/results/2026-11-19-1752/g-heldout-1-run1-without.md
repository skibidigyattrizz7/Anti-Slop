**Pick one enemy: the basic chaser ("grunt").** It's the most common enemy, so improving it changes the most fights.

**The change: give grunts a telegraphed lunge and a sidestep, and make them take two hits.**

1. **Approach with a sidestep.** Instead of walking straight at the player, the grunt moves toward a point offset about 60-90 degrees from the player's position, then switches to a direct approach when it's within 4 tiles. This makes it harder to track and forces the player to aim, not just hold fire.
2. **Telegraph, then lunge.** When the grunt is 3-5 tiles away and stops moving, it flashes or swells for 0.6 s (the wind-up). Then it dashes at about 3x its normal speed for 0.3 s in a fixed direction. Dodging the lunge should be a readable skill.
3. **Two hits to kill.** Grunts get 2 HP instead of 1. The first hit makes them flinch and drop their sidestep for 0.2 s, which rewards landing shots while they're close.
4. **Limit the lunge.** A grunt can only lunge if the player is in its line of sight, so it can't do a long cross-map charge.

**Implementation (about one day):**
- Add a `GruntState` enum: `Approach`, `Sidestep`, `WindUp`, `Lunge`, `Stagger`.
- Pick the sidestep side once when entering `Sidestep` (random, then kept) so grunts don't jitter.
- Tune constants in one config block: `SIDESTEP_ANGLE=75`, `WINDUP_S=0.6`, `LUNGE_SPEED_MULT=3`, `LUNGE_DURATION_S=0.3`, `HP=2`, `STAGGER_S=0.2`, `LUNGE_RANGE=3..5`.
- Add a wind-up visual (scale pulse or color flash) and a lunge trail so the telegraph is obvious.

**How you'll know it worked.** Set these checks before the playtest, and compare against the current build:

| Metric | Current (expected) | Target after change |
|---|---|---|
| Median fight length (first shot to last enemy dead) | Short, under ~5 s | 8-15 s |
| Player deaths to grunts per run | Low, or deaths come from being overwhelmed | Deaths come mostly from lunges the player failed to dodge (log the cause) |
| Grunt hits landed on player per encounter | Hard to read; log it | Under 2 per encounter, with dodges logged |
| Lunge dodge rate | N/A | 50-80%. Below 30% means the telegraph is too short or unclear. Above 90% means lunges are too easy to avoid. |
| Player fun rating (1-5, after each level) | Baseline from 5-8 players | At least 1 point higher on average, with no group rating below 3 |
| Qualitative | "Boring" comments | Players unprompted mention dodging, baiting, or the lunge |

**Playtest protocol:**
- Recruit 5-8 players. Have half play the old build and half the new build, or have everyone play both in a fixed order.
- Log timestamps for each shot, hit, lunge, and death. Use these to compute the metrics above.
- Ask one question after each level: "How fun was that fight, 1-5?" Then ask what they remember most.
- Stop and tune if median fight length is still short or the dodge rate is outside the 30-90% band. Those are the two numbers most likely to be wrong on the first pass.

**Success means:** the metrics move into their target ranges, the fun rating goes up, and players talk about the fight itself rather than only the level's layout. If the metrics improve but the fun rating doesn't, the lunge is probably too predictable, so raise the speed or add a random delay before the lunge.
