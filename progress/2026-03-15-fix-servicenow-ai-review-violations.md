# 2026-03-15 — Fix review violations: servicenow-ai-knowledge-rag-agents

## Session type
Targeted fix — addressing review feedback

## File changed
`Research/completed/2026-03-08-servicenow-ai-knowledge-rag-agents.md`

## Changes made

**citation-discipline fixes:**
- Expanded ITSM → IT Service Management (ITSM) at first use (RSO §1, line 22)
- Expanded CSDM → Common Service Data Model (CSDM) at first use (RSO §1, line 27)
- Expanded GRC → Governance, Risk, and Compliance (GRC) at first use (RSO §0, line 52)
- Expanded IRM → Integrated Risk Management (IRM) at first use (Prior work, line 91)
- Added [inference] label to "The RAG implementation…represents current best practice" sentence

**speculation-control fixes:**
- Added [inference] to "ServiceNow's AI architecture makes a defensible bet"
- Added [inference] to "The RAG implementation…represents current best practice" and "These are sound architectural choices"
- Added [inference] to "For regulated financial services, the compliance architecture is mature"

**remove-ai-slop fix:**
- Removed symmetrical illustration ("The organisation that invested three years… / The organisation that activated Now Assist on a 50,000-article knowledge base…") and replaced with a single direct statement

## Outcome
All 8 violations addressed. Committed on branch `copilot/fix-research-item-errors`.
