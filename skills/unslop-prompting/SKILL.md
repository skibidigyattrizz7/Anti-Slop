---
name: unslop-prompting
description: Load before starting, even for a short task, whenever you are writing a prompt or brief for another AI tool (Claude, ChatGPT, image, video, code, app builders), improving a prompt, or the user wants better results from an AI, or says its outputs all look the same. Not for writing the content itself (human-writing, human-fiction, human-media), chat replies (human-chat), code (human-code) or UI text (human-ui).
---

# Unslop Prompting

Different models give similar answers to open-ended requests, and one model repeats itself across tries. A large study (Infinity-Chat: 26,000 real open-ended queries, 31,250 human ratings) named this the "Artificial Hivemind". A vague prompt returns the average of the internet. The prompt's job is to push away from it, using the user's real facts.

## Top rules

Build the prompt in this order.

1. **Goal and audience.** Who it is for, what they do with it.
2. **Three to five concrete specifics** only this task has: real details, numbers, names, constraints. Take them from the user.
3. **One committed direction.** A style or angle ("1980s field guide", "blunt coach"), not "professional and engaging".
4. **Examples.** A real sample of the voice or look, or a good and a bad one. Examples beat adjectives.
5. **What to avoid, with the reason.** "No lighthouse keepers or names like Elara, since those are overused." Name the default.
6. **Format and length,** exactly.
7. **Ask for variety when you want it.** Several clearly different takes, with the most unusual picked. Verbalized sampling (several answers with probabilities) is reported to add diversity, but results vary by model.

## Never

- Drop, soften or change a fact the user gave. Every one goes into the prompt.
- Invent specifics to fill the template. Ask, or leave `[need: ...]`.
- Promise results. A prompt raises the odds, nothing more.

## Defaults

A brief or the tool's own format overrides these.

- Skip empty asks: "make it good, unique, creative, professional, engaging".
- Skip stacked adjectives and "act as a world-class expert" lines. They add little.
- Iterate by editing: pick the best draft, say what to change. Do not re-roll forever.
- Match the tool: image prompts want subject, setting, light and style; code prompts want inputs, outputs and constraints.

## Read when

| When | Read |
|---|---|
| Turning a request into a prompt, or per-tool shapes | `references/craft.md` |
| Scanning a prompt for generic tells | `references/tells.md` |
| Checking a finished prompt | `references/rubric.md` |

## Template

```
Goal: [what this is for, who uses it]
Specifics to include: [3-5 real details]
Direction: [one committed style or angle]
Example of the voice or look I want: [paste or describe]
Avoid: [the generic defaults] because [reason]
Format: [length, structure]
Give me [3] clearly different versions, then say which is least generic and why.
```

## Before and after

**Before:** "Write a fun story for kids."

**After:** "Write a 300-word story for 8-year-olds about a school bus driver whose bus only drives backward. Funny, dialogue-heavy, grumpy but kind narrator. No magic wands, no lessons at the end, no names like Luna or Max. Give me three different openings first."

## Final check

- Is every fact the user gave in the prompt, unchanged?
- Does it hold 3 to 5 specifics, one direction and one example?
- Does it say what to avoid, and why?
