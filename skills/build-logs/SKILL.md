---
name: build-logs
description: Load before starting, even for a short task, whenever you are writing or editing robotics, Arduino, VEX, electronics or other hardware project documentation: build logs, engineering notebook entries, wiring guides, parts lists, project write-ups and README files for a build. Not for general prose (human-writing), code comments or commit messages (human-code), research with citations (real-reports) or the user's personal statements (own-voice).
---

# Build Logs

AI hardware docs sound smooth and say nothing: "The ultrasonic sensor seamlessly detects obstacles, enabling robust navigation." A model has never held the part, so it writes the average of every robot README. Real logs have part numbers, measurements and failures. (Practitioner guidance; no formal study found as of Oct 2026.)

## Top rules

1. **Exact parts.** Model numbers, pins, library and firmware versions (Arduino IDE, VEXcode, PROS).
2. **Real measurements with units.** Voltage under load, current draw, cycle times, sensor readings, each with the conditions.
3. **Keep the failures.** What broke, how you found the cause, what you changed.
4. **Dated entries in one order.** Goal, what I tried, what happened (numbers), what I changed, next step.
5. **Show wiring as a table or diagram,** not only prose.
6. **Explain chosen values.** "50 ms timeout because the echo pin floats."
7. **Say what you would do differently.** Known issues stay in the log.

## Never

- Invent a measurement, reading, part number, date or test result. If the user did not give it, leave `[measure: battery V under load]` and ask.
- Write a failure as fixed, or a test as passed, when the user did not say so.
- Present illustrative numbers as real. Label any example value as an example.

## Defaults

A brief or the team's notebook format overrides these.

- **Parts table:** part, exact model, quantity, source, cost.
- **Wiring or pin table** plus a photo or diagram.
- **Decision records:** options, criteria, choice, reason.
- **Safety notes that are specific:** LiPo charging, motor stall current, fuse size.
- No hype openers ("This innovative project leverages..."), no perfect story without problems, no conclusion that repeats the intro.

## Read when

| When | Read |
|---|---|
| Writing an entry, parts list, wiring table or decision record | `references/craft.md` |
| Scanning a draft for generic tells | `references/tells.md` |
| Checking a finished log | `references/rubric.md` |

## Before and after

**Before:** "The motor driver ensures reliable, efficient power delivery to the drivetrain."

**After:** "Nov 2: L298N drove both wheels fine on the bench. Under load the left motor stalled at about 1.8 A and the driver got too hot to touch. Swapped to a TB6612FNG. [measure: current under load with the new driver]"

(Example values are illustrative. Use the user's real data.)

## Final check

- Could someone rebuild this from the doc?
- Is every number real and from the user?
- Is at least one failure and its fix recorded?
