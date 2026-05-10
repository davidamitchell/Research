---
review_count: 2
title: "Key-person dependency and Basel execution, delivery, and process-management risk linkage"
added: 2026-05-09T22:56:47+00:00
status: reviewing
priority: high
blocks: []
tags: [organisation, workflow, operational-risk]
started: 2026-05-10T20:39:31+00:00
completed: ~
output: [knowledge]
cites: [2026-05-09-basel-iso-nist-shadow-workforce-risk-classification]
related: [2026-05-09-cobit-cmmi-defined-process-risk-mitigation, 2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis, 2026-05-08-integrated-cascading-failure-agentic-vs-generative-ai-risk]
superseded_by: ~
supersedes: 2026-05-09-enterprise-risk-workforce-shadow-systems
item_type: primary
confidence: medium
versions: []
---

# Key-person dependency and Basel execution, delivery, and process-management risk linkage

## Research Question

How should key-person dependency in workforce-critical processes be mapped to execution, delivery, and process-management risk categories in Basel Committee framing?

## Scope

**In scope:**
- Key-person dependency risk mechanisms in operational processes
- Basel-compatible classification and reporting language
- Escalation triggers and control expectations

**Out of scope:**
- Individual performance management practices
- Enterprise-specific organizational redesign

**Constraints:** Prioritize primary Basel sources and ensure classification guidance is explicit and auditable.

## Context

Key-person dependency, meaning control-critical reliance on one person's presence or tacit knowledge to execute, deliver, or manage a process, is often treated informally as a staffing problem even though Basel Committee sources classify the resulting exposure through broader operational-risk, loss-event, resilience, and risk-data-control categories rather than through a standalone named key-person category. [inference; source: https://www.bis.org/bcbs/publ/d515.pdf; https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf]

## Approach

1. Extract Basel language relevant to operational risk, execution, delivery, and process-management loss events, operational resilience, and risk-data controls.
2. Define mapping rules from key-person dependency patterns to Basel categories and reporting language.
3. Identify escalation triggers and control expectations implied by each mapped category.

## Sources

- [x] [Basel Committee on Banking Supervision (2021) Revisions to the Principles for the Sound Management of Operational Risk](https://www.bis.org/bcbs/publ/d515.pdf) - core operational-risk definition and governance expectations
- [x] [Basel Committee on Banking Supervision (2021) Principles for operational resilience](https://www.bis.org/bcbs/publ/d516.pdf) - critical-operations dependency mapping, tolerance for disruption, and business-continuity triggers
- [x] [Basel Committee on Banking Supervision (2013) Principles for effective risk data aggregation and risk reporting](https://www.bis.org/publ/bcbs239.pdf) - automation, spreadsheet, database, and control expectations
- [x] [Basel Committee on Banking Supervision (2001) Operational Risk Loss Data](https://www.bis.org/bcbs/qisoprisknote.pdf) - Basel loss-event type wording for execution, delivery, and process management
- [x] [Mitchell (2026) Basel Committee on Banking Supervision (BCBS), International Organization for Standardization (ISO), and National Institute of Standards and Technology (NIST): classifying shadow workforce-system risk](https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html) - adjacent completed item on framework-level shadow-workforce classification

## Related

- [Mitchell (2026) Basel Committee on Banking Supervision (BCBS), International Organization for Standardization (ISO), and National Institute of Standards and Technology (NIST): classifying shadow workforce-system risk](https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html)
- [Mitchell (2026) Control Objectives for Information and Related Technologies (COBIT) and Capability Maturity Model Integration (CMMI): process-definition requirements for risk mitigation](https://davidamitchell.github.io/Research/research/2026-05-09-cobit-cmmi-defined-process-risk-mitigation.html)
- [Mitchell (2026) Systems capability debt, citizen development, and agentic Artificial Intelligence (AI) risk: is the causal chain and sequencing imperative a novel contribution?](https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html)

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. Sections 0 to 5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: How should key-person dependency in workforce-critical processes be mapped to Basel Committee on Banking Supervision framing for operational risk, execution, delivery and process management, operational resilience, and risk-data control?
- Working definition: key-person dependency means that one person's availability, tacit knowledge, or approval authority is necessary for a material process step to be executed, delivered, or managed without breakdown.
- Scope: classify the dependency pattern in Basel language, define auditable mapping rules, and identify escalation triggers and control expectations, without turning the item into enterprise-specific organization redesign.
- Constraints: primary Basel sources first, explicit auditable classification logic, Uniform Resource Locator (URL)-backed citations only, and every abbreviation expanded on first use in the document.
- Output: knowledge item with mirrored synthesis and Findings sections, a Basel mapping table, and direct reporting-language guidance.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html] Prior completed-item sweep found adjacent repository work that classifies unmanaged workforce systems across Basel Committee on Banking Supervision, International Organization for Standardization, and National Institute of Standards and Technology frameworks, but that item does not isolate the narrower Basel question of how single-person dependency should be reported against the Basel loss-event and resilience surfaces.

### §1 Question Decomposition

- **Root question:** How should a workforce-critical key-person dependency be classified in Basel-compatible language?
- **A. Basel baseline**
  - A1. Does Basel Committee on Banking Supervision define key-person dependency as a standalone category?
  - A2. Which general Basel category captures a process that fails because one person's knowledge or availability is indispensable?
- **B. Execution, delivery, and process-management linkage**
  - B1. What does the Basel loss-event type "Execution, Delivery & Process Management" cover?
  - B2. Which key-person dependency patterns fit that loss-event type most directly?
- **C. Escalation into wider Basel control surfaces**
  - C1. When does the same dependency become an operational-resilience issue?
  - C2. When does the same dependency become a risk-data-aggregation and reporting issue under Basel Committee on Banking Supervision 239?
- **D. Control and reporting synthesis**
  - D1. What Basel-compatible reporting sentence should describe the dependency?
  - D2. Which control expectations and escalation triggers follow from each mapping?

### §2 Investigation

#### Prior completed-item sweep

- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html] The nearest completed item already establishes that shadow workforce-system handling is an operational-risk problem in Basel Committee on Banking Supervision terms when critical data or process execution depends on unmanaged control surfaces.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html] This item therefore narrows the question from system classification to human-dependency classification: how the same exposure should be written in Basel event-type, resilience, and control language when the weakest point is one person's irreplaceable role in execution.

#### A. Basel baseline classification

- [fact; source: https://www.bis.org/bcbs/publ/d515.pdf] Basel Committee on Banking Supervision defines operational risk as "the risk of loss resulting from inadequate or failed internal processes, people and systems or from external events," and states that operational risk is inherent in all banking products, activities, processes and systems.
- [inference; source: https://www.bis.org/bcbs/publ/d515.pdf] Basel Committee on Banking Supervision therefore does not need a standalone named "key-person dependency" category to classify the pattern, because a process that can fail when one indispensable person is absent already fits the operational-risk definition through failed people and process design.
- [inference; source: https://www.bis.org/bcbs/publ/d515.pdf] The most Basel-compatible base classification is: operational risk driven by concentration of execution knowledge, approval authority, or process custody in one person.

#### B. Execution, delivery, and process-management linkage

- [fact; source: https://www.bis.org/bcbs/qisoprisknote.pdf] Basel Committee on Banking Supervision's loss-event classification note defines "Execution, Delivery & Process Management" as losses from failed transaction processing or process management, and from relations with trade counterparties and vendors.
- [fact; source: https://www.bis.org/bcbs/qisoprisknote.pdf] The same Basel Committee on Banking Supervision note lists examples under that loss-event type including transaction capture, execution and maintenance failures, miscommunication, data-entry or loading error, missed deadline or responsibility, model or system misoperation, accounting or entity-attribution error, other task misperformance, and delivery failure.
- [inference; source: https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d515.pdf] A key-person dependency maps most directly into "Execution, Delivery & Process Management" when the single-person dependency sits inside a recurring operational step such as handoff, reconciliation, transaction capture, deadline ownership, exception handling, or delivery coordination.
- [inference; source: https://www.bis.org/bcbs/qisoprisknote.pdf] The best fit is weaker when the key-person dependency is only latent and has not yet affected an execution step, but the Basel loss-event taxonomy becomes directly applicable as soon as the dependency threatens missed responsibility, task misperformance, miscommunication, or delivery failure.

#### C. Operational-resilience trigger

- [fact; source: https://www.bis.org/bcbs/publ/d516.pdf] Basel Committee on Banking Supervision defines operational resilience as the ability of a bank to deliver critical operations through disruption and defines tolerance for disruption as the level of disruption from any type of operational risk that a bank is willing to accept given a range of severe but plausible scenarios.
- [fact; source: https://www.bis.org/bcbs/publ/d516.pdf] Principle 4 of the operational-resilience guidance requires banks to identify and document the people, technology, processes, information, facilities, and the interconnections and interdependencies among them that are needed to deliver critical operations.
- [fact; source: https://www.bis.org/bcbs/publ/d516.pdf] The same guidance says business-continuity plans should address disruption that impacts key personnel and should clearly set out the internal decision-making process and the triggers for invoking the bank's business-continuity plan.
- [inference; source: https://www.bis.org/bcbs/publ/d516.pdf] A key-person dependency becomes an operational-resilience issue when the person's unavailability could stop or materially degrade a critical operation, because the dependency is then part of the bank's mapped people-process-information interdependency set and must be tested against tolerance for disruption.

#### D. Risk-data and reporting trigger

- [fact; source: https://www.bis.org/publ/bcbs239.pdf] Basel Committee on Banking Supervision 239 requires risk data to be aggregated on a largely automated basis so as to minimise the probability of errors.
- [fact; source: https://www.bis.org/publ/bcbs239.pdf] Basel Committee on Banking Supervision 239 says that where a bank relies on manual processes and desktop applications such as spreadsheets and databases, it should have effective mitigants in place, including end-user computing policies and procedures and other effective controls that are consistently applied across the bank's processes.
- [inference; source: https://www.bis.org/publ/bcbs239.pdf] When the key person owns a manual spreadsheet, database, or other desktop workflow that feeds risk data aggregation or reporting, the same dependency should be classified not only as people-process operational risk but also as a Basel Committee on Banking Supervision 239 data-architecture, automation, and control weakness.

#### E. Mapping rules, escalation triggers, and controls

- [inference; source: https://www.bis.org/bcbs/publ/d515.pdf; https://www.bis.org/bcbs/qisoprisknote.pdf] Mapping rule 1: classify every material key-person dependency at minimum as operational risk when one person's absence, tacit knowledge, or approval monopoly could cause process failure.
- [inference; source: https://www.bis.org/bcbs/qisoprisknote.pdf] Mapping rule 2: add the Basel loss-event type "Execution, Delivery & Process Management" when the dependency threatens processing accuracy, deadline performance, handoffs, reconciliations, or task execution in a repeatable operating process.
- [inference; source: https://www.bis.org/bcbs/publ/d516.pdf] Mapping rule 3: add operational-resilience dependency language when loss of the individual could breach tolerance for disruption for a critical operation or when the dependency appears in the mapped people-process-information chain for that operation.
- [inference; source: https://www.bis.org/publ/bcbs239.pdf] Mapping rule 4: add Basel Committee on Banking Supervision 239 language when the person is the effective control point for manual risk-data aggregation, reporting, spreadsheet logic, desktop database maintenance, or other non-automated risk-information production.
- [inference; source: https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf] Escalation trigger 1: escalate when the dependency could interrupt a critical operation, require invocation of business-continuity decision triggers, or exceed tolerance for disruption.
- [inference; source: https://www.bis.org/publ/bcbs239.pdf; https://www.bis.org/bcbs/qisoprisknote.pdf] Escalation trigger 2: escalate when the dependency creates risk of missed responsibility, miscommunication, delivery failure, or inaccurate, incomplete, or untimely risk data because the process cannot be executed or checked without the individual.
- [inference; source: https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf] Control expectation: Basel Committee sources support documenting the dependency, mapping it into people-process-information interdependencies, defining business-continuity decision triggers, and reducing reliance on manual desktop workflows through automation or consistently applied mitigants and controls.
- [assumption; source: https://www.bis.org/bcbs/publ/d515.pdf; https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf] This item assumes the workforce-critical process affects operational delivery, control execution, or risk reporting; if the process were low-materiality and outside critical operations and risk reporting, Basel classification would still point to control weakness but the escalation threshold would be lower.

### §3 Reasoning

- [inference; source: https://www.bis.org/bcbs/publ/d515.pdf; https://www.bis.org/bcbs/qisoprisknote.pdf] Basel Committee on Banking Supervision operational-risk guidance provides the base classification and the loss-event taxonomy provides the most precise event-type label, so the dependency is best described as a causal driver inside an operational-risk event rather than as a standalone event class.
- [inference; source: https://www.bis.org/bcbs/qisoprisknote.pdf] The fit to "Execution, Delivery & Process Management" is strongest when the dependency creates immediate failure modes in transaction execution, handoff, deadline, reconciliation, or delivery activities, because those examples match the published loss-event wording directly.
- [inference; source: https://www.bis.org/bcbs/publ/d516.pdf] Operational-resilience language is not redundant with the loss-event label, because it answers a different supervisory question: whether the dependency jeopardizes the bank's ability to deliver a critical operation through disruption.
- [inference; source: https://www.bis.org/publ/bcbs239.pdf] Basel Committee on Banking Supervision 239 should be added only when the key person also controls manual risk-data or reporting logic, because that source is about risk-data architecture, automation, and manual-tool control rather than about all workforce dependencies generally.

### §4 Consistency Check

- [inference; source: https://www.bis.org/bcbs/publ/d515.pdf; https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf] The sources do not contradict one another: Basel Committee on Banking Supervision 2021 operational-risk guidance defines the broad risk class, the loss-event note defines the closest execution-focused event type, operational-resilience guidance defines the continuity threshold, and Basel Committee on Banking Supervision 239 defines the risk-data control threshold.
- [inference; source: https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d516.pdf] The main ambiguity is not whether the dependency matters, but which additional Basel surface is activated beyond base operational risk, and that depends on whether the exposure manifests in process execution, critical-operation continuity, or risk-data production.
- [fact; source: https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d515.pdf] Confidence remains medium because the loss-event type wording comes from an older Basel Committee on Banking Supervision operational-risk classification note rather than from the 2021 principles document itself, even though the two sources are consistent.

### §5 Depth and Breadth Expansion

- [inference; source: https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d515.pdf] Technical lens: a key-person dependency is rarely just a labor-capacity issue; it is usually evidence that process design, task decomposition, or control custody is too concentrated to be executed reliably under normal variance.
- [inference; source: https://www.bis.org/bcbs/publ/d516.pdf] Governance lens: once the dependency sits inside a critical operation, supervisors should expect it to be visible in formal interdependency maps, tolerance-for-disruption analysis, and business-continuity invocation logic rather than in informal manager knowledge alone.
- [inference; source: https://www.bis.org/publ/bcbs239.pdf] Data lens: when one person maintains spreadsheet or desktop-database logic for risk reporting, the problem is not only absence risk but also opacity, weak auditability, and higher error probability from low-automation workflows.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html; https://www.bis.org/bcbs/publ/d516.pdf] Cross-item lens: this item sharpens the adjacent shadow-workforce classification by showing that Basel Committee on Banking Supervision supervision can treat the same weakness simultaneously as operational-risk causation, execution-process failure risk, and critical-operation dependency depending on where the single-person bottleneck sits.

### §6 Synthesis

**Executive summary:**

Key-person dependency in a workforce-critical process should be classified first as Basel Committee on Banking Supervision operational risk, and then mapped specifically to "Execution, Delivery & Process Management" when the dependency threatens recurring process execution, handoffs, deadlines, or delivery outcomes. [inference; source: https://www.bis.org/bcbs/publ/d515.pdf; https://www.bis.org/bcbs/qisoprisknote.pdf]
The same dependency should be escalated into operational-resilience reporting when the person's unavailability could disrupt a critical operation, because Basel Committee on Banking Supervision guidance requires banks to map people, processes, information, technology, facilities, and their interdependencies against tolerance for disruption and business-continuity triggers. [inference; source: https://www.bis.org/bcbs/publ/d516.pdf]
If the dependency also sits inside manual spreadsheet or desktop-database production of risk data or risk reports, Basel Committee on Banking Supervision 239 adds a separate classification as a risk-data-aggregation, automation, and control weakness requiring effective mitigants or more automated design. [inference; source: https://www.bis.org/publ/bcbs239.pdf]
The strongest Basel-compatible reporting pattern is therefore to write key-person dependency as a causal driver and then name the activated Basel surface or surfaces: base operational risk, execution-delivery-process-management event risk, operational-resilience dependency risk, and Basel Committee on Banking Supervision 239 control weakness where applicable. [inference; source: https://www.bis.org/bcbs/publ/d515.pdf; https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf]

**Key findings:**

1. **Basel Committee on Banking Supervision guidance supports classifying key-person dependency as operational risk because a process that depends on one indispensable person's availability or tacit knowledge fits the published definition of loss arising from failed people, processes, and systems.** ([inference]; medium confidence; source: https://www.bis.org/bcbs/publ/d515.pdf)
2. **The Basel loss-event type "Execution, Delivery & Process Management" is the closest specific event classification when the dependency threatens transaction capture, execution, maintenance, deadlines, responsibilities, reconciliations, handoffs, or delivery steps, because the published category explicitly covers failed transaction processing and process management.** ([inference]; medium confidence; source: https://www.bis.org/bcbs/qisoprisknote.pdf)
3. **A workforce-critical key-person dependency should be escalated into operational-resilience reporting when the person's absence could disrupt a critical operation, because banks are required to map people, technology, processes, information, facilities, and their interdependencies against tolerance for disruption.** ([inference]; medium confidence; source: https://www.bis.org/bcbs/publ/d516.pdf)
4. **Basel Committee on Banking Supervision guidance also expects business-continuity planning to address disruption that impacts key personnel and to define internal decision-making and invocation triggers, so a single-person bottleneck in a critical process is not Basel-compatible as an undocumented local workaround.** ([inference]; medium confidence; source: https://www.bis.org/bcbs/publ/d516.pdf)
5. **When the same key-person dependency controls manual spreadsheets, desktop databases, or similar workflows used for risk aggregation or risk reporting, Basel Committee on Banking Supervision 239 adds a second supervisory concern because the framework requires largely automated aggregation and effective mitigants over manual desktop applications.** ([inference]; medium confidence; source: https://www.bis.org/publ/bcbs239.pdf)
6. **Escalation becomes strongest once the dependency can cause missed responsibility, task misperformance, delivery failure, business-continuity invocation, or inaccurate, incomplete, or untimely risk data.** ([inference]; medium confidence; source: https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf)
7. **Basel-compatible reporting should therefore describe key-person dependency as a causal concentration in process execution and then add the relevant Basel surface labels, instead of treating it as a generic human-resources issue with no explicit operational-risk taxonomy.** ([inference]; medium confidence; source: https://www.bis.org/bcbs/publ/d515.pdf; https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf; https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Basel Committee on Banking Supervision operational-risk guidance supports classifying key-person dependency as operational risk because the failure sits in people-process-system design. | https://www.bis.org/bcbs/publ/d515.pdf | medium | Base prudential classification. |
| [inference] The closest specific Basel loss-event type is "Execution, Delivery & Process Management" when the dependency threatens repeatable execution, handoff, deadline, or delivery steps. | https://www.bis.org/bcbs/qisoprisknote.pdf | medium | Direct event-type wording plus mapping. |
| [inference] The same dependency becomes an operational-resilience issue when it threatens a critical operation or tolerance for disruption. | https://www.bis.org/bcbs/publ/d516.pdf | medium | Critical-operation dependency mapping. |
| [inference] Business-continuity planning expectations are activated when key personnel disruption requires defined invocation triggers and internal decision-making. | https://www.bis.org/bcbs/publ/d516.pdf | medium | Key-person continuity trigger. |
| [inference] Basel Committee on Banking Supervision 239 adds a risk-data-aggregation and control classification when the key person controls manual spreadsheet or desktop-database reporting workflows. | https://www.bis.org/publ/bcbs239.pdf | medium | Manual-tool control and automation logic. |
| [inference] Escalation is strongest when the dependency can cause missed responsibility, task misperformance, delivery failure, or inaccurate and untimely risk data. | https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/publ/bcbs239.pdf | medium | Execution and reporting failure indicators. |
| [inference] Adjacent repository work supports treating the dependency as an explicit control-surface issue rather than as a generic staffing inconvenience. | https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html | medium | Companion synthesis support only. |

**Assumptions:**

- [assumption; source: https://www.bis.org/bcbs/publ/d515.pdf; https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf] The process is assumed to be material to operational delivery, control execution, or risk reporting; if it were not material, Basel classification would still indicate weak control design but would not necessarily trigger resilience or Basel Committee on Banking Supervision 239 escalation.

**Analysis:**

| Condition | Basel-compatible classification | Main control surface | Source |
|---|---|---|---|
| Single-person dependency exists in a material process, even before disruption occurs. | [inference] Operational risk driven by concentrated people-process dependency. | process design, role concentration, control ownership | https://www.bis.org/bcbs/publ/d515.pdf |
| The dependency threatens recurring execution quality, deadlines, handoffs, reconciliations, or delivery steps. | [inference] Execution, Delivery & Process Management loss-event exposure. | transaction processing, process management, task performance | https://www.bis.org/bcbs/qisoprisknote.pdf |
| The dependency can interrupt a critical operation if the individual is unavailable. | [inference] Operational-resilience dependency and business-continuity issue. | critical-operation mapping, tolerance for disruption, key-person continuity | https://www.bis.org/bcbs/publ/d516.pdf |
| The dependency controls manual risk-data or risk-reporting workflows in spreadsheets or desktop databases. | [inference] Basel Committee on Banking Supervision 239 risk-data aggregation and control weakness. | automation, spreadsheet control, manual-process mitigants | https://www.bis.org/publ/bcbs239.pdf |

Basel Committee on Banking Supervision operational-risk guidance was weighted first because it answers the threshold question of whether key-person dependency is a prudentially relevant risk at all. [inference; source: https://www.bis.org/bcbs/publ/d515.pdf]
The loss-event classification note was weighted next because it provides the most specific Basel wording for execution-facing manifestations of the dependency, even though it is older than the 2021 principles documents. [inference; source: https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d515.pdf]
The strongest rival interpretation is that key-person dependency should stay in human-resources language unless a loss already occurred, but Basel Committee on Banking Supervision resilience and risk-data guidance reject that narrow view by requiring advance mapping, trigger definition, and control treatment before disruption or reporting failure crystallizes. [inference; source: https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf]

**Risks, gaps, uncertainties:**

- Basel Committee on Banking Supervision does not publish a dedicated named "key-person dependency" event type, so the item's mapping remains an inference from the published operational-risk, loss-event, resilience, and risk-data texts rather than from one source that states the full conclusion directly. [inference; source: https://www.bis.org/bcbs/publ/d515.pdf; https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf]
- The "Execution, Delivery & Process Management" wording is drawn from an older Basel Committee on Banking Supervision operational-risk classification note, so firms may need to align internal terminology with current supervisory reporting structures even though the causal logic remains consistent. [fact; source: https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d515.pdf]
- The exact escalation threshold still depends on materiality, because the sources define critical operations, tolerance for disruption, and risk-data quality obligations, but they do not publish a universal numeric threshold for when every single-person dependency becomes reportable. [inference; source: https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf]

**Open questions:**

- What internal taxonomies do large banks currently use to distinguish between latent key-person concentration and already material execution-process dependency in operational-risk registers?
- Which testing methods best demonstrate that a documented backup or alternate operator is sufficient to keep a critical operation inside tolerance for disruption?
- How should Basel-compatible reporting language change when the dependency is concentrated in an external vendor specialist rather than in an internal employee?

**Output:**

- Type: knowledge
- Description: Produced a Basel-specific classification and reporting guide for key-person dependency, showing when to write the issue as base operational risk only and when to add execution-delivery-process-management, operational-resilience, and Basel Committee on Banking Supervision 239 language. [inference; source: https://www.bis.org/bcbs/publ/d515.pdf; https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf]
- Links:
  - https://www.bis.org/bcbs/publ/d515.pdf
  - https://www.bis.org/bcbs/qisoprisknote.pdf
  - https://www.bis.org/bcbs/publ/d516.pdf

### §7 Recursive Review

- [inference; source: https://www.bis.org/bcbs/publ/d515.pdf; https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf] No standalone Basel key-person event type appears in the sources used here, so medium confidence remains appropriate for the synthesis.

---

## Findings

### Executive Summary

Key-person dependency in a workforce-critical process should be classified first as Basel Committee on Banking Supervision operational risk, and then mapped specifically to "Execution, Delivery & Process Management" when the dependency threatens recurring process execution, handoffs, deadlines, or delivery outcomes. [inference; source: https://www.bis.org/bcbs/publ/d515.pdf; https://www.bis.org/bcbs/qisoprisknote.pdf]
The same dependency should be escalated into operational-resilience reporting when the person's unavailability could disrupt a critical operation, because Basel Committee on Banking Supervision guidance requires banks to map people, processes, information, technology, facilities, and their interdependencies against tolerance for disruption and business-continuity triggers. [inference; source: https://www.bis.org/bcbs/publ/d516.pdf]
If the dependency also sits inside manual spreadsheet or desktop-database production of risk data or risk reports, Basel Committee on Banking Supervision 239 adds a separate classification as a risk-data-aggregation, automation, and control weakness requiring effective mitigants or more automated design. [inference; source: https://www.bis.org/publ/bcbs239.pdf]
The strongest Basel-compatible reporting pattern is therefore to write key-person dependency as a causal driver and then name the activated Basel surface or surfaces: base operational risk, execution-delivery-process-management event risk, operational-resilience dependency risk, and Basel Committee on Banking Supervision 239 control weakness where applicable. [inference; source: https://www.bis.org/bcbs/publ/d515.pdf; https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf]

### Key Findings

1. **Basel Committee on Banking Supervision guidance supports classifying key-person dependency as operational risk because a process that depends on one indispensable person's availability or tacit knowledge fits the published definition of loss arising from failed people, processes, and systems.** ([inference]; medium confidence; source: https://www.bis.org/bcbs/publ/d515.pdf)
2. **The Basel loss-event type "Execution, Delivery & Process Management" is the closest specific event classification when the dependency threatens transaction capture, execution, maintenance, deadlines, responsibilities, reconciliations, handoffs, or delivery steps, because the published category explicitly covers failed transaction processing and process management.** ([inference]; medium confidence; source: https://www.bis.org/bcbs/qisoprisknote.pdf)
3. **A workforce-critical key-person dependency should be escalated into operational-resilience reporting when the person's absence could disrupt a critical operation, because banks are required to map people, technology, processes, information, facilities, and their interdependencies against tolerance for disruption.** ([inference]; medium confidence; source: https://www.bis.org/bcbs/publ/d516.pdf)
4. **Basel Committee on Banking Supervision guidance also expects business-continuity planning to address disruption that impacts key personnel and to define internal decision-making and invocation triggers, so a single-person bottleneck in a critical process is not Basel-compatible as an undocumented local workaround.** ([inference]; medium confidence; source: https://www.bis.org/bcbs/publ/d516.pdf)
5. **When the same key-person dependency controls manual spreadsheets, desktop databases, or similar workflows used for risk aggregation or risk reporting, Basel Committee on Banking Supervision 239 adds a second supervisory concern because the framework requires largely automated aggregation and effective mitigants over manual desktop applications.** ([inference]; medium confidence; source: https://www.bis.org/publ/bcbs239.pdf)
6. **Escalation becomes strongest once the dependency can cause missed responsibility, task misperformance, delivery failure, business-continuity invocation, or inaccurate, incomplete, or untimely risk data.** ([inference]; medium confidence; source: https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf)
7. **Basel-compatible reporting should therefore describe key-person dependency as a causal concentration in process execution and then add the relevant Basel surface labels, instead of treating it as a generic human-resources issue with no explicit operational-risk taxonomy.** ([inference]; medium confidence; source: https://www.bis.org/bcbs/publ/d515.pdf; https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf; https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Basel Committee on Banking Supervision operational-risk guidance supports classifying key-person dependency as operational risk because the failure sits in people-process-system design. | https://www.bis.org/bcbs/publ/d515.pdf | medium | Base prudential classification. |
| [inference] The closest specific Basel loss-event type is "Execution, Delivery & Process Management" when the dependency threatens repeatable execution, handoff, deadline, or delivery steps. | https://www.bis.org/bcbs/qisoprisknote.pdf | medium | Direct event-type wording plus mapping. |
| [inference] The same dependency becomes an operational-resilience issue when it threatens a critical operation or tolerance for disruption. | https://www.bis.org/bcbs/publ/d516.pdf | medium | Critical-operation dependency mapping. |
| [inference] Business-continuity planning expectations are activated when key personnel disruption requires defined invocation triggers and internal decision-making. | https://www.bis.org/bcbs/publ/d516.pdf | medium | Key-person continuity trigger. |
| [inference] Basel Committee on Banking Supervision 239 adds a risk-data-aggregation and control classification when the key person controls manual spreadsheet or desktop-database reporting workflows. | https://www.bis.org/publ/bcbs239.pdf | medium | Manual-tool control and automation logic. |
| [inference] Escalation is strongest when the dependency can cause missed responsibility, task misperformance, delivery failure, or inaccurate and untimely risk data. | https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/publ/bcbs239.pdf | medium | Execution and reporting failure indicators. |
| [inference] Adjacent repository work supports treating the dependency as an explicit control-surface issue rather than as a generic staffing inconvenience. | https://davidamitchell.github.io/Research/research/2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.html | medium | Companion synthesis support only. |

### Assumptions

- The process is assumed to be material to operational delivery, control execution, or risk reporting; if it were not material, Basel classification would still indicate weak control design but would not necessarily trigger resilience or Basel Committee on Banking Supervision 239 escalation. [assumption; source: https://www.bis.org/bcbs/publ/d515.pdf; https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf]

### Analysis

| Condition | Basel-compatible classification | Main control surface | Source |
|---|---|---|---|
| Single-person dependency exists in a material process, even before disruption occurs. | [inference] Operational risk driven by concentrated people-process dependency. | process design, role concentration, control ownership | https://www.bis.org/bcbs/publ/d515.pdf |
| The dependency threatens recurring execution quality, deadlines, handoffs, reconciliations, or delivery steps. | [inference] Execution, Delivery & Process Management loss-event exposure. | transaction processing, process management, task performance | https://www.bis.org/bcbs/qisoprisknote.pdf |
| The dependency can interrupt a critical operation if the individual is unavailable. | [inference] Operational-resilience dependency and business-continuity issue. | critical-operation mapping, tolerance for disruption, key-person continuity | https://www.bis.org/bcbs/publ/d516.pdf |
| The dependency controls manual risk-data or risk-reporting workflows in spreadsheets or desktop databases. | [inference] Basel Committee on Banking Supervision 239 risk-data aggregation and control weakness. | automation, spreadsheet control, manual-process mitigants | https://www.bis.org/publ/bcbs239.pdf |

Basel Committee on Banking Supervision operational-risk guidance was weighted first because it answers the threshold question of whether key-person dependency is a prudentially relevant risk at all. [inference; source: https://www.bis.org/bcbs/publ/d515.pdf]
The loss-event classification note was weighted next because it provides the most specific Basel wording for execution-facing manifestations of the dependency, even though it is older than the 2021 principles documents. [inference; source: https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d515.pdf]
The strongest rival interpretation is that key-person dependency should stay in human-resources language unless a loss already occurred, but Basel Committee on Banking Supervision resilience and risk-data guidance reject that narrow view by requiring advance mapping, trigger definition, and control treatment before disruption or reporting failure crystallizes. [inference; source: https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf]

### Risks, Gaps, and Uncertainties

- Basel Committee on Banking Supervision does not publish a dedicated named "key-person dependency" event type, so the item's mapping remains an inference from the published operational-risk, loss-event, resilience, and risk-data texts rather than from one source that states the full conclusion directly. [inference; source: https://www.bis.org/bcbs/publ/d515.pdf; https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf]
- The "Execution, Delivery & Process Management" wording is drawn from an older Basel Committee on Banking Supervision operational-risk classification note, so firms may need to align internal terminology with current supervisory reporting structures even though the causal logic remains consistent. [fact; source: https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d515.pdf]
- The exact escalation threshold still depends on materiality, because the sources define critical operations, tolerance for disruption, and risk-data quality obligations, but they do not publish a universal numeric threshold for when every single-person dependency becomes reportable. [inference; source: https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf]

### Open Questions

- What internal taxonomies do large banks currently use to distinguish between latent key-person concentration and already material execution-process dependency in operational-risk registers?
- Which testing methods best demonstrate that a documented backup or alternate operator is sufficient to keep a critical operation inside tolerance for disruption?
- How should Basel-compatible reporting language change when the dependency is concentrated in an external vendor specialist rather than in an internal employee?

---

## Output

- Type: knowledge
- Description: Produced a Basel-specific classification and reporting guide for key-person dependency, showing when to write the issue as base operational risk only and when to add execution-delivery-process-management, operational-resilience, and Basel Committee on Banking Supervision 239 language. [inference; source: https://www.bis.org/bcbs/publ/d515.pdf; https://www.bis.org/bcbs/qisoprisknote.pdf; https://www.bis.org/bcbs/publ/d516.pdf; https://www.bis.org/publ/bcbs239.pdf]
- Links:
  - https://www.bis.org/bcbs/publ/d515.pdf
  - https://www.bis.org/bcbs/qisoprisknote.pdf
  - https://www.bis.org/bcbs/publ/d516.pdf
