---
title: "General Agent Optimization Framework"
added: 2026-03-05
status: backlog
priority: high
blocks: []
tags: [ai-agents, optimization, benchmarks, dspy, evaluation, self-improvement, prompt-engineering, synthetic-data]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# General Agent Optimization Framework

## Research Question

What is the most principled architecture for a Self-Improving AI Agent Evaluation Loop — specifically, how should a nested inner/outer loop be designed so that a "Meta-Optimizer" rewrites system prompts based on failure analysis without causing instruction drift or overfitting to specific training questions?

## Scope

**In scope:**
- Nested-loop architecture: inner loop (instruction optimization via Meta-Optimizer) and outer loop (robustness through semantic/adversarial variation)
- Principled, generic prompt updates (e.g., rule generalisation) versus specific data injection, and the tradeoffs between them
- Benchmark landscape: general reasoning (GPQA, HLE, MMLU-Pro) and tool-use (GAIA, AgentBench) benchmarks as evaluation harnesses
- Domain-specific benchmarks: FinBen (Finance), LegalBench (Law), SWE-bench (Coding) as "Ground Truth" sources for specialised agents
- Proprietary "Golden Sets": feasibility and methodology for building domain-specific question sets from sources such as Chambers and Partners' Global Practice Guides
- DSPy framework: teleprompters, optimizers, and how they automate inner-loop instruction updates
- Synthetic data generation as the primary fuel for the outer loop's variation engine
- Instruction drift risk: "Brevity Penalties" and "Prompt Pruning" techniques
- Balancing general-reasoning benchmarks with specialised Golden Sets

**Out of scope:**
- Full implementation of a running evaluation harness (that is a downstream tooling item)
- Fine-tuning or weight-level training; this research is limited to prompt/instruction-level optimization
- Infrastructure provisioning (compute, hosting, MLOps pipelines)

**Constraints:** Focus on techniques that are feasible using LLM APIs (no local GPU training assumed). Prioritise peer-reviewed sources, official framework documentation, and established benchmark papers.

## Context

Current agents in this repo (and in production AI deployments generally) are evaluated ad hoc: prompts are tuned by hand, there is no systematic loop that measures failure, generalises a fix, and validates the fix does not regress. As agent complexity grows — multi-step reasoning, tool use, domain knowledge — this manual approach breaks down.

A Self-Improving Evaluation Loop addresses this gap by closing the feedback cycle: (1) run agent on a held-out test set, (2) classify failures, (3) update the system prompt with a generic rule that addresses the failure class, (4) verify the update improves performance across paraphrased variants of the failing question. The outer loop prevents overfitting by continuously generating semantic and adversarial variations.

This research is strategically urgent because:
- The repo's research-loop workflow is currently limited by manual prompt tuning.
- Domain-specific benchmarks (FinBen, LegalBench) are directly relevant to NZ financial services and legal contexts that this repo tracks.
- DSPy is an actively maintained framework that could be integrated into existing Python tooling (`src/`) with minimal new infrastructure.

## Approach

1. **Architecture survey** — Review published literature and blog posts on automated prompt optimization loops. Identify the canonical inner-loop/outer-loop formulation and any named variants (APE, OPRO, DSPy Teleprompters, TextGrad).
2. **Benchmark mapping** — For each of GPQA, HLE, MMLU-Pro, GAIA, AgentBench, FinBen, LegalBench, SWE-bench: document data format, license, size, evaluation metric, and suitability as a training/test split for an optimization loop.
3. **Chambers & Partners feasibility** — Assess whether publicly available Chambers Global Practice Guides can serve as a structured Golden Set source (licensing, structured Q&A availability, coverage of NZ/APAC jurisdictions).
4. **DSPy deep dive** — Read DSPy documentation and the original paper (Khattab et al., 2023). Understand how `BootstrapFewShot`, `MIPRO`, and `BayesianSignatureOptimizer` work. Assess API requirements and cost profile.
5. **Synthetic data generation** — Survey methods for generating semantically equivalent paraphrases and adversarial variants (back-translation, LLM paraphrase prompting, checklist-based perturbations). Identify which methods preserve answer correctness and which introduce noise.
6. **Instruction drift analysis** — Review empirical findings on prompt length vs performance degradation. Identify concrete "Brevity Penalty" formulations (e.g., penalise token count in the optimizer objective) and "Prompt Pruning" heuristics (redundancy detection, coverage-based trimming).
7. **Synthesis and recommendation** — Produce a technical blueprint: recommended architecture, benchmark selection strategy, DSPy integration points, and a go/no-go assessment for building a proprietary Golden Set from Chambers sources.

## Sources

- [ ] Khattab et al. (2023) — "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines" — https://arxiv.org/abs/2310.03714
- [ ] Yang et al. (2024) — "OPRO: Large Language Models as Optimizers" — https://arxiv.org/abs/2309.03409
- [ ] Zhou et al. (2023) — "Large Language Models Are Human-Level Prompt Engineers (APE)" — https://arxiv.org/abs/2211.01910
- [ ] Yuksekgonul et al. (2024) — "TextGrad: Automatic 'Differentiation' via Text" — https://arxiv.org/abs/2406.07496
- [ ] Rein et al. (2023) — "GPQA: A Graduate-Level Google-Proof Q&A Benchmark" — https://arxiv.org/abs/2311.12022
- [ ] Mialon et al. (2023) — "GAIA: A Benchmark for General AI Assistants" — https://arxiv.org/abs/2311.12983
- [ ] Xie et al. (2024) — "FinBen: A Holistic Financial Benchmark for Large Language Models" — https://arxiv.org/abs/2402.12659
- [ ] Guha et al. (2023) — "LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models" — https://arxiv.org/abs/2308.11462
- [ ] Jimenez et al. (2024) — "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?" — https://arxiv.org/abs/2310.06770
- [ ] Liu et al. (2023) — "AgentBench: Evaluating LLMs as Agents" — https://arxiv.org/abs/2308.03688
- [ ] DSPy documentation — https://dspy.ai/
- [ ] Chambers and Partners Global Practice Guides — https://practiceguides.chambers.com/ (assess licensing and structured Q&A availability)
- [ ] HLE (Humanity's Last Exam) — https://agi.safe.ai/ (assess data access and format)
- [ ] MMLU-Pro — https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro

---

## Findings

*(Fill in when completing. Follow the research skill synthesis structure.)*

### Executive Summary

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

- Type: knowledge, backlog-item
- Description:
- Links:
