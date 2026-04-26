---
title: "Access control amplification under agentic operations: whether existing frameworks address the worst-case permission inheritance problem"
added: 2026-04-26
status: backlog
priority: high
blocks: [2026-04-26-agentic-ai-foundational-conditions-dependency-ordering]
tags: [access-control, agentic-ai, amplification, nist, apra-cps-230, dora, least-privilege, zero-trust, regulated-banking]
started: ~
completed: ~
output: [knowledge]
---

# Access control amplification under agentic operations: whether existing frameworks address the worst-case permission inheritance problem

## Research Question

Agents do not inherit a user's typical behaviour — they inherit the worst-case interpretation of that user's full permission set, because they operate without fatigue, attention limits, or working hours. An environment with incomplete least-privilege implementation therefore presents a materially different risk profile under agentic operation than under human operation. Do any existing frameworks — National Institute of Standards and Technology (NIST) Special Publication (SP) 800-207 Zero Trust Architecture (ZTA), NIST SP 800-53, Australian Prudential Regulation Authority (APRA) CPS 230, or the European Union (EU) Digital Operational Resilience Act (DORA) — explicitly address this amplification mechanism, or must the argument be constructed from first principles?

## Scope

**In scope:**
- The specific mechanism by which agents operating continuously without fatigue, attention limits, or working hours inherit the worst-case interpretation of a user's full permission set rather than the user's typical-use subset
- Whether NIST SP 800-207, NIST SP 800-53, APRA CPS 230, and DORA contain explicit provisions addressing this amplification mechanism — not merely general access control or least-privilege requirements, but language that specifically contemplates non-human automated principals operating at machine speed
- Whether the argument can be made from first principles using operational risk or systems safety literature if no framework explicitly addresses it
- The blast radius differential between human and agentic operation under identical permission sets
- Whether any published technical guidance (e.g., NIST AI Risk Management Framework (RMF), vendor security documentation) addresses the specific problem of agent credential scoping
- Relationship to the least-privilege principle and the principle of minimal footprint in agentic systems

**Out of scope:**
- General least-privilege architecture design (covered by NIST SP 800-207 and SP 800-53 directly)
- The RAG-specific access control problem (covered by the companion RAG item)
- The policy coherence problem (covered by the companion policy coherence item)
- The regulatory control-failure characterisation (covered by the completed regulatory preconditions item)

**Constraints:**
- Distinguish between frameworks that explicitly name the amplification mechanism versus frameworks from which the argument must be inferred
- Evidence claims about what frameworks say must reference the actual framework text or official summary, not secondary commentary
- The NZ Crown-owned bank context (Microsoft 365, Copilot Studio, AWS Bedrock) should inform the assessment of which frameworks are most applicable

## Context

The completed regulatory preconditions item ([Regulatory and standards preconditions for deployment of agentic AI systems](https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html)) established that incomplete least-privilege access constitutes a current or foreseeable control failure under APRA CPS 230, DORA, NIST SP 800-207, and ISO 31000, and inferred from NIST SP 800-207 that "agentic credential delegation across an environment that still lacks granular least privilege is a current architectural control failure under zero trust principles." However, that item did not specifically address whether any framework explicitly names the amplification mechanism — the fact that agents operating continuously at machine speed without human-speed friction represent a categorically different risk profile even under identical permission sets. This item closes that gap.

## Approach

1. **Framework text analysis for explicit amplification language:** For each of NIST SP 800-207, NIST SP 800-53, APRA CPS 230, and DORA, search for provisions that explicitly address non-human automated principals, continuous operation without human-speed rate limiting, or the specific risk that automated systems operating on behalf of users present a different blast-radius profile than those same users operating manually.
2. **NIST AI RMF and supplementary guidance:** Check whether NIST AI RMF 1.0, NIST AI RMF Playbook, or NIST guidance on agentic AI addresses the amplification mechanism explicitly.
3. **Operational risk and systems safety literature:** If no framework explicitly addresses the amplification mechanism, construct the argument from the operational risk literature on automation, the speed-of-consequence literature, and systems safety literature on automation failure modes.
4. **Vendor security guidance survey:** Check whether Microsoft Copilot Studio, AWS Bedrock, and comparable vendor security documentation explicitly addresses the amplification problem and recommends specific mitigations (e.g., agent-specific service principals, reduced permission scopes, time-bounded credentials).
5. **Synthesis:** Produce a clear assessment of (a) whether the amplification argument is first-principles or framework-explicit for each named framework, (b) which evidence is strongest for a board risk committee versus a technical architecture audience, and (c) what the minimum control requirements are to address the amplification problem before agentic deployment.

## Sources

- [ ] [NIST SP 800-207 — Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) — primary source for zero trust; assess for explicit language on non-human principals operating at machine speed
- [ ] [NIST SP 800-53 Rev. 5 — Security and Privacy Controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) — control catalog; assess AC family controls for language on automated versus human principals
- [ ] [APRA CPS 230 — Operational Risk Management](https://handbook.apra.gov.au/standard/cps-230) — assess for technology risk and automated system language
- [ ] [DORA — Regulation (EU) 2022/2554](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554) — assess for ICT risk management provisions covering automated systems
- [ ] [NIST AI RMF 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) — assess for explicit coverage of agentic amplification and agent credential scoping
- [ ] [AWS Security blog — four security principles for agentic AI systems](https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/) — primary vendor source on agent permission scope and the minimal footprint principle; assess for explicit treatment of the amplification mechanism
- [ ] [Microsoft Copilot Studio — security and governance documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance) — assess for explicit guidance on agent credential scoping and least-privilege

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
