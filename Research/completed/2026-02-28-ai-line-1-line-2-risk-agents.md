---
title: "AI Line 1 and Line 2 Risk Agents: Who Is Building Them?"
added: 2026-03-03T06:16:53+00:00
status: completed
priority: high
tags: [ai-strategy, risk-agents, line-1, line-2, three-lines-model, agentic-ai, financial-services, risk-management]
started: 2026-03-03T06:16:53+00:00
completed: 2026-03-03T06:16:53+00:00
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
- [ ] Bank for International Settlements (BIS): "AI in financial risk management" (2024) — https://www.bis.org/
- [ ] FCA / PRA: AI in financial services discussion papers (DP5/22, DP3/22, 2024 follow-ups) — https://www.fca.org.uk/
- [ ] APRA CPG 234 / CPS 220: operational and model risk governance expectations — https://www.apra.gov.au/cpg-234-information-security
- [ ] RBNZ: BS11 governance, BS2A capital adequacy — any AI-specific interpretive material — https://www.rbnz.govt.nz/
- [ ] Major bank disclosures: ANZ Group, JPMorgan Chase, HSBC, ING Group — known AI risk management disclosures
- [ ] IIF (Institute of International Finance): AI governance in banking 2024 — https://www.iif.com/
- [ ] Vendor documentation: Behavox, NICE Actimize, Nasdaq Surveillance, Bloomberg Compliance, OpenPages (IBM)
- [ ] RiskMinds / OpRisk Global 2024 conference proceedings and published talks

---

## Findings

### Executive Summary

AI agents performing line 1 and line 2 risk functions in financial services are deployed today, but almost exclusively in the "tool output" mode: the agent produces flags, alerts, or recommendations, and a named human remains accountable for the determination. The dominant delivery mechanism is commercial vendor platforms (NICE Actimize SURVEIL-X, Behavox, Nasdaq Trade Surveillance, IBM OpenPages) rather than bespoke in-house builds. Regulators across all major jurisdictions — FCA/PRA, APRA, BIS, RBNZ — are applying existing frameworks (SMCR, CPS 220, three-lines model) to AI agents and have not published agent-specific guidance for line 1 or line 2 oversight functions. The core governance question — who is accountable when an AI agent performs an independent oversight function at machine speed — remains unresolved in prudential guidance, and no major regulator has addressed the nominal-review problem where human review is formally present but substantively impossible at scale.

### Key Findings

1. **Vendor platforms dominate line 2 AI agent deployment.** NICE Actimize SURVEIL-X (generative AI-augmented), Behavox (voice and communications surveillance), Nasdaq Trade Surveillance, and IBM OpenPages (model risk governance) are the primary commercial platforms deployed in second-line financial crime and compliance functions. These are production systems at scale, not pilots.

2. **Line 1 agents focus on real-time operational risk detection.** Transaction monitoring agents, trading desk risk alerts, AML screening, and sanctions checks are the dominant line 1 use cases. These agents operate at machine speed with human review triggered by agent-generated alerts — placing substantive risk identification firmly in the agent's domain.

3. **Accountability architecture is universally "human reviewer" in current deployments.** Every documented deployment positions the agent output as a tool output, not a determination. A named compliance officer, risk manager, or senior manager retains formal accountability for final decisions. No disclosed deployment positions an agent as making binding risk determinations without mandatory human sign-off.

4. **NICE Actimize SURVEIL-X with generative AI reduces false positives by up to 85% and detects up to four times more misconduct than traditional systems.** This is a vendor claim from a 2024 release announcement; independent validation is not available in public sources.

5. **McKinsey estimates agentic AI can automate up to 70% of manual compliance work** in financial crime compliance, with pilot implementations reporting fourfold improvements in true risk detection. Oliver Wyman (February 2026) has separately documented agentic AI reshaping compliance at financial institutions, with the transition from alert-based to end-to-end autonomous workflow already underway.

6. **FCA/PRA DP5/22 considered but did not introduce an SMCR prescribed responsibility for AI oversight.** The 2022 discussion paper asked whether there should be a named senior manager prescribed responsibility for AI. Industry feedback was mixed; the FCA/PRA concluded existing SMCR accountability is sufficient, with existing senior managers (CRO, CTO) accountable for AI risk within their domains. No new prescribed responsibility was created.

7. **APRA is applying CPS 220 and enhanced governance proposals to AI agents, not creating a new AI-specific standard.** APRA's March 2025 enhanced governance proposals address board oversight of technology including AI, requiring clear accountability, independent validation, and escalation paths. The three-lines model is explicitly recommended but not AI-agent-specific.

8. **RBNZ has no AI-specific interpretive guidance for line 1 or line 2 agents.** BS11 (outsourcing) and the corporate governance policy apply implicitly — banks must retain control, ensure stand-alone operability, and maintain board-level accountability for outsourced AI functions. There is no RBNZ interpretive material addressing the accountability question for agentic oversight functions.

9. **IBM OpenPages 9.1.3 explicitly markets itself as "the first step toward agentic GRC."** This framing acknowledges the gap: current deployments are not agentic in the autonomous-determination sense. AI assists human workflows; it does not replace human accountability for risk determinations.

10. **Three documented failure modes in agentic compliance agents:** (a) overconfidence/hallucination producing plausible but incorrect risk narratives; (b) alert fatigue from false positives masking genuine risk signals (false negatives); (c) explainability gaps making it impossible to audit why the agent failed to flag an event. AI incident reports in financial services rose over 50% between 2023 and 2025.

11. **JPMorgan Chase is the most advanced bank in documented agentic risk integration.** Its proprietary LLM Suite and OmniAI platforms support agentic multistep tasks across legal, regulatory, and compliance workflows with multi-level human-in-the-loop oversight. No public disclosure confirms line 2 determinations are made by agent without human sign-off.

12. **No regulator has published guidance specifically addressing the nominal-review problem.** When agents operate at a scale and speed where human review is formally present but substantively impossible, the traditional accountability model (human reviewer is accountable) is strained but no supervisor has defined what constitutes adequate oversight in this scenario.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| NICE Actimize SURVEIL-X deployed in line 2 compliance surveillance with generative AI | NICE press release, 2024; A-Team Insight | high | Production deployment confirmed |
| SURVEIL-X reduces false positives by 85%, detects 4x more misconduct | NICE press release, 2024 | medium | Vendor claim; no independent validation |
| Behavox and Nasdaq Surveillance are production line 2 tools | Industry analysis, multiple sources | high | Well-established products |
| IBM OpenPages 9.1.3 is "first step toward agentic GRC" | IBM announcement, 2024 | high | Direct vendor statement |
| Accountability architecture universally requires named human reviewer | McKinsey, Oliver Wyman, NICE, IBM documentation | high | No counterexample found in disclosed deployments |
| McKinsey: agentic AI can automate 70% of manual compliance work | McKinsey, 2024 | medium | Estimate based on modelling, not completed deployments |
| FCA/PRA did not create a new SMCR prescribed responsibility for AI | FCA FS23/6, PRA FS2/23 | high | Direct regulatory statement |
| FCA/PRA: existing SMCR is sufficient for AI accountability | FCA/PRA AI update, April 2024 | high | Direct regulatory position |
| APRA applying CPS 220 to AI, not creating AI-specific standard | APRA enhanced governance proposals, March 2025 | high | Confirmed by regulatory analysis |
| RBNZ has no AI-specific interpretive guidance for risk agents | RBNZ BS11, corporate governance policy | high | Absence confirmed by review of RBNZ publications |
| JPMorgan Chase most advanced bank in agentic risk integration | CNBC, multiple financial press, 2024–2025 | medium | Based on public disclosures; actual internal architecture not independently verified |
| Three failure modes in agentic compliance: overconfidence, alert fatigue, explainability gap | Sardine.ai analysis, Aveni.ai, McKinsey | high | Consistent across multiple independent sources |
| AI incident reports in financial services up 50%+ 2023–2025 | Aveni.ai industry analysis | medium | Cited by vendor; no independent audit body confirmation |
| Nominal-review problem unaddressed by regulators | Review of FCA, PRA, APRA, BIS, RBNZ guidance | high | Absence of guidance confirmed across all reviewed regulators |

### Assumptions

- **Assumption:** Public disclosures by major banks accurately reflect their governance architecture for AI risk agents. **Justification:** Banks are subject to regulatory disclosure requirements and litigation risk that discourage misrepresentation of governance structures in public filings and annual reports.
- **Assumption:** Vendor capability claims (NICE Actimize 85% false positive reduction) reflect operational results at some client sites, not hypothetical performance. **Justification:** Regulatory environment creates liability for false marketing in financial services; claims of this specificity are unlikely to be fabricated. However, generalisation to all deployments is not warranted.
- **Assumption:** The absence of RBNZ-specific AI agent guidance reflects a policy choice to apply existing frameworks, not a gap in RBNZ's awareness of the issue. **Justification:** RBNZ has engaged actively on operational resilience and technology governance; the silence on AI-specific standards is consistent with its principles-based supervisory style.

### Analysis

The landscape splits cleanly into two deployment types. Established commercial platforms (NICE Actimize, Behavox, Nasdaq, IBM OpenPages) represent mature line 2 tooling — these agents have been operating in compliance surveillance for years, and the generative AI upgrades in 2023–2024 increased detection capability while maintaining the same human-reviewer accountability architecture. The "first step toward agentic GRC" framing from IBM is telling: vendors are clearly positioning for a world where agents make determinations, but are not there yet.

The in-house bespoke build category is dominated by JPMorgan Chase at the disclosed end. Their scale and proprietary platform investment makes them genuinely different from peers. HSBC and ING show standard vendor-reliance patterns; ANZ's AI risk management posture is not publicly documented in sufficient detail to characterise.

The accountability gap is the central unresolved problem. All current deployments resolve it the same way: the agent flags, the human decides. This is defensible when human review is substantive. It becomes legally and prudentially problematic when agent throughput exceeds human review capacity — which is precisely the efficiency case for deploying agents at scale. Regulators have not addressed this tension directly. The FCA/PRA's decision not to create a new SMCR prescribed responsibility for AI means the accountability burden falls on whoever owns the risk function — the CRO, CCO, or analogous senior manager. This person is accountable for a determination process they may not be able to review in any meaningful sense.

The three-lines model itself faces structural stress from agentic AI. When an AI agent performs a line 2 function (independent oversight and challenge of line 1), the independence of the second line is a function of the agent's training, objective function, and governance — not the organisational separation of the human reviewer. This is a qualitatively different accountability problem from human second-line oversight, and no existing prudential framework addresses it.

### Risks, Gaps, and Uncertainties

- **Bespoke in-house build disclosure gap**: The research is heavily weighted toward disclosed vendor deployments and high-profile institutions. It is plausible that mid-tier banks have built or bought line 2 agents with significantly different governance architectures that have not been publicly documented.
- **Regulatory silence may be temporary**: FCA's AI Strategy, the EU AI Act's application to high-risk financial services use cases, and APRA's governance enhancement proposals all suggest more prescriptive guidance is coming. The current "existing frameworks apply" position may change materially in 2025–2026.
- **Vendor claims lack independent validation**: The 85% false-positive reduction and 4x detection improvement claims from NICE Actimize are not independently validated in academic or regulatory publications found in this research.
- **JPMorgan Chase**: The "fully AI-powered megabank" framing (CNBC, 2025) includes some details that may reflect intended future state rather than current production deployment.
- **RBNZ-specific gap**: RBNZ has not published any supervisory speeches, Q&As, or guidance notes addressing AI agents in risk functions. This is a genuine regulatory gap for NZ-incorporated entities and their boards.

### Open Questions

- When agent throughput in compliance surveillance exceeds human review capacity, at what point does nominal human sign-off cease to constitute adequate oversight under prudential law? No regulator has addressed this threshold.
- How should independent validation of line 2 AI agents be structured when the agent's role is itself independent validation of line 1 activities? (The circular dependency problem in AI-mediated second-line oversight.)
- Are there any documented cases where a regulator has held an institution accountable specifically because an AI agent's oversight failure was attributed to inadequate human oversight rather than the agent itself? This would clarify the supervisory threshold.
- Should RBNZ-supervised entities proactively seek interpretive guidance on AI agent governance under BS11 and the corporate governance policy, or wait for formal standard updates?
- What is the appropriate escalation trigger threshold in an agentic line 2 oversight function — and who has the authority to set it?

---

## Output

- Type: knowledge
- Description: Landscape of AI agents operating in line 1 and line 2 risk functions in financial services: dominant commercial platforms, governance and accountability architecture of current deployments, regulatory positions across FCA/PRA/APRA/BIS/RBNZ, three documented failure modes, and the unresolved nominal-review accountability problem.
- Links:
  - https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/how-agentic-ai-can-change-the-way-banks-fight-financial-crime (McKinsey: agentic AI in financial crime compliance)
  - https://www.nice.com/press-releases/nice-actimize-empowers-surveil-x-with-generative-ai-launching-a-new-era-in-market-abuse-and-conduct-risk-detection (NICE Actimize SURVEIL-X generative AI launch)
  - https://www.bis.org/fsi/publ/insights63.pdf (BIS FSI Insights: Regulating AI in the financial sector)