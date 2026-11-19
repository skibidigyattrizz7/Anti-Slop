# UI craft

How skilled designers work, by area. Sources: owner's skill and 2026 practitioner notes (see `tells.md`). Rules marked "convention" come from checklists, not user research.

## Direction

Start from the subject. A bakery, a physics tool and a clan page should share almost nothing visually. Pick one world (notebook, arcade cabinet, newspaper, hardware manual, museum label) and let it set type, shape and texture. Add one memorable moment: a hand-drawn underline, a big number, a loading screen with character.

## Type

- Two families at most. Weight and size carry hierarchy.
- Few sizes, clear steps (about 1.25 ratio or more between neighbors).
- Body 16px, line height 1.5 to 1.7, lines 60 to 75 characters.
- Tighten tracking slightly on large display type and check it by eye. Shorten the headline before shrinking it.

## Color

- Semantic tokens: `--surface`, `--text-muted`, `--accent`. No raw hex scattered in components.
- Neutrals do most of the work. The accent covers about 10%.
- Contrast: 4.5:1 for normal text, 3:1 for large text (WCAG AA). Show state with words or icons too, never color alone.
- Design dark mode on its own.

## Layout and spacing

- One spacing scale (4 or 8 px). More space between groups than inside them.
- Content picks the shape: table, list, diagram, split pane, one big number. Break the grid on purpose with asymmetry or one oversized element.
- Flatten nested containers. Radius by role: cards about 12 to 16px, pills for tags.
- 16px minimum side padding on phones. No horizontal page scroll.
- Touch targets: WCAG 2.2 AA allows 24px with spacing. Aim for 44px on phones (common guidance, the Apple figure is unverified here).

## States

Design all five: empty, loading, error, disabled, zero results.

- Loading: a skeleton of the real layout, or inline progress. Never show "No results" before data arrives.
- Empty: say why it is empty and give one way forward.
- Error: what failed, why, what to do, was work saved.
- Test with a 60-character name, 200 rows, a missing image.

## Copy

- Buttons: verb plus result ("Save draft", "Send to teacher").
- Onboarding starts the first real task. It does not list features.
- Tone matches stakes: serious for money and data, light only when nothing is at risk.
- Real facts only. Placeholders are marked.

## Motion

Motion answers a question: where did this come from, what changed. One staged entrance at most, plus press and state feedback. Animate `transform` and `opacity`. Honor `prefers-reduced-motion`.

## Slides

One idea per slide. Titles state the claim ("Homework time dropped 20 minutes"). Replace title plus three bullets with a big number, a real image, a diagram or one sentence. No agenda slide restating the deck, no "Key takeaways" closer.

## Dashboards

Start from the decision the reader makes. Show the one number that matters, big, with unit and "so what". Avoid four identical KPI cards with green arrows and charts with no question. Use a dataviz skill for charts when one is installed.

## Mobile app screens

One primary action per screen, reachable by thumb. Native patterns first (back, tabs, sheets). Show the loading and offline states. Keep type 16px or more.

## Longer before and after

**Brief:** study-group app for 9th graders.

**Default:** white page, Inter, "Supercharge Your Productivity" on a purple gradient, three cards with emoji, rounded-2xl everywhere.

**Directed:**
- Direction: notebook paper with faint ruled lines, because students already live in notebooks.
- Type: chunky display face for headings, readable serif for body.
- Palette: highlighter yellow `--accent`, ink-blue `--text`, paper `--bg`.
- Layout: features as slightly rotated sticky notes, the plan view takes most of the screen.
- States: empty plan says "No tasks yet. Add the first one." with one button.
- Copy: "Your group chat, but it finishes the homework plan."
- Check: 375px and 1280px screenshots, tab through the page, run the scanner.

Tools that exist for related checks: Impeccable (`npx impeccable detect src/`) scans source for patterns. Optional. Nothing here depends on it.
