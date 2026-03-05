---
title: "LLM Hallucinations — Types, Causes, and Current Mitigation Approaches"
added: 2026-03-05
status: backlog
priority: high
blocks: [2026-03-05-h-neurons-in-llms]
tags: [llm, hallucinations, reliability, alignment, grounding, mechanistic-interpretability]
started: ~
completed: ~
output: [knowledge]
---

# LLM Hallucinations — Types, Causes, and Current Mitigation Approaches

## Research Question

What are the established types, root causes, and current mitigation strategies for hallucinations in large language models, and what does the macroscopic (training-level) view leave unexplained that motivates neuron-level investigation?

## Scope

**In scope:**
- Taxonomy of hallucination types: intrinsic vs. extrinsic, factual vs. faithfulness, closed-domain vs. open-domain
- Root causes at the macroscopic level: training data noise, distributional shift, over-optimisation of human feedback, sycophancy/over-compliance, decoding strategies
- Current mitigation approaches: retrieval-augmented generation (RAG), RLHF, constitutional AI, chain-of-thought prompting, fact-checking layers, inference-time interventions
- What these macroscopic explanations leave unexplained — the gap that motivates looking at neuron-level mechanisms

**Out of scope:**
- Neuron-level or circuit-level analysis (covered in `2026-03-05-h-neurons-in-llms`)
- Model fine-tuning implementation details
- Benchmark comparisons of specific models

**Constraints:** Primarily literature review of published research and survey papers; focus on conceptual clarity over exhaustive coverage.

## Context

Before investigating the specific finding that a sparse subset of neurons (<0.1%) predicts hallucination occurrences (arXiv:2512.01797), it is essential to have a clear foundation: what exactly counts as a hallucination, why prior work failed to fully explain the phenomenon at the training/objective level, and what practical mitigations exist today. This item establishes that foundation so the H-Neuron paper's contribution can be properly contextualised.

## Approach

1. **Taxonomy** — Review the leading hallucination taxonomies (Ji et al. 2023 survey, Huang et al. 2023) and settle on a working classification that is precise enough to use as a reference frame in subsequent items.

2. **Macroscopic causes** — Summarise the training-data, objective-function, and RLHF-level explanations for why hallucinations occur. Note what each explanation predicts and where each falls short.

3. **Over-compliance as a hallucination cause** — Specifically investigate the link between sycophancy/over-compliance (agreeing with users or producing plausible-sounding outputs rather than accurate ones) and hallucination rates. This is the direct behavioural antecedent identified in the H-Neurons paper.

4. **Current mitigation landscape** — Catalogue the main mitigation strategies, their effectiveness, and their limitations. Note which mitigations operate at inference time (and therefore could benefit from neuron-level insight) vs. training time.

5. **The explanatory gap** — Articulate clearly what the macroscopic view cannot explain and why a neuron-level investigation is a logical next step. This frames the significance of the H-Neurons paper.

## Sources

- [ ] Ji et al. (2023) — "Survey of Hallucination in Natural Language Generation": https://arxiv.org/abs/2202.03629
- [ ] Huang et al. (2023) — "A Survey on Hallucination in Large Language Models": https://arxiv.org/abs/2311.05232
- [ ] Anthropic (2022) — "Constitutional AI": https://arxiv.org/abs/2212.08073
- [ ] Ouyang et al. (2022) — "Training language models to follow instructions with human feedback (InstructGPT/RLHF)": https://arxiv.org/abs/2203.02155
- [ ] Lewis et al. (2020) — "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks": https://arxiv.org/abs/2005.11401
- [ ] Perez et al. (2022) — "Sycophancy in AI assistants": https://arxiv.org/abs/2310.13548
- [ ] `Research/backlog/2026-03-05-h-neurons-in-llms.md` — the paper this item frames

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

-

---

## Output

- Type: knowledge
- Description: A clear taxonomy and causal map of LLM hallucinations, with explicit identification of the explanatory gap that the H-Neurons paper (arXiv:2512.01797) fills.
- Links:
  - `Research/backlog/2026-03-05-h-neurons-in-llms.md`
