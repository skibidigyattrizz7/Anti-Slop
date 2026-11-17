# human-writing eval prompts

Run each task twice with the same model: once with no skill, once after reading `skills/human-writing/SKILL.md`. Save the outputs under neutral names, then have the `judge` agent score them without knowing which is which.

## Tasks

1. Write the homepage intro text (about 120 words) for QuizPaste, a web tool. Facts: you paste your class notes and get 20 quiz questions in about a minute; it is free for students; it was made by a two-person team; it exports quizzes to PDF.
2. Write a short article (about 250 words) for a school newsletter explaining why the sky is blue.
3. Write a post (about 200 words) for a school robotics club blog about what the team learned at its last competition. Facts: the night before, the robot arm dropped the cube every third try; at 11 p.m. a team member took the claw apart and found one bent screw; the team placed 4th out of 22.

## Should trigger the skill

- write a blog post about our school fundraiser
- can you rewrite this paragraph, it sounds robotic
- make this email sound more natural
- edit my essay intro
- this reads like AI wrote it, fix it
- write product copy for my app's homepage
- summarise this article for our newsletter
- tighten up this caption

## Should not trigger the skill

- explain how recursion works (human-chat)
- write a short story about a lighthouse (human-fiction)
- write my personal statement so it sounds like me (own-voice)
- write a commit message for this change (human-code)
- write the error message for a failed upload (human-ui)
- write a research summary with citations (real-reports)
- write a prompt for an image generator (unslop-prompting)
- fix the bug in this function
