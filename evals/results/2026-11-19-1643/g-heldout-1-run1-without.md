## Plan: make the Chaser enemy more fun

**Target:** the basic melee enemy that walks straight at the player and dies in one hit. It's the most common enemy, so it sets the feel of most fights.

**Problem:** It has one behavior (straight-line approach) and no decisions for the player to make. Dying in one hit means the player never has to read or respond to it.

### Changes

1. **Approach with a weave instead of a straight line.** Move toward the player while adding a sine-wave sideways offset: amplitude about 40 px, period about 1.2 s, base speed about 110 px/s. The player has to track its path, not just wait for it to arrive.

2. **Add a telegraphed lunge.** When the enemy gets within about 250 px, it stops, flashes, and draws an aim line for 0.6 s, then dashes at about 450 px/s for a short distance. A dash the player can see coming is a dodge opportunity. A dash they can't see is just unfair.

3. **Take two hits to kill.** Change HP from 1 to 2. The first hit should cause a visible reaction (knockback and a brief stagger). This makes a hit feel like it did something and gives the player a reason to keep shooting.

4. **Make the death matter.** On death, the enemy releases 4 slow projectiles in a ring. This makes killing it up close a small risk, so players think about where they fight it.

Keep the other enemy types unchanged so this is the only variable.

### How you'll know it worked

**Before the change (baseline):** Run 5 playtests and record:
- Deaths caused by this enemy per run
- Average time to clear a room with it present
- Player fun rating, 1–5, asked right after the session

**After the change:** Run 5–8 new playtests with the same setup and check:

- **Fun rating:** median is at least 4/5, and at least 1 point higher than the baseline median.
- **Readable fights:** at least 4 of 5 players can say what they did to dodge or counter the lunge, without prompting. You can ask this in the interview or check in video recordings.
- **Reasonable damage:** players take 1–3 hits from this enemy per encounter. If it's 0, the lunge is too easy to avoid. If it's over 4, it's too punishing.
- **Engagement:** players deliberately fight it (shoot first, reposition) instead of just standing still. Count how often they do this in recordings.

**Failure signals:** players say the lunge feels unfair, complain that the weave makes it hard to aim, or the fun rating doesn't move. If so, widen the telegraph to 0.8 s, reduce the weave amplitude to 25 px, and retest with the same protocol.

Start by changing only the weave in step 1 and retesting, if you want to isolate its effect. Otherwise, implement all four changes together and tune from the playtest data.
