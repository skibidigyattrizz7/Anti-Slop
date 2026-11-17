# human-ui eval, 2026-11-17

One run per arm, 1 task (homepage for Chen's Cycle Repair, supplied facts only), judge in a fresh context with screenshots at 375px and 1280px. The judge did not know which file used the skill.

Key: t-a.html used the skill. t-b.html did not.

| Task | Without skill | With skill | Judge preferred |
|---|---|---|---|
| 1 Chen's Cycle Repair | 4/8, Fix first | 8/8, Ship | With skill |

## What it showed

- The skill won. t-a has a price-tag look that fits a repair shop, two faces, two price tags in place of three equal cards, and only the supplied facts. "Closed Sunday and Monday" follows from "open Tue to Sat".
- t-b had a CSS bug: a `.wrap` padding rule overrode the section padding. Headings touched rules, cards touched the next rule, and the hero sat at x=0 on a phone. U1 passed it because nothing overflowed or was clipped.
- t-b also invented "from $65", "from $15" and "Full tune-up for your bike", and used one system sans for everything.
- The scanner returned 0 flags on both pages. Its font fields were wrong: `named_fonts` was empty for both, and `default_only` was false for t-b, which uses only a system-ui stack.
- U8 and U5 did not separate the pages.

## Changes made after this run

- Rubric U1: added an N/A path for states a static page does not have, and layout breakage seen in a screenshot (touching a rule, flush against the edge, overlap, sideways scroll).
- Rubric U6: derived facts pass. Invented prices, ranges and service descriptions fail.
- Rubric U2: scorable from the page when no reason is written.
- Rubric: added "How to read the edge cases".
- Script: `named_fonts` now reads custom properties (`--display`) and the `font:` shorthand, and lists system fonts too. `default_only` is true for a system-only, Inter-only or Geist-only stack. Selftest cases added for each. Both pages re-scanned: t-a lists its named fonts and is not default-only; t-b is default-only and gets one flag.
- SKILL.md left as it was.

## Limits

One run per arm and one task is too few to be sure of anything. The judge could not check dark mode or live keyboard order, and the sandbox lacked the display font. These scores predate the changes above. Rerun with 3 tasks and 3 runs per arm before trusting the difference.
