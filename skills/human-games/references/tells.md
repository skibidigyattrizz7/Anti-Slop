# Game tells (dated)

last_verified: 2026-11-19 against the owner's `ai-auditor` list (2026-10) and `research_notes/AI tells and craft across media/games.md` (second pass 2026-11-19).
Re-check: asset tells every 3 months (generators improve fast), structure tells every 6 months, everything after a major model or generator release.

A tell is a reason to look closer and rework. It is never proof of who or what made the game. One tell means little; several of different kinds mean the build is running on defaults.

## Structure and design

| Tell | Fix |
|---|---|
| A genre template with no twist: collect coins, dodge enemies, timer | Pick one core verb and twist it (`craft.md`) |
| Theme is only a skin; changing it changes no rule | Let the theme alter a rule |
| Default numbers nobody playtested: speed, gravity, health, damage | Tune one number at a time by playing |
| Menus, shops and save screens exist but actions do not answer back (inference, unverified; no source measured it) | Count fake polish against feel. Spend the time on feel |
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

- Players react most to AI art they can see. At Steam Next Fest (Feb 2026) players said they skip demos with AI capsule art ("the amount of AI key art is insane", Mike Rose) and sort by popularity to avoid them (Kotaku, 2026-02-24). Make capsule and key art by hand.
- "AI slop" is also a gut label: developers report being review-bombed with no evidence (CreativeBloq, 2026-06-29). Judge the game, not the accusation.
- The earlier "about 1 in 3 new Steam games disclosed AI (July 2026)" figure and sales or review-score studies are unverified here and left out.

## Steam rules (verified 2026-11-19)

- The Steamworks Content Survey asks about AI content that ships with the game and that players consume: art, sound, narrative, localization. Efficiency tools are not the focus. Pre-generated content is judged like any other content. Live-generated content also needs a description of guardrails against illegal output. Valve revised the guidance in Jan 2026 so code helpers need no disclosure. Enforcement is by trust. Source: Steamworks docs (undated page); Gigazine 2026-01-20.

## Game-feel numbers (primary code, Celeste)

Celeste's source (`Player.cs`): coyote window 0.1 s (6 frames at 60 fps); dash-start hit freeze 0.05 s (3 frames); wall-hit shake 0.1 s. Starting points only, tune by playing. Jump-buffer window and screen-shake size are not verified.

## Guards

- Stylized, low-poly and flat-shaded art is a choice, not a tell. Judge whether the choice is consistent.
- Placeholder art in an honest prototype is fine. It is a fail only in a build called finished.
- Photogrammetry and scanned assets can look like AI meshes. Check the source.
- Judge the game, never the maker.

## Left out as unverified

Swink's 100 ms response figure, hit-stop frame counts and jump-buffer windows from a named talk, GMTK numbers, the quoted values in `craft.md` beyond the Celeste ones above, and Steam sales or score studies.

## Sources

Owner's `ai-auditor` list (Oct 2026); Steamworks Content Survey (partner.steamgames.com); Kotaku 2026-02-24; CreativeBloq 2026-06-29; Celeste `Player.cs` (github.com/NoelFB/Celeste); Colyseus "Vibe Jam 2026"; Summer Engine "Cursor Vibe Jam 2026 guide"; threejs.org manual, lights; Jonasson and Purho, "Juice It or Lose It" (GDC Europe 2012); Nijman, "The Art of Screenshake" (GDC 2013). Notes with caveats: `research_notes/AI tells and craft across media/games.md`.
