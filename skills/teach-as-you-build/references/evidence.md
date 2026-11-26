# Evidence

Checked 2026-11-26 from `research_notes/Senior craft and teaching mode/teaching.md`. Tags: `[verified: URL]` means the page or abstract was opened and the claim, numbers and date match. `[unverified]` means not confirmed, with the reason. The caps (3 decisions, 120 and 400 words, 40 words per why) are design choices to test with the repo's with-and-without judge. No source gives an ideal length.

## Why explanations are optional and default to off

- Instruction that helps novices can lose its effect or turn negative for more experienced learners (expertise reversal). Kalyuga, Ayres, Chandler, Sweller 2003, Educational Psychologist 38(1), 23-31. A review paper, not one experiment. [verified: https://doi.org/10.1207/s15326985ep3801_4]
- Field trial in one high school in Turkey, nearly a thousand math students. With a plain GPT-4 chat, practice scores rose 48 percent, but on a later exam without AI those students scored 17 percent lower than the no-AI group. A tutor with teacher-designed hints largely removed the harm, though it showed no gain over no AI. Bastani et al., PNAS 122(26), June 2025. [verified: https://www.pnas.org/doi/10.1073/pnas.2422633122]
- Khanmigo: in a two-year study in 18 Tennessee middle schools, students largely stopped using it when it refused answers and asked questions or gave hints. Khanmigo added no benefit beyond Khan Academy practice alone. This is a press report (Hechinger, 21 Sep 2026) of a draft paper by Oreopoulos and Low circulated by NBER in August 2026. The draft itself was not opened. [verified: https://hechingerreport.org/proof-points-khanmigo-math-ai-tutor/]

## Why the explanation sits next to the result

- In a randomized trial of 52 mostly junior engineers learning a Python library (Trio), the AI group averaged 50 percent on the quiz against 67 percent for hand coding (d=0.738, p=0.01). Groups that asked for explanations or concepts scored 65 percent or more, but those groups had 2 to 7 people each and the authors say the pattern is not causal. Anthropic, 29 Jan 2026. [verified: https://www.anthropic.com/research/AI-assistance-coding-skills]
- Claude Code's Explanatory style adds short Insight blocks that explain the choices behind the code. The Learning style explains choices and leaves small pieces of code for you to write. The page does not say these styles are longer. [verified: https://code.claude.com/docs/en/output-styles]

## Why show the work, then fade

- Novices learn more from worked examples than from solving cold. In five algebra experiments, worked examples took much less time, later similar problems were solved faster, and errors fell. The effect was specific to problems with the same structure. Sweller and Cooper 1985, Cognition and Instruction 2(1), 59-89. [verified: https://www.tandfonline.com/doi/abs/10.1207/s1532690xci0201_3]
- Removing solution steps one at a time improved near-transfer performance over example-problem pairs, in small studies on probability and electricity (not geometry). Adding self-explanation prompts at the worked steps helped further, on near and far transfer (n=28). Renkl and Atkinson 2003, Educational Psychologist 38(1), 15-22. Abstract page: https://www.tandfonline.com/doi/abs/10.1207/S15326985EP3801_3 [verified: https://mrbartonmaths.com/resourcesnew/8.%20Research/Explicit%20Instruction/Structuring%20the%20Transition%20From%20Example%20Study%20to%20Problem%20Solving.pdf] (full-text copy read).
- Adaptive fading beat fixed fading, which beat plain problem solving, in a tutored-problem setting. Salden, Aleven, Schwonke, Renkl 2009, Instructional Science. Abstract only. [verified: https://link.springer.com/doi/10.1007/s11251-009-9107-8]
- Modeling, coaching, scaffolding and fading are the four parts of apprenticeship that Collins, Brown and Holum adapt, with the aim of making thinking visible. The article proposes a framework and gives examples. It is a frame, not proof. American Educator, 1991. [verified: https://www.aft.org/node/18441]

## Why one skippable question

- Retrieval beat restudy on delayed tests (2 days and 1 week), while restudy won after 5 minutes. Students who restudied were more confident but remembered less. Roediger and Karpicke 2006, Psychological Science 17(3). [verified: https://pubmed.ncbi.nlm.nih.gov/16507066/]
- In a randomized study of 117 university students on a writing task, the ChatGPT group improved essay scores most, but knowledge gain and transfer did not differ between groups. The ChatGPT group showed fewer metacognitive steps (evaluation, orientation) than the human-expert and checklist groups. Fan et al., BJET 56(2), 489-530, 2025 (online Dec 2024). [verified: https://arxiv.org/abs/2412.09315]
- A purpose-built AI tutor beat in-class active learning in a crossover trial of 194 Harvard physics students (two lessons, surface tension and fluid flow, post-test after each lesson). Median gains were over double, in a median of 49 minutes on task. Kestin et al., Scientific Reports 2025. [verified: https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/]

## Not found

- No test of the five-part card. Its shape follows architecture decision records and is an engineering choice. [unverified: no source exists to open]
- No source opened on ADHD and instructional text. The next-action-first and show-state rules are practitioner guidance from the `i-have-adhd` skill. [unverified: no source opened]
