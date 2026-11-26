# Senior UI/UX craft: numbers, decisions, teaching notes

Fetched 2026-11-26. Tags: [V] = opened this session; [L] = read in a local skill file (path given); [M] = from memory/general knowledge, not opened, treat as unverified. Not reviewed: existing human-ui craft.md/rubric.md/tells.md bodies (only headings read), so the writer must dedupe against them.

## 1. Typography

### Takeaway
Seniors pick few sizes on a ratio, cap line length, tighten leading as size grows, and use tabular figures in data. Contrast in the pair matters more than the font name.

### Cited findings
- Line length: 45 to 90 chars average incl. spaces; check by fitting 2 to 3 alphabets on a line. Why: tracking back to the next line gets hard past ~90. Local skills use a stricter 65 to 75ch for body. Use 45-75ch for body, up to 90 for wide-leading prose. [V] [Butterick](https://practicaltypography.com/line-length.html)
- Body line length cap 65 to 75ch; `text-wrap: balance` on h1-h3, `text-wrap: pretty` on prose; display letter-spacing no tighter than -0.04em; display clamp max about 6rem (96px). [L] impeccable/SKILL.md
- Scale: brand/marketing pages use a fluid `clamp()` scale with ratio >=1.25 between steps; app UI uses fixed rem with 1.125 to 1.2 steps (fluid type breaks spatial predictability in dense layouts). Ratios named: 1.25, 1.333, 1.5. [L] impeccable/reference/typeset.md
- Pairing: do not pair two similar-but-not-identical faces (two geometric sans). Pair on a contrast axis (serif+sans, geometric+humanist) or one family in several weights. [L] impeccable/SKILL.md
- Numbers in tables: `font-variant-numeric: tabular-nums`, right-align numeric columns, units with a non-breaking space (`10&nbsp;MB`). [V] [Vercel Web Interface Guidelines](https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md); Apple also says use monospaced digits for tables/timers/prices [M, fetch returned title only].
- Platform sizes (iOS defaults): Body 17, Callout 16, Subhead 15, Footnote 13, Caption 12/11; avoid thin/light weights for small text; do not tighten system leading. [M, HIG page did not render; verify at https://developer.apple.com/design/human-interface-guidelines/typography]
- Line height by size [M, convention, not sourced this session]: body 1.5 to 1.6; 20-32px 1.3 to 1.4; display 1.0 to 1.15. Rule: leading shrinks as size grows. Refactoring UI makes the same point (unopened).
- Optical sizing: use a font with an `opsz` axis (`font-optical-sizing: auto`) so small text gets wider spacing and large text gets finer detail [M]. Check: caption text uses the text cut, hero uses the display cut.

### Inferences
- A defensible default: one family + one contrast face, 5 to 7 sizes on 1.2 (app) or 1.25 to 1.333 (marketing), 2 to 3 weights. Anything more needs a stated reason.

### Gaps
- Butterick line-spacing page and Refactoring UI not opened. Apple typography page did not render.

## 2. Layout and spacing

### Takeaway
Spacing is a short scale applied by relationship (tight inside a group, loose between groups). Density is a decision about the user, not a style.

### Cited findings
- 4pt/8dp spacing increments; min 8px gap between touch targets; touch targets 44x44pt (Apple) / 48x48dp (Material). [L] ui-ux-pro-max/references/quick-reference.md (cites HIG/MD; HIG/MD pages not opened [M])
- Breakpoints systematic, e.g. 375 / 768 / 1024 / 1440. [L] same file.
- Vary spacing for rhythm; cards are the "lazy answer", nested cards always wrong; `repeat(auto-fit, minmax(280px, 1fr))` for breakpoint-free grids; semantic z-index scale (dropdown, sticky, modal-backdrop, modal, toast, tooltip) not 999. [L] impeccable/SKILL.md
- Oversized equal padding everywhere destroys hierarchy; use a consistent scale and realistic content, not lorem ipsum. [L] ziad-skills/frontend-ui-engineering/SKILL.md
- F-pattern is real but conditional: appears on text-heavy, unformatted pages with an efficiency-minded, low-interest reader; rarely a clean F; NN/g lists other patterns (layer-cake, spotted, commitment). Good headings, bold lead-ins and bullets reduce it. So: it is a failure mode to design against, not a layout to copy. Z-pattern: no primary source found; treat as folklore [M]. [V] [NN/g F-shaped pattern](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/) (published 2017-11-12, reviewed 2026-08-19)
- Density: product register (app UI, admin, dashboards) vs brand register (marketing) is the first fork; read different references for each. [L] impeccable/SKILL.md steps 4. Numeric density guidance (row height 32 to 40px pro tools, 48 to 56px consumer, 8 to 12px cell padding) [M, convention, not sourced].
- Shadows: one light source, offset y = 2x offset x, raise elevation by raising offset+blur and lowering opacity; layered shadows (e.g. 1/2/4/8/16px at ~0.075); tint shadow with the background hue not black; tokenize sm/md/lg. [V] [Josh Comeau](https://www.joshwcomeau.com/css/designing-shadows/)

### Inferences
- Check for a screen: squint test shows one clear first thing; any two groups differ in gap by at least 2x the in-group gap.

### Gaps
- No primary source for Z-pattern; no sourced pro-vs-consumer density numbers.

## 3. Colour

### Takeaway
Build in OKLCH with lightness as the contrast lever, but verify with a contrast method; ship semantic tokens so dark mode is a token swap.

### Cited findings
- OKLCH: L 0 to 1 perceptual; C from 0, stays under ~0.37 in sRGB/P3; H 0 to 360 (red ~20, yellow ~90, green ~140, blue ~220, purple ~320). Unlike HSL, equal L looks equally light across hues. Derive variants with relative color `oklch(from var(--accent) calc(l + 0.1) c h)`. Out-of-gamut values may clip in browsers, so add a `@media (color-gamut: p3)` override. Author's own correction: OKLCH is not a contrast checker, use APCA. [V] [Evil Martians](https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl)
- Dark mode via tokens: redefine `--surface-*`, `--text-*` in `prefers-color-scheme: dark`; components reference tokens only. [V] same.
- WCAG 2.2 1.4.3: 4.5:1 text, 3:1 large; 1.4.11: 3:1 for UI component visuals and required graphics. [V] [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- APCA (candidate for WCAG 3, not final): Lc 90 preferred body, Lc 75 min body, Lc 60 min other content text, Lc 45 large/headline (36px regular, 24px bold), Lc 30 placeholder/disabled/solid icons, Lc 15 dividers (below is invisible). Add Lc 15 for AAA. Lookup depends on size and weight. [V] [APCA in a Nutshell](https://git.apcacontrast.com/documentation/APCA_in_a_Nutshell.html)
- Tinted neutrals: add 0.005 to 0.015 chroma toward the brand hue. Cream/sand near-white bodies (L 0.84-0.97, C<0.06, hue 40-100) are a 2026 AI tell; warmth should come from accent, type, imagery. Four strategies: restrained (neutrals + one accent <=10%), committed (one colour 30 to 60%), full palette, drenched. [L] impeccable/SKILL.md
- Placeholder text needs 4.5:1 like body; muted gray on tinted near-white is the commonest failure. [L] impeccable/SKILL.md
- Dark/light is not a default: write one sentence on who uses it, where, under what light. [L] impeccable/SKILL.md
- Colour for data and dark mode depth: the installed `dataviz` skill has a runnable validator and palette formula (not opened) [L listing only]. Dark mode specifics (lift surfaces with lightness not shadow, desaturate accents ~10 to 20%, avoid pure #000 text-on-black glare) [M].
- Never colour alone for error: add icon and text; red error, orange/yellow warning, green/blue success. [V] [NN/g form errors](https://www.nngroup.com/articles/errors-forms-design-guidelines/)

### Gaps
- Semantic-token naming conventions from a primary source not opened (see section 8).

## 4. Interaction, states, forms

### Takeaway
Design the eight states, validate on blur, answer within 100 ms, signal at 1 s, show progress and cancel at 10 s.

### Cited findings
- Response limits: 0.1s feels instant (show only the result); 1s keeps train of thought (show something is working); 10s loses attention (percent-done and a way to cancel). [V] [NN/g response times](https://www.nngroup.com/articles/response-times-3-important-limits/) (Miller 1968/Card 1991 lineage; page date not shown)
- Eight states for every control: default, hover, focus, active, disabled, loading, error, success. Hover and focus differ; keyboard users never see hover. Focus ring: `:focus-visible`, 2-3px, offset, 3:1 against neighbours, same everywhere. [L] impeccable/reference/interaction-design.md
- Forms: visible labels (placeholders are not labels); validate on blur, not per keystroke (exception: password strength); error below field linked by `aria-describedby`. NN/g agrees: validate when the user leaves the field, error next to field, summary only as supplement, no hover-only error tooltips, same error 3+ times means fix the design. [L] same; [V] [NN/g](https://www.nngroup.com/articles/errors-forms-design-guidelines/)
- Vercel rules: submit stays enabled until request starts then spinner; focus first error on submit; never block paste; correct `type`/`inputmode`/`autocomplete`; loading text ends with an ellipsis; destructive actions need confirmation or undo. [V] [Vercel guidelines](https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md)
- Optimistic UI for low-stakes (likes, follows), not payments or destructive; skeletons beat spinners. [L] impeccable/reference/interaction-design.md
- Undo vs confirm: prefer undo (toast with 5 to 10s undo) for reversible actions; confirm only for irreversible or costly ones, with the verb and the object ("Delete 3 files?") and consequence. [L] design/skills/ux-copy (verb and consequence); the 5 to 10s window is [M].
- Copy shape: error = what happened + why + how to fix (+ was work saved); empty state = what this is + why empty + how to start; CTA starts with a verb. [L] design/skills/ux-copy
- Empty/error states are part of the build, not a follow-up. [L] ziad-skills/frontend-ui-engineering

### Gaps
- Skeleton vs spinner threshold (e.g. skeleton after 300 to 400ms) not sourced; Nielsen undo-over-confirm essay not opened.

## 5. Motion

### Takeaway
Ask frequency first; most high-frequency actions get no animation. When used: transform and opacity, ease-out, under 300ms, interruptible, reduced-motion aware.

### Cited findings
- Frequency table: 100+/day (keyboard, command palette) none; tens/day remove or cut; occasional standard; rare/first-time can delight. [L] emil-design-eng/SKILL.md
- Durations: button press 100-160ms; tooltip 125-200; dropdown 150-250; modal/drawer 200-500; UI stays under 300ms. [L] emil-design-eng/SKILL.md. Alternate table: tooltip 80-120, button 120-180, card 200-350, modal 300-400, page 400-600, exit = 65-75% of entrance, distance scaling (50px=0.8x ... full screen 1.8-2x). [L] motion-design/reference/timing-easing-tables.md. They overlap; pick one table per project.
- Easing: enter/exit ease-out; on-screen move ease-in-out; hover/colour ease; constant linear. Never ease-in on UI. Built-ins are weak: `cubic-bezier(0.23,1,0.32,1)` out, `(0.77,0,0.175,1)` in-out, `(0.32,0.72,0,1)` drawer. [L] emil-design-eng. M3 reference values `(0.2,0,0,1)` standard [L] motion-design table; M3 page itself did not render [unverified at m3.material.io].
- Origin-aware popovers (transform-origin at trigger; modals stay centred); never animate from scale(0), start 0.9-0.97 + opacity; press `scale(0.97)` on :active; transitions over keyframes for interruptibility; springs: duration 0.5, bounce 0.1-0.3. [L] emil-design-eng
- Properties: animate transform/opacity only, never `transition: all`; honour `prefers-reduced-motion` (gentler, not zero: keep opacity/colour, drop movement); gate hover motion behind `(hover: hover) and (pointer: fine)`. [L] review-animations/SKILL.md; [V] Vercel guidelines.
- Reveals must enhance an already-visible default; never hide content until a class fires (hidden tabs and headless renderers never fire it, page ships blank). One identical entrance on every section is the tell. [L] impeccable/SKILL.md
- Apple: respond on pointerdown, 1:1 tracking, velocity on release, always interruptible. [L] apple-design/SKILL.md (derived from WWDC 2018 Designing Fluid Interfaces, not re-watched [M])
- Never animate (rule of thumb): layout properties, keyboard-triggered actions, text content people are reading, errors with shake over 400ms. [L/M]

### Gaps
- M3 duration tokens not retrieved.

## 6. Accessibility

### Takeaway
Native elements first, visible focus, 24px floor (44 target), test with keyboard and a screen reader; automated tools catch a minority.

### Cited findings
- WCAG 2.2 2.5.8 (AA): targets >=24x24 CSS px unless spacing (a 24px circle on each target's bounds must not hit another), equivalent control, inline, user-agent, or essential. 2.5.5 (AAA): 44x44. [V] [W3C Understanding 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- New in 2.2: 2.4.11 Focus Not Obscured (AA, sticky headers must not fully cover focus), 2.4.13 Focus Appearance (AAA), 2.5.7 Dragging Movements (AA, give a non-drag alternative), 3.3.7 Redundant Entry (A), 3.3.8 Accessible Authentication (AA); one-line meanings for the last three are [M]. [V] [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- Native first: `<dialog>.showModal()` or `inert` on background for focus trap; Popover API for non-modal overlays. [L] impeccable/reference/interaction-design.md. No `div`/`span` with click handlers; icon buttons need `aria-label`; async updates in `aria-live="polite"`; sticky headers must not cover focus; no `user-scalable=no`. [V] Vercel guidelines
- Testing approach: automated scan (~30% of issues, per skill claim, unverified number), keyboard-only pass, VoiceOver and NVDA, contrast. [L] design/skills/accessibility-review (note: it cites WCAG 2.1 and 2.5.5 44px as AA, which is wrong; 2.5.5 is AAA and 2.5.8 is the AA one)
- Focus order follows DOM order; fix the DOM, not `tabindex>0` [M]. "No ARIA is better than bad ARIA" (W3C ARIA Authoring Practices) [M, unopened].

## 7. Design systems and tokens

### Takeaway
Three layers: primitive (raw values), semantic (role), component (scoped). Components read semantic tokens only.

### Cited findings
- Token families: colour (brand, semantic, neutral), type, spacing, borders/radius, shadows, motion; components list variants, sizes, states, behaviour, a11y. Principle: consistency over creativity, flexibility within constraints. [L] design/skills/design-system/SKILL.md
- Dark mode proves the layering: components never carry their own `@media` rules. [V] Evil Martians (above)
- Icon sizes, z-index, radius by role, elevation as tokens, not ad-hoc values. [L] ui-ux-pro-max/references/pro-rules.md; impeccable
- Naming: name by role (`--surface-raised`, `--text-muted`, `--accent`) not value (`--gray-200`) at semantic level; names like `--cream`/`--sand` are themselves a tell. [L] impeccable for the tell; role-naming [M].
- When to break the system: when the content demands a new pattern more than 2 to 3 times, or a one-off hero/marketing moment; record the exception and fold it back or delete it. [M, convention]

### Gaps
- No primary design-system source (Material tokens, Primer, Polaris) opened.

## 8. Critique

### Takeaway
Critique the goal first, then hierarchy, usability, consistency, accessibility; separate "what I see" from "what I'd change".

### Cited findings
- Framework: first impression (2 seconds: what draws the eye, is it right, is the purpose clear), usability, hierarchy and reading order, consistency, accessibility. Needs context: what it is, who for, which stage, focus. [L] design/skills/design-critique/SKILL.md
- Two independent passes: a design review and tool-based evidence (detector/browser), with the judgment pass finished before tool output enters, to avoid anchoring. Banner when degraded. [L] impeccable/reference/critique.md
- Anti-slop gate: brief, existing UI and tokens outrank the skill; define a contract (screen's job, primary action, required states, responsive rules, patterns to reject) before building. [L] ziad-skills/anti-ui-slop/SKILL.md, frontend-ui-engineering/SKILL.md
- 30-second screen judgment (synthesis [M], from the above): 1) squint: one primary focus? 2) name the job in one sentence; 3) read contrast of the lightest text; 4) tab through once: focus visible, order sane; 5) find the empty/error/long-text case; 6) 375px check; 7) scan for tells (gradient text, three identical cards, badge, fade-on-scroll).
- Facilitation (Rauno, Linear, Emil, Smashing critique writing) not opened. Treat structure as [M]: state goals, ask "what problem does this solve", critique against the goal not taste, one owner decides.

## Build on these local skills

All under /root/.claude/skills/synced/d13e5c22-fd75-4b81-b6fa-7bbe4432d675_ad4b38a0-ff16-4a31-8117-7e768f4021ea/ unless noted. Plugin root P = /root/.claude/plugins/synced/d13e5c22-fd75-4b81-b6fa-7bbe4432d675_ad4b38a0-ff16-4a31-8117-7e768f4021ea/.

| Path | Reuse | Weak | License |
|---|---|---|---|
| impeccable/ (SKILL.md 2.9k words, reference/*.md: interaction-design, typeset, critique, product, brand, harden, polish) | Best overall. Contrast, type, OKLCH, colour strategies, 8 states, focus, forms, product vs brand register, bans list. Link to reference files rather than copy. | Needs its node scripts and PRODUCT.md setup; long; some rules forced (e.g. critique requires sub-agents). Its own bans overlap the owner's tells list. | Apache 2.0 (frontmatter); no LICENSE file found |
| emil-design-eng/SKILL.md | Motion frequency table, durations, easings, origin-aware, press scale, review table format. Strongest on motion and "unseen details". | Motion-only; initial-response gate says reply only with a canned line; opinionated (blur masking, no ease-in). | none found |
| review-animations/SKILL.md (STANDARDS.md referenced but not present) | Ten motion standards as a review checklist. | Missing STANDARDS.md; manual-invoke only. | none found |
| motion-design/ (reference/timing-easing-tables.md, quality-checklist.md, patterns/) | Duration-by-element, exit 65-75%, springs table, latency limits. | Tables conflict with Emil's (350-800ms premium); pick one. | MIT (LottieFiles 2025) |
| apple-design/SKILL.md | Fluid-interface rules: response, 1:1 tracking, interruptibility, springs. | Source is one talk; web translation is interpretive. | none found |
| ui-ux-pro-max/ (references/quick-reference.md, pro-rules.md, data/) | Touch targets, 4/8 spacing, breakpoints, pre-delivery checklist. | Mobile-leaning; suggests Lucide icons (on owner's flagged list). | MIT (Next Level Builder 2024) |
| web-design-guidelines/SKILL.md | Fetches Vercel's live rules; best terse code-review checklist (verified list above). | Depends on network fetch; 176 words only. | none found; Vercel repo licence unchecked |
| design-taste-frontend/, high-end-visual-design/, minimalist-ui/, redesign-existing-projects/ | Mostly style direction; redesign skill is a useful audit order for existing UIs. | design-taste is 12.8k words and prescribes looks (GSAP, bento, layout randomisation) that risk new defaults; high-end and minimalist ones push specific aesthetics. Not read in depth. | MIT (design-taste: Leonxlnx 2026); others have LICENSE files (text not read) |
| animation-vocabulary/SKILL.md | Glossary to name effects (pop in, stagger, origin-aware). Good for teaching mode. | Naming only. | none found |
| P ziad-skills/skills/anti-ui-slop/ | Contract + required states + finish gate. | Pushes a paid UIZZE MCP; has a CHECKSUMS and NOTICE so keep intact if bundled. | MIT |
| P ziad-skills/skills/design-dna/ | Tokens / style / effects schema from reference screenshots. | Includes glassmorphism and 3D effects by default; heavy. | MIT |
| P ziad-skills/skills/frontend-ui-engineering/ | AI-aesthetic table, a11y, loading, verification. | Says WCAG 2.1; generic. | none found |
| P design/skills/{design-critique, accessibility-review, design-system, ux-copy}/ | Critique framework, copy patterns, system audit. Short and usable. | accessibility-review says 2.5.5 44px is AA (wrong for 2.2); WCAG 2.1 only. | none found |
| vectorlab-ux-skills (listed in session: ux-audit, spacing, typography, colour-palette, motion, forms, errors, empty-states, loaders, reduced-motion) | Likely the fine-grained per-topic rules. | Not found under /root/.claude/plugins (find returned nothing), so not read. | unknown |

## Teaching notes

How a senior explains a choice to a junior (pattern: constraint, choice, number, what breaks otherwise, how to check).
- Scale: "We use 1.2 steps because this is a dense tool; bigger jumps eat rows. Check: can you tell h2 from h3 at arm's length without colour?"
- Line length: "Body stops at 65ch because eyes lose the next line past ~75; Butterick allows 90. Check: count two alphabets across."
- Tabular figures: "Digits differ in width by default, so a column of prices wobbles; `tabular-nums` fixes it. Check: align a column of 1s and 8s."
- Spacing: "Gap inside a group is half the gap between groups; that is how the eye sees groups without borders. Check: squint."
- Colour in OKLCH: "Same L means same lightness, so I can swap hue without re-checking contrast; I still run APCA or WCAG because L is not a checker."
- Contrast: "4.5:1 is the floor, not the target; muted gray 'for elegance' is the commonest fail. Check the placeholder too."
- Validation on blur: "Errors while typing punish people for not being finished. Check: type half an email."
- 0.1/1/10s: "Under 0.1s show the result; at 1s show it is working; at 10s give progress and Cancel."
- Motion: "Used 100 times a day? No animation. Otherwise 150-250ms, ease-out, transform and opacity, because ease-in delays the moment the eye is on it."
- Targets: "24px is the legal floor in WCAG 2.2, 44px is the thumb. Expand the hit area with padding, not the icon."
- Undo over confirm: "Confirm dialogs get clicked through; undo lets people act fast and recover."
- Breaking the system: "I broke the token here because X; if it happens a third time we add a token."
- Mode design: each explanation should name the alternative rejected and the one-line check, in two sentences max, so the junior can repeat the test.
