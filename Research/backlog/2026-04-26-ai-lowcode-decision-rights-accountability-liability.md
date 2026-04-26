---
title: "How should decision rights, accountability, and liability be structured for Artificial Intelligence (AI) systems and low-code applications in enterprise environments?"
added: 2026-04-26T10:11:11+00:00
status: backlog
priority: high
blocks: [2026-04-26-human-in-the-loop-ai-automated-workflows, 2026-04-26-ai-agent-control-plane-architecture-enterprise, 2026-04-26-ai-lowcode-governance-maturity-model]
tags: [decision-rights, accountability, liability, raci, governance, ai-systems, low-code, enterprise-governance, operational-risk, escalation]
started: ~
completed: ~
output: [knowledge]
---

# How should decision rights, accountability, and liability be structured for Artificial Intelligence (AI) systems and low-code applications in enterprise environments?

## Research Question

How should decision rights, accountability, and liability be structured for AI systems and low-code applications in enterprise environments — specifically, who should be empowered to approve new use cases, who owns system behaviour in production, how should formal Responsible-Accountable-Consulted-Informed (RACI) structures and escalation paths be defined, what separation of duties is required, and how should legal and operational liability boundaries be delineated across business, technology, and risk functions?

## Scope

**In scope:**
- Decision rights design: who can approve a new AI or low-code use case (self-service, delegated authority, or committee approval), under what conditions each approval model applies, and what approval criteria are required
- Production accountability: who owns the behaviour of an AI or low-code system after deployment — business owner, technology owner, or shared accountability — and what ownership means operationally (monitoring obligation, incident response, remediation authority)
- RACI frameworks adapted for AI and low-code governance: how standard RACI models need to be modified to address the non-deterministic and continuously changing nature of AI system behaviour
- Escalation paths: what triggers escalation, who receives it, and what the expected response time and authority at each escalation level is
- Separation of duties: what activities must be performed by different people or teams (e.g. the team that builds an AI system should not be the same team that approves its deployment)
- Liability: how operational and legal liability for AI-driven decisions is allocated when the decision crosses organisational boundaries or produces harm — in the context of applicable legal frameworks (EU AI Act liability provisions, national product liability law)

**Out of scope:**
- Technical enforcement mechanisms for accountability (covered by Q3/Q16)
- Observability tools that enable accountability tracing (covered by Q4)
- Regulatory compliance mapping (covered by Q15)
- Per-use-case risk assessment (covered by Q5)

**Constraints:**
- Must produce structures that are operable by business and risk professionals, not just technology teams
- Must be grounded in the regulatory context established in Q15 (EU AI Act, APRA CPS 230, DORA)
- Findings must address the practical challenge of accountability for systems whose behaviour changes over time without explicit change events

## Context

The absence of clear decision rights and accountability structures is the root cause of ungoverned AI and low-code proliferation in enterprise environments. Without a defined approval model, use cases are deployed by whoever has access to the tools. Without clear production ownership, no one monitors or takes responsibility for system behaviour. Without separation of duties, the team building a system is also the team approving its risks. This item provides the accountability architecture that the human-in-the-loop design (Q9) and the control-plane architecture (Q16) require to function — both depend on knowing who has authority to approve, override, or halt automated system behaviour.

This item requires Q5 (risk tier classification) and Q15 (regulatory obligations) as inputs, because the appropriate accountability structure varies by risk tier and must satisfy specific regulatory obligations for high-risk AI systems.

Cross-references:
- Q5: `2026-04-26-ai-lowcode-risk-tier-classification-controls` (prerequisite)
- Q15: `2026-04-26-ai-lowcode-regulatory-compliance-alignment` (prerequisite)
- Q9: `2026-04-26-human-in-the-loop-ai-automated-workflows`
- Q16: `2026-04-26-ai-agent-control-plane-architecture-enterprise`
- Q8: `2026-04-26-ai-governance-cost-performance-delivery-impact`

## Approach

1. **RACI model adaptation:** Review standard IT governance RACI models and assess how they must be modified for AI and low-code systems — specifically, how to handle: non-deterministic system outputs, accountability for systems that change behaviour after deployment, and accountability for outputs of systems built by third-party vendors or platforms.
2. **Approval model design:** Analyse the design space for use case approval: self-service (no approval required below a risk threshold), delegated approval (business unit authority for defined risk classes), and committee approval (for high-risk or cross-boundary use cases). Identify precedents from regulated technology governance (e.g. model risk management in financial services, change management in ITIL).
3. **Production ownership definition:** Define what production ownership means for AI and low-code systems — what obligations it creates (monitoring, incident response, performance review, decommissioning), and how ownership transfers when personnel change.
4. **Separation of duties:** Define which activities must be separated (design, build, approve, deploy, monitor, audit) and what the minimum team structure is to achieve effective separation.
5. **Liability analysis:** Review EU AI Act liability provisions (the AI Liability Directive), national product liability law, and APRA CPS 230 accountability requirements to characterise how legal liability for AI-driven decisions is currently allocated.
6. **Escalation path design:** Propose an escalation path model: trigger conditions, escalation levels, expected response times, and who has authority at each level.
7. **Synthesis:** Produce a governance accountability structure — RACI matrix, approval matrix, and escalation path — suitable for adoption as an enterprise governance artefact.

## Sources

- [ ] [EU AI Act — Regulation (EU) 2024/1689 — Chapter 3 (obligations for high-risk AI systems)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689) — primary source for accountability and liability obligations under EU law
- [ ] [EU AI Liability Directive — Proposal COM(2022)496](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A52022PC0496) — liability allocation for AI-related harm; assess for enterprise accountability implications
- [ ] [APRA CPS 230 — Operational Risk Management](https://handbook.apra.gov.au/standard/cps-230) — Australian prudential accountability requirements; assess for ownership and escalation obligations
- [ ] [SR 11-7 — Guidance on Model Risk Management (US Federal Reserve)](https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm) — model risk management governance; assess for RACI and approval model precedents applicable to AI systems
- [ ] [NIST AI RMF 1.0 — GOVERN function](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) — governance structure guidance for AI systems; assess for accountability and decision rights recommendations
- [ ] [COBIT 2019 — IT governance and management framework](https://www.isaca.org/resources/cobit) — enterprise IT governance RACI models; assess for adaptability to AI and low-code governance

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
