## Plan: make the basic grunt a flanker with a telegraphed shot

**Target:** the basic grunt, the most common enemy. It is the one that currently walks straight in and dies in one hit.

**Core verb:** shooting while moving. The grunt is built to punish standing still, so the player has to keep sidestepping and shooting.

### 1. Behaviour (replaces "walk straight at player")
- Hold a preferred range of 6 tiles from the player. Move sideways around the player at 3.5 tiles/s, and only close in or back off to stay near that range.
- Every 1.8 s (±0.3 s random), stop and raise a short arm. A red line on the ground shows the aim for 0.5 s. Then it fires a slow orb (about 4 tiles/s) at where the player was.
- Changing direction costs it 0.2 s, so it cannot track the player perfectly.

### 2. Health and hit feedback
- 2 hits to kill, so the first hit matters.
- **Hit 1:** white flash for 2 frames, 40 ms hit-stop, 0.3-tile knockback, and a low thump at randomized pitch. It enters a 1.0 s stagger: no shooting, no strafing, and it is open to free hits.
- **Hit 2 (death):** squash for 2 frames, a scorch decal that lingers, a small screen shake that decays over 0.3 s, and a higher pitched thump.

### 3. Readability
- The red aim line and orb must stay visible over the other effects. If the flash or particles hide either one, cut the particles first.

### 4. Starting numbers (tune these by playing)
Change one at a time and write down what you felt:
- Strafe speed 3.5 tiles/s, preferred range 6 tiles
- Windup 0.5 s, cooldown 1.8 s ±0.3 s
- Hit-stop 40 ms, stagger 1.0 s

I have not run the game. No game project was present in the working directory, so these values are untested starting points.

## How you'll know it worked

Compare the old and new grunt on the same map and the same number of enemies.

**Measured in play (10 fights each, old vs. new):**
- Player movement: the player moves for at least 60% of each fight, up from whatever the old baseline shows. Log this from input or position data. If it stays under 40%, the flanking is not doing its job.
- Fight length: an encounter with 3 grunts lasts 8–15 s. If it is under 5 s, the enemies are too weak. If it is over 25 s, they are too tanky or the shots are too slow.
- Damage taken: the player takes 1–3 orb hits per encounter. Zero means the threat is too low. More than 5 means the windup is too hard to read.
- Readability: in a screenshot or recording, the aim line is visible in every fight frame where it should be.

**Performance:**
- Frame time stays under 16.7 ms (60 fps) with 10 grunts and their effects on the lowest graphics setting. Test on the lowest and highest settings.
- After a fight, no orbs, decals or particles are left behind. Count them before and after.

**Playtesting:**
- Get at least 5 people to play the new version, without telling them what changed. Ask them to describe the grunt in their own words.
- It works if at least 3 of 5 mention dodging, sidestepping or the aim line without prompting. If fewer mention it, the behaviour is not readable enough. Change one number (usually the windup) and test again.
- Do not record the result as "fun" from the fight count alone. The playtester's own description is the evidence.

**Decision:** if the measured criteria pass and the playtesters mention dodging unprompted, the change worked. If only the numbers pass, keep tuning. If neither passes, the twist is not strong enough, so revisit the core verb before adding more polish.
