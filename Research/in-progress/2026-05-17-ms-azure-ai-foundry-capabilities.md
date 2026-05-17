---
review_count: 1
title: "Microsoft Foundry (formerly Azure Artificial Intelligence (AI) Foundry): full feature and capability survey"
added: 2026-05-17T10:17:56+00:00
status: reviewing
priority: high
blocks: []
tags: [microsoft, agentic-ai, ai-platform, enterprise, llm, evaluation, ai-governance, regulated-enterprise, workflow]
started: 2026-05-17T14:02:48+00:00
completed: ~
output: [knowledge]
cites: [2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model, 2026-04-28-alternative-pipeline-platforms-copilot-studio-agents, 2026-04-26-ai-agent-identity-access-management-enterprise]
related: [2026-05-06-aibom-platform-observability-control-comparison, 2026-05-10-m365-copilot-sensitive-data-security-governance-risks, 2026-04-26-ms-copilot-cowork]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Microsoft Foundry (formerly Azure Artificial Intelligence (AI) Foundry): full feature and capability survey

## Research Question

What is the complete set of features, functions, and capabilities offered by Microsoft Foundry, and how do those capabilities support the full Artificial Intelligence (AI) development lifecycle, from model selection and fine-tuning through deployment, evaluation, and production governance, in a regulated enterprise?

## Scope

**In scope:**
- Microsoft Foundry model catalogue: available foundation models, model benchmarking, and selection tooling
- Model customisation: fine-tuning, continued pre-training, and distillation where publicly documented
- Development tools: Prompt Flow, Microsoft Foundry Software Development Kit (SDK), agent building capabilities, and playground environments
- Evaluation and testing: built-in evaluation metrics, safety evaluations, and red-teaming tools
- Deployment and serving: managed endpoints, serverless Application Programming Interface (API) options, and deployment configurations
- Responsible AI and safety tooling: content safety filters, grounding checks, and guardrails
- Observability and monitoring: tracing, logging, and cost and usage dashboards
- Enterprise security and access controls: private endpoints, managed identity, role-based access control (RBAC), and data residency
- Integration with Azure Machine Learning (Azure ML), Azure OpenAI Service, and Microsoft Copilot products
- Licensing, pricing model, and resource management
- Product history: transition from Azure AI Studio and Azure AI Foundry branding to Microsoft Foundry, and what changed

**Out of scope:**
- Azure Machine Learning capabilities beyond the Microsoft Foundry integration surface
- Microsoft Copilot Studio capabilities beyond their integration surface with Microsoft Foundry
- On-premises or disconnected deployment scenarios unless directly documented as supported by Microsoft Foundry

**Constraints:** Treat generally available capabilities as the baseline, mark preview capabilities explicitly, and rely primarily on current Microsoft documentation plus clearly linked completed repository items for cross-item synthesis.

## Context

[fact; source: https://learn.microsoft.com/en-us/azure/foundry/what-is-ai-foundry; https://azure.microsoft.com/en-us/products/ai-foundry] Microsoft Foundry is Microsoft's unified enterprise AI platform and current branding for the service family that previously appeared as Azure AI Studio, Azure AI Foundry, and separate Azure AI service surfaces.

[inference; source: https://learn.microsoft.com/en-us/azure/foundry/what-is-ai-foundry; https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture; https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html] For enterprise architecture decisions, the relevant question is not only whether Microsoft Foundry has individual features, but whether its model, agent, evaluation, deployment, and governance surfaces are native enough to reduce the amount of external platform engineering still required in regulated environments.

## Approach

1. What product, resource, and portal changes define the move from Azure AI Studio and Azure OpenAI resource patterns to Microsoft Foundry?
2. What model selection and management capabilities does Microsoft Foundry provide?
   1a. What models are in the catalogue and through what access mechanisms?
   1b. What fine-tuning and model customisation options are available?
   1c. What benchmarking and model evaluation tools are provided?
3. What development tools exist for building AI applications?
   2a. What is Prompt Flow now, and what has replaced it for new development?
   2b. What agent building capabilities are available?
   2c. What SDKs, endpoints, and playgrounds are provided?
4. What evaluation and testing capabilities are available for AI applications?
5. What deployment and serving options are supported?
6. What governance, safety, and responsible AI features are built in?
7. What observability, monitoring, and cost-management capabilities exist?
8. How does Microsoft Foundry integrate with Azure OpenAI, Azure Machine Learning (Azure ML), Microsoft 365 Copilot, Teams, Search, Fabric, and other Azure services?

## Sources

- [x] [Microsoft Learn What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-ai-foundry) - product definition, evolution table, available models, and key capabilities
- [x] [Microsoft Azure Microsoft Foundry product page](https://azure.microsoft.com/en-us/products/ai-foundry) - product composition and integrated-services summary
- [x] [Microsoft Learn Microsoft Foundry documentation home](https://learn.microsoft.com/en-us/azure/foundry/) - current documentation hub and feature map
- [x] [Microsoft Learn Microsoft Foundry architecture](https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture) - resource hierarchy, connected services, and security separation of concerns
- [x] [Microsoft Learn Microsoft Foundry Models overview](https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview) - catalogue structure, model categories, filters, and benchmark surfaces
- [x] [Microsoft Learn Model leaderboards in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/model-benchmarks) - leaderboard methodology and benchmark categories
- [x] [Microsoft Learn Models sold directly by Azure](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure) - Azure Direct model category, support, billing, and model families
- [x] [Microsoft Learn Deployment overview for Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/foundry/concepts/deployments-overview) - standard versus managed compute deployments
- [x] [Microsoft Learn Deployment types for Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types) - global, data-zone, regional, provisioned, batch, and developer deployment types
- [x] [Microsoft Learn Region support for Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/reference/region-support) - project-region list and feature-specific region caveats
- [x] [Microsoft Learn Customize a model with fine-tuning](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/fine-tuning) - fine-tuning methods, supported-model examples, permissions, and deployment flow
- [x] [Microsoft Learn Plan and manage costs for Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs) - cost planning, billing models, and fine-tuned model cost behavior
- [x] [Microsoft Learn SDK overview for Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview) - SDK choices, endpoint patterns, and authentication guidance
- [x] [Microsoft Learn Quickstart: Build with models and agents](https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code) - project endpoint, model call, and agent creation examples
- [x] [Microsoft Learn Foundry Agent Service overview](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) - agent types, tools, observability, publishing, and enterprise capabilities
- [x] [Microsoft Learn Build a workflow in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/workflow) - workflow patterns, visual orchestration, and human-in-the-loop support
- [x] [Microsoft Learn Tool catalog for Microsoft Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog) - built-in tools, custom tools, Model Context Protocol (MCP), and toolbox
- [x] [Microsoft Learn Memory usage in Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/memory-usage) - managed memory stores and per-user scoping
- [x] [Microsoft Learn What is Foundry IQ?](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq) - knowledge-base and agentic-retrieval capabilities
- [x] [Microsoft Learn Publish agents to Microsoft 365 Copilot and Microsoft Teams](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/publish-copilot) - publishing workflow and preview status
- [x] [Microsoft Learn Microsoft Foundry playgrounds](https://learn.microsoft.com/en-us/azure/foundry/concepts/concept-playgrounds) - model and agents playground capabilities
- [x] [Microsoft Learn Prompt flow in Microsoft Foundry portal (classic)](https://learn.microsoft.com/en-us/azure/foundry-classic/concepts/prompt-flow) - Prompt Flow scope, lifecycle, and retirement status
- [x] [Microsoft Learn Audit, rebuild, and validate Prompt Flow for Agent Framework migration](https://learn.microsoft.com/en-us/azure/foundry-classic/how-to/how-to-migrate-prompt-flow-to-agent-framework) - migration path from Prompt Flow to Microsoft Agent Framework
- [x] [Microsoft Learn Observability in generative AI](https://learn.microsoft.com/en-us/azure/foundry/concepts/observability) - evaluation, monitoring, tracing, and red-teaming overview
- [x] [Microsoft Learn Evaluate your AI agents](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/evaluate-agent) - agent evaluation flow and built-in evaluator categories
- [x] [Microsoft Learn Agent tracing in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept) - tracing scope, OpenTelemetry, and preview status
- [x] [Microsoft Learn Monitor agents with the Agent Monitoring Dashboard](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard) - production monitoring, continuous evaluation, and dashboard metrics
- [x] [Microsoft Learn Foundry Control Plane overview](https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview) - cross-project fleet management, compliance, and security panes
- [x] [Microsoft Learn Role-based access control for Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry) - Foundry-specific roles and scope model
- [x] [Microsoft Learn Authentication and authorization in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/authentication-authorization-foundry) - control plane versus data plane and Microsoft Entra identity guidance
- [x] [Microsoft Learn Configure network isolation with private link](https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link) - private endpoints, public network access, and virtual network injection
- [x] [Microsoft Learn Guardrails and controls overview in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview) - guardrail intervention points and supported risk categories
- [x] [Microsoft Learn Task Adherence in Microsoft Foundry and Content Safety](https://learn.microsoft.com/en-us/azure/foundry/guardrails/task-adherence) - task-misalignment detection and tool-call blocking logic
- [x] [Microsoft Learn Add a new connection to your project](https://learn.microsoft.com/en-us/azure/foundry/how-to/connections-add) - supported connection types and preview connectors
- [x] [Microsoft Learn Bring your own Azure Storage to Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/how-to/bring-your-own-azure-storage-foundry) - bring-your-own-storage patterns and capability hosts
- [x] [Microsoft Learn Upgrade Azure OpenAI to Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/how-to/upgrade-azure-openai) - upgrade behavior, preserved endpoints, and governance implications
- [x] [Microsoft Learn Endpoints for Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/endpoints) - deployment and endpoint model
- [x] [Microsoft Learn Microsoft Foundry Models in Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/foundry-models-overview?view=azureml-api-2) - Azure Machine Learning (Azure ML) integration surface for the model catalogue
- [x] [Microsoft Fabric Use OneLake as a knowledge source for Microsoft Foundry](https://learn.microsoft.com/en-us/fabric/onelake/onelake-foundry-knowledge) - Fabric and OneLake grounding path
- [x] [Azure AI Search Indexed OneLake knowledge source for agentic retrieval](https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-how-to-onelake) - Azure AI Search knowledge-source creation for OneLake
- [x] [David Mitchell (2026) Vendor-agnostic enterprise Artificial Intelligence (AI) capability model: Microsoft Copilot and GitHub families vs AWS Bedrock ecosystem](https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html) - prior repository synthesis on enterprise AI capability boundaries
- [x] [David Mitchell (2026) Alternative Continuous Integration and Continuous Delivery pipeline platforms for governing agents built with Microsoft Copilot Studio](https://davidamitchell.github.io/Research/research/2026-04-28-alternative-pipeline-platforms-copilot-studio-agents.html) - prior repository evidence on Microsoft-side pipeline governance boundaries
- [x] [David Mitchell (2026) What identity and access management model is required for Artificial Intelligence (AI) agents and low-code artefacts operating within enterprise systems?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html) - prior repository synthesis on workload identity and attribution

## Related

- [David Mitchell (2026) Vendor-agnostic enterprise Artificial Intelligence (AI) capability model: Microsoft Copilot and GitHub families vs AWS Bedrock ecosystem](https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html)
- [David Mitchell (2026) What introspection, export, and control surfaces actually exist across production agentic Artificial Intelligence (AI) platforms?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html)
- [David Mitchell (2026) Security, Compliance, and Governance Risks of Using Generative AI tools such as Microsoft 365 Copilot on sensitive data](https://davidamitchell.github.io/Research/research/2026-05-10-m365-copilot-sensitive-data-security-governance-risks.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: What capabilities does Microsoft Foundry expose across model selection, customisation, development, evaluation, deployment, observability, security, and integration, and how complete is that lifecycle support for a regulated enterprise?
- Scope: Microsoft Foundry current platform, with Azure AI Studio and Prompt Flow covered only as transition context; generally available features are the baseline and preview features are marked explicitly.
- Constraints: Full mode; primary Microsoft documentation first; connected-service behavior treated as part of the answer only where Microsoft Foundry documents the integration surface explicitly.
- Output: Knowledge with executive summary, key findings, evidence map, assumptions, analysis, risks, and open questions.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html] Prior repository work already treated Microsoft's ecosystem as split between developer-facing build surfaces and broader enterprise governance surfaces, which makes lifecycle completeness and boundary placement central to this item.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-28-alternative-pipeline-platforms-copilot-studio-agents.html] Prior repository work on Microsoft Copilot Studio deployment governance found that release-time enforcement and external pipeline controls still matter even when Microsoft provides native maker tooling.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] Prior repository identity work also established that regulated deployment depends on explicit workload identity, bounded delegation, and attributable action chains rather than only on model quality or platform convenience.

### §1 Question Decomposition

- 1. Product history and architecture
  - 1.1 What changed when Azure AI Studio and Azure AI Foundry were consolidated into Microsoft Foundry?
  - 1.2 What are the top-level resource, project, and connected-resource boundaries?
- 2. Model access and selection
  - 2.1 What categories of models are available in the catalogue?
  - 2.2 What comparison, leaderboard, and benchmark surfaces exist?
- 3. Model customisation
  - 3.1 What fine-tuning methods are documented?
  - 3.2 Which customization paths remain limited to selected models or classic surfaces?
- 4. Development surfaces
  - 4.1 Which agent, workflow, SDK, and playground options exist?
  - 4.2 What is the current status of Prompt Flow?
- 5. Evaluation and testing
  - 5.1 What built-in evaluators and testing loops exist before deployment?
  - 5.2 What post-deployment evaluation and monitoring paths exist?
- 6. Deployment and serving
  - 6.1 Which deployment options exist for Azure Direct and non-Azure Direct models?
  - 6.2 How do data residency, quota, and latency choices vary by deployment type?
- 7. Governance, safety, and security
  - 7.1 Which identity, RBAC, guardrail, and network-isolation controls are native?
  - 7.2 Which controls depend on connected services or preview status?
- 8. Integration and enterprise fit
  - 8.1 How does Microsoft Foundry integrate with Azure OpenAI, Azure Machine Learning (Azure ML), Search, Fabric, and Copilot surfaces?
  - 8.2 Which enterprise-governance responsibilities still sit outside Microsoft Foundry itself?

### §2 Investigation

#### 1. Product history and architecture

- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/what-is-ai-foundry; https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture] Microsoft documents Microsoft Foundry as the current unified platform that replaces the former Azure AI Studio and Azure AI Foundry branding with a single `Microsoft.CognitiveServices/accounts` resource plus project subresources for development isolation.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/what-is-ai-foundry] Microsoft's evolution table says the transition also replaced Assistants API with Responses API, hub plus separate Azure OpenAI and Azure AI Services resources with a single Foundry resource and projects, and multiple prior SDK packages with the unified `azure-ai-projects` client plus OpenAI compatibility.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture] Microsoft Foundry separates top-level governance and deployment settings from project-scoped assets such as files, agents, and evaluations, while connected resources such as Storage, Key Vault, and Azure AI Search remain independent Azure resources with their own governance boundaries.
- [inference; source: https://learn.microsoft.com/en-us/azure/foundry/what-is-ai-foundry; https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture; https://learn.microsoft.com/en-us/azure/foundry/how-to/upgrade-azure-openai] The platform reduces product and endpoint sprawl for builders, but it does not eliminate cross-resource governance work because storage, search, networking, and tenant policy remain materially external to the Foundry resource boundary.

#### 2. Model access and selection

- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview; https://learn.microsoft.com/en-us/azure/machine-learning/foundry-models-overview?view=azureml-api-2] Microsoft documents more than 1,900 models in the Foundry catalogue, spanning Azure Direct models and partner or community models across reasoning, multimodal, small-language, industry, and open-model categories.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview; https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure] Azure Direct models are hosted, billed, and supported by Microsoft under Microsoft product terms and service-level agreements, while partner and community models are supported by their providers and expose different deployment options depending on the provider's configuration.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview; https://learn.microsoft.com/en-us/azure/foundry/concepts/model-benchmarks] The model catalogue includes keyword and capability filters, compare workflows, model cards, and preview leaderboards covering quality, safety, performance, cost, and scenario-specific benchmark views.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/model-benchmarks] Microsoft says leaderboard benchmarks use public reasoning, coding, safety, and throughput datasets such as BIG-Bench Hard and HarmBench to compare curated model subsets.
- [inference; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview; https://learn.microsoft.com/en-us/azure/foundry/concepts/model-benchmarks] Microsoft Foundry's selection surface is stronger than a simple marketplace because model discovery, benchmark comparison, and deployment handoff are integrated in one portal flow, although the leaderboards remain a curated subset rather than a live benchmark for every catalogue model.

#### 3. Model customisation

- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/fine-tuning] Microsoft documents fine-tuning in Microsoft Foundry as a Low-Rank Adaptation (LoRA) based customization path and lists supervised fine-tuning, direct preference optimization, and reinforcement fine-tuning across selected Azure OpenAI and selected open-model entries, with general availability and preview status varying by model family.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/fine-tuning; https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs] Fine-tuning requires project roles, dataset preparation, job monitoring, deployment, and evaluation, and Microsoft separately bills training, hosting, and inference for fine-tuned models.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/deployments-overview; https://learn.microsoft.com/en-us/azure/machine-learning/foundry-models-overview?view=azureml-api-2] Microsoft also documents that some partner and community models still use managed compute rather than the standard Foundry-resource deployment path, which means not every customization path lives on the same serving substrate.
- [inference; source: https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/fine-tuning; https://learn.microsoft.com/en-us/azure/foundry/concepts/deployments-overview] Microsoft Foundry supports meaningful native customization, but customization breadth is narrower than catalogue breadth, so enterprises should not assume that every model family available for selection is equally available for training, hosting, and lifecycle management.

#### 4. Development surfaces

- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview; https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code] Microsoft provides a unified project endpoint for the Foundry SDK, OpenAI-compatible access for Foundry direct models, Anthropic SDK support for Claude deployments, and quickstarts for Python, C#, TypeScript, Java, web API, and the portal.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/agents/overview; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/workflow] Agent Service supports prompt agents, workflow agents in preview, and hosted agents in preview, with workflow templates for sequential, group-chat, and human-in-the-loop orchestration.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog; https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/memory-usage; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq] The development surface includes built-in tools such as web search, file search, code interpreter, and function calling, custom tools such as MCP, Agent-to-Agent (A2A), and OpenAPI, managed memory stores, and Foundry IQ, Microsoft's managed knowledge layer, with multi-source retrieval over indexed and remote sources.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/concept-playgrounds; https://learn.microsoft.com/en-us/azure/foundry/agents/overview] Microsoft Foundry playgrounds provide model and agents playgrounds with model comparison, tool configuration, knowledge-grounding, memory, tracing, evaluation, and browser-based code export to Visual Studio Code.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry-classic/concepts/prompt-flow; https://learn.microsoft.com/en-us/azure/foundry-classic/how-to/how-to-migrate-prompt-flow-to-agent-framework] Prompt Flow is now explicitly a Foundry classic feature, feature development ended on 2026-04-20, full retirement is scheduled for 2027-04-20, and Microsoft recommends migration to Microsoft Agent Framework for future-state development.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/publish-copilot] Publishing Foundry agents to Microsoft 365 Copilot and Teams exists, but Microsoft labels that path Early Access Preview and routes it through a stable endpoint rather than exposing a fully general-purpose Microsoft 365 governance plane inside Foundry.
- [inference; source: https://learn.microsoft.com/en-us/azure/foundry/agents/overview; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/workflow; https://learn.microsoft.com/en-us/azure/foundry-classic/how-to/how-to-migrate-prompt-flow-to-agent-framework] The development center of gravity has moved from prompt-flow-first experimentation to an agent-first stack built around project endpoints, managed runtime, workflows, tools, and Agent Framework interoperability.

#### 5. Evaluation and testing

- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/observability; https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/evaluate-agent] Microsoft documents evaluation across base-model selection, pre-production application testing, and post-production monitoring, with built-in evaluators for quality, safety, text similarity, and agent behavior.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/evaluate-agent; https://learn.microsoft.com/en-us/azure/foundry/concepts/observability] Agent evaluation can score measures such as task adherence, coherence, violence, groundedness, relevance, tool behavior, and custom evaluation logic against datasets and deployed agents.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/observability; https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview] Microsoft also documents an AI red teaming agent, cluster analysis, scheduled evaluation, and continuous evaluation for sampled production traffic as part of the broader observability stack.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept; https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard] Tracing and monitoring are built on Azure Monitor Application Insights and OpenTelemetry, and the dashboard surfaces token usage, latency, run success rate, evaluation metrics, and red-teaming results.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept] Microsoft says tracing is generally available for prompt agents only, while workflow, hosted, and custom agents remain preview for tracing.
- [inference; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/observability; https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept; https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard] Microsoft Foundry has unusually strong native evaluation coverage for a platform service, but the most operationally valuable runtime-inspection features still depend on Application Insights setup and some preview pathways.

#### 6. Deployment and serving

- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/deployments-overview; https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types] Microsoft documents two top-level deployment modes: standard deployment in Foundry resources for Azure Direct and selected partner models, and managed compute deployment for non-Azure-Direct, some partner, and custom models.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types] Standard deployment types include Global Standard, Data Zone Standard, Regional Standard, Global Provisioned, Data Zone Provisioned, Regional Provisioned, Global Batch, Data Zone Batch, and Developer for fine-tuned model evaluation.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types] Microsoft says Global deployments may process inferencing data in any Azure region, DataZone deployments constrain processing to the United States or European Union data zone, and regional deployments constrain processing to a single deployment region.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types; https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs] Provisioned deployments reserve throughput units for predictable capacity, batch deployments target asynchronous high-volume jobs at lower cost, and standard deployments trade guaranteed throughput for pay-per-token flexibility.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/endpoints; https://learn.microsoft.com/en-us/azure/foundry/how-to/upgrade-azure-openai] Microsoft Foundry can preserve existing Azure OpenAI endpoints and keys during resource upgrade while also exposing broader Foundry project and services endpoints for new capabilities.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/reference/region-support; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/limits-quotas-regions] Region support is explicitly feature-specific, with Agent Service only in regions that support the Responses API and with tool availability varying by region.
- [inference; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/deployments-overview; https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types; https://learn.microsoft.com/en-us/azure/foundry/reference/region-support] Microsoft Foundry gives enterprises a real deployment-design space rather than one default managed path, but that flexibility also means compliance, quota, and latency behavior depend on deployment-type choices that architects must make explicitly.

#### 7. Governance, safety, and security

- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/authentication-authorization-foundry; https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry] Microsoft separates control plane and data plane actions in Foundry, recommends Microsoft Entra identity over API keys for production, and provides Foundry User, Foundry Project Manager, Foundry Account Owner, and Foundry Owner roles at resource and project scopes.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link; https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture] Network isolation covers inbound private endpoints and public-network-access settings, outbound private connectivity to Azure Platform as a Service (PaaS) resources, and agent-client virtual-network injection for controlled outbound access.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/how-to/bring-your-own-azure-storage-foundry] Microsoft documents bring-your-own-storage patterns for agents, evaluations, datasets, Content Understanding, Speech, and Language, with capability-host bindings when multiple storage connections exist.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview; https://learn.microsoft.com/en-us/azure/foundry/guardrails/task-adherence; https://learn.microsoft.com/en-us/azure/foundry/concepts/deployments-overview] Guardrails cover user input, tool call, tool response, and output intervention points, and Microsoft documents content risks, prompt attacks, protected material, personally identifiable information in preview, groundedness for models, and task-adherence controls that can block misaligned tool actions.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview; https://learn.microsoft.com/en-us/azure/foundry/how-to/connections-add] Foundry Control Plane adds cross-project inventory, compliance, cost, observability, and security views, while connections extend the platform to Azure AI Search, Azure Storage, Cosmos DB in preview, SharePoint in preview, Fabric in preview, Azure API Management (APIM) in preview, and model-gateway surfaces in preview.
- [inference; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/authentication-authorization-foundry; https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview; https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] Microsoft Foundry is governance-aware, but it is not a complete governance enclosure because identity, storage, search, connected-resource policy, and some agent controls remain distributed across Azure systems and, in several cases, preview-only surfaces.

#### 8. Observability, cost, and enterprise integration

- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard; https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs] Agent monitoring exposes token usage, latency, run-success rates, evaluation metrics, and red-team results, while cost visibility depends on Azure Cost Management roles plus Foundry usage context.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs; https://azure.microsoft.com/en-us/products/ai-foundry] Microsoft says the platform is free to explore, but billing occurs at the deployment and underlying-service level, and there is no single pricing-calculator entry because Foundry composes multiple Azure services.
- [fact; source: https://azure.microsoft.com/en-us/products/ai-foundry; https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture; https://learn.microsoft.com/en-us/azure/machine-learning/foundry-models-overview?view=azureml-api-2] Microsoft positions Foundry as a hub that integrates Azure OpenAI, Azure Machine Learning, Azure App Service, Azure Container Apps, Azure Functions, Azure Logic Apps, Azure API Management, Azure Monitor, Microsoft Defender, Microsoft Purview, and Microsoft Entra based identity services.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq; https://learn.microsoft.com/en-us/fabric/onelake/onelake-foundry-knowledge; https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-how-to-onelake] Foundry IQ, Microsoft's managed knowledge layer, integrates Azure AI Search based multi-source retrieval, supports sources such as Azure Blob Storage, SharePoint, OneLake, and public web data, and can use OneLake content through Azure AI Search knowledge sources.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/how-to/upgrade-azure-openai; https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/endpoints] Azure OpenAI integrates both as a preserved legacy endpoint and as part of the broader Foundry model and project surface after upgrade.
- [inference; source: https://azure.microsoft.com/en-us/products/ai-foundry; https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/publish-copilot; https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html] Microsoft Foundry is best understood as Microsoft's developer and platform-engineering layer for AI applications, which can feed Microsoft Copilot surfaces and Azure services, rather than as a single tenant-wide operations and compliance plane that replaces Microsoft 365 administration or enterprise platform engineering.

### §3 Reasoning

- [inference; source: https://learn.microsoft.com/en-us/azure/foundry/what-is-ai-foundry; https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture; https://learn.microsoft.com/en-us/azure/foundry/concepts/observability] The evidence supports a two-level reading of Microsoft Foundry: it is broad and coherent as an application factory for models, agents, evaluation, and deployment, but its governance completeness depends on how well the surrounding Azure estate is configured.
- [inference; source: https://learn.microsoft.com/en-us/azure/foundry/agents/overview; https://learn.microsoft.com/en-us/azure/foundry-classic/concepts/prompt-flow; https://learn.microsoft.com/en-us/azure/foundry-classic/how-to/how-to-migrate-prompt-flow-to-agent-framework] Prompt Flow should be counted as legacy transition capability rather than current strategic core, because Microsoft explicitly ended feature development and directs net-new workflow design toward agents, workflows, and Agent Framework.
- [inference; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/deployments-overview; https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types; https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs] Deployment flexibility is a strength only if the enterprise is ready to govern data-zone choice, throughput commitments, region support, and cost composition explicitly; otherwise the same flexibility becomes configuration debt.
- [assumption; source: https://learn.microsoft.com/en-us/azure/foundry/agents/overview; https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview; https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview] Preview features are treated as real capabilities for this survey but not as production baseline controls. Justification: Microsoft documents them as available surfaces, but also states that previews lack service-level agreements and can have constrained support.

### §4 Consistency Check

- Contradictions reviewed: none unresolved.
- Naming normalized: Microsoft Foundry is the current name; Azure AI Studio, Azure AI Foundry, and Prompt Flow are included only when transition state matters.
- Preview normalization: workflow agents, hosted agents, some tracing paths, Control Plane panes, publish-to-Copilot, toolbox, and several connector surfaces treated as preview where Microsoft marks them so.
- Adjacent completed-item sweep repeated: https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html ; https://davidamitchell.github.io/Research/research/2026-04-28-alternative-pipeline-platforms-copilot-studio-agents.html ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html ; https://davidamitchell.github.io/Research/research/2026-05-10-m365-copilot-sensitive-data-security-governance-risks.html

### §5 Depth and Breadth Expansion

- [inference; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture; https://learn.microsoft.com/en-us/azure/foundry/concepts/authentication-authorization-foundry; https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link] From a technical and security lens, Microsoft Foundry is strongest when the enterprise already uses Azure-native identity, networking, and connected-resource controls, because its most mature governance surfaces assume Microsoft Entra identity, Private Link, Application Insights, and Azure policy patterns.
- [inference; source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types; https://learn.microsoft.com/en-us/azure/foundry/reference/region-support; https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs] From a regulatory and economic lens, deployment type is not a minor serving detail but a governance choice that directly affects data-processing location, latency variance, quota behavior, and cost predictability.
- [inference; source: https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq; https://learn.microsoft.com/en-us/fabric/onelake/onelake-foundry-knowledge; https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-how-to-onelake] From an information-architecture lens, Microsoft's most differentiated platform move is not only model hosting but its attempt to make search-backed, permission-aware knowledge retrieval a first-class agent primitive through Foundry IQ, its managed knowledge layer, and Azure AI Search integration.
- [inference; source: https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/publish-copilot; https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview; https://davidamitchell.github.io/Research/research/2026-05-10-m365-copilot-sensitive-data-security-governance-risks.html] From a behavioural and operating-model lens, Microsoft Foundry lowers the barrier to experimentation faster than it lowers the barrier to durable governance, so regulated enterprises still need a platform team to decide which preview, publishing, and connected-service paths are actually allowed.

### §6 Synthesis

**Executive Summary**

Microsoft Foundry already covers most of the enterprise AI application lifecycle natively, including model discovery, benchmarking, selected fine-tuning, agent development, evaluation, deployment, tracing, and Azure-native security controls. [inference; source: https://learn.microsoft.com/en-us/azure/foundry/what-is-ai-foundry; https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview; https://learn.microsoft.com/en-us/azure/foundry/concepts/observability; https://learn.microsoft.com/en-us/azure/foundry/concepts/deployments-overview]

Its strongest areas are model access, agent tooling, evaluation and observability, and deployment flexibility, while its weakest areas for regulated enterprises are not missing features so much as fragmented governance boundaries across connected Azure services, tenant administration, and preview-only control surfaces. [inference; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture; https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview; https://learn.microsoft.com/en-us/azure/foundry/concepts/authentication-authorization-foundry]

Prompt Flow is now a legacy transition surface rather than the forward path, and Microsoft's current strategic direction is agent-centric development through Agent Service, workflows, project endpoints, and Microsoft Agent Framework. [fact; source: https://learn.microsoft.com/en-us/azure/foundry-classic/concepts/prompt-flow; https://learn.microsoft.com/en-us/azure/foundry-classic/how-to/how-to-migrate-prompt-flow-to-agent-framework; https://learn.microsoft.com/en-us/azure/foundry/agents/overview]

For a regulated enterprise, Microsoft Foundry is best treated as a strong Azure-native AI application factory, not as a self-sufficient governance plane, because identity, search, storage, compliance, and tenant-wide Copilot controls still require surrounding Azure and Microsoft 365 governance layers. [inference; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture; https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link; https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/publish-copilot; https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html]

**Key Findings**

1. **Microsoft Foundry consolidates the former Azure AI Studio and Azure AI Foundry experience into a single resource and project model, and Microsoft can upgrade Azure OpenAI resources in place without changing existing Azure OpenAI endpoints, keys, or saved state.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/foundry/what-is-ai-foundry; https://learn.microsoft.com/en-us/azure/foundry/how-to/upgrade-azure-openai; https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture)
2. **The model catalogue is broad and practically useful, because Microsoft documents more than 1,900 models, side-by-side comparison, public-benchmark leaderboards, model cards, deployment tabs, and filterable deployment and licence metadata within the same discovery surface.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview; https://learn.microsoft.com/en-us/azure/foundry/concepts/model-benchmarks; https://learn.microsoft.com/en-us/azure/machine-learning/foundry-models-overview?view=azureml-api-2)
3. **Microsoft Foundry supports meaningful native model customisation, especially Low-Rank Adaptation (LoRA) based fine-tuning and selected optimization methods, but customization support is narrower than catalogue support and some partner or open-model paths still depend on managed compute or classic-era deployment patterns.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/fine-tuning; https://learn.microsoft.com/en-us/azure/foundry/concepts/deployments-overview; https://learn.microsoft.com/en-us/azure/machine-learning/foundry-models-overview?view=azureml-api-2)
4. **The development stack is now decisively agent-centric, combining prompt agents, workflow agents, hosted agents, tool catalogues, memory, Foundry IQ, Microsoft's managed knowledge layer, unified SDKs, and playgrounds, while Prompt Flow remains only as a legacy classic feature with retirement and migration guidance already published.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/foundry/agents/overview; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/workflow; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog; https://learn.microsoft.com/en-us/azure/foundry-classic/concepts/prompt-flow; https://learn.microsoft.com/en-us/azure/foundry-classic/how-to/how-to-migrate-prompt-flow-to-agent-framework)
5. **Evaluation and observability are first-class platform features, because Microsoft documents lifecycle evaluation from benchmark-driven model selection through agent testing, continuous evaluation, dashboard monitoring, OpenTelemetry tracing, and automated red-teaming, even though some runtime-inspection paths remain preview.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/observability; https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/evaluate-agent; https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept; https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard)
6. **Deployment and serving flexibility are broad for a managed platform, because Microsoft Foundry supports standard, provisioned, batch, data-zone, regional, and managed-compute serving patterns, but that same flexibility pushes architects to make explicit data-residency, quota, and cost-governance decisions.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/deployments-overview; https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types; https://learn.microsoft.com/en-us/azure/foundry/reference/region-support; https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs)
7. **Microsoft Foundry has serious enterprise-governance machinery, including Microsoft Entra identity, Foundry RBAC roles, Private Link, bring-your-own-storage, guardrails, task-adherence checks, and Control Plane fleet views, but those controls remain distributed across Foundry, connected Azure resources, and several preview-only surfaces.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/authentication-authorization-foundry; https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry; https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link; https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview; https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview)
8. **Microsoft Foundry integrates well with Azure OpenAI, Azure Machine Learning (Azure ML), Azure AI Search, OneLake, and Microsoft Copilot surfaces, but those integrations make the platform more useful as a developer-side AI application factory than as a complete enterprise governance plane in its own right.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/foundry/how-to/upgrade-azure-openai; https://learn.microsoft.com/en-us/azure/machine-learning/foundry-models-overview?view=azureml-api-2; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq; https://learn.microsoft.com/en-us/fabric/onelake/onelake-foundry-knowledge; https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/publish-copilot)

**Evidence Map**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Microsoft Foundry consolidates the former Azure AI Studio and Azure AI Foundry experience into one resource and project model while preserving Azure OpenAI upgrade continuity. | https://learn.microsoft.com/en-us/azure/foundry/what-is-ai-foundry ; https://learn.microsoft.com/en-us/azure/foundry/how-to/upgrade-azure-openai ; https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture | medium | Current platform identity |
| [inference] The model catalogue is broad enough for practical selection work because it spans more than 1,900 models and includes compare, benchmark, and filtered deployment-selection surfaces. | https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview ; https://learn.microsoft.com/en-us/azure/foundry/concepts/model-benchmarks ; https://learn.microsoft.com/en-us/azure/machine-learning/foundry-models-overview?view=azureml-api-2 | medium | Discovery and selection |
| [inference] Native customization is real but narrower than catalogue breadth because selected methods and models are supported while other model paths still use managed compute or classic patterns. | https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/fine-tuning ; https://learn.microsoft.com/en-us/azure/foundry/concepts/deployments-overview ; https://learn.microsoft.com/en-us/azure/machine-learning/foundry-models-overview?view=azureml-api-2 | medium | Customization asymmetry |
| [inference] The active development direction is agent-centric and Prompt Flow is a legacy classic capability with published retirement and migration guidance. | https://learn.microsoft.com/en-us/azure/foundry/agents/overview ; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/workflow ; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog ; https://learn.microsoft.com/en-us/azure/foundry-classic/concepts/prompt-flow ; https://learn.microsoft.com/en-us/azure/foundry-classic/how-to/how-to-migrate-prompt-flow-to-agent-framework | medium | Build-surface transition |
| [inference] Evaluation and observability are first-class platform features, but some of the deepest runtime-inspection paths still depend on preview and Application Insights setup. | https://learn.microsoft.com/en-us/azure/foundry/concepts/observability ; https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/evaluate-agent ; https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept ; https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard | medium | Strong but not fully uniform |
| [inference] Deployment flexibility is strong, but compliance and cost behavior depend on explicit deployment-type and region decisions rather than one default secure serving mode. | https://learn.microsoft.com/en-us/azure/foundry/concepts/deployments-overview ; https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types ; https://learn.microsoft.com/en-us/azure/foundry/reference/region-support ; https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs | medium | Serving trade-offs |
| [inference] Enterprise-governance machinery is substantial but distributed across Foundry, connected Azure resources, and several preview-only surfaces. | https://learn.microsoft.com/en-us/azure/foundry/concepts/authentication-authorization-foundry ; https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry ; https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link ; https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview ; https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview | medium | Governance fragmentation |
| [inference] Microsoft Foundry integrates well with Azure and Copilot-adjacent services, but it remains better framed as an AI application factory than as a complete enterprise governance plane. | https://learn.microsoft.com/en-us/azure/foundry/how-to/upgrade-azure-openai ; https://learn.microsoft.com/en-us/azure/machine-learning/foundry-models-overview?view=azureml-api-2 ; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq ; https://learn.microsoft.com/en-us/fabric/onelake/onelake-foundry-knowledge ; https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/publish-copilot ; https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html | medium | Integration boundary |

**Assumptions**

- Preview features are counted as existing capabilities but not as production-grade baseline controls because Microsoft publishes them in current documentation while also disclaiming service-level agreements and full support. [assumption; source: https://learn.microsoft.com/en-us/azure/foundry/agents/overview; https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview; https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview]
- Azure Machine Learning (Azure ML) integration is assessed only at the documented Microsoft Foundry model-catalogue and deployment surface, not at the level of general Azure ML workspace feature parity, because that broader Azure ML scope is out of scope for this item. [assumption; source: https://learn.microsoft.com/en-us/azure/machine-learning/foundry-models-overview?view=azureml-api-2; https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture]
- This survey treats Microsoft documentation as authoritative for product-capability claims and does not infer undocumented feature parity across every region or every model family. [assumption; source: https://learn.microsoft.com/en-us/azure/foundry/reference/region-support; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/limits-quotas-regions]

**Analysis**

Microsoft's documentation supports a direct answer that Microsoft Foundry is already broad enough to cover most lifecycle stages natively, so the platform is not limited to model hosting or playground experimentation. [inference; source: https://learn.microsoft.com/en-us/azure/foundry/what-is-ai-foundry; https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview; https://learn.microsoft.com/en-us/azure/foundry/concepts/observability]

The stronger competing interpretation is that Microsoft Foundry is now a complete enterprise AI control plane, but the architecture, networking, identity, storage, and publish-to-Copilot documents do not support that stronger claim because multiple essential governance surfaces remain outside the Foundry resource itself. [inference; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture; https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link; https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/publish-copilot]

Another plausible rival interpretation is that the platform is still mostly Azure OpenAI with new branding, but the agent runtime, workflow builder, Foundry IQ knowledge layer, Control Plane, and unified project endpoint together show a materially broader application platform than standalone Azure OpenAI provided. [inference; source: https://learn.microsoft.com/en-us/azure/foundry/agents/overview; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/workflow; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq; https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview]

The best-supported conclusion is therefore narrower and more decision-useful: Microsoft Foundry is a strong Azure-native build, test, deploy, and operate platform for AI applications, but regulated enterprises still need explicit surrounding governance for connected data sources, tenant administration, identity, and release policy. [inference; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/authentication-authorization-foundry; https://learn.microsoft.com/en-us/azure/foundry/how-to/connections-add; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html]

**Risks, gaps, uncertainties**

- Several of the most ambitious management surfaces, including parts of Control Plane, workflow and hosted-agent support, publish-to-Copilot, toolbox, and some tracing and guardrail behaviors, are still preview, which means production commitments and operational stability are not yet equivalent across the whole stack. [fact; source: https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview; https://learn.microsoft.com/en-us/azure/foundry/agents/overview; https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/publish-copilot; https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept]
- Microsoft's public documentation describes model families, regions, and quotas as moving targets, so any procurement or architecture decision still needs a live region and quota check in the target subscription before deployment. [fact; source: https://learn.microsoft.com/en-us/azure/foundry/reference/region-support; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/limits-quotas-regions]
- The survey establishes breadth of documented capability more strongly than day-two operational maturity, because many documents describe setup and feature availability rather than large-scale reference operations in tightly regulated production estates. [inference; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs; https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview; https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard]

**Open questions**

- Which Microsoft Foundry preview surfaces reach general availability first, specifically Control Plane governance panes, hosted-agent observability, and publish-to-Copilot?
- How much of current Microsoft Agent Framework functionality eventually becomes a managed Microsoft Foundry surface rather than remaining an external code framework?
- How much operational evidence will Microsoft publish on large regulated-enterprise deployments using DataZone, private networking, Foundry IQ, and preview governance controls together?

### §7 Recursive Review

- Review result: pass
- Claim-label audit: complete
- Acronym-expansion audit: complete in body text
- Cross-item integration audit: complete
- Findings and §6 synthesis parity: complete

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Microsoft Foundry already covers most of the enterprise AI application lifecycle natively, including model discovery, benchmarking, selected fine-tuning, agent development, evaluation, deployment, tracing, and Azure-native security controls. [inference; source: https://learn.microsoft.com/en-us/azure/foundry/what-is-ai-foundry; https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview; https://learn.microsoft.com/en-us/azure/foundry/concepts/observability; https://learn.microsoft.com/en-us/azure/foundry/concepts/deployments-overview]

Its strongest areas are model access, agent tooling, evaluation and observability, and deployment flexibility, while its weakest areas for regulated enterprises are not missing features so much as fragmented governance boundaries across connected Azure services, tenant administration, and preview-only control surfaces. [inference; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture; https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview; https://learn.microsoft.com/en-us/azure/foundry/concepts/authentication-authorization-foundry]

Prompt Flow is now a legacy transition surface rather than the forward path, and Microsoft's current strategic direction is agent-centric development through Agent Service, workflows, project endpoints, and Microsoft Agent Framework. [fact; source: https://learn.microsoft.com/en-us/azure/foundry-classic/concepts/prompt-flow; https://learn.microsoft.com/en-us/azure/foundry-classic/how-to/how-to-migrate-prompt-flow-to-agent-framework; https://learn.microsoft.com/en-us/azure/foundry/agents/overview]

For a regulated enterprise, Microsoft Foundry is best treated as a strong Azure-native AI application factory, not as a self-sufficient governance plane, because identity, search, storage, compliance, and tenant-wide Copilot controls still require surrounding Azure and Microsoft 365 governance layers. [inference; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture; https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link; https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/publish-copilot; https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html]

### Key Findings

1. **Microsoft Foundry consolidates the former Azure AI Studio and Azure AI Foundry experience into a single resource and project model, and Microsoft can upgrade Azure OpenAI resources in place without changing existing Azure OpenAI endpoints, keys, or saved state.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/foundry/what-is-ai-foundry; https://learn.microsoft.com/en-us/azure/foundry/how-to/upgrade-azure-openai; https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture)
2. **The model catalogue is broad and practically useful, because Microsoft documents more than 1,900 models, side-by-side comparison, public-benchmark leaderboards, model cards, deployment tabs, and filterable deployment and licence metadata within the same discovery surface.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview; https://learn.microsoft.com/en-us/azure/foundry/concepts/model-benchmarks; https://learn.microsoft.com/en-us/azure/machine-learning/foundry-models-overview?view=azureml-api-2)
3. **Microsoft Foundry supports meaningful native model customisation, especially Low-Rank Adaptation (LoRA) based fine-tuning and selected optimization methods, but customization support is narrower than catalogue support and some partner or open-model paths still depend on managed compute or classic-era deployment patterns.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/fine-tuning; https://learn.microsoft.com/en-us/azure/foundry/concepts/deployments-overview; https://learn.microsoft.com/en-us/azure/machine-learning/foundry-models-overview?view=azureml-api-2)
4. **The development stack is now decisively agent-centric, combining prompt agents, workflow agents, hosted agents, tool catalogues, memory, Foundry IQ, Microsoft's managed knowledge layer, unified SDKs, and playgrounds, while Prompt Flow remains only as a legacy classic feature with retirement and migration guidance already published.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/foundry/agents/overview; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/workflow; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog; https://learn.microsoft.com/en-us/azure/foundry-classic/concepts/prompt-flow; https://learn.microsoft.com/en-us/azure/foundry-classic/how-to/how-to-migrate-prompt-flow-to-agent-framework)
5. **Evaluation and observability are first-class platform features, because Microsoft documents lifecycle evaluation from benchmark-driven model selection through agent testing, continuous evaluation, dashboard monitoring, OpenTelemetry tracing, and automated red-teaming, even though some runtime-inspection paths remain preview.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/observability; https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/evaluate-agent; https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept; https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard)
6. **Deployment and serving flexibility are broad for a managed platform, because Microsoft Foundry supports standard, provisioned, batch, data-zone, regional, and managed-compute serving patterns, but that same flexibility pushes architects to make explicit data-residency, quota, and cost-governance decisions.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/deployments-overview; https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types; https://learn.microsoft.com/en-us/azure/foundry/reference/region-support; https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs)
7. **Microsoft Foundry has serious enterprise-governance machinery, including Microsoft Entra identity, Foundry RBAC roles, Private Link, bring-your-own-storage, guardrails, task-adherence checks, and Control Plane fleet views, but those controls remain distributed across Foundry, connected Azure resources, and several preview-only surfaces.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/authentication-authorization-foundry; https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry; https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link; https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview; https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview)
8. **Microsoft Foundry integrates well with Azure OpenAI, Azure Machine Learning (Azure ML), Azure AI Search, OneLake, and Microsoft Copilot surfaces, but those integrations make the platform more useful as a developer-side AI application factory than as a complete enterprise governance plane in its own right.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/foundry/how-to/upgrade-azure-openai; https://learn.microsoft.com/en-us/azure/machine-learning/foundry-models-overview?view=azureml-api-2; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq; https://learn.microsoft.com/en-us/fabric/onelake/onelake-foundry-knowledge; https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/publish-copilot)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Microsoft Foundry consolidates the former Azure AI Studio and Azure AI Foundry experience into one resource and project model while preserving Azure OpenAI upgrade continuity. | https://learn.microsoft.com/en-us/azure/foundry/what-is-ai-foundry ; https://learn.microsoft.com/en-us/azure/foundry/how-to/upgrade-azure-openai ; https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture | medium | Current platform identity |
| [inference] The model catalogue is broad enough for practical selection work because it spans more than 1,900 models and includes compare, benchmark, and filtered deployment-selection surfaces. | https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview ; https://learn.microsoft.com/en-us/azure/foundry/concepts/model-benchmarks ; https://learn.microsoft.com/en-us/azure/machine-learning/foundry-models-overview?view=azureml-api-2 | medium | Discovery and selection |
| [inference] Native customization is real but narrower than catalogue breadth because selected methods and models are supported while other model paths still use managed compute or classic patterns. | https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/fine-tuning ; https://learn.microsoft.com/en-us/azure/foundry/concepts/deployments-overview ; https://learn.microsoft.com/en-us/azure/machine-learning/foundry-models-overview?view=azureml-api-2 | medium | Customization asymmetry |
| [inference] The active development direction is agent-centric and Prompt Flow is a legacy classic capability with published retirement and migration guidance. | https://learn.microsoft.com/en-us/azure/foundry/agents/overview ; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/workflow ; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog ; https://learn.microsoft.com/en-us/azure/foundry-classic/concepts/prompt-flow ; https://learn.microsoft.com/en-us/azure/foundry-classic/how-to/how-to-migrate-prompt-flow-to-agent-framework | medium | Build-surface transition |
| [inference] Evaluation and observability are first-class platform features, but some of the deepest runtime-inspection paths still depend on preview and Application Insights setup. | https://learn.microsoft.com/en-us/azure/foundry/concepts/observability ; https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/evaluate-agent ; https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept ; https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard | medium | Strong but not fully uniform |
| [inference] Deployment flexibility is strong, but compliance and cost behavior depend on explicit deployment-type and region decisions rather than one default secure serving mode. | https://learn.microsoft.com/en-us/azure/foundry/concepts/deployments-overview ; https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types ; https://learn.microsoft.com/en-us/azure/foundry/reference/region-support ; https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs | medium | Serving trade-offs |
| [inference] Enterprise-governance machinery is substantial but distributed across Foundry, connected Azure resources, and several preview-only surfaces. | https://learn.microsoft.com/en-us/azure/foundry/concepts/authentication-authorization-foundry ; https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry ; https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link ; https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview ; https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview | medium | Governance fragmentation |
| [inference] Microsoft Foundry integrates well with Azure and Copilot-adjacent services, but it remains better framed as an AI application factory than as a complete enterprise governance plane. | https://learn.microsoft.com/en-us/azure/foundry/how-to/upgrade-azure-openai ; https://learn.microsoft.com/en-us/azure/machine-learning/foundry-models-overview?view=azureml-api-2 ; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq ; https://learn.microsoft.com/en-us/fabric/onelake/onelake-foundry-knowledge ; https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/publish-copilot ; https://davidamitchell.github.io/Research/research/2026-05-02-ms-copilot-vs-aws-bedrock-enterprise-ai-capability-model.html | medium | Integration boundary |

### Assumptions

- Preview features are counted as existing capabilities but not as production-grade baseline controls because Microsoft publishes them in current documentation while also disclaiming service-level agreements and full support. [assumption; source: https://learn.microsoft.com/en-us/azure/foundry/agents/overview; https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview; https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview]
- Azure Machine Learning (Azure ML) integration is assessed only at the documented Microsoft Foundry model-catalogue and deployment surface, not at the level of general Azure ML workspace feature parity, because that broader Azure ML scope is out of scope for this item. [assumption; source: https://learn.microsoft.com/en-us/azure/machine-learning/foundry-models-overview?view=azureml-api-2; https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture]
- This survey treats Microsoft documentation as authoritative for product-capability claims and does not infer undocumented feature parity across every region or every model family. [assumption; source: https://learn.microsoft.com/en-us/azure/foundry/reference/region-support; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/limits-quotas-regions]

### Analysis

Microsoft's documentation supports a direct answer that Microsoft Foundry is already broad enough to cover most lifecycle stages natively, so the platform is not limited to model hosting or playground experimentation. [inference; source: https://learn.microsoft.com/en-us/azure/foundry/what-is-ai-foundry; https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview; https://learn.microsoft.com/en-us/azure/foundry/concepts/observability]

The stronger competing interpretation is that Microsoft Foundry is now a complete enterprise AI control plane, but the architecture, networking, identity, storage, and publish-to-Copilot documents do not support that stronger claim because multiple essential governance surfaces remain outside the Foundry resource itself. [inference; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture; https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link; https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/publish-copilot]

Another plausible rival interpretation is that the platform is still mostly Azure OpenAI with new branding, but the agent runtime, workflow builder, Foundry IQ knowledge layer, Control Plane, and unified project endpoint together show a materially broader application platform than standalone Azure OpenAI provided. [inference; source: https://learn.microsoft.com/en-us/azure/foundry/agents/overview; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/workflow; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq; https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview]

The best-supported conclusion is therefore narrower and more decision-useful: Microsoft Foundry is a strong Azure-native build, test, deploy, and operate platform for AI applications, but regulated enterprises still need explicit surrounding governance for connected data sources, tenant administration, identity, and release policy. [inference; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/authentication-authorization-foundry; https://learn.microsoft.com/en-us/azure/foundry/how-to/connections-add; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html]

### Risks, Gaps, and Uncertainties

- Several of the most ambitious management surfaces, including parts of Control Plane, workflow and hosted-agent support, publish-to-Copilot, toolbox, and some tracing and guardrail behaviors, are still preview, which means production commitments and operational stability are not yet equivalent across the whole stack. [fact; source: https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview; https://learn.microsoft.com/en-us/azure/foundry/agents/overview; https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/publish-copilot; https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept]
- Microsoft's public documentation describes model families, regions, and quotas as moving targets, so any procurement or architecture decision still needs a live region and quota check in the target subscription before deployment. [fact; source: https://learn.microsoft.com/en-us/azure/foundry/reference/region-support; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/limits-quotas-regions]
- The survey establishes breadth of documented capability more strongly than day-two operational maturity, because many documents describe setup and feature availability rather than large-scale reference operations in tightly regulated production estates. [inference; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs; https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview; https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard]

### Open Questions

- Which Microsoft Foundry preview surfaces reach general availability first, specifically Control Plane governance panes, hosted-agent observability, and publish-to-Copilot?
- How much of current Microsoft Agent Framework functionality eventually becomes a managed Microsoft Foundry surface rather than remaining an external code framework?
- How much operational evidence will Microsoft publish on large regulated-enterprise deployments using DataZone, private networking, Foundry IQ, and preview governance controls together?

---

## Output

- Type: knowledge
- Description: Microsoft Foundry is already a broad Azure-native lifecycle platform for AI applications, but its strongest regulated-enterprise use requires surrounding governance across identity, connected data, tenant administration, and preview management. [inference; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture; https://learn.microsoft.com/en-us/azure/foundry/concepts/authentication-authorization-foundry; https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview]
- Links:
  - https://learn.microsoft.com/en-us/azure/foundry/what-is-ai-foundry
  - https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview
  - https://learn.microsoft.com/en-us/azure/foundry/concepts/observability
