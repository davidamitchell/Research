---
review_count: 1
title: "Taxonomy criteria: process inefficiency versus hidden control and dependency risk in workforce workflows"
added: 2026-05-09T22:56:47+00:00
status: completed
priority: high
blocks: []
tags: [organisation, workflow]
ai_themes: [governance-policy, security-risk, workforce-skills, organisational-design]
started: 2026-05-11T12:11:45+00:00
completed: 2026-05-11T12:28:08+00:00
output: [knowledge]
cites:
  - 2026-05-09-prc-risk-scoring-unstandardized-workforce-processes
  - 2026-05-09-key-person-dependency-basel-risk-linkage
  - 2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts
  - 2026-05-02-hitl-review-volume-bottleneck-rubber-stamp
  - 2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates
related:
  - 2026-04-26-human-in-the-loop-ai-automated-workflows
  - 2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls
  - 2026-05-08-integrated-cascading-failure-agentic-vs-generative-ai-risk
superseded_by: ~
supersedes: 2026-05-09-enterprise-risk-workforce-shadow-systems
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: ac3e5112baeb92b3bbf5018a5065d441b3cb5b41
    changed: 2026-05-11
    progress: progress/2026-05-11-process-inefficiency-vs-latent-risk-taxonomy.md
    summary: "Initial completion"
---

# Taxonomy criteria: process inefficiency versus hidden control and dependency risk in workforce workflows

## Research Question

Which explicit criteria best distinguish ordinary process inefficiency from hidden control and dependency risk in workforce-capacity and skill-tracking workflows?

## Scope

**In scope:**
- Decision criteria for classifying issues as inefficiency versus risk
- Trigger thresholds and evidence requirements for escalation
- Workforce-data process contexts with control implications

**Out of scope:**
- Tool implementation guidance
- Financial quantification models specific to one enterprise

**Constraints:** Criteria must be auditable and mapped to formal risk and control language.

## Context

Misclassifying a control weakness or concentrated dependency as mere inefficiency can delay escalation until disruption, error propagation, or evidentiary failure is already harder to reverse. [inference; source: https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline]

## Approach

1. Define candidate criteria dimensions, especially impact, persistence, detectability, and dependency concentration.
2. Test the criteria against representative workforce-process scenarios.
3. Produce a classification rubric suitable for risk-intake workflows.

## Sources

- [x] [International Organization for Standardization (ISO) 31000 Risk management](https://www.iso.org/iso-31000-risk-management.html) - risk-management principles and evaluation language.
- [x] [National Institute of Standards and Technology (NIST) Special Publication (SP) 800-30 Rev. 1 Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final) - risk assessment as input to response decisions.
- [x] [National Institute of Standards and Technology (NIST) About the Risk Management Framework](https://csrc.nist.gov/Projects/risk-management/about-rmf) - risk-based selection, assessment, authorization, and monitoring lifecycle.
- [x] [Basel Committee Principles for Operational Resilience](https://www.bis.org/bcbs/publ/d516.htm) - operational-risk-related events and significant operational failure framing.
- [x] [Basel Committee Principles for the sound management of operational risk](https://www.bis.org/bcbs/publ/d515.htm) - operational-risk governance principles.
- [x] [Office of the Superintendent of Financial Institutions (OSFI) Operational Risk Management and Resilience Guideline](https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline) - risk appetite, limits, indicators, dependencies, and tolerances for disruption.
- [x] [Institute of Operational Risk Key Risk Indicators](https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/) - indicator thresholds and governance.
- [x] [Lean Enterprise Institute Seven Wastes](https://www.lean.org/lexicon-terms/seven-wastes/) - waiting and correction as waste categories.
- [x] [Lean Enterprise Institute Cycle Time](https://www.lean.org/lexicon-terms/cycle-time/) - cycle time and nonvalue-creating time.
- [x] [Mitchell (2026) How should human-in-the-loop design be adapted when AI review volume makes human reviewers a bottleneck or causes rubber-stamping?](https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html) - review-quality collapse as a hidden control failure.
- [x] [Mitchell (2026) What tiered human oversight models maintain meaningful human-in-the-loop control at scale under high-volume multi-step Artificial Intelligence adoption, and how should organisations measure oversight quality when productivity mandates exist without explicit quality Key Performance Indicators?](https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html) - oversight metrics and challenge quality.
- [x] [Mitchell (2026) When should undocumented, team-local, or manually maintained workforce processes automatically raise inherent-risk floors or cap control-effectiveness ratings in enterprise risk scoring?](https://davidamitchell.github.io/Research/research/2026-05-09-prc-risk-scoring-unstandardized-workforce-processes.html) - risk-scoring implications for undocumented or manual workforce workflows.
- [x] [Mitchell (2026) Under Basel guidance, when should key-person dependency be treated as a workforce management issue versus a reportable operational risk?](https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html) - concentrated people-process dependency.
- [x] [Mitchell (2026) What minimum provenance evidence is required to satisfy National Institute of Standards and Technology (NIST) Special Publication (SP) 800-53 controls when workforce data moves through Microsoft Lists, Excel, and PowerPoint artifacts?](https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html) - detectability and provenance gaps in workforce artifacts.

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. Sections 0 to 5 are the investigation; section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: Which explicit criteria best distinguish ordinary process inefficiency from hidden control and dependency risk in workforce-capacity and skill-tracking workflows?
- Scope: Decision criteria, escalation triggers, and workforce-process control implications; no tool design or enterprise-specific financial modeling.
- Constraints: The output must use auditable language that maps to formal risk, control, appetite, and tolerance concepts.
- Output format: One knowledge item with a classification rubric, representative scenario tests, and source-bound findings.
- Prior completed items checked: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html ; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html ; https://davidamitchell.github.io/Research/research/2026-05-09-prc-risk-scoring-unstandardized-workforce-processes.html ; https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html ; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html
- [inference; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.lean.org/lexicon-terms/cycle-time/] Ordinary process inefficiency refers here to visible waste, such as waiting, unnecessary processing, correction, rework, or other nonvalue-creating time, that raises cycle time or effort but stays within established control limits and disruption tolerances.
- [inference; source: https://www.iso.org/iso-31000-risk-management.html; https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline] Hidden control and dependency risk refers here to a people, process, system, information, facility, or third-party weakness that may not yet have produced a realized loss but can still breach risk appetite, disruption tolerance, or control objectives if the condition persists or interacts with other dependencies.

### §1 Question Decomposition

1. What signals identify ordinary process inefficiency?
   1.1 Which Lean waste categories describe visible delay, rework, and nonvalue-creating work?
   1.2 Which measurable workflow properties show local and reversible performance loss?
2. What signals identify hidden control and dependency risk?
   2.1 Which standards define operational risk, resilience, risk appetite, and tolerances?
   2.2 Which indicators show that a weakness is approaching or exceeding formal limits?
3. Which auditable criteria best separate the two categories?
   3.1 How should consequence and reversibility be used?
   3.2 How should persistence and recurrence be used?
   3.3 How should detectability and provenance be used?
   3.4 How should dependency concentration and interconnectedness be used?
   3.5 How should control-effectiveness evidence be used?
4. How do the criteria behave in representative workforce scenarios?
   4.1 Backlog in a visible skills-update queue.
   4.2 Manual payroll or access-exception tracking owned by one person.
   4.3 Approval queues where review quality collapses into nominal sign-off.
5. What rubric can a risk-intake workflow apply without guessing?
   5.1 Which conditions keep an issue in the inefficiency bucket?
   5.2 Which conditions require immediate or near-term escalation into risk intake?

### §2 Investigation

#### What counts as ordinary process inefficiency?

- [fact; source: https://www.lean.org/lexicon-terms/seven-wastes/] Lean Enterprise Institute defines waiting as operators standing idle while resources, decisions, or needed inputs fail to arrive, and defines correction as inspection, rework, and scrap.
- [fact; source: https://www.lean.org/lexicon-terms/cycle-time/] Lean Enterprise Institute defines cycle time as the time required to complete a process by actual measurement, and defines nonvalue-creating time as time spent on activities such as storage, inspection, and rework that add cost but no customer value.
- [inference; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.lean.org/lexicon-terms/cycle-time/] These sources support a narrow inefficiency baseline: visible queueing, rework, excess handling, and other waste indicate performance loss, but they do not by themselves establish control weakness, critical-operation exposure, or risk-appetite pressure.
- [inference; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.lean.org/lexicon-terms/cycle-time/] A workforce workflow should remain in the ordinary inefficiency bucket when the problem is visible, locally owned, reversible through normal process improvement, and measurable through routine backlog, cycle-time, or rework metrics.

#### What makes the same pattern a risk issue?

- [fact; source: https://www.iso.org/iso-31000-risk-management.html] ISO 31000 describes risk management as identifying, analyzing, evaluating, treating, monitoring, and communicating risk across an organization.
- [fact; source: https://csrc.nist.gov/pubs/sp/800/30/r1/final] NIST Special Publication 800-30 states that risk assessments provide senior leaders and executives with the information needed to determine appropriate courses of action in response to identified risks.
- [fact; source: https://csrc.nist.gov/Projects/risk-management/about-rmf] The National Institute of Standards and Technology Risk Management Framework is a risk-based approach that integrates preparation, categorization, control selection, implementation, assessment, authorization, and continuous monitoring.
- [fact; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline] Office of the Superintendent of Financial Institutions defines operational risk as the risk of loss resulting from people, inadequate processes and systems, or external events, and defines operational resilience as the ability to deliver operations, especially critical operations, through disruption.
- [fact; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline] Office of the Superintendent of Financial Institutions requires operational risk appetite to include qualitative and quantitative measures and explicit limits, and it requires escalation when risk levels approach or exceed those limits.
- [fact; source: https://www.bis.org/bcbs/publ/d516.htm; https://www.bis.org/bcbs/publ/d515.htm] Basel Committee on Banking Supervision frames operational resilience around operational-risk-related events that can cause significant operational failure or wide-scale disruption, and positions that resilience model as an extension of sound operational-risk management.
- [inference; source: https://www.iso.org/iso-31000-risk-management.html; https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.bis.org/bcbs/publ/d516.htm] A workflow problem becomes a risk issue when it threatens objectives, exceeds or trends toward formal limits, weakens required controls, or can impair critical operations under plausible disruption, rather than only making work slower or more expensive.

#### Which auditable criteria best separate inefficiency from hidden risk?

- [fact; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline] Office of the Superintendent of Financial Institutions requires critical operations to be mapped end to end across people, technology, processes, information, facilities, third parties, and the dependencies among them.
- [fact; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline] Office of the Superintendent of Financial Institutions states that Key Risk Indicators, meaning Key Risk Indicator (KRI) tools, should exist at business-unit and enterprise levels, should include leading and lagging indicators, and should have escalation protocols that warn when risk levels approach or exceed limits.
- [fact; source: https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/] Institute of Operational Risk states that Key Risk Indicators help signal changes in risk exposure, resource stretch, and control effectiveness, and that their design includes thresholds, governance, and reporting structures.
- [inference; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.lean.org/lexicon-terms/cycle-time/; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/] The most defensible distinction criteria are consequence and reversibility, persistence and recurrence, detectability and provenance, dependency concentration and interconnectedness, and control-effectiveness evidence relative to appetite and tolerance.
- [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://csrc.nist.gov/pubs/sp/800/30/r1/final] Consequence and reversibility separate local friction from formal risk because a reversible delay that stays inside service tolerance does not require the same response as a condition that can block a critical operation, rights-significant decision, or mandatory control activity.
- [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/] Persistence and recurrence matter because a condition that survives local fixes or reappears across reporting periods behaves like a leading indicator of control weakness or residual risk, not merely like one noisy queue.
- [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html] Detectability and provenance matter because a delay or manual workaround becomes harder to manage when control owners cannot verify what changed, who changed it, or whether downstream decisions are already using stale or altered data.
- [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.bis.org/bcbs/publ/d516.htm; https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html] Dependency concentration and interconnectedness matter because single-person, single-tool, or single-step choke points can turn an otherwise small local delay into a latent interruption path for a critical operation.
- [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://davidamitchell.github.io/Research/research/2026-05-09-prc-risk-scoring-unstandardized-workforce-processes.html] Control-effectiveness evidence matters because undocumented, team-local, or partly manual processes are harder to defend as low-risk when risk and control assessments cannot show that mitigants keep residual risk within limits.

#### How do the criteria behave in representative workforce scenarios?

- [inference; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.lean.org/lexicon-terms/cycle-time/; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline] A visible backlog in a skills-update queue is usually ordinary inefficiency when the queue is measurable, reversible, and not connected to access rights, regulated attestation, payroll, or other critical operations, because the symptom is wasted time rather than impaired control.
- [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html] The same skills-update queue becomes hidden risk when stale records feed training compliance, access gating, or safety certification and the workflow lacks strong provenance, because the issue now combines persistence with low detectability and downstream decision impact.
- [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.bis.org/bcbs/publ/d516.htm; https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html] A manual payroll-exception or access-exception tracker owned by one person is hidden risk rather than mere inefficiency when the owner, spreadsheet, or local process is a single operational dependency, because failure can breach disruption tolerances and critical-operation continuity.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html] An approval queue should be escalated from inefficiency to hidden risk when human review becomes nominal sign-off, because a collapsed verification step removes detectability while preserving the appearance of control.

#### What rubric can risk intake apply?

- [inference; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.lean.org/lexicon-terms/cycle-time/; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline] Classify as ordinary inefficiency when all of the following hold: the symptom is visible waste, the effect is locally reversible, routine metrics can detect and track it, no critical operation or rights-significant decision depends on the weak step, and the condition remains within risk appetite and disruption tolerance.
- [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/; https://www.bis.org/bcbs/publ/d516.htm] Classify as hidden control and dependency risk when any high-severity condition or two moderate conditions are present, because that threshold captures either one clearly material failure path or a reinforcing combination of smaller weaknesses.
- [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html] High-severity conditions are: critical-operation exposure, rights-significant or regulated decision use, single-point dependency, missing or weak provenance, or an observed breach of risk appetite or disruption tolerance.
- [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] Moderate conditions are: recurrence after local fixes, rising backlog or cycle time against limit trends, weak documentation of controls, reduced review quality, or multi-step dependency chains whose combined failure would be hard to detect quickly.
- [assumption; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/] The exact numeric trigger for backlog age, cycle-time deviation, sample rate, or tolerance breach must be set locally, because the reviewed sources support thresholded escalation but do not publish portable numbers for every workforce workflow.

### §3 Reasoning

- [inference; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.lean.org/lexicon-terms/cycle-time/; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline] Cost and delay are insufficient discriminators, because both ordinary inefficiency and formal risk can produce queues, rework, and extra handling; the difference is whether the condition also weakens control, increases dependency exposure, or threatens a limit or tolerance.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline] Auditable classification has to use decision-useful evidence, not intuition, so appetite, limits, tolerances, risk and control assessments, and scenario analysis are stronger anchors than generalized language such as "this feels important."
- [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html] Detectability is pivotal because a hidden data-quality, provenance, or review-quality defect can leave a workflow apparently functioning while silently degrading the trustworthiness of downstream decisions.
- [inference; source: https://www.bis.org/bcbs/publ/d516.htm; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html] Concentrated dependency is the clearest bridge from inefficiency to hidden risk, because it converts a local delay into an interruption path that can disable a wider process when one person, step, or artifact fails.

### §4 Consistency Check

- [fact; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.lean.org/lexicon-terms/cycle-time/; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline] No direct contradiction remained between the process-efficiency sources and the risk-governance sources, because the former describe waste and the latter describe conditions under which weakness becomes loss- or disruption-relevant.
- [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/] The main ambiguity, whether persistence alone is enough to call something risk, was resolved by treating persistence as necessary but not sufficient unless it is paired with control weakness, rising indicator pressure, or material dependency.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html] A second ambiguity, whether overloaded review is only an efficiency problem, was resolved by classifying it as risk once verification quality collapses and the workflow keeps a false signal that a control is still active.

### §5 Depth and Breadth Expansion

- [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html] Technical lens: detectability is the strongest hidden-risk criterion in data-heavy workforce workflows because incomplete provenance and weak auditability let stale, altered, or unverifiable records pass into later decisions without clear alarms.
- [inference; source: https://www.iso.org/iso-31000-risk-management.html; https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline] Regulatory lens: standards bodies consistently expect explicit assessment, monitoring, and response once an issue can affect objectives, limits, or critical operations, which makes "just inefficiency" an unsafe label when evidence already points to control failure.
- [inference; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/] Economic lens: not every delay should enter the risk register, because flooding risk processes with ordinary waste removes signal from genuine limit pressure and wastes scarce escalation capacity.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html] Behavioural lens: repeated schedule pressure can normalize workarounds and nominal review, so a workflow that begins as inefficiency can mature into hidden risk if management treats queue clearance as success while evidence quality deteriorates.

### §6 Synthesis

**Executive summary:**

Ordinary process inefficiency should be classified as hidden control and dependency risk only when the observed waste also threatens control objectives, critical operations, or approved limits through persistence, low detectability, concentrated dependency, or interconnectedness. [inference; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.lean.org/lexicon-terms/cycle-time/; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/]

The strongest formal boundary is not cost alone but whether the condition can still be handled as visible, reversible local waste or has become a people, process, system, information, facility, or third-party weakness that affects risk appetite, disruption tolerance, or decision trustworthiness. [inference; source: https://www.iso.org/iso-31000-risk-management.html; https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline]

For workforce-capacity and skill-tracking workflows, the most decision-useful criteria are consequence and reversibility, persistence and recurrence, detectability and provenance, dependency concentration and interconnectedness, and control-effectiveness evidence. [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/; https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html]

A workable intake heuristic from this evidence is to keep an issue in the inefficiency bucket only when all five criteria remain benign, and to escalate it into risk intake when either one clearly material condition or a reinforcing cluster of weaker conditions appears. [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/; https://www.bis.org/bcbs/publ/d516.htm]

**Key findings:**

1. **Visible waiting, correction, rework, and other nonvalue-creating time are reliable indicators of ordinary process inefficiency, but those signals alone do not prove formal risk because Lean treats them as waste symptoms rather than as evidence of breached control objectives or threatened critical operations.** ([inference]; medium confidence; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.lean.org/lexicon-terms/cycle-time/)
2. **A workforce workflow becomes a formal risk concern when a weakness in people, processes, systems, or external dependencies can affect objectives, drive loss, or require a risk-based response from leadership, because the reviewed ISO, NIST, and Office of the Superintendent of Financial Institutions sources all frame risk in terms of decision-worthy exposure rather than inconvenience alone.** ([inference]; high confidence; source: https://www.iso.org/iso-31000-risk-management.html; https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://csrc.nist.gov/Projects/risk-management/about-rmf; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline)
3. **The most auditable distinction criteria are consequence and reversibility, persistence and recurrence, detectability and provenance, dependency concentration and interconnectedness, and control-effectiveness evidence, because those dimensions map cleanly onto appetite, limits, tolerances, Key Risk Indicator governance, and end-to-end dependency mapping.** ([inference]; medium confidence; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/)
4. **Persistence after local fixes or across repeated reporting periods should usually be treated as an escalation signal rather than as routine noise, because the reviewed guidance uses leading and lagging indicators, residual-risk reassessment, and scenario analysis to detect weaknesses that are maturing toward a breach of limits.** ([inference]; medium confidence; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/)
5. **Low detectability or weak provenance turns a delay or manual workaround into hidden risk when control owners cannot verify what changed, who changed it, or whether stale or altered information is already driving downstream workforce decisions.** ([inference]; medium confidence; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html)
6. **Single-person, single-tool, or single-step dependency is the clearest bridge from local inefficiency to hidden risk, because end-to-end mapping and resilience guidance treat concentrated dependencies as interruption paths that can disable critical operations under plausible disruption.** ([inference]; medium confidence; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.bis.org/bcbs/publ/d516.htm; https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html)
7. **Approval bottlenecks and rubber-stamping should be escalated as hidden risk, not left as efficiency debt, when review quality collapses into nominal sign-off, because the workflow then loses a real detection and challenge control while still presenting a misleading appearance of oversight.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html)
8. **A practical intake heuristic is to keep an issue in the inefficiency bucket only when it is visible, locally reversible, within tolerance, and unlinked to concentrated dependency or evidence gaps, and to escalate it into risk intake when either one clearly material condition or a reinforcing cluster of weaker conditions is present.** ([inference]; medium confidence; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/; https://davidamitchell.github.io/Research/research/2026-05-09-prc-risk-scoring-unstandardized-workforce-processes.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Visible waste signals point to inefficiency, but do not alone prove formal risk. | https://www.lean.org/lexicon-terms/seven-wastes/; https://www.lean.org/lexicon-terms/cycle-time/ | medium | waste baseline |
| [inference] Formal risk begins when exposure can affect objectives, cause loss, or justify risk-based leadership response. | https://www.iso.org/iso-31000-risk-management.html; https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://csrc.nist.gov/Projects/risk-management/about-rmf; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline | high | standards baseline |
| [inference] The five best distinction criteria are consequence, persistence, detectability, concentration, and control evidence. | https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/ | medium | auditable rubric |
| [inference] Persistence and recurrence should usually trigger escalation because indicator and reassessment guidance treats them as warning signals of growing residual risk. | https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/ | medium | indicator pressure |
| [inference] Weak detectability and provenance convert delay into hidden risk when downstream decisions can no longer be trusted or reconstructed. | https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html | medium | hidden-state problem |
| [inference] Concentrated dependency converts local friction into interruption risk for critical operations. | https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.bis.org/bcbs/publ/d516.htm; https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html | medium | concentration path |
| [inference] Review bottlenecks become risk when nominal sign-off removes real challenge and detection. | https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html | medium | control-illusion case |
| [inference] The intake heuristic should use all-benign conditions for inefficiency and a material-condition or clustered-condition test for risk escalation. | https://www.lean.org/lexicon-terms/seven-wastes/; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/; https://davidamitchell.github.io/Research/research/2026-05-09-prc-risk-scoring-unstandardized-workforce-processes.html | medium | synthesized rule |

**Assumptions:**

- [assumption; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/] Each organization must set its own numeric thresholds for backlog age, cycle-time deviation, sample rate, and tolerance breach, because the reviewed guidance supports thresholded escalation but does not prescribe portable numbers for every workforce process.
- [assumption; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.bis.org/bcbs/publ/d516.htm] The financial-sector operational-risk and resilience guidance is directionally applicable to workforce-capacity and skill-tracking workflows outside banking, because the relevant control surfaces, people, process, information, dependency, and continuity questions are shared.
- [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] The prior completed repository items cited here are treated as valid supporting syntheses for provenance failure and review-quality collapse, because they map directly onto the same workforce control surfaces examined in this item.

**Analysis:**

The evidence weighs against both extreme interpretations. [inference; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline] Treating every delay as formal risk would flood intake queues with ordinary waste, while treating every queue or manual workaround as mere inefficiency would ignore the moment at which control failure, concentrated dependency, or low detectability makes the same pattern materially more dangerous. [inference; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.lean.org/lexicon-terms/cycle-time/; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline]

The most useful decision boundary is therefore not "is this annoying or expensive," but "can this weakness still be handled as visible and reversible local waste, or has it become an exposure that could evade detection, exceed a limit, or impair a critical operation." [inference; source: https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline] That boundary makes consequence, persistence, detectability, concentration, and control evidence more decision-useful than raw cost or elapsed time by themselves. [inference; source: https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/; https://davidamitchell.github.io/Research/research/2026-05-09-prc-risk-scoring-unstandardized-workforce-processes.html]

One plausible rival approach is to keep the taxonomy binary but let backlog size decide by itself. [inference; source: https://www.lean.org/lexicon-terms/cycle-time/; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/] The evidence is weaker for that approach because a small backlog can still be materially risky when it sits on a single-point dependency or weak provenance path, while a large backlog can remain ordinary inefficiency if it is visible, reversible, and fully outside critical controls or formal limits. [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html]

The recommended rubric is therefore a starting heuristic: classify as ordinary inefficiency only when all five criteria remain benign, classify as hidden risk when a clearly material condition or a reinforcing cluster of weaker conditions appears, and force immediate escalation when the issue already affects a critical operation, regulated evidence, rights-significant decision, or documented breach of appetite or tolerance. [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.bis.org/bcbs/publ/d516.htm; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/]

**Risks, gaps, uncertainties:**

- [fact; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.lean.org/lexicon-terms/cycle-time/] The process-efficiency evidence is strong on identifying waste categories and timing concepts, but it does not itself provide a native formal risk taxonomy.
- [fact; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/] The formal risk guidance is strong on limits, indicators, dependencies, and escalation, but it does not publish universal numeric thresholds for workforce-specific backlog age, sample size, or acceptable review latency.
- [inference; source: https://www.bis.org/bcbs/publ/d516.htm; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline] The strongest public primary material comes from financial-sector resilience guidance, so cross-sector transfer is well grounded on control surfaces but not yet benchmarked with large public datasets for every workforce workflow type.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html] Review-quality collapse is well supported as a governance mechanism, but the exact breakpoint where an approval queue stops being useful still depends on local workload, skill, and evidence-presentation design.

**Open questions:**

- What portable benchmark ranges, if any, could be published for backlog age, review latency, or sample-rate thresholds in workforce workflows without creating false precision across sectors?
- Which governance overlay most efficiently closes provenance and detectability gaps for ordinary workforce artifacts before those artifacts become authoritative records?
- How should the rubric change when the concentrated dependency sits in an external service provider rather than in an internal person, team, or artifact?

### §7 Recursive Review

- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-05-09-process-inefficiency-vs-latent-risk-taxonomy.md] Review result: self-review completed on the current draft.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-05-09-process-inefficiency-vs-latent-risk-taxonomy.md] Acronym audit: the current draft expands ISO, NIST, Key Risk Indicator, and Office of the Superintendent of Financial Institutions on first use.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-05-09-process-inefficiency-vs-latent-risk-taxonomy.md] Claim audit: visible Research Skill Output claim-bearing prose in the current draft carries a fact, inference, or assumption label with URL-backed source context.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-05-09-process-inefficiency-vs-latent-risk-taxonomy.md] Findings parity check: section 6 Synthesis and Findings are aligned in the current draft.
- [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/; https://www.lean.org/lexicon-terms/seven-wastes/] Confidence result: medium, because the standards baseline is strong but the intake heuristic remains synthesized rather than directly published as a universal taxonomy.

---

## Findings

*(Populated from section 6 Synthesis above.)*

### Executive Summary

Ordinary process inefficiency should be classified as hidden control and dependency risk only when the observed waste also threatens control objectives, critical operations, or approved limits through persistence, low detectability, concentrated dependency, or interconnectedness. [inference; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.lean.org/lexicon-terms/cycle-time/; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/]

The strongest formal boundary is not cost alone but whether the condition can still be handled as visible, reversible local waste or has become a people, process, system, information, facility, or third-party weakness that affects risk appetite, disruption tolerance, or decision trustworthiness. [inference; source: https://www.iso.org/iso-31000-risk-management.html; https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline]

For workforce-capacity and skill-tracking workflows, the most decision-useful criteria are consequence and reversibility, persistence and recurrence, detectability and provenance, dependency concentration and interconnectedness, and control-effectiveness evidence. [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/; https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html]

A workable intake heuristic from that evidence is to keep an issue in the inefficiency bucket only when all five criteria remain benign, and to escalate it into risk intake when either one clearly material condition or a reinforcing cluster of weaker conditions appears. [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/; https://www.bis.org/bcbs/publ/d516.htm]

### Key Findings

1. **Visible waiting, correction, rework, and other nonvalue-creating time are reliable indicators of ordinary process inefficiency, but those signals alone do not prove formal risk because Lean treats them as waste symptoms rather than as evidence of breached control objectives or threatened critical operations.** ([inference]; medium confidence; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.lean.org/lexicon-terms/cycle-time/)
2. **A workforce workflow becomes a formal risk concern when a weakness in people, processes, systems, or external dependencies can affect objectives, drive loss, or require a risk-based response from leadership, because the reviewed ISO, NIST, and Office of the Superintendent of Financial Institutions sources all frame risk in terms of decision-worthy exposure rather than inconvenience alone.** ([inference]; high confidence; source: https://www.iso.org/iso-31000-risk-management.html; https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://csrc.nist.gov/Projects/risk-management/about-rmf; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline)
3. **The most auditable distinction criteria are consequence and reversibility, persistence and recurrence, detectability and provenance, dependency concentration and interconnectedness, and control-effectiveness evidence, because those dimensions map cleanly onto appetite, limits, tolerances, Key Risk Indicator governance, and end-to-end dependency mapping.** ([inference]; medium confidence; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/)
4. **Persistence after local fixes or across repeated reporting periods should usually be treated as an escalation signal rather than as routine noise, because the reviewed guidance uses leading and lagging indicators, residual-risk reassessment, and scenario analysis to detect weaknesses that are maturing toward a breach of limits.** ([inference]; medium confidence; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/)
5. **Low detectability or weak provenance turns a delay or manual workaround into hidden risk when control owners cannot verify what changed, who changed it, or whether stale or altered information is already driving downstream workforce decisions.** ([inference]; medium confidence; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html)
6. **Single-person, single-tool, or single-step dependency is the clearest bridge from local inefficiency to hidden risk, because end-to-end mapping and resilience guidance treat concentrated dependencies as interruption paths that can disable critical operations under plausible disruption.** ([inference]; medium confidence; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.bis.org/bcbs/publ/d516.htm; https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html)
7. **Approval bottlenecks and rubber-stamping should be escalated as hidden risk, not left as efficiency debt, when review quality collapses into nominal sign-off, because the workflow then loses a real detection and challenge control while still presenting a misleading appearance of oversight.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html)
8. **A practical intake heuristic is to keep an issue in the inefficiency bucket only when it is visible, locally reversible, within tolerance, and unlinked to concentrated dependency or evidence gaps, and to escalate it into risk intake when either one clearly material condition or a reinforcing cluster of weaker conditions is present.** ([inference]; medium confidence; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/; https://davidamitchell.github.io/Research/research/2026-05-09-prc-risk-scoring-unstandardized-workforce-processes.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Visible waste signals point to inefficiency, but do not alone prove formal risk. | https://www.lean.org/lexicon-terms/seven-wastes/; https://www.lean.org/lexicon-terms/cycle-time/ | medium | waste baseline |
| [inference] Formal risk begins when exposure can affect objectives, cause loss, or justify risk-based leadership response. | https://www.iso.org/iso-31000-risk-management.html; https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://csrc.nist.gov/Projects/risk-management/about-rmf; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline | high | standards baseline |
| [inference] The five best distinction criteria are consequence, persistence, detectability, concentration, and control evidence. | https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/ | medium | auditable rubric |
| [inference] Persistence and recurrence should usually trigger escalation because indicator and reassessment guidance treats them as warning signals of growing residual risk. | https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/ | medium | indicator pressure |
| [inference] Weak detectability and provenance convert delay into hidden risk when downstream decisions can no longer be trusted or reconstructed. | https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html | medium | hidden-state problem |
| [inference] Concentrated dependency converts local friction into interruption risk for critical operations. | https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.bis.org/bcbs/publ/d516.htm; https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html | medium | concentration path |
| [inference] Review bottlenecks become risk when nominal sign-off removes real challenge and detection. | https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html | medium | control-illusion case |
| [inference] The intake heuristic should use all-benign conditions for inefficiency and a material-condition or clustered-condition test for risk escalation. | https://www.lean.org/lexicon-terms/seven-wastes/; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/; https://davidamitchell.github.io/Research/research/2026-05-09-prc-risk-scoring-unstandardized-workforce-processes.html | medium | synthesized rule |

### Assumptions

- [assumption; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/] Each organization must set its own numeric thresholds for backlog age, cycle-time deviation, sample rate, and tolerance breach, because the reviewed guidance supports thresholded escalation but does not prescribe portable numbers for every workforce process.
- [assumption; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.bis.org/bcbs/publ/d516.htm] The financial-sector operational-risk and resilience guidance is directionally applicable to workforce-capacity and skill-tracking workflows outside banking, because the relevant control surfaces, people, process, information, dependency, and continuity questions are shared.
- [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] The prior completed repository items cited here are treated as valid supporting syntheses for provenance failure and review-quality collapse, because they map directly onto the same workforce control surfaces examined in this item.

### Analysis

The evidence weighs against both extreme interpretations. [inference; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline] Treating every delay as formal risk would flood intake queues with ordinary waste, while treating every queue or manual workaround as mere inefficiency would ignore the moment at which control failure, concentrated dependency, or low detectability makes the same pattern materially more dangerous. [inference; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.lean.org/lexicon-terms/cycle-time/; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline]

The most useful decision boundary is therefore not "is this annoying or expensive," but "can this weakness still be handled as visible and reversible local waste, or has it become an exposure that could evade detection, exceed a limit, or impair a critical operation." [inference; source: https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline] That boundary makes consequence, persistence, detectability, concentration, and control evidence more decision-useful than raw cost or elapsed time by themselves. [inference; source: https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/; https://davidamitchell.github.io/Research/research/2026-05-09-prc-risk-scoring-unstandardized-workforce-processes.html]

One plausible rival approach is to keep the taxonomy binary but let backlog size decide by itself. [inference; source: https://www.lean.org/lexicon-terms/cycle-time/; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/] The evidence is weaker for that approach because a small backlog can still be materially risky when it sits on a single-point dependency or weak provenance path, while a large backlog can remain ordinary inefficiency if it is visible, reversible, and fully outside critical controls or formal limits. [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://davidamitchell.github.io/Research/research/2026-05-09-key-person-dependency-basel-risk-linkage.html; https://davidamitchell.github.io/Research/research/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.html]

The recommended rubric is therefore a starting heuristic: classify as ordinary inefficiency only when all five criteria remain benign, classify as hidden risk when a clearly material condition or a reinforcing cluster of weaker conditions appears, and force immediate escalation when the issue already affects a critical operation, regulated evidence, rights-significant decision, or documented breach of appetite or tolerance. [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.bis.org/bcbs/publ/d516.htm; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/]

### Risks, Gaps, and Uncertainties

- [fact; source: https://www.lean.org/lexicon-terms/seven-wastes/; https://www.lean.org/lexicon-terms/cycle-time/] The process-efficiency evidence is strong on identifying waste categories and timing concepts, but it does not itself provide a native formal risk taxonomy.
- [fact; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/] The formal risk guidance is strong on limits, indicators, dependencies, and escalation, but it does not publish universal numeric thresholds for workforce-specific backlog age, sample size, or acceptable review latency.
- [inference; source: https://www.bis.org/bcbs/publ/d516.htm; https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline] The strongest public primary material comes from financial-sector resilience guidance, so cross-sector transfer is well grounded on control surfaces but not yet benchmarked with large public datasets for every workforce workflow type.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html] Review-quality collapse is well supported as a governance mechanism, but the exact breakpoint where an approval queue stops being useful still depends on local workload, skill, and evidence-presentation design.

### Open Questions

- What portable benchmark ranges, if any, could be published for backlog age, review latency, or sample-rate thresholds in workforce workflows without creating false precision across sectors?
- Which governance overlay most efficiently closes provenance and detectability gaps for ordinary workforce artifacts before those artifacts become authoritative records?
- How should the rubric change when the concentrated dependency sits in an external service provider rather than in an internal person, team, or artifact?

---

## Output

- Type: knowledge
- Description: Produced an auditable taxonomy and intake rubric that separates visible workforce-process waste from hidden control and dependency risk by using consequence, persistence, detectability, concentration, and control-effectiveness evidence. [inference; source: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline; https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/; https://www.lean.org/lexicon-terms/seven-wastes/]
- Links:
  - https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/operational-risk-management-resilience-guideline
  - https://www.ior-institute.org/sound-practice-guidance/key-risk-indicators/
  - https://www.lean.org/lexicon-terms/seven-wastes/
