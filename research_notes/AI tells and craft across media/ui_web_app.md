# AI tells and craft: web, web app, mobile app and interface design

Researched 2026-11-17. Sources are mostly 2026 practitioner pages and tool docs. Primary sources (WCAG, the Impeccable and taste-skill repos) are marked. Nothing below states a model era, so "AI" means "default model-generated output" in general. Items marked **unverified** came only from search snippets or from memory.

## Source reliability

Most "AI tell" lists come from agencies or tool vendors who sell fixes: practitioner opinion, not measured data. The most complete list is the Impeccable slop catalogue (46 patterns; repo https://github.com/pbakaus/impeccable, mirror https://924b8765.impeccable-2rv.pages.dev/slop). NN/g (2021-09-19) and Refactoring UI (2018, secondary summaries only) are possibly outdated in detail.

## Tells

Each entry: **Tell**, **Why it reads as AI**, **Fix / craft move**, **Source**.

**1. Purple-to-blue or indigo gradient (hero, CTA, background)**
- **Tell:** Violet-indigo gradient on hero, buttons, or backgrounds. Cyan-on-dark is a close relative.
- **Why it reads as AI:** It signals no real brand color. The indigo default is often traced to a common utility-framework button color (**unverified**, search summary only).
- **Fix / craft move:** Build the palette from the actual brand or product. Use solid color. Limit the brand color to the logo and primary CTA.
- **Source:** Impeccable slop page (https://924b8765.impeccable-2rv.pages.dev/slop), 2026; utsubo (https://www.utsubo.com/blog/built-with-ai-trust-signals-2026), 2026-06-23; 925studios (https://www.925studios.co/blog/ai-slop-web-design-guide), 2026. No model era stated. Still current.

**2. Gradient text on headings or metrics**
- **Tell:** Decorative gradient fill on the hero headline or on numbers.
- **Why:** Decoration with no meaning. Hurts contrast and scanning.
- **Fix:** Solid color. Use weight or size for emphasis.
- **Source:** Impeccable slop page, 2026. Current.

**3. Emoji as headings or bullets**
- **Tell:** Emoji in feature headings, list bullets, or section titles.
- **Why:** Reads as casual filler, and it stands in for an icon system.
- **Fix:** Inline SVG icons from one consistent set, or nothing.
- **Source:** utsubo, 2026-06-23 (emoji bullets); Impeccable slop page, 2026 (decorative emoji). Current.

**4. Inter (or Geist, Plus Jakarta Sans) as the only typeface**
- **Tell:** One default sans at default weights for everything.
- **Why:** Signals that no typographic choices were made. The sources name Inter as the most common default. The problem is the default, not the font. Inter itself is fine when chosen on purpose.
- **Fix:** Pick a display face with character and pair it with a readable body face. Use weight 400 for body and reserve 600 for emphasis.
- **Source:** Impeccable slop page, 2026; Laith0003 ux-skill wiki (https://github.com/Laith0003/ux-skill/wiki/How-to-detect-AI-slop-in-your-design), last edited 2026-11-11. Current.

**5. Space Grotesk plus Instrument Serif (and italic serif accents)**
- **Tell:** This pairing and the italic serif display headline, often with one italic word in the hero.
- **Why:** Now a common default pairing. Looks like a trend applied without a reason.
- **Fix:** Use a face chosen for this product's voice. Use italic only if the context is editorial.
- **Source:** Impeccable slop page, 2026 (names Space Grotesk, Instrument Serif, and italic serif headlines as AI-typical). Current.

**6. Oversized display headline, crushed or loose tracking**
- **Tell:** A long sentence at display size, with letters either squeezed or wide.
- **Why:** Hurts legibility and reads as a template hero.
- **Fix:** Shorten the copy first. Use slightly negative tracking on large display sizes (about -0.03em as one checklist suggests), and check it visually. Keep body tracking at default.
- **Source:** Impeccable slop page, 2026; Laith wiki, 2026-11-11. Current.

**7. Flat type hierarchy and a default size scale**
- **Tell:** Sizes too close together, or the 12/14/16/18/24/30/36/48 scale unchanged.
- **Why:** Hierarchy has no contrast. Default steps show no decisions.
- **Fix:** Fewer sizes. Use at least about a 1.25 ratio between adjacent steps. Pick the steps for this product and adjust them by eye.
- **Source:** Impeccable slop page, 2026; Laith wiki, 2026-11-11. Current.

**8. Three equal feature cards in a row**
- **Tell:** Three identical cards, each with icon, heading, and two lines of text.
- **Why:** Gives every feature equal weight, so no priority reads. The most repeated AI layout.
- **Fix:** Give the primary feature more space. Mix layouts across the page (list, split, single large item). Show real content instead of a template.
- **Source:** utsubo, 2026-06-23; Laith wiki, 2026-11-11; Impeccable slop page, 2026. Current.

**9. Icon in a rounded tile above each heading**
- **Tell:** Rounded-square or circle icon container repeated over every feature heading.
- **Why:** Stock decoration repeated everywhere. The container adds nothing.
- **Fix:** Put the icon beside the heading, or drop the container. Use icons only where they help scanning.
- **Source:** Impeccable slop page, 2026; taste-skill README (https://github.com/Leonxlnx/taste-skill), v2.5.1, 2026. Current.

**10. Badge or pill above the hero headline**
- **Tell:** Small pill ("New", "Now in beta", "AI-powered") above the headline.
- **Why:** A standard template slot that rarely carries information.
- **Fix:** Drop it, or fold the news into the headline or body copy. Use a real breadcrumb if navigation needs one.
- **Source:** Impeccable slop page, 2026 (hero eyebrow / pill chip). Current.

**11. Centered hero with generic headline and one CTA**
- **Tell:** Centered headline, a sentence that could describe any company, one button below.
- **Why:** Layout and copy are both the default.
- **Fix:** Vary hero composition by product. Name the customer, the problem, and the specific outcome.
- **Source:** utsubo, 2026-06-23 (generic centered hero); taste-skill README, 2026 (eleven hero layouts as an alternative). Current.

**12. Colored side-stripe or thick accent border on rounded cards**
- **Tell:** A rounded card with a thick colored stripe on one side, or a gradient border.
- **Why:** A common template trope. The stripe carries no meaning.
- **Fix:** Remove it. Use a subtle accent, or use one of background tint, border, or shadow, not all three.
- **Source:** Impeccable slop page, 2026 (border accent on rounded element; side-tab accent border); Impeccable README (https://github.com/pbakaus/impeccable), 2026. Current.

**13. Glassmorphism and glow everywhere**
- **Tell:** Blur, translucent glass cards, glowing borders, glowing accents on a dark background.
- **Why:** Decoration used by default, not to solve a layering problem.
- **Fix:** Use blur only where it solves an overlap or hierarchy problem. Use plain surfaces and one elevation method.
- **Source:** Impeccable slop page, 2026 (glassmorphism; dark mode with glowing accents). Current.

**14. Hairline border plus wide soft shadow, or three card treatments combined**
- **Tell:** 1px border plus a large soft shadow plus a tinted background on the same card.
- **Why:** Redundant elevation. Looks busy and undecided.
- **Fix:** Pick one: a defined edge, soft elevation, or a background tint.
- **Source:** Impeccable slop page, 2026; Laith wiki, 2026-11-11. Current.

**15. Oversized corner radius on every element**
- **Tell:** 24px or more on small cards, the same radius everywhere, blob-like shapes.
- **Why:** One radius for everything shows no system.
- **Fix:** Set radius by role. Cards about 12–16px. Pills only for tags and small buttons.
- **Source:** Impeccable slop page, 2026; Laith wiki, 2026-11-11. Current.

**16. Nested cards (cards inside cards)**
- **Tell:** A card inside a card inside a panel, each with its own border and padding.
- **Why:** Adds depth without meaning, and wastes space.
- **Fix:** Flatten with spacing, type, and dividers.
- **Source:** Impeccable slop page, 2026. Current.

**17. Identical section rhythm and monotonous spacing**
- **Tell:** Every section with the same height, padding, and alignment. One spacing value everywhere.
- **Why:** No grouping, so nothing reads as a unit.
- **Fix:** Group tightly, separate groups generously. Alternate anchor and supporting sections. Use spacing values from one scale.
- **Source:** Impeccable slop page, 2026; Laith wiki, 2026-11-11. Current.

**18. Hero metric row (big number, small label, gradient accent)**
- **Tell:** Three large stats with small labels and a gradient accent, often with invented round numbers.
- **Why:** A template slot. Round numbers without a source read as invented.
- **Fix:** Show real metrics with context, or none.
- **Source:** Impeccable slop page, 2026; Laith wiki, 2026-11-11 (round invented stats such as 47% or 99.9%). Current.

**19. Numbered section markers (01, 02, 03)**
- **Tell:** Numbers on every section or feature.
- **Why:** Implies a sequence that does not exist.
- **Fix:** Number only real sequences, such as steps.
- **Source:** Impeccable slop page, 2026. Current.

**20. Scroll fade-in on every element**
- **Tell:** Uniform fade or slide-up as each block enters the viewport.
- **Why:** Motion that responds to nothing. Adds delay and says nothing about state.
- **Fix:** Tie motion to user action or state. Keep one or two deliberate moments per page. Add a `prefers-reduced-motion` fallback.
- **Source:** utsubo, 2026-06-23 (uniform scroll fades); Laith wiki, 2026-11-11 (no reduced-motion handling). Current. The cursor-following beam and hover-fade items from the owner's list are not covered by any source checked. See gaps.

**21. Bounce or elastic easing on UI**
- **Tell:** Springy overshoot on buttons, menus, or cards.
- **Why:** Playful motion on a serious interface.
- **Fix:** Ease-out curves for UI. Animate `transform` and `opacity`, not layout properties.
- **Source:** Impeccable slop page, 2026. Current.

**22. Stock or synthetic imagery; placeholder people and brands**
- **Tell:** Generic stock photos, glossy AI illustrations, "John Doe" and "Jane Smith", "Acme" and "TechCorp".
- **Why:** No proof. Placeholder names signal a template.
- **Fix:** Real product screenshots, real customers, or custom illustration. Names that fit the audience. Real brand names or none.
- **Source:** utsubo, 2026-06-23 (no real proof); Laith wiki, 2026-11-11 (placeholder names); Impeccable slop page, 2026. Current.

**23. Em-dash density in UI copy and body text**
- **Tell:** Frequent em dashes in headlines, descriptions, and microcopy.
- **Why:** Pattern readers now associate with generated text.
- **Fix:** Commas, colons, periods, or parentheses. Use dashes rarely.
- **Source:** utsubo, 2026-06-23; Impeccable slop page, 2026; taste-skill v2 reportedly bans em dashes entirely (README summary, 2026). Current.

**25. Buzzword, filler, and "It's not X, it's Y" copy**
- **Tell:** "Seamless", "robust", "supercharge", "unlock", "build the future of work"; sections ending in a manufactured contrast.
- **Why:** Claims nothing specific. Could describe any product.
- **Fix:** Say what the product does, for whom, with a real number or a before-and-after. Vary sentence rhythm.
- **Source:** utsubo, 2026-06-23; Laith wiki, 2026-11-11; Impeccable slop page, 2026. Current.

**25. Empty states that are blank or say "no records" while loading**
- **Tell:** Empty containers with no message, or a "No data" message shown before the data has arrived.
- **Why:** The user cannot tell "loading", "empty", and "error" apart.
- **Fix:** Show progress while loading. Confirm empty results with a message. Teach in context and give a next step (a button, a link, sample data).
- **Source:** NN/g, Kate Kaplan, 2021-09-19 (https://nngroup.com/articles/empty-state-interface-design). Possibly outdated in detail, principles still current.

**26. Missing states (empty, loading, error, disabled, zero-data)**
- **Tell:** Only the happy path is designed.
- **Why:** Real use hits these states constantly. Templates skip them.
- **Fix:** Design all five. For errors, state the reason, give a retry action, and give a support path if retry fails.
- **Source:** Impeccable/Laith checklist (see items 27 and 28 sources above), 2026. Error copy guidance from search summaries only (**unverified**). The checklist is current; the NN/g article is dated.

**27. Critical actions visible only on hover**
- **Tell:** Delete, edit, or export appears only when hovering a row or card.
- **Why:** Fails on touch, and fails keyboard users.
- **Fix:** Keep actions visible, or move them into a labeled menu.
- **Source:** Impeccable/Laith checklist, 2026. Current.

**28. Same hover effect on every element; no visible focus**
- **Tell:** Identical hover tween on all controls, `outline: none` with no replacement.
- **Why:** Hover tells nothing about state. Removing focus breaks keyboard use.
- **Fix:** Tune hover per element type. Add a `:focus-visible` outline.
- **Source:** Laith wiki checklist, 2026-11-11. Current.

**29. Low-contrast text and color-only state**
- **Tell:** Gray text on a colored background. Errors or charts shown by color alone.
- **Why:** Fails users with low vision and color-vision differences.
- **Fix:** WCAG AA contrast (4.5:1 normal text, 3:1 large text). Add text or icons to every color-coded state.
- **Source:** WCAG (AA contrast thresholds, primary knowledge, not fetched this session); Laith wiki checklist, 2026-11-11; Impeccable slop page, 2026.

## Craft principles

These go past "not looking AI". Each one is supported by at least one source above, or is labeled as general practice.

**Type**
- Few sizes, chosen on purpose. Adjacent steps differ clearly (about 1.25 or more).
- Body text 16px is the safe default (checklists flag under 14px and under 12px as too small). Line-height 1.5–1.7 for body; tighten display type.
- Keep lines to about 60–75 characters.
- Use two families at most. Weight is the main tool for hierarchy.

**Color**
- Semantic tokens (`--surface`, `--text-muted`, `--accent`), not raw hex scattered through the code.
- The brand color covers about 10% of the screen: logo and primary action. Neutrals do most of the work.
- Derive dark mode from its own design, not by inverting light mode.

**Layout and spacing**
- Spacing from one scale (4 or 8 px steps). Put more space between groups than inside them.
- Hierarchy comes from varied size, space, and weight, not from equal boxes.
- Flatten nested containers. Use one radius scale by role.

**Content**
- Real names, real numbers, real screenshots. Remove lorem ipsum and round invented stats before shipping.
- Show the product, not an abstract illustration of it.

**States**
- Design all five: empty, loading, error, disabled, zero-data. Loading should show progress or a skeleton of the real layout (skeletons are the common recommendation, from search summaries, **unverified**). Never show "no records" during loading.

**Motion**
- Motion should answer a question: where did this come from, what changed, what can I do next. Keep it short and purposeful.
- Animate `transform` and `opacity`. Respect `prefers-reduced-motion`.

**Accessibility**
- Contrast at WCAG AA. Visible `:focus-visible`. No color-only state.
- Target size: WCAG 2.2 SC 2.5.8 (AA) requires at least 24 × 24 CSS px, with spacing exceptions (https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html, last updated 2026-11-02). Design targets of 44px are common in checklists and in Apple's guidance. The Apple page did not load this session, so the 44pt iOS figure is **unverified** from memory.

**Responsive and mobile**
- Test at 390, 768 or 820, 1024, and 1440 widths (taste-skill's checker uses this set).
- Keep at least 16px side padding; text should not touch the viewport edge. No horizontal page scroll; clipped tooltips are a common defect (Impeccable checklist, 2026).

**Process**
- Write a short product brief first (audience, job, tone). Impeccable's `/impeccable init` writes a `PRODUCT.md` for this.
- Choose page kind and hero layout from the content (taste-skill lists page kinds and eleven hero layouts as starting points).

## Copy in UI

- Buttons: verb first, naming the outcome ("Save changes"). Avoid "OK", "Submit", "Proceed" (vectorlab-ux-skills list, **unverified** here).
- Errors: what happened, why if known, what to do next. Do not blame the user.
- Empty states: say what goes here and how to start. Copy rules here are conventions from checklists, not primary UX research.

## Existing anti-slop tools

- **Impeccable** (pbakaus; Apache 2.0 per search summary). README (fetched): 62 deterministic detection rules, 24 commands, no API key needed. Install with `npx impeccable install`. Detect with `npx impeccable detect src/`. Scans files in supported agents, runs in CI, and has a Chrome overlay. Counts differ across listing sites (17, 20, 23, 41 rules). The README is the authority. Source: https://github.com/pbakaus/impeccable
- **taste-skill** (Leonxlnx). README (fetched): v2.5.1. Rules include plain copy, real photos or licensed stand-ins, real brand icons, one hero entrance plus one or two moments per page, and a finish gate with browser checks at four widths. v1 is kept as a separate install. Several forks exist; the canonical repo is https://github.com/Leonxlnx/taste-skill. No release dates in the README.
- **Hallmark**, **unslop-ui**, and **ux-skill** wiki (Laith0003): detection or rule lists exist. Only snippets were seen. Not verified in detail. The wiki is at https://github.com/Laith0003/ux-skill/wiki/How-to-detect-AI-slop-in-your-design

## Gaps

- Owner-list items "untouched shadcn", "Lucide icons everywhere", "grain over a gradient", and "cursor-following beam" were not covered by any fetched source. Hover fade and grain are only partly covered. Check them separately before adding them to the tells list.
- Apple HIG and Material 3 pages did not return usable text. Touch-target figures for them are unverified.
- Explanation that models regress to "the statistical center" comes from a search snippet (https://superdesign.dev/blog/why-ai-design-looks-generic), not a fetched page.
- Reference-based style extraction, design tokens from mood boards, and measured recognition studies were not researched.
- Per CLAUDE.md, any of the owner's 20 listed items used in a product needs owner approval with a screenshot first. Existing UI using them should be flagged, not kept silently.
