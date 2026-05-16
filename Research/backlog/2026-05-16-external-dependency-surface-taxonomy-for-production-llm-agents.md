---
title: "External Dependency Surface Taxonomy for Production LLM Agents"
added: 2026-05-16T05:29:47+00:00
status: backlog
priority: high
blocks: []
tags: [agentic-ai, llm, agent-tooling, evaluation]
started: ~
completed: ~
output: []
---

# External Dependency Surface Taxonomy for Production LLM Agents

## Research Question

What is the complete taxonomy of external dependencies for a production Large Language Model (LLM)-based agent, how does each dependency class fail, what is the blast radius of each failure class, and which existing frameworks from software supply chain security, operational risk, and distributed systems engineering are applicable?

## Scope

**In scope:**
- Dependency classes spanning model providers, safety layers, harness software development kits, tool APIs, identity and permissions, and runtime context documents.
- Observed failure modes caused by provider behaviour changes, harness updates, and tool API drift.
- Applicability and limits of existing governance frameworks analogous to software bills of materials.

**Out of scope:**
- Building a production implementation of a dependency-surface registry.
- Legal analysis of contract terms for specific model providers.

**Constraints:**
- Prioritise incident evidence and operational postmortems where available.
- Clearly separate deterministic software dependencies from non-deterministic model-behaviour dependencies.

## Context

The thesis argues that do-mode agents carry an underpriced operational risk because their dependency surface is wider and less observable than standard software systems. This item establishes the taxonomy needed to quantify and govern that risk.

## Approach

1. Define dependency classes and map each class to failure triggers, observability limits, and blast radius.
2. Gather incident evidence attributable to provider, harness, or API change rather than application-layer defects.
3. Evaluate existing frameworks such as software supply chain controls and financial operational risk methods for adaptation to agent systems.

## Sources

- [ ] [NIST AI Risk Management Framework 1.0](https://www.nist.gov/itl/ai-risk-management-framework) — baseline AI risk categories and controls.
- [ ] [CISA Secure Software Development Attestation and Supply Chain Guidance](https://www.cisa.gov/secure-software-development-attestation-form) — software dependency governance patterns.
- [ ] [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — LLM-specific failure classes and controls.
- [ ] [Basel Committee Principles for the Sound Management of Operational Risk](https://www.bis.org/bcbs/publ/d352.htm) — operational risk framework reference.

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

- Type:
- Description:
- Links:
