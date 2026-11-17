---
name: unslop-prompting
description: Writes prompts and briefs for AI tools (Claude, ChatGPT, image, video, code, app builders) so outputs avoid the generic average. Use when the user asks for a prompt, wants better results from another AI, is about to hand a task to an AI tool, or complains that AI outputs all look the same.
---

# Unslop Prompting

## Why outputs converge

Different models give similar answers to open-ended questions, and one model repeats itself across tries. A large study (Infinity-Chat: 26,000 real open-ended queries, 31,250 human ratings) called this the "Artificial Hivemind". So a vague prompt returns the average of the internet. The prompt's job is to push away from the average.

## Build the prompt in this order

1. **The goal and the audience.** Who it's for, what they do with it.
2. **Three to five concrete specifics** only this task has: real details, numbers, names, constraints.
3. **A direction, committed.** One style or angle ("1980s field guide", "blunt coach"), not "professional and engaging".
4. **Examples.** A real sample of the voice or look you want, or a good and a bad example. Examples beat adjectives.
5. **What to avoid, with the reason.** "No lighthouse keepers or names like Elara, since those are overused." Naming the default works better than a vague "be original".
6. **Format and length.** Say exactly how long and in what shape.
7. **Ask for options when you want variety.** Ask for several different takes and have the tool pick the most unusual, or generate them separately. A published technique called verbalized sampling asks the model to produce several answers with probabilities so it samples across the spread instead of the single most likely one. Reported to increase diversity, but results vary by model.
8. **Iterate by editing.** Pick the best draft and tell it what to change (cut the intro, make the second point concrete). Don't re-roll from scratch forever.

## Don't

- "Make it good / unique / creative / professional / engaging." These are empty.
- Stack many adjectives. Give one example instead.
- Paste generic "act as a world-class expert" lines. They add little.
- Accept the first output as final.

## Template

```
Goal: [what this is for, who uses it]
Specifics to include: [3-5 real details]
Direction: [one committed style or angle]
Example of the voice/look I want: [paste or describe]
Avoid: [the generic defaults] because [reason]
Format: [length, structure]
Give me [3] clearly different versions, then tell me which is least generic and why.
```

## Before and after

**Before:** "Write a fun story for kids."

**After:** "Write a 300-word story for 8-year-olds about a school bus driver whose bus only drives backward. Funny, dialogue-heavy, in the voice of a grumpy but kind narrator. No magic wands, no lessons at the end, and avoid names like Luna or Max. Give me three different openings first."
