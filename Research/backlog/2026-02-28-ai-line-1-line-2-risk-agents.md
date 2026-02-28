---
title: "AI Line 1 and Line 2 Risk Agents: Who Is Building Them?"
added: 2026-02-28
status: backlog
priority: high
tags: [ai-strategy, risk-agents, line-1, line-2, three-lines-model, agentic-ai, financial-services, risk-management]
started: ~
completed: ~
output: [knowledge]
---

# AI Line 1 and Line 2 Risk Agents: Who Is Building Them?

## Research Question

Who is currently building or deploying AI agents specifically positioned to operate within the three lines of defence model — line 1 (business/operational risk management) and line 2 (risk and compliance oversight) — and what are the architecture, governance, and accountability patterns for these agents?

## Scope

**In scope:**
- Line 1 agents: AI systems embedded in business units that perform real-time risk identification, monitoring, or escalation as part of operational risk management (e.g. transaction monitoring agents, trading desk risk alerts, operational incident triage)
- Line 2 agents: AI systems operated by risk and compliance functions that conduct independent oversight, challenge, or monitoring of line 1 activities (e.g. AI-powered compliance surveillance, model risk monitoring agents, regulatory change management agents)
- Governance architecture: how accountability, human oversight, and escalation are structured when an agent is performing a risk oversight function
- Vendor and in-house builds: both commercial platforms and known bespoke builds at major financial institutions
- Regulatory acceptability: whether regulators have taken a position on AI agents performing second-line oversight functions

**Out of scope:**
- Line 3 (internal audit) agents — covered by `ai-control-testing-and-assurance.md`
- General AI risk management tools not structured within the three-lines model
- Credit, fraud, and AML models not operating as agentic oversight functions

**Constraints:** Focus on financial services (banks, insurers, asset managers). Prefer disclosed deployments or credible analyst-documented cases over vendor claims.

## Context

The AI strategy research item (completed 2026-02-28) identified four use-case types. Line 1 and line 2 risk agents sit at the boundary of Type 3 (delegated authority agents) and Type 4 (fully agentic business units). The three lines of defence model is a regulatory expectation for RBNZ-supervised entities (embedded in BS11 governance principles and APRA CPS 220 equivalents).

A critical unresolved question from the AI strategy research: when an AI agent performs a line 2 oversight function — challenging line 1 risk decisions, flagging breaches, or producing compliance determinations — who is accountable for that determination? The agent cannot be held accountable. The traditional answer (the risk officer who "reviews" the output) may not hold if the agent is operating faster or at a scale where human review is nominal rather than substantive.

This is the governance problem at the heart of deploying Type 3 risk agents, and it is not resolved by existing prudential guidance. Understanding who is building these agents and how they are solving (or deferring) the accountability question is essential for designing a compliant agentic risk architecture.

## Approach

1. **Landscape scan** — identify financial institutions or vendors known to be operating or building line 1 or line 2 risk agents. Sources: industry publications (Risk.net, FS Tech, Celent reports), conference disclosures (RiskMinds, OpRisk Global), regulatory speeches.
2. **Architecture patterns** — for each identified case, document: what the agent does, which line it sits in, how human oversight is structured, what the escalation trigger is.
3. **Accountability model analysis** — how is accountability for agent outputs structured? Is there a named human reviewer? Is the agent's output treated as a tool output (human decides) or a determination (agent decides, human audits)?
4. **Regulatory position** — have RBNZ, APRA, FCA, PRA, or Fed/OCC published any guidance specifically addressing AI agents in risk oversight functions? What is the current supervisory expectation?
5. **Failure modes** — identify any disclosed incidents where a line 1 or line 2 AI agent produced an incorrect output that resulted in a risk management failure. What went wrong and how was it caught?

## Sources

- [ ] Risk.net: AI in risk management coverage 2023–2025
- [ ] Celent / Oliver Wyman: AI in risk management research reports
- [ ] Bank for International Settlements (BIS): "AI in financial risk management" (2024)
- [ ] FCA / PRA: AI in financial services discussion papers (DP5/22, DP3/22, 2024 follow-ups)
- [ ] APRA CPG 234 / CPS 220: operational and model risk governance expectations
- [ ] RBNZ: BS11 governance, BS2A capital adequacy — any AI-specific interpretive material
- [ ] Major bank disclosures: ANZ Group, JPMorgan Chase, HSBC, ING Group — known AI risk management disclosures
- [ ] IIF (Institute of International Finance): AI governance in banking 2024
- [ ] Vendor documentation: Behavox, NICE Actimize, Nasdaq Surveillance, Bloomberg Compliance, OpenPages (IBM)
- [ ] RiskMinds / OpRisk Global 2024 conference proceedings and published talks

---

## Findings

*(Fill in when completing.)*

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

- Type: knowledge
- Description:
- Links:
