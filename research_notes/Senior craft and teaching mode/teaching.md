# Teach-while-creating mode: research notes (2026-11-26)

Evidence tags: [V] opened this session; [S] seen in search snippet only; [U] unverified, from background knowledge, no source opened. The builder should treat [U] as needing a check before it is quoted.

## 1. Learning science that applies

### Takeaway
Novices learn faster from studied examples with the reasoning shown than from solving cold; that benefit reverses for experts; and long-term retention needs the learner to retrieve or produce something. So the mode must explain for novices, shrink for experts, and sometimes hand the learner a piece.

### Cited Findings
- Rule: show the work, not only the result. Why: worked-example effect, novices learn more from studying solved problems than from solving them (Sweller cognitive load line of work). Design: at the "explain" level show the finished thing plus the reasoning for 1-3 key decisions. Source: [U] Sweller and Cooper 1985; secondary overview [Worked-example effect](https://en.wikipedia.org/wiki/Worked-example_effect) [S].
- Rule: fade support as skill grows. Why: faded examples remove steps one by one (backward fading drops the last step first) until the learner solves alone; combining fading with self-explanation prompts improved learning efficiency in geometry. Design: first task fully explained, later tasks explain only what is new, then ask the learner to try the last step. Source: Renkl and Atkinson fading work, via [search summary of Renkl/Atkinson/Schwonke](https://link.springer.com/doi/10.1007/s11251-009-9107-8) [S]; original 2000 review not opened.
- Rule: explanation hurts experts. Why: expertise reversal effect, techniques that help novices lose effectiveness or turn negative for experienced learners, grounded in cognitive load (redundant info adds load). Design: the mode must detect or ask level, and "just do it" must be the default. Source: Kalyuga, Ayres, Chandler, Sweller 2003, Educational Psychologist 38(1):23-31 [S](https://ro.uow.edu.au/edupapers/136); review [Kalyuga 2007](https://www.doi.org/10.1007/S10648-007-9054-3) [S].
- Rule: apprenticeship order is model, coach, scaffold, fade. Why: Collins, Brown, Newman 1987 / Collins, Brown, Holum 1991 name modeling, coaching, scaffolding, fading, plus articulation, reflection, exploration. Design: map to levels (model = AI narrates its decisions; coach = AI comments on the learner's attempt; scaffold = AI leaves a gap; fade = fewer notes over time). Source: [Collins, Brown, Holum 1991 via secondary pages](https://www.aft.org/node/18441) [S]. One commentary notes the model is rarely discussed in instructional design today, so treat it as a frame, not proof.
- Rule: make the learner retrieve, not re-read. Why: after 5 minutes restudy beat testing, but after 2 days and 1 week prior testing gave substantially greater retention, and restudy raised confidence without raising retention. Design: one optional recall question per session, at the end, never mid-flow. Source: Roediger and Karpicke 2006, Psychological Science 17(3):249-255, [PubMed](https://pubmed.ncbi.nlm.nih.gov/16507066/) [S].
- Rule: effort that feels hard can help. Why: desirable difficulties (Bjork) and the fluency illusion (easy now is not durable). Design: the "learn by doing" level leaves small gaps; never withhold the working result, since the task must still get done. Source: [U] Bjork 1994 / Bjork and Bjork 2011; the local `teach` skill already uses the fluency-versus-storage-strength split (section 7).
- Rule: prompt self-explanation. Why: how much learners gain from examples depends on how well they explain solutions to themselves. Design: after a key decision, one "why do you think I picked X over Y?" at most, and only at the lesson level. Source: Renkl and Atkinson on self-explanation [S](https://link.springer.com/doi/10.1007/s11251-009-9107-8).
- Rule: expert think-aloud is the model, but keep it curated. Why: think-aloud makes tacit reasoning visible, which is the point of cognitive apprenticeship "modeling". Raw stream-of-consciousness would overload working memory. Source: Collins et al. above [S]; think-aloud protocol literature (Ericsson and Simon 1980/1993) [U].

### Inferences
- Explanations are a load. For a novice, load is the point; for an expert it is waste. The user's phrase "without slowing down people who just want the result" is the expertise reversal effect restated.
- Worked-example effect plus fading gives the level ladder in section 7 directly.

### Gaps
- Did not open Sweller's primary papers, Bjork's papers or Ericsson and Simon. Effect sizes for worked examples in code/AI settings not found.

## 2. Evidence on learning with AI assistants (2024-2026)

### Takeaway
Unguarded AI help raises performance now and lowers learning later; designs that keep learning make the learner think first or ask why after. But guarded designs can be ignored by learners, so the mode must be opt-in and low-friction, not a refusal.

### Cited Findings
- Rule: do not hand over answers silently. Why: in a high school math field experiment (about 1,000 students, one school in Turkey, one semester), students with a ChatGPT-like tool did worse when it was removed than students who never had it, a 17% reduction; a "GPT Tutor" with learning guardrails largely removed the harm. Design: explanations are the guardrail; the plain "just do it" level is for people who already know. Source: Bastani et al., PNAS 122(26), 2025, [Penn summary](https://chibe.upenn.edu/publications/generative-ai-without-guardrails-can-harm-learning-evidence-from-high-school-mathematics) [S]. Caveat: single site.
- Rule: asking why after getting code preserves learning. Why: RCT, 52 mostly junior engineers learning the Trio library: AI group 50% vs hand-coding 67% on the quiz (d=0.738, p=0.01), no significant speed gain, biggest gap on debugging. Patterns under 40%: full delegation (39%), progressive reliance (35%), iterative AI debugging (24%). Patterns at 65%+: generation-then-comprehension (86%, n=2), code with explanations (68%, n=3), conceptual questions only (65%, n=7). Cells are tiny and the authors say the pattern analysis is not causal. Design: put the explanation next to the code (hybrid pattern) and offer a "check my understanding" step after generation. Source: [Anthropic research post, Jan 2026](https://www.anthropic.com/research/AI-assistance-coding-skills) [V]; preprint [arXiv 2601.20245](https://www.arxiv.org/pdf/2601.20245) [S]. The authors expect agentic tools (like Claude Code) to show larger effects and point to Claude Code Learning and Explanatory modes as a response [V].
- Rule: keep the learner's own reasoning in the loop. Why: ChatGPT users improved essay scores but showed fewer metacognitive processes (evaluation, orientation) and no difference in knowledge transfer ("metacognitive laziness"). Design: ask the learner to state the goal or choose between options before the AI builds, at the lesson level only. Source: Fan et al., BJET 56:489-530, 2025, [arXiv 2412.09315](https://arxiv.org/abs/2412.09315v1) [S].
- Rule: a tutor built on pedagogy can beat class time. Why: RCT, 194 Harvard physics students, AI tutor built on the same practices as the in-class lesson: median post-test 4.5 vs 3.5, median time 49 vs 60 minutes, two topics, one institution, short-term outcome. Design: scaffold with structure (small sections, feedback), not just a persona. Source: Kestin et al., Scientific Reports 15:17458, 2025, [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/) [S].
- Rule: do not make questions mandatory. Why: Khanmigo's Socratic refusals led many students to stop using it or try to extract the answer; a Toronto study of 18 Tennessee middle schools found gains no larger than Khan practice alone (draft paper, per press). Khan Academy later made it terse before an attempt (hint plus pep talk) and integrated it into the exercise flow. Design: explanations default to short, appear with the answer, and are never a gate. Source: [Hechinger/KQED reporting](https://hechingerreport.org/proof-points-khanmigo-math-ai-tutor/) [S]; paper itself not opened.
- Product designs to copy or avoid: OpenAI Study Mode (July 29, 2025) is a system-prompt layer: Socratic questions, hints, self-reflection prompts, small sections, knowledge checks with feedback; users toggle it from "Study and learn"; coverage notes students can still get answers elsewhere [S](https://openai.com/index/chatgpt-study-mode/). Claude for Education learning mode (April 2025) asks "How would you approach this problem?" style questions, later added to the claude.ai style menu [S](https://www.anthropic.com/news/introducing-claude-for-education). Both are question-first. This project's mode is explanation-first with optional questions, closer to Explanatory.

### Inferences
- Common thread of surviving designs: the learner does a small amount of thinking, the AI does not hold back the result, the mode is opt-in.
- Debugging is where skill gaps show most, so a teach mode should explain failure causes, not just fixes.

### Gaps
- No study found testing explanation-with-code at different lengths. No 2026 replication of the Trio study found. Kosmyna et al. "Your Brain on ChatGPT" (2025) not opened; skip unless verified.

## 3. Claude Code built-in styles (verified)

### Cited Findings
- Claude Code has Default plus four built-in styles: Proactive, Concise, Explanatory, Learning. Each keeps the standard coding instructions and adds its own. Source: [Output styles docs](https://code.claude.com/docs/en/output-styles) [V].
- Explanatory: does the task as normal and adds `★ Insight` blocks of two or three points, before or after the code. Learning: same Insights plus Claude leaves a few lines for the user as `TODO(human)`, sends a "Learn by Doing" request (Context / Your Task / Guidance), stops, then responds with one Insight on the user's code. [V]
- Switch with `/output-style <name>`, `/config`, or `"outputStyle": "Explanatory"` in settings (value is case-sensitive in settings). Custom styles are Markdown files in `~/.claude/output-styles` or `.claude/output-styles`, with `keep-coding-instructions: true` to keep coding behavior; plugins can ship styles. [V]
- Both teaching styles produce longer output by design; styles are instructions, not guarantees. The docs recommend a skill for task-specific instructions that should load only when relevant. [V]

### Inferences
- A skill-based mode complements output styles: a style is session-wide and settings-driven; a skill can be turned on by a phrase and works on tools without output styles (ChatGPT dist copies).

### Gaps
- Whether Insight blocks contain a reusable "trade-off" slot: no, they are free-form two or three points.

## 4. Practical design

### Takeaway
Three levels, switched by plain words, explanation placed next to the thing it explains, hard length caps, and one optional question at the end.

### Cited Findings
- Rule: switching is plain words and sticky. Design: "teach me as you go", "explain your choices", "step by step lesson", "just do it / normal mode" to exit; persists until changed. Pattern from local skills `i-have-adhd` and `caveman` (persist until "stop ... mode") [V local]. Hooks guarantee, instructions do not [V docs].
- Rule: explanation sits at the decision. Design: level 1 inline "Why" lines next to the choice (code comments for code, a note under the section for UI); level 2 a short "Decisions" block after the output; level 3 a separate lesson file so the artifact stays clean. Basis: Anthropic hybrid pattern (code plus explanation) preserved learning [V]; Insight blocks sit beside code [V].
- Rule: short. Design: caps in section 7. Basis: expertise reversal and cognitive load [S]; Study Mode breaks answers into smaller sections [S].
- Rule: check understanding without nagging. Design: at most one question per response, only at level 3 or when asked, always skippable ("skip" accepted, never repeated); question asks for a prediction or a choice, not a definition. Basis: retrieval practice [S]; Khanmigo disengagement when questions were forced [S].
- Rule: adapt to level. Design: infer from the user's vocabulary and past messages; if unclear ask once ("new to this or just want the reasons?"); drop a level after the user says "I know this" or skips twice; never re-explain a concept already explained in the session. Basis: Kalyuga [S]; local `learn` skill: diagnose first with one calibrating question [V local].
- Rule: no condescension. Design: no praise filler, no "simply", no "as you may know"; treat the learner as a capable beginner; say "the usual choice is", not "beginners often". Basis: local human-chat rules (worked example first, name the common mistake) [V local]; engineering judgment, no study.
- Rule: never trade correctness for teaching. Design: the deliverable is complete and works at every level; teaching is added, never withheld. Basis: Khanmigo disengagement and Study Mode circumvention [S].

### Gaps
- No published data on ideal explanation length. The caps below are design guesses to be tested with the repo's with/without eval method.

## 5. How a senior explains a decision

### Takeaway
Five parts in fixed order, one line each. Predictable shape lowers reading load and makes the rule reusable.

### Cited Findings
- Rule: use the five-part form. Design (one decision per card):
  1. Decision: "Used a CSS grid for the card layout."
  2. Options: "Flexbox and floats were the other candidates."
  3. Reason: "Rows and columns both need to line up."
  4. Trade-off: "Grid is harder to make flow when items vary in height."
  5. Rule of thumb: "One dimension, flex; two dimensions, grid."
  Basis: cognitive apprenticeship modeling/articulation make expert reasoning explicit [S]; the structure itself (decision, options, reason, trade-off) mirrors architecture decision records [U]; engineering choice. The rule of thumb is the transfer step, which is what worked-example research says learners fail to extract unaided [U].
- Rule: pick which decisions to explain. Design: only decisions where a reasonable alternative exists and the choice changes the result; skip trivia. Cap at 3 per output at level 2.

### Gaps
- No empirical test of the five-part form found.

## 6. Accessibility: ADHD and different learners

### Takeaway
Next action first, one step per chunk, progress shown, no tangents. Local `i-have-adhd` already encodes this.

### Cited Findings
- Rules from the local skill: lead with the next action; number multi-step work (fewest steps); end with one concrete next action doable in two minutes; suppress tangents (offer them as a separate question); restate state every turn ("step 3 of 5 done"); give concrete time estimates; show completed wins; matter-of-fact error tone; cap lists at five [V local, first 4,500 characters read; rules 9+ not read].
- Design for teach mode: each explanation is one chunk with a bold label, 40 words or fewer; lesson level shows "Lesson 2 of 4" and what now works; the first line of any lesson is what to do, then why; a visible "skip explanations" option on every card; no walls of text; plain words and defined jargon on first use (helps non-native readers and novices). Working-memory basis: Sweller cognitive load [U]; ADHD basis is the skill's own claims, no study opened.

### Gaps
- No peer-reviewed source opened on ADHD and instructional text design; the local skill's claims are unsourced. Mark as practitioner guidance.

## 7. Build on these local skills

Paths: S = /root/.claude/skills/synced/d13e5c22-fd75-4b81-b6fa-7bbe4432d675_ad4b38a0-ff16-4a31-8117-7e768f4021ea; P = /root/.claude/plugins/synced/d13e5c22-fd75-4b81-b6fa-7bbe4432d675_ad4b38a0-ff16-4a31-8117-7e768f4021ea/ziad-skills/skills. I read the first part of each (teach ~5.5k chars of 1,563 words; learn ~4.5k of 2,180 words; i-have-adhd ~4.5k of 1,242; others only headers), so judgments on later sections are untested.

| Path | Reuse | Weakness | License |
|---|---|---|---|
| S/learn/SKILL.md | Diagnose before teaching (one calibrating question, skip when the learner already shows level); one step forward per turn with one question and one scaffold; know when you are done; tells fluent experts to be diagnosed at their level. Best at conversational tutoring. | Built for answering concept questions, not for a build task; question-heavy, so it risks the Khanmigo disengagement if copied wholesale; explicitly does not trigger on tasks. | Apache-2.0 (LICENSE.txt present) |
| S/teach/SKILL.md (+ MISSION-, LEARNING-RECORD-, RESOURCES-, GLOSSARY-FORMAT.md) | Fluency vs storage strength; retrieval, spacing, interleaving; one tightly scoped lesson per file with a single win; lesson files; learning records to track level; assets reuse. Best at multi-session courses. | Stateful workspace (MISSION.md, lessons/, reference/ HTML) is too heavy for teach-while-building; tells the model to find resources, adding cost. | No LICENSE file in folder; unknown, check before copying text |
| S/i-have-adhd/SKILL.md | Persistence wording, next action first, numbered steps, restate state, visible wins, tangent suppression, concrete time estimates. Best at output shape. | Slightly contradicts teaching (suppresses tangents and "by the way" insights); `disable-model-invocation: true`, so it only runs by command. | MIT (frontmatter) |
| S/doc-coauthoring/SKILL.md | Reader testing with a fresh Claude (check a lesson file works for someone with no context); staged context, refine, test. | Long (2,466 words), document-focused, not teaching. | No LICENSE file |
| S/learn-from-mistakes/SKILL.md | Catch-fix-lesson loop on self-detected errors; a "what I got wrong and why" note is genuine modeling of debugging. | Short; no teaching shape beyond that. | No LICENSE file |
| P/interview-me/SKILL.md | One question at a time with a recommended answer; the fit for "new to this or just want reasons?" level check. | Long (2,496 words); aimed at requirements, not level. | No LICENSE file at plugin root found |
| P/grill-me/SKILL.md | Each question carries a recommended answer worded so "yes" accepts it: low-effort checks. Rounds of questions. | Too intense for a learner who did not ask to be grilled. | none found |
| P/idea-refine/SKILL.md (+ frameworks.md, examples.md) | Diverge then converge for decisions; the options step feeds the "options considered" part of the five-part card. | Not teaching. | none found |
| P/caveman/SKILL.md | Persistent-mode, switch-off phrase, status wording ("stays on until 'normal mode'"); pattern for brevity at level 0. | Opposite goal (compression). | none found |

In-repo: /home/user/anti-slop/skills/human-chat/SKILL.md rule 5 already says "explain with one worked example using real numbers, before any general rule; name the common mistake and give the reason behind each step", so reuse that instead of writing new tutoring rules. /home/user/anti-slop/skills/human-ui/SKILL.md says "make those choices, and say why", with a contract (`references/contract.md`) listing audience, direction with a reason, type pair, palette, layout and states: the contract is the natural source of level-1 "why" lines for UI. Repo skill rule: SKILL.md under 500 words, details in `references/`.

## 8. Proposed design

Name: `teach-as-you-build` (a mode other skills defer to, not a replacement for any). Keep SKILL.md under 500 words; put the five-part card and examples in `references/`.

**Triggers (plain words, sticky until changed).**
- On: "teach me as you go", "explain what you're doing", "I'm learning this", "why did you do that", "mentor mode".
- Level words: "just do it" = 0; "explain the key choices" = 1; "walk me through it step by step" or "lesson" = 2.
- Off or reduce: "just the result", "skip the explanations", "I know this", "normal mode". Confirm in one line.
- Default with no trigger: level 0. If the user's wording is unclear, ask once: "New to this, or want the reasons only?"

**Levels.**
- Level 0, just do it: result only, no teaching text. Unchanged from the base skills.
- Level 1, key choices: the full result, then a "Why" block of at most 3 decisions, each in the five-part form compressed to 2-3 lines (decision, reason, trade-off; add rule of thumb only if it transfers). Max 120 words total. Code gets one-line "why" comments only where a choice is non-obvious. Never blocks the work.
- Level 2, lesson: everything in level 1, plus (a) a "What you now have" first line and next action; (b) up to 5 numbered steps, each one action plus one "why" line (40 words or fewer); (c) one worked-example pointer to the closest real file or screen; (d) a separate `lesson.md` (400 words or fewer) with the 3-5 decisions in full five-part form and a "Try it" step; (e) one optional prediction or choice question at the end, skippable. Fades: from the second task in a session explain only what is new, and offer to leave the last step to the learner (faded example).

**Rules for every level.**
- Output is complete and working; teaching never withholds the result.
- Max 3 explained decisions per response; max 40 words per why; one question per response, never repeated if skipped.
- Explain only decisions with a real alternative; skip trivia.
- Define a term once, on first use; never re-explain it in the session.
- Drop one level after two skips or an "I know this"; raise only when asked.
- No praise filler, no "simply", no tangents (offer them after).
- Show state: "Step 2 of 4 done" and what works now (from the ADHD skill).
- Errors: cause, fix, one-line lesson (from learn-from-mistakes).
- Keep AI-made look rules intact; teaching blocks use plain headings with no emoji or decorative badge.

**Where it lives and how it ships.**
- Skill folder with `SKILL.md`, `references/card.md` (five-part form and 3 examples per category: code, UI, writing), `evals/teach-as-you-build/prompts.md`.
- Mode state held in the conversation; for hosts with output styles, also ship a custom output style file that sets level 1, since styles apply per session [V docs].
- Eval, using the repo's existing with/without judge: (1) does level 0 add zero teaching text; (2) at level 1 are explanations at the decision, correct, 3 or fewer; (3) does a learner answer a transfer question after reading, versus without. Check length caps against the judged outputs before fixing them.

## Gaps across the whole note
- Bjork, Sweller, Ericsson and Simon, Kosmyna et al., and the Renkl 2000 review were not opened.
- Studies cited are small or single-site (Trio n=52 and quiz cells of 2-7, Turkey school, Harvard physics, Tennessee draft); effect sizes should not be generalised.
- Anthropic's later claude.ai "Learning" style rollout is from press only. The original April 2025 announcement page was seen only as a search result.
