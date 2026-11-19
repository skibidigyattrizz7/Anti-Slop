## Plan: make the Shieldback worth fighting

**Target:** the one-hit enemy that walks straight at the player. Leave the other enemies alone for now.

**Core verb:** shooting. **Twist:** the enemy's front is armored, so you have to move to its side or back to hurt it.

### Behavior (replaces "walk straight in")
1. **Standoff:** it stops about 6 tiles from the player and strafes at 2.5 tiles/s while keeping its front toward you. It turns at 180°/s, so fast flanking beats it.
2. **Telegraph:** every 3.0 s (±0.5 s random), it winds up for 0.6 s. A ground ring grows, a rising whine plays, and its body leans back.
3. **Lunge:** it charges at 12 tiles/s for 0.3 s toward where the player was when the telegraph started. Contact hurts the player.
4. **Recovery:** 1.0 s with its back exposed. This is the only time it takes damage from every angle.

### Health
- 3 HP.
- Front shots (within ±45° of its facing) do 0 damage and spark off.
- Side and back shots do 1 damage.

### Feedback (answer every input)
- **Front shot:** spark, 30 ms hit-stop, metallic tick with ±8% random pitch.
- **Side or back hit:** 2-frame white flash, 0.3-tile knockback, 40 ms hit-stop, three small squashed sparks.
- **Kill:** 60 ms hit-stop, a bass-layered thump, about 20 particles, and a scorch decal that stays.
- **Lunge hitting the player:** 0.15 s screen shake that decays. No shake on the telegraph.
- **Telegraph:** ring and whine every time. Never silent.

### Tuning (change one number, play 10 attempts, log what you felt)
- Standoff distance: 4 to 8 tiles
- Lunge cooldown: 2 to 4 s
- Recovery window: 0.6 to 1.4 s
- Lunge speed: 9 to 15 tiles/s

### How you'll know it worked
Write these down before you playtest.

- **Readable telegraph:** after the first two encounters, the player is hit by a lunge in 30% or fewer of attempts.
- **Punishable recovery:** at least 60% of lunges are followed by a side or back hit during recovery.
- **Fight length:** median kill takes 8 to 15 s.
- **Blind playtest:** five people who haven't seen the plan play two levels each. Pass if at least four of them describe the enemy's pattern without prompting and start flanking without being told. Fail if they mostly stand and shoot from the front.
- **Quotes, not summaries:** after each session, ask what was the most tense or most annoying moment. Record their exact words.

### Technical checks (on your target device)
- Frame time stays under 16.7 ms (60 fps) with six Shieldbacks and their effects on the lowest graphics setting.
- Fewer than 50 particles spawn per hit.
- After a kill, no rings, sparks, or decals remain past their timers. Count the nodes before and after.

### Status
I haven't run or played anything. The working directory has no game project, so every number above is a starting value to tune. The playtest and frame-time results are still missing, and the plan is only a hypothesis until they come back.
