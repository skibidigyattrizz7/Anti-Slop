# Code tells (dated)

last_verified: 2026-11-17 against the owner's `ai-signs.md` (Jun to Jul 2026 data) and `research_notes/AI tells and craft across media/code.md`.
Re-check: security and dependency numbers every 6 months, style tells after a major model release.

A tell is a reason to rework the code. It is never proof of who wrote it. Many humans do all of these. Judge the code, not the author.

## Structure (strongest, slowest to expire)

| Tell | Fix |
|---|---|
| New helper beside an existing one (`formatDate` next to `dateUtils.format`) | Grep first. Reuse, or extend the old one. |
| Near-identical blocks repeated | Extract on the third copy. |
| Error-swallowing: bare `except`, empty `catch`, a catch that only logs "An error occurred" | Handle it where you can act, or let it surface with a specific message. |
| Defensive checks for values that cannot be null | Validate at trust boundaries only. Let inner invariants fail loudly. |
| Wrapper, factory, `Manager` or config around one call | Inline it. Abstract when the second real caller appears. |
| Style differs from the file: naming case, error pattern, imports, a second test framework | Read the neighbors and match them. |
| Stubs: `TODO: implement`, `pass`, `not implemented`, fake return values | Finish it, or say in the PR what is deferred and why. |
| Fake tests: `toBeDefined()`, mocking the unit under test | Break the code on purpose. The test must fail for the right reason. |
| Oversized PR with drive-by refactors and a generated summary | One purpose per change. Describe why, what was tested, what risk remains. |
| New dependency nobody checked | Confirm it exists, is maintained and is the one you meant. Invented package names can be registered by attackers (Spracklen et al., 2024, older models; rates vary by version). |

## Surface tells

- **Restating comments.** `// increment counter` above `count += 1`. Delete them.
- **Banner comments.** `# ===== Helpers =====`. Use file structure instead.
- **Generic names.** `data`, `result`, `item`, `temp`, `handler`, `utils`, `helper`. Name the domain thing.
- **Docstring on every trivial function**, all from one template.
- **Long if/elif ladders** where a lookup table or early return is clearer (Claude-leaning, DCAN Mar 2026).
- **Model idioms** such as `.zfill` where the project uses f-string padding. Match the project.
- **Agent co-author trailers in commits.** Follow the project's own policy, which may require them. Never add or remove them to disguise anything.
- **Hard-coded secrets, permissive configs** (`CORS: *`, `verify=False`), unchecked input. Security review comes first.
- **Boilerplate README.** Badge walls, emoji headings, "Features" lists of adjectives.
- **Made-up APIs and unused imports.** Check against the real docs or the installed package.

## Guards

- Generated or vendored code, test fixtures and example snippets can trip these patterns legitimately.
- A comment that explains why is not a tell, even a long one.
- Beginners and students write generic names and many comments. That is a teaching point, not a flag.
- Project policy wins: some projects require co-author trailers or disclosure.
- A tell with no failing behavior is style. A tell that hides an error is a bug.

## Sources

Owner's `human-code` skill and `ai-signs.md` (GitClear Jun 2026; Veracode Jul 2026, vendor report; DCAN Mar 2026). Spracklen et al., arXiv:2406.10279 (2024). Google engineering practices, code review. METR RCT (Jul 2025) is why "it felt fast" is not evidence: use verified, merged results. Notes and caveats: `research_notes/AI tells and craft across media/code.md`. The restating-comment, wrapper and stub examples are general review practice with no measured study.
