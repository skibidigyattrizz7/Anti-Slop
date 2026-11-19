# UI tells (dated)

last_verified: 2026-11-17. Source mix: owner's master list (Oct 2026) and practitioner pages from 2026. Most lists come from agencies and tool vendors, so treat them as opinion, not measurement.
Re-check: visual defaults every 3 months (they rotate), layout and states every 6 months, everything after a major model release.

A tell is a reason to ask "did I choose this?". It is never proof of who or what made the page. One tell means little. Several together mean the page is running on defaults.

## Structure and layout (slowest to expire)

| Tell | Fix |
|---|---|
| Centered hero: vague headline, subhead, one or two buttons | Name the customer, the problem and the outcome. Vary the layout by product |
| Three equal feature cards in a row, icon plus title plus two lines | Give the main feature more space. Use a list, split or real screenshot |
| Icon in a rounded tile above each heading | Put the icon beside the text, or drop it |
| Pill badge above the headline ("New", "AI-powered") | Drop it, or put the news in the headline |
| Same section height, padding and alignment all the way down | Group tightly, separate groups widely, alternate anchor and support sections |
| Nested cards, or border plus shadow plus tint on one card | Flatten. Pick one elevation method |
| Stat banner of round invented numbers; fake logo row; fake testimonial | Real numbers with context, or remove |
| Numbered 01, 02, 03 on things that are not a sequence | Number only real steps |
| Only the happy path designed: no empty, loading, error | Design all five states |
| Actions visible only on hover | Keep them visible or in a labeled menu |
| `outline: none` with no replacement | Add `:focus-visible` |
| Placeholder names (John Doe, Acme), lorem ipsum | Real or marked `[needed: ...]` |

## Visual defaults (rotate every few months)

| Tell | Fix |
|---|---|
| Purple to blue or indigo gradient on hero, buttons, background | Palette from the product. Solid color |
| Gradient text on headings or numbers | Solid color. Emphasis by weight or size |
| Inter or Geist (or Plus Jakarta) as the only face at default weights | Choose a display and text pair for the direction. Inter is fine when chosen |
| Space Grotesk with Instrument Serif; italic serif accent word in the hero | Pick for the product's voice. Italic only in editorial work |
| Glassmorphism, glow, blur on every card | Blur only where layers overlap |
| rounded-2xl or 24px+ radius on everything | Radius by role. Pills only for tags |
| Colored left-border cards | Remove the stripe, or use a tint |
| Scroll fade-in on every block; same hover tween on every control | One or two moments tied to action. Respect reduced motion |
| Emoji as headings, bullets or icons | One icon set, or none |
| Bounce or elastic easing on UI | Ease-out on `transform` and `opacity` |
| Second wave (2026): cream background, serif display, terracotta accent, "editorial" with no brand reason | Choose from the subject, not from the trend |

## Copy

| Tell | Fix |
|---|---|
| Elevate, Unlock, Seamless, Transform, Supercharge, all-in-one, "the future of X" | Say what it does, for whom, with a real number or before and after |
| "Oops! Something went wrong", "Submit", "OK" | Reason, next step, saved or not. Verb plus result |
| Many em dashes in UI copy | Commas, colons, periods |
| Manufactured contrast ("It's not X, it's Y") | State Y |

## Guards

- A brand guide, an existing design system or a client's request outranks this list.
- Inter, a three-column grid or a gradient used on purpose and tied to the subject is fine. Say the reason in the contract.
- Check accessibility and states first. Style tells matter less than a page that fails at 375px.
- The scanner reads source text only. Judge the rendered page.

## Sources

- Owner's master list, Websites and UI section, Oct 2026.
- Impeccable slop catalogue, 2026: https://github.com/pbakaus/impeccable
- utsubo trust-signals post, 2026-06-23; Laith0003 ux-skill wiki, edited 2026-11-11.
- NN/g empty-state article, 2021-09-19 (principles current, details dated).
- Unverified, left out: the origin of the indigo default, and the owner-list items shadcn, Lucide, grain and cursor beam (no source checked).
