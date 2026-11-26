# Senior layer: games

Use for a full project or a senior review. It adds to the other references. Each rule gives the rule, why, a check, and a tag. `[verified: SOURCE]` means the source was opened. `[practice]` is common professional practice: teach it as a rule of thumb, never as a fact.

## Design from the aesthetic

- **Write the target aesthetic first.** MDA: the designer builds mechanics, which give dynamics, which give aesthetics; the player meets them in reverse. Pick 1 or 2 of the 8 (sensation, fantasy, narrative, challenge, fellowship, discovery, expression, submission). Why: it tests each mechanic against a feeling. Check: cut any mechanic that serves none. `[verified: http://users.cs.northwestern.edu/~hunicke/MDA.pdf]`
- **Write the loop as one sentence.** "The player does [verb] to get [goal] under [pressure]; failure costs [retry]." Check: a stranger can say it back after one minute. `[practice]`
- **Fix input lag before juice.** The core verb shows a visible response within about 100 ms (6 frames at 60 fps). Check: film at 60 fps and count frames from press to change. `[verified: threejs-gameplay-systems/references/game-feel.md, local]`

## Forgiveness mechanics

- **Widen windows in the player's favour, quietly.** Celeste constants from its source: jump grace 0.1 s, variable jump 0.2 s, upward corner correction 4 px, dash corner correction 4 px. Why: the game feels fair because the code is generous. Check: expose each as a named constant and change it while playing. `[verified: https://raw.githubusercontent.com/NoelFB/Celeste/master/Source/Player/Player.cs]`
- **Add a jump buffer, but tune it by feel.** Celeste buffers jump input; this review did not find a length, so do not quote one. Start at a few frames and test. `[practice]`
- **Name the feeling, then the knob, then what moves.** "Forgiving jump: raise grace from 0.1 s and feel the change." Check: one constant changed per test. `[practice]`

## Playtest protocol

- **Watch, do not explain.** Watch hands and faces. Give a goal ("reach the flag"), never a verb ("try the dash"). Note the first confusion, the first death cause and the quit point. Ask afterwards: "what did you think you were meant to do?" Check: you said nothing leading. `[practice]`
- **Use about 5 fresh testers per round.** A moment that stops 2 of 5 gets fixed, then retest with new people. This is a rule of thumb, not a statistic. `[practice]`
- **Hit-stop and juice come in small amounts.** Nijman's talk describes a roughly 20 ms pause on impact, bigger bullets, knockback, muzzle flash and a smoothed camera. Check: add one effect at a time and replay. `[verified: https://www.youtube.com/watch?v=AJdEqssNZ-U]`

## Difficulty and flow

- **One new variable per level.** Speed, density or combination, never all three. Check: each level's change list has one item. `[practice]`
- **Pressure, then release.** Never two peaks back to back. Check: plot intensity per 30 s; there are valleys. `[practice]`
- **Find spikes by deaths.** A section with about 3 times the deaths of its neighbours is a spike, not a ramp. The 3 is a starting rule of thumb. `[practice]`
- **First use of a mechanic is safe.** Teach where failure is harmless. Check: a tester does the verb within 60 seconds with no text. `[practice]`

## Economy checks

- **Model sinks and faucets in a spreadsheet before tuning.** Check: first upgrade in a few minutes; no currency piles up unspent past about 2 upgrade costs; the best buy is not obvious. These numbers are starting points. `[practice]`

## Vertical slice and scope

- **Finish one minute at final quality** (art, audio, UI, feel) before making more content. Why: it proves the pipeline early. Check: one representative scene with real assets. `[practice]`
- **Write non-goals for the slice.** Check: the list exists and is short. `[practice]`

## Performance budgets

- **Measure, never assume.** Frame time at 60 fps is 16.67 ms (33.3 at 30). Aim for 10 to 12 ms for headroom. `[practice]`
- **Starting contracts from one author.** The threejs-aaa-graphics-builder skill sets desktop / mobile limits: draw calls 300 / 150, triangles 750k / 300k, textures 60 / 40, shadow lights 2 / 1. They are that author's starting points, not a standard. Check: read `renderer.info` at the worst view. `[verified: threejs-aaa-graphics-builder/references/technical-art.md, local]`

## Build on

Use when installed. Each has an inline fallback.

- `game-feel` (Apache-2.0): tiers, trauma-squared shake. Fallback: layer 5 to 8 responses.
- `physics-tuning` (Apache-2.0): fixed step. Fallback: play at 30 and 144 fps; jump height must match.
- `camera-systems` (Apache-2.0): smoothing. Fallback: frame-rate independent smoothing, a deadzone.
- `threejs-game-director`, `threejs-gameplay-systems`, `threejs-aaa-graphics-builder`, `threejs-game-ui-designer` (MIT): scope, loop, budgets, HUD. Fallback: this file.
- `motion-design` (MIT), `brandkit` (MIT), `canvas-design` (Apache-2.0): motion timing, style boards, art direction.
- `animation-forge`: no licence found. Link only.
- Unity skills (Unity Companion License): ideas only.

## Credits

No text copied. Celeste constants are read from its MIT-licensed source; budgets are cited, not reproduced.
