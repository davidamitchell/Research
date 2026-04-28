---
title: "Universal Entity Lifecycle Governance Framework (UELGF) extension: agentic Artificial Intelligence (AI)-specific risks and runtime monitoring for non-deterministic behaviour"
added: 2026-04-28T07:19:00+00:00
status: backlog
priority: high
blocks: []
tags: [uelgf, agentic-ai, emergent-behaviour, goal-misalignment, multi-agent, hallucination, runtime-monitoring, non-determinism, observability, governed-golden-rail]
started: ~
completed: ~
output: [knowledge]
---

# UELGF extension: agentic AI-specific risks and runtime monitoring for non-deterministic behaviour

## Research Question

What agentic Artificial Intelligence (AI)-specific risk categories — specifically emergent behaviour, goal misalignment, multi-agent interaction failures, and hallucinations in decision loops — are insufficiently addressed by the current Universal Entity Lifecycle Governance Framework (UELGF) runtime feedback loop, and what runtime monitoring design is required to detect and respond to non-deterministic behaviour at the governed golden-rail layer?

## Scope

**In scope:**
- Taxonomy of agentic AI-specific risk categories not fully addressed by the UELGF runtime feedback loop as specified in `2026-04-27-uelgf-runtime-feedback-loop`: emergent behaviour, goal misalignment, multi-agent interaction failures, and hallucinations propagated into decision loops
- Definition and characterisation of non-deterministic behaviour in agentic systems: what makes agentic AI outputs non-deterministic, why non-determinism creates governance gaps that deterministic software controls do not address, and what observable signals distinguish acceptable variance from policy-violating drift
- Runtime monitoring design requirements for non-deterministic agents: what signals must be collected, at what frequency, with what latency, and by what mechanism to enable the UELGF runtime feedback loop to close on agentic-specific failure modes
- Multi-agent interaction risks: emergent behaviour arising from agent-to-agent communication, unintended capability composition, and cascading decision loops that no single agent's policy covers
- Hallucination-in-decision-loop risk: how hallucinated outputs propagate into automated downstream actions, what monitoring detects propagation before action execution, and what circuit-breaker designs interrupt the loop
- Goal misalignment detection: what observable deviations from intended agent behaviour indicate goal drift or reward hacking, and what monitoring signals are sensitive to early misalignment before downstream harm materialises
- Integration points between the proposed monitoring design and the existing UELGF governed golden-rail scaffold, runtime feedback loop signal taxonomy, and automated response taxonomy
- Gap analysis against the current UELGF framework specification — explicit identification of which components require extension versus which require new specification

**Out of scope:**
- Training-time alignment techniques (focus is on runtime governance of deployed agents, not pre-deployment alignment)
- Safety engineering of new agent architectures (focus is on governance controls for agents that already exist and enter the governed rail)
- Formal verification or theorem proving of agent behaviour
- Jurisdiction-specific legal obligations beyond those already addressed in the UELGF companion items

**Constraints:**
- Must be grounded in the existing UELGF framework specification (`2026-04-27-uelgf-synthesis-complete-framework`) — extension items must reference and be compatible with existing definitions, entity taxonomy, and policy architecture
- Must produce findings that are actionable at the governed golden-rail layer, not only at the research or model level
- Evidence must include at least one primary source per risk category (emergent behaviour, goal misalignment, multi-agent risk, hallucination propagation)

## Context

The UELGF complete framework synthesis (`2026-04-27-uelgf-synthesis-complete-framework`) specifies a runtime feedback loop with a signal taxonomy and automated response taxonomy. However, the synthesis explicitly notes that the framework governs entities that enter the rail, and its feedback loop was designed with deterministic software and citizen-developed low-code entities as the primary risk profile. Agentic AI systems introduce qualitatively different risks: their outputs are non-deterministic, their behaviour can drift over time without any code change, and multi-agent compositions can exhibit emergent behaviour that no single agent's policy covers.

The referenced agentic AI pieces — `2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment`, `2026-04-26-agentic-ai-foundational-conditions-dependency-ordering`, and `2026-04-26-ai-agent-control-plane-architecture-enterprise` — establish preconditions and control plane architecture but do not specify runtime monitoring requirements for non-deterministic behaviour. This item closes that gap.

