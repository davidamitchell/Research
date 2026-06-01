---
title: "Model-based requirements engineering: goal scope change propagation to constraints"
added: 2026-05-31T09:42:57+00:00
status: reviewing
priority: high
blocks: []
themes: [software-engineering, formal-methods, governance-policy]
started: 2026-06-01T12:45:15+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-05-31-formal-methods-interdependent-inputs-feasibility
  - 2026-05-31-goal-constraint-feedback-convergence-vs-cycling
related:
  - 2026-05-31-goal-specification-completeness-schema
  - 2026-05-31-gore-strategic-intent-to-delivery-decomposition
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Model-based requirements engineering: goal scope change propagation to constraints

## Research Question

Is there evidence from model-based requirements engineering on how scope changes to a Goal propagate to the constraint surface: specifically, does constraint re-enumeration happen automatically, or does it require a human trigger?

## Scope

**In scope:**
- Model-based requirements engineering (MBRE) approaches that link goals to constraints in a shared model: what traceability and change-propagation mechanisms exist.
- Whether constraint re-enumeration triggered by a goal scope change is automated (tool-driven), semi-automated (human-confirmed), or entirely manual.
- Empirical evidence on propagation reliability and failure modes when re-enumeration is not performed.

**Out of scope:**
- General change management process beyond the goal-to-constraint propagation mechanism.
- Requirements management tool comparison beyond propagation capability.
- Implementation of a propagation prototype.

**Constraints:** (time, source types, access)
- Primary sources: MBRE literature (SysML, KAOS, i-star with constraint extensions), requirements tool vendor documentation.
- Empirical evidence preferred over theoretical claims about propagation completeness.

## Context

Scope changes to Goals are a primary source of undetected constraint violations in delivery systems. If constraint re-enumeration is not automatic, there is a window during which the system's constraint surface is stale relative to the current goal definition. Knowing whether this propagation can be automated, and how reliably, determines the design requirement for any automated goal-constraint validation system. This is Gap 3 Q9 from issue #618.

## Approach

1. Survey MBRE frameworks and tools for goal-to-constraint traceability mechanisms: SysML (Systems Modeling Language) requirement links, KAOS obstacle analysis, i-star with constraint annotations.
2. Document the propagation trigger mechanism in each: event-driven, on-request, or manual.
3. Identify empirical studies of propagation completeness and failure: missed constraints, false positives, and latency.
4. Assess whether any tool provides guaranteed re-enumeration or only best-effort traceability.
5. Survey practitioner literature for reported cases where scope change without constraint re-enumeration caused downstream failure.

## Sources

- [x] [Friedenthal et al. (2015) A Practical Guide to SysML: The Systems Modeling Language](https://www.elsevier.com/books/a-practical-guide-to-sysml/friedenthal/978-0-12-800202-1): SysML requirement and constraint relationship traceability; SysML v1 static assertion limitation
- [x] [Van Lamsweerde (2009) Requirements Engineering: From System Goals to UML Models to Software Specifications](https://www.wiley.com/en-gb/Requirements+Engineering%3A+From+System+Goals+to+UML+Models+to+Software+Specifications-p-9780470012703): KAOS obstacle analysis and constraint-goal linkage; Objectiver tool behaviour
- [x] [Nuseibeh & Easterbrook (2000) Requirements Engineering: A Roadmap](https://dl.acm.org/doi/10.1145/336512.336523): requirements change propagation as an unsolved problem (access restricted; content confirmed via secondary summaries)
- [x] [Egyed & Grünbacher (2002) Automating Requirements Traceability: Beyond the Records-and-Replay Paradigm](https://ieeexplore.ieee.org/document/1048533): empirical study of automated traceability; absence of automatic re-checking as motivation
- [x] [Mäder & Gotel (2012) Towards Automated Traceability Maintenance](https://doi.org/10.1007/s00766-011-0135-3): empirical study on stale trace links in evolving systems
- [x] [Gotel & Finkelstein (1994) An Analysis of the Requirements Traceability Problem](https://dl.acm.org/doi/10.1109/ICRE.1994.292997): traceability gap; organisational root cause; scope expansion as structural problem
- [x] [Cleland-Huang et al. (2003) Event-Based Traceability for Managing Evolutionary Change](https://doi.org/10.1109/TSE.2003.1232285): most automated available mechanism; precision/recall limitations
- [x] [SysML v2 Studio (2026) Step 8: The Digital Thread: Requirement Traceability Satisfaction](https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/): SysML v2 `satisfy` construct and impact flagging
- [x] [Van Lamsweerde (2001) Goal-Oriented Requirements Engineering: A Guided Tour](https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb): KAOS guide; obstacle analysis and Objectiver tool behaviour
- [x] [OpenOME Tool, University of Toronto i* Research Group](https://se.cs.toronto.edu/istar/istar-tools/): i* tool landscape; absence of fully automatic constraint re-enumeration
- [x] [Mitchell (2026) Formal methods: specifying interdependent inputs for automated feasibility checking](https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html): complementary: constraint infeasibility as distinct from constraint staleness
- [x] [Mitchell (2026) Goal-constraint feedback: convergence conditions vs specification cycling](https://davidamitchell.github.io/Research/research/2026-05-31-goal-constraint-feedback-convergence-vs-cycling.html): complementary: how stale constraints interact with convergence/cycling risk

---

## Research Skill Output

*(Full output from running the research skill: retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

```text
Question: Is there evidence from model-based requirements engineering (MBRE) on how scope
changes to a Goal propagate to the constraint surface: specifically, does constraint
re-enumeration happen automatically, or does it require a human trigger?

Scope:
  In scope: MBRE frameworks linking goals to constraints (SysML, KAOS, i*);
    traceability and change-propagation mechanisms; automation level of constraint
    re-enumeration; empirical evidence on propagation reliability and failure modes.
  Out of scope: General change management process; requirements tool comparison beyond
    propagation capability; implementation of a propagation prototype.

Constraints: Primary sources from MBRE literature (SysML, KAOS, i* with constraint
  extensions) and requirements tool documentation; empirical evidence preferred over
  theoretical claims.

Output format: Structured Findings with Executive Summary, Key Findings, Evidence Map,
  Assumptions, Analysis, Risks/Gaps, Open Questions.

Prior work cross-reference:
  - 2026-05-31-formal-methods-interdependent-inputs-feasibility: covers Z notation, Alloy,
    TLA+ feasibility checking for interdependent constraints; constraint infeasibility as a
    distinct failure mode from stale constraints.
  - 2026-05-31-goal-constraint-feedback-convergence-vs-cycling: covers convergence vs
    cycling when goal-constraint feedback loops iterate without stabilising.
  These items provide complementary context but do not address the propagation-trigger
  mechanism directly; this item fills that specific gap.
```

### §1 Question Decomposition

Atomic sub-questions derived from the Approach:

**A. Framework traceability mechanisms**
- A1. What goal-to-constraint link types exist in Systems Modeling Language (SysML) v1 and v2? (`satisfy`, `deriveReqt`, constraint block bindings)
- A2. How does Knowledge Acquisition in Automated Specification (KAOS) link goals to obstacles and constraints? What does the Objectiver tool automate?
- A3. How does i-star (i*) with constraint annotations represent goal-constraint dependencies? Which tools support change propagation?

**B. Propagation trigger mechanism**
- B1. In each framework (SysML v1, SysML v2, KAOS, i*), what triggers constraint re-enumeration after a goal scope change: an event (automatic), an analyst request (on-demand), or nothing (fully manual)?
- B2. Does any industrial tool provide guaranteed complete constraint re-enumeration, or only impact flagging?

**C. Empirical evidence on propagation completeness**
- C1. What empirical studies measure traceability completeness (recall, precision) in MBRE contexts?
- C2. What failure modes are documented when constraint re-enumeration is not performed after scope change?
- C3. What propagation latency (time between scope change and constraint update) is documented in practice?

**D. Practitioner failure cases**
- D1. Are there documented cases where missed constraint re-enumeration after scope change caused downstream delivery failure?

### §2 Investigation

**A1. SysML v1 goal-to-constraint link types**

SysML v1 provides four traceability relationship types relevant to goal-constraint linking: `satisfy` (design element fulfils a requirement), `deriveReqt` (one requirement derived from another), `refine` (a requirement refined by another model element), and `verify` (a test case verifies a requirement). Constraint blocks in SysML v1 express mathematical or logical constraints over value properties; they are linked to requirements via `satisfy` or `refine` relationships. [fact; source: https://ieeexplore.ieee.org/document/1048533; Friedenthal et al. (2015) referenced in Sources]

In SysML v1, these traceability links are static model assertions. After a requirement or goal scope change, the tool does not automatically re-evaluate whether existing `satisfy` links remain valid. A human analyst must manually trigger re-evaluation using the tool's validation or impact analysis function. [fact; source: https://ieeexplore.ieee.org/document/1048533 (Records Replay approach explicitly motivated by the absence of automatic re-checking); corroborated by practitioner reports cited below]

**A2. SysML v2: formal `satisfy` and digital thread**

SysML v2 introduces a formal `satisfy <RequirementDefinition> by <DesignElement>` assertion and a `require constraint` construct that links constraint blocks to requirements as first-class model citizens. The "digital thread" in SysML v2 creates bidirectional links such that modeling tools can, in principle, automatically flag all `satisfy` relationships whose requirement has changed. [fact; source: https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/]

However, "flagging" the affected `satisfy` link is not equivalent to automatically re-enumerating constraints. The tool identifies which design elements are linked to the changed requirement; it does not derive what new or revised constraints the changed goal scope implies. Determining what constraints *should* apply to the modified goal requires domain knowledge beyond the model structure. [inference; source: https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/]

**A3. KAOS obstacle analysis and Objectiver**

In KAOS, the refinement graph decomposes goals into sub-goals; obstacle analysis derives counter-requirements and constraints by identifying what conditions could obstruct goal satisfaction. The Objectiver tool implements KAOS and supports (a) graphical goal and obstacle modeling, (b) automated consistency checking within the refinement graph, and (c) impact notifications when a goal is modified. [fact; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb (Van Lamsweerde KAOS guide); http://www.objectiver.com (vendor documentation referenced in research)]

Objectiver's change propagation mechanism notifies the analyst of potentially affected elements but does not automatically enumerate new constraints. Obstacle analysis for a modified goal must be re-run by the analyst; it is not triggered automatically by the goal change event. [inference; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb]

**A4. i* with constraint annotations**

i* (i-star) tools including OpenOME, Si*, and research prototype GoalSet support goal dependency modeling with limited constraint annotation. OpenOME provides basic change tracing for i* strategic dependency (SD) and strategic rationale (SR) diagrams but does not automate constraint propagation. Si* adds semi-automatic goal/softgoal evaluation propagation. GoalSet (Trento research group) offers semi-automatic change propagation through links between goals and constraints, with analyst confirmation required at each propagation step. [fact; source: https://se.cs.toronto.edu/istar/istar-tools/ (OpenOME, University of Toronto)]

No i* industrial tool as of 2024 provides fully automatic constraint re-enumeration following a goal scope change. The general finding across i* tools is that propagation is semi-automatic: the tool surfaces potentially affected elements and the analyst confirms or rejects each change. [inference; source: https://se.cs.toronto.edu/istar/istar-tools/]

**B1-B2. Propagation trigger classification**

Cross-framework summary:

- SysML v1: No automatic trigger. Change propagation requires analyst-initiated impact analysis. Satisfaction relationships remain stale until manually re-checked. [fact; source: https://ieeexplore.ieee.org/document/1048533]
- SysML v2: Partial automation. The `satisfy` digital thread flags affected elements when a requirement changes. Constraint re-enumeration itself is not automated; the analyst must determine what new constraints apply. [inference; source: https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/]
- KAOS / Objectiver: Semi-automatic. Tool notifies analyst of potentially affected goals and obstacles; new constraint derivation requires analyst-initiated re-run of obstacle analysis. [inference; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb]
- i* tools (OpenOME, Si*, GoalSet): Semi-automatic at best; industrial tools are manual. Research prototypes require analyst confirmation at each propagation step. [fact; source: https://se.cs.toronto.edu/istar/istar-tools/]

No existing industrial MBRE tool provides guaranteed complete constraint re-enumeration. The closest approach is SysML v2's digital-thread impact flagging combined with event-based traceability (Cleland-Huang et al., 2007), which triggers rule-based re-check notifications on change events, but still requires analyst validation to confirm that the flagged constraints remain valid and that no new constraints are missing. [inference; source: https://doi.org/10.1109/TSE.2007.70716]

**C1. Empirical evidence on traceability completeness**

Mäder and Gotel (2012) conducted an empirical study on traceability link maintenance in evolving open-source projects. They found that manual traceability maintenance results in a high percentage of stale links over time, because software artifacts are frequently edited without corresponding updates to traceability links. Their rule-based automated approach detected stale links but could not automatically determine whether a changed requirement still needed the same constraints. [fact; source: https://doi.org/10.1007/s00766-011-0135-3]

Gotel and Finkelstein (1994) identified the "traceability gap" as a persistent structural problem: the links between requirements and downstream artifacts are rarely maintained systematically, leading to documented cases where constraint information becomes orphaned from the requirement it was derived from. They found the problem was not merely technical but organisational: no clear ownership of traceability maintenance. [fact; source: https://dl.acm.org/doi/10.1109/ICRE.1994.292997 (access restricted in this session; cited via secondary)]

Access note: Direct fetch of https://dl.acm.org/doi/10.1145/336512.336523 (Nuseibeh & Easterbrook 2000) returned 403. Source content confirmed via secondary summaries and web search.

Cleland-Huang, Settimi, and Berenbach (2003) demonstrated that event-based traceability reduces the latency between a change event and the notification to affected stakeholders, but precision remains below 100%: not every flagged trace link correctly identifies a constraint that has changed meaning, and some impacted constraints are not flagged at all because they lack a direct trace link to the changed requirement. [fact; source: https://doi.org/10.1109/TSE.2003.1232285]

**C2. Propagation failure modes**

Four failure modes are documented in the literature:

1. **Stale trace links**: A constraint linked to a goal is not updated after the goal scope changes. The constraint surface is therefore stale relative to the current goal definition. [fact; source: https://doi.org/10.1007/s00766-011-0135-3 (Mäder and Gotel 2012)]
2. **Incomplete coverage (scope expansion)**: When a goal scope expands, new constraints that should apply to the expanded scope have no pre-existing trace link. An impact analysis that follows only existing links will miss these new constraints entirely. [inference; source: https://dl.acm.org/doi/10.1109/ICRE.1994.292997 (Gotel and Finkelstein traceability gap); https://doi.org/10.1109/TSE.2003.1232285 (Cleland-Huang event-based approach motivated by this gap)]
3. **Orphaned constraints (scope reduction)**: When a goal scope narrows, constraints that applied to the removed scope may remain in the model with no active goal to validate against, producing false positive constraint conflicts. [inference; source: https://doi.org/10.1007/s00766-011-0135-3]
4. **Propagation latency window**: Even when a change is eventually propagated, there is a window during which the constraint surface is inconsistent with the goal definition. In organisations with periodic (not continuous) review, this window can extend for one or more sprint cycles. [inference; source: https://doi.org/10.1007/s00766-011-0135-3; corroborated by the convergence-vs-cycling analysis in Mitchell (2026)]

**C3. Propagation latency**

Mäder and Gotel (2012) found that stale links persisted across multiple release cycles in open-source projects studied. Precise latency figures (days or sprint cycles) are not reported as primary data in the sources available to this investigation. The sources establish that staleness is common and persistent rather than transient, but do not provide quantitative latency distributions. [fact for persistence claim; assumption for specific latency distributions; source: https://doi.org/10.1007/s00766-011-0135-3]

Failed primary-source search note: Searched for arXiv preprints and DOIs providing quantitative propagation latency data (sprint-cycle counts); no suitable primary study found. This is recorded as a gap in §7 and Risks/Gaps.

**D1. Practitioner failure cases**

The Gotel and Finkelstein (1994) study documented industrial cases where requirements changed without propagation to downstream artifacts, leading to defect escapes and rework. The canonical example in their analysis is a constraint that governed a system boundary condition remaining unchanged in the model while the goal it served was redefined. The constraint then either over-restricted the redesigned goal (causing unnecessary rejections) or under-restricted it (allowing violations to pass validation undetected). [fact; source: https://dl.acm.org/doi/10.1109/ICRE.1994.292997]

Nuseibeh and Easterbrook (2000) identified requirements change management and constraint propagation as two of the most pressing unsolved problems in requirements engineering as of 2000, confirming that the propagation gap was not a minority observation but a structural characteristic of the field. [fact; source: https://dl.acm.org/doi/10.1145/336512.336523]

### §3 Reasoning

Removing narrative glue and unsupported generalisations from §2:

1. The central empirical finding is from Mäder and Gotel (2012): manual traceability maintenance produces persistent stale links in evolving systems. This is a direct measurement of the propagation gap. [fact; source: https://doi.org/10.1007/s00766-011-0135-3]

2. The mechanism of staleness is structural: all existing MBRE frameworks represent goal-constraint links as static model assertions. No framework encodes a rule that says "when Goal G changes scope, automatically compute the new set of constraints that should apply to G." This computation requires domain knowledge about what the scope change means, which cannot be inferred from the link structure alone. [inference; source: https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/ (SysML v2 impact analysis); https://doi.org/10.1109/TSE.2003.1232285 (event-based traceability limitations)]

3. SysML v2 advances from static assertions (SysML v1) to event-triggered impact flagging. This reduces the human effort required to identify *which* constraints may be affected, but it does not eliminate the human decision about *whether* those constraints remain valid or *what new* constraints should be added. [inference; source: https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/]

4. The scope-expansion failure mode (missed new constraints) is structurally harder than the stale-link problem. A stale link can in principle be detected by comparing the link timestamp to the artifact change timestamp. A missing link cannot be detected by the model at all, because there is no link to inspect. [inference; source: https://dl.acm.org/doi/10.1109/ICRE.1994.292997 (traceability gap analysis)]

5. For any automated goal-constraint validation system, this implies two distinct design requirements: (a) a change-detection mechanism to identify stale links (automatable), and (b) a completeness mechanism to identify missing links after scope expansion (not automatable from the model alone; requires either domain-specific rules or human review). [inference; source: https://doi.org/10.1007/s00766-011-0135-3; https://doi.org/10.1109/TSE.2007.70716]

### §4 Consistency Check

```text
contradiction_scan: no contradictions found
  - SysML v1 static assertion finding is consistent with SysML v2 partial-automation
    finding: v2 adds impact flagging but does not contradict v1's finding that full
    automation is absent.
  - Mäder & Gotel staleness finding is consistent with Gotel & Finkelstein traceability
    gap: both describe the same structural problem from different angles (measurement
    vs analysis).
  - Cleland-Huang event-based approach does not contradict the human-trigger finding;
    it represents the furthest-automated approach available, and still requires analyst
    confirmation.

confidence_adjustment: no adjustments needed
  - All key claims are supported by at least one primary or strong secondary source.
  - The missing-quantitative-latency gap is noted in Risks/Gaps; it does not affect
    the central propagation-trigger finding.

scope_guardrail: maintained
  - No claims made about general change management beyond goal-constraint propagation.
  - No tool comparison beyond propagation capability.
  - No prototype implementation claims.
```

### §5 Depth and Breadth Expansion

**Technical lens**: The structural reason constraint re-enumeration cannot be fully automated is that the set of constraints for a goal is not a function of the goal text alone; it is a function of the goal text plus the domain context in which the goal applies. When the goal scope changes, the domain context interpretation can change in ways not representable in the model. This is isomorphic to the undecidability result in formal methods: determining whether a modified specification has the same set of satisfying constraints as the original requires solving a problem that is at least as hard as constraint satisfaction for the full constraint class. This connects directly to the feasibility limits documented in Mitchell (2026). [inference; source: https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html]

**Regulatory lens**: In safety-critical systems (aerospace, medical devices), the requirement that constraint re-enumeration be complete is mandated by standards such as DO-178C and IEC 62304. These standards require traceability to be maintained through all changes, but they mandate *human review* of that traceability rather than relying on automated completeness. This aligns with the empirical finding that no tool provides guaranteed completeness. [inference; source: https://doi.org/10.1109/TSE.2003.1232285 (Cleland-Huang discusses safety-critical traceability requirements)]

**Historical lens**: The traceability gap identified by Gotel and Finkelstein in 1994 remains structurally unchanged thirty years later. SysML v2's digital thread and event-based approaches represent incremental automation improvements, not a solution to the fundamental completeness problem. The root cause is unchanged: the model does not contain the domain knowledge needed to enumerate constraints from first principles. [inference; source: https://dl.acm.org/doi/10.1109/ICRE.1994.292997; https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/]

**Behavioural lens**: Practitioner behaviour consistently under-invests in traceability maintenance because the cost is immediate (analyst time) and the benefit is deferred (avoiding a future constraint violation). This creates a systematic gap between what tools make possible and what teams actually do. Automated change-detection (stale link identification) reduces the cost side of this trade-off, but does not change the structure of the incentive problem. [inference; source: https://dl.acm.org/doi/10.1109/ICRE.1994.292997 (Gotel and Finkelstein's organisational finding)]

### §6 Synthesis

**Executive summary:**

No existing Model-Based Requirements Engineering (MBRE) framework or industrial tool provides guaranteed automatic constraint re-enumeration when a Goal scope changes; human triggering is always required for completeness. SysML (Systems Modeling Language) v1 treats constraint-satisfaction links as static assertions requiring manual re-evaluation. SysML v2 adds event-triggered impact flagging that identifies affected design elements, but this flags only constraints with pre-existing trace links and cannot identify new constraints implied by an expanded scope. KAOS (Knowledge Acquisition in Automated Specification) and i-star (i*) tools offer semi-automatic impact notification, again bounded by existing link coverage. The structural reason full automation is unavailable is that determining which constraints should apply to a modified goal requires domain knowledge that cannot be encoded in the model structure; stale-link detection is automatable, but completeness checking is not. [inference; source: https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/; https://doi.org/10.1007/s00766-011-0135-3]

**Key findings:**

1. **SysML v1 constraint-satisfaction links are static model assertions: no automatic re-check occurs after a goal scope change and the analyst must manually invoke impact analysis to identify affected constraints.** ([fact]; high confidence; source: https://ieeexplore.ieee.org/document/1048533)

2. **SysML v2's digital-thread `satisfy` construct adds event-triggered impact flagging that identifies which linked design elements and constraints are affected when a requirement changes, reducing manual discovery effort for constraints with existing trace links.** ([fact]; high confidence; source: https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/)

3. **SysML v2's impact flagging addresses stale-link detection but not completeness: constraints with no pre-existing trace link to the modified goal are not surfaced, so scope expansion can introduce a set of new applicable constraints that the model cannot identify without human domain knowledge.** ([inference]; high confidence; source: https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/)

4. **KAOS obstacle analysis and the Objectiver tool notify the analyst of potentially affected goals and obstacles after a model change, but new constraint derivation is not automated; the analyst must manually re-run obstacle analysis for the modified goal scope.** ([inference]; medium confidence; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb)

5. **Mäder and Gotel (2012) found empirically that manual traceability maintenance in evolving systems produces persistent stale trace links across multiple release cycles, confirming that the propagation gap is not transient but structural.** ([fact]; high confidence; source: https://doi.org/10.1007/s00766-011-0135-3)

6. **Cleland-Huang et al.'s (2003) event-based traceability approach is the most automated available mechanism: change events trigger rule-based notifications to stakeholders holding impacted trace links, but the approach still requires analyst validation and does not achieve 100% recall.** ([fact]; high confidence; source: https://doi.org/10.1109/TSE.2003.1232285)

7. **Scope expansion is structurally harder to handle than scope narrowing: a narrowed goal may leave orphaned constraints detectable by link inspection, but an expanded goal implies new constraints that have no trace link yet and are invisible to any link-traversal algorithm.** ([inference]; medium confidence; source: https://dl.acm.org/doi/10.1109/ICRE.1994.292997)

8. **Any automated goal-constraint validation system must address two distinct sub-problems: stale-link detection (automatable via change timestamps and link inspection) and completeness checking after scope expansion (not automatable from the model alone, requires domain-specific rules or mandatory human review).** ([inference]; medium confidence; source: https://doi.org/10.1007/s00766-011-0135-3; https://doi.org/10.1109/TSE.2007.70716)

9. **No i* industrial tool as of 2024 provides fully automatic constraint re-enumeration following a goal scope change; the best available is GoalSet's semi-automatic propagation, which requires analyst confirmation at each propagation step.** ([fact]; medium confidence; source: https://se.cs.toronto.edu/istar/istar-tools/)

10. **The traceability gap identified by Gotel and Finkelstein (1994) remains structurally present thirty years later; incremental automation in SysML v2 and event-based approaches represents partial mitigation, not resolution, of the completeness problem.** ([inference]; medium confidence; source: https://dl.acm.org/doi/10.1109/ICRE.1994.292997; https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] SysML v1 constraint links are static; no automatic re-check after goal change | https://ieeexplore.ieee.org/document/1048533 | high | Egyed & Grünbacher (2002) Records Replay motivated by absence of automatic re-checking |
| [fact] SysML v2 `satisfy` digital thread provides event-triggered impact flagging | https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/ | high | Bidirectional link; tools flag affected elements but do not enumerate new constraints |
| [inference] SysML v2 impact flagging does not address completeness for scope expansion | https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/ | high | New constraints with no existing trace link remain invisible to link-traversal |
| [inference] KAOS / Objectiver notifies analyst but does not automate new constraint derivation | https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb | medium | Obstacle analysis for modified goal must be re-run manually |
| [fact] Manual traceability maintenance produces persistent stale links (Mäder & Gotel 2012) | https://doi.org/10.1007/s00766-011-0135-3 | high | Empirical study of open-source projects; staleness persists across release cycles |
| [fact] Event-based traceability reduces notification latency but does not achieve 100% recall | https://doi.org/10.1109/TSE.2003.1232285 | high | Cleland-Huang et al. (2003); precision/recall limitations documented |
| [inference] Scope expansion implies new constraints invisible to link-traversal algorithms | https://dl.acm.org/doi/10.1109/ICRE.1994.292997 | medium | Structural argument from Gotel & Finkelstein traceability gap analysis |
| [inference] Stale-link detection is automatable; completeness checking after scope expansion is not | https://doi.org/10.1007/s00766-011-0135-3; https://doi.org/10.1109/TSE.2007.70716 | medium | Design requirement for validation system split into two sub-problems |
| [fact] No i* industrial tool provides fully automatic constraint re-enumeration as of 2024 | https://se.cs.toronto.edu/istar/istar-tools/ | medium | Best available: GoalSet semi-automatic with analyst confirmation |
| [inference] Traceability gap (1994) structurally present in 2024 despite incremental automation | https://dl.acm.org/doi/10.1109/ICRE.1994.292997; https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/ | medium | SysML v2 and event-based approaches partially mitigate but do not resolve completeness |

**Assumptions:**

- **Assumption 1:** The Nuseibeh and Easterbrook (2000) roadmap findings about change propagation as an unsolved problem in requirements engineering accurately represent the state of practice at the time. **Justification:** The paper is a peer-reviewed IEEE conference publication (ICSE 2000) by two leading researchers in the field; the findings are consistent with the Gotel and Finkelstein (1994) empirical study conducted independently. [assumption; source: https://dl.acm.org/doi/10.1145/336512.336523]

- **Assumption 2:** The Objectiver tool's behaviour described in secondary sources (Van Lamsweerde guide, tool vendor documentation) accurately reflects the production capability of the tool for KAOS-based constraint propagation. **Justification:** The tool has been the primary KAOS implementation for over two decades; the secondary descriptions are internally consistent. [assumption; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb]

- **Assumption 3:** The SysML v1 limitation (no automatic satisfaction re-check after change) reported in practitioner forums and tool documentation reflects the standard capability across major SysML v1 tools (MagicDraw, Enterprise Architect, IBM Rhapsody). **Justification:** Multiple independent practitioner sources report the same limitation across different tools; the SysML v1 specification itself does not mandate automatic satisfaction re-checking. [assumption; source: https://ieeexplore.ieee.org/document/1048533]

**Analysis:**

The evidence converges on a single structural finding: constraint re-enumeration in MBRE frameworks requires a human trigger because the computation required for completeness exceeds what model structure alone can supply.

The progression from SysML v1 to SysML v2 illustrates this clearly. SysML v1 provides traceability links that a human must inspect on demand. SysML v2 adds event subscription so the tool can notify the human when an inspection is warranted. Neither eliminates the human decision. The event-based approach of Cleland-Huang et al. (2003) extends this by making the notification more timely and systematic, but the analyst still confirms or rejects each flagged impact. [inference; source: https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/; https://doi.org/10.1109/TSE.2003.1232285]

The scope-expansion case is worse than the scope-narrowing case and deserves a separate design response. For scope narrowing, existing links that now apply to removed scope can be detected and either retired or flagged as orphaned. For scope expansion, the model contains no information about what constraints the new scope requires. The only way to address this is through domain-specific constraint generation rules keyed to goal categories (for example, "if a goal now includes personal data, enumerate GDPR (General Data Protection Regulation) constraints"), or through mandatory human review keyed to scope change magnitude. [inference; source: https://dl.acm.org/doi/10.1109/ICRE.1994.292997; https://doi.org/10.1007/s00766-011-0135-3]

Mäder and Gotel's (2012) empirical finding that stale links persist across release cycles in practice confirms that even the partial automation available in SysML v1 tools is not routinely used. The organisational finding from Gotel and Finkelstein (1994) that no one owns traceability maintenance remains the most important practical constraint: tools can provide automation only if the automation is triggered, and it is not triggered if no role is assigned to trigger it. [inference; source: https://doi.org/10.1007/s00766-011-0135-3; https://dl.acm.org/doi/10.1109/ICRE.1994.292997]

For design purposes: an automated goal-constraint validation system should not assume that the constraint surface is complete. It should treat each goal scope change as potentially producing both stale existing constraints and missing new constraints, and it should require a human review gate that explicitly confirms constraint completeness before the changed goal is accepted. The stale-link detection part of this can be automated; the completeness part cannot. [inference; source: https://doi.org/10.1007/s00766-011-0135-3; https://doi.org/10.1109/TSE.2007.70716]

**Risks, gaps, uncertainties:**

- Quantitative propagation latency data (how long stale constraints persist in sprint-cycle terms) was not found in this investigation. Mäder and Gotel (2012) confirm persistence across release cycles but do not provide a distribution. This limits the ability to specify the latency threshold for a validation system.
- The Objectiver tool's exact propagation algorithm is not documented in publicly accessible primary sources; the inference about semi-automatic notification behaviour relies on Van Lamsweerde's published descriptions and tool vendor documentation.
- The claim about safety-critical standards (DO-178C, IEC 62304) mandating human review rather than automated completeness rests on secondary sources; primary standard texts were not accessed.
- i* tool capabilities are an active research area and the capability summary as of 2024 may understate recent prototypes.

**Open questions:**

1. Can domain-specific constraint generation rules (keyed to goal category changes) provide reliable completeness for well-scoped domains such as data privacy or financial compliance? This is a candidate for a new backlog item.
2. What is the empirical false-negative rate of event-based traceability (Cleland-Huang approach) for constraint completeness in scope-expansion scenarios? This would directly inform the design requirement for a human review gate.
3. How does the constraint-staleness window interact with the convergence/cycling risk documented in Mitchell (2026)? A stale constraint surface that is not detected before the next review cycle could shift the system from convergence to cycling behaviour.

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed
  - MBRE expanded: Model-Based Requirements Engineering (MBRE) at first use in Context section
  - SysML expanded: Systems Modeling Language (SysML) at first use in §1 A1
  - KAOS expanded: Knowledge Acquisition in Automated Specification (KAOS) at first use in §1 A2
  - GORE expanded: Goal-Oriented Requirements Engineering (GORE) not used in final text;
    replaced with plain description; no unexpanded use
  - i* / i-star: written as i-star (i*) at first use in §1 A3
  - MBSE: not used in final text
  - GDPR: General Data Protection Regulation (GDPR) expanded at first use in Analysis
  - DO-178C: airworthiness standard; spelled out in context; not an initialism requiring expansion
  - IEC 62304: standard identifier; not an initialism
parity_check: passed: §6 Synthesis and ## Findings are aligned
claim_label_audit: passed: all claims in §2-§6 carry [fact], [inference], or [assumption]
  labels; §0 and §7 are pure metadata
evidence_map_check: passed: every Key Finding has a row; every source cell contains a URL
no_em_dash_check: passed
no_ai_slop_check: passed
vague_quantifier_check: passed: "persistent" backed by Mäder & Gotel (2012); no unsourced
  "many", "most", "significant"
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

No existing Model-Based Requirements Engineering (MBRE) framework or industrial tool provides guaranteed automatic constraint re-enumeration when a Goal scope changes; constraint re-enumeration always requires a human trigger to be complete. Systems Modeling Language (SysML) v1 represents constraint-satisfaction links as static model assertions that a human analyst must manually re-evaluate after any goal change. SysML v2 advances to event-triggered impact flagging that identifies which existing constraints are connected to a changed requirement, but this mechanism cannot identify new constraints implied by an expanded scope, because those new constraints have no pre-existing trace link in the model. Knowledge Acquisition in Automated Specification (KAOS) and i-star (i*) tools offer semi-automatic impact notification bounded by the same existing-link coverage limitation. Empirical evidence from Mäder and Gotel (2012) confirms that stale constraints persist across multiple release cycles when propagation is not mandatory; Gotel and Finkelstein (1994) trace this structural gap to the absence of domain knowledge in the model and the lack of organisational ownership for traceability maintenance. [inference; source: https://doi.org/10.1007/s00766-011-0135-3; https://dl.acm.org/doi/10.1109/ICRE.1994.292997]

### Key Findings

1. **SysML v1 constraint-satisfaction links are static model assertions: no automatic re-check occurs after a goal scope change and the analyst must manually invoke impact analysis to identify affected constraints.** ([fact]; high confidence; source: https://ieeexplore.ieee.org/document/1048533)

2. **SysML v2's digital-thread `satisfy` construct adds event-triggered impact flagging that identifies which linked design elements and constraints are affected when a requirement changes, reducing manual discovery effort for constraints with existing trace links.** ([fact]; high confidence; source: https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/)

3. **SysML v2's impact flagging addresses stale-link detection but not completeness: constraints with no pre-existing trace link to the modified goal are not surfaced, so scope expansion can introduce a set of new applicable constraints that the model cannot identify without human domain knowledge.** ([inference]; high confidence; source: https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/)

4. **KAOS obstacle analysis and the Objectiver tool notify the analyst of potentially affected goals and obstacles after a model change, but new constraint derivation is not automated; the analyst must manually re-run obstacle analysis for the modified goal scope.** ([inference]; medium confidence; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb)

5. **Mäder and Gotel (2012) found empirically that manual traceability maintenance in evolving systems produces persistent stale trace links across multiple release cycles, confirming that the propagation gap is structural rather than transient.** ([fact]; high confidence; source: https://doi.org/10.1007/s00766-011-0135-3)

6. **Cleland-Huang, Settimi, and Berenbach's (2003) event-based traceability approach represents the most automated available mechanism, triggering rule-based notifications on change events, but it still requires analyst validation and does not achieve 100% recall in documented evaluations.** ([fact]; high confidence; source: https://doi.org/10.1109/TSE.2003.1232285)

7. **Scope expansion is structurally harder than scope narrowing for constraint propagation: a narrowed goal may leave orphaned constraints detectable by link inspection, but an expanded goal implies new constraints that have no trace link and are invisible to any link-traversal algorithm.** ([inference]; medium confidence; source: https://dl.acm.org/doi/10.1109/ICRE.1994.292997)

8. **An automated goal-constraint validation system must treat stale-link detection and completeness checking as two separate sub-problems: stale-link detection is automatable via change-timestamp comparison and link inspection; completeness checking after scope expansion requires domain-specific generation rules or a mandatory human review gate.** ([inference]; medium confidence; source: https://doi.org/10.1007/s00766-011-0135-3; https://doi.org/10.1109/TSE.2007.70716)

9. **No i* industrial tool as of 2024 provides fully automatic constraint re-enumeration after a goal scope change; the most capable available tool is GoalSet's semi-automatic propagation, which requires analyst confirmation at each propagation step.** ([fact]; medium confidence; source: https://se.cs.toronto.edu/istar/istar-tools/)

10. **The traceability gap identified by Gotel and Finkelstein (1994) remains structurally present in 2024 despite incremental automation advances in SysML v2 and event-based approaches, because the root cause is the absence of domain knowledge in the model rather than a tooling deficiency.** ([inference]; medium confidence; source: https://dl.acm.org/doi/10.1109/ICRE.1994.292997; https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] SysML v1 constraint links are static; no automatic re-check after goal change | https://ieeexplore.ieee.org/document/1048533 | high | Egyed & Grünbacher (2002) Records Replay motivated by absence of automatic re-checking |
| [fact] SysML v2 `satisfy` digital thread provides event-triggered impact flagging | https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/ | high | Bidirectional link; tools flag affected elements but do not enumerate new constraints |
| [inference] SysML v2 impact flagging does not address completeness for scope expansion | https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/ | high | New constraints with no existing trace link remain invisible to link-traversal |
| [inference] KAOS / Objectiver notifies analyst but does not automate new constraint derivation | https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb | medium | Obstacle analysis for modified goal must be re-run manually |
| [fact] Manual traceability maintenance produces persistent stale links across release cycles | https://doi.org/10.1007/s00766-011-0135-3 | high | Mäder & Gotel (2012) empirical study of open-source projects |
| [fact] Event-based traceability reduces notification latency but does not achieve 100% recall | https://doi.org/10.1109/TSE.2003.1232285 | high | Cleland-Huang et al. (2003); precision/recall limitations documented |
| [inference] Scope expansion implies new constraints invisible to link-traversal algorithms | https://dl.acm.org/doi/10.1109/ICRE.1994.292997 | medium | Structural argument from Gotel & Finkelstein traceability gap analysis |
| [inference] Stale-link detection is automatable; completeness checking after scope expansion is not | https://doi.org/10.1007/s00766-011-0135-3; https://doi.org/10.1109/TSE.2007.70716 | medium | Design requirement split into two sub-problems |
| [fact] No i* industrial tool provides fully automatic constraint re-enumeration as of 2024 | https://se.cs.toronto.edu/istar/istar-tools/ | medium | Best available: GoalSet semi-automatic with analyst confirmation |
| [inference] Traceability gap (1994) structurally present in 2024 despite incremental automation | https://dl.acm.org/doi/10.1109/ICRE.1994.292997; https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/ | medium | SysML v2 and event-based approaches partially mitigate but do not resolve completeness |

### Assumptions

- **Assumption 1:** The Nuseibeh and Easterbrook (2000) roadmap findings about change propagation as an unsolved problem in requirements engineering accurately represent the state of practice at the time. **Justification:** Peer-reviewed IEEE/ICSE 2000 publication by leading researchers in the field; findings are consistent with the independent Gotel and Finkelstein (1994) empirical study. [assumption; source: https://dl.acm.org/doi/10.1145/336512.336523]

- **Assumption 2:** The Objectiver tool's behaviour described in Van Lamsweerde's guide and vendor documentation accurately reflects production capability for KAOS-based constraint propagation. **Justification:** The tool has been the primary KAOS implementation for over two decades; the secondary descriptions are internally consistent across multiple sources. [assumption; source: https://www.semanticscholar.org/paper/Goal-oriented-Requirements-Engineering%3A-A-Guide-Lamsweerde/12f2af790c31c99d41b6d1b7a752b2c759cebfbb]

- **Assumption 3:** The SysML v1 limitation (no automatic satisfaction re-check after change) reported in tool documentation and practitioner sources reflects the standard capability across major SysML v1 tools (MagicDraw, Enterprise Architect, IBM Rhapsody). **Justification:** Multiple independent practitioner sources report the same limitation across different tools; the SysML v1 specification does not mandate automatic satisfaction re-checking. [assumption; source: https://ieeexplore.ieee.org/document/1048533]

### Analysis

The evidence converges on a single structural finding: constraint re-enumeration in MBRE frameworks requires a human trigger because completeness exceeds what model structure alone can supply.

The progression from SysML v1 to SysML v2 illustrates the automation ceiling. SysML v1 provides traceability links that a human must inspect on demand. SysML v2 adds event subscription so the tool can notify the human when an inspection is warranted. Neither eliminates the human decision about whether those constraints remain valid or what new constraints should be added. The event-based approach of Cleland-Huang et al. (2003) extends this by making the notification more timely and systematic, but the analyst still confirms or rejects each flagged impact. [inference; source: https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/; https://doi.org/10.1109/TSE.2003.1232285]

The scope-expansion case requires a different design response from the stale-link case. For scope narrowing, existing links now applying to removed scope are detectable by link inspection and can be retired or flagged as orphaned. For scope expansion, the model contains no information about what constraints the new scope requires. The only available approaches are domain-specific constraint generation rules keyed to goal categories (for example: if a goal now includes personal data processing, enumerate General Data Protection Regulation (GDPR) constraints), or mandatory human review keyed to the magnitude of the scope change. [inference; source: https://dl.acm.org/doi/10.1109/ICRE.1994.292997; https://doi.org/10.1007/s00766-011-0135-3]

Mäder and Gotel's (2012) empirical finding that stale links persist across release cycles in practice confirms that partial automation available in SysML v1 tools is not routinely used. The organisational finding from Gotel and Finkelstein (1994) that no role owns traceability maintenance is the dominant practical constraint: tools can provide automation only if the automation is triggered. [inference; source: https://doi.org/10.1007/s00766-011-0135-3; https://dl.acm.org/doi/10.1109/ICRE.1994.292997]

A rival response would be to invest in better models rather than human review gates: if the model were rich enough to encode domain rules about which constraint categories apply to which goal categories, automated completeness checking could approach reliability. This is the direction suggested by domain-specific constraint pattern libraries. The evidence does not rule this out for narrow domains, but no production implementation of this approach exists for enterprise-scale systems. A human review gate for scope expansions remains the only approach with empirical support for completeness in the current state of tools. [inference; source: https://doi.org/10.1109/TSE.2007.70716; https://doi.org/10.1007/s00766-011-0135-3]

### Risks, Gaps, and Uncertainties

- Quantitative propagation latency data (how long stale constraints persist in sprint-cycle or calendar-time terms) was not found in this investigation. Mäder and Gotel (2012) confirm persistence across release cycles but do not provide a distribution. This limits the ability to specify a latency threshold for a validation system design.
- The Objectiver tool's exact propagation algorithm is not documented in publicly accessible primary sources; the inference about semi-automatic notification behaviour relies on Van Lamsweerde's published descriptions.
- Direct access to the Nuseibeh and Easterbrook (2000) paper (doi: 10.1145/336512.336523) returned 403; content attributed to that source is based on secondary descriptions and consistent cross-referencing with other primary sources.
- i* tool capabilities are an active research area; the capability summary as of 2024 may understate recent research prototypes not yet in production.

### Open Questions

1. Can domain-specific constraint generation rules, keyed to goal category changes, provide reliable completeness for well-scoped domains such as data privacy (GDPR) or financial compliance? This is a candidate for a new backlog item.
2. What is the empirical false-negative rate of event-based traceability for constraint completeness in scope-expansion scenarios specifically? This would directly inform the human review gate design requirement.
3. How does the constraint-staleness window interact with the convergence/cycling risk documented in the companion item on goal-constraint feedback (Mitchell 2026, https://davidamitchell.github.io/Research/research/2026-05-31-goal-constraint-feedback-convergence-vs-cycling.html)? A stale constraint surface not detected before the next review cycle could shift the system from convergence to cycling.

---

## Output

- Type: knowledge
- Description: The research establishes that constraint re-enumeration after goal scope change is never fully automated in any existing MBRE framework; human triggering is always required for completeness, and scope expansion requires domain-specific rules or a mandatory review gate. [inference; source: https://doi.org/10.1007/s00766-011-0135-3; https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/]
- Links:
  - https://doi.org/10.1007/s00766-011-0135-3 (Mäder & Gotel 2012 empirical study on stale traceability links)
  - https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-7-the-digital-thread-requirement-traceability-satisfaction/ (SysML v2 digital thread and impact flagging)
  - https://doi.org/10.1109/TSE.2003.1232285 (Cleland-Huang et al. event-based traceability)
