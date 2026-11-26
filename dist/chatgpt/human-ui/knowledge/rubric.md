# UI rubric

Used by the judge agent and for self-checks. Each check is PASS, FAIL or N/A. A FAIL needs evidence: a quoted line, a selector or a screenshot note. Check in this order.

**Must-pass check: U1.** The page works at phone width (375px) and desktop, has the states its content needs, and shows visible keyboard focus. If you cannot open a browser, say "not verified in a browser" and judge the code only. Then U1 is "unverified", never PASS.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| U1 | Works | At 375px and 1280px there is no horizontal scroll, nothing is clipped, nothing overlaps, text is readable. Text and cards do not touch a rule or each other, and content is inset from the screen edge (about 16px at 375px). Empty, loading and error states exist where the page has data, forms or async content (N/A on a static page with none). Every control shows a visible focus ring and tabs in a sensible order | Layout breaks, text or cards touch a rule or the screen edge, content overlaps, the page scrolls sideways, a needed state is missing, focus is removed or invisible, or a control cannot be reached by keyboard |
| U2 | Direction | One direction with a reason that fits the audience. The reason may be written in the contract or code, or read from the page: type, colour and layout fit this subject and are not the default clusters | Nobody can say why this look fits. It reads as the default for its era, or would fit any business by swapping the name |
| U3 | Type and color | Two faces with contrast, semantic color tokens, contrast at WCAG AA, state not shown by color alone | Single default sans at default weights, raw hex everywhere, gray on tint, color-only errors |
| U4 | Layout | Content shapes the layout. Hierarchy comes from size, space and weight. Radius and elevation follow a system | Hero plus three equal cards, nested cards, one radius and shadow everywhere |
| U5 | Copy | Specific, real, plain. Buttons are verb plus result. Errors give reason, next step and saved or not | Buzzwords, "Submit", "Oops", generic headline that fits any product |
| U6 | Truth | Every number, name, quote, logo and service claim is given in the brief, follows directly from it, or is marked as a placeholder | Invented stats, testimonials, users, logos, reviews, prices, price ranges or service descriptions the brief never gave |
| U7 | Motion and decoration | Motion tied to action, reduced motion honored. Decoration (gradient, blur, badge, emoji) has a reason | Scroll fade on everything, glass and glow by default, no reduced-motion rule |
| U8 | Scanner review | Script counts were read and each flag was either fixed or justified | Flags ignored, or "scanner passed" used as the only evidence |

## How to read the edge cases

- **U1, N/A states:** a static page with no data, forms or async content has no empty, loading or error states. Score that part N/A, not PASS and not FAIL. The rest of U1 still applies.
- **U1, from a screenshot:** look at the 375px image, not only at scroll width. A heading jammed against a rule, cards touching the next section, or text at x=0 while other content is inset is a FAIL even when nothing overflows. A common cause is a class padding rule overriding section padding.
- **U1, not run:** if you could not open a browser or take a screenshot, write "unverified". Do not infer layout from the CSS alone.
- **U2, no written reason:** judge the page. A price-board look with a slab face on a repair shop page passes. A centred hero, one system sans and white rounded cards that fit any shop fails.
- **U6, derived facts:** a fact that follows from the brief passes. "Open Tue to Sat" supports "Closed Sunday and Monday". The street name supports "4th Street" in a heading.
- **U6, invented detail:** "from $65" (a range), "Full tune-up for your bike" (a scope) and a meta description that adds either fail. Use "$65" as given or drop the line.
- **U8, zero flags:** read the font fields and the counts against the page. A clean scan alone is not a PASS.

## Senior checks

Apply only when the brief is a full project or the user asks for a senior review. They never change the verdict rule for ordinary work. Read `senior.md` for the rules behind each.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| S1 | Type system | One scale ratio, body measure about 45 to 90 characters, tabular figures in number columns | Sizes picked ad hoc, long lines, wobbling number columns |
| S2 | Colour tokens | Role tokens over raw values, dark mode by token swap, measured contrast reported | Hex inside components, dark mode patched per component, contrast guessed |
| S3 | Targets and states | Controls at least 24 px (44 px on touch) and the eight states exist, focus not hidden by sticky bars | Small hit areas, missing hover or focus or error states |
| S4 | Loading and motion | Loading follows the 0.1 s, 1 s, 10 s limits, one duration table, reduced motion honoured | Spinner with no progress on long waits, mixed durations, no reduced-motion rule |
| S5 | Critique | The 30-second critique was run and its findings listed | No critique, or only "looks good" |

## Verdict

- **Ship:** U1 and U6 pass and at most one other check fails.
- **Fix first:** anything else. U1 failing, "unverified", or U6 failing is always "Fix first".

Report the score as passes out of applicable checks, with the verdict. Never the score alone.

## Guards

- Judge the interface, never who or what made it. Do not say "AI-made" or "proves".
- A brand guide, a client request or an existing design system overrides U2 to U4. It never overrides U1 or U6.
- A style tell with a stated reason is a PASS.
- The scanner cannot see a rendered page. Do not mark U1 from script output.
