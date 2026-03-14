---
title: "Can organisational intent be expressed as a formally structured specification from which artefacts are derived and consistency is machine-checked?"
added: 2026-03-14
status: backlog
priority: high
blocks: []
tags: [formal-methods, strategy, okrs, goal-modelling, normative-systems, hoshin-kanri, resource-allocation, consistency-checking, funding, intent]
started: ~
completed: ~
output: [knowledge]
---

# Can organisational intent be expressed as a formally structured specification from which artefacts are derived and consistency is machine-checked?

## Research Question

Can organisational intent — mission, values, strategy, resource allocation — be expressed as a formally structured specification from which human-readable artefacts are derived, and against which Objectives and Key Results (OKRs), funding decisions, and initiative prioritisation can be continuously checked for logical consistency and derivability?

## Scope

**In scope:**
- Formal specification languages and frameworks applicable to organisational intent: Catala, i*/iStar (Goal-oriented Requirements Language), Deon Digital Contract Specification Language (CSL), and Goal-Oriented Requirements Engineering (GORE) broadly
- Normative systems and norm conflict detection from the Artificial Intelligence (AI) and Law literature — specifically coherence and consistency checking across abstraction layers
- Goal derivability: whether the relationship between a strategic objective and an initiative can be checked as a formal derivation rather than a narrative assertion
- Hoshin Kanri X-matrix as a structured derivation chain from strategic objectives to initiatives and metrics — specifically whether machine-checking replaces the workshop process
- Beyond Budgeting (Hope & Fraser) critique: annual funding cycles as structural decoupling of resource allocation from strategic intent; how a formal spec would need to incorporate funding triggers
- Real Options theory (Trigeorgis) applied to initiative portfolios: framing investment decisions as option-exercising against uncertainty and stated risk appetite
- Rumelt's "Good Strategy / Bad Strategy" kernel model (diagnosis, guiding policy, coherent actions) as a near-structured specification
- Resource-Based View (RBV) and dynamic capabilities (Teece): deriving build-vs-buy decisions from formal strategic position
- EOSIO Ricardian Template Toolkit as a concrete example of machine-readable + human-readable dual artefacts derived from a single canonical source
- Near-decomposability (Simon) applied to intent propagation across abstraction layers
- Eric Yu's original iStar thesis on Strategic Dependency (SD) and Strategic Rationale (SR) models

**Out of scope:**
- Business Process Model and Notation (BPMN) / process execution languages (focus is strategic intent, not operational workflow)
- Detailed programming language semantics for Catala beyond its prose/spec inversion methodology
- Specific OKR tooling implementations (focus is on formal foundations, not vendor software)
- Performance management or HR appraisal systems as such

**Constraints:**
- Prioritise sources that engage with *machine-checkability* rather than just structured frameworks designed for human use
- Distinguish between *consistency* (no contradiction between elements) and *derivability* (an element can be formally derived from a higher-level specification) — these are different properties with different checking mechanisms
- Academic sources should be balanced with practitioner frameworks; Hoshin Kanri has decades of industrial application

## Context

Organisations produce strategy documents, OKR hierarchies, funding allocations, and initiative portfolios as separate artefacts, typically in different tools, at different cadences, and by different teams. The connections between them are maintained by narrative, convention, and periodic workshops rather than by any formal relationship. As a result, it is possible — and common — for an approved initiative to be weakly or even negatively related to stated objectives, with no mechanism to detect this until a retrospective review.

The connective thread this research explores: a formal strategy specification should make it possible to ask "is this initiative *derived from*, or merely *consistent with*, stated objectives?" — and to get a checkable answer rather than a narrative one. The funding corollary is whether resource allocation decisions are expressions of policy-as-strategy or are separate political processes that happen to reference strategy language post-hoc.

Two adjacent fields have partially solved related problems: formal contract languages (Ricardian contracts, CSL) separate machine-executable obligation from human-readable prose by deriving both from a single canonical source; and goal-oriented requirements engineering (i*/iStar, Catala) provides formal decomposition of goals into tasks and resources. The question is whether these tools and their underlying ideas transfer to the organisational strategy domain.

## Approach

1. **Formal foundations survey** — survey Catala's prose/spec inversion, i*/iStar Strategic Rationale (SR) model, Deon Digital CSL, and the normative consistency literature. For each: what is the formal model, what properties can be checked, and what is the cost of specification?

2. **Goal derivability and OKR chains** — examine Hoshin Kanri X-matrix as a near-formal derivation chain. Determine what properties of the X-matrix make derivation checkable (or not), and what would need to be added to support machine-checking. Compare with OKR cascade approaches and identify where they lose formal structure.

3. **Funding as strategy policy** — engage Beyond Budgeting's critique of annual funding cycles. Model what a "funding trigger" would look like in a formal strategy spec: a conditional allocation rule derived from strategic state rather than a calendar-driven negotiation.

4. **Real options and risk appetite** — examine Trigeorgis' real options framework applied to initiative portfolios. Identify whether the formal model (option type, exercise conditions, underlying asset) can be grounded in a formal strategy spec in a way that makes investment decisions checkable against stated risk appetite.

5. **Normative consistency across abstraction layers** — investigate the near-decomposability problem (Simon) as applied to intent: specifically how a value stated at mission level must propagate as a binding constraint into initiative selection without re-interpretation at each layer. Survey norm conflict detection methods from AI & Law literature.

6. **Ricardian contracts as a precedent** — examine EOSIO Ricardian Template Toolkit as a working example of dual-artefact generation (machine-readable + human-readable) from a single canonical source. Assess what design choices make this work and whether they translate to strategy artefacts.

7. **Synthesis** — characterise what a "formal strategy specification" would need to include (elements, relations, constraints), what consistency and derivability checking would look like in practice, and what the adoption cost/benefit trade-off looks like compared with existing structured-but-informal approaches (Hoshin Kanri, OKR cascades, balanced scorecards).

## Sources

- [ ] **Yu, E. (1995) — Modelling Strategic Relationships for Process Reengineering.** PhD thesis, University of Toronto. Original iStar thesis — SD and SR models.
- [ ] **Yu, E. & Mylopoulos, J. (1994) — Understanding "Why" in Software Process Modelling, Analysis and Design.** ICSE 1994. Foundational goal-orientation in requirements.
- [ ] **Catala language documentation and Merigoux et al. (2021) — Catala: A Programming Language for the Law.** ICFP 2021. Prose/spec inversion methodology.
- [ ] **Clack, C.D., Bakshi, V.A., & Braine, L. (2016) — Smart Contract Templates: foundations, design landscape and research directions.** arXiv. Ricardian contracts and dual-artefact generation.
- [ ] **EOSIO Ricardian Template Toolkit — documentation and specification.** (github.com/EOSIO/ricardian-template-toolkit)
- [ ] **Governatori, G. et al. (2016) — Detecting Semantic Inconsistencies in Business Process Models.** Norm conflict detection methodology.
- [ ] **Governatori, G. & Rotolo, A. (2008) — Logic of Violation: A Gentzen System for Reasoning with Contrary-to-Duty Obligations.** Australasian Journal of Logic. Normative consistency foundations.
- [ ] **Deon Digital — Contract Specification Language (CSL) documentation.** deon.digital. Normative obligation language separating intent from execution.
- [ ] **Hoshin Kanri X-matrix method** — Hutchins, G. (2008) *Hoshin Kanri: The Strategic Approach to Continuous Improvement*; Jackson, T.L. (2006) *Hoshin Kanri for the Lean Enterprise*.
- [ ] **Hope, J. & Fraser, R. (2003) — Beyond Budgeting: How Managers Can Break Free from the Annual Performance Trap.** Harvard Business School Press. Structural critique of funding cycle decoupling.
- [ ] **Trigeorgis, L. (1996) — Real Options: Managerial Flexibility and Strategy in Resource Allocation.** MIT Press. Real options applied to initiative portfolios.
- [ ] **Rumelt, R. (2011) — Good Strategy / Bad Strategy: The Difference and Why It Matters.** Crown Business. Kernel model and falsifiability of strategy.
- [ ] **Teece, D.J., Pisano, G., & Shuen, A. (1997) — Dynamic Capabilities and Strategic Management.** Strategic Management Journal 18(7). Build-vs-buy derivability from strategic position.
- [ ] **Simon, H.A. (1962) — The Architecture of Complexity.** Proceedings of the American Philosophical Society 106(6). Near-decomposability applied to intent propagation.
- [ ] **van Lamsweerde, A. (2001) — Goal-Oriented Requirements Engineering: A Guided Tour.** RE 2001. Survey of Goal-Oriented Requirements Engineering (GORE) methods including formal properties.
- [ ] **Fuxman, A. et al. (2004) — Specifying and Analyzing Early Requirements in Tropos.** Requirements Engineering 9(2). Formal analysis in i*/Tropos.

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Restate the research question. Confirm scope, constraints, and output format.

-

### §1 Question Decomposition

Approach sub-questions broken into atomic questions — each answerable with a single evidence-based claim.

-

### §2 Investigation

Evidence gathered per atomic question. Label each claim: **[fact]**, **[inference]**, or **[assumption]** with source.

-

### §3 Reasoning

Facts, inferences, and assumptions explicitly separated. No unsupported generalisations or narrative leaps.

-

### §4 Consistency Check

Internal contradictions identified and resolved (or explicitly flagged where unresolvable).

-

### §5 Depth and Breadth Expansion

Findings re-examined through relevant lenses (technical, regulatory, economic, historical, behavioural).

-

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly.

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim.

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

Explicit assumptions made during the investigation and the justification for each.

- **Assumption:** ... **Justification:** ...

### Analysis

How the evidence was weighed, what trade-offs were identified, and how competing interpretations were resolved.

### Risks, Gaps, and Uncertainties

What is still unknown? Where does the evidence fall short? What could change the conclusion?

-

### Open Questions

Questions that surfaced during research but are out of scope for this item. Each may become a new backlog item.

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
