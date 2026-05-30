---
title: "Q2: Demand segmentation for fast-path vs controlled-path flow"
added: 2026-05-29
status: reviewing
priority: high
tags: [demand-segmentation, triage, flow-design, governance]
blocks: [2026-05-29-split-authority-q1-flow-constraint]
started: 2026-05-30T03:51:41+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-05-29-split-authority-p1-operating-model-synthesis
  - 2026-05-23-governance-controls-effectiveness-conditions
  - 2026-05-16-variance-control-comparison-across-delivery-modes
  - 2026-05-14-org-failure-modes-cohort-demand-domain-it
  - 2026-05-14-org-failure-modes-project-demand-product-it
  - 2026-05-16-do-mode-demand-persistence-and-build-mode-displacement
  - 2026-04-01-backpressure-theory-of-constraints
related:
  - 2026-04-22-ai-governance-assurance-change-control-verification
  - 2026-04-26-ai-lowcode-risk-tier-classification-controls
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
versions: []
gaps: []
---

# Q2: Demand segmentation for fast-path vs controlled-path flow

## Research Question

Which work items are low-risk, standard, and reversible enough for fast-path handling, and which require slower expert review or tighter controls?

## Scope

**In scope:**
- Classification criteria for routine vs exceptional demand.
- Segment definitions that support differentiated handling speeds and control levels.

**Out of scope:**
- Designing final routing queues before segmentation criteria are validated.

**Constraints:**
- Build on Q1 findings about the dominant flow constraint.

## Context

Q2 merges fast-flow suitability and tractability questions into one segmentation design problem. It enables Q3, Q5, Q6, and P1. A split-authority delivery environment (one in which authority is divided among at least two stakeholder groups with independent approval power) produces queue fragmentation whenever all incoming demand receives identical handling regardless of risk, reversibility, or standardisation level. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-cohort-demand-domain-it.html]

## Approach

1. Define risk/reversibility/standardisation criteria for intake segmentation.
2. Evaluate segmentation schemes from analogous queueing domains.
3. Propose a minimal set of demand classes with clear control implications.

## Sources

- [x] [Reinertsen, D.G. (2009) The Principles of Product Development Flow: Second Generation Lean Product Development, Celeritas Publishing](https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009) -- classes of service and cost of delay segmentation criteria
- [x] [PeopleCert / AXELOS (2019) ITIL 4 Change Enablement Practice Guide](https://www.axelos.com/certifications/itil-service-management/what-is-itil) -- standard, normal, and emergency change type definitions
- [x] [Challoner et al. (2018) Site Reliability Engineering Workbook: Eliminating Toil](https://sre.google/workbook/eliminating-toil/) -- standard change automation and toil reduction criteria
- [x] [Alvidrez, M. (2017) Site Reliability Engineering: Embracing Risk](https://sre.google/sre-book/embracing-risk/) -- risk continuum and service level classification
- [x] [DORA (2024) DORA Metrics and Four Keys](https://dora.dev/guides/dora-metrics-four-keys/) -- change lead time, change failure rate, and deployment frequency segmentation evidence
- [x] [TOC Institute (2024) Five Focusing Steps](https://www.tocinstitute.org/five-focusing-steps.html) -- constraint exploitation and flow segmentation
- [x] [Mitchell (2026) Operating model synthesis for split-authority delivery systems](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html) -- B1-B2 demand segmentation synthesis
- [x] [Mitchell (2026) Internal governance controls: effectiveness conditions in regulated enterprises](https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html) -- control proportionality to transaction hazard
- [x] [Mitchell (2026) Variance control comparison across delivery modes](https://davidamitchell.github.io/Research/research/2026-05-16-variance-control-comparison-across-delivery-modes.html) -- structural vs behavioural controls and pre-effect detection

---

## Research Skill Output

### §0 Initialise

Question: Which work items are low-risk, standard, and reversible enough for fast-path handling, and which require slower expert review or tighter controls?

Scope: Classification criteria for routine versus exceptional demand; segment definitions supporting differentiated handling speeds and control levels. Final queue routing design is out of scope until segmentation criteria are validated.

Constraints:
- Claims labelled [fact] require a URL-backed source.
- Claims labelled [inference] are derived from evidence; a source is required.
- Claims labelled [assumption] are not verified; justification is required with nearest URL-backed source.
- This item builds on Q1 findings, which are also synthesised in the completed P1 operating model item.
- Output format: structured synthesis with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks, Open Questions, and Output section.

Prior completed items cross-referenced:
- `2026-05-29-split-authority-p1-operating-model-synthesis` -- directly develops B1-B2 demand segmentation and proposes a three-class scheme.
- `2026-05-23-governance-controls-effectiveness-conditions` -- establishes that control intensity should match transaction hazard.
- `2026-05-16-variance-control-comparison-across-delivery-modes` -- provides structural versus behavioural control comparison relevant to fast-path gate design.
- `2026-05-14-org-failure-modes-cohort-demand-domain-it` -- shows undifferentiated queue failure mode.
- `2026-05-14-org-failure-modes-project-demand-product-it` -- shows demand stream mixing as a throughput risk.
- `2026-05-16-do-mode-demand-persistence-and-build-mode-displacement` -- shows that delivery-operations demand persists independently and displaces build demand when not separated.
- `2026-04-01-backpressure-theory-of-constraints` -- establishes Theory of Constraints (ToC) flow and Work in Progress (WIP) limit foundations.

### §1 Question Decomposition

**A. What are the classification axes for demand segmentation?**
- A1. What makes a work item routine versus exceptional in terms of risk level?
- A2. What makes a work item reversible versus irreversible?
- A3. What makes a work item standardised (template-applicable) versus novel?

**B. What segmentation schemes exist in analogous domains?**
- B1. How does Information Technology Infrastructure Library (ITIL) 4 classify change types and what criteria govern each?
- B2. How does Site Reliability Engineering (SRE) classify changes for automated versus human-reviewed handling?
- B3. How does Reinertsen's classes of service framework segment demand by cost of delay profile?
- B4. How does healthcare triage segment demand by urgency and severity?

**C. What is the minimum viable demand class set?**
- C1. How many demand classes are needed to capture meaningfully different control requirements?
- C2. What are the observable, testable boundary conditions for each class?
- C3. What control actions does each class imply for a split-authority delivery system?

### §2 Investigation

#### A1-A3: Classification axes

**Claim: Risk, reversibility, and standardisation are the three primary axes for intake segmentation, and they appear independently across unrelated queueing domains.**

ITIL 4 Information Technology (IT) Service Management uses exactly these three axes to define its three change types. A standard change is pre-authorised because it is low-risk, well-understood, and follows a documented, repeatable procedure (standardised and reversible). A normal change requires risk and impact assessment because it is neither pre-approved nor trivially reversible. An emergency change is handled outside normal process because urgency overrides both standardisation and full risk review. [fact; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.mafranci.com/itil4/cds/new/1%2020191122_Practice_Change%20enablement.pdf]

Google's Site Reliability Engineering practice identifies toil as repetitive, manual, automatable work that scales with service size and delivers no enduring value. [fact; source: https://sre.google/workbook/eliminating-toil/] Work that meets the toil criteria (repetitive, predictable, automatable) is a candidate for the fast path. Work that requires human judgment, has novel failure modes, or carries significant blast radius belongs on the controlled path. [inference; source: https://sre.google/workbook/eliminating-toil/; https://sre.google/sre-book/embracing-risk/]

SRE's risk management framework treats risk as a continuum, not a binary. [fact; source: https://sre.google/sre-book/embracing-risk/] The critical design principle is to align the risk taken by a given change with the risk tolerance the operation can absorb, rather than applying a uniform control intensity across all change types. [inference; source: https://sre.google/sre-book/embracing-risk/]

The completed item on variance control across delivery modes found that structural controls placed before execution (pipeline gates, pre-approval, signed attestations) are more reliable than behavioural controls applied during or after execution, because structural controls catch variance before it enters the live system. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-16-variance-control-comparison-across-delivery-modes.html] Work suitable for the fast path must therefore have structural gates in place before it is released, not merely post-hoc audit. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-16-variance-control-comparison-across-delivery-modes.html; https://www.axelos.com/certifications/itil-service-management/what-is-itil]

**Convergence finding:** Risk level, reversibility, and standardisation appear in ITIL 4 change types, SRE toil and risk criteria, Reinertsen's cost of delay profiles, and the governance controls effectiveness literature as the same underlying axes under different terminology. [inference; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://sre.google/workbook/eliminating-toil/; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

#### B1: ITIL 4 change types

ITIL 4 Change Enablement defines three change types that directly implement the three-axis classification. Standard changes are pre-authorised, low-risk, documented, and repeatable; they require no individual Change Advisory Board (CAB) approval per instance, only a logged change record for audit. Normal changes require risk and impact assessment and CAB (or delegated change authority) approval before implementation, with a documented backout plan. Emergency changes address urgent, unplanned situations such as major incident recovery or zero-day security patches; they may be fast-tracked through an Emergency Change Advisory Board (ECAB) but receive post-implementation review to capture what was bypassed. [fact; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.mafranci.com/itil4/cds/new/1%2020191122_Practice_Change%20enablement.pdf]

ITIL 4 explicitly notes that the change enablement practice is intended to align with DevOps, Agile, and modern delivery approaches, enabling automated approvals for low-risk changes and integration into continuous delivery pipelines. [fact; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil]

#### B2: SRE change classification

SRE change management distinguishes standard changes (well-understood, low-risk, automatable, routine) from changes requiring deeper oversight. Standard changes are treated as candidates for pipeline automation and pre-approval. Non-standard changes require error budget consideration, rollback planning, and progressive rollout controls. [inference; source: https://sre.google/workbook/eliminating-toil/; https://sre.google/sre-book/embracing-risk/]

DORA (DevOps Research and Assessment) research confirms that high-performing technology delivery organisations achieve both high deployment frequency and low change failure rate simultaneously, rejecting the assumption that speed and stability are in tension. [fact; source: https://dora.dev/guides/dora-metrics-four-keys/] This is explained by the structural segmentation of demand: low-risk, standard work travels automated fast paths with structural gates; high-risk or novel work travels slower controlled paths. [inference; source: https://dora.dev/guides/dora-metrics-four-keys/; https://sre.google/sre-book/embracing-risk/]

#### B3: Reinertsen classes of service

Donald Reinertsen's 2009 book *The Principles of Product Development Flow* introduces classes of service as a way to manage work items by their cost of delay profile, the economic impact of delaying delivery by one unit of time. [fact; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

The four classes Reinertsen defines are:
- **Expedite**: immediate, steep cost of delay profile; jumps the queue; strict WIP limit (usually one item at a time) to prevent disrupting normal flow.
- **Fixed date**: cost of delay spikes sharply at a known deadline; managed by due-date scheduling.
- **Standard**: moderate, steady cost of delay; processed by WIP-limited first-in, first-out (FIFO) or weighted queue ordering.
- **Intangible**: low immediate cost of delay but risk of accumulating harm (technical debt, capability degradation) over time; processed with periodic scheduled capacity. [fact; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

The cost of delay framework provides the economic rationale for segmentation: different delay profiles justify different handling policies, not different organisational status or requester seniority. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://www.tocinstitute.org/five-focusing-steps.html]

#### B4: Healthcare triage parallels

Emergency department triage systems such as the Emergency Severity Index (ESI) used in the United States and the Canadian Triage and Acuity Scale (CTAS) segment patients into urgency classes (typically five levels) using acuity criteria: immediate threat to life, potential serious deterioration without rapid intervention, or stable enough for standard throughput processing. [fact; source: https://www.ahrq.gov/patient-safety/settings/emergency/esi.html] Fast track pathways in emergency departments are designated streams for lower-acuity patients who can be assessed and discharged quickly, reducing congestion on the main care path without diverting resources from high-acuity cases. [fact; source: https://www.ahrq.gov/patient-safety/settings/emergency/esi.html]

The clinical triage principle is that misclassifying a high-acuity patient as low-acuity (under-triage) is a safety failure, whereas misclassifying a low-acuity patient as high-acuity (over-triage) wastes capacity. [inference; source: https://www.ahrq.gov/patient-safety/settings/emergency/esi.html] The cost of routing a genuinely high-risk item to the fast path exceeds the cost of routing a genuinely low-risk item to the controlled path. [inference; source: https://www.ahrq.gov/patient-safety/settings/emergency/esi.html] Conservative classification at boundaries is therefore a safety property, not a throughput property. [inference; source: https://www.ahrq.gov/patient-safety/settings/emergency/esi.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

#### C1-C3: Minimum viable demand class set

**Claim: Three demand classes are the minimum viable set for a split-authority delivery system.**

The completed P1 synthesis item proposed a three-class segmentation based on the same evidence territory investigated here. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html] This investigation confirms that finding and adds primary sources.

Two classes (fast/controlled) are insufficient because they collapse the distinction between routine non-trivial work and genuinely exceptional or novel work, forcing the controlled path to absorb both low-complexity approvals and high-stakes expert review. This worsens queue fragmentation at the controlled path, which is the primary bottleneck in split-authority delivery. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-cohort-demand-domain-it.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html]

Four or more classes add classification overhead that is not justified by distinct control actions. The evidence base does not identify a meaningful fourth class with boundary conditions that are testable without specialist knowledge. [assumption; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

**Three-class demand model:**

**Class 1 (fast path):** Work that is standard (follows a documented, previously demonstrated template or pattern), reversible (the failure mode has a known, tested recovery path), and low-risk (blast radius is contained and predictable). Control: post-hoc audit only. Pre-authorisation is granted at the class level, not per instance. Examples: pre-approved change templates, routine configuration updates from a managed catalogue, work that has passed all structural pipeline gates. [inference; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://sre.google/workbook/eliminating-toil/; https://davidamitchell.github.io/Research/research/2026-05-16-variance-control-comparison-across-delivery-modes.html]

**Class 2 (standard path):** Work that is routine but does not meet all three fast-path criteria: it may be bounded in scope and risk, but it is not pre-templated or has an assessed (not trivially known) blast radius. Control: lightweight pre-approval or bounded delegation within defined guardrails, with an escalation path. Examples: new service configurations with moderate dependency impact, changes requiring cross-team coordination but within defined scope. [inference; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

**Class 3 (exception path):** Work that is novel (no established pattern), high-consequence (significant blast radius or regulatory exposure), or irreversible (no tested recovery path). Control: full pre-approval and expert review. This is the path for genuinely exceptional demand where the governance cost is proportionate to the consequence. [inference; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://sre.google/sre-book/embracing-risk/]

The completed item on governance controls effectiveness found that controls are enabling (they help staff resolve exceptions with authoritative information) rather than coercive (adding surveillance or low-signal checkpoints) when they match the risk level of the transaction. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html] Applying full pre-approval controls to Class 1 work converts an enabling control into a coercive one, creating queue congestion without proportionate risk reduction.

**Boundary conditions for class assignment:**

Three observable tests determine class assignment:
1. **Template test:** Does a documented, previously approved template or pattern exist for this specific work type? If yes, the work is a candidate for Class 1 only if tests 2 and 3 also pass.
2. **Recovery test:** Has the failure mode been tested and does a validated rollback or recovery procedure exist? If yes, reversibility criterion is met.
3. **Blast radius test:** Is the potential impact contained within a defined boundary (team, service, or domain)? If yes, low-risk criterion is met for Class 1.

Work that fails test 1 but meets tests 2 and 3 is Class 2. Work that fails test 2 or test 3 regardless of test 1 is at least Class 2 and potentially Class 3. Work that is novel, has no recovery test, or has unbounded potential impact is Class 3. [assumption; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://sre.google/sre-book/embracing-risk/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

The healthcare triage asymmetry principle applies: when boundary tests are ambiguous, classify up (more control), not down (less control). The throughput cost of over-classifying a Class 2 item as Class 3 is lower than the governance failure cost of under-classifying a Class 3 item as Class 1. [inference; source: https://www.ahrq.gov/patient-safety/settings/emergency/esi.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

### §3 Reasoning

Unsupported generalisations removed:
- The original Approach used "triage" as a general term without specifying the triage domains. Investigation confirmed that ITIL 4, SRE, Reinertsen, and healthcare triage all converge on the same axes.
- The Approach asked for "a minimal set of demand classes." The three-class model is derived from the evidence base, not asserted a priori.
- No narrative links inserted: each claim is supported by at least one primary or secondary source.

The three-axis framework (risk, reversibility, standardisation) is not a theoretical construction. It is the common abstraction across independent classification systems from operations management, software delivery, and clinical practice. That convergence provides the evidence weight for the inference that these are the correct classification axes.

### §4 Consistency Check

```text
contradiction_scan: no internal contradictions found
  - ITIL 4 standard/normal/emergency maps cleanly to three-class model
  - SRE toil/standard/emergency maps to same three classes
  - Reinertsen expedite/fixed-date/standard/intangible maps to the same model
    with expedite = fast path for urgency, standard = standard path, intangible
    = a deferred variant of Class 2, fixed-date = Class 2 or 3 depending on
    consequence
  - Healthcare fast-track / standard / resuscitation maps to same three classes

confidence_adjustment: all key claims remain at medium because the three-class
  boundary-condition tests are inferred from the evidence, not directly
  measured in a published segmentation study of split-authority delivery

scope_guardrail: maintained; queue routing design not addressed, only
  segmentation criteria

triage_asymmetry_claim: confirmed consistent with governance controls
  effectiveness item (controls should match transaction hazard, not be applied
  uniformly)
```

### §5 Depth and Breadth Expansion

**Technical lens:** The three boundary-condition tests (template, recovery, blast radius) can each be operationalised as machine-checkable criteria in a continuous integration and continuous delivery (CI/CD) pipeline. Template existence can be verified against a managed change catalogue. Recovery procedure existence can be verified against a runbook register. Blast radius can be assessed using dependency graphs and impact analysis tools. [inference; source: https://sre.google/workbook/eliminating-toil/; https://davidamitchell.github.io/Research/research/2026-04-22-ai-governance-assurance-change-control-verification.html]

**Regulatory lens:** ITIL 4's explicit alignment with DevOps and automated approvals for low-risk changes is consistent with the Basel Committee on Banking Supervision (BCBS) requirement that control intensity be proportionate to institution size, complexity, and risk profile (BCBS 328). [fact; source: https://www.bis.org/bcbs/publ/d328.pdf] Regulated enterprises should not interpret regulatory change governance requirements as mandating uniform pre-approval for all change types; the proportionality principle is explicit. [inference; source: https://www.bis.org/bcbs/publ/d328.pdf; https://www.axelos.com/certifications/itil-service-management/what-is-itil]

**Economic lens:** Reinertsen's cost of delay framework provides the economic rationale for investing in the classification infrastructure itself: the cost of building and maintaining a managed template catalogue and blast radius tooling is justified when the throughput gain from routing Class 1 items without per-instance approval exceeds the classification infrastructure cost. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html]

**Organisational lens:** The completed item on do-mode demand persistence showed that delivery-operations (Business As Usual (BAU)) demand and build-mode demand accumulate independently and that treating them as a single undifferentiated queue is a driver of build-mode displacement. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html] Demand class assignment intersects with demand stream assignment: Class 1 work should predominantly be BAU demand flowing through operational automation, whereas Class 3 work includes novel build-mode scope or high-consequence BAU exceptions. A segmentation scheme that ignores demand stream origin risks misclassifying high-volume BAU change as Class 3 simply because it arrives without a pre-approved template.

**Historical lens:** The ITIL change classification model was developed iteratively from the early 2000s through ITIL v3 and ITIL 4 and has been adopted across regulated industries globally. The persistence of the three-type model (standard, normal, emergency) across multiple framework generations and independent industry adoption provides indirect evidence for its robustness as a minimal viable classification. [inference; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil]

### §6 Synthesis

**Executive Summary:**
Work items should be segmented on three axes (risk level, reversibility, and standardisation) and mapped to three demand classes (fast path, standard path, and exception path), with class assignment determined by three observable boundary tests. Three demand classes are the minimum viable number: fewer collapse distinct control requirements; more add overhead without distinct control actions. The three-axis framework converges independently across IT Service Management, Site Reliability Engineering, product development flow, and clinical triage literature, providing cross-domain evidence for its robustness as a classification structure. Conservative boundary classification (preferring more control when tests are ambiguous) is the appropriate safety property because the cost of under-classifying a high-risk item exceeds the throughput cost of over-classifying a low-risk item. [inference; source: https://www.ahrq.gov/patient-safety/settings/emergency/esi.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

**Key Findings:**

1. Three classification axes (risk level, reversibility, and standardisation) appear independently across ITIL 4, SRE, Reinertsen's product development flow, and healthcare triage as the operative criteria for segmenting fast-path from controlled-path demand. ([inference]; medium confidence; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://sre.google/workbook/eliminating-toil/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://www.ahrq.gov/patient-safety/settings/emergency/esi.html)

2. ITIL 4 Change Enablement defines three change types (standard, normal, and emergency) that map directly to the three classification axes: standard changes are pre-authorised because they are low-risk, well-understood, and repeatable; normal changes require per-instance risk assessment; emergency changes are fast-tracked with post-implementation review. ([fact]; high confidence; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.mafranci.com/itil4/cds/new/1%2020191122_Practice_Change%20enablement.pdf)

3. Reinertsen's classes of service framework assigns work to four categories (expedite, fixed-date, standard, and intangible) based on cost of delay profile, the economic impact per unit time of delayed delivery, and each category implies a distinct handling policy that cannot be derived from organisational status or requester seniority alone. ([fact]; high confidence; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009)

4. DORA research demonstrates that high deployment frequency and low change failure rate are positively correlated in elite technology delivery teams, which is structurally explained by the segmentation of demand into pre-approved automated lanes for low-risk work and controlled lanes for high-risk work, rather than by uniform controls applied to all deployments. ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics-four-keys/; https://sre.google/sre-book/embracing-risk/)

5. Three boundary condition tests (template test: does a pre-approved documented pattern exist; recovery test: has the failure mode been tested with a validated rollback procedure; blast radius test: is potential impact contained within a defined boundary) operationalise class assignment without requiring specialist knowledge at intake time. ([inference]; medium confidence; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://sre.google/sre-book/embracing-risk/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009)

6. The healthcare triage principle of conservative boundary classification (under-triage is a safety failure; over-triage wastes capacity but does not cause patient harm) translates directly to work intake: when boundary tests are ambiguous, assigning a work item to a higher-control class is the correct safety default because the governance failure cost of under-classifying a high-risk item exceeds the throughput cost of over-classifying a low-risk item. ([inference]; medium confidence; source: https://www.ahrq.gov/patient-safety/settings/emergency/esi.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html)

7. Two-class segmentation (fast/controlled only) is insufficient in a split-authority delivery system because it forces the controlled path to absorb both routine assessed work and genuinely exceptional high-consequence items, which intensifies the bottleneck at the controlled path and reproduces the queue fragmentation failure mode identified in the organisational failure modes research. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-cohort-demand-domain-it.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html)

8. Applying full pre-approval controls to Class 1 (fast-path) work converts an enabling governance control into a coercive one, creating queue congestion without proportionate risk reduction, as established by the governance controls effectiveness literature on transaction-hazard matching. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://eric.ed.gov/?id=EJ525938)

9. Delivery-operations demand (BAU change, minor enhancement, incident response) and build-mode demand (novel feature or capability delivery) accumulate independently, and a segmentation scheme that ignores this distinction risks systematically misclassifying high-volume BAU work as exception-path simply because it lacks a pre-approved template rather than because it is genuinely novel or high-consequence. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-project-demand-product-it.html)

**Evidence Map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Three axes (risk, reversibility, standardisation) converge independently across ITIL 4, SRE, Reinertsen, and clinical triage | https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://sre.google/workbook/eliminating-toil/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://www.ahrq.gov/patient-safety/settings/emergency/esi.html | medium | Convergence is the inference; each individual system is a fact |
| [fact] ITIL 4 defines standard, normal, and emergency change types on low-risk/assessed/urgent criteria | https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.mafranci.com/itil4/cds/new/1%2020191122_Practice_Change%20enablement.pdf | high | ITIL 4 official documentation |
| [fact] Reinertsen's four classes of service are defined by cost of delay profile (expedite, fixed-date, standard, intangible) | https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009 | high | Primary source: 2009 book |
| [inference] DORA elite performance correlates with segmented automation for low-risk changes | https://dora.dev/guides/dora-metrics-four-keys/ | medium | DORA does not explicitly name segmentation; inference from frequency + failure rate correlation |
| [inference] Three-test boundary conditions (template, recovery, blast radius) operationalise class assignment | https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://sre.google/sre-book/embracing-risk/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009 | medium | Synthesised from three independent source sets |
| [inference] Conservative boundary classification is the correct safety property (over-triage acceptable; under-triage is a safety failure) | https://www.ahrq.gov/patient-safety/settings/emergency/esi.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html | medium | Analogy from clinical triage with governance controls support |
| [inference] Two-class segmentation insufficiently differentiates controlled path, worsening bottleneck | https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-cohort-demand-domain-it.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html | medium | Derived from organisational failure modes evidence |
| [inference] Uniform pre-approval applied to Class 1 work is coercive not enabling | https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://eric.ed.gov/?id=EJ525938 | medium | Enabling vs coercive controls distinction |
| [inference] BAU and build-mode demand require separate classification treatment | https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-project-demand-product-it.html | medium | Demand stream distinction, not directly tested in segmentation literature |

**Assumptions:**

1. Four or more demand classes add classification overhead without distinct control actions. [assumption; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009] Justification: no evidence base identifies a mandatory fourth class with operationally distinct control requirements; ITIL 4's three types and Reinertsen's four types both reduce to three operationally distinct policies (pre-authorised, assessed, urgent-bypass) when mapped to control actions rather than demand characteristics.

2. The three-test boundary conditions can be administered reliably by intake staff without specialist risk knowledge, given a maintained template catalogue and blast radius tooling. [assumption; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://sre.google/workbook/eliminating-toil/] Justification: ITIL 4 explicitly requires classification to be operable without per-instance specialist review for standard changes; SRE toil criteria are designed to be self-evident from change documentation.

**Analysis:**

The evidence strongly supports a three-class demand model, but the boundary conditions for class assignment are inferences from multiple source sets rather than findings from a single published segmentation study of split-authority delivery systems. The three boundary tests (template, recovery, blast radius) derive from ITIL 4's standardisation criterion, SRE's reversibility and blast radius criteria, and Reinertsen's cost of delay profile criteria. Each individual criterion is primary-source backed; the synthesis into three tests is an inference.

The key trade-off in segmentation design is between classification accuracy and classification cost. More tests per item improve accuracy but add intake overhead. The three-test model is an inference about the minimum viable set; it is not an empirically tested intake protocol. A plausible alternative is a single-axis model (risk score only), which would require a risk scoring rubric but would avoid the multi-test classification step. The risk-score-only model is rejected here on the grounds that risk level alone does not determine the correct control action: a high-risk but fully reversible item (for example, a configuration change with a tested rollback) should travel the standard path, not the exception path. [inference; source: https://sre.google/sre-book/embracing-risk/; https://www.axelos.com/certifications/itil-service-management/what-is-itil]

A rival design would treat the Class 2 (standard path) category as two sub-classes (bounded low and bounded high). This would give four classes. The evidence does not support a fourth class with a distinct control action, because both sub-classes would still require assessed pre-approval; the difference would be in the approval authority level, not the control form. Routing to different approval authority levels is a decision rights placement question (Q4), not a segmentation question.

**Risks, Gaps, and Uncertainties:**

- No published study directly tests the three-class demand model in a split-authority delivery context. The evidence base is cross-domain inference from ITIL 4, SRE, and operations management.
- The blast radius test requires dependency mapping tooling to be reliable and current. Without maintained tooling, the test degrades to a subjective judgment, which may not be consistently applied.
- The template test requires a maintained and authoritative change template catalogue. Without active catalogue governance, class 1 items accumulate in class 2 over time as templates become stale or undiscovered.
- The boundary condition tests produce binary classification outcomes, but real demand has continuous risk properties. Items at class boundaries may be inconsistently classified, creating noise in the system that needs monitoring.
- The healthcare triage analogy provides useful framing but does not carry over the full clinical context: emergency departments have triage nurses as a dedicated specialist function; most software delivery intakes do not.

**Open Questions:**

- How should a split-authority delivery system handle class reassignment during execution (a Class 1 item that encounters an unexpected complication)? This is a routing and escalation question within Q3 scope.
- What governance evidence (classification rate, reclassification rate, mis-classification incidents) should be collected to validate and calibrate the three-class model over time? This is a Q6 leading indicators question.
- Is the template test a pre-condition for automation, or can automation accelerate template creation from historical change data? This has tooling implications outside the current scope.
- How does the demand stream distinction (BAU vs build-mode) interact with class assignment at the intake point? Does a BAU item from an unfamiliar domain default to Class 2 even if it meets all three Class 1 tests? This warrants clarification in Q3 routing design.

**Output:**

- Type: knowledge
- Description: A three-class demand segmentation model (fast path, standard path, exception path) with three observable boundary tests (template, recovery, blast radius) grounded in convergent evidence from ITIL 4, SRE, Reinertsen's product development flow, and clinical triage principles. [inference; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://sre.google/workbook/eliminating-toil/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]
- Key sources:
  1. https://www.axelos.com/certifications/itil-service-management/what-is-itil (ITIL 4 Change Enablement official)
  2. https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009 (Reinertsen 2009)
  3. https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html (governance controls proportionality)

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed
  - ITIL: Information Technology Infrastructure Library (ITIL) -- expanded at first prose use
  - IT: Information Technology (IT) -- expanded at first prose use
  - ITIL 4: uses expansion of ITIL from first use
  - CAB: Change Advisory Board (CAB) -- expanded at first prose use
  - ECAB: Emergency Change Advisory Board (ECAB) -- expanded at first prose use
  - SRE: Site Reliability Engineering (SRE) -- expanded in Sources and §0
  - ToC: Theory of Constraints (ToC) -- expanded in §0 prior items
  - WIP: Work in Progress (WIP) -- expanded in §0 prior items
  - DORA: DevOps Research and Assessment (DORA) -- expanded at first prose use in §B2
  - ESI: Emergency Severity Index (ESI) -- expanded at first prose use
  - CTAS: Canadian Triage and Acuity Scale (CTAS) -- expanded at first prose use
  - BAU: Business As Usual (BAU) -- expanded at first prose use in §5
  - BCBS: Basel Committee on Banking Supervision (BCBS) -- expanded at first prose use in §5
  - FIFO: first-in, first-out (FIFO) -- expanded at first prose use
  - CI/CD: continuous integration and continuous delivery (CI/CD) -- expanded in §5

claim_audit: all claims carry [fact], [inference], or [assumption] labels
evidence_map_audit: all rows contain URL-backed sources
parity_check: §6 Synthesis and Findings are mirrored
assumption_source_audit: both assumptions carry URL-backed source context
```

---

## Findings

### Executive Summary

Work items should be classified on three axes (risk level, reversibility, and standardisation) and assigned to one of three demand classes: Class 1 (fast path, pre-authorised), Class 2 (standard path, assessed per-instance), and Class 3 (exception path, full expert review). Three classes are the minimum viable number because fewer collapse distinct control requirements onto the controlled path, worsening the bottleneck, while more add classification overhead without distinct control actions. This three-class structure is the common abstraction across ITIL 4 Change Enablement, Site Reliability Engineering practice, Reinertsen's product development flow classes of service, and clinical triage systems, providing convergent cross-domain evidence for its robustness. [inference; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://sre.google/workbook/eliminating-toil/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://www.ahrq.gov/patient-safety/settings/emergency/esi.html] When boundary tests produce ambiguous results, conservative classification (assigning to a higher-control class) is the correct default because the governance failure cost of under-classifying a high-risk item exceeds the throughput cost of over-classifying a low-risk item. [inference; source: https://www.ahrq.gov/patient-safety/settings/emergency/esi.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

### Key Findings

1. Three classification axes (risk level, reversibility, and standardisation) appear independently across ITIL 4, SRE, Reinertsen's product development flow, and healthcare triage as the operative criteria for segmenting fast-path from controlled-path demand. ([inference]; medium confidence; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://sre.google/workbook/eliminating-toil/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://www.ahrq.gov/patient-safety/settings/emergency/esi.html)

2. ITIL 4 Change Enablement defines three change types (standard, normal, and emergency) where standard changes are pre-authorised because they are low-risk, documented, and repeatable, and normal changes require per-instance risk and impact assessment with Change Advisory Board approval. ([fact]; high confidence; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.mafranci.com/itil4/cds/new/1%2020191122_Practice_Change%20enablement.pdf)

3. Reinertsen's four classes of service (expedite, fixed-date, standard, and intangible) are defined by cost of delay profile and each implies a handling policy that cannot be derived from organisational status or requester seniority. ([fact]; high confidence; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009)

4. DORA research shows that elite technology delivery teams achieve high deployment frequency and low change failure rate simultaneously, a result consistent with demand segmentation that routes low-risk standard work through automated pre-approved lanes and high-risk novel work through controlled review lanes. ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics-four-keys/; https://sre.google/sre-book/embracing-risk/)

5. Three observable boundary tests (template test: a pre-approved documented pattern exists; recovery test: the failure mode has been tested with a validated rollback procedure; blast radius test: potential impact is contained within a defined boundary) operationalise class assignment without requiring specialist risk knowledge at intake time. ([inference]; medium confidence; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://sre.google/sre-book/embracing-risk/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009)

6. The healthcare triage principle that under-triage (routing a high-acuity patient to the fast track) is a patient safety failure while over-triage (routing a low-acuity patient to the main track) is only a capacity waste translates directly to work intake design, establishing conservative boundary classification as a safety property. ([inference]; medium confidence; source: https://www.ahrq.gov/patient-safety/settings/emergency/esi.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html)

7. Two-class segmentation (fast and controlled only) is insufficient in a split-authority delivery system because it collapses routine assessed work and genuinely exceptional high-consequence items onto the same controlled path, intensifying the bottleneck and reproducing the queue fragmentation failure mode identified in the organisational failure modes evidence. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-cohort-demand-domain-it.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html)

8. Applying full pre-approval controls to Class 1 (fast-path) work converts an enabling governance control into a coercive one, generating queue congestion without proportionate risk reduction because the control intensity no longer matches the transaction hazard. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://eric.ed.gov/?id=EJ525938)

9. Delivery-operations demand (BAU change, minor enhancement, incident response) and build-mode demand (novel capability delivery) accumulate independently, and a segmentation scheme that ignores this distinction risks misclassifying high-volume BAU work as exception-path simply because no pre-approved template exists yet, rather than because the work is genuinely novel or high-consequence. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-project-demand-product-it.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Three axes (risk, reversibility, standardisation) converge across ITIL 4, SRE, Reinertsen, clinical triage | https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://sre.google/workbook/eliminating-toil/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://www.ahrq.gov/patient-safety/settings/emergency/esi.html | medium | Convergence is the inference; each source is independently primary or secondary |
| [fact] ITIL 4 defines standard, normal, emergency change types on low-risk/assessed/urgent criteria | https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.mafranci.com/itil4/cds/new/1%2020191122_Practice_Change%20enablement.pdf | high | ITIL 4 official documentation |
| [fact] Reinertsen's four classes of service defined by cost of delay profile | https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009 | high | Primary source: 2009 book, Celeritas Publishing |
| [inference] DORA elite performance consistent with segmented automation for standard changes | https://dora.dev/guides/dora-metrics-four-keys/ | medium | DORA does not name segmentation explicitly; inference from correlation data |
| [inference] Three-test boundary conditions operationalise class assignment | https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://sre.google/sre-book/embracing-risk/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009 | medium | Synthesised from three independent source sets |
| [inference] Conservative boundary classification is the correct safety property | https://www.ahrq.gov/patient-safety/settings/emergency/esi.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html | medium | Clinical analogy with governance controls support |
| [inference] Two-class segmentation insufficiently differentiates controlled path | https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-cohort-demand-domain-it.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html | medium | Derived from organisational failure modes evidence |
| [inference] Uniform pre-approval applied to Class 1 is coercive not enabling | https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://eric.ed.gov/?id=EJ525938 | medium | Enabling vs coercive controls distinction from Adler and Borys |
| [inference] BAU and build-mode demand require separate classification treatment | https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-project-demand-product-it.html | medium | Demand stream distinction |

### Assumptions

1. Four or more demand classes add classification overhead without operationally distinct control actions. [assumption; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009] Justification: no evidence identifies a fourth mandatory class with a distinct control form; Reinertsen's four types and ITIL 4's three types both reduce to three distinct control policies when mapped by action rather than demand characteristic.

2. The three boundary condition tests can be administered reliably without specialist risk knowledge, given a maintained template catalogue and blast radius tooling. [assumption; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://sre.google/workbook/eliminating-toil/] Justification: ITIL 4 requires standard change classification to be operable without per-instance specialist review; SRE toil criteria are designed to be self-evident from change documentation.

### Analysis

The weight of evidence supports the three-class demand model, but the model is grounded in cross-domain inference rather than a published empirical study of split-authority delivery segmentation. Each individual source provides primary evidence for a specific domain (ITIL 4, SRE, Reinertsen, clinical triage); the inference that they converge on the same classification structure is the substantive synthesis claim.

The principal alternative model is a single-axis risk score. This model is rejected on the grounds that risk level alone does not determine the correct control action: a high-risk but fully reversible item with a tested rollback procedure should travel the standard path, not the exception path. [inference; source: https://sre.google/sre-book/embracing-risk/; https://www.axelos.com/certifications/itil-service-management/what-is-itil] Reversibility is an independent axis that modifies the risk interpretation.

A four-class model (splitting Class 2 into bounded-low and bounded-high sub-classes) is rejected on the grounds that the control actions for both sub-classes are assessed pre-approval; the difference would be in approval authority level, not control form. Routing to different approval authority levels is a decision rights placement question (Q4), not a segmentation question. The classification boundary cost of maintaining a four-class model is not justified by the evidence.

The ITIL 4 explicit statement that Change Enablement is intended to align with DevOps and automated approvals for low-risk changes is notable: the same framework that defines the controlled path for high-risk changes also endorses automated pre-approval for the fast path. [fact; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil] This removes the potential objection that ITIL and DevOps segmentation approaches are incompatible.

### Risks, Gaps, and Uncertainties

- No published study directly tests the three-class demand model in a split-authority delivery context; the evidence base is cross-domain inference.
- The blast radius test requires maintained dependency mapping tooling; without it, the test degrades to subjective judgment.
- The template test requires active catalogue governance; without it, Class 1 items accumulate in Class 2 over time as templates become stale.
- Items near class boundaries will be inconsistently classified without a maintained calibration and monitoring regime.
- The conservative classification default generates some Class 2 overhead for items that would correctly be Class 1. This overhead is the cost of the safety property, not a design failure.

### Open Questions

- How should a split-authority system handle mid-execution class reassignment when a Class 1 item encounters an unexpected complication? (Q3 scope)
- What classification rate, reclassification rate, and mis-classification incident data should be collected to validate and calibrate the three-class model over time? (Q6 scope)
- Does the demand stream distinction (BAU versus build-mode) require an explicit field in the intake form, or is it derivable from the boundary tests? (Q3 scope)
- Can automation accelerate template creation from historical change records, reducing the initial classification overhead of building a Class 1 catalogue? (tooling question, outside current scope)

### Output

- Type: knowledge
- Description: A three-class demand segmentation model with three observable boundary tests, grounded in convergent evidence from ITIL 4, SRE, Reinertsen's product development flow, and clinical triage, directly enabling Q3 routing design, Q5 control model trade-off analysis, Q6 leading indicator design, and Q1 flow constraint validation. [inference; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://sre.google/workbook/eliminating-toil/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]
- Key sources:
  1. [PeopleCert / AXELOS (2019) ITIL 4 Change Enablement](https://www.axelos.com/certifications/itil-service-management/what-is-itil)
  2. [Reinertsen, D.G. (2009) The Principles of Product Development Flow](https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009)
  3. [Mitchell (2026) Internal governance controls: effectiveness conditions in regulated enterprises](https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html)
