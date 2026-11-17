# Evals: human-ui

Run each task prompt twice, with and without the skill. Compare on `references/rubric.md`.

## Task prompts

1. **Library hold shelf.** Build a one-page web app for a school librarian, Ms. Ortiz, to track 40 held books. Fields: student name, title, date held, status (waiting, picked up, overdue after 7 days). She uses it on a school laptop and sometimes on her phone. Include the empty state and an error if saving fails.
2. **Bike repair shop site.** Write the homepage for Chen's Cycle Repair, open Tue to Sat 9 to 5, tune-up $65, flat repair $15, on 4th Street. Phone 555-0142. No testimonials or stats exist yet, so do not make any up.
3. **Upload errors.** A photo-sharing form for a robotics club accepts PNG or JPG up to 10 MB. Write the button labels, the three error messages (file too large, wrong type, network lost mid-upload) and the empty state for the gallery. One upload of 4 photos had 1 failure.

## Should trigger (8)

- "Build me a landing page for my dog-walking business."
- "This dashboard looks generic, fix it."
- "Redesign this settings screen for mobile."
- "Write the error message for when payment fails."
- "Make my React page look less like AI made it."
- "Design the onboarding screens for a budgeting app."
- "Lay out these 6 slides so they don't look like a template."
- "What should the empty state say when there are no orders?"

## Near-misses, should not trigger (8)

- "Design the HUD and pause menu for my platformer." (human-games)
- "Write a 1,000-word blog post about our launch." (human-writing)
- "Review this Python function for bugs." (human-code)
- "Reply to this customer email." (human-writing)
- "Write a story about a lighthouse keeper." (human-fiction)
- "Fix the SQL query that times out."
- "Make a logo as a PNG image."
- "Explain how CSS grid works."
