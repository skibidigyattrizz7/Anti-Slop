# unslop-prompting eval prompts

Run each task twice with the same model: once with no skill, once after reading `skills/unslop-prompting/SKILL.md`. Save the outputs under neutral names, then have the `judge` agent score them without knowing which is which.

## Tasks

1. Write a prompt I can give an AI to make a logo for my dog-walking business. Facts: the business is called Pawprint Walks; it is in Leeds; my customers are mostly older people with small dogs; my dog is a brown dachshund named Pepper; I want it to look friendly, not corporate; I will print it on a van door.
2. Write a prompt for Claude to write a 200-word product description for my handmade candles. Facts: they are soy wax; 8 scents; the best seller is "Wet Pavement"; each candle burns about 40 hours; they cost 14 pounds; I make them in my garage; buyers are mostly 25 to 35.
3. Write a prompt for a code tool to build a simple page that tracks my school homework. Facts: I use HTML and plain JavaScript; I have 6 subjects; I want to tick tasks off and see due dates; data should stay in the browser; it has to work on my phone.

## Should trigger the skill

- write a prompt for ChatGPT to plan my study schedule
- every image my AI makes looks the same, help
- improve this prompt: "write a story about a dragon"
- give me a prompt for Midjourney to make a poster
- I'm about to ask Claude to write my newsletter, help me brief it
- how do I get better results from AI
- write a prompt for a video generator
- make a prompt for an app builder to make a quiz game

## Should not trigger the skill

- write a blog post about our school fundraiser (human-writing)
- write my personal statement so it sounds like me (own-voice)
- document my robot build (build-logs)
- write a short story about a lighthouse (human-fiction)
- explain how recursion works (human-chat)
- fix the bug in this function (human-code)
- write a research summary with citations (real-reports)
- write the error message for a failed upload (human-ui)
