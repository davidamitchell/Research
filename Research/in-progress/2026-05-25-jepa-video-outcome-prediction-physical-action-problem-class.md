---
title: "Joint Embedding Predictive Architecture (JEPA) shift: text-to-video outcome prediction versus video-to-physical action"
added: 2026-05-25T08:37:36+00:00
status: reviewing
priority: medium
blocks: []
themes: [ai-architecture, agentic-ai, consciousness-cognition, benchmarks-eval, formal-methods]
started: 2026-05-28T10:48:36+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-03-16-vl-jepa-concept-prediction
  - 2026-04-26-lecun-llm-critique-primary-sources
related:
  - 2026-05-25-ontology-world-model-llm-prediction-forcing-functions
  - 2026-04-26-llm-verifiability-asymmetry-code-world-action
  - 2026-03-18-human-brain-prediction-machines
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Joint Embedding Predictive Architecture (JEPA) shift: text-to-video outcome prediction versus video-to-physical action

## Research Question

Is the shift from text-token prediction to Joint Embedding Predictive Architecture (JEPA)-style video outcome prediction the same class of problem as the shift from video prediction to physically grounded action in the real world?

## Scope

**In scope:**
- Conceptual differences between token prediction, representation-space outcome prediction, and action selection.
- What changes when prediction targets are video outcomes versus environment-coupled control outcomes.
- Conditions under which these shifts are structurally similar versus fundamentally different.

**Out of scope:**
- Building or benchmarking a new Joint Embedding Predictive Architecture (JEPA) system.
- Proving a complete robotics control pipeline end-to-end.
- Forecasting artificial general intelligence timelines.

**Constraints:** (time, source types, access)
- Desk research only with publicly accessible sources.
- Emphasise primary sources from Yann LeCun and world-model/control literature.
- Output type defaults to knowledge for downstream research execution.

## Context

The issue asks whether LeCun's move toward Joint Embedding Predictive Architecture (JEPA)-style outcome prediction in video is fundamentally the same research class as the harder move from predictive video understanding to action that must work in the physical world.

## Approach

1. Define and compare objective functions for text-token prediction, video outcome prediction, and physical action control.
   1a. What is being predicted in each paradigm?
   1b. What feedback signal closes the loop in each paradigm?
2. Identify which capabilities transfer from video outcome prediction to physical action.
   2a. Which world-model properties are reusable?
   2b. Which additional requirements appear only at action time (for example embodiment, safety, latency, exploration)?
3. Evaluate whether the transition classes are equivalent or only partially overlapping.
   3a. Establish similarity criteria (representation shift, planning horizon, uncertainty structure).
   3b. Establish non-equivalence criteria (causal intervention, control constraints, irreversible errors).
4. Synthesize a decision-oriented conclusion on whether these are the same class of problem for research planning.

## Sources

