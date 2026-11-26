# Senior layer

Load for a big job, a senior review, or when asked for senior-level work. Each rule: the rule, why, check, tag. `[verified: URL]` means the page was opened. `[practice]` means common professional habit with no opened source; never quote its numbers as fact. Defaults in SKILL.md and craft.md still apply.

## Type

- **Body measure 45 to 90 characters; aim 65.** Eyes lose the next line past about 90. Check: count two alphabets across the column. [verified: https://practicaltypography.com/line-length.html]
- **One scale, one ratio.** App UI 1.125 to 1.2 (dense, steps stay small); marketing 1.25 and up. Check: h2 and h3 differ at arm's length without colour. [practice]
- **Tabular figures and right-aligned numbers in columns; non-breaking space before units.** Digits differ in width by default. Check: a column of 1s and 8s lines up. [verified: https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md]

## Spacing and layout

- **Gap between groups at least twice the gap inside a group.** The eye sees groups without borders. Check: squint; groups still read. [practice]
- **One spacing scale (4 or 8 px), one light source for shadows, shadows tinted to the background, not black.** Check: all shadows point the same way. [verified: https://www.joshwcomeau.com/css/designing-shadows/]
- **Do not copy the F-pattern; design against it.** It appears on long unformatted text. Headings, bold lead-ins and bullets reduce it. Check: each section opens with its point. [verified: https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/]

## Colour

- **Build in OKLCH.** Equal lightness looks equally light across hues, so lightness is your contrast lever. Chroma stays under about 0.37; add a `@media (color-gamut: p3)` override for vivid values. Check: swapping hue at fixed L keeps the page balanced. [verified: https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl]
- **OKLCH is not a contrast checker.** Still run WCAG or APCA. Check: report the measured ratio. [verified: same page]
- **Tokens in two layers.** Raw values (`--blue-600`), then roles (`--surface`, `--text-muted`, `--accent`). Components read roles only. Check: no hex or `@media` colour rules inside a component. [practice]
- **Dark mode is a token swap** under `prefers-color-scheme: dark`, designed on its own. Lift surfaces with lightness, ease accent chroma, avoid pure black behind pure white text. Check: toggle; no component changed. [verified: Evil Martians page above for the swap; the lift and chroma advice is practice]

## Contrast and target size

- **WCAG 2.2: text 4.5:1 (large 3:1); UI parts and required graphics 3:1.** Placeholders count as text. Check: measure the lightest text. [verified: https://www.w3.org/TR/WCAG22/]
- **Targets: 24 by 24 CSS px is the AA floor (2.5.8); 44 by 44 is AAA (2.5.5).** Aim for 44 on touch; grow the hit area with padding, not the icon. Check: measure the smallest control. [verified: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html]
- **APCA is a WCAG 3 candidate, not final.** Use it as a second opinion, never to pass something WCAG 2.2 fails. [verified: https://git.apcacontrast.com/documentation/APCA_in_a_Nutshell.html]

## States and forms

- **Eight states per control:** default, hover, focus, active, disabled, loading, error, success. Keyboard users never see hover. Check: tab through and list each. [practice]
- **Focus ring:** `:focus-visible`, 2 to 3 px, offset, 3:1 against neighbours, the same everywhere; a sticky header must not cover it (WCAG 2.4.11). Check: tab to the last control under a sticky bar. [verified: WCAG 2.2 page above for 2.4.11; ring size is practice]
- **Visible labels, validate on blur, error beside the field, never colour alone.** Check: type half an email; no error yet. [verified: https://www.nngroup.com/articles/errors-forms-design-guidelines/]
- **Prefer undo to confirm for reversible actions; confirm names the verb and object** ("Delete 3 files?"). Check: no bare "Are you sure?". [practice]

## Loading

- **0.1 s feels instant: show only the result. 1 s: show that it is working. 10 s: show progress and a way to cancel.** Check: throttle the network and watch each threshold. [verified: https://www.nngroup.com/articles/response-times-3-important-limits/]
- **Skeleton of the real layout beats a spinner for content.** Show nothing before about 300 ms to avoid flicker. Check: fast loads do not flash. [practice]

## Motion

Duration table for this skill: **Material 3 duration tokens** [verified: https://m3.material.io/styles/motion/easing-and-duration/tokens-specs]. Small utility changes 50 to 200 ms; medium 250 to 400 ms; over 600 ms only for ambient motion. Selection controls use 200 ms with standard easing. Do not mix this with another table in one project.

- **Ask frequency first.** Used 100 times a day: no animation. Check: the list of animated actions has no keyboard shortcuts. [practice]
- **Entering and moving things ease out; never ease in on UI.** Standard easing in CSS: `cubic-bezier(0.2, 0, 0, 1)`; decelerate `cubic-bezier(0, 0, 0, 1)`. [verified: M3 page above]
- **Animate `transform` and `opacity` only; never `transition: all`; honour `prefers-reduced-motion` by dropping movement, keeping opacity.** Check: toggle the setting. [verified: Vercel page above]
- **Content is visible without script; reveals only enhance.** Check: disable JS; nothing is blank. [practice]

## Accessibility

- **Native elements first:** `button`, `a`, `dialog`, `inert` for background. No `div` click handlers. Check: unplug the mouse. [verified: Vercel page above]
- **Test by hand:** keyboard pass, one screen reader, contrast. Automated scans catch only part. [practice]

## Design-system tokens

- **Name by role, not value or mood** (`--surface-raised`, not `--gray-200` or `--cream`). Check: renaming the brand colour touches one line. [practice]
- **Tokenise type, space, radius by role, elevation, z-index (dropdown, sticky, modal, toast), motion.** Check: no stray numbers in components. [practice]
- **Break the system on purpose, and log it.** If the same exception appears a third time, add a token. [practice]

## 30-second screen critique

1. Squint: one clear first thing? 2. Say the screen's job in one sentence. 3. Read the lightest text. 4. Tab through once. 5. Find the empty, error and long-text case. 6. View at 375 px. 7. Scan for default looks. Report what you see, then what you would change. [practice]

## Build on

- **impeccable** (Apache-2.0): the main link. Its critique, audit and polish commands and its brand-versus-product split fit big jobs. Fallback: use the 30-second critique above.
- **emil-design-eng** and **apple-design** (no licence: link only, nothing copied): motion detail and fluid-interface feel. Fallback: the motion rules above.
- **see-it-run** (this repo): open the result at 375 and 1280 px and tab through it. Fallback: say "not verified in a browser".

Do not take another skill's prescribed looks or its default icon set as a starting point; the owner's flagged list wins.

## Credits

No text copied. Rules paraphrased from the pages linked above.