Cross-references:
- `2026-04-27-uelgf-runtime-feedback-loop` — the primary UELGF component being extended
- `2026-04-27-uelgf-governed-golden-rails` — the rail layer where monitoring integration points must be specified
- `2026-04-26-ai-agent-control-plane-architecture-enterprise` — existing control-plane design context
- `2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment` — regulatory precondition baseline
- `2026-04-27-pip-invariant-anomaly-detection` — Policy Information Point (PIP) anomaly detection patterns relevant to drift detection

## Approach

1. **Agentic risk taxonomy:** Review academic and practitioner literature to produce a structured taxonomy of agentic AI-specific risks at runtime: emergent behaviour, goal misalignment, multi-agent interaction failures, hallucination propagation into decision loops. For each category, identify: what causes it, what observable signals it produces, and what existing UELGF components (if any) partially address it.
2. **Non-determinism characterisation:** Establish a working definition of non-deterministic behaviour in agentic systems that is actionable at the governance layer — distinguishing acceptable variance (model temperature effects, valid path variation) from policy-violating drift (repeated boundary violations, anomalous action sequences). Review existing literature on runtime behavioural envelopes for AI systems.
3. **Runtime monitoring design requirements:** For each risk category in the taxonomy, specify what monitoring signals are required, what collection mechanism is feasible within a governed rail, and what automated responses are appropriate (halt, escalate, flag, quarantine). Map proposed signals to the existing UELGF signal taxonomy and identify gaps.
4. **Multi-agent interaction risk:** Investigate how multi-agent architectures create emergent risks not visible at the single-agent layer, what monitoring designs detect inter-agent interaction anomalies, and whether the existing UELGF entity taxonomy needs extension to model agent-to-agent relationships.
5. **Hallucination propagation circuit-breaker design:** Review the literature on hallucination detection and propagation in automated decision loops. Specify what pre-action verification checkpoints, confidence-gating mechanisms, and circuit-breaker patterns are required within the governed rail to interrupt propagation before action execution.
6. **Gap analysis and framework extension specification:** Produce a structured gap analysis against the current UELGF runtime feedback loop and governed golden-rail specification. For each gap, propose the minimal extension required and confirm compatibility with the existing policy architecture, entity taxonomy, and decommission lifecycle.
7. **Synthesis:** Produce findings as an extension specification — a structured document that can be appended to or referenced by the UELGF complete framework without requiring redesign of existing components.

## Sources

- [ ] [UELGF complete framework synthesis](https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-synthesis-complete-framework.html) — primary framework being extended
- [ ] [UELGF runtime feedback loop](https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html) — specific component under extension
- [ ] [UELGF governed golden rails](https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-governed-golden-rails.html) — rail layer integration points
- [ ] [Agentic AI regulatory preconditions and control failure assessment](https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html) — existing agentic risk baseline
- [ ] [AI agent control plane architecture in the enterprise](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html) — control plane context
- [ ] [PIP invariant anomaly detection](https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html) — anomaly detection patterns
- [ ] [NIST AI Risk Management Framework 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) — governs AI-specific risks including non-determinism and emergent behaviour
- [ ] [Anthropic model specification](https://www.anthropic.com/research/claude-character) — primary-source treatment of goal alignment and behaviour specification for deployed agents
- [ ] [OpenAI, Practices for Governing Agentic AI Systems](https://openai.com/research/practices-for-governing-agentic-ai) — primary-source treatment of multi-agent risks and monitoring obligations from a leading AI developer
- [ ] [DeepMind, Evaluating the Capabilities and Risks of AI Agents](https://deepmind.google/research/) — academic research on emergent behaviour and capability evaluation
- [ ] [Perez et al., Ignore Previous Prompt: Attack Techniques For Language Models](https://arxiv.org/abs/2211.09527) — primary-source treatment of hallucination and prompt-injection propagation in decision loops
- [ ] [Weidinger et al., Taxonomy of Risks posed by Language Models](https://dl.acm.org/doi/10.1145/3531146.3533088) — structured taxonomy of language model risks applicable to governance classification

---

## Research Skill Output

*(To be populated when this item moves to in-progress.)*

### §0 Initialise

-

### §1 Question Decomposition

-

### §2 Investigation

-

### §3 Reasoning

-

### §4 Consistency Check

-

### §5 Depth and Breadth Expansion

-

### §6 Synthesis

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

-

---

## Findings

*(To be populated from §6 Synthesis when this item completes.)*

### Executive Summary

### Key Findings

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

- Type: knowledge
- Description:
- Links:
