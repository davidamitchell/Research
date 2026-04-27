---
title: "Universal Entity Lifecycle Governance Framework (UELGF): decommission lifecycle — trigger taxonomy, procedural requirements by CIA tier, ghost entity detection and remediation, and the dependency elimination trigger as formal connection to systems capability debt"
added: 2026-04-27T01:28:25+00:00
status: backlog
priority: high
blocks: [2026-04-27-uelgf-synthesis-complete-framework]
tags: [uelgf, decommission, ghost-entity, lifecycle, systems-capability-debt, credential-revocation, dependency-elimination, archive, off-rail-detection, regulated-banking]
started: ~
completed: ~
output: [knowledge]
---

# Universal Entity Lifecycle Governance Framework (UELGF): decommission lifecycle — trigger taxonomy, procedural requirements by CIA tier, ghost entity detection and remediation, and the dependency elimination trigger as formal connection to systems capability debt

## Research Question

How should the UELGF formally specify the decommission lifecycle — including a complete trigger taxonomy, procedural requirements differentiated by CIA tier, a ghost entity detection and remediation mechanism, and the dependency elimination trigger as the formal connection between the UELGF and the systems capability debt remediation programme — such that decommission is a first-class lifecycle stage with the same governance rigour as any other stage?

## Scope

**In scope:**
- Formal definition of decommissioned state and the conditions that must all be satisfied before an entity is considered decommissioned (registry removal, credential revocation, action cessation confirmed, dependent notification, lifecycle archive)
- Complete decommission trigger taxonomy: scheduled sunset, owner departure, policy violation (remediation failed), CIA rating escalation, dependency elimination, explicit decision, ghost entity detection
- For each trigger type: dependent notification with defined notice periods by CIA tier; credential revocation sequence (what credentials, in what order, by what mechanism, with what confirmation); action draining (how in-flight actions are completed or cancelled safely); data disposition (what data the entity held or generated, where it goes, who is responsible); dependency graph update in the Policy Information Point (PIP); and the archive record specification
- Ghost entity detection mechanism: how the framework identifies entities operating without current registration, entities whose registered owner no longer exists, entities whose licence to operate has lapsed without formal decommission, and entities whose actual behaviour has drifted beyond their registered CIA rating
- Ghost entity remediation process for each detected state
- The dependency elimination trigger: the formal mechanism connecting the UELGF to the systems capability debt remediation programme — when a direct engineering solution closes the gap that a citizen-built entity was bridging, the UELGF must formally decommission that entity and record the connection
- Archive record specification: what is retained, in what form, for how long, under what access controls — differentiated by CIA tier and entity type

**Out of scope:**
- Foundational principles and the first-class nature of decommission as a general principle (covered by `2026-04-27-uelgf-foundational-definitions-principles`)
- Entity taxonomy and CIA classification (covered by `2026-04-27-uelgf-entity-taxonomy-cia-classification`)
- Policy architecture (covered by `2026-04-27-uelgf-policy-architecture-8-layer-context`)
- Runtime feedback loop signal processing (covered by `2026-04-27-uelgf-runtime-feedback-loop`) — though the signal that triggers decommission via the feedback loop is in scope

**Constraints:**
- All decommission procedures must be specified at sufficient precision to be automatable — they should not depend on manual steps that can be omitted
- Ghost entity detection must derive from observable system state (registry entries, credential usage logs, action logs, dependency graph state) rather than from entity owner self-declaration
- The dependency elimination trigger must produce a machine-readable record that can be consumed by the systems capability debt programme — the connection must be explicit, not inferred

## Context

Decommission is historically the most neglected lifecycle stage in enterprise software governance. Entities accumulate because decommissioning is effortful, the incentives for owners point toward retention rather than termination, and the costs of ghost entities are diffuse and often invisible until a security incident or regulatory examination makes them visible. The UELGF treats decommission as a first-class concern by embedding it in the rail from the first moment: the scaffold generated at getting started includes a decommission schedule with trigger conditions. The entity's end-of-life is visible from day one, and the conditions under which decommission is triggered are machine-evaluable.

The dependency elimination trigger is the formal connection between the UELGF and the systems capability debt remediation programme. When a direct engineering solution (an API, an integration, a data product) closes the gap that a citizen-built workaround entity was bridging, the UELGF must formally decommission that entity. This records the progress of capability debt remediation and ensures ungoverned workarounds are retired when the underlying problem is solved — rather than coexisting indefinitely with the solution that was supposed to replace them.

Prior completed research directly informs this item:
- [Systems capability debt and agentic AI operational risk](https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html) — context for dependency elimination and ghost entity risk
- [Systems capability debt citizen development empirical evidence](https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-citizen-development-empirical-evidence.html) — empirical evidence for why decommission is neglected
- [AI and low-code lifecycle management](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-lifecycle-management.html) — lifecycle management patterns for low-code and AI entities

## Approach

1. **Ghost entity prevalence and detection methods:** Survey evidence on ghost/orphan entity prevalence in enterprise environments (ServiceNow CMDB reconciliation research, AWS account hygiene studies, Microsoft Azure orphaned resource research) to establish the scale of the problem and identify the detection mechanisms that have been shown to work. Assess applicability to the UELGF context.
2. **Credential revocation sequencing:** Survey how credential revocation is handled in high-assurance systems (certificate lifecycle management in PKI, OAuth 2.0 token revocation, AWS IAM access key rotation) to produce a credible revocation sequence for the UELGF. The sequence must address the ordering problem: revoking credentials before draining in-flight actions produces different outcomes than the reverse.
3. **Action draining patterns:** Survey patterns for safe termination of in-flight operations in distributed systems (saga pattern rollback, circuit breaker drain, graceful shutdown protocols) to specify how the UELGF handles the transition from active to decommissioned without data loss or incomplete operations.
4. **Data disposition frameworks:** Survey data retention requirements in relevant regulatory frameworks (GDPR (General Data Protection Regulation) Article 5 storage limitation, APRA CPS 231, MiFID II (Markets in Financial Instruments Directive II) record-keeping) to produce the data disposition specification for each entity type and CIA tier. The specification must distinguish operational data (what the entity processed) from governance data (what the registry recorded about the entity's lifecycle).
5. **Dependency notification models:** Survey how dependency notification is handled in existing service decommission processes (AWS service deprecation notices, Kubernetes API deprecation policy, ServiceNow plugin decommission process) to produce a notification model with defined notice periods by CIA tier and dependency criticality.
6. **Archive record specification:** Survey what existing governance frameworks require to be retained after decommission (ISO/IEC 27001 record retention, financial services regulatory record-keeping requirements) and produce the UELGF archive record specification: minimum fields, retention period by CIA tier, access controls, and the format in which the record is stored in the PIP.
7. **Dependency elimination trigger formalisation:** Specify the formal structure of the dependency elimination trigger: what information is recorded (the entity being decommissioned, the capability debt item it was bridging, the engineering solution that closed the gap, the date of closure), what system records this event, and how the systems capability debt programme consumes it.

## Sources

- [ ] [Systems capability debt agentic AI risk synthesis — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html) — ghost entity risk and dependency elimination context
- [ ] [Systems capability debt citizen development empirical evidence — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-citizen-development-empirical-evidence.html) — empirical base for decommission neglect
- [ ] [AI and low-code lifecycle management — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-lifecycle-management.html) — lifecycle management patterns
- [ ] [GDPR Article 5 — Principles relating to processing of personal data](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679) — storage limitation and data disposition requirements
- [ ] [APRA CPS 231 — Outsourcing](https://www.apra.gov.au/sites/default/files/Prudential-Standard-CPS-231-Outsourcing-%28July-2017%29.pdf) — record retention for outsourced services analogue
- [ ] [RFC 7009 — OAuth 2.0 Token Revocation](https://datatracker.ietf.org/doc/html/rfc7009) — credential revocation mechanism
- [ ] [Kubernetes API deprecation policy](https://kubernetes.io/docs/reference/using-api/deprecation-policy/) — dependency notification model as analogue
- [ ] [AWS account decommission and offboarding guidance](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_close.html) — cloud entity decommission procedure as analogue
- [ ] [NIST SP 800-88 — Guidelines for Media Sanitisation](https://csrc.nist.gov/pubs/sp/800/88/r1/final) — data disposition and destruction standards
- [ ] [ISO/IEC 27001:2022 — Annex A.8 Technology controls — asset decommission](https://www.iso.org/standard/27001) — formal decommission requirements in information security management

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
