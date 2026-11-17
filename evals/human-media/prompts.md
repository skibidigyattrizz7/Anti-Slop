# Evals: human-media

Run each task with and without the skill. Compare against `references/rubric.md`.

## Task prompts

1. **Poster image.** "Make an image prompt for a poster for the Eastfield Library summer reading night, Friday 14 August, 6 pm. Warm and friendly. The librarian, Ms. Okafor, will be in it." Facts to keep: the event, date and time. The skill should ask before using a real person's likeness, keep the date as real type added afterward, and name medium, light and palette.
2. **Shot list.** "Write a shot list and prompts for a 25-second ad for Birch Coffee, a roaster in Leeds. Opening is the first pour of the day. I will generate it with a video model." The skill should give a purposeful shot list with varied camera moves, reference frames, real titles added in an editor and one grade.
3. **Audio direction.** "I need a 45-second podcast intro: a short music bed and a voiceover reading 'Field Notes with Dana Reyes, a show about small farms in Vermont.'" The skill should give a music structure, a marked script with pauses, a phonetic spelling check and a listening checklist, and say it cannot hear the result. It should note the user should check platform AI-disclosure rules.

## Should trigger

1. "Write a Midjourney prompt for a book cover."
2. "My AI thumbnails look plastic, how do I fix them?"
3. "Help me plan shots for a 30-second product video."
4. "Make a logo concept for my bakery."
5. "How do I make AI music sound less generic?"
6. "Direct a voiceover for my explainer."
7. "This image looks like AI, what gives it away?"
8. "Write a Sora prompt for a rainy street scene."

## Should not trigger

1. "Write the product description for my bakery." (human-writing)
2. "Design the settings page for my app." (human-ui)
3. "Add a jump sound and screen shake to my platformer." (human-games)
4. "Fix this Python function." (human-code)
5. "Write a short story about a lighthouse keeper." (human-fiction)
6. "Reply to my friend's text about dinner." (human-chat)
7. "Summarize this PDF report." (human-writing)
8. "Convert this MP4 to GIF with ffmpeg." (plain tool use)
