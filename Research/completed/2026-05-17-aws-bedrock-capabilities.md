---
review_count: 2
title: "Amazon Web Services (AWS) Bedrock platform capabilities: model access, agents, knowledge bases, guardrails, evaluation, and enterprise governance primitives for regulated environments"
added: 2026-05-17T10:17:56+00:00
status: completed
priority: high
blocks: []
themes: [agentic-ai, rag-retrieval, governance-policy, benchmarks-eval, ai-architecture, tools-infrastructure]
started: 2026-05-17T12:58:58+00:00
completed: 2026-05-17T13:20:19+00:00
output: [knowledge]
cites: [2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model, 2026-04-26-multi-ai-provider-control-planes, 2026-04-26-ai-agent-control-plane-architecture-enterprise]
related: [2026-04-26-access-control-amplification-agentic-operations, 2026-05-09-policy-as-code-guardrails-regulatory-ai-governance]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: 2ebb0fa472f4104575976624270b58573c309a42
    changed: 2026-05-17
    progress: progress/2026-05-17-aws-bedrock-capabilities.md
    summary: Initial completion
---

# Amazon Web Services (AWS) Bedrock platform capabilities: model access, agents, knowledge bases, guardrails, evaluation, and enterprise governance primitives for regulated environments

## Research Question

What is the complete set of features, functions, and capabilities offered by Amazon Web Services (AWS) Bedrock, including its model access, agent building, knowledge bases, guardrails, evaluation, and governance services, and how do those capabilities support enterprise Artificial Intelligence (AI) at scale in a regulated environment?

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
- Amazon Bedrock AgentCore and related suite, covered in a separate research item
- AWS SageMaker capabilities beyond their integration surface with Bedrock
- Specific third-party model performance benchmarks, because model selection rather than benchmark scoring is in scope

**Constraints:** Focus on generally available features as of mid-2025, note preview states explicitly, and use publicly available AWS documentation and announcements.

## Context

Amazon Bedrock is AWS's managed foundation model service and exposes model access, knowledge bases, agents, guardrails, evaluation, prompt tooling, and security controls through one managed platform. [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html; https://aws.amazon.com/bedrock/]

