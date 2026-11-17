## t-a.md

```
Verdict: Fix first      Score: 1/7 checks pass (M8 N/A)
Category: media   Rubric: /home/user/anti-slop/skills/human-media/references/rubric.md

Checks:
M1 FAIL  "Ms. Okafor, the librarian, smiles warmly and holds an open picture book toward the viewer" (a real person is depicted with a described face and expression; no consent is mentioned and no AI-label note is given)
M2 FAIL  "Soft, natural colors ... Slightly textured paper feel, plain and uncluttered." (no medium or format is named: not photo, illustration or print)
M3 PASS  "Late-afternoon golden light pours through tall library windows" ; "cream, honey yellow, sage green, and a touch of terracotta" (one light source, 4 named colors)
M4 FAIL  "In the foreground, Ms. Okafor ... holds an open picture book toward the viewer" (one foreground subject facing the viewer; no off-center placement stated; only the text zones are planned)
M5 FAIL  "cushioned chairs, stacked books, and a few potted plants" (generic props; no named imperfection)
M6 FAIL  "Text to include on the poster: Eastfield Library / Summer Reading Night / Friday, 14 August, 6 pm" ; "smiles warmly ... relaxed, kind expression" (text is left in the generation; a smiling face and children's faces are not hidden, cropped or flagged for checking)
M7 FAIL  "Keep the text large, simple, and easy to read from a distance." (no hand pass is named; the generated image and text are the final output)
M8 N/A   single piece

Top fixes (most important first, 5 at most):
1. Ms. Okafor line "Ms. Okafor, the librarian, smiles warmly and holds an open picture book" -> a real person's likeness is used with no consent -> ask for her consent or use a supplied photo, or render her as an unnamed figure at a distance or in silhouette; add a note on any AI-use label.
2. "Text to include on the poster" -> generated text is likely to be misspelled -> take the text out of the prompt and add it by hand in a real font.
3. "Soft, natural colors ... Slightly textured paper feel" -> no medium -> name one, for example a risograph or gouache print.
4. "smiles warmly ... Children and a parent sit on the rug nearby, looking up" -> faces up close are unchecked -> keep faces small or turned away and say to check them.
5. Whole prompt -> no named flaw and no finishing step -> add one imperfection (for example misregistration or grain) and a hand pass (crop, type, size check).

Could not check: the generated image itself (no image exists to see); how the prompt performs in any specific generator.
```

## t-b.md

```
Verdict: Ship      Score: 7/7 checks pass (M8 N/A)
Category: media   Rubric: /home/user/anti-slop/skills/human-media/references/rubric.md

Checks:
M1 PASS  "I have not drawn her likeness. A real person's face needs her consent. If she agrees, use a photo she supplies" ; "If the poster goes on a platform that asks for an AI-use label, add one." (consent raised, no likeness, label mentioned)
M2 PASS  "Risograph print, two inks (burnt orange and deep green) on warm cream paper"
M3 PASS  "Low evening sun comes through tall library windows from the left" ; burnt orange, deep green, cream, mustard (one light source, 4 named colors)
M4 PASS  "A librarian sits ... in the lower right third" ; "The upper left is empty for the title." (off-center, with a purpose for the empty space)
M5 PASS  "Visible riso misregistration on the orange layer, slight grain" ; "Paper lanterns hang in a loose line across the top edge" ; "low wooden stool"
M6 PASS  "No text in the image." ; "Her face is seen at a distance and is not detailed." ; "No hands visible" ; "Look at the faces, the stool and the lanterns before you use it."
M7 PASS  "Type to add by hand (real font ...)" ; "generate four, pick one, crop tighter, add the type, then shrink it to about 200 px to check it reads."
M8 N/A   single piece

Top fixes (most important first, 5 at most):
1. Notes, first bullet "I have not drawn her likeness" -> the user asked for Ms. Okafor to be in it and the prompt shows only an unnamed librarian; a reader may want a clearer next step -> keep it, and add one line on how to get her consent and a photo before the poster is printed.

Could not check: the generated image itself (none exists); the real font choice and printed result.
```

File t-b.md is better: it is the only one that handles the real-person consent issue (M1, must-pass) and it passes all the other checks that t-a.md fails.

## Rubric notes

- M1 combines three things (consent, passing off as handmade, label mention). A file can pass the consent part and say nothing on labels, or the reverse. Worth splitting or stating which part decides.
- M1 does not say what counts as "using" a real person's face. t-a.md names her and gives her a smile and a pose in a generated image; t-b.md avoids it. The rubric reads that fine, but "a described likeness" versus "a photo of her" is not spelled out.
- M4 "off-center" is unclear when the brief needs space for text. t-a.md reserves top and bottom areas but centers the subject; whether that is a FAIL is a judgement call.
- M6 asks for hands "hidden, cropped or checked" but t-a.md has the librarian holding a book (hands will show) and never mentions hands. Whether silence counts as FAIL is not stated.
- M5: "textured paper feel" in t-a.md is a texture, not a named imperfection. The rubric does not say whether a texture counts.
- M8 is N/A for both (single piece); the check cannot separate these files.
- M2 to M7 are all passed or failed together here, so the rubric separates the two files mainly through M1 and the cluster of prompt-craft checks. No check measures whether the reply still does what the user asked (put Ms. Okafor in the poster); t-b.md's silhouette workaround is not scored.
