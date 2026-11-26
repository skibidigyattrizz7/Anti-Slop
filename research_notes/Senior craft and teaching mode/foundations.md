# Foundations: building anti-slop on existing skills

Date: 2026-11-26. Docs below were fetched from code.claude.com (".md" versions of each page) and raw.githubusercontent.com. Local paths: `S` = `/root/.claude/skills/synced/d13e5c22-.../`, `P` = `/root/.claude/plugins/synced/d13e5c22-.../`. Note: `human-*`, `real-reports`, `own-voice`, `build-logs`, `unslop-prompting` in `S` are the owner's own skills (the anti-slop library itself), not third-party.

## 1. What Claude Code and Agent Skills officially support for composition

### Takeaway
There is one real, documented dependency feature: plugin-to-plugin `dependencies` in `plugin.json`. Skill-to-skill calls have no dedicated syntax; they work through plain-text instructions, the Skill tool, subagent preloading and `context: fork`. The binding limit is the skill listing budget (1% of context window, 1,536 chars per description).

### Cited findings
- **Plugin dependencies exist.** `plugin.json` takes `"dependencies": ["name", "name@marketplace", {"name","marketplace","version"}]`; a dependency is a plugin that "must be enabled for this one to work". Bare names resolve in the declaring plugin's marketplace. — [plugins-reference](https://code.claude.com/docs/en/plugins-reference.md)
- Version constraints are semver ranges (`~2.1.0`, `^2.0`) resolved against git tags named `<plugin-name>--v<version>`; `claude plugin tag --push` creates them. Without a constraint the dependency tracks whatever its marketplace publishes. Dependencies auto-install (needs Claude Code v2.1.319+). — [plugin-dependencies](https://code.claude.com/docs/en/plugin-dependencies.md)
- **Cross-marketplace dependencies are blocked by default.** The root marketplace must list the target in `allowCrossMarketplaceDependenciesOn`; the check is skipped if the user already enabled that plugin at the same scope. — [plugin-dependencies](https://code.claude.com/docs/en/plugin-dependencies.md)
- A plugin whose manifest has only `name` and `dependencies` is a valid "bundle" plugin. — [plugin-dependencies](https://code.claude.com/docs/en/plugin-dependencies.md)
- **Plugin layout:** manifest at `.claude-plugin/plugin.json`; `skills/<name>/SKILL.md`, `agents/`, `hooks/`, `output-styles/` at plugin root. The `skills` key accepts extra directories and `"."`, and adds to the default `skills/` scan. `${CLAUDE_PLUGIN_DATA}` survives updates. — [plugins-reference](https://code.claude.com/docs/en/plugins-reference.md)
- **Listing budget.** Every skill name is always listed; descriptions are dropped to fit "1% of the model's context window", least-invoked skills first. `description` + `when_to_use` are capped at 1,536 chars per entry (`skillListingMaxDescChars`). Raise with `skillListingBudgetFraction` or `SLASH_COMMAND_TOOL_CHAR_BUDGET`; set low-priority skills to `"name-only"` in `skillOverrides`. `/doctor` estimates listing cost, `/skill-doctor` finds unused skills. — [skills](https://code.claude.com/docs/en/skills.md)
- `disable-model-invocation: true` removes a skill from Claude's context entirely (description not listed) and also stops it being preloaded into subagents. `user-invocable: false` hides it from the `/` menu but Claude can still call it. — [skills](https://code.claude.com/docs/en/skills.md)
- **Subagents load skills.** A subagent's `skills:` frontmatter preloads the full skill content at startup; it can still invoke unlisted skills through the Skill tool. — [sub-agents](https://code.claude.com/docs/en/sub-agents.md)
- **`context: fork` + `agent:`** runs a skill in a fresh subagent that sees SKILL.md as its prompt but not the conversation. It only makes sense for skills with an explicit task, not for guideline-only skills. — [skills](https://code.claude.com/docs/en/skills.md)
- **Hooks inject context.** `SessionStart`, `SubagentStart`, `UserPromptSubmit` stdout or `hookSpecificOutput.additionalContext` enters Claude's context; the string is capped at 10,000 characters; several hooks' values all arrive. — [hooks](https://code.claude.com/docs/en/hooks.md)
- **Output styles** replace parts of the system prompt; plugins can ship them in `output-styles/`; `force-for-plugin: true` applies one whenever the plugin is enabled; `keep-coding-instructions: true` keeps coding behaviour. — [output-styles](https://code.claude.com/docs/en/output-styles.md)
- **Open spec rules:** `description` max 1,024 chars (spec) vs 1,536 listing cap (Claude Code); `license` field is "name or reference to a bundled license file"; keep SKILL.md under 500 lines, instructions under ~5,000 tokens, and "keep file references one level deep from SKILL.md". — [Agent Skills specification](https://agentskills.io/specification)
- Skills synced from claude.ai live under reserved `anthropic-skills:`; plugin skills are namespaced `plugin:skill`. — [skills](https://code.claude.com/docs/en/skills.md)

### Inferences
- A skill can name another skill in prose ("if `impeccable` is available, run its `critique` flow") and Claude may invoke it via the Skill tool, but the docs describe no guaranteed "if installed" check. Treat every such pointer as best-effort with a built-in fallback.
- Plugin dependencies only help if our library and the base skill are in the same marketplace, or the root marketplace allowlists the other one. A cross-marketplace base skill (Impeccable, superpowers) cannot be a hard dependency of a plugin in our marketplace without the allowlist, and the user would still have to add that marketplace.
- 12 skills + 10 agents is small, but this machine lists ~300 skills; our descriptions must be short and front-loaded to survive truncation.

### Gaps
- Docs do not say what happens when a prose-referenced skill is missing, or whether the Skill tool can call a skill that is not model-invocable. Not tested here.
- Did not open the plugins/components or marketplace-reference pages in full; dependency-version resolution edge cases are unverified.

## 2. How the best multi-skill libraries compose

### Takeaway
Three working patterns: a mandatory meta-router loaded first (superpowers), a single skill with a command table that forces reading one reference file per command (Impeccable), and a marketplace of many small plugins each with its own skills (wshobson, anthropics). None relies on hard cross-skill dependencies.

### Cited findings
- **superpowers `using-superpowers`:** a short router skill ("Use when starting any conversation") that tells the model to invoke any possibly-relevant skill before any response, with a rationalization table ("This is just a simple question" -> "Questions are tasks"), a priority rule (process skills first, then implementation skills like frontend-design), a `<SUBAGENT-STOP>` block so dispatched subagents ignore it, and per-harness reference files. License MIT, "Copyright (c) 2025 Jesse Vincent". — [SKILL.md](https://raw.githubusercontent.com/obra/superpowers/main/skills/using-superpowers/SKILL.md), [LICENSE](https://raw.githubusercontent.com/obra/superpowers/main/LICENSE)
- **Impeccable** (local copy `S/impeccable/SKILL.md`, 168 lines, 26 reference files): one skill with an `argument-hint` of sub-commands; a table maps each command (`craft`, `shape`, `critique`, `audit`, `polish`, `harden`, `animate`...) to `reference/<command>.md`, and the body says "you MUST read `reference/<command>.md` next. Non-optional." It also runs a context script once per session and reads a register reference (brand vs product). Frontmatter `license: Apache 2.0`. The upstream repo's LICENSE is Apache 2.0 and its NOTICE-style file credits MIT-licensed sources it distilled (ehmo/platform-design-skills) with original URL, license and author. — [LICENSE](https://raw.githubusercontent.com/pbakaus/impeccable/main/LICENSE), [NOTICE.md](https://raw.githubusercontent.com/pbakaus/impeccable/main/NOTICE.md)
- **anthropics/skills:** flat folder of independent skills, installed as marketplace plugins (`document-skills`, `example-skills`). README: many skills are Apache 2.0, and the docx/pdf/pptx/xlsx skills are also Apache 2.0 in this repo. Each skill folder carries its own LICENSE.txt. Locally, `skill-creator`, `pdf` and `learn` carry Apache text; `built-in-browser`, `chrome-browser`, `computer-use` carry "All rights reserved" proprietary text. — [README](https://raw.githubusercontent.com/anthropics/skills/main/README.md), `S/built-in-browser/LICENSE.txt`
- **wshobson/agents:** MIT (Copyright 2024 Seth Hobson). Marketplace of 93 plugins (199 agents, 185 skills, 103 commands per README), each plugin a focused bundle; `marketplace.json` lists plugins with `source: ./plugins/<name>`. Composition is by installing several small plugins, not by dependencies. — [README](https://raw.githubusercontent.com/wshobson/agents/main/README.md), [marketplace.json](https://raw.githubusercontent.com/wshobson/agents/main/.claude-plugin/marketplace.json), [LICENSE](https://raw.githubusercontent.com/wshobson/agents/main/LICENSE)
- **Sibling routing in the wild (local):** `S/threejs-game-director` is an "entrypoint" that routes to sibling skills (`threejs-gameplay-systems`, `-aaa-graphics-builder`, `-game-ui-designer`, `-debug-profiler`) and tells the model to resolve them through `../<skill>/SKILL.md`, falling back to a repo `skills/` directory. Note it names `threejs-qa-release` and `threejs-3d-generator`, which are not installed locally, so graceful degradation is needed.
- **Local ziad-skills `using-agent-skills`** (192 lines): meta-skill with a discovery flowchart that maps engineering phases to skills; `P/ziad-skills/skills/`.

### Inferences
- The strongest pattern for us is Impeccable's: one visible skill per area, a command or "Read when" table, and mandatory read of exactly one reference. That matches our BUILD_SPEC "Read when" tables already.
- A superpowers-style always-on router would cost listing budget and fights "plain words trigger the skill"; our startup hook for chat already does the always-on job.

### Gaps
- Could not open superpowers' `references/claude-code-tools.md` or wshobson plugin internals in detail. How superpowers handles skills across plugins beyond its own router is unverified.

## 3. Licensing for reusing text in an MIT library

### Takeaway
MIT and Apache 2.0 both allow copying and adapting into an MIT repo if you keep the notice. No license means all rights reserved: link, do not copy.

### Cited findings
- **MIT:** permission is granted free of charge to use, copy, modify, merge, publish, distribute and sublicense, subject to one condition: the copyright notice and permission notice must be included in "all copies or substantial portions" (text of LICENSE files above, e.g. [superpowers](https://raw.githubusercontent.com/obra/superpowers/main/LICENSE)).
- **Apache 2.0, section 4:** you must give recipients a copy of the License; mark modified files with prominent notices that you changed them; keep copyright, patent, trademark and attribution notices from the source; and if the Work has a NOTICE file, include its readable attribution content in a NOTICE file, in documentation, or in a display your work shows. The NOTICE text "does not modify the License". — [Apache License 2.0 text](https://www.apache.org/licenses/LICENSE-2.0.txt)
- Apache 2.0 includes an express patent grant; MIT does not. A mixed MIT repo can contain Apache-licensed files if those files keep their license and notice.
- **Agent Skills `license` field** accepts a license name or a bundled license file reference. — [spec](https://agentskills.io/specification)
- **Precedent for credit:** Impeccable keeps a `NOTICE.md` titled "Third-Party Notices" with original work, URL, license and author per source. Our README already credits humanizer (MIT) in a "Credits and license" section.
- **No license file = default copyright:** nobody may copy or adapt. (General law, not a cited source; unverified for any specific jurisdiction.) Several local skills have no LICENSE and no `license:` field: `arena`, `do-competitively`, `skill-doctor`, `teach`, `emil-design-eng`, `apple-design`, `animation-forge`, `human-*` (owner's own), and the whole `ziad-skills` plugin (no LICENSE at plugin root).
- Local license inventory (head of each file): MIT: superpowers-derived `systematic-debugging`, `verification-before-completion`, `writing-plans` (Jesse Vincent), `design-taste-frontend` (Leonxlnx), `ui-ux-pro-max` (Next Level Builder), `motion-design` (LottieFiles), `gsap-*` (GreenSock), `threejs-*` (Majid Manzarpour), `anatomy` (Ryan), `ponytail` (DietrichGebert), `humanizer`, `chief-of-staff`, `i-have-adhd`, `last30days`, `blender-image-to-3d`. Apache 2.0: `impeccable`, `skill-creator`, `learn`, `pdf`, `game-feel`, `algorithmic-art`, `canvas-design`, `mcp-builder`. Proprietary: `built-in-browser`, `chrome-browser`, `computer-use`.

### Inferences
- Copy-with-credit is safe only for MIT/Apache items. For everything else, link or write our own words from the idea (ideas and methods are not copyrightable; the exact text is).
- For adapted Apache text: keep the original header, add "Modified by anti-slop" notes in the file, and put the source in a root `NOTICE` file.
- The `ziad-skills` bundle is a collection of other people's skills (grill-me, code-review-and-quality, etc.) without a stated license: treat as unverified and do not copy text.

### Gaps
- I am not a lawyer; this is not legal advice. Did not check upstream repo licenses for taste-skill, game-feel, ziad-skills origin repos.

## 4. Local skill map (25 most relevant)

Rating = strength as a foundation for that area. Lines = SKILL.md length; "refs" = extra files.

| Skill (path) | Area | Rating | Lines/refs | License | Notes |
|---|---|---|---|---|---|
| impeccable (S) | UI | strong | 168 / 26 refs | Apache 2.0 | Command router, critique/audit/polish/harden/onboard flows, register split (brand vs product). Best UI base. |
| frontend-design (S, P) | UI | usable | 71 | Apache (Anthropic) | Short aesthetic-direction guide; good to point at. |
| vectorlab-ux-skills (listed) | UI | usable | many tiny | unverified | Not found on disk under `S` or `P`; unverified. |
| design (P): design-critique, accessibility-review, ux-copy | UI / review | usable | 107-128 | none at plugin root (unverified) | Structured critique, WCAG audit, microcopy. |
| emil-design-eng + review-animations (S) | UI motion | strong | 679 / 112 | none | Strong animation craft; link, do not copy. |
| motion-design, gsap-core (S) | media / UI | usable | 310, 254 | MIT | Timing and easing; official GSAP skill is MIT. |
| design-taste-frontend (S) | UI | usable | 1206 | MIT (Leonxlnx) | Huge; ban lists conflict with owner's "vibecoded" rule, so use as reference only. |
| humanizer (S) | writing | strong | 393 | MIT | Already the credited base of `human-writing` patterns. |
| doc-coauthoring (S) | writing | usable | 375 | none | Staged co-authoring workflow. |
| real-reports (S, owner's) + deep-research (S) | reports | strong | 44 / 146 | none | deep-research gives the multi-agent loop; wrap, do not copy. |
| learn (S) | teaching | strong | 78 | Apache 2.0 | Diagnose first, one step forward per turn, hold the line vs "just tell me", integrity rules. Best chat-teaching base. |
| teach (S) | teaching | strong | 139 / 6 files | none | Multi-session: mission, learning record, glossary, zone of proximal development, spaced schedule, subagents. Best course base; link or wrap. |
| human-chat (S, owner's) | chat | usable | 56 | none (own) | Our own; pair with `learn`. |
| systematic-debugging (S) | code | strong | 283 / 12 | MIT | Superpowers; root-cause method with reference files. |
| test-driven-development, code-review-and-quality, code-simplification (P ziad) | code / review | strong | 398 each | unverified | Rich, but license unknown. |
| engineering (P): code-review, testing-strategy, architecture | code / review | usable | 33-118 | unverified | Short, company-style. |
| writing-plans (S) | planning | strong | 204 | MIT | Superpowers plan format. |
| planning-and-task-breakdown, spec-driven-development, idea-refine (P ziad) | planning | usable | ~190 | unverified | |
| verification-before-completion (S) | review/testing | strong | 120 | MIT | "Run the command and read output before claiming done." Pairs with our `see-it-run`. |
| game-feel, physics-tuning, camera-systems (S) | games | strong | 159, 144, 148 | Apache / not checked | Engine-neutral techniques; game-feel is Apache. |
| threejs-game-director + 4 siblings (S) | games | strong | 85 + siblings | MIT | Best example of router plus siblings; web games only. |
| unity (P): ui, craft-game-floors, optimize-* | games | usable | per skill | Unity LICENSE.md | Engine-specific; wrap only if engine is named. |
| human-fiction, human-games, human-media (S, owner's) | fiction/games/media | usable | 43-59 | own | No strong third-party fiction base exists locally. |
| imagegen-frontend-web/mobile, brandkit, canvas-design, algorithmic-art (S) | media | usable | 129-1465 | MIT / Apache | Image-direction prompts; canvas-design and algorithmic-art are Apache. |
| dataviz (listed, system skill) + docx/pptx/xlsx/pdf (S) | reports | usable | 98-314 | Apache (pdf) | File-format tooling, not craft. |
| anti-ui-slop (P ziad) + ui-ux-pro-max (S) + taste-skill variants | UI | weak/usable | 58 / 214 | unverified / MIT | Overlap with our `human-ui`; anti-ui-slop depends on an external dataset (UIZZE). |
| ponytail (P) | code | usable | n/a | MIT | Minimal-change discipline; credit if borrowed. |

Skipped as not relevant: buildkite, datarobot, honeycomb, zapier, figma, marketing, productivity, exa, watch, cowork-plugin-management (tool-integration skills, not craft).

### Gaps
- `vectorlab-ux-skills` appears in the skill list but I found no folder for it under either directory; unverified.
- I skimmed headings and frontmatter, not bodies, for most rows. Ratings for ziad-skills items rest on size and description only.

## 5. Meta-work skills for building and testing our library

| Skill | What it offers | Use it for |
|---|---|---|
| skill-creator (S, Apache, 507 lines, `agents/`, `eval-viewer/`, `scripts/`) | Intent capture, writing guide, progressive disclosure, "principle of lack of surprise", spawn with-skill and baseline runs in the same turn, draft assertions, benchmark with variance, description optimizer | The eval loop; our `tools/run_evals.py` overlaps and could borrow its grader/agents layout with credit |
| skill-doctor (S, 152 lines, no license) | Classify a skill into 9 categories, minimal/standard/rich tier fit, structural signals script, scorecard, improve mode, batch and comparison modes; criteria from Anthropic's "Lessons from Building Claude Code: How We Use Skills" | Lint pass over all 12 skills for gotchas, size, trigger quality |
| using-agent-skills (P ziad, 192 lines) | Discovery flow from task phase to skill; meta-skill pattern | Model for a thin router if ever needed; not for copying (license unverified) |
| context-engineering (P ziad, 353 lines) | Context hierarchy, loading only what is needed, rules files | Check that references stay small and loaded on demand |
| fable-playbook (P ziad, 67 lines) | Plan, check own work, fix, report | Short checklist model for our "Final check" sections |
| do-competitively (S, 786 lines, no license) | Generate-Critique-Synthesize: meta-judge writes the spec, N generators in parallel, multi-judge scoring, synthesis | Pattern for our `judge` agent; blind multi-judge reduces noise |
| arena (S, 372 lines, `bracket.py`, `rubric.md`, `strategies.json`) | Tournament of N sub-agents with distinct strategy cards, attacker/defender rounds, per-match judge, final check | Hard-task generation for `polish`; also stress-tests rubrics |
| doubt-driven-development (P ziad, 243 lines) | Fresh-context adversarial reviewer before decisions stand | Reviewing each new category skill before merge; counter to rubric overfitting |
| verify-and-stop (P ziad, 16 lines) | Smallest sufficient proof; pass/fail/unavailable/blocked stated exactly | Template for the must-pass check wording |

### Inferences
- ROADMAP_10 problem 2 (rubrics tuned on the samples they scored) is exactly what do-competitively's "meta-judge writes the spec first, before seeing outputs" and doubt-driven's fresh-context reviewer target.
- skill-creator and skill-doctor are both strong enough that we should run them against our skills rather than rebuild their checks.

### Gaps
- I read only headings and openings; I did not run skill-doctor or skill-creator scripts.

## Recommended foundations per area

| Area | Best local skill | How to build on it |
|---|---|---|
| Code | systematic-debugging (MIT), test-driven-development, code-review-and-quality | Link for debugging and TDD ("for a bug, use systematic-debugging if present; else rule X"). Borrow structure from systematic-debugging with MIT credit; ziad skills: link only (license unverified). |
| UI | impeccable (Apache 2.0) | Wrap: `human-ui` stays the entry; add a "senior UI" reference that points to Impeccable commands (`critique`, `audit`, `polish`) with a fallback checklist. Borrow the register idea with NOTICE credit. Keep the owner's "vibecoded" list authoritative. |
| Writing | humanizer (MIT) | Already borrowed with credit. Add doc-coauthoring as a link for long docs. |
| Chat | learn (Apache 2.0) + human-chat | Wrap: chat-teaching moves (diagnose, one step per turn, hold the line) as a reference in `human-chat`; credit Apache source in NOTICE if text is adapted. |
| Fiction | none strong | Build our own; no third-party base found locally. |
| Media | motion-design, gsap-core (MIT), canvas-design (Apache) | Link for motion timing; keep `human-media` as the craft entry. |
| Games | game-feel (Apache), physics-tuning, camera-systems; threejs-game-director (MIT) | Link by name for feel, physics, camera; borrow router layout from threejs-game-director with credit; engine-specific work stays in Unity or Three.js skills. |
| Reports | deep-research + real-reports | Wrap: `real-reports` sets the rules, deep-research runs the loop when subagents exist. |
| Planning | writing-plans (MIT) | Borrow the plan format with credit; link planning-and-task-breakdown. |
| Review and testing | verification-before-completion (MIT), do-competitively, doubt-driven-development | Borrow the "run it, read the output" rule with credit; wrap judge multi-run in `polish`; link the others. |
| Teaching (course mode) | teach (no license) + learn (Apache) | Link `teach` for multi-session courses (mission, learning record); wrap `learn` rhythm for single-turn tutoring. Do not copy `teach` text. |

## Composition rules for our library

1. **Each skill works alone.** Pointers to other skills are one line in "Read when" with a fallback rule inline ("if impeccable is available use `critique`; otherwise run rubric U1-U6"). Docs give no "if installed" check, so never depend on the pointer.
2. **No hard plugin dependencies on third-party skills.** `dependencies` only works inside one marketplace or with `allowCrossMarketplaceDependenciesOn`. If we ever split into `anti-slop-core` and `anti-slop-extras`, use a bundle plugin whose manifest is only `name` + `dependencies` and tag releases `<name>--v<version>`.
3. **One entry skill per area, commands in a table.** Follow Impeccable: a table maps each sub-task to exactly one `references/<name>.md`; say "read it" in imperative form. Keep references one level deep (spec rule), each under about 900 words (our own rule).
4. **Keep descriptions short and front-loaded.** The listing is capped at 1,536 chars per entry and 1% of context across all skills; ours are already under 600. New senior-craft or teaching skills must justify listing space; use `disable-model-invocation: true` for rarely wanted commands (for example `polish`) so they cost no listing space.
5. **Copy only MIT or Apache text, and credit it at the file and repo level.** Add a root `NOTICE` (Impeccable-style: work, URL, license, author) and a one-line source comment in each adapted reference. For Apache sources also mark the file as modified and keep the original notice. Unlicensed skills (teach, arena, do-competitively, skill-doctor, ziad-skills) are link-only.
6. **Router skills are optional and thin.** A superpowers-style always-on router costs context every turn; keep the existing startup hook for chat and the `planner` agent for big jobs. If a router is added, give it a `<SUBAGENT-STOP>`-style guard so specialists do not reload it.
7. **Subagents load skills explicitly.** Specialists should list their skill in `skills:` frontmatter (full content injected) rather than rely on Glob discovery; use `context: fork` only for task-style skills such as `polish`, never for guideline skills.
8. **Hooks inject small rules, not libraries.** `additionalContext` is capped at 10,000 chars and arrives every session; inject the chat rules only, never craft references.
9. **Use meta skills to test, not to rebuild.** Run skill-creator evals and skill-doctor over our skills; have a fresh-context reviewer (doubt-driven pattern) and a spec-first judge (do-competitively's meta-judge) write rubrics before seeing outputs.
10. **Degrade on missing siblings.** threejs-game-director names two siblings that are not installed here. Every cross-reference gets a "if absent" line, and `tools/check_repo.py` should flag any named skill that has no fallback.
