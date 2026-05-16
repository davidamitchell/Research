---
review_count: 2
title: "External Dependency Surface Taxonomy for Production LLM Agents"
added: 2026-05-16T05:29:47+00:00
status: reviewing
priority: high
blocks: []
tags: [agentic-ai, llm, agent-tooling, workflow, evaluation]
started: 2026-05-16T07:45:33+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-03-08-ai-coding-harnesses-agent-philosophy
  - 2026-03-10-ai-concept-classification-taxonomy
  - 2026-04-26-access-control-amplification-agentic-operations
  - 2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal
  - 2026-04-26-deployment-pipeline-citizen-development-governed-gate
  - 2026-05-06-aibom-identity-attribution-multiagent-practice
  - 2026-05-12-rag-document-drift-agent-behavior
related:
  - 2026-05-13-anthropic-4d-framework-ai-agent-taxonomy
  - 2026-05-13-agent-process-reliability-architecture
  - 2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# External Dependency Surface Taxonomy for Production LLM Agents

## Research Question

What is the complete taxonomy of external dependencies for a production Large Language Model (LLM)-based agent, how does each dependency class fail, what is the blast radius of each failure class, and which existing frameworks from software supply chain security, operational risk, and distributed systems engineering are applicable?

## Scope

**In scope:**
- Dependency classes spanning model providers, safety layers, harness software development kits, tool Application Programming Interfaces (APIs), identity and permissions, and runtime context documents.
- Observed failure modes caused by provider behavior changes, harness updates, and tool API drift.
- Applicability and limits of existing governance frameworks analogous to software bills of materials.

**Out of scope:**
- Building a production implementation of a dependency-surface registry.
- Legal analysis of contract terms for specific model providers.

**Constraints:**
- Prioritise incident evidence and operational postmortems where available.
- Clearly separate deterministic software dependencies from non-deterministic model-behaviour dependencies.

## Context

Artificial Intelligence (AI) agents that call external models, tools, and knowledge sources behave more like distributed systems with delegated action rights than like self-contained applications, so a Software Bill of Materials (SBOM)-style inventory is useful but incomplete on its own. [inference; source: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.ntia.gov/page/software-bill-materials]

Here, "agentic" means a system that uses model reasoning plus tool access to plan or execute multi-step actions with limited real-time human intervention. [fact; source: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/]

## Approach

1. Define dependency classes and map each class to failure triggers, observability limits, and blast radius.
2. Gather incident evidence attributable to provider, harness, or API change rather than application-layer defects.
3. Evaluate existing frameworks such as software supply chain controls and financial operational risk methods for adaptation to agent systems.

## Sources

- [x] [National Institute of Standards and Technology (NIST) (2023) Artificial Intelligence Risk Management Framework 1.0](https://www.nist.gov/itl/ai-risk-management-framework)
- [x] [NIST Artificial Intelligence Risk Management Framework Playbook](https://airc.nist.gov/airmf-resources/playbook/)
- [x] [NIST (2022) Secure Software Development Framework (SSDF) SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final)
- [x] [NIST (2020) Zero Trust Architecture SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final)
- [x] [Cybersecurity and Infrastructure Security Agency (CISA) Software Bill of Materials portal](https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom)
- [x] [National Telecommunications and Information Administration (NTIA) (2021) Software Bill of Materials hub](https://www.ntia.gov/page/software-bill-materials)
- [x] [Open Worldwide Application Security Project (OWASP) Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [x] [Basel Committee (2021) Revisions to the Principles for the Sound Management of Operational Risk](https://www.bis.org/bcbs/publ/d515.htm)
- [x] [Bank for International Settlements (BIS) Financial Stability Institute summary of Principles for the Sound Management of Operational Risk](https://www.bis.org/fsi/fsisummaries/psmor.htm)
- [x] [Google Site Reliability Engineering (SRE) book, Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/)
- [x] [OpenAI API Deprecations](https://developers.openai.com/api/docs/deprecations)
- [x] [OpenAI API Changelog](https://developers.openai.com/api/docs/changelog)
- [x] [OpenAI Assistants migration guide](https://developers.openai.com/api/docs/assistants/migration)
- [x] [OpenAI Status](https://status.openai.com)
- [x] [Anthropic Claude API Docs Model Deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)
- [x] [Anthropic Claude API Docs Migration Guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide)
- [x] [Anthropic Claude Status](https://status.claude.com)
- [x] [LangChain v1 migration guide](https://docs.langchain.com/oss/python/migrate/langchain-v1)
- [x] [Slack API rate limits](https://api.slack.com/apis/rate-limits)
- [x] [Notion API versioning](https://developers.notion.com/reference/versioning)
- [x] [Lewis et al. (2020) Retrieval-Augmented Generation for Knowledge-Intensive Natural Language Processing (NLP) Tasks](https://arxiv.org/abs/2005.11401)
- [x] [Microsoft (2026) Retrieval augmented generation in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation)
- [x] [Microsoft (2026) Agentic retrieval in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview)
- [x] [Amazon Web Services (AWS) (2026) Four security principles for agentic AI systems](https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/)
- [x] [Mitchell (2026) Artificial Intelligence coding harnesses: agent execution model, memory, and context management across commercial and open-source tools](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md)
- [x] [Mitchell (2026) Artificial Intelligence concept classification taxonomy: prompts, instructions, memory, failure modes, controls, and problem domains](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-ai-concept-classification-taxonomy.md)
- [x] [Mitchell (2026) What control and governance principles best address access-control amplification caused by agents operating continuously at machine speed under inherited permissions?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md)
- [x] [Mitchell (2026) To what extent do enterprise Artificial Intelligence and operational-risk frameworks explicitly recognise human speed, attention, fatigue, and working hours as implicit controls whose removal by agentic AI increases blast radius?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.md)
- [x] [Mitchell (2026) Is the deployment pipeline the only truly enforceable governance control point for citizen-developed and agentic systems in a Microsoft low-code stack?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-deployment-pipeline-citizen-development-governed-gate.md)
- [x] [Mitchell (2026) Which identity and attribution model is most appropriate for multi-agent Artificial Intelligence systems that execute tool calls across user-scoped and service-scoped boundaries?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-06-aibom-identity-attribution-multiagent-practice.md)
- [x] [Mitchell (2026) When Retrieval-Augmented Generation source documents change after agent build and test, what failure modes and behavioral regressions arise, and what dependency and change management practices exist to detect, govern, and mitigate them?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-12-rag-document-drift-agent-behavior.md)

## Related

- [Mitchell (2026) What is Anthropic's '4D' framework for Artificial Intelligence fluency, and how does it compare to other agent taxonomies?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-anthropic-4d-framework-ai-agent-taxonomy.md)
- [Mitchell (2026) Architectural patterns for reliable organizational process identification, selection, and execution in Artificial Intelligence agent systems](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md)
- [Mitchell (2026) Systems capability debt, citizen development, and agentic Artificial Intelligence risk](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.md)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation; section 6 seeds the Findings section below.)*

### §0 Initialise

Question: define the external dependency classes for a production LLM agent, explain how each class fails and how large its blast radius can become, then test which existing governance and engineering frameworks actually cover those surfaces.

Scope: model providers, model lifecycle and behavior drift, safety and policy layers, harness and orchestration frameworks, tool APIs, identity and delegated permission systems, runtime knowledge and retrieval dependencies, and applicable supply-chain, operational-risk, and distributed-systems frameworks are in scope; contract-law analysis and full registry implementation are out of scope.

Constraints: prioritize primary platform documentation, standards, and official incident records; separate hard failures from silent quality drift; treat prior repository items as supporting synthesis rather than as sole evidence for central claims.

Output: knowledge, specifically a dependency taxonomy, failure-mode map, blast-radius logic, and framework-fit assessment.

- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-ai-concept-classification-taxonomy.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-deployment-pipeline-citizen-development-governed-gate.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-06-aibom-identity-attribution-multiagent-practice.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-12-rag-document-drift-agent-behavior.md] Prior completed-item scan shows that adjacent repository work already covered dependency concepts, harness architecture, identity propagation, permission amplification, implicit rate limiting, deployment gates, and retrieval drift, so this item's main job is to unify those governance surfaces into one cross-class taxonomy.

### §1 Question Decomposition

- **Root question:** what external dependencies must a production LLM agent rely on, and which of them create silent drift rather than obvious outages?
- **A. Dependency identification**
  - A1. Which external components are required before an agent can reason, act, authenticate, retrieve, and observe?
  - A2. Which of those components are deterministic software dependencies and which are probabilistic behavioral dependencies?
- **B. Failure mechanisms**
  - B1. How do provider outages, quota changes, alias changes, and model retirement fail?
  - B2. How do harness migrations and framework deprecations fail?
  - B3. How do tool API versioning and rate limits fail?
  - B4. How do identity and permission surfaces fail?
  - B5. How do runtime context and retrieval dependencies fail?
  - B6. How do safety and policy layers fail?
- **C. Blast radius**
  - C1. Which dependency classes halt the whole agent estate?
  - C2. Which dependency classes only affect one workflow or one action path?
  - C3. Which dependency classes primarily create silent output-quality or decision-quality degradation?
- **D. Framework fit**
  - D1. Which supply-chain frameworks help inventory deterministic dependencies?
  - D2. Which operational-risk frameworks help govern change, monitoring, resilience, and third-party exposure?
  - D3. Which distributed-systems patterns help contain cascades and preserve service under partial failure?
- **E. Synthesis**
  - E1. What minimum taxonomy is complete enough to be operationally useful?
  - E2. What layered governance pattern best matches the evidence?

### §2 Investigation

#### 2.1 A production LLM agent has a broader dependency surface than ordinary software

- [fact; source: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/] AWS says agentic AI differs from both traditional software and prompt-only generative AI because agents connect to tools and APIs, use LLMs as reasoning engines, and execute sequences of actions autonomously at machine speed with real-world consequences.
- [fact; source: https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.ntia.gov/page/software-bill-materials] CISA and NTIA define an SBOM as a nested inventory or list of ingredients that make up software components.
- [inference; source: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.ntia.gov/page/software-bill-materials; https://owasp.org/www-project-top-10-for-large-language-model-applications/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-ai-concept-classification-taxonomy.md] The minimal complete external-dependency taxonomy for a production LLM agent therefore needs at least seven classes: model service availability and quota, model lifecycle and behavior, safety and policy controls, harness and orchestration framework, tool API contract, identity and delegated permissions, and runtime context and retrieval corpus.

#### 2.2 Model-service availability is the first hard dependency class

- [fact; source: https://status.openai.com] OpenAI's status page explicitly warns that availability metrics are aggregate across tiers, models, and error types and that individual customer availability varies by subscription tier and specific model or API feature.
- [fact; source: https://status.claude.com] Anthropic's status page records repeated incidents affecting specific model families, including elevated errors on Claude Sonnet 4.6 and Haiku 4.5 on 2026-05-12 and errors affecting Claude Opus and Sonnet 4.6 on 2026-05-15.
- [fact; source: https://status.claude.com] Anthropic's 2026-05-07 incident log says a recent infrastructure change altered outbound GitHub source Internet Protocol (IP) addresses and caused Claude Code remote sessions, GitHub Enterprise plugin syncing, and Claude Security to fail for organizations enforcing GitHub IP allowlists.
- [inference; source: https://status.openai.com; https://status.claude.com; https://sre.google/sre-book/addressing-cascading-failures/] Provider-side availability failures create the widest immediate blast radius because they can halt every workflow using the affected model or adjacent integration, and cross-service dependencies can propagate a local provider fault into broader cascading failures when retries or failovers are poorly bounded.

#### 2.3 Model lifecycle, aliasing, and behavior drift form a separate dependency class

- [fact; source: https://developers.openai.com/api/docs/deprecations] OpenAI says deprecated models and endpoints have shut-down dates after which they are no longer accessible, and its deprecations page lists dated removals for model snapshots, endpoints, and whole APIs such as the Assistants API.
- [fact; source: https://developers.openai.com/api/docs/changelog] OpenAI's changelog says `chat-latest` points to the latest model used in ChatGPT and that the underlying model snapshot will be regularly updated.
- [fact; source: https://developers.openai.com/api/docs/assistants/migration] OpenAI says the Assistants API has been deprecated, will shut down on 2026-08-26, and should be migrated to Responses and Conversations, replacing assistants, threads, runs, and run steps with different objects and orchestration semantics.
- [fact; source: https://platform.claude.com/docs/en/about-claude/model-deprecations] Anthropic says deprecated models are likely to be less reliable than active models, gives them retirement dates, and states that requests to retired models will fail.
- [fact; source: https://platform.claude.com/docs/en/about-claude/models/migration-guide] Anthropic's migration guide documents hard breaking changes for Claude Opus 4.7, including removed `thinking` modes, removed non-default sampling parameters, changed default thinking display, token-count changes, and behavioral shifts such as fewer subagents and fewer tool calls by default.
- [inference; source: https://developers.openai.com/api/docs/deprecations; https://developers.openai.com/api/docs/changelog; https://developers.openai.com/api/docs/assistants/migration; https://platform.claude.com/docs/en/about-claude/model-deprecations; https://platform.claude.com/docs/en/about-claude/models/migration-guide] Model-provider dependency risk is not only availability risk: aliases can drift silently, deprecated models can become less reliable before retirement, and migration can require code, prompt, and evaluation changes even when the application's own repository is untouched.

#### 2.4 Harness and orchestration-framework changes are estate-wide software dependencies

- [fact; source: https://docs.langchain.com/oss/python/migrate/langchain-v1] LangChain v1 significantly reduces the `langchain` namespace, moves legacy functionality to `langchain-classic`, changes the recommended import path from `langgraph.prebuilt.create_react_agent` to `langchain.agents.create_agent`, replaces pre-model and post-model hooks with middleware, and no longer accepts `ToolNode` instances or pre-bound models in the same way.
- [inference; source: https://docs.langchain.com/oss/python/migrate/langchain-v1; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md] Harness changes fail differently from provider changes because they usually break orchestration semantics, state handling, middleware behavior, or imports across all agents sharing the framework, which means the blast radius follows reuse concentration inside the estate rather than raw request volume.

#### 2.5 Tool Application Programming Interfaces create contract, quota, and policy dependencies

- [fact; source: https://developers.notion.com/reference/versioning] Notion says the `Notion-Version` header is required, releases a new version when it introduces a backwards-incompatible change, and expects integrations to tolerate additive response changes, identifier-format changes, error-text changes, and rate-limit adjustments.
- [fact; source: https://api.slack.com/apis/rate-limits] Slack documents method-specific rate limits, 429 responses with `Retry-After`, rate-limit changes for some app classes, and states that precise burst limits are intentionally not stable for external builders.
- [inference; source: https://developers.notion.com/reference/versioning; https://api.slack.com/apis/rate-limits; https://owasp.org/www-project-top-10-for-large-language-model-applications/] Tool APIs therefore fail through at least four mechanisms: explicit version incompatibility, quota exhaustion, undocumented tolerance changes, and insecure or weakly controlled plugin boundaries, with blast radius that is often narrower than a model outage but high when one tool is the only path to a critical action.

#### 2.6 Identity, delegated permission, and trust-boundary dependencies have the highest per-action consequence

- [fact; source: https://csrc.nist.gov/pubs/sp/800/207/final] NIST SP 800-207 says zero trust assumes no implicit trust based on network location or asset ownership and focuses on protecting resources, services, workflows, and accounts through explicit authentication and authorization before a session is established.
- [fact; source: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/] AWS says agents operate at greater scale and speed than humans, so excessive privileges carry more potential for unintended consequences, and the broader supply-chain surface includes foundation models, plugins, tool servers, and data retrieval sources.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-06-aibom-identity-attribution-multiagent-practice.md] Identity and permission dependencies deserve their own class because they convert model or tool mistakes into unauthorized writes, unreviewable action chains, or failed actions at trust boundaries, and their blast radius is determined less by traffic volume than by privilege scope and irreversibility of the downstream action.

#### 2.7 Runtime context and Retrieval-Augmented Generation dependencies can drift silently

- [fact; source: https://arxiv.org/abs/2005.11401] Lewis et al. define Retrieval-Augmented Generation (RAG) as a model pattern that combines parametric memory with explicit non-parametric memory accessed through a retriever, and say provenance and updating world knowledge are open research problems.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation] Microsoft says RAG retrieves relevant content from data, includes it in model input as grounding data, relies on indexes for consistent retrieval, and should apply access control at retrieval time while treating retrieved content as untrusted input.
- [fact; source: https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview] Azure AI Search agentic retrieval uses an LLM to break complex queries into focused subqueries, runs them in parallel, and returns grounding data, source references, and execution details.
- [inference; source: https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-12-rag-document-drift-agent-behavior.md] Runtime context documents, indexes, and retrieval plans are true external dependencies because document edits, index changes, or query-planning changes can alter answers and action choices without any model or harness release, so their main blast radius is silent behavioral drift rather than immediate outage.

#### 2.8 Safety and policy layers are external control dependencies, not optional garnish

- [fact; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/] OWASP's Top 10 for LLM applications identifies prompt injection, insecure output handling, model denial of service, supply-chain vulnerabilities, insecure plugin design, excessive agency, and overreliance as distinct failure classes.
- [fact; source: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/] AWS says deterministic external controls should govern what tools, operations, and data an agent can reach because LLMs are probabilistic reasoning engines rather than reliable security-enforcement mechanisms.
- [inference; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/] Safety gateways, prompt-layer rules, moderation services, and policy enforcement services are dependency classes in their own right because they can fail closed and block legitimate work, fail open and permit unsafe actions, or drift out of sync with the tool surface they are meant to constrain.

#### 2.9 Existing frameworks each cover part of the surface, but none covers the whole agent dependency graph alone

- [inference; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.ntia.gov/page/software-bill-materials] Secure Software Development Framework (SSDF) and SBOM guidance help enumerate deterministic software components, secure development practices, and supplier transparency, which makes them suitable controls for harness code, connectors, and release governance.
- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://airc.nist.gov/airmf-resources/playbook/; https://www.bis.org/bcbs/publ/d515.htm; https://www.bis.org/fsi/fsisummaries/psmor.htm] The National Institute of Standards and Technology Artificial Intelligence Risk Management Framework (NIST AI RMF) and Basel operational-risk guidance emphasize governance, change management, monitoring, reporting, control environment, and business continuity, which makes them suitable controls for dependency-class ownership, risk appetite, testing, monitoring, and escalation.
- [fact; source: https://sre.google/sre-book/addressing-cascading-failures/] Google's Site Reliability Engineering guidance treats overload, retries, queue growth, health-check failures, and resource exhaustion as primary cascade mechanisms and emphasizes backoff, containment, and resilience against positive-feedback loops.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.ntia.gov/page/software-bill-materials; https://www.nist.gov/itl/ai-risk-management-framework; https://airc.nist.gov/airmf-resources/playbook/; https://www.bis.org/bcbs/publ/d515.htm; https://sre.google/sre-book/addressing-cascading-failures/; https://owasp.org/www-project-top-10-for-large-language-model-applications/] The evidence supports a layered governance stack rather than a winner-takes-all framework: SBOM-style inventory and SSDF for deterministic components, AI RMF and Basel-style operational risk for oversight and change governance, OWASP for agent-specific failure classes, and Site Reliability Engineering patterns for runtime containment and graceful degradation.

#### 2.10 Blast radius differs by class, not just by severity

- [inference; source: https://status.openai.com; https://status.claude.com; https://developers.openai.com/api/docs/deprecations; https://platform.claude.com/docs/en/about-claude/model-deprecations; https://docs.langchain.com/oss/python/migrate/langchain-v1; https://developers.notion.com/reference/versioning; https://api.slack.com/apis/rate-limits; https://csrc.nist.gov/pubs/sp/800/207/final; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation; https://owasp.org/www-project-top-10-for-large-language-model-applications/] Model endpoint failures and harness-wide migrations create broad estate outages, identity failures create the highest-consequence unauthorized actions, tool API failures usually disable one action path at a time, and runtime-context drift mostly creates silent quality or decision regressions that are harder to detect than hard outages.
- [inference; source: https://sre.google/sre-book/addressing-cascading-failures/; https://status.claude.com; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/] Blast radius is amplified when an agent has no fallback provider, no alternate tool path, no policy sandbox, or no human approval boundary for high-consequence actions, because retries and failover can spread rather than contain a dependency fault.

Access note: seeded CISA attestation URL 404; working replacements used, CISA SBOM portal and NIST SSDF page.

### §3 Reasoning

- [inference; source: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.ntia.gov/page/software-bill-materials] The core reasoning step is to treat "external dependency" as any externally governed component whose change can alter agent behavior, authorization, or availability, not only as a versioned package in source control.
- [inference; source: https://developers.openai.com/api/docs/deprecations; https://platform.claude.com/docs/en/about-claude/model-deprecations; https://docs.langchain.com/oss/python/migrate/langchain-v1; https://developers.notion.com/reference/versioning; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation] That definition cleanly separates deterministic change surfaces, such as harness code or API schemas, from probabilistic or runtime-assembled surfaces, such as model behavior and retrieval context, while still keeping both inside one operational taxonomy.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://www.nist.gov/itl/ai-risk-management-framework; https://www.bis.org/bcbs/publ/d515.htm; https://sre.google/sre-book/addressing-cascading-failures/] Existing frameworks are complementary because they answer different questions: what exists, who owns the risk, what changes must be reviewed, and how runtime faults should be contained.

### §4 Consistency Check

- [fact; source: https://developers.openai.com/api/docs/deprecations; https://platform.claude.com/docs/en/about-claude/model-deprecations] Hard failures from model retirement are directly documented by providers and are not speculative.
- [fact; source: https://docs.langchain.com/oss/python/migrate/langchain-v1; https://developers.notion.com/reference/versioning; https://api.slack.com/apis/rate-limits] Harness and tool-surface changes are directly documented as breaking imports, parameter contracts, required headers, or quota responses rather than inferred from commentary.
- [inference; source: https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview; https://arxiv.org/abs/2005.11401] Silent context drift remains an inference from retrieval mechanics plus platform behavior rather than a named failure class in one single source, so it should remain an inference even though the underlying mechanism is strongly evidenced.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-06-aibom-identity-attribution-multiagent-practice.md; https://csrc.nist.gov/pubs/sp/800/207/final; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/] Identity and permission claims rely partly on prior completed-item synthesis, but the central external evidence still supports the narrower conclusion that permission scope and trust-boundary design are dependency classes with unusually high consequence.

### §5 Depth and Breadth Expansion

- [inference; source: https://www.bis.org/bcbs/publ/d515.htm; https://www.bis.org/fsi/fsisummaries/psmor.htm] Operational-risk lens: the most important governance gap is not inventory alone, but ownership, change criteria, monitoring, and business continuity for each dependency class.
- [inference; source: https://sre.google/sre-book/addressing-cascading-failures/; https://status.claude.com] Distributed-systems lens: provider and tool dependencies should be treated as failure domains with bounded retries, fallback paths, bulkheads, and explicit degradation modes, otherwise agent retry logic can magnify a partial dependency failure.
- [inference; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/] Security lens: prompt injection and insecure plugin design matter here mainly because they exploit dependency boundaries, especially tool APIs, retrieval pipelines, and weakly separated identities.
- [inference; source: https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.ntia.gov/page/software-bill-materials; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-12-rag-document-drift-agent-behavior.md] Information-architecture lens: an agent dependency inventory must record not only binaries and services but also mutable knowledge assets and retrieval endpoints, otherwise the most drift-prone class remains invisible.
- [inference; source: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-deployment-pipeline-citizen-development-governed-gate.md] Governance lens: the safest scaling path is progressive autonomy, class-specific approvals for high-consequence actions, and deployment gates that validate dependency changes before write-capable workflows are promoted.

### §6 Synthesis

**Executive summary:**

A production LLM agent depends on at least seven external classes, and no single existing framework covers their combined failure and blast-radius profile end to end. [inference; source: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.ntia.gov/page/software-bill-materials; https://owasp.org/www-project-top-10-for-large-language-model-applications/]

Model-service availability and lifecycle change create broad outage classes, while identity and delegated permission create the highest-consequence action failures because they turn model or tool mistakes into unauthorized actions. [inference; source: https://status.openai.com; https://status.claude.com; https://developers.openai.com/api/docs/deprecations; https://platform.claude.com/docs/en/about-claude/model-deprecations; https://csrc.nist.gov/pubs/sp/800/207/final; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/]

Harness and tool-API dependencies mostly fail through explicit breaking changes, while retrieval and context dependencies mostly fail through silent behavioral drift that conventional software inventories do not capture. [inference; source: https://docs.langchain.com/oss/python/migrate/langchain-v1; https://developers.notion.com/reference/versioning; https://api.slack.com/apis/rate-limits; https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview]

The strongest governance pattern in this evidence base is layered: use SBOM and Secure Software Development Framework controls for deterministic components, operational-risk and Artificial Intelligence Risk Management Framework controls for ownership and change governance, and Site Reliability Engineering containment patterns for runtime failure handling. [inference; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.ntia.gov/page/software-bill-materials; https://www.nist.gov/itl/ai-risk-management-framework; https://airc.nist.gov/airmf-resources/playbook/; https://www.bis.org/bcbs/publ/d515.htm; https://sre.google/sre-book/addressing-cascading-failures/]

**Key findings:**

1. **A production LLM agent has at least seven distinct external dependency classes, namely model service availability, model lifecycle and behavior, safety and policy controls, harness and orchestration framework, tool API contract, identity and delegated permissions, and runtime context and retrieval corpus.** ([inference]; high confidence; source: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.ntia.gov/page/software-bill-materials; https://owasp.org/www-project-top-10-for-large-language-model-applications/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-ai-concept-classification-taxonomy.md)
2. **Provider availability and infrastructure incidents can disable model-dependent workflows and adjacent integrations, as shown by repeated Anthropic model outages and an infrastructure change that broke GitHub-dependent Claude Code and plugin-sync workflows for customers using source-address allowlists.** ([inference]; high confidence; source: https://status.claude.com; https://status.openai.com)
3. **Model retirement, alias drift, and migration semantics should be treated as a separate failure class from outages, because OpenAI and Anthropic both document shut-down dates, replacement models, and behavior or parameter changes that can break prompts, tools, or orchestration even when application code stays unchanged.** ([inference]; high confidence; source: https://developers.openai.com/api/docs/deprecations; https://developers.openai.com/api/docs/changelog; https://developers.openai.com/api/docs/assistants/migration; https://platform.claude.com/docs/en/about-claude/model-deprecations; https://platform.claude.com/docs/en/about-claude/models/migration-guide)
4. **Harness and orchestration frameworks are shared dependencies whose migrations can change import paths, state-schema rules, middleware hooks, and supported agent-building primitives across every workflow that uses the framework, not just one tool integration.** ([inference]; medium confidence; source: https://docs.langchain.com/oss/python/migrate/langchain-v1; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md)
5. **Tool APIs mainly fail through contract drift, mandatory version headers, quota changes, and rate-limit enforcement, which usually creates narrower blast radius than provider outages but can still disable any workflow whose action path depends on one unredundant external service.** ([inference]; high confidence; source: https://developers.notion.com/reference/versioning; https://api.slack.com/apis/rate-limits; https://owasp.org/www-project-top-10-for-large-language-model-applications/)
6. **Identity and delegated-permission surfaces are the highest-consequence dependency class per action, because zero-trust requirements, machine-speed execution, and shared or weakly bounded credentials can turn one reasoning or tool failure into unauthorized writes, data exposure, or untraceable actor chains.** ([inference]; medium confidence; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-06-aibom-identity-attribution-multiagent-practice.md)
7. **Runtime context and Retrieval-Augmented Generation dependencies differ from package dependencies because document, index, and query-planning changes can silently alter grounding evidence and downstream decisions without any model release, which can make this class more drift-prone and less observable than ordinary software dependencies.** ([inference]; medium confidence; source: https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-12-rag-document-drift-agent-behavior.md)
8. **The most useful governance answer is a layered stack rather than a single imported framework, with SBOM and Secure Software Development Framework practices covering deterministic components, Artificial Intelligence Risk Management Framework and Basel operational-risk controls covering ownership and change governance, OWASP covering agent-specific failure classes, and Site Reliability Engineering patterns containing runtime cascades.** ([inference]; high confidence; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.ntia.gov/page/software-bill-materials; https://www.nist.gov/itl/ai-risk-management-framework; https://airc.nist.gov/airmf-resources/playbook/; https://www.bis.org/bcbs/publ/d515.htm; https://www.bis.org/fsi/fsisummaries/psmor.htm; https://owasp.org/www-project-top-10-for-large-language-model-applications/; https://sre.google/sre-book/addressing-cascading-failures/)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Production LLM agents require at least seven external dependency classes. | https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/ ; https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom ; https://www.ntia.gov/page/software-bill-materials ; https://owasp.org/www-project-top-10-for-large-language-model-applications/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-ai-concept-classification-taxonomy.md | high | Taxonomy synthesized across platform, standards, and prior repository classification work |
| [inference] Provider incidents can disable model-dependent workflows and adjacent integrations. | https://status.claude.com ; https://status.openai.com | high | Anthropic gives detailed incident evidence; OpenAI confirms provider-side availability surface |
| [inference] Model lifecycle and migration changes should be tracked separately from outage handling because they can cause hard failures and behavior drift without repo changes. | https://developers.openai.com/api/docs/deprecations ; https://developers.openai.com/api/docs/changelog ; https://developers.openai.com/api/docs/assistants/migration ; https://platform.claude.com/docs/en/about-claude/model-deprecations ; https://platform.claude.com/docs/en/about-claude/models/migration-guide | high | Explicit retirement, alias, endpoint, and parameter changes support the separate-control classification |
| [inference] Harness migrations create shared orchestration break risk across workflows that reuse the same framework. | https://docs.langchain.com/oss/python/migrate/langchain-v1 ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md | medium | Blast radius follows framework reuse concentration |
| [inference] Tool APIs fail through version drift, mandatory headers, and rate-limit enforcement. | https://developers.notion.com/reference/versioning ; https://api.slack.com/apis/rate-limits ; https://owasp.org/www-project-top-10-for-large-language-model-applications/ | high | Contract and quota surface |
| [inference] Identity and delegated-permission surfaces are the highest-consequence per-action dependency class. | https://csrc.nist.gov/pubs/sp/800/207/final ; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-06-aibom-identity-attribution-multiagent-practice.md | medium | Strong external support for least privilege and machine-speed consequence, but some attribution detail comes from prior repository synthesis |
| [inference] Retrieval and context dependencies can fail through silent drift that is harder to observe than explicit outage handling. | https://arxiv.org/abs/2005.11401 ; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation ; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-12-rag-document-drift-agent-behavior.md | medium | Mechanism is strongly evidenced, but the comparative observability claim remains a synthesis |
| [inference] Layered governance fits the evidence better than any single imported framework. | https://csrc.nist.gov/pubs/sp/800/218/final ; https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom ; https://www.ntia.gov/page/software-bill-materials ; https://www.nist.gov/itl/ai-risk-management-framework ; https://airc.nist.gov/airmf-resources/playbook/ ; https://www.bis.org/bcbs/publ/d515.htm ; https://www.bis.org/fsi/fsisummaries/psmor.htm ; https://owasp.org/www-project-top-10-for-large-language-model-applications/ ; https://sre.google/sre-book/addressing-cascading-failures/ | high | Inventory, governance, and runtime containment answer different questions |

**Assumptions:**

- [assumption; source: https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.ntia.gov/page/software-bill-materials; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/] Treating mutable knowledge assets and policy services as inventory-worthy dependencies is a reasonable extension of SBOM logic even though CISA and NTIA define SBOM around software components rather than around agent reasoning inputs. Justification: the cited sources establish inventory logic and the broader agent surface, but they do not themselves publish a canonical agent-specific inventory schema.
- [assumption; source: https://status.openai.com; https://status.claude.com; https://sre.google/sre-book/addressing-cascading-failures/] Public status pages under-report some tenant-specific failures, but they are still adequate for proving that provider availability is a real dependency surface. Justification: the item's claim is about dependency-class existence, not about exact outage frequency.

**Analysis:**

The evidence supports a taxonomy that separates hard-fail classes from silent-drift classes. [inference; source: https://developers.openai.com/api/docs/deprecations; https://platform.claude.com/docs/en/about-claude/model-deprecations; https://docs.langchain.com/oss/python/migrate/langchain-v1; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation]

Model endpoints, retired aliases, and many harness migrations surface as explicit failures in logs or error rates when the dependency breaks compatibility. [inference; source: https://status.claude.com; https://developers.openai.com/api/docs/deprecations; https://docs.langchain.com/oss/python/migrate/langchain-v1]

Retrieval context, policy tuning, and some model-behavior changes instead degrade outputs or action choices while the agent still appears healthy at the transport layer. [inference; source: https://platform.claude.com/docs/en/about-claude/models/migration-guide; https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview]

A rival interpretation would treat these surfaces as ordinary vendor-management issues rather than as a special taxonomy problem, but that misses two distinctive properties of agents: one reasoning loop can traverse several dependency classes in one run, and delegated action rights can make a small upstream change materially consequential. [inference; source: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://csrc.nist.gov/pubs/sp/800/207/final; https://api.slack.com/apis/rate-limits]

That is why a package-only bill of materials is insufficient, a generic AI-risk checklist is insufficient, and generic SRE containment alone is insufficient: the operationally useful design needs all three viewpoints at once. [inference; source: https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.nist.gov/itl/ai-risk-management-framework; https://sre.google/sre-book/addressing-cascading-failures/]

**Risks, gaps, uncertainties:**

- [inference; source: https://status.openai.com; https://status.claude.com] Public status pages prove the dependency surface exists, but they do not expose tenant-by-tenant blast radius or all second-order failures.
- [inference; source: https://developers.openai.com/api/docs/changelog; https://platform.claude.com/docs/en/about-claude/models/migration-guide] Provider behavior drift is more weakly evidenced than retirement and migration because some semantic changes appear in release notes or migration advice rather than in formal incident postmortems.
- [inference; source: https://developers.notion.com/reference/versioning; https://api.slack.com/apis/rate-limits] Tool API evidence is strong for contract and quota drift, but less strong for multi-tool cascade frequency because official vendors document constraints more readily than they publish root-cause postmortems.
- [inference; source: https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview] Retrieval and context claims are high-confidence on mechanism and lower-confidence on prevalence because named public incident records remain sparser than the platform mechanics.

**Open questions:**

- [inference; source: https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.ntia.gov/page/software-bill-materials; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-06-aibom-identity-attribution-multiagent-practice.md] What is the minimum agent-specific bill-of-materials schema that can record model alias, tool contract, identity boundary, and runtime knowledge source in one machine-readable inventory?
- [inference; source: https://sre.google/sre-book/addressing-cascading-failures/; https://status.claude.com] Which fallback and degradation patterns actually reduce cascade risk for multi-provider agent estates rather than merely multiplying complexity?
- [inference; source: https://developers.openai.com/api/docs/deprecations; https://platform.claude.com/docs/en/about-claude/model-deprecations; https://docs.langchain.com/oss/python/migrate/langchain-v1] What evaluation protocol best catches cross-class drift when a provider, harness, and tool API all change inside one release window?

### §7 Recursive Review

- Review result: pass.
- Acronym audit: Large Language Model (LLM), Artificial Intelligence (AI), Application Programming Interface (API), Software Bill of Materials (SBOM), Retrieval-Augmented Generation (RAG), Secure Software Development Framework (SSDF), and Site Reliability Engineering (SRE) are expanded on first use.
- Claim audit: visible claims in `## Context`, `## Research Skill Output`, and `## Findings` carry epistemic labels and URL-backed sources or are written as metadata fragments.
- Cross-item audit: prior completed items on harnesses, access control, identity attribution, deployment gates, and RAG drift are cited where they materially sharpen the same governance surfaces.

---

## Findings

### Executive Summary

A production LLM agent depends on at least seven external classes, and no single existing framework covers their combined failure and blast-radius profile end to end. [inference; source: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.ntia.gov/page/software-bill-materials; https://owasp.org/www-project-top-10-for-large-language-model-applications/]

Model-service availability and lifecycle change create broad outage classes, while identity and delegated permission create the highest-consequence action failures because they turn model or tool mistakes into unauthorized actions. [inference; source: https://status.openai.com; https://status.claude.com; https://developers.openai.com/api/docs/deprecations; https://platform.claude.com/docs/en/about-claude/model-deprecations; https://csrc.nist.gov/pubs/sp/800/207/final; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/]

Harness and tool-API dependencies mostly fail through explicit breaking changes, while retrieval and context dependencies mostly fail through silent behavioral drift that conventional software inventories do not capture. [inference; source: https://docs.langchain.com/oss/python/migrate/langchain-v1; https://developers.notion.com/reference/versioning; https://api.slack.com/apis/rate-limits; https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview]

The strongest governance pattern in this evidence base is layered: use SBOM and SSDF controls for deterministic components, operational-risk and NIST AI RMF controls for ownership and change governance, and SRE containment patterns for runtime failure handling. [inference; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.ntia.gov/page/software-bill-materials; https://www.nist.gov/itl/ai-risk-management-framework; https://airc.nist.gov/airmf-resources/playbook/; https://www.bis.org/bcbs/publ/d515.htm; https://sre.google/sre-book/addressing-cascading-failures/]

### Key Findings

1. **A production LLM agent has at least seven distinct external dependency classes, namely model service availability, model lifecycle and behavior, safety and policy controls, harness and orchestration framework, tool API contract, identity and delegated permissions, and runtime context and retrieval corpus.** ([inference]; high confidence; source: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.ntia.gov/page/software-bill-materials; https://owasp.org/www-project-top-10-for-large-language-model-applications/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-ai-concept-classification-taxonomy.md)
2. **Provider availability and infrastructure incidents can disable model-dependent workflows and adjacent integrations, as shown by repeated Anthropic model outages and an infrastructure change that broke GitHub-dependent Claude Code and plugin-sync workflows for customers using source-address allowlists.** ([inference]; high confidence; source: https://status.claude.com; https://status.openai.com)
3. **Model retirement, alias drift, and migration semantics should be treated as a separate failure class from outages, because OpenAI and Anthropic both document shut-down dates, replacement models, and behavior or parameter changes that can break prompts, tools, or orchestration even when application code stays unchanged.** ([inference]; high confidence; source: https://developers.openai.com/api/docs/deprecations; https://developers.openai.com/api/docs/changelog; https://developers.openai.com/api/docs/assistants/migration; https://platform.claude.com/docs/en/about-claude/model-deprecations; https://platform.claude.com/docs/en/about-claude/models/migration-guide)
4. **Harness and orchestration frameworks are shared dependencies whose migrations can change import paths, state-schema rules, middleware hooks, and supported agent-building primitives across every workflow that uses the framework, not just one tool integration.** ([inference]; medium confidence; source: https://docs.langchain.com/oss/python/migrate/langchain-v1; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md)
5. **Tool APIs mainly fail through contract drift, mandatory version headers, quota changes, and rate-limit enforcement, which usually creates narrower blast radius than provider outages but can still disable any workflow whose action path depends on one unredundant external service.** ([inference]; high confidence; source: https://developers.notion.com/reference/versioning; https://api.slack.com/apis/rate-limits; https://owasp.org/www-project-top-10-for-large-language-model-applications/)
6. **Identity and delegated-permission surfaces are the highest-consequence dependency class per action, because zero-trust requirements, machine-speed execution, and shared or weakly bounded credentials can turn one reasoning or tool failure into unauthorized writes, data exposure, or untraceable actor chains.** ([inference]; medium confidence; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-06-aibom-identity-attribution-multiagent-practice.md)
7. **Runtime context and Retrieval-Augmented Generation dependencies differ from package dependencies because document, index, and query-planning changes can silently alter grounding evidence and downstream decisions without any model release, which can make this class more drift-prone and less observable than ordinary software dependencies.** ([inference]; medium confidence; source: https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-12-rag-document-drift-agent-behavior.md)
8. **The most useful governance answer is a layered stack rather than a single imported framework, with SBOM and SSDF practices covering deterministic components, NIST AI RMF and Basel operational-risk controls covering ownership and change governance, OWASP covering agent-specific failure classes, and SRE patterns containing runtime cascades.** ([inference]; high confidence; source: https://csrc.nist.gov/pubs/sp/800/218/final; https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.ntia.gov/page/software-bill-materials; https://www.nist.gov/itl/ai-risk-management-framework; https://airc.nist.gov/airmf-resources/playbook/; https://www.bis.org/bcbs/publ/d515.htm; https://www.bis.org/fsi/fsisummaries/psmor.htm; https://owasp.org/www-project-top-10-for-large-language-model-applications/; https://sre.google/sre-book/addressing-cascading-failures/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Production LLM agents require at least seven external dependency classes. | https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/ ; https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom ; https://www.ntia.gov/page/software-bill-materials ; https://owasp.org/www-project-top-10-for-large-language-model-applications/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-ai-concept-classification-taxonomy.md | high | Taxonomy synthesized across platform, standards, and prior repository classification work |
| [inference] Provider incidents can disable model-dependent workflows and adjacent integrations. | https://status.claude.com ; https://status.openai.com | high | Anthropic gives detailed incident evidence; OpenAI confirms provider-side availability surface |
| [inference] Model lifecycle and migration changes should be tracked separately from outage handling because they can cause hard failures and behavior drift without repo changes. | https://developers.openai.com/api/docs/deprecations ; https://developers.openai.com/api/docs/changelog ; https://developers.openai.com/api/docs/assistants/migration ; https://platform.claude.com/docs/en/about-claude/model-deprecations ; https://platform.claude.com/docs/en/about-claude/models/migration-guide | high | Explicit retirement, alias, endpoint, and parameter changes support the separate-control classification |
| [inference] Harness migrations create shared orchestration break risk across workflows that reuse the same framework. | https://docs.langchain.com/oss/python/migrate/langchain-v1 ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md | medium | Blast radius follows framework reuse concentration |
| [inference] Tool APIs fail through version drift, mandatory headers, and rate-limit enforcement. | https://developers.notion.com/reference/versioning ; https://api.slack.com/apis/rate-limits ; https://owasp.org/www-project-top-10-for-large-language-model-applications/ | high | Contract and quota surface |
| [inference] Identity and delegated-permission surfaces are the highest-consequence per-action dependency class. | https://csrc.nist.gov/pubs/sp/800/207/final ; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-06-aibom-identity-attribution-multiagent-practice.md | medium | Strong external support for least privilege and machine-speed consequence, but some attribution detail comes from prior repository synthesis |
| [inference] Retrieval and context dependencies can fail through silent drift that is harder to observe than explicit outage handling. | https://arxiv.org/abs/2005.11401 ; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation ; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-12-rag-document-drift-agent-behavior.md | medium | Mechanism is strongly evidenced, but the comparative observability claim remains a synthesis |
| [inference] Layered governance fits the evidence better than any single imported framework. | https://csrc.nist.gov/pubs/sp/800/218/final ; https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom ; https://www.ntia.gov/page/software-bill-materials ; https://www.nist.gov/itl/ai-risk-management-framework ; https://airc.nist.gov/airmf-resources/playbook/ ; https://www.bis.org/bcbs/publ/d515.htm ; https://www.bis.org/fsi/fsisummaries/psmor.htm ; https://owasp.org/www-project-top-10-for-large-language-model-applications/ ; https://sre.google/sre-book/addressing-cascading-failures/ | high | Inventory, governance, and runtime containment answer different questions |

### Assumptions

- [assumption; source: https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.ntia.gov/page/software-bill-materials; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/] Treating mutable knowledge assets and policy services as inventory-worthy dependencies is a reasonable extension of SBOM logic even though CISA and NTIA define SBOM around software components rather than around agent reasoning inputs. Justification: the cited sources establish inventory logic and the broader agent surface, but they do not themselves publish a canonical agent-specific inventory schema.
- [assumption; source: https://status.openai.com; https://status.claude.com; https://sre.google/sre-book/addressing-cascading-failures/] Public status pages under-report some tenant-specific failures, but they are still adequate for proving that provider availability is a real dependency surface. Justification: the item's claim is about dependency-class existence, not about exact outage frequency.

### Analysis

The evidence supports a taxonomy that separates hard-fail classes from silent-drift classes. [inference; source: https://developers.openai.com/api/docs/deprecations; https://platform.claude.com/docs/en/about-claude/model-deprecations; https://docs.langchain.com/oss/python/migrate/langchain-v1; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation]

Model endpoints, retired aliases, and many harness migrations surface as explicit failures in logs or error rates when the dependency breaks compatibility. [inference; source: https://status.claude.com; https://developers.openai.com/api/docs/deprecations; https://docs.langchain.com/oss/python/migrate/langchain-v1]

Retrieval context, policy tuning, and some model-behavior changes instead degrade outputs or action choices while the agent still appears healthy at the transport layer. [inference; source: https://platform.claude.com/docs/en/about-claude/models/migration-guide; https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview]

A rival interpretation would treat these surfaces as ordinary vendor-management issues rather than as a special taxonomy problem, but that misses two distinctive properties of agents: one reasoning loop can traverse several dependency classes in one run, and delegated action rights can make a small upstream change materially consequential. [inference; source: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://csrc.nist.gov/pubs/sp/800/207/final; https://api.slack.com/apis/rate-limits]

That is why a package-only bill of materials is insufficient, a generic AI-risk checklist is insufficient, and generic SRE containment alone is insufficient: the operationally useful design needs all three viewpoints at once. [inference; source: https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.nist.gov/itl/ai-risk-management-framework; https://sre.google/sre-book/addressing-cascading-failures/]

### Risks, Gaps, and Uncertainties

- [inference; source: https://status.openai.com; https://status.claude.com] Public status pages prove the dependency surface exists, but they do not expose tenant-by-tenant blast radius or all second-order failures.
- [inference; source: https://developers.openai.com/api/docs/changelog; https://platform.claude.com/docs/en/about-claude/models/migration-guide] Provider behavior drift is more weakly evidenced than retirement and migration because some semantic changes appear in release notes or migration advice rather than in formal incident postmortems.
- [inference; source: https://developers.notion.com/reference/versioning; https://api.slack.com/apis/rate-limits] Tool API evidence is strong for contract and quota drift, but less strong for multi-tool cascade frequency because official vendors document constraints more readily than they publish root-cause postmortems.
- [inference; source: https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview] Retrieval and context claims are high-confidence on mechanism and lower-confidence on prevalence because named public incident records remain sparser than the platform mechanics.

### Open Questions

- [inference; source: https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.ntia.gov/page/software-bill-materials; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-06-aibom-identity-attribution-multiagent-practice.md] What is the minimum agent-specific bill-of-materials schema that can record model alias, tool contract, identity boundary, and runtime knowledge source in one machine-readable inventory?
- [inference; source: https://sre.google/sre-book/addressing-cascading-failures/; https://status.claude.com] Which fallback and degradation patterns actually reduce cascade risk for multi-provider agent estates rather than merely multiplying complexity?
- [inference; source: https://developers.openai.com/api/docs/deprecations; https://platform.claude.com/docs/en/about-claude/model-deprecations; https://docs.langchain.com/oss/python/migrate/langchain-v1] What evaluation protocol best catches cross-class drift when a provider, harness, and tool API all change inside one release window?

---

## Output

- Type: knowledge
- Description: This item produces a dependency-surface taxonomy showing that production LLM agents combine software-supply-chain, operational-risk, identity, tool-contract, and runtime-context dependencies that must be governed together rather than through a package-only inventory. [inference; source: https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom; https://www.nist.gov/itl/ai-risk-management-framework; https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/; https://sre.google/sre-book/addressing-cascading-failures/]
- Links:
  - https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/
  - https://developers.openai.com/api/docs/deprecations
  - https://platform.claude.com/docs/en/about-claude/model-deprecations
