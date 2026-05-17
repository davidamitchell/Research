---
review_count: 2
title: "Amazon Bedrock AgentCore and related suite: full feature and capability survey"
added: 2026-05-17T10:17:56+00:00
status: completed
priority: high
blocks: [2026-05-17-aws-bedrock-capabilities]
tags: [aws, agentic-ai, ai-platform, enterprise, agent-tooling, ai-governance, regulated-enterprise, identity, memory-system, observability, control-plane]
ai_themes: [agentic-ai, tools-infrastructure, governance-policy, memory-context, mlops-deployment]
started: 2026-05-17T12:32:18+00:00
completed: 2026-05-17T12:53:38+00:00
output: [knowledge]
cites: [2026-04-26-ai-agent-control-plane-architecture-enterprise, 2026-04-26-ai-agent-identity-access-management-enterprise, 2026-04-26-multi-ai-provider-control-planes, 2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model]
related: [2026-04-22-enterprise-ai-platform-operating-models, 2026-04-22-enterprise-ai-capability-model, 2026-05-02-vendor-lock-in-portability-multi-platform-ai]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: f5464c79c21398a8fbaccbd65ecc7b65c7914cc7
    changed: 2026-05-17
    progress: progress/2026-05-17-aws-bedrock-agentcore-suite-capabilities.md
    summary: "Initial completion"
---

# Amazon Bedrock AgentCore and related suite: full feature and capability survey

## Research Question

What is the complete set of features, functions, and capabilities offered by Amazon Bedrock AgentCore and its related suite, including AgentCore Gateway, AgentCore Memory, AgentCore Identity, and the Strands Agents Software Development Kit (SDK), and how do those capabilities support the deployment and operation of production Artificial Intelligence (AI) agents at enterprise scale in a regulated environment?

## Scope

**In scope:**
- Amazon Bedrock AgentCore runtime, what it provides for hosting and managing production AI agent workloads
- AgentCore Gateway, tool and Application Programming Interface (API) access management for agents, tool registry, permissions model
- AgentCore Memory, agent memory persistence, memory types (semantic, episodic, procedural), memory retrieval mechanisms
- AgentCore Identity, OAuth 2.0 / OpenID Connect (OIDC) flows for agent authentication and authorisation, identity delegation model
- AgentCore observability and debugging, tracing, logging, evaluation integration
- Strands Agents SDK, open-source agent framework, relationship to AgentCore runtime, supported orchestration patterns
- Amazon Bedrock AgentCore Code Interpreter, capability, security model, use cases
- Pricing, packaging, and General Availability (GA) vs preview status for each component
- Regulatory and compliance implications for agent identity and memory persistence in financial services

**Out of scope:**
- Amazon Bedrock core services (Knowledge Bases, Guardrails, Flows, model access), covered in the separate Amazon Web Services (AWS) Bedrock capabilities research item
- General AWS Lambda, Amazon Elastic Container Service (ECS), or infrastructure not specific to AgentCore
- Non-AWS agent frameworks (LangChain, AutoGen, CrewAI) except for brief comparison to Strands Agents

**Constraints:** Amazon Bedrock AgentCore was announced at AWS re:Invent season in May 2025; many components launched in preview; note GA vs preview status for every capability; use publicly available AWS documentation, blog posts, and announcements.

## Context

- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-multi-ai-provider-control-planes.html] Prior completed repository work already argues that enterprise agent platforms need explicit control-plane, machine-identity, and observability surfaces above the agent framework itself.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html; https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/] AgentCore matters because AWS is productizing those missing runtime surfaces as modular services that sit alongside, rather than inside, a single managed agent abstraction.
- [fact; source: https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/; https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/] AWS announced AgentCore in preview in May 2025 and moved the core service family to General Availability on 2025-10-13, so this item distinguishes launch-stage claims from current documented capability.

## Approach

1. What is the AgentCore runtime and what production agent management capabilities does it provide?
   1a. How does the AgentCore runtime differ from standard Bedrock Agents for hosting agent workloads?
   1b. What scaling, isolation, and lifecycle management capabilities are included?
2. What does AgentCore Gateway provide for tool and API access management for agents?
   2a. How is the tool registry structured and how are permissions enforced?
   2b. What tool types are supported (Representational State Transfer (REST) APIs, Model Context Protocol (MCP) servers, Lambda functions, etc.)?
3. What does AgentCore Memory provide for agent memory persistence?
   3a. What memory types are supported (semantic, episodic, procedural)?
   3b. How is memory indexed, retrieved, and expired?
   3c. What data residency and privacy controls apply to persisted agent memory?
4. What does AgentCore Identity provide for agent authentication and authorisation?
   4a. What OAuth 2.0 / OIDC flows are supported for agent-to-tool and agent-to-agent authentication?
   4b. How does identity delegation work for multi-agent chains?
5. What observability, monitoring, and debugging capabilities does the AgentCore suite provide?
6. What is the Strands Agents SDK and how does it relate to AgentCore at runtime?
7. What are the pricing, packaging, and access model for AgentCore components?
8. What is the current GA vs preview boundary for each AgentCore component, and what is the expected GA timeline?

## Sources

- [x] [AWS News Blog (2025) Introducing Amazon Bedrock AgentCore: Securely deploy and operate AI agents at any scale](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/) - launch announcement, preview positioning, and original component descriptions
- [x] [AWS What's New (2025) Amazon Bedrock AgentCore is now generally available](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/) - GA boundary and post-preview capability additions
- [x] [AWS Documentation What is Amazon Bedrock AgentCore?](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) - canonical suite overview
- [x] [AWS Documentation Host agent or tools with Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) - runtime capabilities, execution model, protocols, and security properties
- [x] [AWS Documentation File system configurations for AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-filesystem-configurations.html) - persistent storage modes and preview boundary for managed session storage
- [x] [AWS Documentation Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) - gateway purpose, target conversion, authentication, and semantic tool selection
- [x] [AWS Documentation Fine-grained access control for Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-fine-grained-access-control.html) - JSON Web Token (JWT), AWS Identity and Access Management (IAM), interceptor, and parameter-level access controls
- [x] [AWS Documentation AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) - memory service overview and use cases
- [x] [AWS Documentation AgentCore Memory types](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html) - short-term and long-term memory mechanics
- [x] [AWS Documentation AgentCore Memory organization](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html) - actor, session, namespace, and IAM scoping
- [x] [AWS Documentation Encrypt your Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html) - memory encryption and customer responsibilities
- [x] [AWS Documentation AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) - identity service overview
- [x] [AWS Documentation Features of AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html) - workload identities, token vault, and OAuth support
- [x] [AWS Documentation Authenticate and authorize with Inbound Auth and Outbound Auth](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html) - runtime inbound and outbound auth model
- [x] [AWS Documentation Obtain OAuth 2.0 access token](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-authentication.html) - user federation, machine-to-machine, and refresh token handling
- [x] [AWS Documentation AgentCore Identity data protection](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-protection.html) - AWS Key Management Service (KMS), logging, and free-form-field warnings
- [x] [AWS Documentation AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) - dashboarding, OpenTelemetry (OTEL) export, and CloudWatch integration
- [x] [AWS Documentation AgentCore generated observability data](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-service-provided.html) - metrics, spans, and logs by resource type
- [x] [AWS Documentation Amazon Bedrock AgentCore Browser](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-tool.html) - browser runtime, live view, session replay, and security model
- [x] [AWS Documentation Amazon Bedrock AgentCore Code Interpreter](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html) - sandbox execution, languages, file limits, and long-running sessions
- [x] [AWS Documentation Policy in Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) - policy enforcement using Cedar, a language for writing authorization policies
- [x] [AWS Documentation AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) - registry scope, approval workflow, and MCP access
- [x] [AWS Pricing Amazon Bedrock AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/) - pricing, included usage, and preview notes
- [x] [AWS Documentation Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) - baseline managed agent abstraction for comparison
- [x] [AWS Documentation Amazon Bedrock Agents memory](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-memory.html) - baseline Bedrock Agents memory model for comparison
- [x] [Model Context Protocol official documentation index](https://modelcontextprotocol.io/) - authoritative definition of Model Context Protocol (MCP)
- [x] [Agent2Agent Protocol official documentation](https://a2aproject.github.io/A2A/latest/) - authoritative definition of Agent to Agent (A2A)
- [x] [Firecracker microVM Lightweight virtual machines](https://firecracker-microvm.github.io/) - authoritative definition of lightweight virtual machine (microVM)
- [x] [Cedar documentation Welcome to the Cedar policy language](https://docs.cedarpolicy.com/) - authoritative definition of Cedar as an authorization policy language
- [x] [Strands Agents GitHub sdk-python README](https://github.com/strands-agents/sdk-python) - SDK capabilities and model/provider support
- [x] [Research (2026) AI agent control-plane architecture](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html) - prior repository synthesis on control-plane needs
- [x] [Research (2026) AI agent identity and access management model](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html) - prior repository synthesis on machine identity and delegation
- [x] [Research (2026) Multi-provider AI control planes](https://davidamitchell.github.io/Research/research/2026-04-26-multi-ai-provider-control-planes.html) - prior repository synthesis on cross-provider runtime governance gaps
- [x] [Research (2026) Vendor-agnostic enterprise AI capability model](https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html) - prior repository synthesis positioning AgentCore inside AWS enterprise capability coverage
- [ ] [AWS YouTube Amazon Web Services channel](https://www.youtube.com/user/AmazonWebServices) - seeded pointer to session recordings; not consulted because the official documentation set was sufficient for this item

## Related

- [AI agent control-plane architecture](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html)
- [AI agent identity and access management model](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html)
- [Multi-provider AI control planes](https://davidamitchell.github.io/Research/research/2026-04-26-multi-ai-provider-control-planes.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: identify the full Amazon Bedrock AgentCore capability set, including runtime, Gateway, Memory, Identity, Observability, Browser, Code Interpreter, Policy, Registry, and the relationship to the Strands Agents SDK, then assess how well that suite supports enterprise production agents in regulated settings.
- Scope: current public AWS documentation and announcement material, plus the Strands Agents primary repository and relevant completed repository syntheses.
- Constraints: prefer primary AWS sources; distinguish preview from GA; treat regulatory implications as bounded architecture implications rather than legal advice.
- Output: knowledge, with executive summary, key findings, evidence map, assumptions, analysis, risks, and open questions.
- Prior work checked: [AI agent control-plane architecture](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html); [AI agent identity and access management model](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html); [Multi-provider AI control planes](https://davidamitchell.github.io/Research/research/2026-04-26-multi-ai-provider-control-planes.html); [Vendor-agnostic enterprise AI capability model](https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html).

### §1 Question Decomposition

1. **Suite boundary**
   1. Which services are part of the documented AgentCore family?
   2. Which adjacent capabilities remain preview or ancillary rather than core?
2. **Runtime**
   1. What execution, scaling, protocol, isolation, and lifecycle features does Runtime provide?
   2. How does Runtime differ from standard Amazon Bedrock Agents?
3. **Gateway and Policy**
   1. What targets can Gateway expose?
   2. How are discovery, authentication, and fine-grained authorization enforced?
4. **Memory**
   1. What short-term and long-term memory types exist?
   2. How are memory records organized, retrieved, encrypted, and governed?
   3. What retention or expiry behavior is documented?
5. **Identity**
   1. What identity primitives exist for agents?
   2. Which OAuth 2.0 flows support user-delegated and autonomous access?
   3. How are refresh tokens and audit signals handled?
6. **Observability and built-in tools**
   1. What metrics, traces, logs, and dashboards are available?
   2. What do Browser and Code Interpreter add to runtime capability?
7. **Strands relationship**
   1. What does Strands provide as a framework?
   2. Is Strands required, optional, or strategically preferred with AgentCore?
8. **Commercial and operational fit**
   1. How is each component priced?
   2. What is GA versus preview today?
   3. Which control surfaces matter most for regulated-enterprise deployment?

### §2 Investigation

- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html; https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/; https://github.com/strands-agents/sdk-python] Primary sources consulted in this run were AWS documentation, AWS announcement pages, AWS pricing pages, and the Strands Agents primary repository; completed repository items were used only as secondary synthesis context.

#### A. Suite boundary and release status

- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html] The current AgentCore developer guide describes a modular suite that includes Runtime, Memory, Gateway, Identity, Code Interpreter, Browser, Observability, Payments, Evaluations, Policy, and Registry.
- [fact; source: https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/; https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/] AWS announced AgentCore in preview in May 2025 and states that Amazon Bedrock AgentCore became generally available on 2025-10-13.
- [fact; source: https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/] At GA, AWS says AgentCore services gained support for Virtual Private Cloud (VPC), AWS PrivateLink, AWS CloudFormation, and resource tagging.
- [fact; source: https://aws.amazon.com/bedrock/agentcore/pricing/; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-filesystem-configurations.html] The pricing and runtime storage pages explicitly mark AWS Agent Registry, AgentCore Optimization recommendations, and managed session storage as preview capabilities.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html; https://aws.amazon.com/bedrock/agentcore/pricing/] The most defensible current boundary is therefore: Runtime, Gateway, Memory, Identity, Observability, Browser, Code Interpreter, Policy, and the basic AgentCore platform are GA, while some adjacent governance and optimization surfaces still retain preview elements.

#### B. Runtime and the difference from Amazon Bedrock Agents

- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html; https://modelcontextprotocol.io/; https://a2aproject.github.io/A2A/latest/] AgentCore Runtime is a secure, serverless hosting environment for arbitrary agent or tool code that supports any framework, any Large Language Model (LLM), Model Context Protocol (MCP), Agent to Agent (A2A), bidirectional streaming, 100 MB payloads, and execution windows up to eight hours.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html; https://firecracker-microvm.github.io/] Runtime isolates each session in a dedicated lightweight virtual machine (microVM) with separate central processing unit (CPU), memory, and filesystem resources, sanitizes memory after session completion, and exposes execution-role credentials only inside that session boundary.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-filesystem-configurations.html] Runtime supports two persistence models: managed session storage, which is isolated per session and currently preview with a 14-day idle expiry, and bring-your-own file systems using Amazon Simple Storage Service (S3) Files or Amazon Elastic File System (EFS), which require VPC connectivity.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html] Amazon Bedrock Agents is a managed agent abstraction that orchestrates action groups, knowledge bases, prompt templates, and traces without requiring customers to host arbitrary runtime infrastructure.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-memory.html] Bedrock Agents memory is session-summary retention attached to the managed agent abstraction, with configurable retention between 1 and 365 days.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents-memory.html] Compared with Amazon Bedrock Agents, AgentCore Runtime is the platform layer for running arbitrary agent code and protocols, while Bedrock Agents remains a more opinionated managed orchestration surface with narrower runtime control but more baked-in orchestration behavior.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html] Runtime can accept either AWS Signature Version 4 (SigV4) or JSON Web Token (JWT) bearer tokens for inbound auth, not both at the same time, and AWS explicitly requires customers to derive delegated user identifiers from the authenticated principal rather than trusting arbitrary client-supplied identifiers.

#### C. Gateway and Policy as the agent-to-tool control surface

- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-supported-targets.html] AgentCore Gateway can expose Hypertext Transfer Protocol (HTTP) targets directly and aggregate MCP targets, while also converting APIs, Lambda functions, and existing services into MCP-compatible tools behind a single gateway endpoint.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-features.html] Gateway includes semantic tool selection, response streaming, MCP sessions, elicitation, sampling, custom encryption, debugging controls, and one-click integrations for several software-as-a-service (SaaS) tools.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-fine-grained-access-control.html] Fine-grained access control is documented at gateway, tool, operation, and parameter level through interceptors, JWT-claims validation, AWS Identity and Access Management (IAM) principal matching, request filtering, and external authorization calls.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html; https://docs.cedarpolicy.com/] Policy in AgentCore uses Cedar, a language for writing authorization policies, plus optional natural-language policy authoring to intercept every Gateway tool call before execution, evaluate the request against a policy engine, and emit monitoring and audit signals through Amazon CloudWatch.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-fine-grained-access-control.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] Gateway plus Policy is the strongest documented AgentCore governance surface because it concentrates tool discovery, authentication, authorization, and interception outside the agent code path, which matches prior control-plane guidance in the repository.

#### D. Memory architecture, governance, and retention implications

- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html] AgentCore Memory separates short-term memory, stored as raw events tied to sessions, from long-term memory, stored as extracted memory records that persist across sessions.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html] AWS documents Memory in short-term and long-term operational categories, not in an explicit semantic, episodic, and procedural taxonomy.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html] Short-term memory is event-based and retrieved through CreateEvent, ListSessions, ListEvents, and GetEvent operations, while long-term memory records are retrieved through GetMemoryRecord, ListMemoryRecords, and semantically ranked RetrieveMemoryRecords.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-strategies.html] Long-term extraction can use built-in strategies, built-in overrides, or self-managed strategies, with self-managed strategies providing the most control over extraction logic, schemas, and namespaces.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html] Memory can be scoped by actor, session, strategy, and namespace, and AWS documents IAM conditions that restrict retrieval to exact namespace or namespace-path hierarchies.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/data-encryption.html] Memories support AWS Key Management Service (KMS) encryption with either service-managed or customer-managed keys, while AWS also states that memory poisoning and prompt-injection defenses remain customer responsibilities.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html] Event metadata is useful for retrieval filtering but AWS explicitly says it is not meant to hold sensitive content because it is not encrypted with a customer-managed key.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html] AgentCore Memory gives enterprises a more explicit memory architecture than Bedrock Agents memory because it separates raw event capture, extraction strategy, namespace design, and retrieval APIs instead of collapsing memory into one summarization feature.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html] On the pages consulted, AgentCore Memory documents encryption and access scoping but does not document a native retention timer or automatic expiry policy for long-term memory records, so regulated adopters should treat retention and deletion workflow design as an application responsibility unless newer service-level controls are documented later.

#### E. Identity, delegation, and credential management

- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html] AgentCore Identity creates centralized workload identities for agents, stores OAuth 2.0 tokens and API keys in a token vault, and supports both customer-managed and service-managed KMS encryption for credentials.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idps.html] AWS documents native support for OAuth 2.0 authorization code grant for user-delegated access, OAuth 2.0 client credentials grant for machine-to-machine flows, and built-in providers for services such as GitHub, Slack, Salesforce, Google, and Microsoft.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-authentication.html] Runtime can invoke external services on behalf of users or autonomously, and AgentCore automatically stores refresh tokens when providers return them, then silently renews access tokens until the refresh token expires or is invalidated.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-use-cases.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-identity-metrics.html] AWS explicitly positions Identity for user-delegated and autonomous enterprise scenarios, and emits metrics and spans that distinguish user federation from machine-to-machine flow usage.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-protection.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html] AWS warns customers not to place sensitive identifying information into free-form fields, recommends CloudTrail and KMS controls, and notes that user-to-session mapping and delegated user-identifier derivation remain customer implementation responsibilities.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] Identity is the feature that most clearly moves AgentCore toward regulated-enterprise readiness because it treats the agent as a first-class workload identity while preserving explicit user-consent flows for delegated access, which aligns with the repository's prior machine-identity guidance.

