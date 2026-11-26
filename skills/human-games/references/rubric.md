# Games rubric

Used by the judge agent and for self-checks. Each check is PASS, FAIL or N/A. A FAIL needs evidence: what you did, saw or measured, or a quoted line. Check in this order, every time.

First decide the mode. **Running game or asset:** it exists and can be run. **Design or plan:** only a written design, VFX spec or test plan exists. Use the "PASS when" column for a running game and the "Design or plan" column for a plan. 
| ID | Check | PASS when (running) | Design or plan: PASS when | FAIL when |
|---|---|---|---|---|
| G1 | Played and works, or a concrete test plan (must-pass) | The game was run or played, the core action works, and it gives visible or audible feedback. The report says what was tested | The reply has a test plan with numbers: a pass/fail threshold (for example a frame time in ms), a count with an assert or limit, the lowest quality level to test, and a cleanup check. It says what to watch. Nothing is claimed as tested that was not | Running: not run, core action fails, or code only was read. Plan: no numbers or thresholds, "check performance" with no limit, or an untested result stated as fact |
| G2 | Core verb | One core verb is stated in a sentence and has a twist or a theme-driven rule | The design names what the player does and what makes this version specific. N/A for a pure VFX or asset spec | Stock template (collect, dodge, timer) and the theme changes no rule |
| G3 | Tuning | Key numbers were changed and re-tested, and the notes say what changed | Numbers are labeled starting values with a plan to change one at a time. N/A if the design has no tunable numbers | Running: defaults untouched, or many numbers changed with no notes. Plan: numbers presented as tuned or final |
| G4 | Feedback | Important actions get layered feedback scaled to importance, and the action stays readable | The design layers at least three channels (for example flash, sound, shake, particles), scaled to importance, and states one rule for keeping the enemy, hitbox or crosshair readable | Actions silent or flat, or effects hide the enemy or hitbox |
| G5 | One world | Assets, VFX and UI follow one style bible. Each AI asset was checked from behind and close up | A palette or style rule is stated, and placeholders are labeled as placeholders. N/A if there is nothing visual | Mixed styles, painted-in lighting, melted shapes or placeholder art in a build called finished |
| G6 | Mesh and budget | `check_mesh.py` (or an engine stat) shows triangles within the budget, UVs present, no degenerate faces, and platform limits were read from current docs | The count or budget is stated and the arithmetic is right, the plan says how to measure it, and unread platform limits are marked "not checked, read the docs" | Counts exceed the budget, limits were guessed and presented as fact, or no measure is planned for an AI mesh or effect |
| G7 | Structure | Levels teach, test and twist. The game has an ending or goal and hand-authored key moments | The design has a goal or end state, or is N/A when it covers one effect or system | Symmetric evenly spaced content, no ending, or all content generated |
| G8 | Sound and UI | Repeated sounds vary, UI fits the world and shows needed numbers, and it works at phone size | Repeated sounds are specified to vary (pitch or sample), UI shows the numbers needed, and a small-screen check is planned. N/A for the part not designed | Identical repeated sounds, generic default UI, or unreadable at small size |

## Verdict

- **Ship:** G1 passes and at most one other check fails.
- **Fix first:** anything else. G1 failing is always "Fix first", and "Could not run" counts as a fail.
- **G1 judged as a plan:** a G1 PASS means "the plan is ready to execute", not "the work is verified". Name the verdict **Ship the plan** or **Fix first**, and say the work itself is untested. Never write plain "Ship" for work nobody ran.
- **G1 is never N/A.** A reply with no run and no plan fails G1. A plan with spawned objects needs a cleanup check (for example, instance count back to baseline).

Report the score as passes out of applicable checks, with the verdict, never alone.

## Edge cases

- **G1, plan numbers:** a plan passes with one threshold per thing it names. "Frame time under 33 ms for 2 s after a burst at quality level 1" passes. "Watch the frame rate" fails.
- **G1, honest gaps:** "I did not run this" is required, not a fail. A reply that claims a result nobody saw fails.
- **G6, honest "not checked":** stating that a platform limit was not read passes. Silence about limits that matter is a FAIL only when the design depends on them (a particle cap, a triangle cap).
- **Stating what was not checked:** a clear "Could not check" line earns credit under G1 and G6. Hiding it fails them.

## Guards

- Judge the game, never who or what made it. Do not say "AI-made" or "proves".
- Stylized, low-poly and flat-shaded art is a choice. Fail it only when inconsistent.
- An honest prototype may use placeholders. G5 applies to builds called finished.
- A brief or the owner's style overrides G2, G7 and G8 defaults. It never overrides G1.
- If the game cannot be run in this environment, say so, grade G1 as a plan if a plan exists (otherwise FAIL, not run), and list what a human should test.

## Senior checks

Apply only when the brief is a full project or the user asks for a senior review. They never change the verdict for ordinary work. Report them beside the score.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| S1 | Target aesthetic | One or two aesthetics are named and each mechanic serves one | Mechanics listed with no target feeling |
| S2 | Forgiveness constants | Grace, buffer and corner values are named constants, tuned one at a time; Celeste numbers are cited, and no jump-buffer length is quoted | Hard-coded windows, or a made-up buffer figure |
| S3 | Playtest protocol | Fresh testers, no leading prompts, first confusion and quit point recorded; small counts are not called statistics | Developer-only testing, or "players loved it" with no evidence |
| S4 | Difficulty and economy | One new variable per level; sinks and faucets modelled | Many changes per level, or an untested economy |
| S5 | Slice and budgets | A vertical slice and non-goals exist; budgets are measured, and threejs numbers are credited as one author's starting points | Content built before a slice, or budgets stated as standards |
