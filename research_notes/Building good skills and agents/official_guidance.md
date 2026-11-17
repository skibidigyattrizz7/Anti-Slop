# Official guidance on skill, subagent and agent-instruction quality

Fetched 2026-11-17. Builds on `research_notes/AI tells and craft across media/skill_craft_and_distribution.md`, which covers the format basics (frontmatter limits, 500-line cap, progressive disclosure, plugin layout, Codex paths, AGENTS.md, Custom GPT limit). None of those are repeated here. Dates are as shown on the page. "Undated" means no visible date. "Unverified" means the claim came from a search snippet or a page that did not load.

## 1. Length, specificity, examples vs rules

### Context engineering: "right altitude" and examples over edge-case lists

- **Rule / fact:** Prompts should sit at the "right altitude", between two failure modes: brittle hardcoded logic and vague high-level guidance. For examples, Anthropic says teams "will often stuff a laundry list of edge cases into a prompt" and "We do not recommend this." It recommends "a set of diverse, canonical examples" instead.
- **Why it matters for our skills:** Our SKILL.md should not turn into a list of every slop pattern. Pick a few canonical bad-to-good examples per rule, and state the rule once.
- **Concrete example or pattern:** One before/after pair for "generic opener" ("In today's fast-paced world, ..." becomes a specific first sentence). Do not add a 40-item banned-phrase list in SKILL.md. Put the long list in `references/` and have the script check it.
- **Source:** https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (published Sep 29, 2025)

- **Rule / fact:** "As the number of tokens in the context window increases, the model's ability to accurately recall information" falls. Anthropic calls this context rot.
- **Why it matters for our skills:** Every extra line in SKILL.md competes with the code being checked. This backs the "only what the model would get wrong" rule with a measured-quality reason, not just a cost reason.
- **Concrete example or pattern:** Keep the checker's SKILL.md to the procedure and push the rubric into `references/` that loads only on demand.
- **Source:** same URL (Sep 29, 2025)

### Skill authoring: concise, degrees of freedom

- **Rule / fact:** "Only add context Claude doesn't already have." The official test is to ask "Does Claude really need this explanation?" and "Does this paragraph justify its token cost?"
- **Why it matters for our skills:** Gives a concrete per-paragraph test to run in the checker. The prior notes state the rule. This is the test form.
- **Concrete example or pattern:** Their own "bad" example for PDF extraction explains what a PDF is in about 150 tokens. The good version is a 50-token code block.
- **Source:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices (date not shown)

- **Rule / fact:** Match specificity to fragility. High freedom (text heuristics) when "multiple approaches are valid"; medium (pseudocode or templates with parameters) when "a preferred pattern exists"; low (exact script, "Do not modify the command or add additional flags") when "operations are fragile and error-prone".
- **Why it matters for our skills:** Our checker's scoring step is low freedom (run the script, report its JSON). Its judgment on tone is high freedom. Say which is which in each SKILL.md. Do not give the same freedom to both.
- **Concrete example or pattern:** "Run `python scripts/check_slop.py FILE` and report its JSON exactly. Judge only the lines the script did not flag." Low freedom for the first sentence, high freedom for the second.
- **Source:** same URL (date not shown)

- **Rule / fact:** Avoid offering many options. Give a default with an escape hatch. The official bad example lists five PDF libraries. The good example uses one, with one fallback for a named case.
- **Why it matters for our skills:** Our fixer should use one default fix per rule, with a fallback only for a named case.
- **Concrete example or pattern:** "Replace the phrase with a specific claim. If no specific claim exists, delete the sentence." Not a menu of six rewrites.
- **Source:** same URL (date not shown)

### Prompting docs: what not to do

- **Rule / fact:** "Tell Claude what to do instead of what not to do." Their example: "Do not use markdown in your response" should become "Your response should be composed of smoothly flowing prose paragraphs."
- **Why it matters for our skills:** Most of our rules are "don't use X". Rewrite each as the positive behaviour, and keep the banned term only in the checker's list.
- **Concrete example or pattern:** Not "Don't use em dashes." Instead: "Join clauses with a comma, a full stop, or a conjunction." Keep "em dash" in the script's regex, not in the model's instructions.
- **Source:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices (Anthropic prompting guide; date not shown; fetched through a saved, truncated copy)

- **Rule / fact:** Explain the why. The skill-creator guide says: "Try hard to explain the why behind everything you're asking the model to do." It says "If you find yourself writing ALWAYS or NEVER in all caps, or using super rigid structures, that's a yellow flag."
- **Why it matters for our skills:** A bare rule is harder to apply to cases it did not name. A reason lets the model judge the edge cases.
- **Concrete example or pattern:** "Avoid stock openers. Readers skip them, which costs the first line its job." Not "NEVER start with 'In today's world'."
- **Source:** https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md (date not shown)

### Examples

- **Rule / fact:** Anthropic recommends "3–5 examples for best results" in wrapped `<example>` tags. Multishot examples also shape the model's thinking.
- **Why it matters for our skills:** Three is the recommended count. Our SKILL.md should carry at most three examples, and the rest belong in `references/`.
- **Concrete example or pattern:** A commit-message skill with three input/output pairs in an `<examples>` block, not ten.
- **Source:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices (date not shown)

## 2. Failure modes: too many rules, contradictions, negatives, triggering

- **Rule / fact:** Contradictory rules hurt GPT-5 more than other models. The OpenAI guide says "poorly-constructed prompts containing contradictory or vague instructions can be more damaging to GPT-5 than to other models." Removing conflicts "drastically streamlined and improved their GPT-5 performance."
- **Why it matters for our skills:** Our checker's rubric must not contain two rules that disagree (for example, "keep sentences short" and "always add a supporting example"). Add a lint step that catches rules that point in opposite directions.
- **Concrete example or pattern:** Their healthcare prompt had conflicting rules about when to contact a patient and when to look up a profile. The fix was one consistent rule.
- **Source:** https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide (OpenAI cookbook; date not shown; the page says it "is archived and may reference outdated models")

- **Rule / fact:** Instruction density hurts accuracy. IFScale (Jaroslawicz et al., arXiv 2507.11538, submitted Jul 15, 2025) tested up to 500 keyword instructions. It reports: "even the best frontier models only achieve 68% accuracy at the max density of 500 instructions." Models also "show a bias toward earlier instructions."
- **Why it matters for our skills:** A rule list is not free. Put the most important rule first in each file. Keep each SKILL.md to a small number of hard rules. Their paper does not give a curve for smaller counts, so do not claim a specific safe number.
- **Concrete example or pattern:** Put "Never change the meaning of a claim" at the top of the fixer, not after 30 style rules.
- **Source:** https://arxiv.org/abs/2507.11538 (Jul 15, 2025). The page gives no accuracy figures below 500 instructions. That gap is unverified for our size.

- **Rule / fact:** Newer Claude models overtrigger on emphasis. The Anthropic guide says: "If your prompts were designed to reduce undertriggering on tools or skills, these models might now overtrigger. The fix is to soften any aggressive language." Its example is changing "CRITICAL: You MUST use this tool when..." to "Use this tool when...". It also says "Instructions such as 'If in doubt, use [tool]' cause overtriggering."
- **Why it matters for our skills:** This conflicts with the skill-creator advice in the next entry. Our trigger text should be specific about when to use the skill, and should not add urgency words.
- **Concrete example or pattern:** Description: "Use when the user asks to check or rewrite UI copy for generic AI phrasing. Not for code comments." No "ALWAYS", no "if in doubt".
- **Source:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices (date not shown). Opus 4.5 and 4.6 are named in that guide.

