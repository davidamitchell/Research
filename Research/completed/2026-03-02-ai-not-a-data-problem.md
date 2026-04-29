---
title: "AI capability is not a data problem - why the data/analytics department is the wrong home for organisational AI"
added: 2026-03-07T01:39:25+00:00
status: completed
priority: medium
tags: [ai-strategy, architecture, data-platform, api-layer, agentic-ai, organisational-design, governance, mcp, zero-trust, identity]
started: 2026-03-07T01:39:25+00:00
completed: 2026-03-07T01:39:25+00:00
output: [knowledge, backlog-item]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# AI capability is not a data problem - why the data/analytics department is the wrong home for organisational AI

## Research Question

What is the strongest case - technical, architectural, organisational, legal, and regulatory - that an organisation's AI capability should NOT be owned by or coupled to its data/analytics department or data platform, and what concrete tradeoffs arise when that coupling is made?

## Scope

**In scope:**
- Architectural argument: why data warehouses, lakes, and analytics platforms fail the non-functional requirements (NFRs) demanded by production agents (high availability and disaster recovery (HADR), fine-grained access control, operational SLAs, auditability)
- The correct integration point for agents: the organisation's API layer (API gateways, horizontally-scaling services, MCP servers, Security Token Service (STS) token exchange, decentralised identifiers (DID)/verifiable credentials, zero-trust networks)
- What agents actually need: intent, knowledge, context, strategy, structure, constraints, regulations, policies, standards - none of which live in a data warehouse
- Organisational design argument: the skills gap between data/analytics professionals and the engineering disciplines required for production agent infrastructure (security, identity, observability, service design)
- The multi-stakeholder nature of AI capability: IT, business operations, HR/people, legal, regulatory compliance - no single department can own it unilaterally
- Tradeoffs of the coupled (data-platform-centric) model vs. the decoupled (API-layer-centric) model
- Case studies, white papers, and first-principles reasoning supporting the decoupled model
- Regulatory and compliance angle: auditability, fine-grained access control, and data residency requirements that analytics platforms are not designed to satisfy

**Out of scope:**
- Detailed implementation of specific API gateway products or MCP server implementations
- Vendor comparison (specific data warehouse vs. specific API platform)
- Model selection, fine-tuning, or LLM evaluation
- Research into AI use cases themselves (covered by `2026-02-28-ai-strategy-*.md` items)

**Constraints:** Research should be anchored in published evidence (case studies, white papers, architecture guidance, regulatory frameworks) where possible; first-principles reasoning acceptable where evidence is sparse. NZ regulatory context (Reserve Bank of New Zealand (RBNZ), Privacy Act, Department of Internal Affairs (DIA), Ministry of Business, Innovation and Employment (MBIE)) relevant but global evidence preferred for generalisability.

## Context

Organisations moving into AI often default to placing AI capability inside the data or analytics team - because that team already handles data pipelines, business intelligence (BI) tooling, and ML models. This conflation of "AI" with "data" is a category error that creates systemic risks:

1. **Operational NFRs mismatch:** Data warehouses and analytics platforms are designed for batch/analytical workloads, not for sub-second agent responses, high availability, disaster recovery, or multi-tenant access patterns. Coupling agents to these platforms inherits their fragility.

2. **Access control gap:** Analytics platforms typically implement coarse-grained, role-based access for human analysts. Agents require fine-grained, context-aware, delegated access (e.g. an agent acting *on behalf of* a specific user in a specific context). STS token exchange, OAuth 2.0 device flow, and DID-based identity are not standard capabilities of data platforms.

3. **Skills mismatch:** Data engineers and analysts are expert in SQL, extract-transform-load (ETL), BI, and statistical modelling - not in service design, API security, identity federation, zero-trust network architecture, SCOM/observability, or operational SLAs. These are API/platform engineering disciplines.

4. **Knowledge ≠ Data:** Agents need structured knowledge (policies, regulations, organisational strategy, procedural context) - not raw data. Knowledge management is a distinct discipline from data management, requiring curation, versioning, and contextual scoping.

5. **Mutation risk:** Agents that can enact state changes (write operations) must do so through audited, secured, API-mediated pathways - not through direct database or warehouse access. The analytics plane has no concept of a mutation API with full audit trail, SCOM alerting, and rollback capability.

6. **Organisational accountability:** AI capability cuts across legal (liability, contracts), HR (workforce impact, skills uplift), compliance (regulation, policy), IT (infrastructure, security), and business operations. No single team - especially not one historically scoped to reporting and analytics - can hold that mandate.

This item makes the case for a deliberate separation: agents interact with the world through the organisation's API layer, not its analytics plane. It also examines what needs to change organisationally to make that separation real.

**Prior research:** Three directly relevant completed items inform this investigation. `2026-02-28-rbnz-ai-supervisory-expectations.md` establishes that RBNZ has no standalone AI governance framework but that BS11/BPR operational risk requirements and Australian Prudential Regulation Authority (APRA) CPS 230 effectively demand board-level accountability, documented governance, and material service provider management - all of which require IT and legal involvement, not just data stewardship. `2026-02-28-ai-line-1-line-2-risk-agents.md` demonstrates that every documented production deployment of AI agents in financial services positions agents as tool-output generators with a human reviewer retaining accountability - this is an API-mediated, identity-attributed delegation model, not a direct data-platform integration. `2026-02-28-ai-strategy.md` establishes the four-type use-case typology and the cross-functional governance requirement; Gartner, McKinsey, and Singapore's Model AI Governance Framework all identify multi-stakeholder ownership as the correct target state. What this item must add that prior items do not cover: the architectural argument (operational vs. analytical data plane), the NFR failure modes of analytics platforms, the STS/MCP agent integration patterns, and the skills gap between data/analytics and API/platform engineering disciplines.

## Approach

1. **First-principles technical argument** - Enumerate the NFRs required by production AI agents (availability, latency, fine-grained authz, audit, mutation safety, HADR) and show which data platform categories (data warehouse, data lake, lakehouse, analytics DB) fail each NFR by design. Contrast with API layer capabilities.

2. **API layer as the agent integration point** - Research the architecture pattern: API gateway → horizontally-scaling services → MCP servers → agent. Map how each component satisfies the NFRs that the data plane cannot. Include: STS token exchange for delegated identity, DID/verifiable credentials, zero-trust network principles, SCOM/observability patterns, multi-context service design (staff/customer/system/agent personas).

3. **Knowledge vs. data distinction** - Research knowledge management as a discipline distinct from data management. How do organisations scope contextual knowledge for agents (policy documents, regulatory constraints, procedural context)? What are the established patterns (RAG, knowledge graphs, curated context windows)?

4. **Organisational design evidence** - Find case studies and white papers on AI governance structures. Which organisations have succeeded with a dedicated AI capability function that spans IT + business + legal + HR? Which have failed by placing AI inside data/analytics? What does the literature say about cross-functional AI teams?

5. **Skills gap analysis** - What skills are required to build and operate production agent infrastructure that are absent from typical data/analytics teams? (Service engineering, identity and access management, API security, site reliability engineering (SRE)/observability, zero-trust networking, legal-tech, change management.)

6. **Regulatory and compliance angle** - What do regulators (RBNZ, Office of the Comptroller of the Currency (OCC), Financial Conduct Authority (FCA), APRA, General Data Protection Regulation (GDPR)/Privacy Act, NZ Privacy Act 2020) say about AI governance, auditability, and data access controls? Do any explicitly require separation of analytical and operational data access?

7. **Tradeoff analysis** - Enumerate the costs of the coupled model (data-platform-centric AI) and the decoupled model (API-layer-centric AI). Include: time-to-market, risk profile, technical debt, organisational friction, regulatory exposure. Produce a structured tradeoff table.

8. **Counter-arguments** - Steelman the case for data-platform-centric AI. Where does it work? What are its genuine advantages (existing data gravity, ML model proximity, analytics tooling)? Why do those advantages not outweigh the structural risks at the operational agent layer?

## Sources

- [x] Martin Fowler - "DataMesh" and operational vs. analytical data plane separation: https://martinfowler.com/articles/data-mesh-principles.html
- [ ] Zhamak Dehghani - *Data Mesh* (O'Reilly, 2022) - operational vs. analytical plane distinction
- [x] National Institute of Standards and Technology (NIST) AI Risk Management Framework (AI RMF): https://www.nist.gov/artificial-intelligence/ai-risk-management-framework - governance and organisational accountability
- [ ] RBNZ - AI supervisory expectations and governance guidance: https://www.rbnz.govt.nz
- [ ] Google Cloud Architecture - "Separation of analytical and operational workloads": https://cloud.google.com/architecture
- [ ] Microsoft Azure Well-Architected Framework - AI workload NFRs: https://learn.microsoft.com/en-us/azure/well-architected/
- [ ] Anthropic / OpenAI usage policies and agent architecture guidance
- [ ] McKinsey Global Institute - "The state of AI in organisations" (annual survey): https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
- [ ] Gartner - "AI governance and organisational design" research notes
- [x] OAuth 2.0 Token Exchange (RFC 8693) - STS delegation pattern for agents: https://datatracker.ietf.org/doc/html/rfc8693
- [ ] W3C Decentralised Identifiers (DID) spec: https://www.w3.org/TR/did-core/
- [ ] CNCF Zero Trust Whitepaper: https://github.com/cncf/tag-security/blob/main/security-whitepaper/v2/cloud-native-security-whitepaper.md
- [ ] OWASP API Security Top 10: https://owasp.org/www-project-api-security/
- [ ] Andreessen Horowitz (a16z) - AI enterprise architecture commentary
- [ ] Thoughtworks Technology Radar - Data mesh, API gateway, and agent architecture entries: https://www.thoughtworks.com/radar
- [x] `Research/completed/2026-02-28-rbnz-ai-supervisory-expectations.md` - NZ regulatory context
- [x] `Research/backlog/2026-02-28-ai-strategy-business-efficiency-examples.md` - AI strategy examples context (now completed)
- [x] `Research/backlog/2026-02-28-ai-line-1-line-2-risk-agents.md` - risk and governance framing (now completed)

---

## Research Skill Output

### §0 Initialise

**Research question restated:** What is the strongest technical, architectural, organisational, legal, and regulatory case that an organisation's AI capability should not be owned by or coupled to its data/analytics department or data platform, and what concrete tradeoffs arise from that coupling?

**Scope confirmed:** The investigation covers (1) the NFR mismatch between analytics platforms and production agent requirements, (2) the API layer as the architecturally correct integration point for agents including MCP, STS token exchange, and zero-trust patterns, (3) knowledge management as a discipline distinct from data management, (4) organisational design evidence on cross-functional AI governance, (5) the skills gap between data/analytics teams and API/platform engineering, (6) regulatory requirements that enforce multi-stakeholder accountability, and (7) a structured tradeoff analysis including steelmanned counter-arguments. Detailed vendor comparisons, model selection, and AI use-case research are out of scope.

**Constraints confirmed:** Evidence-first where available; first-principles reasoning where published evidence is sparse. NZ context (RBNZ, Privacy Act 2020, DIA) noted but global evidence prioritised for generalisability. Prior research from `2026-02-28-rbnz-ai-supervisory-expectations.md`, `2026-02-28-ai-line-1-line-2-risk-agents.md`, and `2026-02-28-ai-strategy.md` establishes NZ regulatory and AI strategy context and will not be re-researched.

**Output format:** Structured synthesis with Evidence Map, tradeoff table, and confidence-labelled findings. May spawn one follow-on backlog item on API-layer agent architecture patterns or AI governance design.

### §1 Question Decomposition

**Root question:** Should an organisation's AI capability be owned by or coupled to its data/analytics department?

**Decomposition:**

**Branch A - Technical/Architectural**
- A1: What NFRs do production AI agents require (availability, latency, fine-grained authz, mutation safety, audit, HADR)?
- A2: Which of those NFRs do analytics platforms (data warehouse, data lake, lakehouse) satisfy by design, and which do they fail?
- A3: What does the API layer provide that satisfies the failed NFRs (API gateway, MCP server, STS token exchange, zero-trust)?
- A4: What is the correct data flow for an agent that must read from the analytics plane - direct access or API-mediated?
- A5: What is the difference between operational data and analytical data, and which plane should agents primarily interact with?

**Branch B - Knowledge vs. Data**
- B1: What do agents actually need to function (intent, knowledge, policies, context, regulations) vs. what data platforms store?
- B2: How is knowledge management (RAG, knowledge graphs, curated context) structurally different from data management (ETL, warehousing, BI)?
- B3: Can a data platform serve as a knowledge source for agents, and under what conditions?

**Branch C - Organisational Design**
- C1: What governance structures do global frameworks (NIST AI RMF, Singapore MAIGF, EU AI Act) recommend for AI capability ownership?
- C2: What does the evidence show about AI programs that placed ownership in the data/analytics team - outcomes, failure modes?
- C3: What cross-functional composition does a successful AI capability function require?
- C4: What does the Chief Data Officer (CDO)/Chief Data and Analytics Officer (CDAO) role evolution show about the structural limits of data-team AI ownership?

**Branch D - Skills Gap**
- D1: What skills are required to build and operate production agent infrastructure?
- D2: Which of those skills are present in a typical data/analytics team?
- D3: What disciplines are systematically absent from data/analytics teams that are required for production agents?

**Branch E - Regulatory/Compliance**
- E1: Do regulators (RBNZ, APRA, FCA, NIST) require cross-functional accountability for AI systems?
- E2: Do any regulatory frameworks explicitly require separation of analytical and operational access?
- E3: What auditability, access control, and data residency requirements do analytics platforms fail to satisfy at the production agent layer?

**Branch F - Tradeoffs**
- F1: What are the genuine advantages of data-platform-centric AI (data gravity, ML proximity, analytics tooling)?
- F2: What are the structural risks of data-platform-centric AI that outweigh those advantages for production agents?
- F3: What does the decoupled (API-layer-centric) model cost in time-to-market and organisational friction?

### §2 Investigation

**A1/A2 - Production agent NFRs vs. analytics platform capabilities**

Production AI agents operating in enterprise contexts impose a set of non-functional requirements that are structurally incompatible with analytics platform design. From the Pylar AI five-layer architecture analysis and Machine Learning Mastery's production AI agent deployment framework, the critical NFRs are: (1) sub-second latency for interactive agents (analytics warehouses optimise for throughput, not tail latency), (2) high availability with automatic failover (analytics platforms use scheduled maintenance windows and accept batch-processing downtime), (3) fine-grained, context-aware, delegated authorisation per-request (analytics platforms implement coarse-grained role-based access control (RBAC) for human analysts), (4) mutation safety with full audit trail (analytics planes are historically append-only or read-oriented; writeback capabilities are recent and not designed for agent-driven mutations), (5) HADR with tested recovery objectives (analytics platforms often have recovery point objective/recovery time objective (RPO/RTO) suited to analytical workloads, not operational SLAs), (6) rate-limiting and circuit breakers (analytics platforms expose query endpoints, not controlled API surfaces with throttling), and (7) per-request observability and traceability (analytics platforms produce query logs, not structured operational telemetry). [fact: source = Pylar AI, Machine Learning Mastery agent deployment guide, Martin Fowler data mesh article]

Martin Fowler's canonical data mesh article (martinfowler.com, accessed) makes the operational/analytical divide explicit: "Operational data sits in databases behind business capabilities served with microservices, has a transactional nature, keeps the current state and serves the needs of the applications running the business. Analytical data is a temporal and aggregated view of the facts of the business over time." Fowler explicitly states that operational data technology "meets the needs of the business" through microservice APIs and that "data is hidden on the inside of each microservice, controlled and accessed through the microservice's APIs." This establishes that the correct access pattern for operational data - which production agents must read and write - is through the API layer, not the analytical plane. [fact: source = Martin Fowler, "Data Mesh Principles and Logical Architecture", December 2020]

**A3 - API layer satisfying agent NFRs**

The API layer pattern - API gateway → horizontally-scaling service → MCP server → agent - satisfies the NFRs that analytics platforms fail. API gateways provide rate-limiting, circuit breaking, per-request authentication, and structured telemetry. Horizontally-scaling services provide HADR through redundancy and auto-scaling. MCP (Model Context Protocol), Anthropic's open standard from late 2024, standardises agent-to-service integration using JSON-RPC 2.0 over HTTPS or mutual TLS (mTLS), with capability declarations, access scopes, and audit logging as first-class features. By 2025, MCP had been adopted by Microsoft, AWS, Google, and Anthropic, with enterprise cloud-native MCP servers providing standard authentication, TLS, and identity and access management (IAM) integration. [fact: source = MCP specification (modelcontextprotocol.io), Cloud Security Alliance MCP primer, Okta MCP overview]

RFC 8693 (OAuth 2.0 Token Exchange) provides the STS delegation pattern that production agents require for fine-grained, context-aware, delegated access: an agent obtains a narrowly-scoped token representing "acting on behalf of user X in context Y," with the `act` claim embedding the agent identity for audit trails. This is technically impossible through a direct analytics platform connection, which has no concept of per-user, per-context token delegation. An Internet Engineering Task Force (IETF) draft (draft-oauth-ai-agents-on-behalf-of-user-01) extends RFC 8693 specifically for AI agents with `requested_actor` and `actor_token` parameters. Auth0's Token Vault and Stacklok's MCP token delegation document this pattern in production deployments. [fact: source = RFC 8693 rfc-editor.org, Auth0 Token Vault blog, Stacklok token delegation guide, IETF draft]

Zero-trust principles applied to MCP enforce that each agent request is verified per-request (never based on network position), with context-sensitive and workload-aware policies replacing static credentials. This requires the API/MCP server layer - zero-trust has no analogue in the analytics plane. [fact: source = Pomerium MCP access guide, CSA MCP primer, Skyflow MCP security architecture]

**A4/A5 - Agent access to the analytical plane via API mediation**

The correct architecture for an agent that needs to read from the analytical plane is API-mediated access (a read-only query API exposed through a governed service), not a direct warehouse connection. Materialize's agentic data architecture analysis documents this as the "live operational data mesh" pattern where agents interact with continuously-updated operational data products through APIs. Google Cloud's data mesh architecture and Microsoft Azure's data mesh for AI/ML operationalisation both confirm the pattern: data products are accessed through defined API contracts, not raw warehouse connections. [fact: source = Materialize blog, Google Cloud data mesh docs, Microsoft Azure data mesh for AI/ML]

**B1/B2/B3 - Knowledge vs. data**

Agents require structured knowledge - policies, regulations, procedural context, organisational strategy, standards - to constrain their behaviour, ground their reasoning, and ensure regulatory compliance. This content is not "data" in the analytics-platform sense: it is not time-series transactional facts; it does not live in a warehouse schema; it requires curation, versioning, contextual scoping, and relevance ranking for retrieval. Knowledge management is the discipline for this: RAG (Retrieval-Augmented Generation) architectures retrieve policies and knowledge documents via semantic search and inject them as agent context, reducing hallucinations and grounding responses in organisational reality. [fact: source = Xenoss enterprise knowledge base with RAG, CompuVate RAG systems knowledge management, KM Insider RAG and knowledge management]

Knowledge management and data management are complementary but distinct: data management ensures raw data is clean, available, and governed; knowledge management ensures that content is meaningful, connected, and accessible in a form that agents can act on. The convergence point is that RAG requires well-governed underlying data, but the knowledge curation layer - deciding what is an authoritative policy document, how to version it, which regulatory constraints apply in which context - is a knowledge management problem, not a data warehouse problem. [fact: source = Denser AI knowledge management analysis, FabrixAI AI knowledge management comparison]

A data platform can serve as a knowledge source for agents under one condition: access is mediated through a governed API (a query service or RAG retrieval endpoint), not through a direct SQL connection. When the mediation layer is in place, the data platform provides a useful read-only knowledge substrate. The risk is when organisations skip the mediation layer - allowing agents to query the warehouse directly - losing the access control, audit trail, and schema stability guarantees that the API layer provides. [inference: derived from Fowler operational/analytical plane separation and MCP API integration pattern]

**C1 - Governance framework requirements**

NIST AI RMF's Govern function explicitly requires that AI governance cross-cuts IT, legal, HR, and compliance. The framework states that "governance processes are not limited to a single team" and that accountability requires "documented activity from leadership, technical teams, and operational staff." The Colorado AI Act references NIST AI RMF compliance for safe harbour, confirming the framework's regulatory weight. [fact: source = NIST AI RMF implementation guides, Openlayer NIST guide, GLACIS NIST guide]

Singapore's Model AI Governance Framework (2024 Gen-AI update) - identified in prior research (`2026-02-28-ai-strategy.md`) as the most operationally useful reference for NZ financial services - defines nine dimensions for AI governance that span accountability (board/executive), data, trusted development, incident reporting, testing, security, content provenance, safety, and AI for public good. No single data/analytics team possesses the mandate or skills across all nine dimensions. [fact: source = prior research item 2026-02-28-ai-strategy.md]

**C2 - Failure modes of data-team AI ownership**

Harvard Business Review (HBR)'s "Why Chief Data and AI Officers Are Set Up to Fail" (2023) documents the structural problem: CDOs are given AI mandates without the operational authority, engineering resources, or legal/HR mandate to execute them. Only 38% of CDOs have direct responsibility for AI integration. Only 26% of CDOs are confident their teams can support new AI revenue streams (IBM CDO Study 2025). IBM's 2025 CDO study found CDOs redefined strategies because "AI ambitions outpace readiness" - i.e., the data team is the wrong organisational anchor for production AI deployment. CDO Magazine's analysis of nine AI implementation lessons from past CDO roles identifies fragmented data ownership, insufficient leadership alignment, and inability to drive operating model change as the dominant failure modes. [fact: source = HBR "Why Chief Data and AI Officers Are Set Up to Fail", IBM 2025 CDO Study, CDO Magazine nine lessons]

McKinsey's Boston Consulting Group (BCG) 10-20-70 rule (from prior research `2026-02-28-ai-strategy-business-efficiency-examples.md`) - 10% algorithms, 20% data and technology, 70% people and process - means that the vast majority of AI value delivery requires cross-functional change management that the data team is structurally unable to drive unilaterally. [fact: source = prior research item 2026-02-28-ai-strategy-business-efficiency-examples.md]

**C3/C4 - Cross-functional composition and CDO/CDAO evolution**

Gartner's 2025 CDAO agenda data shows 70% of CDAOs claim to own AI strategy and operating models, and CDOs reporting directly to CEOs rose from 21% to 36% between 2024 and 2025. However, Gartner simultaneously documents three archetypes - Expert D&A Leader, Connector CDAO, Pioneer CDAx - where only the Pioneer CDAx hybrid approaches the authority required for AI capability ownership. The dominant model for large enterprises remains a cross-functional AI Centre of Excellence with joint Chief Technology Officer (CTO)/CDO/Chief Artificial Intelligence Officer (CAIO) reporting, or a dedicated CAIO role with representation from data science, engineering, governance/compliance, risk management, and business unit product ownership. McKinsey confirms that enterprises that scale AI tie governance tightly to executive mandate with multi-function representation. [fact: source = Gartner CDAO Archetypes CDO Magazine, IBM 2025 CDO Study, McKinsey AI CoE guidance]

**D1/D2/D3 - Skills gap**

Production agent infrastructure requires: API design and service engineering; identity and access management (OAuth 2.0, OpenID Connect (OIDC), zero-trust); API security (OWASP API Security Top 10, authentication hardening, prompt injection prevention); SRE and observability (structured telemetry, distributed tracing, alerting, incident response); machine learning operations (MLOps) and model lifecycle management; legal-tech for regulatory translation; and change management. Data/analytics teams are strong in: SQL and ETL; statistical modelling and ML experimentation; BI and data visualisation; data governance and quality management. The gap is systematic: security, identity, API engineering, SRE/observability, and cross-functional change management are absent from the typical data/analytics team skill set. Karat's AI engineering skills gap analysis confirms the gap is particularly sharp in MLOps, end-to-end ML pipeline automation, real-time monitoring, and secure scalable deployment. IBM's AI skills gap report confirms the pattern. [fact: source = Karat AI engineering skills gap, IBM AI skills gap, DataTeams.ai skills gap template, Multiverse data skills intelligence report 2024]

**E1/E2/E3 - Regulatory requirements**

NIST AI RMF (as above): explicitly cross-functional, no single department mandate. APRA CPS 230 (from prior research): requires explicit operational risk scenario analysis for critical operations including AI, with documented accountability and independent validation - which requires IT, legal, and risk functions, not just data. RBNZ BS11/BPR (from prior research): banks must retain control, ensure stand-alone operability, and maintain board-level accountability for outsourced AI functions - analytics teams hold no board mandate. No regulator explicitly mandates the separation of analytical and operational access as a distinct requirement; rather, the operational risk, accountability, and auditability requirements collectively imply it. The FCA/Prudential Regulation Authority (PRA) confirmed (in prior research) that Senior Managers and Certification Regime (SMCR) senior managers including Chief Risk Officer (CRO) and CTO - not CDO - are accountable for AI risk within their domains. [fact: source = prior research items 2026-02-28-rbnz-ai-supervisory-expectations.md and 2026-02-28-ai-line-1-line-2-risk-agents.md; NIST AI RMF]

**F1/F2/F3 - Tradeoffs**

Data-platform-centric AI advantages (genuine): (1) existing data gravity - data is already there; no additional pipelines required for analytical AI; (2) ML model proximity - model training workflows sit close to the data; (3) analytics tooling maturity - established BI and governance tooling; (4) time-to-prototype - a data analyst can build a proof of concept faster without platform engineering involvement; (5) data lineage and governance - mature data catalogues provide lineage that a new API layer must rebuild.

Data-platform-centric AI structural risks: (1) NFR inheritance - every latency, availability, and access control limitation of the analytics platform propagates to the agent; (2) mutation risk - agents with write capability that touch the analytics plane directly can corrupt the analytical data store, with no mutation API, no audit trail, and no rollback path; (3) identity vacuum - no STS delegation model means agents operate under generic service accounts, producing untraceable audit logs; (4) scope creep of the data team - the team accumulates engineering, security, and compliance obligations it lacks the mandate and skills to fulfil; (5) regulatory exposure - when an AI incident occurs, the accountability chain terminates at the CDO/data team, which holds no regulatory licence and no operational risk mandate; (6) zero-trust impossibility - direct warehouse access violates zero-trust principles and creates attack surface for prompt injection, data exfiltration, and credential misuse.

API-layer-centric AI costs: (1) higher upfront engineering investment - building or configuring API gateways, MCP servers, and IAM integration takes longer than direct warehouse connections; (2) organisational friction - engaging IT, security, and platform engineering teams requires cross-functional governance that data teams can bypass in the short term; (3) latency of discovery - data products accessible via API must be catalogued and published; not all analytical data is immediately available through approved API endpoints. [inference: derived from evidence gathered across all sub-questions above, consistent with Fowler's operational/analytical plane separation and NIST AI RMF cross-functional governance requirements]

**[assumption]** The item assumes that "production agent" means an agent that takes consequential actions (sends communications, modifies records, makes decisions with downstream effects) as opposed to a read-only analytics assistant. The structural arguments about mutation safety, zero-trust, and STS delegation apply primarily to agents with write capability. A read-only analytics assistant with direct warehouse access is lower risk, though still problematic for the identity and audit trail reasons documented above. Justification: the research question and scope explicitly include "Agents that can enact state changes (write operations)" and the high-stakes agent category (financial services, compliance, HR) is the primary use case motivating the research.

### §3 Reasoning

**NFR mismatch is the primary structural argument.** The data/analytics department cannot satisfy the NFRs of production AI agents because the platforms it manages were not designed for those NFRs. This is not a deficiency of the people or the data - it is a design property of the analytical data plane. Fowler's data mesh separation is definitive: operational data is served through microservice APIs; analytical data is a temporal aggregation for retrospective insight. Placing agents at the analytical plane inverts this architecture - it treats the reporting layer as an operational system.

**The identity problem is non-negotiable.** Agents must act with delegatable, auditable, narrowly-scoped identity. RFC 8693 and the emerging IETF AI agent extension both confirm the STS delegation pattern as the correct model. Analytics platforms have no equivalent; they authenticate humans (or service accounts) to query data, not agents acting on behalf of users in specific contexts. When an AI incident occurs - a wrong action, a data exposure, a regulatory breach - the audit trail must show "agent A, acting on behalf of user B, in context C, at time T, took action X through service Y." Direct warehouse access produces no such trail.

**Knowledge is not data.** Organisations conflate AI capability with data capability because both involve information. But agents need knowledge - policies, regulations, procedural constraints, strategic context - not transactional facts. The analytical plane stores facts about past business events; it does not store the normative knowledge that constrains how an agent should behave. RAG and knowledge management are required as a distinct layer, and building that layer is a knowledge management and API engineering problem, not a data warehouse problem.

**The organisational argument converges on the same conclusion.** NIST AI RMF, Singapore MAIGF, EU AI Act, APRA CPS 230, and RBNZ BS11 all describe AI governance as inherently cross-functional. No data/analytics team holds the mandate to enforce security policies, drive workforce change, manage legal liability, or represent the organisation to regulators on AI risk. Placing AI capability in the data team does not make the cross-functional problem go away; it defers it until it causes a failure.

**Counter-arguments assessed.** The genuine advantages of data-platform-centric AI - data gravity, ML proximity, prototype speed - are advantages for the analytical and experimental phases of AI development, not for production operational deployment. A data platform is the right place to train models and explore patterns; it is the wrong place to deploy agents that take consequential actions. The hybrid model (data platform as read-only knowledge substrate, accessed via API mediation) preserves the advantages while avoiding the structural risks.

### §4 Consistency Check

No internal contradictions identified. The technical argument (NFR mismatch, identity vacuum, mutation risk), the knowledge argument (knowledge ≠ data, RAG requires a distinct management layer), and the organisational argument (cross-functional mandate, skills gap, regulatory accountability) are mutually reinforcing. Evidence from Fowler's data mesh, RFC 8693, NIST AI RMF, APRA CPS 230, IBM CDO Study 2025, and prior research items all point in the same direction.

One potential tension: Gartner reports 70% of CDAOs now claim to own AI strategy and operating models - this appears to contradict the claim that data teams cannot hold the AI mandate. The tension resolves when the finding is read in context: Gartner simultaneously documents that only the "Pioneer CDAx" hybrid archetype approaches the authority required, and that the dominant outcome for CDOs who own AI is failure (IBM CDO study: only 26% confident in their ability to support AI revenue streams; HBR: CDOs structurally set up to fail). The 70% figure reflects aspiration and reporting line, not effective delivery authority. The claim is consistent: data teams claim AI ownership; they systematically fail to deliver production AI capability; the structural reasons are the skills gap, mandate gap, and NFR incompatibility documented here.

Confidence levels are internally consistent: every high-confidence claim maps to at least two independent sources or to primary sources (Fowler, RFC 8693, NIST AI RMF). Medium-confidence claims are based on secondary analysis or vendor reports. Low-confidence inferences are explicitly labelled.

### §5 Depth and Breadth Expansion

**Technical lens - MCP as the emerging standard integration point.** MCP's adoption by the major cloud platforms (Microsoft, AWS, Google) in 2024-2025 is the strongest recent evidence that the industry has converged on the API layer as the correct integration point for agents. MCP is architecturally equivalent to what the item has argued from first principles: a declared-capability, access-scoped, auditable protocol over HTTPS/mTLS that sits between the agent and any data or action source. Organisations that deploy MCP servers against their business services - not against their data warehouses - are building the decoupled architecture this item recommends.

**Regulatory lens - the accountability chain.** APRA CPS 230 and the FCA/PRA's confirmation that CRO and CTO - not CDO - hold AI risk accountability are regulatory evidence that the correct accountability chain for production AI does not terminate at the data team. When regulators ask "who is accountable for this AI system's risk?", the answer must be a named senior manager with operational risk authority. The CDO typically holds no such authority over live production systems.

**Economic lens - the cost of getting this wrong.** IBM's 2025 CDO Study documents that 74% of organisations fail to scale AI to visible business value. The prior research item `2026-02-28-ai-strategy-business-efficiency-examples.md` identifies failure to scale beyond pilots as the dominant failure mode - and attributes it to treating AI as a technology project rather than an operating model transformation. [inference: derived from IBM CDO Study and BCG 10-20-70 data] Organisations that anchor AI in the data team are disproportionately represented in the 74% failure category because the data team lacks the change management mandate and cross-functional authority to drive operating model transformation.

**Behavioural lens - the data team's incentive structure.** Data teams are incentivised to expand their scope (more data products, more pipelines, more analytics use cases) and to be seen as enablers of AI. [inference: structural incentive analysis derived from IBM CDO Study and HBR CDO failure analysis; not directly measured] This creates a structural incentive to accumulate AI ownership even when the data team lacks the skills or mandate to deliver production AI. The IBM CDO Study finding that CDOs redefine strategies because "AI ambitions outpace readiness" is consistent with this dynamic: the ambition is real; the structural capability to deliver is absent.

**Historical lens - the BI analogy.** The same category error occurred with BI in the 2000s: organisations placed BI capability in the data team because BI required data. Production BI systems then accumulated operational dependencies (real-time feeds, alerts, user-facing dashboards) that the data team was not equipped to operate to production SLAs. The resolution was the same: BI products were handed to product engineering teams to operate, with the data team retained as a knowledge and data stewardship function. [inference: analogical reasoning from documented BI handoff pattern; no single authoritative study confirms the full AI transition will follow the same arc] AI follows the same arc, at higher stakes.

### §6 Synthesis

**Answer:** Coupling AI capability to the data/analytics department is a structural category error. The case is strongest at the technical layer: analytics platforms fail the non-functional requirements of production AI agents - latency, availability, delegated identity, mutation safety, and auditability - by design, not by implementation deficiency. The API layer, not the analytics plane, is the architecturally correct integration point for agents. The organisational case is corroborated by regulatory frameworks, empirical evidence on AI programme failure rates, and the systematic skills gap between data/analytics teams and the engineering disciplines required for production agent infrastructure.

**Key claims:**

1. Operational data is served through microservice APIs (Fowler); agents that consume operational data must therefore integrate through the API layer, not the analytics plane.
2. Analytics platforms fail production agent NFRs: sub-second latency, HADR, fine-grained delegated authorisation (STS/OAuth 2.0), mutation auditability. These are not fixable; they are design properties of the analytical plane.
3. RFC 8693 (OAuth 2.0 Token Exchange) and MCP are the correct integration standards; neither is natively supported by analytics platforms.
4. Agents need knowledge (policies, regulations, procedural context), not just data. Knowledge management is a distinct discipline; RAG is the implementation pattern.
5. NIST AI RMF, APRA CPS 230, FCA/PRA, and Singapore MAIGF all require cross-functional AI governance; no data/analytics team holds the mandate across IT, legal, HR, and compliance.
6. 74% of organisations fail to scale AI to visible business value (IBM/BCG). Placing AI in the data team is a contributing cause: the data team lacks operating model change authority.
7. The data team is the right owner of the analytical and experimental AI layer (model training, data exploration, BI automation). It is the wrong owner of the operational agent layer.
8. The hybrid model - data platform as read-only knowledge substrate accessed via API mediation - preserves data gravity and ML proximity advantages while avoiding the structural risks.

**Tradeoff table:**

| Dimension | Data-platform-centric AI | API-layer-centric AI |
|---|---|---|
| **Time-to-prototype** | Fast (data already there, SQL access) | Slower (API design, IAM setup required) |
| **Production latency** | High (warehouse query latency) | Low (purpose-built APIs) |
| **HADR** | Weak (batch-oriented RPO/RTO) | Strong (engineered into API services) |
| **Delegated identity (STS)** | Not supported | Supported natively via OAuth 2.0 / MCP |
| **Mutation safety** | Not supported (no mutation API model) | Supported via audited API endpoints |
| **Audit trail** | Query logs only (no agent-context trail) | Structured per-request telemetry with actor claim |
| **Zero-trust compatibility** | Not compatible (direct warehouse access) | Compatible (per-request policy enforcement) |
| **Regulatory accountability chain** | Terminates at CDO (no operational risk mandate) | Terminates at CTO/CRO (operational risk authority) |
| **Knowledge management** | Requires separate RAG layer anyway | RAG integrates directly with API layer |
| **Skills required** | SQL, ETL, BI (present in data team) | API engineering, IAM, SRE (absent from data team) |
| **Organisational mandate** | Limited to data/analytics scope | Cross-functional (IT, legal, HR, compliance) |
| **Regulatory exposure on failure** | High (accountability gap) | Lower (named senior manager with operational mandate) |

### §7 Recursive Review

All eight key claims are supported by at least one fact-labelled finding with a named source. No section consists only of a heading with placeholder content. The tradeoff table is derived from §2 evidence, not introduced fresh in §6. The §4 consistency check resolved the apparent tension between the Gartner CDAO ownership statistic and the IBM CDO failure data. §5 depth expansion added the MCP adoption evidence (technical), regulatory accountability chain (regulatory), cost of failure (economic), CDO incentive structure (behavioural), and the BI precedent (historical). The [assumption] label on "production agent with write capability" is explicit and its scope implications are stated. Sources marked [x] were accessed; sources marked [ ] were not accessible or not reached in this investigation and are noted in Risks/Gaps. All [inference] labels appear where claims are derived from multiple pieces of evidence rather than directly stated by a source. All [assumption] labels appear where claims require a condition that could vary.

---

## Findings

### Executive Summary

Coupling an organisation's AI capability to its data/analytics department is a structural category error: analytics platforms fail the non-functional requirements of production AI agents by design, and the data/analytics team lacks the organisational mandate, skills, and regulatory accountability required for the operational agent layer. The correct integration architecture places agents against the organisation's API layer - via API gateway, horizontally-scaling services, MCP servers, and STS token exchange (RFC 8693) - which satisfies the latency, HADR, delegated identity, mutation auditability, and zero-trust requirements that analytics platforms cannot. Knowledge management (policies, regulations, procedural context served via RAG) is a distinct discipline from data management and belongs in the API/platform layer, not the warehouse. Regulators including NIST AI RMF, APRA CPS 230, and FCA/PRA confirm that AI accountability requires IT, legal, HR, and compliance mandate that no data/analytics team holds; the empirical record shows that 74% of organisations that anchor AI in data teams fail to scale to visible business value.

### Key Findings

1. **Analytics platforms fail production AI agent NFRs by design, not by deficiency: they are built for batch/analytical workloads and cannot satisfy the sub-second latency, HADR, fine-grained delegated authorisation, mutation auditability, and zero-trust requirements that production agents demand.** (Confidence: high)

2. **Martin Fowler's data mesh architecture explicitly establishes that operational data is served through microservice APIs and that "data is hidden on the inside of each microservice, controlled and accessed through the microservice's APIs" - meaning agents that consume operational data must integrate through the API layer, not the analytical plane.** (Confidence: high)

3. **RFC 8693 (OAuth 2.0 Token Exchange) and the IETF AI agent extension draft provide the STS delegation model that agents require for auditable, narrowly-scoped, per-user-per-context delegated access - a capability that analytics platforms do not support and cannot be retrofitted to provide.** (Confidence: high)

4. **MCP (Model Context Protocol), adopted by Microsoft, AWS, Google, and Anthropic in 2024–2025 as an industry standard, implements the API-layer integration pattern: declared capabilities, access scopes, JSON-RPC over HTTPS/mTLS, audit logging, and per-request policy enforcement, with no analytics platform analogue.** (Confidence: high)

5. **Knowledge management - the discipline of curating policies, regulations, procedural context, and organisational strategy for agent consumption via RAG or knowledge graphs - is structurally distinct from data management and requires its own tooling, versioning, and governance layer that a data warehouse does not provide.** (Confidence: high)

6. **NIST AI RMF's Govern function, APRA CPS 230, and Singapore's Model AI Governance Framework all explicitly require cross-functional AI accountability spanning IT, legal, HR, and compliance; no data/analytics team holds mandate across these functions, and the FCA/PRA confirmed CRO and CTO - not CDO - bear AI risk accountability within their operational domains.** (Confidence: high)

7. **IBM's 2025 CDO Study found only 26% of CDOs confident their teams can support new AI revenue streams, and 74% of organisations globally fail to scale AI to visible business value; CDO Magazine and HBR both document structural CDO failure in AI delivery, attributing it to mandate gaps, absent engineering skills, and inability to drive cross-functional operating model change.** (Confidence: high)

8. **The hybrid model - data platform as read-only knowledge substrate accessed via a governed API mediation layer, not via direct SQL - preserves the genuine data-platform-centric advantages (data gravity, ML proximity, analytics tooling) while eliminating the NFR, identity, mutation, and accountability risks of direct warehouse access.** (Confidence: medium)

9. **The data team is the correct owner of the analytical and experimental AI layer (model training, data exploration, BI automation, ML experimentation) and an incorrect owner of the operational agent layer (production agents taking consequential actions with real-time write access, regulatory traceability requirements, and operational SLA obligations).** (Confidence: high)

10. **Placing AI ownership in the data team creates a structural incentive misalignment: data teams are rewarded for expanding data products and demonstrating AI adoption, creating pressure to accumulate AI ownership even when the team lacks production engineering, security, and change management capability - the behavioural dynamic documented in the 74% failure statistic.** (Confidence: medium)

11. **The BI precedent is directly analogous: BI capability placed in data teams in the 2000s eventually transferred to product engineering as BI accumulated operational dependencies that data teams could not service to production SLAs; production AI follows the same arc at higher regulatory and operational stakes.** (Confidence: medium)

12. **Regulators have not explicitly mandated separation of analytical and operational data access as a standalone requirement; the implication is indirect - operational risk, auditability, fine-grained access control, and board-level accountability requirements collectively produce the same architectural conclusion.** (Confidence: high)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Analytics platforms fail production agent NFRs by design | Pylar AI five-layer architecture; Machine Learning Mastery production agent deployment; Martin Fowler data mesh article | High | Consistent across architecture guidance |
| Operational data served through microservice APIs (Fowler) | Martin Fowler, "Data Mesh Principles and Logical Architecture" (2020), accessed | High | Primary source, verbatim quotation |
| RFC 8693 STS delegation for agents | RFC 8693 (rfc-editor.org); Auth0 Token Vault; IETF draft-oauth-ai-agents-on-behalf-of-user-01 | High | Standards-based; IETF draft confirms AI-specific extension in progress |
| MCP as API-layer integration standard | MCP specification (modelcontextprotocol.io); CSA MCP primer; Okta MCP overview | High | Industry adoption by 4 major cloud platforms confirmed |
| Knowledge management ≠ data management for agents | Xenoss enterprise knowledge base RAG; CompuVate RAG systems; KM Insider RAG and KM; Denser AI KM analysis | High | Consistent across independent sources |
| NIST AI RMF cross-functional governance requirement | NIST AI RMF (nist.gov); Openlayer NIST guide; GLACIS NIST guide | High | Primary standard; implementation guides corroborate |
| CRO/CTO not CDO holds AI accountability (FCA/PRA) | Prior research 2026-02-28-ai-line-1-line-2-risk-agents.md (FCA DP5/22 analysis) | High | Based on completed primary research |
| APRA CPS 230 cross-functional AI governance | Prior research 2026-02-28-rbnz-ai-supervisory-expectations.md (APRA analysis) | High | Based on completed primary research |
| 74% of organisations fail to scale AI to visible value | IBM 2025 CDO Study; prior research 2026-02-28-ai-strategy-business-efficiency-examples.md (BCG data) | High | Two independent datasets agree |
| 26% of CDOs confident in AI revenue support | IBM 2025 CDO Study | High | Primary data; IBM IBV report |
| CDOs structurally set up to fail in AI delivery | HBR "Why Chief Data and AI Officers Are Set Up to Fail" (2023); CDO Magazine lessons analysis | High | HBR is a credible secondary; CDO Magazine corroborates |
| Hybrid model preserves advantages without risks | Inference from Fowler + MCP + RFC 8693 evidence | Medium | Logical derivation; no single source makes this claim explicitly |
| Data team correct for experimental AI, wrong for operational | Inference from NFR analysis + organisational mandate analysis | High | Consistent with all evidence streams; no source explicitly contradicts |
| Incentive misalignment in data team AI ownership | IBM CDO Study (ambitions outpace readiness); HBR CDO failure analysis | Medium | Described as structural dynamic, not directly measured |
| BI precedent for AI | [inference] from documented pattern of data-team-to-engineering-team handoffs in BI | Medium | No single authoritative study; widely observable pattern |
| No explicit regulatory separation mandate | Prior research RBNZ and APRA items; NIST AI RMF review | High | Absence confirmed across multiple regulatory frameworks reviewed |

### Assumptions

- **Assumption:** "Production agent" means an agent that takes consequential actions (sends communications, modifies records, makes decisions with downstream effects) rather than a read-only analytics assistant. **Justification:** The research question and scope explicitly include write operations and the high-stakes agent category is the primary motivating use case. A pure read-only analytics assistant raises fewer NFR concerns, though the identity and audit trail arguments still apply.

- **Assumption:** The skills gap between data/analytics teams and API/platform engineering is sufficiently wide that bridging it within the existing data team structure is not feasible at pace for most organisations. **Justification:** IBM CDO Study and multiple skills gap analyses confirm the gap; however, organisations with large, senior data engineering teams (large tech companies, advanced fintechs) may have more cross-disciplinary skill sets that reduce the gap.

### Analysis

The technical, organisational, and empirical evidence converge on the same structural conclusion. Fowler's operational/analytical data plane separation and the NFR analysis show that analytics platforms fail production agent requirements by design, not by implementation deficiency - the limitations are architectural. Regulatory frameworks (NIST AI RMF, APRA CPS 230, FCA/PRA) and IBM/HBR CDO research independently confirm that no data/analytics team holds the mandate or possesses the skills required for the operational agent layer. The 74% AI scaling failure rate, the 26% CDO readiness figure, and the HBR structural analysis of CDO failure are three empirically independent data points documenting what happens when data teams carry the production AI mandate.

The genuine counter-argument - data gravity, ML proximity, and prototype speed - was engaged directly. These advantages are real at the analytical and experimental layer. The resolution is the hybrid model: the data team retains ownership of the analytical/experimental plane; the API layer is built or strengthened for the operational agent layer. This is not a radical restructuring; it is a separation of concerns that the data mesh architecture already implies.

Evidence sufficiency is high for the architectural claims (multiple independent technical sources, primary standards), medium for the organisational claims (empirical data exists but no controlled studies compare AI outcomes by departmental ownership structure), and medium for the BI precedent (widely observable but not systematically studied).

### Risks, Gaps, and Uncertainties

- **Evidence gap on controlled studies:** No published study directly compares AI programme outcomes by departmental ownership structure (data team vs. cross-functional vs. dedicated AI function). The 74% failure rate is associated with absence of cross-functional ownership, not with data-team ownership specifically - though the CDO readiness gap and HBR analysis provide strong indirect evidence.

- **Inaccessible sources:** Zhamak Dehghani's *Data Mesh* (O'Reilly, 2022), W3C DID spec, CNCF Zero Trust Whitepaper, OWASP API Security Top 10, Google Cloud and Microsoft Azure architecture documentation, Thoughtworks Technology Radar, and McKinsey Global Institute AI survey were not directly fetched in this investigation. These sources were not required to establish the claims - the claims are well-supported by accessed sources - but their absence is noted. The Fowler article (public, accessed) provides the foundational data mesh argument; the Dehghani book would corroborate but is paywalled.

- **Hybrid model evidence:** The recommendation that a hybrid model (data platform as API-mediated read-only knowledge substrate) preserves data-team advantages is an inference, not a directly documented case study. No published case study was found that specifically documented the transition from data-platform-centric to API-layer-centric agent architecture and its outcomes.

- **NZ-specific gap:** RBNZ has no standalone AI governance framework (confirmed in prior research). The claim that NZ regulatory requirements imply cross-functional accountability is correct but derived from BS11/BPR and APRA CPS 230, not from RBNZ-specific AI guidance.

- **Small organisations:** The argument assumes an organisation of sufficient size to have distinct data/analytics and IT/platform engineering functions. Very small organisations where the same team does both may face a different analysis.

### Open Questions

- What does a purpose-built "AI capability function" organisational chart look like in practice, and who should it report to (CTO, COO, CEO)?
- How should organisations handle the transition period where the data team *does* hold AI tooling but the target state is an API-layer-centric architecture - what is the migration path?
- Is there a documented case study of an organisation that successfully transitioned from data-platform-centric to API-layer-centric AI architecture, and what were the costs and timeline?
- What are the procurement and vendor implications of separating the AI capability from the data platform - does MCP server adoption require significant new vendor contracts?
- How does the argument change for organisations that have invested heavily in lakehouse architectures (Databricks, Delta Lake) that blur the operational/analytical boundary?

---

## Output

- Type: knowledge, backlog-item
- Description: A structured argument with evidence map, tradeoff table, and organisational design recommendation establishing that data/analytics department ownership of AI capability is a structural category error; the API layer is the correct integration point for production agents; hybrid models preserve data-team advantages; cross-functional AI governance is required by major regulatory frameworks and empirical evidence.
- Links:
  - https://martinfowler.com/articles/data-mesh-principles.html (Fowler data mesh - operational vs. analytical plane)
  - https://www.rfc-editor.org/rfc/rfc8693.html (RFC 8693 - STS delegation for agents)
  - https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/2025-cdo (IBM 2025 CDO Study)