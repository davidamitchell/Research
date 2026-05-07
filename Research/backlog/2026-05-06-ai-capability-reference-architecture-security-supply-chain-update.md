---
title: "Integrating 2026-05 security and supply chain findings into the enterprise AI capability reference architecture"
added: 2026-05-06T12:12:52+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, enterprise, capability-model, ai-governance, security, supply-chain, sbom, evaluation, reference-architecture]
started: ~
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites:
  - 2026-04-22-enterprise-ai-capability-model
  - 2026-04-26-ai-agent-control-plane-architecture-enterprise
  - 2026-04-26-ai-lowcode-governance-enforcement-architecture
  - 2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain
  - 2026-04-22-ai-governance-assurance-change-control-verification
  - 2026-05-02-meta-analysis-standards-and-ai-skill-evaluation
  - 2026-05-06-aibom-sbom-conceptual-gaps-theory
  - 2026-05-06-aibom-schema-design-standards-alignment
  - 2026-05-06-aibom-identity-delegation-trust-theory
  - 2026-05-06-aibom-runtime-generation-divergence-theory
  - 2026-02-28-ai-control-testing-and-assurance
  - 2026-04-30-explainable-ai-xai-regulation-governance
related:
  - 2026-05-05-enterprise-ai-capability-stack
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []
---

# Integrating 2026-05 security and supply chain findings into the enterprise Artificial Intelligence capability reference architecture

## Research Question

How should the enterprise Artificial Intelligence (AI) ecosystem capability reference architecture (as expressed in `2026-04-22-enterprise-ai-capability-model` and the `2026-05-05-enterprise-ai-capability-stack` Knowledge synthesis) be revised and extended to incorporate findings from the 2026-05 research cycle on: Software Bill of Materials (SBOM) and Artificial Intelligence Bill of Materials (AIBOM) conceptual gaps and schema design; AI supply chain risk and runtime composition integrity; the enterprise AI security threat model covering prompt injection, Retrieval-Augmented Generation (RAG)-based attacks and model supply chain compromise; automated governance assurance and change-control verification; and AI evaluation frameworks?

## Scope

**In scope:**
- Gap analysis: which capability domains in the existing reference architecture are absent or underspecified relative to the 2026-05 completed items
- SBOM/AIBOM integration: how AI Bill of Materials concepts (provenance graph, runtime divergence, identity and attribution, schema standards alignment) fit into the architecture as first-class supply-chain capabilities
- Supply chain risk layer: where in the layered architecture supply-chain integrity controls belong, how they interact with the model registry, artifact promotion pipelines, and runtime observation
- Security threat model integration: mapping the security capabilities (prompt injection defense, RAG poisoning controls, model supply chain compromise mitigations, data exfiltration guards) to specific architectural layers and control surfaces
- Governance assurance integration: how automated change-control verification and governance gating fit into the delivery pipeline and control-plane components
- Evaluation capability integration: how AI skill evaluation and meta-analysis standards inform the observability and quality-gate layers of the architecture
- Revised architectural diagram (component list and layering) and updated capability ownership recommendations

**Out of scope:**
- Implementation guidance for specific vendor products
- Original research into supply chain standards (rely on already-completed items)
- Cost modelling or tooling selection for individual capability domains

**Constraints:**
- Must build on and extend (not replace) the existing reference architecture in `2026-04-22-enterprise-ai-capability-model` and the `2026-05-05-enterprise-ai-capability-stack` Knowledge item
- All claims must cite the completed 2026-05 items or their primary sources; no new primary research required
- Output must be a revised Knowledge item (or versioned amendment to the existing `enterprise-ai-capability-stack` synthesis) — do not duplicate content already in source items

## Context

The enterprise AI ecosystem capability reference architecture was established in April 2026 across `2026-04-22-enterprise-ai-capability-model` and extended by the `2026-05-05-enterprise-ai-capability-stack` synthesis. That architecture defines a five-layer stack: data and knowledge, model and inference, orchestration, delivery and platform engineering, and operating model. Since then, a significant body of research has been completed — covering SBOM/AIBOM conceptual gaps, schema design, runtime generation divergence, supply-chain integrity, the enterprise AI security threat model, automated governance assurance, and AI evaluation standards — none of which are reflected in the architecture. Without this update, the reference architecture will be cited without the security, supply-chain, and governance controls that the more recent evidence demands, creating a risk that architectural decisions reference an outdated and incomplete model.

## Approach

1. **Gap mapping:** Read the existing reference architecture (`2026-04-22-enterprise-ai-capability-model`, `2026-05-05-enterprise-ai-capability-stack`) and the newly completed items. For each completed item, list: (a) which capability domain it informs, (b) which architectural layer it belongs to, and (c) whether a gap currently exists in the architecture.

