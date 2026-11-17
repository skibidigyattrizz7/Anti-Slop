# Judge report: human-code, run 2026-11-17

Brief: "Write a 30-line Python script that reads `grades.csv` (columns: student, subject, score) and prints each student's average, lowest first." The note is the message sent back with the script. No repo or neighbor files were supplied, so C2 is N/A for both.

Run evidence (temp folder, sample grades.csv):
- Normal (Ann 90/80, Bob 60/70.5, Cy 75): A and B both print `Bob: 65.25`, `Cy: 75.00`, `Ann: 85.00`, exit 0.
- Bad score row (Bob "abc"): A prints `skipping line 3` to stderr, then `Cy: 70.00`, `Ann: 90.00`, exit 0 (Bob is absent). B prints `grades.csv line 3: cannot read {...} (could not convert string to float: 'abc')` and exits 1, no averages.
- Blank score: same behavior as the bad score for each.
- Missing file: both raise an uncaught `FileNotFoundError` traceback, exit 1.
- Header-only file: A prints nothing, exit 1. B prints nothing, exit 0.
- `count_code_smells.py`: no flags for either. A: 26 code lines, 1 comment, 32 lines in file (`wc -l`). B: 17 code lines, 2 comments, 23 lines in file.

---

## Submission A (t-a.py + t-a-note.md)

```
Verdict: Ship      Score: 6/7 checks pass
Category: code   Rubric: /home/user/anti-slop/skills/human-code/references/rubric.md

Checks:
C1 PASS  "python3 t-a.py" in a temp folder with a 5-row grades.csv printed "Bob: 65.25 / Cy: 75.00 / Ann: 85.00", sorted lowest first, matching the brief
C2 N/A   no existing code or helpers supplied to reuse
C3 PASS  "print(f"skipping line {line_no}", file=sys.stderr)" names the line; missing file gives a specific FileNotFoundError and the note says it is not caught
C4 PASS  "totals", "name", "score", "avg" describe their domain values; "s" and "n" are short but local to one line
C5 PASS  "# student -> [sum, count]" explains the data shape; docstring gives usage
C6 FAIL  file is 32 lines against the requested 30; "def main():" wrapper with "return 0 if totals else 1" and the "[KeyError, TypeError, ValueError]" score=None branch are extras the brief did not ask for
C7 PASS  "name = (row.get("student") or "").strip()" and the float() try/except validate input at the boundary
C8 PASS  note says what it does, how to run it, what was tested ("Tested once on a small sample file (3 students, 2 bad rows)"), and what was not (no test file, file errors not caught)

Top fixes (most important first, 5 at most):
1. t-a.py `print(f"skipping line {line_no}", file=sys.stderr)` -> a student whose only row is bad vanishes from the output and the exit code is still 0, so a partial result looks complete -> either stop on a bad row, or print a final "N rows skipped" line and exit non-zero when any were skipped
2. t-a.py whole file (32 lines) -> over the 30 lines asked -> drop `main()` and the `return 0 if totals else 1` exit-code logic, or trim blank lines
3. t-a.py `print(f"skipping line {line_no}", ...)` -> says which line but not why -> add the bad value or the reason

Could not check: nothing
```

## Submission B (t-b.py + t-b-note.md)

```
Verdict: Ship      Score: 7/7 checks pass
Category: code   Rubric: /home/user/anti-slop/skills/human-code/references/rubric.md

Checks:
C1 PASS  "python3 t-b.py" in a temp folder with a 5-row grades.csv printed "Bob: 65.25 / Cy: 75.00 / Ann: 85.00", sorted lowest first, matching the brief
C2 N/A   no existing code or helpers supplied to reuse
C3 PASS  "sys.exit(f"{path} line {line_no}: cannot read {row!r} ({exc})")" gives file, line, row and cause; missing file gives a specific FileNotFoundError
C4 PASS  "scores", "averages", "student", "name", "vals" all say what they hold
C5 PASS  "# Stop on the first bad row: an average over a silently skipped score is wrong." gives a reason
C6 PASS  23 lines, no helper or option beyond the brief; note says "It is 23 lines" (matches wc -l) and says the test files were not saved
C7 PASS  "float(row["score"])" inside try with "except (KeyError, TypeError, ValueError)" validates at the boundary; no secrets, standard library only
C8 PASS  note says what, how to run, why it stops on bad rows, and what was tested ("a five-row sample and on a bad row")

Top fixes (most important first, 5 at most):
1. t-b.py `scores[row["student"]].append(...)` -> a blank student name is accepted and prints as ": 70.00" -> reject an empty name in the same try block
2. t-b-note.md "Tested on a five-row sample and on a bad row" -> missing file, header-only file and empty-name cases are not mentioned -> add one line saying they were not tested (a header-only file prints nothing and exits 0)
3. t-b.py `with open(path, newline="") as f:` -> no encoding given, so a UTF-8 file with a BOM or non-ASCII names may misread on some systems -> pass `encoding="utf-8-sig"`

Could not check: nothing
```

---

Better: B. It fits the 30 lines (23), and it fails loudly on a bad score instead of exiting 0 with a student missing from the output.

## Rubric notes

- C6 "smallest change" does not say how to treat a stated line budget. I counted 32 lines against 30 as a FAIL for A. A reviewer could call that too strict, since the brief's "30-line" may be a rough size. Add a line to C6 saying whether a stated size limit is a hard cap.
- C6 also lumps three things together: size, extra features and honesty. A's `main()` wrapper is not clearly "an abstraction with one use", so the FAIL rests on line count alone, which is a weak basis.
- C3 does not say whether "skip and report" is acceptable. A's skip with a stderr line passed "surfaces with a specific message", yet the output is silently incomplete and the exit code is 0. B's stop-on-first-error also passed. The rubric cannot tell these two designs apart, and it should say whether partial output with exit 0 counts as handled.
- C2 is N/A for any standalone-script brief with no neighbor code, so the denominator differs between categories of task.
- C5, C4 and the smell script found nothing in either file, so they did not separate the two. The only separating checks were C3 (weakly) and C6.
- The C1 PASS rule requires "the command run and its result". The rubric does not require testing failure cases (missing file, bad row), so the C1 PASS is the same for both even though the bad-row behavior differs. The judge instructions in this task (bad row, missing file) went beyond what C1 asks.
- Verdict rule: A fails one non-C1 check and still gets "Ship". That seems loose when the failing check is about size, not correctness.
