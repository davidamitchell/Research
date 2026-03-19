---
title: "GitAgent and declarative agent definition: concepts, adoption, and cross-platform integration"
added: 2026-03-16
status: reviewing
priority: high
blocks: []
tags: [agent, declarative-agent, gitagent, copilot, aws, azure, microsoft-365, git, ai-platform, multi-agent]
started: 2026-03-19
completed: ~
output: [knowledge, backlog-item]
---

# GitAgent and declarative agent definition: concepts, adoption, and cross-platform integration

## Research Question

What is GitAgent (https://github.com/open-gitagent/gitagent), how can it be used in this repository, what concepts does it build on and produce, and how does the broader idea of declarative agent definition apply across Microsoft 365 (M365) Copilot, Amazon Web Services (AWS) Agent Core, and the Azure agentic platform?

Supporting questions:
- What is GitAgent, what problem does it solve, and what is its architecture?
- What concepts (for example declarative agent manifests, tool use, event-driven triggers, policy-as-code) does GitAgent build on?
- How could GitAgent be adopted or integrated in this repository's research tooling?
- How does the declarative agent definition pattern manifest across Microsoft 365 (M365) Copilot extensions, AWS Agent Core, and Azure Artificial Intelligence (AI) Agent Service, and what are the similarities and differences?
- What is the general declarative agent definition concept, and what prior art or standards does it draw from (for example OpenAI plugin manifests, Model Context Protocol (MCP), and OpenAPI Specification (OAS) documents)?

## Scope

**In scope:**
- GitAgent repository: architecture, manifest format, key concepts, and usage patterns
- Declarative agent definition as a design pattern: what it means to describe an agent's capabilities, tools, triggers, and policies in a configuration file rather than in code
- Microsoft 365 (M365) Copilot: declarative agent extensions, Teams Artificial Intelligence (AI) Library, Graph connectors, and the Copilot Studio declarative agent manifest format
- AWS Agent Core: Amazon Bedrock Agents, agent action groups, knowledge bases, and how agents are declared via CloudFormation and Cloud Development Kit (CDK) style infrastructure vs. code-first approaches
- Azure Artificial Intelligence (AI) Foundry / Azure Artificial Intelligence (AI) Agent Service: agent definitions, Azure Artificial Intelligence (AI) Studio agent builder, and Semantic Kernel agent framework
- Cross-platform comparison: what is portable, what is platform-specific, and what standards bridge the platforms
- How GitAgent relates to or uses Git as a trigger or event source for agents

**Out of scope:**
- Low-level Large Language Model (LLM) fine-tuning or training
- Pricing and commercial comparisons
- Identity and access management implementation details for each platform beyond what is needed to understand agent authentication
- General prompt engineering not specific to declarative agent definitions

**Constraints:** Prefer primary sources such as official documentation, GitHub repositories, and published specifications. GitAgent is an open-source project, so inspect the repository directly. For Microsoft 365, AWS, and Azure, prefer official documentation from 2024-2026 to capture current state.

## Context

The issue asks two interrelated questions: (1) what GitAgent is and how it can be used here; and (2) what the general pattern of declarative agent definition looks like across major agentic platforms. These belong together because GitAgent appears to be a Git-native instance of the broader declarative agent pattern.

This repository already uses GitHub Actions workflows and the Model Context Protocol (MCP) for agent tooling. Sources: https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml ; https://github.com/davidamitchell/Research/blob/main/.github/mcp.json

Understanding GitAgent may reveal integration opportunities, such as packaging the repository's skills, tools, and workflows into a portable agent definition instead of leaving them entirely as repository-specific conventions. Understanding the cross-platform landscape also informs decisions about whether future research agents should remain repository-local or be surfaced through Microsoft 365 Copilot, Amazon Bedrock, Azure Foundry, or OpenAI-compatible runtimes.

The declarative agent definition concept matters because it separates an agent's identity, instructions, tools, knowledge sources, and governance rules from any one execution runtime. That separation can improve portability, reviewability, and auditability, but only if the underlying platform keeps enough of the agent definition in machine-readable form.

## Approach

1. **Inspect GitAgent** - inspect the repository, README, specification, and comparison docs. Identify what runtime executes the agent, what the manifest declares, what optional files add, and what the Command Line Interface (CLI) can export or run.
2. **Declarative agent definition taxonomy** - survey the concept across platforms: Microsoft 365 Copilot declarative agent manifest, AWS Bedrock Agent resources and action groups, Azure Foundry prompt and workflow agents, and OpenAI tool definitions.
3. **Standards and prior art** - trace the genealogy of declarative agent definitions: OpenAI plugin manifests, OpenAPI Specification (OAS), Model Context Protocol (MCP), and newer tool declaration formats.
4. **GitAgent x this repository** - compare GitAgent's expected structure with this repository's actual structure, skills, Model Context Protocol (MCP) configuration, workflows, and memory or state files.
5. **Cross-platform integration** - identify what is portable across Microsoft 365 Copilot, AWS, Azure, and OpenAI-compatible runtimes and what remains vendor-specific.
6. **Synthesis** - produce a cross-platform comparison and an actionable recommendation for this repository.

## Sources

- [x] https://github.com/open-gitagent/gitagent - GitAgent repository inspected locally via a fresh clone on 2026-03-19.
- [x] https://raw.githubusercontent.com/open-gitagent/gitagent/main/README.md - GitAgent README.
- [x] https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md - GitAgent specification.
- [x] https://raw.githubusercontent.com/open-gitagent/gitagent/main/docs/comparison.md - GitAgent comparison document.
- [x] https://api.github.com/repos/open-gitagent/gitagent - GitAgent repository metadata for age and adoption signal.
- [x] https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/agents-overview.md - Microsoft 365 Copilot agents overview source markdown.
- [x] https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/overview-declarative-agent.md - Microsoft 365 Copilot declarative agents overview source markdown.
- [x] https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md - Microsoft 365 Copilot declarative agent manifest schema 1.6.
- [x] https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/plugin-manifest-2.4.md - Microsoft 365 Copilot plugin manifest schema 2.4.
- [x] https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/includes/sample-manifests/declarative-agent-sample-manifest-1.6.json - sample declarative agent manifest.
- [x] https://learn.microsoft.com/en-us/azure/foundry/agents/overview - Foundry Agent Service overview.
- [x] https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog - Foundry tool catalog.
- [x] https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html - Agents for Amazon Bedrock.
- [x] https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html - Amazon Bedrock action groups.
- [x] https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html - CloudFormation `AWS::Bedrock::Agent` resource.
- [x] https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrock-agent-agentactiongroup.html - CloudFormation `AgentActionGroup` resource.
- [x] https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html - Amazon Bedrock AgentCore overview.
- [x] https://modelcontextprotocol.io - Model Context Protocol (MCP) overview.
- [x] https://developers.openai.com/api/docs/assistants/tools/ - deprecated Assistants API tools page.
- [x] https://developers.openai.com/api/docs/guides/tools?api-mode=responses - current Responses API tools guide.
- [x] https://developers.openai.com/api/docs/guides/tools-remote-mcp - OpenAI remote Model Context Protocol (MCP) guide.
- [x] https://raw.githubusercontent.com/openai/plugins-quickstart/main/.well-known/ai-plugin.json - OpenAI plugin manifest example.
- [x] https://raw.githubusercontent.com/openai/plugins-quickstart/main/openapi.yaml - OpenAI plugin OpenAPI example.
- [x] https://github.com/davidamitchell/Research/blob/main/.github/mcp.json - repository MCP configuration.
- [x] https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml - repository research loop workflow.
- [x] https://github.com/davidamitchell/Research/blob/main/README.md - repository top-level structure.
- [x] https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-self-hosted-mcp-server-options.md - prior completed item on self-hosted MCP deployment.
- [x] https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md - prior completed item on agent harness philosophy and MCP.
- [x] https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-claude-ios-mcp-remote-integration.md - prior completed item on remote MCP transport and clients.
- [ ] https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore/ - listed in the brief, but returned HTTP 404 on 2026-03-19; replaced with the official AgentCore developer guide.
- [ ] https://platform.openai.com/docs/assistants/overview - listed in the brief, but current official documentation split the material across the deprecated Assistants tools page and the newer Responses tools guides.
- [ ] https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agents-overview - rendered page required authorization in this environment; used public source markdown instead.
- [ ] https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/declarative-agent-manifest - rendered page required authorization in this environment; used public source markdown for schema 1.6 instead.

---

## Research Skill Output

### §0 Initialise

- **[fact]** The central question is whether GitAgent is a useful declarative agent definition standard for this repository, and how its model compares with Microsoft 365 Copilot, Amazon Web Services (AWS), Azure Foundry, and OpenAI tool-definition patterns. Source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-03-16-gitagent-declarative-agent-definition.md
- **[fact]** The requested output is a full-mode research item with sections §0-§7, followed by a structured Findings section seeded from §6. Sources: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-03-16-gitagent-declarative-agent-definition.md ; https://github.com/davidamitchell/Research/blob/main/.github/skills/research/SKILL.md
- **[fact]** The scope explicitly includes GitAgent internals, declarative agent manifests, Microsoft 365 Copilot declarative agents, Amazon Bedrock and AgentCore, Azure Foundry Agent Service, and prior-art standards such as Model Context Protocol (MCP) and OpenAPI Specification (OAS). Source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-03-16-gitagent-declarative-agent-definition.md
- **[fact]** Prior completed items already established that this repository uses Model Context Protocol (MCP) as an integration layer and GitHub Actions as the operational control plane for agent work. Sources: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-self-hosted-mcp-server-options.md ; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml
- **[inference]** This item therefore extends prior work from "how do agents call tools?" into "how should an agent be packaged and described so the same identity can travel across runtimes?" Sources: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md

### §1 Question Decomposition

1. GitAgent itself
   1.1 What does GitAgent claim to be?
   1.2 What files and directories define a GitAgent agent?
   1.3 Which fields are required in `agent.yaml`, and which are optional?
   1.4 What does GitAgent export, validate, or run through adapters and its Command Line Interface (CLI)?
   1.5 What evidence exists about GitAgent maturity and adoption?
2. Declarative agent definition as a general pattern
   2.1 Which agent attributes are consistently captured declaratively across platforms?
   2.2 Which parts remain runtime-specific or imperative?
3. Microsoft 365 Copilot
   3.1 What does a declarative agent manifest contain?
   3.2 How are actions, plugins, and Model Context Protocol (MCP) connections represented?
   3.3 Which responsibilities stay inside Microsoft-hosted orchestration?
4. Amazon Web Services (AWS)
   4.1 What does an Amazon Bedrock Agent resource declare?
   4.2 How are action groups, knowledge bases, memory, and guardrails attached?
   4.3 How does Amazon Bedrock AgentCore differ from Bedrock Agents?
5. Azure Foundry
   5.1 What is the difference between prompt agents, workflow agents, and hosted agents?
   5.2 How are tools declared, especially Model Context Protocol (MCP), OpenAPI Specification (OAS), and Agent-to-Agent (A2A) endpoints?
6. OpenAI prior art and bridges
   6.1 What did OpenAI plugin manifests contribute as prior art?
   6.2 What is the current OpenAI pattern in the Responses API?
7. Repository fit
   7.1 Which GitAgent concepts already exist in this repository under different names?
   7.2 What would GitAgent improve here?
   7.3 What would GitAgent not replace?

### §2 Investigation

#### Source register

**Consulted**
- [x] https://raw.githubusercontent.com/open-gitagent/gitagent/main/README.md
- [x] https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md
- [x] https://raw.githubusercontent.com/open-gitagent/gitagent/main/docs/comparison.md
- [x] https://api.github.com/repos/open-gitagent/gitagent
- [x] https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/agents-overview.md
- [x] https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/overview-declarative-agent.md
- [x] https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md
- [x] https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/plugin-manifest-2.4.md
- [x] https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/includes/sample-manifests/declarative-agent-sample-manifest-1.6.json
- [x] https://learn.microsoft.com/en-us/azure/foundry/agents/overview
- [x] https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog
- [x] https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html
- [x] https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- [x] https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html
- [x] https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrock-agent-agentactiongroup.html
- [x] https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- [x] https://modelcontextprotocol.io
- [x] https://developers.openai.com/api/docs/assistants/tools/
- [x] https://developers.openai.com/api/docs/guides/tools?api-mode=responses
- [x] https://developers.openai.com/api/docs/guides/tools-remote-mcp
- [x] https://raw.githubusercontent.com/openai/plugins-quickstart/main/.well-known/ai-plugin.json
- [x] https://raw.githubusercontent.com/openai/plugins-quickstart/main/openapi.yaml
- [x] https://github.com/davidamitchell/Research/blob/main/.github/mcp.json
- [x] https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml
- [x] https://github.com/davidamitchell/Research/blob/main/README.md
- [x] https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-self-hosted-mcp-server-options.md
- [x] https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md
- [x] https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-claude-ios-mcp-remote-integration.md

**Identified but not consulted**
- [ ] https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore/ - returned HTTP 404 in this environment.
- [ ] https://platform.openai.com/docs/assistants/overview - superseded by accessible current guides.
- [ ] https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agents-overview - rendered page required authorization.
- [ ] https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/declarative-agent-manifest - rendered page required authorization.

#### Q1. What is GitAgent, and what problem does it solve?

- **[fact]** GitAgent describes itself as "a framework-agnostic, git-native standard for defining AI agents" and summarizes its value proposition as "Clone a repo, get an agent." Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/README.md ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md
- **[fact]** GitAgent's required files are `agent.yaml` and `SOUL.md`; optional directories and files include `RULES.md`, `DUTIES.md`, `AGENTS.md`, `skills/`, `tools/`, `knowledge/`, `memory/`, `workflows/`, `hooks/`, `agents/`, `compliance/`, and `config/`. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/README.md ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md
- **[fact]** The strict schema lives in `agent.yaml`, where required fields are `name`, `version`, and `description`, and optional fields include `model`, `extends`, `dependencies`, `skills`, `tools`, `agents`, `delegation`, `runtime`, `a2a`, `compliance`, `tags`, and `metadata`. Source: https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md
- **[fact]** GitAgent exposes a Command Line Interface (CLI) that can initialize agents, validate them, export them to other targets, import from some targets, run them through adapters, audit compliance, and manage skills. Source: https://raw.githubusercontent.com/open-gitagent/gitagent/main/README.md
- **[fact]** GitAgent's own comparison document says runtime orchestration, live tool execution, memory input and output, and iterative loops stay in the target framework, while the portable layer carries prompts, rules, tool schemas, role policies, and metadata. Source: https://raw.githubusercontent.com/open-gitagent/gitagent/main/docs/comparison.md
- **[inference]** GitAgent therefore solves the packaging, portability, and governance problem more directly than the runtime problem: it standardizes the agent's identity and interfaces, but does not abolish the need for framework-specific execution logic. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/README.md ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/docs/comparison.md

#### Q2. What is GitAgent's maturity and adoption level?

- **[fact]** GitHub repository metadata on 2026-03-19 showed `open-gitagent/gitagent` was created on 2026-02-24, had 563 stars, 45 forks, and 13 open issues, and still advertised spec version `0.1.0`. Sources: https://api.github.com/repos/open-gitagent/gitagent ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/README.md
- **[inference]** The project shows meaningful early interest but not long-run maturity, because the repository is less than one month old and the published specification remains at `0.1.0`. Sources: https://api.github.com/repos/open-gitagent/gitagent ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md

#### Q3. What is the general declarative agent definition pattern?

- **[fact]** Microsoft's manifest documentation says a declarative agent manifest is a machine-readable document that gives a Large Language Model (LLM) the instructions, knowledge, and actions needed to specialize on a set of user problems. Source: https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md
- **[fact]** Azure Foundry says each agent combines a model, instructions, and tools, and that prompt agents are defined entirely through configuration while workflow agents can be expressed declaratively. Source: https://learn.microsoft.com/en-us/azure/foundry/agents/overview
- **[fact]** Amazon Bedrock exposes agent declaration through service and infrastructure resources that capture the agent name, model, instruction, action groups, knowledge bases, memory, orchestration type, and guardrails. Sources: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html ; https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html
- **[fact]** OpenAI's current Responses API guide says developers configure built-in tools, function calling, tool search, and remote Model Context Protocol (MCP) servers through the `tools` parameter of the request payload. Sources: https://developers.openai.com/api/docs/guides/tools?api-mode=responses ; https://developers.openai.com/api/docs/guides/tools-remote-mcp
- **[inference]** Across vendors, the common declarative core is a machine-readable description of an agent's instructions, capabilities, knowledge access, and guardrails, while the main point of variation is the unit of declaration: repository, app package, cloud resource, workflow file, or request payload. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md ; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html ; https://learn.microsoft.com/en-us/azure/foundry/agents/overview ; https://developers.openai.com/api/docs/guides/tools?api-mode=responses

#### Q4. How does Microsoft 365 Copilot represent declarative agents?

- **[fact]** Microsoft 365 Copilot distinguishes declarative agents from custom engine agents; declarative agents use Copilot's own orchestrator and foundation models and require no additional hosting. Sources: https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/agents-overview.md ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/overview-declarative-agent.md
- **[fact]** Manifest schema 1.6 defines root properties including `version`, `id`, `name`, `description`, `instructions`, `capabilities`, `conversation_starters`, `actions`, `behavior_overrides`, `disclaimer`, `sensitivity_label`, `worker_agents`, and `user_overrides`. Source: https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md
- **[fact]** The sample schema 1.6 manifest shows capabilities such as `WebSearch`, `OneDriveAndSharePoint`, `GraphConnectors`, `CodeInterpreter`, `TeamsMessages`, `Email`, `People`, `ScenarioModels`, `Meetings`, and `EmbeddedKnowledge`, alongside `actions` that reference a plugin manifest file. Source: https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/includes/sample-manifests/declarative-agent-sample-manifest-1.6.json
- **[fact]** Plugin manifest schema 2.4 says plugins can interact with Model Context Protocol (MCP) servers or Representational State Transfer (REST) Application Programming Interfaces (APIs) described by an OpenAPI description, and introduces a `RemoteMCPServer` runtime type. Source: https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/plugin-manifest-2.4.md
- **[inference]** Microsoft's declarative layer is powerful inside the Microsoft ecosystem, but its portability depends on the plugin boundary rather than on the declarative agent manifest itself, because the manifest is tied to app packages, Microsoft capabilities, and Copilot-hosted orchestration. Sources: https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/plugin-manifest-2.4.md

#### Q5. How do Amazon Bedrock Agents and Amazon Bedrock AgentCore represent agents?

- **[fact]** Amazon Bedrock says an agent orchestrates interactions between foundation models, data sources, software applications, and user conversations, and can automatically call APIs and knowledge bases. Source: https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html
- **[fact]** The `AWS::Bedrock::Agent` resource captures action groups, collaborators, description, foundation model, instruction, knowledge bases, memory configuration, orchestration type, custom orchestration, guardrails, and prompt overrides. Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html
- **[fact]** An `AgentActionGroup` can declare an OpenAPI-backed `ApiSchema`, a `FunctionSchema`, a Lambda executor, or special signatures such as `AMAZON.UserInput` and `AMAZON.CodeInterpreter`. Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrock-agent-agentactiongroup.html
- **[fact]** Amazon Bedrock AgentCore is a modular platform with Runtime, Memory, Gateway, Identity, Code Interpreter, Browser, Observability, Evaluations, and Policy services; AgentCore Gateway can convert APIs, Lambda functions, and services into Model Context Protocol (MCP)-compatible tools. Source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- **[inference]** Bedrock Agents and AgentCore complement each other but solve different layers: Bedrock Agents define a managed agent resource, whereas AgentCore supplies a broader runtime and governance substrate that can host agents built with many frameworks. Sources: https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html ; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html

#### Q6. How does Azure Foundry represent agents and tools?

- **[fact]** Foundry Agent Service describes itself as a fully managed platform for building, deploying, and scaling agents, and it supports prompt agents, workflow agents, and hosted agents. Source: https://learn.microsoft.com/en-us/azure/foundry/agents/overview
- **[fact]** Prompt agents are defined through configuration consisting of instructions, model selection, and tools; workflow agents are declarative multi-step orchestrations that can be built visually or in YAML Ain't Markup Language (YAML); hosted agents are code-based containers. Source: https://learn.microsoft.com/en-us/azure/foundry/agents/overview
- **[fact]** Foundry's tool catalog includes built-in tools such as web search, code interpreter, file search, and function calling, plus custom tools via Model Context Protocol (MCP), OpenAPI, and Agent-to-Agent (A2A) endpoints. Source: https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog
- **[fact]** Foundry documentation shows agent creation through a `PromptAgentDefinition` object that includes `model`, `instructions`, and a `tools` list, and it supports structured inputs for runtime substitution of values such as vector store identifiers, Model Context Protocol (MCP) server URLs, and headers. Source: https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog
- **[inference]** Azure combines declarative single-agent and workflow patterns more explicitly than Microsoft 365 Copilot or Bedrock, but the resulting definitions still live inside an Azure-managed platform rather than a runtime-agnostic repository standard. Sources: https://learn.microsoft.com/en-us/azure/foundry/agents/overview ; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog

#### Q7. What prior art and current patterns come from OpenAI?

- **[fact]** The OpenAI plugin quickstart `ai-plugin.json` includes schema version, names for humans and models, descriptions, authentication, an `api` block of type `openapi`, logo URL, contact email, and legal information URL. Source: https://raw.githubusercontent.com/openai/plugins-quickstart/main/.well-known/ai-plugin.json
- **[fact]** The accompanying `openapi.yaml` defines the callable operations by `operationId`, path, method, parameters, request body schema, and response schema. Source: https://raw.githubusercontent.com/openai/plugins-quickstart/main/openapi.yaml
- **[fact]** OpenAI's Assistants Application Programming Interface (API) tools page now states that the Assistants Application Programming Interface (API) has been deprecated and will shut down on 2026-08-26 after feature parity in the Responses Application Programming Interface (API). Source: https://developers.openai.com/api/docs/assistants/tools/
- **[fact]** The current Responses tools guide says developers declaratively enable function calling, web search, file search, skills, shell, computer use, image generation, tool search, and remote Model Context Protocol (MCP) servers via the `tools` parameter. Sources: https://developers.openai.com/api/docs/guides/tools?api-mode=responses ; https://developers.openai.com/api/docs/guides/tools-remote-mcp
- **[fact]** The remote Model Context Protocol (MCP) guide shows an `mcp` tool definition that includes `server_label`, `server_description`, `server_url`, `require_approval`, and `allowed_tools`, and the service materializes `mcp_list_tools` and `mcp_call` items at runtime. Source: https://developers.openai.com/api/docs/guides/tools-remote-mcp
- **[inference]** OpenAI has preserved the declarative idea while changing its shape: older plugin manifests packaged capabilities as files, while current Responses requests package capabilities as tool objects bound at request time. Sources: https://raw.githubusercontent.com/openai/plugins-quickstart/main/.well-known/ai-plugin.json ; https://developers.openai.com/api/docs/guides/tools?api-mode=responses

#### Q8. Which standards bridge platforms most effectively?

- **[fact]** The Model Context Protocol (MCP) site describes MCP as an open-source standard for connecting artificial intelligence applications to external systems and says it is supported by clients including Claude, ChatGPT, Visual Studio Code, and Cursor. Source: https://modelcontextprotocol.io
- **[fact]** Microsoft plugin manifest schema 2.4 added explicit support for `RemoteMCPServer` runtimes. Source: https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/plugin-manifest-2.4.md
- **[fact]** Azure Foundry supports Model Context Protocol (MCP) tools and OpenAPI tools in the same tool catalog. Source: https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog
- **[fact]** Amazon Bedrock AgentCore Gateway converts existing APIs, Lambda functions, and services into Model Context Protocol (MCP)-compatible tools. Source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- **[fact]** OpenAI's Responses API supports remote Model Context Protocol (MCP) servers as an `mcp` tool type. Source: https://developers.openai.com/api/docs/guides/tools-remote-mcp
- **[inference]** Model Context Protocol (MCP) is the strongest current bridge for portable tool invocation, while OpenAPI Specification (OAS) remains the strongest bridge for Hypertext Transfer Protocol (HTTP) action surfaces; vendor-specific agent manifests themselves do not port cleanly across ecosystems. Sources: https://modelcontextprotocol.io ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/plugin-manifest-2.4.md ; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog ; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrock-agent-agentactiongroup.html ; https://developers.openai.com/api/docs/guides/tools-remote-mcp

#### Q9. How could GitAgent fit this repository?

- **[fact]** This repository already exposes reusable skills, Model Context Protocol (MCP) server configuration, GitHub Actions workflows, research knowledge artifacts, and persistent state or session artifacts through `.github/skills`, `.github/mcp.json`, `.github/workflows/research-loop.yml`, `Research/`, `progress/`, and `state/`. Sources: https://github.com/davidamitchell/Research/blob/main/.github/mcp.json ; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml ; https://github.com/davidamitchell/Research/blob/main/README.md
- **[fact]** The research loop currently executes by invoking the GitHub Copilot Command Line Interface (CLI) from GitHub Actions with repository secrets, Python tooling, and repository-specific state transitions. Source: https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml
- **[inference]** The repository already contains most of the semantic ingredients that GitAgent expects, but they are organized as repository conventions rather than as a single portable agent definition rooted in `agent.yaml`. Sources: https://github.com/davidamitchell/Research/blob/main/README.md ; https://github.com/davidamitchell/Research/blob/main/.github/mcp.json ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md
- **[inference]** A plausible adoption path is to add GitAgent as a portability and governance layer: define `agent.yaml`, `SOUL.md`, `RULES.md`, and `DUTIES.md`; map current skills and Model Context Protocol (MCP) tools into GitAgent-compatible locations; and optionally export derived artifacts for Claude Code, GitHub Copilot, or OpenAI runtimes. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/README.md ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md ; https://github.com/davidamitchell/Research/blob/main/.github/mcp.json ; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml
- **[inference]** GitAgent should not replace the current research loop outright, because the loop's scheduling, retries, repository mutation rules, and direct GitHub Actions integration are operational logic that GitAgent would still need custom adapters or wrappers to invoke. Sources: https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/docs/comparison.md
- **[assumption]** The repository owner values cross-runtime portability enough to justify an additional definition layer, because the prompt explicitly asks how the same conceptual agent could apply across Microsoft 365 Copilot, AWS, Azure, and Git-native workflows. Source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-03-16-gitagent-declarative-agent-definition.md

### §3 Reasoning

- **[fact]** GitAgent, Microsoft 365 Copilot, Amazon Bedrock, Azure Foundry, and OpenAI all expose a machine-readable layer for at least part of the agent definition. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md ; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html ; https://learn.microsoft.com/en-us/azure/foundry/agents/overview ; https://developers.openai.com/api/docs/guides/tools?api-mode=responses
- **[inference]** I treat these as members of the same design family because each separates descriptive metadata from at least some runtime execution logic, even though the declaration unit differs across platforms. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md ; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html ; https://developers.openai.com/api/docs/guides/tools?api-mode=responses
- **[inference]** I do not treat Amazon Bedrock AgentCore or Azure hosted agents as portable declarative standards in themselves, because their value lies in managed execution, security, and observability rather than in a reusable cross-runtime manifest. Sources: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html ; https://learn.microsoft.com/en-us/azure/foundry/agents/overview
- **[assumption]** A packaging layer is only worth adding here if it improves portability, reviewability, or governance more than it increases maintenance burden. Source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-03-16-gitagent-declarative-agent-definition.md
- **[inference]** On current evidence, the strongest portable substrate is not a single universal agent manifest but a combination of a repository-level definition plus shared tool protocols such as Model Context Protocol (MCP) and OpenAPI Specification (OAS). Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md ; https://modelcontextprotocol.io ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/plugin-manifest-2.4.md ; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog

### §4 Consistency Check

- **[fact]** Terminology conflict resolved: GitAgent is a repository-level standard and adapter ecosystem, while Amazon Bedrock AgentCore and Azure Foundry hosted agents are managed runtime platforms. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html ; https://learn.microsoft.com/en-us/azure/foundry/agents/overview
- **[fact]** Chronology conflict resolved: OpenAI's Assistants Application Programming Interface (API) is now deprecated, so current OpenAI evidence must rely primarily on the Responses Application Programming Interface (API) tools guides, with the Assistants page treated as legacy context. Sources: https://developers.openai.com/api/docs/assistants/tools/ ; https://developers.openai.com/api/docs/guides/tools?api-mode=responses
- **[fact]** Access conflict resolved: Microsoft Learn rendered pages for some Microsoft 365 Copilot references were authorization-gated in this environment, so the investigation used the public MicrosoftDocs source markdown instead. Sources: https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/agents-overview.md ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md
- **[inference]** No unresolved contradiction remains on the main conclusion: every platform studied supports some declarative layer, but GitAgent is the only source inspected that treats the repository itself as the canonical agent artifact. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md ; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html ; https://learn.microsoft.com/en-us/azure/foundry/agents/overview ; https://developers.openai.com/api/docs/guides/tools?api-mode=responses

### §5 Depth and Breadth Expansion

- **[fact]** Technical lens: GitAgent standardizes repository structure, model metadata, tool schemas, hooks, workflows, and duty separation; Microsoft 365 Copilot, Azure Foundry, Amazon Bedrock, and OpenAI each externalize only the slices they can operationalize inside their own platforms. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md ; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html ; https://learn.microsoft.com/en-us/azure/foundry/agents/overview ; https://developers.openai.com/api/docs/guides/tools?api-mode=responses
- **[fact]** Governance lens: GitAgent includes explicit compliance and segregation-of-duties fields; Microsoft emphasizes inherited Microsoft 365 compliance; AgentCore adds deterministic policy and identity services; Azure emphasizes managed identity, content safety, and private networking. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/agents-overview.md ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html ; https://learn.microsoft.com/en-us/azure/foundry/agents/overview
- **[fact]** Historical lens: OpenAI's plugin manifest plus OpenAPI description is a clear earlier example of declaratively describing what an external capability does and how the orchestrator may call it. Sources: https://raw.githubusercontent.com/openai/plugins-quickstart/main/.well-known/ai-plugin.json ; https://raw.githubusercontent.com/openai/plugins-quickstart/main/openapi.yaml
- **[inference]** Operational lens: managed platforms reduce the amount of infrastructure the user must own, but that convenience usually increases dependence on the host platform's packaging model and publishing path. Sources: https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/agents-overview.md ; https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html ; https://learn.microsoft.com/en-us/azure/foundry/agents/overview
- **[inference]** Organizational lens: a repository-level definition such as GitAgent is most valuable when a team wants human review, versioned prompts and rules, and export to multiple runtimes without rewriting the agent's identity each time. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/README.md ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/docs/comparison.md

### §6 Synthesis

**Executive summary:**

- **[inference]** GitAgent is best understood as a Git-native packaging and governance standard for agents rather than as a drop-in replacement runtime, and in this repository it would add the most value as a portable identity layer on top of the existing GitHub Actions and Python automation. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md ; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml
- **[fact]** Microsoft 365 Copilot, Amazon Bedrock, Azure Foundry, and OpenAI all implement some form of declarative agent definition, but they do so at different layers: app package, managed cloud resource, managed platform configuration, or request payload. Sources: https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md ; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html ; https://learn.microsoft.com/en-us/azure/foundry/agents/overview ; https://developers.openai.com/api/docs/guides/tools?api-mode=responses
- **[inference]** The main cross-platform bridge is Model Context Protocol (MCP), with OpenAPI Specification (OAS) still important for Hypertext Transfer Protocol (HTTP) action surfaces. Sources: https://modelcontextprotocol.io ; https://developers.openai.com/api/docs/guides/tools-remote-mcp ; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrock-agent-agentactiongroup.html
- **[inference]** The practical recommendation for this repository is to adopt GitAgent only if the goal is exportability and governance, not if the goal is to replace the current research loop. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/docs/comparison.md ; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml

**Key findings:**

1. **[High][fact]** GitAgent defines the repository itself as the canonical agent artifact, anchored by `agent.yaml` and `SOUL.md`, with optional skills, tools, workflows, hooks, memory, and compliance files.
2. **[Medium][inference]** GitAgent shows credible early momentum, but its youth and `0.1.0` specification mean it should still be treated as an early-stage standard.
3. **[High][fact]** Microsoft 365 Copilot declarative agents are manifest-centric and Microsoft-hosted, while their action layer is now bridged through plugin manifests that support both OpenAPI and remote Model Context Protocol (MCP) servers.
4. **[High][fact]** Amazon Bedrock Agents are declarative service resources with action groups, knowledge bases, memory, and guardrails, while Amazon Bedrock AgentCore is a broader governed runtime and tooling layer.
5. **[High][fact]** Azure Foundry Agent Service combines declarative prompt agents, declarative workflow agents, and code-based hosted agents inside one managed platform.
6. **[High][fact]** OpenAI has preserved declarative agent configuration while moving from file-based plugin manifests toward request-scoped Responses tool definitions, including remote Model Context Protocol (MCP) servers.
7. **[High][inference]** Model Context Protocol (MCP) is the strongest cross-platform tool bridge in the evidence base, whereas vendor-specific manifests remain platform-specific packaging formats.
8. **[Medium][inference]** This repository already contains most of the ingredients a GitAgent definition would need, so GitAgent would fit as an exportable packaging layer but not as a full operational replacement for the current research loop.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] GitAgent uses repo-as-agent with `agent.yaml` and `SOUL.md` plus optional directories. | https://raw.githubusercontent.com/open-gitagent/gitagent/main/README.md ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md | high | Two primary GitAgent sources agree. |
| [inference] GitAgent maturity is promising but early. | https://api.github.com/repos/open-gitagent/gitagent ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/README.md | medium | Strong adoption signal, but only one month of project history. |
| [fact] Microsoft 365 Copilot declarative agents are manifest-based and action-bridged through plugins. | https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/plugin-manifest-2.4.md | high | Both official Microsoft schema references are explicit. |
| [fact] Amazon Bedrock Agents are declarative managed resources; AgentCore is a broader runtime layer. | https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html | high | Resource-level and platform-level AWS docs separate the roles clearly. |
| [fact] Azure Foundry supports prompt, workflow, and hosted agents with shared tool catalog support. | https://learn.microsoft.com/en-us/azure/foundry/agents/overview ; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog | high | Two official Azure pages agree. |
| [fact] OpenAI moved from plugin manifests toward Responses tool declarations while retaining declarative tool configuration. | https://raw.githubusercontent.com/openai/plugins-quickstart/main/.well-known/ai-plugin.json ; https://developers.openai.com/api/docs/guides/tools?api-mode=responses ; https://developers.openai.com/api/docs/assistants/tools/ | high | Historical and current official sources align. |
| [inference] Model Context Protocol (MCP) is the strongest cross-platform bridge. | https://modelcontextprotocol.io ; https://developers.openai.com/api/docs/guides/tools-remote-mcp ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/plugin-manifest-2.4.md ; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html | high | Independent vendor documents all converge on MCP support. |
| [inference] This repository is structurally compatible with GitAgent as a packaging layer but not as a runtime replacement. | https://github.com/davidamitchell/Research/blob/main/.github/mcp.json ; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml ; https://github.com/davidamitchell/Research/blob/main/README.md ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md | medium | Repo fit is an inference grounded in inspected structure. |

**Assumptions:**

- **[assumption]** Adding a second packaging layer is only worthwhile here if exportability or governance is a real future need. Source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-03-16-gitagent-declarative-agent-definition.md
- **[assumption]** A future GitAgent integration for this repository would keep using GitHub Actions and the existing Python Command Line Interface (CLI) rather than replacing them immediately. Source: https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml

**Analysis:**

- **[inference]** The evidence supports a layered view rather than a winner-take-all view. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md ; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html ; https://learn.microsoft.com/en-us/azure/foundry/agents/overview ; https://developers.openai.com/api/docs/guides/tools?api-mode=responses
- **[inference]** GitAgent is unique in making the repository the agent, whereas Microsoft 365 Copilot and Azure Foundry are stronger when the goal is to live inside Microsoft-managed user experiences, Amazon Bedrock is strongest when the goal is a managed agent resource inside Amazon Web Services, and OpenAI's current pattern is the least packaging-centric and the most request-centric. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/agents-overview.md ; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html ; https://learn.microsoft.com/en-us/azure/foundry/agents/overview ; https://developers.openai.com/api/docs/guides/tools?api-mode=responses
- **[inference]** That means GitAgent is best compared with packaging and governance standards, not with fully managed runtimes. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/docs/comparison.md ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html

**Risks, gaps, uncertainties:**