Current AWS product and user-guide material present Bedrock as the main managed generative-AI build surface inside AWS, which makes its capability boundaries important for enterprise architecture and regulated-environment design. [inference; source: https://aws.amazon.com/bedrock/; https://docs.aws.amazon.com/bedrock/latest/userguide/security.html; https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html]

## Approach

1. What foundation models are available in Bedrock and through what access mechanisms?
   1a. What first-party (Amazon) and third-party models are in the catalogue?
   1b. What throughput and access options exist, including on-demand, provisioned, and cross-region inference?
2. What agent-building capabilities does Bedrock Agents provide?
   2a. How are agents defined, what action group types are supported, and how is orchestration handled?
   2b. What multi-agent collaboration patterns are supported?
3. What knowledge management and Retrieval-Augmented Generation (RAG) capabilities are in Bedrock Knowledge Bases?
   3a. What data sources, vector stores, and chunking and retrieval strategies are available?
   3b. What query rewriting, reranking, and metadata filtering capabilities exist?
4. What safety, content filtering, and governance features do Bedrock Guardrails provide?
5. What model customisation options are available, including fine-tuning, continued pre-training, and distillation?
6. What workflow and automation capabilities exist in Bedrock Flows and Bedrock Data Automation?
7. What evaluation, observability, and cost-management features are built in?
8. What security, compliance, and enterprise access controls are available, and which regulated-industry certifications apply?

## Sources

- [x] [AWS Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/) - documentation entry point
- [x] [AWS Amazon Bedrock Product Page](https://aws.amazon.com/bedrock/) - product overview and capability summary
- [x] [AWS Bedrock User Guide: What is Amazon Bedrock?](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) - service overview and supported model families
- [x] [AWS Bedrock User Guide: Models at a glance](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html) - provider and model catalogue
- [x] [AWS Bedrock User Guide: Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) - agent lifecycle and orchestration
- [x] [AWS Bedrock User Guide: Multi-agent collaboration](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html) - supervisor and collaborator model
- [x] [AWS Bedrock User Guide: Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) - RAG capability overview
- [x] [AWS Bedrock User Guide: Knowledge base setup](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html) - vector stores and metadata fields
- [x] [AWS Bedrock User Guide: Knowledge base chunking](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html) - chunking modes and multimodal handling
- [x] [AWS Bedrock User Guide: Configure and customize queries and response generation](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html) - search modes, metadata filters, query decomposition, and prompt customization
- [x] [AWS Bedrock User Guide: Supported models and Regions for Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.html) - embeddings, parsing, reranking, and structured-data support
- [x] [AWS Bedrock User Guide: Use a reranker model in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank-use.html) - reranking support
- [x] [AWS Bedrock User Guide: Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) - filter and safeguard catalog
- [x] [AWS Bedrock User Guide: Automated Reasoning checks](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html) - logic-based verification and limitations
- [x] [AWS Bedrock User Guide: Guardrails enforcements](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-enforcements.html) - organization-level and account-level enforcement
- [x] [AWS Bedrock User Guide: Custom models](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) - supported customization methods
- [x] [AWS Bedrock User Guide: Fine-tuning custom models](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html) - fine-tuning model and Region support
- [x] [AWS Blog (2023) Customize models in Amazon Bedrock with your own data using fine-tuning and continued pre-training](https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/) - launch evidence for continued pre-training
- [x] [AWS Bedrock User Guide: Bedrock Data Automation works](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-how-it-works.html) - document, image, video, and audio automation
- [x] [AWS Bedrock User Guide: Flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html) - workflow builder and deployment model
- [x] [AWS Bedrock User Guide: Flow node types](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html) - supported node types and integrations
- [x] [AWS Bedrock User Guide: Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html) - reusable prompts, variants, and versions
- [x] [AWS Bedrock User Guide: Prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) - cache checkpoints, supported models, and limits
- [x] [AWS What's New (2025) Amazon Bedrock general availability prompt caching](https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-bedrock-general-availability-prompt-caching/) - general availability timing and supported baseline models
- [x] [AWS Bedrock User Guide: Evaluation](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html) - automatic, judge-model, human, and RAG evaluations
- [x] [AWS Bedrock User Guide: Model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) - request, response, and token logging
- [x] [AWS Bedrock User Guide: Inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html) - cross-region routing, usage metrics, and cost tags
- [x] [AWS Bedrock User Guide: Cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) - geographic and global routing trade-offs
- [x] [AWS Bedrock User Guide: Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) - fixed-capacity throughput and custom-model serving
- [x] [AWS Bedrock User Guide: Batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html) - asynchronous offline inference
- [x] [AWS What's New (2024) Amazon Bedrock batch inference at 50% of on-demand price](https://aws.amazon.com/about-aws/whats-new/2024/08/amazon-bedrock-fms-batch-inference-50-price/) - general availability and discount signal
- [x] [AWS Bedrock Security and Compliance](https://aws.amazon.com/bedrock/security-compliance/) - product security and compliance summary
- [x] [AWS Bedrock User Guide: Security](https://docs.aws.amazon.com/bedrock/latest/userguide/security.html) - shared responsibility and security control entry point
- [x] [AWS Bedrock User Guide: Data encryption](https://docs.aws.amazon.com/bedrock/latest/userguide/data-encryption.html) - transport and at-rest encryption with AWS Key Management Service (KMS)
- [x] [AWS Bedrock User Guide: VPC interface endpoints](https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html) - AWS PrivateLink networking and endpoint policies
- [x] [AWS Bedrock User Guide: Protect your data using Amazon VPC and AWS PrivateLink](https://docs.aws.amazon.com/bedrock/latest/userguide/usingVPC.html) - workload-isolation guidance
- [x] [AWS Bedrock User Guide: Compliance validation](https://docs.aws.amazon.com/bedrock/latest/userguide/compliance-validation.html) - compliance-program discovery and audit-report path
- [x] [David Mitchell (2026) Vendor-agnostic enterprise Artificial Intelligence capability model: Microsoft Copilot and GitHub families vs AWS Bedrock ecosystem](https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html) - prior repository synthesis on Bedrock family boundaries
- [x] [David Mitchell (2026) Multi-provider AI control planes: capabilities, vendors, and coverage gaps](https://davidamitchell.github.io/Research/research/2026-04-26-multi-ai-provider-control-planes.html) - prior repository synthesis on Bedrock as runtime layer
- [x] [David Mitchell (2026) What control-plane architecture is required to manage AI agents and low-code systems as distributed, semi-autonomous actors within enterprise environments?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html) - prior repository synthesis on layered governance implications

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: What Bedrock capabilities are publicly documented across model access, agents, knowledge bases, guardrails, customization, workflow tooling, evaluation, observability, security, compliance, pricing, and enterprise governance?
- Scope: Bedrock core service only, excluding AgentCore and broader SageMaker functionality.
- Constraints: Full mode; publicly available AWS documentation and announcements; generally available mid-2025 baseline with later preview surfaces explicitly marked.
- Output: Full structured synthesis with executive summary, key findings, evidence map, assumptions, analysis, risks, and open questions.
- Prior work:
  - [fact; source: https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html] A prior repository comparison concluded that Bedrock is strongest as a modular runtime family but still depends on customer-built governance integration for identity, logging, region policy, and economics.
  - [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-multi-ai-provider-control-planes.html] Prior repository work also treated Bedrock as a strong multi-model operating layer inside AWS rather than a cross-tool enterprise control plane.
  - [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] Prior repository architecture work implies that Bedrock capability breadth should be evaluated both as a runtime stack and as one layer inside a larger enterprise control plane.

### §1 Question Decomposition

- 1. Model access
  - 1.1 Which providers and model families are visible in Bedrock's documented catalogue?
  - 1.2 Which invocation modes exist for interactive, cross-region, provisioned, and batch use?
  - 1.3 Which cost and throughput controls attach to those access modes?
- 2. Agents
  - 2.1 What core components define an agent?
  - 2.2 How do action groups, knowledge bases, prompt templates, traces, versions, and aliases work together?
  - 2.3 What collaboration patterns are documented for multiple agents?
- 3. Knowledge Bases
  - 3.1 What document, multimodal, and structured-data retrieval capabilities are documented?
  - 3.2 Which vector stores, embedding options, chunking modes, search modes, filters, reranking, and query decomposition features are documented?
- 4. Guardrails
  - 4.1 Which input and output safety controls exist?
  - 4.2 Which grounding and verification controls exist?
  - 4.3 What organization-level enforcement or limitation surfaces exist?
- 5. Customisation
  - 5.1 Which custom-model methods are currently documented?
  - 5.2 What evidence exists for continued pre-training within the scoped period?
- 6. Flows and Data Automation
  - 6.1 What workflow-construction capabilities exist in Flows?
  - 6.2 What extraction and processing capabilities exist in Bedrock Data Automation?
- 7. Evaluation, observability, and economics
  - 7.1 Which evaluation modes are documented?
  - 7.2 Which logging and monitoring features are documented?
  - 7.3 Which cost-management controls are documented?
- 8. Security, compliance, and regulated-enterprise fit
  - 8.1 Which networking, IAM, encryption, and audit controls are documented?
  - 8.2 Which compliance statements are explicit?
  - 8.3 Which gaps still require compensating controls?

### §2 Investigation

#### 1. Model access

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html] Bedrock documents access to 100+ foundation models and a catalogue spanning Amazon and multiple third-party providers, including Anthropic, Cohere, DeepSeek, Meta, Mistral AI, MiniMax, Moonshot AI, NVIDIA, OpenAI, Qwen, Stability AI, TwelveLabs, Writer, and Z.AI.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html; https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html] On-demand inference can be routed through inference profiles, which can track usage metrics, apply cost-allocation tags, and distribute requests across one or more Regions.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html] Cross-region inference has two documented routing modes: geographic profiles that keep data within a geography and global profiles that maximize throughput and cost optimization but can route across any supported commercial Region.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html] Provisioned Throughput purchases fixed model capacity through model units and commitment terms, and custom models require Provisioned Throughput to serve inference.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html; https://aws.amazon.com/about-aws/whats-new/2024/08/amazon-bedrock-fms-batch-inference-50-price/] Batch inference is a separate asynchronous path that writes outputs to Amazon Simple Storage Service (Amazon S3), is not supported for provisioned models, and was announced as generally available with select models at 50% of on-demand price.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html; https://aws.amazon.com/bedrock/] Bedrock's model-access surface is broad enough to act as a provider-abstraction layer inside AWS, but individual provider availability and some preview providers are moving targets rather than a stable mid-2025 baseline.

#### 2. Agents

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html] Bedrock Agents are documented as orchestrators that break user requests into steps, collect additional information conversationally, invoke Application Programming Interface (API) actions, and query knowledge bases without customer-managed orchestration infrastructure.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html] The standard agent lifecycle includes action groups or knowledge bases, customizable pre-processing and orchestration prompts, test aliases, traces, versioning, and deployment aliases.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html] Multi-agent collaboration uses a hierarchical supervisor-and-collaborator pattern in which a supervisor agent plans and routes work to collaborator agents in real time.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html] Collaborator agents retain the same core Bedrock agent capabilities, including tools, action groups, knowledge bases, and guardrails, which means multi-agent composition reuses the same governance primitives rather than adding a separate control plane.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] Bedrock's agent surface is strong on runtime orchestration and decomposition inside AWS, but it still sits below the broader enterprise-layer controls described in prior repository architecture work.

#### 3. Knowledge Bases

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html] Knowledge Bases document RAG support for proprietary content, source citations, multimodal queries, structured-database access, reranking, and agent integration.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html; https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.html] Knowledge Bases support both quick-created and customer-managed vector stores, support multiple embedding models, and impose compatibility constraints between embedding dimensions and vector-store choice.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html] Amazon OpenSearch Serverless and Amazon OpenSearch Managed clusters are the only documented vector stores that support binary vectors for Knowledge Bases.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html] Knowledge Bases document default, fixed-size, no-chunking, hierarchical, semantic, and multimodal chunking paths, with semantic chunking incurring additional model cost and multimodal chunking varying by parser and embedding path.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html] Retrieval can use default, hybrid, or semantic search, supports a wide range of metadata-filter operators, and documents implicit metadata filtering generated by a model from a metadata schema.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html; https://docs.aws.amazon.com/bedrock/latest/userguide/rerank-use.html] Knowledge Bases support reranker models and query decomposition, where a complex query is split into smaller sub-queries before response generation.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.html] Knowledge Bases also document structured-data support that turns natural-language requests into database queries, with region-specific availability and explicit notice that cross-region inference can share data across Regions.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html; https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html] Knowledge Bases are one of Bedrock's most enterprise-relevant surfaces because they combine retrieval, citation, filtering, and workflow reuse, but regulated deployments still need careful metadata, vector-store, and region-policy design.

#### 4. Guardrails

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html] Guardrails document content filters, denied topics, word filters, sensitive-information filters, contextual grounding checks, and Automated Reasoning checks.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html] Guardrails can be attached directly to model inference, used through the standalone `ApplyGuardrail` API, or selectively applied to tagged prompt sections through the Software Development Kit (SDK) path.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html] Automated Reasoning checks are generally available in a limited Region set, support English only, add validation latency, and operate in detect mode by returning findings and feedback instead of blocking content by themselves.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-enforcements.html] Guardrails enforcements document organization-level and account-level enforcement through AWS Organizations policies, with the effective control being the union of organization and application guardrails.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-enforcements.html] Guardrails enforcements explicitly exclude Automated Reasoning policies, which means the most advanced logical verification control is not the same as the centrally enforceable cross-account control surface.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-enforcements.html; https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html] Bedrock Guardrails provide a strong native moderation and verification layer, but regulated designs still need external policy logic and logging discipline when the decision must be provably deterministic or centrally enforced across accounts.

#### 5. Model customisation

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html] The current custom-model overview documents three active customization methods: supervised fine-tuning, reinforcement fine-tuning, and distillation.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html] The fine-tuning guide documents explicit model and Region support for Amazon, Anthropic, and Meta models and treats fine-tuning as a managed Bedrock workflow.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html] Distillation is documented as a managed teacher-student workflow in which Bedrock synthesizes responses from a larger teacher model and fine-tunes a smaller student model.
- [fact; source: https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/; https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html] AWS's November 2023 launch post documented continued pre-training for Amazon Titan Text as a public-preview customization path, but the current custom-models overview foregrounds fine-tuning, reinforcement fine-tuning, and distillation instead of a dedicated continued-pre-training guide.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html; https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/] Both the current throughput guide and the launch post align on the point that custom models need Provisioned Throughput for serving.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html; https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html; https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/] Bedrock's customization surface is real and useful, but the continued-pre-training story is less stable in current public documentation than the current fine-tuning and distillation paths, so date-scoping matters.

#### 6. Flows and Bedrock Data Automation

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html] Bedrock Flows document a visual workflow builder with draft, version, and alias lifecycle states for moving from testing to production.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html] Flows include logic nodes such as conditions, iterators, collectors, and do-while loops, plus prompt, agent, knowledge-base, Amazon S3, AWS Lambda, and preview inline-code nodes.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html; https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html] Flows can embed guardrails on prompt and knowledge-base nodes, call Lambda functions, retrieve from Amazon S3, and support asynchronous executions.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/bda-how-it-works.html] Bedrock Data Automation supports document, image, video, and audio inputs and can return either standard output or blueprint-driven custom output.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/bda-how-it-works.html; https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.html] Data Automation also appears inside the Knowledge Bases parsing surface, where the Data Automation parser is documented as preview in US West (Oregon).
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html; https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html; https://docs.aws.amazon.com/bedrock/latest/userguide/bda-how-it-works.html] Together, Flows and Bedrock Data Automation make Bedrock more than a model endpoint catalog by adding native orchestration and multimodal extraction primitives that reduce the amount of custom glue code customers have to build.

#### 7. Evaluation, observability, and economics

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html] Bedrock evaluations support automatic evaluation, human-worker evaluation, judge-model evaluation, and RAG evaluation for Bedrock and non-Bedrock RAG sources.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html] Evaluation jobs support foundation models, marketplace models, customized models, imported models, prompt routers, and models purchased through Provisioned Throughput.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html] Model invocation logging can write request and response bodies, token counts, and metadata to Amazon S3 and Amazon CloudWatch Logs, but it is disabled by default and only covers calls through the `bedrock-runtime` endpoint.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html; https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html] Inference profiles and the product page document cost-allocation tags, CloudWatch usage metrics, and cost-allocation by IAM user and role.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html; https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html; https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-bedrock-general-availability-prompt-caching/] Prompt management adds prompt variants and versions, while prompt caching reduces latency and input-token cost for repeated prompt prefixes and was announced as generally available in April 2025 for a defined baseline model set.
- [fact; source: https://aws.amazon.com/bedrock/pricing/; https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html; https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html] Bedrock pricing documents on-demand, Standard, Flex, Priority, Reserved, batch, prompt-caching, Knowledge Bases, Guardrails, evaluation, Data Automation, and routing-related price surfaces rather than a single flat inference tariff.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html; https://aws.amazon.com/bedrock/pricing/; https://davidamitchell.github.io/Research/research/2026-04-26-multi-ai-provider-control-planes.html] Bedrock gives customers enough primitives to build strong observability and cost governance, but the customer still has to switch them on, choose destinations, define tags, and join the resulting data into one financial and audit view.

#### 8. Security, compliance, and regulated-enterprise fit

- [fact; source: https://aws.amazon.com/bedrock/security-compliance/; https://docs.aws.amazon.com/bedrock/latest/userguide/security.html] AWS states that Bedrock data is not used to train base models, documents the shared-responsibility model, and positions Bedrock as suitable for security-sensitive organizations when configured correctly.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html; https://docs.aws.amazon.com/bedrock/latest/userguide/usingVPC.html] Bedrock supports interface endpoints through AWS PrivateLink for control-plane, runtime, mantle, and agent endpoints, with endpoint policies and private Domain Name System (DNS) support.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/data-encryption.html] Bedrock documents Transport Layer Security (TLS) 1.2 for data in transit and AWS Key Management Service (KMS)-backed encryption for custom models, agents, data-source ingestion jobs, vector stores in OpenSearch, and evaluation jobs.
- [fact; source: https://aws.amazon.com/bedrock/security-compliance/; https://docs.aws.amazon.com/bedrock/latest/userguide/compliance-validation.html] AWS states that Bedrock is in scope for International Organization for Standardization (ISO) certifications, System and Organization Controls (SOC), Cloud Security Alliance (CSA) Security, Trust, Assurance, and Risk (STAR) Level 2, General Data Protection Regulation (GDPR) use, Health Insurance Portability and Accountability Act (HIPAA) eligibility, and Federal Risk and Authorization Management Program (FedRAMP) High in AWS GovCloud, and points customers to AWS Artifact and the services-in-scope list for program-specific verification.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html; https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.html] Cross-region inference and Knowledge Bases both document region-sensitive data movement implications, which means regulated customers have to treat throughput optimization as a policy choice rather than a neutral default.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html; https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html] Bedrock is well equipped for regulated enterprise use, but it is still a shared-responsibility runtime platform, so identity scoping, network isolation, key management, log destinations, budget tagging, and region policy remain customer design tasks rather than automatic Bedrock defaults.

### §3 Reasoning

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html; https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html] The primary evidence base is almost entirely AWS first-party product documentation and launch material, which makes feature-existence claims strong.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html; https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html] Breadth claims about Bedrock as a platform are credible because AWS documents model diversity, region-routing modes, and multiple build-time services in one user-guide family.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/security.html; https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html] Governance-completeness claims are weaker than feature-existence claims because Bedrock exposes primitives for logging, security, and private networking but leaves activation and composition to the customer.
- [assumption; source: https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-bedrock-general-availability-prompt-caching/; https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html] The item treats core capability families as the stable object of analysis even though provider rosters and some preview model listings have moved after mid-2025. Justification: the research question asks for the capability set more than an exact historical provider snapshot.
- [assumption; source: https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/; https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html] The item treats continued pre-training as historically real but currently less prominent because AWS's own older launch material documents it directly while the current custom-model overview emphasizes other methods. Justification: this is the most faithful way to represent the current evidence without claiming a stronger current public position than the docs show.

### §4 Consistency Check

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html; https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html; https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html] The access-mode evidence is internally consistent: inference profiles handle on-demand routing and cross-region scaling, while Provisioned Throughput remains a separate fixed-capacity path.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-enforcements.html] The guardrails evidence is internally consistent: Bedrock has both moderation-style filters and logical verification, but Automated Reasoning is detect-only and excluded from organization-level enforcement.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html] The Knowledge Bases evidence is internally consistent: Bedrock combines multiple chunking strategies, retrieval modes, filters, and response-generation controls without requiring a separate product family.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html] The main tension in the evidence is responsibility allocation, because AWS documents many governance controls while simultaneously making them customer-activated and architecture-dependent.

### §5 Depth and Breadth Expansion

- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html; https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html] Technical lens: Bedrock's strongest differentiator is that its retrieval, orchestration, prompting, guardrails, and evaluation surfaces are documented as composable native services rather than only as isolated APIs.
- [inference; source: https://aws.amazon.com/bedrock/pricing/; https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html; https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html] Economic lens: Bedrock's cost posture is tunable through caching, batch, tiered inference, inference profiles, and model choice, but it is operationally complex enough that cost governance must be designed rather than assumed.
- [inference; source: https://aws.amazon.com/bedrock/security-compliance/; https://docs.aws.amazon.com/bedrock/latest/userguide/compliance-validation.html; https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html] Regulatory lens: Bedrock exposes enough explicit security and compliance material for regulated use, but region-routing options and shared-responsibility boundaries mean evidence of capability does not equal evidence of compliant deployment.
- [inference; source: https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/; https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-bedrock-general-availability-prompt-caching/; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html] Historical lens: the Bedrock surface has expanded from model access and early customization into a broader platform with prompt caching, logical verification, workflow orchestration, and multimodal automation.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-enforcements.html] Behavioural lens: Bedrock encourages disciplined platform engineering only if teams actually enable logging, version prompts and flows, publish immutable guardrail versions, and attach customer governance around those primitives.

### §6 Synthesis

**Executive summary:**

Amazon Bedrock already exposes documented managed capabilities across every major surface examined here: multi-model access, agents, knowledge bases, guardrails, workflow orchestration, evaluation, logging, private networking, and compliance support. Enterprise governance still depends on customer-designed identity architecture, logging destinations, region policy, and cost attribution above those native primitives. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html; https://docs.aws.amazon.com/bedrock/latest/userguide/security.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html]

Bedrock's strongest documented areas are breadth of model access, native orchestration through Agents and Flows, retrieval tooling through Knowledge Bases, and built-in safety layers through Guardrails. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html; https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html; https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html]

The platform also documents several cost and performance levers, including inference profiles, Provisioned Throughput, batch inference, prompt caching, and feature-level pricing. [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html; https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html; https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html; https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html; https://aws.amazon.com/bedrock/pricing/]

For a regulated environment, Bedrock's controls work best as powerful primitives that still require customer policy choices around AWS Identity and Access Management (IAM) scope, Virtual Private Cloud networking, key management, data residency, and unified audit evidence. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html; https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html; https://docs.aws.amazon.com/bedrock/latest/userguide/data-encryption.html; https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html; https://davidamitchell.github.io/Research/research/2026-04-26-multi-ai-provider-control-planes.html]

**Key findings:**

1. **Amazon Bedrock documents access to 100+ foundation models from Amazon, Anthropic, AI21 Labs, Cohere, DeepSeek, Luma AI, Meta, Mistral AI, poolside, Stability AI, and Writer, plus separate on-demand, cross-region, provisioned, and batch serving paths that let enterprises tune throughput, routing, and commitment levels for different workloads.** ([fact]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html; https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html; https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html; https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html)
2. **Bedrock Agents provide a managed orchestration surface with action groups, knowledge-base integration, prompt customization, traces, aliases, and hierarchical multi-agent collaboration, which places substantial orchestration capability inside the Bedrock service boundary instead of leaving it entirely to customer-built code.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html)
3. **Knowledge Bases combine retrieval, citation, structured-data access, customer-managed vector databases for embedding storage, document chunking modes that split source text before indexing, reranking models that reorder retrieved results, query decomposition that breaks complex questions into sub-queries, and metadata-aware search inside one managed Bedrock feature family for enterprise information retrieval.** ([fact]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html; https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html; https://docs.aws.amazon.com/bedrock/latest/userguide/rerank-use.html)
4. **Bedrock Guardrails cover moderation, sensitive-data handling, grounding, and logic-based verification, and the centrally enforceable organization-level guardrail surface stops short of Automated Reasoning checks.** ([fact]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-enforcements.html)
5. **Bedrock's current customization story is strongest for supervised fine-tuning, reinforcement fine-tuning, and distillation, while continued pre-training is clearly evidenced in AWS launch material but is less prominent in the current public custom-model documentation, so it should be treated as date-sensitive rather than as a stable headline capability.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html; https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html; https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/)
6. **Flows and Bedrock Data Automation extend Bedrock beyond direct model invocation by adding native workflow logic, service integrations, and multimodal extraction surfaces that customers can use in place of some custom orchestration code.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html; https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html; https://docs.aws.amazon.com/bedrock/latest/userguide/bda-how-it-works.html)
7. **Bedrock includes meaningful built-in evaluation, logging, and cost-management primitives, including automatic and human evaluations, invocation logging, prompt caching, inference-profile tagging, and feature-level pricing, and those controls become governance evidence only after the customer enables and joins them operationally.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html; https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html; https://aws.amazon.com/bedrock/pricing/)
8. **For regulated enterprises, Bedrock fits best as a strong AWS-native AI runtime and control surface, while enterprise governance still depends on customer-built identity, network, region, and audit architecture above Bedrock's native capabilities.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html; https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html; https://docs.aws.amazon.com/bedrock/latest/userguide/data-encryption.html; https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html; https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html; https://davidamitchell.github.io/Research/research/2026-04-26-multi-ai-provider-control-planes.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Bedrock exposes provider choice across Amazon, Anthropic, AI21 Labs, Cohere, DeepSeek, Luma AI, Meta, Mistral AI, poolside, Stability AI, and Writer, plus multiple serving modes. | https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html; https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html; https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html; https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html | medium | Core platform and serving docs agree. |
| [inference] Bedrock Agents place substantial orchestration capability inside the Bedrock service boundary. | https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html | medium | Feature set supports the orchestration interpretation. |
| [fact] Knowledge Bases combine retrieval, citation, structured-data access, customer-managed vector databases for embedding storage, document chunking modes, reranking models, query decomposition, and metadata-aware search inside one managed feature family. | https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html; https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html; https://docs.aws.amazon.com/bedrock/latest/userguide/rerank-use.html | medium | Retrieval, filtering, and tuning surfaces are all documented. |
| [fact] Guardrails combine moderation and logical verification, and the organization-enforcement surface excludes Automated Reasoning. | https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-enforcements.html | medium | Strong direct documentation. |
| [inference] Customization is current and useful, but continued pre-training is more date-sensitive than fine-tuning or distillation. | https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html; https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html; https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/ | medium | Older launch evidence plus current docs. |
| [inference] Flows and Bedrock Data Automation can replace some custom orchestration code with native workflow and multimodal extraction primitives. | https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html; https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html; https://docs.aws.amazon.com/bedrock/latest/userguide/bda-how-it-works.html | medium | Product docs show the primitives; the code-reduction claim is interpretive. |
| [inference] Evaluation, logging, and cost controls are substantial but customer-activated. | https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html; https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html; https://aws.amazon.com/bedrock/pricing/ | medium | Features are explicit; activation burden is interpretive. |
| [inference] Bedrock is a strong runtime and control surface, but not a complete enterprise governance plane by itself. | https://docs.aws.amazon.com/bedrock/latest/userguide/security.html; https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html; https://docs.aws.amazon.com/bedrock/latest/userguide/data-encryption.html; https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html; https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html; https://davidamitchell.github.io/Research/research/2026-04-26-multi-ai-provider-control-planes.html | medium | Prior repository synthesis sharpens the governance interpretation. |

**Assumptions:**

- [assumption; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html; https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-bedrock-general-availability-prompt-caching/] The capability families are the stable object of analysis, even though the exact provider roster and preview model lineup moved after mid-2025. Justification: the question asks what Bedrock can do, not for a frozen vendor census.
- [assumption; source: https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/; https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html] Continued pre-training should be treated as historically evidenced but currently less foregrounded. Justification: that is the narrowest statement consistent with both the older launch material and the current overview page.

**Analysis:**

AWS documents Bedrock as one managed stack that combines model access, orchestration, retrieval, safety, and evaluation. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html; https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html; https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html]

That makes Bedrock stronger than a bare model marketplace for platform engineering, but the security and governance evidence still looks like a shared-responsibility toolkit rather than a self-completing governance solution. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html]

