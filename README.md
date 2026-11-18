# Anti-Slop

Skills and agents that help AI tools make writing, code, UI, games and media the way a skilled human would: specific, working and well made.

This is a quality tool. It does not hide that AI was used, and it will not tune work to beat an AI detector.

## What is in it

### Skills

Each skill is a short set of craft rules that loads when you ask for that kind of work in plain words. Each works alone.

| Skill | Use it for |
|---|---|
| `human-writing` | Essays, articles, posts, emails, product copy |
| `human-chat` | Chat replies, explanations, tutoring, feedback |
| `human-fiction` | Stories, dialogue, names, poems |
| `human-code` | Code, READMEs, comments, commit messages |
| `human-ui` | Websites, apps, dashboards, UI text |
| `human-media` | Images, video, music, voiceover |
| `human-games` | Mechanics, levels, game feel, assets |
| `real-reports` | Research, reports, slides, charts |
| `see-it-run` | Opening the real page and looking before calling it done |
| `own-voice` | Writing that must sound like you |
| `build-logs` | Hardware and robotics project logs |
| `unslop-prompting` | Prompts for other AI tools |

### Agents

Agents are optional. They use many more tokens than a skill, so they run when you ask or on big jobs.

| Agent | What it does |
|---|---|
| `planner` | Splits a big job into steps and picks the skills for each |
| `viewer` | Opens the result in a browser, takes phone and desktop screenshots, clicks through it |
| `judge` | Scores finished work against a rubric, with quoted evidence. Read-only |
| `writing-specialist`, `chat-specialist`, `fiction-specialist`, `code-specialist`, `ui-specialist`, `media-specialist`, `games-specialist`, `reports-specialist` | Fix work in one category and keep every fact |

## Install

Claude Code:

```
/plugin marketplace add skibidigyattrizz7/Anti-Slop
/plugin install anti-slop@anti-slop
```

ChatGPT and other tools: each skill has a ready copy in `dist/chatgpt/<skill>/`. Paste `instructions.md` into a Custom GPT's instructions or a project's instructions, and upload the files in `knowledge/`. The copies are built by `python3 tools/build_chatgpt.py`. Scripts and agents do not carry over.

## How a skill is laid out

```
skills/<name>/SKILL.md           under 500 words: rules, bans, defaults, examples
skills/<name>/references/        dated tells, craft notes, the judge's rubric
skills/<name>/scripts/           counts what can be counted
agents/<name>.md
evals/<name>/prompts.md          test tasks and trigger phrases
```

The scripts need Python 3 and nothing else. `see-it-run` needs Node and Playwright. Every script has a self-test:

```
python3 skills/human-writing/scripts/count_tells.py --selftest
node skills/see-it-run/scripts/shoot.cjs --selftest
```

## How it is tested

Each skill is run on the same task with and without the skill, then scored by the judge in a fresh context that does not know which is which. The first round is summarised in `evals/RESULTS.md`: the skill version was preferred in 6 of 8 categories on the first pass. The two that did not win cleanly (fiction and reports) were changed and re-tested, and the skill version was preferred in both.

Check the whole repo with one command:

```
python3 tools/check_repo.py
```

## Status

Version 0.1.0. Honest state of things:

- The eval round is small: one run per arm and one task per category. It shows the skills change the output. It does not prove how much.
- The viewer and the writing specialist were each tested on real files (results in `evals/RESULTS.md`). The planner and the other seven specialists have not run yet.
- Writing, fiction and reports were re-tested after their fixes. The rubric changes in the other categories have not been re-tested yet.
- The scripts are tested on their own samples and a few eval files, not on large real projects.
- The research notes for games and audio are thin, and some items are marked unverified.
- Tells go out of date. Each `tells.md` carries a `last_verified` date and a re-check schedule.

The research behind the skills is in `research_notes/`. The plan and the build rules are in `docs/`.

## Credits and license

MIT. The pattern files in `human-writing` are adapted from the humanizer skill (MIT), whose patterns come from Wikipedia's "Signs of AI writing" by WikiProject AI Cleanup.
