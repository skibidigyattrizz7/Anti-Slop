## t-a.md

```
Verdict: Ship      Score: 2/2 applicable checks pass (6 N/A, design only)
Category: games   Rubric: /home/user/anti-slop/skills/human-games/references/rubric.md

Checks:
G1 N/A   "I have not run this in Roblox. The numbers above are starting values for you to tune by playing, not tested results."
G2 N/A   VFX design, not a game or level; no core verb is required of it (the reply does state one: "throw and it hits hard")
G3 N/A   nothing was run or re-tested; the reply says the numbers are starting values
G4 PASS  "0.2 s before impact: a small dark ring ... a hard white flash ... a low thump ... a short camera shake"; readability: "Keep the explosion away from the player's crosshair and the enemy hitbox, so danger stays readable."
G5 N/A   no assets exist yet; palette is stated ("one hue family ... plus charcoal smoke") and placeholder flipbooks are flagged
G6 N/A   count is stated and within budget ("Total is 46 particles", 8+24+14 is correct); no engine stat run; platform caps not read ("I did not confirm Roblox's current per-second particle caps")
G7 N/A   no levels
G8 PASS  "a low thump at a randomized pitch" (repeated sound varies)

Top fixes (most important first, 5 at most):
1. Test section "Confirm the particle count with a quick script: `#emitter:GetChildren()` is not enough, so count the number of `Emit` calls" -> unclear, gives no assert and no limit -> state one concrete check, e.g. sum the Emit arguments per explosion and assert <= 60.
2. Test section "watch the frame rate in the Developer Console (F9) and the Microprofiler. Compare against an empty arena." -> no pass or fail threshold -> add a number, e.g. no frame spike above a stated ms during a burst.
3. "Check the phone-sized view on a mobile emulator, since the particle cap is lower there." -> stated as fact, then listed as unchecked -> reword as "may be lower, check the docs" in the test line.
4. Low-quality section -> only tests how it looks at level 1; no plan for what the effect does at low quality -> add a reduced emit count for low levels.

Could not check: whether the numbers look right in a running game; real Roblox particle caps and low-quality behavior; Roblox API details beyond what the reply states.
```

## t-b.md

```
Verdict: Ship      Score: 1/1 applicable checks pass (7 N/A, design only)
Category: games   Rubric: /home/user/anti-slop/skills/human-games/references/rubric.md

Checks:
G1 N/A   "the numbers are untested on a device" (no test is claimed)
G2 N/A   VFX design, not a game or level; no core verb stated
G3 N/A   nothing was run or re-tested
G4 PASS  "Flash ... Fireball ... Sparks ... Smoke ... Debris", layered and sized by importance; readability is not discussed, but nothing hides the enemy or hitbox
G5 N/A   no assets exist yet; no style or palette is stated beyond per-layer colors
G6 N/A   count is stated and within budget ("18 + 20 + 12 = 50 particles"); no engine stat run; platform limits not mentioned or read
G7 N/A   no levels
G8 N/A   no sound is designed, so there is no repeated sound to vary

Top fixes (most important first, 5 at most):
1. Layers list -> no sound or camera feedback, so the blast is visual only -> add a thump with random pitch and a short shake.
2. "Explosions still read as explosions, and the flash and smoke carry the look." -> an untested claim stated as fact -> mark it as an expectation to check at level 1.
3. "Read `UserSettings().GameSettings.SavedQualityLevel.Value` once. At levels 1 to 3, halve each emit count" -> level cutoffs and the API are not checked against current docs -> add a docs check, and say it only works on the client.
4. Layers list -> no rule for keeping crosshair and hitbox readable -> add one line.

Could not check: whether the numbers look right in a running game; the 33 ms threshold; Roblox API and quality-level behavior.
```

Better: t-a.md, because on the one applicable-check difference it covers layered feedback including a varied-pitch sound and an explicit hitbox-readability rule, which t-b.md omits. t-b.md has the stronger test plan (assert, 33 ms threshold, quality-scaled emit counts, cleanup check).

## Rubric notes

- G1 is "must-pass" but the brief says nothing was run, so it is N/A for both. The verdict rule does not say what to do when G1 is N/A. I used "Ship if no applicable check fails", which is lenient.
- G2, G3, G5, G7 are about whole games or built assets. They are N/A for a VFX design, so 6 to 7 of 8 checks are N/A. The rubric cannot separate these two replies on most rows.
- G4 PASS for t-b.md is close to the line. "Layered" is met, but "action stays readable" is only met by absence of a problem.
- G6 asks for a mesh or engine stat and docs-read limits. A design reply can be within budget by arithmetic but cannot meet it. t-a.md honestly flags the unread caps and t-b.md is silent; the rubric gives no credit for that honesty.
- G8 mixes sound and UI. Sound variation counted only for t-a.md because it mentions sound at all, which rewards scope more than quality.
- No check scores whether the test plan is concrete (pass thresholds, asserts, cleanup). That was the main difference the user asked about and the rubric does not capture it.
- `check_mesh.py` is for .obj files and had nothing to run on here.
