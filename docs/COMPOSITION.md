# How the skills fit together

These rules decide how Anti-Slop skills work with each other and with other installed skills.

## Precedence

When two rules disagree, the higher one wins:

1. The owner's standing rules (the flagged-look list, secrets never in files).
2. The user's brief and the project's existing conventions.
3. Correctness and honesty: never invent a fact, never withhold a working result.
4. The skill's own craft rules.
5. The senior layer (`references/senior.md`).
6. Teaching (`teach-as-you-build`).

A borrowed design skill never overrides the flagged-look list. When two installed skills disagree, the skill that links them names which one to follow.

## Rules

1. **Every skill works alone.** A pointer to another skill is one line with its fallback inline, for example "if impeccable is installed, use its critique; otherwise run rubric checks U1 to U6". Nothing depends on the other skill being there.
2. **One entry skill per area.** Detail lives in `references/`, one level deep, each file under about 1,100 words.
3. **Teaching is an overlay.** `teach-as-you-build` explains decisions that the area's skill and rubric already make. It never adds a second set of rules.
4. **Licences decide the verb.** MIT and Apache-2.0 text may be adapted, with credit in the file and in `NOTICE`. Anything else is linked or put in our own words.
5. **Keep listing cost low.** Descriptions stay under about 600 characters and start with "Load before starting". No new always-on router.
6. **Agents load their skill explicitly.** Each agent file says which skill folder to read.
7. **Hooks stay small.** The startup note holds the chat rules and the skill map only.
8. **Test before keeping.** A new rule stays only if `python3 tools/run_evals.py` shows it changes the output on held-out tasks.
