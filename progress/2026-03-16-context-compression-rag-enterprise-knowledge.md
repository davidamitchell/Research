# 2026-03-16 — Research Loop (context-compression-rag-enterprise-knowledge)

**Completed:**

Research item:
- `Research/completed/2026-03-15-context-compression-rag-enterprise-knowledge.md` — completed; Advanced RAG (RAPTOR, modular routing, hybrid search) is the current best practice for surfacing organisational knowledge into an LLM context window. Extending the context window to 1M tokens does not substitute for structured retrieval — NVIDIA's RULER benchmark confirms quality degrades significantly. LLMLingua-2 achieves 2–5x production-ready compression; knowledge corpus governance remains the primary determinant of RAG quality.

Sources consulted:
- https://arxiv.org/abs/2312.10997 (Gao et al. RAG Survey 2024 — comprehensive taxonomy of Naive/Advanced/Modular RAG)
- https://arxiv.org/abs/2401.18059 (RAPTOR — hierarchical tree-based retrieval, ICLR 2024)
- https://arxiv.org/abs/2403.12968 (LLMLingua-2 and LongLLMLingua — production-ready context compression, ACL 2024)

## Mini-Retro

1. **Did the process work?** Yes. The six-section research skill output structure produced a well-evidenced, internally consistent item. The review passed on first submission with no open violations.
2. **What slowed down or went wrong?** The arXiv ID provided in the original backlog item for LLMLingua (2310.06025) resolved to an unrelated physics paper — the correct ID is 2310.05736. This required a corrective search step. The SKILL.md file was absent from `.github/skills/` (empty directory), so the research skill was applied from memory via the loop instructions rather than from the file directly.
3. **What single change would prevent this next time?** Verify arXiv IDs in backlog items at time of creation rather than at time of research, by linking to the abstract page and confirming the title.
4. **Is this a pattern?** The missing SKILL.md is a known pattern — it is present when the sync-skills workflow runs but empty at session start. The arXiv ID mismatch is a one-off data-entry error, not a recurring structural pattern.