#### F. Observability, Browser, and Code Interpreter

- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-service-provided.html] AgentCore Observability stores telemetry in Amazon CloudWatch, exports OpenTelemetry (OTEL)-compatible data, and provides default metrics for agents, Gateway, Memory, Policy, Identity, Payments, and built-in tools, with spans and logs available for some resources.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html] For runtime-hosted agents, AWS documents a CloudWatch generative AI observability dashboard with trace visualization, custom span graphs, error breakdowns, and downloadable metrics, spans, and logs.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-tool.html] The Browser tool provides isolated browser sessions, live view, WebSocket control, configurable timeouts from 15 minutes to eight hours, CloudTrail logging, and session replay stored in Amazon Simple Storage Service (S3) for custom browsers.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html] Code Interpreter provides sandboxed execution for Python, JavaScript, and TypeScript, supports inline uploads up to 100 MB and S3-backed uploads up to 5 GB, and exposes long-running sessions up to eight hours.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-tool.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html] Browser and Code Interpreter make AgentCore materially broader than a routing or orchestration layer because they add managed execution substrates for web automation and computation that can be governed and observed with the same control stack.

#### G. Strands Agents SDK relationship

- [fact; source: https://github.com/strands-agents/sdk-python] Strands Agents is an open-source, model-driven SDK that supports multiple model providers, built-in MCP integration, Python-defined tools, streaming, and multi-agent patterns.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html] AWS documentation consistently lists Strands Agents as one of several frameworks that can run on AgentCore rather than as a required authoring layer.
- [inference; source: https://github.com/strands-agents/sdk-python; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html] Strands is complementary to AgentCore: Strands supplies the agent-programming abstraction and local developer ergonomics, while AgentCore supplies deployment, identity, tool-governance, memory, and observability surfaces for production operation.

#### H. Pricing and packaging

- [fact; source: https://aws.amazon.com/bedrock/agentcore/pricing/] Runtime, Browser, and Code Interpreter use active-consumption pricing with separate CPU and gigabyte-hour rates, so compute idle time during I/O wait is not billed as if the workload were pinned to a pre-allocated instance.
- [fact; source: https://aws.amazon.com/bedrock/agentcore/pricing/] Gateway is priced per MCP operation, semantic-search call, and indexed tools; Memory is priced per short-term event, long-term stored record, and long-term retrieval call; Identity is priced per token or API-key request only when it is not already used through Runtime or Gateway.
- [fact; source: https://aws.amazon.com/bedrock/agentcore/pricing/] Observability is billed through Amazon CloudWatch ingestion, storage, and query charges, while Policy charges per authorization request and per 1,000 natural-language input tokens processed for Cedar policy generation.
- [fact; source: https://aws.amazon.com/bedrock/agentcore/pricing/] Registry has a free tier and is marked preview on the pricing page, and Optimization recommendations are also marked preview and free during preview.
- [inference; source: https://aws.amazon.com/bedrock/agentcore/pricing/] The commercial model is intentionally modular: AWS is pricing AgentCore as separable control surfaces rather than as one bundled platform license, which lowers entry cost but makes full-fleet cost modeling dependent on real usage patterns across multiple services.

#### I. Regulated-environment implications

- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html; https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/] AgentCore now supports VPC and PrivateLink deployment patterns, and AWS recommends least-privilege IAM, explicit session-to-user mappings, and careful scoping of execution-role credentials inside the microVM.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-protection.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html] AWS explicitly frames AgentCore under the shared-responsibility model, recommends CloudTrail, KMS, Transport Layer Security (TLS), and sensitive-data hygiene, and says prompt injection and memory poisoning must be mitigated by the customer.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html] Memory design choices such as actor identifiers, namespace hierarchy, metadata usage, and retrieval permissions directly affect privacy segmentation and auditability because those fields determine how user context is partitioned and retrieved.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] For financial-services or similarly regulated environments, AgentCore provides most of the required technical control surfaces, but compliance readiness still depends on the customer's own design for consent propagation, memory retention, classification-aware prompting, approval workflows, and audit review.

### §3 Reasoning

- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html; https://aws.amazon.com/bedrock/agentcore/pricing/] AWS documentation and pricing pages were treated as definitive for the existence, scope, and commercial model of each service component.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html] The runtime-versus-Bedrock-Agents distinction is an inference from documented scope: one surface hosts arbitrary agent code and protocols, while the other manages a predefined orchestration abstraction.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html] The memory-retention gap conclusion is intentionally narrow and applies only to the public pages consulted here, not to undocumented service behavior.
- [assumption; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-protection.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] "Regulated environment" is treated in this item as an enterprise that needs least privilege, auditability, encryption governance, network isolation, and retention control, because those are the recurring technical control surfaces across AWS guidance and prior repository synthesis.

### §4 Consistency Check

- [fact; source: https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/; https://aws.amazon.com/bedrock/agentcore/pricing/; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-filesystem-configurations.html] Status boundary resolved: core AgentCore services are documented as GA from 2025-10-13, while Registry, Optimization recommendations, and managed session storage remain preview on the current pages consulted.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html] Memory claims were narrowed to what AWS documents explicitly, namely event storage, extracted records, namespace control, and encryption behavior, without claiming undocumented retention timers for long-term memory.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-authentication.html] Identity claims were checked for flow consistency, and the final synthesis distinguishes runtime inbound auth mode selection from downstream outbound OAuth 2.0 token retrieval.

### §5 Depth and Breadth Expansion

- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-fine-grained-access-control.html] **Technical lens:** AgentCore's architecture is strongest when Runtime, Gateway, Identity, and Observability are combined, because each one closes a different operational gap in production agent deployment.
- [inference; source: https://aws.amazon.com/bedrock/agentcore/pricing/] **Economic lens:** The modular pricing model reduces initial adoption friction, but it can also hide total platform cost if enterprises treat observability, memory, tool search, and evaluation traffic as negligible overhead.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-protection.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html] **Regulatory lens:** Identity and memory are the two surfaces most likely to trigger compliance review because they determine consent scope, token custody, user-context persistence, and whether sensitive fields enter logs or metadata.
- [fact; source: https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/; https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/] **Historical lens:** AWS moved quickly from a preview framing around missing production infrastructure to a GA framing around private networking, infrastructure-as-code, and enterprise deployment automation.
- [inference; source: https://github.com/strands-agents/sdk-python; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html] **Behavioural lens:** AWS is intentionally steering developers toward an open-framework ecosystem, with Strands as a prominent example, while reserving the more defensible operational and governance surfaces for AgentCore itself.

### §6 Synthesis

**Executive summary:**

Amazon Bedrock AgentCore is a production-agent platform layer that adds runtime isolation, tool governance, machine identity, memory services, and operational observability around arbitrary agent code rather than replacing agent frameworks with a single managed abstraction. [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html] The suite's core services, Runtime, Gateway, Memory, Identity, Observability, Browser, Code Interpreter, and Policy, are documented as generally available from 2025-10-13, while Registry, Optimization recommendations, and managed session storage remain preview on the current public pages. [fact; source: https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/; https://aws.amazon.com/bedrock/agentcore/pricing/; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-filesystem-configurations.html] For regulated enterprises, AgentCore directly covers runtime isolation, workload identity, tool authorization, observability, and private-network deployment, but it does not remove customer responsibility for consent mapping, retention policy, sensitive-data hygiene, and policy design. [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-protection.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html; https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/]

**Key findings:**

1. **Amazon Bedrock AgentCore is best understood as an execution and control-plane layer for arbitrary agent code, because Runtime hosts any framework and model while Amazon Bedrock Agents remains a narrower managed orchestration abstraction.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)
2. **AgentCore Runtime provides lightweight virtual machine (microVM) session isolation, eight-hour execution windows, protocol support for MCP and A2A, persistent storage options, streaming, and built-in auth hooks for hosted agent workloads.** ([fact]; medium confidence; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-filesystem-configurations.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html; https://firecracker-microvm.github.io/)
3. **Gateway plus Policy function as the suite's tool-governance surface, because AWS documents target translation, semantic tool discovery, interceptor-based authorization, and Cedar, a language for writing authorization policies, as the pre-execution policy layer at the agent-to-tool boundary.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-fine-grained-access-control.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html; https://docs.cedarpolicy.com/)
4. **AWS documents AgentCore Memory as short-term event memory plus long-term extracted records, not as an explicit semantic, episodic, and procedural taxonomy, and that design is still more operationally explicit than Bedrock Agents memory because it separates event capture, extraction strategy, namespace scoping, retrieval, and encryption choices.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents-memory.html)
5. **AgentCore Identity gives agents first-class workload identities, supports both user-delegated and autonomous OAuth 2.0 patterns, and automatically manages refresh-token reuse, which makes it the suite capability most directly aligned with regulated-enterprise machine-identity requirements.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-authentication.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html)
6. **Observability, Browser, and Code Interpreter move AgentCore beyond pure orchestration into managed operational infrastructure, because AWS couples trace and metric collection with isolated browser automation and sandboxed code execution under the same control stack.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-service-provided.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-tool.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html)
7. **Strands Agents is optional rather than mandatory, and its open-source authoring model pairs naturally with AgentCore because AWS positions AgentCore as a runtime and governance substrate for Strands and other frameworks alike.** ([inference]; medium confidence; source: https://github.com/strands-agents/sdk-python; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)
8. **The current GA boundary covers the core service family but not every adjacent surface, because AWS documents core AgentCore as GA while still marking Registry, Optimization recommendations, and managed session storage as preview.** ([fact]; medium confidence; source: https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/; https://aws.amazon.com/bedrock/agentcore/pricing/; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-filesystem-configurations.html)
9. **For financial-services-style deployments, AgentCore provides most required technical controls but still leaves critical governance work to the customer, especially around delegated-user mapping, memory-retention policy, sensitive-field handling, and approval logic.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-protection.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] AgentCore is a platform layer around arbitrary agent code, while Bedrock Agents is a managed orchestration abstraction. | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html | Medium | Comparison bounded to documented product scope |
| [fact] Runtime provides lightweight virtual machine (microVM) isolation, long execution windows, protocol support, persistence options, streaming, and built-in auth hooks. | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-filesystem-configurations.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html; https://firecracker-microvm.github.io/ | Medium | Directly documented by AWS plus definition source |
| [inference] Gateway plus Policy function as the suite's tool-governance surface through tool discovery, translation, and pre-execution authorization using Cedar, a language for writing authorization policies. | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-fine-grained-access-control.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html; https://docs.cedarpolicy.com/ | Medium | Higher-level synthesis from direct product docs |
| [inference] AWS documents AgentCore Memory as short-term plus long-term operational memory, not as semantic, episodic, and procedural labels, and that design is more explicit than Bedrock Agents memory. | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents-memory.html | Medium | Comparison bounded to docs consulted |
| [inference] Identity provides workload identities, user-delegated and autonomous OAuth 2.0 flows, and refresh-token handling in a pattern closely aligned with regulated-enterprise machine identity needs. | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-authentication.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html | Medium | Alignment judgment is inferential |
| [inference] Observability, Browser, and Code Interpreter move the suite into managed operational infrastructure. | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-tool.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html | Medium | Higher-level synthesis from component docs |
| [inference] Strands is optional rather than mandatory, and its open-source authoring model pairs naturally with AgentCore. | https://github.com/strands-agents/sdk-python; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html | Medium | Optionality is direct; pairing is inferential |
| [fact] Core AgentCore is GA, but Registry, Optimization recommendations, and managed session storage remain preview. | https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/; https://aws.amazon.com/bedrock/agentcore/pricing/; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-filesystem-configurations.html | Medium | Current status boundary |
| [inference] Regulated deployments still require customer-owned governance design around consent, retention, and sensitive-data handling. | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-protection.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html | Medium | Technical-control inference, not legal advice |

**Assumptions:**

- [assumption; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-protection.html] This item treats "regulated environment" as a technical-control question about identity, audit, encryption, network isolation, and retention, because AWS documentation addresses those controls directly while not providing legal compliance determinations.
- [assumption; source: https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/; https://aws.amazon.com/bedrock/agentcore/pricing/] This item treats the current public documentation set as the operative truth for service availability, even if additional private roadmap information exists outside the public pages.

**Analysis:**

AWS is not presenting AgentCore as one more agent framework. [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html] It is presenting AgentCore as the missing operating layer that lets teams keep their preferred framework while AWS supplies the harder production surfaces: runtime isolation, token custody, tool gateways, and telemetry. [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html; https://github.com/strands-agents/sdk-python] A plausible rival interpretation is that Amazon Bedrock Agents already covers production needs, but that interpretation fits only when a team is comfortable with the managed orchestration model and does not need arbitrary frameworks, external-model flexibility, or a first-class Gateway and Identity layer. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html] A remaining limitation is customer work at the governance boundary: AWS gives the building blocks, yet the customer still has to define who may delegate to whom, how long memory should persist, and what fields may safely enter metadata, prompts, or logs. [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-protection.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html]

**Risks, gaps, uncertainties:**

- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html] The current public Memory pages do not provide the same explicit retention-time documentation that Bedrock Agents memory does, so regulated data-lifecycle conclusions remain partly inferential.
- [inference; source: https://aws.amazon.com/bedrock/agentcore/pricing/; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-filesystem-configurations.html] Preview surfaces such as Registry, Optimization recommendations, and managed session storage could change materially before their eventual GA behavior and pricing settle.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html] Because execution-role credentials are reachable inside the microVM, runtime security depends heavily on least-privilege role design and trusted code inside the session.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html] Memory poisoning and prompt-injection mitigation remain customer obligations, which means service adoption does not by itself create a complete safety case for autonomous agents.

**Open questions:**

- [inference; source: https://aws.amazon.com/bedrock/agentcore/pricing/] When Registry and Optimization reach GA, will AWS keep them modular or move toward a more opinionated bundled control-plane offering?
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html] Will AWS add explicit long-term memory retention and expiry controls comparable to the documented retention window in Bedrock Agents memory?
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html] How much of the delegated-identity and approval model can be standardized across multi-agent chains without forcing application teams back into custom orchestration code?

### §7 Recursive Review

- Review result: pass
- Acronym audit: passed for AI, SDK, API, OIDC, GA, REST, MCP, LLM, A2A, VPC, JWT, IAM, OTEL, S3, EFS, KMS, CPU, and SaaS
- Claim-label audit: all visible claims in `## Research Skill Output` labeled or written as metadata fragments
- Cross-item check: prior completed items on control plane, identity, and AWS capability positioning cited with URL-backed links
- Synthesis parity check: Findings seeded directly from this section without substantive divergence

---

## Findings

### Executive Summary

Amazon Bedrock AgentCore is a production-agent platform layer that adds runtime isolation, tool governance, machine identity, memory services, and operational observability around arbitrary agent code rather than replacing agent frameworks with a single managed abstraction. [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html] The suite's core services, Runtime, Gateway, Memory, Identity, Observability, Browser, Code Interpreter, and Policy, are documented as generally available from 2025-10-13, while Registry, Optimization recommendations, and managed session storage remain preview on the current public pages. [fact; source: https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/; https://aws.amazon.com/bedrock/agentcore/pricing/; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-filesystem-configurations.html] For regulated enterprises, AgentCore directly covers runtime isolation, workload identity, tool authorization, observability, and private-network deployment, but it does not remove customer responsibility for consent mapping, retention policy, sensitive-data hygiene, and policy design. [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-protection.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html; https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/]

### Key Findings

1. **Amazon Bedrock AgentCore is best understood as an execution and control-plane layer for arbitrary agent code, because Runtime hosts any framework and model while Amazon Bedrock Agents remains a narrower managed orchestration abstraction.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)
2. **AgentCore Runtime provides lightweight virtual machine (microVM) session isolation, eight-hour execution windows, protocol support for MCP and A2A, persistent storage options, streaming, and built-in auth hooks for hosted agent workloads.** ([fact]; medium confidence; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-filesystem-configurations.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html; https://firecracker-microvm.github.io/)
3. **Gateway plus Policy function as the suite's tool-governance surface, because AWS documents target translation, semantic tool discovery, interceptor-based authorization, and Cedar, a language for writing authorization policies, as the pre-execution policy layer at the agent-to-tool boundary.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-fine-grained-access-control.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html; https://docs.cedarpolicy.com/)
4. **AWS documents AgentCore Memory as short-term event memory plus long-term extracted records, not as an explicit semantic, episodic, and procedural taxonomy, and that design is still more operationally explicit than Bedrock Agents memory because it separates event capture, extraction strategy, namespace scoping, retrieval, and encryption choices.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents-memory.html)
5. **AgentCore Identity gives agents first-class workload identities, supports both user-delegated and autonomous OAuth 2.0 patterns, and automatically manages refresh-token reuse, which makes it the suite capability most directly aligned with regulated-enterprise machine-identity requirements.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-authentication.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html)
6. **Observability, Browser, and Code Interpreter move AgentCore beyond pure orchestration into managed operational infrastructure, because AWS couples trace and metric collection with isolated browser automation and sandboxed code execution under the same control stack.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-service-provided.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-tool.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html)
7. **Strands Agents is optional rather than mandatory, and its open-source authoring model pairs naturally with AgentCore because AWS positions AgentCore as a runtime and governance substrate for Strands and other frameworks alike.** ([inference]; medium confidence; source: https://github.com/strands-agents/sdk-python; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)
8. **The current GA boundary covers the core service family but not every adjacent surface, because AWS documents core AgentCore as GA while still marking Registry, Optimization recommendations, and managed session storage as preview.** ([fact]; medium confidence; source: https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/; https://aws.amazon.com/bedrock/agentcore/pricing/; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-filesystem-configurations.html)
9. **For financial-services-style deployments, AgentCore provides most required technical controls but still leaves critical governance work to the customer, especially around delegated-user mapping, memory-retention policy, sensitive-field handling, and approval logic.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-protection.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] AgentCore is a platform layer around arbitrary agent code, while Bedrock Agents is a managed orchestration abstraction. | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html | Medium | Comparison bounded to documented product scope |
| [fact] Runtime provides lightweight virtual machine (microVM) isolation, long execution windows, protocol support, persistence options, streaming, and built-in auth hooks. | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-filesystem-configurations.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html; https://firecracker-microvm.github.io/ | Medium | Directly documented by AWS plus definition source |
| [inference] Gateway plus Policy function as the suite's tool-governance surface through tool discovery, translation, and pre-execution authorization using Cedar, a language for writing authorization policies. | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-fine-grained-access-control.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html; https://docs.cedarpolicy.com/ | Medium | Higher-level synthesis from direct product docs |
| [inference] AWS documents AgentCore Memory as short-term plus long-term operational memory, not as semantic, episodic, and procedural labels, and that design is more explicit than Bedrock Agents memory. | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents-memory.html | Medium | Comparison bounded to docs consulted |
| [inference] Identity provides workload identities, user-delegated and autonomous OAuth 2.0 flows, and refresh-token handling in a pattern closely aligned with regulated-enterprise machine identity needs. | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-authentication.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html | Medium | Alignment judgment is inferential |
| [inference] Observability, Browser, and Code Interpreter move the suite into managed operational infrastructure. | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-tool.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html | Medium | Higher-level synthesis from component docs |
| [inference] Strands is optional rather than mandatory, and its open-source authoring model pairs naturally with AgentCore. | https://github.com/strands-agents/sdk-python; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html | Medium | Optionality is direct; pairing is inferential |
| [fact] Core AgentCore is GA, but Registry, Optimization recommendations, and managed session storage remain preview. | https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/; https://aws.amazon.com/bedrock/agentcore/pricing/; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-filesystem-configurations.html | Medium | Current status boundary |
| [inference] Regulated deployments still require customer-owned governance design around consent, retention, and sensitive-data handling. | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-protection.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html | Medium | Technical-control inference, not legal advice |

### Assumptions

- [assumption; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-protection.html] This item treats "regulated environment" as a technical-control question about identity, audit, encryption, network isolation, and retention, because AWS documentation addresses those controls directly while not providing legal compliance determinations.
- [assumption; source: https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/; https://aws.amazon.com/bedrock/agentcore/pricing/] This item treats the current public documentation set as the operative truth for service availability, even if additional private roadmap information exists outside the public pages.

### Analysis

AWS is not presenting AgentCore as one more agent framework. [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html] It is presenting AgentCore as the missing operating layer that lets teams keep their preferred framework while AWS supplies the harder production surfaces: runtime isolation, token custody, tool gateways, and telemetry. [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html; https://github.com/strands-agents/sdk-python] A plausible rival interpretation is that Amazon Bedrock Agents already covers production needs, but that interpretation fits only when a team is comfortable with the managed orchestration model and does not need arbitrary frameworks, external-model flexibility, or a first-class Gateway and Identity layer. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html] The more important limitation is not missing runtime capability but the remaining customer work at the governance boundary: AWS gives the building blocks, yet the customer still has to define who may delegate to whom, how long memory should persist, and what fields may safely enter metadata, prompts, or logs. [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-protection.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html]

### Risks, Gaps, and Uncertainties

- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html] The current public Memory pages do not provide the same explicit retention-time documentation that Bedrock Agents memory does, so regulated data-lifecycle conclusions remain partly inferential.
- [inference; source: https://aws.amazon.com/bedrock/agentcore/pricing/; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-filesystem-configurations.html] Preview surfaces such as Registry, Optimization recommendations, and managed session storage could change materially before their eventual GA behavior and pricing settle.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html] Because execution-role credentials are reachable inside the microVM, runtime security depends heavily on least-privilege role design and trusted code inside the session.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html] Memory poisoning and prompt-injection mitigation remain customer obligations, which means service adoption does not by itself create a complete safety case for autonomous agents.

### Open Questions

- [inference; source: https://aws.amazon.com/bedrock/agentcore/pricing/] When Registry and Optimization reach GA, will AWS keep them modular or move toward a more opinionated bundled control-plane offering?
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html] Will AWS add explicit long-term memory retention and expiry controls comparable to the documented retention window in Bedrock Agents memory?
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html] How much of the delegated-identity and approval model can be standardized across multi-agent chains without forcing application teams back into custom orchestration code?

---

## Output

- Type: knowledge
- Description: Amazon Bedrock AgentCore provides a mostly complete AWS-native operating layer for production AI agents, but regulated deployments still depend on customer-owned identity, retention, and governance design choices. [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-protection.html]
- Links:
  - https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
  - https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html
  - https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/
