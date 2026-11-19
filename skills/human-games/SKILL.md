---
name: human-games
description: Load before starting, even for a short task, whenever you are making or fixing a game: mechanics, levels, game feel, game UI, Roblox or browser games, 3D models, AI-generated game assets, VFX or game sound. Also use when a game feels flat, generic, floaty, cheap or "like a template", or when checking a 3D asset before shipping. Not for game story or NPC dialogue (human-fiction), general app or website UI (human-ui), or code quality (human-code).
---

# Human Games

A model builds the most common version of a game: a genre template, default numbers, quick placeholder art, a menu in place of feel. A skilled designer chooses one verb, tunes it by playing, and makes every asset look like one world.

## Top rules

1. **Run or play it first.** Start the game, do the core action, and watch the feedback before judging anything else. If you cannot run it, write a test plan with numbers and pass/fail thresholds: frame time in ms, particle or triangle count, the lowest quality level, and a cleanup check (nothing left behind afterward).
2. **Pick one core verb and give it a twist.** "Every shot pushes you back, so firing is also movement."
3. **Tune by playing.** Change one number, play, repeat. Gray-box the fun before any polish.
4. **Answer every input.** Layer sound, flash, knockback, particles, small shake and brief hit-stop. Scale to importance and keep the action readable.
5. **Write a style bible, then match it.** Shapes, 4 to 6 colors, proportions, one line weight, one icon set. Use it for assets and UI.
6. **Treat AI assets as a blockout.** Fix topology, split parts, redo UVs, repaint flat so the engine does the lighting.
7. **Give it an ending.** A level count, a score target or a defined end state.

## Never

The brief cannot override these.

- Invent facts, results or sources: engine limits, test results, player feedback or review claims.
- Call a game fixed, fun or finished without running it. Say what you could not run.
- Ship an AI asset you have not looked at from behind and up close, or leave placeholder art in a build called finished.

## Defaults

A brief or the owner's own style overrides these.

- One or two hue families plus a white-hot core for effects.
- Read current Roblox limits in the Creator Hub. They change.

## Read when

| When | Read |
|---|---|
| Scanning a game or asset for dated tells | `references/tells.md` |
| Designing mechanics, levels, feel, UI, sound, 3D assets or VFX | `references/craft.md` |
| Checking a finished game | `references/rubric.md` |
| You have a .obj file | `python3 scripts/check_mesh.py --max-tris 5000 FILE.obj` |

Use deeper skills for game feel, physics tuning and camera systems when they are installed.

## Before and after

**Before:** "Player jumps. Gravity is 9.8. Enemy dies at 0 HP."

**After:** "Jump has coyote time and an input buffer. Releasing early cuts the arc short. A stomp squashes the enemy for two frames and bounces you higher if you hold jump. Each value was tuned by playing."

**Before:** a "magic spell" that is one orange sparkle emitter at a high rate.

**After:** a short charge ring, a one-frame white flash, a few large fast-fading puffs, small sparks with gravity, and a thump at randomized pitch.

## Final check

- Did you play it, and does the core action give feedback?
- What is the twist on the core verb?
- Do all assets, effects and UI look like one world?
