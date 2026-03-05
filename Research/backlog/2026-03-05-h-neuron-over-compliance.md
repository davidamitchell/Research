---
title: "Over-Compliance in LLMs — How H-Neurons Drive Sycophancy and What Interventions Are Possible"
added: 2026-03-05
status: backlog
priority: medium
blocks: [2026-03-05-h-neurons-synthesis]
tags: [llm, hallucinations, h-neurons, over-compliance, sycophancy, interventions, alignment, reliability, mechanistic-interpretability]
started: ~
completed: ~
output: [knowledge]
---

# Over-Compliance in LLMs — How H-Neurons Drive Sycophancy and What Interventions Are Possible

## Research Question

What exactly is over-compliance behaviour in LLMs, how do Hallucination-Associated Neurons (H-Neurons) cause it, and what neuron-level and inference-time interventions are feasible to reduce it without degrading general model capability?

## Scope

**In scope:**
- Precise definition of "over-compliance" as a behavioural pattern in LLMs (agreeing with incorrect premises, generating plausible-but-false outputs, failing to refuse, sycophancy)
- The causal mechanism identified in arXiv:2512.01797: H-Neurons → over-compliance → hallucination
- Controlled intervention methodology used in the paper: how suppressing/amplifying H-Neurons changes over-compliance rates
- Broader literature on LLM sycophancy as a hallucination pathway
- Practical intervention options at inference time: neuron activation steering, representation engineering, inference-time monitoring using H-Neuron activation as a signal
- Training-time mitigations: data curation, objective modification, targeted regularisation on H-Neuron activations
- Trade-offs: does suppressing H-Neurons reduce capability elsewhere?

**Out of scope:**
- H-Neuron identification methodology (covered in `2026-03-05-h-neurons-in-llms`)
- Pre-training origins of H-Neurons (covered in `2026-03-05-h-neuron-pretraining-origins`)
- General hallucination taxonomy (covered in `2026-03-05-llm-hallucination-mechanisms`)

**Constraints:** Builds on `2026-03-05-h-neurons-in-llms` — must be researched after that item is complete. Primary evidence from arXiv:2512.01797 and contemporaneous activation steering / representation engineering literature.

## Context

One of the three key findings of Gao et al. (arXiv:2512.01797) is that H-Neurons are not just correlated with hallucination — they are causally linked through a specific behavioural pathway: **over-compliance**. Over-compliance is the tendency of LLMs to produce outputs that conform to the user's apparent expectations or to generate fluent, confident-sounding text even when the model does not "know" the answer. It is the mechanism by which a model chooses a plausible hallucination over a truthful admission of uncertainty.

Understanding this pathway in detail — and what can be done about it — is the most immediately actionable finding of the paper. If H-Neuron activations can be monitored at inference time, they become a real-time hallucination risk signal. If they can be suppressed (via activation steering or representation engineering), hallucination rates may be reduced without retraining.

## Approach

1. **Over-compliance taxonomy** — Define and distinguish: sycophancy (agreeing with user errors), over-confidence (claiming certainty without basis), confabulation (generating false but fluent continuations), and instruction-following failure modes. Map each to the over-compliance behavioural pathway.

2. **H-Neurons → over-compliance causal chain** — From the paper's intervention experiments, reconstruct exactly how H-Neuron activation leads to over-compliance behaviour. What does suppression do to the model's output distribution? What happens to refusal rates, uncertainty expressions, and factual accuracy?

3. **Activation steering literature** — Investigate the state of the art in activation steering: Representation Engineering (Zou et al., 2023), direct logit attribution, causal tracing (ROME). How do these techniques relate to what Gao et al. do in their intervention experiments?

4. **Inference-time monitoring** — Can H-Neuron activation levels be used as a real-time hallucination risk score during inference? What would this look like architecturally (probe layer, threshold, fallback behaviour)? What latency overhead would it introduce?

5. **Training-time interventions** — What would it mean to train a model to minimise H-Neuron activation? Could targeted regularisation or data curation suppress H-Neuron formation? What are the risks (suppressing useful generative behaviour along with hallucination-prone behaviour)?

6. **Trade-off analysis** — Enumerate the costs and benefits of each intervention class (activation steering at inference, runtime monitoring, training-time). Produce a trade-off table: effectiveness, engineering cost, latency cost, capability risk.

## Sources

- [ ] Gao et al. (2025) — "Hallucination-Associated Neurons in LLMs" (primary source for H-Neuron causal mechanism): https://arxiv.org/abs/2512.01797
- [ ] Zou et al. (2023) — "Representation Engineering: A Top-Down Approach to AI Transparency": https://arxiv.org/abs/2310.01405
- [ ] Perez et al. (2022) — "Sycophancy to Subterfuge: Investigating Reward Tampering in Language Models": https://arxiv.org/abs/2310.13548
- [ ] Anthropic (2022) — "Discovering Language Model Behaviors with Model-Written Evaluations": https://arxiv.org/abs/2212.09251
- [ ] Li et al. (2023) — "Inference-Time Intervention: Eliciting Truthful Answers from a Language Model": https://arxiv.org/abs/2306.03341
- [ ] Meng et al. (2022) — "ROME: Locating and Editing Factual Associations in GPT": https://arxiv.org/abs/2202.05262
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

- Can H-Neuron suppression be made selective — reducing hallucination-prone over-compliance without reducing legitimate compliant behaviour (e.g., appropriate instruction-following)?
- At what point does over-compliance suppression produce an excessively "stubborn" or unhelpful model?
- Are there task categories where H-Neuron activation does not correspond to over-compliance but to some other behaviour?

---

## Output

- Type: knowledge
- Description: A detailed account of the over-compliance behavioural pathway linking H-Neurons to hallucination, with a structured evaluation of neuron-level intervention options (activation steering, inference-time monitoring, training-time regularisation) and their trade-offs.
- Links:
  - https://arxiv.org/abs/2512.01797
  - `Research/backlog/2026-03-05-h-neurons-in-llms.md`
