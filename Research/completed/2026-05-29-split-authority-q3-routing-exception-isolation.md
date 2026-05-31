---
review_count: 2
title: "Q3: Routing design that isolates exceptions from routine flow"
added: 2026-05-29
status: completed
priority: high
tags: [routing, queue-design, exception-handling, triage]
blocks: [2026-05-29-split-authority-q1-flow-constraint, 2026-05-29-split-authority-q2-demand-segmentation]
started: 2026-05-31T10:00:34+00:00
completed: 2026-05-31T10:43:18+00:00
output: [knowledge]
cites:
  - 2026-05-29-split-authority-q2-demand-segmentation
  - 2026-05-29-split-authority-p1-operating-model-synthesis
  - 2026-04-01-backpressure-theory-of-constraints
  - 2026-05-23-governance-controls-effectiveness-conditions
related:
  - 2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention
  - 2026-04-26-human-in-the-loop-ai-automated-workflows
supersedes: ~
superseded_by: []
item_type: primary
confidence: medium
themes:
  - governance-policy
  - organisational-design
  - cost-performance
  - tools-infrastructure
  - enterprise-adoption
gaps: []
versions:
  - version: "1.0"
    sha: "0f3dd408698a6907deabfeaa8f9bcd42371b3701"
    changed: "2026-05-31"
    progress: "progress/2026-05-31-split-authority-q3-routing-exception-isolation.md"
    summary: "Initial completion"
---

# Q3: Routing design that isolates exceptions from routine flow

## Research Question

What intake, triage, queueing, escalation, and routing model allows routine work to move quickly while isolating high-risk or ambiguous work?

## Scope

**In scope:**
- Intake and routing designs that avoid one-queue-for-all bottlenecks.
- Escalation models for ambiguous/high-risk exceptions.

**Out of scope:**
- Control-policy selection independent of routing and segmentation evidence.

**Constraints:**
- Must incorporate Q1 constraint findings and Q2 demand classes.

## Context

Q3 combines routing and classification with exception-handling design to prevent exceptional work from blocking routine flow. It enables Q5, Q6, and P1. A split-authority delivery environment, defined as a delivery context in which authority is divided among at least two stakeholder groups with independent approval power, requires explicit routing infrastructure to convert demand segmentation (established in Q2) into operationally distinct queues with protected throughput. Without physical lane separation, classification alone is insufficient: exceptions will inevitably displace routine work from shared processing capacity. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-cohort-demand-domain-it.html]

## Approach

1. Compare serial, parallel, and hybrid lane-routing patterns.
2. Evaluate exception isolation mechanisms and escalation thresholds.
3. Define a routing model that protects baseline throughput under uncertainty.

## Sources

- [x] [Reinertsen, D.G. (2009) The Principles of Product Development Flow: Second Generation Lean Product Development, Celeritas Publishing](https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009) -- classes of service, expedite lane WIP limits, queue discipline
- [x] [PeopleCert / AXELOS (2019) ITIL 4 Change Enablement Practice Guide](https://www.axelos.com/certifications/itil-service-management/what-is-itil) -- change routing, reclassification on deviation, emergency escalation via Emergency Change Advisory Board (ECAB)
- [x] [Invensis Learning (2024) ITIL Change Management: Normal, Standard, and Emergency Change Types](https://www.invensislearning.com/blog/itil-change-management/) -- procedural detail on standard, normal, and emergency change routing
- [x] [Google SRE (2018) Workbook: Incident Response](https://sre.google/workbook/incident-response/) -- Incident Command System (ICS) as a structured escalation framework for production exceptions
- [x] [Google SRE (2016) Site Reliability Engineering: Being On-Call](https://sre.google/sre-book/being-on-call/) -- on-call escalation tiers, response-time tiers, non-preemptive paging model
- [x] [TOC Institute (2024) Five Focusing Steps](https://www.tocinstitute.org/five-focusing-steps.html) -- constraint subordination: all non-constraints must yield to protect constraint throughput
- [x] [DORA (2024) DORA Metrics and Four Keys](https://dora.dev/guides/dora-metrics-four-keys/) -- change lead time and change failure rate as throughput measurement
- [x] [DORA (2024) Loosely coupled teams capability](https://dora.dev/capabilities/loosely-coupled-teams/) -- structural independence between lanes reduces coordination overhead
- [x] [Little, J.D.C. (1961) A proof for the queuing formula, Operations Research](https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387) -- Little's Law: average queue length equals arrival rate times average wait time
- [x] [Adler and Borys (1996) Two types of bureaucracy: enabling and coercive, Administrative Science Quarterly](https://eric.ed.gov/?id=EJ525938) -- enabling versus coercive formalisation applied to routing controls
- [x] [Mitchell (2026) Q2: Demand segmentation for fast-path vs controlled-path flow](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html) -- three demand classes and three boundary tests this item builds on
- [x] [Mitchell (2026) Operating model synthesis for split-authority delivery systems](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html) -- five design principles, including lane architecture and leading indicators
- [x] [Mitchell (2026) Backpressure infrastructure and the Theory of Constraints](https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html) -- Drum-Buffer-Rope (DBR) scheduling and buffer management
- [x] [Mitchell (2026) Internal governance controls: effectiveness conditions in regulated enterprises](https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html) -- control proportionality to transaction hazard

---

## Research Skill Output

### §0 Initialise

Question: What intake, triage, queueing, escalation, and routing model allows routine work to move quickly while isolating high-risk or ambiguous work?

A split-authority delivery environment is defined as a delivery context in which authority is divided among at least two stakeholder groups with independent veto or approval power. The Q2 investigation established a three-class demand segmentation (Class 1: fast path; Class 2: standard path; Class 3: exception path) and three observable boundary tests (template test, recovery test, blast radius test) for class assignment. Q3 builds directly on those outputs and asks how the three classes are physically routed and how exceptions are isolated so that they cannot contaminate routine flow.

Scope: In scope are intake mechanisms, physical lane design, exception isolation approaches, in-flight escalation triggers, and throughput protection mechanisms. Out of scope is the selection of specific control policies independent of routing design, which belongs to Q5.

Constraints:
- Claims labelled [fact] require a URL-backed source.
- Claims labelled [inference] are derived from evidence; a source is required.
- Claims labelled [assumption] are not verified; justification and nearest URL-backed source are required.
- Output format: structured synthesis with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks, Open Questions, and Output section.

Prior completed items cross-referenced:
- `2026-05-29-split-authority-q2-demand-segmentation` -- directly provides the three-class model and three boundary tests this item implements as routing logic.
- `2026-05-29-split-authority-p1-operating-model-synthesis` -- establishes five design principles including the three-lane architecture and WIP limit rationale.
- `2026-04-01-backpressure-theory-of-constraints` -- provides Drum-Buffer-Rope (DBR) scheduling and buffer management as the flow mechanics substrate.
- `2026-05-23-governance-controls-effectiveness-conditions` -- establishes control proportionality principle used to justify lane-specific control intensity.
- `2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention` -- shows that coercive routing controls generate workaround behaviour, constraining routing design choices.

### §1 Question Decomposition

**A. What routing patterns exist across analogous domains?**
- A1. How does Information Technology Infrastructure Library (ITIL) 4 Change Enablement physically route work to change types and escalate deviations?
- A2. How does Site Reliability Engineering (SRE) route incidents through severity tiers with explicit escalation paths?
- A3. How does Reinertsen's classes of service framework govern queue discipline and Work in Progress (WIP) limits per lane?
- A4. How do emergency department fast-track designs isolate low-acuity lanes from high-acuity lanes?

**B. What are the mechanisms for exception isolation?**
- B1. What is the structural difference between logical classification and physical queue separation?
- B2. What WIP controls prevent exception lanes from dominating capacity?
- B3. How does in-flight escalation (reclassification during execution) work, and what triggers it?

**C. What escalation thresholds should trigger lane changes?**
- C1. What observable conditions should trigger an item to move from Class 1 to Class 2 or Class 3 during execution?
- C2. What system-level conditions should trigger a temporary tightening of fast-path gate criteria?
- C3. How should escalation authority be structured so that escalation decisions are made without delay?

**D. How does the routing model protect baseline throughput?**
- D1. Does serial queue discipline (all lanes share a single server pool) adequately protect routine flow from exception contamination?
- D2. Does parallel queue discipline (dedicated capacity per lane) protect throughput better?
- D3. What hybrid scheduling policy best balances isolation with capacity utilisation?

### §2 Investigation

#### A1: ITIL 4 change routing

ITIL 4 Information Technology Service Management (ITSM) routes changes at intake based on the three-type classification established in the Q2 item. Standard changes are routed to a pre-authorised fast path and implemented without per-instance Change Advisory Board (CAB) approval; only a logged change record is required. Normal changes are routed to a risk-and-impact assessment step and require change authority approval before implementation. Emergency changes are routed to an Emergency Change Advisory Board (ECAB), which is a designated small-membership authority that can convene rapidly and authorise emergency work without waiting for the full CAB cycle. [inference; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/]

The critical routing mechanism in ITIL 4 is reclassification on deviation: if a standard change encounters conditions that no longer match its pre-approved template (unexpected scope, novel failure mode, or expanded blast radius), it must be stopped and reclassified as a normal change before work continues. This is an in-flight escalation trigger; it does not require a new intake but does require routing to the normal change review path. [inference; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/]

The Emergency Change Advisory Board is a structural exception isolation mechanism: it is a standing body with pre-agreed membership and a rapid convening protocol, which prevents emergency changes from entering the normal CAB queue and displacing normal change review. [inference; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/]

#### A2: SRE severity tiers and incident escalation

Google's Site Reliability Engineering practice routes production incidents through severity tiers, which are the analogue of demand classes for operational events. Severity 1 (immediate risk to users) is handled preemptively by the primary on-call engineer with a five-minute response target; severity 2 and below are handled non-preemptively and can be queued for business hours. [fact; source: https://sre.google/sre-book/being-on-call/]

The SRE escalation path follows an Incident Command System (ICS) structure adapted from emergency response organisations. The Incident Commander (IC) is the first-named escalation point; the IC coordinates response, delegates to an Operations Lead (OL) for technical resolution, and delegates to a Communications Lead (CL) for stakeholder communication. If the primary on-call cannot resolve the incident, escalation proceeds to a secondary on-call and then to a team or service lead. [fact; source: https://sre.google/workbook/incident-response/]

The ICS structure provides two properties that are relevant to this routing model: first, named escalation authority means no incident waits for committee formation; second, the distinction between the IC's coordination role and the OL's technical resolution role means that exception management and routine work can proceed in parallel rather than competing for the same scarce expert attention. [inference; source: https://sre.google/workbook/incident-response/; https://sre.google/sre-book/being-on-call/]

The SRE on-call workbook notes that pager load exceeding two incidents per on-call shift is a signal that the exception rate is unsustainable and corrective action is required, because the capacity available for on-call engineers to do non-interrupt project work falls below 50% when pager load is high. [fact; source: https://sre.google/sre-book/being-on-call/]

#### A3: Reinertsen classes of service and lane discipline

Reinertsen's four classes of service (expedite, fixed-date, standard, and intangible) each imply a distinct queue discipline and WIP limit. The expedite lane operates with a WIP limit of one: only one expedite item at a time. This strict WIP limit is not incidental; it is the primary mechanism that prevents the expedite lane from contaminating normal flow. If expedite WIP were unlimited, any work could be declared urgent and the fast-pass benefit would disappear. [fact; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

The fixed-date class is ordered by due-date scheduling; the standard class is ordered by WIP-limited first-in, first-out (FIFO) or weighted queue ordering; the intangible class is scheduled in periodic batches with dedicated capacity, not interleaved with standard work. [fact; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

The consequence for split-authority delivery is that the exception path lane is the analogue of the expedite lane and must carry an explicit WIP limit. Without a WIP limit on the exception lane, any stakeholder can declare a work item exceptional and receive priority service, which converts the exception lane into a second, uncontrolled fast path that destroys the throughput protection the segmentation was designed to provide. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html]

#### A4: Emergency department fast-track lane design

Emergency department fast-track designs separate low-acuity patients from high-acuity patients using both physical space and dedicated staffing. Low-acuity patients are triaged into a physically separate fast-track area staffed by nurse practitioners or physician assistants; they follow a compressed assessment-and-discharge pathway without entering the main resuscitation or monitoring areas where high-acuity patients are treated. This physical separation ensures that fast-track throughput is not disrupted by resource competition with resuscitation events. [inference; source: https://www.ahrq.gov/patient-safety/settings/emergency/esi.html]

The key throughput protection mechanism in emergency department design is dedicated resourcing per lane, not simply priority ordering. Priority ordering without dedicated resourcing still allows a high-acuity surge to consume fast-track nursing capacity, because priority rules only govern the order of service when both types of patient compete for the same resource. Physical lane separation with dedicated staffing eliminates that competition entirely. [inference; source: https://www.ahrq.gov/patient-safety/settings/emergency/esi.html]

The mechanism for routing exceptions that develop within the fast-track lane is explicit reclassification and transfer: a fast-track patient who deteriorates is transferred to the main emergency area with a documented acuity reassessment, not handled in-place by the fast-track team. This reclassification protocol defines in-flight escalation as a lane transfer event, not a local escalation within the original lane. [inference; source: https://www.ahrq.gov/patient-safety/settings/emergency/esi.html]

#### B1: Logical classification versus physical queue separation

A classification scheme that assigns work items to named classes without creating physically separate queues and dedicated processing resources does not produce throughput isolation. Under a shared-queue model with priority ordering, the server pool processes higher-priority items first, but the total server capacity consumed by high-priority exception work reduces the capacity available for lower-priority routine work in the same time window. [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html]

Little's Law, which states that average queue length equals arrival rate multiplied by average wait time in a stable system, implies that reducing the capacity available to routine work directly lengthens routine lead time even if no individual routine item is explicitly blocked. [fact; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387] A classification scheme without lane separation therefore fails the throughput protection requirement even if it succeeds at the classification accuracy requirement. [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

The Theory of Constraints (ToC) subordination step (focusing step 3) requires that all non-constraint activities yield to protect the constraint's throughput. In a split-authority delivery system where the exception review capability is the constraint, the routing model must subordinate all other intake to protect exception review throughput. Physical lane separation achieves this by decoupling routine work intake from exception review capacity consumption. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html]

#### B2: WIP controls for exception lane

A WIP limit on the exception lane serves three purposes: it prevents exception lane overflow from consuming resources intended for other lanes; it creates visible pressure that reveals when the exception classification criteria are being applied too broadly; and it provides a natural circuit-breaker for the governance constraint. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://www.tocinstitute.org/five-focusing-steps.html]

The WIP limit appropriate for the exception lane in a split-authority delivery system depends on the capacity of the expert review function. Reinertsen's WIP-of-one rule for expedite is appropriate for contexts where a single expert reviewer is the constraint; in organisations with a panel of expert reviewers who can convene in parallel, the WIP limit can be calibrated to match the panel's concurrent review capacity. [assumption; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; justification: the one-item WIP rule derives from single-constraint logic; organisations with multiple expert reviewers should calibrate accordingly]

When exception lane WIP hits its limit, new arrivals that would be classified as Class 3 must be queued, not routed around the limit. The queue of waiting Class 3 items is a leading indicator of constraint saturation that should trigger the escalation conditions defined in C2 below. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

#### B3: In-flight escalation

In-flight escalation is the mechanism by which a work item that has already entered one lane is transferred to a higher-control lane because conditions observed during execution no longer match the class criteria that determined the item's original lane assignment. This is the routing analogue of ITIL 4's reclassification-on-deviation rule and the emergency department's acuity reassessment and transfer protocol. [inference; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/; https://www.ahrq.gov/patient-safety/settings/emergency/esi.html]

The three-boundary-test model from Q2 provides the natural in-flight escalation criteria. An item that entered the fast path (Class 1) because it passed all three boundary tests should be escalated to the standard path (Class 2) if it encounters a failed recovery test during execution (that is, the tested rollback procedure does not work as expected) or an expanded blast radius (a dependency not present in the original blast radius assessment is now exposed). [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/]

In-flight escalation from Class 1 to Class 3 is warranted when a work item reveals novel behaviour or irreversibility not identified at intake. The distinction between Class 2 and Class 3 in-flight escalation triggers is whether expert review is required before work can continue (Class 3) or whether bounded delegation within pre-agreed guardrails is still sufficient to continue (Class 2). [inference; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html]

The Incident Command System (ICS) model from Site Reliability Engineering (SRE) provides a well-supported escalation authority structure for in-flight escalation. A named Incident Commander-equivalent in the delivery context, defined here as the on-call decision authority, should hold the in-flight reclassification decision right. This prevents reclassification decisions from requiring committee formation, which would introduce the same approval latency that the routing model is designed to avoid. [inference; source: https://sre.google/workbook/incident-response/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html]

#### C1: Item-level escalation triggers

The following observable conditions should trigger in-flight escalation upward (from lower-control to higher-control lane):

1. **Failed recovery test during execution**: a rollback or backout procedure that was tested before intake fails to restore the pre-change state. This converts a reversible item into an irreversible one and requires immediate escalation to at least Class 2 and potentially Class 3. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; https://sre.google/workbook/incident-response/]

2. **Blast radius breach**: execution reveals a dependency not identified in the pre-intake blast radius assessment, expanding the potential impact beyond the agreed boundary. Escalation to Class 2 if still bounded; to Class 3 if impact boundary is now undefined. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/]

3. **Template deviation**: execution reveals that the work type does not conform to the pre-approved template used to satisfy the template test at intake (for example, a configuration value outside the permitted range, or a dependency the template was not designed to accommodate). This revokes the Class 1 pre-authorisation and requires reclassification. [inference; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html]

These three item-level triggers are observable without specialist judgment; the person executing the work can identify them without a separate review body. That is a design requirement: if escalation triggers require specialist judgment to identify, in-flight escalation becomes a second expert-review gate that reintroduces the approval latency it is supposed to avoid. [inference; source: https://sre.google/sre-book/being-on-call/; https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/]

#### C2: System-level escalation triggers

System-level escalation triggers govern temporary changes to the routing model itself, not individual item reclassifications. Two system-level triggers are supported by the evidence:

1. **Exception volume threshold**: when the ratio of Class 3 items to total intake exceeds a sustained level (for example, more than 20% of weekly intake, or three consecutive days above a trigger level), the fast-path gate criteria should be temporarily tightened by requiring a secondary review on items that would normally be auto-routed to Class 1. This circuit-breaker mechanism prevents the fast path from becoming a default bypass for a genuinely elevated risk environment. [inference; source: https://dora.dev/guides/dora-metrics-four-keys/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html]

2. **WIP limit reached on exception lane**: when the exception lane WIP limit is hit and a queue of waiting Class 3 items is building, the constraint is saturated and work entry to all lanes should be rationed to prevent system-wide WIP accumulation. The Theory of Constraints subordination step requires non-exception lanes to reduce intake rate when the constraint (exception review capacity) is at limit. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387]

The specific threshold values (percentage, day count, WIP limit number) must be calibrated empirically to the organisation; the evidence does not provide universal numbers. [assumption; source: https://dora.dev/guides/dora-metrics-four-keys/; justification: DevOps Research and Assessment (DORA) acknowledges that threshold calibration is organisation-specific]

#### C3: Escalation authority structure

Escalation authority for item-level reclassification should rest with a named single decision point: the delivery team lead or a designated on-call authority, not a committee. This follows the Incident Command System principle that command authority must be unambiguous to avoid decision latency during time-sensitive events. [inference; source: https://sre.google/workbook/incident-response/; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html]

System-level trigger decisions (tightening the fast-path gate, rationing intake) require the named integrator authority described in P1: the person or body with explicit budget-recommendation, prioritisation, and exception-veto rights. Team leads should not hold system-level escalation authority unilaterally, because system-level changes affect multiple teams and require cross-functional visibility. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html; https://sre.google/workbook/incident-response/]

The distinction between item-level and system-level escalation authority matches the ITIL 4 distinction between Change Manager authority (individual change decisions) and Change Advisory Board authority (policy and process-level decisions affecting multiple changes). [inference; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/]

#### D1-D3: Throughput protection mechanisms

**Serial versus parallel queue discipline:**

A serial queue model (single server pool, priority ordering) is insufficient for throughput protection because priority ordering reduces but does not eliminate capacity competition between lanes. Little's Law implies that reducing the processing time available to lower-priority items raises their lead time proportionally to the capacity consumed by higher-priority items. A serial model with high exception volume will produce measurable lead time inflation in the routine lane even if individual routine items are never explicitly blocked. [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html]

A fully parallel model (independent server pools per lane, no cross-lane capacity sharing) eliminates capacity competition but introduces resource stranding: if exception volume is low, the capacity dedicated to the exception lane is idle, which is economically wasteful. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

**Hybrid scheduling as the minimum viable throughput protection policy:**

The Drum-Buffer-Rope (DBR) scheduling pattern from the Theory of Constraints provides a minimum viable hybrid design. In DBR, the drum sets the pace at the constraint (the exception review function in split-authority delivery), the buffer protects the constraint from starvation (a queue of pre-approved standard path items that can be released immediately when exception review has spare capacity), and the rope controls work release upstream to prevent WIP accumulation beyond the drum's pace. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html; https://www.tocinstitute.org/five-focusing-steps.html]

Applied to the three-lane model, the hybrid scheduling policy is:
- Dedicate a minimum capacity fraction to each lane (for example, a minimum of 60% of processing capacity to the fast path, 30% to the standard path, and no more than 10% to the exception path under normal operating conditions). [assumption; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; justification: percentage values are illustrative; the design principle is minimum capacity reservation per lane, not a specific ratio, which must be calibrated to observed demand mix]
- Allow exception path to exceed its minimum only when the fast path and standard path are not WIP-constrained.
- Apply a WIP limit to the exception path that corresponds to the exception review function's concurrent processing capacity.
- Release work to the fast path at a rate governed by the downstream constraint (the merge or deployment gate), not at the maximum possible intake rate.

**DORA evidence on structural independence:**

DORA research on loosely coupled teams confirms that the highest-performing delivery organisations design team and system boundaries so that each team can deploy and change systems without depending on other teams. [fact; source: https://dora.dev/capabilities/loosely-coupled-teams/] This structural independence is the organisational analogue of lane separation: when the fast path lane and exception path lane share neither approval authority nor deployment infrastructure, exception volume on the exception path cannot block fast path deployments. [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html]

### §3 Reasoning

Unsupported generalisations removed:
- "Exception contamination" is used as a shorthand for the mechanism where exception-path work consumes capacity or authority time that would otherwise serve routine-path work. This is an inference from Little's Law and Reinertsen's WIP argument, not a named term in the cited literature; it is defined operationally on first use.
- The claim that serial queue discipline is insufficient does not require that serial models are always worse; it applies specifically to the split-authority delivery context where exception volume is variable and uncontrolled without a WIP limit.
- The hybrid scheduling policy fractions (60/30/10) are assumptions, not empirically established thresholds; they are stated as illustrative only.

The causal chain for Q3 is:
1. Q2 established three demand classes with observable boundary tests. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html]
2. Without physical lane separation, higher-priority items reduce effective capacity for lower-priority items (Little's Law + shared server pool). [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387]
3. Lane separation without Work in Progress (WIP) limits on the exception lane allows exception inflation to consume dedicated exception capacity, causing queue buildup at the exception gate. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://www.tocinstitute.org/five-focusing-steps.html]
4. Physical lane separation with WIP limits and minimum capacity reservation per lane provides the minimum structure that prevents exception contamination while preserving resource flexibility. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://www.tocinstitute.org/five-focusing-steps.html]
5. In-flight escalation via observable item-level triggers and a named single escalation authority prevents both under-escalation (items that should have been reclassified continuing on the wrong lane) and over-escalation (committee formation delays that add governance latency). [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://sre.google/workbook/incident-response/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

### §4 Consistency Check

```text
contradiction_scan: no internal contradictions found
  - ITIL 4 reclassification-on-deviation and Q2 boundary-test triggers are
    consistent; both name template deviation, blast radius breach, and failed
    reversibility as escalation signals
  - Reinertsen expedite WIP=1 and the DBR drum design are consistent;
    both derive from the constraint subordination principle
  - DORA loosely coupled teams and physical lane separation are consistent;
    structural independence between lanes is the organisational implementation
    of architectural loose coupling
  - SRE ICS model and the named-single-authority escalation requirement
    are consistent; both reject committee escalation for time-sensitive
    exception decisions

confidence_adjustment: all key claims kept at medium because the hybrid
  scheduling fractions are assumptions, not empirically measured values,
  and no published study directly measures three-lane routing in split-authority
  delivery settings

scope_guardrail: maintained; control policy selection (Q5) not addressed;
  decision rights placement (Q4) referenced only as it bears on escalation
  authority

triage_asymmetry_claim: consistent with Q2; over-classification on ambiguous
  items remains the correct safety default
```

### §5 Depth and Breadth Expansion

**Technical lens:** The three-lane routing model can be partially automated at the intake step. The template test (does a pre-approved pattern exist?) can be machine-checked against a managed change catalogue. The blast radius test (is impact contained within a defined boundary?) can be evaluated using dependency graphs and impact analysis tools. The recovery test (has the failure mode been tested?) can be verified against a runbook register or automated test suite. Items that pass all three automated checks are auto-routed to Class 1 without human intake review; items that fail any check are routed to Class 2 or 3 for human assessment. [inference; source: https://sre.google/workbook/eliminating-toil/; https://dora.dev/capabilities/loosely-coupled-teams/]

**Regulatory lens:** Banking supervisory guidance under the Basel Committee on Banking Supervision (BCBS) publication 328 requires that responsibilities, authority, and reporting lines be clearly allocated across business lines, management, and control functions. [fact; source: https://www.bis.org/bcbs/publ/d328.pdf] A three-lane routing model with explicit lane definitions, named escalation authority, and observable escalation triggers satisfies this allocation requirement without mandating uniform pre-approval for all work types. [inference; source: https://www.bis.org/bcbs/publ/d328.pdf] The proportionality principle in BCBS 328 explicitly permits differentiated control intensity by risk profile. [fact; source: https://www.bis.org/bcbs/publ/d328.pdf]

**Behavioural lens:** Adler and Borys' 1996 distinction between enabling and coercive formalisation (formalisation being the degree to which work processes are codified) is directly relevant to routing design. An enabling routing model is one where the lane assignment is legible to the person doing the work, the escalation path is defined and known in advance, and the controls on each lane are experienced as supporting the work rather than obstructing it. A coercive routing model is one where lane assignment is opaque, escalation requires committee formation, and controls are perceived as surveillance checkpoints. [inference; source: https://eric.ed.gov/?id=EJ525938; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html] The routing design principles above (observable triggers, named single authority, transparent lane definitions) are oriented toward the enabling form and away from the coercive form. [inference; source: https://eric.ed.gov/?id=EJ525938; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

The completed item on governance failure mechanisms found that bureaucracy-circumvention patterns (shadow workflows, informal approvals, deliberate misclassification) emerge when controls are experienced as coercive. A routing model where teams can bypass the exception lane by deliberately misclassifying work as Class 1 is a predictable failure mode. Observable boundary tests administered at intake reduce this misclassification incentive by making correct classification legible and auditable. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

**Historical lens:** The ITIL change management framework evolved the emergency change path precisely because organisations repeatedly observed that urgent work, if forced through the standard change approval cycle, produced either dangerous delays (waiting for the next CAB meeting while a critical system is degraded) or policy bypass (emergency work declared as standard to avoid the wait). The Emergency Change Advisory Board is the historical solution to this design tension: a standing authority that can convene rapidly and authorise emergency work without either waiting for the full CAB or bypassing governance entirely. [inference; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/] This historical pattern confirms that exception isolation requires a dedicated escalation authority, not simply a policy permitting faster processing. [inference; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/]

**Economic lens:** The economic justification for physical lane separation rather than priority ordering is that priority ordering still requires shared capacity. Dedicated capacity per lane is expensive when exception volume is low; it is cheap when exception volume is high, because it prevents the cascading lead time inflation that shared-pool degradation produces. The decision threshold for investing in lane separation infrastructure is whether the cost of lead time inflation in the routine lane (from shared-pool priority ordering) exceeds the cost of capacity reservation. For a split-authority delivery system where the routine lane carries the majority of delivery throughput, this threshold is typically crossed at moderate exception volumes. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387]

### §6 Synthesis

A three-lane physical routing model, with explicit WIP limits on the exception lane, observable item-level escalation triggers drawn from the Q2 boundary tests, a named single escalation authority for item-level reclassification, and a Drum-Buffer-Rope hybrid scheduling policy for capacity allocation, provides the minimum viable design that allows routine work to move quickly while isolating high-risk or ambiguous work. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://www.tocinstitute.org/five-focusing-steps.html; https://sre.google/workbook/incident-response/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html]

**Key Findings:**

1. Physical lane separation with dedicated minimum capacity per lane is necessary for throughput protection, because priority ordering alone does not prevent exception work from reducing effective capacity available to the routine lane and raising its lead time in proportion to exception volume, as Little's Law implies. ([inference]; medium confidence; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009)

2. A WIP limit on the exception lane is the primary mechanism preventing exception inflation, whereby stakeholders route work as Class 3 to receive priority service, which erodes the throughput protection that lane separation was designed to provide; without this limit, the exception lane becomes an uncontrolled second fast path. ([inference]; medium confidence; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://www.tocinstitute.org/five-focusing-steps.html)

3. In-flight escalation should be triggered by three observable, self-evident item-level conditions: a failed recovery test during execution, a blast radius breach revealing dependencies not identified at intake, and a template deviation confirming the item no longer matches its pre-approved pattern; all three conditions are drawn from the Q2 boundary tests and require no specialist judgment to identify. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/)

4. Escalation authority for item-level reclassification should be held by a named single decision point, the delivery team lead or a designated on-call authority, following the Incident Command System principle that unambiguous command authority is a prerequisite for rapid exception response and that committee formation for time-sensitive decisions reintroduces the approval latency the routing model is designed to avoid. ([inference]; medium confidence; source: https://sre.google/workbook/incident-response/; https://sre.google/sre-book/being-on-call/)

5. System-level escalation (temporarily tightening the fast-path gate or rationing all-lane intake) requires the named integrator authority established in the P1 operating model, because system-level changes affect multiple teams and require cross-functional visibility beyond the team lead's scope. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html; https://sre.google/workbook/incident-response/)

6. Two system-level circuit-breaker triggers are supported by the evidence: a sustained exception volume ratio above a calibrated threshold, which signals that fast-path gate criteria should be temporarily tightened; and exception lane WIP limit saturation, which signals that all-lane intake should be rationed to prevent system-wide WIP accumulation consistent with the Theory of Constraints subordination step. ([inference]; medium confidence; source: https://www.tocinstitute.org/five-focusing-steps.html; https://dora.dev/guides/dora-metrics-four-keys/)

7. The Drum-Buffer-Rope scheduling pattern provides a minimum viable hybrid capacity allocation design: the exception review function is the drum setting the pace, a buffer of pre-approved standard path items protects the drum from starvation, and the rope controls upstream work release to prevent WIP accumulation beyond the drum's pace, yielding a model that is neither fully serial nor fully parallel and avoids both the lead time inflation of pure priority ordering and the resource stranding of fully dedicated pools. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html; https://www.tocinstitute.org/five-focusing-steps.html)

8. The ITIL 4 Emergency Change Advisory Board and the SRE Incident Command System both implement exception lane isolation through a standing authority with pre-agreed rapid convening protocol rather than through ad-hoc committee formation, and this design pattern confirms that exception isolation requires a dedicated escalation authority structure, not only a policy permitting faster processing. ([inference]; medium confidence; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/; https://sre.google/workbook/incident-response/)

9. Deliberate misclassification of exception-path work as fast-path work to avoid governance overhead is a predictable behavioural failure mode of any routing model; observable boundary tests administered at intake reduce this incentive by making correct classification legible and auditable, consistent with the enabling rather than coercive formalisation principle. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://eric.ed.gov/?id=EJ525938)

**Assumptions:**

1. The exception review function is the binding constraint in the split-authority delivery system; if a different function (for example, a testing environment or a deployment pipeline) is the actual constraint, the DBR drum should be placed there instead. [assumption; source: https://www.tocinstitute.org/five-focusing-steps.html; justification: Q1 (not yet completed as a standalone item) and P1 both identify governance-generated queueing as the dominant constraint, which places exception review as the most likely drum candidate]

2. The hybrid scheduling capacity fractions (minimum 60% fast path, 30% standard path, 10% exception path) are illustrative; actual fractions must be calibrated to the organisation's observed demand mix. [assumption; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; justification: no published study provides universal capacity fractions; the design principle is minimum reservation per lane, not a specific ratio]

3. Observable item-level escalation triggers (failed recovery test, blast radius breach, template deviation) can be identified reliably by the person executing the work without specialist judgment; if work execution requires specialist knowledge to identify boundary conditions, an intake specialist function is required before the routing model is operable. [assumption; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/; justification: ITIL 4 requires classification to be operable without per-instance specialist review for standard changes; this assumption extends that requirement to in-flight escalation triggers]

**Evidence Map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Physical lane separation with dedicated capacity is necessary; priority ordering alone is insufficient | https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009 | medium | Little's Law provides the mechanism; Reinertsen provides the WIP/priority interaction argument |
| [inference] WIP limit on exception lane prevents exception inflation | https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://www.tocinstitute.org/five-focusing-steps.html | medium | Reinertsen's expedite WIP=1 rule; ToC subordination step |
| [inference] Three observable item-level escalation triggers (recovery test failure, blast radius breach, template deviation) | https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/ | medium | Q2 boundary tests extended to in-flight context; ITIL 4 reclassification-on-deviation |
| [inference] Named single escalation authority for item-level reclassification, following ICS principle | https://sre.google/workbook/incident-response/; https://sre.google/sre-book/being-on-call/ | medium | ICS unambiguous command authority; SRE on-call model |
| [inference] System-level escalation requires named integrator authority | https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html; https://sre.google/workbook/incident-response/ | medium | Cross-functional scope beyond team lead; P1 integrator authority bundle |
| [inference] Two system-level circuit-breaker triggers: exception volume ratio and WIP limit saturation | https://www.tocinstitute.org/five-focusing-steps.html; https://dora.dev/guides/dora-metrics-four-keys/ | medium | ToC subordination; DORA exception volume as leading indicator |
| [inference] DBR hybrid scheduling is the minimum viable throughput protection policy | https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html; https://www.tocinstitute.org/five-focusing-steps.html | medium | DBR directly applicable; fractions are assumption |
| [inference] ITIL 4 ECAB and SRE ICS confirm dedicated escalation authority structure is required | https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/; https://sre.google/workbook/incident-response/ | medium | Two independent domain implementations of the same design principle |
| [inference] Observable boundary tests reduce misclassification incentive | https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://eric.ed.gov/?id=EJ525938 | medium | Circumvention behaviour from completed item; enabling vs coercive formalisation |
| [fact] DORA loosely coupled teams: highest-performing organisations can deploy without cross-team dependency | https://dora.dev/capabilities/loosely-coupled-teams/ | medium | DORA published research finding |
| [fact] BCBS 328 requires authority and reporting lines clearly allocated across business, management, and control functions | https://www.bis.org/bcbs/publ/d328.pdf | high | Primary regulatory source; proportionality principle is explicit |

**Analysis:**

The evidence supports a three-lane physical routing model with DBR hybrid scheduling as the minimum viable design for exception isolation. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; https://www.tocinstitute.org/five-focusing-steps.html] The alternative of a two-lane model (fast path and exception path only, collapsing Class 2 into one of them) is rejected on the grounds established in Q2: two lanes force the exception path to absorb both routine assessed work and genuinely exceptional items, intensifying the bottleneck at the exception gate. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html]

The alternative of serial queue discipline (priority ordering without lane separation) is rejected on Little's Law grounds: priority ordering reduces but does not eliminate capacity competition, and at moderate exception volumes it produces measurable lead time inflation in the routine lane. [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387]

The alternative of fully parallel queues (independent server pools per lane, no cross-lane sharing) is not rejected as incorrect but is noted as economically wasteful at low exception volumes. DBR hybrid scheduling preserves cross-lane capacity sharing while using the WIP limit and rope mechanism to prevent exception work from consuming routine capacity above the established minimum reservation. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html]

The key trade-off in the routing model design is between escalation speed and escalation accuracy. A model with low escalation thresholds (trigger on any deviation from the template) will produce many in-flight reclassifications; a model with high thresholds will leave items that should have been escalated on the wrong lane. The three observable trigger conditions (failed recovery test, blast radius breach, template deviation) are calibrated toward accuracy over speed: they do not trigger on subjective uncertainty but only on observable, binary test failures. This calibration is consistent with the governance controls effectiveness principle that controls should provide useful challenge, not blanket surveillance. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://sre.google/workbook/incident-response/]

**Risks, Gaps, and Uncertainties:**

- The calibration of exception lane WIP limits must be done empirically for each organisation; the evidence base does not supply universal values.
- The circuit-breaker threshold values (exception volume percentage, day count) are inferences from leading indicator logic, not empirically measured trigger points.
- The claim that observable boundary tests can be applied reliably by non-specialist executors is an assumption; if execution requires specialist knowledge, an intake specialist function is required before the routing model is operable.
- No published study directly tests the three-lane DBR routing model in a split-authority delivery setting. The evidence is cross-domain inference from ITIL 4, SRE, Reinertsen, and ToC.
- The emergency department fast-track analogy assumes that dedicated staffing per lane is feasible; for small delivery teams where individuals span multiple roles, full dedicated staffing may not be achievable, requiring a weaker hybrid.

**Open Questions:**

- What is the minimum viable exception lane WIP limit for a split-authority delivery team of fewer than ten people, where the expert review function may be a single named individual?
- How should the routing model handle Class 2 items that complete assessment and are downgraded to Class 1 (reverse escalation)? Should they re-enter the fast-path queue or be held in the standard path for the remainder of execution?
- What governance evidence (reclassification rate, escalation trigger frequency, misclassification incidents) should be collected to validate and calibrate the routing model over time? This is a Q6 leading indicators question.
- How does the routing model interact with Artificial Intelligence (AI)-assisted intake triage: can AI automate the three boundary tests reliably, and does AI-assisted classification change the false-escalation or under-escalation rate?

**Output:**

- Type: knowledge
- Description: A three-lane physical routing model with Drum-Buffer-Rope hybrid scheduling, WIP limit on the exception lane, three observable item-level escalation triggers (failed recovery test, blast radius breach, template deviation), named single escalation authority for item-level decisions, named integrator authority for system-level circuit-breaker decisions, and two system-level trigger conditions that govern temporary gate tightening, grounded in convergent evidence from ITIL 4 change routing, SRE Incident Command System escalation, Reinertsen's classes of service, and the Theory of Constraints. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://sre.google/workbook/incident-response/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/]
- Key sources:
  1. https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009 (Reinertsen 2009 -- classes of service and WIP limits)
  2. https://sre.google/workbook/incident-response/ (Google SRE Workbook -- ICS escalation model)
  3. https://www.tocinstitute.org/five-focusing-steps.html (TOC Institute -- five focusing steps and DBR)

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed
  - ITIL: Information Technology Infrastructure Library (ITIL) -- expanded at A1 first prose use
  - IT: Information Technology (IT) -- expanded in ITSM expansion
  - ITSM: IT Service Management (ITSM) -- expanded at first prose use in A1
  - CAB: Change Advisory Board (CAB) -- expanded at first prose use in A1
  - ECAB: Emergency Change Advisory Board (ECAB) -- expanded at first prose use in A1
  - SRE: Site Reliability Engineering (SRE) -- expanded in Sources and §0 first prose use
  - ICS: Incident Command System (ICS) -- expanded at A2 first prose use
  - IC: Incident Commander (IC) -- expanded at A2 first prose use
  - OL: Operations Lead (OL) -- expanded at A2 first prose use
  - CL: Communications Lead (CL) -- expanded at A2 first prose use
  - ToC: Theory of Constraints (ToC) -- expanded at §2 B1 first prose use
  - WIP: Work in Progress (WIP) -- expanded at §1 first prose use
  - DBR: Drum-Buffer-Rope (DBR) -- expanded at D3 first prose use
  - DORA: DevOps Research and Assessment (DORA) -- expanded at C2 assumption sentence (first prose use)
  - BCBS: Basel Committee on Banking Supervision (BCBS) -- expanded at §5 regulatory lens first prose use
  - FIFO: first-in, first-out (FIFO) -- expanded at A3 first prose use
  - AI: Artificial Intelligence (AI) -- expanded in Open Questions first use
  - BAU not used in this item
  - LLM, API, SDK, PAT, MCP, RAG, CoT not used in this item
claim_label_audit: all factual and inferential claims in §2 carry [fact], [inference], or [assumption] labels with URL-backed sources
parity_check: §6 Key Findings and Findings Key Findings are mirrored; §6 Assumptions and Findings Assumptions are mirrored
source_url_audit: all sources carry URLs; no bare source names without URLs
em_dash_scan: no em-dashes present
ai_slop_scan: no "Furthermore", "Additionally", "Importantly", "It is important to note" found
vague_quantifier_scan: "majority" used once in §5 economic lens with a qualified conditional clause; "moderate" used with an inferential label; no unsourced absolute quantifiers
binary_contrast_check: no "not X but Y" contrast formulas present in Findings
evidence_map_audit: all nine Key Findings represented in Evidence Map; all source cells contain URLs
alternative_explanations_audit: three rival designs addressed in Analysis (two-lane model, serial queue, fully parallel queue); each rejected with evidence or noted as conditionally valid
```

---

## Findings

### Executive Summary

A three-lane physical routing model, in which fast-path (Class 1), standard-path (Class 2), and exception-path (Class 3) work each occupy dedicated queues with minimum capacity reservations and the exception lane carries an explicit Work in Progress (WIP) limit, is the minimum viable design for allowing routine work to move quickly while isolating high-risk or ambiguous work in a split-authority delivery environment. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html] Priority ordering alone within a shared queue is insufficient because Little's Law implies that exception work reduces the processing capacity available to routine work even if no individual item is explicitly blocked, raising routine lead time in proportion to exception volume. [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387] In-flight escalation uses three observable item-level triggers (failed recovery test, blast radius breach, template deviation) drawn from the Q2 boundary tests, with a named single escalation authority modelled on the Incident Command System to prevent committee formation delays. [inference; source: https://sre.google/workbook/incident-response/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html] Two system-level circuit-breaker triggers govern temporary gate tightening and intake rationing when exception volume rises or the exception lane WIP limit is saturated. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://dora.dev/guides/dora-metrics-four-keys/]

### Key Findings

1. Physical lane separation with dedicated minimum capacity per lane is necessary for throughput protection, because priority ordering alone does not prevent exception work from reducing effective capacity available to the routine lane and raising its lead time in proportion to exception volume, as Little's Law implies. ([inference]; medium confidence; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009)

2. A WIP limit on the exception lane is the primary mechanism preventing exception inflation, whereby stakeholders route work as Class 3 to receive priority service, which erodes the throughput protection that lane separation was designed to provide; without this limit, the exception lane becomes an uncontrolled second fast path. ([inference]; medium confidence; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://www.tocinstitute.org/five-focusing-steps.html)

3. In-flight escalation should be triggered by three observable, self-evident item-level conditions: a failed recovery test during execution, a blast radius breach revealing dependencies not identified at intake, and a template deviation confirming the item no longer matches its pre-approved pattern; all three conditions require no specialist judgment to identify. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/)

4. Escalation authority for item-level reclassification should be held by a named single decision point, the delivery team lead or a designated on-call authority, following the Incident Command System principle that unambiguous command authority is a prerequisite for rapid exception response and that committee formation for time-sensitive decisions reintroduces the approval latency the routing model is designed to avoid. ([inference]; medium confidence; source: https://sre.google/workbook/incident-response/; https://sre.google/sre-book/being-on-call/)

5. System-level escalation, meaning temporarily tightening the fast-path gate or rationing all-lane intake, requires the named integrator authority established in the P1 operating model because system-level changes affect multiple teams and require cross-functional visibility beyond the scope of a single team lead. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html; https://sre.google/workbook/incident-response/)

6. Two system-level circuit-breaker triggers are supported by the evidence: a sustained exception volume ratio above a calibrated threshold, which signals that fast-path gate criteria should be temporarily tightened; and exception lane WIP limit saturation, which signals that all-lane intake should be rationed to prevent system-wide WIP accumulation consistent with the Theory of Constraints subordination step. ([inference]; medium confidence; source: https://www.tocinstitute.org/five-focusing-steps.html; https://dora.dev/guides/dora-metrics-four-keys/)

7. The Drum-Buffer-Rope scheduling pattern provides a minimum viable hybrid capacity allocation design: the exception review function is the drum setting the pace, a buffer of pre-approved standard path items protects the drum from starvation, and the rope controls upstream work release to prevent WIP accumulation beyond the drum's pace, yielding a model that avoids both the lead time inflation of pure priority ordering and the resource stranding of fully dedicated pools. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html; https://www.tocinstitute.org/five-focusing-steps.html)

8. The ITIL 4 Emergency Change Advisory Board and the SRE Incident Command System both implement exception lane isolation through a standing authority with pre-agreed rapid convening protocol rather than through ad-hoc committee formation, confirming that exception isolation requires a dedicated escalation authority structure, not only a policy permitting faster processing. ([inference]; medium confidence; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/; https://sre.google/workbook/incident-response/)

9. Deliberate misclassification of exception-path work as fast-path work to avoid governance overhead is a predictable behavioural failure mode of any routing model; observable boundary tests administered at intake reduce this incentive by making correct classification legible and auditable, consistent with the enabling rather than coercive formalisation principle. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://eric.ed.gov/?id=EJ525938)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Physical lane separation with dedicated capacity is necessary; priority ordering alone is insufficient | https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009 | medium | Little's Law provides the mechanism; Reinertsen provides the WIP/priority interaction argument |
| [inference] WIP limit on exception lane prevents exception inflation | https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://www.tocinstitute.org/five-focusing-steps.html | medium | Reinertsen expedite WIP=1 rule; ToC subordination step |
| [inference] Three observable item-level escalation triggers (recovery test failure, blast radius breach, template deviation) | https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/ | medium | Q2 boundary tests extended to in-flight context; ITIL 4 reclassification-on-deviation |
| [inference] Named single escalation authority for item-level reclassification, following ICS principle | https://sre.google/workbook/incident-response/; https://sre.google/sre-book/being-on-call/ | medium | ICS unambiguous command authority; SRE on-call model |
| [inference] System-level escalation requires named integrator authority | https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html; https://sre.google/workbook/incident-response/ | medium | Cross-functional scope beyond team lead; P1 integrator authority bundle |
| [inference] Two system-level circuit-breaker triggers: exception volume ratio and WIP limit saturation | https://www.tocinstitute.org/five-focusing-steps.html; https://dora.dev/guides/dora-metrics-four-keys/ | medium | ToC subordination; DORA exception volume as leading indicator |
| [inference] DBR hybrid scheduling is the minimum viable throughput protection policy | https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html; https://www.tocinstitute.org/five-focusing-steps.html | medium | DBR directly applicable; capacity fractions are assumption |
| [inference] ITIL 4 ECAB and SRE ICS confirm dedicated escalation authority structure is required | https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/; https://sre.google/workbook/incident-response/ | medium | Two independent domain implementations of the same design principle |
| [inference] Observable boundary tests reduce misclassification incentive | https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://eric.ed.gov/?id=EJ525938 | medium | Circumvention behaviour from completed item; enabling vs coercive formalisation |
| [fact] DORA loosely coupled teams: highest-performing organisations deploy without cross-team dependency | https://dora.dev/capabilities/loosely-coupled-teams/ | medium | DORA published research finding |
| [fact] BCBS 328 requires authority and reporting lines clearly allocated across business, management, and control functions | https://www.bis.org/bcbs/publ/d328.pdf | high | Primary regulatory source; proportionality principle is explicit |

### Assumptions

1. The exception review function is the binding constraint in the split-authority delivery system. If a different function is the actual constraint, the DBR drum should be placed there instead. [assumption; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html; justification: Q1 and P1 both identify governance-generated queueing as the dominant constraint]

2. The hybrid scheduling capacity fractions stated in §2 D3 (minimum 60% fast path, 30% standard path, 10% exception path) are illustrative; actual fractions must be calibrated to the organisation's observed demand mix. [assumption; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; justification: no published study provides universal capacity fractions; the design principle is minimum reservation per lane]

3. Observable item-level escalation triggers can be identified reliably by the person executing the work without specialist judgment; if work execution requires specialist knowledge to identify boundary conditions, an intake specialist function is required before the routing model is operable. [assumption; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/; justification: ITIL 4 requires standard change classification to be operable without per-instance specialist review; this item extends that requirement to in-flight escalation triggers]

### Analysis

The evidence supports a three-lane physical routing model with Drum-Buffer-Rope hybrid scheduling as the minimum viable design. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; https://www.tocinstitute.org/five-focusing-steps.html] The alternative of a two-lane model is rejected because it forces the exception path to absorb both routine assessed work and genuinely exceptional items, intensifying the bottleneck at the exception gate, as established in the Q2 demand segmentation item. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html]

Serial queue discipline with priority ordering is insufficient on Little's Law grounds: priority ordering reduces but does not eliminate capacity competition, and at moderate exception volumes it produces measurable lead time inflation in the routine lane. [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387] Fully parallel queues with independent server pools eliminate capacity competition but strand capacity at low exception volumes; DBR hybrid scheduling preserves cross-lane capacity sharing while using the WIP limit and rope mechanism to prevent exception work from consuming routine capacity above the minimum reservation. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html]

The key design tension in the escalation model is between escalation speed and escalation accuracy. Observable triggers that are binary and self-evident (failed recovery test, blast radius breach, template deviation) favour accuracy: they do not trigger on subjective uncertainty, only on observable test failures. A rival design would use a single risk-score escalation threshold (for example, any item whose estimated impact score rises above a number triggers escalation); that model trades accuracy for simplicity but requires a maintained risk scoring tool and introduces the risk that scores drift from actual risk levels over time. The observable-test model is preferred here because it requires less ongoing calibration and is legible to the person executing the work. [inference; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.invensislearning.com/blog/itil-change-management/; https://sre.google/workbook/incident-response/]

The behavioural risk of misclassification to avoid governance overhead is addressed by two design features: the legibility and auditability of the boundary tests (making correct classification the path of least resistance), and the WIP limit on the exception lane (removing the incentive to declare work as Class 3 to receive priority service). Both features address the root cause of circumvention behaviour identified in the governance failure mechanisms item, which is that coercive or opaque controls generate resistance and workaround behaviour. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://eric.ed.gov/?id=EJ525938]

### Risks, Gaps, and Uncertainties

- Exception lane WIP limit and circuit-breaker threshold values must be calibrated empirically; the evidence base does not supply universal numbers.
- No published study directly tests the three-lane DBR routing model in a split-authority delivery setting; the evidence base is cross-domain inference from ITIL 4, SRE, Reinertsen, and Theory of Constraints.
- The observable escalation triggers assume that executors can reliably identify boundary test failures in real time; this assumption may not hold for complex, highly coupled systems where blast radius is difficult to assess without specialist tooling.
- The emergency department and SRE analogies assume dedicated staffing per lane or per escalation tier, which may not be feasible for small teams where individuals span multiple roles.
- Reverse escalation (downgrading a Class 2 item to Class 1 mid-execution) is not addressed; this requires a separate policy decision about whether re-entry to the fast-path queue is permitted.

### Open Questions

- What is the minimum viable exception lane WIP limit for a delivery team where the expert review function is a single named individual?
- How should the routing model handle Class 2 items that complete assessment and are downgraded to Class 1 (reverse escalation)?
- What governance evidence should be collected to calibrate and validate the routing model over time? (Q6 leading indicators question)
- How does AI-assisted intake triage affect the false-escalation and under-escalation rates for the three boundary tests?

### Output

- Type: knowledge
- Description: A three-lane physical routing model with Drum-Buffer-Rope hybrid scheduling, WIP limit on the exception lane, three observable item-level escalation triggers, and two system-level circuit-breaker triggers, grounded in convergent evidence from ITIL 4 change routing, SRE Incident Command System escalation, Reinertsen's classes of service, and the Theory of Constraints. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://sre.google/workbook/incident-response/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]
- Key sources:
  1. https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009 (Reinertsen 2009 -- classes of service and WIP limits)
  2. https://sre.google/workbook/incident-response/ (Google SRE Workbook -- ICS escalation model)
  3. https://www.tocinstitute.org/five-focusing-steps.html (TOC Institute -- five focusing steps and DBR)
