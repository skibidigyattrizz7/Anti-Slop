# human-code eval, 2026-11-17

One run per arm, 1 task. The judge ran in a fresh context and did not know which file used the skill.

Key: t-b.py used the skill. t-a.py did not.

| Task | Without skill | With skill | Judge preferred |
|---|---|---|---|
| grades.csv averages | 6/7 (Ship) | 7/7 (Ship) | With skill |

## What it showed

- Both scripts ran correctly on normal input. The gap was in behavior the old rubric did not test. On a bad score row, A skipped it and exited 0 with the student missing. B stopped with a message naming the line and exited 1.
- A was 32 lines against a requested 30 and lost C6 on that alone. B was 23 lines.
- Neither handled a missing file or a header-only file well, and neither run was shown as a failure test in the rubric's terms.
- `count_code_smells.py` flagged nothing on either file.

## Changes made after this run

- C1: needs a normal run and at least one failure-case run (bad input or missing file), with the command and output shown. A claim of testing with no command or output fails.
- C3: stopping with a clear error and skipping with a report and a non-zero exit both pass. Skipping silently, or skipping with exit 0 and partial output, fails.
- C6: a stated size limit is a target with about 10 percent tolerance unless the brief calls it a hard cap.
- Added a "How to read the edge cases" section. SKILL.md unchanged.

## Limits

One run per arm and one task is too few to be sure of anything. These scores predate the rubric changes above, so the old and new rubrics are not directly comparable. With the new C6 tolerance, A's 32 lines would pass, so A would fail on C3 and C1 instead. Rerun with 3 runs per arm before trusting the difference.
