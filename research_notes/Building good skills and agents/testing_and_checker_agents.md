# Testing skills and building checker/fixer agents: research notes

Fetched 2026-11-17. Not repeated from the earlier notes: SKILL.md format, progressive disclosure, subagent frontmatter, plugin layout, Pombal 2026 self-preference and Li et al. 2025 rubric-order findings. Items marked UNVERIFIED came from search snippets or were not fetched. Several sources are secondary summaries; these are flagged.

## Skill evals: with-skill vs baseline

- **Rule / method:** Run each test prompt twice: with the skill, and without it (or with the previous version, snapshotted first). Store results per iteration (`iteration-N/eval-X/with_skill/` and `without_skill/`, each with `outputs/`, `timing.json`, `grading.json`), then aggregate into `benchmark.json`. Start with 2-3 prompts and expand later.
- **Why it matters for our checker/fixer/skills:** This answers the owner's core complaint directly: "does the skill change output at all?" If `without_skill` passes the same assertions, the skill adds nothing and should be cut. Our library needs the same baseline run for every skill.
- **Concrete example or pattern:** Benchmark JSON reports `pass_rate` mean and stddev per configuration, plus `delta` (pass rate, time, tokens). The page's example: pass-rate delta +0.50 for +13 s. Its own rule: a skill that doubles tokens for a 2-point gain "might not" be worth it.
- **Source:** https://agentskills.io/skill-creation/evaluating-skills (page `dateModified` 2026-03-16)

- **Rule / method:** Sample size guidance is weak in the source. It says to start with 2-3 cases and run single runs early. Stddev is "only meaningful with multiple runs per eval." No minimum N is given.
- **Why it matters:** We have no published N for a skill. Use multiple runs per prompt before trusting a delta. Our own choice of N is a gap to decide.
- **Source:** https://agentskills.io/skill-creation/evaluating-skills (2026-03-16). Gap: no minimum run count given.

- **Rule / method:** Analyze assertions after each run, not just totals:
  - Drop assertions that pass in both configurations (they inflate the with-skill score).
  - Fix assertions that fail in both (broken assertion, or the test is too hard).
  - Study assertions that pass only with the skill. Those show where the skill adds value.
  - Read transcripts when stddev is high. High variance usually means ambiguous instructions.
- **Why it matters:** This is the direct test for "skill does nothing." A checker that passes both arms is useless. Our checker's rules should each show a with/without difference.
- **Concrete example or pattern:** An assertion "Both axes are labeled" that passes in both arms should be removed, not counted as skill value.
- **Source:** https://agentskills.io/skill-creation/evaluating-skills (2026-03-16)

- **Rule / method:** Assertions must be objective and checkable. Good: "The output file is valid JSON", "includes at least 3 recommendations". Weak: "The output is good". Too brittle: exact phrase matching. Style and "feels right" are left to human review. Grading requires a concrete quote as evidence for PASS, with no benefit of the doubt. Mechanical checks use scripts, not LLM judgment.
- **Why it matters:** This gives a rule for which checks belong in code (our word lists, counts, line lengths) and which need the model (tone, specificity). It also sets the PASS-needs-evidence rule for our checker output.
- **Concrete example or pattern:** `{"text": "Both axes are labeled", "passed": false, "evidence": "Y-axis is labeled 'Revenue ($)' but X-axis has no label"}`
- **Source:** https://agentskills.io/skill-creation/evaluating-skills (2026-03-16)

- **Rule / method:** Blind pairwise comparison for two skill versions: show both outputs to a judge without labels, and score holistic quality. Use it alongside assertions, since two outputs can both pass every assertion and still differ in quality.
- **Why it matters:** Our slop checker can pass a text that is still bland. Blind A/B against the no-skill output catches this.
- **Source:** https://agentskills.io/skill-creation/evaluating-skills (2026-03-16)

- **Rule / method:** Human review produces a per-case `feedback.json`. The page calls "the chart is missing axis labels" actionable and "looks bad" not. Empty feedback means the case passed review.
- **Why it matters:** Our fixer should be fed specific complaints, not general unhappiness.
- **Source:** https://agentskills.io/skill-creation/evaluating-skills (2026-03-16)

- **Rule / method:** skill-creator automates this loop (run evals, grade assertions, aggregate benchmarks, present for review). The GitHub page 403'd for us, so its contents are UNVERIFIED beyond the link on agentskills.io.
- **Source:** https://github.com/anthropics/skills/tree/main/skills/skill-creator (fetch returned 403; UNVERIFIED). Linked from https://agentskills.io/skill-creation/evaluating-skills

## Judge design: binary checks vs scales

- **Rule / method:** Use binary pass/fail per criterion, not 1-5 scales. Reason given: scores like 3 vs 4 are undefined, so teams disagree. Pass/fail lets you explain each verdict with a critique. Hamel also reports that domain-expert scores on such scales often do not correlate with the metrics built on them.
- **Why it matters:** This supports a checklist-style checker: each anti-slop rule is one yes/no with evidence, and the score is the count. It avoids the fake precision of "7/10".
- **Concrete example or pattern:** Per-rule verdict with a critique, e.g. "It failed to offer empathetic support or additional assistance." Hamel says a critique must be detailed enough that "a new employee could understand it."
- **Source:** https://hamel.dev/blog/posts/llm-judge/ (published 2024-10-29; modified 2026-09-01). Note: published before 2025; treat its advice as "possibly outdated" for model specifics, but the method is still standard.

- **Rule / method:** Label about 100 examples per failure mode, with enough Pass and Fail cases to measure both classes. Below about 60 examples, Hamel says confidence intervals are often too wide. Measure the judge with true-positive and true-negative rates, because raw agreement "can be misleading when failures are rare."
- **Why it matters:** Our checker needs a labelled set of human-written slop vs craft text. Without it, we cannot say whether the checker is accurate. Rare tells (the failures) make plain agreement look good when the checker is useless.
- **Source:** https://hamel.dev/blog/posts/llm-judge/ (2024-10-29; modified 2026-09-01)

- **Rule / method:** Common judge-prompt mistakes Hamel lists: no critiques; terse critiques; no external context; no diverse examples. He says most fixes come from adding good examples.
- **Why it matters:** Our checker prompt needs example findings for each rule (a flagged example and a passing example), not just the rule name.
- **Source:** https://hamel.dev/blog/posts/llm-judge/ (2024-10-29; modified 2026-09-01)

- **Rule / method:** Pairwise comparison is more stable than direct scoring for subjective qualities (tone, coherence, persuasiveness). Direct scoring suits objective checks (faithfulness, policy violation). Some criteria, like instruction-following, do not fit pairwise at all. Metrics: Cohen's kappa for agreement with chance removed (his bands: 0.21-0.40 fair, 0.41-0.60 moderate); Kendall tau or Spearman rho for ranking.
- **Why it matters:** Use direct per-rule checks for the checker. Use pairwise (blind) only for "is version B better than A," which is the fixer's acceptance test.
- **Source:** https://eugeneyan.com/writing/llm-evaluators/ (page's date not shown in the fetched text; the post is long-form and drawn from "two dozen papers"). Partially read: the bias and fine-tuning sections were not fetched.

- **Rule / method:** Zheng et al. (MT-Bench / Chatbot Arena) document position bias (judges favor the first-listed answer), verbosity bias, and self-enhancement bias (judges favor their own model's outputs). GPT-4 judges reached over 80% agreement with human preferences in their study. Mitigation: swap positions and average.
- **Why it matters:** The checker and fixer must not be the same model in the same context, and the checker must run with the candidate order swapped when comparing two texts. The 2023 paper is older than 2025 and is "possibly outdated" for model details, but the bias taxonomy is still the reference.
- **Source:** https://arxiv.org/abs/2306.05685 (2023; NeurIPS 2023 Datasets and Benchmarks). The bias wording and the 80% figure come from a secondary summary (emergentmind.com) and search snippets; the arXiv abstract itself was not fetched (UNVERIFIED for exact numbers).

- **Gap:** G-Eval (Liu et al.), Prometheus, and their 2025-2026 follow-ups were not searched or fetched in this pass. Do not cite them as verified.

## Deterministic checks plus model judgment

- **Rule / method:** Vale is a Go CLI linter for prose, MIT-licensed. Rules are YAML "extension points" in a `.vale.ini` config. The docs list these check types: existence, substitution, occurrence, repetition, consistency, conditional, capitalization, metric, readability, spelling, sequence, script. Each rule has `level` (`error` fails CI). Rules are scope-aware: code and inline code are ignored by default, and rules can target headings only.
- **Why it matters:** This is the closest existing model for our banned-pattern layer. A "substitution" rule for tells, a "repetition" rule for repeated sentence openers, and a "metric" rule for sentence-length spread are all already defined types. We can reuse the shape and use `level: error` for the CI gate.
- **Concrete example or pattern:** A `substitution` rule with `swap:` pairs and `message: Use '%s' instead of '%s'.`, with `ignorecase: true`, `level: error`.
- **Source:** https://vale.sh/docs/ (page date not shown; "last updated 3 months ago" relative to fetch). Check types list from the docs table of contents; the substitution example is from the docs introduction.

- **Rule / method:** `impeccable detect` (Paul Bakaus, Apache-2.0) is a deterministic scanner that needs no LLM or API key. It runs regex and CSS-parsing rules on a directory, HTML file, or URL, and reportedly emits machine-readable output with exit codes for PR checks.
- **Why it matters:** It is a working example of the split we want: rules that can be computed run in code, and a separate LLM review handles the rest. Its own page reportedly separates deterministic rules from an LLM-based critique command.
- **Concrete example or pattern:** Rules for side-tab borders, purple gradients, bounce easing, and dark glows (listed in secondary summaries).
- **Source:** https://seunghyeonlab.blogspot.com/2026/05/impeccable-design-linter-that-catches.html (blog, 2026-05; secondary). The project's own slop page was not fetched. Rule counts conflict across sources (24, 37, 44, 46; the project page reportedly says 25 deterministic); treat counts as UNVERIFIED and check the repo before citing. Repo not fetched (GitHub returned 403 for the path we tried).

- **Rule / method:** Hamel's and Eugene's guidance both point to the same split: use code where a rule is objective (counts, banned strings, line length, whether a required section exists), and the model only where a judgment is needed. Eugene's direct-scoring guidance for "objective assessments" supports this.
- **Why it matters:** Deterministic checks give stable numbers across runs, which makes the fixer loop measurable. Put word lists and statistics in a script, and have the model read only the flagged lines.
- **Source:** https://eugeneyan.com/writing/llm-evaluators/ (date not shown); https://agentskills.io/skill-creation/evaluating-skills (2026-03-16)

- **Gap:** Sentence-length variance, contrast-ratio checks, and any published "AI tell" statistics were not verified. Do not claim a threshold for burstiness or a specific sentence-variance cut-off without a source.

## Fixer loops and failure modes

- **Gap:** No primary source was found in this pass for fixer-loop design: generate-check-fix-recheck stop conditions, diff-based minimal edits, or voice preservation. The earlier notes' stop-condition advice is our own design, not a cited benchmark. Needs a separate search.

- **Rule / method (inference, not a source):** Vale's model suggests a banned-word problem: a substitution rule that swaps "delve" for another stock word creates a new tell. Mitigation: the checker should score patterns (opener shapes, repeated structures, count of hedges) rather than single words, and the word list should carry a date and a version.
- **Why it matters:** This addresses the "whack-a-mole" risk the owner raised. We have no published evidence for the claim, so it stays a design hypothesis to test with before/after fixtures.
- **Source:** Inference from the Vale substitution model (https://vale.sh/docs/). Not verified against any study.

- **Rule / method (from Hamel):** Re-run the judge calibration "whenever something material changes," such as a model update. The process "never truly ends."
- **Why it matters:** Our checker's word lists and judge prompt need a re-validation step on a schedule and when the target model changes. Dated tells and a changelog follow from this.
- **Source:** https://hamel.dev/blog/posts/llm-judge/ (2024-10-29; modified 2026-09-01)

## Packaging and CI for evals

- **Rule / method:** Store test cases in `evals/evals.json` inside the skill folder: `prompt`, `expected_output`, optional `files`, and `assertions` added after the first run. Keep iteration folders in a sibling workspace directory.
- **Why it matters:** This is a concrete repo layout for "eval prompts folder with fixtures." Before/after fixtures can sit in `files/` and be run with the same harness.
- **Source:** https://agentskills.io/skill-creation/evaluating-skills (2026-03-16)

- **Rule / method:** Assertion checks that can be scripted should be scripts (valid JSON, row count, file exists). These can run in CI on every change, while model-graded assertions run only on demand because they cost tokens.
- **Why it matters:** Cheap deterministic CI on each push; costly eval runs only before a release. This matches the owner's token-saving rule.
- **Source:** https://agentskills.io/skill-creation/evaluating-skills (2026-03-16); the CI split is our inference.

## Gaps summary (not verified in this pass)

- promptfoo, Inspect AI, OpenAI Evals: not searched. No claims made.
- G-Eval, Prometheus, and 2025-2026 judge follow-ups: not fetched. Only Zheng et al. (2023) and Pombal 2026 (earlier notes, snippets) are referenced.
- Anthropic skill-creator source: GitHub returned 403; UNVERIFIED.
- Fixer-loop literature and stop-condition evidence: none found.
- Anti-slop word lists and tell-specific statistics (sentence-length variance, contrast checks): none verified.
- Eugene Yan's post and Vale's docs were read in part only (page dates not shown).
