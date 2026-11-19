# Build log craft

## Entry shape

Date, then five lines.

- **Goal:** one sentence.
- **Tried:** what you did, with parts and settings.
- **Result:** numbers with units and the conditions.
- **Changed:** what you changed because of it.
- **Next:** one step.

Ask the user for each line they have not supplied. Leave a blank instead of guessing.

## Parts list

| Part | Exact model | Qty | Source | Cost |
|---|---|---|---|---|

Fill only what the user gave. Mark missing cells `[ask]`. Add firmware, library and IDE versions below the table.

## Wiring and pins

Use a table: signal, from, to, pin, wire colour. Add a photo or diagram note. Prose can explain why a pin was chosen, never replace the table.

## Measurements

- Give the unit and the condition: "11.1 V battery, 6.8 V at motor under load", not "voltage drop".
- Give the sample: "0 errors in 200 readings", not "reliable".
- Give the tool if known: multimeter, serial monitor, stopwatch.
- If the user gave a range, keep the range.

## Failures

Record what broke, how it was found, what changed, and whether it is fixed. A failure still open goes under Known issues. Do not close it for the user.

## Decision records

Options considered, criteria, choice, reason. Two lines each is enough. Example criteria: cost, weight, pin count, availability.

## Code comments

Explain why a value was chosen: `// 50 ms timeout: echo pin floats when sensor is unplugged`. Do not restate the code.

## Safety

Be specific and tied to the part: LiPo charge current and a fireproof bag, motor stall current against the driver rating, fuse size, loose wires near moving parts. Only claim a rating if the user gave it; otherwise write `[check datasheet: rating]`.

## Longer before and after

**Facts the user gave:** Nov 5. Arduino Uno, HC-SR04 on pins 7 and 8. Reads 0 cm about 1 time in 10. Wire was loose. Re-crimped, added a 50 ms timeout, ignores readings under 2 cm. Tested 200 readings, no zeros.

**Before:** "The ultrasonic sensor provides reliable distance sensing, ensuring robust obstacle avoidance for the robot."

**After:**
"Nov 5. Goal: stop false zero readings.
Tried: HC-SR04 on pins 7 (trig) and 8 (echo), Uno. About 1 in 10 readings was 0 cm.
Cause: loose echo wire.
Changed: re-crimped it, added a 50 ms timeout, ignore anything under 2 cm.
Result: 0 zeros in 200 readings.
Next: [ask: test with the motors running]"

What changed: the claim became numbers, the cause and fix are recorded, and the missing test is a question, not a guess.
