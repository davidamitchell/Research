---
title: "What Are We Losing and Gaining by Inserting Agentic Systems Into Production Workflows?"
added: 2026-05-18T19:40:00+00:00
status: backlog
priority: high
blocks: []
tags: [agentic-ai, llm, workflow, evaluation, formal-methods]
started: ~
completed: ~
output: [knowledge, backlog-item]
cites:
  - 2026-05-18-agentic-explainability-vs-traditional
  - 2026-05-18-rq5-2-flexibility-vs-predictability-auditability
  - 2026-05-18-rq6-3-complexity-horizon-classical-systems
related:
  - 2026-05-18-agentic-explainability-vs-traditional
  - 2026-05-18-rq5-1-stochastic-vs-deterministic-failures
  - 2026-05-18-rq5-2-flexibility-vs-predictability-auditability
  - 2026-05-18-rq4-3-ood-generalization-agentic
superseded_by: ~
supersedes: ~
item_type: synthesis
confidence: medium
versions: []
---

# What Are We Losing and Gaining by Inserting Agentic Systems Into Production Workflows?

## Research Question

What are we concretely losing and gaining — across the dimensions of capability, reliability, auditability, explainability, and organisational risk — by inserting agentic systems into production workflows and systems that were previously served by deterministic coded software or human operators?

## Scope

**In scope:**
- Capability gains: tasks that agentic systems can perform that deterministic code cannot do practically (open-ended language generation, multi-step reasoning over unstructured input, adaptive tool use)
- Reliability losses: how agentic systems reduce formal verifiability, determinism, and crash-fast failure behaviour
- Auditability losses: how reduced explainability (see predecessor item) affects regulatory compliance and incident investigation
- Organisational risk changes: how inserting agentic systems changes the risk profile of the organisation operating the pipeline
- Decision framework: under what conditions is the net tradeoff positive for a production system?

**Out of scope:**
- Cost and infrastructure economics of agentic vs. coded systems
- Narrow AI tools (classifiers, recommenders) that are not agentic in the loop sense defined in Phase 4

**Constraints:** This is the terminal synthesis item for the entire research programme; it should produce a structured, evidence-backed decision framework grounded in all preceding items. The output type includes `backlog-item` because the decision framework may warrant implementation as a tool or checklist.

## Context

This item is the terminus of the dependency chain. Every preceding phase has built a piece of the answer:
- Phase 1 established the epistemological distinction between prediction and explanation.
- Phase 2 proved the mathematical limits of observational learning.
- Phase 3 characterised LLM epistemic limitations.
- Phase 4 showed that agentic wrapping does not resolve those limitations.
- Phase 5 compared agentic and coded failure modes.
- Phase 6 established that classical systems are not trivially reliable or transparent.
- The explainability synthesis item provided a formal comparative verdict.

This item synthesises all of that into a practitioner-oriented answer: given that both system classes have fundamental limitations, when does the net tradeoff favour agentic insertion, and when does it not?

## Approach

1. Compile a structured gains register from the research programme: what do agentic systems genuinely add that deterministic code cannot match?
2. Compile a structured losses register: what formal guarantees, failure properties, and auditability capabilities are forfeited when a deterministic pipeline component is replaced by an agentic system?
3. Weight the tradeoffs by production context: regulated vs. unregulated, high-stakes vs. low-stakes, reversible vs. irreversible actions.
4. Construct a decision framework: a set of criteria and questions that a practitioner can use to evaluate whether a specific agentic insertion is net-positive.
5. Identify the category of tasks where agentic insertion is clearly net-positive, clearly net-negative, and genuinely uncertain.

## Sources

- [ ] [Brynjolfsson, E. & McAfee, A. (2014) The Second Machine Age — W. W. Norton](https://www.wwnorton.com/books/the-second-machine-age/) — macro-level analysis of what automation gains and loses relative to human operators
- [ ] [Wieringa, R. J. (2014) Design Science Methodology for Information Systems and Software Engineering — Springer](https://doi.org/10.1007/978-3-662-43839-8) — design science framework for evaluating artefact tradeoffs; applicable to the gains/losses schema
- [ ] [European Parliament (2024) EU AI Act — Official Journal of the European Union](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) — regulatory framework defining high-risk AI contexts where losses are non-negotiable
- [ ] [Anthropic (2024) Claude Model Card and Usage Policy](https://www.anthropic.com/model-card) — primary vendor documentation of known agentic system limitations; source for capability boundaries

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

- Type: knowledge, backlog-item
- Description:
- Links:
