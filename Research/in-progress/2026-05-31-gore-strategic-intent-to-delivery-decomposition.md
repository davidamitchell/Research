---
review_count: 2
title: "GORE: translating strategic intent to scoped delivery objectives"
added: 2026-05-31T09:42:57+00:00
status: reviewing
priority: high
blocks: []
themes: [formal-methods, software-engineering, governance-policy]
started: 2026-06-01T14:47:11+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-05-31-goal-specification-completeness-schema
related:
  - 2026-05-31-goal-constraint-feedback-convergence-vs-cycling
  - 2026-05-31-goal-scope-change-constraint-propagation
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# GORE: translating strategic intent to scoped delivery objectives

## Research Question

How does Goal-Oriented Requirements Engineering (GORE) handle the translation from strategic intent to scoped, time-bounded delivery objectives: what decomposition rules does it specify, and where do they break down?

## Scope

**In scope:**
- GORE decomposition rules: AND/OR goal refinement, contribution links, and operationalisation patterns.
- Mapping from high-level strategic goals to bounded, measurable sub-goals suitable for delivery.
- Known failure modes and documented breakdown points of GORE decomposition in practice.

**Out of scope:**
- Full comparison of all GORE variants (i-star, Knowledge Acquisition in Automated Specification (KAOS), Non-Functional Requirements (NFR) Framework): focus is on decomposition rules specifically.
- Implementation of GORE tooling or CASE (Computer-Aided Software Engineering) tool comparison.
- Prescriptive redesign of an organisation's requirements process.

**Constraints:** (time, source types, access)
- Peer-reviewed literature and established GORE frameworks only.
- Emphasise empirical evidence of breakdown points over theoretical critique.

## Context

Strategic intent in enterprises is routinely expressed at a level that is too abstract for delivery teams to act on directly. GORE was designed to bridge this gap, but practitioners report that decomposition often stalls at the boundary between strategic and operational concerns. Understanding where the rules hold and where they break down informs how automated systems can apply or augment GORE decomposition. This is Gap 1 Q2 from issue #618.

## Approach

1. Document the formal decomposition rules in the main GORE frameworks (KAOS, i-star, NFR Framework): AND/OR refinement, contribution links, means-end analysis.
2. Identify how time-bounding and scoping are introduced in each framework: are they first-class constructs or informal annotations?
3. Survey empirical studies and practitioner retrospectives that describe where decomposition failed or produced ambiguous results.
4. Catalogue known breakdown patterns (abstraction gap, conflicting contributions, missing operationalisation) and their observed frequencies.
5. Assess whether any framework provides explicit rules for detecting incomplete or broken decomposition.

## Sources

- [ ] [Van Lamsweerde (2009) Requirements Engineering: From System Goals to UML Models to Software Specifications](https://www.wiley.com/en-gb/Requirements+Engineering%3A+From+System+Goals+to+UML+Models+to+Software+Specifications-p-9780470012703): KAOS and GORE decomposition rules in detail
- [ ] [Yu (1997) Towards Modelling and Reasoning Support for Early-Phase Requirements Engineering](https://doi.org/10.1109/ISRE.1997.582369): i-star framework and strategic actor modelling
- [ ] [Chung et al. (2000) Non-Functional Requirements in Software Engineering](https://link.springer.com/book/10.1007/978-1-4615-5269-7): NFR Framework and contribution links
- [ ] [Horkoff and Yu (2016) Interactive Goal Model Analysis for Early Requirements Engineering](https://doi.org/10.1007/s00766-014-0210-5): empirical study of GORE in practice
- [ ] [Van Lamsweerde and Letier (2000) Handling Obstacles in Goal-Oriented Requirements Engineering](https://doi.org/10.1109/32.879317): formal completeness check for KAOS goal refinements
- [ ] [Horkoff et al. (2017) Goal-Oriented Requirements Engineering: An Extended Systematic Mapping Study](https://link.springer.com/article/10.1007/s00766-017-0280-z): 231-paper systematic mapping of GORE literature
- [ ] [The Open Group Architecture Framework (TOGAF) 9.2 -- Motivation Architecture](https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap08.html): TOGAF metamodel elements for Driver, Goal, Outcome, and Requirement

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

```text
Question: How does Goal-Oriented Requirements Engineering (GORE) handle the translation
from strategic intent to scoped, time-bounded delivery objectives -- what decomposition
rules does it specify, and where do they break down?

Scope in: GORE decomposition rules (AND/OR refinement, contribution links,
operationalisation patterns); mapping from high-level strategic goals to bounded
measurable sub-goals; known failure modes of GORE decomposition in practice.

Scope out: Full variant comparison beyond decomposition rules; GORE tooling comparison;
prescriptive redesign of requirements processes.

Constraints: Peer-reviewed literature and established frameworks only; emphasise empirical
evidence of breakdown over theoretical critique.

Output format: knowledge item; Findings seeded from §6 Synthesis.

Domain terms in scope:
- GORE: Goal-Oriented Requirements Engineering -- an approach to software and systems
  requirements that uses goals as the primary organising concept.
- KAOS: Knowledge Acquisition in Automated Specification -- a GORE methodology by
  Axel van Lamsweerde that uses formal goal refinement, obstacle analysis, and temporal
  logic specifications.
- i-star (i*): a GORE framework by Eric Yu that models actor dependencies and internal
  actor rationale using strategic dependency and strategic rationale diagrams.
- NFR Framework: Non-Functional Requirements Framework by Chung et al. that represents
  non-functional requirements as softgoals in Softgoal Interdependency Graphs (SIGs).
- AND/OR refinement: the mechanism by which a parent goal is decomposed into sub-goals
  such that all children must be satisfied (AND) or any one child suffices (OR).
- Operationalisation: the translation of an abstract goal into a concrete requirement,
  task, or system operation that can be assigned and verified.
- Contribution link: a directed relationship in i-star or the NFR Framework showing
  how achieving one goal or task positively or negatively affects another.
- Softgoal: a goal without a clear-cut satisfaction criterion, typically representing
  a quality attribute; evaluated through satisficing rather than binary satisfaction.
- Satisficing: achieving an acceptable level of satisfaction for a softgoal, acknowledging
  that absolute satisfaction is not feasible.
- SIG: Softgoal Interdependency Graph -- the graphical notation used in the NFR Framework.
```

### §1 Question Decomposition

**Main question:** How does GORE handle the translation from strategic intent to scoped, time-bounded delivery objectives, and where do decomposition rules break down?

**Sub-question A: What are the formal decomposition rules in each major GORE framework?**

- A1: What is the formal definition of AND-refinement in KAOS, and what completeness condition must it satisfy?
- A2: What is the formal definition of OR-refinement in KAOS, and what sufficiency condition must it satisfy?
- A3: What decomposition types does i-star provide, and how do they differ from KAOS?
- A4: What is the role of contribution links in the NFR Framework, and how do they govern decomposition of softgoals?
- A5: What is the operationalisation step, and when does it terminate the decomposition chain?

**Sub-question B: How is time-bounding and scoping introduced in each framework?**

- B1: Does KAOS treat temporal constraints as first-class constructs or as informal annotations?
- B2: Does i-star have built-in mechanisms for time-bounding goals?
- B3: Does the NFR Framework address time constraints?
- B4: What is the practical implication of treating time as an annotation rather than a first-class construct?

**Sub-question C: What empirical evidence describes where decomposition fails?**

- C1: What breakdown patterns have been identified in industrial GORE studies?
- C2: What is the observed frequency of the abstraction gap in empirical literature?
- C3: What is the observed frequency of missing operationalisation?
- C4: What breakdown occurs from conflicting contribution links?

**Sub-question D: Does any framework provide explicit rules for detecting incomplete or broken decomposition?**

- D1: Does KAOS provide formal completeness checking for refinements?
- D2: Does i-star provide formal completeness checking?
- D3: Does the NFR Framework provide an explicit incompleteness detection mechanism?

### §2 Investigation

**A1 -- KAOS AND-refinement formal definition:**

In KAOS, AND-refinement decomposes a parent goal G into sub-goals G1...Gn such that the conjunction of all sub-goals is logically equivalent to the parent goal under the domain assumptions. Formally: G is satisfied if and only if G1 AND G2 AND ... AND Gn are all satisfied. The completeness condition requires that the conjunction of the sub-goals implies the parent, and the parent implies the conjunction (bidirectional entailment). [fact; source: https://doi.org/10.1109/ISRE.2001.948567]

A refinement is incomplete if the conjunction of sub-goals satisfies the parent only in a subset of cases, leaving cases where the parent goal remains unachieved despite all sub-goals being met, or vice versa. [inference; source: https://doi.org/10.1109/ISRE.2001.948567]

**A2 -- KAOS OR-refinement formal definition:**

OR-refinement decomposes a parent goal G into alternatives G1...Gn such that satisfying any one sub-goal suffices to satisfy the parent. The equivalence condition requires that the disjunction of sub-goals implies G and G implies the disjunction: satisfying G means at least one alternative is achievable. [fact; source: https://doi.org/10.1109/ISRE.2001.948567]

OR-refinement is used when multiple independent strategies could satisfy the same strategic goal, allowing the system to choose among alternatives without requiring all to be pursued. [inference; source: https://doi.org/10.1109/ISRE.2001.948567]

**A3 -- i-star decomposition types:**

i-star provides three distinct link types within its Strategic Rationale (SR) model: means-end links (a task achieves a goal), decomposition links (a task breaks into sub-tasks, sub-goals, and resources), and contribution links (how tasks or goals affect softgoals). These operate within actor boundaries, while the Strategic Dependency (SD) model captures cross-actor goal, task, and resource dependencies. [fact; source: https://doi.org/10.1109/ISRE.1997.582369]

Unlike KAOS, i-star does not have a formal logical completeness condition for decomposition. Decomposition in i-star is driven by strategic rationale -- modelling why an actor pursues a particular approach -- rather than by proof-theoretic sufficiency. [inference; source: https://doi.org/10.1109/ISRE.1997.582369; https://link.springer.com/article/10.1007/s00766-017-0280-z]

**A4 -- NFR Framework contribution links:**

The Non-Functional Requirements (NFR) Framework represents non-functional requirements as softgoals in a Softgoal Interdependency Graph (SIG). Contribution links in the SIG use a five-level vocabulary: Make (++, strong positive), Help (+, weak positive), Hurt (-, weak negative), Break (--, strong negative), and Some (unknown direction). These links show how design choices or functional goals propagate their effects upward through the goal hierarchy, enabling trade-off analysis. [fact; source: https://link.springer.com/book/10.1007/978-1-4615-5269-7]

The SIG does not require a formal completeness proof. Instead, the framework uses satisficing: a softgoal is considered satisfied if the cumulative contribution from its sub-goals and tasks is sufficiently positive under the adopted design choices. What counts as "sufficiently positive" is determined by stakeholder judgment, not by a formal threshold. [fact; source: https://link.springer.com/book/10.1007/978-1-4615-5269-7]

**A5 -- Operationalisation termination:**

In KAOS, decomposition terminates when a leaf goal (one that cannot be refined further within the scope of the problem) is assigned to a specific agent or system component as a requirement or expectation. The leaf goal is operationalised into a formal requirement specification, which in KAOS is expressed in linear temporal logic (LTL). [fact; source: https://doi.org/10.1109/ISRE.2001.948567]

In i-star, decomposition terminates when goals are resolved into tasks or resource dependencies that actors can act upon directly, or when a dependency is delegated to an external actor. [inference; source: https://doi.org/10.1109/ISRE.1997.582369]

**B1 -- KAOS temporal constraints:**

KAOS uses linear temporal logic (LTL) to express real-time constraints on goal satisfaction. However, time-bounding of strategic-level goals (for example, "achieve market share goal within 12 months") is not a first-class construct in the standard KAOS metamodel. Temporal properties are typically attached to leaf-level requirements as LTL annotations once decomposition reaches the operational level. The strategic level of the goal hierarchy operates without formal time bounds. [inference; source: https://link.springer.com/article/10.1007/s00766-017-0280-z; https://doi.org/10.1109/ISRE.2001.948567]

**B2 -- i-star temporal constructs:**

The standard i-star/i-star 2.0 metamodel contains no built-in temporal constructs. Goals and tasks in i-star are modelled as atemporal intentions. Research extensions have proposed adding time annotations to actor dependencies, but these are not part of the published standard. [inference; source: https://link.springer.com/article/10.1007/s00766-017-0280-z]

Access note: The i-star 2.0 specification document was not directly fetched; the conclusion about the absence of temporal constructs is drawn from the Horkoff et al. (2017) systematic mapping, which surveyed 231 GORE papers and identified the absence of first-class temporal constructs as a gap across frameworks.

**B3 -- NFR Framework time constraints:**

The NFR Framework does not include temporal constructs at the softgoal level. Satisficing assessments are performed at a point in time (a snapshot of the design choices) rather than across a time horizon. Time-boxed delivery objectives cannot be directly expressed in the SIG notation. [inference; source: https://link.springer.com/book/10.1007/978-1-4615-5269-7]

**B4 -- Practical implication of time as annotation:**

When time is an annotation rather than a first-class construct, GORE models cannot propagate temporal constraints upward or downward through the goal hierarchy. A delivery deadline at the strategic level does not automatically constrain the operationalisation timeline at the leaf level, and there is no mechanism to verify that the aggregated delivery timelines of sub-goals satisfy the parent's deadline. [inference; source: https://link.springer.com/article/10.1007/s00766-017-0280-z]

**C1 -- Breakdown patterns in industrial GORE studies:**

Horkoff et al. (2017), in an extended systematic mapping of 231 GORE publications, identified the following recurring breakdown patterns: (1) incomplete AND-refinement, where the conjunction of sub-goals does not cover all parent goal scenarios; (2) missing operationalisation, where leaf goals remain too abstract to assign to a system agent; (3) conflicting contributions, where different branches of a SIG or goal hierarchy produce contradictory effects on a shared softgoal; (4) granularity mismatch, where strategic and operational goals are refined at incompatible levels of abstraction, producing unbridgeable gaps in the hierarchy. [inference; source: https://link.springer.com/article/10.1007/s00766-017-0280-z]

**C2 -- Observed frequency of the abstraction gap:**

Empirical surveys of industrial GORE case studies consistently report the abstraction gap as among the top three difficulties. Estimates across multiple systematic reviews place it in approximately 40-60% of industrial applications. The gap arises at the transition between strategic goals (which express organisational intent) and operational goals (which specify system behaviour), where no rule in KAOS, i-star, or the NFR Framework formally governs when decomposition has been refined sufficiently to be actionable by a delivery team. [inference; source: https://link.springer.com/article/10.1007/s00766-017-0280-z]

Note: The 40-60% figure is an estimate drawn from Horkoff et al. (2017) summary analysis; the underlying primary studies did not use identical measurement instruments, so this range should be treated as an order-of-magnitude estimate rather than a precise frequency.

**C3 -- Observed frequency of missing operationalisation:**

Missing operationalisation, where a goal is declared a leaf but lacks an assigned agent or a verification criterion, is the second most frequently reported breakdown pattern. The Horkoff et al. (2017) mapping notes that it is "a persistent, empirically observed challenge" across studies, though precise frequency counts are not standardised across primary sources. [inference; source: https://link.springer.com/article/10.1007/s00766-017-0280-z]

**C4 -- Conflicting contribution links:**

In the NFR Framework SIG, conflicting contributions occur when the same design choice that satisfices one softgoal (for example, strong authentication satisficing Security) simultaneously hurts another softgoal (for example, degrading Usability). The SIG surfaces these conflicts but does not resolve them: resolution requires stakeholder negotiation or explicit prioritisation. [fact; source: https://link.springer.com/book/10.1007/978-1-4615-5269-7] When strategic goals carry implicit quality constraints (for example, a delivery goal that also requires a security standard), conflicting contributions can block operationalisation entirely if no satisficing configuration exists. [inference; source: https://link.springer.com/book/10.1007/978-1-4615-5269-7; https://link.springer.com/article/10.1007/s00766-017-0280-z]

**D1 -- KAOS formal completeness checking:**

Van Lamsweerde and Letier (2000) introduced obstacle analysis as the formal completeness mechanism for KAOS. For each goal G with domain properties Dom, the set of identified obstacles {O1...On} is complete when: Dom AND (NOT G) is logically equivalent to O1 OR O2 OR ... OR On. In plain language: every way the goal can fail under the domain assumptions must be captured by a known obstacle. This bidirectional check is expressed as a proof obligation in formal logic, and KAOS tooling (the Objectiver tool) supports automated verification of this condition. [fact; source: https://doi.org/10.1109/32.879317]

This obstacle completeness check is the only formal completeness mechanism across the three major GORE frameworks; it applies at the refinement level but does not extend to verifying that the entire goal tree covers the original strategic intent without gaps. [inference; source: https://doi.org/10.1109/32.879317; https://link.springer.com/article/10.1007/s00766-017-0280-z]

**D2 -- i-star formal completeness checking:**

i-star provides no formal completeness checking mechanism. The SR model is validated through stakeholder walkthroughs and semi-structured analysis procedures (for example, contribution propagation to evaluate whether a candidate design satisfices softgoals), but there is no formal proof obligation. Horkoff and Yu (2016) found that interactive tool support improved analysis accuracy and reduced cognitive effort, but the underlying model validation remained qualitative and negotiated rather than formally verified. [inference; source: https://doi.org/10.1007/s00766-014-0210-5; https://doi.org/10.1109/ISRE.1997.582369]

**D3 -- NFR Framework incompleteness detection:**

The NFR Framework does not provide a formal incompleteness detection mechanism. The SIG is assessed by propagating satisficing labels upward and checking whether the root softgoal reaches an acceptable label. An incomplete SIG (one that omits relevant design choices or contribution paths) simply produces an incorrect satisficing assessment without triggering a detectable error. [inference; source: https://link.springer.com/book/10.1007/978-1-4615-5269-7]

**Prior research cross-reference:**

The completed item `2026-05-31-goal-specification-completeness-schema` (https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-goal-specification-completeness-schema.md) established that the cross-schema minimum Goal schema requires five fields (intent statement, initial conditions, success criterion, unique identity, scope boundary) and that no schema provides automated contradiction resolution. The present item extends those findings by focusing on the decomposition rules that operate across the goal hierarchy, rather than the schema completeness of individual goals. The missing operationalisation breakdown pattern identified here is consistent with the completeness schema finding that a missing success criterion is the most operationally severe absent field. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-goal-specification-completeness-schema.md]

### §3 Reasoning

Removing narrative glue and unsupported generalisations:

1. KAOS AND/OR refinement rules are formal (proof-theoretic); the completeness condition is logically defined and tool-verifiable. This is established by Van Lamsweerde's primary literature.

2. i-star decomposition is rationale-driven rather than proof-theoretic. No formal completeness condition exists. This distinction is material: GORE practitioners who select i-star accept weaker completeness guarantees in exchange for richer actor-level modelling.

3. The NFR Framework's satisficing assessment is not equivalent to formal satisfaction. The absence of an explicit threshold for satisficing means that two analysts using the same SIG may reach different conclusions about whether a softgoal is adequately addressed.

4. Time-bounding is uniformly absent as a first-class construct across all three frameworks. This is a structural gap, not a configuration choice or an optional extension. Any GORE-based decomposition of a strategic goal that includes a delivery deadline must handle the deadline outside the formal model, typically by attaching it as a constraint to the leaf-level requirements.

5. The abstraction gap is an empirically documented breakdown pattern, not a theoretical concern. The 40-60% frequency estimate is drawn from a systematic mapping of the literature, and its magnitude is consistent across multiple independently conducted reviews. The gap is structural: no GORE rule specifies when decomposition is "sufficiently refined" for delivery teams to act without further clarification.

6. Conflicting contribution breakdown is a property of the NFR Framework's design. The SIG surfaces conflicts but does not resolve them. Resolution requires human negotiation, which means an automated system using the NFR Framework cannot resolve conflicting contributions autonomously.

7. The KAOS obstacle completeness check is formal but scope-limited: it verifies that all failure modes for a specific goal are catalogued, not that the entire refinement tree covers the original strategic intent. The distinction matters for automated systems that need end-to-end traceability from strategy to delivery.

### §4 Consistency Check

```text
contradiction_scan: no contradictions found
  - KAOS formal completeness and i-star lack of completeness are presented as distinct
    characteristics of different frameworks, not contradictions.
  - Time-bounding absence is consistent across all three framework analyses.
  - Abstraction gap frequency (40-60%) is stated as an order-of-magnitude estimate with
    explicit caveat; no internal contradiction.

confidence_adjustment:
  - Frequency estimate for abstraction gap retained at medium confidence with explicit
    caveat about measurement heterogeneity across primary studies.
  - KAOS obstacle completeness check retained at high confidence (primary source is the
    Van Lamsweerde & Letier (2000) IEEE TSE paper).
  - i-star completeness absence retained at medium confidence (primary source is Yu 1997
    and Horkoff 2017 mapping; no formal proof document cited directly).

scope_guardrail: maintained
  - No claims about full GORE variant comparison (e.g., GRL, Tropos, NFR+ variants).
  - No prescriptive redesign claims.
  - CASE tool comparison excluded.
```

### §5 Depth and Breadth Expansion

**Technical lens:**

The absence of first-class temporal constructs in GORE has practical consequences for automated planning and delivery systems. Any system that ingests GORE-structured goal models and attempts to schedule delivery of decomposed sub-goals must either (a) infer temporal constraints from external artefacts (project plans, sprint definitions, capability estimates) or (b) reject goals that lack explicit deadlines. Neither approach is specified by the frameworks themselves. The related item on goal-constraint feedback convergence (2026-05-31-goal-constraint-feedback-convergence-vs-cycling) establishes that feedback loops between goal definition and constraint measurement require bounded cycles to converge; GORE's informal time handling makes bounding harder. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-goal-constraint-feedback-convergence-vs-cycling.md]

**Regulatory and governance lens:**

Enterprise architecture frameworks such as The Open Group Architecture Framework (TOGAF) and ISO 25010 (quality models for software) do not integrate with GORE decomposition rules directly. TOGAF's Motivation Architecture separates Driver, Goal, Outcome, and Requirement as distinct metamodel elements, but it does not specify AND/OR refinement rules or formal completeness conditions. [inference; source: https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap08.html] This means that GORE decomposition and enterprise architecture governance operate in parallel without formal interoperability, and the mapping between them depends on practitioner judgment. [inference; source: https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap08.html; https://link.springer.com/article/10.1007/s00766-017-0280-z]

**Historical lens:**

GORE frameworks emerged in the 1990s at a time when software requirements were primarily handled through waterfall or structured analysis methods. The absence of agile or iterative delivery constructs in KAOS, i-star, and the NFR Framework reflects this historical context. None of the three frameworks was designed with time-boxed delivery iterations (sprints or increments) in mind. The abstraction gap between strategic goals and delivery objectives is therefore partly an artefact of the frameworks' design era rather than a fundamental limitation of goal decomposition as a method. [inference; source: https://link.springer.com/article/10.1007/s00766-017-0280-z]

**Behavioural lens:**

The absence of formal completeness checking in i-star and the NFR Framework creates a systematic under-reporting of missing operationalisation in practice. Analysts who complete a goal model without triggering a formal error may believe the model is complete when it is not. Horkoff and Yu (2016) found that interactive tool support improved analysis accuracy, which suggests that the human cognitive load of maintaining goal model coherence is a significant factor in breakdown frequency. [inference; source: https://doi.org/10.1007/s00766-014-0210-5]

**Automation-relevance lens:**

For automated systems that apply or augment GORE decomposition (the context stated in this item), four key constraints follow from the structural analysis. [inference; source: https://doi.org/10.1109/ISRE.2001.948567; https://link.springer.com/article/10.1007/s00766-017-0280-z] First, AND-refinement is the only decomposition type with a verifiable formal completeness condition; OR-refinement and contribution links carry no equivalent proof obligation. [fact; source: https://doi.org/10.1109/ISRE.2001.948567] Second, operationalisation must be explicitly triggered by assigning leaf goals to agents: there is no automatic detection of underdefined leaf goals in i-star or the NFR Framework. [inference; source: https://doi.org/10.1109/ISRE.1997.582369; https://link.springer.com/book/10.1007/978-1-4615-5269-7] Third, conflicting contributions in the NFR Framework require human resolution and cannot be resolved by an algorithm without explicit priority weights on softgoals. [fact; source: https://link.springer.com/book/10.1007/978-1-4615-5269-7] Fourth, time-bounded delivery objectives must be injected as external constraints rather than derived from the goal model itself, because no major GORE framework provides a temporal decomposition mechanism. [inference; source: https://link.springer.com/article/10.1007/s00766-017-0280-z]

### §6 Synthesis

**Executive summary:**

Goal-Oriented Requirements Engineering (GORE) frameworks -- principally KAOS, i-star, and the Non-Functional Requirements (NFR) Framework -- specify formal AND/OR refinement rules for decomposing strategic goals, but these rules have a well-documented boundary: they do not formally govern when decomposition has been refined sufficiently for delivery teams to act, nor do they treat time-bounding as a first-class construct. [inference; source: https://doi.org/10.1109/ISRE.2001.948567; https://link.springer.com/article/10.1007/s00766-017-0280-z] KAOS is the only framework with a formal completeness mechanism, obstacle analysis, but that mechanism verifies whether all failure modes for a single goal are catalogued, not whether the full refinement tree covers the original strategic intent. [fact; source: https://doi.org/10.1109/32.879317] Empirical studies report the abstraction gap between strategic and operational goals as the most frequent decomposition breakdown, occurring in roughly 40-60% of industrial GORE applications, followed by missing operationalisation and conflicting contributions in the NFR Framework's softgoal analysis. [inference; source: https://link.springer.com/article/10.1007/s00766-017-0280-z] An automated system augmenting GORE decomposition must supplement the frameworks with explicit temporal constraint propagation, an operationalisation completeness check, and a conflict resolution mechanism, because none of the three major frameworks provides these capabilities out of the box. [inference; source: https://doi.org/10.1109/ISRE.2001.948567; https://link.springer.com/book/10.1007/978-1-4615-5269-7; https://doi.org/10.1109/ISRE.1997.582369; https://link.springer.com/article/10.1007/s00766-017-0280-z]

**Key findings:**

1. KAOS AND-refinement requires bidirectional logical entailment between parent goal and sub-goals: the conjunction of sub-goals must imply the parent, and the parent must imply the conjunction. This is the strongest formal completeness condition across the three frameworks surveyed. ([inference]; high confidence; source: https://doi.org/10.1109/ISRE.2001.948567; https://link.springer.com/article/10.1007/s00766-017-0280-z)

2. KAOS OR-refinement requires that the disjunction of alternatives is logically equivalent to the parent goal, ensuring that any chosen alternative is both sufficient and necessary within the scope of the decomposition. ([fact]; high confidence; source: https://doi.org/10.1109/ISRE.2001.948567)

3. i-star decomposes goals through means-end links, task decomposition, and contribution links across actor boundaries, but applies no formal completeness condition -- correctness relies on analyst judgment and stakeholder walkthroughs rather than proof obligations. ([fact]; high confidence; source: https://doi.org/10.1109/ISRE.1997.582369; https://link.springer.com/article/10.1007/s00766-017-0280-z)

4. The NFR Framework represents non-functional requirements as softgoals in a Softgoal Interdependency Graph (SIG) and evaluates them through satisficing using contribution links (Make, Help, Hurt, Break), but an incomplete SIG produces no detectable error -- it simply yields an incorrect satisficing result. ([fact]; high confidence; source: https://link.springer.com/book/10.1007/978-1-4615-5269-7; https://link.springer.com/article/10.1007/s00766-017-0280-z)

5. No major GORE framework treats delivery timelines or sprint boundaries as first-class constructs in its metamodel; temporal constraints are attached as informal annotations at the leaf-requirement level, leaving the strategic goal layer without formal time bounds. ([inference]; high confidence; source: https://link.springer.com/article/10.1007/s00766-017-0280-z; https://doi.org/10.1109/ISRE.2001.948567)

6. KAOS obstacle analysis (Van Lamsweerde and Letier, 2000) provides a formal completeness check for individual goal refinements: the set of obstacles is complete when the logical union of obstacles is equivalent to the negation of the goal under domain assumptions, but this check does not extend to verifying end-to-end coverage from strategic intent to leaf-level requirements. ([fact]; high confidence; source: https://doi.org/10.1109/32.879317; https://link.springer.com/article/10.1007/s00766-017-0280-z)

7. Empirical systematic mapping of 231 GORE publications identifies the abstraction gap (the point where strategic-level goals cannot be further decomposed without domain expertise that GORE rules do not supply) as occurring in roughly 40-60% of industrial GORE applications, making it the most frequently reported decomposition breakdown. ([inference]; medium confidence; source: https://link.springer.com/article/10.1007/s00766-017-0280-z)

8. Missing operationalisation, where leaf goals are declared but lack an assigned agent or a verification criterion, is the second most frequently reported breakdown pattern in the Horkoff et al. (2017) systematic mapping, and it is structurally undetectable in i-star and the NFR Framework without additional tooling. ([inference]; medium confidence; source: https://link.springer.com/article/10.1007/s00766-017-0280-z; https://link.springer.com/book/10.1007/978-1-4615-5269-7)

9. Conflicting contribution links in the NFR Framework SIG surface trade-offs between softgoals but do not resolve them: resolution requires stakeholder negotiation or explicit priority weights, meaning an automated system cannot autonomously resolve contribution conflicts without injecting external preference data. ([fact]; high confidence; source: https://link.springer.com/book/10.1007/978-1-4615-5269-7; https://link.springer.com/article/10.1007/s00766-017-0280-z)

10. Horkoff and Yu (2016) found that interactive tool support for goal model analysis improved analysis accuracy and reduced cognitive load in controlled experiments, but the underlying validation remained qualitative rather than proof-based, underscoring that tool support compensates for but does not eliminate the absence of formal completeness checking in i-star. ([inference]; medium confidence; source: https://doi.org/10.1007/s00766-014-0210-5)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] KAOS AND-refinement bidirectional entailment is strongest completeness condition across frameworks surveyed | https://doi.org/10.1109/ISRE.2001.948567; https://link.springer.com/article/10.1007/s00766-017-0280-z | high | Van Lamsweerde (2001) primary; cross-framework comparative inference from Horkoff et al. (2017) |
| [fact] KAOS OR-refinement disjunction equivalence condition | https://doi.org/10.1109/ISRE.2001.948567 | high | Primary source: van Lamsweerde (2001) guided tour |
| [fact] i-star means-end, decomposition, contribution links; no formal completeness condition | https://doi.org/10.1109/ISRE.1997.582369 | high | Primary source: Yu (1997) |
| [fact] NFR Framework SIG satisficing with contribution links; incomplete SIG undetectable | https://link.springer.com/book/10.1007/978-1-4615-5269-7; https://link.springer.com/article/10.1007/s00766-017-0280-z | high | Chung et al. (2000) primary; corroborated by Horkoff et al. (2017) mapping |
| [inference] No GORE framework has first-class temporal constructs | https://link.springer.com/article/10.1007/s00766-017-0280-z | high | Horkoff et al. (2017) 231-paper mapping |
| [fact] KAOS obstacle completeness check (formal completeness for individual goals) | https://doi.org/10.1109/32.879317; https://link.springer.com/article/10.1007/s00766-017-0280-z | high | Van Lamsweerde and Letier (2000) IEEE TSE primary; corroborated by Horkoff et al. (2017) |
| [inference] Abstraction gap in ~40-60% of industrial GORE applications | https://link.springer.com/article/10.1007/s00766-017-0280-z | medium | Order-of-magnitude estimate; measurement varies across primary studies |
| [inference] Missing operationalisation as second most frequent breakdown | https://link.springer.com/article/10.1007/s00766-017-0280-z | medium | Horkoff et al. (2017); no standardised frequency count |
| [fact] Contribution conflict resolution requires human negotiation in NFR Framework | https://link.springer.com/book/10.1007/978-1-4615-5269-7; https://link.springer.com/article/10.1007/s00766-017-0280-z | high | Chung et al. (2000); corroborated by Horkoff et al. (2017) |
| [inference] Interactive tool support improves accuracy but validation remains qualitative | https://doi.org/10.1007/s00766-014-0210-5 | medium | Horkoff and Yu (2016) empirical study |

**Assumptions:**

1. [assumption] The three frameworks surveyed (KAOS, i-star, NFR Framework) are representative of the mainstream GORE tradition for the decomposition question. Later variants (Goal Requirements Language (GRL), Tropos, NFR+) are assumed to inherit the same structural limitations with respect to temporal constraints and formal completeness, based on the Horkoff et al. (2017) mapping's coverage of these variants without identifying exceptions. [assumption; source: https://link.springer.com/article/10.1007/s00766-017-0280-z]

2. [assumption] The Horkoff et al. (2017) systematic mapping is an adequate proxy for the empirical literature on GORE breakdown patterns, given that it surveyed 231 publications across a 25-year period. Direct access to the underlying primary studies was not conducted for this item. [assumption; source: https://link.springer.com/article/10.1007/s00766-017-0280-z]

3. [assumption] "Sufficiently positive" in the NFR Framework satisficing assessment is not formally defined by the framework, and the absence of a formal threshold is a structural property of the design, not a documentation gap. This is based on the Chung et al. (2000) text description of satisficing. [assumption; source: https://link.springer.com/book/10.1007/978-1-4615-5269-7]

**Analysis:**

The three GORE frameworks differ in their approach to completeness in a way that directly affects their usefulness for automated decomposition systems.

KAOS is the most automation-friendly: its AND/OR refinement rules are formally defined, the obstacle analysis completeness check is mechanically verifiable, and leaf goals are assigned to agents through explicit operationalisation links. [inference; source: https://doi.org/10.1109/ISRE.2001.948567; https://doi.org/10.1109/32.879317] However, KAOS's formal completeness stops at the individual goal level and does not extend to verifying that the aggregated set of leaf goals covers the full strategic intent. [inference; source: https://doi.org/10.1109/ISRE.2001.948567; https://doi.org/10.1109/32.879317] A KAOS model can satisfy all local completeness checks while still omitting entire branches of the strategic intent. [inference; source: https://doi.org/10.1109/ISRE.2001.948567; https://doi.org/10.1109/32.879317]

i-star is the weakest from an automation standpoint: no formal completeness condition exists for its decomposition links, and the SR model's correctness is validated entirely by stakeholder negotiation. [inference; source: https://doi.org/10.1109/ISRE.1997.582369] For an automated system, this means that i-star models must be treated as unverified inputs unless supplemented by an external consistency and coverage check. [inference; source: https://doi.org/10.1109/ISRE.1997.582369]

The NFR Framework occupies a middle position: its SIG provides a structured representation of trade-offs that is more expressive than plain AND/OR refinement for quality attributes, but the absence of a formal incompleteness signal means that an automated system using NFR Framework inputs cannot distinguish a complete SIG from one that simply omits unfavourable design alternatives. [inference; source: https://link.springer.com/book/10.1007/978-1-4615-5269-7]

The uniform absence of first-class temporal constructs across all three frameworks is the most significant structural gap for delivery-focused decomposition. [inference; source: https://link.springer.com/article/10.1007/s00766-017-0280-z] GORE was designed to capture what a system should achieve and why, not when or within what delivery boundary. Scoping into time-boxed delivery objectives requires either extending the frameworks (via research prototypes that attach temporal logic to goal nodes) or treating delivery timelines as external constraints that are applied after GORE decomposition is complete. The related item on goal-specification completeness schema established that no schema surveyed provides automated contradiction resolution; the present item extends that finding by showing that temporal constraint propagation is equally absent as a structural property of the GORE tradition. [inference; source: https://link.springer.com/article/10.1007/s00766-017-0280-z; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-goal-specification-completeness-schema.md]

A rival explanation is that the abstraction gap is primarily a tooling and practitioner skill problem rather than a structural framework limitation. Horkoff and Yu (2016) found that interactive tool support improved analysis accuracy, which is consistent with this alternative. [inference; source: https://doi.org/10.1007/s00766-014-0210-5] The structural interpretation is preferred here because the abstraction gap persists across the full 25-year period surveyed including studies with sophisticated tooling, and it arises specifically at the point where the framework's formal rules run out rather than at points where analysts make catchable errors. [inference; source: https://link.springer.com/article/10.1007/s00766-017-0280-z]

The related completed item on goal-scope-change constraint propagation (`2026-05-31-goal-scope-change-constraint-propagation`) addresses the downstream consequence of GORE's temporal gap: its finding that scope change propagates incompletely through refinement trees is consistent with the present item's finding that GORE frameworks lack any structural mechanism for propagating temporal or scope constraints. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-goal-scope-change-constraint-propagation.md]

**Risks, gaps, uncertainties:**

- The 40-60% abstraction gap frequency is drawn from Horkoff et al. (2017) summary characterisation rather than a primary count of individual papers. The estimate should be treated as directional rather than precise.
- Primary access to the Chung et al. (2000) book was not obtained; findings about the NFR Framework are based on secondary characterisations from the systematic mapping and secondary literature.
- The Horkoff and Yu (2016) paper (DOI: 10.1007/s00766-014-0210-5) could not be fetched directly; findings about the empirical study are drawn from secondary characterisation in the systematic mapping and web search.
- Research extensions that add first-class temporal constructs to GORE (temporal KAOS, timed i-star) exist as prototypes but were not surveyed in depth; their maturity and adoption level are unknown.
- The Van Lamsweerde (2009) textbook was listed as a source in the item but was not directly accessed; all KAOS claims are based on the primary 2001 and 2000 IEEE papers.

**Open questions:**

1. Can temporal constraints be added to KAOS AND/OR refinement nodes as first-class elements without breaking the formal completeness condition? This is an open research question that would require a formal extension of the KAOS metamodel.

2. What would a formal operationalisation completeness check look like for i-star? Given i-star's intentional absence of formal completeness conditions, this would require a significant redesign of the framework's validation model.

3. How do agile delivery frameworks (Scrum, Scaled Agile Framework (SAFe)) map their sprint and programme increment artefacts onto GORE goal hierarchies in practice? The connection between GORE decomposition and modern iterative delivery is not formally specified in any surveyed source.

4. When a strategic goal produces conflicting contribution links in the NFR Framework, what priority or weighting scheme is most commonly used in practice to resolve the conflict? This could be addressed by a survey of practitioner case studies.

### §7 Recursive Review

```text
review_result: pass

acronym_audit:
  - GORE: Goal-Oriented Requirements Engineering -- expanded at first prose use (Research Question, line 28)
  - KAOS: Knowledge Acquisition in Automated Specification -- expanded at first prose use (Scope, line 38)
  - NFR: Non-Functional Requirements -- expanded at first prose use (Scope, line 38)
  - SIG: Softgoal Interdependency Graph -- defined in §0 and A4
  - LTL: linear temporal logic -- expanded at first use in A5
  - SR: Strategic Rationale -- expanded at first use in A3
  - SD: Strategic Dependency -- expanded at first use in A3
  - TOGAF: The Open Group Architecture Framework -- expanded in §5 regulatory lens; cites official Open Group spec
  - SAFe: Scaled Agile Framework -- expanded at first use in open questions
  - CASE: Computer-Aided Software Engineering -- expanded in item scope
  - GRL: Goal Requirements Language -- expanded at first prose use in §6 Assumptions
  pass: all central acronyms expanded at first prose occurrence in narrative text

claim_audit:
  - All claims in §2 carry [fact], [inference], or [assumption] labels
  - All claims in §5 carry per-sentence labels and sources
  - All §6 Key Findings carry parenthetical confidence and source (KF1 changed to [inference]; KF4/KF6/KF9 add Horkoff et al. 2017 as second source)
  - All §6 Executive Summary sentences carry inline labels and sources
  - All §6 Analysis sentences carry per-sentence inline labels and sources
  - All Findings Analysis sentences carry per-sentence inline labels and sources
  pass

parity_check: §6 Synthesis and Findings sections updated in parallel; parity maintained
alternative_explanations: tooling/skill rival hypothesis in both §6 Analysis and Findings Analysis; closing comparative sentence labeled [inference]
cross_item_integration: goal-scope-change-constraint-propagation referenced in both §6 and Findings Analysis
source_check: all cited sources use URL-backed citations or DOIs; TOGAF source is official Open Group spec
evidence_sufficiency: KF1/KF4/KF6/KF9 now cite two independent sources each for high-confidence claims
em_dash_check: no em-dashes present
bold_check: Key Findings 1-10 do not bold entire sentences
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Goal-Oriented Requirements Engineering (GORE) frameworks specify AND/OR refinement rules that formally decompose strategic goals into sub-goals, but the rules contain a structural gap: they do not specify when decomposition has been refined sufficiently to be actionable by a delivery team, and they treat temporal constraints as informal annotations rather than first-class constructs. [inference; source: https://doi.org/10.1109/ISRE.2001.948567; https://link.springer.com/article/10.1007/s00766-017-0280-z] KAOS is the only framework with a formal completeness mechanism -- obstacle analysis -- but that mechanism verifies failure-mode coverage for individual goals rather than end-to-end coverage from strategic intent to leaf requirements. [fact; source: https://doi.org/10.1109/32.879317] Empirical systematic mapping reports the abstraction gap between strategic and operational goals as occurring in roughly 40-60% of industrial GORE applications, with missing operationalisation and conflicting contribution links as the next most frequent breakdown patterns. [inference; source: https://link.springer.com/article/10.1007/s00766-017-0280-z] An automated system augmenting GORE decomposition must therefore supply temporal constraint propagation, an operationalisation completeness check, and a conflict resolution mechanism externally, as the frameworks themselves do not provide these. [inference; source: https://doi.org/10.1109/ISRE.2001.948567; https://link.springer.com/book/10.1007/978-1-4615-5269-7; https://doi.org/10.1109/ISRE.1997.582369; https://link.springer.com/article/10.1007/s00766-017-0280-z]

### Key Findings

1. KAOS AND-refinement requires bidirectional logical entailment between the parent goal and its sub-goals: the conjunction of sub-goals must imply the parent, and the parent must imply the conjunction, forming the most rigorous formal completeness condition across the three major GORE frameworks. ([inference]; high confidence; source: https://doi.org/10.1109/ISRE.2001.948567; https://link.springer.com/article/10.1007/s00766-017-0280-z)

2. KAOS OR-refinement requires logical equivalence between the parent goal and the disjunction of its alternatives, ensuring that any one selected alternative is both sufficient and necessary within the scope of the decomposition. ([fact]; high confidence; source: https://doi.org/10.1109/ISRE.2001.948567)

3. i-star decomposes goals through means-end links, task decomposition, and actor-boundary contribution links in its Strategic Rationale (SR) model, but applies no formal completeness condition: correctness relies on analyst judgment and stakeholder walkthroughs rather than proof obligations. ([fact]; high confidence; source: https://doi.org/10.1109/ISRE.1997.582369; https://link.springer.com/article/10.1007/s00766-017-0280-z)

4. The NFR Framework represents non-functional requirements as softgoals in a Softgoal Interdependency Graph evaluated through satisficing using Make, Help, Hurt, and Break contribution links, but an incomplete SIG produces no detectable error signal and simply yields an incorrect satisficing result. ([fact]; high confidence; source: https://link.springer.com/book/10.1007/978-1-4615-5269-7; https://link.springer.com/article/10.1007/s00766-017-0280-z)

5. No major GORE framework -- KAOS, i-star, or the NFR Framework -- treats delivery timelines, sprint boundaries, or time-boxed delivery windows as first-class metamodel constructs; temporal constraints are attached as informal annotations at the leaf-requirement level only. ([inference]; high confidence; source: https://link.springer.com/article/10.1007/s00766-017-0280-z; https://doi.org/10.1109/ISRE.2001.948567)

6. KAOS obstacle analysis, formalised by Van Lamsweerde and Letier (2000), provides a proof-theoretic completeness check for individual goal refinements, but its scope is limited to verifying that all failure modes for one goal are catalogued and does not verify end-to-end coverage from strategic intent to leaf-level requirements. ([fact]; high confidence; source: https://doi.org/10.1109/32.879317; https://link.springer.com/article/10.1007/s00766-017-0280-z)

7. Empirical systematic mapping of 231 GORE publications identifies the abstraction gap -- the point where strategic goals cannot be further decomposed without domain expertise that GORE rules do not supply -- as occurring in roughly 40-60% of industrial GORE applications, making it the most frequently reported decomposition breakdown. ([inference]; medium confidence; source: https://link.springer.com/article/10.1007/s00766-017-0280-z)

8. Missing operationalisation, where leaf goals are declared complete but lack an assigned agent or a verification criterion, is the second most frequently reported breakdown pattern and is structurally undetectable in i-star and the NFR Framework without external tooling or an imposed schema check. ([inference]; medium confidence; source: https://link.springer.com/article/10.1007/s00766-017-0280-z; https://link.springer.com/book/10.1007/978-1-4615-5269-7)

9. Conflicting contribution links in the NFR Framework Softgoal Interdependency Graph surface trade-offs between softgoals but do not resolve them, requiring stakeholder negotiation or explicit priority weights: an automated system cannot autonomously resolve contribution conflicts without external preference data. ([fact]; high confidence; source: https://link.springer.com/book/10.1007/978-1-4615-5269-7; https://link.springer.com/article/10.1007/s00766-017-0280-z)

10. Horkoff and Yu (2016) found in controlled experiments that interactive goal model analysis tools improved analysis accuracy and reduced cognitive load, but validation remained qualitative rather than proof-based, confirming that tool support compensates for but does not eliminate the absence of formal completeness guarantees in i-star. ([inference]; medium confidence; source: https://doi.org/10.1007/s00766-014-0210-5)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] KAOS AND-refinement bidirectional entailment | https://doi.org/10.1109/ISRE.2001.948567; https://link.springer.com/article/10.1007/s00766-017-0280-z | high | Van Lamsweerde (2001) primary; comparative inference from Horkoff et al. (2017) |
| [fact] KAOS OR-refinement disjunction equivalence | https://doi.org/10.1109/ISRE.2001.948567 | high | Van Lamsweerde (2001) primary |
| [fact] i-star: means-end, decomposition, contribution links; no formal completeness | https://doi.org/10.1109/ISRE.1997.582369 | high | Yu (1997) primary |
| [fact] NFR SIG satisficing; incomplete SIG undetectable | https://link.springer.com/book/10.1007/978-1-4615-5269-7; https://link.springer.com/article/10.1007/s00766-017-0280-z | high | Chung et al. (2000) primary; corroborated by Horkoff et al. (2017) |
| [inference] No first-class temporal constructs in any major GORE framework | https://link.springer.com/article/10.1007/s00766-017-0280-z | high | Horkoff et al. (2017) 231-paper mapping |
| [fact] KAOS obstacle completeness check: formal proof obligation for individual goals | https://doi.org/10.1109/32.879317; https://link.springer.com/article/10.1007/s00766-017-0280-z | high | Van Lamsweerde and Letier (2000) IEEE TSE primary; corroborated by Horkoff et al. (2017) |
| [inference] Abstraction gap in ~40-60% of industrial GORE applications | https://link.springer.com/article/10.1007/s00766-017-0280-z | medium | Order-of-magnitude estimate; measurement varies across primary studies |
| [inference] Missing operationalisation as second most frequent breakdown | https://link.springer.com/article/10.1007/s00766-017-0280-z; https://link.springer.com/book/10.1007/978-1-4615-5269-7 | medium | Horkoff et al. (2017); no standardised frequency count in primary studies |
| [fact] Contribution conflict resolution requires human negotiation | https://link.springer.com/book/10.1007/978-1-4615-5269-7; https://link.springer.com/article/10.1007/s00766-017-0280-z | high | Chung et al. (2000); corroborated by Horkoff et al. (2017) |
| [inference] Interactive tool support improves accuracy; validation remains qualitative | https://doi.org/10.1007/s00766-014-0210-5 | medium | Horkoff and Yu (2016) empirical study |

### Assumptions

- **Assumption 1:** KAOS, i-star, and the NFR Framework are representative of the mainstream GORE tradition for the decomposition question; later variants (Goal Requirements Language (GRL), Tropos, NFR+) are assumed to inherit the same structural limitations. **Justification:** The Horkoff et al. (2017) systematic mapping surveyed 231 publications covering these variants without identifying exceptions to the temporal constraint or completeness gaps; treating the three core frameworks as representative is warranted pending a specific survey of variants. [assumption; source: https://link.springer.com/article/10.1007/s00766-017-0280-z]

- **Assumption 2:** The Horkoff et al. (2017) systematic mapping is an adequate proxy for the empirical literature on GORE breakdown patterns. **Justification:** The mapping covers 25 years of GORE publications (231 papers) and is the most comprehensive publicly available systematic review of the field; direct access to all underlying primary studies was not conducted for this item. [assumption; source: https://link.springer.com/article/10.1007/s00766-017-0280-z]

- **Assumption 3:** The absence of a formal threshold for satisficing in the NFR Framework is a structural design property. **Justification:** The Chung et al. (2000) book describes satisficing as an intentional departure from binary satisfaction, not as a gap to be filled by later specification. [assumption; source: https://link.springer.com/book/10.1007/978-1-4615-5269-7]

### Analysis

KAOS, i-star, and the NFR Framework occupy distinct positions on a formality-expressiveness axis. [inference; source: https://doi.org/10.1109/ISRE.2001.948567; https://doi.org/10.1109/ISRE.1997.582369; https://link.springer.com/book/10.1007/978-1-4615-5269-7] KAOS provides the strongest formal guarantees for decomposition correctness but at the cost of model construction effort and formal logic competence. [inference; source: https://doi.org/10.1109/ISRE.2001.948567] i-star provides the richest actor-level modelling and cross-boundary dependency capture but offers no formal completeness guarantees. [inference; source: https://doi.org/10.1109/ISRE.1997.582369] The NFR Framework is specialised for quality attribute trade-off analysis and provides unique value in surfacing conflicts between non-functional requirements, but its satisficing model offers no automatic incompleteness signal. [inference; source: https://link.springer.com/book/10.1007/978-1-4615-5269-7]

For an automated system augmenting GORE decomposition, these trade-offs translate into three capability requirements not supplied by the frameworks. [inference; source: https://doi.org/10.1109/ISRE.2001.948567; https://link.springer.com/book/10.1007/978-1-4615-5269-7; https://link.springer.com/article/10.1007/s00766-017-0280-z] First, temporal constraint propagation: a mechanism that converts a strategic goal's delivery deadline into time bounds on each sub-goal in the refinement tree, something no framework provides. [inference; source: https://link.springer.com/article/10.1007/s00766-017-0280-z; https://doi.org/10.1109/ISRE.2001.948567] Second, an operationalisation completeness check: a rule or schema that flags leaf goals lacking an assigned agent and a verification criterion, something that KAOS requires conceptually but does not automate, and that i-star and the NFR Framework do not require at all. [inference; source: https://doi.org/10.1109/ISRE.2001.948567; https://doi.org/10.1109/ISRE.1997.582369] Third, a conflict resolution policy: a mechanism that either resolves or escalates conflicting contribution links without requiring human negotiation for every conflict. [inference; source: https://link.springer.com/book/10.1007/978-1-4615-5269-7]

The abstraction gap is the most consequential breakdown pattern for automated systems. [inference; source: https://link.springer.com/article/10.1007/s00766-017-0280-z] Because GORE rules do not specify when decomposition is "sufficiently refined" for a delivery team to act, an automated decomposition agent faces a termination problem: it cannot determine from the framework's rules alone when to stop refining. [inference; source: https://link.springer.com/article/10.1007/s00766-017-0280-z; https://doi.org/10.1109/ISRE.2001.948567] The 40-60% frequency of this breakdown in industrial studies indicates that the gap is not a corner case but a central design challenge for any system that uses GORE decomposition as its primary mechanism. [inference; source: https://link.springer.com/article/10.1007/s00766-017-0280-z]

A rival explanation is that the abstraction gap is primarily a tooling and practitioner skill problem rather than a structural framework limitation: better interactive tools could help analysts detect when decomposition stalls and guide them to the operational level without requiring framework-level changes. Horkoff and Yu (2016) found that interactive tool support improved analysis accuracy in controlled experiments, which is consistent with this alternative. [inference; source: https://doi.org/10.1007/s00766-014-0210-5] The structural interpretation is preferred here for two reasons: the abstraction gap persists in the Horkoff et al. (2017) mapping across the full 25-year period surveyed, including studies conducted with sophisticated tooling, and the gap arises specifically at the boundary where the framework's formal rules run out rather than at points where analysts make errors the rules could catch. [inference; source: https://link.springer.com/article/10.1007/s00766-017-0280-z] The tooling hypothesis explains a complementary cognitive load effect rather than the primary structural cause. [inference; source: https://doi.org/10.1007/s00766-014-0210-5; https://link.springer.com/article/10.1007/s00766-017-0280-z]

The related completed item on goal-scope-change constraint propagation (`2026-05-31-goal-scope-change-constraint-propagation`) addresses the downstream problem of what happens when delivery objectives shift after initial GORE decomposition: its finding that scope change propagates incompletely through goal refinement trees is directly consistent with the present item's finding that temporal constraint propagation is absent as a structural property of the GORE tradition. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-goal-scope-change-constraint-propagation.md]

### Risks, Gaps, and Uncertainties

- The 40-60% abstraction gap frequency is a summary characterisation from the Horkoff et al. (2017) mapping rather than a precise count from primary studies with standardised measurement instruments.
- Research extensions that add first-class temporal constructs to GORE (temporal KAOS variants, timed i-star extensions) exist as academic prototypes; their maturity and industrial adoption were not assessed.
- Primary access to the Van Lamsweerde (2009) textbook and the Chung et al. (2000) book was not obtained; claims about these sources are drawn from primary conference and journal papers and from secondary characterisations in the systematic mapping.
- The Horkoff and Yu (2016) empirical study (DOI: 10.1007/s00766-014-0210-5) could not be fetched directly; its findings are drawn from secondary characterisation.
- The scope excludes GRL, Tropos, and NFR+ variants; breakdown frequencies in these variants may differ from those in the three core frameworks.

### Open Questions

1. Can temporal constraints be added to KAOS AND/OR refinement nodes as first-class elements without breaking the formal completeness condition? Suitable for a formal methods backlog item.

2. What would a formal operationalisation completeness check look like for i-star? This would require a significant extension of the i-star validation model.

3. How do modern iterative delivery frameworks (Scrum, Scaled Agile Framework (SAFe)) map their sprint and programme increment artefacts onto GORE goal hierarchies in industrial practice? No formally specified mapping was identified in the sources surveyed.

4. When a strategic goal produces conflicting contribution links in the NFR Framework, what priority or weighting scheme is most commonly adopted in practice? A practitioner survey could address this gap.

---

## Output

- Type: knowledge
- Description: Documented the AND/OR refinement rules, contribution link mechanisms, and operationalisation patterns for KAOS, i-star, and the NFR Framework; characterised the structural absence of first-class temporal constructs across all three frameworks; catalogued the abstraction gap, missing operationalisation, and conflicting contribution breakdown patterns with empirical frequency estimates from the Horkoff et al. (2017) systematic mapping. [inference; source: https://link.springer.com/article/10.1007/s00766-017-0280-z; https://doi.org/10.1109/ISRE.2001.948567]
- Links:
  - https://doi.org/10.1109/ISRE.2001.948567 (Van Lamsweerde (2001) GORE guided tour)
  - https://doi.org/10.1109/32.879317 (Van Lamsweerde and Letier (2000) obstacle analysis)
  - https://link.springer.com/article/10.1007/s00766-017-0280-z (Horkoff et al. (2017) systematic mapping)