- **[fact]** GitAgent is new enough that adapter stability and long-term ecosystem support remain uncertain. Sources: https://api.github.com/repos/open-gitagent/gitagent ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md
- **[fact]** The source brief pointed to an Amazon Bedrock AgentCore blog post that returned 404 in this environment, so AgentCore conclusions rely on the official developer guide rather than the launch announcement. Sources: https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore/ ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- **[fact]** Microsoft 365 rendered pages were authorization-gated here, so Microsoft claims rely on public source markdown rather than the rendered site. Sources: https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/agents-overview.md ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md

**Open questions:**

- Which minimum subset of GitAgent files would provide value in this repository without duplicating existing instructions and workflows?
- Would a GitAgent export target for GitHub Copilot and this repository's specific research workflow need a custom adapter rather than stock GitAgent adapters?
- If this repository eventually publishes agents into Microsoft 365 Copilot or Azure Foundry, should GitAgent be the canonical authoring format or only an internal packaging aid?

### §7 Recursive Review

- **[fact]** Every factual, inferential, or assumptive statement in the Research Skill Output is explicitly labelled. Source: this section.
- **[fact]** First-use expansion was checked for Large Language Model (LLM), Command Line Interface (CLI), Application Programming Interface (API), Microsoft 365 (M365), Amazon Web Services (AWS), Model Context Protocol (MCP), OpenAPI Specification (OAS), Agent-to-Agent (A2A), JavaScript Object Notation (JSON), and YAML Ain't Markup Language (YAML). Source: this document.
- **[fact]** Every key finding in §6 maps to a named source in the evidence map. Source: §6 Synthesis above.
- **[fact]** Alternative interpretations were considered and rejected where evidence allowed, especially the idea that GitAgent, Amazon Bedrock AgentCore, and Azure Foundry are interchangeable runtimes rather than different layers in the stack. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/docs/comparison.md ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html ; https://learn.microsoft.com/en-us/azure/foundry/agents/overview
- **[inference]** The main recommendation is adequately supported because it depends on documented platform boundaries and observed repository structure, not on speculative vendor roadmaps. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md ; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml

---

## Findings

### Executive Summary

**[inference]** GitAgent is best understood as a portable, Git-native authoring and packaging layer, and the best-supported use for this repository is to layer it on top of the current GitHub Actions and Python runtime rather than to replace that runtime. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/docs/comparison.md ; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml

**[fact]** Microsoft 365 Copilot, Amazon Bedrock, Azure Foundry, and OpenAI all expose declarative agent configuration, but they do so at different layers: Microsoft through app and plugin manifests, Amazon through managed agent resources, Azure through managed prompt or workflow definitions, and OpenAI through request-scoped tool objects. Sources: https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/plugin-manifest-2.4.md ; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html ; https://learn.microsoft.com/en-us/azure/foundry/agents/overview ; https://developers.openai.com/api/docs/guides/tools?api-mode=responses

**[inference]** Model Context Protocol (MCP) (https://modelcontextprotocol.io) is the strongest cross-platform bridge in this comparison, while OpenAPI Specification (OAS) (https://www.openapis.org/what-is-openapi) remains the most common neutral format for Hypertext Transfer Protocol (HTTP) tool and action descriptions. Sources: https://modelcontextprotocol.io ; https://www.openapis.org/what-is-openapi ; https://developers.openai.com/api/docs/guides/tools-remote-mcp ; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrock-agent-agentactiongroup.html

**[inference]** Without a concrete export target, this repository already has the execution, retry, and state-management machinery it needs, so GitAgent is easier to justify as a portability layer than as an operational rewrite. Sources: https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml ; https://github.com/davidamitchell/Research/blob/main/.github/mcp.json ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/docs/comparison.md

### Key Findings

1. **[high][fact]** GitAgent defines an agent primarily as a Git repository rooted in `agent.yaml` and `SOUL.md`, and its specification deliberately extends that core with optional skills, tools, hooks, workflows, memory, compliance, and sub-agent directories rather than forcing one framework-specific runtime model. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/README.md ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md
2. **[medium][inference]** GitAgent has already attracted visible early interest, but the repository's creation date in late February 2026 and its still-current `0.1.0` specification mean that teams should evaluate it as an early-stage standard instead of assuming it is already a stable industry baseline. Sources: https://api.github.com/repos/open-gitagent/gitagent ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/README.md ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md
3. **[high][fact]** Microsoft 365 Copilot implements declarative agent definition through a dedicated manifest that captures instructions, capabilities, conversation starters, and actions, while the platform keeps orchestration and hosting inside Microsoft-managed Copilot infrastructure instead of exposing a portable runtime-neutral package. Sources: https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/agents-overview.md ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/overview-declarative-agent.md
4. **[high][fact]** Microsoft 365 Copilot's plugin manifest layer now bridges declarative agents to both OpenAPI-described services and remote Model Context Protocol (MCP) servers, which shows that Microsoft treats cross-system tool connectivity as a separate interface layer from the declarative agent manifest itself. Sources: https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/plugin-manifest-2.4.md ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md
5. **[high][fact]** Amazon Bedrock Agents represent declarative agent definition as a managed cloud resource with fields for model selection, instructions, action groups, knowledge bases, memory, prompt overrides, guardrails, and orchestration type, while Amazon Bedrock AgentCore supplies a broader governed runtime, tool gateway, identity, and policy platform around that resource model. Sources: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html ; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrock-agent-agentactiongroup.html ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
6. **[high][inference]** Azure Foundry Agent Service offers the broadest explicit mix of declarative prompt, declarative workflow, and code-hosted agent patterns in the current evidence base, because it supports all three behind one managed service and one shared tool catalog. Sources: https://learn.microsoft.com/en-us/azure/foundry/agents/overview ; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog
7. **[high][fact]** OpenAI's older plugin manifest pattern and its newer Responses API tools pattern express the same underlying declarative idea at different scopes, because both hand the model machine-readable descriptions of callable capabilities even though one is file-packaged and the other is request-scoped. Sources: https://raw.githubusercontent.com/openai/plugins-quickstart/main/.well-known/ai-plugin.json ; https://raw.githubusercontent.com/openai/plugins-quickstart/main/openapi.yaml ; https://developers.openai.com/api/docs/assistants/tools/ ; https://developers.openai.com/api/docs/guides/tools?api-mode=responses ; https://developers.openai.com/api/docs/guides/tools-remote-mcp
8. **[high][inference]** Model Context Protocol (MCP) is the clearest cross-platform convergence layer because OpenAI, Azure Foundry, Microsoft 365 Copilot plugins, Amazon Bedrock AgentCore, and this repository's existing tooling all expose or consume MCP-compatible tool connections. Sources: https://modelcontextprotocol.io ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/plugin-manifest-2.4.md ; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html ; https://developers.openai.com/api/docs/guides/tools-remote-mcp ; https://github.com/davidamitchell/Research/blob/main/.github/mcp.json
9. **[medium][inference]** This repository already contains most of the structural pieces that a GitAgent definition expects, so an incremental adoption path would package existing rules, skills, workflows, and tools for export instead of redesigning the runtime that already runs the research loop. Sources: https://github.com/davidamitchell/Research/blob/main/README.md ; https://github.com/davidamitchell/Research/blob/main/.github/mcp.json ; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] GitAgent treats a repository as the agent and uses `agent.yaml` plus `SOUL.md` as the minimum required core. | https://raw.githubusercontent.com/open-gitagent/gitagent/main/README.md ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md | high | README and specification agree on required files and directory model. |
| [inference] GitAgent is promising but still early-stage rather than an established de facto standard. | https://api.github.com/repos/open-gitagent/gitagent ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/README.md | medium | Strong public interest exists, but project age and spec version remain early. |
| [fact] Microsoft 365 Copilot declarative agents are manifest-centric and Microsoft-hosted rather than runtime-portable artifacts. | https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/agents-overview.md ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/overview-declarative-agent.md | high | Official Microsoft docs define the manifest and hosting model directly. |
| [fact] Microsoft plugin manifests bridge actions to OpenAPI and remote Model Context Protocol (MCP) servers. | https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/plugin-manifest-2.4.md | high | Schema 2.4 explicitly names both OpenAPI and `RemoteMCPServer`. |
| [fact] Amazon Bedrock Agents are declarative managed resources, while Amazon Bedrock AgentCore is a broader runtime and policy substrate. | https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html ; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrock-agent-agentactiongroup.html ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html | high | AWS resource and platform docs are complementary and specific. |
| [inference] Azure Foundry supports the broadest explicit mix of declarative and hosted agent patterns among the researched vendor platforms. | https://learn.microsoft.com/en-us/azure/foundry/agents/overview ; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog | high | Azure explicitly documents prompt, workflow, and hosted agents together. |
| [fact] OpenAI shifted from plugin manifests toward request-scoped Responses tools while retaining declarative tool descriptions. | https://raw.githubusercontent.com/openai/plugins-quickstart/main/.well-known/ai-plugin.json ; https://developers.openai.com/api/docs/assistants/tools/ ; https://developers.openai.com/api/docs/guides/tools?api-mode=responses ; https://developers.openai.com/api/docs/guides/tools-remote-mcp | high | Historical and current sources show the shift explicitly. |
| [inference] Model Context Protocol (MCP) is the strongest interoperability layer across the researched ecosystems. | https://modelcontextprotocol.io ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/plugin-manifest-2.4.md ; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html ; https://developers.openai.com/api/docs/guides/tools-remote-mcp ; https://github.com/davidamitchell/Research/blob/main/.github/mcp.json | high | Independent vendor sources plus this repository all point to MCP. |
| [inference] This repository aligns structurally with GitAgent, but the current research-loop runtime already handles execution concerns that GitAgent does not replace by itself. | https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml ; https://github.com/davidamitchell/Research/blob/main/.github/mcp.json ; https://github.com/davidamitchell/Research/blob/main/README.md ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/docs/comparison.md | medium | Repo fit is evidence-based but still inferential. |

### Assumptions

- Future GitAgent adoption would only be justified here if the repository needs stronger exportability, reviewability, or machine-readable governance than the current conventions already provide. Sources: https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml ; https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-03-16-gitagent-declarative-agent-definition.md
- A first GitAgent integration would likely stay thin and wrap existing skills, Model Context Protocol (MCP) tools, and workflows instead of migrating all operational logic on day one. Sources: https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml ; https://github.com/davidamitchell/Research/blob/main/README.md ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md

### Analysis

**[inference]** GitAgent sits above runtimes: it packages identity, rules, skills, tool schemas, and governance in repository files, while Microsoft 365 Copilot, Amazon Bedrock, Azure Foundry, and OpenAI package comparable concerns inside service-specific manifests, cloud resources, or request payloads. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md ; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html ; https://learn.microsoft.com/en-us/azure/foundry/agents/overview ; https://developers.openai.com/api/docs/guides/tools?api-mode=responses

**[inference]** For interoperability, the declarations that travel best are the tool-facing ones rather than the vendor-facing ones, which is why Model Context Protocol (MCP) and OpenAPI Specification (OAS) matter more than any one vendor's agent package format. Sources: https://modelcontextprotocol.io ; https://www.openapis.org/what-is-openapi ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/plugin-manifest-2.4.md ; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog ; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrock-agent-agentactiongroup.html ; https://developers.openai.com/api/docs/guides/tools-remote-mcp

**[inference]** The repository-specific takeaway is practical rather than ideological: preserve the existing GitHub Actions control plane, and add GitAgent only if there is a real downstream need to publish or export the repository's agent definition elsewhere. Sources: https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml ; https://github.com/davidamitchell/Research/blob/main/.github/mcp.json ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/docs/comparison.md

#### Cross-platform comparison

| Platform | Main declarative unit | What it captures well | What stays platform-specific | Best bridge format |
|---|---|---|---|---|
| GitAgent | Repository rooted in `agent.yaml` | Identity, rules, skills, tools, workflows, governance, composition | Actual runtime orchestration and adapters | Model Context Protocol (MCP), OpenAPI Specification (OAS), exported target formats |
| Microsoft 365 Copilot | Declarative agent manifest plus plugin manifest | Instructions, Microsoft knowledge sources, conversation starters, actions | Copilot hosting, Microsoft capabilities, app packaging | Plugin manifest with OpenAPI and remote MCP |
| Amazon Bedrock | `AWS::Bedrock::Agent` plus action groups | Model, instructions, action groups, knowledge bases, memory, guardrails | AWS-managed orchestration and deployment | OpenAPI in action groups; MCP via AgentCore Gateway |
| Azure Foundry | Prompt agent definition or workflow definition | Instructions, model, tools, workflow logic, structured inputs | Azure-managed runtime, publishing, identity, observability | MCP, OpenAPI, Agent-to-Agent (A2A) |
| OpenAI | Request-scoped `tools` objects; earlier plugin manifest files | Tool declarations, approvals, remote MCP servers | Hosted runtime behavior and conversation state model | MCP, function calling, OpenAPI through prior plugin pattern |

### Risks, Gaps, and Uncertainties

- **[fact]** GitAgent's published specification is still `0.1.0`, so field names, adapter behavior, and best practices could change quickly. Sources: https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md ; https://api.github.com/repos/open-gitagent/gitagent
- **[fact]** The Amazon Bedrock AgentCore launch blog cited in the original source list was unavailable in this environment, so conclusions rely on the official developer guide rather than the announcement post. Sources: https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore/ ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- **[fact]** Some Microsoft 365 rendered documentation required authorization in this environment, so Microsoft evidence comes from the public MicrosoftDocs source repository rather than the rendered Learn pages. Sources: https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/agents-overview.md ; https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md
- **[fact]** This research did not test a live GitAgent-to-this-repository prototype, so the adoption recommendation is architecture-grounded rather than implementation-proven. Sources: https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml ; https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md

### Open Questions

- What is the smallest useful GitAgent layer for this repository: only `agent.yaml` and core identity files, or a fuller mapping of skills, tools, and workflows?
- Should a future GitAgent integration here target GitHub Copilot first, or should it target an export path into Azure Foundry, Microsoft 365 Copilot, or OpenAI-compatible runtimes?
- Would it be cleaner to author a custom GitAgent adapter for this repository's research workflow than to force the existing workflow into a generic runtime model?

---

## Output

- Type: knowledge
- Description: Cross-platform analysis of GitAgent and declarative agent definition, with a repository-specific recommendation to use GitAgent as an optional portability and governance layer rather than as a replacement for the current GitHub Actions research loop.
- Links:
  - https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md
  - https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/declarative-agent-manifest-1.6.md
  - https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html
