# Games rubric

Used by the judge agent and for self-checks. Each check is PASS, FAIL or N/A. A FAIL needs evidence: what you did, saw or measured. Check in this order, every time.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| G1 | Played and works (must-pass) | The game was run or played, the core action works, and it gives visible or audible feedback. The report says what was tested | It was not run, the core action fails or gives no feedback, or the review only read code |
| G2 | Core verb | One core verb is stated in a sentence and has a twist or a theme-driven rule | It is a stock template (collect, dodge, timer) and the theme changes no rule |
| G3 | Tuning | Key numbers (speed, gravity, jump, damage) were changed and re-tested, and the notes say what changed | Defaults are untouched, or several numbers changed at once with no notes |
| G4 | Feedback | Important actions get layered feedback scaled to their importance, and the action stays readable | Actions are silent or flat, or effects hide the enemy or hitbox |
| G5 | One world | Assets, VFX and UI follow one style bible. Each AI asset was checked from behind and close up | Mixed styles, painted-in lighting, melted shapes or placeholder art remain |
| G6 | Mesh and budget | `check_mesh.py` (or an engine stat) shows triangles within the budget, UVs present, no degenerate faces, and platform limits were read from current docs | Counts exceed the budget, limits were guessed, or no check was run on an AI mesh |
| G7 | Structure | Levels teach, test and twist. The game has an ending or goal and hand-authored key moments | Symmetric evenly spaced content, no ending, or all content generated |
| G8 | Sound and UI | Repeated sounds vary, UI fits the world and shows needed numbers, and it works at phone size | Identical repeated sounds, UI that is a generic default, or unreadable at small size |

## Verdict

- **Ship:** G1 passes and at most one other check fails.
- **Fix first:** anything else. G1 failing is always "Fix first", and "Could not run" counts as a fail.

Report the score as passes out of applicable checks, with the verdict, never alone.

## Guards

- Judge the game, never who or what made it. Do not say "AI-made" or "proves".
- Stylized, low-poly and flat-shaded art is a choice. Fail it only when inconsistent.
- An honest prototype may use placeholders. G5 applies to builds called finished.
- A brief or the owner's style overrides G2, G7 and G8 defaults. It never overrides G1.
- If the game cannot be run in this environment, say so, mark G1 FAIL (not run), and list what a human should test.
