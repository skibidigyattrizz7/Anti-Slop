# JUDGE report: human-ui, run 2026-11-17

Brief and audience: homepage for Chen's Cycle Repair, local walk-in customers on phones. Facts given: Tue to Sat 9 to 5, tune-up $65, flat repair $15, 4th Street, 555-0142, no invented testimonials or stats. Fidelity check applies (U6).
Evidence: shoot.cjs screenshots (phone 375, desktop 1280) read with Read, scan_ui_defaults.py --json, full source read.

## t-a.html

```
Verdict: Ship      Score: 8/8 checks pass
Category: ui   Rubric: /home/user/anti-slop/skills/human-ui/references/rubric.md

Checks:
U1 PASS  Phone and desktop screenshots: no horizontal scroll (overflowPx 0), nothing clipped, text readable. `a:focus-visible { outline: 3px solid var(--focus); outline-offset: 3px; }`, links are the only controls and are in natural order. No empty/loading/error states exist because the page has no data or forms (static page; N/A in spirit, counted PASS). Live keyboard tabbing not run.
U2 PASS  Price-tag look: `.tag { border: 2px dashed ...}` with big serif `$65` / `$15`, slab serif display `--display: Rockwell, "Roboto Slab", Georgia`, warm paper `--bg: #f3ede2`. Fits a small shop with a price board. Reason is visible in the page, not written in a comment.
U3 PASS  Two faces (`--display` slab serif + `--text-font: system-ui`), color tokens on :root with a dark-mode set, muted text `#5b5448` on `#f3ede2` is about 6:1, white on `#b8460f` about 5.4:1. No color-only state.
U4 PASS  Two price tags, not three equal cards; hierarchy from size ($65 at up to 4rem), rules `section { border-top: 1px solid var(--text) }`, one 12px radius on tags and 6px on button. No nested cards. Desktop column is a narrow 40rem, fine for content this short.
U5 PASS  "Bike repair on 4th Street", "Call 555-0142" (verb plus result), "Tune-ups and flat repairs. Open Tuesday to Saturday, 9 to 5." No buzzwords. "Closed: Sunday and Monday" is a direct consequence of Tue to Sat, not a new fact.
U6 PASS  Only $65, $15, Tue to Sat, 9 to 5, 4th Street, 555-0142 appear. No testimonials, stats, logos, or service claims.
U7 PASS  No animation, nothing to honor reduced-motion for. Dashed border has a job (price tag).
U8 PASS  Scanner returned 0 flags and all zero counts. Read against screenshots: no gradient, blur, badge, emoji, em dash. Note the scanner's font result is wrong (see Tool notes), so it was not used as the only evidence.

Top fixes (most important first, 5 at most):
1. .lede "Tune-ups and flat repairs. Open Tuesday to Saturday, 9 to 5." -> at 1280px wraps with "to 5." alone on line 2 (max-width 30rem) -> widen to about 36rem or use text-wrap: balance.
2. a (all links, e.g. `<a href="tel:555-0142">555-0142</a>` in the hours list) -> unstyled default blue underlined link, low contrast in dark mode on #242019/#1a1815 and clashes with the palette -> add `a { color: var(--accent) }` or inherit text color, and give it a 44px tap area (scanner/shoot flags 1 small tap target, this link).
3. h1 "Bike repair on 4th Street" -> wraps to "Bike repair on 4th / Street" on phone, orphan -> text-wrap: balance.
4. .hours "Find us / On 4th Street" -> label adds nothing and there is no street number, so a visitor cannot find the shop -> mark the address as a placeholder or ask for the number (do not invent one).
5. Dark mode -> not screenshotted by the tool; confirm the link color and dashed border in dark.

Could not check: dark-mode rendering (shoot.cjs only captures the light scheme), live keyboard tab order (judged from source), real Rockwell rendering (the sandbox fell back to a Times-like serif; the slab look depends on the visitor's fonts).
```

## t-b.html

```
Verdict: Fix first      Score: 4/8 checks pass
Category: ui   Rubric: /home/user/anti-slop/skills/human-ui/references/rubric.md

Checks:
U1 PASS  No horizontal scroll (overflowPx 0), nothing clipped, text readable at 375 and 1280. `.btn:focus-visible, .phone:focus-visible { outline: 3px solid var(--accent); ...}` present. Static page, no data states needed. BUT the layout has a visible spacing defect, see U4. Live keyboard tabbing not run.
U2 FAIL  No visible reason for the look: centered-left hero with big sans h1, thin gray rules, white rounded cards, system sans. Nothing says "bike shop"; it would fit any small business by swapping the name. Reads as the default for its era.
U3 FAIL  One face only: `font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;` for everything including h1 and h2. Tokens and contrast are fine (muted #5c5a55 on #f7f5f0 about 6:1), but the type pairing requirement fails.
U4 FAIL  `.wrap { padding: 0 16px }` (class) beats `section { padding: 40px 0 }` (element), and sections carry class `wrap`, so section vertical padding is wiped. Screenshot proof: the "Prices" h2 sits touching the top rule, the price cards touch the next section's rule ("Visit us" heading jammed under it), and the hero `.hero.wrap` overrides horizontal padding so the h1, lede and button sit at x=0 on phone while everything else is at x=16 (desktop: hero at x=200, rest at x=216). Cards: `.price` 8px radius with border, all equal, one system.
U5 PASS  "Bike repair on 4th Street.", "Call 555-0142", plain wording. Minor filler: "Full tune-up for your bike." and "Fixing a flat tire." restate the label; "done by Chen's Cycle Repair" is redundant next to the header name.
U6 FAIL  `<meta name="description" content="... Tune-ups from $65, flat repairs from $15 ...">` ("from" implies a price range the brief never gave) and visible "Full tune-up for your bike." (claims a scope of service nobody supplied). Small, but they are invented claims about the business, not given facts.
U7 PASS  No motion, no decoration.
U8 PASS  Scanner 0 flags. Read against screenshots; the scanner's `default_only: false` is wrong for this page (it uses system-ui only), so it was not trusted alone.

Top fixes (most important first, 5 at most):
1. `<section class="wrap" id="prices">` and `id="visit"` -> `.wrap`'s `padding: 0 16px` overrides `section { padding: 40px 0 }`, so headings crash into rules and cards touch the next rule -> move `.wrap` to an inner div or use `padding-block`/`padding-inline` separately.
2. `<div class="hero wrap">` -> `.hero { padding: 64px 0 48px }` wipes the 16px side padding, so the h1, lede and button hug the screen edge (x=0 on phone) while other content is inset -> same fix as 1.
3. font-family on body -> one system sans for every heading and body -> give headings or prices a second face and weight/size contrast.
4. `.price p` "Full tune-up for your bike." / meta "Tune-ups from $65, flat repairs from $15" -> invented scope and "from" pricing -> use "$65" and "$15" as given, drop the descriptions or mark them placeholders.
5. `.amount` "$65" at 1.75rem -> the price, the thing visitors want, is smaller than the h2 and gray-feeling -> make it the largest element in its card.

Could not check: dark-mode rendering (shoot.cjs only captures light), live keyboard tab order (judged from source).
```

## Which is better

t-a.html is better: its layout is clean, type and look fit a repair shop, and it keeps to the given facts, while t-b.html has a CSS specificity bug that wipes section padding and misaligns the hero, plus a single-face generic look and a small invented "from $" and "Full tune-up" claim.

## Rubric notes

- U1 asks for empty, loading and error states. A static one-screen page has none. The rubric has no N/A rule for this. I counted PASS; a stricter judge could mark it FAIL or "unverified". Add: "N/A when the page has no data, forms or async content".
- U1 is the must-pass check but cannot catch t-b's spacing/alignment bug (nothing clipped, no overflow). That bug landed in U4 only. Consider adding "consistent gutters, nothing touching an edge or a rule" to U1 or U4 wording.
- U3 "two faces" is strict: system-ui plus a fallback stack serif passes only because A names a display stack. A page using one font at strong weight contrast fails with no way to PASS on a deliberate one-font design (the guard "style tell with a stated reason" helps only if a reason is written; neither page wrote one).
- U2 asks for "the contract or the code shows one direction with a reason". Neither file has a written reason; A passes on visible fit. Unclear whether a visible fit without a stated reason counts. I allowed it.
- U6 does not say whether derived facts (A's "Closed Sunday and Monday") or invented service descriptions/"from" pricing (B) count. I passed the first, failed the second. Needs a line.
- U8 can PASS trivially with zero flags and says nothing about the scanner being wrong. Both pages got U8 PASS and it separated nothing.
- U5 did not separate the pages cleanly; B's filler is mild.
- Verdict rule: B fails 4 checks and U6, so Fix first either way. A at 8/8 leaves no way to see where Ship vs near-miss sits.

## Tool notes

shoot.cjs
- Worked, no crash. Output: phone.png (375 wide, full page) and desktop.png (1280, viewport-height crop, not full page; A's footer was just at the edge, B fit).
- Only the light color scheme is captured, so the dark-mode token sets that both pages ship (and the unstyled default-blue phone link in dark) are not seen.
- `smallTapTargets: 1` on both pages in both views; this is the inline `555-0142` text link in the hours list. Real but minor, and identical for both so it does not separate them. It does not report which element.
- `overflowPx: 0` is correct for both. It cannot see the padding/alignment bug in B; only the screenshot shows it.
- Rockwell is absent in the sandbox, so A's display face rendered as a Times-like fallback; screenshots understate its intended look.

scan_ui_defaults.py
- Both files: 0 flags, all counts 0. No false alarms.
- Miss 1: `fonts.named_fonts` is empty for both. A names Rockwell, "Roboto Slab", Georgia; B names Segoe UI, Roboto. Likely it only lists web fonts, not stacks.
- Miss 2: `fonts.default_only` is false for B, which uses only `system-ui, ... sans-serif` for everything. That is the exact "single default sans" case U3 describes, so this flag should be true. It would have been wrong to use it as evidence.
- No check for CSS specificity or padding collisions, unequal gutters, or invented numbers/claims (U4/U6 stay manual).
- `buzzwords` and `em_dashes` returned 0, which matches the source.
