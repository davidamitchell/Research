---
title: "Updating the enterprise Artificial Intelligence ecosystem capability reference architecture using second-cycle 2026-05 completed items"
added: 2026-05-08T09:16:11+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []
tags: [agentic-ai, enterprise, capability-model, ai-governance, security, supply-chain, sbom, evaluation, reference-architecture, regulation]
started: ~
completed: ~
output: [knowledge]
cites:
  - 2026-05-06-ai-capability-reference-architecture-security-supply-chain-update
  - 2026-05-06-aibom-declared-construction-practice
  - 2026-05-06-aibom-effectiveness-risk-mitigation-limits
  - 2026-05-06-aibom-identity-attribution-multiagent-practice
  - 2026-05-06-aibom-platform-observability-control-comparison
  - 2026-05-06-aibom-regulatory-eu-ai-act-intersection
  - 2026-05-06-aibom-runtime-capture-opentelemetry-practice
  - 2026-05-07-ai-production-incidents-deep-dive
  - 2026-05-07-ai-regulatory-guidance-update-gap-check
  - 2026-05-07-five-eyes-ai-risks-and-advice
  - 2026-05-06-gpt-oss-safeguard-policy-enforcement-open-weight
  - 2026-05-06-it-system-legibility-measurement-frameworks
related:
  - 2026-04-22-enterprise-ai-capability-model
  - 2026-05-05-enterprise-ai-capability-stack
superseded_by: ~
supersedes: ~
item_type: synthesis
confidence: medium
versions: []
---

# Updating the enterprise Artificial Intelligence ecosystem capability reference architecture using second-cycle 2026-05 completed items

## Research Question

How should the enterprise Artificial Intelligence (AI) ecosystem capability reference architecture (as expressed in `2026-04-22-enterprise-ai-capability-model`, `2026-05-05-enterprise-ai-capability-stack`, and `2026-05-06-ai-capability-reference-architecture-security-supply-chain-update`) be revised and extended to incorporate findings from the second-cycle 2026-05 completed items — covering AI Bill of Materials (AIBOM) declared construction practices, effectiveness and risk-mitigation limits, multi-agent identity attribution, platform observability controls, EU AI Act regulatory intersection, and OpenTelemetry-based runtime capture; AI production incidents; regulatory guidance updates; Five Eyes AI risk posture; open-weight model safeguard policies; and Information Technology (IT) legibility and measurement frameworks — that were not incorporated in the first-cycle update?

## Scope

**In scope:**
- Gap analysis: which capability domains in the first-cycle updated architecture are absent or underspecified relative to the second-cycle completed items listed in `cites`
- AIBOM operational practice integration: how AIBOM declared construction practices, effectiveness and risk limits, multi-agent identity attribution, platform observability comparison, EU AI Act intersection, and OpenTelemetry (OTel) runtime capture translate to refined or new capability components in the architecture
- Production incident mapping: how failure modes and operational controls documented in `2026-05-07-ai-production-incidents-deep-dive` map to existing or missing capability layers; whether the architecture adequately anticipates the failure classes observed
- Regulatory guidance currency: what capability requirements arise from the regulatory guidance delta (`2026-05-07-ai-regulatory-guidance-update-gap-check`) that are absent from the current architecture, particularly for financial-services regulators (Australian Prudential Regulation Authority (APRA), Reserve Bank of New Zealand (RBNZ), Financial Markets Authority (FMA), Office of the Superintendent of Financial Institutions (OSFI))
- Five Eyes security integration: how the Five Eyes AI risk posture (`2026-05-07-five-eyes-ai-risks-and-advice`) translates to architectural control requirements not covered by the first-cycle security threat model
- Open-weight model safeguard capabilities: where open-weight model safeguard and policy-enforcement approaches (`2026-05-06-gpt-oss-safeguard-policy-enforcement-open-weight`) belong in the architecture
- IT legibility and measurement: how IT legibility and measurement frameworks (`2026-05-06-it-system-legibility-measurement-frameworks`) inform the observability and evidence-collection layers
- Reconciliation of overlaps and conflicts across the second-cycle items before finalising architectural recommendations
- Updated capability ownership recommendations and a revised component list (additions, amendments, and explicit supersessions of first-cycle components)

**Out of scope:**
- Items already incorporated in the first-cycle update (`2026-05-06-ai-capability-reference-architecture-security-supply-chain-update`)
- Implementation guidance for specific vendor products
- Original primary research into any of the cited source domains (rely on already-completed items)
- Revision of the underlying five-layer baseline model structure (unless the second-cycle items give specific grounds to do so)

**Constraints:**
- Must cite only completed research items; no speculative claims about items still in backlog or in-progress
- Must produce a revised architecture component list that is directly traceable to evidence in the cited items
- Must use the same structural conventions as `2026-05-06-ai-capability-reference-architecture-security-supply-chain-update` to enable comparison

## Context

The first-cycle architecture update (`2026-05-06-ai-capability-reference-architecture-security-supply-chain-update`, completed 2026-05-07) integrated the foundational AIBOM conceptual and schema items, the AI security threat model, governance assurance, and evaluation standards into the enterprise reference architecture. Since then, a further twelve items have been completed that either extend those domains with operational practice detail (six additional AIBOM items), introduce entirely new evidence streams (AI production incidents, Five Eyes risk posture, regulatory guidance delta, open-weight safeguards, IT legibility frameworks), or expose failure modes that the current architecture may not anticipate. Without this second-cycle update the architecture understates the operational and regulatory burden on enterprise teams responsible for SBOM/AIBOM, security operations, and compliance.

## Approach

1. **AIBOM operational gap analysis** — For each of the six second-cycle AIBOM items (declared construction, effectiveness limits, multi-agent attribution, platform observability, EU AI Act intersection, OpenTelemetry runtime capture), identify what capability is implied that is absent from or only partially present in the first-cycle architecture. Produce a gap table.
2. **Production incident layer review** — Map the failure modes and control categories from `2026-05-07-ai-production-incidents-deep-dive` onto the current architecture layers. Determine whether existing capability domains cover the required controls or whether new domains are needed.
3. **Regulatory capability requirements** — Extract capability-level requirements from `2026-05-07-ai-regulatory-guidance-update-gap-check` and evaluate coverage in the current architecture. Focus on financial-services-specific obligations not addressed in the first cycle.
4. **Five Eyes security posture mapping** — Translate the AI risk and advisory posture from `2026-05-07-five-eyes-ai-risks-and-advice` into architectural control surfaces. Identify gaps relative to the existing security capability domains.
5. **Open-weight model safeguard placement** — Determine the correct architectural home for open-weight model safeguard policies and policy-enforcement gates (`2026-05-06-gpt-oss-safeguard-policy-enforcement-open-weight`).
6. **Legibility and measurement layer** — Evaluate whether the observability and evidence-collection layers sufficiently reflect IT legibility frameworks (`2026-05-06-it-system-legibility-measurement-frameworks`). Propose additions where coverage is lacking.
7. **Cross-item reconciliation** — Identify overlaps or conflicts among the second-cycle items (e.g., AIBOM runtime capture vs. production-incident telemetry requirements) and state explicitly how they are resolved in the revised architecture.
8. **Revised architecture output** — Produce an updated capability component list and ownership table that incorporates findings from steps 1–7, explicitly noting which first-cycle components are amended and which new components are added.

## Sources

- [ ] [Mitchell (2026) Integrating 2026-05 security and supply chain findings into the enterprise AI capability reference architecture](https://davidamitchell.github.io/Research/research/2026-05-06-ai-capability-reference-architecture-security-supply-chain-update.html) — first-cycle update; establishes baseline for second-cycle gap analysis
- [ ] [Mitchell (2026) AIBOM declared construction practice](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-declared-construction-practice.html) — operational practice for constructing declared AIBOM artifacts
- [ ] [Mitchell (2026) AIBOM effectiveness and risk-mitigation limits](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-effectiveness-risk-mitigation-limits.html) — where AIBOM controls are and are not effective
- [ ] [Mitchell (2026) AIBOM identity attribution in multi-agent systems: practice](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html) — multi-agent identity attribution practices and architectural implications
- [ ] [Mitchell (2026) AIBOM platform observability and control comparison](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html) — comparative view of platform observability controls for AIBOM
- [ ] [Mitchell (2026) AIBOM and EU AI Act regulatory intersection](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-regulatory-eu-ai-act-intersection.html) — compliance obligations and intersection between AIBOM and EU AI Act
- [ ] [Mitchell (2026) AIBOM runtime capture via OpenTelemetry: practice](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-capture-opentelemetry-practice.html) — runtime AIBOM generation using OpenTelemetry instrumentation
- [ ] [Mitchell (2026) Production incidents linked to AI systems](https://davidamitchell.github.io/Research/research/2026-05-07-ai-production-incidents-deep-dive.html) — documented AI production incident failure modes and mitigations
- [ ] [Mitchell (2026) AI regulatory guidance delta check](https://davidamitchell.github.io/Research/research/2026-05-07-ai-regulatory-guidance-update-gap-check.html) — new regulatory guidance and coverage gaps since prior review
- [ ] [Mitchell (2026) Five Eyes stance on AI risk and policy advice](https://davidamitchell.github.io/Research/research/2026-05-07-five-eyes-ai-risks-and-advice.html) — Five Eyes AI risk posture and architectural security implications
- [ ] [Mitchell (2026) Open-weight model safeguard policy enforcement](https://davidamitchell.github.io/Research/research/2026-05-06-gpt-oss-safeguard-policy-enforcement-open-weight.html) — safeguard and policy enforcement for open-weight models
- [ ] [Mitchell (2026) IT system legibility and measurement frameworks](https://davidamitchell.github.io/Research/research/2026-05-06-it-system-legibility-measurement-frameworks.html) — legibility and measurement frameworks for IT systems; informs observability layer

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

-

### §7 Recursive Review

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

### Key Findings

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | | |

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

### Open Questions

---

## Output

- Type: knowledge
- Description:
- Links:
