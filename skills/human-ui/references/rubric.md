# UI rubric

Used by the judge agent and for self-checks. Each check is PASS, FAIL or N/A. A FAIL needs evidence: a quoted line, a selector or a screenshot note. Check in this order.

**Must-pass check: U1.** The page works at phone width (375px) and desktop, with empty, loading and error states and visible keyboard focus. If you cannot open a browser, say "not verified in a browser" and judge the code only. Then U1 is "unverified", never PASS.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| U1 | Works | At 375px and 1280px there is no horizontal scroll, nothing is clipped, text is readable. Empty, loading and error states exist and make sense. Every control shows a visible focus ring and tabs in a sensible order | Layout breaks, a state is missing, focus is removed or invisible, or a control cannot be reached by keyboard |
| U2 | Direction | The contract or the code shows one direction with a reason that fits the audience | Nobody can say why this look fits. It reads as the default for its era |
| U3 | Type and color | Two faces with contrast, semantic color tokens, contrast at WCAG AA, state not shown by color alone | Single default sans at default weights, raw hex everywhere, gray on tint, color-only errors |
| U4 | Layout | Content shapes the layout. Hierarchy comes from size, space and weight. Radius and elevation follow a system | Hero plus three equal cards, nested cards, one radius and shadow everywhere |
| U5 | Copy | Specific, real, plain. Buttons are verb plus result. Errors give reason, next step and saved or not | Buzzwords, "Submit", "Oops", generic headline that fits any product |
| U6 | Truth | Every number, name, quote and logo is real or marked as a placeholder | Invented stats, testimonials, users, logos or reviews |
| U7 | Motion and decoration | Motion tied to action, reduced motion honored. Decoration (gradient, blur, badge, emoji) has a reason | Scroll fade on everything, glass and glow by default, no reduced-motion rule |
| U8 | Scanner review | Script counts were read and each flag was either fixed or justified | Flags ignored, or "scanner passed" used as the only evidence |

## Verdict

- **Ship:** U1 and U6 pass and at most one other check fails.
- **Fix first:** anything else. U1 failing, "unverified", or U6 failing is always "Fix first".

Report the score as passes out of applicable checks, with the verdict. Never the score alone.

## Guards

- Judge the interface, never who or what made it. Do not say "AI-made" or "proves".
- A brand guide, a client request or an existing design system overrides U2 to U4. It never overrides U1 or U6.
- A style tell with a stated reason is a PASS.
- The scanner cannot see a rendered page. Do not mark U1 from script output.
