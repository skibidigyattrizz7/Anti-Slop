---
name: human-code
description: Use when writing, fixing or reviewing code, scripts, a README, code comments, a commit message or a pull request description, or when the user says code looks generic, over-commented, copy-pasted or "like AI wrote it". Not for chat replies (human-chat), prose (human-writing) or game and UI design (human-games, human-ui).
---

# Human Code

A model writes the most likely code for the prompt, not for your project. It restates the code in comments, wraps it in try/catch, names things `data` and `result`, and writes a new helper beside the one you already have. GitClear (Jun 2026, per the owner's notes): +81% duplicated blocks, +47% error-masking code, -70% refactoring. Veracode (Jul 2026, vendor report): about 44% of AI coding tasks added a security flaw.

## Top rules

1. **Search the project before writing.** Grep for an existing helper, pattern or naming style. Reuse it and match it.
2. **Handle an error where you can act on it.** Otherwise let it surface with a message that says what failed.
3. **Name things after the problem.** `rewardSurvivors`, `retryQueue`, not `handler`, `data`.
4. **Comment the why.** A constraint, a workaround, a bug link. Skip comments the code already says.
5. **Write the smallest thing that works.** No factory, config or abstraction without a second real use.
6. **Check trust boundaries.** Validate input from outside, keep secrets out of source, verify each new dependency exists.
7. **Run it.** Run the tests or the code, or trace it by hand. Report what you verified and what you did not.

## Never

The brief cannot override these.

- Invent a fact, result or source: an API, flag, package, test result or "it works".
- Leave a stub, `TODO` or fake return value in work you present as done.
- Swallow an error to make a run look clean.

## Defaults

A brief, the project's style or the user's habits override these.

- Commit message: what changed and why, in the imperative.
- README: what it is, how to run it, one non-obvious thing.
- PR description: why, what you tested, what risk is left.

## Read when

| When | Read |
|---|---|
| Scanning code for tells | `references/tells.md` |
| Writing or fixing code, a README, a commit or a PR | `references/craft.md` |
| Checking a finished change | `references/rubric.md` |
| You can run code | `python3 scripts/count_code_smells.py FILE` |

## Before and after

**Before:**
```python
def process_data(data):
    try:
        return json.loads(data)  # parse the data
    except Exception:
        print("An error occurred")
```

**After:**
```python
def parse_webhook_body(raw):
    return json.loads(raw)  # bad JSON from the sender should 400 upstream
```

**Before:** commit "Improve logic"

**After:** commit "Skip retry when the server returns 409"

## Final check

- Did I search for and reuse what the project already has?
- Does every error get handled or surfaced?
- Did I run it, and does my report say what I did not check?
