# Judge report: human-fiction, run 2026-11-17

Brief given: 400-word scene, Lagos bus depot, 5 a.m. Tunde (dispatcher, 52, owes a driver 3 weeks' pay), Bisi (driver, knows). 11 buses, 2 broken. End without a settled outcome.
Script run: count_story_tells.py on both files (A 367 words, B 450 words; no stock names, phrases, body-sensation hits or lesson patterns in either).

## t-a.md

```
Verdict: Fix first      Score: 7/8 checks pass
Category: fiction   Rubric: /home/user/anti-slop/skills/human-fiction/references/rubric.md

Checks:
F1 FAIL  Tunde's age (52) is never stated or shown; "Tunde" appears with no age anywhere. Kept: "Eleven buses in two rows", "two at the far end with their bonnets up", "Three weeks", "You are the company at five in the morning, Tunde." Length 367 words vs 400 asked.
F2 PASS  "The gate was already half up when Bisi arrived... Generator noise. Diesel on the concrete."
F3 PASS  Bisi wants pay before "the twentieth"; Tunde offers "Sell the tyres off nine" and cannot meet her eye. Cost lands on her.
F4 PASS  "Ayo said Thursday last Thursday." / "Then he is consistent." Lines dodge and answer sideways; Tunde and Bisi sound different.
F5 PASS  "She could see him reaching for the old voice... It did not arrive." "She looked at the pen for a long time." Feeling carried by objects.
F6 PASS  Conductor enters, danfo horn, escalation from broken buses to the pay to "Sell the tyres off nine".
F7 PASS  "She looked at the pen for a long time." Outcome open; she has not signed or refused.
F8 PASS  Script: no stock names, no stock phrases, 0 body-sensation hits.

Top fixes (most important first, 5 at most):
1. Line 3 area, Tunde's introduction "Seven and nine," Tunde said -> his age of 52 is missing, so a brief fact is dropped -> add one concrete detail that carries it (for example "fifty-two years old and still writing in pencil") and add about 30 words to reach 400.

Could not check: whether the Lagos setting is accurate to local depot practice (danfo, Ibadan run are plausible, not verified).
```

## t-b.md

```
Verdict: Ship      Score: 8/8 checks pass
Category: fiction   Rubric: /home/user/anti-slop/skills/human-fiction/references/rubric.md

Checks:
F1 PASS  "He was fifty-two", "Eleven buses in the yard", "Number seven has the gearbox. Number four, the radiator again", "Three weeks." Time of 5 a.m. is implied ("yard lights were still on", owner due "at six"), not stated. Invented Madam Ngozi and the fuel man are story details, not presented as real facts. Length 450 words, 12% over.
F2 PASS  "The yard lights were still on when Bisi pulled her bus through the gate" (names Oshodi). The clause "the sky... had not yet decided what colour it wanted to be" is a weather-style opener but sits after a concrete scene.
F3 PASS  Bisi wants pay; Tunde wants to protect the owner's sheet and his own standing; "The Ikeja route is making money" shows the fuel man was paid first.
F4 PASS  "The mechanic says Friday every Friday." / "What list has me at the top, Tunde?" Dodging is real. Speakers are fairly alike in register.
F5 PASS  Borderline: "she could see him knowing it, the way his shoulders went up and stayed there" and "which was not the sound of anything being fixed" explain what the detail already shows. Script: 0 body-sensation hits.
F6 PASS  Owner arrival at six sets a deadline; commuters outside gives a second thread.
F7 PASS  "neither of them moved toward the door." Unresolved, though it ends on stasis rather than a consequence.
F8 PASS  Script: no stock names, no stock phrases, 0 body-sensation hits.

Top fixes (most important first, 5 at most):
1. Paragraph 11 "She did not need to say the number, and she could see him knowing it" -> narration restates what the dialogue already shows -> cut the explanation and keep the shoulders.
2. "She thought of her daughter's school fees... did not say it." -> told interior, and the fee detail is only gestured at -> give it a spoken line or cut.
3. Opening sentence, "the sky over Oshodi had not yet decided what colour it wanted to be" -> soft weather personification -> open on the yard lights and the bus.
4. Whole piece -> 450 words against a 400 target -> trim about 50.

Could not check: whether the Lagos setting is accurate to local depot practice.
```

## Which is better

t-a.md is the better scene: its detail does the work (the pen, the tyres, "Then he is consistent."), where t-b.md explains more of what it shows. By the rubric t-a.md is "Fix first" only because it never states Tunde's age.

## Rubric notes

- F1 is a must-pass, so one dropped character detail (age 52) flips t-a.md to "Fix first" and t-b.md to "Ship", the reverse of the craft order. The rubric does not say whether a character attribute counts as a "fact" the same as a count or number. Needs a rule, or a lighter fail tier for a dropped minor fact.
- F1 has no word-count rule. t-a.md is 8% under and t-b.md 12% over; the check cannot say whether either is a fail. Needs a tolerance (for example plus or minus 10%).
- F1 does not say whether an implied time (5 a.m. shown by light and a 6 o'clock deadline) counts as keeping the fact. I treated implied as kept.
- F2 lists "weather" as a fail but not dawn sky or light described as a personification. t-b.md's opening is borderline; I passed it.
- F5 "explained again" and "body sensation" are loose. The script count was 0 for both, so it could not separate the two files; the difference between them (narration restating shown feeling) rests on judgement.
- F6 and F7 passed both files with no separation. F7 does not distinguish an open ending that leaves a concrete object (t-a.md's pen on the sheet) from one that ends on stasis (t-b.md's "neither of them moved").
- Overall: seven of eight checks passed for both; the rubric could not separate the files except through F1.
