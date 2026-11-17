# Detection science: background for a quality checker

Scope: what detectors measure, how reliable they are, and what a checker can honestly say. Not a guide to evading detection. Coverage gaps are listed at the end. Items marked *(secondary)* come from law-firm or news summaries, not the primary text.

## 1. Text detectors: how they work and how well

- **Signal / fact:** Zero-shot methods score text with a language model. Perplexity (how predictable the text is to a model) and burstiness (variation in sentence predictability) are the classic inputs. Binoculars contrasts two related LMs, using perplexity and cross-perplexity, and needs no labelled training data.
  - **How reliable / limits:** Binoculars reports over 90% detection of ChatGPT-style text at a 0.01% false-positive rate, with no ChatGPT training data. These are the authors' numbers on their own benchmark, not independent results. Perplexity-style scores also rise for plain, simple human prose, so they are not measures of "AI-ness".
  - **How a quality-checker could use it:** Do not use. A checker has no reference model and no labelled corpus, and a score would not describe craft anyway.
  - **Source:** Hans et al., "Spotting LLMs With Binoculars", arXiv 2401.12070 (Jan 2024, v3 Oct 2024), https://arxiv.org/abs/2401.12070

- **Signal / fact:** RAID is the largest shared robustness benchmark found: over 6 million generations, 11 models, 8 domains, 11 adversarial attacks, 4 decoding strategies. Its finding is that detectors fail badly out of domain and under simple changes such as sampling strategy, repetition penalty and adversarial edits.
  - **How reliable / limits:** It is a 2024 paper (ACL 2024). I found no 2025-2026 follow-up with the same scope. Treat its results as a lower bound on fragility for the 2024 detectors it tested.
  - **How a quality-checker could use it:** Confirms that any text-origin score is brittle. Supports the rule that a checker should never output a verdict on origin.
  - **Source:** Dugan et al., "RAID", ACL 2024, https://arxiv.org/abs/2405.07940

- **Signal / fact:** Liang et al. (Stanford, 2023) ran 91 TOEFL essays by non-native English writers through seven popular GPT detectors. More than half were flagged as AI-generated, and one detector flagged 98%. Simple prompting reduced the bias. Published in *Patterns* after the 2023 arXiv preprint. Native-speaker essays were classified accurately.
  - **How reliable / limits:** Small sample, one test set, 2023 detectors. Possibly outdated as a number, but the mechanism is still cited: low-perplexity, constrained vocabulary reads as "AI".
  - **How a quality-checker could use it:** Strong reason to never penalise plain or simple prose. A "generic" score must not correlate with writing that is simply clear or formal. Flag it as a possibly outdated figure.
  - **Source:** Liang et al., "GPT detectors are biased against non-native English writers", arXiv 2304.02819 (Apr 2023) *(possibly outdated)*, https://arxiv.org/abs/2304.02819

- **Signal / fact:** Classifier-based detectors are trained on one generation of models and degrade on newer ones. OpenAI released and then withdrew its own AI text classifier in 2023 because accuracy was too low. I could not re-fetch the OpenAI page (HTTP 403), so the exact rates are unverified in this session.
  - **How reliable / limits:** As recalled, the withdrawal reason was low accuracy. Treat the numbers as unverified until checked.
  - **How a quality-checker could use it:** Justifies the principle that the vendor of a detector is not confident in it. Cite only after verifying.
  - **Source:** OpenAI, "New AI classifier for indicating AI-written text", Jan 2023 *(possibly outdated; page not re-read)*, https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text/

- **Signal / fact:** Google DeepMind's SynthID-Text is a sampling-time watermark. It biases word choice during generation, and detection runs without the model. Published in *Nature* in Oct 2024 (vol. 634, pp. 818-823). A non-distortionary mode is reported to keep quality, and a live test on about 20 million Gemini responses found no meaningful quality loss.
  - **How reliable / limits:** Works only on text from providers who use it. The authors note that editing or paraphrasing can remove the watermark. The public reference implementation says it is not for production use.
  - **How a quality-checker could use it:** Not usable. A checker cannot read watermarks it does not hold keys for. Note that origin tools exist, so a checker should not claim to be one.
  - **Source:** Dathathri et al., "Scalable watermarking for identifying large language model outputs", Nature, Oct 2024, https://www.nature.com/articles/s41586-024-08025-4 (via https://ideas.repec.org/a/nat/nature/v634y2024i8035d10.1038_s41586-024-08025-4.html)

- **Signal / fact:** Vendor caveats are consistent: Turnitin and GPTZero publish false-positive warnings and say scores are not proof of misconduct. I did not retrieve their current pages in this session.
  - **Gap:** Current Turnitin and GPTZero caveat wording, and any 2025-2026 false-accusation case studies, were not verified.

## 2. Human detection of AI text

- **Signal / fact:** Russell, Karpinska and Iyyer (ACL 2025, arXiv 2501.15654, Jan 2025) asked annotators to label 300 non-fiction articles as human or AI (GPT-4o, Claude, o1) and explain their choices. Annotators who often use LLMs for writing were strong detectors with no special training. A majority vote of five such experts misclassified 1 of 300 articles, and they beat most commercial and open detectors, including on paraphrased text.
  - **How reliable / limits:** Non-fiction articles only. Five-person panels are impractical per text. Secondary write-ups disagree on author affiliations, so do not cite those.
  - **How a quality-checker could use it:** The experts' cues were lexical ("AI vocabulary") plus formality and over-clarity. This is the strongest evidence that a human-style checklist can work, but as a prompt for a human reviewer, not an automated verdict.
  - **Source:** Russell et al., "People who frequently use ChatGPT for writing tasks are accurate and robust detectors of AI-generated text", arXiv 2501.15654 / ACL 2025, https://arxiv.org/abs/2501.15654

- **Signal / fact:** Earlier studies (for example, Clark et al., 2021, on GPT-3 text) found that lay readers were often near chance at telling model text from human text.
  - **How reliable / limits:** Pre-2025 and older models. Possibly outdated.
  - **How a quality-checker could use it:** Shows why a checker's output should not rely on a reader's gut sense of "AI-ness".
  - **Source:** Clark et al., "All That's 'Human' Is Not Gold", 2021 *(possibly outdated; not re-fetched in this session)*

- **Gap:** Image, video and voice human-detection studies were not searched in this session (rate limits). This is the largest gap in the notes.

## 3. Measurable linguistic signals

- **Signal / fact:** Excess word usage. Kobak et al. compared word frequencies in about 14 million PubMed abstracts (2010-2024) against an expected trend and estimated that at least 13.5% of 2024 abstracts were LLM-processed (v3). The estimate varies by field and journal, reaching about 30% in some sub-corpora. "delve" is among the strongest excess words.
  - **How reliable / limits:** Population-level estimate, not per-text. Word trends also follow human fads (a Language Log critique argues this). Shares of "delve" dropped in later data, so the list ages quickly.
  - **How a quality-checker could use it:** A checker can count a flagged-word list, but must weight it against a baseline and say that a hit is a style note, not evidence. Re-validate the list every model generation.
  - **Source:** Kobak et al., "Delving into LLM-assisted writing in biomedical publications through excess vocabulary", Science Advances, Jul 2025 (arXiv 2406.07016), https://arxiv.org/abs/2406.07016; Language Log, https://languagelog.ldc.upenn.edu/nll/?p=64877

- **Signal / fact:** Lexical diversity, sentence-length variance, hedging phrases, em-dash frequency, and repeated sentence templates have all been proposed as tells. I did not verify measured effect sizes or cross-model stability for these in 2025-2026 sources.
  - **How reliable / limits:** Unknown. Each one overlaps with normal human style, and the values shift with prompting and model version.
  - **How a quality-checker could use it:** Computing them is cheap and fine, but only as a "this reads templated" prompt for a human. Do not report them as an AI score. Em-dash counts are a UI-copy style choice, which the owner's rule list already handles separately.
  - **Source:** Gap, no primary source retrieved.

## 4. Image, video, audio and provenance

- **Signal / fact:** C2PA Content Credentials attach a signed manifest to an asset, with optional soft bindings (watermarks, fingerprints) to re-find it after metadata is stripped. The spec (v2.2 text) states that a manifest can be separated from its asset, that a soft binding "shall not be used as a hard binding", that soft bindings are "not statistically unique", and that a manifest without a timestamp stops being valid when the signing credential expires or is revoked.
  - **How reliable / limits:** Proves who signed and what was recorded, not whether content is true. Absence of a manifest proves nothing. Trust depends on the signer and certificate lists.
  - **How a quality-checker could use it:** Checkers can display a credential if present. Absence should never be read as "AI" or as "human".
  - **Source:** C2PA Specification 2.2, https://spec.c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html

- **Signal / fact:** EU AI Act Article 50 transparency duties apply from 2 Aug 2026. The Commission's final Code of Practice on marking and labelling AI-generated content was reported as published on 10 June 2026. It is voluntary, has a provider section (marking and detection) and a deployer section (labelling deepfakes and AI text), and reportedly rejects a single technical fix. It is reported to carve out AI text that a human reviews and takes editorial responsibility for. Labelling icons were released.
  - **How reliable / limits:** All details here are *(secondary)*, from law-firm and news summaries. Check the Commission text before citing the text carve-out or icon details.
  - **How a quality-checker could use it:** Point users to the labelling duty for AI-generated media they publish in the EU. Do not build detection into the checker to meet it.
  - **Source:** European Commission code of practice page, https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content (secondary summaries reviewed: Jones Day, Jun 2026, https://www.jonesday.com/en/insights/2026/06/european-commission-publishes-final-code-of-practice-on-marking-and-labelling-aigenerated-content)

- **Gap, not searched:** Forensic artifacts (GAN/diffusion fingerprints), frequency-domain detectors and their known failure under compression, Google SynthID for images/video and its detector availability, and detection accuracy numbers for image and video tools. These need a second pass.
- **Gap, not searched:** Platform disclosure rules for YouTube, Meta, Steam and Spotify. Current wording needs checking.

## 5. How a checker should report results

- **Signal / fact:** Across the sources above, every detector vendor and study warns against using a single score as proof. Error rates vary by domain and writer, and non-native and formal writers are over-flagged (Liang et al.).
  - **How a quality-checker could use it:** Report bands, not a verdict. Example: "Low / Medium / High templated-style signals, with these specific lines". Include a false-positive note on every output. Never label a person as using AI, and never use a score for grading, hiring or discipline.
  - **Source:** Synthesis of sections 1-2 above.

- **Gap:** University and publisher policy pages were not retrieved in this session.

## Summary for the library

- No text or media origin detector is reliable enough to ship inside a checker. The honest product is a craft review: generic patterns, missing specifics, unclear hierarchy, inconsistent spacing, and the owner's "looks vibecoded" list, with a visible note that it describes style, not origin.
- Lexical tells (for example, "delve") are population-level and time-limited. Use them as review prompts only, and re-validate them each model generation.
- Provenance (C2PA) is useful when present and should never be read as evidence of AI when absent.
- Before publishing anything externally, verify: the OpenAI classifier figures, Turnitin and GPTZero caveats, the EU Code text, and all image, video and platform-policy items.
