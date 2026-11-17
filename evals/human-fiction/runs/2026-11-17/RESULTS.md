# human-fiction eval, 2026-11-17

One run per arm, 1 task (Lagos bus depot, 400 words), judge model in a fresh context. The judge did not know which file used the skill.

Key: t-a used the skill. t-b did not.

| Task | Without skill | With skill | Judge preferred |
|---|---|---|---|
| 1 Lagos depot scene | 8/8, Ship | 7/8, Fix first | With skill (as prose) |

## What it showed

- The skill scene was the better prose: the pen, the tyres and "Then he is consistent." carry the feeling. The no-skill scene explained more of what it showed ("she could see him knowing it").
- The skill scene failed F1 because Tunde's age (52) never appears, and it ran short at 367 words. The skill did not say to keep every supplied detail or the asked length.
- The no-skill scene kept all facts but ran 450 words (12% over), and ended on stasis ("neither of them moved").
- F5, F6 and F7 passed both files. The rubric could not tell narration that restates a shown feeling from narration that adds, or an open ending with an object from one that ends on mood. F1 had no rule for shown versus stated details or for length.

## Changes made after this run

- Rubric: F1 now lists the facts that must appear (counts, ages, times, places, roles, what is owed), accepts a detail shown instead of stated if the number is clear, and fails length outside 10%. F2 covers sky or light with a mood. F5, F6 and F7 were sharpened. An edge-case section was added.
- SKILL.md: one Never item (do not drop a brief detail; show it concretely if not stated) and one Default (stay within 10% of the asked length). Nothing else changed.
- With the new rubric both files would be Fix first (A fails F1 on age, B on length). A would score 7/8 and B about 5/8 (F1, F5, F7 fail), so the score separates them in the editor's order.

## Limits

One run per arm and one task is too few to be sure of anything. The same model family wrote and judged the rubric changes. Rerun with 3 tasks and 3 runs per arm, and a different judge, before trusting the difference.

## Rerun after the changes (same day)

The scene was written again with the changed skill (file t-c) and scored by a new blind judge against the same no-skill scene (t-b), using the changed rubric. Report: `JUDGE-rerun.md`.

| Without skill | With changed skill | Judge preferred |
|---|---|---|
| 4/8, Fix first | 8/8, Ship | With skill |

Both the skill and the rubric changed between rounds, so part of this gap comes from the stricter rubric. The no-skill scene now fails on length (449 words), a moody-sky opening, narration that restates a shown feeling, and an ending on stillness. One run per arm.
