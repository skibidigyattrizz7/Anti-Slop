# Prompt craft

## Start from the user's facts

List every fact the user gave before writing. Check the list against the finished prompt. If a fact is missing from the prompt, put it back. If the prompt needs a fact the user did not give, ask one short question or leave `[need: ...]`.

## By tool

- **Chat models (Claude, ChatGPT):** goal, reader, specifics, format, length, what to avoid. Paste the sample you want matched.
- **Image tools:** subject, setting, light, lens or medium, style reference, what to leave out. Name the real thing ("overcast Glasgow tenement courtyard"), not "beautiful".
- **Video tools:** shot by shot: framing, movement, subject action, length. One idea per shot.
- **Code tools:** inputs, outputs, constraints, language and version, how it should fail, a test case.
- **App builders:** who uses it, the three screens or actions that matter, data it holds, what to skip, the look in one reference.

## Direction

Pick one. "Blunt coach" works; "friendly but authoritative and fun" averages out. If the user has no direction, offer three and let them choose.

## Examples

A real sample beats a description. Two examples, one good and one bad, with a line on why. Keep them short so the tool copies the quality, not the content.

## Avoid lists

Name the specific default and the reason: "No glowing orbs; every dashboard image I get has them." One to three items. Do not write a wall of bans.

## Variety

Ask for three clearly different versions and have the tool say which is least generic. Or run the prompt separately three times. Verbalized sampling is a reported technique: ask for several answers with probabilities. Results vary by model.

## Iterating

Pick the best draft. Say what to change: "cut the intro, make the second point concrete, keep paragraph three." Do not paste the whole prompt again with more adjectives.

## Longer before and after

**Facts the user gave:** a poster for the Year 9 science fair; Friday 14 March, 6 p.m., school hall; entry is free; 30 projects; the audience is parents.

**Before:** "Make a cool poster for a science fair."

**After:**
"Goal: a poster for parents of Year 9 students, to be printed A3 and hung in corridors.
Specifics to include: Year 9 science fair, Friday 14 March, 6 p.m., school hall, free entry, 30 projects.
Direction: 1960s lab notebook, graph-paper background, hand-lettered headline.
Avoid: glowing atoms and test-tube clip art, since every science poster uses them.
Format: portrait A3, headline, one line of details, nothing else.
Give me three clearly different layouts as text descriptions, then say which is least generic."

What changed: every user fact is in, one direction is committed, the default is named with a reason, and variety is asked for.
