# Game craft

Contents: mechanics, levels, game feel, UI, sound, 3D and AI assets, VFX, one longer example.

Practitioner guidance from talks and studio guides ("The Art of Screenshake", "Juice It or Lose It", Riot's VFX guide), not lab studies. Testing beats any rule. Tune numbers yourself.

## Mechanics

- **Find one core verb and twist it.** "You can only jump while shooting." "The floor is lava, and the lava is also your ammo."
- **Make the theme change the rules.** In a haunted house, light should matter mechanically.
- **Gray-box first.** If the loop is not fun with plain boxes, polish will not rescue it.
- **Tune by playing.** Acceleration, jump arc, coyote time, input buffering, damage. Change one number, play, repeat. Write down what you changed and what you felt.
- **Hand-author the memorable parts**: the first minute, the boss, the ending. Use generators for filler. Kate Compton's point: ten thousand bowls of oatmeal are all different and all look the same, so make differences the player can see.
- **Scope small.** One mechanic understood in seconds, and a finish line.

## Levels

- Teach, test, twist, then retire a mechanic (Nintendo's four-step pattern).
- Use landmarks for navigation, sightlines that preview goals, and real rest areas.
- Avoid symmetric rooms and evenly spaced enemies or pickups. Place by hand and break the grid on purpose.

## Game feel

Give every action a response out of proportion to the input. Layers: sound with some bass, a white hit-flash for a frame or two, knockback, particles, a small camera shake, brief hit-stop (a few tens of milliseconds), squash and stretch, lasting marks such as scorch decals, camera kick.

- **Scale to importance.** A footstep gets almost nothing. A boss kill gets everything.
- **Test each effect.** One team kept screen shake and dropped freeze-frames and gun kickback because they felt like bugs. Too much polish can break immersion, so match juice to the experience you want.
- **Keep it readable.** If an effect hides the enemy or the hitbox, cut it.
- **Do not let easing make direct controls mushy.**

## Game UI

- Fit the world: its shapes, materials and type.
- Show the numbers the player needs, where the eye already is.
- No glowing border on everything. Pick one emphasis style.
- Tooltips say more than the button name.

## Game sound

- Randomize pitch and volume on repeated sounds.
- Layer 2 or 3 sources for impacts: a click, a body, a tail.
- Match reverb to the space.
- Leave silence. Constant sound has no contrast.

## 3D and AI-generated assets

1. **Write a style bible first.** Shape language, 4 to 6 colors, material rules, proportions. Example: "chunky toy proportions, oversized hands and heads, flat colors with one gradient accent, everything slightly leaning."
2. **Silhouette test.** Fill it black. If you cannot tell what it is, exaggerate.
3. **Exaggerate.** Stylized reads better than semi-real, especially on a phone.
4. **AI is a blockout.** Generate, then clean topology, separate parts, redo UVs after retopology, and repaint flat and unlit.
5. **Add one wrong-but-memorable detail.** A lamp with teeth. A sword made from a frozen fish.
6. **Inspect every side.** Orbit it, check the back, zoom in. Run `scripts/check_mesh.py`.
7. **Mind the budget.** A crate needs about 500 triangles, not 50,000. Roblox limits change, so read the Creator Hub specs before shipping. Reuse meshes and textures.
8. **Light the scene on purpose.** Key, fill and rim, an environment map, shadows on.

Prompt a 3D generator with style and shape: "chunky cartoon sword made of a frozen fish, thick bevels, flat colors, no painted shadows."

## VFX

- **Timing:** a short telegraph, a fast high-contrast impact, a slow low-contrast fade. Fast attack, slow decay, never linear.
- **Layers:** core flash, main shape, sparks, smoke or residue, light, decal, sound. Layers move at different speeds.
- **Shape language:** round reads friendly, sharp reads dangerous. Shapes show direction and size.
- **Value first, then color.** One or two hue families plus a hot white core. Mix dark normal-blend smoke with additive highlights.
- **Clarity beats spectacle.** Players must read danger zones and hitboxes.
- **Fewer, bigger, better particles.** Use flipbook textures for detail, not a high emission rate.

Roblox (check current docs, these change): a ParticleEmitter has a per-second cap, lower on mobile. Large screen-covering and stacked transparent layers cost fill rate. Fade with Transparency and Size NumberSequences so nothing pops. LightEmission 1 is additive glow, so use it on purpose. Test at the lowest and highest graphics quality.

## Longer example: a Roblox explosion

**Generic:** one ParticleEmitter, high rate, orange sparkle texture, constant transparency, LightEmission 1.

**Intentional:** a quarter-second anticipation with a shrinking ring and a rising whine. At impact, a one-frame white flash part, a short hit-stop for the attacker, and camera shake that decays over about a third of a second. Layers: a small burst of large flipbook fireball particles that ease out fast, a few dozen small squashed sparks with gravity, a handful of dark normal-blend smoke particles that rise slowly and fade out, a point light that flares then fades, and a scorch decal that lingers. Palette runs white core, yellow, orange, charcoal. Around fifty particles total, not hundreds.

**Mechanic, generic:** "Player shoots enemies. Enemy HP drops by 10." **Intentional:** a slow, heavy slug. On hit the enemy flashes white for two frames, a short hit-stop lands, knockback scales with damage, and a low thump plays at randomized pitch. Twist: every shot pushes you back, so firing is also how you move.

## Before and after: a spell effect

**Before:** a "magic spell" that is one orange sparkle emitter at a high rate.

**After:** a short charge ring, a one-frame white flash, a few large fast-fading puffs, small sparks with gravity, and a thump at randomized pitch.
