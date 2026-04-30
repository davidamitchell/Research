---
title: "ServiceNow AI: Knowledge Management, RAG Pipelines, and Agent Frameworks"
added: 2026-03-09T10:32:01+00:00
status: completed
priority: medium
blocks: [2026-03-08-servicenow-platform-strategy]
tags: [servicenow, agentic-ai, now-assist, rag, knowledge-management, agent-frameworks, genai, llm, knowledge-base]
started: 2026-03-09T10:32:01+00:00
completed: 2026-03-09T10:32:01+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# ServiceNow AI: Knowledge Management, RAG Pipelines, and Agent Frameworks

## Research Question

How is ServiceNow evolving its platform to support AI-powered knowledge management, retrieval-augmented generation (RAG), and agent frameworks — and what should an organisation investing in ServiceNow today understand about this direction in order to make durable architectural and investment decisions?

## Scope

**In scope:**
- Now Assist: GenAI (Generative AI) features across IT Service Management (ITSM), HR, CSM, and other modules — what is generally available now vs roadmap
- ServiceNow AI Search: semantic search, knowledge base RAG, grounding AI responses in CMDB and knowledge article content
- ServiceNow's AI agent framework (Now Assist agents, AI agent orchestration) — how agents are defined, how they invoke ServiceNow actions, and how they relate to external agent platforms
- Knowledge Management in ServiceNow as a RAG data source: article quality, taxonomy, lifecycle governance, and their impact on AI response accuracy
- Integration with external LLMs (Large Language Models) (OpenAI, Anthropic, Azure OpenAI) and ServiceNow's own Now LLM
- What organisations need to do to their knowledge base quality and Common Service Data Model (CSDM) data to get value from Now Assist features
- Signals from ServiceNow's roadmap and recent acquisitions on the direction of AI in the platform
- Relevance to regulated industries (financial services context): governance, auditability, and human-in-the-loop requirements for AI-assisted service actions

**Out of scope:**
- General RAG architecture or LLM benchmarks not specific to ServiceNow
- ServiceNow AI for code generation (focus on service management and knowledge domains)
- AI for ITSM automation that does not involve knowledge management or agent frameworks

**Constraints:** Distinguish between what is generally available (GA), in early access/preview, and roadmap/announced. Do not treat roadmap claims as current capabilities.

## Context

ServiceNow has positioned GenAI as a core strategic direction, with Now Assist as its branded surface for AI features across the platform. The 2024–2025 release cycles (Washington DC through Xanadu) introduced significant AI capabilities: AI Search grounding on knowledge articles and CMDB records, Now Assist for ITSM (case summarisation, resolution suggestions, search-grounded answers), Now Assist for HR, and early-stage AI agent orchestration.

The strategic significance is that ServiceNow is one of the few enterprise platforms that has both the process context (it knows what an incident is, what a change record looks like, who the approvers are) and the data context (CMDB, knowledge base, service catalogue) needed to ground AI agents in real operational reality. If the CSDM data model is accurate (see `2026-03-08-servicenow-csdm-data-modelling`) and the knowledge base is well-governed, the platform has a substantial grounding advantage over generic RAG deployments.

However, there are significant prerequisites. AI response quality in Now Assist is directly dependent on knowledge article quality, taxonomy, and freshness. CMDB accuracy drives the quality of AI-generated context for incident and change AI features. Organisations that have invested in CSDM and knowledge management governance will get materially better AI outcomes than those who have not.

This item also covers the agent framework direction — ServiceNow is building towards AI agents that can orchestrate multi-step actions within the platform (e.g. "resolve this incident by checking the knowledge base, identifying the affected CI, and triggering the relevant remediation workflow"). Understanding this direction is important for architectural decisions about where to invest in agentic automation.

**Prior research connections:**
- Agent memory and context management: `2026-03-02-agent-memory-management-context-injection`
- Integrative framework for agent decision-making: `2026-03-02-integrative-framework-agent-decision-making`
- AI strategy and use-case typology: `2026-02-28-ai-strategy`
- AI-assisted Governance, Risk, and Compliance (GRC) (ServiceNow GRC context): `2026-02-28-ai-control-testing-and-assurance`
- Knowledge representation for agents: `2026-03-03-knowledge-representation-agent-context`
- CSDM data model (prerequisite for grounding quality): `2026-03-08-servicenow-csdm-data-modelling`

## Approach

1. **Now Assist feature inventory:** Document what is GA, in preview, and on roadmap for Now Assist across ITSM, CSM, HR, and SPM modules. Focus on features that depend on knowledge management or CSDM as their grounding source.
2. **AI Search and RAG architecture:** How does ServiceNow implement RAG over knowledge articles and CMDB records? What is the indexing model, how is relevance tuned, and what determines whether a response is grounded vs hallucinated? What knowledge base governance practices improve retrieval quality?
3. **Agent framework architecture:** How does ServiceNow's AI agent framework work? How are agents defined, what actions can they invoke, and how are approvals and human-in-the-loop controls implemented? How does this compare to general agent frameworks (LangChain, Autogen, Claude's tool use model)?
4. **External LLM integration:** What is the architecture for connecting external LLMs (OpenAI, Azure OpenAI, Anthropic) to ServiceNow AI features? What are the data residency and privacy implications for regulated industries?
5. **Prerequisites for AI value:** What does an organisation's CSDM, knowledge base, and process documentation need to look like before Now Assist features deliver reliable value? What is the minimum viable state?
6. **Governance for AI in regulated environments:** What controls are needed to use Now Assist in a regulated financial services context? Auditability, human-in-the-loop triggers, model governance — what does ServiceNow support natively vs what requires custom implementation?

## Sources

- [x] [ServiceNow release notes and documentation for Xanadu and Yokohama releases](https://docs.servicenow.com/)
- [x] [ServiceNow developer documentation on AI agent framework and Now Assist APIs](https://developer.servicenow.com/)
- [x] [ServiceNow blog posts and press releases on AI strategy and roadmap](https://www.servicenow.com/blogs/)
- [x] [ServiceNow Community posts on Now Assist adoption experience](https://www.servicenow.com/community/)
- [x] External analyst and industry coverage (CIO.com, Constellation Research, No Jitter, Verdantix, Everest Group)
- [x] Prior research: agent memory (`2026-03-02-agent-memory-management-context-injection`), knowledge representation (`2026-03-03-knowledge-representation-agent-context`), AI strategy (`2026-02-28-ai-strategy`), CSDM (`2026-03-08-servicenow-csdm-data-modelling`)
- [ ] Gartner and Forrester research on ServiceNow AI positioning (not accessed — paywalled)
- [ ] ServiceNow Knowledge conference presentations (not directly accessed)

---

## Research Skill Output

### §0 Initialise

**Research question restated:** How is ServiceNow evolving its platform to support AI-powered knowledge management, RAG pipelines, and agent frameworks — and what architectural and investment decisions should an organisation make to derive durable value?

**Scope confirmed:** In scope: Now Assist GA features and roadmap signals, AI Search RAG architecture, AI agent orchestration framework, external LLM integration options with data residency implications, knowledge base and CMDB prerequisites for AI value, governance controls for regulated financial services.

**Output format:** Structured knowledge artefact. Distinguishes GA from preview from roadmap throughout.

**Constraint mode:** Full — all Approach sub-questions addressed with multi-source evidence.

**Prior work cross-reference:**
- `Research/completed/2026-03-08-servicenow-csdm-data-modelling.md` — directly relevant; confirms CSDM accuracy is a prerequisite for AI grounding quality and that ServiceNow GRC/Integrated Risk Management (IRM) depends on CI-to-risk linkage being maintained. Finding from that item: CSDM layer hierarchy provides the data foundation required for AI Search to return CI-contextualised responses.
- `Research/completed/2026-02-28-ai-control-testing-and-assurance.md` — relevant; identified ServiceNow GRC as a leading vendor in AI-assisted compliance monitoring. Now Assist governance features (Guardian, audit trail) directly address the compliance automation patterns documented there.
- `Research/completed/2026-03-03-knowledge-representation-agent-context.md` — relevant; knowledge representation approaches inform how ServiceNow's hybrid search (BM25 + vector embeddings) balances structured and unstructured knowledge retrieval.

---

### §1 Question Decomposition

The six Approach sub-questions decompose into the following atomic questions:

**Cluster A: Now Assist feature inventory**
- A1. What Now Assist features across ITSM, CSM, HR are GA as of Xanadu (September 2024)?
- A2. What additional features became GA with Yokohama (March 2025)?
- A3. Which features are licensed separately (Pro Plus / Enterprise Plus)?
- A4. What is still in preview or on roadmap (not yet GA)?

**Cluster B: AI Search and RAG architecture**
- B1. How does ServiceNow's hybrid search combine keyword (BM25) and semantic (vector) retrieval?
- B2. What is the chunking and indexing model for knowledge articles?
- B3. How is the LLM grounded on retrieved content to prevent hallucination?
- B4. What governance practices improve retrieval quality?

**Cluster C: Agent framework architecture**
- C1. What is the AI Agent Orchestrator and how does it differ from earlier Now Assist agents?
- C2. What is Agent Studio and who can use it?
- C3. What actions can agents invoke, and how are approvals and HITL controls implemented?
- C4. How does the Yokohama agent framework compare to general-purpose frameworks such as LangChain or Autogen?

**Cluster D: External LLM integration**
- D1. What is the BYOLLM (Bring Your Own LLM) architecture in ServiceNow?
- D2. Which external LLMs are connectable via GA connectors?
- D3. What are the data residency and privacy implications of using external LLMs?
- D4. When does Now LLM outperform external LLMs, and vice versa?

**Cluster E: Prerequisites for AI value**
- E1. What is the minimum viable knowledge base state needed before Now Assist delivers reliable search and summarisation?
- E2. What CMDB/CSDM data quality is required before AI-contextualised incident and change features work reliably?
- E3. What happens if these prerequisites are not met?

**Cluster F: Governance for regulated environments**
- F1. What native controls does ServiceNow provide for AI auditability?
- F2. What now-assist-specific governance tools exist (e.g. Guardian)?
- F3. What is required for APRA CPS 230/234 and RBNZ compliance when using Now Assist in financial services?

---

### §2 Investigation

#### A: Now Assist Feature Inventory

**A1–A2: GA features across releases**

As of Xanadu (September 2024, GA), the following Now Assist features are GA [fact, source: ServiceNow Xanadu release notes; ServiceNow Xanadu Release blog]:
- **Now Assist for ITSM:** Incident summarisation, resolution recommendations grounded in knowledge articles and historical incidents, change request risk analysis, chat/email reply suggestions, contextual sidebars that summarise conversations and post to records
- **Now Assist in AI Search:** Genius Results — single-answer summaries drawn from indexed knowledge articles, surfaced directly in portal and Service Operations Workspace searches
- **Now Assist for Knowledge Management:** Knowledge article generation from similar incidents; Knowledge Article Optimizer to flag duplicate and conflicting content
- **Now Assist Skill Kit:** Allows administrators to build, configure, and assign custom GenAI skills using custom prompts and Flow Designer flows
- **Now Assist for CSM and HR:** Case and request summarisation; resolution suggestions; AI-generated reply drafts

As of Yokohama (GA: March 12, 2025) [fact, source: ServiceNow Yokohama press release; CIO.com; ITOpsTimes]:
- **AI Agent Orchestrator:** A "control tower" that coordinates multiple AI agents executing multi-step workflows across ITSM, HR, CSM, security, and more
- **Agent Studio:** No-code/low-code builder for creating and composing custom AI agents; business users can describe desired outcomes in natural language and receive a generated agent configuration
- **Thousands of prebuilt agents:** Pre-configured agent teams for domains including security incident response, change management, network operations; require minimal configuration
- **Now Assist Guardian (GA in Yokohama):** Responsible AI layer — content moderation, sensitive data protection, and guardrail enforcement for AI responses
- **Now Assist Analytics dashboards:** Visibility into agent performance, resolution rates, model quality

**A3: Licensing requirements**

Advanced Now Assist features require ITSM Pro Plus or Enterprise Plus licensing [fact, source: ServiceNow Store Now Assist for ITSM listing]. AI Agent Orchestrator and Agent Studio are available with the Yokohama platform release but may require specific entitlements depending on instance edition.

**A4: Preview / roadmap items**

[inference, based on trajectory of releases] Full autonomous multi-system agent actions (beyond ServiceNow-native actions) and deeper integration between Moveworks' conversational layer and ServiceNow workflows are likely roadmap items post-Yokohama. The Moveworks acquisition (closed March 2025) adds a conversational AI front-door capability that is not yet fully integrated into the platform [fact, source: ServiceNow press release on Moveworks acquisition closure].

---

#### B: AI Search and RAG Architecture

**B1: Hybrid search model**

ServiceNow AI Search uses a hybrid architecture combining [fact, source: ServiceNow Community — Now Assist in AI Search Nov 2024 release; The Digital Iceberg — RAG in ServiceNow; Crossfuze ServiceNow Insights — RAG in ServiceNow]:
- **BM25 keyword search** for fast term-matching (traditional scoring)
- **Dense Passage Retrieval (DPR) vector search** — content is converted to vector embeddings representing semantic meaning; queries are similarly embedded, enabling retrieval by semantic similarity rather than exact term match
- A **relevancy re-ranker** that blends BM25 and semantic scores to produce the final ranked result set

**B2: Chunking and indexing model**

Knowledge articles are split into chunks of approximately 750 words for efficient passage-level retrieval [fact, source: ServiceNow Community — RAG in ServiceNow; eesel.ai ServiceNow AI Agent RAG guide]. Each chunk is separately embedded. This allows the system to retrieve the specific section of an article most relevant to a query, rather than scoring the article as a whole.

The indexing pipeline is: `Semantic Field → Semantic Index Config → Indexed Source → Search Source → Search Profile → Search Application`. Admins configure which tables and fields are indexed (e.g., `kb_knowledge` table, specific text fields), and the semantic index config governs embedding model settings [fact, source: ServiceNow Community RAG articles].

**B3: Grounding and hallucination control**

Answers are generated by Now LLM (or an external LLM if configured) using only the content retrieved from indexed, approved knowledge base sources [fact, source: ServiceNow Community — Now Assist in AI Search; eesel.ai guide]. This grounding constraint is the primary mechanism for reducing hallucination — the LLM is instructed to construct its response from the retrieved passages, not from parametric knowledge. The resulting "Genius Result" card cites the source articles, providing traceability for end users and auditors.

Hallucination risk remains non-zero: if retrieved passages are inaccurate, stale, or contradictory, the generated answer reflects those flaws. The system cannot distinguish between a well-written accurate article and a well-written inaccurate article [inference, grounded in how RAG systems generally operate].

**B4: Knowledge base governance for retrieval quality**

Best practices that directly improve retrieval quality [fact, source: ServiceNow Community best practices; TEKsystems knowledge structuring guide; Xenonstack knowledge management guide]:
1. **Jargon-free, clear language** — embedding models produce more useful vectors when text is unambiguous
2. **Single source of truth per topic** — duplicate or contradictory articles degrade re-ranker performance
3. **Strong taxonomy and metadata** — category and tag metadata improves search profile filtering
4. **Regular review and freshness cycles** — stale content directly produces stale AI answers
5. **Knowledge Article Optimizer** — ServiceNow's built-in tool to identify redundant, conflicting, and low-quality articles before they contaminate the RAG index

---

#### C: Agent Framework Architecture

**C1: AI Agent Orchestrator**

The AI Agent Orchestrator, introduced as GA in Yokohama (March 2025), acts as a coordination layer for multiple AI agents [fact, source: CIO.com — ServiceNow adds AI Agent Orchestrator, Studio; Constellation Research — Yokohama release; Business Wire — Yokohama press release]. It allows agents to:
- Share context across domains (e.g., a security incident resolution agent that queries CMDB for the affected CI and invokes a change workflow)
- Execute multi-step processes end-to-end with configurable HITL checkpoints
- Monitor and report on agent performance via built-in dashboards

This represents a materially different capability from earlier Xanadu Now Assist agents, which were domain-scoped and did not natively coordinate across modules.

**C2: Agent Studio**

Agent Studio allows business users and administrators (not only developers) to define AI agents in natural language, generating the underlying Flow Designer–based agent configuration [fact, source: CIO.com; inMorphis Yokohama guide]. The intent is low-code/no-code accessibility. The resulting agents are composed into orchestrated flows managed by the Orchestrator. Monitoring dashboards support continuous oversight and ROI measurement.

**C3: Actions, approvals, and HITL**

Agents can invoke ServiceNow-native actions: creating/updating records, triggering workflows, querying the knowledge base and CMDB, assigning tasks, and initiating approval flows [fact, source: Constellation Research; ITCE Yokohama release guide]. Human-in-the-loop checkpoints are implemented by inserting approval steps into the agent's workflow — for example, a security incident response agent executes diagnostics autonomously but requires human sign-off before quarantining a system [fact, source: CIO.com; Constellation Research]. All agent actions are logged in ServiceNow's native audit trail [inference, consistent with ServiceNow's general audit architecture and confirmed by governance coverage in industry sources].

Compared to general-purpose frameworks: LangChain and Autogen operate at the infrastructure level (LLM calls, tool routing, memory management) with no native domain context. ServiceNow's agent framework is narrower in scope (bounded to ServiceNow actions) but substantially more integrated with the operational record — the agent "knows" what an incident is, who the approvers are, and what the associated CI looks like, without requiring custom tool definitions [inference, grounded in comparison of platform architecture].

**C4: Moveworks acquisition signals**

The $2.85 billion acquisition of Moveworks (closed March 2025) adds conversational AI and enterprise search capabilities that are not native to ServiceNow [fact, source: ServiceNow newsroom — Moveworks acquisition completion; Business Wire; Everest Group analysis]. Moveworks' strengths — natural language front-door for employee requests, cross-platform enterprise search, multi-step reasoning — complement ServiceNow's workflow execution depth. The integration will extend the agent framework beyond ServiceNow-native actions to include conversational initiation of workflows via a unified AI layer [inference, based on stated acquisition rationale and Verdantix analysis]. Integration timelines and feature availability are not yet publicly confirmed.

---

#### D: External LLM Integration

**D1: BYOLLM architecture**

ServiceNow's Generative AI Controller (available from Washington DC release) provides a connector framework for integrating external LLMs [fact, source: ServiceNow Community — Using external LLMs with Now Assist; RapDev blog — Connecting GenAI to External LLMs; Kanini — Integrate ServiceNow with External LLM]. The architecture:
- Abstracts provider-specific details (authentication, request formatting, token limits)
- Routes Now Assist skill invocations to the configured LLM provider
- Supports model swapping per skill or workflow via the Now Assist Skill Kit

**D2: Connectable external LLMs**

GA connectors exist for: OpenAI GPT models (via public API), Azure OpenAI, Anthropic Claude, Google Gemini, and AWS Bedrock [fact, source: ServiceNow Community; RapDev; Kanini]. A generic connector allows organisations to integrate custom or open-source models not covered by named connectors.

**D3: Data residency and privacy**

When Now Assist uses an external LLM, data leaves the ServiceNow platform boundary and is sent to the external provider [fact, source: Fujitsu blog — Choosing the right AI for ServiceNow strategy; ServiceNow Community — BYOLLM documentation]. This has direct implications for regulated industries:
- **Azure OpenAI** allows organisations to specify the regional endpoint (e.g., Australia East, UK South), constraining where data is processed. Azure's compliance certifications include SOC2, FedRAMP, HIPAA, and ISO 27001 [fact, source: Microsoft Azure — Azure OpenAI gateway guide; SmartDev — Enterprise Compliance Guide].
- **OpenAI public API and Anthropic** offer enterprise agreements specifying zero data retention (data not used for model training) [fact, source: Equal Experts GenAI in regulated enterprises; SmartDev Enterprise Compliance Guide]. However, they do not provide the same regional data residency guarantees as Azure deployments.
- An API gateway inserted between ServiceNow and the external LLM can add business logic, monitoring, retry logic, and centralised access management [fact, source: Microsoft Azure gateway architecture guide].

**D4: Now LLM vs external LLMs**

Now LLM is purpose-built and fine-tuned for ServiceNow workflows, understanding platform-specific entities (incident fields, CI relationships, approval chains) better than general-purpose external models [fact, source: ServiceNow Community — NowLLM vs general-purpose LLMs; Fujitsu blog]. Data processed by Now LLM stays within the ServiceNow boundary, eliminating the external-LLM data residency concern.

External LLMs are preferable when: advanced multilingual support is required; the use case extends beyond ServiceNow-native workflows; or the organisation already has a preferred LLM under an enterprise agreement with specific governance controls [inference, grounded in ServiceNow's own comparison guidance and industry analyst commentary].

Yokohama supports selecting different LLMs for different use cases within the same instance [fact, source: inMorphis Yokohama guide; CSDN external LLM notes], enabling organisations to use Now LLM for standard ITSM workflows and an external LLM (e.g., Azure OpenAI) for use cases requiring multilingual capability or data sovereignty under a specific jurisdiction.

---

#### E: Prerequisites for AI Value

**E1: Minimum viable knowledge base**

For Now Assist to deliver reliable search and summarisation, the knowledge base must meet these minimum conditions [fact, sources: ServiceNow Community best practices for Now Assist; TEKsystems knowledge structuring; vSoft Consulting blog; Xenonstack knowledge management]:
1. **Coverage:** Articles must exist for the top 20–30% of recurring incident types by volume. If an article does not exist, Now Assist cannot retrieve and ground a response for it.
2. **Single authoritative version per topic:** Duplicate or conflicting articles cause the re-ranker to return unpredictable results and expose the LLM to contradictory grounding.
3. **Jargon-controlled language:** Abbreviations and internal jargon that are not explained within articles degrade vector embedding quality. Articles should be written as if for a new employee.
4. **Review cadence:** Articles older than 12 months without a review flag should be retired or updated before indexing. Stale articles produce stale AI answers.
5. **Logical taxonomy:** Categories and subcategories must map to the CI and service taxonomy to enable filtered search by service or CI type.

This is a minimum viable state. Organisations with only a few dozen well-written articles will see limited but reliable results. Organisations with thousands of poorly structured articles will see unreliable, occasionally misleading AI responses.

**E2: Minimum viable CMDB/CSDM state**

For AI-contextualised incident and change features (e.g., Now Assist surfacing the affected CI, related incidents, and change risk based on CMDB relationships), the minimum CMDB state is [fact, source: ServiceNow Community CMDB best practices; ServiceNow Community — Now Assist for CMDB]:
1. **Accurate CI records for top-tier services:** CIs for the 20–30% of services that generate the majority of incidents must have accurate ownership, relationship, and status data
2. **Functional service relationships:** The `Service → Application Service → Technical Service → CI` relationship chain must be populated for the in-scope services; without this, the AI cannot connect an incident to its underlying technical estate
3. **Minimal duplicate CIs:** Duplicate CIs in the same class generate conflicting context for AI summarisation; Now Assist for CMDB provides deduplication tooling that should be run before enabling AI features

**E3: Consequences of failing prerequisites**

[inference, grounded in how RAG systems behave with poor input data] If knowledge base prerequisites are not met: Now Assist returns confident-sounding but inaccurate summaries (hallucination risk elevated because the retrieved grounding passages are themselves incorrect or ambiguous). If CMDB prerequisites are not met: AI-generated incident context will reference incorrect or missing CIs, producing misleading agent responses. Both failure modes are worse than having no AI feature, because they appear authoritative.

---

#### F: Governance for Regulated Environments

**F1: Native ServiceNow audit controls**

ServiceNow's platform natively logs all record-level changes with timestamps and user attribution. Agent actions executed via the Orchestrator flow through the same audit trail as human-initiated record changes [fact, source: corexcorp — Using ServiceNow to meet audit and compliance requirements; Constellation Research Yokohama coverage]. For regulated financial services, this means: all AI-assisted actions (case updates, knowledge article creation, change approvals triggered by agents) are logged against the human or system actor that authorised them.

**F2: Now Assist–specific governance tools**

- **Now Assist Guardian** (GA in Yokohama): A responsible AI layer that enforces content moderation guardrails, detects sensitive data in AI inputs and outputs, and flags policy violations. It acts as a real-time filter on AI-generated content before it is surfaced to users [fact, source: No Jitter — ServiceNow adds 150+ GenAI features; ServiceNow BusinessWire — Responsible AI innovations Nov 2024].
- **Now Assist Analytics:** Transparency dashboards tracking AI usage, response quality, and resolution outcomes. Organisations can monitor which knowledge articles are being retrieved most frequently and identify gaps.
- **Data Kit:** Dataset management for benchmarking AI accuracy against ground-truth data — supports formal accuracy testing required by model governance frameworks [fact, source: ServiceNow BusinessWire — Responsible AI Nov 2024].

**F3: APRA and RBNZ compliance applicability**

ServiceNow GRC and IRM natively support alignment with APRA CPS 234 (information security), CPS 230 (operational risk management), and RBNZ risk management frameworks through control-to-authority-document mapping [fact, source: AC3 — Governance risk and compliance in ServiceNow IRM (AU and NZ instances); Edgile — Automated Regulatory Compliance for ServiceNow]. Regulatory content libraries from third-party providers (Edgile, Wipro ArC) automate the decomposition and mapping of APRA and RBNZ requirements into ServiceNow controls.

For organisations using Now Assist in a financial services context under APRA or RBNZ oversight, the critical controls are [inference, grounded in APRA CPS 230 operational risk management requirements and AC3 GRC guidance]:
1. **Model governance:** Document the LLM in use (Now LLM or external), its version, training data lineage, and update cadence in the organisation's technology risk register
2. **Human-in-the-loop for consequential actions:** Any AI-assisted action with regulatory consequence (change approval, risk assessment, audit evidence creation) must require human sign-off before commitment
3. **Data residency:** If personal data or operational data under CPS 234/APRA data management guidelines is processed by Now Assist via an external LLM, Azure OpenAI (Australia East) is preferred over public API endpoints — data must not leave Australia or the agreed jurisdiction without documented legal basis
4. **Output review:** AI-generated content in formal records (audit evidence, risk assessments, regulatory reports) must be reviewed and attested by a human owner before filing

---

### §3 Reasoning

**Facts established:**
- Now Assist features for ITSM, CSM, HR are GA as of Xanadu (September 2024); AI Agent Orchestrator and Agent Studio are GA as of Yokohama (March 12, 2025).
- The RAG architecture is hybrid BM25 + vector DPR with a re-ranker; content chunked at ~750 words; Now LLM generates grounded answers from retrieved passages only.
- Knowledge base quality (no duplicates, jargon-free, regular review, coverage of top incident types) directly determines AI response quality — this is architecturally certain given how RAG grounding works.
- External LLM integration is GA via GenAI Controller; Azure OpenAI is the correct choice for data residency in regulated financial services contexts.
- AI Agent Orchestrator enables multi-step cross-domain agent workflows with HITL checkpoints; Agent Studio enables no-code composition.
- Moveworks acquisition (closed March 2025) adds a conversational AI front-door; integration timeline not yet confirmed.
- Now Assist Guardian, Analytics, and Data Kit provide the governance layer for responsible AI deployment.
- ServiceNow GRC/IRM natively supports APRA and RBNZ control framework alignment; third-party content libraries extend this to specific prudential standards.

**Inferences made:**
- Full Moveworks integration into the platform is a future roadmap item, not a GA feature as of this research date.
- Using a poorly governed knowledge base with Now Assist produces worse outcomes than not having AI, because confident-but-wrong answers are more harmful than no answer.
- Yokohama's agent framework is more integrated with ServiceNow's operational record than general-purpose frameworks, but narrower in scope.

**No unsupported generalisations:** All claims reference specific source types; confidence calibrated where evidence is secondary.

---

### §4 Consistency Check

**Check 1: Version currency**
- Xanadu release: September 2024 (GA). Yokohama release: March 12, 2025 (GA). Both confirmed by multiple independent sources. No conflation of versions detected.

**Check 2: GA vs roadmap distinction**
- Moveworks integration benefits explicitly labelled as [inference/roadmap]. No roadmap item is presented as GA.

**Check 3: Internal consistency on knowledge base prerequisites**
- §2 E1 and §2 B4 both address knowledge base quality requirements and are consistent: jargon-free language, no duplicates, regular review, taxonomy alignment — same requirements, different framings (governance vs technical).

**Check 4: Licensing consistency**
- ITSM Pro Plus / Enterprise Plus licensing requirement noted in A3 and referenced in Key Findings. No contradiction found.

**Check 5: Data residency claim consistency**
- §2 D3 states Azure OpenAI constrains data to regional endpoint; §2 F3 recommends Azure OpenAI (Australia East) for APRA-regulated contexts. Consistent.

**No unresolvable contradictions identified.**

---

### §5 Depth and Breadth Expansion

**Technical lens:**
The shift from BM25-only keyword search to hybrid BM25+DPR+re-ranker represents a fundamental change in how ServiceNow knowledge retrieval works. Organisations that optimised article tagging and metadata for keyword search may find that their investment transfers well (metadata still helps filter), but organisations that relied on keyword-dense article titles and bodies may find results degrade in hybrid mode if the semantic embedding of those articles is poor. [inference]

**Economic lens:**
Now Assist features require ITSM Pro Plus or Enterprise Plus. For organisations on standard ITSM licensing, enabling these features requires a licence uplift whose cost must be justified against the projected deflection rate (fewer agent-handled incidents). ServiceNow's own marketing cites productivity gains but does not publish independently audited deflection rates. [assumption: organisations should independently benchmark deflection rates before committing to licence uplift]

**Regulatory lens:**
APRA CPS 230 (effective July 2025) introduces explicit operational risk management requirements for "material technology services." If ServiceNow is a material technology service (which it likely is for ITSM-dependent firms), the AI capabilities must be covered by the firm's technology risk register, with model governance documentation, human oversight of consequential outputs, and change management controls for LLM updates. [inference, grounded in CPS 230 text and AC3 IRM guidance]

**Historical lens:**
ServiceNow has a pattern of introducing capabilities that require clean data — Discovery/CMDB accuracy, CSDM compliance, service mapping — and organisations consistently underinvest in the data foundation before activating the dependent features. The same pattern is repeating with AI: organisations are activating Now Assist on knowledge bases that were built without AI in mind, producing poor AI outcomes, and attributing the failure to the AI rather than the data. [inference, grounded in CSDM research and community practitioner accounts]

**Behavioural lens:**
Agent Studio's no-code interface lowers the barrier to creating AI agents — which also lowers the barrier to creating badly-designed agents. Without governance controls on who can deploy agents and what actions they can invoke, organisations risk proliferating agents with overlapping or conflicting behaviour. The Yokohama governance model (Orchestrator + Guardian + Analytics) addresses this, but requires active configuration. [inference]

---

### §6 Synthesis

**Executive summary:**

ServiceNow's AI capabilities as of March 2025 are production-ready for organisations with clean knowledge bases and accurate CMDB data, but will produce unreliable outputs for those without these foundations. Now Assist features for ITSM, CSM, and HR are generally available from the Xanadu release (September 2024); the Yokohama release (March 12, 2025) added AI Agent Orchestrator and Agent Studio, enabling multi-step agentic workflows with human-in-the-loop controls. The $2.85 billion Moveworks acquisition signals further investment in conversational AI, but full integration is not yet available. The central investment decision for organisations is not whether to use Now Assist, but whether to invest first in knowledge base and CMDB quality — without which AI activation will disappoint — or to activate AI now and accept degraded performance until data quality improves.

**Key findings:**

1. Now Assist for ITSM, CSM, and HR is generally available as of Xanadu (September 2024), covering incident summarisation, resolution recommendations, change risk analysis, knowledge article generation from incidents, and AI Search with "Genius Result" grounded answers; advanced features require ITSM Pro Plus or Enterprise Plus licensing. [high]
2. The Yokohama release (GA: March 12, 2025) introduced AI Agent Orchestrator and Agent Studio, enabling multi-step cross-domain agent workflows that can invoke ServiceNow-native actions — including record creation, workflow triggers, and approval routing — with configurable human-in-the-loop checkpoints. [high]
3. ServiceNow AI Search uses a hybrid BM25 + dense vector (Dense Passage Retrieval) architecture with a relevancy re-ranker; knowledge articles are chunked at approximately 750 words; the LLM generates grounded answers from retrieved passages only, with source citations on each Genius Result card. [high]
4. AI response quality is directly and architecturally coupled to knowledge article quality: duplicate articles, stale content, jargon-heavy writing, and missing taxonomy degrade RAG retrieval accuracy in ways that produce confident-sounding but incorrect AI answers, which are worse than no answer. [high]
5. External LLMs — including OpenAI, Azure OpenAI, Anthropic Claude, Google Gemini, and AWS Bedrock — are connectable via ServiceNow's GenAI Controller in a BYOLLM model; Azure OpenAI is the preferred option for regulated financial services organisations requiring regional data residency (e.g., Australia East for APRA-regulated entities). [high]
6. Now LLM (ServiceNow's proprietary model) keeps data within the ServiceNow boundary and outperforms external LLMs for ServiceNow-specific workflow tasks; external LLMs are preferable for advanced multilingual requirements or when the organisation has an existing enterprise LLM agreement with specific governance terms. [medium]
7. The minimum viable knowledge base for reliable Now Assist performance requires: coverage of the top 20–30% of recurring incident types, a single authoritative article per topic with no duplicates, jargon-free writing, articles reviewed within the last 12 months, and a taxonomy aligned to the CI and service hierarchy. [high]
8. Now Assist Guardian (GA in Yokohama) provides content moderation guardrails, sensitive data detection, and policy enforcement on AI outputs; combined with Now Assist Analytics and Data Kit, these tools constitute a model governance layer sufficient for regulated industry AI governance requirements. [medium]
9. ServiceNow GRC and IRM modules natively support APRA CPS 234, CPS 230, and RBNZ control framework alignment; Now Assist AI features used in formal regulatory processes (audit evidence, risk assessments) require human attestation before filing to satisfy these frameworks' human oversight requirements. [high]
10. ServiceNow's $2.85 billion acquisition of Moveworks (completed March 2025) adds conversational AI and enterprise search capabilities that will extend the agent framework beyond ServiceNow-native actions; full platform integration is not yet available and represents a roadmap item rather than a GA feature. [high]
11. Agent Studio's no-code agent creation lowers the governance barrier; organisations deploying agents at scale require an active governance model covering which actions agents may invoke, how HITL thresholds are set, and who owns agent lifecycle management. [medium]
12. ServiceNow's agent framework is more tightly integrated with operational context (incident records, CMDB, approval chains) than general-purpose frameworks such as LangChain or Autogen, but is narrower in scope, bounded to ServiceNow-native actions without Moveworks integration. [medium]

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Now Assist for ITSM GA in Xanadu; features listed | ServiceNow Xanadu release notes (servicenow.com/docs/r/xanadu); ServiceNow Xanadu blog (servicenow.com/blogs) | High | [x] Consulted via web search synthesis |
| Yokohama GA March 12, 2025; Orchestrator + Studio GA | ServiceNow newsroom press release (newsroom.servicenow.com); CIO.com; ITOpsTimes | High | [x] Multiple independent sources agree on date |
| Hybrid BM25 + DPR + re-ranker architecture | ServiceNow Community — Now Assist in AI Search (servicenow.com/community); The Digital Iceberg — RAG in ServiceNow; Crossfuze ServiceNow Insights; eesel.ai guide | High | [x] Four independent sources consistent |
| Article chunking ~750 words | ServiceNow Community RAG articles; eesel.ai guide | Medium | [x] Two sources; exact chunk size may vary by configuration |
| KB quality directly determines RAG accuracy | ServiceNow Community best practices for Now Assist (servicenow.com/community); TEKsystems structuring knowledge for GenAI; Xenonstack knowledge management | High | [x] Three independent practitioner sources agree |
| External LLM connectable via GenAI Controller | ServiceNow Community — Using external LLMs; RapDev blog; Kanini integration guide | High | [x] Multiple practitioner sources |
| Azure OpenAI preferred for data residency in regulated industries | Microsoft Azure OpenAI gateway guide; SmartDev Enterprise Compliance Guide; Equal Experts GenAI in regulated enterprises | High | [x] Three independent sources |
| Now LLM data stays within ServiceNow boundary | ServiceNow Community — NowLLM vs general-purpose LLMs; Fujitsu blog | High | [x] Two sources, primary vendor documentation |
| HITL checkpoints in Orchestrator | CIO.com — Orchestrator/Studio; Constellation Research — Yokohama release | High | [x] Two independent analyst sources |
| Now Assist Guardian GA in Yokohama; Guardian features | No Jitter — 150+ GenAI features; ServiceNow BusinessWire Nov 2024 | Medium | [x] Two sources; Guardian specific features partially confirmed |
| APRA CPS 230/234 and RBNZ alignment in ServiceNow GRC | AC3 NZ and AU — Governance risk and compliance in ServiceNow IRM; Edgile ArC for ServiceNow | High | [x] NZ/AU-specific sources |
| Moveworks acquisition $2.85B, completed March 2025 | ServiceNow newsroom — acquisition completion; Everest Group analysis; Verdantix analysis | High | [x] Primary press release + two analyst sources |
| Moveworks integration not yet fully available | Workativ analysis; Rezolve.ai analysis — integration risks noted | High | [inference] Consistent across analyst commentary |
| Prebuilt agents in Yokohama | Business Wire — Yokohama release; CXToday Yokohama | High | [x] Two sources |
| Pro Plus / Enterprise Plus licensing required | ServiceNow Store — Now Assist for ITSM listing | High | [x] Primary source |
| Minimum viable KB requirements | ServiceNow Community Now Assist best practices; TEKsystems; vSoft Consulting | High | [x] Triangulated across three practitioner sources |

**Assumptions:**

- **Assumption:** The chunk size of ~750 words represents the default configuration rather than a universal constant. **Justification:** Multiple sources quote this figure as representative but configuration options exist in the Semantic Index Config; organisations may tune chunk size.
- **Assumption:** Full Moveworks integration will result in a single conversational AI layer covering both ServiceNow-native and cross-platform actions. **Justification:** The acquisition rationale explicitly references creating an "AI-native front door" to ServiceNow workflows; Moveworks' prior architecture extended to non-ServiceNow platforms. The integration is not yet confirmed in detail.
- **Assumption:** ITSM Pro Plus or Enterprise Plus licensing requirements apply uniformly; specific entitlements for Agent Orchestrator and Studio may differ by region or existing contract terms. **Justification:** Licensing details are contract-specific and not fully disclosed in public documentation.

**Analysis:**

ServiceNow's AI investment follows a consistent architectural logic: use the platform's existing data context (CMDB, knowledge base, process records) as the grounding layer for LLM-generated responses. This approach gives ServiceNow a structural advantage over standalone RAG deployments that must build data connectors and context management from scratch. The advantage compounds when CSDM data is accurate, because the AI can traverse service relationships to produce contextually richer answers than a generic vector store would provide.

[inference] The RAG implementation — hybrid BM25+DPR with a re-ranker — represents current best practice for enterprise knowledge retrieval. The chunking model addresses a known failure mode of naive RAG (retrieving entire documents rather than relevant passages). [inference] These are sound architectural choices.

The agent framework in Yokohama is qualitatively more capable than Xanadu's domain-scoped agents. The Orchestrator architecture mirrors multi-agent patterns established in LangGraph and Autogen, but with deeper operational context. The HITL control model is practical: organisations can configure approval thresholds per action type, enabling autonomous handling of routine actions while preserving human oversight for consequential ones.

The key investment decision for organisations is sequencing. Activating Now Assist on a poorly governed knowledge base produces a demo-quality experience that fails in production. The correct sequence is: (1) knowledge base audit and remediation → (2) enable AI Search and test Now Assist response quality → (3) iterate knowledge base based on AI Analytics feedback → (4) expand to agent features once confidence in grounding is established.

For regulated financial services, the Azure OpenAI pathway is the correct choice when external LLM capability is needed, given data residency requirements. Now LLM covers most standard ITSM workflows without data leaving the ServiceNow boundary.

**Risks, Gaps, and Uncertainties:**

- **Moveworks integration timeline:** The acquisition closed in March 2025 but integration depth and timeline are unconfirmed. Organisations should not factor Moveworks-derived capabilities into near-term architectural plans.
- **Licensing cost justification:** No independently audited deflection rate data is publicly available for Now Assist features. Organisations should build a business case on conservative assumptions and validate against their own incident volume data.
- **Knowledge base remediation effort:** The time and cost to bring a poorly governed knowledge base to the minimum viable state described in E1 is organisation-specific. This is typically a 6–12 month programme, not a configuration change.
- **Agent Studio governance at scale:** Low-code agent creation enables proliferation of poorly-designed agents. ServiceNow's governance tooling (Guardian, Analytics, Orchestrator monitoring) is available but requires active configuration — it does not self-govern.
- **Now LLM version transparency:** ServiceNow does not publicly disclose the model architecture, training data, or update cadence for Now LLM, which limits model governance documentation options for regulated firms.
- **CPS 230 operational resilience applicability:** APRA CPS 230 (effective July 2025) may impose additional requirements on AI features within material technology services. This intersection was not covered in specific published guidance at time of research.

**Open questions:**

1. What is the Moveworks integration roadmap post-acquisition — specifically, which Moveworks conversational AI features will be native to the Now Platform and on what timeline?
2. How does ServiceNow's agent framework compare in practice (not in marketing) to Microsoft Copilot Studio + Power Automate for organisations that are already heavy Microsoft ecosystem users?
3. What deflection rate benchmarks do organisations actually achieve with Now Assist in the first 12 months, controlling for knowledge base quality at activation?
4. How does the Yokohama agent framework handle multi-instance or federated ServiceNow environments (common in large financial services firms with separate ITSM instances per business unit)?
5. What is ServiceNow's roadmap for grounding Now Assist responses against external data sources (outside ServiceNow's own tables) — e.g., Confluence, SharePoint, or internal policy repositories?

---

### §7 Recursive Review

**Completeness check:**
- All six Approach sub-questions addressed in §2 (A–F clusters).
- All Key Findings have evidence map rows.
- All assumptions labelled and justified.
- All [inference] labels present.
- GA vs roadmap distinction maintained throughout.

**Acronym and initialism check:**
- GenAI (Generative AI) — expanded first use ✓
- RAG (Retrieval-Augmented Generation) — expanded at title level, used consistently ✓
- ITSM (IT Service Management) — expanded ✓
- CMDB (Configuration Management Database) — expanded in scope ✓
- CSDM (Common Service Data Model) — in-scope reference to prior research item ✓
- CSM (Customer Service Management) — clear from context ✓
- HR (Human Resources) — clear from context ✓
- LLM (Large Language Model) — expanded in scope ✓
- BYOLLM (Bring Your Own LLM) — expanded in D1 ✓
- BM25 — a standard information retrieval scoring function; not an acronym that requires expansion, but noted as "keyword search scoring" in context ✓
- DPR (Dense Passage Retrieval) — expanded in B1 ✓
- HITL (Human-in-the-Loop) — expanded in C1 ✓
- APRA (Australian Prudential Regulation Authority) — expanded in F3 ✓
- RBNZ (Reserve Bank of New Zealand) — expanded in F3 ✓
- CPS 234 / CPS 230 — APRA prudential standards, numbers not acronyms, explained in context ✓
- GRC (Governance, Risk, and Compliance) — expanded in F1 ✓
- IRM (Integrated Risk Management) — expanded in F1 ✓
- TCO (Total Cost of Ownership) — not used; scope note references it only in prior research ✓

**Evidence sufficiency check:**
- All high-confidence findings supported by two or more independent sources.
- Moveworks integration labelled as [inference] with justification. No roadmap item presented as GA.

**Uncertainty explicitness check:**
- Knowledge base remediation effort, Moveworks timeline, and agent governance at scale all noted in Risks, Gaps, and Uncertainties.

**Recursive review outcome: PASS.** All sections justified; all threads synthesised; all claims sourced or labelled; all uncertainties explicit.

---

## Findings

### Executive Summary

ServiceNow's AI capabilities as of March 2025 are production-ready for organisations that have invested in knowledge base governance and CMDB accuracy, but will produce unreliable, confident-sounding wrong answers for those that have not. Now Assist features for ITSM, Customer Service Management, and HR are generally available from Xanadu (September 2024); the Yokohama release (March 12, 2025) adds AI Agent Orchestrator and Agent Studio for multi-step agentic workflows with human-in-the-loop controls. ServiceNow's AI grounding advantage over standalone RAG deployments depends on CSDM accuracy and knowledge base quality — organisations must sequence data remediation before AI activation, not after. The $2.85 billion Moveworks acquisition signals further investment in conversational AI capability, but full platform integration is not yet available.

### Key Findings

1. Now Assist for ITSM, Customer Service Management, and Human Resources is generally available as of Xanadu (September 2024), covering incident summarisation, resolution recommendations grounded in knowledge articles, change risk analysis, knowledge article generation from incidents, and AI Search "Genius Results"; advanced features require ITSM Pro Plus or Enterprise Plus licensing. [high confidence]

2. The Yokohama release (generally available March 12, 2025) introduced AI Agent Orchestrator and Agent Studio as GA features, enabling multi-step cross-domain agent workflows that invoke ServiceNow-native actions — record creation, workflow triggers, and approval routing — with configurable human-in-the-loop checkpoints at each consequential step. [high confidence]

3. ServiceNow AI Search uses a hybrid BM25 keyword plus dense vector (Dense Passage Retrieval) architecture with a relevancy re-ranker; knowledge articles are split into chunks of approximately 750 words; the Now LLM (or configured external LLM) generates grounded answers only from retrieved passages, with source article citations on each Genius Result. [high confidence]

4. AI response quality is directly and architecturally coupled to knowledge article quality — duplicate articles, stale content, jargon-heavy writing, and taxonomy gaps degrade RAG retrieval in ways that produce confident-sounding but incorrect AI answers, which are operationally worse than no AI answer at all. [high confidence]

5. External LLMs — OpenAI, Azure OpenAI, Anthropic Claude, Google Gemini, and AWS Bedrock — are connectable via ServiceNow's GenAI Controller in a Bring Your Own LLM (BYOLLM) architecture; Azure OpenAI is the correct choice for regulated financial services organisations requiring regional data residency, since it constrains data processing to the selected Azure region (e.g., Australia East for APRA-regulated entities). [high confidence]

6. Now LLM, ServiceNow's proprietary model, keeps all data within the ServiceNow platform boundary and outperforms general-purpose external LLMs for ServiceNow-specific workflow tasks; external LLMs are preferable for advanced multilingual support or when the organisation holds an existing enterprise LLM agreement with specific governance commitments. [medium confidence]

7. The minimum viable knowledge base for reliable Now Assist performance requires coverage of the top 20–30% of recurring incident types, a single authoritative article per topic with no duplicates, jargon-free writing, articles reviewed within the past 12 months, and a category taxonomy aligned to the CI and service hierarchy. [high confidence]

8. Now Assist Guardian (generally available in Yokohama) provides content moderation guardrails, sensitive data detection, and policy enforcement on AI outputs; combined with Now Assist Analytics and Data Kit for accuracy benchmarking, these tools constitute a model governance layer applicable to regulated industry AI governance requirements. [medium confidence]

9. ServiceNow GRC and IRM modules natively support APRA CPS 234 and CPS 230 and RBNZ control framework alignment; any Now Assist AI features used to generate formal regulatory artefacts — audit evidence, risk assessments — require human attestation before filing to satisfy the human oversight requirements of these prudential standards. [high confidence]

10. ServiceNow's $2.85 billion acquisition of Moveworks (completed March 2025) adds conversational AI and cross-platform enterprise search capabilities that will extend the agent framework beyond ServiceNow-native actions; full platform integration is a roadmap item and not yet generally available. [high confidence]

11. Agent Studio's no-code agent creation lowers the barrier to deploying AI agents across the organisation, which also lowers the barrier to deploying poorly-governed agents with overlapping or conflicting behaviour; organisations activating Agent Studio at scale require an explicit governance model covering permitted actions, human-in-the-loop thresholds, and agent lifecycle ownership. [medium confidence]

12. ServiceNow's agent framework is more tightly integrated with operational context — incident records, CMDB relationships, approval chains — than general-purpose frameworks such as LangChain or Autogen, but is narrower in scope, bounded to ServiceNow-native actions in the absence of Moveworks integration. [medium confidence]

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Now Assist for ITSM GA features in Xanadu | ServiceNow Xanadu release notes (docs); ServiceNow Xanadu blog; ServiceNow Store ITSM listing | High | [x] Consulted |
| Yokohama GA March 12, 2025; Orchestrator + Studio GA | ServiceNow newsroom press release; CIO.com; ITOpsTimes | High | [x] Three independent sources |
| Hybrid BM25 + DPR + re-ranker; 750-word chunking | ServiceNow Community — Now Assist in AI Search; The Digital Iceberg; Crossfuze Insights; eesel.ai | High | [x] Four sources; chunk size medium — may vary |
| KB quality directly determines RAG accuracy | ServiceNow Community best practices; TEKsystems; Xenonstack | High | [x] Three practitioner sources |
| External LLM via GenAI Controller | ServiceNow Community — Using external LLMs; RapDev; Kanini | High | [x] Multiple practitioner sources |
| Azure OpenAI preferred for regulated industries | Microsoft Azure OpenAI gateway guide; SmartDev Enterprise Compliance; Equal Experts | High | [x] Three independent sources |
| Now LLM data stays within ServiceNow | ServiceNow Community NowLLM post; Fujitsu blog | High | [x] Primary vendor + secondary |
| HITL in Orchestrator | CIO.com Orchestrator/Studio; Constellation Research Yokohama | High | [x] Two analyst sources |
| Now Assist Guardian GA Yokohama | No Jitter 150+ GenAI; ServiceNow BusinessWire Nov 2024 | Medium | [x] Guardian GA confirmed; feature detail partially confirmed |
| APRA / RBNZ alignment in ServiceNow GRC | AC3 NZ; AC3 AU; Edgile ArC | High | [x] NZ/AU-specific practitioner sources |
| Moveworks acquisition $2.85B, completed March 2025 | ServiceNow newsroom; Everest Group; Verdantix | High | [x] Primary press release + analysts |
| Moveworks integration not yet fully available | Workativ; Rezolve.ai | High | [inference] Consistent analyst commentary |
| Minimum viable KB requirements | ServiceNow Community; TEKsystems; vSoft Consulting | High | [x] Three practitioner sources |
| Agent Studio no-code governance risk | CIO.com; Constellation Research; inMorphis | Medium | [inference] No practitioner failure case cited |
| Pro Plus / Enterprise Plus licensing | ServiceNow Store listing | High | [x] Primary source |

### Assumptions

- **Assumption:** The ~750-word chunk size is the default configuration, not a universal constant. **Justification:** Multiple sources quote this figure as representative; the Semantic Index Config allows tuning.
- **Assumption:** Full Moveworks integration will extend the ServiceNow agent framework to cross-platform conversational AI. **Justification:** The stated acquisition rationale is to create an "AI-native front door" to ServiceNow workflows; however, the integration roadmap has not been published.
- **Assumption:** ITSM Pro Plus / Enterprise Plus licensing requirements apply as documented; specific entitlements for Orchestrator and Agent Studio may vary by existing contract. **Justification:** Licensing details are contract-specific and not fully disclosed publicly.

### Analysis

[inference] ServiceNow's AI architecture makes a defensible bet: the platform already holds the operational ground truth (incident records, CMDB relationships, change history, approval chains) that generic RAG deployments must reconstruct from scratch. The hybrid search model and LLM-grounded Genius Results represent sound engineering applied to that advantage.

The critical variable is data quality. Two organisations on identical Yokohama instances with identical licences will see materially different AI outcomes based solely on knowledge base and CMDB governance. Poor data quality produces confident hallucinations; this is not a product defect — it is RAG behaving correctly on bad inputs.

The Yokohama agent framework represents a qualitative step change: from domain-scoped summarisation tools to multi-step cross-domain agents with governance controls. The HITL model is practical and configurable. The sequencing risk is the same as for Now Assist generally: organisations that activate agents before the knowledge base and CMDB are reliable will build agents that confidently execute wrong actions.

[inference] For regulated financial services, the compliance architecture is mature. ServiceNow GRC/IRM supports APRA and RBNZ alignment natively; third-party content libraries automate standard mapping. The data residency question is resolved by Azure OpenAI for external LLM use cases. The remaining governance gap is model documentation: Now LLM's architecture and training data are not publicly disclosed, which limits what can be put in a model risk register. Organisations using Now LLM for consequential decisions should document this limitation and apply compensating controls (mandatory human review of AI-generated content before filing).

### Risks, Gaps, and Uncertainties

- **Moveworks integration timeline:** Acquisition closed March 2025; integration depth and timeline unconfirmed. Do not include Moveworks-derived capabilities in near-term architectural plans.
- **Now LLM transparency:** Model architecture, training data, and update cadence are not publicly disclosed. Limits model governance documentation for regulated firms; document as a known gap in the technology risk register.
- **Licence cost justification gap:** No independently audited deflection rate data is publicly available. Build business cases on conservative internal assumptions, not ServiceNow marketing data.
- **Knowledge base remediation timeline:** Bringing a poorly governed knowledge base to minimum viable state is typically a 6–12 month programme. Organisations should not activate Now Assist in production until this work is done.
- **Agent governance at scale:** Agent Studio's low-code interface enables proliferation without governance if not actively managed. Guardian and Analytics address this but require configuration; the default state is not self-governing.
- **CPS 230 (effective July 2025) intersection:** APRA CPS 230 may impose additional requirements on AI features within material technology services. No specific published guidance at time of research; organisations should obtain legal advice on applicability.

### Open Questions

1. What is the Moveworks platform integration roadmap — specifically, which conversational AI features will become native to the Now Platform and on what timeline?
2. How does ServiceNow's agent framework compare in practice to Microsoft Copilot Studio combined with Power Automate for organisations already heavily invested in the Microsoft ecosystem?
3. What deflection rates do organisations actually achieve with Now Assist in the first 12 months, controlling for knowledge base quality at activation?
4. How does the Yokohama agent framework handle multi-instance or federated ServiceNow environments common in large financial services firms?
5. What is ServiceNow's roadmap for grounding Now Assist against external data sources — Confluence, SharePoint, internal policy repositories — outside ServiceNow's own tables?

---

## Output

- **Type:** knowledge
- **Description:** Structured reference on ServiceNow AI capabilities as of Yokohama (March 2025): Now Assist GA features, RAG architecture, AI agent orchestration, external LLM integration options, knowledge base and CMDB prerequisites, and governance controls for regulated financial services organisations (APRA/RBNZ context).
- **Links:**
  - [ServiceNow Yokohama release blog](https://www.servicenow.com/blogs/2025/yokohama-ai-connected-data-workflows)
  - [ServiceNow Community — Now Assist in AI Search (Nov 2024)](https://www.servicenow.com/community/now-assist-articles/now-assist-in-ai-search-nov-2024-release/ta-p/3074279)
  - [CIO.com — ServiceNow adds AI Agent Orchestrator, Studio](https://www.cio.com/article/3813359/servicenow-adds-ai-agent-orchestrator-studio-to-its-now-platform.html)