# Code rubric

Used by the judge agent and for self-checks. Each check is PASS, FAIL or N/A. A FAIL needs a quoted line or a file and line as evidence. A PASS on C1 needs the command run and its result.

Check in this order, every time.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| C1 | Runs (must-pass) | The normal case was run (or traced by hand on a stated input) and at least one failure case (bad input or a missing file) was run too, with the command and its output shown, and the result matches what was asked | Never run or traced, the run fails, the output differs from the request, no failure case was run, or testing is claimed with no command or output shown |
| C2 | Reuse and fit | Existing helpers were searched for and used, and style matches the neighbors | A duplicate helper, copy-pasted block, or a different naming or error style than the file |
| C3 | Errors | Every error is handled where it can be acted on or surfaces with a specific message. Stopping with a clear error passes. Skipping a bad item and reporting it, with a non-zero exit, passes | A bare except, empty catch, or a catch that only logs a generic message. Skipping silently, or skipping with exit 0 and partial output, fails |
| C4 | Names | Names say what the thing is in this domain | `data`, `result`, `handler`, `temp`, `utils` for domain values |
| C5 | Comments | Comments give a reason, a constraint or a link | Comments restate the next line, banner comments, or a template docstring on trivial functions |
| C6 | Scope and honesty | Smallest change that solves the ask, no stubs, the report names what was not verified, and any stated size limit is met within about 10 percent | An abstraction with one use, a `TODO` or placeholder shipped as done, "should work" with no check, or a size more than about 10 percent over the stated limit |
| C7 | Security | No secrets in source, input validated at boundaries, new dependencies confirmed real | A secret-looking string, unchecked input at a boundary, or an unverified package |
| C8 | Text | Commit, PR and README say what changed, why, how to run it, what was tested | "Improve logic", a diff summary as PR text, badge walls, or no test notes |

## How to read the edge cases

- **C1, failure cases:** one normal run is not enough. Run at least one bad input or a missing file and show what happened. "Tested it" with no command or output fails.
- **C3, skip or stop:** both are fine when the reply says which it does. "Stop with a clear error" and "skip, report each skipped item, exit non-zero" pass. A skip that prints nothing, or one that prints a note but exits 0 with partial output, fails, because the result looks complete.
- **C6, size limits:** a stated size ("30-line script") is a target with about 10 percent tolerance, so 32 lines passes and 40 fails. Only a brief that says "hard cap" or "at most" makes it exact.
- **C6, extras:** judge extras (a wrapper, an option) on whether the brief needed them. Line count alone is a weak basis for a FAIL inside the tolerance.
## Verdict

- **Ship:** C1 passes and at most one other check fails.
- **Fix first:** anything else. C1 failing is always "Fix first".

Report passes out of applicable checks with the verdict, never the score alone.

## Guards

- Judge the code, never who or what wrote it. Do not say "AI-written" or "proves".
- Generated, vendored and fixture files are N/A for C3 to C5.
- Project conventions and the brief override C4, C5 and C8 defaults. They never override C1 or C7.
- Script counts are evidence for a reviewer. A reviewer reads the code.

## Senior checks

Apply only when the brief is a full project or the user asks for a senior review. They never change the verdict rule for ordinary work. Report them beside the verdict, not inside it.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| S1 | Design | Each new abstraction has two real callers or a stated reason, and each new interface is simpler than its body | A one-use wrapper, a pass-through method, or one likely change touching several modules |
| S2 | Tests | Tests assert behaviour, names state scenario and outcome, and a bug fix has a test that fails without the fix | Tests that break on a rename, a fix with no failing test first, or a flaky test rerun until green |
| S3 | Reviewable | One logical change of about 100 to 400 lines, refactor kept apart, description gives why, tests and risk | A mixed change over about 1,000 lines, or a description that restates the diff |
| S4 | Reliability | Every remote call has a timeout, retries are idempotent at one layer with backoff and jitter, writes are idempotent | A call with no timeout, a blind retry of a POST, or stacked retries |
| S5 | Boundaries and change | Input is validated by allowlist at each boundary, no secret in source, breaking edits are expand then contract, each new flag has an owner and expiry | Unvalidated input, a key in the repo, a breaking change in one step, or a flag with no removal plan |
