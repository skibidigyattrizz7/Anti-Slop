## t-a.md

```
Verdict: Fix first      Score: 5/7 checks pass
Category: chat   Rubric: /home/user/anti-slop/skills/human-chat/references/rubric.md

Checks:
H1 PASS  "5x = 3x + 16 ... 2x = 16 / x = 8" (steps correct; 5(8)-7 = 33 = 3(8)+9; "9 - 7 = 2" does give x = 1; slip is marked "probably")
H2 FAIL  "You're close. The mistake is in one sign."
H3 PASS  "If you got x = 1, you probably did 9 - 7 = 2 instead of 9 + 7 = 16."
H4 PASS  short, plain steps, right level for 8th grade
H5 FAIL  "you have to add 7 to both sides, not subtract it" (rule comes before the example; no reason why adding 7 works)
H6 N/A   explanation, not feedback
H7 PASS  plain prose and equation lines, no emoji or bold
H8 PASS  "Watch the sign every time you move a number across the equals sign." (one short tip, no offer, no question)

Top fixes (most important first, 5 at most):
1. line 1 "You're close. The mistake is in one sign." -> opens with encouragement and a flat claim about an unseen slip, answer x = 8 not first -> open with "x = 8" and say the slip is probably a sign.
2. line 3 "you have to add 7 to both sides, not subtract it" -> rule with no reason -> say why: adding 7 undoes the -7, so the left side keeps only 5x.

Could not check: which slip the user actually made (steps not shown)
```

## t-b.md

```
Verdict: Ship      Score: 7/7 checks pass
Category: chat   Rubric: /home/user/anti-slop/skills/human-chat/references/rubric.md

Checks:
H1 PASS  "2x - 7 = 9 ... 2x = 16 ... x = 8" (correct; "2x = 9 - 7 = 2" does give x = 1; slip marked "likely"/"probably")
H2 PASS  "The answer is x = 8."
H3 PASS  "That subtracts 7 when you need to add it."
H4 PASS  86 words, plain, right level for 8th grade
H5 PASS  "adding 7 undoes subtracting 7: 2x = 16" (real numbers, reason shown, common mistake named)
H6 N/A   explanation, not feedback
H7 PASS  plain prose, no list, emoji or bold
H8 PASS  "Check: 5(8) - 7 = 33 and 3(8) + 9 = 33. Both sides match." (stops with the content)

Top fixes (most important first, 5 at most):
1. line 1 "Your method is right" -> says the method is right without seeing it, while the answer was wrong -> drop it or say "your setup looks right".

Could not check: which slip the user actually made (steps not shown)
```

t-b.md is better: it opens with the answer (H2) and gives the reason for adding 7 (H5), and t-a.md fails both.

## Rubric notes

- Fidelity: the user showed no steps. Both files guess the slip, and both mark it "probably". t-a.md's "The mistake is in one sign" and t-b.md's "Your method is right" are flat claims about work nobody saw. H1 says "true or marked uncertain" but gives no rule for a claim about unseen work. I passed both and noted it; a stricter judge could fail either.
- H5 says "explanations only", but this reply is half diagnosis. I applied it because it explains a method. The rubric does not say how to treat a mixed reply.
- H5 "worked example before the rule": here the user's own equation is the example, so any reply that works the equation passes the example half. Only "reason shown" separated the files.
- H2 and H3 overlap on "You're close". I failed H2 only, because the line is mild praise, not a sandwich.
- H8 cannot tell a closing tip ("Watch the sign every time...") from a recap. I passed it as one short, needed tip.
- The tells script flagged nothing in either file, so it could not separate them.
