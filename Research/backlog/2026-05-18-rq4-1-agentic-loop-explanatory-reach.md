---
title: "RQ 4.1 — Agentic Loops and Explanatory Reach: Does Wrapping an LLM Introduce Genuine Understanding or Just Delay Failure?"
added: 2026-05-18T19:40:00+00:00
status: backlog
priority: high
blocks:
  - 2026-05-18-rq4-2-adversarial-error-propagation
tags: [agentic-ai, llm, machine-learning, causal-inference, evaluation]
started: ~
completed: ~
output: [knowledge]
cites:
  - 2026-05-18-rq3-3-cot-counterfactual-limits
  - 2026-05-18-rq3-1-llm-statistical-vs-causal
related:
  - 2026-05-18-rq3-3-cot-counterfactual-limits
  - 2026-05-18-rq4-2-adversarial-error-propagation
  - 2026-05-18-rq4-3-ood-generalization-agentic
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# RQ 4.1 — Agentic Loops and Explanatory Reach: Does Wrapping an LLM Introduce Genuine Understanding or Just Delay Failure?

## Research Question

When an LLM is wrapped in an agentic loop (Perception → Strategy Selection → Tool Action → Verification), does the outer loop introduce true explanatory reach, or does it merely delay failure when encountering novel inputs?

## Scope

**In scope:**
- The ReAct (Reason and Act) paradigm as a representative agentic loop architecture
- Error cascade analysis: how a single incorrect step in a multi-step agentic loop propagates to subsequent steps
- State space search vs. epistemic discovery as competing models of what agentic loops accomplish
- Whether adding tool access and a feedback loop gives an LLM access to Level 2 or Level 3 causal reasoning

**Out of scope:**
- Specific agent frameworks (LangChain, AutoGen, CrewAI) beyond their formal properties
- Multi-agent coordination (addressed elsewhere)

**Constraints:** Must build on Phase 3's findings; must evaluate explanatory reach in formal terms from Phase 2 (causal hierarchy levels).

## Context

Phase 3 established that LLMs are statistical optimisers that do not acquire causal models and that CoT prompting does not cross any causal hierarchy boundary. Phase 4 asks: does wrapping the LLM in an agentic loop — giving it tools, a verification step, and a feedback mechanism — change this fundamental limitation? The ReAct paradigm is the canonical architecture. This item is the entry point for Phase 4 and directly blocks Phase 5's comparison of stochastic vs. deterministic systems.

## Approach

1. Formally characterise the agentic loop: Perception (input parsing), Strategy Selection (planning), Tool Action (external call), Verification (output check), Retry.
2. Apply the causal hierarchy test: can any component of the agentic loop produce interventional or counterfactual outputs that the core LLM cannot?
3. Model error cascade: if the LLM makes a Level 1 error in Strategy Selection, how does that propagate through Tool Action and Verification?
4. Survey empirical evidence of agentic systems: where do ReAct-style agents succeed, and where do they fail in ways consistent with the causal hierarchy analysis?
5. Classify agentic loops: does the outer scaffolding elevate the system's causal hierarchy level, or is the composite system still Level 1 with more steps?

## Sources

- [ ] [Yao, S. et al. (2022) ReAct: Synergizing Reasoning and Acting in Language Models — arXiv:2210.03629](https://arxiv.org/abs/2210.03629) — canonical agentic loop architecture; primary source for the Perception-Action-Verification loop
- [ ] [Shinn, N. et al. (2023) Reflexion: Language Agents with Verbal Reinforcement Learning — NeurIPS 2023](https://arxiv.org/abs/2303.11366) — agentic loop with internal feedback; tests whether feedback improves genuine reasoning
- [ ] [Mialon, G. et al. (2023) Augmented Language Models: a Survey — arXiv:2302.07842](https://arxiv.org/abs/2302.07842) — survey of tool-augmented LLMs and their formal properties
- [ ] [Valmeekam, K. et al. (2023) Large Language Models Still Can't Plan — NeurIPS 2023 Workshop](https://arxiv.org/abs/2206.10498) — empirical evidence that agentic wrapping does not resolve LLM planning limitations

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
