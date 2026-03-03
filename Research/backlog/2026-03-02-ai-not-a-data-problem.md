---
title: "AI capability is not a data problem — why the data/analytics department is the wrong home for organisational AI"
added: 2026-03-02
status: backlog
priority: high
tags: [ai-strategy, architecture, data-platform, api-layer, agents, organisational-design, governance, mcp, zero-trust, identity]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# AI capability is not a data problem — why the data/analytics department is the wrong home for organisational AI

## Research Question

What is the strongest case — technical, architectural, organisational, legal, and regulatory — that an organisation's AI capability should NOT be owned by or coupled to its data/analytics department or data platform, and what concrete tradeoffs arise when that coupling is made?

## Scope

**In scope:**
- Architectural argument: why data warehouses, lakes, and analytics platforms fail the non-functional requirements (NFRs) demanded by production agents (HADR, fine-grained access control, operational SLAs, auditability)
- The correct integration point for agents: the organisation's API layer (API gateways, horizontally-scaling services, MCP servers, STS token exchange, DID/verifiable credentials, zero-trust networks)
- What agents actually need: intent, knowledge, context, strategy, structure, constraints, regulations, policies, standards — none of which live in a data warehouse
- Organisational design argument: the skills gap between data/analytics professionals and the engineering disciplines required for production agent infrastructure (security, identity, observability, service design)
- The multi-stakeholder nature of AI capability: IT, business operations, HR/people, legal, regulatory compliance — no single department can own it unilaterally
- Tradeoffs of the coupled (data-platform-centric) model vs. the decoupled (API-layer-centric) model
- Case studies, white papers, and first-principles reasoning supporting the decoupled model
- Regulatory and compliance angle: auditability, fine-grained access control, and data residency requirements that analytics platforms are not designed to satisfy

**Out of scope:**
- Detailed implementation of specific API gateway products or MCP server implementations
- Vendor comparison (specific data warehouse vs. specific API platform)
- Model selection, fine-tuning, or LLM evaluation
- Research into AI use cases themselves (covered by `2026-02-28-ai-strategy-*.md` items)

**Constraints:** Research should be anchored in published evidence (case studies, white papers, architecture guidance, regulatory frameworks) where possible; first-principles reasoning acceptable where evidence is sparse. NZ regulatory context (RBNZ, Privacy Act, DIA, MBIE) relevant but global evidence preferred for generalisability.

## Context

Organisations moving into AI often default to placing AI capability inside the data or analytics team — because that team already handles data pipelines, BI tooling, and ML models. This conflation of "AI" with "data" is a category error that creates systemic risks:

1. **Operational NFRs mismatch:** Data warehouses and analytics platforms are designed for batch/analytical workloads, not for sub-second agent responses, high availability, disaster recovery, or multi-tenant access patterns. Coupling agents to these platforms inherits their fragility.

2. **Access control gap:** Analytics platforms typically implement coarse-grained, role-based access for human analysts. Agents require fine-grained, context-aware, delegated access (e.g. an agent acting *on behalf of* a specific user in a specific context). STS token exchange, OAuth 2.0 device flow, and DID-based identity are not standard capabilities of data platforms.

3. **Skills mismatch:** Data engineers and analysts are expert in SQL, ETL, BI, and statistical modelling — not in service design, API security, identity federation, zero-trust network architecture, SCOM/observability, or operational SLAs. These are API/platform engineering disciplines.

4. **Knowledge ≠ Data:** Agents need structured knowledge (policies, regulations, organisational strategy, procedural context) — not raw data. Knowledge management is a distinct discipline from data management, requiring curation, versioning, and contextual scoping.

5. **Mutation risk:** Agents that can enact state changes (write operations) must do so through audited, secured, API-mediated pathways — not through direct database or warehouse access. The analytics plane has no concept of a mutation API with full audit trail, SCOM alerting, and rollback capability.

6. **Organisational accountability:** AI capability cuts across legal (liability, contracts), HR (workforce impact, skills uplift), compliance (regulation, policy), IT (infrastructure, security), and business operations. No single team — especially not one historically scoped to reporting and analytics — can hold that mandate.

This item makes the case for a deliberate separation: agents interact with the world through the organisation's API layer, not its analytics plane. It also examines what needs to change organisationally to make that separation real.

## Approach

1. **First-principles technical argument** — Enumerate the NFRs required by production AI agents (availability, latency, fine-grained authz, audit, mutation safety, HADR) and show which data platform categories (data warehouse, data lake, lakehouse, analytics DB) fail each NFR by design. Contrast with API layer capabilities.

2. **API layer as the agent integration point** — Research the architecture pattern: API gateway → horizontally-scaling services → MCP servers → agent. Map how each component satisfies the NFRs that the data plane cannot. Include: STS token exchange for delegated identity, DID/verifiable credentials, zero-trust network principles, SCOM/observability patterns, multi-context service design (staff/customer/system/agent personas).

3. **Knowledge vs. data distinction** — Research knowledge management as a discipline distinct from data management. How do organisations scope contextual knowledge for agents (policy documents, regulatory constraints, procedural context)? What are the established patterns (RAG, knowledge graphs, curated context windows)?

4. **Organisational design evidence** — Find case studies and white papers on AI governance structures. Which organisations have succeeded with a dedicated AI capability function that spans IT + business + legal + HR? Which have failed by placing AI inside data/analytics? What does the literature say about cross-functional AI teams?

5. **Skills gap analysis** — What skills are required to build and operate production agent infrastructure that are absent from typical data/analytics teams? (Service engineering, identity and access management, API security, SRE/observability, zero-trust networking, legal-tech, change management.)

6. **Regulatory and compliance angle** — What do regulators (RBNZ, OCC, FCA, APRA, GDPR/Privacy Act, NZ Privacy Act 2020) say about AI governance, auditability, and data access controls? Do any explicitly require separation of analytical and operational data access?

7. **Tradeoff analysis** — Enumerate the costs of the coupled model (data-platform-centric AI) and the decoupled model (API-layer-centric AI). Include: time-to-market, risk profile, technical debt, organisational friction, regulatory exposure. Produce a structured tradeoff table.

8. **Counter-arguments** — Steelman the case for data-platform-centric AI. Where does it work? What are its genuine advantages (existing data gravity, ML model proximity, analytics tooling)? Why do those advantages not outweigh the structural risks at the operational agent layer?

## Sources

- [ ] Martin Fowler — "DataMesh" and operational vs. analytical data plane separation: https://martinfowler.com/articles/data-mesh-principles.html
- [ ] Zhamak Dehghani — *Data Mesh* (O'Reilly, 2022) — operational vs. analytical plane distinction
- [ ] NIST AI RMF (AI Risk Management Framework): https://www.nist.gov/artificial-intelligence/ai-risk-management-framework — governance and organisational accountability
- [ ] RBNZ — AI supervisory expectations and governance guidance: https://www.rbnz.govt.nz
- [ ] Google Cloud Architecture — "Separation of analytical and operational workloads": https://cloud.google.com/architecture
- [ ] Microsoft Azure Well-Architected Framework — AI workload NFRs: https://learn.microsoft.com/en-us/azure/well-architected/
- [ ] Anthropic / OpenAI usage policies and agent architecture guidance
- [ ] McKinsey Global Institute — "The state of AI in organisations" (annual survey): https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
- [ ] Gartner — "AI governance and organisational design" research notes
- [ ] OAuth 2.0 Token Exchange (RFC 8693) — STS delegation pattern for agents: https://datatracker.ietf.org/doc/html/rfc8693
- [ ] W3C Decentralised Identifiers (DID) spec: https://www.w3.org/TR/did-core/
- [ ] CNCF Zero Trust Whitepaper: https://github.com/cncf/tag-security/blob/main/security-whitepaper/v2/cloud-native-security-whitepaper.md
- [ ] OWASP API Security Top 10: https://owasp.org/www-project-api-security/
- [ ] Andreessen Horowitz (a16z) — AI enterprise architecture commentary
- [ ] Thoughtworks Technology Radar — Data mesh, API gateway, and agent architecture entries: https://www.thoughtworks.com/radar
- [ ] `Research/completed/2026-02-28-rbnz-ai-supervisory-expectations.md` — NZ regulatory context
- [ ] `Research/backlog/2026-02-28-ai-strategy-business-efficiency-examples.md` — AI strategy examples context
- [ ] `Research/backlog/2026-02-28-ai-line-1-line-2-risk-agents.md` — risk and governance framing

---

## Findings

*(Fill in when completing. Follow the research skill synthesis structure.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly.

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim.

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

Explicit assumptions made during the investigation and the justification for each.

- **Assumption:** ... **Justification:** ...

### Analysis

How the evidence was weighed, what trade-offs were identified, and how competing interpretations were resolved.

### Risks, Gaps, and Uncertainties

What is still unknown? Where does the evidence fall short? What could change the conclusion?

-

### Open Questions

Questions that surfaced during research but are out of scope for this item. Each may become a new backlog item.

- What does a purpose-built "AI capability function" org chart look like in practice, and who should it report to?
- How should organisations handle the transition period where the data team *does* hold AI tooling but the target state is decoupled?
- Is there a hybrid model where the data platform serves as a read-only knowledge source (via API mediation) rather than a direct agent integration point?
- What are the procurement and vendor implications of separating the AI capability from the data platform?

---

## Output

- Type: knowledge, backlog-item
- Description: A structured argument (evidence map + tradeoff table + organisational design recommendation) that makes the case for decoupling AI capability from the data/analytics department; may spawn a follow-on backlog item on API-layer agent architecture patterns or organisational AI governance design
- Links:
  - `Research/completed/2026-02-28-rbnz-ai-supervisory-expectations.md`
  - `Research/backlog/2026-02-28-ai-strategy-business-efficiency-examples.md`
  - `Research/backlog/2026-02-28-ai-line-1-line-2-risk-agents.md`