2. **SBOM/AIBOM capability integration:** Using `2026-05-06-aibom-sbom-conceptual-gaps-theory`, `2026-05-06-aibom-schema-design-standards-alignment`, `2026-05-06-aibom-identity-delegation-trust-theory`, and `2026-05-06-aibom-runtime-generation-divergence-theory`, determine the minimum AIBOM capability set (provenance graph generation, schema-conformant output, runtime-divergence detection, identity and attribution tracking) that must appear as explicit architectural components.

3. **Supply chain risk layer:** Using `2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain` and `2026-02-28-ai-control-testing-and-assurance`, establish where supply-chain integrity controls (model registry signing, artifact lineage, trojan weight detection, supply-chain audit) belong in the architecture and how they interact with the delivery pipeline layer.

4. **Security capability integration:** Map the security capabilities from `2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain` (prompt injection defense, RAG poisoning controls, exfiltration guards, runtime monitoring) to specific architectural layers, filling gaps against the existing control-surface architecture in `2026-04-26-ai-lowcode-governance-enforcement-architecture`.

5. **Governance assurance integration:** Using `2026-04-22-ai-governance-assurance-change-control-verification` and `2026-04-30-explainable-ai-xai-regulation-governance`, determine how automated change-control verification, explainability requirements, and regulatory evidence generation fit into the control-plane and delivery-pipeline components.

6. **Evaluation capability integration:** Using `2026-05-02-meta-analysis-standards-and-ai-skill-evaluation`, identify which evaluation and quality-gate capabilities are absent from the architecture and where they should be inserted (model evaluation gates, quality benchmarks, systematic review processes for AI outputs).

7. **Synthesis:** Produce an updated architectural component list (layers, components, ownership), a revised layered diagram, and delta findings showing what has changed from the prior version. Record as a versioned amendment to `2026-05-05-enterprise-ai-capability-stack` or as a new Knowledge item (decide based on the scope of change).

## Sources

- [Enterprise AI capability model (2026)](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-capability-model.md) — establishes the five-layer reference architecture and capability domains
- [Enterprise capability stack for sustainable multi-provider AI (2026)](https://github.com/davidamitchell/Research/blob/main/Knowledge/2026-05-05-enterprise-ai-capability-stack.md) — current synthesis baseline to be extended
- [SBOM/AIBOM conceptual gaps theory (2026)](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-06-aibom-sbom-conceptual-gaps-theory.md) — defines the provenance graph abstraction and why traditional SBOM fails for agentic workloads
- [AIBOM schema design and standards alignment (2026)](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-06-aibom-schema-design-standards-alignment.md) — identifies standards (CycloneDX, SPDX) and schema design decisions for AI-specific Bill of Materials
- [AIBOM identity delegation and trust theory (2026)](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-06-aibom-identity-delegation-trust-theory.md) — attribution and identity tracking for multi-agent provenance
- [AIBOM runtime generation and divergence theory (2026)](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-06-aibom-runtime-generation-divergence-theory.md) — gap between declared and runtime composition in agentic AI systems
- [Enterprise AI security threat model (2026)](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.md) — security capabilities for prompt injection, RAG-based attacks, model supply chain compromise, and data exfiltration
- [AI control testing and assurance (2026)](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-ai-control-testing-and-assurance.md) — control testing approaches and assurance patterns
- [Automated governance assurance and change-control verification (2026)](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-ai-governance-assurance-change-control-verification.md) — automated governance gating and change-control verification patterns
- [Explainable Artificial Intelligence regulation and governance (2026)](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-explainable-ai-xai-regulation-governance.md) — XAI requirements and regulatory intersection
- [Meta-analysis standards and AI skill evaluation (2026)](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-meta-analysis-standards-and-ai-skill-evaluation.md) — evaluation frameworks and quality standards for AI outputs

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Restate the research question. Confirm scope, constraints, and output format.

-

### §1 Question Decomposition

Approach sub-questions broken into atomic questions — each answerable with a single evidence-based claim.

-

### §2 Investigation

Evidence gathered per atomic question. Label each claim: **[fact]**, **[inference]**, or **[assumption]** with source.

-

### §3 Reasoning

Facts, inferences, and assumptions explicitly separated. No unsupported generalisations or narrative leaps.

-

### §4 Consistency Check

Internal contradictions identified and resolved (or explicitly flagged where unresolvable).

-

### §5 Depth and Breadth Expansion

Findings re-examined through relevant lenses (technical, regulatory, economic, historical, behavioural).

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

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

### Key Findings

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: knowledge
- Description: Revised enterprise AI ecosystem capability reference architecture incorporating SBOM/AIBOM supply chain, security threat model, governance assurance, and evaluation capability domains
- Links:
