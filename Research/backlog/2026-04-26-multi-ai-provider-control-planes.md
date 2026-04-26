---
title: "Multi-provider AI control planes: capabilities, vendors, and coverage gaps"
added: 2026-04-26
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [ai-governance, control-plane, multi-provider, microsoft, aws, cursor, codex, claude, finops, security, observability]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
---

# Multi-provider AI control planes: capabilities, vendors, and coverage gaps

## Research Question

Which platforms or architectural designs provide multi-provider Artificial Intelligence (AI) control planes that unify discoverability, oversight, logging, security, data-access control, Financial Operations (FinOps), and quality of service (QoS) across Microsoft (GitHub Copilot, Microsoft 365 (M365) Copilot, Azure AI Foundry), Amazon Web Services (AWS) Bedrock and AWS Agent Core, Cursor, OpenAI Codex, and Anthropic Claude Code — and what capability gaps remain unaddressed?

## Scope

**In scope:**
- Shipping products and publicly documented architectural designs for multi-provider AI control planes
- Capability coverage across each control-plane domain: discoverability, legibility/observability, oversight/audit, logging, security/identity, data-access policy, FinOps, and quality of service
- Coverage mapping by provider: GitHub Copilot, M365 Copilot, Azure AI Foundry, AWS Bedrock, AWS Agent Core, Cursor, OpenAI Codex CLI, Claude Code
- Gaps: capabilities absent in existing products or documented as roadmap-only

**Out of scope:**
- General AI governance frameworks not tied to a concrete product or architecture (e.g. policy papers with no implementation reference)
- Model-level benchmarks or evaluation tooling not related to operational control planes
- On-premises or air-gapped deployments unless also covered by a named multi-provider plane

**Constraints:**
- Prioritise primary sources: vendor documentation, design documents, conference talks, or peer-reviewed papers; secondary summaries acceptable only if primary is unavailable
- Sources must be no older than 24 months unless they represent a foundational architectural design still in active use
- Focus on enterprise-grade capability (not consumer-tier tooling)

## Context

Enterprises deploying AI at scale across multiple providers face a proliferating set of control problems: which model is being called, by whom, at what cost, under which data-access policy, with what audit trail, and with what fallback when quality degrades. A dedicated control plane — analogous to a service mesh or API gateway in cloud-native architecture — is the proposed answer, but it is unclear which vendors have shipped one, which have documented reference architectures, and where the coverage gaps lie. This question directly informs architectural decisions for organisations currently evaluating or operating Microsoft Copilot alongside AWS and developer tools such as Cursor, Codex, and Claude Code.

## Approach

1. **Baseline capability taxonomy** — Define the canonical control-plane capability domains (discoverability, legibility, oversight, logging, security, data access, FinOps, QoS) with a brief definition of each so coverage comparisons are like-for-like.
2. **Vendor product survey** — For each named provider (GitHub Copilot, M365 Copilot, Azure AI Foundry, AWS Bedrock, AWS Agent Core, Cursor, OpenAI Codex, Claude Code), identify what control-plane capabilities are documented in their official product or architecture documentation.
3. **Third-party and open-source control planes** — Search for non-vendor products (e.g. LiteLLM, PortKey, OpenRouter, MLflow AI Gateway, Kong AI Gateway, Apigee AI) that claim multi-provider control-plane coverage; map their claimed capabilities against the taxonomy.
4. **Coverage gap analysis** — Build a capability × provider matrix; identify cells that are absent or undocumented; infer whether the gap is a product gap, a documentation gap, or an architectural limitation.
5. **Design document and reference architecture review** — Locate any published multi-provider AI control-plane reference architectures (vendor or community) and assess completeness against the taxonomy.
6. **Synthesis** — Identify the most complete existing solution, the providers with the weakest control-plane coverage, and the most frequently absent capability domains.

## Sources

- [ ] [Azure AI Foundry documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/) — Microsoft's primary hub for AI project management, model deployment, and governance in Azure
- [ ] [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) — AWS managed foundation model service with guardrails, logging, and access control
- [ ] [AWS Agent Core (Amazon Bedrock Agents)](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) — AWS agentic workflow layer built on Bedrock
- [ ] [GitHub Copilot for Business / Enterprise documentation](https://docs.github.com/en/copilot/github-copilot-enterprise) — GitHub Copilot management, policy, and audit features
- [ ] [Microsoft 365 Copilot admin guide](https://learn.microsoft.com/en-us/microsoft-365-copilot/microsoft-365-copilot-setup) — M365 Copilot deployment, data-access controls, and governance
- [ ] [LiteLLM proxy documentation](https://docs.litellm.ai/docs/proxy/quick_start) — open-source multi-provider AI gateway with budget controls, logging, and access management
- [ ] [PortKey AI Gateway](https://portkey.ai/docs) — commercial multi-provider AI gateway with observability, fallback routing, and cost tracking
- [ ] [Kong AI Gateway](https://docs.konghq.com/gateway/latest/ai-gateway/) — enterprise API gateway with AI-specific plugins for rate limiting, logging, and provider routing
- [ ] [Apigee AI documentation](https://cloud.google.com/apigee/docs) — Google Cloud API management with AI extensions

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

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
