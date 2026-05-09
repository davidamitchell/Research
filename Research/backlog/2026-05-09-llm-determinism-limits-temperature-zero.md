---
title: "Practical Limits of LLM Determinism: Temperature Zero, Fixed Seeds, and Constrained Prompts"
added: 2026-05-09T22:44:23+00:00
status: backlog
priority: high
blocks: []
tags: [llm, governance, agentic-ai, evaluation, ai-governance]
started: ~
completed: ~
output: []
cites: []
related:
  - 2026-05-09-governance-policy-determinism-vs-stochastic-llm
  - 2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance
  - 2026-05-09-compliance-risks-stochastic-llm-governance-decisions
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Practical Limits of LLM Determinism: Temperature Zero, Fixed Seeds, and Constrained Prompts

## Research Question

What are the practical limits of making LLM (Large Language Model)-based decisions or policy enforcement deterministic, even with temperature=0, fixed seeds, and constrained prompts?

## Scope

**In scope:**
- Empirical evidence on LLM output variability at temperature=0 and with fixed random seeds
- Sources of non-determinism beyond temperature: floating-point hardware variation, batching, model versioning, API infrastructure changes
- Structural prompt-engineering techniques (constrained output formats, grammar-based sampling, function calling) and their effect on reproducibility
- Implications for governance and compliance use cases requiring auditability

**Out of scope:**
- Theoretical ML proofs of stochasticity — focus is applied/empirical evidence
- Non-LLM probabilistic systems (Bayesian networks, diffusion models) except as comparators

**Constraints:** Focus on production-grade LLM APIs (OpenAI, Anthropic, open-source models via HuggingFace); peer-reviewed or well-sourced empirical findings preferred

## Context

A common engineering response to governance concerns about LLM variability is to set temperature=0 or use fixed seeds. However, multiple sources suggest that LLMs can still produce varied outputs under these settings due to hardware-level floating-point non-determinism, parallelisation, and model API version drift. Understanding the actual reproducibility envelope of constrained LLMs is essential before architects can determine which decisions can be delegated to LLM components and which require deterministic rule-based enforcement.

## Approach

1. Review empirical studies and developer reports on LLM output variability at temperature=0 across repeated calls
2. Identify all known sources of residual non-determinism in LLM inference (hardware, batching, kernel ordering, model updates)
3. Assess structured output techniques (JSON schema, grammar-constrained sampling, tool-use/function-calling) and their determinism properties
4. Synthesise a taxonomy of "determinism levels" achievable with current LLM infrastructure and the conditions for each

## Sources

- [ ] [OpenAI Reproducible Outputs documentation](https://platform.openai.com/docs/guides/reproducible-outputs) — official guidance on seed parameter and known limitations
- [ ] [Anthropic Claude API reference — temperature parameter](https://docs.anthropic.com/en/api/getting-started) — Anthropic's documentation on temperature and determinism
- [ ] [Ouyang et al. (2022) Training language models to follow instructions with human feedback (arXiv:2203.02155)](https://arxiv.org/abs/2203.02155) — InstructGPT paper; baseline understanding of RLHF-tuned model behaviour
- [ ] [Peng et al. (2023) LMQL: Interactively Constrained Language Model Queries (VLDB 2023)](https://lmql.ai/) — grammar-constrained LLM query language; empirical results on output control
- [ ] [Tamkin et al. (2021) Understanding the Capabilities, Limitations, and Societal Impact of Large Language Models (arXiv:2102.02503)](https://arxiv.org/abs/2102.02503) — limitations survey relevant to reproducibility

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
| | | high / medium / low | |

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type:
- Description:
- Links:
