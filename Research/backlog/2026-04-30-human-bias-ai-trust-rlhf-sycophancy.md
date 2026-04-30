---
title: "Human cognitive bias toward AI correctness and explainability: automation bias, Reinforcement Learning from Human Feedback (RLHF) sycophancy, and mechanistic interpretability limits"
added: 2026-04-30T06:52:37+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []
tags: [governance, explainability, human-oversight, llm, alignment, evaluation, cognitive-bias, rlhf, mechanistic-interpretability]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []
related: [2026-04-30-explainable-ai-xai-regulation-governance, 2026-04-30-orthogonality-thesis-ai-alignment-interpretability, 2026-04-02-claude-mythos, 2026-04-26-human-in-the-loop-ai-automated-workflows, 2026-04-28-uelgf-human-oversight-accountability-layer]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Human cognitive bias toward AI correctness and explainability: automation bias, Reinforcement Learning from Human Feedback (RLHF) sycophancy, and mechanistic interpretability limits

## Research Question

To what extent do humans systematically over-trust AI-generated explanations, and what mechanisms — automation bias, Reinforcement Learning from Human Feedback (RLHF)-induced sycophancy in post-training, and the polysemantic nature of hidden-layer neurons (h-neurons) as revealed by mechanistic interpretability research — combine to make AI systems appear more correct and more explainable than they actually are?

## Scope

**In scope:**
- Automation bias literature: the human tendency to defer to automated systems even when evidence of error is present; studies in aviation, clinical decision support, and financial services
- RLHF sycophancy: how post-training reward models trained on human preference ratings encode the human preference for confident, fluent, and agreeable outputs over correct ones; empirical evidence of sycophantic behaviour in large language models (LLMs)
- Mechanistic interpretability and h-neurons: Anthropic's Circuits research thread; the superposition hypothesis (polysemantic neurons encode multiple unrelated features); implications for the faithfulness of post-hoc explanations (SHAP, LIME) when the underlying representations are not cleanly decomposable
- The gap between plausible explanations and faithful explanations: empirical work showing that humans rate unfaithful but plausible explanations as more convincing than faithful but counterintuitive ones
- Implications for governance: how this bias undermines the regulatory intent of explanation requirements (GDPR Article 22, EU AI Act transparency obligations)

**Out of scope:**
- Full algorithmic derivations of RLHF training procedures — survey only
- Neuroscience of human trust formation at a biological level
- Adversarial attacks on explanation systems (a separate threat model)
- Full treatment of the orthogonality thesis — see related item `2026-04-30-orthogonality-thesis-ai-alignment-interpretability`

**Constraints:**
- Empirical studies preferred over purely theoretical arguments; include both laboratory and field evidence where available
- Focus on LLMs and transformer-based systems as primary subject; classical ML references used for automation bias anchor only

## Context

A governance regime that mandates AI explainability implicitly assumes that explanations produced by AI systems are (a) faithful to the model's actual reasoning and (b) correctly evaluated by the humans who receive them. Both assumptions are challenged by evidence. RLHF post-training optimises model outputs for human approval, which tends to reward confident-sounding, agreeable explanations regardless of their fidelity. At the same time, mechanistic interpretability research (Anthropic's Circuits thread, the superposition hypothesis) shows that the internal representations of transformer models are polysemantic — individual neurons respond to multiple unrelated concepts — making post-hoc explanation methods (SHapley Additive exPlanations (SHAP), Local Interpretable Model-agnostic Explanations (LIME)) potentially unfaithful approximations of the actual computation. Humans, who are already prone to automation bias, then over-weight these plausible but potentially unfaithful explanations.

This item directly links to the XAI landscape survey (`2026-04-30-explainable-ai-xai-regulation-governance`) and to the orthogonality thesis item (`2026-04-30-orthogonality-thesis-ai-alignment-interpretability`). The governance implication is significant: if explanation requirements can be satisfied by outputs that humans will accept but that do not accurately represent the model's reasoning, the regulatory intent is undermined even when the letter of the rule is met.

## Approach

1. **Automation bias baseline** — Survey the established automation bias literature: Parasuraman & Manzey (2010) as the foundational review; clinical decision support studies (Goddard et al., 2012); aviation complacency; financial services fraud alert fatigue. Establish the empirical magnitude of the bias.

2. **RLHF sycophancy mechanisms** — Review how RLHF reward models are constructed from human preference data and how this creates selection pressure for agreeable, confident outputs. Review Anthropic's published work on sycophancy (Perez et al., 2022); OpenAI's internal discussions; DeepMind's work on reward misspecification. Identify whether sycophancy is more pronounced in explanation generation than in factual generation.

3. **Mechanistic interpretability and polysemanticity** — Review Anthropic's Circuits thread (Olah et al.); the superposition hypothesis (Elhage et al., 2022) showing that LLMs store more features than dimensions using near-orthogonal directions; implications for the reliability of explanation methods that assume additive or locally linear attribution. Identify which XAI methods are most vulnerable to polysemanticity.

4. **Plausibility vs. faithfulness gap** — Review empirical work on how humans evaluate explanations: Lage et al. (2019); Adebayo et al. (2018, "Sanity Checks for Saliency Maps"); Hase & Bansal (2020, "Evaluating Explainable AI"). Quantify the gap between explanations humans prefer and explanations that are actually faithful.

5. **Governance implications** — Synthesise: what does this combined bias mean for compliance regimes that rely on human review of AI-generated explanations? Does the combination of sycophancy + automation bias + polysemanticity create a systematic governance blind spot? What countermeasures exist (adversarial red-teaming of explanations, faithfulness metrics, structured human review protocols)?

## Sources

- [ ] [Parasuraman & Manzey (2010) — Complacency and bias in human use of automation: An attentional integration](https://doi.org/10.1177/0018720810376055) — foundational automation bias review
- [ ] [Perez et al. (2022) — Sycophancy to Subterfuge: Investigating Reward Tampering in Language Models](https://arxiv.org/abs/2310.09625) — Anthropic sycophancy empirical evidence
- [ ] [Anthropic Circuits thread — Zoom In: An Introduction to Circuits (Olah et al., 2020)](https://distill.pub/2020/circuits/zoom-in/) — mechanistic interpretability; individual neuron features in neural networks
- [ ] [Elhage et al. (2022) — Toy Models of Superposition (Anthropic)](https://transformer-circuits.pub/2022/toy_model/index.html) — superposition hypothesis; polysemantic neurons; near-orthogonal feature encoding
- [ ] [Adebayo et al. (2018) — Sanity Checks for Saliency Maps](https://arxiv.org/abs/1810.03292) — empirical evidence that popular explanation methods fail basic faithfulness checks
- [ ] [Hase & Bansal (2020) — Evaluating Explainable AI: Which Algorithmic Explanations Help Users Predict Model Behavior?](https://arxiv.org/abs/2010.09875) — human evaluation of explanation faithfulness vs. plausibility
- [ ] [Goddard et al. (2012) — Automation bias: A systematic review of frequency, effect mediators, and mitigators](https://doi.org/10.1016/j.ijmedinf.2012.02.006) — clinical decision support; automation bias magnitude
- [ ] [Lage et al. (2019) — Human Evaluation of Models Built for Interpretability](https://arxiv.org/abs/1902.00006) — user studies on interpretability; plausibility vs. utility
- [ ] [Weidinger et al. (2022) — Taxonomy of Risks posed by Language Models (DeepMind)](https://arxiv.org/abs/2112.04359) — reward misspecification and sycophancy risks in LLMs
- [ ] [Anthropic Model Specification (2024)](https://www.anthropic.com/research/model-specification) — Anthropic's published values and training intent; relevant to understanding RLHF design choices and sycophancy mitigation
