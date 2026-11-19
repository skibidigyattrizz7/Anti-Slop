## Plan: the Bracer, one new enemy

**Status: design only. Nothing was run.** Every number below is a starting value to be tuned by playing. None of them is tested. `[detail needed: engine, screen size, current Chaser speed, player bullet speed and fire rate, art style or palette]`. I wrote the numbers as ratios to the Chaser where I can, so they hold once you fill those in.

**What stays the same:** the Chaser, its straight-line walk, and its one-hit death are not touched. The Bracer is added next to it. It also dies in one hit, but only if the hit lands in the right place.

### The idea in one sentence
The Bracer walks straight at you holding a shield in front, so you can't just stand and shoot. You have to move to its side to kill it.

Core verb: shoot. The twist is that where you stand decides whether a shot counts, so the shot makes the player move.

### Behavior (starting values)
- Walks straight at the player like a Chaser, at about 0.8x Chaser speed. Slower is deliberate: it gives the player time to move around it.
- Shield covers a 120° arc in front. A shot that hits the shield does no damage. A shot that hits anywhere else kills it in one hit, same as every other enemy.
- Turns toward the player at a capped rate, about 90°/s. This is the number that makes flanking possible. Too slow and it is trivial, too fast and the shield is a wall. Tune it first.
- Placed by hand at first: one Bracer in a mixed group, not a room full of them. Spacing is uneven on purpose.

### Feedback (scaled to importance: a blocked shot is small, a kill is normal)
- **Blocked shot:** a one-frame white flash on the shield, a metallic "tink" with randomized pitch (a few different samples if you have them), a small spark burst at the impact point, and a slight shove back of the bullet's direction on the enemy.
- **Kill from the side:** same death as a Chaser plus a heavier thud layer, so a flank reads as a reward. Keep it modest. It is a common enemy.
- **Readability rule:** the shield is one bright, high-contrast shape on one side of the body, and the body's silhouette stays visible with the shield on. No effect may cover the enemy's body or the player's bullet path. If the spark burst hides the enemy, cut it.
- **Style:** the shield uses the existing palette. If there is no style bible, `[detail needed: palette and shape language]`. Any placeholder art is labeled as placeholder.

Platform limits (particle caps, draw budgets) not checked. Read the current docs once the engine is known.

### Tuning plan
Change one number, play, write down what happened, then change the next. Never two at once. Order:
1. Turn rate (start 90°/s).
2. Shield arc (start 120°).
3. Walk speed (start 0.8x Chaser).
4. Feedback layers, one at a time, keep the ones that help and drop the ones that feel like bugs.

### How to test it (nothing below has been run)
Unless a row says otherwise, run each check in a build with 1 Bracer plus 4 Chasers.

| Check | Pass threshold |
|---|---|
| Shield works | Run 20 trials of 1 shot each at the front arc from 300 px (fresh Bracer each trial): 0 kills. Run 20 trials from behind: 20 kills. Run 20 trials at the arc edge, ±5° inside and outside: the hit/miss split matches the arc. |
| One-hit death kept | Every hit outside the shield kills in 1 hit. Assert no Bracer survives a non-shield hit. |
| Flanking is possible | A tester (or a scripted bot that strafes) kills a lone Bracer from a 400 px start in under 6 s with no damage taken. If not, turn rate is too high. Starting target, tune it. |
| Not trivial | The same tester standing still and firing never kills it before it reaches them. If it does, the shield is not doing anything. |
| Doesn't hide the fight | In a stress wave of 5 Bracers, the player and every enemy stay visible in a screenshot at the smallest supported screen size. `[detail needed: smallest screen size]` |
| Frame time | Under 16.7 ms per frame (60 fps target, change if your target differs) for 10 s in a stress wave of 5 Bracers and 20 Chasers, with a burst of shield sparks, on the lowest quality setting. |
| Particles | Spark count on screen never over 50 at once (a starting cap, not a platform limit). `[detail needed: your particle budget]` |
| Cleanup | After clearing a wave, enemy, bullet and spark instance counts are back to the count before the wave. |
| Sound | Ten blocked shots in a row play with at least 3 different pitches or samples. |

**Player test, only after the checks above pass:** have 5 people play with the Bracer and without it, same setup. Record: how often they move before shooting, kills per minute, damage taken, and ask each one in their own words what the Bracer wanted them to do. Treat the results as notes. Five people is too few to prove anything, so use it to find problems, not to declare the enemy fun.

**If it fails:**
- Players stand still and get hit: shield feels fake or too wide. Reduce the arc first.
- Players ignore it and shoot the Chasers: it is too slow or too easy to avoid. Raise speed first.
- Flanking feels impossible: lower turn rate first.

Stop after two rounds on the same problem and report which check still fails and why.
