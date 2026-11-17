# Game tells (dated)

last_verified: 2026-11-17 against the owner's `ai-auditor` list (2026-10) and `research_notes/AI tells and craft across media/games.md`.
Re-check: asset tells every 3 months (generators improve fast), structure tells every 6 months, everything after a major model or generator release.

A tell is a reason to look closer and rework. It is never proof of who or what made the game. One tell means little; several of different kinds mean the build is running on defaults.

## Structure and design

| Tell | Fix |
|---|---|
| A genre template with no twist: collect coins, dodge enemies, timer | Pick one core verb and twist it (`craft.md`) |
| Theme is only a skin; changing it changes no rule | Let the theme alter a rule |
| Default numbers nobody playtested: speed, gravity, health, damage | Tune one number at a time by playing |
| Menus, shops and save screens exist but actions do not answer back (inference from a 2026 jam write-up, not a measured finding) | Count fake polish against feel. Spend the time on feel |
| A single-screen toy with no end | Add a level count, score target or end state |
| Procedural content that varies in numbers but not in what the player perceives | Hand-author the first minute, the boss and the ending. Constrain generators so differences show |
| 2026 jam entries cluster in arena or .io brawlers and idle or progression loops (Vibe Jam 2026, 945 submissions, 90%+ AI-written code rule; pattern read from titles by a vendor post) | Choose a different genre or a distinctive rule within it |

## 3D and assets

| Tell | Fix |
|---|---|
| Lighting or shadows painted into the texture | Repaint flat and let the engine light it |
| Melted or blob shapes, triangle soup, holes | Retopologize or rebuild by hand |
| Chaotic UVs, no clean edge flow | Redo UVs after any retopology |
| Huge triangle counts for simple props (a crate with 50,000 triangles, not about 500) | Decimate. Run `scripts/check_mesh.py` |
| Fine from the front, mush from behind or close up | Inspect every side before accepting |
| Parts fused, pose baked in | Split into parts for rigging |
| Over-smooth semi-real average style, weak silhouette | Silhouette test, then exaggerate |
| Mixed AI styles across assets | One style bible, regenerate outliers |
| Default Three.js look: flat uniform ambient light, no shadows, default colors (Three.js manual, date not stated) | Key, fill and rim lights, an environment map, shadows turned on and wired up |

Photogrammetry shares several mesh traits, so false positives are likely. This family is fading as tools improve.

## VFX and sound (practitioner guidance, not studies)

| Tell | Fix |
|---|---|
| Effects pop in and out, constant linear fade | Anticipation, fast attack, slow decay |
| One particle layer, rainbow colors, additive glow everywhere | Layer it. One or two hues plus a hot core |
| Identical sound on every repeat | Randomize pitch and volume, layer 2 or 3 sources |

## Market signal (dated)

- About 1 in 3 new Steam games disclosed AI use (July 2026). Players notice and punish AI art, textures and store capsule images most (Bazzaz and Cooper, Aug 2026; from the owner's list, not re-read). Good asset work is a trust issue as well as a quality one.

## Guards

- Stylized, low-poly and flat-shaded art is a choice, not a tell. Judge whether the choice is consistent.
- Placeholder art in an honest prototype is fine. It is a fail only in a build called finished.
- Photogrammetry and scanned assets can look like AI meshes. Check the source.
- Judge the game, never the maker.

## Left out as unverified

Steam's current AI disclosure rules (not retrieved this session). Numbers for screen shake, hit-stop frames, coyote time and input buffer windows. The quoted values in `craft.md` are practitioner starting points, not sourced findings.

## Sources

Owner's `ai-auditor` list (Oct 2026); Colyseus "Vibe Jam 2026"; Summer Engine "Cursor Vibe Jam 2026 guide"; threejs.org manual, lights; Jonasson and Purho, "Juice It or Lose It" (GDC Europe 2012); Nijman, "The Art of Screenshake" (GDC 2013). Notes with caveats: `research_notes/AI tells and craft across media/games.md`.
