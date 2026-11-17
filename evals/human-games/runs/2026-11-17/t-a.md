Here is a grenade explosion that reads as a real blast and stays under about 60 particles.

**Idea:** the grenade is a short, heavy punch. Anticipation, a hard white flash, then a fast fireball, flying sparks and slow smoke. The core verb is "throw and it hits hard", so the explosion should also push the arena: a short camera shake for players nearby.

**Timing**
- 0.2 s before impact: a small dark ring on the ground shrinks in (a Part or decal, not particles).
- Impact frame: one white flash Part for 1 frame, a low thump at a randomized pitch, a short camera shake that fades over about 0.3 s.

**Particles (one burst, not a continuous Rate). Use `Emit(n)` when the grenade lands, with `Enabled` off.**

| Layer | Count | Lifetime | Look |
|---|---|---|---|
| Fireball core | 8 | 0.25 to 0.4 s | Large flipbook fire, fast ease-out size, white to yellow to orange color, LightEmission 1 |
| Sparks | 24 | 0.4 to 0.7 s | Small, squashed, strong downward Acceleration (tune by eye), LightEmission 1 |
| Smoke | 14 | 1.2 to 1.8 s | Dark charcoal, normal blend (LightEmission 0), slow rise, grows then fades out |

Total is 46 particles, with headroom under 60. The palette is one hue family (orange and yellow) with a white core, plus charcoal smoke.

Add one PointLight that flares to bright and fades over about 0.3 s, and one scorch decal that stays for a few seconds.

**Rules to keep it clean**
- Fade every layer through Size and Transparency NumberSequences so nothing pops off.
- Do not stack large transparent layers over the screen.
- Keep the explosion away from the player's crosshair and the enemy hitbox, so danger stays readable.

**How I would test at low graphics quality**
- Set Studio's graphics mode to the lowest level (manual level 1) and play solo. Check that the explosion still reads: the fire core and sparks should be visible, and the smoke should not vanish into the floor.
- Throw grenades in a loop (about 20 in a row, in the same spot and in a cluster) and watch the frame rate in the Developer Console (F9) and the Microprofiler. Compare against an empty arena.
- Check the phone-sized view on a mobile emulator, since the particle cap is lower there.
- Look at it from several angles and distances, and check the silhouette with the lights off.
- Confirm the particle count with a quick script: `#emitter:GetChildren()` is not enough, so count the number of `Emit` calls and the emitter counts per burst.

**What I did not check**
- I have not run this in Roblox. The numbers above are starting values for you to tune by playing, not tested results.
- I did not confirm Roblox's current per-second particle caps or how low graphics quality changes emitters. Check the Creator Hub before you ship, because these limits change.
- Nothing here is a finished build. Replace any placeholder flipbook textures with final art before calling it done.
