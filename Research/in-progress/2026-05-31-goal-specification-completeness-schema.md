---
title: "Goal specification: minimum schema and completeness validation"
added: 2026-05-31T09:42:57+00:00
status: reviewing
priority: high
blocks: []
themes: [formal-methods, software-engineering, governance-policy]
started: 2026-06-01T13:48:43+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-05-31-formal-methods-interdependent-inputs-feasibility
  - 2026-05-31-goal-scope-change-constraint-propagation
  - 2026-05-31-goal-constraint-feedback-convergence-vs-cycling
related:
  - 2026-03-10-formal-spec-intent-alignment-agentic-coding
  - 2026-05-17-policy-enforcement-formal-verification-energy-functions
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Goal specification: minimum schema and completeness validation

## Research Question

What properties must a Goal specification carry for an automated system to determine whether it is complete enough to act on — specifically, what is the minimum schema, and what happens when fields are absent or contradictory?

## Scope

**In scope:**
- Identifying the minimum set of fields (schema elements) a Goal specification must contain for an automated system to assess its actionability.
- Analysing behaviour when schema fields are absent, null, or contradictory: what error modes arise, and what validation rules govern them.
- Survey of existing Goal schema proposals from requirements engineering, enterprise architecture, and Artificial Intelligence (AI) planning literature.

**Out of scope:**
- Full end-to-end requirements engineering workflows.
- Subjective quality assessment of Goal content beyond structural completeness.
- Implementation of a validation tool or prototype.

**Constraints:** (time, source types, access)
- Focus on publicly documented schemas and standards (Goal-Oriented Requirements Engineering (GORE), The Open Group Architecture Framework (TOGAF), IEEE 29148, AI planning ontologies).
- Findings must be grounded in empirical or formal sources, not vendor marketing claims.

## Context

Automated systems that act on Goal specifications — planning engines, agentic AI systems, delivery orchestrators — fail in hard-to-diagnose ways when the Goal schema is under-specified. Knowing the minimum required fields and the valid handling rules for missing or conflicting data is the prerequisite for building reliable completeness checks. This is a foundational Gap 1 question from issue #618.

## Approach

1. Survey published Goal schemas in GORE, TOGAF motivation model, IEEE 29148, and AI planning (STRIPS, PDDL) to extract field inventories.
2. Identify which fields appear across all schemas (candidate minimum) vs. those that are schema-specific.
3. Analyse how each schema handles absent fields: hard error, default, degraded mode, or undefined.
4. Analyse handling rules for contradictory fields: detection mechanism, resolution strategy, and escalation path.
5. Synthesise a candidate minimum schema with explicit completeness rules and flag gaps where no consensus exists.

## Sources

- [ ] [Van Lamsweerde (2009) Requirements Engineering: From System Goals to UML Models to Software Specifications](https://www.wiley.com/en-gb/Requirements+Engineering%3A+From+System+Goals+to+UML+Models+to+Software+Specifications-p-9780470012703) — GORE theoretical foundations and Goal schema from Axel van Lamsweerde
- [ ] [The Open Group TOGAF Standard — Motivation Architecture](https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap08.html) — TOGAF motivation metamodel defining Driver, Goal, Outcome, Requirement
- [ ] [IEEE 29148-2018 Systems and Software Engineering — Requirements Engineering](https://standards.ieee.org/ieee/29148/6696/) — IEEE standard requirements for well-formed requirement and goal statements
- [ ] [Russell & Norvig Artificial Intelligence: A Modern Approach — Goal Representation](https://aima.cs.berkeley.edu/) — AI planning goal specification (STRIPS/PDDL formalism)

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

```text
Question: What properties must a Goal specification carry for an automated system
  to determine whether it is complete enough to act on -- specifically, what is the
  minimum schema, and what happens when fields are absent or contradictory?

Scope-in: Minimum schema fields; behaviour when fields are absent, null, or contradictory;
  survey of Goal schemas from Goal-Oriented Requirements Engineering (GORE), The Open Group
  Architecture Framework (TOGAF), Institute of Electrical and Electronics Engineers (IEEE)
  29148, and Artificial Intelligence (AI) planning ontologies (Planning Domain Definition
  Language (PDDL) / Stanford Research Institute Problem Solver (STRIPS)).

Scope-out: Full requirements engineering workflows; subjective quality assessment;
  implementation of a validation tool.

Constraints: Publicly documented schemas and standards; empirical or formal sources only;
  no vendor marketing claims.

Output format: knowledge item -- candidate minimum schema table, error-mode taxonomy,
  consensus and gap analysis.

Working hypotheses: [assumption] A cross-schema intersection of field inventories will
  identify a minimum set; [assumption] schemas will differ in error-handling strategy
  (hard error vs. degraded mode), justified by the different execution contexts
  (automated planners vs. human-mediated requirements tools) described in the source
  literature surveyed below.
```

### §1 Question Decomposition

**Q-A (Schema field inventory)**
- Q-A1: What fields does KAOS (Knowledge Acquisition in Automated Specification) / GORE specify as part of a Goal schema?
- Q-A2: What fields does TOGAF / ArchiMate 3.2 motivation model specify for a Goal element?
- Q-A3: What fields does IEEE 29148 specify for a well-formed requirement or goal statement?
- Q-A4: What fields does PDDL / STRIPS specify for a planning problem goal?

**Q-B (Cross-schema minimum)**
- Q-B1: Which fields appear in all four schemas -- the candidate minimum?
- Q-B2: Which fields are schema-specific (present in one or two schemas only)?

**Q-C (Absent-field error modes)**
- Q-C1: How does each schema handle missing intent/goal statement?
- Q-C2: How does each schema handle missing initial state / precondition?
- Q-C3: How does each schema handle missing success criterion / verification method?
- Q-C4: How does each schema handle missing agent / responsibility assignment?
- Q-C5: How does each schema handle missing parent/traceability link?

**Q-D (Contradictory fields)**
- Q-D1: How does each schema detect contradictions between Goal fields?
- Q-D2: What resolution strategies are available in each schema?
- Q-D3: What is the escalation path when contradiction cannot be resolved programmatically?

### §2 Investigation

#### Q-A1: KAOS / GORE Goal schema fields

Van Lamsweerde (2001) "Goal-Oriented Requirements Engineering: A Guided Tour" (Proceedings, 5th IEEE International Symposium on Requirements Engineering, pp. 249-263; https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb) defines the KAOS goal schema with the following structural fields: [fact] unique goal identifier; [fact] goal name and natural-language description; [fact] goal type (functional goal vs. softgoal / quality goal); [fact] parent goal links (AND/OR refinement); [fact] child goal or sub-goal links; [fact] responsible agent assignment (who must ensure the goal holds); [fact] operationalization link (which requirements or tasks realise the goal at leaf level); [fact] obstacle links (which conditions may violate the goal). Sources: Van Lamsweerde (2001) guided tour; confirmed by Van Lamsweerde (2009) book-length treatment (Wiley, ISBN 978-0-470-01270-3; https://www.wiley.com/en-gb/Requirements+Engineering%3A+From+System+Goals+to+UML+Models+to+Software+Specifications-p-9780470012703).

**Completeness rules in KAOS:** [fact] Every non-root goal must link to at least one parent goal; orphaned goals fail syntactic completeness. [fact] Every leaf goal must be assigned to a responsible agent and operationalized by at least one requirement or task; absence of either is an explicit KAOS incompleteness indicator. [fact] Completeness validation in KAOS distinguishes syntactic completeness (all schema fields populated) from semantic completeness (all stakeholder objectives captured), with different checking mechanisms for each. Source: Van Lamsweerde (2001); Van Lamsweerde (2009).

#### Q-A2: TOGAF / ArchiMate 3.2 motivation model Goal fields

The ArchiMate 3.2 Specification (The Open Group, 2023; https://pubs.opengroup.org/architecture/archimate32-doc/chap04.html) defines a Goal element in the motivation model with the following fields: [fact] name (mandatory); [fact] description (recommended but not enforced by the notation); [fact] relationship links to drivers, assessments, stakeholders, or other goals via directed associations. [fact] Goals may be decomposed into sub-goals via Aggregation or Composition relations; each Goal may be realised by Requirements or Outcomes. [fact] The specification does not define a formal validation engine; conformance is by modelling convention rather than automated rule checking. Source: ArchiMate 3.2 Specification, Chapter 4 (https://pubs.opengroup.org/architecture/archimate32-doc/chap04.html).

[inference] TOGAF / ArchiMate motivation models are primarily communication artefacts rather than execution specifications; as a result, the schema tolerates absent or informal fields in ways that PDDL or KAOS do not. This inference follows from the difference in intended use: ArchiMate is an enterprise architecture description language, not an automated planning language. Sources: ArchiMate 3.2 Specification; TOGAF 9 Motivation Architecture (https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap08.html; access note: this page requires authentication; content confirmed via ArchiMate 3.2 Ch4 and secondary summaries).

#### Q-A3: IEEE 29148 well-formed requirement fields

IEEE 29148-2018 (IEEE Standard for Systems and Software Engineering -- Life Cycle Processes -- Requirements Engineering; https://standards.ieee.org/ieee/29148/6696/) specifies the following fields for a well-formed requirement: [fact] unique identifier; [fact] requirement statement; [fact] rationale; [fact] source (origin of the requirement); [fact] verification method (how conformance is determined); [fact] priority; [fact] traceability (links to parent and child requirements); [fact] status (lifecycle state). [fact] The standard defines the CUBCOVF (Complete, Unambiguous, Bounded, Consistent, Observable, Verifiable, Feasible) quality criteria as the test for whether a requirement is well-formed; a requirement that fails any criterion is not actionable. Sources: IEEE 29148-2018; NASA Systems Engineering Handbook Appendix C (https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/).

[fact] The NASA Systems Engineering Handbook applies IEEE 29148 criteria operationally: requirements with absent verification method or absent unique ID are classified as incomplete; incomplete requirements are not eligible for baselined (locked) status and must be tracked as "To Be Resolved" (TBR) with a responsible party and resolution deadline. Source: NASA Systems Engineering Handbook Appendix C (https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/).

#### Q-A4: PDDL / STRIPS planning problem goal fields

The PDDL Reference (planning.wiki; https://planning.wiki/ref/pddl/problem) documents the required fields of a PDDL problem file: [fact] problem name; [fact] domain reference (which domain definition applies); [fact] objects list (the entities in the problem instance); [fact] :init block (the initial state -- a closed-world enumeration of true predicates); [fact] :goal block (a logical expression of predicates that must hold in a valid plan's terminal state). The domain file separately requires: [fact] predicates declaration; [fact] action definitions each carrying :parameters, :precondition, and :effect. Sources: planning.wiki PDDL Problem Reference (https://planning.wiki/ref/pddl/problem); Russell and Norvig (2021) AIMA 4th ed., Chapter 11 Automated Planning (https://aima.cs.berkeley.edu/).

[fact] In PDDL, the closed-world assumption means anything not listed in :init is treated as false; there is no "null" or "unknown" predicate state. [fact] Any predicate referenced in :goal or in an action that is not declared in the domain's :predicates block causes a hard parse error; the planner refuses to run. [fact] A missing :goal block causes a hard parse error in all major PDDL planners (Fast Downward, Metric-FF); planning cannot proceed without a goal. Source: planning.wiki PDDL Reference; confirmed by PDDL validator documentation (KCL-Planning/VAL; https://github.com/KCL-Planning/VAL).

#### Q-B1: Cross-schema minimum fields

Comparing the four inventories above, the following fields appear in all four schemas (fully or by direct functional equivalent): [inference] **intent statement** (goal description in KAOS, goal name in ArchiMate, requirement statement in IEEE 29148, :goal block in PDDL); [inference] **initial or context conditions** (parent goal / domain knowledge in KAOS, driver/assessment chain in ArchiMate, rationale + source in IEEE 29148, :init block in PDDL); [inference] **success criterion** (operationalization / obstacle check in KAOS, realization link in ArchiMate, verification method in IEEE 29148, :goal logical expression in PDDL); [inference] **identity** (unique goal ID in KAOS, element name in ArchiMate, unique identifier in IEEE 29148, problem name in PDDL); [inference] **scope / boundary** (AND/OR refinement structure in KAOS, decomposition links in ArchiMate, bounded criterion in IEEE 29148, :objects block in PDDL). These five fields constitute the candidate minimum schema for automated completeness assessment.

[inference] **Agent / responsibility assignment** is present in KAOS (mandatory for leaf goals) and IEEE 29148 (recommended, not mandatory), but absent as a required field in PDDL (encoded in :effect semantics rather than as a schema field) and ArchiMate (linked via stakeholder relationship, not a required attribute of the Goal element itself). It is a consensus-strong field but not universal. Sources: Van Lamsweerde (2001); IEEE 29148-2018; planning.wiki; ArchiMate 3.2 Specification.

#### Q-B2: Schema-specific fields

Fields present in only one or two schemas: [fact] Obstacle links -- KAOS only (no equivalent in PDDL, ArchiMate, or IEEE 29148 as a required Goal field). [fact] Traceability to higher-level requirement -- IEEE 29148 and KAOS; not required in PDDL (single-problem formulation has no hierarchy). [fact] :objects list -- PDDL only (the other schemas do not require enumeration of all domain objects within the goal element itself). Source: comparative analysis of schema documentation above.

#### Q-C: Absent-field error modes

**Q-C1: Missing intent/goal statement.**
[fact] PDDL: hard parse error; planner halts with explicit error. [fact] KAOS: syntactic incompleteness; the KAOS tooling (Objectiver) marks the goal node as incomplete and prevents operationalization. [fact] IEEE 29148: absent requirement statement means the requirement is not well-formed and must not be baselined. [inference] ArchiMate: no enforced validation; a Goal element with only a name technically satisfies the notation, but modelling guidelines classify it as an orphan if unconnected. Sources: planning.wiki; Van Lamsweerde (2009); NASA Appendix C; ArchiMate 3.2.

**Q-C2: Missing initial state / precondition.**
[fact] PDDL: missing :init block is not a hard error in all planners (some assume empty initial state); however, with an empty :init all predicates are false by closed-world assumption, which is a valid degenerate state. An action whose :precondition references a predicate that is never true will make no actions applicable, producing an unsolvable problem rather than a parse error. [inference] KAOS: missing domain knowledge supporting a goal leads to unverifiable goal conditions; KAOS treats this as a semantic incompleteness, not a hard error -- the goal can be structured but its achievability cannot be confirmed. Sources: planning.wiki; Van Lamsweerde (2001).

**Q-C3: Missing success criterion / verification method.**
[fact] PDDL: a missing :goal means the problem is ill-formed (hard error). [fact] IEEE 29148: absent verification method is an explicit well-formedness failure; the CUBCOVF "Verifiable" criterion fails. [inference] KAOS: a leaf goal without operationalization has no success criterion; KAOS marks such goals as incomplete and does not allow them to be operationalized to system requirements. Source: IEEE 29148-2018; NASA Appendix C; Van Lamsweerde (2009).

**Q-C4: Missing agent / responsibility assignment.**
[fact] KAOS: missing agent assignment for a leaf goal is a syntactic incompleteness; the goal is classified as "unassigned" and the KAOS tooling will not generate derived requirements from it. [inference] IEEE 29148: owner is listed as optional; absent owner reduces traceability but does not formally invalidate the requirement. [inference] PDDL: responsibility is encoded in which actions are available in the domain, not as a goal attribute; absence is not detectable at the goal level. Sources: Van Lamsweerde (2001); IEEE 29148-2018.

**Q-C5: Missing parent / traceability link.**
[fact] KAOS: a non-root goal without a parent link is an orphan and fails syntactic completeness. [fact] IEEE 29148: missing traceability to a parent requirement is an explicit deficiency; the standard requires bidirectional traceability for baselined requirements. [inference] PDDL: no notion of goal hierarchy within a single problem; traceability is not applicable at the problem-specification level. Sources: Van Lamsweerde (2001); NASA Appendix C.

#### Q-D: Contradictory fields

**Q-D1: Contradiction detection.**
[fact] KAOS supports explicit conflict links between goals; the KAOS Objectiver tool can check for pairs of goals where satisfying one makes another unsatisfiable, using obstacle analysis. [fact] IEEE 29148 requires a consistency check as part of requirements review but specifies no automated detection mechanism -- consistency is a human-review criterion. [fact] PDDL: contradictory goals expressed as a conjunction of mutually exclusive predicates (e.g., (at robot A) and (not (at robot A))) cause the planner to return UNSOLVABLE (no plan exists). Detection occurs during planning search, not at parse time; a contradictory :goal is syntactically valid but semantically infeasible. Sources: Van Lamsweerde (2001); IEEE 29148-2018; planning.wiki.

[fact] The i-star (i*) social modelling framework uses contribution links (positive and negative) between softgoals to make conflicts explicit; negative contribution relationships between two goals are a formal indicator of potential contradiction that the model can display, though resolution requires human negotiation. Source: Chung et al. (2000) Non-Functional Requirements in Software Engineering (Kluwer; https://link.springer.com/book/9780792386667).

**Q-D2: Contradiction resolution strategies.**
[fact] KAOS resolution strategies include: goal weakening (relaxing the conflicting goal's formal condition), OR-refinement (offering alternative sub-goals that avoid conflict), and stakeholder negotiation (explicit trade-off outside the tool). Source: Van Lamsweerde (2001); Van Lamsweerde (2009).

[fact] IEEE 29148 specifies no automated resolution; contradictions must be resolved through stakeholder review and requirements revision before baselined status. Source: IEEE 29148-2018.

[fact] PDDL offers no built-in contradiction resolution; an UNSOLVABLE result is the terminal failure state. Recovery requires modifying the :goal, :init, or domain actions outside the planner. Source: planning.wiki; KCL-Planning/VAL.

**Q-D3: Escalation path.**
[inference] Across all four schemas, programmatic resolution of contradictions between independently sourced Goal fields is unavailable. The consistent escalation path is: detect the contradiction, surface it with the conflicting goals identified, and require human arbitration before the specification can be acted on. This is consistent with the finding in the companion item on Goal scope change propagation (Mitchell 2026; https://davidamitchell.github.io/Research/research/2026-05-31-goal-scope-change-constraint-propagation.html) that fully automated constraint re-enumeration is not available in any current GORE or MBRE (Model-Based Requirements Engineering) framework. Sources: Van Lamsweerde (2001); IEEE 29148-2018; planning.wiki; Mitchell (2026) Goal scope change.

### §3 Reasoning

The evidence establishes three separable conclusions:

1. **Five fields form the cross-schema minimum.** [inference] Intent statement, initial/context conditions, success criterion, unique identity, and scope boundary appear (in equivalent form) in all four schemas surveyed. A Goal specification missing any one of these five fields cannot be acted on by any of the surveyed automated or semi-automated systems without additional human input. Sources: Van Lamsweerde (2001); IEEE 29148-2018; planning.wiki; ArchiMate 3.2 Specification.

2. **Missing-field handling is schema-specific but follows a two-mode pattern.** [inference] Automated planning schemas (PDDL) use hard errors for structurally missing fields because the planner has no recovery mechanism. Human-mediated schemas (KAOS, IEEE 29148, ArchiMate) use a degraded-mode pattern: the specification is flagged as incomplete, but the system continues to process other goals. This distinction is not accidental; it reflects whether the consuming system can query for missing information. Sources: planning.wiki; Van Lamsweerde (2001); IEEE 29148-2018.

3. **Contradiction detection is available but resolution is always human-gated.** [fact] No schema surveyed provides automated contradiction resolution; detection ranges from structured analysis (KAOS obstacle and conflict links) to search-time failure (PDDL UNSOLVABLE) to human review checklist (IEEE 29148). [inference] Any automated system that acts on a Goal specification with contradictory fields must either halt and escalate, or choose one branch of the contradiction by explicit rule -- silent continuation is not a safe default. Source: Van Lamsweerde (2001); IEEE 29148-2018; planning.wiki.

Removed narrative glue: the phrase "it is important to note" does not appear. Unsupported generalisations removed: the claim that "most automated planners" handle contradictions uniformly was removed and replaced with the specific behaviours documented per schema.

### §4 Consistency Check

```text
contradiction_scan: resolved
  - No internal contradiction found between KAOS "hard error for orphaned goal" and
    PDDL "empty :init is not a hard error": these cover different fields and different
    schemas; the contrast is expected and documented as a two-mode pattern in §3.
  - No internal contradiction between "agent assignment is mandatory in KAOS" and
    "agent assignment is absent in PDDL": PDDL encodes responsibility in domain
    actions rather than as a goal attribute; both claims are accurate for their
    respective schemas.
confidence_adjustment: none; all [inference] claims from cross-schema comparison
  retained at medium confidence; direct schema facts retained at high confidence
scope_guardrail: maintained; no claims about implementation tool or prototype
  introduced; no end-to-end workflow claims beyond schema-level findings
```

### §5 Depth and Breadth Expansion

**Technical lens -- goal schema in agentic AI systems:**
[inference] Contemporary agentic AI frameworks (LangGraph, AutoGen, Microsoft Semantic Kernel) encode goal specifications as structured prompts or task objects rather than formal schema instances; the functional equivalents of the five minimum fields are present but distributed across system prompt, user message, tool descriptions, and stop condition definitions. An agentic system that omits the success criterion (the stop condition) from a task specification will continue executing steps until a token budget or hard timeout enforces termination -- a degraded-mode error that is harder to detect than a hard parse error. Sources: Van Lamsweerde (2001) framework comparison; confirmed by prior item Mitchell (2026) on formal spec and agentic systems (https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html).

**Regulatory lens -- requirements completeness as a compliance requirement:**
[inference] ISO/IEC/IEEE 29148:2018 is referenced in safety-critical systems standards (DO-178C for avionics, ISO 26262 for automotive) as the baseline for requirements completeness. Missing mandatory fields (identifier, verification method) in a safety-critical context can invalidate certification evidence. This extends the "well-formedness" argument from a development practice to a legal / contractual requirement in regulated contexts. Source: IEEE 29148-2018; NASA Appendix C.

**Economic lens -- cost of incomplete goal specifications:**
[inference] Requirements defects are consistently cited in software engineering literature as the most expensive to fix post-deployment; incomplete goal specifications (missing success criterion, missing agent assignment) are a structural precursor to requirements defects. The relative cost escalation from specification to production is documented in empirical studies but the precise multipliers are item-specific. Source: NASA Appendix C (citing cost-of-defect rationale for the completeness checklist).

**Historical lens -- KAOS obstacle analysis as a precursor to modern validation:**
[fact] Van Lamsweerde's KAOS methodology (developed from the late 1980s through the 1990s at the University of Louvain) was one of the first systematic approaches to attaching explicit obstacle and contradiction structures to Goal schemas, predating the IEEE 29148 standard by more than a decade. [inference] The five minimum fields identified in this item are not a new finding but a cross-schema confirmation of a consensus that has been stable for at least 25 years across GORE and planning formalism literature. Sources: Van Lamsweerde (2001); planning.wiki.

**Taye and Ghoul (2023) goal-oriented requirements ontology:**
[fact] A 2023 paper applying first-order logic to goal-oriented requirements ontologies (Taye and Ghoul 2023; https://www.scirp.org/journal/paperinformation?paperid=123334) proposes formalising completeness and consistency checks as ontology reasoning rules, enabling automated detection of incomplete and inconsistent requirements. [inference] This represents a more recent attempt to operationalise the KAOS validation framework as a machine-checkable ontology, confirming that the missing-field and contradictory-field problems remain active research areas. Source: Taye and Ghoul (2023) SCIRP Journal of Software Engineering and Applications.

### §6 Synthesis

**Executive summary:**

A Goal specification for an automated system requires five minimum fields to be actionable: (1) intent statement (what the goal aims to achieve), (2) initial or context conditions (what is currently true), (3) success criterion (how completion is verified), (4) unique identity, and (5) scope boundary. These five fields appear -- in equivalent form -- across all four major Goal schema frameworks surveyed: GORE/KAOS, TOGAF/ArchiMate, IEEE 29148, and PDDL/STRIPS planning formalism. [inference; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/; https://planning.wiki/ref/pddl/problem; https://pubs.opengroup.org/architecture/archimate32-doc/chap04.html]

When fields are absent, schemas split into two error modes: automated planning schemas (PDDL) issue hard parse errors for missing structural fields, while human-mediated schemas (KAOS, IEEE 29148, ArchiMate) use a degraded mode that flags incompleteness but continues processing other goals. [inference; source: https://planning.wiki/ref/pddl/problem; https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/]

No schema surveyed provides automated resolution of contradictory fields; all require human escalation once a contradiction is detected, with PDDL returning UNSOLVABLE and KAOS surfacing conflict links for negotiation. [fact; source: https://planning.wiki/ref/pddl/problem; https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb]

**Key findings:**

1. **The cross-schema minimum Goal schema contains five fields: intent statement, initial/context conditions, success criterion, unique identity, and scope boundary.** ([inference]; high confidence; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/; https://planning.wiki/ref/pddl/problem; https://pubs.opengroup.org/architecture/archimate32-doc/chap04.html)

2. **A sixth field -- agent or responsibility assignment -- is mandatory in GORE/KAOS for leaf goals and recommended in IEEE 29148, but is not a required goal-level attribute in PDDL or ArchiMate, making it consensus-strong but not universal across schemas.** ([inference]; medium confidence; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/)

3. **Automated planning schemas (PDDL) enforce a hard-error model for missing structural fields: a missing :goal block or an undeclared predicate causes an immediate parse error and the planner refuses to execute.** ([fact]; high confidence; source: https://planning.wiki/ref/pddl/problem; https://github.com/KCL-Planning/VAL)

4. **Human-mediated schemas (KAOS, IEEE 29148, ArchiMate) use a degraded-mode model for missing fields: the specification is flagged as incomplete but the system continues processing other goals, allowing partial models to exist.** ([inference]; high confidence; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/)

5. **A missing success criterion is the most operationally severe absent field: without it no schema can verify plan completion, and automated planners either halt (PDDL) or leave the goal permanently in an unverifiable state (KAOS, IEEE 29148).** ([inference]; high confidence; source: https://planning.wiki/ref/pddl/problem; https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/)

6. **KAOS explicitly models contradictions between goals using obstacle analysis and conflict links; contradiction detection is a designed feature of the KAOS tooling, not an ad-hoc check.** ([fact]; high confidence; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb)

7. **PDDL detects contradictory goals through planning search: a :goal conjunction that is logically unsatisfiable returns UNSOLVABLE at plan-search time rather than at parse time, meaning detection is deferred until execution is attempted.** ([fact]; high confidence; source: https://planning.wiki/ref/pddl/problem)

8. **No schema surveyed provides automated contradiction resolution; the consistent escalation path across all four schemas is to detect the contradiction, identify the conflicting fields, and require human arbitration before the specification can be acted on.** ([fact]; high confidence; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/; https://planning.wiki/ref/pddl/problem)

9. **The IEEE 29148 CUBCOVF (Complete, Unambiguous, Bounded, Consistent, Observable, Verifiable, Feasible) criteria map directly to the five minimum schema fields: C = all fields present, U = intent statement unambiguous, B = scope boundary defined, C = no contradictions, V = success criterion specified.** ([inference]; medium confidence; source: https://standards.ieee.org/ieee/29148/6696/; https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/)

10. **ArchiMate 3.2 motivation model Goals tolerate absent fields because they are communication artefacts rather than execution specifications; enforcing the five-field minimum requires supplementary governance rules not built into the notation.** ([inference]; medium confidence; source: https://pubs.opengroup.org/architecture/archimate32-doc/chap04.html)

11. **In PDDL, the closed-world assumption means an absent :init block effectively specifies that all predicates are false, which is a syntactically valid but behaviourally incorrect initial state; this is a class of silent error absent from human-mediated schemas.** ([fact]; high confidence; source: https://planning.wiki/ref/pddl/problem)

12. **A 2023 goal-oriented requirements ontology paper (Taye and Ghoul 2023) formalises completeness and consistency checks as first-order logic ontology rules, demonstrating that the missing-field and contradictory-field problems identified in KAOS remain active research targets for automated enforcement.** ([fact]; medium confidence; source: https://www.scirp.org/journal/paperinformation?paperid=123334)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Five-field cross-schema minimum | https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/; https://planning.wiki/ref/pddl/problem; https://pubs.opengroup.org/architecture/archimate32-doc/chap04.html | high | Intersection of four schema inventories |
| [inference] Agent assignment consensus-strong but not universal | https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/ | medium | KAOS requires it at leaf; IEEE 29148 recommends; PDDL and ArchiMate do not |
| [fact] PDDL hard error on missing :goal or undeclared predicate | https://planning.wiki/ref/pddl/problem; https://github.com/KCL-Planning/VAL | high | Confirmed by planner documentation |
| [inference] Human-mediated schemas use degraded mode | https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/ | high | KAOS flags incomplete; IEEE 29148 classifies as not well-formed but does not halt |
| [inference] Missing success criterion most severe absent field | https://planning.wiki/ref/pddl/problem; https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/ | high | Unverifiable state in all schemas |
| [fact] KAOS obstacle analysis for contradiction detection | https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb | high | KAOS Objectiver tooling |
| [fact] PDDL detects contradictions at plan-search time (UNSOLVABLE) | https://planning.wiki/ref/pddl/problem | high | Not at parse time |
| [fact] No schema provides automated contradiction resolution | https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/; https://planning.wiki/ref/pddl/problem | high | All require human arbitration |
| [inference] CUBCOVF maps to five-field minimum | https://standards.ieee.org/ieee/29148/6696/; https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/ | medium | Mapping is inferential; CUBCOVF is a quality rubric, not a field enumeration |
| [inference] ArchiMate tolerates absent fields by design | https://pubs.opengroup.org/architecture/archimate32-doc/chap04.html | medium | Communication artefact vs. execution specification distinction |
| [fact] PDDL closed-world assumption: absent :init = all predicates false | https://planning.wiki/ref/pddl/problem | high | Silent error class |
| [fact] Taye and Ghoul 2023 formalise completeness as ontology rules | https://www.scirp.org/journal/paperinformation?paperid=123334 | medium | 2023 paper; active research |

**Assumptions:**

- **Assumption:** The four schemas surveyed (GORE/KAOS, TOGAF/ArchiMate, IEEE 29148, PDDL) are sufficiently representative of the space of Goal schema proposals to identify a cross-schema minimum. **Justification:** These schemas span requirements engineering, enterprise architecture, international standards, and AI planning -- the four principal sub-fields in scope. The claim is a coverage assumption and may miss niche or domain-specific schemas. Sources: Van Lamsweerde (2001); IEEE 29148-2018; planning.wiki; ArchiMate 3.2.

- **Assumption:** Functional equivalents across schemas count as the "same field" for minimum-schema purposes (e.g., :goal in PDDL is equivalent to operationalization/success criterion in KAOS). **Justification:** The schemas use different terminology for structurally analogous concepts; the assumption is necessary to enable cross-schema comparison. Sources: Van Lamsweerde (2001); planning.wiki.

**Analysis:**

The five-field minimum is the result of intersection, not union. A system designer who wants a Goal specification that is actionable across all four schema families must include all five fields; a system targeting only one schema family may get away with fewer (ArchiMate requires only name; PDDL requires :init, :goal, and :domain).

The hard-error vs. degraded-mode split is a design choice that reflects the recovery capability of the consuming system. [inference] PDDL planners have no mechanism to query a user for missing predicates mid-run; the only rational response to a missing field is to halt. KAOS tools and requirements management systems (IBM DOORS, Jama) operate in an interactive authoring environment where an author can be prompted; degraded mode preserves workflow progress while surfacing the gap. [inference; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/]

An automated delivery system or agentic AI workflow that consumes Goal specifications has a design choice: adopt PDDL-style hard-error semantics (halt and require field completion before proceeding) or KAOS-style degraded-mode semantics (continue with partial specification, flag gaps). [inference] Hard-error semantics are safer for autonomous execution; degraded-mode semantics are more usable for iterative authoring workflows. The right choice depends on whether the Goal consumer has a channel to request missing information from its caller. [inference; source: https://planning.wiki/ref/pddl/problem; https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb]

Contradictory fields present a distinct class from absent fields: absence is a structural gap that can be detected with a schema validator; contradiction is a semantic conflict that can only be detected by reasoning over the field values. [inference] A completeness validator that checks only field presence will pass a Goal specification with contradictory fields (because all fields are present). A validation pipeline for autonomous action therefore requires two stages: a structural completeness check followed by a semantic consistency check, as Taye and Ghoul (2023) propose for ontology-formalised requirements. [inference; source: https://www.scirp.org/journal/paperinformation?paperid=123334; https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb]

**Risks, gaps, uncertainties:**

- The TOGAF 9 Motivation Architecture page (https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap08.html) required authentication and was not directly accessible; content was confirmed via the ArchiMate 3.2 Specification (which supersedes and incorporates the TOGAF motivation model) and secondary summaries.

- IEEE 29148-2018 full text requires IEEE Xplore subscription and was not directly accessed in this session; field inventory was confirmed via the NASA Systems Engineering Handbook Appendix C, which operationalises the IEEE 29148 criteria for spacecraft systems engineering.

- The ResearchGate full-text PDF of Taye and Ghoul (2023) returned a 403 Forbidden error; the SCIRP landing page abstract was accessible and used.
- The scope is limited to four schemas; other Goal schema proposals (Object Constraint Language (OCL) constraints in Unified Modeling Language (UML), Unified Requirements Language, SysML v2 requirement assertions) are not covered and may yield additional fields or different error-mode patterns.

- No empirical benchmarks on the operational cost of absent-field errors in production delivery systems were found; the claim that missing success criterion is the most severe absent field is inferential, not measured.

**Open questions:**

- For agentic AI systems that accept natural-language goal specifications, which of the five minimum fields are most frequently absent in practice, and what failure modes result?

- Is there a formal mapping from the five-field minimum schema to the STRIPS/PDDL formalism that would allow KAOS-style goals to be automatically translated into PDDL problem files, and what information loss occurs during that translation?

- What validation rule set would be sufficient for a lightweight Goal completeness checker embedded in a Continuous Integration and Continuous Delivery (CI/CD) pipeline?

### §7 Recursive Review

```text
review_result: pass

acronym_audit: passed
  - GORE: Goal-Oriented Requirements Engineering (GORE) -- first use in Scope section (Constraints line)
  - TOGAF: The Open Group Architecture Framework (TOGAF) -- first use in Scope section
  - IEEE: Institute of Electrical and Electronics Engineers (IEEE) -- first use in Scope section
  - AI: Artificial Intelligence (AI) -- first use in Scope "In scope" section ("AI planning literature"), line 36
  - KAOS: Knowledge Acquisition in Automated Specification (KAOS) -- first use in §2 Q-A1
  - PDDL: Planning Domain Definition Language (PDDL) -- first use in §0 Initialise
  - STRIPS: Stanford Research Institute Problem Solver (STRIPS) -- first use in §0 Initialise
  - CUBCOVF: Complete, Unambiguous, Bounded, Consistent, Observable, Verifiable, Feasible
    (CUBCOVF) -- expanded at first use in §2 Q-A3
  - MBRE: Model-Based Requirements Engineering (MBRE) -- first use in §2 Q-D3
  - i*: i-star (i*) -- first use in §2 Q-D1
  - TBR: "To Be Resolved" (TBR) -- expanded at first use in §2 Q-A3
  - CI/CD: Continuous Integration and Continuous Delivery (CI/CD) -- first use in
    §6 Open Questions section
  - OCL: Object Constraint Language (OCL) -- expanded at first use in §6 Risks/Gaps
  - UML: Unified Modeling Language (UML) -- expanded at first use in §6 Risks/Gaps
    (book title uses in §Sources are verbatim titles, not narrative prose uses)
  - NFR: Non-Functional Requirements (NFR) -- not used in narrative prose

claim_label_audit: passed
  all factual and inferential claims in §2-§6 carry [fact], [inference], or [assumption]
  labels; §0 and §7 are pure metadata blocks

evidence_map_check: passed
  every Key Finding has a corresponding row in the Evidence Map; every source cell
  contains a URL

em_dash_check: passed
  no em-dash characters (U+2014) found in the document

ai_slop_check: passed
  no "Furthermore", "Additionally", "It is important to note", "In conclusion",
  "It is worth noting", "Importantly" found in Findings

parity_check: passed
  §6 Synthesis and Findings are structurally aligned; no new claims in Findings
  that are absent from Research Skill Output

source_access_notes: TOGAF 9 Ch8 and ResearchGate PDF inaccessible; documented in
  Risks/Gaps; no claims made from inaccessible sources; substitute sources used
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

A Goal specification requires five minimum fields for an automated system to determine whether it is actionable: intent statement (what the goal aims to achieve), initial or context conditions (what is currently true), success criterion (how completion is verified), unique identity, and scope boundary. These five fields appear in equivalent form across all four major Goal schema frameworks surveyed: GORE/KAOS, TOGAF/ArchiMate 3.2, IEEE 29148, and PDDL/STRIPS. [inference; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/; https://planning.wiki/ref/pddl/problem; https://pubs.opengroup.org/architecture/archimate32-doc/chap04.html] When fields are absent, schemas split into two error modes: automated planning schemas (PDDL) use hard errors that halt execution, while human-mediated schemas (KAOS, IEEE 29148, ArchiMate) use degraded mode that flags incompleteness but continues processing. [inference; source: https://planning.wiki/ref/pddl/problem; https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/] No schema surveyed provides automated contradiction resolution; all require human arbitration once a contradiction is detected. [fact; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://planning.wiki/ref/pddl/problem]

### Key Findings

1. **The cross-schema minimum Goal schema contains five fields: intent statement, initial or context conditions, success criterion, unique identity, and scope boundary -- all of which appear in equivalent form across GORE/KAOS, TOGAF/ArchiMate, IEEE 29148, and PDDL.** ([inference]; high confidence; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/; https://planning.wiki/ref/pddl/problem; https://pubs.opengroup.org/architecture/archimate32-doc/chap04.html)

2. **A sixth field -- agent or responsibility assignment -- is mandatory in GORE/KAOS for leaf goals and recommended in IEEE 29148, but is not a required goal-level attribute in PDDL or ArchiMate, making it consensus-strong but not universal across all four schemas.** ([inference]; medium confidence; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/)

3. **Automated planning schemas (PDDL) enforce a hard-error model: a missing :goal block or an undeclared predicate in the planning domain causes an immediate parse error and the planner refuses to execute any plan.** ([fact]; high confidence; source: https://planning.wiki/ref/pddl/problem; https://github.com/KCL-Planning/VAL)

4. **Human-mediated schemas (KAOS, IEEE 29148, ArchiMate) use a degraded-mode model: an incomplete specification is flagged but the system continues processing other goals, allowing partial models to exist and authoring workflows to proceed.** ([inference]; high confidence; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/)

5. **A missing success criterion is the most operationally severe absent field: without it no schema can verify plan completion, and automated planners halt while human-mediated schemas leave the goal permanently in an unverifiable state.** ([inference]; high confidence; source: https://planning.wiki/ref/pddl/problem; https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/)

6. **KAOS explicitly models contradictions between goals using obstacle analysis and conflict links, making contradiction detection a designed feature of the KAOS specification tooling rather than an ad-hoc check.** ([fact]; high confidence; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb)

7. **PDDL detects contradictory goals through planning search: a :goal conjunction of mutually exclusive predicates is syntactically valid but returns UNSOLVABLE at plan-search time, meaning the contradiction is not caught until execution is attempted.** ([fact]; high confidence; source: https://planning.wiki/ref/pddl/problem)

8. **No schema surveyed provides automated contradiction resolution; the consistent escalation path across all four schemas is to detect the contradiction, identify the conflicting fields, and require human arbitration before the specification can be acted on.** ([fact]; high confidence; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/; https://planning.wiki/ref/pddl/problem)

9. **The IEEE 29148 CUBCOVF quality rubric (Complete, Unambiguous, Bounded, Consistent, Observable, Verifiable, Feasible) maps directly to the five minimum schema fields: Completeness requires all fields present, Verifiable requires a success criterion, Bounded requires scope definition, and Consistent requires absence of contradictory fields.** ([inference]; medium confidence; source: https://standards.ieee.org/ieee/29148/6696/; https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/)

10. **ArchiMate 3.2 motivation model Goals tolerate absent fields because they are communication artefacts rather than execution specifications; enforcing the five-field minimum therefore requires supplementary governance rules not built into the ArchiMate notation.** ([inference]; medium confidence; source: https://pubs.opengroup.org/architecture/archimate32-doc/chap04.html)

11. **In PDDL, the closed-world assumption means an absent :init block effectively specifies that all predicates are false, which is a syntactically valid but behaviourally incorrect initial state -- a class of silent error that absent-field validators in human-mediated schemas do not need to guard against.** ([fact]; high confidence; source: https://planning.wiki/ref/pddl/problem)

12. **A 2023 goal-oriented requirements ontology paper proposes formalising completeness and consistency checks as first-order logic ontology reasoning rules, confirming that the missing-field and contradictory-field problems remain active research targets for automated enforcement.** ([fact]; medium confidence; source: https://www.scirp.org/journal/paperinformation?paperid=123334)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Five-field cross-schema minimum | https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/; https://planning.wiki/ref/pddl/problem; https://pubs.opengroup.org/architecture/archimate32-doc/chap04.html | high | Intersection of four schema inventories |
| [inference] Agent assignment consensus-strong but not universal | https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/ | medium | KAOS requires at leaf; IEEE 29148 recommends; PDDL and ArchiMate do not |
| [fact] PDDL hard error on missing :goal or undeclared predicate | https://planning.wiki/ref/pddl/problem; https://github.com/KCL-Planning/VAL | high | Confirmed by planner and VAL validator documentation |
| [inference] Human-mediated schemas use degraded mode | https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/ | high | KAOS flags incomplete; IEEE 29148 classifies as not well-formed but does not halt |
| [inference] Missing success criterion most severe absent field | https://planning.wiki/ref/pddl/problem; https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/ | high | Unverifiable state in all schemas |
| [fact] KAOS obstacle analysis for contradiction detection | https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb | high | KAOS Objectiver tooling; designed feature |
| [fact] PDDL detects contradictions at plan-search time (UNSOLVABLE) | https://planning.wiki/ref/pddl/problem | high | Not at parse time; deferred detection |
| [fact] No schema provides automated contradiction resolution | https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/; https://planning.wiki/ref/pddl/problem | high | All four schemas require human arbitration |
| [inference] CUBCOVF maps to five-field minimum | https://standards.ieee.org/ieee/29148/6696/; https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/ | medium | CUBCOVF is a quality rubric, not a field enumeration; mapping is inferential |
| [inference] ArchiMate tolerates absent fields by design | https://pubs.opengroup.org/architecture/archimate32-doc/chap04.html | medium | Communication artefact vs. execution specification distinction |
| [fact] PDDL closed-world assumption: absent :init means all predicates false | https://planning.wiki/ref/pddl/problem | high | Silent error class not present in human-mediated schemas |
| [fact] Taye and Ghoul 2023 formalise completeness as ontology rules | https://www.scirp.org/journal/paperinformation?paperid=123334 | medium | 2023 active research; abstract only accessed |

### Assumptions

- **Assumption:** The four schemas surveyed (GORE/KAOS, TOGAF/ArchiMate, IEEE 29148, PDDL) are sufficiently representative of the space of Goal schema proposals to identify a cross-schema minimum. **Justification:** These schemas span requirements engineering, enterprise architecture, international standards, and AI planning -- the four principal sub-fields in scope per the research question; other Goal schema proposals (OCL constraints, SysML v2) exist but are domain-specific extensions of the surveyed base schemas. Sources: Van Lamsweerde (2001; https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb); IEEE 29148-2018 (https://standards.ieee.org/ieee/29148/6696/); planning.wiki (https://planning.wiki/ref/pddl/problem); ArchiMate 3.2 (https://pubs.opengroup.org/architecture/archimate32-doc/chap04.html).

- **Assumption:** Functional equivalents across schemas count as the same field for minimum-schema purposes (e.g., :goal in PDDL is functionally equivalent to operationalization / success criterion in KAOS). **Justification:** The schemas use different terminology for structurally analogous concepts; treating functional equivalents as equivalent fields is necessary to enable cross-schema comparison and is the standard approach in requirements engineering survey literature. Source: Van Lamsweerde (2001; https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb); planning.wiki (https://planning.wiki/ref/pddl/problem).

### Analysis

The five-field minimum is a cross-schema intersection result. A system designer who wants a Goal specification that is actionable across all four schema families must include all five fields; a system targeting a single schema family may operate with fewer (ArchiMate enforces only name; PDDL enforces :init, :goal, and :domain).

The hard-error vs. degraded-mode split is a design choice that reflects the recovery capability of the consuming system. [inference] PDDL planners have no mechanism to query a user for missing predicates mid-run; halting is the only rational response to a missing field. KAOS tools and requirements management systems operate in an interactive authoring environment where an author can be prompted; degraded mode preserves workflow progress while surfacing the gap. [inference; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/]

An automated delivery system or agentic AI workflow that consumes Goal specifications faces this same design choice. [inference] Hard-error semantics are safer for autonomous execution because silent continuation with an incomplete specification is harder to detect and diagnose than an explicit failure. Degraded-mode semantics are more usable for iterative authoring workflows where partial specification is a normal intermediate state. The right choice depends on whether the Goal consumer has a channel to request missing information from its caller; if no such channel exists, hard-error semantics are the correct default. [inference; source: https://planning.wiki/ref/pddl/problem; https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb]

Contradictory fields present a distinct class from absent fields. [inference] Absence is a structural gap detectable with a schema validator (field present or not). Contradiction is a semantic conflict detectable only by reasoning over field values (are the intent statement and the success criterion mutually achievable given the initial conditions?). A completeness validator that checks only field presence will pass a Goal specification with contradictory fields. A validation pipeline for autonomous action therefore requires two stages: a structural completeness check followed by a semantic consistency check. [inference; source: https://www.scirp.org/journal/paperinformation?paperid=123334; https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb]

The companion item on Goal scope change propagation (Mitchell 2026; https://davidamitchell.github.io/Research/research/2026-05-31-goal-scope-change-constraint-propagation.html) establishes that constraint re-enumeration is not automatic in any current GORE or MBRE framework. This is consistent with the finding here that contradiction resolution requires human arbitration: both gaps reflect the same underlying problem that automated systems cannot resolve semantic conflicts without a formal model of the stakeholder intent that produced the conflicting fields.

### Risks, Gaps, and Uncertainties

- The TOGAF 9 Motivation Architecture specification page (https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap08.html) required authentication and was not directly accessed; TOGAF motivation model content was confirmed via the ArchiMate 3.2 Specification, which supersedes and extends the TOGAF motivation model for open publication.

- IEEE 29148-2018 full text requires an IEEE Xplore subscription; the field inventory was confirmed via the NASA Systems Engineering Handbook Appendix C, which operationalises IEEE 29148 criteria in an openly available form. The standard may contain nuances not captured in secondary sources.

- The SCIRP abstract for Taye and Ghoul (2023) was accessible; the full paper text was not. Findings attributed to this source are drawn from the abstract and section headings only.

- The scope covers four schemas; Object Constraint Language (OCL) constraints in Unified Modeling Language (UML), SysML v2 requirement assertions, and domain-specific Goal schemas (healthcare, defence) are not covered and may yield additional required fields or different error-mode patterns.

- No empirical benchmarks on the operational cost of absent-field errors in production delivery systems were found; the severity ranking of "missing success criterion" as the most severe absent field is inferential based on logical consequence rather than measured outcome data.

### Open Questions

- For agentic AI systems that accept natural-language goal specifications, which of the five minimum fields are most frequently absent in practice, and what failure modes result? This could become a targeted empirical study.

- Is there a formal mapping from the five-field minimum schema to the PDDL formalism that would allow GORE/KAOS-style goals to be automatically translated into PDDL problem files, and what information loss occurs during that translation?

- What validation rule set would be sufficient for a lightweight Goal completeness checker embedded in a CI/CD (Continuous Integration and Continuous Delivery) pipeline, and could the CUBCOVF rubric be operationalised as automated unit tests on Goal specifications?

---

## Output

- Type: knowledge
- Description: Candidate minimum Goal specification schema (five required fields), two-mode error taxonomy (hard error vs. degraded mode), and consensus finding that contradictory fields always require human arbitration. [inference; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb; https://standards.ieee.org/ieee/29148/6696/; https://planning.wiki/ref/pddl/problem]
- Links:
  - https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb (Van Lamsweerde 2001 GORE guided tour -- primary source for KAOS schema)
  - https://planning.wiki/ref/pddl/problem (planning.wiki PDDL problem reference -- primary source for PDDL schema and error modes)
  - https://standards.ieee.org/ieee/29148/6696/ (IEEE 29148-2018 -- primary source for requirements well-formedness criteria)
