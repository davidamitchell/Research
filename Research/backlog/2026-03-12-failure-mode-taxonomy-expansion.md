---
title: "Failure mode taxonomy: empirical frequency, causal mechanisms, detection signals, and cascade patterns in production agentic systems"
added: 2026-03-12
status: backlog
priority: high
blocks: []
tags: [failure-modes, taxonomy, hallucination, reward-hacking, prompt-injection, alignment, agentic-systems, owasp, safety, observability]
started: ~
completed: ~
output: [knowledge]
---

# Failure mode taxonomy: empirical frequency, causal mechanisms, detection signals, and cascade patterns in production agentic systems

## Research Question

The five-layer failure mode taxonomy established in `2026-03-10-ai-concept-classification-taxonomy.md` (Q5) provides a structurally sound classification, but leaves three empirical gaps unanswered: (1) which failure mode layers are most common in production agentic systems; (2) what are the precise causal mechanisms for each failure type at the model and system level; and (3) can failure modes cascade across layers — and if so, which cross-layer cascades are most dangerous? This item closes those gaps.

## Scope

**In scope:**
- Empirical evidence on failure mode frequency: which of the five layers (generation, goal, alignment, safety/security, operational) produces the most incidents in deployed agentic systems
- Causal mechanism depth for each layer: going beyond the taxonomy labels to the architectural or training-level cause of each failure type
- Detection signals: observable indicators (log patterns, metric anomalies, output signatures) that allow each failure type to be identified before it causes downstream harm
- Cascade analysis: which failure modes, if undetected, trigger failures in other layers (e.g. Layer 1 hallucination leading to Layer 2 goal drift; Layer 5 context overflow leading to Layer 1 generation failures)
- Cross-referencing the existing completed research corpus: which items speak directly to each layer (see Context below)
- Mapping each failure mode to the control category that addresses it (structural / semantic / procedural / architectural), extending the mapping in the parent taxonomy item

**Out of scope:**
- Rebuilding the top-level taxonomy — that is complete in `2026-03-10-ai-concept-classification-taxonomy.md`; this item deepens it, not replaces it
- Hardware-level or infrastructure failures not caused by AI system design
- Benchmark comparisons of specific LLM models on hallucination rates
- Full treatment of mitigation implementation (that belongs in follow-on engineering items)

**Constraints:** Evidence must come from production deployment reports, empirical studies, or credible practitioner sources — not purely theoretical. Inference labelling required for any claim that goes beyond available evidence.

## Context

The Q5 taxonomy from `2026-03-10-ai-concept-classification-taxonomy.md` defines five failure layers:

- **Layer 1 — Generation failures:** hallucination, sycophancy
- **Layer 2 — Goal failures:** intent mismatch, under-specification, goal drift
- **Layer 3 — Alignment failures:** reward hacking, specification gaming
- **Layer 4 — Safety/security failures:** prompt injection, guardrail bypass, excessive agency
- **Layer 5 — Operational failures:** context overflow, instruction conflict, unbounded consumption

That item explicitly flagged as an open question: *"Failure mode frequency in the wild — which failure mode layers are most common in production agentic systems? Empirical data would validate the taxonomy's practical utility."*

The corpus already contains substantial directly relevant prior research for several layers. This item must treat that prior work as primary evidence, not re-derive what is already settled:

### Prior research by layer

**Layer 1 — Generation failures**
- `2026-03-05-llm-hallucination-mechanisms.md` — hallucination types (intrinsic vs. extrinsic, factual vs. faithfulness), macroscopic root causes (training data noise, distributional shift, RLHF over-optimisation, sycophancy), and current mitigations (RAG, RLHF, constitutional AI, chain-of-thought). Establishes the explanatory gap that motivates neuron-level investigation.
- `2026-03-05-h-neurons-in-llms.md` — a sparse set of feed-forward network neurons (<0.1% of total) causally drives hallucination via over-compliance; generalises across models and tasks; global suppression insufficient for production.
- `2026-03-05-h-neuron-over-compliance.md` — precise causal chain: H-Neuron activation → over-compliance → hallucinated output. Covers activation steering (Representation Engineering, Inference-Time Intervention, ROME) and trade-offs of each intervention class.
- `2026-03-05-h-neuron-pretraining-origins.md` — H-Neurons are already predictive in base models before RLHF or instruction tuning; they form during pre-training from noisy/distributional data; RLHF cannot fully suppress them.
- `2026-03-05-h-neurons-synthesis.md` — unified intervention map: pre-training → fine-tuning/RLHF → inference-time monitoring → architectural choices; confidence calibration across claims.
- `2026-02-28-controlled-hallucination-perception-as-construction.md` — biological analogy: perception-as-hallucination as the generative default; useful conceptual contrast with LLM generation failures.

**Layer 2 — Goal failures**
- `2026-03-10-formal-spec-intent-alignment-agentic-coding.md` — specification hierarchy (informal → structured → contract → type-level → formal verification); intent mismatch in agentic coding systems; how richer specification structurally reduces goal failures; reward hacking as a Goodhart's Law phenomenon (covers both Layer 2 and Layer 3).
- `2026-03-08-context-engineering-first-principles.md` — token-level steering vs. goal-level steering; failure mode when context engineering produces compliance (Layer 1 satisfied) but not goal achievement (Layer 2 failure). Note: the parent taxonomy describes sycophancy as a "two-mechanism failure: high token-level compliance combined with systematic goal-level failure" — spanning both Layer 1 and Layer 2 — and has a known internal inconsistency: Key Finding 5 places sycophancy at Layer 1, while the Evidence Map places it at Layer 2. Resolving this boundary classification is in scope for this item.

**Layer 3 — Alignment failures**
- `2026-03-10-formal-spec-intent-alignment-agentic-coding.md` — reward hacking and specification gaming as alignment failures; Krakovna et al. 2020 specification gaming compendium; Gao et al. 2022 scaling laws for reward model overoptimisation; structural remedies at the specification level.

**Layer 4 — Safety/security failures**
- `2026-03-01-agent-lsp-policy-enforcement.md` — real-time LSP-like policy enforcement for headless agentic coding agents; architectural approaches to in-loop guardrail enforcement before code is committed; OPA + LSP, Semgrep LSP, MCP tool wrappers as guardrail mechanisms.
- `2026-02-28-ai-line-1-line-2-risk-agents.md` — governance architecture for AI agents operating within the three-lines-of-defence model; accountability, human oversight, and escalation when agents perform risk oversight functions; regulatory acceptability of AI-generated assurance.

**Layer 5 — Operational failures**
- `2026-03-08-context-engineering-first-principles.md` — context overflow as a failure mode when the context window is exhausted; instruction conflict when multiple instructions contradict each other; the engineering of context as a mitigation for operational failures.

**Parent taxonomy**
- `2026-03-10-ai-concept-classification-taxonomy.md` — full five-layer taxonomy definition and controls-to-failures mapping; the anchor item for this research.

## Approach

1. **Empirical frequency survey** — Search for production incident reports, empirical studies, and practitioner benchmarks that give frequency data on which failure mode layers occur most often in deployed agentic and LLM systems. Sources: OWASP LLM Top 10 2025 rationale (frequency data behind ranking), published incident post-mortems, academic benchmarks (HELM, BIG-Bench, TruthfulQA for Layer 1; specification gaming compendium for Layer 3; red-team studies for Layer 4).

2. **Causal mechanism depth per layer** — For each layer, draw on prior research (cited above) to articulate the precise causal chain from architecture or training to observed failure. For layers not yet covered in depth (Layer 4 and Layer 5 in particular), conduct fresh investigation. Produce a causal diagram or structured summary per layer.

3. **Detection signal identification** — For each failure type, identify the earliest observable signal that indicates a failure has occurred or is imminent. Distinguish: (a) output-observable signals (response patterns, anomalous token distributions, confidence scores); (b) trace-observable signals (tool call sequences, latency spikes, token budget exhaustion); (c) system-observable signals (audit logs, policy violation flags, resource consumption metrics).

4. **Cascade analysis** — Investigate whether failures in one layer predictably cause failures in another. Construct a directed failure cascade graph: nodes are failure types, edges indicate empirically observed or strongly inferred triggering relationships. Identify the most dangerous cascades (high impact, hard to detect at source).

5. **Control mapping extension** — Extend the controls-to-failures mapping from the parent taxonomy to include: which detection signal triggers which control; what the latency of each control type is (structural controls are instant; procedural controls introduce human-in-the-loop latency); and what the failure mode of the control itself is (when does the control fail to fire?).

6. **Synthesis and prioritisation** — Produce a prioritised failure mode register: each failure type ranked by (frequency × impact × detectability). This register becomes the primary output artefact.

## Sources

- [ ] `Research/completed/2026-03-10-ai-concept-classification-taxonomy.md` — parent taxonomy (Q5 section); required reading before beginning
- [ ] `Research/completed/2026-03-05-llm-hallucination-mechanisms.md` — Layer 1 foundation
- [ ] `Research/completed/2026-03-05-h-neurons-in-llms.md` — Layer 1 causal mechanism
- [ ] `Research/completed/2026-03-05-h-neuron-over-compliance.md` — Layer 1 intervention mechanics
- [ ] `Research/completed/2026-03-05-h-neurons-synthesis.md` — Layer 1 unified intervention map
- [ ] `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md` — Layer 2 and 3
- [ ] `Research/completed/2026-03-08-context-engineering-first-principles.md` — Layer 2 and 5
- [ ] `Research/completed/2026-03-01-agent-lsp-policy-enforcement.md` — Layer 4
- [ ] `Research/completed/2026-02-28-ai-line-1-line-2-risk-agents.md` — Layer 4 governance
- [ ] OWASP Top 10 for LLM Applications 2025 (frequency rationale): https://owasp.org/www-project-top-10-for-large-language-model-applications/
- [ ] Krakovna et al. (2020) — Specification Gaming compendium (Layer 3 empirical frequency): https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/
- [ ] Ji et al. (2023) — Survey of Hallucination in LLMs (Layer 1 taxonomy and frequency): https://arxiv.org/abs/2202.03629
- [ ] Gao et al. (2022) — Scaling laws for reward model overoptimisation (Layer 3 empirical): https://arxiv.org/abs/2210.10760
- [ ] HELM / TruthfulQA benchmarks — Layer 1 empirical frequency in deployed systems
- [ ] Perez et al. (2022) — Sycophancy in AI assistants (Layer 1/2 boundary): https://arxiv.org/abs/2310.13548
- [ ] Production incident post-mortems from AI safety incident databases (e.g. AIAAIC repository): https://www.aiaaic.org/