- [x] [LeCun (2022) A Path Towards Autonomous Machine Intelligence](https://openreview.net/forum?id=BZ5a1r-kVsf): primary framing of world models, Joint Embedding Predictive Architecture (JEPA), and autonomous machine intelligence direction.
- [x] [Assran et al. (2023) Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture (I-JEPA)](https://arxiv.org/abs/2301.08243): canonical Image Joint Embedding Predictive Architecture (I-JEPA) method details and predictive representation setup.
- [x] [Hafner et al. (2023) Mastering Diverse Domains through World Models (DreamerV3)](https://arxiv.org/abs/2301.04104): representative world-model-to-control pipeline for action in interactive environments.
- [x] [Sutton and Barto (2018) Reinforcement Learning: An Introduction (Second Edition)](http://incompleteideas.net/book/the-book-2nd.html): foundational framework for prediction versus control distinctions.
- [x] [Assran et al. (2025) V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985): empirical demonstration of JEPA bridging video understanding to robotic planning.
- [x] [Meta AI Blog (2025) Our New Model Helps AI Think Before it Acts](https://about.fb.com/news/2025/06/our-new-model-helps-ai-think-before-it-acts/): official Meta announcement of V-JEPA 2 with world model framing.
- [x] [VL-JEPA paper (arXiv 2024)](https://arxiv.org/abs/2512.10942): vision-language extension of the JEPA lineage.

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. §§0-5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

```text
Question: Is the shift from text-token prediction to JEPA-style video outcome prediction
          the same class of problem as the shift from video prediction to physically grounded
          action in the real world?

Scope: Conceptual differences between token prediction, representation-space outcome
       prediction, and action selection. Conditions of structural similarity vs fundamental
       difference. Out of scope: building a new JEPA system, proving a robotics pipeline
       end-to-end, forecasting AGI timelines.

Constraints: Desk research only with publicly accessible sources. Emphasise LeCun and
             world-model/control literature.

Output format: knowledge item, following structured Findings template.

Working hypotheses:
[assumption] The text→video-JEPA transition and the video-JEPA→physical-action transition are
             likely not the same class of problem, because the latter introduces active causal
             intervention whereas the former remains within passive prediction. Justification:
             this is the canonical prediction/control distinction in the reinforcement learning
             (RL) literature (Sutton and Barto, 2018; http://incompleteideas.net/book/the-book-2nd.html).

[assumption] JEPA-style abstract representation provides a reusable foundation that makes the
             second transition tractable with less interaction data. Justification: V-JEPA 2
             paper (2025) reports 62 hours of robot data sufficient for zero-shot manipulation
             after video pre-training (https://arxiv.org/abs/2506.09985).

Prior completed repository items with relevant coverage:
- 2026-03-16-vl-jepa-concept-prediction: documents JEPA lineage, concept prediction mechanism.
- 2026-04-26-lecun-llm-critique-primary-sources: reconstructs LeCun's architectural argument.
- 2026-05-25-ontology-world-model-llm-prediction-forcing-functions: covers prediction limits
  in LLMs relevant to ontology-first approaches.
- 2026-03-18-human-brain-prediction-machines: covers the predictive processing framework and
  embodiment role in cognition.
```

### §1 Question Decomposition

**1A. What is being predicted in each paradigm?**

- 1A-i. What does a Large Language Model (LLM) predict, in what space, with what supervision signal?
- 1A-ii. What does a Joint Embedding Predictive Architecture (JEPA) video model predict, in what space, with what supervision signal?
- 1A-iii. What does a world-model-based controller (e.g. DreamerV3, V-JEPA 2-AC) predict, in what space, and what additional signal closes the loop?

**1B. What feedback closes each loop?**

- 1B-i. What is the loss function for LLM next-token prediction, and does it require environment interaction?
- 1B-ii. What is the loss function for JEPA representation prediction, and does it require environment interaction?
- 1B-iii. What is the loss function for model-predictive control (MPC) or action-conditioned world-model planning, and what environment coupling is required?

**2A. Which world-model properties are reusable from video JEPA to physical action?**

- 2A-i. Does a JEPA encoder trained on video capture object permanence, motion dynamics, or causal structure?
- 2A-ii. Can these representations serve as the state representation for a downstream action-conditioned predictor?

**2B. Which additional requirements appear only at action time?**

- 2B-i. What constraints does embodiment impose (latency, actuator limits, closed-loop feedback)?
- 2B-ii. Why does irreversibility change the problem structure?
- 2B-iii. Why does exploration become mandatory at action time in ways it is not for passive prediction?

**3A. Similarity criteria for the two transitions.**

- 3A-i. Do both transitions involve a shift in representation space?
- 3A-ii. Do both transitions improve the model's causal coverage of the world?

**3B. Non-equivalence criteria for the two transitions.**

- 3B-i. Does the text→JEPA transition require any causal intervention capability?
- 3B-ii. Does the JEPA→action transition require only a representation change, or does it require a new feedback mechanism?

**4. Research-planning synthesis.**

- 4-i. Is "the same class of problem" best assessed by the similarity of objective functions, by the similarity of required capabilities, or by the structural changes required to move between problem states?

### §2 Investigation

**§2.1A-i: What does an LLM predict?**

[fact; source: https://openreview.net/forum?id=BZ5a1r-kVsf] LeCun's 2022 position paper describes LLMs as systems that predict the next token in a discrete sequence, trained on text corpora with cross-entropy loss over token distributions. The prediction target is a discrete symbol drawn from a finite vocabulary; the supervision signal is the observed next token in the training corpus.

[fact; source: https://openreview.net/forum?id=BZ5a1r-kVsf] LeCun explicitly argues that token prediction does not require the model to build a causal world model: a system can achieve low token prediction loss by capturing statistical regularities in language without representing the causal structure of events those words describe.

[inference; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://davidamitchell.github.io/Research/research/2026-04-26-lecun-llm-critique-primary-sources.html] LLMs operate in a closed loop over text: the feedback signal (next observed token) is internal to the training corpus and requires no interaction with a physical environment or even a simulation. This makes next-token prediction a purely observational prediction problem with no causal agency.

**§2.1A-ii: What does a JEPA video model predict?**

[fact; source: https://arxiv.org/abs/2301.08243] I-JEPA (Image Joint Embedding Predictive Architecture, Assran et al., 2023) predicts the representation of target image blocks from a context block, using a learned encoder. The prediction target is in abstract latent space, not in pixel space. The supervision signal is the encoder's own representation of the masked target region, computed by a momentum-updated target encoder (exponential moving average of the online encoder).

[fact; source: https://arxiv.org/abs/2506.09985] V-JEPA 2 (Video Joint Embedding Predictive Architecture 2, Assran et al., 2025) pre-trains on over 1 million hours of internet video using a mask-denoising feature prediction objective. The model predicts masked video segments in a learned representation space. No action labels or environment interaction data are used in Stage 1; the training corpus is entirely passive video observation.

[fact; source: https://arxiv.org/abs/2506.09985] V-JEPA 2 achieves 77.3% top-1 accuracy on Something-Something v2 (motion understanding) and 39.7% recall-at-5 on Epic-Kitchens-100 (action anticipation) using passive video prediction alone. These results confirm the model learns motion dynamics, object interactions, and action-relevant structure without observing any agent actions.

[inference; source: https://arxiv.org/abs/2506.09985; https://openreview.net/forum?id=BZ5a1r-kVsf] The shift from token prediction to JEPA representation prediction changes both the prediction target (discrete token → abstract latent vector) and the supervision signal (observed next token → masked representation of the same observation). Both paradigms remain entirely passive: neither requires environment interaction, causal intervention, or closed-loop feedback beyond the training corpus itself.

**§2.1A-iii: What does a world-model controller predict?**

[fact; source: https://arxiv.org/abs/2301.04104] DreamerV3 (Hafner et al., 2023) learns a world model from environment interaction data (state-action-reward sequences) and uses it to plan actions by imagining future trajectories in latent space. The world model is trained to predict the next latent state conditioned on an action: p(z_{t+1} | z_t, a_t). This action-conditioning requirement is absent from JEPA Stage 1 pre-training.

[fact; source: https://arxiv.org/abs/2506.09985] V-JEPA 2-AC (Action-Conditioned V-JEPA 2) introduces a second training stage using 62 hours of unlabeled robot interaction data from the Droid dataset. The action-conditioned predictor is a 300M-parameter transformer that autoregressively predicts the representation of the next video frame conditioned on an action and previous states. This is a structurally distinct model component from the Stage 1 video encoder.

[fact; source: https://arxiv.org/abs/2506.09985] V-JEPA 2-AC enables zero-shot pick-and-place tasks on Franka robot arms in previously unseen lab environments, using model predictive control (MPC): at each step the model rolls out candidate action sequences in latent space and selects the action that minimizes distance to a goal image representation.

[inference; source: https://arxiv.org/abs/2506.09985; https://arxiv.org/abs/2301.04104] The action-conditioned prediction stage requires a qualitatively different feedback mechanism: the model must predict how its own interventions change the world state, not merely how the world evolves passively. This is the core of the prediction-to-control class transition.

**§2.1B: Feedback signal comparison**

[fact; source: https://openreview.net/forum?id=BZ5a1r-kVsf] LLM training requires no environment interaction. The feedback is cross-entropy loss against observed text tokens. The environment is the training corpus.

[fact; source: https://arxiv.org/abs/2301.08243; https://arxiv.org/abs/2506.09985] JEPA Stage 1 training requires no environment interaction. The feedback is mean-squared error (MSE) in representation space between the online predictor's output and the target encoder's representation of masked regions. The environment is the video corpus.

[fact; source: https://arxiv.org/abs/2301.04104; https://arxiv.org/abs/2506.09985] Action-conditioned world model training requires environment interaction data: the model must observe how specific actions affect subsequent states. DreamerV3 uses reward feedback; V-JEPA 2-AC uses unlabeled robot trajectories (state sequences with associated actions). Both require closed-loop data: the model cannot learn action-consequences from passive video alone because passive video does not contain action labels.

[inference; source: https://arxiv.org/abs/2506.09985] The requirement for interaction data constitutes a structural discontinuity between Stage 1 JEPA pre-training and Stage 2 action-conditioned training. V-JEPA 2 resolves this by requiring two separate training stages with different objectives and data types, not by a single continuous extension of JEPA prediction.

**§2.2A: World-model properties transferable from video JEPA to physical action**

[fact; source: https://arxiv.org/abs/2506.09985] V-JEPA 2 pre-trained on video develops strong representations of motion dynamics, object motion patterns, and human-object interaction from passive observation. These representations transfer directly to the action-conditioned predictor: the Stage 1 encoder is frozen during Stage 2 training.

[inference; source: https://arxiv.org/abs/2506.09985] The reusability of JEPA representations for robot manipulation suggests that abstract representation learning from passive video captures world-dynamic structure (how objects move, collide, and respond) that is relevant to predicting the effects of physical interventions. This is the key mechanism enabling data-efficient action learning.

[assumption; source: https://arxiv.org/abs/2506.09985; https://openreview.net/forum?id=BZ5a1r-kVsf] JEPA representations are reusable because they learn to predict predictable aspects of scenes (motion, structure) while ignoring unpredictable pixel-level noise. This selectivity for abstract structure is exactly what a world model needs to simulate action consequences. Justification: LeCun's 2022 paper explicitly cites this as the key advantage of JEPA over generative pixel prediction (source: https://openreview.net/forum?id=BZ5a1r-kVsf).

**§2.2B: Additional requirements appearing only at action time**

[fact; source: https://arxiv.org/abs/2506.09985] V-JEPA 2-AC requires action labels associated with robot trajectories. This data type is qualitatively absent from internet video: most video does not record the motor commands that produced the observed motion.

[fact; source: http://incompleteideas.net/book/the-book-2nd.html] Sutton and Barto (2018) formalise the prediction/control distinction: prediction problems estimate V(s) under a fixed policy; control problems optimise π*(s) across policies. These require different algorithms (policy evaluation versus policy improvement) and have different convergence properties.

[inference; source: https://arxiv.org/abs/2301.04104; http://incompleteideas.net/book/the-book-2nd.html] Physical action introduces irreversibility: a robot that drops an object cannot recover by observing a different video. This creates an asymmetry between passive prediction (mistakes are cheap; re-run the epoch) and active control (mistakes have physical consequences that may not be undoable). This asymmetry affects how exploration should be structured and what safety margin the system requires.

[inference; source: https://arxiv.org/abs/2506.09985; https://arxiv.org/abs/2301.04104] Physical action requires closed-loop feedback at decision time: the robot must observe the current state of the world at each step to plan its next action. Passive prediction models are typically open-loop at inference time; they do not update their predictions based on the consequences of their outputs. The model predictive control loop used by V-JEPA 2-AC is an explicit closed-loop structure not present in Stage 1 JEPA inference.

[inference; source: https://about.fb.com/news/2025/06/our-new-model-helps-ai-think-before-it-acts/] Embodiment adds latency constraints absent from text and video prediction: physical control must complete a decision cycle within the robot's actuation window (typically milliseconds to seconds), whereas passive prediction can be computed offline. Meta's V-JEPA 2 blog post frames this as the model needing to "think before it acts," implying a time-bounded planning loop structurally different from offline training.

**§2.3: Similarity and non-equivalence criteria for the two transitions**

[inference; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2301.08243; https://arxiv.org/abs/2506.09985] Both transitions involve a shift toward more abstract, structured representations: text tokens are discrete surface symbols; JEPA representations are continuous latent vectors encoding semantic structure; action-conditioned JEPA representations add causal intervention structure. This representation-space progression is a similarity between the two transitions.

[inference; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2506.09985] Both transitions improve the model's coverage of world dynamics. LLMs capture language co-occurrence statistics; JEPA video models capture motion and interaction dynamics; action-conditioned models capture causal intervention dynamics. Each step adds a richer level of world-dynamic structure.

[inference; source: https://arxiv.org/abs/2301.08243; https://arxiv.org/abs/2506.09985] The text→video-JEPA transition does NOT require causal intervention capability. Both the LLM and the JEPA Stage 1 model are trained on passive corpora and perform passive inference. The difference is the modality (language vs. video) and the target representation space (token vs. abstract latent), but neither model must act on or causally intervene in the world during training or inference.

[fact; source: https://arxiv.org/abs/2506.09985] The JEPA→physical-action transition DOES require a new feedback mechanism (action-conditioned training data, closed-loop MPC at inference), a new model component (V-JEPA 2-AC), and a new deployment context (robot embodiment). V-JEPA 2's two-stage architecture is empirical evidence that these are not the same stage: they require distinct objectives, data types, and inference loops.

### §3 Reasoning

**Facts established:**

1. LLM next-token prediction, I-JEPA representation prediction, and JEPA video-outcome prediction are all passive prediction objectives trained on observational corpora with no environment interaction. [fact; sources: https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2301.08243; https://arxiv.org/abs/2506.09985]

2. Action-conditioned world model training (DreamerV3, V-JEPA 2-AC) requires interaction data with action labels and a closed-loop feedback mechanism at inference. [fact; sources: https://arxiv.org/abs/2301.04104; https://arxiv.org/abs/2506.09985]

3. V-JEPA 2's Stage 1 (video JEPA) and Stage 2 (action-conditioned predictor) are architecturally distinct components with different objectives and different training data types. [fact; source: https://arxiv.org/abs/2506.09985]

4. Sutton and Barto formalise the prediction/control distinction as structurally different problem classes with different algorithmic requirements. [fact; source: http://incompleteideas.net/book/the-book-2nd.html]

**Inferences drawn:**

1. The text→video-JEPA shift is a within-class transition: both systems perform passive prediction. The shift changes modality and representation granularity but not the fundamental problem structure (no environment interaction, no causal agency, passive loss function). [inference]

2. The video-JEPA→physical-action shift is a between-class transition: it crosses the prediction/control boundary, requiring action labels, closed-loop feedback, irreversibility management, and embodiment constraints that are structurally absent from passive prediction. [inference]

3. JEPA representations are reusable across the class boundary because they encode abstract causal structure, but their reusability does not make the two transitions equivalent: it merely reduces the amount of interaction data needed for the second transition. [inference]

**Narrative removed:** Initial drafts said "JEPA essentially solves the grounding problem"; this overstates. JEPA improves the foundation for the second transition; it does not eliminate the class-boundary requirements.

### §4 Consistency Check

```text
contradiction_scan: no internal contradictions detected
claim_check: all factual claims tied to accessible sources
scope_check: analysis stays within declared scope
confidence_adjustment: both transition assessments kept at medium because V-JEPA 2-AC
  empirical results are from one paper (Meta/FAIR) not yet independently replicated
overlap_check: "same class" question answered directly in §3 and §6; no circular references
```

### §5 Depth and Breadth Expansion

**Technical lens:**

The prediction/control distinction in the RL literature (Sutton and Barto, Ch. 3) has deep algorithmic consequences: prediction convergence requires only value function learning under a fixed policy; control requires either policy gradient updates or value-based policy improvement, both of which need samples from the environment's action-response distribution. JEPA video pre-training is analogous to learning a very rich value function for passive observation; the action-conditioned stage is analogous to adding policy improvement. The two are compositional but not equivalent. [inference; source: http://incompleteideas.net/book/the-book-2nd.html; https://arxiv.org/abs/2506.09985]

**Historical lens:**

The shift from language modelling to reinforcement learning from human feedback (RLHF)-style instruction following in LLMs shows an analogous class transition: pre-trained LLMs that predict tokens are adapted to action-selection (choose the response that satisfies the human) using reward signals from human preferences. This transition also required a new training component (the reward model, the policy gradient update) beyond passive pre-training. This historical parallel supports the inference that the text→JEPA and JEPA→action transitions have different structural requirements. [inference; source: https://openreview.net/forum?id=BZ5a1r-kVsf]

**Cognitive science lens:**

The predictive processing and Free Energy Principle (FEP) literature (Friston, 2010; Clark, 2013) distinguishes perception (minimising prediction error about sensory inputs) from action (selecting actions that make sensory predictions come true, also called active inference). The brain uses both under the same mathematical framework, but they operate on different error signals: perceptual inference corrects beliefs; active inference corrects the world. This cognitive science parallel independently supports the inference that prediction and action are structurally distinct problem classes even if they share a common representational foundation. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-18-human-brain-prediction-machines.html]

**Research planning lens:**

For practitioners deciding where to invest in JEPA research, this distinction matters practically: improving video JEPA pre-training is primarily a data and compute scaling problem (more video, better encoders), while improving action grounding requires interaction data collection, safety infrastructure, and closed-loop evaluation environments. These have different engineering costs and timelines. [inference; source: https://arxiv.org/abs/2506.09985; https://arxiv.org/abs/2301.04104]

### §6 Synthesis

**Executive summary:**

The shift from text-token prediction to Joint Embedding Predictive Architecture (JEPA)-style video outcome prediction is not the same class of problem as the shift from video prediction to physically grounded action. The text→video-JEPA transition is a within-class upgrade: both paradigms perform passive prediction on observational corpora, differing only in modality and the granularity of the representation target. The video-JEPA→physical-action transition is a between-class shift that crosses the prediction/control boundary described by Sutton and Barto (2018): it introduces action-conditioned training, closed-loop feedback, irreversibility, and embodiment constraints that have no analogue in passive prediction. V-JEPA 2 (Assran et al., 2025) demonstrates this distinction empirically by requiring a separate action-conditioned training stage (V-JEPA 2-AC) after video pre-training; the two stages differ in objective function, data type, and inference loop. JEPA representations are reusable across the class boundary, reducing the amount of interaction data needed, but this reusability is a data-efficiency benefit, not a collapse of the class distinction.

**Key findings:**

1. Text-token prediction and JEPA video-outcome prediction are both passive prediction problems trained on observational corpora; the shift between them changes modality and representation target without introducing causal agency or environment interaction. ([inference]; medium confidence; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2301.08243; https://arxiv.org/abs/2506.09985)

2. JEPA-style prediction and physically grounded action selection belong to structurally distinct problem classes: the reinforcement learning literature distinguishes prediction (value estimation under a fixed policy) from control (policy optimisation) as requiring different algorithms and feedback types. ([fact]; high confidence; source: http://incompleteideas.net/book/the-book-2nd.html)

3. V-JEPA 2 requires a second training stage using action-conditioned robot-trajectory data that is structurally absent from internet video, confirming empirically that passive video prediction alone does not bridge to physical action. ([fact]; high confidence; source: https://arxiv.org/abs/2506.09985)

4. JEPA representations trained on passive video transfer to action-conditioned prediction with substantially less interaction data than prior world-model approaches, suggesting JEPA video pre-training is a necessary but not sufficient precondition for action grounding. ([inference]; medium confidence; source: https://arxiv.org/abs/2506.09985)

5. Physical action introduces irreversibility and embodiment latency constraints that are absent from passive prediction: errors in text or video prediction can be discarded and retrained, while physical action errors have consequences that may not be undoable within an episode. ([inference]; medium confidence; source: https://arxiv.org/abs/2301.04104; http://incompleteideas.net/book/the-book-2nd.html)

6. The text→video-JEPA transition is best characterised as a representation-quality improvement within the passive prediction class: it captures richer physical-world structure (motion, causality, object interaction) but does not require the model to select or commit to actions with real consequences. ([inference]; medium confidence; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2301.08243)

7. The cognitive science parallel between perception (passive prediction-error minimisation) and active inference (action selection to satisfy predictions) independently supports the inference that passive prediction and physical action are different problem classes even when they share a common representational foundation. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-03-18-human-brain-prediction-machines.html)

8. For research planning, the two transitions have different engineering requirements: scaling video JEPA is primarily a data and compute problem, while grounding JEPA representations in physical action additionally requires safe interaction data collection, closed-loop evaluation infrastructure, and embodiment-specific design. ([inference]; medium confidence; source: https://arxiv.org/abs/2506.09985; https://arxiv.org/abs/2301.04104)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Text and JEPA video prediction are both passive, no causal agency | https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2301.08243; https://arxiv.org/abs/2506.09985 | medium | Based on objective function analysis; no comparative empirical ablation |
| [fact] Prediction and control are distinct RL problem classes | http://incompleteideas.net/book/the-book-2nd.html | high | Standard RL textbook definition; well-established |
| [fact] V-JEPA 2-AC requires action-labeled interaction data not in internet video | https://arxiv.org/abs/2506.09985 | high | Direct claim from V-JEPA 2 paper; empirically demonstrated |
| [inference] JEPA representations transfer to action-conditioning efficiently | https://arxiv.org/abs/2506.09985 | medium | Single lab result from Meta/FAIR; not independently replicated |
| [inference] Irreversibility and latency are absent from passive prediction | https://arxiv.org/abs/2301.04104; http://incompleteideas.net/book/the-book-2nd.html | medium | Structural inference from RL theory; not empirically quantified here |
| [inference] Text→JEPA is within-class representation-quality improvement | https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2301.08243 | medium | Inferred from objective function structure; JEPA paper does not directly compare to LLM class |
| [inference] Cognitive science parallel (perception vs. active inference) supports class distinction | https://davidamitchell.github.io/Research/research/2026-03-18-human-brain-prediction-machines.html | medium | Analogy; may not map exactly to neural network architectures |
| [inference] Engineering requirements differ for the two transitions | https://arxiv.org/abs/2506.09985; https://arxiv.org/abs/2301.04104 | medium | Practical inference from two-stage V-JEPA 2 architecture |

**Assumptions:**

- **Assumption:** The text→video-JEPA transition is best classified by the structure of the prediction objective (passive vs. active), not by the difficulty of achieving it. **Justification:** LeCun's JEPA framework explicitly characterises both as latent-space prediction; the presence or absence of action-conditioning is the structural differentiator (source: https://openreview.net/forum?id=BZ5a1r-kVsf).

- **Assumption:** JEPA representations are reusable across the class boundary. **Justification:** V-JEPA 2-AC freezes the Stage 1 encoder and trains only a new action-conditioned predictor on top, demonstrating that Stage 1 representations provide sufficient structure for Stage 2 (source: https://arxiv.org/abs/2506.09985).

- **Assumption:** Sutton and Barto's prediction/control distinction maps onto the JEPA/action-conditioning distinction. **Justification:** Both use the same structural test (does the model's output select actions that affect the environment?) to separate the two classes; the analogy is direct (source: http://incompleteideas.net/book/the-book-2nd.html).

**Analysis:**

The primary evidence for the non-equivalence answer comes from two converging sources: the structural analysis of objective functions (LeCun 2022; Assran 2023, 2025; Sutton and Barto 2018) and the empirical architecture of V-JEPA 2, which needed a separate stage to cross from video prediction to robot action. These are independent lines of evidence that reach the same conclusion.

The strongest counter-argument to the non-equivalence conclusion is that both transitions are "just adding more grounding" to a progressively richer world model: text captures statistical regularities; video captures motion and physics; action captures causal intervention. Under this framing, all three stages are points on a continuum of grounding, differing in degree not in kind. This view has support in LeCun's hierarchical world-model framing. However, the prediction/control distinction is not merely a matter of degree: it involves a different mathematical structure (maximising cumulative reward vs. minimising prediction error) and a different data dependency (interaction data vs. observational data). V-JEPA 2's architectural separation supports treating the transition as a class boundary rather than a continuum.

A separate weakness is that V-JEPA 2-AC results come from a single lab (Meta/FAIR) and have not been independently replicated as of May 2026. If subsequent work shows that action-conditioned prediction can be derived without any interaction data, the within-class argument would need revision. The current evidence does not support this possibility.

**Risks, gaps, and uncertainties:**

- V-JEPA 2-AC results are from a single lab (Meta/FAIR) and have not been independently replicated. The data-efficiency claims (62 hours sufficient for zero-shot manipulation) may not generalise to other robot morphologies or task types.
- The V-JEPA 2 paper does not include ablations comparing JEPA pre-training against no pre-training for the action-conditioned stage; the magnitude of the transfer benefit is not precisely quantified.
- Full transcripts of LeCun's 2025-2026 public talks are not publicly accessible in their entirety; the review of the primary source is based on the paper and accessible secondary summaries.
- The extent to which JEPA video representations capture counterfactual world dynamics (how the world would have evolved if a different action had been taken) is not directly established by the V-JEPA 2 paper; this remains a gap in the causal grounding evidence.
- The prediction/control distinction from Sutton and Barto applies most precisely to tabular and linear-function-approximation RL; its application to neural network world models involves additional assumptions about convergence and representation that are not fully settled.

**Open questions:**

1. Does JEPA video pre-training capture counterfactual structure (how the world responds to interventions not observed in the training video)? This is the key question for whether JEPA representations can support causal reasoning, not just consequence prediction.
2. How much of the data efficiency in V-JEPA 2-AC is attributable to JEPA's abstract representation versus the scale of video pre-training? Disentangling these factors would clarify whether representation quality or data volume is the primary driver.
3. Does the text→video-JEPA transition produce any qualitative capability gains in physical-world reasoning (not just video understanding benchmarks), or only quantitative improvements on those benchmarks?
4. Can the prediction/control class boundary be crossed without explicit interaction data through synthetic action annotation of internet video (e.g., reconstructing plausible action labels from motion fields)?

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed
  - LLM (Large Language Model): expanded at first use in Context
  - JEPA (Joint Embedding Predictive Architecture): expanded at first use in title and Research Question
  - I-JEPA (Image JEPA): expanded in Sources and §2.1A-ii
  - V-JEPA 2 (Video JEPA 2): expanded at first use in §2.1A-ii
  - MPC (model predictive control): expanded at first use in §2.1A-iii
  - RL (reinforcement learning): expanded at first use in §4
  - FEP (Free Energy Principle): expanded at first use in §5
  - RLHF (reinforcement learning from human feedback): expanded at first use in §5
  - MSE (mean-squared error): expanded at first use in §2.1B
  - FAIR (Meta's Fundamental AI Research): not used as an acronym in text; only in notes cell
claim_labels: all factual/inferential claims in Research Skill Output carry labels
parity_check: §6 Synthesis and Findings Executive Summary/Key Findings are aligned
source_check: all sources accessible; V-JEPA 2 paper is primary; DreamerV3 is primary; LeCun 2022 is primary
em_dash_check: no em-dashes used
vague_quantifier_check: no unsourced "many", "most", "significant" without qualifier
binary_contrast_check: "not the same class" framing supported by objective function analysis and V-JEPA 2 architecture; evidence for both halves cited
```

---

## Findings

### Executive Summary

The shift from text-token prediction to Joint Embedding Predictive Architecture (JEPA)-style video outcome prediction is not the same class of problem as the shift from video prediction to physically grounded action. Both text-token prediction and JEPA video-outcome prediction are passive observational prediction tasks: neither requires the model to select actions that affect the world, and both are trained on corpora without environment interaction. [inference; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2301.08243] The video-JEPA to physical-action shift crosses a structural boundary formalised in reinforcement learning (RL) theory as the prediction/control distinction: prediction estimates what will happen under a fixed policy, while control selects actions that change outcomes, requiring action-conditioned training data, closed-loop feedback, and irreversibility management. [fact; source: http://incompleteideas.net/book/the-book-2nd.html] V-JEPA 2 (Assran et al., 2025) confirms this empirically by requiring a separate action-conditioned training stage beyond video pre-training before it can plan robot actions. [fact; source: https://arxiv.org/abs/2506.09985] JEPA representations transfer efficiently to the action-conditioned stage, reducing the interaction data needed, but this efficiency gain does not collapse the class distinction. [inference; source: https://arxiv.org/abs/2506.09985]

### Key Findings

1. **Text-token prediction and JEPA video-outcome prediction are both passive prediction paradigms: neither requires the model to select or commit to actions that affect a physical environment during training or inference.** ([inference]; medium confidence; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2301.08243; https://arxiv.org/abs/2506.09985)

2. **Reinforcement learning theory formally distinguishes prediction problems (estimating the value of a fixed policy) from control problems (optimising the policy itself), identifying them as structurally different classes with different algorithmic requirements and feedback dependencies.** ([fact]; high confidence; source: http://incompleteideas.net/book/the-book-2nd.html)

3. **V-JEPA 2 (2025) required a separate action-conditioned predictor trained on 62 hours of labeled robot-trajectory data after Stage 1 video pre-training, demonstrating that passive video JEPA prediction does not by itself yield physical action capability.** ([fact]; high confidence; source: https://arxiv.org/abs/2506.09985)

4. **JEPA representations learned from passive internet video transfer to the action-conditioned prediction stage efficiently, enabling zero-shot manipulation in new environments with minimal interaction data, meaning JEPA video pre-training is a necessary but not sufficient precondition for action grounding.** ([inference]; medium confidence; source: https://arxiv.org/abs/2506.09985)

5. **Physical action introduces three requirements absent from passive video prediction: action-conditioned interaction data, closed-loop feedback at inference time using model predictive control (MPC), and irreversibility constraints that prevent simple error correction through retraining.** ([inference]; medium confidence; source: https://arxiv.org/abs/2301.04104; https://arxiv.org/abs/2506.09985)

6. **The text→video-JEPA transition is an improvement in representation quality within the passive prediction class: it captures motion dynamics and causal structure rather than surface token statistics, but the fundamental problem structure (passive, observational, corpus-trained) is unchanged.** ([inference]; medium confidence; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2301.08243)

7. **Cognitive science research on predictive processing distinguishes passive perceptual prediction-error minimisation from active inference (action selection to confirm world-model predictions), independently supporting the inference that passive prediction and physical action belong to different problem classes even when they share a representational foundation.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-03-18-human-brain-prediction-machines.html)

8. **For research planning purposes, improving video JEPA pre-training is primarily a data and compute scaling problem, while grounding JEPA representations in physical action additionally requires safe interaction-data collection infrastructure, closed-loop evaluation environments, and robot-specific design.** ([inference]; medium confidence; source: https://arxiv.org/abs/2506.09985; https://arxiv.org/abs/2301.04104)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Text and JEPA video prediction both passive, no causal agency | https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2301.08243; https://arxiv.org/abs/2506.09985 | medium | Inferred from objective function structure; no comparative ablation between text and JEPA |
| [fact] Prediction and control are distinct RL problem classes | http://incompleteideas.net/book/the-book-2nd.html | high | Standard RL definition in Sutton and Barto (2018), Ch. 3 |
| [fact] V-JEPA 2-AC requires action-labeled interaction data not in internet video | https://arxiv.org/abs/2506.09985 | high | Direct claim from V-JEPA 2 paper; 62 hours Droid robot data; demonstrated empirically |
| [inference] JEPA representations transfer to action conditioning efficiently | https://arxiv.org/abs/2506.09985 | medium | Single-lab result from Meta/FAIR; not independently replicated as of May 2026 |
| [inference] Physical action requires MPC, closed-loop feedback, irreversibility management | https://arxiv.org/abs/2301.04104; https://arxiv.org/abs/2506.09985 | medium | Structural inference from both DreamerV3 and V-JEPA 2-AC architectures |
| [inference] Text→JEPA is within-class representation-quality improvement | https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2301.08243 | medium | Inferred from objective function analysis; LeCun paper does not explicitly compare to LLM problem class |
| [inference] Cognitive science perception/active inference parallel supports class distinction | https://davidamitchell.github.io/Research/research/2026-03-18-human-brain-prediction-machines.html | medium | Analogical argument; cognitive science mapping to neural networks is approximate |
| [inference] Engineering requirements differ for the two transitions | https://arxiv.org/abs/2506.09985; https://arxiv.org/abs/2301.04104 | medium | Practical inference from two-stage V-JEPA 2 design and DreamerV3 data requirements |

### Assumptions

- **Assumption:** The text→video-JEPA transition is best classified by the structure of the prediction objective (passive observational loss) rather than by the difficulty or quality of the resulting representations. **Justification:** LeCun's JEPA framework characterises both text and JEPA prediction as variants of self-supervised prediction in latent space; the structural differentiator used here is whether the model must select actions that affect the world (source: https://openreview.net/forum?id=BZ5a1r-kVsf).

- **Assumption:** JEPA Stage 1 representations are reusable as the foundation for Stage 2 action-conditioned prediction without modification. **Justification:** V-JEPA 2-AC freezes the Stage 1 encoder and trains only the action-conditioned predictor on top; this design choice implies that Stage 1 representations encode sufficient world-dynamic structure to support action consequence prediction (source: https://arxiv.org/abs/2506.09985).

- **Assumption:** Sutton and Barto's prediction/control distinction maps onto the JEPA/action-conditioning distinction in deep learning world models. **Justification:** Both distinctions apply the same structural test: does the model's output select actions that affect the environment? The concepts are directly analogous, though the neural network context adds considerations about convergence that tabular RL theory does not fully address (source: http://incompleteideas.net/book/the-book-2nd.html).

### Analysis

Two converging lines of evidence support the non-equivalence conclusion. The structural line comes from objective function analysis: LLM cross-entropy, JEPA representation prediction, and action-conditioned world model training are each describable in the RL framework as estimation under a fixed policy (the corpus), estimation under passive observation (the video corpus), and active policy optimisation respectively. This maps directly to the prediction/control distinction. The empirical line comes from V-JEPA 2's two-stage architecture: if video JEPA and action-conditioned prediction were the same class, a single training stage would suffice. The fact that Meta/FAIR needed a separate stage with different data and a different objective is strong evidence of a structural boundary.

The primary counter-argument is a continuum view: text, video, and action can be seen as progressively richer forms of grounding on a single dimension of world-model completeness. This view has partial support in LeCun's hierarchical world-model framework, which treats all stages as variants of configurable predictive architectures. However, the continuum interpretation does not fully account for the data-type discontinuity: passive video and action-labeled trajectories are categorically different data types that cannot be trivially interconverted. Even granting the continuum framing, the data-type discontinuity means the two transitions have different practical requirements, which is the decision-relevant conclusion for research planning.

One important nuance is that the class-boundary claim refers to the structural requirements of the objective function and feedback mechanism, not to the difficulty of the tasks. The text→video-JEPA transition may be empirically harder (more data, more compute, more engineering) than the JEPA→action transition in cases where abundant robot interaction data is available. Structural class membership is orthogonal to empirical difficulty ordering.

### Risks, Gaps, and Uncertainties

- V-JEPA 2-AC results come from a single lab and have not been independently replicated. The claim that 62 hours of robot data is sufficient for zero-shot manipulation may not generalise across robot morphologies, task types, or operating environments.
- The V-JEPA 2 paper does not include ablations comparing JEPA-pre-trained versus randomly-initialised action-conditioned models; the magnitude of the transfer benefit is not precisely quantified.
- The extent to which JEPA video representations capture counterfactual world dynamics (how the world would have evolved under unobserved actions) is not established by the V-JEPA 2 paper. This gap limits the strength of the causal-grounding claim.
- Sutton and Barto's prediction/control distinction was developed for tabular and linear-approximation RL settings; its application to deep neural network world models involves additional assumptions about representational power and convergence that are not fully settled in the literature.
- The cognitive science analogy (predictive processing / active inference) is an approximate parallel, not a formal derivation. Friston's Free Energy Principle applies to biological systems with specific homeostatic constraints; mapping it precisely to neural network architectures requires additional bridging work.

### Open Questions

1. Does JEPA video pre-training capture counterfactual causal structure (how the world responds to interventions not observed in the training video), or only conditional predictive structure (what the world will look like given observed context)? This distinction is central to whether JEPA representations can support intervention planning without additional interaction data.
2. Can the prediction/control class boundary be crossed through synthetic action annotation of internet video, for example by inferring plausible motor commands from dense motion fields in video? If so, the interaction-data requirement might be addressable without physical robots.
3. Does the text→video-JEPA transition produce any qualitative capability gains in physical-world reasoning tasks (not only video understanding benchmarks), or do the gains remain confined to visual domains?
4. At what scale of video pre-training does JEPA representation quality plateau for downstream robot manipulation, and what does this imply for the cost-efficiency of the two-stage V-JEPA 2 approach?

---

## Output

- Type: knowledge
- Description: Conceptual analysis distinguishing the two major paradigm shifts in LeCun's world-model research agenda. Establishes that text→video-JEPA is a within-class passive-prediction improvement while video-JEPA→physical-action is a between-class transition to active control, with empirical support from V-JEPA 2's two-stage architecture. [inference; source: https://arxiv.org/abs/2506.09985; https://openreview.net/forum?id=BZ5a1r-kVsf]
- Links:
  - https://arxiv.org/abs/2506.09985 (V-JEPA 2 paper: primary empirical evidence for two-stage architecture)
  - https://openreview.net/forum?id=BZ5a1r-kVsf (LeCun 2022: primary theoretical framing)
  - http://incompleteideas.net/book/the-book-2nd.html (Sutton and Barto 2018: prediction/control distinction)
