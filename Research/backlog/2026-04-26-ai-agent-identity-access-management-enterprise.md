---
title: "What identity and access management model is required for Artificial Intelligence (AI) agents and low-code artefacts operating within enterprise systems?"
added: 2026-04-26T10:11:11+00:00
status: backlog
priority: high
blocks: [2026-04-26-ai-lowcode-governance-enforcement-architecture, 2026-04-26-ai-lowcode-observability-telemetry-governance, 2026-04-26-ai-agent-control-plane-architecture-enterprise]
tags: [identity, access-management, machine-identity, ai-agents, low-code, credential-management, enterprise-iam, delegation, attribution]
started: ~
completed: ~
output: [knowledge]
---

# What identity and access management model is required for Artificial Intelligence (AI) agents and low-code artefacts operating within enterprise systems?

## Research Question

What identity and access management (IAM) model is required for non-human actors — AI agents and low-code artefacts — operating within enterprise systems, specifically: how should machine identities be assigned and managed; what delegation models (user-initiated vs autonomous execution) are appropriate; how should permission inheritance, credential management, and end-to-end attribution of actions across users, agents, and downstream systems be handled?

## Scope

**In scope:**
- Machine identity standards applicable to AI agents and low-code automation artefacts (workload identity, service accounts, managed identities)
- Delegation models: user-initiated delegation (agent acts on behalf of user), system-level delegation (agent acts autonomously within a defined permission scope), and the conditions under which each is appropriate
- Permission inheritance: how an agent or low-code artefact should inherit, constrain, or exceed the permissions of the initiating user or system context
- Credential management: lifecycle management of credentials held by non-human actors (rotation, revocation, scope limitation, secret management)
- End-to-end attribution: how actions taken by agents or artefacts can be attributed to the initiating user, the artefact, and any intermediate systems for audit and accountability purposes
- Applicability to major enterprise identity platforms (Microsoft Entra ID, AWS Identity and Access Management (IAM), Google Cloud Identity)
- Relevant standards (OAuth 2.0 token delegation, OpenID Connect, SPIFFE/SPIRE workload identity, NIST SP 800-63)

**Out of scope:**
- General enterprise IAM architecture for human users
- The enforcement mechanisms that consume identity (covered by Q3)
- Observability of identity-attributed actions (covered by Q4)
- Vendor-specific limitations on machine identity (covered by Q11)

**Constraints:**
- Must address the distinction between identity (who an actor is) and authorisation (what it may do)
- Must be grounded in existing standards rather than proposing novel identity architectures
- Sources must be assessable for applicability to a regulated enterprise with existing identity infrastructure

## Context

Enterprise AI and low-code systems introduce non-human actors that perform consequential actions — reading data, calling APIs, writing records, executing workflows — but existing IAM models were designed for human users. Without a defined machine identity model, agents operate under shared service accounts (preventing attribution), over-privileged system accounts (violating least privilege), or borrowed user credentials (creating accountability gaps when users leave). Addressing this gap is a prerequisite for governance enforcement (Q3), observability (Q4), and the control-plane architecture (Q16), because enforcement requires knowing *who* is acting, observability requires attributing *what was done to whom*, and the control-plane requires a coherent identity substrate across all actors.

Cross-references:
- Q3: `2026-04-26-ai-lowcode-governance-enforcement-architecture`
- Q4: `2026-04-26-ai-lowcode-observability-telemetry-governance`
- Q1: `2026-04-26-ai-lowcode-decision-rights-accountability-liability`
- Q16: `2026-04-26-ai-agent-control-plane-architecture-enterprise`

## Approach

1. **Survey machine identity standards:** Review NIST SP 800-63, OAuth 2.0 Token Exchange (RFC 8693), SPIFFE/SPIRE workload identity, and Microsoft Entra workload identities for their applicability to AI agent and low-code artefact identity.
2. **Delegation model analysis:** Characterise user-initiated delegation (agent acts within user's permission scope via token exchange) vs autonomous execution (agent operates under its own identity and permission scope) — assess when each model is appropriate, what risks each introduces, and how each should be authorised.
3. **Permission inheritance and least privilege:** Assess how permission scoping should work for agents (should an agent be able to do everything the delegating user can, or only a defined subset?) and what mechanisms enforce least-privilege for non-human actors.
4. **Credential lifecycle:** Review credential management best practices for non-human actors — rotation frequency, revocation mechanisms, secret store integration (Azure Key Vault, AWS Secrets Manager, HashiCorp Vault), and the risks of long-lived credentials held by autonomous agents.
5. **Attribution chain:** Assess how a full attribution chain can be maintained from the initiating user through the agent to downstream systems — what identity claims need to propagate, and at what points the chain is typically broken in practice.
6. **Enterprise platform assessment:** Assess how Microsoft Entra ID (managed identities, workload identity federation), AWS IAM (roles for service accounts, IAM Roles Anywhere), and Google Cloud Identity handle machine identity for AI workloads.
7. **Synthesis:** Produce a machine identity and delegation model suitable for enterprise AI governance, with explicit decision criteria for when each pattern applies.

## Sources

- [ ] [NIST SP 800-63 Digital Identity Guidelines](https://pages.nist.gov/800-63-3/) — foundational identity assurance framework; assess for applicability to non-human actors
- [ ] [RFC 8693 — OAuth 2.0 Token Exchange](https://www.rfc-editor.org/rfc/rfc8693) — standard for user-to-agent delegation via token exchange; primary standard for user-initiated delegation model
- [ ] [SPIFFE/SPIRE — workload identity framework](https://spiffe.io/) — open standard for workload identity in distributed systems; assess for applicability to AI agent identity
- [ ] [Microsoft Entra workload identities](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview) — Microsoft's enterprise model for non-human actor identity; primary enterprise reference
- [ ] [AWS IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) — AWS model for workload identity outside AWS; assess for multi-cloud agent scenarios
- [ ] [NIST SP 800-207 — Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) — zero trust principles applicable to identity-first access models for non-human actors

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
