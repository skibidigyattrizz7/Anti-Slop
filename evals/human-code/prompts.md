# Evals: human-code

Run each task with and without the skill. Compare against `references/rubric.md`. C1 means the output was actually run.

## Task prompts

1. **Retry helper.** "Our `sync_orders.py` calls `requests.post(url, json=payload)` to the warehouse API. It sometimes returns 503 or times out. Add retries: 3 attempts, 2 s then 4 s wait, only for 503 and timeouts. A 400 must fail at once. The repo already has `utils/backoff.py` with `sleep_for(attempt)`." Check: reuses `sleep_for`, no bare except, 400 not retried, run against a fake server or a mock.
2. **Commit and PR text.** "I changed `parse_invoice()` in `billing/parse.py` so a missing `due_date` returns `None` instead of raising KeyError. Tests: `test_parse_missing_due_date` added and passing; the PDF export path is untested. Write the commit message and PR description." Check: specific, says what was not tested, no invented details.
3. **Small CLI.** "Write a 30-line Python script that reads `grades.csv` (columns: student, subject, score) and prints each student's average, lowest first." Check: no argparse or classes, domain names, runs on a sample file, missing-file error is clear.

## Should trigger

1. "Review this Python function, it looks like AI wrote it."
2. "Write a bash script that backs up my notes folder."
3. "Fix the bug in this JavaScript and tell me what you tested: `function avg(a){let s=0;for(let i=0;i<=a.length;i++)s+=a[i];return s/a.length}`"
4. "Write a commit message for this diff: `- if (user.age > 18)` `+ if (user.age >= 18)` in signup.js"
5. "Clean up the comments in my code, they are way too many."
6. "Write a README for my weather CLI."
7. "Why does my code have try/except everywhere? Tighten it: `try:\n    x = int(s)\nexcept:\n    pass`"
8. "Write the pull request description for these changes."

## Should not trigger

1. "Write a blog post about learning Rust." (human-writing)
2. "Reply to my friend's text about the party." (human-chat)
3. "Design a landing page for my bakery." (human-ui)
4. "Explain how a for loop works to a 10-year-old." (human-writing)
5. "Make the jump feel better in my platformer." (human-games)
6. "Write a short story about a programmer." (human-fiction)
7. "Summarize this paper on sorting algorithms." (human-writing)
8. "Make this logo look less generic." (human-media)
