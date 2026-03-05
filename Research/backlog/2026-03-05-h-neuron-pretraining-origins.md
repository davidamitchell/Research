---
title: "Pre-Training Origins of Hallucination-Associated Neurons — Implications for LLM Development"
added: 2026-03-05
status: backlog
priority: medium
blocks: []
tags: [llm, hallucinations, h-neurons, pre-training, alignment, rlhf, training-dynamics, mechanistic-interpretability, reliability]
started: ~
completed: ~
output: [knowledge]
---

# Pre-Training Origins of Hallucination-Associated Neurons — Implications for LLM Development

## Research Question

Given that Hallucination-Associated Neurons (H-Neurons) emerge during pre-training rather than instruction tuning or RLHF, what does this reveal about how hallucination-prone behaviour is encoded during the pre-training phase, and what concrete changes to pre-training data, objectives, or architecture could reduce H-Neuron formation?

## Scope

**In scope:**
- The specific finding in arXiv:2512.01797 that H-Neurons are already predictive in base pre-trained models — before RLHF or instruction tuning
- What it means mechanistically for a neuron to "emerge during pre-training": what training signal causes these neurons to form?
- The relationship between pre-training data characteristics (noise, misinformation, distributional bias) and H-Neuron formation
- The relationship between the next-token prediction objective and the encoding of over-compliance behaviour at the neuron level
- What RLHF and instruction tuning can and cannot do to reverse or suppress H-Neurons that already exist
- Implications for scaling: does scaling pre-training compute increase or decrease H-Neuron density?
- Practical interventions at the pre-training stage: data curation, curriculum learning, objective modification, architectural choices

**Out of scope:**
- H-Neuron identification methodology (covered in `2026-03-05-h-neurons-in-llms`)
- Inference-time and fine-tuning-time interventions (covered in `2026-03-05-h-neuron-over-compliance`)
- General hallucination taxonomy and causes (covered in `2026-03-05-llm-hallucination-mechanisms`)

**Constraints:** Builds on `2026-03-05-h-neurons-in-llms` — must be researched after that item is complete. Much of this item will require first-principles reasoning from the paper's findings plus the broader pre-training and training-dynamics literature, as direct pre-training interventions for H-Neuron suppression are not yet established in the literature.

## Context

The finding that H-Neurons originate in pre-training — not in the RLHF or instruction-tuning phase — has a profound implication: **post-training alignment cannot fully solve the hallucination problem**. If the neurons that drive over-compliance and hallucination are already present in the base model, RLHF and constitutional AI can only suppress their expression, not eliminate their existence. The underlying causal mechanism remains, ready to surface under distributional shift or adversarial conditions.

This shifts the research agenda in two directions:

1. **Understanding pre-training dynamics** — What in the standard pre-training procedure (next-token prediction on diverse web-scale corpora) causes these neurons to form? Is it noisy/contradictory training data? The objective function itself? The model architecture? Scale?

2. **Pre-training-time interventions** — Can the pre-training procedure be modified to prevent H-Neurons from forming in the first place? What would this cost in terms of data scale, compute, or general capability?

## Approach

1. **Pre-training origin evidence** — Work through the evidence from arXiv:2512.01797 for the pre-training origin claim. What comparison is made between base and instruction-tuned/RLHF models? How strong is the evidence? What alternative explanations are ruled out?

2. **Next-token prediction and over-compliance** — Investigate the theoretical connection between the next-token prediction objective and the encoding of over-compliance behaviour. Does training on corpora containing sycophantic text (human-written examples of agreeing with errors, confident falsehoods, etc.) directly cause H-Neuron formation?

3. **Pre-training data quality research** — Survey the literature on how pre-training data quality affects model behaviour. What do we know about the effect of noisy, contradictory, or sycophantic text in training corpora on hallucination rates? What deduplication, quality filtering, and source-weighting strategies exist?

4. **RLHF limits** — What does the RLHF and post-training alignment literature say about the limits of post-training alignment for fixing problems that originate in pre-training? Can reward signals selectively suppress pre-trained features, or do they primarily reroute behaviour at the surface level?

5. **Scaling dynamics** — What do scaling laws and mechanistic interpretability research suggest about how neuron-level features change with model scale? Does H-Neuron density decrease as models become larger (suggesting scale "solves" the problem) or does it remain stable/increase?

6. **Pre-training intervention design** — Synthesise the above into a structured set of candidate pre-training interventions: data filtering approaches, curriculum learning strategies (e.g., deprioritising known-sycophantic sources), auxiliary training objectives (explicit uncertainty calibration), and architectural choices (e.g., mechanisms that reduce superposition). Evaluate feasibility and estimated effectiveness.

## Sources

- [ ] Gao et al. (2025) — "Hallucination-Associated Neurons in LLMs" (primary source for origins finding): https://arxiv.org/abs/2512.01797
- [ ] Hoffmann et al. (2022) — "Training Compute-Optimal Large Language Models (Chinchilla)": https://arxiv.org/abs/2203.15556 — scaling laws and data quality
- [ ] Gunasekar et al. (2023) — "Textbooks Are All You Need" (Phi-1) — data quality over data scale: https://arxiv.org/abs/2306.11644
- [ ] Penedo et al. (2023) — "The RefinedWeb Dataset for Falcon LLM: Outperforming Curated Corpora with Web Data Alone": https://arxiv.org/abs/2306.01116 — pre-training data curation
- [ ] Anthropic (2022) — "Constitutional AI: Harmlessness from AI Feedback": https://arxiv.org/abs/2212.08073 — RLHF limits for alignment
- [ ] Elhage et al. (2022) — "Toy Models of Superposition" — how pre-training encodes features in neurons: https://transformer-circuits.pub/2022/toy_model/index.html
- [ ] Biderman et al. (2023) — "Pythia: A Suite for Analysing Large Language Models Across Training and Scaling" — training dynamics: https://arxiv.org/abs/2304.01373
- [ ] `Research/backlog/2026-03-05-h-neurons-in-llms.md` — **prerequisite**: must be completed before starting this item

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

- Is there a variant of next-token prediction that does not inadvertently train over-compliance — e.g., by treating factual uncertainty as a first-class training signal?
- Can "H-Neuron density" become a measurable property reported as part of model evaluations, analogous to perplexity or benchmark accuracy?
- If H-Neurons emerge from noisy/sycophantic web text, does synthetic data generation (e.g., Phi-1's "textbooks") reduce their formation?

---

## Output

- Type: knowledge
- Description: A structured analysis of what the pre-training origin of H-Neurons implies for the limits of post-training alignment and for the design of pre-training data, objectives, and architecture; includes a candidate set of pre-training-time interventions and their estimated feasibility.
- Links:
  - https://arxiv.org/abs/2512.01797
  - `Research/backlog/2026-03-05-h-neurons-in-llms.md`
