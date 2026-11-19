# StoryScope evidence

Source: Russell et al., "StoryScope: Investigating idiosyncrasies in AI fiction," arXiv 2604.03136 (April 2026), University of Maryland and Google DeepMind. Preprint; some features were labeled by an AI. Code: github.com/jenna-russell/storyscope. Re-check for a newer version by mid-2027.

Setup: 10,272 prompts, each answered by one human and five AI models (61,608 stories, ~5,000 words each), 304 narrative features.

| Pattern | AI stories | Human stories |
|---|---|---|
| No subplots | 79% | 57% |
| Narrator states the theme | 77% | 52% |
| Dialogue used for philosophical debate | 59% | 34% |
| Ending driven by the protagonist | 69% | 46% |
| Ends with internal acceptance | 47% | 27% |
| Emotion shown through body sensation | 81% | 38% |
| Emotion named directly | 8% | 29% |
| References real texts or authors | 24% | 47% |
| Addresses the reader | 7% | 28% |
| Lands in the rarest 10% of stories | 7.1% | 24.7% |

- Plot features alone: 93.2% macro-F1 for human vs AI; style plus plot: 96.0%.
- The human story was the rarest of the six for the same prompt 57.8% of the time.
- The five AI models resemble each other more than they resemble humans.
- Model quirks: Claude has flat event escalation, GPT overuses dream sequences, Gemini describes characters by appearance.