- **Rule / fact:** Claude tends to undertrigger skills, so descriptions should be "pushy". The skill-creator text reads: "Currently Claude has a tendency to 'undertrigger' skills -- to not use them when they'd be useful." It says: "please make the skill descriptions a little bit 'pushy'."
- **Why it matters for our skills:** Pushy wording and the overtrigger warning above both apply. The resolution is to be pushy about the skill's real scope (listing contexts, including indirect ones) and explicit about exclusions, not to add urgency.
- **Concrete example or pattern:** Their example is "Make sure to use this skill whenever the user mentions dashboards, data visualization, internal metrics". Ours could be "Use whenever the user asks to make text sound less AI-written, even if they say 'humanize', 'polish this', or 'does this sound robotic'."
- **Source:** https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md (date not shown)

- **Rule / fact:** Negative instructions are weak when they are the only guidance. The OpenAI guide uses both styles and gives no general rule. Anthropic recommends positive instructions (previous entry).
- **Why it matters for our skills:** Use exclusions only where the near-miss is real. For a slop checker, "Do not rewrite code comments" is needed. "Do not use bullet points" is not, if the model already avoids them.
- **Source:** https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide (date not shown); Anthropic guide above.

## 3. Descriptions and triggering from everyday words

- **Rule / fact:** Write the description in the third person, with what it does and when to use it. Anthropic says: "Always write in third person... inconsistent point-of-view can cause discovery problems." It gives the example "Processes Excel files and generates reports" and says to avoid "I can help you process Excel files."
- **Why it matters for our skills:** Our descriptions must be third person, and must name everyday user phrases (the search pool is what users type, not our taxonomy).
- **Concrete example or pattern:** "Rewrites UI copy and docs to remove generic AI phrasing. Use when the user asks to make text sound less AI-written, humanize it, or polish copy, even without naming a file."
- **Source:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices (date not shown)

- **Rule / fact:** Triggering depends on the description alone, and skills tend to be consulted only for tasks that need knowledge beyond the agent's basic tools. "A simple, one-step request like 'read this PDF' may not trigger a PDF skill even if the description matches perfectly." Specialized domains are where a good description matters.
- **Why it matters for our skills:** A slop check on one sentence may never trigger the skill. Our trigger wording should target multi-step review or rewrite requests, and the skill should be useful enough to be worth loading.
- **Source:** https://agentskills.io/skill-creation/optimizing-descriptions (undated)

- **Rule / fact:** Build a trigger eval. About 20 queries, 8–10 should-trigger and 8–10 should-not-trigger. Include near-misses as the most valuable negatives. Queries must be "realistic and something a Claude Code or Claude.ai user would actually type." Run each query about 3 times and count a trigger rate. Threshold: 0.5 for should-trigger, below 0.5 for should-not.
- **Why it matters for our skills:** This is the only concrete method published for triggering reliability. Use the 3-run, 0.5-threshold scheme in our CI.
- **Concrete example or pattern:** For the slop skill, a should-not-trigger near-miss is "Make this paragraph shorter for my slide deck" (length, not slop). A should-trigger is "my boss says this sounds like ChatGPT wrote it, can you fix it?"
- **Source:** https://agentskills.io/skill-creation/optimizing-descriptions (undated)

- **Rule / fact:** Split the trigger queries 60% train and 40% held-out. Edit only from train failures. Pick the final description by validation score. Five iterations are usually enough. Avoid adding keywords taken from failed queries, because that overfits.
- **Why it matters for our skills:** Without a held-out set, our description tuning will look better than it is.
- **Source:** https://agentskills.io/skill-creation/optimizing-descriptions (undated); the 60/40 split is also quoted in the skill-creator SKILL.md (date not shown)

- **Rule / fact:** Skill evaluation should compare with and without the skill. Start with 2–3 test cases. Use a with-skill run, a without-skill baseline, and assertions that can be checked objectively. Remove assertions that pass in both settings, because they measure nothing.
- **Why it matters for our skills:** Our checker must show it changes results versus a plain model prompt. If the plain model scores the same, the skill adds nothing.
- **Source:** https://agentskills.io/skill-creation/evaluating-skills (undated)

- **Rule / fact:** Grade assertions with evidence. "Require concrete evidence for a PASS. Don't give the benefit of the doubt." Prefer scripts for mechanical checks.
- **Why it matters for our skills:** Matches our plan of script for counts, model for judgement. The rule also shows what a valid judge output looks like: PASS or FAIL plus a quote.
- **Source:** https://agentskills.io/skill-creation/evaluating-skills (undated)

- **Rule / fact:** Anthropic's own skill tests use Haiku, Sonnet and Opus. "What works perfectly for Opus might need more detail for Haiku." The checklist requires "Tested with Haiku, Sonnet, and Opus."
- **Why it matters for our skills:** Test the checker on the cheapest model we plan to use, since a rule that Haiku ignores is not a working rule.
- **Source:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices (date not shown)

## 4. Scripts vs prose

- **Rule / fact:** Scripts should handle errors, and their messages should list what is valid. Anthropic's example says: "Field 'signature_date' not found. Available fields: customer_name, order_total, signature_date_signed." Also: "Make validation scripts verbose with specific error messages."
- **Why it matters for our skills:** Our checker output and the fixer's validation loop should print the valid options, so the model can self-correct without another read.
- **Source:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices (date not shown)

- **Rule / fact:** Use plan-validate-execute for batch or destructive edits. Write a plan file, validate it with a script, and apply only after it passes.
- **Why it matters for our skills:** This is the right fixer shape for multi-edit runs. It also gives a diff for the checker to re-score.
- **Source:** same URL (date not shown)

- **Rule / fact:** A script the model runs does not load its source into context. "Only the script's output consumes tokens." Read-as-reference and run-as-tool must be stated separately.
- **Why it matters for our skills:** Say "run `scripts/check.py`" for the checker, and "read `references/rubric.md`" for the rubric. Never mix them.
- **Source:** same URL (date not shown)

## 5. Multi-agent systems and subagents

- **Rule / fact:** Anthropic's multi-agent research system (Opus 4 lead, Sonnet 4 subagents) "outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval." Token use alone "explains 80% of the variance" on BrowseComp. Multi-agent runs "use about 15× more tokens than chats."
- **Why it matters for our skills:** Subagents buy quality at a steep token price. Our checker and fixer subagents only pay off if their gain beats the token cost on our own eval. Measure this; do not assume it.
- **Concrete example or pattern:** Run the same 10 drafts with and without the checker subagent, and compare the score per token.
- **Source:** https://www.anthropic.com/engineering/multi-agent-research-system (published Jun 13, 2025)

- **Rule / fact:** Each subagent task needs four things: "an objective, an output format, guidance on the tools and sources to use, and clear task boundaries." Vague delegation caused two subagents to duplicate work.
- **Why it matters for our skills:** The fixer prompt must carry the checker's findings as text, plus the objective, output format, allowed files, and stop condition.
- **Concrete example or pattern:** "Objective: fix only findings F1–F4 below. Output: edited file plus a list of changed line numbers as JSON. Boundaries: do not edit lines not cited in a finding; do not change the rubric. Findings: [...]"
- **Source:** https://www.anthropic.com/engineering/multi-agent-research-system (Jun 13, 2025)

- **Rule / fact:** Multi-agent is a poor fit when "all agents share the same context" or when there are "many dependencies between agents."
- **Why it matters for our skills:** A fixer that edits the same file the checker reads is a shared-context task. Run it in sequence in the same context, or give the fixer its own copy and merge.
- **Source:** same URL (Jun 13, 2025)

- **Rule / fact:** Subagents return condensed results. Anthropic describes subagents returning "only a condensed, distilled summary of its work (often 1,000-2,000 tokens)."
- **Why it matters for our skills:** Our checker subagent should return a short JSON findings list, not its reasoning. That keeps the main context clean.
- **Source:** https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (Sep 29, 2025)

- **Rule / fact:** Newer Claude models delegate to subagents readily. "Claude Opus 4.6 has a strong tendency to use subagents... for code exploration when a direct grep call is faster." Anthropic gives a damping prompt: "Use subagents when tasks can run in parallel, require isolated context, or involve independent workstreams that don't need to share state. For simple tasks... work directly rather than delegating."
- **Why it matters for our skills:** Our SKILL.md files that spawn checkers should say when not to spawn one. Otherwise a one-line fix becomes a subagent call.
- **Source:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices (date not shown)

- **Rule / fact:** Start simple. Anthropic's "Building effective agents" post (Dec 2024) recommends the simplest workable pattern and adding agents only when needed. **Possibly outdated** (2024). Not fetched in this pass; treat as unverified.
- **Source:** https://www.anthropic.com/research/building-effective-agents (Dec 2024; not fetched)

## 6. Tool descriptions (for checker tools and scripts)

- **Rule / fact:** Tool descriptions are "one of the most effective methods for improving tools." Describe inputs and outputs clearly and "enforce with strict data models."
- **Why it matters for our skills:** Our script CLI should have a fixed input and output schema, documented in its `--help` and in SKILL.md.
- **Source:** https://www.anthropic.com/engineering/writing-tools-for-agents (Sep 11, 2025)

- **Rule / fact:** Give the agent a response-format choice: "concise" or "detailed". Cap output with "pagination, range selection, filtering, and/or truncation."
- **Why it matters for our skills:** The checker should default to a compact findings list and offer a `--verbose` flag only on request.
- **Source:** same URL (Sep 11, 2025)

## 7. OpenAI vs Claude guidance: where they differ

- **Rule / fact:** OpenAI's GPT-5 guide asks for persistence on purpose. It suggests "You are an agent - please keep going until the user's query is completely resolved," and says to control eagerness with `reasoning_effort`. Anthropic instead warns against over-prompting persistence, and says to soften emphasis.
- **Why it matters for our skills:** The same SKILL.md text can behave differently on each model. Test on each one we claim to support.
- **Source:** https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide (date not shown; archived page)

- **Rule / fact:** OpenAI's GPT-5 guide recommends XML-style spec blocks. Its example says "using structured XML specs like <[instruction]_spec> improved instruction adherence" in Cursor's testing. Anthropic also uses XML tags, with `<example>` and `<examples>`.
- **Why it matters for our skills:** Wrapping rules and examples in tags works on both. Keep tag names consistent across the library.
- **Source:** https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide (date not shown); Anthropic prompting guide (date not shown)

- **Rule / fact:** OpenAI's agent guide: "A Practical Guide to Building Agents" (PDF). **Unverified.** The fetch returned binary PDF data with no readable text, so I could not confirm its manager vs. handoff advice or any date.
- **Source:** https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf (not readable in this pass)

## Gaps

- **Measured trigger rates for any published skill library:** none found. The only method is the agentskills.io 3-run, 0.5-threshold scheme. No lab published trigger-accuracy numbers in the pages read.
- **Instruction count threshold:** IFScale gives only the 500-instruction endpoint (68% for the best frontier models). No safe count for a SKILL.md was found.
- **OpenAI agent-building PDF:** unverified (binary only). Custom GPT and Codex-specific instruction advice beyond the prior notes: not read.
- **Claude Code subagent docs and skill docs:** covered in the prior notes, not re-read here.
- **Anthropic "Building effective agents" (Dec 2024):** possibly outdated; not fetched.
- **Anthropic Opus 5 and Fable 5.2 prompting pages:** listed in the prompting guide but not read. They may change the overtrigger and subagent advice above.
- **Blind-comparison judging and self-preference bias:** covered in the prior notes; not re-checked.
