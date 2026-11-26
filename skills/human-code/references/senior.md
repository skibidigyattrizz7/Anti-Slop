# Senior layer

Read for a big job, a senior review, or when the user asks for senior-level work. Each rule has the rule, why, a check, and a tag. `[verified: URL]` means the page was opened. `[practice]` means common professional practice with no opened source, so quote no numbers from it.

## Architecture and module design

1. **Deep modules.** Give each module a small interface and real behaviour behind it. Why: a shallow wrapper costs the reader as much as it saves. Check: would a caller know less than if the body were inline? Pass-through methods fail. [verified: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign]
2. **Tie-break order.** When judgement calls collide: passes the tests, reveals intention, no duplication, fewest elements. Check: remove anything that serves none of the four. [verified: https://martinfowler.com/bliki/BeckDesignRules.html]
3. **Abstract late.** A wrong shared function costs more than two copies. Why: each new case adds a parameter and an `if` until nobody can change it. Check: can you name the shared idea in domain words, and do all callers change for the same reason? To undo one, inline it back and re-extract. [verified: https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction]
4. **Build only what is asked.** Presumptive features cost to build, delay, carry and repair. This does not forbid tests or refactoring. Check: which requirement needs this? Slow down on public APIs, schemas and wire formats; decide fast on internal shapes. [verified: https://martinfowler.com/bliki/Yagni.html]
5. **Boundaries follow change.** Check: list the three likeliest changes and count the modules each touches. More than one means the boundary is in the wrong place. [practice]
7. **Record costly decisions.** Write a short ADR: title, status, context, decision ("We will ..."), consequences. Never delete one; mark it superseded. Check: would a new hire ask "why this way?" [verified: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions]

## Testing strategy

1. **Test at the lowest level that catches the bug.** Keep few end-to-end tests; they are slow and flaky. Check: if a high-level test fails and no lower one does, add the lower one. [verified: https://martinfowler.com/articles/practical-test-pyramid.html]
2. **Test behaviour, not internals.** Check: rename a private method; any test that fails is coupled to internals. One condition per test; the name states scenario and outcome. [verified: https://martinfowler.com/articles/practical-test-pyramid.html]
4. **Bug fix starts with a failing test.** Check: the test fails on the old code and passes on the fix. [practice]
5. **Never retry a flaky test until it is green.** Fix or quarantine it, and say which. Check: no silent rerun in CI config. [practice]
6. **Coverage is a floor.** A test that never asserts still counts as covered. Check on critical logic: change a line and see if a test fails. Google runs this on changed lines only. [verified: https://research.google/pubs/state-of-mutation-testing-at-google/]

## Reviewability and change size

1. **Approve when code health improves, even if imperfect.** Facts and data beat opinion. Check: each blocking comment names a concrete harm. [verified: https://google.github.io/eng-practices/review/reviewer/standard.html]
2. **Review design first, then function, complexity, tests, naming, comments.** Check: the first comment is about design, not style. [verified: https://google.github.io/eng-practices/review/reviewer/looking-for.html]
3. **Keep a change small.** Google calls about 100 lines good and about 1,000 too large. One logical change; refactors separate from features; tests ship with the code; each piece keeps the build green. Check: can each piece be reverted alone? [verified: https://google.github.io/eng-practices/review/developer/small-cls.html]
4. **Label comments by weight.** Use `issue (blocking):`, `suggestion (non-blocking):`, `nitpick:`, `question:`, `praise:`. Check: the author can tell what blocks. [verified: https://conventionalcomments.org/]
5. **Describe the change.** Why, what you tested, what risk remains. Add `shortcut: <limit>, <when to upgrade>` where you cut a corner. [practice]

## Reliability

1. **Put a timeout on every remote call.** Size it from the downstream latency percentile, and include connection setup. Check: no call without a timeout; the number has a stated basis. [verified: https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter]
2. **Retry only idempotent calls, at one layer.** Use capped exponential backoff with jitter and a retry budget. Why: retries stacked across layers multiply load on a failing service. Retry server errors, not client errors. Check: what happens to a POST that timed out after the server committed? [verified: same AWS page]
3. **Make writes idempotent.** Accept a client key and return the stored result on repeats. Check: send the same request twice in a test; one side effect. [verified: same AWS page]
4. **Measure before optimising.** Check: before and after numbers on the same workload sit in the change. [practice]
6. **Log structured events with context, and define what "working" means first.** Check: from an alert you can reach the failing request's logs without a deploy. [practice]

## Security at trust boundaries

1. **Ask STRIDE per boundary.** Spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege. Check: each boundary has an answer for each letter or a reason it does not apply. [verified: https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats]
2. **Validate on the server by allowlist.** Check syntax and meaning, cap size and nesting before parsing, bind only expected fields, reject rather than clean. It does not replace parameterized queries or authorization. Check: send a hostile value at each entry point. [verified: https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html]
3. **Keep secrets out of source and images.** Short-lived, least privilege, rotated; scan before commit. Check: `git log -p` and the built image hold no key, and a leaked key can be revoked fast. [verified: https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html]
4. **Vet dependencies.** Read the lockfile diff, one upgrade per change, confirm each package exists and is the one meant. [practice]

## Changing a live codebase

1. **Read, match, reuse.** Check: you can name the helper you searched for. Do not remove code until you know why it exists (blame, tests, callers). [practice]
2. **Parallel change for breaking edits.** Add the new beside the old, move callers, then remove the old. Every step is releasable; skipping the last step leaves it worse. Applies to schemas, APIs and signatures. [verified: https://martinfowler.com/bliki/ParallelChange.html]
3. **Flags get an owner and an expiry.** Classify each (release, experiment, ops, permission); flag off means old behaviour; test all-off. Check: a removal task exists. [verified: https://martinfowler.com/articles/feature-toggles.html]

## Build on

Use these when installed. Each has an inline fallback, so nothing breaks if it is missing.

- `systematic-debugging` (MIT): reproduce, find the root cause, then fix. Fallback: no fix before you can explain the failure.
- `verification-before-completion` (MIT): evidence before claims. Fallback: run it and show the output.
- `writing-plans` (MIT): plan a multi-step job. Fallback: list steps, each with a check.
- `code-review-and-quality` (ziad-skills, MIT in its frontmatter): five-axis review. Fallback: the review order above.
- `ponytail` (MIT): smallest complete change and `shortcut:` comments. Fallback: reuse, then standard library, then new code.
- ziad-skills `test-driven-development`, `api-and-interface-design`, `security-and-hardening`, `performance-optimization`, `code-simplification`, `incremental-implementation`, `deprecation-and-migration`, `documentation-and-adrs`, `observability-and-instrumentation`: no licence declared, so link or paraphrase only.

## Credits

The smallest-change order and the `shortcut:` comment form paraphrase `ponytail`, MIT, copyright 2026 DietrichGebert. No text was copied from other skills.
