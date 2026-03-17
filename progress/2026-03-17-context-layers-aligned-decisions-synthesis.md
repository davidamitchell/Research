# 2026-03-17 — Research Loop (context-layers-aligned-decisions-synthesis)

**Completed:**

Research item:
- `Research/completed/2026-03-15-context-layers-aligned-decisions-synthesis.md` — completed; defines an 8-layer Layered Organisational Context Architecture (LOCA) ordering knowledge by authority (regulatory → immediate task), with per-layer storage/retrieval/compression strategies; three independent frameworks (cognitive neuroscience, AI context management, enterprise KM) converge on the same hierarchical structure; governance of source corpora at each layer is the primary unsolved deployment prerequisite.

Sources consulted:
- https://arxiv.org/abs/2401.18059 — RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval (ICLR 2024); establishes hierarchical tree indexing as the correct offline strategy for Layers 1 and 5
- https://arxiv.org/abs/2212.08073 — Anthropic Constitutional AI paper; establishes the self-evaluation mechanism used for Layer 2 values encoding
- https://arxiv.org/abs/2308.03688 — AgentBench: Evaluating LLMs as Agents; empirical confirmation that missing business/policy context (Layers 5–6) is the dominant cause of enterprise agent failures

## Mini-Retro

1. **Did the process work?** Yes. The research skill sections produced well-sourced output and the review workflow passed on the first submission. The prerequisite item (`2026-03-15-context-compression-rag-enterprise-knowledge.md`) was already completed and provided the RAG/compression foundation; researching neurological aspects independently via web search worked well.

2. **What slowed down or went wrong?** Acronym audit caught several violations that required multiple rounds of fixes (TOGAF, RAPTOR, GraphRAG, RAG, LLM first-use ordering, EU, AIOS format, SLAs, ADM format). Each fix was straightforward once identified, but the volume of abbreviations in a synthesis item is higher than in a single-topic item — the audit pass took longer than expected.

3. **What single change would prevent this next time?** Run the acronym audit as a final step before writing §6 Synthesis, not after completing Findings. The violations were concentrated in §2 Investigation, so catching them before the content propagates to Findings would halve the fix count.

4. **Is this a pattern?** Yes — this matches the known pattern documented in the research-prompt.md table: acronym violations are the most common review failure. The synthesis item format amplifies this because it integrates terminology from multiple domains (neuroscience, enterprise KM, AI context management) each with its own abbreviation set. No new pattern; the existing mitigation (run acronym audit earlier in the process) applies.
