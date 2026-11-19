# Build log tells (dated)

last_verified: 2026-11-19 against the owner's original skill. No formal study found as of Oct 2026; this is practitioner guidance.
Re-check: word lists every 6 months, everything after a major model release.

A tell is a reason to rework a passage, never proof of who wrote it.

## Structure

| Tell | Fix |
|---|---|
| Parts named by type only ("a motor", "a sensor") | Ask for the model and quantity |
| Sensor or motor behaviour described with no reading | Ask for the number and conditions, or leave `[measure: ...]` |
| Every step works the first time | Ask what broke. Record the failure and fix |
| Wiring explained in a paragraph | Move it into a pin table |
| Code values with no reason | Add the reason in a comment, or ask |
| Intro that sells the project, conclusion that repeats it | Open on the goal, end on the next step |
| Undated, one block of narrative | Split into dated entries |
| Safety missing where hazards exist | Add the specific note (LiPo charge rate, stall current, fuse) |

## Words and phrases

Count these in clusters of three or more:

- seamlessly, robust, reliable, efficient, innovative, cutting-edge, leverages, empowers, enabling
- "ensures optimal performance", "this project showcases", "provides a solution"
- "The system then...", "Finally, the robot..." as a chain with no data

Fix by replacing with the reading, the cause or the part: "reliable" becomes "0 errors in 200 readings" only when the user gave those numbers.

## Guards

- Short, informal or beginner logs are not AI writing.
- A competition notebook may require a set layout. Follow it.
- Never fill a blank with a plausible number to make a log look complete.
- Example values shown in skill files are illustrative only.

## Sources

Owner's original skill. No outside source cited.
