---
title: "AWS Bedrock: full feature and capability survey"
added: 2026-05-17T10:17:56+00:00
status: backlog
priority: high
blocks: []
tags: [aws, agentic-ai, ai-platform, enterprise, llm, rag, ai-governance, regulated-enterprise, evaluation]
started: ~
completed: ~
output: [knowledge]
cites: []
related: [2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model, 2026-04-26-multi-ai-provider-control-planes, 2026-04-26-ai-agent-control-plane-architecture-enterprise]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# AWS Bedrock: full feature and capability survey

## Research Question

What is the complete set of features, functions, and capabilities offered by Amazon Web Services (AWS) Bedrock — including its model access, agent building, knowledge bases, guardrails, evaluation, and governance services — and how do those capabilities support enterprise Artificial Intelligence (AI) at scale in a regulated environment?

## Scope

**In scope:**
- Bedrock foundation model (FM) access: model catalogue, on-demand and provisioned throughput, cross-region inference
- Bedrock Agents: agent building, action groups, orchestration, inline agents, multi-agent collaboration
- Bedrock Knowledge Bases: Retrieval-Augmented Generation (RAG) pipeline, data source connectors, vector store options, chunking strategies, query rewriting
- Bedrock Guardrails: content filtering, topic denial, sensitive information redaction, hallucination grounding checks
- Bedrock Model Customisation: fine-tuning, continued pre-training, model distillation
- Bedrock Data Automation: document, image, video, and audio processing pipelines
- Bedrock Flows: visual workflow builder for AI pipelines
- Bedrock Prompt Management and prompt caching
- Bedrock Model Evaluation: automated and human evaluation jobs
- Bedrock Model Invocation Logging and observability
- Security and compliance: Virtual Private Cloud (VPC) endpoints, AWS Identity and Access Management (IAM), encryption, compliance certifications
- Pricing model, throughput options, and cost management tooling
- Limitations and known gaps requiring compensating controls

**Out of scope:**
- Amazon Bedrock AgentCore and related suite (covered in a separate research item)
- AWS SageMaker capabilities beyond their integration surface with Bedrock
- Specific third-party model performance benchmarks (model selection, not benchmarking, is in scope)

**Constraints:** Focus on generally available features as of mid-2025; note preview/in-preview features explicitly; use publicly available AWS documentation and announcements.

## Context

Amazon Bedrock is AWS's managed foundation model service, providing access to a catalogue of models from Amazon and third parties alongside a suite of tools for building and operating AI applications. It is the primary AWS surface for enterprise AI workloads. Understanding its complete capability set — including recent additions like Bedrock Flows, Data Automation, and multi-agent collaboration — informs enterprise AI architecture decisions, multi-cloud strategy, and vendor evaluation for regulated environments.

## Approach

1. What foundation models are available in Bedrock and through what access mechanisms?
   1a. What first-party (Amazon) and third-party models are in the catalogue?
   1b. What throughput and access options exist (on-demand, provisioned, cross-region inference)?
2. What agent-building capabilities does Bedrock Agents provide?
   2a. How are agents defined, what action group types are supported, and how is orchestration handled?
   2b. What multi-agent collaboration patterns are supported?
3. What knowledge management and Retrieval-Augmented Generation (RAG) capabilities are in Bedrock Knowledge Bases?
   3a. What data sources, vector stores, and chunking/retrieval strategies are available?
   3b. What query rewriting, reranking, and metadata filtering capabilities exist?
4. What safety, content filtering, and governance features do Bedrock Guardrails provide?
5. What model customisation options are available (fine-tuning, continued pre-training, distillation)?
6. What workflow and automation capabilities exist in Bedrock Flows and Bedrock Data Automation?
7. What evaluation, observability, and cost management features are built in?
8. What security, compliance, and enterprise access controls are available, and which regulated-industry certifications apply?

## Sources

- [ ] [AWS Bedrock documentation](https://docs.aws.amazon.com/bedrock/) — official product documentation and feature reference
- [ ] [AWS Bedrock product page](https://aws.amazon.com/bedrock/) — product overview and capability summary
- [ ] [AWS Bedrock Guardrails documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) — guardrails feature documentation
- [ ] [AWS Bedrock Agents documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) — agents feature documentation
- [ ] [AWS re:Invent and re:Inforce 2024–2025 Bedrock announcements](https://aws.amazon.com/blogs/aws/) — latest feature releases and roadmap signals

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

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

### Open Questions

---

## Output

- Type: knowledge
- Description:
- Links:
