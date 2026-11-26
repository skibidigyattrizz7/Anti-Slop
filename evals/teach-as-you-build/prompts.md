# teach-as-you-build eval prompts

Run each task twice with the same model: once with no skill, once after reading `skills/teach-as-you-build/SKILL.md`. Save the outputs under neutral names, then have the `judge` agent score them against `skills/teach-as-you-build/references/rubric.md` without knowing which is which. Also run each task with no teaching phrase and check that the skill adds nothing.

## Tasks

1. Write a Python function that counts how many times each word appears in a text, ignoring case and punctuation. Teach me as you go.
2. Build a one-page "Contact us" form in HTML and CSS with name, email and message fields and a send button. Explain as you build. Facts: it is for a bakery called Rye and Co, and the form posts to /contact.
3. Write a 120-word announcement that the library will close at 5 p.m. on Friday 12 June for a staff day and reopen Monday at 9 a.m. I want to learn this, so explain your choices.

## Should trigger the skill

- teach me as you go while you build this login page
- explain as you build the sorting function
- I want to learn this, so walk me through making a budget spreadsheet
- why did you do that? Why a dictionary and not a list?
- mentor mode: help me write my club's newsletter intro
- explain what you're doing as you set up this script
- I'm learning React, build me a to-do app and say why you chose each part
- just do it, no explanations (turns the mode down)

## Should not trigger the skill

- explain how recursion works (learn)
- quiz me on the French Revolution (learn)
- write a short story about a lighthouse (human-fiction)
- write a commit message for this change (human-code)
- fix the bug in this function
- rewrite this paragraph so it sounds natural (human-writing)
- summarise this article in three bullets
- help me with my graded essay, write the conclusion (learn, with integrity rules)
