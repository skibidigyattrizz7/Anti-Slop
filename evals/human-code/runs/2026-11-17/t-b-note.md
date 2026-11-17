# Note: grade averages script

**What it is:** `t-b.py` reads `grades.csv` (columns `student, subject, score`) and prints each student's average score to two decimals, lowest average first. Ties are sorted by name.

**How to run:** `python3 t-b.py` reads `grades.csv` in the current folder. Pass another path to use a different file: `python3 t-b.py path/to/file.csv`.

**Things to know:**
- It stops at the first bad row (non-numeric score, missing column) and prints the line number. It does not skip bad rows, because a silently dropped score would change the average.
- Blank or missing scores count as bad rows.
- It uses only the standard library.
- It is 23 lines, under the 30 requested.
- Tested on a five-row sample and on a bad row (non-numeric score). Both behaved as expected. The test files were in a scratch folder and are not saved.
