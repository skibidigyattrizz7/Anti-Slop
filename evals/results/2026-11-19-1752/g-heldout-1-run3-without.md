## Plan: Make the Grunt a Flanker

**Target:** the basic walking enemy (call it the Grunt). Change only this type so you can tell what caused any difference.

**Changes**

1. **Stop beelining.** Instead of moving straight at the player, the Grunt keeps a distance of about 200–260 px and orbits or strafes sideways. It only closes in when it's ready to attack. Start with 60°/s angular speed and tune from there.
2. **Telegraph the attack.** Before each attack, the Grunt stops, flashes, and holds for 0.6 s. Draw a faint aim line to the player's position at that moment. The player must be able to read the warning at a glance.
3. **Dash, don't hit.** The attack is a fast dash (about 600 px/s, 0.35 s) toward the position the player occupied when the telegraph started. It deals damage on contact.
4. **Punish window.** If the dash misses, the Grunt stays stunned for 1.0 s and takes double damage. Dodging becomes a chance to attack, not just a way to survive.
5. **Two hits to kill.** The Grunt takes two hits, with a brief stagger on the first. Players now have to make a choice between dodging and shooting, rather than just shooting.
6. **Pair spawns.** Spawn Grunts in pairs from alternating edges, with attack cooldowns offset so they don't telegraph in sync.

Start with 1–5 and tune the numbers in playtests. Add 6 only if the fights still feel thin.

## How you'll know it worked

**Before changing anything, record a baseline** with about 8–10 players on the same level:
- Average fight length against Grunts (seconds from first contact to kill or death)
- Per death, what killed the player (Grunt vs. other)
- Each player's fun rating (1–5) and the single thing they found boring

**Log these during the new playtest:**
- Dodge rate: dashes that missed / total dashes
- Punish rate: stunned Grunts killed during the stun window
- Hits taken from telegraphed attacks vs. from anything else

**It worked if most of these hold:**
- Median fight length rises to at least 4 s (from the baseline).
- Grunts account for 20–35% of deaths. Below that, players ignore them. Above that, they're just annoying.
- At least 70% of players, when asked, can describe the warning without being told what it is.
- Median fun rating rises by at least 1 point.
- Most player deaths to Grunts come from a dash the player saw coming. Few come from unreadable hits.
- Players report choosing between dodging and shooting, not just shooting.

**Red flags:**
- Players die to dashes they didn't see: the telegraph is too faint or too short. Lengthen it or make it more visible.
- Players stop attacking Grunts and just run from them: the punish window is too small, or the reward is too weak.
- Fights are longer but still feel flat: the problem may be the level layout or player abilities, not this enemy.

If the numbers miss, change one parameter at a time (telegraph length, dash speed, or stun duration) and run the same playtest again.