The prior repository comparison and control-plane research remain compatible with this reading: Bedrock is strong enough to anchor an AWS-native runtime layer, yet the enterprise still needs identity standards, network policy, audit aggregation, and economic governance above that layer. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html; https://davidamitchell.github.io/Research/research/2026-04-26-multi-ai-provider-control-planes.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html]

An alternative interpretation is that an all-AWS estate could treat Bedrock plus surrounding AWS services as a sufficient governance plane. That interpretation is plausible for narrow estates, but the shared-responsibility and customer-activation evidence makes it too broad for a general regulated-enterprise conclusion. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html]

The platform's operational trade-off is therefore favorable for enterprises that want rich native primitives and are willing to assemble them carefully, but less favorable for teams expecting one turnkey governance plane that automatically normalizes every identity, region, and audit choice. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html; https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html; https://docs.aws.amazon.com/bedrock/latest/userguide/security.html; https://aws.amazon.com/bedrock/security-compliance/]

**Risks, gaps, uncertainties:**

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html; https://aws.amazon.com/bedrock/] The current Bedrock provider list includes post-mid-2025 additions and preview surfaces, so exact provider breadth should be date-qualified when making historical comparisons.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-enforcements.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html] Automated Reasoning checks do not currently map cleanly onto the organization-level enforcement surface, which creates a real distinction between verification depth and central policy rollout.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/security.html] A customer can easily overestimate Bedrock's governance completeness if they read feature availability as evidence that logging, retention, and audit correlation are already fully configured.
- [inference; source: https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/; https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html] The continued-pre-training story has lower confidence than the other major surfaces because the strongest direct evidence is older launch material rather than a prominent current guide.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html; https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.html] Cross-region performance features can pull against data-residency expectations, so regulated deployments need explicit policy about when higher throughput is allowed to move data across Regions.

