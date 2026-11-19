## Plan: make the Shield Walker a flanking enemy

**Core verb:** aiming. The player lines up shots. The twist is that this enemy has a front shield, so the player has to move around it to fire.

**Enemy: Shield Walker** (replaces the current walker in one room type first)

1. **Movement:** Don't walk straight at the player. It keeps a ring about 220 px from the player and strafes around it. It changes direction every 1.2 to 2.0 s (randomized). Speed is 90 px/s, and it speeds up to 150 px/s when it gets close.
2. **Shield:** It blocks shots from a 90° arc in front of it. Blocked shots do 0 damage and show a spark. The shield faces the player's position, but it takes 0.4 s to turn, so a player who moves fast gets a window to hit its back.
3. **Damage:** Back hits do 2 damage. The enemy has 4 HP, so two back hits kill it. Side hits do 1 damage.
4. **Telegraph:** Before it fires, it stops for 0.45 s, the shield flashes, and a thin aim line appears. Its shot does 1 damage to a player with 4 HP.
5. **Feedback per hit:** a one-frame white flash on the enemy, a short sound with randomized pitch, a small knockback, and a 3 px shake for about 0.1 s. A kill gets a 35 ms hit-stop and a larger pop. A blocked shot gets a spark and a dull "tink," with no shake.
6. **Placement:** Put 1 to 2 of these in a room with a normal walker. Don't put them in evenly spaced rows.
7. **Ending:** Level 3 has a finish line: clear the room with a shield walker, then reach the exit.

**Tuning order:** Change one number at a time and play after each change. Tune the turn time (0.4 s) first, then the strafe ring radius, then the shield arc.

## How you'll know it worked

I haven't run your game. Your project isn't in this working directory, so I can't check any of this against real play. Treat the numbers below as the test plan.

**Before you change anything, record a baseline:**
- Average time from first contact to kill for this enemy.
- Percent of fights where the player took damage from it.
- Percent of player deaths caused by it.

**After the change, play 10 runs and record:**
- **Wasted shots:** shots that hit the shield, as a share of all shots at this enemy. Pass: 20% to 35%. Above 50% means it's frustrating. Below 10% means the shield does nothing.
- **Time to kill:** should go up from baseline but stay under about 6 s per enemy. If it goes higher, the shield is too strong.
- **Flank rate:** share of kills that came from the back. Pass: 40% or more.
- **Player description:** ask 5 people to describe what they did in one sentence after a fight. Pass: at least 3 of 5 mention moving around the enemy or lining up its back without being told.
- **Performance:** frame time stays under 16.6 ms at 60 fps on the lowest graphics setting. Check the cleanup too: no shield, aim line or particles remain after the enemy dies.

**It worked if** the flank rate passes, the player description passes, and the wasted-shot share is in range. If players still say fights are boring after these pass, the problem is elsewhere (pacing, enemy count), and this plan won't fix it.
