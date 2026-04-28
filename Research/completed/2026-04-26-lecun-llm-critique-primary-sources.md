---
review_count: 2
title: "What is Yann LeCun's complete argument against Large Language Models as a path to autonomous machine intelligence, and what is the precise technical basis for each claim?"
added: 2026-04-26T18:31:29+00:00
status: completed
priority: high
blocks: [2026-04-26-lecun-critique-citizen-development-enterprise-risk, 2026-04-26-software-engineering-investment-case-llm]
tags: [lecun, llm, large-language-models, autonomous-intelligence, causal-reasoning, world-models, ai-critique, primary-sources]
started: 2026-04-27T02:04:05+00:00
completed: 2026-04-27T02:25:23+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# What is Yann LeCun's complete argument against Large Language Models as a path to autonomous machine intelligence, and what is the precise technical basis for each claim?

## Research Question

What is Yann LeCun's complete and precise argument against Large Language Models (LLMs) as a path to autonomous machine intelligence, meaning Artificial Intelligence (AI) that can reason, plan, and act autonomously, drawing only on primary or host-published source material around "A Path Towards Autonomous Machine Intelligence" (OpenReview, 2022), the Brown University lecture, the accessible April 2025 interview material, the seeded VivaTech keynote URL, and the November 2025 "Do LLMs Understand?" conversation; what is the specific technical basis for his claim that LLMs are text-trained statistical predictors without a causal world model or reliable consequence reasoning; where does he draw the boundary between domains where optimization over constrained symbolic structures can work and domains where real-world action requires predictive world modelling; and how stable is that position across the accessible 2022 to 2026 record?

## Scope

**In scope:**
- LeCun's primary paper, "A Path Towards Autonomous Machine Intelligence" (OpenReview, 2022)
- Brown University host material and lecture video for "World Models: Enabling the AI Revolution"
- The accessible official April 2025 interview material checked in this session
- The seeded VivaTech keynote URL, checked in this session and treated according to what is actually accessible at that URL
- The Pioneer Works host page and official YouTube page for "Do LLMs Understand?"
- The technical mechanism LeCun identifies as the deficit: no predictive world model for action, weak common sense from text alone, and limited reasoning in token-only generative systems
- The proposed alternative architecture, Joint Embedding Predictive Architecture (JEPA) and Hierarchical Joint Embedding Predictive Architecture (H-JEPA)
- Whether LeCun's position shifts between the 2022 paper and the later public talks

**Out of scope:**
- Third-party commentary used as substantive evidence
- Claims about LeCun's views that cannot be tied back to accessible primary or host-published material checked in this session
- Empirical testing of whether LeCun is correct
- Competing critiques from other researchers unless necessary for a narrow clarification of terminology

**Constraints:**
- Every factual claim about LeCun's argument must be tied to an accessible source URL checked in this session
- Where a host page is accessible but a full transcript is not, the item must say so explicitly and lower confidence accordingly
- The item must distinguish between what LeCun directly states, what follows as a synthesis from his accessible material, and what remains uncertain because transcript-level evidence was unavailable in this runtime

## Context

- [fact; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] The strongest accessible primary evidence in this session comes from LeCun's 2022 OpenReview paper and Brown University's 2026 lecture coverage, both of which frame intelligence as requiring a predictive world model that supports planning and action rather than text manipulation alone.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-lecun-critique-citizen-development-enterprise-risk.html; https://davidamitchell.github.io/Research/research/2026-03-18-human-brain-prediction-machines.html; https://davidamitchell.github.io/Research/research/2026-03-05-llm-hallucination-mechanisms.html] Prior completed items in this repository already connect LLM failure modes to missing grounded prediction, hallucination, and enterprise risk, so this item focuses on reconstructing LeCun's argument itself rather than re-proving those downstream applications.
- [inference; source: https://pioneerworks.org/broadcast/video/ai-yann-lecun-adam-brown; https://podcasts.apple.com/us/podcast/why-cant-ai-make-its-own-discoveries-with-yann-lecun/id1522960417?i=1000699824574; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] The 2025 to 2026 host materials are best used to test continuity of emphasis and public framing, while the 2022 paper remains the main technical anchor because it is the only fully accessible primary source with detailed mechanism.

## Approach

1. **Primary-source audit:** Check every seeded source URL, replace labels where the accessible host page differs from the seeded description, and record transcript-access limits explicitly.
2. **Core argument extraction:** Use the 2022 paper to reconstruct LeCun's architectural argument in its most detailed form.
3. **Public-framing extraction:** Use Brown University host material, the Brown lecture video metadata, the April 2025 interview summaries published by the official host, and the Pioneer Works host page to identify what LeCun repeats or sharpens later.
4. **Boundary analysis:** Separate the negative boundary, real-world action without predictive world modelling, from the positive boundary, constrained symbolic or optimization-heavy reasoning tasks, and mark any parts that remain weakly evidenced.
5. **Position evolution check:** Compare the accessible 2022, 2025, and 2026 materials for continuity, refinement, or reversal.
6. **Synthesis:** Produce a structured answer with explicit confidence levels, evidence map, assumptions, and open questions.

## Sources

- [x] [Yann LeCun, "A Path Towards Autonomous Machine Intelligence" (OpenReview forum page)](https://openreview.net/forum?id=BZ5a1r-kVsf) - primary technical source and canonical paper landing page
- [x] [Yann LeCun, "A Path Towards Autonomous Machine Intelligence" (OpenReview Portable Document Format (PDF) file)](https://openreview.net/pdf?id=BZ5a1r-kVsf) - primary paper text used for detailed technical claims
- [x] [Brown University News, "In lecture at Brown, Yann LeCun discusses a new approach to AI"](https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer) - official Brown University write-up with direct quotations
- [x] [Brown University Lemley Lecture page, "2026 Lemley Lecture Featuring AI Pioneer Yann LeCun"](https://lemley-lecture.brown.edu/past-lecture/2026-lemley-lecture-featuring-ai-pioneer-yann-lecun) - official event page and lecture title
- [x] [Brown University livestream page for the Lemley lecture](https://livestream.brown.edu/lemley) - official page linking the full lecture video
- [x] [Brown University YouTube lecture, "2026 Lemley Lecture Featuring AI Pioneer Yann LeCun"](https://www.youtube.com/watch?v=ZbrfvMLZZK4) - official lecture video page checked in this session
- [x] [Big Technology Podcast episode page, "Why Can't AI Make Its Own Discoveries? - With Yann LeCun"](https://podcasts.apple.com/us/podcast/why-cant-ai-make-its-own-discoveries-with-yann-lecun/id1522960417?i=1000699824574) - official host-published episode summary for the March 2025 interview material used here as the nearest accessible April 2025-era source
- [x] [Spotify mirror of the same Big Technology episode](https://open.spotify.com/episode/2mOKCpKSUdaLkFPz8Shgbp) - corroborating host-published summary text
- [x] [YouTube page checked for the April 2025 interview material identified during search](https://www.youtube.com/watch?v=8sS9UJzb_t4) - official video URL checked in this session; transcript not publicly accessible in this runtime
- [x] [Pioneer Works host page, "Deep Thoughts of Artificial Minds"](https://pioneerworks.org/broadcast/video/ai-yann-lecun-adam-brown) - official host page for the November 2025 discussion
- [x] [Pioneer Works YouTube page, "Do LLMs Understand? AI Pioneer Yann LeCun Spars with DeepMind's Adam Brown."](https://www.youtube.com/watch?v=ykfQD1_WPBQ) - official video page checked in this session
- [x] [Seeded VivaTech keynote URL checked in this session, "Meta's AI chief delivers keynote speech at VivaTech in Paris"](https://www.youtube.com/watch?v=EIo1YKEUac4) - accessible official video URL at the seeded source location; transcript not publicly accessible in this runtime

## Related

- [What does synthesising LeCun's architectural critique of Large Language Models with systems capability debt and citizen development arguments produce as a unified risk framework for regulated financial institutions?](https://davidamitchell.github.io/Research/research/2026-04-26-lecun-critique-citizen-development-enterprise-risk.html)
- [LLM Hallucinations: Types, Causes, and Current Mitigation Approaches](https://davidamitchell.github.io/Research/research/2026-03-05-llm-hallucination-mechanisms.html)
- [Are Human Brains Just Prediction Machines? Comparing Predictive Processing and Large Language Model next-token generation](https://davidamitchell.github.io/Research/research/2026-03-18-human-brain-prediction-machines.html)
- [Controlled hallucination, perception as construction, and the limits of "seeing reality directly"](https://davidamitchell.github.io/Research/research/2026-02-28-controlled-hallucination-perception-as-construction.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] Research question restated: what exactly is LeCun's argument that text-trained LLMs are not a sufficient path to autonomous machine intelligence, what technical mechanism underlies that claim, and how stable is that argument across the accessible 2022 to 2026 record?
- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://lemley-lecture.brown.edu/past-lecture/2026-lemley-lecture-featuring-ai-pioneer-yann-lecun; https://pioneerworks.org/broadcast/video/ai-yann-lecun-adam-brown] Scope confirmed: the item covers the paper, Brown lecture, accessible 2025 interview material, the seeded VivaTech URL as actually accessible, and the Pioneer Works discussion, while excluding third-party paraphrase as substantive evidence.
- [fact; source: https://podcasts.apple.com/us/podcast/why-cant-ai-make-its-own-discoveries-with-yann-lecun/id1522960417?i=1000699824574; https://www.youtube.com/watch?v=8sS9UJzb_t4; https://www.youtube.com/watch?v=EIo1YKEUac4; https://www.youtube.com/watch?v=ykfQD1_WPBQ] Constraint confirmed: transcript access is uneven, so the paper and Brown sources carry most of the technical weight, while several 2025 video sources are used mainly for chronology and host-published framing.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-lecun-critique-citizen-development-enterprise-risk.html; https://davidamitchell.github.io/Research/research/2026-03-18-human-brain-prediction-machines.html; https://davidamitchell.github.io/Research/research/2026-03-05-llm-hallucination-mechanisms.html] Prior-work cross-reference was completed before investigation; the closest completed items already use LeCun's critique downstream, but none reconstruct the argument from source material with this level of primary-source discipline.
- [fact; source: https://openreview.net/forum?id=BZ5a1r-kVsf] Output format confirmed: knowledge.

### §1 Question Decomposition

- **Root question:** What is LeCun's actual architectural argument against LLMs as a route to autonomous machine intelligence?
- **A. Core architecture**
  - A1. What does the 2022 paper say intelligence needs?
  - A2. What role do predictive world models play in planning, common sense, and safe action?
  - A3. What alternative architecture does LeCun propose?
- **B. LLM critique**
  - B1. What does LeCun say text-trained LLMs can do?
  - B2. What does he say they cannot do?
  - B3. What are his exact technical reasons for saying scaling is insufficient?
- **C. Domain boundary**
  - C1. Where do the accessible sources place the negative boundary, namely consequential real-world action?
  - C2. Do the accessible sources also support a positive boundary for constrained symbolic or formally checkable tasks?
  - C3. Which parts of that positive boundary remain weakly evidenced in this runtime?
- **D. Position evolution**
  - D1. Is the 2025 to 2026 public framing consistent with the 2022 paper?
  - D2. Does LeCun sharpen the rhetoric without changing the mechanism?
- **E. Output discipline**
  - E1. Which claims are direct facts from source text?
  - E2. Which claims are inferences from multiple accessible sources?
  - E3. Which claims remain assumptions because the needed transcript was not accessible?

### §2 Investigation

#### Source triage, substitutions, and failed-search notes

- [fact; source: https://lemley-lecture.brown.edu/past-lecture/2026-lemley-lecture-featuring-ai-pioneer-yann-lecun; https://livestream.brown.edu/lemley] Access note: query `site:livestream.brown.edu/lemley transcript Yann LeCun World Models Enabling the AI Revolution`, no public transcript indexed; Brown host pages exposed the event title and the full lecture link, and Brown News supplied direct quotations.
- [fact; source: https://pioneerworks.org/broadcast/video/ai-yann-lecun-adam-brown; https://www.youtube.com/watch?v=ykfQD1_WPBQ] Access note: query `site:pioneerworks.org/broadcast/video/ai-yann-lecun-adam-brown transcript`, no public transcript indexed in this runtime; the host page and official YouTube page were accessible and were used for event framing and chronology only.
- [fact; source: https://podcasts.apple.com/us/podcast/why-cant-ai-make-its-own-discoveries-with-yann-lecun/id1522960417?i=1000699824574; https://open.spotify.com/episode/2mOKCpKSUdaLkFPz8Shgbp; https://www.youtube.com/watch?v=8sS9UJzb_t4] Failed primary-source search record: queries `site:youtube.com Yann LeCun April 2025 interview world models LLMs` and `"Yann LeCun Explores the Future of AI Reasoning and World Models" transcript`, official episode and video pages were found but no public transcript was accessible in this runtime, so only host-published summary claims were used.
- [fact; source: https://www.youtube.com/watch?v=EIo1YKEUac4] Access note: the seeded VivaTech URL was accessible as a YouTube video page, but no public transcript or separate official event transcript was accessible in this runtime, so it could not bear detailed argumentative weight.

#### A. What the 2022 paper says intelligence requires

- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] LeCun's 2022 paper states that the answer to current machine-learning brittleness may lie in learning world models, meaning internal models of how the world works.
- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] The paper defines common sense as a collection of models of the world that tell an agent what is likely, plausible, and impossible.
- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] LeCun argues that with such world models, animals can predict the consequences of their actions, reason, plan, explore, imagine solutions, and avoid dangerous mistakes in unknown situations.
- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] The proposed architecture includes a perception module, short-term memory, a world model, an actor, a cost module, a critic, and a configurator, with the world model predicting future world states from imagined action sequences and the actor choosing the sequence that minimizes future cost.
- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] In the paper's account of active agency, causal models arise when the agent's actions influence sensory streams, allowing the system to learn to predict the consequences of its actions.

#### B. What the 2022 paper says about LLM limits

- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] The paper says Large Language Models possess a surprisingly large amount of background knowledge extracted from written text, but that much human common-sense knowledge is not represented in text and instead comes from interaction with the physical world.
- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] LeCun writes that because LLMs have no direct experience with an underlying reality, the kind of common-sense knowledge they exhibit is very shallow and can be disconnected from reality.
- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] In section 8.3.1, "Scaling is not enough," LeCun gives two explicit reasons that scaling LLM-style architectures is insufficient for human-level intelligence.
- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] First, he argues that current models operate on tokenized data and are generative, which works for text but is less suitable for continuous, high-dimensional signals such as video and does not represent complex uncertainty well in continuous spaces.
- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] Second, he argues that current models are only capable of very limited forms of reasoning because the absence of abstract latent variables precludes exploring multiple interpretations of a percept and searching for optimal courses of action to achieve a goal, and because dynamically specifying a goal in such models is essentially impossible.
- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] The strongest paper-level version of the "statistical pattern matcher" claim is therefore not merely that LLMs fit text statistics, but that their tokenized generative objective and missing abstract latent-variable machinery make them structurally weak at consequence-aware planning in the continuous world.

#### C. How the later public materials restate the argument

- [fact; source: https://podcasts.apple.com/us/podcast/why-cant-ai-make-its-own-discoveries-with-yann-lecun/id1522960417?i=1000699824574; https://open.spotify.com/episode/2mOKCpKSUdaLkFPz8Shgbp] The accessible March 2025 Big Technology episode summary says LeCun discusses why current AI models have been unable to invent new things despite possessing almost all the world's written knowledge, and says AI systems must build an abstract knowledge of the way the world operates to truly advance.
- [fact; source: https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] Brown University's official report quotes LeCun saying that current systems can manipulate language and fool us into thinking they are smart, but are completely helpless when it comes to the physical world.
- [fact; source: https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] The same Brown source quotes LeCun saying that almost none of today's agentic systems can predict the outcome of their actions, and that producing actions without being able to predict the consequences may be dangerous.
- [fact; source: https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] Brown also quotes LeCun defining a world model as a predictive system that, given the current state of the world and an imagined action, predicts the next state of the world, and saying that this predictive ability enables planning.
- [fact; source: https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] Brown's report says LeCun views the text-only Large Language Model approach as essentially a dead end.
- [fact; source: https://www.youtube.com/watch?v=ZbrfvMLZZK4; https://livestream.brown.edu/lemley] The official Brown lecture video page and Brown livestream page establish the lecture's identity and availability, but because a public transcript was not accessible in this runtime, this item does not rely on the video page alone for specific quoted phrasing.
- [inference; source: https://pioneerworks.org/broadcast/video/ai-yann-lecun-adam-brown; https://www.youtube.com/watch?v=ykfQD1_WPBQ] Pioneer Works presents the November 2025 conversation as a discussion of what LLMs can and cannot do and whether machines are anywhere close to thinking the way humans do, which is consistent with the same control question rather than a reversal of his earlier position.

#### D. Domain boundary, what is strongly supported and what is weaker

- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] The negative boundary is strongly supported in accessible primary material: LeCun explicitly treats consequence-predicting action in the world as the key requirement, and explicitly warns that systems that cannot predict action outcomes are dangerous when framed as agentic systems.
- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] The paper supports a narrower positive claim than the item's original wording implied: LeCun treats reasoning as optimization or constraint satisfaction over latent variables, which fits bounded objective-driven problems better than open-ended world action, but the exact "formal systems with external verifiers" formula was not directly recoverable from accessible primary text in this runtime.
- [assumption; source: https://www.youtube.com/watch?v=ykfQD1_WPBQ; https://www.youtube.com/watch?v=EIo1YKEUac4; https://www.youtube.com/watch?v=8sS9UJzb_t4] A full transcript of the seeded 2025 sources might sharpen this boundary further, but that cannot be asserted from the accessible material alone.

#### E. Position evolution check

- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://podcasts.apple.com/us/podcast/why-cant-ai-make-its-own-discoveries-with-yann-lecun/id1522960417?i=1000699824574; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer; https://pioneerworks.org/broadcast/video/ai-yann-lecun-adam-brown] Across the accessible 2022 to 2026 sources, LeCun's position remains structurally consistent: text-trained models capture linguistic knowledge, but intelligence that can reason, plan, and act safely requires an abstract predictive model of the world.
- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] What changes over time is not the mechanism but the bluntness of the public framing, from a technical position paper in 2022 to explicit public statements in 2026 that the text-only path to human-level intelligence is "complete BS."
- [assumption; source: https://www.youtube.com/watch?v=8sS9UJzb_t4; https://www.youtube.com/watch?v=ykfQD1_WPBQ; https://www.youtube.com/watch?v=EIo1YKEUac4] Because the April 2025, VivaTech, and November 2025 transcripts were not fully accessible here, subtle shifts of emphasis within those talks cannot be resolved with high confidence.

### §3 Reasoning

- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] The paper-level technical core is precise: a predictive world model is needed because action planning requires representing likely future world states and evaluating imagined action sequences before acting.
- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] The paper-level LLM critique is also precise: tokenized generative models are weak at continuous uncertainty and lack the abstract latent-variable machinery LeCun says is needed for richer reasoning and goal-conditioned search.
- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] Brown's public-language formulation, systems can manipulate language but are helpless in the physical world, is best read as a simplified restatement of the same architecture claim rather than as a separate thesis.
- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] The paper's account of reasoning as energy minimization or constraint satisfaction matters because it implies LeCun is not denying all machine reasoning; he is denying that token-only next-step generation is enough for the kinds of reasoning that require explicit search over latent possibilities and consequence prediction.
- [assumption; source: https://www.youtube.com/watch?v=ykfQD1_WPBQ; https://www.youtube.com/watch?v=EIo1YKEUac4; https://www.youtube.com/watch?v=8sS9UJzb_t4] The claim that LLMs lack an internal mechanism for detecting their own errors is only partially recoverable from accessible source text here, so it should be treated as an inference from the missing-world-model argument rather than as a separately quoted statement.

### §4 Consistency Check

- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] No accessible primary source in this session contradicted the 2022 paper's central architecture claim.
- [fact; source: https://podcasts.apple.com/us/podcast/why-cant-ai-make-its-own-discoveries-with-yann-lecun/id1522960417?i=1000699824574; https://pioneerworks.org/broadcast/video/ai-yann-lecun-adam-brown] The later host-published summaries align with the same world-knowledge-versus-text-knowledge distinction rather than with a softened or reversed position.
- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://www.youtube.com/watch?v=8sS9UJzb_t4; https://www.youtube.com/watch?v=EIo1YKEUac4; https://www.youtube.com/watch?v=ykfQD1_WPBQ] The main asymmetry in the evidence is that the negative boundary around consequential world action is explicit in accessible source text, while the positive boundary is limited by missing transcript-level access for the later talks.

### §5 Depth and Breadth Expansion

- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] **Technical lens:** LeCun's objection is not "language models are useless." It is that tokenized generative prediction over text is the wrong substrate for learning compact predictive representations of the continuous world and for planning under uncertainty.
- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] **Safety lens:** The world-model argument becomes a safety argument as soon as the system can act, because inability to forecast consequences turns autonomous action from a capability limitation into a danger mechanism.
- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] **Reasoning lens:** The paper treats reasoning as search or optimization over latent possibilities, not as single-pass token continuation, which clarifies why LeCun's preferred architecture fits bounded objective-driven reasoning better than unguided world action.
- [inference; source: https://podcasts.apple.com/us/podcast/why-cant-ai-make-its-own-discoveries-with-yann-lecun/id1522960417?i=1000699824574; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] **Historical lens:** The later public materials sharpen the rhetoric from "scaling is not enough" to "the text-only path is a dead end," but they continue to point back to the same abstract-world-knowledge requirement.

### §6 Synthesis

**Executive summary:**

- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] LeCun's core claim is that text-trained Large Language Models are not a sufficient path to autonomous machine intelligence because autonomous intelligence requires a predictive world model that can represent plausible future states, evaluate imagined actions, and support planning before acting.
- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] The precise technical basis in the accessible paper is twofold: tokenized generative models handle discrete text well but are poorly suited to continuous, uncertainty-rich world modelling, and they lack the abstract latent-variable machinery LeCun says is required for richer reasoning and goal-directed search.
- [fact; source: https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer; https://www.youtube.com/watch?v=ZbrfvMLZZK4] The later Brown lecture material sharpens that argument into a public warning, namely that systems which manipulate language but cannot predict the consequences of their actions are unsafe foundations for agentic action in the physical or operational world.
- [inference; source: https://pioneerworks.org/broadcast/video/ai-yann-lecun-adam-brown; https://podcasts.apple.com/us/podcast/why-cant-ai-make-its-own-discoveries-with-yann-lecun/id1522960417?i=1000699824574; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] Across the accessible 2025 to 2026 record, LeCun's stance appears consistent and rhetorically sharper, but the exact positive boundary around "formal systems with external verifiers" remains only partially recoverable here because the needed transcripts were not fully accessible in this runtime.

**Key findings:**

1. [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] **High confidence:** In the 2022 paper and Brown's 2026 coverage, LeCun argues that common sense, planning, and safe action depend on predictive world models that encode what states of the world are likely, plausible, or impossible and that let an agent evaluate imagined action sequences before acting.
2. [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] **Medium confidence:** LeCun gives two explicit technical reasons that scaling token-based generative models is insufficient, namely that they are ill-suited to representing uncertainty in continuous high-dimensional domains and that their lack of abstract latent variables limits multi-interpretation reasoning and goal-directed search.
3. [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] **Medium confidence:** The paper does not claim that LLMs know nothing; instead, it says they extract substantial background knowledge from text while still exhibiting shallow common sense because text alone omits much of the physical and causal structure humans learn through worldly interaction.
4. [fact; source: https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer; https://openreview.net/pdf?id=BZ5a1r-kVsf] **High confidence:** By the Brown lecture, LeCun is publicly applying the same mechanism to agentic systems, arguing that systems which can produce actions in the world but cannot predict the outcomes of those actions are dangerous foundations for autonomous behaviour.
5. [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] **Medium confidence:** The paper suggests a narrower positive claim than the item's original wording, because it frames reasoning as optimization or constraint satisfaction over latent possibilities, which fits bounded objective-driven problems better than open-ended world action without itself specifying a full list of safe domains.
6. [inference; source: https://podcasts.apple.com/us/podcast/why-cant-ai-make-its-own-discoveries-with-yann-lecun/id1522960417?i=1000699824574; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer; https://pioneerworks.org/broadcast/video/ai-yann-lecun-adam-brown] **Medium confidence:** The accessible 2025 to 2026 host materials indicate continuity rather than reversal, because they keep returning to the same distinction between text knowledge and abstract world knowledge even when the public rhetoric becomes much blunter.
7. [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://www.youtube.com/watch?v=ZbrfvMLZZK4; https://www.youtube.com/watch?v=ykfQD1_WPBQ] **Low confidence:** The item's original positive-boundary wording about "formal systems with external verifiers" is directionally compatible with the accessible evidence, but it could not be directly confirmed as LeCun's own exact formulation from the primary material available in this runtime.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Autonomous intelligence requires predictive world models for plausible-state judgement, consequence prediction, and planning. | https://openreview.net/pdf?id=BZ5a1r-kVsf ; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer | high | Core mechanism is stated in the paper and echoed in Brown's official quotation about planning. |
| [fact] Scaling LLM-style models is insufficient because tokenized generative training handles continuous uncertainty poorly and lacks latent-variable reasoning machinery. | https://openreview.net/pdf?id=BZ5a1r-kVsf | medium | Section 8.3.1 provides the two explicit reasons, but this row rests on one source. |
| [fact] LLMs extract background knowledge from text but exhibit shallow common sense because they lack direct experience with underlying reality. | https://openreview.net/pdf?id=BZ5a1r-kVsf | medium | Directly stated in the paper, but this row rests on one source. |
| [fact] Agentic systems that cannot predict action outcomes are dangerous. | https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer ; https://openreview.net/pdf?id=BZ5a1r-kVsf | high | Brown provides the direct quotation and the paper provides the underlying consequence-prediction mechanism. |
| [inference] The paper suggests a narrower positive claim than the item's original wording because it frames reasoning as optimization or constraint satisfaction over latent possibilities. | https://openreview.net/pdf?id=BZ5a1r-kVsf | medium | This is a paper-grounded inference, not a transcript-level quote from a later talk. |
| [inference] The accessible 2025 to 2026 host materials show continuity of the same world-knowledge-versus-text-knowledge critique. | https://podcasts.apple.com/us/podcast/why-cant-ai-make-its-own-discoveries-with-yann-lecun/id1522960417?i=1000699824574 ; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer ; https://pioneerworks.org/broadcast/video/ai-yann-lecun-adam-brown | medium | Host summaries are thinner than the paper, so this is inferential rather than transcript-level. |
| [assumption] The exact phrase "formal systems with external verifiers" is part of LeCun's explicit positive boundary. | https://www.youtube.com/watch?v=8sS9UJzb_t4 ; https://www.youtube.com/watch?v=EIo1YKEUac4 ; https://www.youtube.com/watch?v=ykfQD1_WPBQ | low | Compatible with accessible material but not directly recoverable here. |

**Assumptions:**

- [assumption; source: https://www.youtube.com/watch?v=8sS9UJzb_t4; https://www.youtube.com/watch?v=EIo1YKEUac4; https://www.youtube.com/watch?v=ykfQD1_WPBQ] **Assumption:** The inaccessible transcript-level detail in the 2025 talks would likely reinforce rather than reverse the paper-level mechanism. **Justification:** every accessible host summary remains aligned with the world-model critique, but the missing transcripts prevent a stronger claim.
- [assumption; source: https://www.youtube.com/watch?v=8sS9UJzb_t4; https://www.youtube.com/watch?v=EIo1YKEUac4; https://www.youtube.com/watch?v=ykfQD1_WPBQ] **Assumption:** The inaccessible transcript detail in the 2025 talks may spell out a broader positive boundary around constrained, optimizable, or externally verifiable reasoning tasks. **Justification:** the accessible host material points in that direction, but the missing transcripts prevent direct confirmation.

**Analysis:**

- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] The paper should carry the most evidential weight because it contains the only fully accessible primary technical exposition of LeCun's mechanism in this session.
- [inference; source: https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer; https://www.youtube.com/watch?v=ZbrfvMLZZK4] Brown should carry the next-highest weight because it provides direct quotations and an official lecture context that restates the planning-and-consequence argument in public-facing language.
- [inference; source: https://podcasts.apple.com/us/podcast/why-cant-ai-make-its-own-discoveries-with-yann-lecun/id1522960417?i=1000699824574; https://pioneerworks.org/broadcast/video/ai-yann-lecun-adam-brown] The Apple Podcasts and Pioneer Works pages are useful mainly for chronology and continuity because they are host-published summaries rather than full transcripts.
- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] The resulting reconstruction is therefore strongest on the negative claim, namely that text-only LLMs are architecturally unsuited for autonomous world action, and weaker on the most detailed version of the positive claim, namely exactly which constrained domains LeCun still treats as suitable.

**Risks, gaps, uncertainties:**

- [fact; source: https://www.youtube.com/watch?v=8sS9UJzb_t4; https://www.youtube.com/watch?v=EIo1YKEUac4; https://www.youtube.com/watch?v=ykfQD1_WPBQ] Full transcripts for the April 2025, seeded VivaTech, and November 2025 video sources were not publicly accessible in this runtime, so those sources could not support line-by-line reconstruction.
- [fact; source: https://www.youtube.com/watch?v=EIo1YKEUac4] The seeded VivaTech URL was accessible only as a YouTube page in this session, so it could serve as a checked source location but not as a detailed evidence source.
- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://www.youtube.com/watch?v=ZbrfvMLZZK4] The claim that LLMs lack an internal mechanism for detecting their own errors is only indirectly supported here through the missing-world-model and shallow-common-sense argument, not through a direct accessible quote using that exact phrasing.
- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://www.youtube.com/watch?v=8sS9UJzb_t4; https://www.youtube.com/watch?v=EIo1YKEUac4; https://www.youtube.com/watch?v=ykfQD1_WPBQ] The positive boundary around formal or externally verifiable tasks remains medium-to-low confidence because the paper supports only a general optimization-and-constraint-satisfaction framing while the later talk transcripts were not fully accessible.

**Open questions:**

- [inference; source: https://www.youtube.com/watch?v=8sS9UJzb_t4; https://www.youtube.com/watch?v=ykfQD1_WPBQ] Do the inaccessible 2025 transcripts contain a more explicit statement that LLMs are acceptable in code or other externally checkable domains while remaining unfit for consequential world action?
- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] How far does LeCun think optimization-based reasoning can go without a richer world model when the task is symbolic rather than physical?
- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] Which parts of LeCun's proposed architecture, especially the world model, critic, and configurator, are intended as immediate engineering proposals versus long-horizon research directions?

### §7 Recursive Review

- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer; https://www.youtube.com/watch?v=ZbrfvMLZZK4; https://podcasts.apple.com/us/podcast/why-cant-ai-make-its-own-discoveries-with-yann-lecun/id1522960417?i=1000699824574; https://pioneerworks.org/broadcast/video/ai-yann-lecun-adam-brown] Every substantive claim in this item now maps either to the paper, to official Brown material, to the official Brown lecture video, or to host-published episode pages, and thinner sources are used only for chronology and continuity.
- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://www.youtube.com/watch?v=ZbrfvMLZZK4] The strongest likely review challenge, the positive boundary around formal or verifiable reasoning, is now explicitly marked as weaker evidence than the negative boundary around world action.
- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] Acronym first-use checks were applied for Large Language Models (LLMs), Joint Embedding Predictive Architecture (JEPA), Hierarchical Joint Embedding Predictive Architecture (H-JEPA), and Self-Supervised Learning (SSL).
- [fact; source: https://www.youtube.com/watch?v=8sS9UJzb_t4; https://www.youtube.com/watch?v=EIo1YKEUac4; https://www.youtube.com/watch?v=ykfQD1_WPBQ] The remaining uncertainty is explicit rather than hidden: inaccessible 2025 transcripts limit how strongly this item can claim to have reconstructed every nuance of LeCun's later talks.

---

## Findings

### Executive Summary

- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] LeCun's core claim is that text-trained Large Language Models are not a sufficient path to autonomous machine intelligence because autonomous intelligence requires a predictive world model that can represent plausible future states, evaluate imagined actions, and support planning before acting.
- [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] The precise technical basis in the accessible paper is twofold: tokenized generative models handle discrete text well but are poorly suited to continuous, uncertainty-rich world modelling, and they lack the abstract latent-variable machinery LeCun says is required for richer reasoning and goal-directed search.
- [fact; source: https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer; https://www.youtube.com/watch?v=ZbrfvMLZZK4] The later Brown lecture material sharpens that argument into a public warning, namely that systems which manipulate language but cannot predict the consequences of their actions are unsafe foundations for agentic action in the physical or operational world.
- [inference; source: https://pioneerworks.org/broadcast/video/ai-yann-lecun-adam-brown; https://podcasts.apple.com/us/podcast/why-cant-ai-make-its-own-discoveries-with-yann-lecun/id1522960417?i=1000699824574; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] Across the accessible 2025 to 2026 record, LeCun's stance appears consistent and rhetorically sharper, but the exact positive boundary around "formal systems with external verifiers" remains only partially recoverable here because the needed transcripts were not fully accessible in this runtime.

### Key Findings

1. [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] **High confidence:** In the 2022 paper and Brown's 2026 coverage, LeCun argues that common sense, planning, and safe action depend on predictive world models that encode what states of the world are likely, plausible, or impossible and that let an agent evaluate imagined action sequences before acting.
2. [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] **Medium confidence:** LeCun gives two explicit technical reasons that scaling token-based generative models is insufficient, namely that they are ill-suited to representing uncertainty in continuous high-dimensional domains and that their lack of abstract latent variables limits multi-interpretation reasoning and goal-directed search.
3. [fact; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] **Medium confidence:** The paper does not claim that LLMs know nothing; instead, it says they extract substantial background knowledge from text while still exhibiting shallow common sense because text alone omits much of the physical and causal structure humans learn through worldly interaction.
4. [fact; source: https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer; https://openreview.net/pdf?id=BZ5a1r-kVsf] **High confidence:** By the Brown lecture, LeCun is publicly applying the same mechanism to agentic systems, arguing that systems which can produce actions in the world but cannot predict the outcomes of those actions are dangerous foundations for autonomous behaviour.
5. [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] **Medium confidence:** The paper suggests a narrower positive claim than the item's original wording, because it frames reasoning as optimization or constraint satisfaction over latent possibilities, which fits bounded objective-driven problems better than open-ended world action without itself specifying a full list of safe domains.
6. [inference; source: https://podcasts.apple.com/us/podcast/why-cant-ai-make-its-own-discoveries-with-yann-lecun/id1522960417?i=1000699824574; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer; https://pioneerworks.org/broadcast/video/ai-yann-lecun-adam-brown] **Medium confidence:** The accessible 2025 to 2026 host materials indicate continuity rather than reversal, because they keep returning to the same distinction between text knowledge and abstract world knowledge even when the public rhetoric becomes much blunter.
7. [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://www.youtube.com/watch?v=ZbrfvMLZZK4; https://www.youtube.com/watch?v=ykfQD1_WPBQ] **Low confidence:** The item's original positive-boundary wording about "formal systems with external verifiers" is directionally compatible with the accessible evidence, but it could not be directly confirmed as LeCun's own exact formulation from the primary material available in this runtime.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Autonomous intelligence requires predictive world models for plausible-state judgement, consequence prediction, and planning. | https://openreview.net/pdf?id=BZ5a1r-kVsf ; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer | high | Core mechanism is stated in the paper and echoed in Brown's official quotation about planning. |
| [fact] Scaling LLM-style models is insufficient because tokenized generative training handles continuous uncertainty poorly and lacks latent-variable reasoning machinery. | https://openreview.net/pdf?id=BZ5a1r-kVsf | medium | Section 8.3.1 provides the two explicit reasons, but this row rests on one source. |
| [fact] LLMs extract background knowledge from text but exhibit shallow common sense because they lack direct experience with underlying reality. | https://openreview.net/pdf?id=BZ5a1r-kVsf | medium | Directly stated in the paper, but this row rests on one source. |
| [fact] Agentic systems that cannot predict action outcomes are dangerous. | https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer ; https://openreview.net/pdf?id=BZ5a1r-kVsf | high | Brown provides the direct quotation and the paper provides the underlying consequence-prediction mechanism. |
| [inference] The paper suggests a narrower positive claim than the item's original wording because it frames reasoning as optimization or constraint satisfaction over latent possibilities. | https://openreview.net/pdf?id=BZ5a1r-kVsf | medium | This is a paper-grounded inference, not a transcript-level quote from a later talk. |
| [inference] The accessible 2025 to 2026 host materials show continuity of the same world-knowledge-versus-text-knowledge critique. | https://podcasts.apple.com/us/podcast/why-cant-ai-make-its-own-discoveries-with-yann-lecun/id1522960417?i=1000699824574 ; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer ; https://pioneerworks.org/broadcast/video/ai-yann-lecun-adam-brown | medium | Host summaries are thinner than the paper, so this is inferential rather than transcript-level. |
| [assumption] The exact phrase "formal systems with external verifiers" is part of LeCun's explicit positive boundary. | https://www.youtube.com/watch?v=8sS9UJzb_t4 ; https://www.youtube.com/watch?v=EIo1YKEUac4 ; https://www.youtube.com/watch?v=ykfQD1_WPBQ | low | Compatible with accessible material but not directly recoverable here. |

### Assumptions

- [assumption; source: https://www.youtube.com/watch?v=8sS9UJzb_t4; https://www.youtube.com/watch?v=EIo1YKEUac4; https://www.youtube.com/watch?v=ykfQD1_WPBQ] **Assumption:** The inaccessible transcript-level detail in the 2025 talks would likely reinforce rather than reverse the paper-level mechanism. **Justification:** every accessible host summary remains aligned with the world-model critique, but the missing transcripts prevent a stronger claim.
- [assumption; source: https://www.youtube.com/watch?v=8sS9UJzb_t4; https://www.youtube.com/watch?v=EIo1YKEUac4; https://www.youtube.com/watch?v=ykfQD1_WPBQ] **Assumption:** The inaccessible transcript detail in the 2025 talks may spell out a broader positive boundary around constrained, optimizable, or externally verifiable reasoning tasks. **Justification:** the accessible host material points in that direction, but the missing transcripts prevent direct confirmation.

### Analysis

- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] The paper should carry the most evidential weight because it contains the only fully accessible primary technical exposition of LeCun's mechanism in this session.
- [inference; source: https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer; https://www.youtube.com/watch?v=ZbrfvMLZZK4] Brown should carry the next-highest weight because it provides direct quotations and an official lecture context that restates the planning-and-consequence argument in public-facing language.
- [inference; source: https://podcasts.apple.com/us/podcast/why-cant-ai-make-its-own-discoveries-with-yann-lecun/id1522960417?i=1000699824574; https://pioneerworks.org/broadcast/video/ai-yann-lecun-adam-brown] The Apple Podcasts and Pioneer Works pages are useful mainly for chronology and continuity because they are host-published summaries rather than full transcripts.
- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] The resulting reconstruction is therefore strongest on the negative claim, namely that text-only LLMs are architecturally unsuited for autonomous world action, and weaker on the most detailed version of the positive claim, namely exactly which constrained domains LeCun still treats as suitable.

### Risks, Gaps, and Uncertainties

- [fact; source: https://www.youtube.com/watch?v=8sS9UJzb_t4; https://www.youtube.com/watch?v=EIo1YKEUac4; https://www.youtube.com/watch?v=ykfQD1_WPBQ] Full transcripts for the April 2025, seeded VivaTech, and November 2025 video sources were not publicly accessible in this runtime, so those sources could not support line-by-line reconstruction.
- [fact; source: https://www.youtube.com/watch?v=EIo1YKEUac4] The seeded VivaTech URL was accessible only as a YouTube page in this session, so it could serve as a checked source location but not as a detailed evidence source.
- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://www.youtube.com/watch?v=ZbrfvMLZZK4] The claim that LLMs lack an internal mechanism for detecting their own errors is only indirectly supported here through the missing-world-model and shallow-common-sense argument, not through a direct accessible quote using that exact phrasing.
- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf; https://www.youtube.com/watch?v=8sS9UJzb_t4; https://www.youtube.com/watch?v=EIo1YKEUac4; https://www.youtube.com/watch?v=ykfQD1_WPBQ] The positive boundary around formal or externally verifiable tasks remains medium-to-low confidence because the paper supports only a general optimization-and-constraint-satisfaction framing while the later talk transcripts were not fully accessible.

### Open Questions

- [inference; source: https://www.youtube.com/watch?v=8sS9UJzb_t4; https://www.youtube.com/watch?v=ykfQD1_WPBQ] Do the inaccessible 2025 transcripts contain a more explicit statement that LLMs are acceptable in code or other externally checkable domains while remaining unfit for consequential world action?
- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] How far does LeCun think optimization-based reasoning can go without a richer world model when the task is symbolic rather than physical?
- [inference; source: https://openreview.net/pdf?id=BZ5a1r-kVsf] Which parts of LeCun's proposed architecture, especially the world model, critic, and configurator, are intended as immediate engineering proposals versus long-horizon research directions?

---

## Output

- Type: knowledge
- Description: Reconstructed LeCun's accessible primary-source argument against text-only Large Language Models as a route to autonomous machine intelligence, separating high-confidence paper-level mechanism from lower-confidence chronology claims where transcript access was incomplete.
- Links:
  - https://openreview.net/forum?id=BZ5a1r-kVsf
  - https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer
  - https://www.youtube.com/watch?v=ZbrfvMLZZK4
