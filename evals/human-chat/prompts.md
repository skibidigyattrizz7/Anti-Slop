# Evals: human-chat

Run each task prompt with and without the skill. Compare with `skills/human-chat/references/rubric.md`.

## Task prompts

1. **Math help.** "I'm in 8th grade. I have to solve 5x - 7 = 3x + 9 and I keep getting x = 1. What am I doing wrong?" Facts: the answer is x = 8. Steps: 2x = 16, so x = 8; x = 1 comes from an arithmetic slip, so ask to see their steps if the slip is unknown. Expect: answer first, a worked check with real numbers, the likely mistake named, plain 8th-grade words, no praise opener.

2. **Business advice.** "I run a small bakery. A cafe offered to buy 200 croissants a week at 1.10 each. My cost is 0.95 each and I'd need to hire a part-timer for 120 a week. Should I take it?" Facts: margin is 0.15 each, 200 x 0.15 = 30 a week, which is less than the 120 wage. Expect: "No" or equivalent in the first sentence, the arithmetic, the price or volume at which it would work (about 800 a week at that wage, or 1.55 each), no menu of offers.

3. **Feedback on work.** "Rate my thesis statement: 'Social media has both positive and negative effects on teenagers, and this essay will discuss them.'" Facts: the statement takes no position and announces the essay instead of arguing. Expect: the biggest problem first, a rewrite example with a real claim marked as an example, honest rating because it was asked for, no praise sandwich.

## Should trigger (8)

1. "Explain how interest compounds like I'm 15."
2. "Can you help me with this algebra problem?"
3. "Your last answer was too long and too nice. Just tell me."
4. "Give me honest feedback on my business idea."
5. "Why does my sourdough come out dense? Quick answer please."
6. "I'm a beginner. What's the difference between a virus and a bacterium?"
7. "This reply sounds like a chatbot. Fix it."
8. "Should I take the job offer or stay? I want your actual opinion."

## Near-misses, should not trigger (8)

1. "Write a 1,500-word essay on the causes of World War I." (human-writing)
2. "Draft a cold email to a recruiter." (human-writing)
3. "Write a short story about a lighthouse." (human-fiction)
4. "Refactor this Python function to use a dict." (human-code)
5. "Design a landing page for my app." (human-ui)
6. "Write this in my own voice using these past posts." (own-voice)
7. "Make this slide deck look better." (human-media)
8. "Translate this paragraph into Spanish."
