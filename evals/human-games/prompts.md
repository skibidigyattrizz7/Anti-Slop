# Evals for human-games

Run each task prompt with and without the skill. Compare on `references/rubric.md`, G1 first.

## Task prompts

1. **Platformer feel.** "My browser platformer is in `game.js`. Player speed is 5, gravity is 0.5, jump velocity is -10, and the player stops instantly when you release a key. Landing and jumping make no sound. Make the jump feel good. Keep the level as it is. Tell me what you tested."

2. **Roblox sword asset.** "I generated a 3D sword for my Roblox game with an AI tool. It is a .obj with 38,000 triangles, no UVs, and the lighting looks painted onto the blade. My game is chunky cartoon pirates in flat colors. What should I do before I put it in, and what is wrong with it?"

3. **Explosion effect.** "In my Roblox arena game, grenades make one ParticleEmitter with an orange sparkle and then nothing else. Design a better explosion that stays under about 60 particles, and say how you will test it at low graphics quality."

## Should trigger

1. "My jump feels floaty, help me tune it."
2. "Make this Roblox explosion look better."
3. "Is this AI-generated 3D model okay to use in my game?"
4. "The enemies in my game feel boring to fight."
5. "Design level 2 for my puzzle platformer."
6. "My game's health bar and menus look generic."
7. "Add hit effects and sounds to my shooter."
8. "Check the triangle count on this .obj file."

## Should not trigger

1. "Write the backstory for my game's villain." (human-fiction)
2. "Write dialogue for the shopkeeper NPC." (human-fiction)
3. "Make my SaaS dashboard look less generic." (human-ui)
4. "Refactor this Python function." (human-code)
5. "Write a launch post for my game." (human-writing)
6. "Which game engine is faster, in general?"
7. "Explain how a hash map works."
8. "Draw a logo for my studio."
