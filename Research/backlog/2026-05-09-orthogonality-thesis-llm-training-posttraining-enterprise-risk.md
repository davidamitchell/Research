---
title: "Orthogonality thesis under modern Large Language Model (LLM) training and post-training: implications for enterprise agentic workload risk"
added: 2026-05-09T01:45:34+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []
tags: [agentic-ai, llm, alignment, enterprise, ai-governance, operational-risk, mechanistic-interpretability]
started: ~
completed: ~
output: [knowledge]
cites:
  - 2026-04-30-orthogonality-thesis-ai-alignment-interpretability
  - 2026-04-30-human-bias-ai-trust-rlhf-sycophancy
  - 2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring
related:
  - 2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain
  - 2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls
  - 2026-04-26-ai-agent-control-plane-architecture-enterprise
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Orthogonality thesis under modern Large Language Model (LLM) training and post-training: implications for enterprise agentic workload risk

## Research Question

How should the orthogonality thesis be interpreted for modern Large Language Models (LLMs) given current pre-training and post-training methods, and what does that imply for enterprise risk when agentic workloads are allowed to plan, use tools, and take actions inside production environments?

## Scope

**In scope:**
- The original orthogonality thesis and its claims about capability-goal separation
- How modern LLM pre-training shapes broad capabilities without directly specifying stable enterprise-safe objectives
- How post-training methods, including Supervised Fine-Tuning (SFT), Reinforcement Learning from Human Feedback (RLHF), Direct Preference Optimisation (DPO), and constitution-style training, change behaviour without necessarily proving durable goal alignment
- The extent to which current interpretability and evaluation work can distinguish behavioural compliance from underlying objective robustness
- Risk implications for enterprise agentic workloads that can retrieve context, call tools, chain actions, or act with delegated permissions
- What governance, monitoring, and assurance posture follows if post-training is better understood as behaviour-shaping than objective-certifying

**Out of scope:**
- A full survey of all alignment theory beyond what is needed to answer the enterprise deployment question
- Speculative superintelligence scenarios not needed for present-day enterprise decisions
- Vendor-by-vendor product comparison
- Detailed mathematical treatment of individual optimisation algorithms unless it materially changes the risk conclusion

**Constraints:**
- Keep the answer anchored to current LLM training and post-training practice rather than purely philosophical argument
- Separate what is evidenced for present-day frontier and production models from what remains hypothetical
- End with an operational enterprise risk framing that can inform deployment, controls, and assurance decisions

## Context

The existing completed item on the orthogonality thesis explains why capability does not by itself reveal goals, but this issue asks a narrower and more operational follow-up: whether modern training and post-training pipelines materially weaken, preserve, or merely mask that separation in deployed LLM systems. That matters because enterprises are increasingly deploying agentic workloads on the assumption that post-trained assistants are not just more helpful but also more reliably aligned, even when those systems can use tools, traverse internal context, and trigger downstream actions. The answer should help distinguish between "the model behaves well in benchmarked conditions" and "the deployment is safe enough to trust with enterprise agency."

## Approach

1. **Re-state the core thesis in current terms** — Translate the orthogonality thesis from general Artificial Intelligence (AI) philosophy into claims that can be tested or bounded for present-day LLMs.
2. **Map the training stack** — Separate what pre-training, instruction tuning, preference optimisation, and constitution-style post-training each plausibly do to objectives, behaviours, and failure modes.
3. **Review empirical evidence** — Examine work on alignment faking, sycophancy, goal misgeneralisation, deceptive or strategically compliant behaviour, and mechanistic interpretability limits to see whether current evidence weakens or supports the thesis in practice.
4. **Test the enterprise leap** — Assess whether common enterprise assumptions about helpfulness, harmlessness, and policy-following survive when the model is embedded in agentic workflows with memory, tools, and delegated permissions.
5. **Derive a risk model** — Identify what classes of enterprise risk follow if post-training improves behaviour under observation without proving stable underlying alignment.
6. **Translate to controls** — Specify what governance, monitoring, evaluation, and containment controls are justified for enterprises deploying agentic workloads under that uncertainty.

## Sources

- [ ] [Bostrom (2012) The Superintelligent Will: Motivation and Instrumental Rationality in Advanced Artificial Agents](https://nickbostrom.com/superintelligentwill.pdf) — original orthogonality-thesis framing
- [ ] [Ouyang et al. (2022) Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) — canonical Reinforcement Learning from Human Feedback (RLHF) post-training paper
- [ ] [Rafailov et al. (2023) Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) — preference-optimisation alternative to RLHF
- [ ] [Anthropic (2024) Alignment faking in large language models](https://www.anthropic.com/research/alignment-faking) — evidence relevant to behaviour under monitoring versus underlying preference preservation
- [ ] [Anthropic (2025) Tracing the thoughts of a language model](https://www.anthropic.com/research/tracing-thoughts-language-model) — current interpretability capability and limits for reasoning traces
- [ ] [Mitchell (2026) The orthogonality thesis in Artificial Intelligence (AI) alignment: intelligence, goals, and the limits of interpretability](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-orthogonality-thesis-ai-alignment-interpretability.md) — completed repository item establishing the base thesis and interpretability framing
- [ ] [Mitchell (2026) Human cognitive bias toward Artificial Intelligence (AI) correctness and explainability: automation bias, Reinforcement Learning from Human Feedback (RLHF) sycophancy, and mechanistic interpretability limits](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-human-bias-ai-trust-rlhf-sycophancy.md) — repository item on post-training incentives, explanation trust, and interpretability limits
- [ ] [Mitchell (2026) Universal Entity Lifecycle Governance Framework (UELGF) extension: agentic Artificial Intelligence (AI)-specific risks and runtime monitoring for non-deterministic behaviour](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.md) — repository item on runtime monitoring requirements for deployed agentic systems

## Related

- [The orthogonality thesis in Artificial Intelligence (AI) alignment: intelligence, goals, and the limits of interpretability](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-orthogonality-thesis-ai-alignment-interpretability.md)
- [Human cognitive bias toward Artificial Intelligence (AI) correctness and explainability: automation bias, Reinforcement Learning from Human Feedback (RLHF) sycophancy, and mechanistic interpretability limits](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-human-bias-ai-trust-rlhf-sycophancy.md)
- [What control-plane architecture is required to manage Artificial Intelligence (AI) agents and low-code systems as distributed, semi-autonomous actors within enterprise environments?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-ai-agent-control-plane-architecture-enterprise.md)

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

-

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
| | | | |

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

### Open Questions

---

## Output

- Type: knowledge
- Description:
- Links:
