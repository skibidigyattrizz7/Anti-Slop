# Plan: make the Drifter enemy fun

**Core verb:** shoot. **Twist:** the Drifter's shot is telegraphed, and the player can interrupt it by shooting the Drifter during its wind-up. Shooting becomes both the way you fight and the way you dodge.

## Enemy behavior (starting numbers, to tune by playing)

- **Movement:** it never walks straight at the player. It orbits at 4 to 5 tiles from the player, switching direction every 1.5 to 2.5 s (randomized). Speed 2.5 tiles/s.
- **Attack:** every 3 to 4 s it stops, turns toward the player, and draws a thin red aim line for a 0.6 s wind-up. Then it fires one slow bolt (6 tiles/s) along that line. The aim line does not track after the wind-up starts.
- **Interrupt:** one hit during wind-up cancels the shot and staggers it for 1 s. The stagger is the reward for aiming well.
- **Health:** 3 hits from the basic gun, so a single hit does not kill it. Kill it on the second or third hit with a short hit-stop and a small death burst.
- **Spawn:** 2 to 3 Drifters per room, placed by hand so they do not sit on an even grid.

## Feel (answer every input)

- **Shot telegraphed:** the aim line flickers on the wind-up, plus a rising whine.
- **Hit on Drifter:** white flash for 2 frames, 40 ms hit-stop, a low thump at randomized pitch, knockback scaled to damage.
- **Interrupt:** a brief sharp sound and a bigger flash, so the player notices the reward.
- **Player hit:** short screen shake that decays over about 0.3 s. Keep it small so it does not hide the bolts.
- **Readability:** the bolt is a round, bright-edged shape in one hue family. The aim line stays visible above the floor, not hidden by particles.

## Scope

One enemy, one room type, one arena. Once this works, the other enemies can use the same interrupt rule.

## How you'll know it worked

Run 20 encounters with the Drifter in an arena, then check these:

| Measure | Pass | Fail means |
|---|---|---|
| Encounter length (first sighting to all Drifters dead) | 8 to 15 s | Under 5 s: too easy. Over 25 s: boring. |
| Interrupts per encounter | 1 to 3 | 0: the telegraph is too short or the player never sees it. |
| Bolt dodge rate (bolts that miss the player / bolts fired) | 40 to 70% | Above 85%: the bolt is too slow. Below 25%: the telegraph is not readable. |
| Deaths caused by a Drifter bolt where the aim line was visible | At least 80% of deaths | Lower means the player died to something they could not see. |
| Hits per Drifter kill (average) | 2 to 3 | Always 1: one-shot problem still exists. |
| Can a playtester describe the pattern after one encounter? | 3 of 5 playtesters | Fewer means the pattern is too subtle. |

**Pass condition:** all rows pass on the first 10 encounters, and the playtesters' description matches what the telegraph and orbit actually do.

**Cleanup check:** after 20 encounters, no bolts, particles, or aim lines remain in the scene. Check the object count before and after the run.

**Performance check:** frame time stays under 16.7 ms at the lowest graphics setting with 3 Drifters and 10 bolts on screen.

## Limits

I have not run your game. I don't have its code, so these numbers are starting points, not tested values. The first real job is to play 20 encounters, change one number at a time (telegraph length, orbit radius, bolt speed), and record what you felt. Until that is done, do not call the Drifter fun or finished.
