# Senior craft for prose, explanation and fiction (notes for human-writing, human-chat, human-fiction)

Source key. **[opened]** = fetched this session. **[classic]** = well-known book, cited from memory, not re-opened. **[unverified]** = could not open; treat as lead only. All before/after examples are my own illustrations unless a source is named.

Not opened: Chicago Manual of Style (login wall), GOV.UK writing rules (sub-pages 404/redirect; only the landing page loaded), Write the Docs / Stripe, Le Guin's *Steering the Craft*, Williams' *Style*, Zinsser, Gardner's book itself, the Gopen and Swan paper's example sentences (only the guideline wording loaded).

## 1. Structural editing before line editing

### Takeaway
Editors fix the whole before the parts: purpose and reader, then shape, then sentences, then correctness. Line edits on a draft with the wrong shape are wasted.

### Cited findings
- **Order of passes: developmental (big picture) > line/stylistic > copyedit (grammar, consistency, house style) > proof (final-proof errors).** Why: each pass invalidates the next; polishing a paragraph you will cut is waste. Example: don't fix commas in section 3 when the brief says section 3 should go. Source: standard editorial practice [classic; Chicago's "levels of editing" page not opened, unverified].
- **Diagnose with three questions before touching text: Who is the reader? What should they know or do afterward? What is the single claim or ask?** Why: all later cuts need a criterion. Example: "This memo's reader is the CFO; she must approve $40k by Friday." Anything not serving that is a cut candidate. Source: classic editorial practice (also Williams, *Style*, "know your point") [classic].
- **One-sentence point test (already in human-writing).** Senior addition: write it as a claim, not a topic. "About onboarding" fails; "New hires ship faster when the first ticket is pre-scoped" passes. [classic]
- **Reverse outline.** After drafting, write one line per paragraph saying what it does ("introduces objection", "gives data"). Read the lines in order: do they make an argument? Look for paragraphs that do two jobs (split), two that do the same job (merge), jobs out of order (move), and jobs that serve no claim (cut). Why: the outline you planned is not the outline you wrote. Source: widely taught in university writing centers [classic; no single primary page opened].
- **Argument-shape check.** Claim, reason, evidence, the strongest objection, response. If the strongest objection is missing, the reader supplies it and stops trusting you. [classic, rhetoric/Toulmin tradition]
- **One unit, one point.** "Every unit of discourse, no matter the size, should serve a single function or make a single point." Applies to sentence, paragraph, section. — Gopen and Swan guideline wording, [mirror of paper](https://wstomv.win.tue.nl/quotes/science-of-scientific-writing.html) [opened; American Scientist 78(6), 1990].
- **Context before new:** "provide context for your reader before asking that reader to consider anything new." Same source [opened]. Structural use: a section's first sentence restates the question it answers.
- **Cut at the level of ideas first.** Delete whole paragraphs and sections before shortening sentences; 10 percent from line edits rarely fixes a 30 percent-too-long draft. [classic, Zinsser *On Writing Well*, "clutter" chapter]

### Inferences
- A model drafting for the user should run a structure pass silently (purpose, reader, point, reverse outline) before any line pass, and report only what changed.
- Reverse outlining is cheap for an LLM and catches the "five parallel paragraphs, no argument" AI shape.

### Gaps
- Chicago Manual's exact definitions of editing levels could not be fetched. The four-level order above is common practice, not quoted.

## 2. Line-level craft

### Takeaway
Readers expect certain information in certain sentence positions. Put old/known material first, the new or important thing last, keep subject and verb close, and let the verb carry the action.

### Cited findings
- **Subject-verb proximity.** "Follow a grammatical subject as soon as possible with its verb." Before: "The smallest of the polyps, which are fed by the plankton that drift past, **is** ..." (own example). After: put the subject and verb together, move the aside after. — [Gopen and Swan](https://wstomv.win.tue.nl/quotes/science-of-scientific-writing.html) [opened, rule text only].
- **Stress position (end focus).** "Place in the stress position the 'new information' you want the reader to emphasize." Before: "Sales rose 12 percent, which is why we hired two people." After: "We hired two people because sales rose 12 percent" if the number is the news; keep the original if the hiring is. Test: say which word the reader should remember, then check it lands last. Same source [opened].
- **Topic position: old before new.** Open with what the previous sentence ended on; end with what is new. "Place the person or thing whose 'story' a sentence is telling at the beginning." Before: "A review found an error. Fixing the error took three days." Good as is, the error repeats at the head. Before (broken): "Three days went to the fix. A review had found an error." After the swap, the link is restored. Same source [opened].
- **Action in the verb.** "Articulate the action of every clause or sentence in its verb." Before: "We made a determination of the cause." After: "We found the cause." Same source [opened]; same idea as Williams' nominalization advice [classic].
- **Caution on mechanical use.** A Duke handout (per search summary, PDF not opened) warns against "Gopenizing": check that the stress position holds what truly needs emphasis. [unverified]
- **Characters as subjects, actions as verbs (Williams).** Before: "The reduction of errors was achieved by our implementation of checks." After: "We cut errors by adding checks." Joseph Williams, *Style: Lessons in Clarity and Grace* [classic].
- **Length variety on purpose.** After a run of 20-word sentences, a 4-word one lands. Long sentences carry qualifications; short ones carry the verdict. Test: count words per sentence for one paragraph; a flat 17-22 range is the tell. [classic craft; Gary Provost's rhythm demo, not opened]
- **Paragraph shape.** First sentence states the paragraph's point; the rest supports it; last sentence hands off. Uneven lengths. Split when the point changes, not at a length. [classic]
- **Transitions are logical, not decorative.** "However" must mark a real reversal; "therefore" a real consequence. Often a repeated key term does the linking better than "Moreover". [classic; Gopen and Swan old-before-new is the mechanism]
- **Cutting: delete the throat-clearing and the restated ending first.** Before: "It is important to note that the results, in many cases, tend to suggest..." After: "The results suggest..." Zinsser: "clutter is the disease of American writing" [classic].
- **Google developer style, line rules** [opened, highlights page only]: active voice ("The script creates the file", not "The file is created"); put the condition before the instruction ("If the build fails, rerun the tests"); second person "you"; numbered lists for sequences, bulleted lists otherwise; conversational but not frivolous. Source: [Google developer documentation style guide](https://developers.google.com/style/highlights).

### Inferences
- "End focus" is the highest-value, least-known rule for fixing the flat AI cadence: AI sentences often end on a vague abstraction ("...in meaningful ways"). Moving the news to the end fixes both rhythm and content.

### Gaps
- Did not see Gopen and Swan's original example sentences, so examples above are mine. GOV.UK sentence-length figures (commonly quoted as about 25 words) not verified.

## 3. Genre craft

### Takeaway
Each genre has a reader with a job. Name the job, put its answer first, and organize by what the reader will do.

### Cited findings
- **Diataxis: four forms, four needs.** Tutorial (learning by doing), how-to guide (goal-directed action), reference (description of the machinery), explanation (understanding). Mixing them is the commonest docs failure. [Diataxis](https://diataxis.fr/) [opened, landing page lists the forms].
- **Tutorial rules** [opened](https://diataxis.fr/tutorials/): "always learning-oriented"; show the destination early; "visible results early and often"; narrate what the learner should see and warn of likely mistakes; "minimise explanation" and link out; stay on one path, ignore options; make it work every time. Before: a tutorial step that pauses to explain three config options. After: "Run `npm start`. You should see 'Listening on 3000'." and a link to the config explanation.
- **How-to rules** [opened](https://diataxis.fr/how-to-guides/): goal-oriented; title says exactly what it shows ("How to configure reconnection back-off", not "Back-off"); "no digression, explanation, teaching"; assumes a competent user; allows forks and judgment ("If you want x, do y"); order for the user's flow.
- **Explanation rules** [opened](https://diataxis.fr/explanation/): "discursive treatment ... that permits reflection"; covers why, history, constraints, alternatives, and opinion; tightly bounded; no instructions creeping in. Titles like "About ...".
- **Reference:** described as a "close-up view of the machinery" scoped to the thing itself; detailed principles not opened [opened, thin]. Common practice: consistent structure, complete, neutral, no narrative [classic].
- **README test:** within the first screen, answer what it is, who it is for, how to install, one working example. Then the tutorial/how-to links. [classic practice; Write the Docs unverified]
- **Emails and memos: BLUF (bottom line up front).** First line: the ask or decision plus the deadline. Then the three facts needed to act. Before: "Hope you're well! I wanted to touch base about the vendor situation..." After: "Please approve the $40k Acme renewal by Friday; the current contract lapses Monday." Origin: US military writing guidance [classic; primary doc not opened]. Already echoed in human-writing's emails rule.
- **Persuasive essays and op-eds.** Open with the claim or a case that forces it; concede the best counterargument in its strongest form, then answer it; end on the consequence or call, not a recap. Op-ed: one idea, under about 800 words, a "why now" in the first paragraph, a specific ask. [classic craft; no primary source opened]
- **Product copy:** say what it does with a number or picture; one reader; claim plus proof adjacent. Already covered in human-writing craft.md. Local ux-copy skill adds: error = what happened + why + how to fix; button = verb + object ("Delete files" not "OK"). [local, see below]
- **Speeches (speechwriter craft):** write for the ear. Short sentences, repetition of a key phrase, rule of three used sparingly, one idea per speech, concrete story over claim, say the key line last. Test: read aloud at speaking pace and mark where you run out of breath. [classic; no single primary source opened]

### Inferences
- Add a "which Diataxis form is this?" check to human-writing for any technical doc. It stops the AI habit of a README that is half tutorial, half reference, half pitch.

### Gaps
- GOV.UK content design rules, Write the Docs, Stripe docs principles: not opened. Speech and op-ed items are craft consensus, not sourced.

## 4. Explanation craft

### Takeaway
Great explainers start from the reader's current model, name the likely misconception, then use a worked example before the general rule.

### Cited findings
- **Diagnose before teaching.** The local `learn` skill states: dialogue without diagnosis "produces more engagement and no more learning"; ask one calibrating question. [local `learn/SKILL.md`, Apache-2.0; its research claim not independently checked].
- **Misconception first.** Name the wrong model the reader likely holds, say why it is tempting, then replace it. Before: "Heavier objects fall faster? No." After: "Most people expect the heavy ball to land first, because a feather does. That's air, not weight. In a vacuum both land together." (own example) [classic; Derek Muller / Veritasium misconception research not opened, unverified].
- **Worked example before rule.** Show 12 x 15 broken into 12 x 10 plus 12 x 5, then state "split a factor." Already in human-chat and human-writing.
- **Analogies must map structure, not vibes.** State where the analogy holds and where it breaks. "Voltage is like water pressure: more pressure, more flow through the same pipe. It breaks down because electrons don't run out the end of the pipe." Test: can you list two correspondences between parts and one limit? [classic craft]
- **Feynman-style checks** [classic, attributed, not sourced to a primary document]: (1) explain it without the field's jargon; (2) if you can't, you don't yet understand it; (3) find the example that would make a freshman nod.
- **Layered depth.** One sentence, then one paragraph, then the detail; the reader can stop at any layer. [classic science-writing practice]
- **Concrete before abstract, small before big, one new idea per step.** Tutorial rule "general patterns emerge from concrete experience" from [Diataxis tutorials](https://diataxis.fr/tutorials/) [opened].
- **Check understanding without a quiz tone.** Ask the reader to predict the next step or apply the rule to a fresh case. [local `learn` skill leans on this]

### Inferences
- human-chat already has "one worked example, name the mistake". The senior layer adds: state the misconception explicitly, and say where the analogy breaks.

### Gaps
- No primary study of misconception-first teaching was opened; the evidence claim should not be repeated as fact.

## 5. Fiction at a senior level

### Takeaway
Seniors work on scene function, desire and subtext, and control of distance, then revise in separate passes rather than "polish everything".

### Cited findings
- **Psychic distance (Gardner).** "The distance the reader feels between himself and the events in the story" ([Stanford teaching writing page](https://teachingwriting.stanford.edu/psychic-distance), quoting *The Art of Fiction*, p. 111) [opened; Gardner's example ladder not on that page]. Another source says sudden unmotivated shifts read as amateur [search summary, [UNR](https://www.unr.edu/writing-speaking-center/student-resources/writing-speaking-resources/psychic-distance-in-creative-writing), page not opened, unverified]. Exercise (from Stanford page): rewrite one paragraph at two distances. Own example: far: "It was winter and the town was quiet." Mid: "Marta hated the quiet in winter." Close: "Quiet. God, the quiet. She'd take the sirens back."
- **Scene and sequel (Dwight Swain, *Techniques of the Selling Writer*).** Scene = goal, conflict, disaster; sequel = reaction, dilemma, decision. Use: if a scene has no goal and no opposing force, it is a sequel or filler; cut or merge. [classic, not opened]
- **Want vs need.** Want is the conscious pursuit; need is what the character lacks, often opposite. Tension lives in the gap. [classic craft shorthand]
- **Subtext.** Characters talk about the thing next to the thing. Before: "'I'm angry you forgot our anniversary.'" After: "'Nice tie. New?' She straightened his collar and didn't look up." (own example) Echoes human-fiction's dialogue rule.
- **Le Guin on craft** [classic; book not opened]: exercises isolate one tool at a time (sentence rhythm, repetition, point of view, punctuation). Use: one-variable revisions are teachable and checkable.
- **Pacing:** compress what the character does routinely, expand moments of choice. Summary for time, scene for change. [classic]
- **Revision passes novelists use** [classic craft consensus, no single source]: (1) structure/plot: move, cut, merge scenes; (2) character and want per scene; (3) dialogue and subtext; (4) distance and POV consistency; (5) sentence rhythm and specificity; (6) cut 10 percent; (7) proof.

### Inferences
- human-fiction's top-rules list lacks scene-function and distance checks; both are cheap to add as pass/fail items (section 7).

### Gaps
- Le Guin's specific exercises, Swain's exact terms, and Gardner's distance ladder were not verified in this session.

## 6. Editing someone else's voice; giving feedback

### Takeaway
Edit toward what the writer was trying to do, keep marks that sound like them, and give feedback that is ranked, specific, and actionable.

### Cited findings
- **Read for intent first, mark second.** Restate what the piece is trying to do; if you can't, that's finding one. [classic editor practice]
- **Preserve idiolect:** keep their dialect words, sentence length habit and quirks; fix only what blocks the reader. Local `own-voice`: "Edit lightly... Keep a slightly rough line if it sounds like them." [local, license unknown, no LICENSE file seen]
- **Query, don't rewrite, when meaning is uncertain.** "Do you mean A or B?" [classic copyediting practice]
- **Feedback order:** biggest issue first, at most 3 priorities, each with a place and a fix. Name what works so it survives revision. Local human-chat rule: "Feedback leads with the biggest real problem and the fix." [local]
- **Describe the reader's experience, not the writer's failing.** "I lost the thread here" beats "this is confusing." [classic workshop practice]
- **Offer a pattern, not a patch:** fix one instance, name the pattern, point to two others. Local `my-writing-voice` targets feedback at "recurring habits". [local]

### Gaps
- No primary editing-ethics source opened (e.g., EFA or Chicago).

## 7. Pass/fail checklists

### Structure pass
- [ ] I can state the claim or ask in one sentence. Pass: it is a claim, not a topic.
- [ ] Reader and their next action are named.
- [ ] Reverse outline written; every paragraph has one job.
- [ ] Strongest objection is present and answered (arguments).
- [ ] Nothing remains that doesn't serve the point.

### Line pass
- [ ] Subject and verb within about a dozen words of each other.
- [ ] Each sentence's last words carry its news.
- [ ] Each sentence opens on something the reader already has.
- [ ] Action is in verbs; nominalizations "the X-ation of" count under 2 per page.
- [ ] Sentence lengths vary: at least one under 8 words and one over 25 per 200 words (heuristic, mine).
- [ ] Every "however/therefore" marks a real logical turn.

### Genre pass
- [ ] Docs: each page is exactly one of tutorial / how-to / reference / explanation.
- [ ] Email: first line is the ask/answer; deadline stated.
- [ ] Speech: reads aloud without a breath problem; one idea.
- [ ] Explanation: misconception named; one worked example before the rule; analogy limit stated.

### Fiction pass
- [ ] Each scene: goal, opposition, change (or it is a sequel with a decision).
- [ ] Distance stays consistent within a paragraph unless the shift is deliberate.
- [ ] At least one exchange where the spoken line differs from the want.
- [ ] Ending leaves one cost or one open question.

### Feedback pass
- [ ] At most 3 priorities, ranked.
- [ ] Each has a location and a concrete fix or question.
- [ ] One true strength named.
- [ ] Writer's idiom preserved in the edit.

## Build on these local skills

Base path A: `/root/.claude/skills/synced/d13e5c22-fd75-4b81-b6fa-7bbe4432d675_ad4b38a0-ff16-4a31-8117-7e768f4021ea/`. Base path B: `/root/.claude/plugins/synced/d13e5c22-fd75-4b81-b6fa-7bbe4432d675_ad4b38a0-ff16-4a31-8117-7e768f4021ea/`. I skimmed SKILL.md only (not all references).

| Path | Reuse | Weak/missing | License |
|---|---|---|---|
| A `humanizer/SKILL.md` (5.2k words) | Tell taxonomy, "keep what it says, invent nothing", staging/rhythm/inflation grouping. Already adapted into human-writing/rewrite.md | Pure de-slop; no structure, no teaching | `license: MIT` in frontmatter; no LICENSE file |
| A `human-writing`, `human-chat`, `human-fiction` | The base layer in the repo (copies). Strong: specifics rule, tells, rubrics | No structural pass, no given-new, no scene/distance, no teaching mode | No LICENSE file seen (repo owner's own) |
| A `own-voice/SKILL.md` | Edit lightly; get real material; let user draft first on high-stakes; never invent experience | Short; no feedback structure | No LICENSE file; license unknown |
| A `my-writing-voice/` | Pattern for a voice profile + reference sample; "feedback targets recurring habits" | User-specific content; reuse the pattern only | No LICENSE file; user-specific, do not copy contents |
| A `doc-coauthoring/SKILL.md` (2.5k) | Three stages: context gathering, refine by section, reader testing with a fresh Claude. Good as a structure pass for docs | Heavy workflow; assumes shared-doc tools | No LICENSE file in folder; license unknown |
| A `internal-comms/` | 3P (Progress/Plans/Problems) update format; example files | Thin on craft; company-specific | Apache-2.0 (LICENSE.txt) |
| A `learn/SKILL.md` (2.2k) | Diagnose before teaching; one calibrating question; answer-vs-ask balance. Best base for "teach while creating" | Learner-centered; not about editing | Apache-2.0 (LICENSE.txt) |
| B `ziad-skills/skills/content-strategy/` | Audience/customer-language questions; topic clusters | Marketing-planning, not craft | Plugin has a LICENSE file; header showed Apache-2.0 for the top-level LICENSE (verify per plugin) |
| B `ziad-skills/skills/documentation-and-adrs/` | ADR template (Status/Context/Decision/Alternatives/Consequences); README structure; when to comment (the why) | Code-doc focused; no Diataxis | same as above |
| B `design/skills/ux-copy/` | Error = what/why/fix; CTA verb+object; confirmation buttons name the action | Generic tone list ("celebratory") | design plugin has a LICENSE file; I did not read it; verify |
| B `marketing/skills/*` (content-creation etc.) | Channel templates (blog, social) | Formulaic (hook-body-CTA, "bold claim"); risks the slop the library fights | marketing plugin LICENSE not read; verify |

Caution: three plugin LICENSE files exist (ziad-skills, design, marketing); I printed only the first lines of ziad-skills (Apache-2.0 header) and did not check the other two individually.

## Teaching notes

How an editor explains an edit so the writer learns (craft consensus [classic] plus the local `learn` skill's diagnose-first principle):

1. **Say the rule in one clause, then show the instance.** "Put the news last: 'We hired two people because sales rose 12 percent.'" Not a paragraph of grammar.
2. **Name the reader effect.** "The reader finishes on 'which is why we hired', so the 12 percent gets lost." Effects persuade; rules don't.
3. **Show before and after side by side, same content.** Change only the thing being taught.
4. **Teach one pattern per edit round (max 3).** Mark the first instance in full; list the line numbers of the rest.
5. **Ask before telling when the writer can find it.** "Which word do you want them to remember? Where does it sit?" (diagnose-first, from `learn`).
6. **Say what you kept and why.** "I left your short sentence in paragraph 4; it's doing the work."
7. **Make the check portable.** Give a test they can run alone: read the last three words of each sentence; are they the news?
8. **Mark taste calls as taste.** "My preference" vs "this breaks the reader's expectation" (the latter has a Gopen and Swan basis).
9. **Offer a teaching toggle.** Default: edit silently and report briefly. Teaching mode: add a "why" line per change and one transferable test. Keep the explanation shorter than the edit.
10. **Never explain with jargon the writer hasn't met** ("nominalization" needs "turning a verb into a noun, like 'make a decision' for 'decide'").
