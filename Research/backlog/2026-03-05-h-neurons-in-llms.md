---
title: "Hallucination-Associated Neurons (H-Neurons) in LLMs — Identification, Behavioural Impact, and Origins"
added: 2026-03-05
status: backlog
priority: high
blocks: [2026-03-05-h-neuron-over-compliance, 2026-03-05-h-neuron-pretraining-origins]
tags: [llm, hallucinations, h-neurons, mechanistic-interpretability, over-compliance, pre-training, alignment, reliability, arxiv]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# Hallucination-Associated Neurons (H-Neurons) in LLMs — Identification, Behavioural Impact, and Origins

## Research Question

What are Hallucination-Associated Neurons (H-Neurons) in large language models, how can they be identified, what behaviours do they cause, where do they come from, and what do these findings imply for building more reliable LLMs?

## Scope

**In scope:**
- The three-part investigation structure of arXiv:2512.01797: identification, behavioural impact, and origins of H-Neurons
- The methodology for identifying H-Neurons: what features make a neuron "hallucination-associated" and how sparse that set is (<0.1% of total neurons)
- How controlled interventions (activation suppression/amplification) confirm the causal link between H-Neurons and hallucination
- The specific behavioural pathway: H-Neurons → over-compliance → hallucination
- The pre-training origin finding: H-Neurons are already predictive in base models before instruction tuning or RLHF
- Generalisation across diverse scenarios and LLM architectures
- Implications for future work: neuron-level detection, targeted suppression, training-time interventions

**Out of scope:**
- Broad hallucination taxonomy (covered in `2026-03-05-llm-hallucination-mechanisms`)
- Detailed over-compliance behaviour and intervention design (covered in `2026-03-05-h-neuron-over-compliance`)
- Deep dive on pre-training implications for LLM development (covered in `2026-03-05-h-neuron-pretraining-origins`)

**Constraints:** Primary source is arXiv:2512.01797 (Gao et al., Dec 2025); supplemented by contemporaneous mechanistic interpretability literature. Aim for a thorough but accessible synthesis — assume the reader has completed `2026-03-05-llm-hallucination-mechanisms` first.

## Context

Prior work on LLM hallucinations has operated at a macroscopic level: training data quality, RLHF objectives, decoding strategies. What has been missing is a microscopic account — which specific parts of the network are doing what, and why? Gao et al. (arXiv:2512.01797) take a systematic neuron-level approach to this question for the first time.

Their key result is striking: fewer than 0.1% of neurons reliably predict whether the model will hallucinate, and this prediction generalises across diverse tasks. These neurons are not incidental — controlled interventions show that suppressing them reduces hallucination, while amplifying them increases it. Furthermore, they are not an artefact of RLHF: they are already present and predictive in base pre-trained models.

This combination of findings — sparsity, causal role, generality, and pre-training origin — opens up a concrete new angle for improving LLM reliability: targeted neuron-level monitoring and intervention.

## Approach

1. **Read and annotate the paper** — Work through arXiv:2512.01797 section by section. Produce a structured summary of each of the three investigation axes (identification, behavioural impact, origins).

2. **Identification methodology** — How do the authors identify H-Neurons? What is the activation-level criterion? What classifier or statistical test distinguishes H-Neurons from the other 99.9%+? How is "generalisation across scenarios" evaluated?

3. **Behavioural impact** — What exactly is "controlled intervention"? How is the causal link established (vs. correlation)? What is the over-compliance pathway — how does an H-Neuron produce a plausible-but-false output?

4. **Origins investigation** — How do the authors test whether H-Neurons originate in pre-training? What is compared between base models and instruction-tuned/RLHF variants? What does it mean that these neurons "emerge during pre-training"?

5. **Generalisation and limits** — On which model families and tasks does the finding hold? Where does it not hold, or where is the evidence weak? What are the authors' own stated limitations?

6. **Implications synthesis** — What concrete next steps do the findings suggest? Immediate applications (runtime hallucination detection), medium-term applications (targeted neuron suppression at inference), longer-term applications (training-time regularisation or data curation to suppress H-Neuron formation).

## Sources

- [ ] Gao et al. (2025) — "Hallucination-Associated Neurons in LLMs": https://arxiv.org/abs/2512.01797 ← **primary source**
- [ ] "They solved AI hallucinations!" (YouTube explainer) — accessible walkthrough of the H-Neurons paper: the liar circuit concept, L1-regularised sparse probe methodology, intervention challenges, and implications for real-time hallucination detection: https://youtu.be/1ONwQzauqkc
- [ ] Elhage et al. (2022) — "Toy Models of Superposition" (Anthropic) — background on how neurons encode features: https://transformer-circuits.pub/2022/toy_model/index.html
- [ ] Meng et al. (2022) — "Locating and Editing Factual Associations in GPT" (ROME) — neuron-level causal tracing in GPT-family decoder models: https://arxiv.org/abs/2202.05262
- [ ] Bereska & Gavves (2024) — "Mechanistic Interpretability for AI Safety — A Review": https://arxiv.org/abs/2404.14082
- [ ] `Research/backlog/2026-03-05-llm-hallucination-mechanisms.md` — prerequisite: hallucination taxonomy and macroscopic causes
- [ ] `Research/backlog/2026-03-05-h-neuron-over-compliance.md` — downstream: behavioural consequences and interventions
- [ ] `Research/backlog/2026-03-05-h-neuron-pretraining-origins.md` — downstream: pre-training origins and LLM development implications

---

## Findings

*(Fill in when completing. Follow the research skill synthesis structure.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly.

### Key Findings

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

- **Assumption:** ... **Justification:** ...

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

- How sparse is "sparse"? Does the 0.1% figure hold across all model sizes and architectures?
- Can H-Neurons be suppressed at inference time without degrading general capabilities?
- Do the same H-Neurons fire for all hallucination types, or are they hallucination-type-specific?
- Can training data or objectives be modified to prevent H-Neurons from forming in the first place?

---

## Output

- Type: knowledge, backlog-item
- Description: A thorough synthesis of arXiv:2512.01797 — the H-Neurons identification methodology, causal behavioural pathway (H-Neurons → over-compliance → hallucination), and pre-training origin finding. Seeds two downstream research items.
- Links:
  - https://arxiv.org/abs/2512.01797
  - `Research/backlog/2026-03-05-h-neuron-over-compliance.md`
  - `Research/backlog/2026-03-05-h-neuron-pretraining-origins.md`
