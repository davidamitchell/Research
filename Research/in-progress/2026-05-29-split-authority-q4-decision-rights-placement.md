---
title: "Q4: Decision rights that should move closer to execution"
added: 2026-05-29
status: reviewing
priority: high
tags: [decision-rights, delegation, governance, execution]
blocks: [2026-05-29-split-authority-q1-flow-constraint]
started: 2026-05-31T10:45:25+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-05-29-split-authority-p1-operating-model-synthesis
  - 2026-05-23-governance-controls-effectiveness-conditions
  - 2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance
  - 2026-05-29-split-authority-q2-demand-segmentation
  - 2026-05-29-split-authority-q3-routing-exception-isolation
related:
  - 2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention
  - 2026-05-23-funding-authority-delivery-capability-risk-accountability-split
  - 2026-04-01-backpressure-theory-of-constraints
supersedes: ~
superseded_by: []
item_type: primary
confidence: medium
themes:
  - governance-policy
  - organisational-design
  - cost-performance
  - enterprise-adoption
  - software-engineering
gaps: []
versions: []
---

# Q4: Decision rights that should move closer to execution

## Research Question

Which decisions about sequencing, scope, reliability, technical debt, local spend, and incident response must sit with delivery teams to reduce delay without losing control?

## Scope

**In scope:**
- Delegation boundaries for high-frequency execution decisions.
- Trade-offs between local autonomy and central control consistency.

**Out of scope:**
- Full operating-model synthesis before other dependency items complete.

**Constraints:**
- Build on Q1 evidence about where delay and instability originate.

## Context

Q4 isolates the split-authority placement problem: which decision rights must move nearer execution to reduce queueing delay while preserving governance outcomes. It enables Q5 and P1. A split-authority delivery environment is one in which authority is divided among at least two stakeholder groups with independent veto or approval power, typically a business owner, a technology delivery team, and an independent risk or compliance function. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

The P1 synthesis established that fragmented decision rights and approval gates generate work-in-progress (WIP) accumulation, that WIP accumulation extends lead time by Little's Law, and that extending lead time reduces predictability and throughput. Q4 investigates which specific decision categories must move to delivery teams to break this causal chain, and what guardrails make that delegation safe. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html]

## Approach

1. Map decision categories by frequency, reversibility, and risk.
2. Evaluate centralised vs delegated placement outcomes.
3. Propose a bounded delegation map with escalation triggers.

## Sources

