# 2026-03-08 — ServiceNow CSDM research backlog items

**Task:** Create new backlog research items covering ServiceNow CSDM, modules (ITSM, APM, SPM, IRM/GRC, FSO), process mapping, and the future of ServiceNow with AI/RAG/agent frameworks.

## What was created

Four new backlog items in `Research/backlog/`:

### 1. `2026-03-08-servicenow-csdm-data-modelling.md` (priority: high)
**Question:** How should organisations model their enterprise data in ServiceNow to meet the CSDM standard while keeping the model maintainable and accurate — and what are the practical patterns for aligning ITSM, APM, SPM, IRM/GRC, and FSO to that shared data foundation?

Key scope decisions:
- Covers all five major modules and how each depends on CSDM
- Explicitly connects to prior RUN/BUILD research on application definition governance
- Includes TCO linkage via ITFM/TBM
- Blocks the holistic platform strategy item

### 2. `2026-03-08-servicenow-process-mapping.md` (priority: medium)
**Question:** What options exist within ServiceNow for documenting, mapping, and maintaining business and IT processes — and which approaches are sustainable enough to stay meaningful over time?

Key scope decisions:
- Covers native SNOW capabilities: Process Universe, Flow Designer, Playbooks, Process Mining
- Explicitly framed around sustainability — what *stays* accurate vs what decays
- Includes governance models and ownership triggers
- Blocks the holistic platform strategy item

### 3. `2026-03-08-servicenow-ai-knowledge-rag-agents.md` (priority: medium)
**Question:** How is ServiceNow evolving its platform to support AI-powered knowledge management, RAG, and agent frameworks — and what should an organisation understand about this direction to make durable decisions?

Key scope decisions:
- Covers Now Assist, AI Search, agent orchestration, external LLM integration
- Links to prior agent memory, knowledge representation, and AI strategy research
- Explicitly separates GA vs preview vs roadmap
- Includes regulated-industry governance requirements
- Blocks the holistic platform strategy item

### 4. `2026-03-08-servicenow-platform-strategy.md` (priority: high)
**Question:** How should an organisation develop a coherent, practical ServiceNow platform strategy integrating data foundations, modules, process documentation, and AI into a sustainable operating model?

Key scope decisions:
- Synthesis item — cannot start until items 1–3 are complete
- Connects ServiceNow to RUN/BUILD TCO and application definition research
- Includes 12–24 month sequencing, governance operating model, and maturity model
- NZ/Australia regulated financial services lens (FSO, operational resilience)
- `output: [knowledge, backlog-item]` as it may spawn further items

## Related research identified

- `2026-03-07-run-build-it-allocation-implementation-how` — application definition problem is the same governance challenge as CSDM Application record governance
- `2026-03-07-run-vs-build-it-spending-allocation` — RUN/BUILD frameworks and TCO, directly connectable to CSDM+ITFM cost allocation
- `2026-02-28-ai-control-testing-and-assurance` — ServiceNow GRC vendor context, IRM module; AI agents for compliance

## Sequencing rationale

Split the original request into three specific items (CSDM, Process, AI) plus one holistic synthesis item. The synthesis item explicitly blocks on all three using the `blocks` frontmatter field, ensuring the holistic view is built on completed evidence rather than assumptions.
