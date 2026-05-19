---
title: "RQ 4.2 — Adversarial Inputs and Error Propagation Through Agentic Verification and Strategy Phases"
added: 2026-05-18T19:40:00+00:00
status: backlog
priority: high
blocks:
  - 2026-05-18-rq4-3-ood-generalization-agentic
tags: [agentic-ai, llm, machine-learning, evaluation]
started: ~
completed: ~
output: [knowledge]
cites:
  - 2026-05-18-rq4-1-agentic-loop-explanatory-reach
related:
  - 2026-05-18-rq4-1-agentic-loop-explanatory-reach
  - 2026-05-18-rq4-3-ood-generalization-agentic
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# RQ 4.2 — Adversarial Inputs and Error Propagation Through Agentic Verification and Strategy Phases

## Research Question

How do adversarial inputs or unexpected environmental shifts propagate error through an agentic system's verification and strategy-selection phases when the core underlying model lacks a grounding in the system's causal mechanisms?

## Scope

**In scope:**
- Semantic drift: gradual corruption of the agent's working context across multi-step inference
- Cascading failure modes in the Perception → Strategy → Action → Verification loop
- Brittle heuristics in verification loops: how verification steps based on LLM self-assessment fail under adversarial input
- Formal error propagation model for multi-step agentic sequences
- Prompt injection as a concrete class of adversarial input for agentic systems

**Out of scope:**
- Adversarial attacks on underlying model weights (white-box gradient attacks)
- Defences against adversarial inputs (the focus is characterising the failure, not fixing it)

**Constraints:** Builds directly on RQ 4.1's error cascade analysis; must model error propagation formally, not just catalogue failure cases.

## Context

RQ 4.1 established that the agentic loop does not elevate the LLM above Level 1 causal reasoning and that errors in Strategy Selection propagate. This item models that propagation formally under adversarial conditions. Adversarial inputs are particularly revealing because they expose the brittleness of heuristic verification: when an attacker constructs inputs that look correct to the LLM but are semantically corrupted, the verification phase cannot detect the error because it uses the same causally blind model. This is the formal basis for the safety concerns in Phase 5's comparison with deterministic systems.

## Approach

1. Define the adversarial input model for agentic systems: inputs that are in-distribution for the LLM (it assigns them high probability) but are semantically corrupted or malicious.
2. Model error propagation through the loop: if Perception generates a corrupted state representation, how does that corrupt Strategy Selection, Tool Action, and Verification in sequence?
3. Formalise brittle verification: show that LLM self-verification cannot detect errors that are within its own distributional blind spots.
4. Survey prompt injection attacks as empirical evidence of adversarial propagation through agentic systems.
5. Quantify: what is the error amplification factor across N steps of an agentic loop under adversarial input?

## Sources

- [ ] [Amodei, D. et al. (2016) Concrete Problems in AI Safety — arXiv:1606.06565](https://arxiv.org/abs/1606.06565) — formal taxonomy of AI safety failure modes; includes specification gaming and reward hacking relevant to agentic verification
- [ ] [Goodfellow, I. J. et al. (2014) Explaining and Harnessing Adversarial Examples — arXiv:1412.6572](https://arxiv.org/abs/1412.6572) — foundational adversarial examples work; basis for understanding adversarial input construction
- [ ] [Perez, F. & Ribeiro, I. (2022) Ignore Previous Prompt: Attack Techniques For Language Models — NeurIPS 2022 ML Safety Workshop](https://arxiv.org/abs/2211.09527) — prompt injection as the canonical adversarial attack on agentic LLM systems
- [ ] [Ziegler, D. M. et al. (2022) Adversarial Training for High-Stakes Reliability — NeurIPS 2022](https://arxiv.org/abs/2205.01663) — empirical evidence of adversarial failure modes in deployed LLM systems

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

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

*(Populated from §6 Synthesis above.)*

### Executive Summary

### Key Findings

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|

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
