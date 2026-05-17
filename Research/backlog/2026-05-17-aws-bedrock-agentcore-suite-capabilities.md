---
title: "Amazon Bedrock AgentCore and related suite: full feature and capability survey"
added: 2026-05-17T10:17:56+00:00
status: backlog
priority: high
blocks: [2026-05-17-aws-bedrock-capabilities]
tags: [aws, agentic-ai, ai-platform, enterprise, agent-tooling, ai-governance, regulated-enterprise, identity, memory-system, observability]
started: ~
completed: ~
output: [knowledge]
cites: []
related: [2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model, 2026-04-26-ai-agent-control-plane-architecture-enterprise, 2026-04-26-ai-agent-identity-access-management-enterprise, 2026-04-26-multi-ai-provider-control-planes]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Amazon Bedrock AgentCore and related suite: full feature and capability survey

## Research Question

What is the complete set of features, functions, and capabilities offered by Amazon Bedrock AgentCore and its related suite — including AgentCore Gateway, AgentCore Memory, AgentCore Identity, and the Strands Agents Software Development Kit (SDK) — and how do those capabilities support the deployment and operation of production Artificial Intelligence (AI) agents at enterprise scale in a regulated environment?

## Scope

**In scope:**
- Amazon Bedrock AgentCore runtime: what it provides for hosting and managing production AI agent workloads
- AgentCore Gateway: tool and Application Programming Interface (API) access management for agents, tool registry, permissions model
- AgentCore Memory: agent memory persistence, memory types (semantic, episodic, procedural), memory retrieval mechanisms
- AgentCore Identity: OAuth 2.0 / OpenID Connect (OIDC) flows for agent authentication and authorisation, identity delegation model
- AgentCore observability and debugging: tracing, logging, evaluation integration
- Strands Agents SDK: open-source agent framework, relationship to AgentCore runtime, supported orchestration patterns
- Amazon Bedrock AgentCore Code Interpreter: capability, security model, use cases
- Pricing, packaging, and General Availability (GA) vs preview status for each component
- Regulatory and compliance implications for agent identity and memory persistence in financial services

**Out of scope:**
- Amazon Bedrock core services (Knowledge Bases, Guardrails, Flows, model access) — covered in the separate AWS Bedrock capabilities research item
- General AWS Lambda, Amazon Elastic Container Service (ECS), or infrastructure not specific to AgentCore
- Non-AWS agent frameworks (LangChain, AutoGen, CrewAI) except for brief comparison to Strands SDK

**Constraints:** Amazon Bedrock AgentCore was announced at AWS re:Invent May 2025; many components may be in preview; note GA vs preview status for every capability; use publicly available AWS documentation, blog posts, and announcements.

## Context

Amazon Bedrock AgentCore is a new production-focused runtime and services suite for deploying AI agents at enterprise scale. It extends the Bedrock platform with dedicated infrastructure for agent identity, memory, tool access management, and runtime observability — capabilities that are not covered by the core Bedrock Agents service. Understanding AgentCore's full capability set is essential for enterprise AI architecture decisions, particularly for organisations evaluating AWS as their primary agent deployment platform and assessing whether AgentCore addresses the operational gaps identified in existing agent deployment patterns.

## Approach

1. What is the AgentCore runtime and what production agent management capabilities does it provide?
   1a. How does the AgentCore runtime differ from standard Bedrock Agents for hosting agent workloads?
   1b. What scaling, isolation, and lifecycle management capabilities are included?
2. What does AgentCore Gateway provide for tool and Application Programming Interface (API) access management for agents?
   2a. How is the tool registry structured and how are permissions enforced?
   2b. What tool types are supported (REST APIs, Model Context Protocol/MCP servers, Lambda functions, etc.)?
3. What does AgentCore Memory provide for agent memory persistence?
   3a. What memory types are supported (semantic, episodic, procedural)?
   3b. How is memory indexed, retrieved, and expired?
   3c. What data residency and privacy controls apply to persisted agent memory?
4. What does AgentCore Identity provide for agent authentication and authorisation?
   4a. What OAuth 2.0 / OpenID Connect (OIDC) flows are supported for agent-to-tool and agent-to-agent authentication?
   4b. How does identity delegation work for multi-agent chains?
5. What observability, monitoring, and debugging capabilities does the AgentCore suite provide?
6. What is the Strands Agents Software Development Kit (SDK) and how does it relate to AgentCore at runtime?
7. What are the pricing, packaging, and access model for AgentCore components?
8. What is the current General Availability (GA) vs preview boundary for each AgentCore component, and what is the expected GA timeline?

## Sources

- [ ] [AWS — Introducing Amazon Bedrock AgentCore (blog post, May 2025)](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore/) — primary announcement with capability overview
- [ ] [Amazon Bedrock AgentCore documentation](https://docs.aws.amazon.com/bedrock-agentcore/) — official technical documentation (may be limited at time of research)
- [ ] [Strands Agents SDK GitHub repository](https://github.com/strands-agents/sdk-python) — open-source SDK code and documentation
- [ ] [AWS re:Invent 2025 AgentCore session recordings](https://www.youtube.com/user/AmazonWebServices) — detailed technical presentations

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
