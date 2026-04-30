---
title: "Explainable Artificial Intelligence (XAI): current research state, leading institutions, and regulatory intersection in heavily regulated industries"
added: 2026-04-30T06:42:30+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []
tags: [governance, regulation, agentic-ai, artificial-intelligence, financial-services, eu-ai-act, audit, explainability]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []
related: [2026-04-24-ai-agent-regulation-global-financial-services, 2026-04-22-ai-governance-assurance-change-control-verification, 2026-02-28-ai-control-testing-and-assurance, 2026-02-28-rbnz-ai-supervisory-expectations]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Explainable Artificial Intelligence (XAI): current research state, leading institutions, and regulatory intersection in heavily regulated industries

## Research Question

What is the current state of Explainable Artificial Intelligence (XAI) research — who leads it and what are the primary techniques — and how does XAI intersect with regulatory obligations, audit requirements, and accountability for automated decisions made by AI agents in heavily regulated industries such as financial services and healthcare?

## Scope

**In scope:**
- Definition and taxonomy of Explainable Artificial Intelligence (XAI): how it differs from interpretability; key technique families (post-hoc, ante-hoc; local, global; model-agnostic, model-specific)
- Leading research groups, institutions, funded programmes, and published benchmarks in XAI as of 2024–2026
- Regulatory frameworks that explicitly require or incentivise explanations for AI-driven decisions: EU Artificial Intelligence Act (EU AI Act), GDPR Article 22 (right to explanation), US Federal Reserve SR 11-7 (model risk management), Basel operational risk principles, APRA CPS 220/230, UK FCA/PRA AI guidance, ISO 42001
- How XAI applies to audit trail design and third-line review for automated decisions in financial services and healthcare
- XAI challenges in agentic AI systems where the decision chain is distributed across multiple models or tools

**Out of scope:**
- Full algorithmic derivations of individual XAI methods (SHAP, LIME, Grad-CAM, etc.) — technique survey only
- XAI for consumer-facing applications outside regulated contexts
- Hardware-level explainability (neuromorphic chips, analogue computing)
- Fairness and bias auditing as a separate discipline (referenced only where it intersects XAI obligations)

**Constraints:**
- Primary focus on published research and regulatory guidance from 2020 onwards; earlier foundational work cited only for context
- English-language sources; non-English regulatory documents accepted where official translations exist

## Context

Regulated industries — financial services, healthcare, critical infrastructure — are under increasing pressure from regulators to justify automated decisions made by AI systems. The EU AI Act (2024) imposes transparency obligations on high-risk AI systems; GDPR Article 22 grants data subjects the right to a meaningful explanation for solely automated decisions; SR 11-7 requires model validation including sensitivity analysis; and emerging agentic AI deployments raise the question of whether an explanation can even be extracted when a decision emerges from a chain of loosely coupled models. This item maps the XAI landscape and identifies what is and is not technically achievable given current regulatory expectations.

This item links to the existing threads on AI governance assurance (`2026-04-22-ai-governance-assurance-change-control-verification`), global AI agent regulation in financial services (`2026-04-24-ai-agent-regulation-global-financial-services`), and AI control testing (`2026-02-28-ai-control-testing-and-assurance`).

## Approach

1. **Define XAI** — Distinguish Explainable Artificial Intelligence from interpretability; map the taxonomy of techniques by scope (local/global), timing (ante-hoc/post-hoc), and model dependency (model-agnostic/model-specific). Identify the most cited survey papers as anchor references.

2. **Survey leading researchers and institutions** — Identify the top research groups, funded programmes (DARPA XAI programme, EU Horizon projects), and prolific authors. Identify whether academia or industry labs (Google DeepMind, Microsoft Research, IBM Research) dominate the current frontier.

3. **Review technique landscape** — Survey the primary XAI method families: SHAP (SHapley Additive exPlanations), LIME (Local Interpretable Model-agnostic Explanations), attention-based explanations, counterfactual explanations, concept activation vectors (TCAV), and rule extraction. Note known limitations (faithfulness vs. plausibility trade-off, explanation instability).

4. **Map regulatory requirements** — Identify which regulations impose XAI-adjacent obligations, what they specifically require (right to explanation, model documentation, audit trail, human review), and how organisations are currently meeting these obligations.

5. **Audit and accountability intersection** — Examine how XAI outputs are used (or should be used) in first-line validation, second-line model risk management, and third-line audit. Review published guidance from the Bank of England, FCA, APRA, OCC, and ISO 42001 on AI auditability.

6. **Agentic AI and XAI** — Identify the specific XAI challenges that arise when decisions are produced by multi-step agentic systems (tool-use chains, multi-agent pipelines): attribution across steps, causal tracing, explanation aggregation. Review emerging work on mechanistic interpretability as a potential answer.

## Sources

- [ ] [EU AI Act (Regulation 2024/1689) — Official Text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689) — primary regulatory text; transparency obligations for high-risk AI systems
- [ ] [GDPR Article 22 — Automated individual decision-making](https://gdpr-info.eu/art-22-gdpr/) — right not to be subject to solely automated decisions; right to explanation
- [ ] [Federal Reserve SR 11-7 — Guidance on Model Risk Management](https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm) — US model risk management; conceptual soundness and sensitivity analysis requirements
- [ ] [Arrieta et al. (2020) — Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI](https://doi.org/10.1016/j.inffus.2019.12.012) — most-cited XAI survey paper; taxonomy anchor
- [ ] [Lundberg & Lee (2017) — A Unified Approach to Interpreting Model Predictions (SHAP)](https://arxiv.org/abs/1705.07874) — foundational SHAP paper
- [ ] [Ribeiro et al. (2016) — "Why Should I Trust You?": Explaining the Predictions of Any Classifier (LIME)](https://arxiv.org/abs/1602.04938) — foundational LIME paper
- [ ] [DARPA Explainable AI (XAI) programme](https://www.darpa.mil/program/explainable-artificial-intelligence) — US government-funded XAI research programme; overview of funded projects
- [ ] [ISO/IEC 42001:2023 — AI Management Systems](https://www.iso.org/standard/81230.html) — international standard; transparency and explainability obligations
- [ ] [Bank of England / FCA — AI Public-Private Forum Final Report (2022)](https://www.bankofengland.co.uk/paper/2022/aippf-final-report) — UK financial sector AI governance; explainability expectations
- [ ] [APRA CPG 234 / CPS 230 — Operational Risk and Resilience](https://www.apra.gov.au/operational-risk-management) — APRA operational risk guidance relevant to AI model governance
- [ ] [Kim et al. (2018) — Interpretability Beyond Classification (TCAV)](https://arxiv.org/abs/1711.11279) — concept activation vectors; ante-hoc global explanation technique
- [ ] [Doshi-Velez & Kim (2017) — Towards a rigorous science of interpretable machine learning](https://arxiv.org/abs/1702.08608) — foundational framing of interpretability vs. accuracy trade-offs