**Open questions:**

- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-enforcements.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html] Will AWS unify Automated Reasoning checks with organization-level guardrail enforcement, or will logical verification remain a more local application control?
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html] What minimum event schema should enterprises standardize across Bedrock logs, inference-profile usage records, and external approval systems to make one coherent audit trail?
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html; https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/] How should customers interpret the current status of continued pre-training against newer customization methods when planning long-lived regulated model-customization programs?

### §7 Recursive Review

- Review result: pass
- Acronym audit: pass
- Claim-label audit: pass
- Citation audit: pass
- Cross-item integration audit: pass
- Remaining uncertainty: continued pre-training prominence in current public documentation

---

## Findings

### Executive Summary

Amazon Bedrock already exposes documented managed capabilities across every major surface examined here: multi-model access, agents, knowledge bases, guardrails, workflow orchestration, evaluation, logging, private networking, and compliance support. Enterprise governance still depends on customer-designed identity architecture, logging destinations, region policy, and cost attribution above those native primitives. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html; https://docs.aws.amazon.com/bedrock/latest/userguide/security.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html]

Bedrock's strongest documented areas are breadth of model access, native orchestration through Agents and Flows, retrieval tooling through Knowledge Bases, and built-in safety layers through Guardrails. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html; https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html; https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html]

The platform also documents several cost and performance levers, including inference profiles, Provisioned Throughput, batch inference, prompt caching, and feature-level pricing. [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html; https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html; https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html; https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html; https://aws.amazon.com/bedrock/pricing/]

For a regulated environment, Bedrock's controls work best as powerful primitives that still require customer policy choices around AWS Identity and Access Management (IAM) scope, Virtual Private Cloud networking, key management, data residency, and unified audit evidence. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html; https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html; https://docs.aws.amazon.com/bedrock/latest/userguide/data-encryption.html; https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html; https://davidamitchell.github.io/Research/research/2026-04-26-multi-ai-provider-control-planes.html]

### Key Findings

1. **Amazon Bedrock documents access to 100+ foundation models from Amazon, Anthropic, AI21 Labs, Cohere, DeepSeek, Luma AI, Meta, Mistral AI, poolside, Stability AI, and Writer, plus separate on-demand, cross-region, provisioned, and batch serving paths that let enterprises tune throughput, routing, and commitment levels for different workloads.** ([fact]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html; https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html; https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html; https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html)
2. **Bedrock Agents provide a managed orchestration surface with action groups, knowledge-base integration, prompt customization, traces, aliases, and hierarchical multi-agent collaboration, which places substantial orchestration capability inside the Bedrock service boundary instead of leaving it entirely to customer-built code.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html)
3. **Knowledge Bases combine retrieval, citation, structured-data access, customer-managed vector databases for embedding storage, document chunking modes that split source text before indexing, reranking models that reorder retrieved results, query decomposition that breaks complex questions into sub-queries, and metadata-aware search inside one managed Bedrock feature family for enterprise information retrieval.** ([fact]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html; https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html; https://docs.aws.amazon.com/bedrock/latest/userguide/rerank-use.html)
4. **Bedrock Guardrails cover moderation, sensitive-data handling, grounding, and logic-based verification, and the centrally enforceable organization-level guardrail surface stops short of Automated Reasoning checks.** ([fact]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-enforcements.html)
5. **Bedrock's current customization story is strongest for supervised fine-tuning, reinforcement fine-tuning, and distillation, while continued pre-training is clearly evidenced in AWS launch material but is less prominent in the current public custom-model documentation, so it should be treated as date-sensitive rather than as a stable headline capability.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html; https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html; https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/)
6. **Flows and Bedrock Data Automation extend Bedrock beyond direct model invocation by adding native workflow logic, service integrations, and multimodal extraction surfaces that customers can use in place of some custom orchestration code.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html; https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html; https://docs.aws.amazon.com/bedrock/latest/userguide/bda-how-it-works.html)
7. **Bedrock includes meaningful built-in evaluation, logging, and cost-management primitives, including automatic and human evaluations, invocation logging, prompt caching, inference-profile tagging, and feature-level pricing, and those controls become governance evidence only after the customer enables and joins them operationally.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html; https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html; https://aws.amazon.com/bedrock/pricing/)
8. **For regulated enterprises, Bedrock fits best as a strong AWS-native AI runtime and control surface, while enterprise governance still depends on customer-built identity, network, region, and audit architecture above Bedrock's native capabilities.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html; https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html; https://docs.aws.amazon.com/bedrock/latest/userguide/data-encryption.html; https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html; https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html; https://davidamitchell.github.io/Research/research/2026-04-26-multi-ai-provider-control-planes.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Bedrock exposes provider choice across Amazon, Anthropic, AI21 Labs, Cohere, DeepSeek, Luma AI, Meta, Mistral AI, poolside, Stability AI, and Writer, plus multiple serving modes. | https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html; https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html; https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html; https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html | medium | Core platform and serving docs agree. |
| [inference] Bedrock Agents place substantial orchestration capability inside the Bedrock service boundary. | https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html | medium | Feature set supports the orchestration interpretation. |
| [fact] Knowledge Bases combine retrieval, citation, structured-data access, customer-managed vector databases for embedding storage, document chunking modes, reranking models, query decomposition, and metadata-aware search inside one managed feature family. | https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html; https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html; https://docs.aws.amazon.com/bedrock/latest/userguide/rerank-use.html | medium | Retrieval, filtering, and tuning surfaces are all documented. |
| [fact] Guardrails combine moderation and logical verification, and the organization-enforcement surface excludes Automated Reasoning. | https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-enforcements.html | medium | Strong direct documentation. |
| [inference] Customization is current and useful, but continued pre-training is more date-sensitive than fine-tuning or distillation. | https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html; https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html; https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/ | medium | Older launch evidence plus current docs. |
| [inference] Flows and Bedrock Data Automation can replace some custom orchestration code with native workflow and multimodal extraction primitives. | https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html; https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html; https://docs.aws.amazon.com/bedrock/latest/userguide/bda-how-it-works.html | medium | Product docs show the primitives; the code-reduction claim is interpretive. |
| [inference] Evaluation, logging, and cost controls are substantial but customer-activated. | https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html; https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html; https://aws.amazon.com/bedrock/pricing/ | medium | Features are explicit; activation burden is interpretive. |
| [inference] Bedrock is a strong runtime and control surface, but not a complete enterprise governance plane by itself. | https://docs.aws.amazon.com/bedrock/latest/userguide/security.html; https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html; https://docs.aws.amazon.com/bedrock/latest/userguide/data-encryption.html; https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html; https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html; https://davidamitchell.github.io/Research/research/2026-04-26-multi-ai-provider-control-planes.html | medium | Prior repository synthesis sharpens the governance interpretation. |

### Assumptions

- [assumption; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html; https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-bedrock-general-availability-prompt-caching/] The capability families are the stable object of analysis, even though the exact provider roster and preview model lineup moved after mid-2025. Justification: the question asks what Bedrock can do, not for a frozen vendor census.
- [assumption; source: https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/; https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html] Continued pre-training should be treated as historically evidenced but currently less foregrounded. Justification: that is the narrowest statement consistent with both the older launch material and the current overview page.

### Analysis

AWS documents Bedrock as one managed stack that combines model access, orchestration, retrieval, safety, and evaluation. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html; https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html; https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html; https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html]

That makes Bedrock stronger than a bare model marketplace for platform engineering, but the security and governance evidence still looks like a shared-responsibility toolkit rather than a self-completing governance solution. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html]

The prior repository comparison and control-plane research remain compatible with this reading: Bedrock is strong enough to anchor an AWS-native runtime layer, yet the enterprise still needs identity standards, network policy, audit aggregation, and economic governance above that layer. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html; https://davidamitchell.github.io/Research/research/2026-04-26-multi-ai-provider-control-planes.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html]

An alternative interpretation is that an all-AWS estate could treat Bedrock plus surrounding AWS services as a sufficient governance plane. That interpretation is plausible for narrow estates, but the shared-responsibility and customer-activation evidence makes it too broad for a general regulated-enterprise conclusion. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html]

The platform's operational trade-off is therefore favorable for enterprises that want rich native primitives and are willing to assemble them carefully, but less favorable for teams expecting one turnkey governance plane that automatically normalizes every identity, region, and audit choice. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html; https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html; https://docs.aws.amazon.com/bedrock/latest/userguide/security.html; https://aws.amazon.com/bedrock/security-compliance/]

### Risks, Gaps, and Uncertainties

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html; https://aws.amazon.com/bedrock/] The current Bedrock provider list includes post-mid-2025 additions and preview surfaces, so exact provider breadth should be date-qualified when making historical comparisons.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-enforcements.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html] Automated Reasoning checks do not currently map cleanly onto the organization-level enforcement surface, which creates a real distinction between verification depth and central policy rollout.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/security.html] A customer can easily overestimate Bedrock's governance completeness if they read feature availability as evidence that logging, retention, and audit correlation are already fully configured.
- [inference; source: https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/; https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html] The continued-pre-training story has lower confidence than the other major surfaces because the strongest direct evidence is older launch material rather than a prominent current guide.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html; https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.html] Cross-region performance features can pull against data-residency expectations, so regulated deployments need explicit policy about when higher throughput is allowed to move data across Regions.

### Open Questions

- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-enforcements.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html] Will AWS unify Automated Reasoning checks with organization-level guardrail enforcement, or will logical verification remain a more local application control?
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html] What minimum event schema should enterprises standardize across Bedrock logs, inference-profile usage records, and external approval systems to make one coherent audit trail?
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html; https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/] How should customers interpret the current status of continued pre-training against newer customization methods when planning long-lived regulated model-customization programs?

---

## Output

- Type: knowledge
- Description: Bedrock capability survey concluding that AWS already offers a broad managed runtime stack for enterprise AI, but that regulated deployments still need customer-built identity, network, audit, and region-policy architecture above Bedrock's native primitives. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html; https://docs.aws.amazon.com/bedrock/latest/userguide/security.html; https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html]
- Links:
  - https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html
  - https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html
  - https://aws.amazon.com/bedrock/security-compliance/
