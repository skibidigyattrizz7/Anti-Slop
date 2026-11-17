# Note: student averages script

**What it does:** `t-a.py` reads `grades.csv` (columns: student, subject, score) and prints each student's average score, lowest first, to 2 decimals. Run it as `python3 t-a.py` (uses `./grades.csv`) or `python3 t-a.py path/to/grades.csv`.

**Things to know:**
- Each row counts equally, so a student's average is the mean of all their scores across subjects, not a mean of per-subject averages.
- Rows with a non-numeric score or a blank student name are skipped, and the line number is printed to stderr. Nothing is corrected or guessed.
- Ties are ordered by name.
- It exits with status 1 and prints nothing if no valid rows are found.
- A missing file or a file with bad encoding raises a Python error. It is not caught.
- Tested once on a small sample file (3 students, 2 bad rows). Averages and skips were correct. No test file was added to the repo.
