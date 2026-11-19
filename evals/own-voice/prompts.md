# own-voice eval prompts

Run each task twice with the same model: once with no skill, once after reading `skills/own-voice/SKILL.md`. Save the outputs under neutral names, then have the `judge` agent score them without knowing which is which.

## Tasks

1. Write the opening paragraph (about 100 words) of my cover letter for a weekend job at Harbor Books. Facts: I am 17; I have shelved books at my school library for two years; last spring I found 14 misfiled books in one afternoon and fixed the catalog entries; I like quiet shops. My writing is plain and short, like this sample: "I don't talk much. I fix things. Ask my mum, she'll tell you the toaster still works."
2. Write a short email (under 100 words) to my chemistry teacher, Mr Okafor, asking for an extension on the lab report from Friday to Tuesday. Facts: I was at a regional swim meet in Leeds on Thursday and Friday; I have finished the method and results sections; I only need the conclusion.
3. Write a 120-word bio for my school's yearbook page. Facts: I am Dani; I run 5 km before school; I fix bikes for the neighbours; I once rebuilt a rear wheel from three broken ones; my favourite sandwich is cheese and pickle.

## Should trigger the skill

- write my college personal statement, it has to sound like me
- this draft doesn't sound like me, can you fix it
- help me write a cover letter for a barista job
- write a speech for my brother's wedding
- make my resume bullets stronger, here are my jobs: cashier, dog walker
- write a bio for my Instagram
- email my landlord about the broken heater, in my voice
- write my LinkedIn About section

## Should not trigger the skill

- write a blog post about our school fundraiser (human-writing)
- explain how photosynthesis works (human-chat)
- write a short story about a ghost ship (human-fiction)
- write the error message for a failed upload (human-ui)
- write a research summary with citations (real-reports)
- write a commit message for this change (human-code)
- write a prompt for an image generator (unslop-prompting)
- document my Arduino build (build-logs)
