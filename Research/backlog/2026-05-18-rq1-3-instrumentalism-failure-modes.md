---
title: "RQ 1.3 — Failure Modes of Instrumentalism When Applied to Complex Dynamic Systems Under Distribution Shift"
added: 2026-05-18T19:40:00+00:00
status: backlog
priority: high
blocks:
  - 2026-05-18-rq2-1-erm-causal-blindness
tags: [epistemology, philosophy-of-science, machine-learning, causal-inference]
started: ~
completed: ~
output: [knowledge]
cites:
  - 2026-05-18-rq1-1-popper-falsifiability
  - 2026-05-18-rq1-2-deutsch-hard-to-vary
related:
  - 2026-05-18-rq1-1-popper-falsifiability
  - 2026-05-18-rq1-2-deutsch-hard-to-vary
  - 2026-05-18-rq2-1-erm-causal-blindness
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# RQ 1.3 — Failure Modes of Instrumentalism When Applied to Complex Dynamic Systems Under Distribution Shift

## Research Question

What are the operational failure modes of an epistemic framework that prioritises instrumentalism (predictive performance) over explanatory reach when applied to complex dynamic systems undergoing structural or distribution shifts?

## Scope

**In scope:**
- Instrumentalism vs. scientific realism as competing epistemic frameworks for model evaluation
- Goodhart's Law in the context of model optimisation and metric gaming
- Structural break detection and distribution shift as empirical stress tests of purely predictive models
- Documented real-world failure cases where instrumentalist models collapsed under distribution shift

**Out of scope:**
- Theoretical philosophy of science beyond directly applicable framings
- Cases where instrumentalist models succeeded under shift (counter-evidence is captured but not the primary focus)

**Constraints:** Must draw on formal treatments from RQ 1.1 and RQ 1.2; illustrative failures should be grounded in documented cases.

## Context

The first two items in this phase established the epistemological tools for evaluating models. This item asks: what happens in practice when those tools are ignored and pure predictive performance (instrumentalism) drives model selection? The answer directly motivates Phases 2–4: it shows why Empirical Risk Minimisation (ERM) is epistemically insufficient, why LLMs fail on out-of-distribution (OOD) prompts, and why agentic loops cannot compensate for a causally blind core model.

## Approach

1. Characterise the instrumentalist position in machine learning (optimise only for predictive accuracy on training distribution).
2. Apply Goodhart's Law: when predictive metrics become targets, they cease to be good measures.
3. Survey structural break scenarios: economic model failures (2008 financial crisis), epidemiological model failures (COVID-19), recommendation system failures under preference drift.
4. Formalise the failure mode: show how distribution shift exposes the absence of invariant causal structure.
5. Connect to Pearl's causal hierarchy as a theoretical explanation of why instrumentalist models cannot recover.

## Sources

- [ ] [Friedman, M. (1953) The Methodology of Positive Economics — University of Chicago Press](https://doi.org/10.7208/chicago/9780226264011.001.0001) — primary instrumentalist position in economics
- [ ] [Pearl, J. (2000) Causality: Models, Reasoning, and Inference — Cambridge University Press](https://doi.org/10.1017/CBO9780511803161) — causal hierarchy as explanation for instrumentalist failure
- [ ] [Goodhart, C. A. E. (1975) Problems of Monetary Management — Reserve Bank of Australia conference paper](https://www.rba.gov.au/publications/confs/1975/pdf/goodhart.pdf) — original formulation of Goodhart's Law
- [ ] [Sugihara, G. et al. (2012) Detecting Causality in Complex Ecosystems — Science Vol 338](https://doi.org/10.1126/science.1227079) — empirical evidence of distribution shift exposing non-causal models

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