- [x] [DORA (2024) Loosely Coupled Teams Capability](https://dora.dev/capabilities/loosely-coupled-teams/) -- empirical research on team autonomy and delivery performance
- [x] [DORA (2024) DORA Metrics and Four Keys](https://dora.dev/guides/dora-metrics-four-keys/) -- change lead time, deployment frequency, and change failure rate
- [x] [Skelton and Pais (2019) Team Topologies Key Concepts](https://teamtopologies.com/key-concepts) -- stream-aligned teams, cognitive load limits, and inter-team interaction modes
- [x] [Bain and Company (2022) RAPID Decision Making](https://www.bain.com/insights/rapid-decision-making/) -- Recommend, Agree, Perform, Input, and Decide framework role definitions
- [x] [Bain and Company (2011) Decisions: Who Does What?](https://www.bain.com/insights/decisions-who-does-what/) -- single decision owner, decision placement close to implementation
- [x] [Massachusetts Institute of Technology Center for Information Systems Research (MIT CISR) (n.d.) Classic Topics: Decision Rights](https://cisr.mit.edu/content/classic-topics-decision-rights) -- governance as allocation of decision rights and accountabilities
- [x] [MIT CISR (2023) Simplifying Decision Rights for Growth](https://cisr.mit.edu/content/simplifying-decision-rights-growth) -- what vs. how decisions, investment prioritisation, exception handling
- [x] [Google SRE (2018) Workbook: Incident Response](https://sre.google/workbook/incident-response/) -- Incident Command System (ICS) authority structure during live incidents
- [x] [Google SRE (2016) Site Reliability Engineering: Being On-Call](https://sre.google/sre-book/being-on-call/) -- on-call decision authority, escalation tiers, response-time constraints
- [x] [Google SRE (2018) Workbook: Eliminating Toil](https://sre.google/workbook/eliminating-toil/) -- toil characteristics and the operational cost of repetitive manual decisions
- [x] [Google SRE (2016) Site Reliability Engineering: Embracing Risk](https://sre.google/sre-book/embracing-risk/) -- risk continuum and cost-benefit trade-offs in reliability decisions
- [x] [Amazon Web Services (AWS) (2025) Empower Your Teams with Modern Architecture Governance](https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/) -- preapproved blueprints, distributed governance, automated controls
- [x] [Mitchell (2026) Operating Model Synthesis for Split-Authority Delivery Systems](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html) -- five design principles including bounded delegation
- [x] [Mitchell (2026) Q2: Demand Segmentation for Fast-Path vs Controlled-Path Flow](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html) -- three demand classes and boundary tests this item builds on
- [x] [Mitchell (2026) Q3: Routing Design that Isolates Exceptions from Routine Flow](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html) -- physical lane separation and escalation thresholds
- [x] [Mitchell (2026) Governance Designs where Explicit Integrator Rights Substitute for Co-location](https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html) -- integrator authority bundle and boundary conditions
- [x] [Mitchell (2026) Internal Governance Controls: Effectiveness Conditions in Regulated Enterprises](https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html) -- control proportionality to transaction hazard
- [x] [Adler and Borys (1996) Two Types of Bureaucracy: Enabling and Coercive](https://eric.ed.gov/?id=EJ525938) -- enabling vs. coercive formalisation and team behavioural responses
- [x] [Basel Committee on Banking Supervision (BCBS) (2015) Corporate Governance Principles for Banks](https://www.bis.org/bcbs/publ/d328.pdf) -- independent risk challenge and second-line-of-defence role
- [x] [Williamson (1991) Comparative Economic Organization, working paper version](https://ageconsearch.umn.edu/record/294665/files/ipr018.pdf) -- transaction cost economics and governance choice

---

## Research Skill Output

### §0 Initialise

Question: Which decisions about sequencing, scope, reliability, technical debt, local spend, and incident response must sit with delivery teams to reduce delay without losing control?

A split-authority delivery environment is one in which authority is divided among at least two stakeholder groups with independent veto or approval power. The P1 synthesis established that governance-generated queueing (approval latency, multi-party coordination, fragmented decision rights) is the dominant flow constraint in such systems, and proposed bounded delegation as the primary remedy. Q2 established a three-class demand segmentation. Q3 established physical lane separation and escalation thresholds. Q4 asks which specific decision categories belong in each delegation tier, and what guardrails make that delegation safe.

Scope: In scope are the six decision types named in the Research Question (sequencing, scope, reliability, technical debt, local spend, incident response), the criteria that determine their appropriate delegation tier, and the guardrail and escalation designs that preserve governance outcomes. Out of scope is the full operating-model synthesis (P1) and the control model trade-off selection between pre-approval, bounded delegation, and post-hoc review (Q5).

Constraints:
- Claims labelled [fact] require a URL-backed source.
- Claims labelled [inference] are derived from evidence; a source is required.
- Claims labelled [assumption] are not verified; justification and a nearest URL-backed source are required.
- Output format: structured synthesis with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks, Open Questions, and Output section.

### §1 Question Decomposition

The research question decomposes into three atomic question groups:

**A. Decision taxonomy: how do the six decision types differ in frequency, reversibility, and blast radius?**
- A1. What is the frequency and reversibility of daily task sequencing?
- A2. What is the frequency and reversibility of sprint-level scope adjustment?
- A3. What is the frequency and reversibility of reliability decisions (Service Level Objective (SLO) trade-offs, rollback authority)?
- A4. What is the frequency and reversibility of technical debt prioritisation within a capacity band?
- A5. What is the frequency and reversibility of local environment spend (development, test tooling, minor infrastructure)?
- A6. What is the frequency and reversibility of incident response decisions (escalation, rollback, disable, reroute)?

**B. Evidence for delegation outcomes: what happens when each decision type is centralised vs. delegated?**
- B1. What does DevOps Research and Assessment (DORA) evidence show about team autonomy and delivery performance?
- B2. What does the Incident Command System (ICS) model show about incident decision authority?
- B3. What does the Bain Recommend, Agree, Perform, Input, and Decide (RAPID) framework say about placement of the Decide role?
- B4. What does MIT CISR research say about the what-vs-how distinction in decision rights?
- B5. What does the Amazon Web Services (AWS) distributed governance model show about preapproved blueprints as a substitute for per-decision approval?

**C. Bounded delegation design: what guardrails preserve governance outcomes without requiring per-decision approval?**
- C1. What parameters define a bounded delegation boundary (budget ceiling, blast radius limit, approved technology catalog)?
- C2. What are the escalation triggers that bring a decision back to the central approval path?
- C3. How does Site Reliability Engineering (SRE) on-call authority demonstrate bounded delegation in practice?

### §2 Investigation

#### §2.A Decision taxonomy

**A1. Daily task sequencing**

The order in which work items within an approved sprint or iteration are processed is revised multiple times per day, imposes no cost on the system when changed, and is immediately reversible at zero overhead. No external party is affected by the sequence chosen; the only consequence is the delivery team's internal productivity. [inference; source: https://teamtopologies.com/key-concepts; https://dora.dev/capabilities/loosely-coupled-teams/]

Centralising daily sequencing forces delivery teams to queue decisions that have no governance value, producing approval latency for a category with zero blast radius. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html; https://www.bain.com/insights/decisions-who-does-what/]

**A2. Sprint-level scope adjustment**

Minor scope adjustments (swapping one backlog item for another within the same priority band, deferring a low-priority item to the next iteration) occur at sprint cadence (typically one to two weeks), carry bounded consequence (the item is deferred, not lost), and are reversible in the next planning cycle. [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://teamtopologies.com/key-concepts]

Major scope adjustments (changing a release commitment, removing a feature that was promised to an external stakeholder, or expanding scope beyond approved capacity) have higher blast radius and external dependency and require a different delegation tier. The distinction between minor and major scope adjustment is therefore an escalation trigger, not a binary rule. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://www.bain.com/insights/rapid-decision-making/]

**A3. Reliability decisions**

SLOs and error budget decisions involve balancing feature delivery velocity against reliability investment. Google SRE frames this as a risk continuum where the acceptable level of unplanned downtime is set explicitly rather than maximised: a team targets 99.99% availability (not 100%) to preserve capacity for new feature delivery. [fact; source: https://sre.google/sre-book/embracing-risk/]

Decisions within an already-approved SLO (deploying during an approved change window, performing a canary rollout with automated rollback, adjusting alert thresholds within policy) are high-frequency, bounded, and reversible. They belong with the delivery team. Decisions that change the SLO itself, or that accept a reliability trade-off with external customer impact, require escalation. [inference; source: https://sre.google/sre-book/embracing-risk/; https://sre.google/sre-book/being-on-call/]

**A4. Technical debt prioritisation within a capacity band**

Technical debt accumulates at a compounding rate when deferred: unaddressed debt increases the cost of all subsequent work by raising cognitive overhead, reducing automated test coverage, and increasing incident probability. [inference; source: https://sre.google/workbook/eliminating-toil/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html]

Decisions about which technical debt items to address within a pre-authorised capacity band (for example, up to 20% of sprint velocity) are high-frequency within their cycle, bounded in scope, and carry no external commitment implications. Requiring central pre-approval for these decisions produces approval latency at precisely the point where fast execution reduces future risk. [inference; source: https://sre.google/workbook/eliminating-toil/; https://dora.dev/capabilities/loosely-coupled-teams/]

Technical debt work that exceeds the pre-authorised band, or that requires architectural changes outside the approved technology catalog, requires escalation. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/]

**A5. Local environment spend**

Development and test environment spend (spinning up ephemeral test environments, acquiring minor tooling within an approved vendor list, extending cloud resource allocation within a monthly budget ceiling) is high-frequency, bounded in cost, and reversible (environments can be decommissioned, tooling can be removed). [inference; source: https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/; https://dora.dev/capabilities/loosely-coupled-teams/]

Centralising approval for environment spend below a defined budget ceiling produces approval queue latency with no proportionate risk-reduction value, because the cost ceiling already bounds the downside. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

Spend that exceeds the defined ceiling, involves a vendor not on the approved list, or creates a persistent rather than ephemeral infrastructure commitment requires escalation. [inference; source: https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/; https://www.bain.com/insights/rapid-decision-making/]

**A6. Incident response decisions**

During a live service incident, the window for effective mitigation is measured in minutes. Response times of five minutes are required for user-facing services targeting four nines of availability (99.99%). [fact; source: https://sre.google/sre-book/being-on-call/]

External approval during an active incident is structurally incompatible with these response-time requirements: the approval latency alone would consume a material fraction of the quarterly downtime budget. SRE incident management therefore places all live-incident authority with a single named Incident Commander (IC), who coordinates response, delegates to an Operations Lead (OL) and Communications Lead (CL), and escalates to senior IC only when the incident scope exceeds predefined bounds. [fact; source: https://sre.google/workbook/incident-response/; https://sre.google/sre-book/being-on-call/]

The ICS model represents the most extreme case of bounded delegation: during an incident, the IC has autonomous authority within the incident scope; external parties are informed rather than consulted. This is governance operating correctly at the right level of the hierarchy, not a governance gap. [inference; source: https://sre.google/workbook/incident-response/; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

#### §2.B Evidence for delegation outcomes

**B1. DORA evidence on team autonomy and delivery performance**

DORA research identifies loosely coupled teams as a capability that predicts higher software delivery performance. The specific characteristics are: teams can make large-scale changes to system design without permission from outside the team; teams can complete work without fine-grained communication with parties outside the team; teams deploy independently of services they depend on or services that depend on them. [fact; source: https://dora.dev/capabilities/loosely-coupled-teams/]

DORA's five software delivery performance metrics (change lead time, deployment frequency, failed deployment recovery time, change failure rate, and deployment rework rate) show that top performers achieve high throughput and high stability simultaneously. [fact; source: https://dora.dev/guides/dora-metrics-four-keys/] The implication is that team autonomy over execution decisions is positively correlated with delivery performance, not inversely correlated as a central-control model would predict. [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://dora.dev/guides/dora-metrics-four-keys/]

**B2. Incident Command System evidence**

ICS was established in 1968 by firefighters as a way to manage high-stakes, time-critical situations. The framework's core design is: a single named commander holds authority; roles are clearly defined before the event; communication is structured; and command can be handed off, but the handoff is explicit. Google SRE adopted this framework for production incidents. [fact; source: https://sre.google/workbook/incident-response/]

The ICS model demonstrates that delegating authority to an on-the-ground decision-maker is compatible with disciplined governance, provided the authority boundary is pre-defined (incident scope), the reporting structure is clear (IC reports status to stakeholders), and escalation triggers are explicit (incident scale exceeds IC authority; external customer impact requires executive notification). [inference; source: https://sre.google/workbook/incident-response/; https://sre.google/sre-book/being-on-call/]

**B3. RAPID framework evidence**

Bain's RAPID framework defines five roles: Recommend (R), Agree (A), Perform (P), Input (I), and Decide (D). The Decide role is described as holding "primary accountability for the outcome" and sitting "as close to where the decision will be implemented as possible." [fact; source: https://www.bain.com/insights/rapid-decision-making/]

The Agree role is used sparingly: it is reserved for parties who must sign off for legal or regulatory compliance reasons. Broad use of the Agree role increases decision latency without improving decision quality. [fact; source: https://www.bain.com/insights/rapid-decision-making/; https://www.bain.com/insights/decisions-who-does-what/]

**B4. MIT CISR what-vs-how distinction**

MIT CISR research on decision rights identifies three key decision types in digital transformation: what is done versus how the goal is accomplished; how much is invested and how spending is prioritised; and who handles exceptions. In successful digital transformations, business leaders own "what," while delivery teams own "how." [fact; source: https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://cisr.mit.edu/content/classic-topics-decision-rights]

Daily sequencing, technical approach selection within an approved architecture, and technical debt prioritisation are all "how" decisions. Placing them in a central approval queue violates the what-vs-how boundary and creates governance overhead for decisions that should be owned by the team doing the work. [inference; source: https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html]

**B5. AWS distributed governance evidence**

AWS documents a modern architecture governance model based on three elements: preapproved blueprints (reference architectures and code templates that set principles for security and resilience without micromanaging implementation), distributed governance (asynchronous approval workflows with stakeholder participation), and automated guardrail enforcement (non-negotiable controls such as encryption enforced via policy-as-code rather than per-decision review). Traditional signoffs are reserved as an exception path for use cases that do not match any preapproved blueprint. [fact; source: https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/]

This model shows that the choice between central control and team autonomy is not binary: preapproved blueprints substitute for per-decision approval while preserving standards compliance. Decisions within a blueprint boundary need no approval. Decisions outside it trigger the exception path. [inference; source: https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

#### §2.C Bounded delegation design

**C1. Parameters that define a delegation boundary**

A bounded delegation boundary (delegation within defined guardrails with pre-agreed escalation paths, as defined in the P1 synthesis) requires at least three parameters: a cost ceiling (the maximum spend the team may authorise without external approval), a blast radius limit (the maximum scope of impact the team may accept without escalation), and an approved catalog (the set of technologies, vendors, or architectural patterns the team may use without a new review). [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html; https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/; https://www.bain.com/insights/rapid-decision-making/]

These three parameters replace per-decision approval with per-parameter governance: the governance work is front-loaded into setting the parameters rather than distributed across every individual decision. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/]

**C2. Escalation triggers**

Four escalation triggers bring a decision back to the central approval path: (1) deviation from the approved catalog or blueprint (the proposed decision requires a technology, vendor, or architectural pattern not in the pre-approved set); (2) cost ceiling breach (the estimated cost exceeds the team's authorised ceiling); (3) blast radius overflow (the potential impact exceeds the team's authorised scope limit, defined as: affects services outside the team's ownership boundary, affects external stakeholders, or is irreversible at the team level); and (4) external commitment (the decision creates a contractual, regulatory, or public-facing obligation). [inference; source: https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/; https://www.bain.com/insights/rapid-decision-making/; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

These four triggers are binary: a decision either crosses a trigger or does not. This avoids the ambiguity that produces shadow approval seeking or deliberate mis-classification of work. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

**C3. SRE on-call as a bounded delegation model**

SRE on-call authority demonstrates bounded delegation at the most time-critical end of the delegation spectrum. The on-call engineer is authorised to perform operations within the service boundary without per-action approval. Operations outside that boundary (impacting a dependent service owned by another team, for example) require coordination. Incidents are declared when the scope exceeds the on-call engineer's authority, triggering a command transition to the IC role. [fact; source: https://sre.google/sre-book/being-on-call/; https://sre.google/workbook/incident-response/]

Toil, defined by SRE as repetitive, manual, automatable operational work that lacks enduring value, is the class of execution work that most clearly demonstrates the cost of inadequate local authority: if every toil item requires external approval, the approval overhead scales with the system size at the same rate as the toil itself, producing a compounding overhead rather than a fixed cost. [inference; source: https://sre.google/workbook/eliminating-toil/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html]

### §3 Reasoning

Removing narrative glue:

1. Daily sequencing decisions have zero blast radius and full reversibility; central approval produces approval latency with no governance value return. [inference; source: https://teamtopologies.com/key-concepts; https://dora.dev/capabilities/loosely-coupled-teams/]
2. Sprint-level minor scope adjustments (within the same priority band, not changing external commitments) have bounded consequence and cycle-level reversibility; they belong with the delivery team subject to an escalation trigger at the major-vs-minor boundary. [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.bain.com/insights/rapid-decision-making/]
3. Reliability decisions within an already-approved SLO are bounded by the SLO itself; the delivery team's authority is implicitly pre-granted by the SLO approval. [inference; source: https://sre.google/sre-book/embracing-risk/; https://sre.google/sre-book/being-on-call/]
4. Technical debt prioritisation within a pre-authorised capacity band is a "how" decision that delivery teams are best positioned to make; deferring it through central approval increases the cost it is meant to address. [inference; source: https://sre.google/workbook/eliminating-toil/; https://cisr.mit.edu/content/simplifying-decision-rights-growth]
5. Local environment spend below a cost ceiling is bounded by the ceiling itself; central approval of spend below the ceiling produces queue latency while the ceiling alone provides the risk control. [inference; source: https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html]
6. Incident response decisions during an active incident are incompatible with external approval latency given the response times required for availability targets; ICS-based authority delegation is the established operational pattern. [fact; source: https://sre.google/workbook/incident-response/; https://sre.google/sre-book/being-on-call/]

### §4 Consistency Check

```text
contradiction_scan: no contradictions detected
- All six decision types in scope converge on the same pattern: bounded delegation is
  appropriate when frequency is high, consequence is reversible, and blast radius is
  contained.
- DORA, ICS, RAPID, MIT CISR, and AWS governance evidence all independently support
  delegation of execution decisions to delivery teams with guardrails rather than
  per-decision central approval.
- The four escalation trigger design is consistent with the three-class demand
  segmentation from Q2 and the physical lane design from Q3.
confidence_adjustment: none required; all key claims remain at medium confidence
  because the underlying evidence is secondary or inferential synthesis rather than
  primary controlled studies
scope_guardrail: maintained; Q5 control model trade-off selection (pre-approval vs.
  bounded delegation vs. post-hoc review) is explicitly out of scope and not addressed
  here
```

### §5 Depth and Breadth Expansion

**Technical lens:** The four escalation triggers (catalog deviation, cost ceiling breach, blast radius overflow, external commitment) map cleanly onto the three demand classes from Q2. Class 1 decisions (fast path: standard, reversible, low blast radius) remain entirely within the delegation boundary and need no trigger. Class 2 decisions (standard path: routine but non-trivial, bounded scope) may approach the boundary and require the team to check against the trigger conditions before proceeding. Class 3 decisions (exception path: novel, high-consequence, or irreversible) will typically trip at least one escalation trigger and move to the controlled path. The Q4 delegation map therefore complements the Q2 segmentation: Q2 classifies incoming demand at intake, while Q4 determines which governance regime applies to execution decisions after demand has entered a lane. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html]

**Regulatory lens:** In regulated sectors (banking, insurance, healthcare), the Agree role in RAPID maps to the compliance or risk function. The Basel Committee on Banking Supervision (BCBS) 328 principle of independent risk challenge requires that a second line of defence can challenge decisions, but does not require that the second line approve every individual execution decision. Pre-approved blueprints and automated guardrails satisfy the independent challenge requirement for routine decisions, reserving second-line challenge for decisions that trip an escalation trigger. [inference; source: https://www.bis.org/bcbs/publ/d328.pdf; https://www.bain.com/insights/rapid-decision-making/; https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/]

**Behavioural lens:** When delivery teams lack authority over "how" decisions, they experience controls as coercive rather than enabling. Formalisation is the degree to which work processes and procedures are codified; Adler and Borys (1996) distinguish enabling formalisation (which supports team work) from coercive formalisation (which constrains it). Coercive controls generate workaround behaviour: shadow approval, deliberate mis-classification of work, informal side-channels. The bounded delegation model preserves team agency over execution while maintaining explicit accountability through the escalation trigger structure, which shifts the behavioural dynamic from constraint to enablement. [inference; source: https://eric.ed.gov/?id=EJ525938; https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

**Economic lens:** Transaction cost economics (associated with Williamson and Coase) justifies pre-approval only for transactions with high relationship-specific investment, high uncertainty, or high consequence. High-frequency, low-blast-radius execution decisions fail all three tests. The coordination cost of central pre-approval for these decisions exceeds its error-reduction value, which is the governance-cost argument for bounded delegation independent of the throughput argument. [inference; source: https://ageconsearch.umn.edu/record/294665/files/ipr018.pdf; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

**Historical lens:** ICS as a framework was developed in 1968 precisely because command-and-control structures that required upward approval for each action during active wildfires produced fatal coordination failures. The post-incident analysis showed that the constraint was not competence but approval latency at the most time-critical decision moments. The SRE adoption of ICS three decades later reflects the same finding in a software operations context. [fact; source: https://sre.google/workbook/incident-response/]

### §6 Synthesis

The research question for Q4 is: which decisions about sequencing, scope, reliability, technical debt, local spend, and incident response must sit with delivery teams to reduce delay without losing control? All six categories should be delegated to delivery teams for execution decisions that are high-frequency, bounded in consequence, and reversible, provided three governance parameters are pre-defined (cost ceiling, blast radius limit, approved catalog) and four escalation triggers are active (catalog deviation, ceiling breach, blast radius overflow, external commitment). [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://sre.google/workbook/incident-response/; https://www.bain.com/insights/rapid-decision-making/; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/]

**Key Findings:**

1. **Daily task sequencing within an approved iteration must sit with delivery teams, because it is fully reversible, has zero blast radius, and produces only approval-queue latency when centralised.** ([inference]; medium confidence; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://teamtopologies.com/key-concepts; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html)

2. **Minor sprint-level scope adjustment (swapping items within the same priority band without changing external commitments) must sit with delivery teams; escalation is triggered only when the adjustment changes an external stakeholder commitment or exceeds the team's priority-band boundary.** ([inference]; medium confidence; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.bain.com/insights/rapid-decision-making/)

3. **Reliability decisions within an already-approved Service Level Objective must sit with delivery teams, because the SLO approval itself constitutes pre-authorised governance; decisions that change the SLO or accept reliability trade-offs with measurable external customer impact require escalation.** ([inference]; medium confidence; source: https://sre.google/sre-book/embracing-risk/; https://sre.google/sre-book/being-on-call/)

4. **Technical debt prioritisation within a pre-authorised capacity band must sit with delivery teams, because deferring this decision through central approval compounds the future cost of the debt faster than the governance cost of per-decision review adds risk-reduction value.** ([inference]; medium confidence; source: https://sre.google/workbook/eliminating-toil/; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://dora.dev/capabilities/loosely-coupled-teams/)

5. **Local environment spend below a defined cost ceiling must sit with delivery teams, because the cost ceiling itself is the risk control; central pre-approval of spend below the ceiling produces approval latency without providing additional risk reduction beyond what the ceiling already provides.** ([inference]; medium confidence; source: https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html)

6. **Live incident response decisions must sit with delivery teams under the Incident Command System authority structure, because external approval latency during an active incident is structurally incompatible with the five-minute response time required for services targeting four nines of availability (99.99%).** ([fact]; medium confidence; source: https://sre.google/workbook/incident-response/; https://sre.google/sre-book/being-on-call/)

7. **DORA research shows that teams authorised to make large-scale changes without external permission achieve higher software delivery performance across throughput and stability metrics simultaneously, indicating that team autonomy over execution decisions correlates positively with delivery outcomes.** ([inference]; medium confidence; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://dora.dev/guides/dora-metrics-four-keys/)

8. **The Bain RAPID framework places the Decide role as close to implementation as possible and restricts the Agree role to mandatory legal or regulatory requirements, providing a practitioner-validated design principle for moving decision authority toward execution rather than upward.** ([fact]; medium confidence; source: https://www.bain.com/insights/rapid-decision-making/; https://www.bain.com/insights/decisions-who-does-what/)

9. **MIT CISR research distinguishes what decisions (owned by business leaders) from how decisions (owned by delivery teams); daily sequencing, technical approach within an approved architecture, and technical debt prioritisation are all how decisions that belong with delivery teams, not with central approval functions.** ([fact]; medium confidence; source: https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://cisr.mit.edu/content/classic-topics-decision-rights)

10. **A bounded delegation boundary defined by three parameters (cost ceiling, blast radius limit, approved technology catalog) and four escalation triggers (catalog deviation, ceiling breach, blast radius overflow, external commitment) preserves governance outcomes for high-consequence decisions while eliminating per-decision approval overhead for all six routine execution decision categories.** ([inference]; medium confidence; source: https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://www.bain.com/insights/rapid-decision-making/)

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed
- WIP: work-in-progress (WIP) -- expanded at first narrative prose use in Context section
- SLO: Service Level Objective (SLO) -- expanded at first use in §1.A3 question text
- ICS: Incident Command System (ICS) -- expanded at first narrative prose use in §1.B2
- IC: Incident Commander (IC) -- expanded at first narrative prose use in §2.A6
- OL: Operations Lead (OL) -- expanded at first narrative prose use in §2.A6
- CL: Communications Lead (CL) -- expanded at first narrative prose use in §2.A6
- DORA: DevOps Research and Assessment (DORA) -- expanded at first narrative prose use in §1.B1
- RAPID: Recommend, Agree, Perform, Input, and Decide (RAPID) -- expanded at first use in §1.B3
- SRE: Site Reliability Engineering (SRE) -- expanded at first narrative prose use in §1.C3
- MIT CISR: Massachusetts Institute of Technology Center for Information Systems Research (MIT CISR) -- expanded in Sources section, first narrative prose use
- BCBS: Basel Committee on Banking Supervision (BCBS) -- expanded at first narrative prose use in §5 Regulatory lens
- AWS: Amazon Web Services (AWS) -- expanded in Sources section and §1.B5
- RAPID R/A/P/I/D: each role expanded at first use in §2.B3
parity_check: passed -- §6 Synthesis key findings match Findings Key Findings 1-10 verbatim
claim_label_audit: all claims in §2-§6 carry [fact], [inference], or [assumption] labels with URL-backed sources
em_dash_audit: no em-dashes (U+2014) present
ai_slop_audit: no filler phrases (Furthermore, Additionally, It is important to note, In conclusion, It is worth noting, Importantly) detected
evidence_map_audit: all 10 key findings have a corresponding Evidence Map row with URL-backed source cells
```

---

## Findings

### Executive Summary

Delivery teams must own all six categories of execution decision (daily sequencing, minor scope adjustment, reliability choices within an approved Service Level Objective, technical debt prioritisation within a pre-authorised capacity band, local environment spend below a cost ceiling, and live incident response) when those decisions are high-frequency, reversible, and bounded in blast radius. Centralising these decisions generates approval-queue latency with no proportionate governance value and, in the incident-response case, is structurally incompatible with the response times required to meet availability targets. [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://sre.google/workbook/incident-response/; https://cisr.mit.edu/content/simplifying-decision-rights-growth] The appropriate governance mechanism is bounded delegation: three pre-defined parameters (cost ceiling, blast radius limit, approved technology catalog) and four binary escalation triggers (catalog deviation, ceiling breach, blast radius overflow, external commitment) replace per-decision approval while preserving central oversight for genuinely high-consequence choices. [inference; source: https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/; https://www.bain.com/insights/rapid-decision-making/; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html] DORA, Bain RAPID, MIT CISR, and the Incident Command System all independently converge on the same design principle: the Decide role should sit as close to implementation as possible, and the Agree role should be used only for mandatory legal or regulatory requirements. [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.bain.com/insights/rapid-decision-making/; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://sre.google/workbook/incident-response/]

### Key Findings

1. **Daily task sequencing within an approved iteration must sit with delivery teams, because it is fully reversible, has zero blast radius, and produces only approval-queue latency when centralised.** ([inference]; medium confidence; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://teamtopologies.com/key-concepts; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html)

2. **Minor sprint-level scope adjustment (swapping items within the same priority band without changing external commitments) must sit with delivery teams; escalation is triggered only when the adjustment changes an external stakeholder commitment or exceeds the team's priority-band boundary.** ([inference]; medium confidence; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.bain.com/insights/rapid-decision-making/)

3. **Reliability decisions within an already-approved Service Level Objective must sit with delivery teams, because the SLO approval itself constitutes pre-authorised governance; decisions that change the SLO or accept reliability trade-offs with measurable external customer impact require escalation.** ([inference]; medium confidence; source: https://sre.google/sre-book/embracing-risk/; https://sre.google/sre-book/being-on-call/)

4. **Technical debt prioritisation within a pre-authorised capacity band must sit with delivery teams, because deferring this decision through central approval compounds the future cost of the debt faster than the governance cost of per-decision review adds risk-reduction value.** ([inference]; medium confidence; source: https://sre.google/workbook/eliminating-toil/; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://dora.dev/capabilities/loosely-coupled-teams/)

5. **Local environment spend below a defined cost ceiling must sit with delivery teams, because the cost ceiling itself is the risk control; central pre-approval of spend below the ceiling produces approval latency without providing additional risk reduction beyond what the ceiling already provides.** ([inference]; medium confidence; source: https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html)

6. **Live incident response decisions must sit with delivery teams under the Incident Command System authority structure, because external approval latency during an active incident is structurally incompatible with the five-minute response time required for services targeting four nines of availability (99.99%).** ([fact]; medium confidence; source: https://sre.google/workbook/incident-response/; https://sre.google/sre-book/being-on-call/)

7. **DORA research shows that teams authorised to make large-scale changes without external permission achieve higher software delivery performance across throughput and stability metrics simultaneously, indicating that team autonomy over execution decisions correlates positively with delivery outcomes.** ([inference]; medium confidence; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://dora.dev/guides/dora-metrics-four-keys/)

8. **The Bain RAPID framework places the Decide role as close to implementation as possible and restricts the Agree role to mandatory legal or regulatory requirements, providing a practitioner-validated design principle for moving decision authority toward execution rather than upward.** ([fact]; medium confidence; source: https://www.bain.com/insights/rapid-decision-making/; https://www.bain.com/insights/decisions-who-does-what/)

9. **MIT CISR research distinguishes what decisions (owned by business leaders) from how decisions (owned by delivery teams); daily sequencing, technical approach within an approved architecture, and technical debt prioritisation are all how decisions that belong with delivery teams, not with central approval functions.** ([fact]; medium confidence; source: https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://cisr.mit.edu/content/classic-topics-decision-rights)

10. **A bounded delegation boundary defined by three parameters (cost ceiling, blast radius limit, approved technology catalog) and four escalation triggers (catalog deviation, ceiling breach, blast radius overflow, external commitment) preserves governance outcomes for high-consequence decisions while eliminating per-decision approval overhead for all six routine execution decision categories.** ([inference]; medium confidence; source: https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://www.bain.com/insights/rapid-decision-making/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Daily sequencing: zero blast radius, full reversibility, central approval produces only latency | https://dora.dev/capabilities/loosely-coupled-teams/; https://teamtopologies.com/key-concepts | medium | Derived from DORA team-autonomy criteria and Team Topologies stream-aligned team design |
| [inference] Minor scope adjustment: bounded consequence, escalation triggered only at external-commitment boundary | https://dora.dev/capabilities/loosely-coupled-teams/; https://www.bain.com/insights/rapid-decision-making/ | medium | Distinction between minor (within band) and major (external commitment) is the escalation trigger |
| [inference] Reliability decisions within approved SLO: SLO approval is the pre-authorised governance | https://sre.google/sre-book/embracing-risk/; https://sre.google/sre-book/being-on-call/ | medium | SRE risk continuum and availability target logic |
| [inference] Technical debt within capacity band: deferral compounds debt cost faster than governance overhead justifies | https://sre.google/workbook/eliminating-toil/; https://cisr.mit.edu/content/simplifying-decision-rights-growth | medium | Toil compounding logic and MIT CISR what-vs-how distinction |
| [inference] Local spend below cost ceiling: ceiling is the risk control; pre-approval below ceiling adds latency without risk reduction | https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html | medium | AWS blueprint model and integrator rights evidence |
| [fact] Incident response: external approval incompatible with five-minute response time for four nines availability | https://sre.google/workbook/incident-response/; https://sre.google/sre-book/being-on-call/ | medium | Response time constraint and ICS authority structure directly stated in SRE sources |
| [inference] DORA: team autonomy positively correlated with delivery performance | https://dora.dev/capabilities/loosely-coupled-teams/; https://dora.dev/guides/dora-metrics-four-keys/ | medium | DORA findings are observational; causal direction is inferred |
| [fact] RAPID: Decide role sits as close to implementation as possible; Agree role used sparingly | https://www.bain.com/insights/rapid-decision-making/; https://www.bain.com/insights/decisions-who-does-what/ | medium | Directly stated in Bain RAPID role definitions |
| [fact] MIT CISR: delivery teams own how decisions; business leaders own what decisions | https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://cisr.mit.edu/content/classic-topics-decision-rights | medium | Directly stated in MIT CISR research summaries |
| [inference] Bounded delegation: three parameters plus four escalation triggers preserves governance while eliminating per-decision approval | https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html | medium | Synthesised from AWS blueprint model and governance effectiveness conditions |

### Assumptions

- **Delivery team competence:** [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html; https://dora.dev/capabilities/loosely-coupled-teams/] The delivery team has the technical competence to make reliable execution decisions within each category. If capability gaps exist, the bounded delegation model requires capability-building before delegation, not permanent centralisation.

- **Parameter maintenance:** [assumption; source: https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/; https://www.bain.com/insights/rapid-decision-making/] Governance parameters (cost ceilings, blast radius limits, approved catalogs) are maintained and updated on a regular cadence by the central function; stale parameters are a governance risk in the bounded delegation model.

- **Binary escalation trigger clarity:** [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html] Escalation triggers are objective and binary; if trigger conditions are ambiguous, teams will either over-escalate (recreating approval latency) or under-escalate (creating governance gaps). The bounded delegation model is only as good as the precision of its trigger definitions.

### Analysis

The six decision types in scope share a structural property: their governance risk is bounded before the decision is made, not during it. Daily sequencing risk is bounded by the iteration boundary. Scope adjustment risk is bounded by the priority-band definition. Reliability risk is bounded by the SLO. Technical debt risk is bounded by the capacity allocation. Spend risk is bounded by the cost ceiling. Incident response risk is bounded by the incident-scope definition. When governance parameters pre-bound the risk, the residual governance value of per-decision approval falls to near zero, while the coordination cost of that approval remains proportional to the decision frequency. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://ageconsearch.umn.edu/record/294665/files/ipr018.pdf; https://www.bain.com/insights/rapid-decision-making/]

The four independent evidence sources (DORA, ICS, RAPID, MIT CISR) converge on this same structural conclusion from different starting points. DORA reaches it from empirical measurement of delivery outcomes. ICS reaches it from operational analysis of time-critical coordination failures. RAPID reaches it from practitioner case studies of decision quality and speed. MIT CISR reaches it from strategic governance research in digital transformation. This convergence from independent sources is the primary reason the key findings are held at medium rather than low confidence, despite the absence of controlled experimental evidence. [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://sre.google/workbook/incident-response/; https://www.bain.com/insights/rapid-decision-making/; https://cisr.mit.edu/content/simplifying-decision-rights-growth]

The behavioural dimension reinforces the structural argument. Adler and Borys (1996) show that controls perceived as coercive generate workaround behaviour; the bounded delegation model shifts formalisation from coercive (centrally approved per-decision) to enabling (team-owned within pre-agreed bounds). The governance failure mechanisms item in this corpus documents that the workaround patterns (shadow workflows, deliberate mis-classification, informal approval channels) emerge specifically when controls are applied uniformly to all work regardless of transaction hazard. The bounded delegation model disrupts this pattern by differentiating control intensity by risk category. [inference; source: https://eric.ed.gov/?id=EJ525938; https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

The one rival remedy worth noting is adding central approval capacity rather than delegating. This approach preserves the central-control model while attempting to reduce its latency by adding reviewers. Evidence from queueing theory (Little's Law) and the Theory of Constraints shows that adding capacity to a non-bottleneck position does not reduce system lead time: if the constraint is the serial nature of the approval gate, adding reviewers does not remove the serial dependency. Delegation removes the dependency; capacity addition does not. [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html]

### Risks, Gaps, and Uncertainties

- **Competence prerequisite:** The bounded delegation model assumes delivery team competence in each decision category. No primary evidence was gathered in this item on how competence gaps manifest in practice or how to diagnose them before delegation. This is an evidence gap.
- **Parameter calibration:** The three governance parameters (cost ceiling, blast radius limit, approved catalog) require calibration for each organisation and each team. No empirical evidence on typical calibration values or calibration failure modes was gathered. This is an evidence gap.
- **DORA causal direction:** DORA data is observational. The correlation between team autonomy and delivery performance could reflect reverse causation (high-performing teams are granted more autonomy) rather than autonomy driving performance. The item treats DORA as corroborative evidence rather than proof of causation.
- **Regulated sectors:** The BCBS 328 analysis in §5 is an inference from the regulatory text, not a confirmed interpretation by a regulator. Application in highly regulated sectors (banking, healthcare) requires legal review of whether pre-approved blueprint governance satisfies applicable independent-review requirements.

### Open Questions

1. How should cost ceilings and blast radius limits be calibrated for teams at different maturity levels? (Potential backlog item for Q5 or a standalone item.)
2. What monitoring design detects under-escalation before it becomes a governance failure, without recreating approval-queue latency through surveillance overhead?
3. At what organisation scale does the parameter-maintenance cost of bounded delegation exceed its throughput benefit compared to alternative control models?

### Output

- **Type:** knowledge
- **Description:** A bounded delegation map for six execution decision categories, with three governance parameters and four escalation triggers, synthesised from DORA, ICS, RAPID, MIT CISR, and AWS governance evidence. [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://sre.google/workbook/incident-response/; https://www.bain.com/insights/rapid-decision-making/]
- **Key sources:**
  - [DORA Loosely Coupled Teams](https://dora.dev/capabilities/loosely-coupled-teams/)
  - [Google SRE Workbook: Incident Response](https://sre.google/workbook/incident-response/)
  - [AWS: Empower Your Teams with Modern Architecture Governance](https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/)
