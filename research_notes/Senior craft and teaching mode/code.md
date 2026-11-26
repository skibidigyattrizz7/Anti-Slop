# Senior craft for the human-code skill (research notes, 2026-11-26)

Format per item: **Rule.** Why. Check. Source. "Opened" = fetched this session. "Unverified" = not opened; from memory or secondhand. Dates are publication dates unless noted.

## 1. Architecture and design

**Deep modules: small interface, lots of behaviour behind it.** Learning a shallow module costs about what it saves. Check: for each new class/function, would a caller need to know less than if they wrote the body inline? Red flags: pass-through methods, wrapper that adds no behaviour, design decision leaked through the interface, structure that mirrors execution order. Size is not the target: "classes should be small" produces "classitis"; Ousterhout's notes say 200-2,000 line classes can be fine and a simple interface matters more than a simple implementation. Source: Ousterhout CS190 notes, https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign (opened; book 1st ed. 2018, 2nd ed. July 2021, https://web.stanford.edu/~ouster/cgi-bin/aposd.php opened, page updated 2025-02-26). Tactical vs strategic programming (fast now, complexity accumulates) is secondhand via https://blog.pragmaticengineer.com/a-philosophy-of-software-design-review/ (search snippet only). A "spend 10-20% of time on design" figure was NOT found in any source: do not quote it.

**Beck's four rules, in priority order: passes the tests, reveals intention, no duplication, fewest elements.** Gives a tie-break order when judgement calls collide. Check: remove anything that serves none of the four, especially structure added "for flexibility". Source: Fowler, Beck Design Rules, 2015-03-02, https://martinfowler.com/bliki/BeckDesignRules.html (opened; rules date to late 1990s, classic).

