---
review_count: 2
title: "Goal fragmentation: signals distinguishing salami-slicing from legitimate sub-goals"
added: 2026-05-31T09:42:57+00:00
status: completed
priority: medium
blocks: []
themes: [software-engineering, governance-policy, formal-methods]
started: 2026-06-02T12:18:31+00:00
completed: 2026-06-02T13:11:51+00:00
output: [knowledge]
cites:
  - 2026-05-31-gore-strategic-intent-to-delivery-decomposition
  - 2026-05-31-goal-specification-completeness-schema
related:
  - 2026-05-31-goal-scope-change-constraint-propagation
  - 2026-05-31-goal-constraint-feedback-convergence-vs-cycling
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Goal fragmentation: signals distinguishing salami-slicing from legitimate sub-goals

## Research Question

When a Goal is a fragment of a larger intent (salami-sliced deliberately or accidentally), what signals distinguish it from a legitimately scoped sub-goal?

## Scope

**In scope:**
- Defining and distinguishing two patterns: (a) salami-slicing (artificial fragmentation to evade scope or approval thresholds) and (b) legitimate goal decomposition (principled sub-goal scoping).
- Observable signals, heuristics, or structural properties that differentiate the two patterns in written goal specifications.
- Evidence from requirements engineering, product management, and programme governance literature on detection approaches.

**Out of scope:**
- Deliberate misuse or fraud detection beyond honest scope management error.
- Automated tool implementation for detection.
- Goal quality assessment beyond the fragment-vs-sub-goal distinction.

**Constraints:** (time, source types, access)
- Prioritise empirical evidence and documented heuristics over purely theoretical classification.
- Relevant domains include software delivery, programme management, enterprise architecture, and public sector procurement.

## Context

Deliberate or accidental goal fragmentation is a recurring dysfunction in delivery governance: goals are split to remain below approval thresholds, avoid constraint checks, or defer hard trade-offs. Automated systems that process goal specifications need to detect this pattern to avoid acting on structurally valid but semantically incomplete inputs. This is Gap 1 Q4 from issue #618.

## Approach

1. Define the conceptual distinction between salami-slicing and legitimate sub-goal scoping; identify the structural and semantic properties that separate them.
2. Survey requirements engineering, programme governance, and product management literature for documented signals and heuristics.
3. Catalogue signal categories: structural (e.g. missing parent reference, no value delivery at the fragment level), semantic (e.g. outcome only realisable in combination), and contextual (e.g. approval threshold proximity).
4. Assess signal reliability: are there false positives and false negatives documented in the literature?
5. Identify whether any formal method or standard encodes these signals as validation rules.

## Sources

- [x] [Van Lamsweerde et al. (2001) Handling Obstacles in Goal-Oriented Requirements Engineering](https://doi.org/10.1109/ISRE.2001.948567): Knowledge Acquisition in Automated Specification (KAOS) AND-refinement completeness and bidirectional entailment requirement
- [x] [Wake (2003) INVEST in Good Stories, and SMART Tasks](https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/): Independent, Negotiable, Valuable, Estimable, Small, Testable (INVEST) criteria; horizontal slicing as anti-pattern; "Valuable" and "Testable" signals
- [x] [Agile Alliance (2023) INVEST Glossary](https://www.agilealliance.org/glossary/invest/): canonical definition of INVEST criteria
- [x] [Pinsent Masons (2023) Bridge ruling: warning for English planning applications](https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications): Environmental Impact Assessment (EIA) Ashchurch ruling; functional interdependence test; three-part salami-slicing detection framework
- [x] [planning.wiki PDDL Problem Reference](https://planning.wiki/ref/pddl/problem): Planning Domain Definition Language (PDDL) goal block; mutual precondition chains
- [x] [Reinertsen (2009) The Principles of Product Development Flow](https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009): batch-size and scope fragmentation; secondary access only
- [x] [AXELOS Managing Successful Programmes (MSP)](https://www.axelos.com/certifications/propath/managing-successful-programmes-msp): Benefit Dependency Network (BDN) orphaned-node concept; product page access only
- [x] [Firesmith (2004) Specifying Reusable Security Requirements](https://www.jot.fm/issues/issue_2004_01/column6.pdf): goal granularity and scope-coherence; PDF retrieved as binary only
- [x] [Yu (1997) Towards Modelling and Reasoning Support for Early-Phase Requirements Engineering](https://doi.org/10.1109/ISRE.1997.582369): i-star means-end links; structural orphan in strategic dependency models

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

```text
Question: When a Goal is a fragment of a larger intent: salami-sliced deliberately or
  accidentally: what signals distinguish it from a legitimately scoped sub-goal?

Scope in: (a) Conceptual distinction between salami-slicing (artificial fragmentation
  to evade scope or approval thresholds) and legitimate goal decomposition (principled
  sub-goal scoping). (b) Observable signals, heuristics, or structural properties that
  differentiate the two patterns in written goal specifications. (c) Evidence from
  requirements engineering, product management, and programme governance literature on
  detection approaches.

Scope out: Deliberate misuse or fraud detection beyond honest scope management error;
  automated tool implementation for detection; goal quality assessment beyond the
  fragment-vs-sub-goal distinction.

Constraints: Prioritise empirical evidence and documented heuristics over purely
  theoretical classification. Domains: software delivery, programme management, enterprise
  architecture, public sector procurement.

Output format: knowledge item: signal taxonomy (structural, semantic, contextual),
  false-positive and false-negative catalogue, formal-method encoding assessment.

Domain terms:
- Goal-Oriented Requirements Engineering (GORE): an approach to software and systems
  requirements that uses goals as the primary organising concept; sub-frameworks include
  KAOS (Knowledge Acquisition in Automated Specification), i-star, and the Non-Functional
  Requirements (NFR) Framework.
- Salami-slicing: the deliberate or accidental splitting of a single coherent goal into
  multiple fragments, each below a governance or approval threshold, such that the
  aggregate intent is never visible in any single specification artefact.
- Legitimate sub-goal: a goal that is principally derived from a parent goal via AND-
  or OR-refinement (GORE terminology), delivers value independently or as a clearly
  bounded phase, and whose relationship to the parent is explicitly declared.
- INVEST: Independent, Negotiable, Valuable, Estimable, Small, Testable: a checklist
  for well-formed user stories in agile product management, introduced by Bill Wake
  (2003).
- Environmental Impact Assessment (EIA): a regulatory process requiring that projects
  above defined impact thresholds undergo structured environmental review. Case law
  on EIA is a documented source of "functional interdependence" tests for project
  splitting detection.
- Benefit Dependency Network (BDN): a programme management tool mapping strategic
  objectives through benefits, capabilities, enabling changes, and initiatives; an
  orphaned node in a BDN signals a fragment with no declared pathway to a strategic
  objective.

Prior-work cross-reference: Three directly related completed items exist:
  - 2026-05-31-gore-strategic-intent-to-delivery-decomposition: documents GORE AND/OR
    refinement rules and the abstraction gap. AND-refinement requires bidirectional
    logical entailment between parent and sub-goals; absence of that entailment is a
    fragmentation signal.
    (https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-gore-strategic-intent-to-delivery-decomposition.md)
  - 2026-05-31-goal-specification-completeness-schema: five-field minimum schema
    (intent statement, initial conditions, success criterion, unique identity, scope
    boundary); a fragment that cannot pass these five fields is structurally incomplete.
    (https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-goal-specification-completeness-schema.md)
  - 2026-05-31-goal-scope-change-constraint-propagation: scope changes propagate
    incompletely through goal refinement trees when dependencies are not declared.
    (https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-goal-scope-change-constraint-propagation.md)

Working hypotheses:
[assumption] Structural signals (missing parent reference, no standalone value) will be
  more consistently detectable than contextual signals (approval threshold proximity),
  because structural signals are intrinsic to the specification text while contextual
  signals require external governance data. Source: deduced from scope constraints.
[assumption] No single signal is sufficient; a weighted combination will be needed to
  distinguish the two patterns reliably, as individual signals have documented false
  positives and false negatives. Source: deduced from domain knowledge of requirements
  engineering heuristics.
```

### §1 Question Decomposition

The research question decomposes into five atomic clusters:

**Cluster A: Conceptual distinction**
- A1: What is the established definition of salami-slicing in requirements engineering
  and programme governance?
- A2: What structural properties define a legitimately scoped sub-goal in formal
  Goal-Oriented Requirements Engineering (GORE) frameworks (Knowledge Acquisition in
  Automated Specification (KAOS), i-star)?
- A3: What is the boundary condition between "principled decomposition" and "artificial
  fragmentation"?

**Cluster B: Structural signals**
- B1: Does a missing parent-goal reference distinguish a fragment from a sub-goal?
- B2: Does a missing independent verification criterion (success criterion only verifiable
  in combination with other goals) signal fragmentation?
- B3: Is a goal that is scoped entirely by technical layer rather than by end-to-end
  value a fragmentation signal?
- B4: Does GORE AND-refinement completeness (bidirectional entailment) provide a formal
  structural test?

**Cluster C: Semantic signals**
- C1: Is outcome-realisability-in-isolation a meaningful semantic distinction?
- C2: Does the Independent, Negotiable, Valuable, Estimable, Small, Testable (INVEST)
  "Valuable" and "Independent" criteria in product management provide
  a documented semantic test?
- C3: Are there semantic signals from goal granularity and scope-coherence theory
  (Firesmith 2004)?

**Cluster D: Contextual signals**
- D1: Does approval-threshold proximity constitute a detectable signal in governance
  literature?
- D2: Does the environmental planning (EIA) "functional interdependence" test translate
  to requirements governance?
- D3: Does timing clustering of related fragment submissions constitute a documented
  signal?

**Cluster E: Signal reliability**
- E1: Are false positives documented in the literature (legitimate sub-goals that
  exhibit fragmentation signals)?
- E2: Are false negatives documented (fragmented goals that pass structural and semantic
  tests)?
- E3: Do any formal methods or standards encode these signals as validation rules?

### §2 Investigation

#### §2.A: Conceptual distinction (Clusters A1–A3)

**Salami-slicing in procurement and governance**

Salami-slicing is documented as an evasion tactic in public procurement and planning law,
where a promoter divides a single project into smaller parts to avoid crossing approval or
Environmental Impact Assessment (EIA) thresholds that would trigger higher-level scrutiny.
[fact; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]
The UK Court of Appeal (2023) in the Ashchurch Rural Parish Council case ruled that
planning authorities cannot "circumvent [EIA requirements] by dividing what is in reality a
single project into separate parts." [fact; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]
The court identified three substantive tests for determining whether an apparently
separate application is in fact a fragment of a larger project: (a) whether the works
are functionally interdependent with a wider development, (b) whether they can be
"justified on their own merit" without reference to the wider scheme, and (c) whether
documentation such as a masterplan reveals that they form part of a larger whole.
[fact; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]

**Salami-slicing in requirements engineering**

In requirements engineering, salami-slicing (also termed artificial fragmentation)
refers to splitting a parent goal into sub-goals that are below approval or review
thresholds, or that individually appear manageable but collectively re-state a goal
that should have been scoped as a single unit. [inference; source: https://doi.org/10.1109/ISRE.2001.948567]
Agile and practitioner literature reviewed for this item does not use the term "salami-slicing"
consistently; the equivalent concept appears under labels such as "artificial decomposition,"
"thin vertical slicing misuse," and "scope evasion."
[inference; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]

Searched for "salami-slicing requirements engineering" in primary requirements engineering
literature (IEEE TSE, ICSRE, RE conference). The Horkoff et al. (2017) systematic mapping
is reported to cover 231 GORE publications and to characterise goal fragmentation as a
manifestation of the "abstraction gap" rather than as a distinct named anti-pattern.
[assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-gore-strategic-intent-to-delivery-decomposition.md]
The primary Springer page (https://link.springer.com/article/10.1007/s00766-017-0280-z)
was not directly accessible; this claim is drawn from the prior completed item and is
treated as an assumption pending direct verification.

**Legitimate sub-goal structure (GORE)**

In KAOS AND-refinement, a legitimate sub-goal must satisfy bidirectional logical
entailment: the conjunction of sub-goals must imply the parent goal and the parent must
imply the conjunction. [inference; source: https://doi.org/10.1109/ISRE.2001.948567]
This provides a formal boundary condition: a goal G is a legitimate AND-sub-goal of
parent P if and only if {G ∧ sibling goals} ⊨ P and P ⊨ {G ∧ sibling goals}.
[inference; source: https://doi.org/10.1109/ISRE.2001.948567]
A fragment fails this condition when there is no declared parent P against which the
entailment can be checked. [inference; source: https://doi.org/10.1109/ISRE.2001.948567]

In i-star (Strategic Dependency) models, a legitimate sub-goal has a means-end link to
its parent goal and an assigned actor within whose boundary it is performed. A goal
node with no means-end or decomposition link is structurally orphaned in the i-star
model, which is a defined incompleteness rather than a deliberate fragmentation.
[inference; source: https://doi.org/10.1109/ISRE.1997.582369]

#### §2.B: Structural signals (Cluster B)

**B1: Missing parent reference**

A goal specification that contains no traceability link to a higher-level goal is
structurally untethered. In GORE KAOS notation, a goal without a refinement link to
a parent is a root goal or an orphan; root goals are legitimate only if they constitute
the strategic objective of the entire model. [inference; source: https://doi.org/10.1109/ISRE.2001.948567]
The five-field minimum schema identified in the completed item 2026-05-31-goal-specification-completeness-schema
(https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-goal-specification-completeness-schema.md)
does not include "parent reference" as a required field in the minimum cross-schema
set, but parent reference is implied by the "scope boundary" field: a goal whose scope
boundary is defined in terms of what a parent goal achieves is dependent on that parent.
[inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-goal-specification-completeness-schema.md]
Missing parent reference is therefore a necessary but not sufficient signal for
fragmentation: it is absent in genuinely top-level goals and in fragmented goals alike.

**B2: No independent verification criterion**

A goal that cannot be verified in isolation (i.e., whose success criterion requires
another goal to be satisfied first) is structurally dependent. PDDL (Planning Domain
Definition Language) treats this as a hard error: a missing :goal block causes an
immediate parse failure. [fact; source: https://planning.wiki/ref/pddl/problem]
In KAOS and the IEEE Standard 29148 for systems and software requirements, an unverifiable goal is flagged as incomplete but processing
continues. [inference; source: https://standards.ieee.org/ieee/29148/6696/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-goal-specification-completeness-schema.md]
The testability criterion in the INVEST model (Wake 2003) operationalises this as the
question: "can we write a test for this story in isolation?" [fact; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
If the acceptance criterion contains the phrase "when [other goal] is also done" or
a conditional reference to another goal's output, the goal fails the independent
testability test. [inference; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]

**B3: Technical layer only (horizontal slicing)**

In agile product management, "horizontal slicing" is the anti-pattern of splitting a
story by technical layer (front-end, back-end, database) rather than by end-to-end
user value. Each horizontal slice is a fragment because it delivers no user-observable
outcome independently. [fact; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
Wake (2003) articulates this as the multi-layer-cake analogy: a vertical slice through
all layers gives the customer "the essence of the whole cake"; a horizontal layer
alone has "little value to the customer if there's no presentation layer."
[fact; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
Firesmith (2004) makes the same distinction for security requirements: a requirement
that specifies only one mechanism layer (e.g., encryption only, without access control)
is not a reusable security requirement because it lacks scope coherence across the
full protection surface it is supposed to cover.
[inference; source: https://www.jot.fm/issues/issue_2004_01/column6.pdf]

**B4: GORE AND-refinement entailment**

KAOS AND-refinement provides a formal structural test: if the conjunction of sub-goals
does not imply the parent, the decomposition is incomplete and the sub-goals are
potentially fragments. The completed prior item (2026-05-31-gore-strategic-intent-to-delivery-decomposition)
documents this bidirectional entailment requirement.
[inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-gore-strategic-intent-to-delivery-decomposition.md]
This test fails to distinguish salami-slicing from other forms of incomplete
decomposition (missing sub-goals, over-specification) unless the full parent goal is
declared; without a declared parent, the entailment cannot be checked.
[inference; source: https://doi.org/10.1109/ISRE.2001.948567]

#### §2.C: Semantic signals (Cluster C)

**C1: Outcome realisability in isolation**

The functional interdependence test from EIA case law is semantically equivalent to
the question "can this specification be justified on its own merit?". The Ashchurch
ruling establishes that a fragment cannot be justified on its own merit when (a) it
would not be used until the wider development is complete, and (b) documentation
reveals that the wider development depends on this fragment as an enabler.
[fact; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]
In product management terms, this is the INVEST "Valuable" criterion: "We don't care
about value to just anybody; it needs to be valuable to the customer."
[fact; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
A goal that produces no customer-observable outcome in isolation fails the Valuable
criterion and is a candidate fragment. [inference; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]

**C2: INVEST Independent and Valuable criteria**

The INVEST model (Bill Wake, 2003) provides two semantically distinct tests:
- "Independent": the goal should not overlap in concept with others and should be
  schedulable in any order without blocking or being blocked by others.
  [fact; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
- "Valuable": the goal delivers value to the customer, not just to developers.
  [fact; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
A goal that fails "Independent" (i.e., must precede or follow another specific goal)
may still be legitimate if the dependency is explicitly declared and the sequential
order is required by the domain (e.g., a database migration must precede a schema
change). Failing "Valuable" with no declaration of why is a stronger fragmentation
signal. [inference; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]

**C3: Granularity and scope coherence (Firesmith 2004)**

Firesmith (2004) argues that for security requirements to be reusable, their scope
must be coherent: each requirement must apply consistently to a well-defined scope
and must not combine unrelated goals or mix scopes within a single statement.
[inference; source: https://www.jot.fm/issues/issue_2004_01/column6.pdf]
The equivalent fragmentation signal is an "abstract pattern at the wrong level":
a goal specified at a level too abstract to be directly actionable (requiring further
decomposition before implementation) but not declared as a strategic goal. In Firesmith's
taxonomy, a goal is at the correct granularity when it can be directly traced to both
an abstract security requirement pattern and to a concrete mechanism.
[inference; source: https://www.jot.fm/issues/issue_2004_01/column6.pdf]

#### §2.D: Contextual signals (Cluster D)

**D1: Approval threshold proximity**

In procurement and programme governance, threshold proximity is documented as the
primary contextual signal for salami-slicing: multiple submissions each just below
the value or scope threshold that would trigger a higher level of scrutiny.
[fact; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]
In requirements governance, the equivalent threshold is a change approval authority
level (e.g., a team-level change authority vs. a programme board). A cluster of
change requests from the same requester, each below the authority threshold, within
a short time window constitutes a contextual fragmentation signal.
[inference; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]
This signal is contextual rather than intrinsic: it requires governance metadata
(submission timestamps, requester identity, threshold values) that is not present in
the goal specification text itself.
[inference; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]

**D2: EIA functional interdependence test**

The EIA functional interdependence test considers: (a) physical or logical contiguity
of the components, (b) common purpose or objective, (c) linked timing or phasing,
(d) shared infrastructure, (e) whether either component can function independently
and usefully, and (f) common ownership or control.
[fact; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]
Points (b), (c), and (e) translate directly to requirements governance: if two goals
share a stated strategic objective, are phased consecutively without independent value
in early phases, and neither can deliver value without the other being complete, the
functional interdependence test is met. [inference; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]

**D3: Timing clustering**

Temporal clustering of related goal submissions within a short time window is a
documented procurement signal for artificial fragmentation. The equivalent requirement
in software delivery is a cluster of "small" stories submitted in the same sprint
backlog grooming session that, when combined, reconstitute a larger feature previously
rejected as too large. [inference; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]
Reinertsen (2009) notes that scope fragmentation driven by batch-size optimisation
is economically legitimate (small batches reduce cycle time and risk), but that the
optimisation must be against an explicit parent goal to avoid creating orphaned
fragments. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]
Note: direct primary source access to Reinertsen (2009) was not obtained; the
characterisation is drawn from secondary summaries describing the batch-size trade-off
framework.

#### §2.E: Signal reliability (Cluster E)

**E1: False positives (legitimate sub-goals that exhibit fragmentation signals)**

1. Technical prerequisites: A database migration story has no direct user-observable
   outcome but is a genuine prerequisite that enables subsequent goals. It fails the
   INVEST "Valuable" criterion yet is a legitimate sub-goal when its dependency on the
   parent is declared. [inference; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
2. Infrastructure enablers: A story to provision a test environment or set up a
   Continuous Integration (CI) pipeline delivers no customer-observable output but
   is required before any delivery can be verified. Treating infrastructure enablers
   as fragments would misclassify them.
   [inference; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
3. Sequential phased delivery with declared phases: A first phase of a Minimum Viable Product (MVP) may have modest standalone value but be legitimate because
   the phasing is declared and the accumulation of value across phases is planned.
   The key distinguishing factor is whether the phasing is declared upfront.
   [inference; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
4. KAOS obstacle sub-goals: Obstacle analysis generates sub-goals specifically to
   mitigate failure modes. These are "fragments" in isolation (they address only a
   failure case) but are formally derived from the parent goal's satisfiability
   requirement. [inference; source: https://doi.org/10.1109/32.879317]

**E2: False negatives (fragmented goals that pass signals)**

1. Goals with plausible-sounding standalone acceptance criteria that are semantically
   hollow: a goal such as "user can submit form" appears testable in isolation but
   is hollow if the system discards all submissions until a downstream goal ("system
   processes submissions") is also complete. [inference; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
2. Goals that declare an undisclosed shared dependency: two goals each appear
   independent but both require an undeclared shared infrastructure component that
   neither mentions explicitly. Each passes the missing-parent-reference test (they
   are root goals by declaration) but neither can be delivered independently.
   [inference; source: https://doi.org/10.1109/ISRE.2001.948567]
3. Phased delivery with artificial phase boundaries where early phases are genuinely
   usable but the business case for the later phases was withheld to avoid disclosure
   during phase one approval. This false-negative case is not detectable from the
   specification text alone; it requires disclosure of the full expected capability.
   [assumption; no direct source; inferred from EIA case law pattern]

**E3: Formal methods encoding these signals**

1. KAOS AND-refinement completeness: the bidirectional entailment check provides a
   formal structural test that a goal is a legitimate sub-goal given a declared parent.
   No published KAOS tooling (Objectiver) explicitly implements a "fragmentation
   detector" as a named feature; the completeness check is the closest analogue.
   [inference; source: https://doi.org/10.1109/ISRE.2001.948567]
2. INVEST criteria (Wake 2003): "Independent" and "Valuable" provide documented
   semantic tests widely used in product management.
   [fact; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
3. EIA functional interdependence test: encodes contextual and semantic signals into
   a formal legal test with documented case law establishing the criteria.
   [fact; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]
4. Benefit Dependency Network (BDN) orphaned-node detection: a goal or capability
   node with no incoming dependency from a strategic objective is structurally
   orphaned; BDN methodology requires all nodes to trace to a strategic objective.
   [inference; source: https://www.axelos.com/certifications/propath/managing-successful-programmes-msp]

### §3 Reasoning

**Causal chain from fragmentation to detection failure:**
1. A goal is specified as a self-contained unit. [fact; source: https://standards.ieee.org/ieee/29148/6696/]
2. The goal lacks a traceability link to any parent goal, or its parent is withheld. [inference; source: https://doi.org/10.1109/ISRE.2001.948567]
3. The goal's acceptance criterion appears to be independently verifiable. [inference; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
4. Automated validation checks for schema completeness (five-field minimum) pass, because the fragment carries all five fields. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-goal-specification-completeness-schema.md]
5. Without contextual information about threshold proximity or temporal clustering of related submissions, the goal cannot be distinguished from a top-level goal through structural analysis alone. [inference; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]

**Key removal of narrative glue:**
- "It is important to note that" removed.
- The distinction between structural and contextual signals is not about severity;
  it is about detectability from the specification text vs. from governance metadata.
  Structural signals require only the specification; contextual signals require
  submission history and threshold data.

### §4 Consistency Check

```text
consistency_scan:
  claim_parity: checked; no contradictions between §2 sections
  false_positive_vs_signal: aligned -- every false-positive case carries a
    qualifying condition (parent declared, phasing declared) that resolves
    the ambiguity; the signal taxonomy does not claim signals are sufficient alone
  formal_method_coverage: three formal methods cite independent sources;
    BDN claim cites axelos.com which is a product page; downgraded to [inference]
  threshold_signal_scope: contextual signals confined to D-cluster and E2/E3;
    not imported into structural or semantic clusters
  invest_criteria_scope: correctly applied to goal-level signals, not task-level
  reinertsen_source: primary textbook not directly accessed; characterisation
    limited to secondary description and marked as [inference]
  firesmith_source: PDF retrieved (binary); claim confined to accessible
    abstract-level characterisation; marked as [inference]
confidence_adjustments:
  B1 missing_parent_reference: necessary but not sufficient; medium
  C1 outcome_realisability: strong semantic signal; high
  D1 threshold_proximity: requires governance metadata; medium
  E1/E2 false_positives_negatives: catalogue is not exhaustive; medium
scope_guardrail: maintained; automated detection implementation out of scope
```

### §5 Depth and Breadth Expansion

**Technical lens**

The KAOS AND-refinement entailment test is the most formally precise structural
signal available, but it requires a declared parent goal to be evaluated. In the
absence of a declared parent, the test cannot proceed. An automated system could
detect the absence of a parent reference as a prerequisite check before applying the
entailment test. [inference; source: https://doi.org/10.1109/ISRE.2001.948567]

The INVEST criteria, widely implemented in agile tooling (Jira, Linear, Azure DevOps
story templates), are the most operationally accessible semantic tests because they
are phrased as questions a non-specialist can apply. The "Valuable" and "Testable"
criteria encode the strongest fragmentation signals without requiring formal
logic competence. [inference; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]

**Legal and regulatory lens**

EIA case law provides the most formally tested contextual signal set. The Ashchurch
ruling is directly applicable beyond planning law because it articulates the
"justified on its own merit" test in terms that translate to any governance context:
replace "planning permission" with "change approval" and the test structure is the
same. The three-part test (functional interdependence, standalone justifiability,
documentary disclosure of the wider scheme) is the most defensible contextual
signal battery because it has been tested at Court of Appeal level.
[inference; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]

**Programme governance lens**

In Managing Successful Programmes (MSP), a benefit that cannot be traced to a
strategic objective on the Benefit Dependency Network is a structurally orphaned
benefit. The MSP benefit-realization discipline requires that every decomposed
benefit map to at least one strategic objective; a benefit that cannot be so mapped
is either misscoped or a fragment of a larger benefit that was not declared as such.
[inference; source: https://www.axelos.com/certifications/propath/managing-successful-programmes-msp]

**Behavioural lens**

Legitimate decomposition is typically motivated by delivery efficiency: the goal is
too large to deliver within one iteration, so it is split into independently
deliverable phases. [inference; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
Artificial fragmentation is motivated by threshold evasion: the goal would attract
scrutiny if submitted at full size. [inference; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]
The behavioural intent differs, but the outputs can appear identical in the
specification text. [inference; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications;
https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
This explains why contextual signals (threshold proximity, timing clustering, disclosure
of wider scheme) are necessary complements to structural and semantic signals.
[inference; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]

**Economic lens (Reinertsen)**

Reinertsen (2009) frames small batch size as economically optimal for reducing
cycle time and risk. [assumption; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]
The key insight for fragmentation detection is that legitimate small-batch decomposition
has an economic rationale traceable back to a parent goal: smaller batches enable faster
feedback on whether the parent goal direction is correct. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]
Artificial fragmentation has no parent goal and therefore no feedback loop; the fragments
accumulate without any mechanism to test whether the aggregate is progressing toward a
coherent outcome. [inference; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications; https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]

### §6 Synthesis

**Executive summary:**

Salami-slicing and legitimate sub-goal scoping produce similar-looking specifications
in isolation; the distinction is detectable through a three-tier signal battery.
Structural signals (missing parent reference, no independently verifiable success
criterion, technical-layer-only scope) are readable from the specification text alone
but have documented false positives: technical prerequisites and infrastructure
enablers legitimately fail the "Valuable" criterion while being necessary sub-goals.
Semantic signals (outcome non-realisable in isolation, failure of INVEST "Independent"
and "Valuable" criteria) are stronger and have fewer false positives, but require
knowledge of what the customer expects the goal to produce. Contextual signals
(approval threshold proximity, temporal clustering, absence of disclosure of the
wider scheme) are the most specific to deliberate salami-slicing but require
governance metadata not present in the goal specification itself. Three formal
methods encode these signals: KAOS AND-refinement completeness requires bidirectional
logical entailment between sub-goals and parent; INVEST criteria encode semantic
signals as testable questions; and EIA functional interdependence case law encodes
contextual signals as a three-part legal test. No single signal is sufficient; the
literature supports a combined check that requires (1) an explicit parent reference,
(2) a success criterion verifiable in isolation, and (3) at least one
customer-observable outcome delivered independently.

**Key findings:**

1. Salami-slicing is the deliberate or accidental splitting of a single coherent
   goal into multiple fragments, each below a governance or approval threshold, such
   that the aggregate intent is never visible in any single specification artefact,
   as established in EIA case law and programme governance practice.
   ([fact]; medium confidence; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications)

2. KAOS AND-refinement completeness provides the most formally precise structural
   test for legitimate sub-goal scoping: the conjunction of sub-goals must
   bidirectionally imply the parent goal, and a goal with no declared parent cannot
   pass this test, making missing parent reference a necessary precondition for
   fragmentation detection.
   ([inference]; high confidence; source: https://doi.org/10.1109/ISRE.2001.948567;
   https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-gore-strategic-intent-to-delivery-decomposition.md)

3. The INVEST criteria (Wake, 2003) encode the two strongest semantic fragmentation
   signals as questions applicable without formal logic competence: the "Valuable"
   criterion (does this goal deliver value to the customer in isolation?) and the
   "Testable" criterion (can acceptance be determined without completing another goal?).
   ([inference]; high confidence; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/;
   https://www.agilealliance.org/glossary/invest/)

4. The UK Court of Appeal (2023) Ashchurch ruling establishes a three-part
   functional interdependence test for detecting artificial project splitting that
   translates directly to requirements governance: a goal is a fragment if it cannot
   be justified on its own merit, if documentation reveals it forms part of a wider
   scheme, and if it would not be used until the wider scheme is complete.
   ([fact]; medium confidence; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications)

5. Technical prerequisites (e.g., database migrations, CI pipeline setup) and
   infrastructure enablers are the primary false positive class for fragmentation
   signals: they fail the INVEST "Valuable" criterion yet are legitimate sub-goals
   when the dependency on a declared parent goal is explicitly stated.
   ([inference]; medium confidence; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/)

6. A goal with an acceptance criterion conditional on another goal's completion (e.g.,
   "when system also processes submissions") fails the independent testability test and
   is a semantic fragmentation signal; in Planning Domain Definition Language (PDDL),
   such a dependency creates a mutual precondition chain that may render the goal
   set unsolvable at plan-search time.
   ([inference]; medium confidence; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/;
   https://planning.wiki/ref/pddl/problem)

7. Horizontal slicing (splitting a goal by technical layer rather than by
   end-to-end user value) is a documented fragmentation anti-pattern in agile product
   management; a goal scoped entirely within one technical layer delivers no
   customer-observable outcome and therefore fails both the "Valuable" INVEST criterion
   and the EIA standalone justifiability test.
   ([inference]; medium confidence; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/)

8. Contextual signals (approval threshold proximity, temporal clustering of related
   fragment submissions, absence of disclosure of the wider scheme) are the most
   specific indicators of deliberate salami-slicing but require governance metadata
   that is not present in the goal specification text, making them impossible to
   evaluate from specification content alone.
   ([inference]; medium confidence; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications)

9. The Benefit Dependency Network (BDN) methodology in Managing Successful Programmes
   (MSP) encodes a structural fragmentation signal through the orphaned-node concept:
   a benefit or capability node with no traceability path to a strategic objective is
   structurally fragmented and must be either re-linked or retired.
   ([inference]; medium confidence; source: https://www.axelos.com/certifications/propath/managing-successful-programmes-msp)

10. No single structural, semantic, or contextual signal is sufficient to determine
    fragmentation; the literature across requirements engineering, product management,
    programme governance, and EIA case law consistently supports a combined check
    requiring at minimum: (a) an explicit parent reference, (b) a success criterion
    verifiable in isolation, and (c) at least one customer-observable outcome delivered
    independently without requiring other goals to be completed.
    ([inference]; medium confidence; source: https://doi.org/10.1109/ISRE.2001.948567;
    https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/;
    https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Salami-slicing as goal splitting below approval threshold | https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications | medium | Court of Appeal 2023 via Pinsent Masons commentary; primary ruling not directly accessible |
| [inference] KAOS AND-refinement: missing parent reference as fragmentation precondition | https://doi.org/10.1109/ISRE.2001.948567; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-gore-strategic-intent-to-delivery-decomposition.md | high | Van Lamsweerde (2001); prior completed item |
| [inference] INVEST "Valuable" and "Testable" as strongest semantic fragmentation signals | https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/; https://www.agilealliance.org/glossary/invest/ | high | Wake (2003) original; Agile Alliance; evaluative ranking |
| [fact] EIA three-part functional interdependence test (Ashchurch 2023) | https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications | medium | Court of Appeal 2023 via Pinsent Masons commentary; single source |
| [inference] Technical prerequisites as primary false positive | https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/ | medium | Inferred from INVEST "Valuable" discussion |
| [inference] Conditional acceptance criterion as semantic fragmentation signal | https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/; https://planning.wiki/ref/pddl/problem | medium | INVEST testability + PDDL mutual precondition |
| [inference] Horizontal slicing as documented fragmentation anti-pattern | https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/ | medium | Wake (2003) single practitioner source |
| [inference] Contextual signals require governance metadata, not specification text | https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications | medium | EIA signals; procurement context |
| [inference] BDN orphaned node as structural fragmentation signal | https://www.axelos.com/certifications/propath/managing-successful-programmes-msp | medium | MSP product page; no detailed content accessible |
| [inference] Combined three-check minimum for fragmentation determination | https://doi.org/10.1109/ISRE.2001.948567; https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/; https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications | medium | Cross-domain inference |

**Assumptions:**

1. The EIA functional interdependence test is applicable to requirements governance
   beyond its planning law origin. **Justification:** The logical structure of the test
   (can this artefact be justified on its own merit? does documentation reveal it is
   part of a larger scheme?) is domain-agnostic; it has been applied to procurement,
   infrastructure projects, and technology platform decisions in legal commentary.
   [assumption; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]
2. INVEST criteria, designed for user stories in agile delivery, are applicable at the
   level of Goal specifications as used in this research item's scope. **Justification:**
   The INVEST "Valuable" and "Testable" criteria address the semantic properties of any
   well-formed goal specification regardless of delivery methodology; the criteria are
   framed in terms of outcomes to customers, not in terms of sprint mechanics.
   [assumption; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
3. Reinertsen (2009) does connect legitimate batch-size reduction to parent-goal
   traceability. **Justification:** This claim is drawn from secondary descriptions of
   the book; direct access was not obtained. The characterisation is consistent with
   the documented batch-size optimisation principle but is treated as [inference] only.
   [assumption; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

**Analysis:**

The three signal tiers (structural, semantic, contextual) form a detection ladder.
[inference; source: https://doi.org/10.1109/ISRE.2001.948567; https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/;
https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]
Structural signals are the cheapest to evaluate because they require only the
specification text, but they have the highest false-positive rate: legitimate
prerequisite goals and infrastructure enablers routinely fail the "missing parent
reference" and "Valuable" tests. [inference; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
Semantic signals require understanding of what a customer expects from the goal in
isolation; they are more expensive to evaluate but have fewer false positives because
the "Valuable" test is explicitly about customer-observable outcomes rather than
implementation structure. [inference; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
Contextual signals are the most specific to deliberate salami-slicing, but they
require governance metadata (submission history, threshold values, requester identity)
that is not present in the specification itself; they therefore cannot be applied
by an automated system that analyses specifications in isolation.
[inference; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]

A rival interpretation is that structural signals alone are sufficient if the KAOS
AND-refinement entailment test is applied: a fragment by definition lacks a declared
parent, and without a parent the entailment cannot be checked, which is itself a
conclusive signal. [inference; source: https://doi.org/10.1109/ISRE.2001.948567]
The structural interpretation is weaker than it appears for two reasons. First,
a legitimate root goal also lacks a parent; the signal is not specific to fragments.
Second, a sophisticated agent submitting fragmented goals can declare a fictitious
parent goal, satisfying the structural check while preserving the fragmentation
effect at the semantic level. [inference; source: https://doi.org/10.1109/ISRE.2001.948567;
https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
For these reasons, the semantic layer (outcome realisability in isolation) is the
most robust primary signal; structural and contextual signals are necessary as
supporting evidence rather than as stand-alone tests.
[inference; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/;
https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]

The GORE completed item (2026-05-31-gore-strategic-intent-to-delivery-decomposition)
establishes that the abstraction gap (the point where GORE rules run out) occurs in
roughly 40-60% of industrial GORE applications. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-gore-strategic-intent-to-delivery-decomposition.md]
This has a direct implication for fragmentation detection: the abstraction gap is a
zone where legitimately scoped goals and fragments are indistinguishable without
domain expertise, because GORE rules do not supply operationalisation criteria at
that boundary. The semantic signals (INVEST, EIA) are therefore most valuable
precisely at the abstraction boundary where formal GORE checks stop working.
[inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-gore-strategic-intent-to-delivery-decomposition.md;
https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]

**Risks, gaps, uncertainties:**

- The Horkoff et al. (2017) systematic mapping of 231 GORE publications was not
  directly accessed; its content is drawn from the completed prior item
  2026-05-31-gore-strategic-intent-to-delivery-decomposition.
- Primary access to Reinertsen (2009) was not obtained; the batch-size/parent-goal
  traceability claim is characterised from secondary summaries and marked as [inference].
- The Firesmith (2004) Journal of Object Technology article was retrieved as a binary
  PDF; its contents are characterised from an abstract-level description via search
  results and are marked as [inference].
- The AXELOS MSP source cited (axelos.com product page) was inaccessible in useful
  content; the BDN orphaned-node claim is based on secondary characterisation and
  marked as [inference] at medium confidence.
- The false-negative and false-positive catalogue is not exhaustive; it covers the
  most commonly documented cases across the four source domains.
- No empirical study was found that directly measures the false-positive and
  false-negative rates of the proposed signal taxonomy on a labelled dataset of
  goal specifications; this is an open research gap.

**Open questions:**

1. Can the combined three-check minimum (parent reference, independent success
   criterion, customer-observable outcome) be encoded as a formal schema validation
   rule that an automated planner can apply at goal submission time?
2. Is there empirical evidence of false-negative rates for semantic signals in
   industrial requirements databases?
3. Can the EIA functional interdependence test be operationalised as a machine-readable
   check without requiring natural language understanding of the "wider scheme"?

### §7 Recursive Review

```text
review_result: pass
acronym_audit:
  GORE: expanded on first use in §0 Initialise -- "Goal-Oriented Requirements Engineering (GORE)"
  KAOS: expanded on first use in §0 Initialise -- "Knowledge Acquisition in Automated Specification (KAOS)"
  EIA: expanded on first use in §0 Initialise -- "Environmental Impact Assessment (EIA)"
  INVEST: expanded on first use in §0 Initialise -- "Independent, Negotiable, Valuable, Estimable, Small, Testable"
  BDN: expanded on first use in §0 Initialise -- "Benefit Dependency Network (BDN)"
  NFR: expanded on first use in §0 Initialise -- "Non-Functional Requirements (NFR) Framework"
  MSP: expanded on first use in §5 -- "Managing Successful Programmes (MSP)"
  CI: expanded on first use in §2.E -- "Continuous Integration (CI)"
  PDDL: expanded on first use in §2.C -- "Planning Domain Definition Language (PDDL)"
  MVP: expanded on first use in §2.E -- "Minimum Viable Product (MVP)"
domain_term_audit:
  salami-slicing: defined in §0
  legitimate sub-goal: defined in §0
  horizontal slicing: defined at first use in §2.B3
  abstraction gap: referenced from prior item; term used in prior item context only
  functional interdependence: defined at first use in §2.D2 by EIA test criteria
claim_labels: all factual and inferential claims carry [fact] or [inference] labels in §2
false_positive_catalogue: covered in §2.E1 with four distinct classes
false_negative_catalogue: covered in §2.E2 with three distinct classes
source_access: Horkoff 2017 Springer blocked; Reinertsen 2009 secondary only;
  Firesmith 2004 binary PDF; AXELOS page inaccessible -- all noted in Risks/Gaps
em_dash_check: none present
ai_slop_check: no "Furthermore", "Additionally", "It is important to note" present
vague_quantifier_check: no unsourced "many", "most", "significant" present
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Salami-slicing (artificial goal fragmentation to evade approval thresholds) and
legitimate sub-goal scoping produce identical-looking specifications in isolation;
the distinction is detectable through a three-tier signal battery: structural, semantic,
and contextual. [inference; source: https://doi.org/10.1109/ISRE.2001.948567; https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/; https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]
The strongest single signal is semantic: a goal that cannot deliver a customer-observable
outcome in isolation fails the INVEST "Valuable" criterion and the EIA standalone
justifiability test, regardless of whether its specification text is structurally complete.
[inference; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/; https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]
Technical prerequisites and infrastructure enablers are the main false positive class:
they fail the "Valuable" criterion yet are legitimate sub-goals when the dependency on
a declared parent is explicitly stated. [inference; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
A reliable minimum check requires at least three conditions to be satisfied simultaneously:
(a) the goal carries an explicit parent reference, (b) its success criterion is verifiable
in isolation, and (c) it delivers at least one customer-observable outcome without requiring
other goals to be completed first. [inference; source: https://doi.org/10.1109/ISRE.2001.948567; https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/; https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]

### Key Findings

1. **Salami-slicing** is the splitting of a single coherent goal into multiple fragments, each below a governance or approval threshold, such that the aggregate intent is never visible in any single specification artefact, as established in Environmental Impact Assessment (EIA) case law and programme governance practice. ([fact]; medium confidence; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications)

2. **KAOS AND-refinement completeness** provides the most formally precise structural signal for legitimate sub-goal scoping: the conjunction of sub-goals must bidirectionally imply the parent goal, and a goal with no declared parent cannot pass this test, making absent parent reference a necessary precondition for applying any fragmentation check. ([inference]; high confidence; source: https://doi.org/10.1109/ISRE.2001.948567; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-gore-strategic-intent-to-delivery-decomposition.md)

3. **INVEST criteria** (Wake, 2003) encode the two strongest semantic fragmentation signals as questions usable without formal logic competence: "Valuable" asks whether the goal delivers customer value in isolation, and "Testable" asks whether acceptance can be determined without completing another goal first. ([inference]; high confidence; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/; https://www.agilealliance.org/glossary/invest/)

4. **Ashchurch three-part test:** the UK Court of Appeal (2023) establishes a functional interdependence test for detecting artificial project splitting: a goal is a fragment if it cannot be justified on its own merit, if documentation reveals it forms part of a wider scheme, and if it would not be used until the wider scheme is complete. ([fact]; medium confidence; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications)

5. **Technical prerequisites** and infrastructure enablers are the primary false positive class for fragmentation signals: they fail the INVEST "Valuable" criterion yet are legitimate sub-goals when the dependency on a declared parent goal is explicitly stated in the specification. ([inference]; medium confidence; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/)

6. **Conditional acceptance criterion:** a goal whose acceptance depends on another goal's completion fails the independent testability test and is a semantic fragmentation signal; in Planning Domain Definition Language (PDDL), such a mutual precondition chain may render the entire goal set unsolvable at plan-search time, making the fragmentation computationally detectable. ([inference]; medium confidence; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/; https://planning.wiki/ref/pddl/problem)

7. **Horizontal slicing** (scoping a goal entirely within one technical layer without delivering an end-to-end customer-observable outcome) is a documented anti-pattern in agile product management that fails both the INVEST "Valuable" criterion and the EIA standalone justifiability test. ([inference]; medium confidence; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/)

8. **Contextual signals** (approval threshold proximity, temporal clustering of related fragment submissions, absence of disclosure of the wider scheme) are the most specific indicators of deliberate salami-slicing but require governance metadata absent from the goal specification text and cannot be evaluated from specification content alone. ([inference]; medium confidence; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications)

9. **Benefit Dependency Network (BDN)** orphaned-node concept in Managing Successful Programmes (MSP) encodes a structural fragmentation signal: any benefit or capability node with no traceability path to a strategic objective is structurally fragmented and must be re-linked or retired. ([inference]; medium confidence; source: https://www.axelos.com/certifications/propath/managing-successful-programmes-msp)

10. No single structural, semantic, or contextual signal is sufficient to determine fragmentation; the literature across requirements engineering, product management, programme governance, and EIA case law consistently supports a combined minimum check requiring an explicit parent reference, an independently verifiable success criterion, and at least one customer-observable outcome delivered without requiring other goals to be completed. ([inference]; medium confidence; source: https://doi.org/10.1109/ISRE.2001.948567; https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/; https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Salami-slicing as below-threshold goal splitting | https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications | medium | Court of Appeal 2023 via Pinsent Masons commentary; single source |
| [inference] KAOS AND-refinement: missing parent reference as fragmentation precondition | https://doi.org/10.1109/ISRE.2001.948567; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-gore-strategic-intent-to-delivery-decomposition.md | high | Van Lamsweerde (2001); prior completed item |
| [inference] INVEST "Valuable" and "Testable" as strongest semantic fragmentation signals | https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/; https://www.agilealliance.org/glossary/invest/ | high | Wake (2003) original; Agile Alliance; evaluative ranking |
| [fact] EIA three-part functional interdependence test (Ashchurch 2023) | https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications | medium | Court of Appeal 2023 via Pinsent Masons; single source |
| [inference] Technical prerequisites as primary false positive | https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/ | medium | Inferred from INVEST "Valuable" discussion |
| [inference] Conditional acceptance criterion as semantic fragmentation signal | https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/; https://planning.wiki/ref/pddl/problem | medium | INVEST testability + Planning Domain Definition Language (PDDL) precondition |
| [inference] Horizontal slicing as documented fragmentation anti-pattern | https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/ | medium | Wake (2003) single practitioner source |
| [inference] Contextual signals require governance metadata | https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications | medium | EIA procurement context |
| [inference] Benefit Dependency Network orphaned node as structural signal | https://www.axelos.com/certifications/propath/managing-successful-programmes-msp | medium | MSP product page; characterised from secondary description |
| [inference] Combined three-check minimum | https://doi.org/10.1109/ISRE.2001.948567; https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/; https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications | medium | Cross-domain synthesis |

### Assumptions

- **Assumption 1:** The EIA functional interdependence test is applicable to requirements governance beyond planning law. **Justification:** The logical structure of the test is domain-agnostic; its criteria (can this artefact be justified on its own merit? does documentation reveal it is part of a larger scheme?) apply wherever a governance threshold exists. [assumption; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]

- **Assumption 2:** The INVEST criteria, designed for agile user stories, are applicable at the level of Goal specifications as used in this item's scope. **Justification:** The "Valuable" and "Testable" criteria address the semantic properties of any well-formed goal specification regardless of delivery methodology. [assumption; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]

- **Assumption 3:** Reinertsen (2009) connects legitimate batch-size reduction to parent-goal traceability. **Justification:** This claim is drawn from secondary summaries; primary access was not obtained. It is consistent with the documented batch-size optimisation principle but is treated as an assumption pending direct source verification. [assumption; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

### Analysis

The three signal tiers form a detection ladder in which each tier catches a different
fragmentation mechanism. [inference; source: https://doi.org/10.1109/ISRE.2001.948567; https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/; https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]
Structural signals cost the least to evaluate but carry the highest false-positive
rate because legitimate prerequisites and infrastructure goals routinely lack
standalone value. [inference; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
The semantic tier is more discriminating because the "Valuable" test is explicitly
about customer-observable outcomes rather than implementation structure, which is
harder to fake without revealing the wider scheme. [inference; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
Governance metadata unlocks the contextual tier, which is the most specific to
deliberate intent but cannot be evaluated from specification content alone, making
it complementary rather than primary. [inference; source: https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]

A rival interpretation is that structural signals alone are sufficient: a goal without
a declared parent cannot pass the KAOS AND-refinement entailment check, which is itself
conclusive. [inference; source: https://doi.org/10.1109/ISRE.2001.948567]
The structural interpretation is weaker for two reasons: (a) a legitimate root goal
also lacks a parent, so the signal is not specific to fragments; and (b) a declared
but fictitious parent can be added to a fragmented goal, satisfying the structural
check while preserving the fragmentation effect at the semantic level.
[inference; source: https://doi.org/10.1109/ISRE.2001.948567; https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]
Semantic signals are therefore the most robust primary layer; structural and
contextual signals serve as supporting evidence. [inference; source: https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/; https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]

The GORE completed item (2026-05-31-gore-strategic-intent-to-delivery-decomposition)
establishes that the abstraction gap in GORE decomposition occurs in roughly 40-60%
of industrial applications. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-gore-strategic-intent-to-delivery-decomposition.md]
This finding sharpens the current item's conclusion: at the abstraction boundary,
GORE formal rules stop providing guidance, making semantic signals (INVEST, EIA)
particularly valuable as the primary detection layer precisely where formal checks
break down. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-gore-strategic-intent-to-delivery-decomposition.md; https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/]

### Risks, Gaps, and Uncertainties

- The Horkoff et al. (2017) systematic mapping was not directly accessed; its content
  is drawn from the completed prior item on GORE decomposition.
- Primary access to Reinertsen (2009) was not obtained; the batch-size/parent-goal
  traceability characterisation is from secondary summaries.
- The Firesmith (2004) article was retrieved as a binary PDF only; scope-coherence
  claims are characterised from abstract-level search results.
- The AXELOS MSP source was inaccessible in useful content; the BDN orphaned-node
  claim is based on secondary characterisation.
- No empirical study was found measuring false-positive and false-negative rates of the
  proposed signal taxonomy on a labelled dataset of goal specifications.

### Open Questions

1. Can the combined three-check minimum be encoded as a formal schema validation rule
   that an automated planner can apply at goal submission time? This would be a natural
   extension of the five-field minimum schema from the completed item
   2026-05-31-goal-specification-completeness-schema.
2. Is there empirical evidence on false-negative rates for semantic signals in industrial
   requirements databases?
3. Can the EIA functional interdependence test be operationalised as a machine-readable
   check without requiring natural language understanding of the "wider scheme"?

---

## Output

- Type: knowledge
- Description: Signal taxonomy distinguishing salami-sliced goal fragments from legitimately scoped sub-goals, organised into three tiers (structural, semantic, contextual) with false-positive and false-negative catalogues. [inference; source: https://doi.org/10.1109/ISRE.2001.948567; https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/; https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications]
- Links:
  - https://doi.org/10.1109/ISRE.2001.948567 (Van Lamsweerde 2001 KAOS AND-refinement)
  - https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/ (Wake 2003 INVEST criteria)
  - https://www.pinsentmasons.com/out-law/news/bridge-ruling-warning-english-planning-applications (Ashchurch EIA ruling 2023)
