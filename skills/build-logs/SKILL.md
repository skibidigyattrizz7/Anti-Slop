---
name: build-logs
description: Use for robotics, Arduino, VEX, electronics, or hardware project docs, engineering notebooks, build logs, wiring guides, and project write-ups so they read like a real builder's record, not generic AI docs.
---

# Build Logs

AI hardware docs sound smooth and say nothing: "The ultrasonic sensor seamlessly detects obstacles, enabling robust navigation." Real logs have part numbers, measurements, and failures. (Practitioner guidance; no formal study found as of Oct 2026.)

## Top rules

1. **Exact parts.** Model numbers, pins, library and firmware versions (Arduino IDE, VEXcode, PROS).
2. **Real measurements with units.** Voltage under load, current draw, cycle times, sensor readings.
3. **Keep the failures.** What broke, how you found the cause, what you changed.
4. **Dated entries.** Goal → what I tried → what happened (numbers) → what I changed → next step.
5. **Never invent data.** If the user hasn't given a measurement, leave a blank like `[measure: battery V under load]` and ask.

## Include

- **Parts list table:** part, exact model, quantity, source, cost.
- **Wiring/pin table** plus a photo or diagram.
- **Decision records:** options, criteria, choice, reason.
- **Code comments that explain chosen values** ("50 ms timeout because the echo pin floats").
- **Safety notes that are specific:** LiPo charging, motor stall current, fuse size.
- **Known issues / what I'd do differently.**

## Avoid

- "This innovative project leverages Arduino to…"
- A perfect story with no problems
- Wiring described only in prose
- A conclusion that repeats the intro

## Before and after

**Before:** "The ultrasonic sensor seamlessly detects obstacles, enabling robust navigation."

**After:** "Oct 3: HC-SR04 on pins 7/8 read 0 cm about 1 in 10 times. The echo wire was loose. Re-crimped it, added a 50 ms timeout, and now ignore readings under 2 cm. 0 errors in 200 readings."

(Example values are illustrative. Use the user's real data.)

## Final check

- Could someone rebuild this from the doc?
- Is every number real and from the user?
- Is at least one failure and its fix recorded?