**Abstract late; the wrong abstraction costs more than duplication.** Failure path: extract, new case almost fits, add a parameter and an `if`, repeat until nobody can change it. Fix: inline it back into callers, keep only what each uses, delete dead branches, re-extract. Check: before extracting, can you name the shared concept in domain words, and do all callers change for the same reason? Two copies is fine; the "rule of three" is a heuristic for that wait. Source: Sandi Metz, The Wrong Abstraction, 2016-01-20, https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction (opened). Rule of three origin (Fowler's Refactoring / Don Roberts): unverified, not opened. Tests: Vocke applies the rule of three before DRYing test code, https://martinfowler.com/articles/practical-test-pyramid.html (opened).

**YAGNI covers features, not changeability.** Fowler's four costs of a presumptive feature: build, delay, carry, repair. YAGNI does not forbid refactoring, tests or keeping code malleable, and does not apply when preparing adds no complexity. Check: "Is this needed by a requirement in the ticket? If not, what is the cost of carry?" Reversible decisions (internal function shape): decide fast. Hard-to-reverse (public API, data schema, wire format): slow down. Source: https://martinfowler.com/bliki/Yagni.html, 2015-05-26 (opened). The reversible/irreversible split is my inference.

**Coupling and cohesion as a change test.** Pick module boundaries so one likely change touches one module. Check: list the 3 most likely changes; count files each one touches; if >1 module, the boundary is in the wrong place. Source: Ousterhout "information leakage" red flag above; the checklist is an inference.

**API design: contract first, validate at the boundary, add rather than modify, assume someone depends on every observable behaviour (Hyrum's Law).** Check: can you add a field without breaking a client? Are error shapes consistent? Does a retry of a POST do the right thing (idempotency key)? Source: local skill `api-and-interface-design` (below); Hyrum's Law original https://www.hyrumslaw.com/ unverified.

**Data modelling: make illegal states unrepresentable; the schema outlives the code.** Check: could two columns/flags contradict each other? Prefer a union/enum over booleans plus nullable fields. Migrations are expand/contract (section 6). Source: inference; local `api-and-interface-design` has discriminated unions and branded IDs.

**ADRs: record decisions that are costly to reverse, on one or two pages.** Nygard format: Title, Status (proposed/accepted/deprecated/superseded), Context (neutral forces), Decision ("We will ..."), Consequences (good, bad, neutral). Numbers never reused; reversed decisions are marked superseded, not deleted. Stored in repo at `doc/arch/adr-NNN.md`. Check: would a new hire ask "why did we do it this way?" Source: Nygard, 2011-11-15, https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions (opened; classic, still the base format). Staff Engineer book / staffeng.com: fetch of the strategy page failed (404); unverified.

**Function length heuristics.** No source found with hard data. Do not state a line limit as fact. Defensible tests (inference): can you name it without "and"; does it mix abstraction levels; does reading it need scrolling for one idea. Gap.

## 2. Testing strategy

**Push each test as low as it can go; keep few end-to-end tests.** Vocke: "Push your tests as far down the test pyramid as you can"; E2E and UI tests are "notoriously flaky"; if a high-level test fails and no lower one does, write the lower one; delete high-level tests that add nothing. Check: for each new test, what is the cheapest level that would still catch this bug? Source: https://martinfowler.com/articles/practical-test-pyramid.html, 2018-02-26 (opened).

**Trophy vs pyramid: a difference of weighting, not of principle.** Trophy layers: static, unit, integration, E2E; most value in integration. Guiding line: "The more your tests resemble the way your software is used, the more confidence they can give you." Both agree: fewest E2E, tests should survive refactors. Pick by cost: a cheap in-process integration test beats a mock-heavy unit test. Source: Kent C. Dodds, https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications, 2021-06-03 (opened; JavaScript/frontend slant).

**Test behaviour, not implementation.** Tests coupled to internals break on refactor and stop being a safety net. Check: rename a private method or reorder internal calls; any test failing is coupled. Don't test private methods; if you want to, the class has too many jobs. Skip trivial getters. Source: Vocke 2018 (opened).

**Structure and naming.** Arrange-Act-Assert (or Given-When-Then), one condition per test. Name = scenario + expected outcome ("rejects_order_when_stock_is_zero"); a failure message should show input, expected, actual and say which rule broke. Prefer readable over DRY in tests ("DAMP"). Source: Vocke 2018 (opened) for structure and one-condition; naming and failure-message format are my synthesis plus local `test-driven-development`.

**Bug fix = failing test first (prove-it).** Check: the new test fails on the old code and passes on the fix. Source: local `test-driven-development` (below).

**Flaky tests.** Cause: timing, animations, shared state, real network. Policy: quarantine or fix; never retry-until-green silently. Google's blog says reruns are used only for tests marked flaky or on request and "a persistently failing test is giving a clear signal" (comment thread only, https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html opened). The oft-quoted figures (about 1.5% of runs, about 16% of tests show flakiness) were NOT retrieved: unverified.

**Property-based tests** (generate inputs, assert an invariant such as round-trip, idempotence, ordering preserved). Good for parsers, serializers, state machines. Hillel Wayne page fetch failed (404): unverified. No source opened.

**Mutation testing measures whether tests catch change, not whether lines ran.** Google runs it diff-based: only mutate changed lines, skip lines without coverage and "arid" lines, show surviving mutants in code review; used by 6,000 engineers, about 30% of diffs with coverage. Check: coverage is a floor, not proof; surviving mutants on critical logic mean a missing assertion. Source: Petrovic & Ivankovic, ICSE-SEIP 2018, https://research.google/pubs/state-of-mutation-testing-at-google/ (opened; 2018).

**Mocks.** Use for slow or side-effecting collaborators; pair fakes with contract tests so they stay faithful; never integrate with real production in automated tests. Source: Vocke 2018 (opened).

## 3. Reviewing (and making reviewable) a large change

**Standard: approve when the change definitely improves code health, even if imperfect.** "Technical facts and data overrule opinions"; style guide is authority on style, otherwise match existing code; unresolved disagreement escalates, never sits. Source: https://google.github.io/eng-practices/review/reviewer/standard.html (opened; undated).

**Review order: design, functionality, complexity, tests, naming, comments, style, consistency, docs; look at every line; look at context beyond the diff; praise good things.** Design first because it is the costly thing to change. Tests: would they fail when the code breaks; no false positives. Complexity: over-engineering for needs that "might" arise is a defect. If you lack expertise in a part (security, concurrency), get a qualified reviewer. Source: https://google.github.io/eng-practices/review/reviewer/looking-for.html (opened).

**Size: about 100 lines good, about 1,000 too large; files matter too (200 lines in 1 file ok, across 50 usually not).** Deleting a file counts as about one line; trusted automated refactors are exempt. A new API ships with a usage. Refactors go in separate changes from features; tiny local cleanups may stay. Tests ship with the code. Split by stacking, by file/reviewer, horizontally (layers) or vertically (slices); every piece must keep the build green. Source: https://google.github.io/eng-practices/review/developer/small-cls.html (opened).

**SmartBear/Cisco data.** Review "no more than 200 to 400 lines of code at a time"; defect density drops sharply above about 500 LOC/hour; a review of 200-400 LOC over 60-90 minutes finds 70-90% of defects; checklists "are the most effective way to eliminate frequently made errors"; author annotations help. The article does not tie every figure to the Cisco study. Source: https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/ (opened; study is c. 2006-2007, classic, possibly dated, and vendor-published).

**Comment with labels so the author knows what blocks.** Conventional Comments format: `<label> [decorations]: <subject>` plus optional discussion. Labels: praise, nitpick, suggestion, issue, todo, question, thought, chore, note (also typo, polish, quibble). Decorations: (blocking), (non-blocking), (if-minor). Google equivalent: prefix non-mandatory points "Nit:". Source: https://conventionalcomments.org/ (opened; undated).

**Author side: write the description as why / what you tested / remaining risk, annotate the diff, keep the stack bisectable.** Source: SmartBear annotation point (opened); description template is already in human-code Defaults.

**Mutation results in review** (see section 2) is a concrete way to review test quality, not just test presence.

## 4. Performance and reliability

**Measure before changing; fix the bottleneck; verify; keep or revert; guard against regression.** Check: before/after numbers on the same workload, attached to the change. Source: local `performance-optimization` (below). Primary sources on profiling (e.g. Knuth "premature optimization", Brendan Gregg) not opened: unverified.

**N+1 queries**: one query per row in a loop. Check: query count for a list endpoint with 1 vs 100 rows should be equal; fix with a join/batched `IN` query. No primary source opened: unverified; widely documented in ORM docs.

**Set a timeout on every remote call, sized from the downstream latency percentile.** AWS example: accept 0.1% false timeouts, so use p99.9; include connection setup in the budget (a 20 ms timeout broke after deploys because it covered new TLS setup). Source: AWS Builders' Library, Timeouts, retries, and backoff with jitter, 2019-12-05, https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter (opened; 2019, still the standard text).

**Retry only idempotent operations, at one layer, with capped exponential backoff plus jitter and a retry budget.** Three retries at each of five layers can multiply load on a failing database 243x. Retry server errors, not client errors. Token bucket caps retry volume. Retries are "selfish": they spend server capacity for one client's odds. Check: what happens to a non-idempotent POST that times out after the server committed? Same AWS source (opened).

**Idempotency**: accept a client-supplied key and return the stored result for repeats. Check: submit the same request twice in a test; one side effect. Source: AWS above (retries need idempotency); local `api-and-interface-design` section 6.

**Caching trade-offs**: you buy speed with staleness and an invalidation problem. Check: state the TTL, who invalidates, and what the user sees when it is stale; cache only after measuring. Inference; no primary source opened.

**Observability: log structured events with context, metrics for rates and latency, traces across services; define "working" (an SLO) before instrumenting.** Charity Majors / Honeycomb "wide events" article failed to load (404): unverified. Local `observability-and-instrumentation` and `honeycomb` plugin skills cover the practice. Check: from an alert, can you reach the failing request's trace and its logs in under a few clicks without a deploy.

## 5. Security at senior level

**Threat-model with STRIDE before building.** Spoofing (stolen auth), Tampering (data modified at rest or in transit), Repudiation (no audit trail), Information disclosure, Denial of service, Elevation of privilege. Ask per trust boundary and data flow: "how can an attacker change the authentication data? what if they read the profile? what if the database is unavailable?" Check: every boundary on the diagram has a line for each letter or a reason it does not apply. Source: Microsoft Learn, Threat Modeling Tool threats, page ms.date 2017-08-17, updated 2026-03-04, https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats (opened).

**Validate at every trust boundary, on the server, by allowlist; validation does not replace parameterized queries, output encoding or authorization.** Check syntax and semantics (end date after start date); enforce size and nesting limits before parsing; bind only intended fields (mass assignment); reject, do not "clean"; do not log rejected input verbatim. Applies to internal queues and partner feeds too. Source: OWASP Input Validation Cheat Sheet, https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html (opened; undated).

**Secrets: never in source or images; short-lived, least-privilege, rotated, audited; scan before commit.** Restarting an app does not revoke a stolen credential. Check: `git log -p` and the built image contain no keys; a leaked key can be revoked in minutes. Source: OWASP Secrets Management Cheat Sheet, https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html (opened; undated).

**Dependencies: review the lockfile diff, one upgrade per change, verify the package exists and is the one you meant (typosquats, slopsquatting).** Source: local `code-review-and-quality` (below); OWASP supply-chain cheat sheet not opened: unverified.

**Least privilege**: default deny, narrowest role/scope, separate read and write credentials. Source: OWASP Secrets (opened) for credentials; wider claim is general practice, no further source.

## 6. Working in a real codebase

**Read before writing; match the conventions; reuse.** Check: you can name the existing helper you grepped for and why you did or did not use it. Source: human-code rule 1 and Google "Consistency" item (opened).

**Chesterton's fence**: do not remove or simplify code until you know why it exists (git blame, tests, callers). Source: local `code-simplification`; original is Chesterton 1929 (classic).

**Breaking changes: parallel change (expand, migrate, contract).** Add new beside old, move clients incrementally, remove old when unused. Every step is releasable. Skipping contract leaves the code worse than before. Applies to schemas, APIs, function signatures. Source: Danilo Sato, 2014-05-13, https://martinfowler.com/bliki/ParallelChange.html (opened; classic, still current).

**Feature flags: classify them, give each an expiry and a removal task.** Types: release (about 1-2 weeks), experiment (until significant), ops (short, some long-lived kill switches), permission (years). Test the production combination plus all-off (fallback); convention: flag off = legacy behaviour. Cap total flags; add a "time bomb" test that fails after expiry. Source: Pete Hodgson on martinfowler.com, 2017-10-09, https://martinfowler.com/articles/feature-toggles.html (opened).

**Deleting code safely**: confirm no callers (grep, including strings, config, dynamic dispatch), deprecate first when others depend on it (Hyrum's Law), delete in its own change so revert is clean, and delete flags and dead branches when done. A deleted file counts as about one line in review size. Source: Google small-cls (opened); local `deprecation-and-migration`.

**Small, releasable slices; keep the build green; scope discipline.** Source: local `incremental-implementation`.

## Pass/fail checklist (draft for the senior layer)

1. Pass if an existing helper was searched for and reused or its absence stated.
2. Pass if each new abstraction has at least two real callers or an explicit reason.
3. Pass if each new public interface is simpler than its body.
4. Pass if one likely change touches one module.
5. Pass if a bug fix has a test that fails without the fix.
6. Pass if tests assert behaviour, with a name stating scenario and outcome.
7. Pass if the change is reviewable: about 100-400 lines, one logical change, refactor separate.
8. Pass if every remote call has a timeout; retries only on idempotent calls, one layer, backoff with jitter.
9. Pass if every trust boundary validates by allowlist, with no secret in source.
10. Pass if a schema or API change is expand/contract, and a new flag has an owner and expiry.
11. Pass if a perf claim has before/after numbers.
12. Pass if the description states why, what was tested, what risk remains.

## Build on these local skills

Base path A: `/root/.claude/plugins/synced/d13e5c22-fd75-4b81-b6fa-7bbe4432d675_ad4b38a0-ff16-4a31-8117-7e768f4021ea/`. No LICENSE file exists under `ziad-skills/` or `engineering/` (checked with find, maxdepth 3). Three ziad skills (be-ambitious, video-lens, code-review-and-quality) declare `license: MIT` in frontmatter; others declare none. `engineering` plugin.json author: Anthropic, no license field. `ponytail/LICENSE` is MIT, copyright 2026 DietrichGebert. So: link and paraphrase; copy text only from MIT-marked or ponytail files with attribution; treat the rest as "unlicensed, link only".

| Path (under A + `ziad-skills/skills/`) | Words | Reuse | Weak | License |
|---|---|---|---|---|
| `code-review-and-quality/SKILL.md` | 3,295 | Five axes; approval standard from Google; size table (~100 good, ~300 ok, ~1000 split); severity labels Critical/Nit/Optional/FYI; "verify the verification"; dependency/lockfile rules; "relocating complexity isn't reducing it" | Long; labels are a subset of Conventional Comments | MIT (frontmatter only) |
| `test-driven-development/` | 2,406 | Red-green-refactor; prove-it bug pattern; pyramid ~5% E2E / ~15% integration; test sizes; Beyonce rule; DAMP; state over interactions; anti-patterns | Pyramid percentages are not sourced in-skill | none declared |
| `api-and-interface-design/` | 2,129 | Hyrum's Law; one-version rule; contract first; addition over modification; idempotency key; discriminated unions, branded IDs | REST/TypeScript-centred | none declared |
| `performance-optimization/` (+ references/optimization-patterns.md) | 2,480 | Measure, find bottleneck, fix, verify keep-or-revert, regression guard; rationalizations and red flags | Core Web Vitals heavy | none declared |
| `security-and-hardening/` (+ references/hardening-patterns.md) | 2,490 | Threat-model-first; Always/Ask-first/Never tiers; SSRF, rate limit, secrets, supply chain, LLM features | Not STRIDE-labelled; long | none declared |
| `code-simplification/` | 2,004 | Five principles; Chesterton's fence step; scope to what changed | Language examples are generic | none declared |
| `incremental-implementation/` | 1,453 | Vertical, contract-first, risk-first slicing; rules 0-5 (flags, safe defaults, rollback) | Overlaps ponytail | none declared |
| `debugging-and-error-recovery/` | 1,602 | Stop-the-line; reproduce, localize, reduce, root cause, guard, verify; bisect | None notable | none declared |
| `deprecation-and-migration/` | 1,945 | Code is a liability; compulsory vs advisory deprecation; strangler, adapter, flag, expand/contract | Long | none declared |
| `documentation-and-adrs/` | 1,623 | ADR template and lifecycle; when to comment | Template is heavier than Nygard's | none declared |
| `observability-and-instrumentation/` | 2,133 | Define "working" first; pick signal per question; structured logs; alerts with runbooks; verify the telemetry | No wide-event stance | none declared |
| `doubt-driven-development/` | 2,540 | Claim, extract, doubt (fresh-context reviewer), reconcile, bounded stop | Needs external CLIs; heavy | none declared |

Path A + `engineering/skills/`: `architecture` (351 words, ADR output with options and trade-off analysis), `code-review` (474, security/performance/correctness/maintainability), `system-design` (191), `tech-debt` (222, prioritisation), `testing-strategy` (177). All are thin stubs: use only the ADR "options considered / trade-off analysis" shape and the tech-debt prioritisation idea. License: none found; author Anthropic.

Path A + `ponytail/skills/` (MIT, DietrichGebert 2026): `ponytail` (591) the smallest-complete-change ladder (does it need to exist, existing code, stdlib, installed dependency, one line) and the "shortcut: limit, when to upgrade" comment; `ponytail-review` (859) and `ponytail-audit` (899) have look-for / check-before-report / output structure; `ponytail-debt` (268) lists `shortcut:` comments as a debt ledger. Weak: tuned for terseness, not teaching.

Local base to extend: `/home/user/anti-slop/skills/human-code/` (SKILL.md 513 words; references craft 583, rubric 679, tells 602). The senior layer should be a new reference file plus a few links, not a rewrite.

## Teaching notes (how a senior explains a decision to a junior)

Pattern (inference, consistent with Google's guidance that reviews teach and that educational comments not required for approval are marked Nit): **state the decision, the forces, the rejected option, the trigger to revisit.** One to three sentences, in the commit or PR, not a lecture.

- Template: "I did X because [constraint]. I did not do Y because [cost]. I would revisit if [measurable trigger]."
- Abstraction: "I left two copies. Wait for a third caller; then we will know what really varies. A wrong shared function costs more than a copy." (Metz, Beck.)
- Deep module: "The caller passes one argument and gets the result. Retries, parsing and cleanup live inside, so nobody else needs to know them." (Ousterhout.)
- Tests: "This test breaks if the result is wrong, not if I rename a helper." Ask the junior to predict which edit would make it fail.
- Review comment: label it (`suggestion (non-blocking):`, `issue (blocking):`) and say why in one line; mark pure preference as nit; say what is good (Google "Good Things").
- Size: "I split this so each part can be reverted alone. Rule of thumb: about 100 lines, one idea, refactor separate."
- Reliability: "The retry is safe because the call is idempotent, there is one retry layer, and backoff has jitter. Three layers of three retries would be 27x load." (AWS.)
- Security: walk STRIDE as six questions on the diagram; ask "what crosses a trust boundary here?"
- Mark uncertainty honestly: "I measured this" vs "I think this; I did not measure" (matches human-code's report-what-you-verified rule).
- Offer a check the learner can run (a grep, a query-count assertion, a failing test), not just a rule.

## Gaps

- No source found for function-length numbers, the rule of three origin, N+1 and caching, property-based testing, Charity Majors/Honeycomb on wide events, Google flaky-test percentages, Staff Engineer ADR/strategy practice, Hyrum's Law original, OWASP supply-chain or threat-modelling sheets. Fetches that failed: hillelwayne.com post, honeycomb.io post, staffeng.com guide.
- SmartBear/Cisco figures are c. 2006-07 and vendor-published.
