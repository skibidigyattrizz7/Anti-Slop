# Judge rerun, human-writing, 2026-11-17

Briefs were supplied for both pieces, so W3 is applied in full. Script run on every file (count_tells.py); counts used as evidence.

## p1-a.md (Brief 1, QuizPaste homepage intro)

```
Verdict: Fix first      Score: 5/8 checks pass
Category: writing   Rubric: /home/user/anti-slop/skills/human-writing/references/rubric.md

Checks:
W1 PASS  "Paste your class notes into QuizPaste and get 20 quiz questions in about a minute. It is free for students."
W2 PASS  "20 quiz questions", "about a minute", "two-person team", "export it to PDF", "last week's notes" (the 40+ word paragraphs each hold one)
W3 FAIL  "built by a two-person team who wanted a faster way to test what they had just learned" (motive not in the brief); "a lecture, a chapter summary or a page of messy notes" (input types not supplied); "Print it for a study group" (use not supplied)
W4 FAIL  "check your memory before the exam instead of after it" (a contrast nobody claimed)
W5 FAIL  "a lecture, a chapter summary or a page of messy notes" and "Print it for a study group, save it for later, or work through it on paper" (two triads in 114 words). Script variation 0.53, fine.
W6 PASS  script: 0 cluster words, 0 stock phrases
W7 PASS  "Try it with last week's notes and see how much you still remember."
W8 PASS  three plain paragraphs, no formatting

Top fixes (most important first, 5 at most):
1. Paragraph 2 "who wanted a faster way to test what they had just learned" -> invented motive -> delete; say only "made by a two-person team".
2. Paragraph 2 "a lecture, a chapter summary or a page of messy notes" -> input types the brief never gave -> say "class notes".
3. Paragraph 3 "Print it for a study group" -> invented use -> say "export it to PDF" only.
4. Paragraph 2 "before the exam instead of after it" -> unclaimed contrast -> cut the clause.
5. Paragraphs 2 and 3 -> two three-item lists -> turn each into a single plain item.

Could not check: whether the facts match the real product beyond the brief; word count target (about 120) is not a rubric check, text is 114 words.
```

## p1-c.md (Brief 1, QuizPaste homepage intro)

```
Verdict: Ship      Score: 8/8 checks pass
Category: writing   Rubric: /home/user/anti-slop/skills/human-writing/references/rubric.md

Checks:
W1 PASS  "Paste your class notes into QuizPaste and get 20 quiz questions in about a minute."
W2 PASS  "20 quiz questions", "about a minute", "Two people built it", "PDF", "the week before the test" (no paragraph reaches 40 words; piece is above one per 100 words)
W3 PASS  every supplied fact is present and unchanged: 20 questions, about a minute, free for students, two people, PDF. "The questions come from what you wrote" follows from "paste class notes".
W4 PASS  no unclaimed contrasts or vague attribution
W5 PASS  script variation 0.49; no triads
W6 PASS  script: 0 cluster words, 0 stock phrases
W7 PASS  "Try it after your next lecture, while the notes are still fresh. Then run it again the week before the test."
W8 PASS  three short paragraphs, no formatting

Top fixes (most important first, 5 at most):
1. Last sentence "every quiz checks you on your own material" -> restates the value, adds nothing -> optional cut.
2. Whole piece -> 81 words against a brief of about 120 -> only a length note, no rubric check covers it; add only facts the brief supplies.

Could not check: whether the facts match the real product beyond the brief.
```

## p3-a.md (Brief 3, robotics club blog post)

```
Verdict: Fix first      Score: 4/8 checks pass
Category: writing   Rubric: /home/user/anti-slop/skills/human-writing/references/rubric.md

Checks:
W1 FAIL  "Going into the competition, we thought the robot was ready. It wasn't." (sets a scene; first fact comes in sentence 3)
W2 PASS  "every third try", "11 p.m.", "one bent screw", "4th out of 22 teams", "spare fasteners in the pit kit"
W3 FAIL  "we ran the course again until we felt confident in it"; "We didn't get much sleep"; "no amount of adjusting made the problem go away"; "Searching methodically found the problem faster than guessing ever did"; "we check the hardware before we check the code" (events not in the brief, stated as having happened)
W4 FAIL  "test the full run the day before, not just a quick check" (nobody claimed a quick check was enough); "we know how close it came to going differently" (vague)
W5 FAIL  script variation 0.29 on 185 words; three similar-length sentences in a row: "Once it was fixed, the grip held steady, and we ran the course again until we felt confident in it." / "We didn't get much sleep, but the night taught us three things." / "First, test the full run the day before, not just a quick check."
W6 PASS  script: 0 cluster words, 0 stock phrases
W7 PASS  "Next season, we start testing earlier, and we check the hardware before we check the code."
W8 PASS  one title, plain paragraphs

Top fixes (most important first, 5 at most):
1. Paragraph 2 "we ran the course again until we felt confident in it" -> invented event -> delete.
2. Paragraph 1 "no amount of adjusting made the problem go away" and paragraph 3 "We didn't get much sleep" / "Searching methodically found the problem faster" -> invented -> delete or restate as a view.
3. Paragraph 1 "we thought the robot was ready. It wasn't." -> scene-setting opener -> start with "The night before, the arm dropped the cube every third try."
4. Paragraph 3 "not just a quick check" and paragraph 4 "how close it came to going differently" -> unclaimed contrast, vague -> cut.
5. Whole piece -> even sentence length -> mix short and long sentences.

Could not check: whether the team did anything beyond the three supplied facts.
```

