---
title: "How Do Enterprise AI Maturity Frameworks Map onto the LLM Consumption Ladder?"
added: 2026-08-13T18:27:40+00:00
status: backlog
priority: high
blocks: []
themes: [agentic-ai, tools-infrastructure, governance-policy]
started: ~
completed: ~
output: [knowledge]
cites: []
related: []
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# How Do Enterprise AI Maturity Frameworks Map onto the LLM Consumption Ladder?

## Research Question

How do theoretical frameworks of enterprise AI / generative AI maturity map onto the observed, practice-driven progression of large language model (LLM) consumption strategies — from reliance on a single frontier model and its proprietary harness, through subscription services with manual selection and managed multi-model platforms (e.g., Amazon Bedrock, Microsoft Foundry), to dynamic task-based model routing, self-hosted open-weight models, fine-tuning of those models, and ultimately owned-hardware inference — and what organizational, economic, technical, and governance factors drive (or inhibit) transitions across these stages?

**Supporting sub-questions:**

1. To what extent do existing maturity models (organizational capability stages) predict or explain the specific technical consumption ladder of LLM usage?
2. What empirical evidence from production systems demonstrates cost, quality, latency, compliance, or risk trade-offs at each transition point?
3. How do dynamic routing mechanisms and hybrid architectures function as bridging practices between managed platforms and full self-hosting?
4. Under what conditions do organizations reverse or hybridize stages (e.g., retain frontier models for certain workloads while self-hosting others)?
5. What gaps exist between theoretical prescriptions for "AI future-ready" or "scale" maturity and the operational realities of model ownership, fine-tuning pipelines, and on-premises inference?

## Scope

**In scope:**
- Theoretical maturity models for generative AI / foundation-model adoption (MIT CISR (Center for Information Systems Research), AWS, Gartner, Forrester, Deloitte, McKinsey, academic IS literature)
- Technical LLM consumption ladder: single-API → managed multi-model platforms → dynamic routing → self-hosted open-weight → fine-tuned → owned-hardware inference
- Dynamic model routing and cascade mechanisms as bridging practices
- Organizational, economic, technical, and governance factors driving stage transitions
- TCO (Total Cost of Ownership) analyses, production case studies, practitioner post-mortems
- Sector-specific evidence: healthcare, finance, software engineering, regulated industries
- Negative cases: organizations remaining on single-frontier or pure managed platforms
- Hybrid / reverse-stage patterns

**Out of scope:**
- Non-generative / pre-LLM AI systems and their maturity models (except where directly compared)
- Hardware design and fabrication specifics
- Inference optimization below the deployment-strategy level (kernel-level, quantization internals)

**Constraints:**
- Primary focus on English-language literature and practitioner sources
- Evidence weight toward 2023–2026 (fast-moving field; older sources valid for foundational frameworks only)
- No primary data collection (interviews, surveys) unless publicly available transcripts or reports exist

## Context

Enterprises adopting large language models face a heterogeneous strategy landscape: some remain API consumers of a single frontier model; others orchestrate dozens of models dynamically across managed platforms or self-hosted infrastructure. Maturity-model frameworks from consulting firms and cloud vendors prescribe staged progressions, but whether those prescriptions map onto observed practice — and what actually drives transitions — is poorly documented. Understanding this mapping is decision-critical for AI leads, platform engineers, and enterprise architects choosing infrastructure strategy.

## Approach

**A mixed-methods design spanning framework analysis, systematic literature review, and case study reconstruction:**

1. **Map the theoretical landscape** — inventory maturity-model frameworks (MIT CISR (Center for Information Systems Research), AWS Prescriptive Guidance, Gartner Hype Cycle / Maturity models, Forrester Wave, Deloitte, McKinsey) and extract their stage definitions, transition criteria, and capability descriptors.

2. **Define the empirical consumption ladder** — synthesize practitioner accounts and production reports into a working taxonomy of LLM consumption strategies (stages, entry criteria, exit signals).

3. **Cross-map theory to practice** — for each maturity-model stage, identify which consumption-ladder position(s) it predicts or implies; surface gaps and mismatches.

4. **Analyze transition factors** — for each rung of the consumption ladder, gather evidence on cost (TCO (Total Cost of Ownership)), quality, latency, compliance, and risk trade-offs from production deployments, benchmark studies, and analyst reports.

5. **Examine routing and hybrid architectures** — survey dynamic routing literature (LLM (Large Language Model) cascade, task-based routing classifiers, Universal Model Routing, LLMRank) and production routing systems (LiteLLM, OpenRouter, Not Diamond, Amazon Bedrock Intelligent Prompt Routing) as bridging mechanisms.

6. **Identify sector-specific and boundary cases** — collect evidence from healthcare, finance, and regulated industries where data-sovereignty or latency constraints force earlier movement to self-hosting or fine-tuning; document organizations that remained on managed platforms and why.

7. **Assess agentic and continual-adaptation frontiers** — review emerging literature on mixture-of-models, agentic orchestration, and post-training / continual-learning that reframes what "model ownership" means at the capability level.

## Sources

**Theory / Framework side:**
- MIT CISR Enterprise AI Maturity Model (Weill, Woerner, Sebastian et al., 2024–2025): https://cisr.mit.edu/
- AWS Prescriptive Guidance — Maturity model for adopting generative AI: https://docs.aws.amazon.com/prescriptive-guidance/latest/generative-ai-maturity/introduction.html
- Moslem & Kelleher, "Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey" (arXiv 2603.04445): https://arxiv.org/abs/2603.04445
- IDC FutureScape projections on multi-tool / dynamic model routing adoption: https://www.idc.com/

**Practice / Evidence side:**
- Amazon Bedrock Intelligent Prompt Routing documentation: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Microsoft Azure AI Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/
- LiteLLM open-source routing documentation: https://docs.litellm.ai/
- Menlo Ventures State of Enterprise AI reports: https://menlovc.com/
- a16z AI enterprise spend surveys: https://a16z.com/

## Research Skill Output

<!-- To be populated during research execution -->

## Findings

<!-- To be populated during research execution -->
