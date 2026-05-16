---
review_count: 1
title: "Decommission Trigger Design for Temporary Bridge Agents"
added: 2026-05-16T05:29:48+00:00
status: reviewing
priority: high
blocks: []
tags: [agentic-ai, workflow, organisation, agent-tooling, systems-capability-debt]
started: 2026-05-16T06:59:18+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-04-27-uelgf-decommission-lifecycle
  - 2026-04-27-uelgf-runtime-feedback-loop
  - 2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis
  - 2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls
related:
  - 2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates
  - 2026-05-08-capability-debt-definition-measurement-ai-risk-amplification
  - 2026-05-02-hitl-review-volume-bottleneck-rubber-stamp
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Decommission Trigger Design for Temporary Bridge Agents

## Research Question

What technical and organisational mechanisms most reliably cause temporary bridge Artificial Intelligence (AI) agents to be decommissioned when the corresponding software capability is delivered, and which design patterns in registration and runtime feedback loops can enforce this without manual intervention as the primary trigger?

## Scope

**In scope:**
- Decommission outcomes from Robotic Process Automation (RPA) and low-code retirement programmes.
- Machine-verifiable trigger representations tied to incremental software delivery milestones.
- Governance and incentive mechanisms that counter path dependency and keep decommission commitments credible.

**Out of scope:**
- Building a full decommission orchestration tool in this item.
- Organisation-specific change-management implementation plans.

**Constraints:**
- Focus on mechanisms that can be operationalised and audited.
- Prioritise evidence from environments with strong governance requirements.

## Context

- Temporary bridge agents become persistent automation debt when no registry or runtime control can prove that their bridging function has ended. [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html]
- Prior completed repository work already ties workaround persistence to systems capability debt and shows that decommission triggers need observable runtime evidence rather than owner self-declaration. [fact; source: https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-decommission-lifecycle.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html; https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html]
- Official low-code and automation governance sources now expose the specific control surfaces that make machine-triggered retirement practical, especially inventory, inactivity detection, orphaned-owner detection, approval workflows, and dependency-aware deletion. [fact; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-orphan-components; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data]

## Approach

1. Review evidence from RPA and low-code retirement programmes on what drives successful decommissioning.
2. Define verifiable decommission-condition patterns that remain stable across iterative software releases.
3. Evaluate incentive and governance patterns that reduce persistence of no-longer-justified automations.

## Sources

- [x] [National Institute of Standards and Technology (NIST) Artificial Intelligence Risk Management Framework Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) - official lifecycle-governance outcomes, including safe decommissioning and ongoing monitoring.
- [x] [National Institute of Standards and Technology (NIST) AI Risk Management Framework Playbook](https://airc.nist.gov/airmf-resources/playbook/) - official playbook for operationalising lifecycle governance outcomes.
- [x] [ISACA, originally the Information Systems Audit and Control Association (2026) Governing AI Across its Lifecycle: A Framework for Risk Practitioners](https://www.isaca.org/resources/toolkits/governing-ai-across-its-lifecycle-a-framework-for-risk-practitioners) - official five-stage lifecycle model that includes retirement and artifact retention.
- [x] [ISACA, originally the Information Systems Audit and Control Association (2020) An Introduction to Assessing the Compliance Risk of RPA Enabled Processes](https://www.isaca.org/resources/news-and-trends/newsletters/atisaca/2020/volume-11/an-introduction-to-assessing-the-compliance-risk-of-rpa-enabled-processes) - control-room, governance-board, change-management, and audit requirements for RPA.
- [x] [ISACA, originally the Information Systems Audit and Control Association (2023) RPA Is Evolving but Risk Still Exists](https://www.isaca.org/resources/isaca-journal/issues/2023/volume-2/rpa-is-evolving-but-risk-still-exists) - ongoing privileged-access, monitoring, and audit risks in RPA estates.
- [x] [UiPath (2026) Automation Hub Deleting Data](https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data) - platform delete controls, role restrictions, and dependency-aware deletion blocks.
- [x] [UiPath (2026) Automation Hub Customize Idea Flows](https://docs.uipath.com/automation-hub/automation-suite/2.2510/user-guide/customize-idea-flows) - flow enable and disable controls for lifecycle gating.
- [x] [Microsoft (2026) Set up inactivity notifications components](https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components) - scheduled inactivity detection, approvals, and optional auto-delete workflow for unused apps and flows.
- [x] [Microsoft (2026) Automatic deletion of Power Platform environments](https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup) - machine-defined inactivity windows, warning schedule, disablement, and deletion for unused environments.
- [x] [Microsoft (2026) Power Platform inventory](https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory) - inventory, ownerless-resource detection, resource filtering, and programmatic query surfaces.
- [x] [Microsoft (2026) Implement reactive governance controls](https://learn.microsoft.com/en-us/power-platform/guidance/adoption/reactive-governance) - real-time governance actions for inactive, overshared, and ownerless resources.
- [x] [Microsoft (2026) Set up clean-up for orphaned objects](https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-orphan-components) - manager-routed reassignment process for ownerless objects.
- [x] [Mitchell (2026) Universal Entity Lifecycle Governance Framework decommission lifecycle](https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-decommission-lifecycle.html) - prior completed item formalising dependency-elimination decommission.
- [x] [Mitchell (2026) Universal Entity Lifecycle Governance Framework runtime feedback loop](https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html) - prior completed item formalising machine-readable runtime signals and feedback closure.
- [x] [Mitchell (2026) Systems capability debt, citizen development, and agentic AI risk](https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html) - prior completed item linking persistent workarounds to underlying capability gaps.
- [x] [Mitchell (2026) Incentive misalignment, shadow AI, and skill decay controls](https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html) - prior completed item on why manual cleanup is unreliable under local delivery pressure.
- [x] [Mitchell (2026) Tiered human oversight quality measurement under scale](https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html) - prior completed item on why manual approvals degrade under volume.

## Related

- [Mitchell (2026) Universal Entity Lifecycle Governance Framework decommission lifecycle](https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-decommission-lifecycle.html)
- [Mitchell (2026) Universal Entity Lifecycle Governance Framework runtime feedback loop](https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html)
- [Mitchell (2026) Systems capability debt, citizen development, and agentic AI risk](https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: what technical and organisational mechanisms most reliably cause temporary bridge AI agents to be decommissioned once the replacement software capability is actually live and in use?
- Scope: RPA and low-code retirement analogues, registration and runtime trigger design, and governance patterns that make retirement auditable without making manual approval the primary trigger.
- Constraints: use machine-observable signals where possible, prioritise official lifecycle and platform sources, and treat software-capability delivery as insufficient on its own unless runtime evidence confirms the old bridge is no longer needed.
- Output: knowledge.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-decommission-lifecycle.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html; https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html; https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html] Prior completed-item sweep shows that adjacent repository work already established dependency-elimination as a legitimate decommission trigger, runtime feedback as the preferred evidence source, systems capability debt as the cause of workaround persistence, and incentive plus oversight limits as reasons not to rely on manual cleanup alone.

### §1 Question Decomposition

- **Root question:** What trigger architecture actually retires a temporary automation once the underlying capability gap is closed?
- **A. Lifecycle and governance**
  - A1. What do official lifecycle frameworks require for retirement and decommission?
  - A2. What governance artifacts make retirement auditable rather than ad hoc?
- **B. Observable trigger surfaces**
  - B1. Which platform features already detect inactivity, owner departure, or stale objects automatically?
  - B2. Which platform features block deletion while dependencies still exist?
- **C. Reliability of trigger classes**
  - C1. Which trigger classes are objective enough to run without owner self-declaration?
  - C2. Which trigger classes still need a grace period or appeal path?
- **D. Registration pattern**
  - D1. Which fields must a temporary bridge agent registry carry to make later retirement machine-verifiable?
  - D2. How should the registry reference the replacement capability?
- **E. Runtime feedback pattern**
  - E1. Which runtime signals prove the old bridge is no longer needed?
  - E2. Which runtime signals prove retirement is unsafe because dependencies remain?
- **F. Governance and incentives**
  - F1. Why is manual owner action an unreliable primary trigger?
  - F2. What role should human approval still play?

### §2 Investigation

#### A. Retirement is an explicit lifecycle duty, not a cleanup afterthought

- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] The NIST AI Risk Management Framework Core states in GOVERN 1.7 that processes and procedures should be in place for decommissioning and phasing out AI systems safely and in a manner that does not increase risks or decrease the system's trustworthiness.
- [inference; source: https://airc.nist.gov/airmf-resources/playbook/; https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] The NIST AI Risk Management Framework Playbook should be read as part of a broader operational lifecycle that includes decommissioning, because it is the implementation companion to a core framework that explicitly includes safe phase-out.
- [fact; source: https://www.isaca.org/resources/toolkits/governing-ai-across-its-lifecycle-a-framework-for-risk-practitioners] ISACA's 2026 lifecycle toolkit names retirement as one of five critical governance stages and says defensible oversight requires tangible artifacts such as documented decisions and monitoring reports across the lifecycle.
- [inference; source: https://www.isaca.org/resources/news-and-trends/newsletters/atisaca/2020/volume-11/an-introduction-to-assessing-the-compliance-risk-of-rpa-enabled-processes; https://www.isaca.org/resources/isaca-journal/issues/2023/volume-2/rpa-is-evolving-but-risk-still-exists] ISACA's RPA guidance requires governance boards, formal risk assessments, change-management controls, privileged-access scrutiny, regular audits, and documented oversight for automation estates, which means retirement can be governed through the same evidence surfaces as deployment and operation.

#### B. Official low-code and automation platforms already implement machine-observed retirement patterns

- [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components] Microsoft's Center of Excellence guidance checks for apps not modified or launched in the last six months by default, starts approval workflows for owners, records the approval task in Microsoft Dataverse, and can auto-delete approved inactive apps and flows through a daily cleanup flow.
- [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components] The same Microsoft guidance exposes an `Auto Delete on Archive` setting, which shows that automatic deletion is treated as a configurable downstream action once a machine-detected inactivity condition and approval state are reached.
- [fact; source: https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup] Microsoft Power Platform also performs inactivity-based cleanup for environments using fixed time windows, warning emails, disablement, and eventual deletion, and it defines activity from user, maker, admin, and scheduled-flow behavior rather than from owner attestation.
- [fact; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory] Power Platform inventory provides a tenant-wide view of agents, apps, and flows, updates created, updated, or deleted resources within 15 minutes, supports filtering by owner and environment, and explicitly advertises owner-departure detection to prevent orphaned agents.
- [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-orphan-components; https://learn.microsoft.com/en-us/power-platform/guidance/adoption/reactive-governance] Microsoft's orphaned-object and reactive-governance guidance routes ownerless resources into reassignment or corrective workflows, which makes owner departure an operational signal rather than a passive record problem.
- [fact; source: https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] UiPath restricts deletion to specific administrative roles, requires explicit delete actions, and refuses deletion of App Inventory entries when the application is still used in ideas or components.
- [inference; source: https://docs.uipath.com/automation-hub/automation-suite/2.2510/user-guide/customize-idea-flows] UiPath also allows flows to be disabled for action while preserving the underlying configuration, which separates "stop new intake" from final removal.

#### C. The most reliable trigger classes are objective state changes, not voluntary declarations

- [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] Platform documentation converges on the same high-reliability trigger classes: observed inactivity, observed owner absence, observed inventory state, approval state, and dependency state.
- [inference; source: https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-orphan-components; https://www.isaca.org/resources/news-and-trends/newsletters/atisaca/2020/volume-11/an-introduction-to-assessing-the-compliance-risk-of-rpa-enabled-processes] These sources support a design in which deletion is the end of a governed sequence, while the actual retirement trigger is the machine-observed condition that starts the sequence.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.isaca.org/resources/toolkits/governing-ai-across-its-lifecycle-a-framework-for-risk-practitioners; https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html] Manual owner action is a weak primary trigger because local incentives reward keeping useful bridges alive, and manual approvals degrade under queue pressure, so human intervention should be reserved for exceptions, disputes, and high-consequence confirmation.

#### D. Replacement-capability delivery needs runtime confirmation before it can become a safe trigger

- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-decommission-lifecycle.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html] Prior completed repository items formalise two ideas that the external platform sources do not name directly: dependency elimination is the correct retirement condition for workaround entities, and runtime feedback is the right place to observe whether that condition has actually been reached.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html] The systems-capability-debt synthesis argues that workaround automations persist when central capability gaps remain, which implies that a release ticket or deployment event alone does not prove the underlying gap has closed in operating practice.
- [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html] The defensible design pattern is therefore to bind software-delivery metadata to runtime evidence, for example route migration, zero remaining launches or executions, loss of prior exception demand, and capability overlap visible in inventory, before a decommission sequence becomes automatic.
- [inference; source: https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data; https://docs.uipath.com/automation-hub/automation-suite/2.2510/user-guide/customize-idea-flows; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-decommission-lifecycle.html] Dependency-aware deletion blocks and flow-disable controls indicate that the right technical sequence is freeze new intake first, then verify dependency elimination, then revoke or remove, rather than deleting first and discovering hidden dependencies afterward.

#### E. The trigger design that best fits the evidence is expiry plus observable supersession

- [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://www.isaca.org/resources/toolkits/governing-ai-across-its-lifecycle-a-framework-for-risk-practitioners] A temporary bridge agent registry should carry at least an owner, a last-review date, an explicit expiry date, the intended replacement capability identifier, dependency references, and the runtime metrics that prove ongoing need or safe retirement.
- [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/adoption/reactive-governance; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-orphan-components; https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html] The default operating model should be "expire unless renewed by evidence" rather than "persist until someone remembers to delete it", because reactive governance and incentive evidence both favor default-off lifecycle controls over optional cleanup behavior.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.isaca.org/resources/toolkits/governing-ai-across-its-lifecycle-a-framework-for-risk-practitioners; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html] The runtime feedback loop should evaluate three classes of retirement evidence together: replacement evidence that the deterministic or engineered capability is live, non-need evidence that the temporary bridge agent is no longer exercised, and safety evidence that no live dependencies or critical exceptions remain.

### §3 Reasoning

- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.isaca.org/resources/toolkits/governing-ai-across-its-lifecycle-a-framework-for-risk-practitioners] Official lifecycle sources establish that retirement must be governed, documented, and monitored.
- [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] Official platform sources establish that inventory, inactivity thresholds, ownerless-resource detection, dependency checks, approvals, disablement, and auto-delete flows are practical, production-used trigger surfaces.
- [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html] Therefore the best trigger design for temporary bridge agents is not a single milestone but a composed state machine, where software delivery opens the evaluation window and runtime evidence closes it.
- [assumption; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-decommission-lifecycle.html] Assumption: "corresponding software capability delivered" can be represented in a registry by a deployment or capability identifier that can later be reconciled against runtime and dependency data. Justification: the reviewed sources expose the needed inventory and dependency surfaces, but none standardizes one universal replacement-marker schema for all platforms.

### §4 Consistency Check

- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.isaca.org/resources/toolkits/governing-ai-across-its-lifecycle-a-framework-for-risk-practitioners; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] No primary-source contradiction appeared on the core claim that decommission belongs inside the managed lifecycle and should use inventories, approvals, and documented control steps.
- [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html] The main unresolved uncertainty is not whether machine-observed triggers are better than manual cleanup, but how to detect capability supersession precisely enough to avoid premature retirement on complex partial replacements.

### §5 Depth and Breadth Expansion

- [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/guidance/adoption/reactive-governance; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html] Technical lens: the trigger surface should be built from inventory, dependency graph, last-use signals, and routed corrective workflows, because these are the observable primitives already present in mature governance platforms.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.isaca.org/resources/toolkits/governing-ai-across-its-lifecycle-a-framework-for-risk-practitioners] Regulatory lens: lifecycle frameworks treat retirement as part of ongoing oversight, which means decommission evidence has to be retained and reviewable, not only executed.
- [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components] Economic lens: default expiry and inactivity-based cleanup reduce carrying cost for stale automations because they remove dormant assets without waiting for a special project.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-orphan-components] Behavioural lens: the human role should shift from remembering to clean up, to contesting or approving exceptional cases, because manual cleanup is vulnerable to neglect, queue pressure, and local optimization.

### §6 Synthesis

#### Executive Summary

- [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html] The most reliable way to decommission temporary bridge agents is to register them as expiring exceptions and retire them from machine-observed evidence of supersession and non-use.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html] Manual owner declarations belong in exception and appeal handling.
- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.isaca.org/resources/toolkits/governing-ai-across-its-lifecycle-a-framework-for-risk-practitioners] Official lifecycle frameworks require retirement to be governed, documented, and monitored as part of normal operations.
- [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] Microsoft and UiPath already operationalize the relevant primitives through inactivity thresholds, approval tasks, disable-before-delete flows, dependency-aware deletion blocks, and scheduled cleanup.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html; https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html] A software-delivery milestone should therefore start a decommission evaluation window, but the actual automatic trigger should depend on runtime proof that the workaround's demand and dependencies have collapsed.

#### Key Findings

1. [inference] **The strongest decommission pattern uses an expiring registration plus runtime evidence of supersession, because official platform controls already rely on inactivity, ownerless-state, approval-state, and dependency-state signals to decide when cleanup work should start.** (medium confidence; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data)
2. [fact] **Official lifecycle frameworks treat retirement as a first-class governance stage, so temporary bridge agents need documented trigger logic, retained evidence, and reviewable decommission records to satisfy that governance burden.** (high confidence; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://airc.nist.gov/airmf-resources/playbook/; https://www.isaca.org/resources/toolkits/governing-ai-across-its-lifecycle-a-framework-for-risk-practitioners)
3. [fact] **Microsoft's Power Platform guidance demonstrates that scheduled inactivity checks, warning windows, reassignment flows, and optional auto-delete are already mature low-code patterns for machine-initiated retirement workflows.** (medium confidence; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-orphan-components)
4. [fact] **UiPath's delete and disable controls show that retirement should distinguish between stopping new intake, preserving history, and final removal, and that deletion must be blocked while explicit dependencies still exist.** (medium confidence; source: https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data; https://docs.uipath.com/automation-hub/automation-suite/2.2510/user-guide/customize-idea-flows)
5. [inference] **A software release does not independently prove decommission readiness, because the replacement capability may be technically deployed while users, routes, or exceptions still rely on the old bridge in production.** (medium confidence; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html)
6. [inference] **The most defensible automatic trigger is a composite state change in which the replacement capability is registered as live, the temporary bridge agent shows sustained non-use or collapsing exception demand, and dependency checks show no remaining justified consumers.** (medium confidence; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/guidance/adoption/reactive-governance; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-decommission-lifecycle.html)
7. [inference] **Human approval belongs in an exception, appeal, and high-consequence confirmation layer, because incentive pressure and volume-sensitive oversight failure make manual cleanup unreliable as the main retirement mechanism.** (medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html; https://www.isaca.org/resources/news-and-trends/newsletters/atisaca/2020/volume-11/an-introduction-to-assessing-the-compliance-risk-of-rpa-enabled-processes)

#### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Expiring registrations with observable retirement signals are more reliable than voluntary cleanup. | https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components ; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup ; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory ; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data | medium | Built from convergent platform-control patterns. |
| [fact] Retirement is a required lifecycle stage in official governance frameworks. | https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ ; https://airc.nist.gov/airmf-resources/playbook/ ; https://www.isaca.org/resources/toolkits/governing-ai-across-its-lifecycle-a-framework-for-risk-practitioners | high | Directly stated in framework materials. |
| [fact] Power Platform operationalizes machine-initiated retirement through inactivity checks, warnings, reassignment, and optional auto-delete. | https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components ; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup ; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-orphan-components | medium | Strong official implementation analogue. |
| [fact] UiPath separates disablement from deletion and blocks deletion while dependencies remain. | https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data ; https://docs.uipath.com/automation-hub/automation-suite/2.2510/user-guide/customize-idea-flows | medium | Direct platform behavior. |
| [inference] Deployment alone is not a safe trigger because runtime dependence can survive release. | https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory ; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup ; https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html ; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html | medium | Requires synthesis of runtime and workaround evidence. |
| [inference] Composite supersession, non-use, and dependency-clear signals are the best automatic trigger. | https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory ; https://learn.microsoft.com/en-us/power-platform/guidance/adoption/reactive-governance ; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data ; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-decommission-lifecycle.html | medium | Best-fit synthesis across official and prior-item evidence. |
| [inference] Human approval belongs in an exception and appeal layer, while default retirement uses objective signals. | https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html ; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html ; https://www.isaca.org/resources/news-and-trends/newsletters/atisaca/2020/volume-11/an-introduction-to-assessing-the-compliance-risk-of-rpa-enabled-processes | medium | Cross-item integration plus governance evidence. |

#### Assumptions

- [assumption; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html] A temporary bridge agent can be represented in a unified registry with enough metadata to reconcile software-delivery milestones against runtime usage and dependency evidence. Justification: the reviewed inventory and runtime-feedback sources expose the required surfaces, but they do not prescribe one universal schema for all agent platforms.
- [assumption; source: https://www.isaca.org/resources/news-and-trends/newsletters/atisaca/2020/volume-11/an-introduction-to-assessing-the-compliance-risk-of-rpa-enabled-processes; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] RPA and low-code retirement controls are close enough to temporary bridge agent controls to transfer the governance pattern. Justification: the lifecycle, inventory, approval, dependency, and identity surfaces are operationally similar even though the implementation substrate differs.

#### Analysis

- [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] The strongest evidence in this item comes from official platform documentation, because those sources show which retirement primitives are already reliable enough to ship in production products.
- Those official sources directly support inventory, inactivity, ownerless-state, approvals, disablement, and dependency-aware deletion, but they do not directly define "replacement capability delivered" as a universal trigger, so that part of the answer is necessarily a synthesis. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data]
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-decommission-lifecycle.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html; https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html] Prior repository items materially strengthen that synthesis because they already frame workaround retirement as dependency elimination, treat runtime telemetry as the correct evidence surface, and show why underlying capability gaps keep temporary automations alive.
- A plausible rival remedy is to preserve manual periodic reviews, add more reviewers, and let owners decide when the bridge is no longer needed. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html; https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html]
- That rival is weaker because the reviewed evidence shows that low-value queues, local delivery incentives, and stale ownership all push in the opposite direction, while the official platforms that actually manage large automation estates prefer objective state checks and scheduled workflows over memory-based cleanup. [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-orphan-components; https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html]
- The design implication is a layered trigger model: software delivery registers a potential supersession event, runtime evidence tests whether the bridge has truly gone cold, dependency checks prevent unsafe removal, and only disputed or high-risk cases reach human review. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html]

#### Risks, Gaps, and Uncertainties

- [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] No reviewed vendor document publishes a native, cross-platform definition of "replacement capability delivered," so the mapping from release metadata to retirement eligibility remains a design inference rather than a directly stated platform standard.
- [inference; source: https://www.isaca.org/resources/news-and-trends/newsletters/atisaca/2020/volume-11/an-introduction-to-assessing-the-compliance-risk-of-rpa-enabled-processes; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] The strongest external evidence comes from low-code and RPA governance, not from public temporary bridge agent retirement case studies, so transfer to agent-specific orchestration should be treated as well-grounded but not fully validated.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.isaca.org/resources/toolkits/governing-ai-across-its-lifecycle-a-framework-for-risk-practitioners; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup] Grace-period length, appeal path, and archival retention details will still need tiering by business criticality, because the reviewed sources expose the control primitives but not one universal policy threshold.

#### Open Questions

- What is the best machine-readable way to detect semantic capability overlap between a newly delivered deterministic feature and a legacy temporary bridge agent?
- Which risk tiers justify automatic revocation after composite trigger satisfaction, and which still require explicit secondary approval?
- How should shared sub-agents be handled when one consumer workflow is superseded but others remain active?

### §7 Recursive Review

- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-05-16-decommission-trigger-design-for-do-mode-agents.md] Internal review of this item found acronym expansion, claim labeling, and Section 6 versus Findings parity complete after the first-pass fixes.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-05-16-decommission-trigger-design-for-do-mode-agents.md] The residual uncertainty remains limited to how a replacement capability is represented and proven across heterogeneous platforms.

## Findings

### Executive Summary

The most reliable way to decommission temporary bridge agents is to register them as expiring exceptions and retire them from machine-observed evidence of supersession and non-use. [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html]

Manual owner declarations belong in exception and appeal handling. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html]

Official lifecycle frameworks require retirement to be governed, documented, and monitored as part of normal operations. [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.isaca.org/resources/toolkits/governing-ai-across-its-lifecycle-a-framework-for-risk-practitioners]

Microsoft and UiPath already operationalize the relevant primitives through inactivity thresholds, approval tasks, disable-before-delete flows, dependency-aware deletion blocks, and scheduled cleanup. [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data]

A software-delivery milestone should therefore start a decommission evaluation window, but the automatic trigger should depend on runtime proof that the workaround's demand and dependencies have collapsed. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html]

### Key Findings

1. **The strongest decommission pattern uses an expiring registration plus runtime evidence of supersession, because official platform controls already rely on inactivity, ownerless-state, approval-state, and dependency-state signals to decide when cleanup work should start.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data)
2. **Official lifecycle frameworks treat retirement as a first-class governance stage, so temporary bridge agents need documented trigger logic, retained evidence, and reviewable decommission records to satisfy that governance burden.** ([fact]; high confidence; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://airc.nist.gov/airmf-resources/playbook/; https://www.isaca.org/resources/toolkits/governing-ai-across-its-lifecycle-a-framework-for-risk-practitioners)
3. **Microsoft's Power Platform guidance demonstrates that scheduled inactivity checks, warning windows, reassignment flows, and optional auto-delete are already mature low-code patterns for machine-initiated retirement workflows.** ([fact]; medium confidence; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-orphan-components)
4. **UiPath's delete and disable controls show that retirement should distinguish between stopping new intake, preserving history, and final removal, and that deletion must be blocked while explicit dependencies still exist.** ([fact]; medium confidence; source: https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data; https://docs.uipath.com/automation-hub/automation-suite/2.2510/user-guide/customize-idea-flows)
5. **A software release does not independently prove decommission readiness, because the replacement capability may be technically deployed while users, routes, or exceptions still rely on the old bridge in production.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html)
6. **The most defensible automatic trigger is a composite state change in which the replacement capability is registered as live, the temporary bridge agent shows sustained non-use or collapsing exception demand, and dependency checks show no remaining justified consumers.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/guidance/adoption/reactive-governance; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-decommission-lifecycle.html)
7. **Human approval belongs in an exception, appeal, and high-consequence confirmation layer, because incentive pressure and volume-sensitive oversight failure make manual cleanup unreliable as the main retirement mechanism.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html; https://www.isaca.org/resources/news-and-trends/newsletters/atisaca/2020/volume-11/an-introduction-to-assessing-the-compliance-risk-of-rpa-enabled-processes)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Expiring registrations with observable retirement signals are more reliable than voluntary cleanup. | https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components ; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup ; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory ; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data | medium | Built from convergent platform-control patterns. |
| [fact] Retirement is a required lifecycle stage in official governance frameworks. | https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ ; https://airc.nist.gov/airmf-resources/playbook/ ; https://www.isaca.org/resources/toolkits/governing-ai-across-its-lifecycle-a-framework-for-risk-practitioners | high | Directly stated in framework materials. |
| [fact] Power Platform operationalizes machine-initiated retirement through inactivity checks, warnings, reassignment, and optional auto-delete. | https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components ; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup ; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-orphan-components | medium | Strong official implementation analogue. |
| [fact] UiPath separates disablement from deletion and blocks deletion while dependencies remain. | https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data ; https://docs.uipath.com/automation-hub/automation-suite/2.2510/user-guide/customize-idea-flows | medium | Direct platform behavior. |
| [inference] Deployment alone is not a safe trigger because runtime dependence can survive release. | https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory ; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup ; https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html ; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html | medium | Requires synthesis of runtime and workaround evidence. |
| [inference] Composite supersession, non-use, and dependency-clear signals are the best automatic trigger. | https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory ; https://learn.microsoft.com/en-us/power-platform/guidance/adoption/reactive-governance ; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data ; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-decommission-lifecycle.html | medium | Best-fit synthesis across official and prior-item evidence. |
| [inference] Human approval belongs in an exception and appeal layer, and default retirement should rely on objective signals. | https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html ; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html ; https://www.isaca.org/resources/news-and-trends/newsletters/atisaca/2020/volume-11/an-introduction-to-assessing-the-compliance-risk-of-rpa-enabled-processes | medium | Cross-item integration plus governance evidence. |

### Assumptions

- [assumption; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html] A temporary bridge agent can be represented in a unified registry with enough metadata to reconcile software-delivery milestones against runtime usage and dependency evidence. Justification: the reviewed inventory and runtime-feedback sources expose the required surfaces, but they do not prescribe one universal schema for all agent platforms.
- [assumption; source: https://www.isaca.org/resources/news-and-trends/newsletters/atisaca/2020/volume-11/an-introduction-to-assessing-the-compliance-risk-of-rpa-enabled-processes; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] RPA and low-code retirement controls are close enough to temporary bridge agent controls to transfer the governance pattern. Justification: the lifecycle, inventory, approval, dependency, and identity surfaces are operationally similar even though the implementation substrate differs.

### Analysis

The strongest evidence in this item comes from official platform documentation, because those sources show which retirement primitives are already reliable enough to ship in production products. [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data]

Those official sources directly support inventory, inactivity, ownerless-resource detection, approvals, disablement, and dependency-aware deletion, but they do not directly define "replacement capability delivered" as a universal trigger, so that part of the answer is necessarily a synthesis. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data]

Prior repository items materially strengthen that synthesis because they already frame workaround retirement as dependency elimination, treat runtime telemetry as the correct evidence surface, and show why underlying capability gaps keep temporary automations alive. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-decommission-lifecycle.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html; https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html]

A plausible rival remedy is to preserve manual periodic reviews, add more reviewers, and let owners decide when the bridge is no longer needed. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html; https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html]

That rival is weaker because the reviewed evidence shows that low-value queues, local delivery incentives, and stale ownership all push in the opposite direction, while the official platforms that actually manage large automation estates prefer objective state checks and scheduled workflows over memory-based cleanup. [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-orphan-components; https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html]

The design implication is a layered trigger model: software delivery registers a potential supersession event, runtime evidence tests whether the bridge has truly gone cold, dependency checks prevent unsafe removal, and only disputed or high-risk cases reach human review. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html]

### Risks, Gaps, and Uncertainties

- No reviewed vendor document publishes a native, cross-platform definition of "replacement capability delivered," so the mapping from release metadata to retirement eligibility remains a design inference rather than a directly stated platform standard. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data]
- The strongest external evidence comes from low-code and RPA governance, not from public temporary bridge agent retirement case studies, so transfer to agent-specific orchestration should be treated as well-grounded but not fully validated. [inference; source: https://www.isaca.org/resources/news-and-trends/newsletters/atisaca/2020/volume-11/an-introduction-to-assessing-the-compliance-risk-of-rpa-enabled-processes; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data]
- Grace-period length, appeal path, and archival retention details will still need tiering by business criticality, because the reviewed sources expose the control primitives but not one universal policy threshold. [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.isaca.org/resources/toolkits/governing-ai-across-its-lifecycle-a-framework-for-risk-practitioners; https://learn.microsoft.com/en-us/power-platform/admin/automatic-environment-cleanup]

### Open Questions

- What is the best machine-readable way to detect semantic capability overlap between a newly delivered deterministic feature and a legacy temporary bridge agent?
- Which risk tiers justify automatic revocation after composite trigger satisfaction, and which still require explicit secondary approval?
- How should shared sub-agents be handled when one consumer workflow is superseded but others remain active?

## Output

- Type: knowledge
- Description: A decommission-trigger design note arguing for expiring registrations plus runtime-confirmed supersession, grounded in official lifecycle and platform governance evidence. [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data]
- Links:
  - https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
  - https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components
  - https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data