## p3-c.md (Brief 3, robotics club blog post)

```
Verdict: Fix first      Score: 6/8 checks pass
Category: writing   Rubric: /home/user/anti-slop/skills/human-writing/references/rubric.md

Checks:
W1 PASS  "The night before the competition, the robot arm dropped the cube every third try."
W2 FAIL  "Three lessons stand out. First, check the hardware before the final night, not during it. Second, when a robot fails in the same way each time, take the mechanism apart before you change the code. Third, take the robot apart early, while there is still time to fix what you find." (55 words; the only number is the list count)
W3 FAIL  "The night before a competition is a bad time to learn that it was loose." (the supplied screw was bent, not loose); "A bolt takes a minute to check" (screw became a bolt); "Our checklist for next time starts with the claw" (a checklist is not in the brief and is stated as fact); "The cause was a single bent screw" (brief says only that it was found)
W4 PASS  "before the final night, not during it" compares two real options; no vague attribution
W5 PASS  script variation 0.41; one triad ("every screw, every fastener and every moving joint")
W6 PASS  script: 0 cluster words, 0 stock phrases
W7 PASS  "Our checklist for next time starts with the claw: every screw, every fastener and every moving joint."
W8 PASS  one title, plain paragraphs

Top fixes (most important first, 5 at most):
1. Last paragraph "learn that it was loose" -> changes bent to loose -> say "learn that a screw was bent".
2. Last paragraph "A bolt takes a minute to check" -> screw changed to bolt, minute invented -> "a screw is quick to check".
3. Last paragraph "Our checklist for next time starts with the claw" -> invented artifact stated as fact -> "next time we should check the claw first".
4. Paragraph 2 "The cause was a single bent screw" -> cause is an inference -> "we found one bent screw".
5. Lessons paragraph -> no specific named -> tie each lesson to the cube drop or the claw.

Could not check: whether the team did anything beyond the three supplied facts.
```

## Pair verdicts

- Brief 1: p1-c is better; p1-a invents a team motive and uses cases (study group, chapter summary) that the brief never gave, p1-c does not.
- Brief 3: p3-c is better; p3-a invents several events (ran the course again, little sleep, no amount of adjusting) while p3-c has one meaning slip (bent became loose) and an invented checklist. Both are "Fix first".

## Rubric notes

- W3 does not say whether a plan or a cause is a view or an event. "The cause was a single bent screw" and "Our checklist starts with the claw" sit on the line; I treated an invented artifact and a changed word (bent to loose) as FAIL, and the cause claim as minor.
- W2 per-paragraph rule: unclear whether a list count ("Three lessons") is a checkable number. I said no. This makes the lessons paragraph the usual W2 failure, and it separated p3-a (has "pit kit") from p3-c by a thin margin. Consider requiring a named thing or example.
- W5 "habitual triad" is not defined and the script does not count triads. p1-a has two in 114 words; the "more than one per 300 words" rule scales badly on short pieces. Real-count lists ("First, second, third") are not clearly exempt.
- W4 "a not-X half that nobody claimed" is judgement. "instead of after it" (p1-a) and "not just a quick check" (p3-a) are borderline; the script flagged only one tail in p3-a and p3-c, and p3-c's was a real contrast. A real-versus-unclaimed test needs an example.
- W1 "sets a scene" vs "delivers content": p3-a's "we thought the robot was ready. It wasn't." is both a scene and a claim. I failed it, but another judge could pass it.
- No check covers length against the brief (p1-c is 81 words for "about 120"), so a short but clean piece scores 8/8.
- W7 passes p3-c on the next-step sentence, although the final two lines restate lesson 1. Paragraph-level reading is too loose to separate them.
- Verdict rule gave both p3 files "Fix first", so only the score separates them. W3 as a gate works, but it hides the size of the gap between one slip and several invented events.
