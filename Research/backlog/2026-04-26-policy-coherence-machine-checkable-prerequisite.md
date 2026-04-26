---
title: "Policy coherence as a machine-checkable prerequisite: policy-as-code, formal specification, and invariant registries for regulated financial institutions deploying agentic Artificial Intelligence (AI)"
added: 2026-04-26
status: backlog
priority: high
blocks: [2026-04-26-agentic-ai-foundational-conditions-dependency-ordering]
tags: [policy-coherence, policy-as-code, open-policy-agent, formal-specification, invariant-registry, agentic-ai, regulated-banking, governance, automated-enforcement]
started: ~
completed: ~
output: [knowledge]
---

# Policy coherence as a machine-checkable prerequisite: policy-as-code, formal specification, and invariant registries for regulated financial institutions deploying agentic Artificial Intelligence (AI)

## Research Question

Contradictory or outdated policy documents are a chronic governance failure that organisations tolerate because the consequences under human operation are slow-moving. Under agentic operation, agents built in good faith against one policy document will violate another, and will do so repeatedly at machine speed before detection. What does the literature say about policy coherence as a prerequisite for automated enforcement, and does the policy-as-code literature — formal policy specification, Open Policy Agent (OPA) patterns, invariant registries — provide an applicable framework for ensuring agents operate within a coherent, non-contradictory policy space in a regulated financial institution?

## Scope

**In scope:**
- The mechanism by which contradictory or outdated policy documents become a machine-speed failure mode under agentic AI, rather than a slow-moving governance issue under human operation
- The governance literature on policy coherence and policy conflict as an organisational failure mode — what the academic and practitioner literature says about the frequency, causes, and consequences of policy contradiction in large organisations
- The policy-as-code literature: formal policy specification approaches, OPA (Open Policy Agent) and Rego patterns, declarative policy languages, constraint satisfaction frameworks
- Whether invariant registries — explicit registries of non-negotiable policy rules that must hold across all agents and automated systems — provide a workable pattern for regulated financial institutions
- Evidence on whether any organisation has successfully implemented policy-as-code at scale in a regulated environment, and what the preconditions and failure modes were
- Relationship between policy coherence and the information architecture layer: whether unclassified data estates make policy coherence assessment impossible or merely harder
- Whether any regulatory framework (APRA CPS 230, DORA, ISO 42001, FCA/PRA guidance) explicitly requires machine-checkable policy coherence as a precondition for agentic AI deployment

**Out of scope:**
- General policy management and governance frameworks not specifically related to automated enforcement
- The deployment pipeline enforcement mechanism (covered by the companion deployment pipeline item)
- The RAG access control layer (covered by the companion RAG item)
- Technical implementation details of OPA or specific policy engines beyond what is needed to assess applicability

**Constraints:**
- Distinguish between what the policy-as-code literature says is achievable in principle versus what has been demonstrated in production in regulated environments
- The primary question is applicability to a regulated financial institution, not general software engineering context
- Assess whether policy-as-code approaches require a minimum level of policy clarity and classification before they can be applied — i.e., whether policy coherence is a prerequisite for policy-as-code rather than a consequence of it

## Context

The completed regulatory preconditions item ([Regulatory and standards preconditions for deployment of agentic AI systems](https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html)) established that deploying agentic AI into an environment with incomplete governance constitutes a control failure under multiple frameworks. The completed business-led low-code governance item ([Business-led low-code agent governance: conditions for durable value versus fragmentation in regulated environments](https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html)) established that governed knowledge, bounded use-case routing, and enforceable platform guardrails are preconditions for durable value.

This item addresses a specific gap: even if an organisation commits to applying its policies to agentic AI, the operational consequence of doing so against a contradictory or stale policy set is that agents will predictably violate policies at machine speed. The research question is whether the policy-as-code literature provides a workable path to making policy coherence a machine-checkable property rather than a periodic manual audit finding.

## Approach

1. **Policy coherence as an organisational problem:** Review the organisational behaviour, compliance, and governance literature for evidence on how frequently large regulated organisations operate with contradictory policy documents, what the consequences are under human operation, and whether any framework requires proactive policy conflict detection.
2. **Policy-as-code survey:** Review the technical literature on formal policy specification — OPA and Rego, Cedar Policy Language, AWS IAM policy conditions, Kubernetes admission controllers, and comparable approaches — for evidence of applicability at enterprise scale and in regulated contexts.
3. **Invariant registries:** Assess whether the concept of an invariant registry — an explicit, maintained set of non-negotiable policy rules that all automated systems must satisfy — has been implemented in practice, what the governance model looks like, and what the failure modes are.
4. **Regulatory requirement check:** For APRA CPS 230, DORA, ISO 42001, and FCA/PRA guidance, assess whether any provision explicitly requires machine-checkable policy coherence or policy-as-code as a precondition for agentic AI deployment.
5. **Precondition analysis:** Assess whether policy-as-code approaches require a minimum level of policy clarity and information classification before they can be applied — and whether the typical large-organisation policy estate (contradictory, stale, unclassified) makes the approach inapplicable without prior remediation.
6. **Evidence of production implementations:** Search for case studies or published accounts of policy-as-code implementations in regulated financial services environments — banking, insurance, or comparable — with measured outcomes.
7. **Synthesis:** Produce a decision framework characterising when policy-as-code is applicable, what the minimum preconditions are, and what the gap is between the policy-as-code literature's capability claims and the practical state of a typical large financial institution's policy estate.

## Sources

- [ ] [Open Policy Agent (OPA) documentation](https://www.openpolicyagent.org/docs/latest/) — primary source for OPA and Rego policy language; assess for enterprise scale, regulated context, and integration patterns
- [ ] [AWS Cedar policy language](https://www.cedarpolicy.com/en) — assess as an alternative formal policy specification approach with verification properties
- [ ] [NIST SP 800-53 Rev. 5 — Policy and procedures controls (PM family)](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) — assess for provisions on policy consistency and policy management as a control requirement
- [ ] [APRA CPS 230 — Operational Risk Management](https://handbook.apra.gov.au/standard/cps-230) — assess for requirements on policy documentation, consistency, and governance
- [ ] [DORA — Regulation (EU) 2022/2554](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554) — assess for ICT risk management requirements on policy documentation and automated enforcement
- [ ] [ISO/IEC 42001 — AI Management System](https://www.iso.org/standard/81230.html) — assess for policy coherence requirements specific to AI management systems
- [ ] https://dl.acm.org/doi/10.1145/3194133.3194139 — policy conflict detection in information systems; assess for evidence on the frequency and mechanism of policy conflicts in large organisations
- [ ] [Styra DAS (Declarative Authorization Service) enterprise OPA case studies](https://www.styra.com/case-studies/) — assess for evidence of OPA deployment at financial services scale

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
