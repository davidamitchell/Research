---
title: "Universal Entity Lifecycle Governance Framework (UELGF): runtime feedback loop — signal taxonomy, automated response taxonomy, feedback closure to the rail system, and feedback closure to the systems capability debt programme as a structured demand signal"
added: 2026-04-27T01:28:25+00:00
status: backlog
priority: high
blocks: [2026-04-27-uelgf-synthesis-complete-framework]
tags: [uelgf, runtime-feedback, continuous-evaluation, observability, signal-aggregation, scope-drift, rail-improvement, systems-capability-debt, demand-signal, pep, pip, regulated-banking]
started: ~
completed: ~
output: [knowledge]
---

# Universal Entity Lifecycle Governance Framework (UELGF): runtime feedback loop — signal taxonomy, automated response taxonomy, feedback closure to the rail system, and feedback closure to the systems capability debt programme as a structured demand signal

## Research Question

How should the UELGF specify the runtime feedback loop — covering signal taxonomy, signal aggregation and evaluation mechanism, automated response taxonomy proportionate to signal severity, re-evaluation trigger mechanism, feedback closure to the rail system, and feedback closure to the systems capability debt programme as a machine-readable structured demand signal — to ensure governance is a continuous property of operational existence rather than a point-in-time check at deployment?

## Scope

**In scope:**
- Signal taxonomy: action blocks (PEP denied a request), scope boundary approaches (entity consistently requesting actions at the edge of its registered scope), volume anomalies (entity acting at a rate inconsistent with registered purpose), data access anomalies (entity accessing data not previously accessed at or near its CIA ceiling), dependency anomalies (entity calling systems not in its registered dependency graph), scope drift (pattern of actions diverging from registered scope boundary over time)
- Signal aggregation and evaluation mechanism: how individual PEP (Policy Enforcement Point) signals are aggregated over time, what thresholds trigger automated responses, and how the PDP (Policy Decision Point) evaluates aggregate signal against the entity's current governance profile
- Automated response taxonomy proportionate to signal severity: logging only; owner notification; soft suspension (licence flagged as under review, owner must respond within a defined period by CIA tier); hard suspension (licence immediately revoked pending investigation); decommission trigger (signal sufficient to initiate formal decommission without owner action)
- Re-evaluation trigger mechanism: what signal patterns trigger formal re-evaluation of CIA rating, invariants, or rail classification; what the re-evaluation process produces; how the outcome is enacted
- Feedback closure to the rail system: how aggregate signal across all entities on a given rail informs rail improvement; how repeated scope boundary violations on a given rail trigger expansion of the rail's scope specification rather than continued individual escalations; how repeated exceptions trigger creation of a new governed rail
- Feedback closure to the systems capability debt programme: how the aggregate pattern of scope violations, volume anomalies, and dependency anomalies across citizen-built entities constitutes a structured demand signal — a machine-readable map of where systems capability debt is generating ungoverned workaround pressure — and how this signal is formally reported to the engineering investment programme
- The latency requirements for each automated response type by CIA tier

**Out of scope:**
- Policy architecture component design (covered by `2026-04-27-uelgf-policy-architecture-8-layer-context`) — though the interaction between PEP signals and the PIP is in scope
- Decommission procedure details (covered by `2026-04-27-uelgf-decommission-lifecycle`) — though the decommission trigger from the feedback loop is in scope
- Rail specifications (covered by `2026-04-27-uelgf-governed-golden-rails`) — though rail improvement from aggregate signal is in scope

**Constraints:**
- Signal taxonomy must be grounded in observable PEP events — signals must be derivable from system logs, not from entity owner self-reporting
- The structured demand signal to the systems capability debt programme must be machine-readable and formally reported — it cannot be an informal observation by a governance analyst
- Threshold values for automated responses must be parameterisable by CIA tier and entity type — a single threshold for all entities is not acceptable

## Context

Without a runtime feedback loop, governance is a point-in-time property: an entity is compliant at scaffold generation and progressively non-compliant in operation with no detection mechanism. The feedback loop converts governance from a check into a continuous property. Its secondary function — feedback closure to the systems capability debt programme — transforms the UELGF from a governance-only framework into an active input to the engineering investment prioritisation process. When citizen-built entities consistently approach or exceed their scope boundaries, this is a machine-readable signal that the underlying capability gap has not been closed. The systems capability debt programme needs this signal to prioritise integration and capability remediation work objectively rather than based on anecdote and stakeholder lobbying.

Prior completed research directly informs this item:
- [AI and low-code observability and telemetry governance](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html) — observability patterns for citizen-built entities
- [AI agent control plane architecture for enterprise](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html) — agent observability and runtime control
- [Systems capability debt agentic AI risk synthesis](https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html) — structured demand signal concept and systems capability debt context
- [Access control amplification under agentic operations](https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html) — volume and dependency anomaly detection context

## Approach

1. **Signal taxonomy grounding:** Survey existing runtime signal taxonomies in security monitoring (SIEM (Security Information and Event Management) alert categories, MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) technique categories, AWS GuardDuty finding types) and in SRE (Site Reliability Engineering) observability practice (the Four Golden Signals: latency, traffic, errors, saturation) to determine whether existing taxonomies cover the UELGF signal types or whether novel signal definitions are required. Justify each signal type in the taxonomy against a stated detection objective.
2. **Signal aggregation mechanisms:** Survey anomaly detection and threshold evaluation patterns in observability platforms (Prometheus AlertManager, Datadog Monitors, AWS CloudWatch Anomaly Detection) to identify which aggregation mechanisms are applicable to the UELGF signal types. Distinguish absolute threshold triggers (entity exceeded N action blocks in M minutes) from relative/anomaly triggers (entity's action rate is X standard deviations above its historical baseline).
3. **Automated response taxonomy calibration:** Survey how automated response taxonomies are calibrated in comparable governance frameworks — PCI DSS automated response requirements, DORA (Digital Operational Resilience Act) incident classification and response timelines, APRA CPS 230 operational risk event response — to produce a calibrated UELGF response taxonomy with defined latency requirements per CIA tier.
4. **Rail improvement feedback mechanism:** Survey how product teams use operational telemetry as input to product roadmaps (user research from system behaviour, error rate analysis as feature prioritisation input, A/B test signals) and assess how these mechanisms translate to the rail-as-product model. The specific question is: what aggregate signal pattern constitutes evidence that the rail's scope specification is too narrow and needs expansion?
5. **Structured demand signal specification:** Specify the format of the structured demand signal to the systems capability debt programme. The signal must be machine-readable and formally reportable. Survey how demand signals are structured in product management and engineering investment contexts (JIRA epics, OKR (Objectives and Key Results) input signals, technical debt backlog management) to identify a format that is compatible with existing investment prioritisation practice.
6. **Re-evaluation trigger formalisation:** Specify the signal patterns that trigger formal re-evaluation of CIA rating, invariants, or rail classification. Distinguish patterns that trigger re-evaluation (elevated ongoing anomaly) from patterns that trigger immediate suspension (acute violation). Specify the re-evaluation process: who conducts it, what evidence is evaluated, what outcomes are possible (confirmed classification, reclassification, decommission trigger), and how the outcome is implemented.

## Sources

- [ ] [AI and low-code observability and telemetry governance — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html) — observability patterns for UELGF entities
- [ ] [AI agent control plane architecture — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html) — agent runtime observability
- [ ] [Systems capability debt agentic AI risk synthesis — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html) — demand signal and systems capability debt context
- [ ] [Access control amplification under agentic operations — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html) — volume and dependency anomaly patterns
- [ ] [MITRE ATT&CK — Tactics, Techniques, and Procedures taxonomy](https://attack.mitre.org/) — runtime signal taxonomy analogue for scope violations
- [ ] [Google SRE Book — Chapter 6: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) — Four Golden Signals and anomaly detection patterns
- [ ] [DORA Regulation (EU) 2022/2554 — ICT-related incident classification](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554) — automated response and incident classification standards
- [ ] [APRA CPS 230 — Operational risk event response requirements](https://handbook.apra.gov.au/standard/cps-230) — calibrated response taxonomy for regulated financial services
- [ ] [Prometheus AlertManager — alerting rules and routing](https://prometheus.io/docs/alerting/latest/alertmanager/) — signal aggregation and threshold evaluation in practice
- [ ] [NIST SP 800-137 — Information Security Continuous Monitoring](https://csrc.nist.gov/pubs/sp/800/137/final) — continuous monitoring as a governance property framework

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

-

### §1 Question Decomposition

-

### §2 Investigation

-

### §3 Reasoning

-

### §4 Consistency Check

-

### §5 Depth and Breadth Expansion

-

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

### Key Findings

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

- **Assumption:** ... **Justification:** ...

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: knowledge
- Description:
- Links:
