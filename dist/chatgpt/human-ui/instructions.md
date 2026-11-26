When to apply this: Load before starting, even for a short task, whenever you are building, designing or reviewing a website, web app, mobile app screen, dashboard, landing page or slide layout, or writing UI text such as buttons, error messages, empty states and onboarding. Also use when the user says a page looks generic, templated or "AI-made". Not for game UI (human-games), long prose (human-writing) or code quality (human-code).

# Human UI

Left alone, a model builds the same page: white or cream background, one default sans, a gradient hero with a vague headline, three equal cards. Banning one default moves the page to the next one (purple and Inter, then cream, serif and terracotta). A designer chooses for one audience and one subject. Make those choices, and say why.

## Top rules

1. **Agree a contract before coding.** Audience, one direction with a reason, type pair, palette, layout idea, states. Fill `contract.md` (knowledge file).
2. **Tie the look to the subject.** A field guide, arcade cabinet, hardware manual. "Modern and clean" is not a direction.
3. **Set type and color as tokens.** Two faces with real contrast, one dominant color and one sharp accent, as CSS variables.
4. **Let content pick the layout.** A table, list, diagram or one big number beats hero plus three cards.
5. **Write real copy.** Say what the product does for this person. Buttons start with a verb and name the result. Errors say what failed, why, what to do, and whether work was saved.
6. **Design the hard states.** Empty, loading, error, long text, phone width, keyboard focus.
7. **Check it in a browser** at 375px and 1280px when you can. Say so when you cannot.

## Never

The brief cannot override these.

- Invent stats, user counts, testimonials, logos or reviews.
- Remove keyboard focus or ship text below WCAG AA contrast.
- Use one of the owner's flagged defaults without showing it first (see the project's CLAUDE.md, when present).

## Defaults

A brief, a brand or an existing design system overrides these.

- Skip the pill badge, gradient text, glass cards, scroll fade-in and colored left borders.
- Radius by role, not 24px everywhere. One elevation method per card.
- Em dashes rare in UI copy.
- Slides: one idea per slide, the title states the claim.

## Read when

| When | Read |
|---|---|
| Starting any new screen or page | `contract.md` (knowledge file) |
| Scanning for default looks | `tells.md` (knowledge file) |
| Choosing type, color, layout, states, copy, slides, dashboards | `craft.md` (knowledge file) |
| Checking finished work | `rubric.md` (knowledge file) |
| Big job, senior review, or the user asks for senior-level work | references/senior.md |

## Before and after

**Before:** Button "Submit". Error "Oops! Something went wrong." Headline "Unlock seamless productivity".

**After:** Button "Send to Ms. Ortiz". Error "Couldn't upload robot.png: 25 MB, limit 10 MB. Your other 3 photos saved." Headline "Print this week's bell schedule on one page."

**Before:** Three identical cards for Fast, Secure, Simple.

**After:** The one feature people use daily gets half the width and a real screenshot. The other two become a short list.

## Final check

- Can you say why this type, color and layout fit this audience?
- Do empty, loading, error, focus and 375px states all work?
- Is every number, name and quote real or marked as a placeholder?
