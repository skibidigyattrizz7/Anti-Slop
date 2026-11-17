Here is a grenade explosion that reads as a real blast and stays under 60 particles.

**Layers (each fires once, then cleans up)**

1. **Flash:** one neon sphere Part that grows and fades over about 0.15 s. No particles.
2. **Fireball:** one ParticleEmitter, 18 particles. Orange to dark red, size grows then shrinks, Lifetime 0.4 to 0.7, Speed 8 to 14, SpreadAngle 180, LightEmission 0.6.
3. **Sparks:** one ParticleEmitter, 20 particles. Bright yellow, thin and stretched, Acceleration of (0, -30, 0) so they fall, Lifetime 0.5 to 0.9.
4. **Smoke:** one ParticleEmitter, 12 particles. Grey, slow, Lifetime 1.5 to 2.5, transparency rising over its life.
5. **Debris:** 6 small Parts thrown outward, removed after 2 s.

Total: 18 + 20 + 12 = 50 particles. Each emitter is set to Enabled = false and fired with `:Emit(count)`, so nothing runs after the burst.

**Low graphics quality**

Read `UserSettings().GameSettings.SavedQualityLevel.Value` once. At levels 1 to 3, halve each emit count so the total stays near 25 to 30. Explosions still read as explosions, and the flash and smoke carry the look.

**How I would test it at low quality**

- **Count check:** log the total `:Emit` count per explosion and assert it is 60 or less.
- **Studio:** set Graphics Quality to 1, throw 5 grenades in quick succession, and watch frame time with the MicroProfiler (Ctrl+F6). Pass if no frame goes above about 33 ms during an explosion.
- **Visual check:** capture screenshots at 0.05 s, 0.3 s, 1 s and 2 s. The flash should read first, then the fireball, with smoke lingering.
- **Real device:** publish to a private test place and try a low-end phone or tablet at quality 1 to 2.
- **Cleanup check:** after 3 s, the Effects folder should be empty. If it is not, the grenade is leaking Parts.

I did not open your grenade script, so the function names and damage hooks are guesses and the numbers are untested on a device. The main risk is cleanup: if the debris or emitters are not destroyed, repeated grenades will fill the workspace.
