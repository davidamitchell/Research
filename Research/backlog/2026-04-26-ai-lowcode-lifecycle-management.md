---
title: "What lifecycle management model is required for Artificial Intelligence (AI) models, prompts, and low-code applications?"
added: 2026-04-26
status: backlog
priority: high
blocks: [2026-04-26-ai-lowcode-sdlc-platform-engineering-integration, 2026-04-26-ai-agent-control-plane-architecture-enterprise]
tags: [lifecycle-management, ai-models, prompts, low-code, versioning, deployment-controls, rollback, decommissioning, change-management, enterprise-governance]
started: ~
completed: ~
output: [knowledge]
---

# What lifecycle management model is required for Artificial Intelligence (AI) models, prompts, and low-code applications?

## Research Question

What comprehensive lifecycle management model is required for AI models, prompts, and low-code applications — covering versioning strategies, deployment controls, rollback mechanisms, ownership tracking, change management, documentation standards, and processes for decommissioning or retiring unused or unsafe artefacts?

## Scope

**In scope:**
- Lifecycle stages for AI models, prompts, and low-code artefacts: development, testing, staging, production deployment, monitoring in production, version updates, and decommissioning
- Versioning strategies: how AI models, prompts, and low-code applications should be versioned to enable reproducibility, auditability, and rollback
- Deployment controls: what gates, approvals, and automated checks should be required before promoting an artefact to production (consistent with Q5 risk tiers and Q1 approval structures)
- Rollback mechanisms: when and how a deployed model, prompt, or low-code application can be rolled back to a previous version, and what constitutes a rollback trigger
- Ownership tracking: how artefact ownership is recorded and maintained through the lifecycle, including ownership transitions when personnel change
- Change management: how changes to deployed artefacts (model updates, prompt modifications, low-code logic changes) are classified, reviewed, and approved
- Documentation standards: what documentation is required at each lifecycle stage (design documentation, risk assessment, approval records, deployment records, decommissioning records)
- Decommissioning: what conditions trigger decommissioning, what the decommissioning process requires, and how to ensure no unsafe or ungoverned artefacts remain in production
- Alignment with data governance (Q6) for the data associated with each lifecycle stage

**Out of scope:**
- Model training and fine-tuning processes (focus is on post-training artefact lifecycle)
- Technical implementation of CI/CD pipelines for AI (covered by Q10)
- The identity model for artefact ownership attribution (covered by Q2)
- Per-artefact risk assessment (covered by Q5)

**Constraints:**
- Must address the distinct lifecycle characteristics of AI models (which can change behaviour without explicit code changes due to model updates), prompts (which are natural language artefacts with no traditional versioning convention), and low-code applications (which may have implicit dependencies on underlying platform changes)
- Must be grounded in existing software lifecycle management standards (ISO/IEC 12207, ITIL) and AI-specific lifecycle guidance, adapted for the unique characteristics of AI artefacts

## Context

The lifecycle of an AI model, prompt, or low-code application differs materially from traditional software in ways that existing change management and lifecycle frameworks do not address: AI models can change behaviour when the underlying foundation model is updated without any explicit change event; prompts produce non-deterministic outputs that are not testable to a pass/fail criterion; and low-code applications can have invisible dependencies on platform-level changes. Without a lifecycle management model that accounts for these differences, enterprises face: ungoverned artefacts in production with no known owner, inability to roll back when a model update causes unexpected behaviour, and no audit trail of how an artefact has changed over its operational life.

This item provides the lifecycle framework that SDLC integration (Q10) requires — you cannot integrate lifecycle management into delivery pipelines until you know what the lifecycle model is. It also provides the artefact management layer that the control-plane (Q16) requires to track and govern artefacts at scale.

Cross-references:
- Q1: `2026-04-26-ai-lowcode-decision-rights-accountability-liability`
- Q5: `2026-04-26-ai-lowcode-risk-tier-classification-controls`
- Q6: `2026-04-26-data-governance-ai-lowcode-enterprise-enforcement`
- Q10: `2026-04-26-ai-lowcode-sdlc-platform-engineering-integration`
- Q16: `2026-04-26-ai-agent-control-plane-architecture-enterprise`

## Approach

1. **Lifecycle stage definition:** Define the lifecycle stages for each artefact type (AI model, prompt, low-code application) and identify where each stage differs from traditional software lifecycle stages.
2. **Versioning model design:** Review versioning conventions for AI models (SemVer, hash-based, model card versioning), prompts (prompt versioning in LangSmith, Weights & Biases Prompts, Azure AI Foundry Prompt Flow), and low-code applications (platform-native versioning in Power Platform, Salesforce). Propose a unified versioning approach that supports rollback and reproducibility.
3. **Deployment gate design:** Based on Q5 risk tiers, define the deployment gates required at each tier — what automated checks (testing, security scanning, compliance checks), what human approvals, and what documentation artefacts are required before production promotion.
4. **Rollback mechanism design:** Define rollback triggers (e.g. performance degradation, compliance failure, incident) and the technical mechanisms for rollback for each artefact type. Assess the challenges specific to AI models (model rollback may not restore behaviour if external data has changed) and prompts (prompt rollback must be paired with model version pinning).
5. **Decommissioning model:** Define decommissioning triggers (end-of-life date, owner departure, risk re-assessment, regulatory change) and the decommissioning process requirements (owner sign-off, successor identification, data deletion obligations, documentation archiving).
6. **Change management integration:** Assess how changes to deployed AI artefacts (model updates from vendors, prompt modifications, low-code logic changes) should be classified under existing change management frameworks (ITIL change management) and what additional AI-specific change categories are required.
7. **Synthesis:** Produce a lifecycle management model suitable for adoption as an enterprise governance artefact, with stage definitions, gate criteria, rollback protocols, and decommissioning requirements.

## Sources

- [ ] [ISO/IEC 12207 — Systems and software engineering — Software life cycle processes](https://www.iso.org/standard/88064.html) — foundational software lifecycle standard; assess for applicability to AI artefact lifecycle stages
- [ ] [ITIL 4 — Change Enablement Practice](https://www.axelos.com/certifications/itil-service-management) — IT service management change management framework; assess for applicability to AI and low-code change classification
- [ ] [MLflow — model lifecycle and registry](https://mlflow.org/docs/latest/model-registry.html) — open-source AI model lifecycle management; assess for versioning and promotion gate capabilities
- [ ] [Microsoft Power Platform — Application Lifecycle Management (ALM)](https://learn.microsoft.com/en-us/power-platform/alm/) — low-code lifecycle management reference; primary source for Power Platform artefact lifecycle
- [ ] [Azure AI Foundry — Prompt Flow versioning and deployment](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/flow-deploy) — Microsoft prompt and agent lifecycle tooling; assess for versioning and deployment control features
- [ ] [SR 11-7 — Guidance on Model Risk Management (US Federal Reserve)](https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm) — model risk management lifecycle requirements from a financial services regulator; assess for lifecycle stage and documentation standard obligations applicable to AI models

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
