# Skill craft and distribution: research notes

Fetched 2026-11-17. Dates are shown where the source gives one. "Undated" means the page had no visible date. Items marked UNVERIFIED were seen only in search snippets or not fetched.

## 1. Agent Skills format (agentskills.io spec, Claude Code docs)

- **Rule / fact:** SKILL.md needs YAML frontmatter with `name` (1-64 chars, lowercase a-z, 0-9, hyphens; no leading/trailing or double hyphen; must equal the parent folder name) and `description` (1-1024 chars). Optional: `license`, `compatibility` (max 500 chars), `metadata` (string map), `allowed-tools` (experimental).
- **Why it matters for our library:** Our `name` values must match folder names exactly, and the validator should enforce this. The spec gives us a portable baseline that Codex and other clients also read.
- **Example or pattern:** `name: pdf-processing` in folder `pdf-processing/`. Good description: "Extracts text and tables from PDF files, fills PDF forms, and merges multiple PDFs. Use when working with PDF documents or when the user mentions PDFs, forms, or document extraction." Poor: "Helps with PDFs."
- **Source:** https://agentskills.io/specification (undated; fetched 2026-11-17)

- **Rule / fact:** Keep SKILL.md under 500 lines and under about 5,000 tokens. Move detail to `references/`, `scripts/`, `assets/`. Keep references one level deep from SKILL.md.
- **Why it matters for our library:** This is the direct answer to "SKILL.md short, detail elsewhere." Our SKILL.md target should be well under 150 lines, with the top-level file acting as a router.
- **Example or pattern:** "Read `references/api-errors.md` if the API returns a non-200 status code." Tell the agent when to load each file. A generic "see references/ for details" is weaker.
- **Source:** https://agentskills.io/specification ; https://agentskills.io/skill-creation/best-practices (undated)

- **Rule / fact:** Claude Code reads only `name` and `description` (plus `when_to_use`) for the listing. Those two are truncated together at 1,536 characters. Full SKILL.md loads only on invocation. Re-attached skills after compaction keep the first 5,000 tokens each, with a 25,000-token combined budget.
- **Why it matters for our library:** Trigger words must sit in the first sentence, because later text may be cut. Keep bodies short so compaction does not drop them.
- **Example or pattern:** Front-load the use case: "Use when writing or reviewing UI copy, to remove generic phrasing. Triggers: 'make this less AI', 'humanize', 'polish copy'."
- **Source:** https://code.claude.com/docs/en/skills (page cites Claude Code v2.1.319; undated)

- **Rule / fact:** Claude Code frontmatter fields are optional and unknown fields are silently ignored. Useful ones: `disable-model-invocation: true` (manual `/name` only), `user-invocable: false`, `allowed-tools`, `context: fork` plus `agent` (run in a subagent), `paths`.
- **Why it matters for our library:** Checker and fixer agents should use `context: fork` so their long reasoning does not fill the main context. Pure manual tools can use `disable-model-invocation` to save description budget.
- **Example or pattern:** `context: fork` with `agent: anti-slop-checker` for a heavy audit skill.
- **Source:** https://code.claude.com/docs/en/skills (undated)

- **Rule / fact:** Official progressive-disclosure tiers are: metadata (~100 tokens, always loaded), SKILL.md body (loaded on activation), resources (loaded only when needed). Scripts run without their source being loaded into context.
- **Why it matters for our library:** Put a checker's deterministic logic in `scripts/` and its rules in `references/`. The model then reads only the output, not the code.
- **Example or pattern:** `scripts/check_slop.py file.md` prints JSON findings with line numbers. SKILL.md says: "Run the script first; fix only the reported lines."
- **Source:** https://code.claude.com/docs/en/skills ; https://agentskills.io/specification (undated)

- **Rule / fact:** Anthropic's own best practices: include only what the agent would get wrong without the instruction. Prefer defaults over menus. Use gotchas lists, templates, checklists, and validation loops. Match instruction specificity to how fragile the task is.
- **Why it matters for our library:** This is the explicit anti-bloat rule the owner wants. Every line in our SKILL.md must pass "would the model get this wrong without it?"
- **Example or pattern:** Gotcha: "The `users` table uses soft deletes; queries need `WHERE deleted_at IS NULL`." Bloat: "PDF stands for Portable Document Format."
- **Source:** https://agentskills.io/skill-creation/best-practices (undated)

- **Rule / fact:** Validation loop: do the work, run a validator, fix, rerun, proceed only on pass. A validator's error messages should say what is valid ("available fields: a, b, c") so the agent can self-correct.
- **Why it matters for our library:** Our fixer loop should be this exact pattern, with a stop condition.
- **Example or pattern:** Plan-validate-execute: `validate.py plan.json source.json` before any write.
- **Source:** https://agentskills.io/skill-creation/best-practices (undated)

- **Rule / fact:** Official validator: `skills-ref validate ./my-skill` (checks frontmatter and naming). Evaluation guidance lives at agentskills.io/skill-creation/evaluating-skills and optimizing-descriptions (we did not fetch these pages).
- **Why it matters for our library:** Use this in CI from day one. Our own checks should go beyond it (content quality), not replace it.
- **Source:** https://agentskills.io/specification (undated); evaluation pages UNVERIFIED (not fetched)

## 2. Subagents (.claude/agents/*.md)

- **Rule / fact:** A subagent is one Markdown file with frontmatter. Only `name` and `description` are required. `name` is unique (max 256 chars, no `:`). Fields include `tools` (allowlist), `disallowedTools`, `model` (`sonnet`, `opus`, `haiku`, `inherit`, or ID), `maxTurns`, `skills` (preloaded), `effort`, `color`, `isolation: worktree`, `memory`. Unknown fields are silently ignored. Files lacking `name` or `description` are skipped silently.
- **Why it matters for our library:** A checker must be read-only: `tools: Read, Grep, Glob` (and `Bash` only for our scripts). A fixer gets `Edit, Write` but not the ability to change the rubric. Missing a `description` means the agent never runs.
- **Example or pattern:**
  ```
  ---
  name: slop-checker
  description: Scores a UI or copy file against the anti-slop rubric. Use proactively after UI edits.
  tools: Read, Grep, Glob, Bash
  model: sonnet
  ---
  ```
- **Source:** https://code.claude.com/docs/en/sub-agents (undated; cites Claude Code v2.1.x)

- **Rule / fact:** The subagent body is its whole system prompt. A non-fork subagent does not see the conversation, so the caller's delegation message must carry the task, paths, and any rule that must reach it. Keep descriptions brief: combined non-built-in descriptions above 15,000 tokens trigger a startup warning.
- **Why it matters for our library:** The fixer must receive the checker's findings as explicit text, not as "see above." Keep each description to one or two sentences.
- **Source:** https://code.claude.com/docs/en/sub-agents (undated)

## 3. Plugins and marketplaces

- **Rule / fact:** Plugin layout: `.claude-plugin/plugin.json` (only `name` is required; kebab-case), with components at the plugin root: `skills/<name>/SKILL.md`, `agents/`, `commands/`, `hooks/hooks.json`, `scripts/`. A plugin with `SKILL.md` at its root and no `skills/` loads as one skill. Put nothing except the manifest inside `.claude-plugin/`.
- **Why it matters for our library:** One repo can ship several skills, the checker agent, and a hook, as one plugin. Use `claude plugin validate ./plugin --strict` in CI.
- **Example or pattern:** `anti-slop/.claude-plugin/plugin.json` with `version`, `description`, `author`, `license: "MIT"`, `keywords`.
- **Source:** https://code.claude.com/docs/en/plugins-reference (undated; cites v2.1.281-2.1.288)

- **Rule / fact:** Plugin names must not start with `claude-`, `anthropic-`, `anthropics-`, or `cc-plugin-`, and must not be `claude`, `anthropic`, `claude-code`, etc. Names containing `claude` or `anthropic` as a word get a warning. Using `official` next to those words is an error.
- **Why it matters for our library:** Avoid names like `claude-antislop`. Use `slopbuster` or `anti-slop-kit`. This also avoids implying Anthropic endorsement.
- **Source:** https://code.claude.com/docs/en/plugins-reference (undated)

- **Rule / fact:** `version` is a free string, not checked as semver. Setting it pins users to that version until it changes. `defaultEnabled` is only read the first time. Unknown top-level keys are stripped with a warning. Strict objects (`userConfig`, `channels`) reject unknown keys.
- **Why it matters for our library:** Bump `version` on every release, or users never receive updates.
- **Source:** https://code.claude.com/docs/en/plugins-reference (undated)

- **Rule / fact:** `plugin.json` fields `icon`, `documentationUrl`, `supportUrl`, `privacyPolicyUrl`, `termsOfServiceUrl` are read only by Anthropic's directory on submission. Submit via the directory process.
- **Source:** https://code.claude.com/docs/en/plugins-reference (undated)

## 4. Cross-tool formats (Codex, Custom GPTs, AGENTS.md)

- **Rule / fact:** Codex scans `.agents/skills` from the working directory up to the repo root, plus `$HOME/.agents/skills`, `/etc/codex/skills`, and bundled system skills. Same SKILL.md with `name` and `description`. Optional `agents/openai.yaml` sets UI metadata and `policy.allow_implicit_invocation`. Codex loads the body only when it selects a skill.
- **Why it matters for our library:** One `skills/<name>/` tree can serve Claude Code and Codex. Copy or symlink into `.agents/skills` for Codex. Symlinks are supported.
- **Size limit:** the skill list uses at most 2% of context (8,000 chars if unknown). `skills.max_context_tokens` can raise it to 10,000 tokens. The page gives no body limit.
- **Source:** https://learn.chatgpt.com/docs/build-skills (redirected from developers.openai.com/codex/skills; undated). The page says Codex builds on the agentskills standard but does not claim full conformance.

- **Rule / fact:** AGENTS.md is plain Markdown at the repo root, with no required fields. The nearest file in the directory tree wins. It is read by Codex, Cursor, Copilot, Gemini CLI, Aider, Zed, and others. It is now stewarded by the Agentic AI Foundation (Linux Foundation). The page gives no size limit.
- **Why it matters for our library:** Ship a short AGENTS.md that tells non-Claude agents to read `skills/*/SKILL.md`. This is the cheapest cross-tool path. Ruled out: making AGENTS.md the full library.
- **Source:** https://agents.md (undated; claims over 60k projects)

- **Rule / fact:** ChatGPT Custom GPT builder: instructions field limit is 8,000 characters (several third-party sources agree; the error text is quoted in a community thread). Knowledge file count and size are inconsistent across sources: 20 files and 512 MB per file is the most common figure, but it is UNVERIFIED against OpenAI's Help Center (the Help Center fetch returned 403).
- **Why it matters for our library:** A Custom GPT cannot hold a full library. Its instructions must be a condensed rubric (under 8,000 characters), with the references uploaded as knowledge files. Flag that the file count is unverified.
- **Source:** https://help.openai.com/en/articles/8554397-creating-a-gpt (fetch returned 403; figures from search snippets, e.g. https://community.openai.com/t/how-can-i-increase-the-ceiling-for-gpt-instructions-beyond-8000-characters/801867 ; undated)

- **Rule / fact:** ChatGPT account-level custom instructions were reportedly raised from 1,500 to 5,000 characters, effective 2026-07-15, for paid plans. Plan lists differ between sources.
- **Why it matters for our library:** This is a per-user field, not the GPT builder limit. Do not confuse the two in docs.
- **Source:** Search snippets only, e.g. https://www.kucoin.com/news/flash/openai-raises-chatgpt-custom-instructions-limit-to-5-000-characters-for-paid-users (2026, UNVERIFIED against OpenAI)

## 5. Agensi.io (creator marketplace)

- **Rule / fact:** Agensi is a curated marketplace for SKILL.md skills. Creators keep 70% of net revenue ("one all-inclusive 30% platform fee on the net price"). Listing is free. Prices are set by the creator, either as one-time purchase or monthly subscription. Example prices on the page: $29 one-time, $19/mo, $29/mo.
- **Why it matters for our library:** Sets the payout norm for paid skills. Note that PromptSpace gives 80/20; the company's own page says 70%. Trust the page, and recheck before pricing anything.
- **Source:** https://www.agensi.io/sell (page shows "© 2026"; no effective date). Search summary: https://www.agensi.io/learn/how-to-sell-skills-on-agensi

- **Rule / fact:** Submission is a ZIP containing SKILL.md, plus optional scripts, templates, or references. Each skill gets an 8-check automated security scan, an AI review of safety and intent, and a human review (usually 24-48 hours). Obfuscated code, undisclosed network calls, credential harvesting, and repackaged free skills are rejected. Creators keep ownership but grant Agensi a distribution licence. Skills run inside the buyer's agent and are not downloaded. Paid skills need a payout method before going live.
- **Why it matters for our library:** If we ever sell, the packaging and "no repackaged free skills" rule means our free MIT skills cannot simply be re-listed as paid. Licence must be clean. Their security scan rules are a free checklist for our own CI.
- **Source:** https://www.agensi.io/sell (undated)

- **Rule / fact:** Payouts: Stripe to a bank account, or USDC on Solana via Zoneless, 14 days after each sale. Payout triggers at $3.50 in waiting earnings. KYC required.
- **Source:** https://www.agensi.io/sell (undated)

- **Rule / fact:** Scale claims conflict. Search summaries cite "over 2,000 skills three months after launch" (Barchart newswire) and "5,000+ skills live" on the sell page. Treat both as unverified.
- **Source:** https://www.barchart.com/story/news/3197508/agensi-crosses-2-000-skills-three-months-after-launching-its-ai-agent-marketplace (undated)

## 6. What separates strong skills from weak ones (exemplars)

- **Rule / fact:** anthropics/skills contains docx, pdf, pptx, xlsx (Apache 2.0 per the page), plus a `template/template-skill` and a `spec/` folder. The repo says its skills are "for demonstration and educational purposes." It lists no CI for skills and no evals convention on the page. Repo has about 196k stars (page figure).
- **Why it matters for our library:** The document skills are the best public model of production-grade SKILL.md. Their value is in procedure and tooling, not prose. Read them before writing ours. Check each folder's licence before reuse.
- **Source:** https://github.com/anthropics/skills (undated; fetched 2026-11-17)

- **Rule / fact:** obra/superpowers (MIT) ships about 20 workflow skills (test-driven-development, systematic-debugging, verification-before-completion, writing-plans, requesting-code-review, subagent-driven-development, writing-skills, etc.). It ships plugin manifests for Claude Code, Cursor, Codex, and Gemini. Skill-behaviour tests use a separate eval harness (`superpowers-evals`), not a unit test. Installable via `/plugin install superpowers@claude-plugins-official`.
- **Why it matters for our library:** Strongest public evidence that skills can be multi-harness and tested. Its workflow-gate style (verify before claiming done) is the model for our finish checks. We did not confirm its internal SKILL.md structure (the page did not show it). Read `skills/writing-skills/SKILL.md` directly before copying the style.
- **Source:** https://github.com/obra/superpowers (undated; about 318k stars per page)

- **Rule / fact:** Patterns the official docs endorse as high quality: gotchas sections, concrete templates, checklists with validation gates, scripts for fragile steps, and a single default with an escape hatch.
- **Why it matters for our library:** These are the testable features our checker can score: presence of a gotcha list, a pass/fail checklist, a validator script, and no "see docs" filler.
- **Source:** https://agentskills.io/skill-creation/best-practices (undated)

- Other repos named in the brief (anti-ui-slop, Impeccable, taste-skill, awesome-copilot, humanizer variants): UNVERIFIED. Not fetched in this pass. Gap to close before we claim what they get right or wrong.

## 7. Checker and judge agents

- **Rule / fact:** Self-preference bias is real in rubric-based grading. Pombal, Rei and Martins (April 2026) study judges giving binary yes/no verdicts per rubric item. They find judges systematically favour their own outputs. Ensembling several judges reduces this but does not remove it. They also give rubric-design guidance (details UNVERIFIED; read the paper).
- **Why it matters for our library:** A fixer must not grade its own fix. Use a separate fresh-context checker, and do not use the same model family as the judge for any score we publish.
- **Source:** https://arxiv.org/pdf/2604.06996 (April 2026; from search snippets, not fully read)

- **Rule / fact:** Li et al. (Ant Group, arXiv 2506.22316, 2025) show LLM judges shift scores when rubric order, score IDs, or reference answers change. They recommend robust scoring-prompt design.
- **Why it matters for our library:** Keep rubric order fixed and identical across runs. Use score labels with words, not bare numbers, and rerun with shuffled criteria to test stability.
- **Source:** https://arxiv.org/html/2506.22316v3 (2025; from search snippets)

- **Rule / fact:** Pattern for a deterministic-plus-model checker: scripts catch what regex can (banned phrases, em-dash counts, line length, pattern counts). The model judges what needs reading (tone, specificity, invented claims). Output is structured JSON with rule ID, line, evidence quote, and severity.
- **Why it matters for our library:** Scripts give stable numbers across runs. The model adds judgment only where scripts cannot.
- **Example or pattern:** `{"rule":"generic-opener","line":3,"quote":"In today's fast-paced world","severity":"high"}`
- **Source:** Derived from https://agentskills.io/skill-creation/best-practices (undated) and the scripts pattern above. Pattern, not a cited benchmark.

- **Rule / fact:** Fixer loop stop conditions should be explicit: max N iterations, stop when the checker score stops improving, stop when the diff touches files outside scope. Validation must run after each edit.
- **Why it matters for our library:** Without a cap, fixer loops burn tokens and drift.
- **Source:** Pattern from the validation-loop guidance at https://agentskills.io/skill-creation/best-practices (undated). Specific caps are our design choice.

## 8. Packaging, licensing, repo hygiene

- **Rule / fact:** Anthropic repo licences are per skill; many are Apache 2.0, and each folder must be checked. Superpowers is MIT.
- **Why it matters for our library:** Use MIT for the library for maximum reuse. Put `license:` in each SKILL.md frontmatter, since the spec allows it.
- **Source:** https://github.com/anthropics/skills ; https://github.com/obra/superpowers (undated)

- **Rule / fact:** `plugin.json` `version` is pinned by value; `repository`, `homepage`, `license` (SPDX) and `keywords` are standard fields.
- **Why it matters for our library:** Use semver tags (v1.2.0) and a CHANGELOG. Bump `version` in plugin.json with every tag.
- **Source:** https://code.claude.com/docs/en/plugins-reference (undated)

- **Rule / fact:** Recommended CI for skill repos: `skills-ref validate` for every skill, `claude plugin validate --strict` for the plugin, a line-count gate (SKILL.md under 500 lines, our target about 150), a check that `name` equals the folder name, and a check that no SKILL.md links to a missing reference.
- **Why it matters for our library:** These are cheap, deterministic, and catch the bloat and broken-link problems the owner complained about.
- **Source:** Built from https://agentskills.io/specification and https://code.claude.com/docs/en/plugins-reference (undated). CI shape is our proposal.

## 9. Gaps (not answered in this pass)

- Impeccable, taste-skill, anti-ui-slop, awesome-copilot, humanizer forks: no source fetched. No claim made about them.
- SkillsMP, Smithery, PromptBase-style marketplaces and what sells: not searched.
- agentskills.io evaluation pages (evaluating-skills, optimizing-descriptions) and skill-creator guidance: linked, not read.
- OpenAI Custom GPT knowledge-file limit: unresolved; OpenAI Help Center returned 403.
- Full text of the 2026 self-preference paper and the 2025 scoring-bias paper: only snippets read.
- All Anthropic and OpenAI docs pages are undated in fetched form. Treat them as current as of 2026-11-17, not as dated releases.
