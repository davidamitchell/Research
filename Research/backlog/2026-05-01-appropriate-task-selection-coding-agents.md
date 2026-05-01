---
title: "What criteria define tasks where AI coding agents reliably add value versus where they introduce systemic risk?"
added: 2026-05-01T08:17:39+00:00
status: backlog
priority: high
blocks: []
tags: [agentic-ai, coding-agents, software-engineering, governance, llm]
started: ~
completed: ~
output: []
cites: []
related: [2026-05-01-compound-error-accumulation-ai-codebases, 2026-05-01-human-oversight-ai-software-development, 2026-05-01-sustainable-ai-software-development-synthesis]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What criteria define tasks where AI coding agents reliably add value versus where they introduce systemic risk?

## Research Question

What empirically grounded criteria define the characteristics of software development tasks where AI coding agents reliably add value, versus tasks where agent autonomy introduces unacceptable systemic risk?

## Scope

**In scope:**
- Characteristics of well-suited agent tasks: bounded scope, verifiable success criteria, non-mission-critical, repetitive/boring, and good isolation (agent can find everything it needs in context)
- Characteristics of poorly suited agent tasks: unbounded scope, no objective success function, mission-critical, high global interdependency, or requiring architectural judgment
- Evidence from practitioner accounts and empirical studies on task types where agent performance is reliable vs. degraded
- The role of modularity: how codebase structure affects which tasks are safe to delegate
- Specific task categories named in the talk: bug reproduction, rubber-duck debugging, boilerplate, non-critical polishing, reproduction cases
- Hill-climbing and auto-evaluation patterns as enablers of reliable agent use

**Out of scope:**
- Detailed treatment of agent benchmarks (covered in the TerminalBench item)
- Compound error accumulation (covered in the compound error item)
- Full governance framework (covered in the synthesis item)

**Constraints:**
- Prefer evidence from controlled studies or structured practitioner accounts over anecdote
- Task categorisations should be actionable: a developer should be able to apply them to a specific work item

## Context

At a 2026 developer conference, Mario (Pi coding agent creator) offered a framework for task selection: good agent tasks have a scope the agent is guaranteed to find all context for, a function to evaluate how well it performed, and are non-mission-critical or boring. He specifically named: reproduction cases for user issues, rubber-duck debugging, and anything where the correctness criteria are explicit. He argued that the discipline of "learn to say no" — deliberately choosing not to delegate certain tasks to agents — is the most valuable current capability for software developers. This item investigates whether that intuition is backed by evidence and whether it can be formalised into actionable criteria.

## Approach

1. **Practitioner task taxonomies** — Document the task characteristics from the talk and survey other published practitioner frameworks (e.g., Karpathy's "vibe coding" critique, other developer accounts) for overlap and divergence.
2. **Empirical evidence** — What controlled studies or structured evaluations exist on the reliability of coding agents across task types? Survey SWE-bench task categories and their failure modes as a proxy.
3. **The scope and evaluability criteria** — Why do bounded scope and evaluability matter so much? Survey the agent planning and benchmark literature on the relationship between task definition quality and agent success rate.
4. **Modularity as an enabler** — What evidence exists that codebase modularity (small, well-bounded modules) correlates with better agent task success? Review software architecture literature on modularity and change isolation.
5. **Actionable taxonomy** — Synthesise the above into a practical decision framework: given a specific work item, what questions should a developer ask to determine whether to delegate it to an agent?

## Sources

- [ ] [Mario (2026) — Pi coding agent talk transcript](https://github.com/davidamitchell/Research) — primary task selection framework and rationale
- [ ] [Jimenez et al. (2024) — SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) — empirical data on agent success rates by task type
- [ ] [Karpathy (2025) — Software Is Changing (Again)](https://karpathy.ai/blog/software-is-changing) — practitioner perspective on appropriate vs. inappropriate AI code generation
- [ ] [Parnas (1972) — On the Criteria To Be Used in Decomposing Systems into Modules](https://dl.acm.org/doi/10.1145/361598.361623) — foundational modularity theory; information hiding as a modularity criterion
- [ ] [Brooks (1987) — No Silver Bullet: Essence and Accidents of Software Engineering](https://dl.acm.org/doi/10.1109/MC.1987.1663532) — essential vs. accidental complexity; relevant to distinguishing delegatable from non-delegatable tasks

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

### Open Questions

---

## Output

- Type:
- Description:
- Links:
