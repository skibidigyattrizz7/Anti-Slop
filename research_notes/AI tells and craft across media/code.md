# AI-made code: tells, failure modes, and craft

Sourcing note: "Source: none" means I could not verify a citation this session. Those entries are general engineering practice and need a check before they go into a skill. Search hit rate limits twice; the slopsquatting and Ghostty claims are from fetched or abstract text only.

## Key question 1: Tells and failure patterns

### Takeaway
AI code fails less by being visibly wrong than by being plausible, repetitive and unowned. The measurable damage shows up as duplication, churn and security holes. The visible tells are mostly signs that nobody read the diff.

### Cited Findings

- **Tell: Copy-paste duplication instead of reuse.** Cloned (copy/pasted) lines rose from 8.3% of changed lines in 2021 to 12.3% in 2024. Moved (refactored) lines fell from 25% to under 10% over the same period. Sample: 211M changed lines, Jan 2020 to Dec 2024. Why it matters: duplicate logic drifts apart and every fix must be made N times. Fix: search the codebase for an existing helper before writing one; extract on the third copy, not the first. Source: [GitClear 2025 AI Copilot Code Quality](https://www.gitclear.com/ai_assistant_code_quality_2025_research), 2025. Model era: 2020–2024 code, pre-agentic tools. Note: a secondary write-up claims "4x" clone growth; the page's own figures show about 1.5x, so use 8.3% to 12.3%.

- **Tell: Security flaws in generated code.** Veracode tested about 80 coding tasks across 100+ LLMs; output introduced OWASP Top 10 flaws in 45% of cases. Java above 70%; Python, C# and JavaScript 38–45%. Models missed XSS in 86% and log injection in 88% of cases. Fix: treat input handling, output encoding and auth as review hot spots; run SAST in CI. Source: [Veracode 2025 GenAI Code Security Report](https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/), 30 Jul 2025. Caveat: vendor research, and the test design is a curated task set, so it is a strong signal, not a population rate.

- **Tell: Hallucinated packages ("slopsquatting").** In Spracklen et al., 576,000 samples across 16 models and Python/JS. Hallucinated-package rates were reported as at least 5.2% for commercial models and 21.7% for open-source, with 205,474 unique fake names. Attackers can register those names. Fix: verify every new dependency exists, is maintained, and is the one you meant (check the registry, age, downloads) before adding it. Source: [arXiv:2406.10279](https://arxiv.org/abs/2406.10279), first posted June 2024, USENIX Security 2025 version. Possibly outdated: model era is 2023–2024 models. The abstract numbers differ between versions; cite the version you use.

- **Tell: Confident maintainer-facing slop.** curl ended its HackerOne bug bounty at the end of January 2026 after floods of AI-generated, unreproduced reports. Stenberg: the goal was to "remove the incentive for people to submit crap and non-well researched reports… AI generated or not." His rule: never report a bug you do not understand and cannot reproduce. Fix: reproduce first, state what you tested, and say what you could not verify. Source: [The Register, 21 Jan 2026](https://www.theregister.com/2026/01/21/curl_ends_bug_bounty/). Note: slop-share figures (about 20%) and a later "stopped accepting reports" claim come only from blogs; unverified.

- **Tell: Slower, not faster, on real work (perception gap).** In METR's RCT, 16 experienced open-source developers on 246 real issues were 19% slower with AI allowed. They predicted a 24% speedup and still believed afterward they were about 20% faster. Why it matters: "it feels fast" is not evidence. Fix: measure the time to a verified, merged change, not time to first draft. Source: [METR, 10 Jul 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/). Possibly outdated: early-2025 tools (Claude 3.5/3.7 Sonnet, Cursor). METR says it has newer data from Feb 2026, which I did not fetch.

- **Tell: Over-commenting that restates the code.** `// increment counter` above `count += 1`; docstrings that repeat the signature. Why it reads as AI: comments describe what, add length, and rot. Fix: delete any comment that a reader could get from the code. Keep only the why (a constraint, a workaround, a non-obvious invariant). Source: [Google eng practices, "Comments"](https://google.github.io/eng-practices/review/reviewer/looking-for.html). Possibly outdated page, but the principle is stable. Source: stated in the Google guide; the specific examples are general practice.

- **Tell: Generic names (`data`, `result`, `handler`, `utils`, `helper`, `process`).** Why: names carry no domain meaning, so a reader must open the body to learn what the value is. Fix: name by what the thing is in this domain (`invoiceLines`, `retryQueue`). Google's rule: a good name is long enough to say what the item is or does. Source: [Google eng practices](https://google.github.io/eng-practices/review/reviewer/looking-for.html). Source for the specific list: none.

- **Tell: Needless wrappers and abstraction.** A class or interface around one function; a `Manager`/`Service`/`Factory` for a single call; options and config nobody set. Why: complexity without a second use case; reviewers' main complaint. Fix: inline it. Abstract when the second real caller appears. Google: "'Too complex' usually means 'can't be understood quickly by code readers.'" Solve the problem that exists now. Source: [Google eng practices](https://google.github.io/eng-practices/review/reviewer/looking-for.html). Source for the specific examples: none.

- **Tell: Defensive try/catch and null checks everywhere.** Catch-and-log-and-rethrow; `if (x) { ... } else { return null }` on values that cannot be null; swallowed errors. Why: it hides real failures and makes the happy path hard to read. Fix: validate at trust boundaries (input, network, file, external API), and let internal invariants fail loudly. Source: none verified; this is standard review practice (Ousterhout's "define errors out of existence" idea, *A Philosophy of Software Design*, 2018, possibly outdated as a source but still the reference).

- **Tell: Placeholder and stub code.** `// TODO: implement`, `pass`, `throw new Error("not implemented")`, fake return values, `// rest of code here`. Why: looks complete in a diff while doing nothing. Fix: no stubs in a finished change; if work is deferred, say so in the PR and leave a `shortcut:`-style note with the limit and trigger for upgrading. Source: none verified (general practice).

- **Tell: Fake tests.** Tests that assert `toBeDefined()`, mock the unit under test, or only check that code runs. Google: tests should "fail when the code is broken"; ask "will the tests actually fail when the code is broken?" Fix: for each new test, break the code on purpose and confirm the test fails for the right reason. Source: [Google eng practices](https://google.github.io/eng-practices/review/reviewer/looking-for.html).

- **Tell: Inconsistent style with the surrounding file.** Different error-handling pattern, naming case, import style, or a new test framework next to an existing one. Why: it signals no one read the neighbors. Fix: match the local conventions; if the convention is bad, change it in a separate change. Google: keep major reformatting separate from functional changes. Source: [Google eng practices](https://google.github.io/eng-practices/review/reviewer/looking-for.html).

- **Tell: Duplicate helpers and parallel utilities.** A new `formatDate` next to an existing `dateUtils.format`. Same root as duplication above. Fix: grep before writing. Source: GitClear (see above).

- **Tell: Boilerplate READMEs and docs.** Sections like "Features / Getting Started / Contributing" with generic claims, emoji headings, and em dashes. Fix: a README says what the thing is, how to run it, and what is not done. Source: none verified; the "Ghostty" and "curl" style policies below push the same way.

- **Tell: Over-long functions and speculative flexibility.** One 200-line function with nested branches; config flags for features nobody asked for. Fix: smallest change that solves the stated problem; split only on a real seam. Source: [Google eng practices, "Complexity"](https://google.github.io/eng-practices/review/reviewer/looking-for.html).

- **Tell: Oversized, unexplained PRs.** Many files touched, drive-by refactors, a PR description that is a generated summary of the diff. Fix: one purpose per change; the description says why, what was tested, and what risk remains. Source: [Google eng practices, "Small CLs"](https://google.github.io/eng-practices/review/developer/small-cls.html) (not fetched; general guidance).

### Inferences
- The strongest measured failures are duplication, security holes and unverified dependencies. Surface-level style tells matter mostly because they signal that the author did not read the output.
- Maintainers now treat reporter ownership as the control point, not the tool. Both the Linux and Ghostty policies put the burden on the human submitter.

### Gaps
- No verified citation for the specific comment, wrapper, try/catch, stub and README examples. They are common review complaints, but I did not find a 2025–2026 study that measured them.
- Hallucinated-API (non-package) rates: not searched.

## Key question 2: Maintainer policies

### Takeaway
Open-source projects are converging on one rule: the human who submits owns every line and must be able to explain it. Several projects also ban or restrict AI-generated reports and comments.

### Cited Findings

- **Linux kernel.** `Documentation/process/coding-assistants.rst` lets AI assistants help on the same standards as any contributor. "AI agents MUST NOT add Signed-off-by tags." Only humans can certify the DCO, and the human submitter reviews the code, checks licensing and takes responsibility. Assistants must confirm a bug with a reproducer where possible, and "the assistant must never send anything itself." Source: [kernel.org coding-assistants.rst](https://www.kernel.org/doc/Documentation/process/coding-assistants.rst), merged around April 2026 (Linux 7.0 per press reports). Conflict: The Register reported in October 2026 that maintainers agreed to deprecate the "Assisted-by" tag. I did not verify the current file; check the tree before citing the tag.

- **Ghostty.** CONTRIBUTING: "you must understand your code." "If you can't explain what your changes do and how they interact with the greater system without the aid of AI tools, do not contribute to this project." "Using AI to write code is fine. What's not fine is submitting agent-generated slop without that understanding." First-time contributors go through a vouch system; the page says "AI has unfortunately made it so we can no longer trust-by-default" and asks people to "write in your own voice." The full rules are in a separate AI_POLICY.md, which I did not read. Source: [Ghostty CONTRIBUTING.md](https://github.com/ghostty-org/ghostty/blob/main/CONTRIBUTING.md), date not confirmed.

- **curl.** Ended bug bounty (Jan 2026) because of AI-generated noise. See Key question 1. Source: [The Register](https://www.theregister.com/2026/01/21/curl_ends_bug_bounty/).

- **Gentoo.** Not searched. No finding.

### Inferences
- The common policy shape is: disclose or not (varies), human owns and understands, no unverified reports, no AI-authored sign-offs or votes of trust.

### Gaps
- Gentoo policy text: not fetched.
- Whether the Linux "Assisted-by" tag was actually removed: conflicting sources.

## Key question 3: Review checklist for AI-assisted code

### Takeaway
Use the normal review standard, with extra weight on design fit, duplication, dependency existence and tests that can fail.

### Cited Findings (checklist, drawn from the sources above)
- Does it belong in this codebase, or does an existing module already do it? (Google: "whether the change belongs in this codebase or in a library")
- Does every new dependency exist and was it chosen on purpose? (Spracklen et al.)
- Is there copy-pasted logic that should be a shared helper? (GitClear)
- Is every input from outside validated, and is output encoded? (Veracode)
- Would the tests fail if the code broke? Break it on purpose. (Google)
- Are names domain-specific, and are comments only the why? (Google)
- Can the author explain every changed line without the tool? (Ghostty, Linux)
- Was the bug reproduced before the report or fix? (curl; Linux procedure)

### Gaps
- No verified published checklist from a major project beyond the policies above. Other checklist repos on GitHub were not searched.

## Key question 4: What makes human code good

### Takeaway
Skilled engineers optimize for the next reader's understanding and for the smallest correct change. Most of the AI tells are the opposite of that.

### Cited Findings
- Google: review the overall design first; check functionality and edge cases; watch complexity; keep tests in the same change; name clearly; comment why, not what; follow the style guide; mark taste-only points "Nit:". Source: [Google eng practices, "What to look for in a code review"](https://google.github.io/eng-practices/review/reviewer/looking-for.html). Possibly outdated as a page but still the current guide in form.
- Ousterhout: complexity is the enemy; prefer deep modules with simple interfaces; define errors out of existence where you can. Source: *A Philosophy of Software Design*, 2018. Possibly outdated; not verified this session.
- Clean Code (Martin, 2008) gets criticism for overusing small functions and abstractions. Source: none fetched. Possibly outdated; use as a warning, not a rule.

### Craft principles
1. Read the neighbors first; match their conventions, error style and naming.
2. Smallest correct change. Delete before adding.
3. Names carry meaning; comments carry only the non-obvious why.
4. Validate at boundaries, fail loudly inside.
5. Tests must be able to fail, and you should have seen them fail.
6. Verify each dependency and claim before stating it.
7. Write PR and commit text in your own plain words: what changed, why, what you tested, what you did not test.
8. Know the code well enough to explain it without the tool. This is the main test.

## Source list
- [GitClear 2025 report](https://www.gitclear.com/ai_assistant_code_quality_2025_research), 2025
- [Veracode 2025 GenAI report press release](https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/), 30 Jul 2025
- [arXiv:2406.10279 Spracklen et al.](https://arxiv.org/abs/2406.10279), June 2024
- [METR RCT](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), 10 Jul 2025
- [The Register, curl bounty end](https://www.theregister.com/2026/01/21/curl_ends_bug_bounty/), 21 Jan 2026
- [kernel.org coding-assistants.rst](https://www.kernel.org/doc/Documentation/process/coding-assistants.rst), 2026
- [Ghostty CONTRIBUTING.md](https://github.com/ghostty-org/ghostty/blob/main/CONTRIBUTING.md), undated
- [Google eng practices](https://google.github.io/eng-practices/review/reviewer/looking-for.html), undated (possibly outdated form)
