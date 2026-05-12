---
title: "When Retrieval-Augmented Generation source documents change after agent build and test, what failure modes and behavioral regressions arise, and what dependency and change management practices exist to detect, govern, and mitigate them?"
added: 2026-05-12T11:03:22+00:00
status: reviewing
priority: high
blocks: []
tags: [agentic-ai, llm, evaluation, workflow, organisation]
started: 2026-05-12T19:03:28+00:00
completed: ~
output: []
cites:
  - 2026-05-12-knowledge-graph-agentic-runtime-dependency
  - 2026-04-29-knowledge-scaffolding-context-engineering
  - 2026-03-21-dependency-mapping-dotnet-terraform-dynatrace
  - 2026-05-06-aibom-runtime-generation-divergence-theory
  - 2026-03-08-servicenow-ai-knowledge-rag-agents
  - 2026-04-27-servicenow-orchestration-agentic-ai-roadmap
related:
  - 2026-05-12-knowledge-graph-lifecycle-management-agentic
  - 2026-05-06-aibom-declared-construction-practice
  - 2026-05-02-cross-item-synthesis-knowledge-map-architecture
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# When Retrieval-Augmented Generation source documents change after agent build and test, what failure modes and behavioral regressions arise, and what dependency and change management practices exist to detect, govern, and mitigate them?

## Research Question

When the source documents indexed in a Retrieval-Augmented Generation (RAG) pipeline change after an agent has been built and tested, what failure modes and behavioral regressions can result in production, and what practices, covering document versioning, behavioral baseline testing, Configuration Management Database (CMDB)-style dependency registration of agent-to-document relationships, and Information Technology Infrastructure Library (ITIL)-inspired change-management governance, exist to detect, govern, and mitigate these regressions?

## Scope

**In scope:**
- Mechanism by which source-document changes propagate into agent context windows at inference time
- Taxonomy of document change types, including wording, factual update, structural change, and deletion, and their likelihood of altering retrieved context
- Documented failure modes and behavioral regression categories when RAG source documents change post-deployment
- Evaluation and testing frameworks that support behavioral baselines over document-corpus versions, including Ragas, TruLens, and LangSmith
- Regression-testing patterns applicable to RAG-dependent agents, including golden-set evaluations, invariant checking, and output comparison
- Document versioning and corpus management approaches, including snapshot indices, version-pinned retrieval, and change-gated pipeline promotion
- Deployment-governance patterns for controlled document-corpus rollouts, including staged index promotion, review gates, and rollback
- How software-engineering concepts, including semantic versioning, contract testing, and dependency management, translate to document corpora as dependencies
- **Dependency registration and discovery:** whether and how CMDB or service-registry patterns can formally record the relationship between a deployed agent and the specific document corpus, or corpus version, it depends on, so that the impact of a document change can be assessed before propagation
- **Change-management governance:** how ITIL change-management concepts, including change authorization, impact assessment, rollback planning, and authorized change gates, apply to document-corpus updates when those documents are runtime dependencies for production agents, and how platforms such as ServiceNow already surface dependency maps that could be extended to cover agent-to-knowledge-base linkages

**Out of scope:**
- Knowledge Graph-specific runtime architecture, covered in `2026-05-12-knowledge-graph-agentic-runtime-dependency`
- Knowledge Graph lifecycle and schema versioning, covered in `2026-05-12-knowledge-graph-lifecycle-management-agentic`
- Agent model fine-tuning or weight updates, because the focus is context and document changes rather than model changes
- RAG system architecture and embedding-model selection outside their role in document-drift sensitivity
- Non-retrieval-based context injection, such as hardcoded system prompts not sourced from documents

**Constraints:**
- Focus on production or near-production systems; prefer documented case studies, published evaluations, and official platform documentation over speculation
- Cover both detection, meaning how to know a regression has occurred, and mitigation, meaning how to prevent or recover from it
- Time horizon: current state of practice, 2022 to 2026

## Context

In this item, a document corpus is treated as a runtime dependency when a deployed agent retrieves passages from it during inference and those passages can change without a code or model release. [inference; source: https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation; https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search]

This item uses "agentic retrieval" to mean a multi-query retrieval pipeline in which a model plans or decomposes the search request before returning grounding data for a downstream answer. [fact; source: https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview]

That dependency is operationally closer to a versioned search index or knowledge source than to static prompt text, because indexers, chunking policy, deletion handling, duplication, and article-governance choices can all change what the agent sees at runtime. [inference; source: https://learn.microsoft.com/azure/search/search-howto-index-changed-deleted-blobs?tabs=portal; https://docs.datastax.com/en/ragstack/intro-to-rag/indexing.html; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219]

The practical problem therefore mirrors broader dependency-governance work: teams need to know which agents depend on which corpus, what version was tested, and how to stage or roll back changes before updated content silently changes behavior in production. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html]

## Approach

1. Characterize the propagation mechanism: how does a document change reach an agent's context window?
   - 1a. Which change types, including rewording, factual update, structural rearrangement, and deletion, most reliably change what is retrieved and injected?
   - 1b. What is the sensitivity of embedding-based retrieval to each change type, and does it differ from keyword or hybrid retrieval?

2. Survey documented failure modes and real-world incidents where document drift caused agent behavioral regressions.
   - 2a. What categories of behavioral regression, including wrong decision, hallucination amplification, altered tool selection, and changed reasoning path, are associated with document changes?
   - 2b. Are there published case studies or incident reports of production agents behaving incorrectly after source document updates?

3. Evaluate testing and evaluation frameworks for their ability to detect document-drift-induced regressions.
   - 3a. How do Ragas, TruLens, LangSmith, and comparable tools support corpus-version-aware behavioral baselines?
   - 3b. What regression-testing patterns, including golden-set evaluations, output comparison, and invariant checking, are applicable and documented in the literature?

4. Identify mitigation and governance patterns for managing document corpora as versioned runtime dependencies.
   - 4a. What versioning approaches, including snapshot indices, version-pinned retrieval, and corpus changelogs, have been proposed or adopted in practice?
   - 4b. How do software engineering concepts, including semantic versioning, contract testing, and dependency lock files, translate to document-corpus management?
   - 4c. What deployment-governance patterns, including staged index promotion and review gates before propagation, are applicable?

5. Synthesize lessons from adjacent completed research that apply to this problem.
   - 5a. What failure-mode mitigations from the Knowledge Graph runtime-dependency item apply to document-corpus dependencies?
   - 5b. What does the Artificial Intelligence Bill of Materials (AIBOM) runtime-divergence item reveal about tracing which document versions participated in a given agent run?
   - 5c. What does the existing Common Service Data Model (CSDM) dependency-mapping item reveal about how service-to-Configuration Item (CI) linkages are currently modeled, and how far that model needs to be extended to cover agent-to-document relationships?

6. Investigate dependency-management and change-management patterns for agent-to-document relationships.
   - 6a. How do CMDB and service-registry patterns represent the dependency between a deployed service and its supporting data sources, and how could those patterns be extended to register an agent's dependency on a specific document corpus or corpus version?
   - 6b. What ITIL change-management concepts, including change authorization, impact assessment, rollback planning, and post-implementation review, apply directly to document-corpus updates when those documents are known runtime dependencies for production agents?
   - 6c. How does ServiceNow's existing dependency mapping and change-management capability model the relationship between knowledge-base articles and the services that consume them, and what gap exists for AI agent consumers specifically?
   - 6d. What leading indicators, including corpus diff size, semantic delta, and affected-agent scope, could feed an automated impact-assessment check in a change-management gate before a document-corpus update is promoted to production?

## Sources

- [x] [Lewis et al. (2020) Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
- [x] [Gao et al. (2024) Retrieval-Augmented Generation for Large Language Models: A Survey](https://arxiv.org/abs/2312.10997)
- [x] [Es et al. (2023) RAGAS: Automated Evaluation of Retrieval Augmented Generation](https://arxiv.org/abs/2309.15217)
- [x] [Ragas Documentation](https://docs.ragas.io/en/stable/)
- [x] [Ragas RAG Evaluation Quickstart](https://docs.ragas.io/en/latest/howtos/cli/rag_eval/)
- [x] [Ragas Production Monitoring](https://docs.ragas.io/en/v0.1.21/getstarted/monitoring.html)
- [x] [LangSmith Evaluation Documentation](https://docs.smith.langchain.com/evaluation)
- [x] [TruLens Instrumentation Overview](https://www.trulens.org/component_guides/instrumentation/)
- [x] [TruLens Groundtruth Evaluations for Retrieval Systems](https://www.trulens.org/getting_started/quickstarts/groundtruth_evals_for_retrieval_systems/)
- [x] [Microsoft Foundry Retrieval Augmented Generation](https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation)
- [x] [Azure AI Search Overview](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search)
- [x] [Azure AI Search Agentic Retrieval Overview](https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview)
- [x] [Azure AI Search Changed and Deleted Blob Handling](https://learn.microsoft.com/azure/search/search-howto-index-changed-deleted-blobs?tabs=portal)
- [x] [Azure AI Search Reliability](https://learn.microsoft.com/en-us/azure/reliability/reliability-ai-search)
- [x] [Azure AI Search Data Plane Representational State Transfer (REST) Application Programming Interfaces](https://learn.microsoft.com/en-us/rest/api/searchservice/)
- [x] [Elasticsearch Aliases](https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html)
- [x] [Amazon OpenSearch Service Configuration Changes](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html)
- [x] [DataStax RAGStack Indexing Guidance](https://docs.datastax.com/en/ragstack/intro-to-rag/indexing.html)
- [x] [ServiceNow Community: Best practices to use your knowledge articles with Now Assist](https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219)
- [x] [TEKsystems Structuring Knowledge for Gen AI in ServiceNow](https://www.teksystems.com/en/insights/article/structuring-knowledge-for-gen-ai-servicenow)
- [ ] [Axelos ITIL 4 Foundation landing page](https://www.axelos.com/certifications/itil-service-management/itil-4-foundation)
- [ ] [ServiceNow Change Management documentation](https://www.servicenow.com/docs/r/it-service-management/change-management/c_ITILChangeManagement.html)
- [ ] [ServiceNow Dependency Views documentation](https://www.servicenow.com/docs/r/zurich/servicenow-platform/dependency-views/c_NextGenBSMMaps.html)
- [ ] [ServiceNow Knowledge article versioning documentation](https://www.servicenow.com/docs/r/servicenow-platform/knowledge-management/article-versioning)
- [x] [Mitchell (2026) Knowledge Graph in the live execution path of multi-step Large Language Model systems](https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html)
- [x] [Mitchell (2026) Is knowledge scaffolding an established concept within context engineering for Large Language Models and AI agents?](https://davidamitchell.github.io/Research/research/2026-04-29-knowledge-scaffolding-context-engineering.html)
- [x] [Mitchell (2026) Dependency Mapping Across .NET Codebases, Terraform, Dynatrace, Confluence, Log Aggregation, and the Configuration and Service Data Model](https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html)
- [x] [Mitchell (2026) Declared versus runtime AIBOM divergence](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html)
- [x] [Mitchell (2026) ServiceNow AI: Knowledge Management, RAG Pipelines, and Agent Frameworks](https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-ai-knowledge-rag-agents.html)
- [x] [Mitchell (2026) ServiceNow orchestration and agentic AI roadmap](https://davidamitchell.github.io/Research/research/2026-04-27-servicenow-orchestration-agentic-ai-roadmap.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: determine what failure modes and behavioral regressions arise when a tested RAG corpus changes in production, and identify the dependency-registration and change-governance practices that can detect and mitigate those regressions.
- Scope: propagation mechanism, change taxonomy, regression types, evaluation frameworks, versioning and rollout, dependency registration, and change governance are in scope; model-weight changes and Knowledge Graph architecture are not.
- Constraints: current practice only, 2022 to 2026; prefer primary or official sources; full research mode; output must remain usable as an operational knowledge note.
- Output format: full section 0 to section 7 investigation plus Findings with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks, Gaps, Uncertainties, Open Questions, and Output.
- [inference] Prior completed-item cross-reference: the most relevant completed items are the runtime-dependency item on live Knowledge Graph serving, the knowledge-scaffolding item on staged context assembly, the dependency-mapping item on layered registries, the runtime-divergence AIBOM item on observed-versus-declared state, and the ServiceNow items on knowledge-quality governance and orchestration. [source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://davidamitchell.github.io/Research/research/2026-04-29-knowledge-scaffolding-context-engineering.html; https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-ai-knowledge-rag-agents.html; https://davidamitchell.github.io/Research/research/2026-04-27-servicenow-orchestration-agentic-ai-roadmap.html]
- [inference] Working definition for this item: document drift means a post-test change in corpus content, chunking or indexing state, deletion handling, or duplication behavior that changes what evidence the agent can retrieve or how that evidence is ranked at runtime. [source: https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/azure/search/search-howto-index-changed-deleted-blobs?tabs=portal; https://docs.datastax.com/en/ragstack/intro-to-rag/indexing.html; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219]

### §1 Question Decomposition

- A. Propagation mechanism
  - A1. How do retrieved passages or knowledge-source results become part of model input at inference time?
  - A2. How does agentic retrieval add extra sensitivity through query planning, subquerying, and merged references?
- B. Change taxonomy
  - B1. Which corpus changes affect retrieval directly, including factual edits, structural rewrites, duplication, deletion, rename, and metadata changes?
  - B2. Which indexer or ingestion behaviors allow stale or orphaned content to survive?
- C. Regression taxonomy
  - C1. Which output-level regressions follow from changed retrieval evidence?
  - C2. Which behavior-level regressions follow when changed evidence alters tool choice or workflow path?
- D. Detection
  - D1. Which offline evaluation patterns can compare corpus versions?
  - D2. Which online tracing and monitoring patterns can expose drift after deployment?
- E. Mitigation and rollout
  - E1. Which versioning and promotion patterns treat the corpus as a deployable artifact?
  - E2. Which rollback or staged-cutover mechanisms already exist in search infrastructure?
- F. Dependency registration and governance
  - F1. How far do existing dependency-mapping patterns go toward agent-to-corpus registration?
  - F2. Which change-management controls can be applied directly to corpus updates?

### §2 Investigation

#### 2.1 Propagation mechanism

- [fact] Lewis et al. define Retrieval-Augmented Generation as language generation conditioned on retrieved passages from a dense vector index, so retrieved documents are part of the model's effective input rather than a background reference. [source: https://arxiv.org/abs/2005.11401]
- [fact] Microsoft Foundry describes RAG as a three-step retrieve, augment, generate flow in which retrieved content is added to the prompt as grounding data before the model answers. [source: https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation]
- [fact] Azure AI Search says agentic retrieval uses a Large Language Model (LLM) to break complex requests into focused subqueries, runs them in parallel, reranks them, and returns merged grounding data, source references, and execution metadata. [source: https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview]
- [fact] Azure AI Search distinguishes indexed knowledge sources from remote knowledge sources, which means a deployed agent can depend either on a refreshed local index or on live remote retrieval. [source: https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search]
- [inference] In classical RAG the change surface is the retrieved chunk set and its rank order; in agentic retrieval the change surface also includes query planning, subquery coverage, and merged citations, so a small corpus edit can alter both evidence and reasoning path. [source: https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview; https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search]

#### 2.2 Change taxonomy and sensitivity

- [fact] Azure AI Search indexers automatically pick up new and changed blobs by using built-in timestamps, but deletion detection is not automatic and requires an explicit soft-delete strategy from the first indexer run. [source: https://learn.microsoft.com/azure/search/search-howto-index-changed-deleted-blobs?tabs=portal]
- [fact] Azure AI Search documents that renaming Azure Data Lake Storage Gen2 directories does not update blob timestamps, so the indexer will not reindex those blobs unless their `LastModified` timestamp is updated. [source: https://learn.microsoft.com/azure/search/search-howto-index-changed-deleted-blobs?tabs=portal]
- [fact] ServiceNow's Now Assist guidance says duplicate articles with different content can produce incorrect or disjointed answers and recommends a single source of truth instead of duplicated content across knowledge bases. [source: https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219]
- [fact] ServiceNow's guidance says the LLM cannot click links or infer missing content from screenshots and videos, so knowledge articles must contain self-contained text; the same guidance notes that only certain text attachments are indexed and that attachment size limits apply. [source: https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219]
- [fact] DataStax's RAG indexing guidance treats chunking strategy as a major quality lever, because sentence, paragraph, content-aware, and recursive chunking behave differently across document structures and context-window sizes. [source: https://docs.datastax.com/en/ragstack/intro-to-rag/indexing.html]
- [fact] TEKsystems' ServiceNow knowledge-governance guidance recommends taxonomy, review cadence, governance standards, and duplicate/conflict checks because unstructured or outdated content degrades generative outputs. [source: https://www.teksystems.com/en/insights/article/structuring-knowledge-for-gen-ai-servicenow]
- [inference] The materially risky change classes are factual edits, structural rewrites that change chunk boundaries, duplicate or conflicting replacements, deletions or renames that leave orphaned indexed content, attachment-only additions the retriever cannot fully consume, and metadata or taxonomy changes that alter filtering or ranking. [source: https://learn.microsoft.com/azure/search/search-howto-index-changed-deleted-blobs?tabs=portal; https://docs.datastax.com/en/ragstack/intro-to-rag/indexing.html; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219; https://www.teksystems.com/en/insights/article/structuring-knowledge-for-gen-ai-servicenow]

#### 2.3 Failure modes and behavioral regressions

- [fact] Gao et al. frame RAG as a response to hallucination, outdated knowledge, and non-transparent reasoning in Large Language Models, which means freshness and traceability are central rather than peripheral RAG concerns. [source: https://arxiv.org/abs/2312.10997]
- [fact] Ragas states that RAG performance is affected by the retrieval model, the corpus, the LLM, and the prompt formulation, which means corpus changes can alter measured quality even when the model and prompt stay fixed. [source: https://arxiv.org/html/2309.15217v2; https://docs.ragas.io/en/stable/]
- [fact] Ragas production-monitoring guidance explicitly targets faithfulness, bad retrieval, bad response, bad format, and distribution shift between production and test sets. [source: https://docs.ragas.io/en/v0.1.21/getstarted/monitoring.html]
- [fact] Azure AI Search's retrieval architecture returns not only retrieved text but also source references and execution metadata, so a corpus change can alter citation surface and provenance even when the answer text still looks plausible. [source: https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview]
- [inference] Post-deployment document drift therefore produces at least six operational regression classes: stale answers from outdated passages, omissions after failed deletion handling, blended answers from conflicting duplicates, citation drift when a different passage is selected, changed workflow choice when altered grounding changes relevance ranking, and false freshness where the system looks grounded but is serving an older index state. [source: https://arxiv.org/abs/2312.10997; https://docs.ragas.io/en/v0.1.21/getstarted/monitoring.html; https://learn.microsoft.com/azure/search/search-howto-index-changed-deleted-blobs?tabs=portal; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview]

#### 2.4 Detection and evaluation frameworks

- [fact] LangSmith distinguishes offline evaluations for benchmarking, regression testing, unit testing, and backtesting from online evaluations for production monitoring, anomaly detection, and live-traffic quality tracking. [source: https://docs.smith.langchain.com/evaluation]
- [fact] LangSmith offline evaluations run on curated datasets and examples, and each experiment captures outputs, evaluator scores, and traces for a specific application version. [source: https://docs.smith.langchain.com/evaluation]
- [fact] The Ragas `rag_eval` template creates local datasets, experiment runs, logs, and CSV outputs so the same test set can be exercised repeatedly against a RAG application. [source: https://docs.ragas.io/en/latest/howtos/cli/rag_eval/]
- [fact] TruLens supports ground-truth retrieval evaluation, including information-retrieval hit rate, normalized discounted cumulative gain at k, recall at k, and semantic agreement with a ground-truth answer. [source: https://www.trulens.org/getting_started/quickstarts/groundtruth_evals_for_retrieval_systems/]
- [fact] TruLens instrumentation is OpenTelemetry compatible and can record query text, retrieved contexts, return values, and custom attributes as span data for later evaluation. [source: https://www.trulens.org/component_guides/instrumentation/]
- [inference] These frameworks can detect document-drift regressions if teams freeze golden questions and compare runs before and after corpus changes, but none of the inspected docs makes corpus version, index alias, or retrieved-document hash a mandatory first-class dependency field, so teams must add that metadata explicitly. [source: https://docs.smith.langchain.com/evaluation; https://docs.ragas.io/en/latest/howtos/cli/rag_eval/; https://docs.ragas.io/en/v0.1.21/getstarted/monitoring.html; https://www.trulens.org/getting_started/quickstarts/groundtruth_evals_for_retrieval_systems/; https://www.trulens.org/component_guides/instrumentation/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]

#### 2.5 Versioning, rollout, and rollback patterns

- [fact] Elasticsearch aliases allow applications to change which index they query in real time, and the aliases API supports atomic remove-plus-add swaps with no downtime. [source: https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html]
- [fact] Amazon OpenSearch Service uses blue/green deployment for significant configuration changes by copying the production environment, migrating data, and switching traffic only when the green environment is ready; the service also supports dry-run eligibility checks and change-progress tracking. [source: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html]
- [fact] Azure AI Search recommends at least two replicas for production read workloads, retries for transient faults, and treats indexes, indexers, data sources, and skillsets as separate service objects that can be automated and recovered independently. [source: https://learn.microsoft.com/en-us/azure/reliability/reliability-ai-search; https://learn.microsoft.com/en-us/rest/api/searchservice/]
- [fact] Azure AI Search indexers use change tracking to resume from the last successfully indexed document, which means index refresh itself is a managed pipeline step rather than an implicit guarantee. [source: https://learn.microsoft.com/en-us/azure/reliability/reliability-ai-search; https://learn.microsoft.com/azure/search/search-howto-index-changed-deleted-blobs?tabs=portal]
- [inference] The strongest mitigation pattern is therefore to treat the corpus and retrieval index as deployable artifacts: build a new version, evaluate it against a stable baseline, promote it through an alias or staged cutover, and keep the prior version available for rollback. [source: https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html; https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html; https://learn.microsoft.com/en-us/azure/reliability/reliability-ai-search; https://docs.smith.langchain.com/evaluation]

#### 2.6 Dependency registration, prior work, and governance extension

- [fact] The prior dependency-mapping item concluded that no single surface gives a complete dependency picture and that layered maps are needed across code, runtime, documentation, and Common Service Data Model surfaces. [source: https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html]
- [fact] The prior AIBOM runtime-divergence item concluded that declared and observed state diverge across retrieval, memory, external-state, and control-policy surfaces, and that runtime evidence must preserve the actual retrieval set. [source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]
- [fact] The prior ServiceNow AI knowledge item found that answer quality is directly dependent on knowledge article quality, taxonomy, and freshness. [source: https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-ai-knowledge-rag-agents.html]
- [fact] The prior ServiceNow orchestration item found that ServiceNow's differentiation comes from combining orchestration with Configuration Management Database relationships, approval chains, and workflow records rather than from the CMDB alone. [source: https://davidamitchell.github.io/Research/research/2026-04-27-servicenow-orchestration-agentic-ai-roadmap.html]
- [fact] The prior Knowledge Graph runtime-dependency item concluded that once knowledge infrastructure sits in the live execution path, freshness budgets, consistency, fallback behavior, and observability become part of runtime governance. [source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]
- [inference] Taken together, these sources support extending a dependency registry or AIBOM to include agent-to-corpus edges, corpus version identifiers, approved source sets, and blast-radius metadata, but the accessible vendor material inspected here does not show a mature off-the-shelf pattern that automatically registers an agent against the exact corpus version it was tested on. [source: https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-ai-knowledge-rag-agents.html; https://davidamitchell.github.io/Research/research/2026-04-27-servicenow-orchestration-agentic-ai-roadmap.html; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219]
- [inference] An ITIL-style operating model maps cleanly onto corpus updates even without an agent-specific product pattern: low-risk editorial fixes can flow quickly, while changes that modify authoritative facts, delete high-use articles, or restructure retrieval-critical content should trigger impact assessment, baseline re-evaluation, scheduled promotion, and rollback readiness. [source: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html; https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219; https://davidamitchell.github.io/Research/research/2026-04-27-servicenow-orchestration-agentic-ai-roadmap.html]

### §3 Reasoning

- [inference] The strongest causal chain in the evidence is direct retrieval-conditioned generation: if retrieved passages or query plans change, the model input changes, so behavior can change without any model release. [source: https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview]
- [inference] Evidence for detection and mitigation is stronger than evidence for incident prevalence, because the inspected material includes multiple evaluation frameworks and rollout documents but few public postmortems naming document drift as the root cause. [source: https://docs.smith.langchain.com/evaluation; https://docs.ragas.io/en/v0.1.21/getstarted/monitoring.html; https://www.trulens.org/component_guides/instrumentation/; https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html]
- [assumption] When a framework does not store corpus version automatically, teams can still attach corpus version, index alias, or retrieved-document identifiers as experiment metadata, trace attributes, or registry records. **Justification:** the inspected tools expose datasets, experiments, and custom span attributes even though they do not mandate corpus-version fields. [source: https://docs.smith.langchain.com/evaluation; https://docs.ragas.io/en/latest/howtos/cli/rag_eval/; https://www.trulens.org/component_guides/instrumentation/]
- [inference] Governance recommendations were limited to controls directly supported by the inspected evidence, namely versioned rollout, deletion policy, baseline testing, content-governance rules, and dependency registration, rather than to speculative platform features that were not accessible here. [source: https://learn.microsoft.com/azure/search/search-howto-index-changed-deleted-blobs?tabs=portal; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219; https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html; https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html]

### §4 Consistency Check

- [fact] Foundational RAG sources and current Azure platform docs agree that retrieved external content is added to model input at inference time, so the propagation mechanism is consistent across foundational and platform evidence. [source: https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation; https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search]
- [fact] The corpus-governance sources agree that duplicates, stale content, and missing deletion handling are distinct risks rather than one generic drift problem. [source: https://learn.microsoft.com/azure/search/search-howto-index-changed-deleted-blobs?tabs=portal; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219; https://www.teksystems.com/en/insights/article/structuring-knowledge-for-gen-ai-servicenow]
- [inference] The main unresolved trade-off is freshness versus reproducibility: more live retrieval reduces staleness, while more version pinning improves auditability, rollback, and comparability to prior tests. [source: https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search; https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html; https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]
- [inference] Overall confidence remains medium because the operational mechanism and control patterns are well supported, but public incident evidence and directly accessible ServiceNow change-governance documentation were incomplete. [source: https://docs.smith.langchain.com/evaluation; https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: deletion detection and chunking policy are as important as model choice, because they determine whether the retrieved evidence set is current, coherent, and comparable to what was tested. [source: https://learn.microsoft.com/azure/search/search-howto-index-changed-deleted-blobs?tabs=portal; https://docs.datastax.com/en/ragstack/intro-to-rag/indexing.html; https://arxiv.org/abs/2005.11401]
- [inference] Economic and operational lens: versioned indexes, baseline datasets, and rollback capacity add process and storage cost, but they replace unpredictable investigation cost after a grounded agent silently changes behavior. [source: https://docs.smith.langchain.com/evaluation; https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html; https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html]
- [inference] Governance lens: knowledge articles and search indexes deserve owners and change classes when they feed production agents, because content updates become decision-input changes rather than mere documentation edits. [source: https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219; https://davidamitchell.github.io/Research/research/2026-04-27-servicenow-orchestration-agentic-ai-roadmap.html; https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html]
- [inference] Behavioral lens: grounded systems can create over-trust, so stale or conflicting retrieved content is especially risky because the answer still appears sourced and context-aware to the user. [source: https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219; https://docs.ragas.io/en/v0.1.21/getstarted/monitoring.html]

### §6 Synthesis

**Executive summary:**

Post-deployment document changes in Retrieval-Augmented Generation systems act like dependency updates: they can change the retrieved evidence, citations, and downstream agent behavior even when model weights and prompts stay fixed. [inference; source: https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview]

The highest-confidence failure mechanisms are stale or orphaned indexed content, duplicate or conflicting articles, chunk or structure changes that alter ranking, and multi-query retrieval plans that change which evidence reaches the model. [inference; source: https://learn.microsoft.com/azure/search/search-howto-index-changed-deleted-blobs?tabs=portal; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219; https://docs.datastax.com/en/ragstack/intro-to-rag/indexing.html; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview]

Current evaluation frameworks can catch many of these regressions through golden datasets, retrieval metrics, and traced production monitoring, but they do not turn the corpus version into a first-class governed dependency on their own. [inference; source: https://docs.smith.langchain.com/evaluation; https://docs.ragas.io/en/latest/howtos/cli/rag_eval/; https://docs.ragas.io/en/v0.1.21/getstarted/monitoring.html; https://www.trulens.org/getting_started/quickstarts/groundtruth_evals_for_retrieval_systems/; https://www.trulens.org/component_guides/instrumentation/]

The strongest operational pattern is to treat the corpus and index as deployable artifacts with version identifiers, staged promotion or alias swaps, rollback paths, and registry links from each agent to the corpus version it was tested against. [inference; source: https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html; https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html; https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]

**Key findings:**

1. **Retrieval-Augmented Generation and agentic retrieval systems can change behavior after document updates because retrieved passages and query plans are part of the model input at inference time, not fixed compile-time assets.** ([inference]; high confidence; source: https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview)
2. **Retrieval regressions arise from more than factual edits, because failed deletion handling, renamed paths, duplicate articles, non-self-contained articles, and chunking changes can all alter what evidence is retrieved or summarized.** ([inference]; high confidence; source: https://learn.microsoft.com/azure/search/search-howto-index-changed-deleted-blobs?tabs=portal; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219; https://docs.datastax.com/en/ragstack/intro-to-rag/indexing.html)
3. **The most operationally important behavioral regressions are stale answers, missing facts, blended or contradictory answers, citation drift, and changed workflow choices when altered grounding changes what the agent considers relevant.** ([inference]; medium confidence; source: https://arxiv.org/abs/2312.10997; https://docs.ragas.io/en/v0.1.21/getstarted/monitoring.html; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219)
4. **LangSmith, Ragas, and TruLens collectively provide datasets, experiment comparison, retrieval metrics, ground-truth checks, and traced production monitoring, which together form the practical ingredients for corpus-change regression testing.** ([inference]; high confidence; source: https://docs.smith.langchain.com/evaluation; https://docs.ragas.io/en/latest/howtos/cli/rag_eval/; https://docs.ragas.io/en/v0.1.21/getstarted/monitoring.html; https://www.trulens.org/getting_started/quickstarts/groundtruth_evals_for_retrieval_systems/; https://www.trulens.org/component_guides/instrumentation/)
5. **None of the inspected evaluation frameworks or platform documents automatically turns the document corpus into a first-class dependency record, so teams need explicit corpus version identifiers, trace metadata, or registry entries to know what was tested and what is live.** ([inference]; medium confidence; source: https://docs.smith.langchain.com/evaluation; https://docs.ragas.io/en/latest/howtos/cli/rag_eval/; https://www.trulens.org/component_guides/instrumentation/; https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html)
6. **Mature rollout patterns already exist for the retrieval layer even though they are rarely described as RAG governance, because aliases, blue-green deployment, replicas, and retryable indexers provide the mechanics for staged promotion and rollback of new corpus versions.** ([inference]; high confidence; source: https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html; https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html; https://learn.microsoft.com/en-us/azure/reliability/reliability-ai-search; https://learn.microsoft.com/en-us/rest/api/searchservice/)
7. **Accessible vendor and repository evidence supports extending CMDB-like dependency mapping and ITIL-like change control to agent-to-corpus relationships, but the accessible sources do not show a mature off-the-shelf product that automatically registers each agent against the exact corpus version it depends on.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-ai-knowledge-rag-agents.html; https://davidamitchell.github.io/Research/research/2026-04-27-servicenow-orchestration-agentic-ai-roadmap.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Retrieved passages and query plans are runtime inputs, so document updates can change behavior without a model release. | https://arxiv.org/abs/2005.11401 ; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation ; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview | high | Propagation mechanism |
| [inference] Failed deletion handling, rename drift, duplicates, weak article structure, and chunking changes are distinct regression triggers. | https://learn.microsoft.com/azure/search/search-howto-index-changed-deleted-blobs?tabs=portal ; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219 ; https://docs.datastax.com/en/ragstack/intro-to-rag/indexing.html | high | Source-layer failure classes |
| [inference] Stale answers, omissions, blended answers, citation drift, and changed workflow choice are the main behavior regressions. | https://arxiv.org/abs/2312.10997 ; https://docs.ragas.io/en/v0.1.21/getstarted/monitoring.html ; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview ; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219 | medium | Output and action effects |
| [inference] LangSmith, Ragas, and TruLens collectively provide the building blocks needed for corpus-change regression testing. | https://docs.smith.langchain.com/evaluation ; https://docs.ragas.io/en/latest/howtos/cli/rag_eval/ ; https://docs.ragas.io/en/v0.1.21/getstarted/monitoring.html ; https://www.trulens.org/getting_started/quickstarts/groundtruth_evals_for_retrieval_systems/ ; https://www.trulens.org/component_guides/instrumentation/ | high | Datasets, traces, retrieval metrics |
| [inference] Corpus versioning is not first-class in the inspected tools, so teams must attach metadata or registry records themselves. | https://docs.smith.langchain.com/evaluation ; https://docs.ragas.io/en/latest/howtos/cli/rag_eval/ ; https://www.trulens.org/component_guides/instrumentation/ ; https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html | medium | Control-plane gap |
| [inference] Alias swaps, blue-green rollout, replicas, and recoverable indexers support staged promotion and rollback for corpus versions. | https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html ; https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html ; https://learn.microsoft.com/en-us/azure/reliability/reliability-ai-search ; https://learn.microsoft.com/en-us/rest/api/searchservice/ | high | Release mechanics |
| [inference] CMDB-like dependency mapping and ITIL-like change control can be extended to agent-to-corpus relationships, but a mature automatic registration pattern is still missing. | https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html ; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-ai-knowledge-rag-agents.html ; https://davidamitchell.github.io/Research/research/2026-04-27-servicenow-orchestration-agentic-ai-roadmap.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html ; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219 | medium | Registry-extension gap |

**Assumptions:**

- [assumption] Teams can surface stable corpus or index version identifiers even when tools do not require them. **Justification:** aliases, index objects, and custom trace attributes already exist in the inspected infrastructure, so the missing piece is discipline rather than a missing technical hook. [source: https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html; https://learn.microsoft.com/en-us/rest/api/searchservice/; https://www.trulens.org/component_guides/instrumentation/]
- [assumption] For remote knowledge sources, an equivalent control can use source snapshot identifiers, retrieval-response identifiers, or timestamped export bundles when no local search index exists. **Justification:** Azure AI Search explicitly supports remote knowledge sources in agentic retrieval, so version pinning cannot rely only on local index names. [source: https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview]
- [assumption] The inaccessible full ITIL practice guide would not reverse the governance mapping here, because the recommendation is limited to controls already visible in accessible rollout and content-governance sources: approval, impact review, staged promotion, and rollback readiness. [source: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html; https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219]

**Analysis:**

The evidence was weighted toward foundational RAG papers and current platform documentation because the core question is operational causality, namely how a document change reaches inference-time behavior, rather than market positioning or vendor rhetoric. [inference; source: https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview; https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html]

Mechanism evidence is stronger than incident evidence: Lewis and Azure show how corpus changes alter the prompt surface, while Azure and ServiceNow show concrete ways stale, deleted, duplicate, or weakly structured content can survive into retrieval and summarization. [inference; source: https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/azure/search/search-howto-index-changed-deleted-blobs?tabs=portal; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219]

The evaluation frameworks are useful but incomplete for governance because they measure outcomes and traces, not authoritative dependency registration; prior repository work on dependency mapping and runtime divergence fills that missing control-plane perspective. [inference; source: https://docs.smith.langchain.com/evaluation; https://docs.ragas.io/en/latest/howtos/cli/rag_eval/; https://www.trulens.org/component_guides/instrumentation/; https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]

A rival response would be to keep corpora fully live for freshness and accept occasional regression, but alias and blue-green rollout sources show that safer staged promotion is already technically normal in search infrastructure, so unmanaged freshness is a governance choice rather than a technical inevitability. [inference; source: https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html; https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html; https://learn.microsoft.com/en-us/azure/reliability/reliability-ai-search]

**Risks, gaps, uncertainties:**

- Publicly accessible named postmortems for document-drift incidents remain sparse in the inspected source base, so incident prevalence and typical blast radius are lower-confidence than the mechanism and mitigation claims above. [inference; source: https://docs.smith.langchain.com/evaluation; https://docs.ragas.io/en/v0.1.21/getstarted/monitoring.html; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219]
- ServiceNow official documentation on Change Management, Dependency Views, and article versioning was not directly readable from the seeded URLs in this session, so ServiceNow-specific governance conclusions rely more on accessible community guidance and prior completed repository items than on first-party manual text. [inference; source: https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-ai-knowledge-rag-agents.html; https://davidamitchell.github.io/Research/research/2026-04-27-servicenow-orchestration-agentic-ai-roadmap.html]
- The evidence base is stronger for indexed corpora than for fully remote or ephemeral retrieval sources, so some version-pinning advice may need adaptation when the agent retrieves directly from live APIs or remote knowledge sources. [inference; source: https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview]
- The inspected evaluation tools show how to compare runs and monitor retrieval quality, but they do not by themselves prove that most teams in production already run corpus-version-aware gates, so maturity of real-world adoption remains uncertain. [inference; source: https://docs.smith.langchain.com/evaluation; https://docs.ragas.io/en/latest/howtos/cli/rag_eval/; https://www.trulens.org/component_guides/instrumentation/]

**Open questions:**

- Which minimum metadata set is sufficient for agent-to-corpus dependency registration: corpus identifier only, index alias plus timestamp, or retrieved-document hashes per run?
- What threshold of semantic delta or affected-article count should trigger mandatory regression testing before a corpus update is promoted?
- How should teams govern remote knowledge sources, where freshness is high but rollback and reproducibility are weaker than with pinned local indexes?

### §7 Recursive Review

- Review result: pass
- Acronym audit: Retrieval-Augmented Generation (RAG), Large Language Model (LLM), Configuration Management Database (CMDB), Information Technology Infrastructure Library (ITIL), Common Service Data Model (CSDM), Configuration Item (CI), and Artificial Intelligence Bill of Materials (AIBOM) expanded on first use
- Claim audit: visible claims in sections 0 to 6 are labeled or framed as metadata fragments, and Findings remain aligned with section 6 synthesis
- Cross-item audit: runtime dependency, dependency mapping, knowledge-governance, and runtime-divergence items incorporated into cites, synthesis, and evidence mapping

---

## Findings

### Executive Summary

Post-deployment document changes in Retrieval-Augmented Generation systems act like dependency updates: they can change the retrieved evidence, citations, and downstream agent behavior even when model weights and prompts stay fixed. [inference; source: https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview]

The highest-confidence failure mechanisms are stale or orphaned indexed content, duplicate or conflicting articles, chunk or structure changes that alter ranking, and multi-query retrieval plans that change which evidence reaches the model. [inference; source: https://learn.microsoft.com/azure/search/search-howto-index-changed-deleted-blobs?tabs=portal; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219; https://docs.datastax.com/en/ragstack/intro-to-rag/indexing.html; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview]

Current evaluation frameworks can catch many of these regressions through golden datasets, retrieval metrics, and traced production monitoring, but they do not turn the corpus version into a first-class governed dependency on their own. [inference; source: https://docs.smith.langchain.com/evaluation; https://docs.ragas.io/en/latest/howtos/cli/rag_eval/; https://docs.ragas.io/en/v0.1.21/getstarted/monitoring.html; https://www.trulens.org/getting_started/quickstarts/groundtruth_evals_for_retrieval_systems/; https://www.trulens.org/component_guides/instrumentation/]

The strongest operational pattern is to treat the corpus and index as deployable artifacts with version identifiers, staged promotion or alias swaps, rollback paths, and registry links from each agent to the corpus version it was tested against. [inference; source: https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html; https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html; https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]

### Key Findings

1. **Retrieval-Augmented Generation and agentic retrieval systems can change behavior after document updates because retrieved passages and query plans are part of the model input at inference time, not fixed compile-time assets.** ([inference]; high confidence; source: https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview)
2. **Retrieval regressions arise from more than factual edits, because failed deletion handling, renamed paths, duplicate articles, non-self-contained articles, and chunking changes can all alter what evidence is retrieved or summarized.** ([inference]; high confidence; source: https://learn.microsoft.com/azure/search/search-howto-index-changed-deleted-blobs?tabs=portal; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219; https://docs.datastax.com/en/ragstack/intro-to-rag/indexing.html)
3. **The most operationally important behavioral regressions are stale answers, missing facts, blended or contradictory answers, citation drift, and changed workflow choices when altered grounding changes what the agent considers relevant.** ([inference]; medium confidence; source: https://arxiv.org/abs/2312.10997; https://docs.ragas.io/en/v0.1.21/getstarted/monitoring.html; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219)
4. **LangSmith, Ragas, and TruLens collectively provide datasets, experiment comparison, retrieval metrics, ground-truth checks, and traced production monitoring, which together form the practical ingredients for corpus-change regression testing.** ([inference]; high confidence; source: https://docs.smith.langchain.com/evaluation; https://docs.ragas.io/en/latest/howtos/cli/rag_eval/; https://docs.ragas.io/en/v0.1.21/getstarted/monitoring.html; https://www.trulens.org/getting_started/quickstarts/groundtruth_evals_for_retrieval_systems/; https://www.trulens.org/component_guides/instrumentation/)
5. **None of the inspected evaluation frameworks or platform documents automatically turns the document corpus into a first-class dependency record, so teams need explicit corpus version identifiers, trace metadata, or registry entries to know what was tested and what is live.** ([inference]; medium confidence; source: https://docs.smith.langchain.com/evaluation; https://docs.ragas.io/en/latest/howtos/cli/rag_eval/; https://www.trulens.org/component_guides/instrumentation/; https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html)
6. **Mature rollout patterns already exist for the retrieval layer even though they are rarely described as RAG governance, because aliases, blue-green deployment, replicas, and retryable indexers provide the mechanics for staged promotion and rollback of new corpus versions.** ([inference]; high confidence; source: https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html; https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html; https://learn.microsoft.com/en-us/azure/reliability/reliability-ai-search; https://learn.microsoft.com/en-us/rest/api/searchservice/)
7. **Accessible vendor and repository evidence supports extending CMDB-like dependency mapping and ITIL-like change control to agent-to-corpus relationships, but the accessible sources do not show a mature off-the-shelf product that automatically registers each agent against the exact corpus version it depends on.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-ai-knowledge-rag-agents.html; https://davidamitchell.github.io/Research/research/2026-04-27-servicenow-orchestration-agentic-ai-roadmap.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Retrieved passages and query plans are runtime inputs, so document updates can change behavior without a model release. | https://arxiv.org/abs/2005.11401 ; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation ; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview | high | Propagation mechanism |
| [inference] Failed deletion handling, rename drift, duplicates, weak article structure, and chunking changes are distinct regression triggers. | https://learn.microsoft.com/azure/search/search-howto-index-changed-deleted-blobs?tabs=portal ; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219 ; https://docs.datastax.com/en/ragstack/intro-to-rag/indexing.html | high | Source-layer failure classes |
| [inference] Stale answers, omissions, blended answers, citation drift, and changed workflow choice are the main behavior regressions. | https://arxiv.org/abs/2312.10997 ; https://docs.ragas.io/en/v0.1.21/getstarted/monitoring.html ; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview ; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219 | medium | Output and action effects |
| [inference] LangSmith, Ragas, and TruLens collectively provide the building blocks needed for corpus-change regression testing. | https://docs.smith.langchain.com/evaluation ; https://docs.ragas.io/en/latest/howtos/cli/rag_eval/ ; https://docs.ragas.io/en/v0.1.21/getstarted/monitoring.html ; https://www.trulens.org/getting_started/quickstarts/groundtruth_evals_for_retrieval_systems/ ; https://www.trulens.org/component_guides/instrumentation/ | high | Datasets, traces, retrieval metrics |
| [inference] Corpus versioning is not first-class in the inspected tools, so teams must attach metadata or registry records themselves. | https://docs.smith.langchain.com/evaluation ; https://docs.ragas.io/en/latest/howtos/cli/rag_eval/ ; https://www.trulens.org/component_guides/instrumentation/ ; https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html | medium | Control-plane gap |
| [inference] Alias swaps, blue-green rollout, replicas, and recoverable indexers support staged promotion and rollback for corpus versions. | https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html ; https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html ; https://learn.microsoft.com/en-us/azure/reliability/reliability-ai-search ; https://learn.microsoft.com/en-us/rest/api/searchservice/ | high | Release mechanics |
| [inference] CMDB-like dependency mapping and ITIL-like change control can be extended to agent-to-corpus relationships, but a mature automatic registration pattern is still missing. | https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html ; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-ai-knowledge-rag-agents.html ; https://davidamitchell.github.io/Research/research/2026-04-27-servicenow-orchestration-agentic-ai-roadmap.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html ; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219 | medium | Registry-extension gap |

### Assumptions

- **Assumption:** Teams can surface stable corpus or index version identifiers even when tools do not require them. **Justification:** aliases, index objects, and custom trace attributes already exist in the inspected infrastructure, so the missing piece is discipline rather than a missing technical hook. [assumption; source: https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html; https://learn.microsoft.com/en-us/rest/api/searchservice/; https://www.trulens.org/component_guides/instrumentation/]
- **Assumption:** For remote knowledge sources, an equivalent control can use source snapshot identifiers, retrieval-response identifiers, or timestamped export bundles when no local search index exists. **Justification:** Azure AI Search explicitly supports remote knowledge sources in agentic retrieval, so version pinning cannot rely only on local index names. [assumption; source: https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview]
- **Assumption:** The inaccessible full ITIL practice guide would not reverse the governance mapping here, because the recommendation is limited to controls already visible in accessible rollout and content-governance sources: approval, impact review, staged promotion, and rollback readiness. [assumption; source: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html; https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219]

### Analysis

The evidence was weighted toward foundational RAG papers and current platform documentation because the core question is operational causality, namely how a document change reaches inference-time behavior, rather than market positioning or vendor rhetoric. [inference; source: https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview; https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html]

Mechanism evidence is stronger than incident evidence: Lewis and Azure show how corpus changes alter the prompt surface, while Azure and ServiceNow show concrete ways stale, deleted, duplicate, or weakly structured content can survive into retrieval and summarization. [inference; source: https://arxiv.org/abs/2005.11401; https://learn.microsoft.com/azure/search/search-howto-index-changed-deleted-blobs?tabs=portal; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219]

The evaluation frameworks are useful but incomplete for governance because they measure outcomes and traces, not authoritative dependency registration; prior repository work on dependency mapping and runtime divergence fills that missing control-plane perspective. [inference; source: https://docs.smith.langchain.com/evaluation; https://docs.ragas.io/en/latest/howtos/cli/rag_eval/; https://www.trulens.org/component_guides/instrumentation/; https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]

A rival response would be to keep corpora fully live for freshness and accept occasional regression, but alias and blue-green rollout sources show that safer staged promotion is already technically normal in search infrastructure, so unmanaged freshness is a governance choice rather than a technical inevitability. [inference; source: https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html; https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html; https://learn.microsoft.com/en-us/azure/reliability/reliability-ai-search]

### Risks, Gaps, and Uncertainties

- Publicly accessible named postmortems for document-drift incidents remain sparse in the inspected source base, so incident prevalence and typical blast radius are lower-confidence than the mechanism and mitigation claims above. [inference; source: https://docs.smith.langchain.com/evaluation; https://docs.ragas.io/en/v0.1.21/getstarted/monitoring.html; https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219]
- ServiceNow official documentation on Change Management, Dependency Views, and article versioning was not directly readable from the seeded URLs in this session, so ServiceNow-specific governance conclusions rely more on accessible community guidance and prior completed repository items than on first-party manual text. [inference; source: https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-ai-knowledge-rag-agents.html; https://davidamitchell.github.io/Research/research/2026-04-27-servicenow-orchestration-agentic-ai-roadmap.html]
- The evidence base is stronger for indexed corpora than for fully remote or ephemeral retrieval sources, so some version-pinning advice may need adaptation when the agent retrieves directly from live APIs or remote knowledge sources. [inference; source: https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search; https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview]
- The inspected evaluation tools show how to compare runs and monitor retrieval quality, but they do not by themselves prove that most teams in production already run corpus-version-aware gates, so maturity of real-world adoption remains uncertain. [inference; source: https://docs.smith.langchain.com/evaluation; https://docs.ragas.io/en/latest/howtos/cli/rag_eval/; https://www.trulens.org/component_guides/instrumentation/]

### Open Questions

- Which minimum metadata set is sufficient for agent-to-corpus dependency registration: corpus identifier only, index alias plus timestamp, or retrieved-document hashes per run?
- What threshold of semantic delta or affected-article count should trigger mandatory regression testing before a corpus update is promoted?
- How should teams govern remote knowledge sources, where freshness is high but rollback and reproducibility are weaker than with pinned local indexes?

---

## Output

- Type: knowledge
- Description: This item defines a drift taxonomy and operating model for treating RAG corpora as versioned runtime dependencies with baseline evaluation, staged promotion, rollback, and explicit dependency registration. [inference; source: https://arxiv.org/abs/2005.11401; https://docs.smith.langchain.com/evaluation; https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html; https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html]
- Links:
  - https://arxiv.org/abs/2005.11401
  - https://docs.smith.langchain.com/evaluation
  - https://www.elastic.co/guide/en/elasticsearch/reference/current/aliases.html
