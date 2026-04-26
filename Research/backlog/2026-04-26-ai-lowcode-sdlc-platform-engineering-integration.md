---
title: "How should AI and low-code governance integrate with existing software development and platform engineering practices?"
added: 2026-04-26T10:11:11+00:00
status: backlog
priority: high
blocks: [2026-04-26-ai-governance-cost-performance-delivery-impact, 2026-04-26-ai-agent-control-plane-architecture-enterprise]
tags: [sdlc, platform-engineering, ci-cd, devops, ai-governance, low-code, testing, release-management, infrastructure-as-code, enterprise-engineering]
started: ~
completed: ~
output: [knowledge]
---

# How should AI and low-code governance integrate with existing software development and platform engineering practices?

## Research Question

How should AI and low-code governance integrate with existing software development and platform engineering practices — specifically, how should governance controls be integrated with Continuous Integration/Continuous Delivery (CI/CD) pipelines, infrastructure-as-code, testing frameworks, release management, and platform engineering standards to avoid fragmentation between traditional and AI/low-code delivery models?

## Scope

**In scope:**
- Integration of AI and low-code governance checks into CI/CD pipelines: automated governance gates (security scanning, compliance checks, licence validation, model performance tests) as pipeline stages
- Infrastructure-as-code (IaC) for AI and low-code governance: expressing governance policy, environment configuration, and deployment constraints as code (Terraform, Bicep, Pulumi) rather than manual configuration
- Testing frameworks for AI and low-code artefacts: unit testing for low-code logic, integration testing for AI-human workflows, evaluation frameworks for AI model outputs (LLM evaluation, accuracy benchmarking, adversarial testing)
- Release management: how AI and low-code releases should be coordinated with traditional software releases when they share dependencies, data, or user interfaces
- Platform engineering standards: how AI and low-code development should be scaffolded via internal developer platforms (IDPs) — paved roads that embed governance by default rather than requiring developers to manually apply governance controls
- Preventing fragmentation: the risk that AI/low-code delivery operates on an entirely separate governance track from traditional software delivery, creating inconsistent standards and audit surface

**Out of scope:**
- Lifecycle management of AI artefacts (covered by Q7)
- Enforcement architecture at deployment time (covered by Q3)
- Vendor platform-specific limitations (covered by Q11)

**Constraints:**
- Must address both the developer-facing side (how governance affects development workflow and tooling) and the governance-facing side (how governance controls are assured through the pipeline)
- Must assess the specific challenge of testing AI systems — where traditional pass/fail testing is insufficient for non-deterministic outputs — and propose evidence-based testing approaches
- This item requires Q3 (enforcement architecture) and Q7 (lifecycle model) as inputs because pipeline integration depends on knowing what enforcement points to connect to and what the lifecycle stages are

## Context

AI and low-code delivery programmes frequently operate on separate tracks from traditional software engineering — using different tools, different approval processes, and different quality standards. This fragmentation creates: inconsistent governance assurance across the technology estate, audit gaps where AI/low-code systems are not subject to the same evidence generation as traditional systems, and knowledge silos that prevent platform engineers from applying their expertise to AI/low-code governance. Integrating AI/low-code governance into existing software development and platform engineering practices is the mechanism by which governance becomes continuous rather than periodic.

Cross-references:
- Q3: `2026-04-26-ai-lowcode-governance-enforcement-architecture` (prerequisite)
- Q7: `2026-04-26-ai-lowcode-lifecycle-management` (prerequisite)
- Q1: `2026-04-26-ai-lowcode-decision-rights-accountability-liability`
- Q8: `2026-04-26-ai-governance-cost-performance-delivery-impact`
- Q16: `2026-04-26-ai-agent-control-plane-architecture-enterprise`

## Approach

1. **CI/CD governance gate design:** Review current practice for integrating governance checks into CI/CD pipelines for traditional software (SAST, DAST, licence compliance, SBOM generation); assess which checks translate directly to AI and low-code pipelines, and which new checks are required (model evaluation, prompt safety testing, low-code dependency scanning).
2. **Infrastructure-as-code for AI governance:** Review how IaC can be used to codify AI governance environment configuration — access controls, network policies, model deployment configuration, logging configuration — and assess existing IaC modules for AI platform deployments (Terraform modules for Azure AI Foundry, AWS Bedrock).
3. **AI testing frameworks:** Review AI-specific testing frameworks (DeepEval, Promptfoo, Ragas for RAG evaluation, Giskard for AI model testing) and assess their integration with standard CI/CD pipeline tooling (GitHub Actions, Azure DevOps, Jenkins). Assess the fundamental testing challenge for non-deterministic systems and what evaluation standards are emerging.
4. **Platform engineering patterns:** Review the internal developer platform (IDP) literature and assess how golden paths and paved roads can embed AI/low-code governance by default — so developers cannot easily deploy without governance compliance. Assess Backstage, Port, and similar IDP platforms for AI governance plugin capability.
5. **Fragmentation risk assessment:** Identify the specific ways that AI/low-code delivery fragmentation creates governance gaps and audit surface inconsistency; propose integration patterns that close these gaps.
6. **Synthesis:** Produce a set of integration patterns — pipeline gate specifications, IaC module designs, testing framework recommendations, and IDP scaffolding guidance — for integrating AI/low-code governance into existing platform engineering practice.

## Sources

- [ ] [DORA (DevOps Research and Assessment) — Accelerate State of DevOps Report 2024](https://dora.dev/research/2024/dora-report/) — empirical research on software delivery performance and governance integration; assess for AI/low-code delivery performance evidence
- [ ] [NIST SSDF (Secure Software Development Framework) SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) — secure software development lifecycle; assess for applicability to AI and low-code artefact delivery pipelines
- [ ] [GitHub Actions — governance and compliance workflows](https://docs.github.com/en/actions) — CI/CD platform reference; assess for AI governance gate implementation patterns
- [ ] [Backstage — internal developer platform for governance by default](https://backstage.io/docs/overview/what-is-backstage) — IDP platform; assess for AI/low-code governance plugin ecosystem
- [ ] [DeepEval — LLM evaluation framework](https://docs.confident-ai.com/) — AI testing framework for large language model (LLM) applications; assess for CI/CD integration capability
- [ ] [Ragas — RAG evaluation framework](https://docs.ragas.io/en/latest/) — evaluation framework for Retrieval-Augmented Generation (RAG) systems; assess for pipeline integration
- [ ] [Terraform — infrastructure-as-code for cloud governance](https://developer.hashicorp.com/terraform/docs) — IaC tooling; assess for AI platform governance configuration management patterns

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
