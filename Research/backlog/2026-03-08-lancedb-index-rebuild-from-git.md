---
title: "LanceDB index rebuild speed from git: enabling stateless deployment"
added: 2026-03-08
status: backlog
priority: high
blocks: []
tags: [lancedb, performance, indexing, serverless, memory-system]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# LanceDB index rebuild speed from git: enabling stateless deployment

## Research Question

Can the LanceDB index be rebuilt from the `.md` files in the repo on startup fast enough to enable stateless (per-request) deployment? Measure rebuild time at: current corpus size, 100 files, 500 files, 1000 files. Is the embedding model load time (BAAI/bge-small-en-v1.5) the bottleneck or the LanceDB write operations? Would a lighter embedding model (e.g. MiniLM) or pre-computed embeddings stored in git change the equation?

## Scope

**In scope:**
- Benchmark rebuild time for BAAI/bge-small-en-v1.5 at multiple corpus sizes (current, 100, 500, 1000 files)
- Profiling: model load time vs embedding time vs LanceDB write time — which is the bottleneck?
- Alternative lightweight embedding models: `sentence-transformers/all-MiniLM-L6-v2` and similar
- Pre-computed embeddings stored as JSON in git: feasibility and git repo size implications
- LanceDB cold-start characteristics: is there a minimum viable warm-up time?
- Comparison with pure GitHub code search as a zero-rebuild alternative (keyword-only)

**Out of scope:**
- Alternative vector databases (Qdrant, Pinecone, Weaviate — out of scope for Memory-System architecture)
- Changing the embedding model in production without a migration plan (out of scope for this item)

**Constraints:** Target: rebuild in under 5–10 seconds for a typical personal corpus. Test environment should match the target deployment (low-CPU, low-memory free tier).

## Context

Currently `.lancedb` is excluded from git and must persist on the local machine. If the index can be rebuilt in under 5–10 seconds for a typical corpus, the deployment model simplifies significantly: any stateless compute (Cloudflare Worker with bundled index, Lambda, GitHub Actions) becomes viable for retrieval as well as capture. This is a direct design input to the self-hosted MCP server decision (`2026-03-08-self-hosted-mcp-server-options.md`).

Cross-reference: `Research/completed/2026-03-02-agent-memory-management-context-injection.md` notes that MemoryOS achieves +49% F1 with an OS-inspired three-tier memory hierarchy — startup rebuild latency is a direct design constraint on which tier model is viable for a self-hosted deployment. The completed `2026-03-02-semantic-full-text-search.md` may also have relevant findings on embedding model selection for semantic search.

## Approach

1. Instrument the current `add_memory` / index-build path in `mcp_server.py` to measure: model load time, per-file embedding time, LanceDB write time
2. Run benchmarks at corpus sizes: current (baseline), 100, 500, 1000 synthetic `.md` files
3. Profile with BAAI/bge-small-en-v1.5 and compare with `all-MiniLM-L6-v2`
4. Prototype pre-computed embeddings: generate vectors once, store as `.json` in git, load directly into LanceDB at startup
5. Measure git repo size impact of storing pre-computed embeddings for 1000 files
6. Evaluate GitHub code search as a fallback for zero-rebuild retrieval: precision/recall trade-off
7. Produce a recommendation: which deployment model (stateless rebuild vs persistent index) is viable at each corpus size?

## Sources

- [ ] `Research/completed/2026-03-02-agent-memory-management-context-injection.md` — MemoryOS three-tier hierarchy; startup latency as design constraint
- [ ] `Research/completed/2026-03-02-semantic-full-text-search.md` — semantic search and embedding model selection findings
- [ ] LanceDB docs: https://lancedb.github.io/lancedb/
- [ ] LanceDB Python API (Table, add, search): https://lancedb.github.io/lancedb/python/python/
- [ ] BAAI/bge-small-en-v1.5 model card: https://huggingface.co/BAAI/bge-small-en-v1.5
- [ ] `sentence-transformers/all-MiniLM-L6-v2` model card: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
- [ ] GitHub code search API (as zero-rebuild alternative): https://docs.github.com/en/rest/search/search
- [ ] `2026-03-08-self-hosted-mcp-server-options.md` — deployment options that depend on this benchmark

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Restate the research question. Confirm scope, constraints, and output format.

-

### §1 Question Decomposition

Approach sub-questions broken into atomic questions — each answerable with a single evidence-based claim.

-

### §2 Investigation

Evidence gathered per atomic question. Label each claim: **[fact]**, **[inference]**, or **[assumption]** with source.

-

### §3 Reasoning

Facts, inferences, and assumptions explicitly separated. No unsupported generalisations or narrative leaps.

-

### §4 Consistency Check

Internal contradictions identified and resolved (or explicitly flagged where unresolvable).

-

### §5 Depth and Breadth Expansion

Findings re-examined through relevant lenses (technical, regulatory, economic, historical, behavioural).

-

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

-

---

## Findings

*(Populated from §6 Synthesis above.)*

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

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: knowledge, backlog-item
- Description:
- Links:
