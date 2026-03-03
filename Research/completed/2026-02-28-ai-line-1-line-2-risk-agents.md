---
title: "AI Line 1 and Line 2 Risk Agents: Who Is Building Them?"
added: 2026-02-28
status: completed
priority: high
tags: [ai-strategy, risk-agents, line-1, line-2, three-lines-model, agentic-ai, financial-services, risk-management]
started: 2026-03-03
completed: 2026-03-03
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
3. **Accountability model analysis** — how is accountability for agent outputs structured? Is there a named human reviewer? Is the agent's output treated as a tool output (human decides) or a determination (agent decides, human audits)?\
4. **Regulatory position** — have RBNZ, APRA, FCA, PRA, or Fed/OCC published any guidance specifically addressing AI agents in risk oversight functions? What is the current supervisory expectation?
5. **Failure modes** — identify any disclosed incidents where a line 1 or line 2 AI agent produced an incorrect output that resulted in a risk management failure. What went wrong and how was it caught?

## Sources

- [x] Risk.net: AI in risk management coverage 2023–2025
- [x] Celent / Oliver Wyman: AI in risk management research reports
- [x] Bank for International Settlements (BIS): FSI Insights #63 "Regulating AI in the financial sector" (2024)
- [x] FCA / PRA: AI in financial services discussion papers (DP5/22, DP3/22, 2024 follow-ups)
- [x] APRA CPG 234 / CPS 220: operational and model risk governance expectations
- [x] RBNZ: BS11 governance — no AI-specific interpretive material found
- [x] Major bank disclosures: ANZ Group, JPMorgan Chase, HSBC, ING Group
- [x] IIF (Institute of International Finance): IIF-EY AI/ML Survey 2024
- [x] Vendor documentation: Behavox, NICE Actimize, Nasdaq Surveillance
- [ ] RiskMinds / OpRisk Global 2024 conference proceedings — not directly accessible

---

## Findings

### Executive Summary

AI agents operating within line 1 and line 2 of the three lines of defence model are deployed at scale by major banks and vendors as of 2024–2025, primarily in compliance surveillance, transaction monitoring, AML, and market abuse detection. The dominant architecture treats agent output as a decision-support tool rather than a binding determination: the agent flags or triages, and a named human reviewer makes or ratifies the final call. Every major regulator (FCA/PRA, APRA, RBNZ via general principles, BIS FSI) has declined to issue AI-specific rules, relying instead on existing governance and accountability frameworks — principally SM&CR in the UK and CPS 230 in Australia — to assign human accountability. The critical unresolved problem identified in this research: no regulator has defined a threshold at which nominal human review of high-volume AI output ceases to be substantive, leaving institutions exposed to accountability gaps as agent autonomy and alert volumes grow.

### Key Findings

1. **Vendor market is mature for line 2 surveillance agents.** Behavox (serving 10 of 24 G-SIBs) and NICE Actimize (SURVEIL-X) are the dominant commercial providers of AI-powered compliance and conduct surveillance. Both have integrated generative AI and LLMs. Behavox reports 86% customer base growth in 2025; NICE Actimize claims up to 85% false-positive reduction with GenAI. Nasdaq Surveillance has embedded AI for market abuse detection with demonstrated 40% false-positive reduction.

2. **JPMorgan Chase has the most explicit second-line AI governance disclosure.** Its dedicated Model Risk Governance function (second line) assesses every ML/AI use case for bias, drift, and unplanned outcomes. LLM Suite is deployed to 250,000 employees. Human review is structurally required for sensitive judgments. This is a disclosed Type 3 pattern: agents act, second-line function audits and validates.

3. **HSBC operates a billion-transaction-scale Line 1 AML agent.** In partnership with Google, HSBC's Dynamic Risk Assessment system checks approximately 1 billion transactions monthly for fraud and AML signals. The system is overseen by responsible AI committees. This is the most operationally scaled disclosed deployment found.

4. **ING Group has deployed agentic AI across KYC and transaction monitoring.** ING's agentic AI handles KYC data checks (seconds vs days previously) and prioritises AML alerts, with human investigators focused on high-risk activity. ING publicly positions this as occurring "within a controlled, well-governed framework."

5. **The universal architecture is alert-to-human-review, not agent-determines.** Across all identified deployments, the agent produces alerts, flags, or triage outputs; a human ratifies or acts. No major financial institution has publicly disclosed a deployment where an AI agent in a line 2 function issues final compliance determinations without human sign-off. The output is treated as a tool output, not a binding judgment.

6. **Human review at scale creates a structural accountability gap.** At billion-transaction scale or with thousands of daily alerts, human review becomes sampling rather than case-by-case review. The accountability chain requires a named human to be responsible, but substantive review of each alert is impossible. No regulator has drawn the line between adequate review and nominal rubber-stamping.

7. **FCA/PRA rely on SM&CR rather than AI-specific rules.** UK supervisors require a named senior manager to be explicitly accountable for any AI function under the Senior Managers and Certification Regime. No new AI-specific rules are planned. Consumer Duty and existing principles apply. This is the current UK accountability mechanism for line 2 AI agents.

8. **APRA's CPS 230 (effective July 2024) is the primary Australian accountability framework.** CPS 230 Operational Risk Management covers AI agents under its operational risk and third-party governance requirements. APRA has explicitly declined to introduce AI-specific rules, stating existing standards are adequate. Human-in-the-loop accountability is mandatory; organisations cannot fully delegate responsibility to AI systems.

9. **RBNZ has no AI-specific guidance; general BS11 principles apply.** RBNZ BS11 governance principles require accountability, human oversight, and board-level risk management, but contain no AI-specific interpretive material. RBNZ-supervised entities operating line 2 AI agents must rely on general governance expectations, without explicit supervisory guidance on agentic oversight functions.

10. **BIS FSI Insights #63 (2024) identifies explainability and vendor risk as key systemic concerns.** BIS calls for risk-based approaches covering explainability, transparency, data security, and strong oversight for both banks and vendors. The BIS also flags the concentration risk in third-party AI vendors as a systemic vulnerability not adequately addressed by existing regulation.

11. **Governance readiness is low relative to deployment pace.** Industry surveys (Kroll 2024, Fenergo 2024) indicate only one-third of bank executives believe their compliance programs are "very prepared" for AI-driven agent risks. Only ~4.5% of organisations are willing to allow agentic AI to act fully autonomously. Early GenAI pilots have failed to deliver expected ROI in a significant proportion of cases.

12. **No major publicly disclosed incident of a line 2 AI agent failure has occurred yet.** Compliance lapses linked to AI agents (AML/KYC failures, missed suspicious activity) are documented in aggregate industry surveys but not yet attributed to specific named institutions with a specific Line 2 agent failure. The first major publicly attributed incident is a matter of when, not if.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Behavox serves 10 of 24 G-SIBs; 86% customer growth 2025 | Morningstar/BusinessWire (Behavox press release, Feb 2026) | high | Vendor-reported; corroborated by multiple trade press sources |
| NICE Actimize SURVEIL-X claims 85% false-positive reduction with GenAI | NICE press release; FinTech Alliance | high | Vendor-reported; independent validation not found |
| Nasdaq AI surveillance reduces false positives ~40%; 33% investigation time reduction | Traders Magazine; investing.com (2024) | high | Pilot results; Saudi Arabia proof-of-concept cited |
| JPMorgan Chase LLM Suite deployed to 250,000 employees; MRG is second-line function | JPMorgan Chase corporate site; CEF Pro; AI Magazine | high | Disclosed by JPMorgan; multiple corroborating sources |
| HSBC checks ~1 billion transactions monthly with Google AI partnership | HSBC corporate views; Google Cloud blog | high | Disclosed by HSBC and Google; corroborating sources |
| ING agentic AI deployed for KYC and transaction monitoring | BFSI Insider (2024) | medium | Trade press; ING has not published detailed technical disclosure |
| Universal architecture: agent flags, human ratifies | Across all vendor and bank disclosures reviewed | high | No exceptions found; consistent across all sources |
| Accountability gap at high alert volumes | Moodys Insights; Fulcrum Digital; IBM whitepaper | medium | Identified as structural risk; no specific incident documented |
| FCA/PRA rely on SM&CR for AI accountability; no AI-specific rules | FCA website; DLA Piper analysis; Traverse Smith analysis (2024) | high | Multiple legal analysis sources corroborate |
| APRA CPS 230 effective July 2024 covers AI operational risk | Lexology; Ashurst; Insurance News | high | Corroborated by multiple Australian legal sources |
| RBNZ has no AI-specific guidance | Web search across RBNZ publications | medium | Absence of evidence; no specific document reviewed |
| BIS FSI Insights #63 identifies explainability and vendor concentration risk | BIS FSI publication; Charltons Quantum analysis | high | Primary source accessible |
| Only 1/3 of executives believe compliance programs are "very prepared" | Kroll report via Corporate Compliance Insights (2024) | medium | Survey-based; single source |
| ~4.5% of organisations willing to let agentic AI act fully autonomously | Moodys Insights (2025) | medium | Single survey source |
| No major publicly attributed line 2 AI agent failure | Broad web search and industry survey review | medium | Absence of finding; may reflect under-reporting |

### Assumptions

- **Assumption:** Vendor-reported performance metrics (false-positive reduction rates) are directionally accurate, though may be optimistically stated. **Justification:** Multiple independent sources corroborate general performance improvement claims, even if absolute figures are vendor-reported.
- **Assumption:** Disclosed deployments at JPMorgan and HSBC are representative of leading practice, not outliers. **Justification:** These are among the most advanced and publicly transparent institutions; actual industry practice is likely less mature.
- **Assumption:** RBNZ-supervised entities are subject to the same fundamental governance accountability constraints as APRA/FCA-supervised entities, notwithstanding the absence of AI-specific RBNZ guidance. **Justification:** BS11 governance principles contain equivalent general accountability requirements.

### Analysis

The market has moved ahead of regulation. Major banks and specialist vendors are deploying line 1 and line 2 AI agents at scale — primarily for compliance surveillance, AML, and market abuse detection — while regulators have deliberately maintained technology-neutral, principles-based stances. The BIS, FCA/PRA, and APRA all reached the same conclusion: existing frameworks (SM&CR, CPS 230, general governance principles) are sufficient for now.

The dominant accountability pattern is consistent: AI agents are classified as tools, not decision-makers. This classification holds the accountability chain intact — the agent produces output, a human decides, a human is accountable. This is the design that is both technically accurate and regulatorily acceptable.

The structural challenge identified in the original context is real and unresolved. At HSBC's scale (1 billion transactions monthly), any human "review" of every alert is fictional. The practical model is sampling and exception review — which is defensible as an operational model but creates an accountability ambiguity: is the reviewer accountable for alerts they never individually reviewed? No regulator has answered this question explicitly. The current position defers the problem by treating it as a question of risk appetite and internal governance rather than regulatory bright-line.

The governance readiness gap (only ~1/3 of executives "very prepared") is the most operationally significant finding for institutions building these systems now. The gap between deployment pace and governance maturity is where the first major incident will originate — most likely an AML or compliance surveillance failure where a line 2 AI agent produced incorrect output, human review was nominal, and the failure was not caught until regulatory examination.

Vendor concentration (a small number of providers serving the majority of large FIs) amplifies systemic risk, as noted by BIS. A failure in Behavox or NICE Actimize could simultaneously degrade second-line oversight at a significant proportion of the global banking system.

### Risks, Gaps, and Uncertainties

- **Nominal review threshold undefined.** The point at which sampling-based human review of AI alerts ceases to constitute genuine accountability is not defined by any regulator. This gap will be stress-tested when a major incident occurs.
- **RBNZ-specific guidance absent.** RBNZ has not published AI-specific supervisory guidance. RBNZ-supervised entities must extrapolate from general BS11 principles. The gap creates uncertainty for New Zealand bank compliance functions.
- **Vendor concentration risk unquantified.** The degree to which major banks rely on the same 2–3 surveillance vendors for line 2 oversight creates correlated failure risk. No public data on concentration levels was found.
- **Failure mode data is aggregate, not case-specific.** Industry surveys document compliance lapses linked to AI agents in aggregate. No specific publicly named institution-incident pair was found for a line 2 failure. The research cannot characterise failure modes at the specific case level.
- **Agentic AI vs. ML distinction blurs in practice.** Many disclosures conflate traditional ML models (not agentic) with agentic systems. The transition point from model-based to agent-based is not clearly disclosed, making it difficult to distinguish true agents from sophisticated models.

### Open Questions

- At what alert volume or review ratio does regulatorily accepted "human review" become substantively meaningless? Is there a safe harbour standard?
- Has RBNZ engaged with any bank on AI governance expectations for line 2 oversight functions, even informally?
- Do the G-SIBs using Behavox and NICE Actimize treat the vendor's AI as a line 2 tool or have they structured it formally as a second-line function with specific governance overlay?
- What does a "reasonable" governance framework look like for a line 2 agent in a mid-size New Zealand bank that cannot afford the JPMorgan MRG architecture?
- Is there a disclosed case from RiskMinds or OpRisk Global 2024 that documents a line 2 AI agent failure and the post-incident governance response?

---

## Output

- Type: knowledge
- Description: Landscape of vendors and deployments for line 1/line 2 AI risk agents; architecture patterns; accountability frameworks by jurisdiction; the nominal review gap problem.
- Links:
  - https://www.jpmorganchase.com/about/technology/news/ai-and-model-risk-governance (JPMorgan MRG disclosure)
  - https://www.bis.org/fsi/publ/insights63.pdf (BIS FSI Insights #63 — Regulating AI in the financial sector)
  - https://www.moodys.com/web/en/us/insights/ai/navigating-the-shift-how-agentic-ai-is-reshaping-risk-and-compliance.html (Moody's: agentic AI reshaping risk and compliance)
