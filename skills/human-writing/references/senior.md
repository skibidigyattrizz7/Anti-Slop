# Senior layer: writing

Use for a big job, a senior review, or when the user asks for senior-level work. It adds to SKILL.md. Tags: `[verified: URL]` means the page was opened; `[practice]` means common professional practice with no opened source, so never quote it as a finding.

## Pass order: structure before lines

- **Edit in this order: purpose and reader, shape, sentences, correctness.** Each pass can make the next one wasted work. Check: no comma fixes in a section the structure pass cut. [practice]
- **Name the reader and their next action first.** It gives every later cut a test. Check: "CFO, approves $40k by Friday" is written down before drafting. [practice]
- **Cut ideas before words.** Deleting a paragraph beats trimming ten sentences. Check: for an over-long draft, whole paragraphs went first. [practice]

## Point and argument

- **Write the point as a claim, not a topic.** A claim can be wrong, so the reader can test it. Check: "About onboarding" fails; "New hires ship faster when the first ticket is pre-scoped" passes. [practice]
- **Reverse outline.** Write one line per paragraph saying what it does, then read the lines in order. Split a paragraph that does two jobs, merge two that do one, move jobs out of order, cut any that serve no claim. Check: the lines read as an argument, not five parallel paragraphs. [verified: https://www.ou.edu/content/dam/writingcenter/docs/writing-guides/reverse_outline_handout.pdf]
- **Answer the strongest objection.** If it is missing, the reader supplies it and trusts you less. Check: the best counterargument appears in its strongest form, with a reply. [practice]
- **One unit, one point.** Sentence, paragraph and section each serve one function. Check: you can name each paragraph's single job. [verified: https://wstomv.win.tue.nl/quotes/science-of-scientific-writing.html]

## Line craft (Gopen and Swan)

- **Stress position: put the news last.** Readers give the end of a sentence the most weight. Check: say which word the reader should keep; it lands last. "We hired two people because sales rose 12 percent" fits when the number is the news. [verified: https://wstomv.win.tue.nl/quotes/science-of-scientific-writing.html]
- **Topic position: old before new.** Open on what the reader already has and the person or thing the sentence is about. Check: each sentence starts with something the last one gave. [verified: same page]
- **Keep subject and verb close.** Anything long between them reads as an aside. Check: move the aside after the verb. [verified: same page]
- **Put the action in the verb.** "We made a determination of the cause" becomes "We found the cause." Check: few "the X-ing of" or "make a decision" forms per page. [verified: same page]
- **Use these as tests, not laws.** A flat run of one length is the cue to look, not a rule to apply by machine. Check: vary on purpose, and keep a long sentence that carries a qualification. [practice]

## Genre forms

- **Docs: pick one Diataxis form per page.** Tutorial (learn by doing), how-to (do a task), reference (describe), explanation (understand). Mixing is the common failure. Check: the page is exactly one, and links out for the rest. [verified: https://diataxis.fr/]
- **How-to: the title says what it shows, no teaching inside.** Check: "How to configure reconnection back-off", not "Back-off". [verified: https://diataxis.fr/how-to-guides/]
- **Email: bottom line up front.** The first line is the ask or decision plus the deadline; then only what the reader needs to act. Check: "Please approve the $40k renewal by Friday" opens it. [verified: https://mitcommlab.mit.edu/aeroastro/2025/03/17/how-to-write-effective-emails/]
- **Instructions: condition before the step.** Check: "If the build fails, rerun the tests", not the reverse. [verified: https://developers.google.com/style/highlights]
- **README: what it is, who it is for, how to install, one working example, in the first screen.** Check: all four are visible without scrolling. [practice]

## Editing someone else's text

- **Restate what the piece is trying to do before marking anything.** If you cannot, that is the first finding. Check: one sentence of intent precedes the edits. [practice]
- **Keep their voice.** Keep dialect words, sentence habits and rough lines that sound like them; fix only what blocks the reader. Check: a reader who knows the writer would still hear them. [practice]
- **Query, do not rewrite, when meaning is unclear.** Check: "Do you mean A or B?" appears where you guessed nothing. [practice]
- **Give at most three ranked priorities, each with a place and a fix, and one true strength.** Describe the reader's experience ("I lost the thread here"). Check: three or fewer, each located. [practice]

## Build on

- **`humanizer` (MIT):** the tell patterns are already adapted in this skill's references. If the skill is present, run it for a de-slop pass; if not, use `references/tells.md`.
- **`doc-coauthoring`:** for long shared docs, use its context, refine-by-section and reader-test stages. If missing: do the structure pass above, then test the draft on a reader who has not seen the brief.
- **`own-voice`:** when the text must sound like the user, use it. If missing: edit lightly and keep their rough lines.
- **`ux-copy` (design plugin):** for UI text, error = what happened, why, how to fix; button = verb plus object. If missing, use those two lines.

## Credits

No text here is copied from an MIT or Apache-2.0 skill. The Gopen and Swan wording is cited from the page above, and the Diataxis, Google and MIT Communication Lab pages are linked, not copied. `doc-coauthoring`, `own-voice` and `ux-copy` carry no licence that was found, so they are linked or paraphrased only.
