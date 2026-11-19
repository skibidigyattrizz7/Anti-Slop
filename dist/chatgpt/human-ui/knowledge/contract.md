# Design contract

Fill this in before writing code. It takes ten minutes and saves a redesign. Keep it in the repo (for example `DESIGN.md`) so later changes follow it. If the user has a brand or design system, copy its values in and skip the choices. If a field is unknown, ask or write `[needed: ...]`. Never invent a fact about the audience.

## 1. Who and what for

- **Audience:** one sentence. Age, setting, device, how much time they have.
- **The one job:** what they come here to do, in a verb phrase.
- **Where they use it:** phone in a hallway, desktop at work, projector.

## 2. Direction and reason

- **One direction:** a thing from the real world that matches the subject (field guide, arcade cabinet, hardware manual, newspaper, record sleeve).
- **Why it fits:** one sentence linking it to the audience or the content.
- **Not this:** two defaults you are avoiding for this project and why.

## 3. Type pair

- **Display:** family, weight, where used.
- **Text:** family, weight, size (16px or more for body), line height 1.5 to 1.7.
- **Why they contrast:** a different shape, weight or width, not two similar sans faces.
- **Fallback stack** and how fonts load (self-hosted or a link).

## 4. Palette as CSS variables

```css
:root {
  --bg: ;            /* page */
  --surface: ;       /* cards, panels */
  --text: ;          /* body, passes 4.5:1 on --bg */
  --text-muted: ;    /* passes 4.5:1 on --bg */
  --accent: ;        /* primary action, about 10% of the screen */
  --accent-text: ;   /* text on --accent, passes 4.5:1 */
  --danger: ;        /* errors, with an icon or words too */
  --focus: ;         /* focus ring, 3:1 against what it touches */
}
```

- Dark mode: own values, or none. Do not invert light mode.

## 5. Layout shaped by content

- **What the content is:** list, table, steps, one number, a long read, a gallery.
- **The shape that fits it:** name it (split pane, single column, table with filters). Say what gets the most space and why.
- **Mobile at 375px:** what collapses, what stays visible, which actions are reachable by thumb.
- **Spacing scale:** 4 or 8 px steps. One radius per role (card, button, tag).

## 6. States to design

For each screen or component, one line each:

| State | What the user sees and can do |
|---|---|
| Empty | Why it is empty, one way forward |
| Loading | Skeleton of the real layout, or inline progress |
| Error | What failed, why, what to do, was work saved |
| Long or odd content | Long names, 200 items, no image |
| Keyboard | Order, visible focus on every control |
| Reduced motion | What stops or becomes instant |

## 7. Motion and finish gate

- **Motion:** one or two moments tied to an action. Animate `transform` and `opacity`.
- **Finish gate, after building:** the rubric in `rubric.md` passes. Screenshots at 375px and 1280px, or a note that no browser was available. `scripts/scan_ui_defaults.py` counts reviewed.

## Agreed by

Name and date. Changes to sections 2 to 5 need a new line in the contract, with the reason.
