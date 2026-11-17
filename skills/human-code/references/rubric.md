# Code rubric

Used by the judge agent and for self-checks. Each check is PASS, FAIL or N/A. A FAIL needs a quoted line or a file and line as evidence. A PASS on C1 needs the command run and its result.

Check in this order, every time.

| ID | Check | PASS when | FAIL when |
|---|---|---|---|
| C1 | Runs (must-pass) | The code or its tests were run, or traced by hand on a stated input, and the result matches what was asked | It was never run or traced, the run fails, or the output differs from the request |
| C2 | Reuse and fit | Existing helpers were searched for and used, and style matches the neighbors | A duplicate helper, copy-pasted block, or a different naming or error style than the file |
| C3 | Errors | Every error is handled where it can be acted on or surfaces with a specific message | A bare except, empty catch, or a catch that only logs a generic message |
| C4 | Names | Names say what the thing is in this domain | `data`, `result`, `handler`, `temp`, `utils` for domain values |
| C5 | Comments | Comments give a reason, a constraint or a link | Comments restate the next line, banner comments, or a template docstring on trivial functions |
| C6 | Scope and honesty | Smallest change that solves the ask, no stubs, and the report names what was not verified | An abstraction with one use, a `TODO` or placeholder shipped as done, or "should work" with no check |
| C7 | Security | No secrets in source, input validated at boundaries, new dependencies confirmed real | A secret-looking string, unchecked input at a boundary, or an unverified package |
| C8 | Text | Commit, PR and README say what changed, why, how to run it, what was tested | "Improve logic", a diff summary as PR text, badge walls, or no test notes |

## Verdict

- **Ship:** C1 passes and at most one other check fails.
- **Fix first:** anything else. C1 failing is always "Fix first".

Report passes out of applicable checks with the verdict, never the score alone.

## Guards

- Judge the code, never who or what wrote it. Do not say "AI-written" or "proves".
- Generated, vendored and fixture files are N/A for C3 to C5.
- Project conventions and the brief override C4, C5 and C8 defaults. They never override C1 or C7.
- Script counts are evidence for a reviewer. A reviewer reads the code.
