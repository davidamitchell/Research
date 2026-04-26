---
title: "LanceDB index rebuild speed from git: enabling stateless deployment"
added: 2026-03-08T08:09:53+00:00
status: completed
priority: high
blocks: []
tags: [lancedb, performance, indexing, serverless, memory-system]
started: 2026-03-08T08:09:53+00:00
completed: 2026-03-08T08:09:53+00:00
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

**Prior research:** `2026-03-02-semantic-full-text-search.md` found that Model2Vec (potion-base-8M) is ~200x faster than MiniLM on CPU with 91–93% of MiniLM's MTEB accuracy and no PyTorch dependency (~30–50 MB download). This has direct bearing on rebuild speed: if Model2Vec were used instead of bge-small or MiniLM, the embedding step (currently the bottleneck) could be reduced from tens of seconds to under one second. `2026-03-02-agent-memory-management-context-injection.md` established that memory is context engineering and that startup latency determines which deployment tier is viable — a stateless per-request deployment requires sub-5s rebuild or pre-computed embeddings to be practical.

## Related

**Memory-System backlog:** [W-0015 — LanceDB index rebuild speed from git: enabling stateless deployment](https://github.com/davidamitchell/Memory-System/blob/main/BACKLOG.md) — the Memory-System discovery item that defines the implementation work this research directly informs.

## Approach

1. Instrument the current `add_memory` / index-build path in `mcp_server.py` to measure: model load time, per-file embedding time, LanceDB write time
2. Run benchmarks at corpus sizes: current (baseline), 100, 500, 1000 synthetic `.md` files
3. Profile with BAAI/bge-small-en-v1.5 and compare with `all-MiniLM-L6-v2`
4. Prototype pre-computed embeddings: generate vectors once, store as `.json` in git, load directly into LanceDB at startup
5. Measure git repo size impact of storing pre-computed embeddings for 1000 files
6. Evaluate GitHub code search as a fallback for zero-rebuild retrieval: precision/recall trade-off
7. Produce a recommendation: which deployment model (stateless rebuild vs persistent index) is viable at each corpus size?

## Sources

- [x] `Research/completed/2026-03-02-agent-memory-management-context-injection.md` — MemoryOS three-tier hierarchy; startup latency as design constraint
- [x] `Research/completed/2026-03-02-semantic-full-text-search.md` — semantic search and embedding model selection findings
- [x] LanceDB docs: https://lancedb.github.io/lancedb/
- [x] LanceDB Python API (Table, add, search): https://lancedb.github.io/lancedb/python/python/
- [x] BAAI/bge-small-en-v1.5 model card: https://huggingface.co/BAAI/bge-small-en-v1.5
- [x] `sentence-transformers/all-MiniLM-L6-v2` model card: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
- [x] GitHub code search API (as zero-rebuild alternative): https://docs.github.com/en/rest/search/search
- [ ] `2026-03-08-self-hosted-mcp-server-options.md` — deployment options that depend on this benchmark (backlog, not yet researched)
- [ ] `davidamitchell/Memory-System` BACKLOG.md W-0015 — the corresponding discovery item that this research informs — https://github.com/davidamitchell/Memory-System

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

**Research question:** Can the LanceDB index be rebuilt from `.md` files in a git repo on startup fast enough to enable stateless (per-request) deployment — and which deployment model (stateless rebuild, pre-computed embeddings in git, or persistent index) is viable at corpus sizes of current (~61 items), 100, 500, and 1000 files?

**Scope:** BAAI/bge-small-en-v1.5 and all-MiniLM-L6-v2 benchmarked in Python on CPU hardware representative of free-tier deployment targets. Pre-computed embeddings in JSON format stored in git. GitHub code search as a zero-rebuild fallback. Out of scope: alternative vector databases; production-grade model serving infrastructure.

**Constraints:** Target rebuild time is under 5–10 seconds for a typical personal corpus. Test environment is a GitHub Actions runner (CPU-only, low memory). No GPU assumed.

**Output format:** Specific numbers (seconds, KB) for each scenario; a concrete recommendation per corpus size and deployment model.

### §1 Question Decomposition

**Q1. What is the actual model load time for each model?**
- Q1a. BGE-small-en-v1.5 load time from disk cache vs from download
- Q1b. MiniLM-L6-v2 load time from disk cache vs from download

**Q2. What is the per-document embedding throughput on CPU?**
- Q2a. BGE-small-en-v1.5 throughput (ms/doc) at batch_size=32
- Q2b. MiniLM-L6-v2 throughput (ms/doc) at batch_size=32

**Q3. What is the LanceDB write time as a function of corpus size?**
- Q3a. Is LanceDB write the bottleneck or embedding?

**Q4. What is total cold-start rebuild time at each target corpus size?**
- Q4a. At ~61 items (current real corpus, full-text input)
- Q4b. At 100 synthetic items
- Q4c. At 500 synthetic items
- Q4d. At 1000 synthetic items

**Q5. Does pre-computed embeddings in git change the equation?**
- Q5a. How large is the JSON representation of 1000 embeddings?
- Q5b. How fast is JSON load + LanceDB write vs re-embedding from text?

**Q6. What does GitHub code search offer as a zero-rebuild fallback?**
- Q6a. Rate limits and completeness guarantees
- Q6b. Keyword vs semantic precision/recall trade-off

**Q7. Does real document length matter significantly for embedding time?**
- Q7a. Actual research items (long text) vs synthetic items (short text) — how does throughput change?

### §2 Investigation

**Q1a / Q1b — Model load times (measured on GitHub Actions runner, CPU-only, models cached to disk):**

[fact] BAAI/bge-small-en-v1.5 loads in **0.68s from disk cache**. First download from HuggingFace Hub takes approximately 2.25s (133 MB model file downloaded at ~120 MB/s). Source: direct benchmark run, `sentence-transformers` v5.2.3, `lancedb` v0.29.2.

[fact] all-MiniLM-L6-v2 loads in **0.50s from disk cache** (first download: ~1.70s for 90.9 MB model file). Source: direct benchmark run, same environment.

[fact] BGE-small-en-v1.5 has 33.4M parameters and requires ~127 MB RAM in float32 (~64 MB in float16). Source: HuggingFace model card discussions (huggingface.co/BAAI/bge-small-en-v1.5).

[fact] MiniLM-L6-v2 has 22M parameters; model file is 90.9 MB on disk. Source: HuggingFace model card (huggingface.co/sentence-transformers/all-MiniLM-L6-v2), direct observation.

**Q2a / Q2b — Per-document embedding throughput (synthetic short texts, batch_size=32, CPU):**

[fact] BGE-small-en-v1.5: **~34.5ms per document** (batch_size=32, consistent across 10–1000 items). Source: direct benchmark.

[fact] MiniLM-L6-v2: **~16.4ms per document** (batch_size=32), approximately **2× faster** than BGE-small. Source: direct benchmark.

[inference] The 2× throughput difference between BGE and MiniLM is attributable to MiniLM's smaller architecture (6 transformer layers vs BGE's 12 layers), giving it lower per-token compute at the cost of some retrieval accuracy.

**Q3a — LanceDB write time:**

[fact] LanceDB write time is negligible: 0.01s at 10 docs, 0.01s at 100, 0.02s at 500, 0.03s at 1000. Write time is **less than 1% of total rebuild time** at all tested corpus sizes. Source: direct benchmark.

[fact] LanceDB query time (embed query vector + vector search, 5 results, 50-item table): **25ms** end-to-end. Source: direct benchmark.

[inference] The LanceDB write path uses an append-optimized Lance file format (Arrow-based columnar storage); the low write latency reflects efficient columnar serialisation rather than index construction. For tables under ~10,000 rows, LanceDB performs flat (brute-force) vector search, which requires no ANN index build time. Source: LanceDB documentation (docs.lancedb.com/indexing/reindexing).

**Q4 — Total cold-start rebuild times (model load included):**

[fact] Benchmark results on CPU-only GitHub Actions runner (lancedb v0.29.2, sentence-transformers v5.2.3, batch_size=32, synthetic short texts):

| Corpus size | BGE embed | BGE total (incl. load) | MiniLM embed | MiniLM total (incl. load) |
|---|---|---|---|---|
| 10 docs  | 0.34s | 1.02s | 0.17s | 0.67s |
| 50 docs  | 1.60s | 2.28s | 0.82s | 1.32s |
| 100 docs | 3.23s | 3.91s | 1.64s | 2.14s |
| 500 docs | 16.30s | 16.98s | 8.23s | 8.73s |
| 1000 docs | 34.81s | 35.49s | — | ~17.5s (extrapolated) |

Source: direct benchmark.

**Q4a — Actual corpus (61 items, full research item text truncated to 2000 chars):**

[fact] Actual corpus rebuild (61 `.md` files, content truncated to 2000 chars per file): BGE embed = **10.82s**, LanceDB write = 0.004s, total = **10.82s**. With cached model load: **11.50s total**. Source: direct benchmark against `/Research/completed/` directory.

[inference] The actual corpus takes 10.82s to embed 61 items, versus 1.60s for 50 synthetic short texts. This 6.8× slowdown per item is explained by document length: real research items are multi-thousand-character Markdown files containing hundreds of tokens, whereas the synthetic texts were ~50 words. BERT-based models process full token sequences (capped at 512 tokens for bge-small), and longer inputs take proportionally more compute.

**Q5 — Pre-computed embeddings stored as JSON in git:**

[fact] JSON representation size for BGE-small embeddings (384-dimensional float vectors): **7.74 KB per document**. Storage at scale: 100 docs = 0.77 MB, 500 docs = 3.87 MB, 1000 docs = 7.74 MB. Source: direct measurement (json.dumps of numpy float32 vectors).

[fact] Numpy float32 binary storage (same embeddings): **1.5 KB per document** (1536 bytes = 384 dims × 4 bytes). For 1000 docs: 1.5 MB. Source: direct measurement.

[fact] Pre-computed embeddings approach (JSON load from file + LanceDB write, no re-embedding): 10 docs = 0.006s, 100 docs = 0.015s, 500 docs = 0.065s, 1000 docs = 0.130s. Source: direct benchmark.

[inference] Storing embeddings as JSON in git adds ~7.74 MB for 1000 research items. For a personal research corpus (expected max 200–300 items over several years), this is ~1.5–2.3 MB — well within git's practical limits for text files and smaller than most single PDF attachments. Binary numpy format would reduce this by ~5×, but introduces a non-text blob into git and loses human readability.

[assumption] Assumption: The embedding model in the git-stored JSON and the model running at query time must match exactly (same model, same version). Any model upgrade requires regenerating all stored embeddings. Justification: embedding spaces are model-specific; cross-model dot-product similarity is meaningless.

**Q6 — GitHub code search as a zero-rebuild fallback:**

[fact] GitHub REST API code search has a rate limit of **10 requests per minute** for authenticated requests, separate from the general 5,000 requests/hour limit. Source: GitHub Docs (docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api); GitHub Changelog (github.blog/changelog/2023-03-10-changes-to-the-code-search-api/).

[fact] GitHub code search is keyword-based (lexical matching), not semantic. It indexes only the default branch, files below 384 KB, and may return `incomplete_results: true` for large queries. Maximum 100 results per page. Source: GitHub API docs (github.apidog.io/api-3489557).

[inference] GitHub code search is not a viable semantic search fallback. It cannot answer vocabulary-mismatch queries (e.g., "what did I learn about agent memory" when the relevant item uses "context engineering" terminology). It is suitable as a supplementary keyword search layer, not a replacement for vector search.

**Q7 — Document length effect on embedding time:**

[fact] Synthetic 50-word texts: BGE throughput = ~34.5ms/doc. Actual research items (2000-char truncated): BGE throughput = ~177ms/doc (10.82s ÷ 61 items). Source: direct benchmark comparison.

[inference] Real research items are approximately 5× slower to embed than synthetic short texts with the same model and batch size. This is consistent with BERT's O(n²) self-attention cost scaling with sequence length. Truncating input to the first 256 tokens (rather than the 512-token limit) would roughly halve embedding time for long documents.

### §3 Reasoning

The embedding model — not LanceDB — is the bottleneck in every scenario tested. LanceDB write operations account for under 1% of total rebuild time at all corpus sizes. This rules out LanceDB optimisation as a lever for improving cold-start performance.

The question resolves into three distinct deployment models with different viability windows:

**Deployment model 1: Rebuild from text on every cold start.** This is currently the default and works correctly for corpora under ~100 short documents (~4s with BGE-small). For the actual corpus (61 items with full Markdown content), it already exceeds the 5s target at 11.5s. Growth to 100–200 items will push this to 18–35s, making it unsuitable for interactive latency requirements. Switching to MiniLM halves embedding time but does not change the fundamental scaling problem: at 500 items even MiniLM takes ~8.7s.

**Deployment model 2: Pre-computed embeddings in git.** Generate embeddings once per write (as part of `add_memory`), store as JSON alongside `.md` files, rebuild the LanceDB table at startup by reading JSON (not re-running model inference). Cold-start time becomes ~0.1–0.2s regardless of corpus size (dominated by file I/O, not model inference). Git storage cost is ~7.74 KB/doc in JSON, ~1.5 KB in binary numpy. For a personal corpus expected to reach 200–300 items: 1.5–2.3 MB JSON (acceptable). This is the only approach that hits sub-second startup at any corpus size.

**Deployment model 3: Persistent index (current behaviour).** Keep `.lancedb` on disk across invocations. Eliminates startup cost entirely but requires persistent storage, which is incompatible with stateless compute (Cloudflare Workers, Lambda ephemeral environments, GitHub Actions). Compatible with always-on deployments (Fly.io, Raspberry Pi, VPS).

The pre-computed embeddings approach has one critical constraint: any query-time model must produce vectors in the same space as the stored vectors. A model version bump requires a full re-embedding pass before deployment. For a single-owner personal corpus this is a low operational burden (a single `python regen_embeddings.py` run), but it must be explicitly accounted for in the upgrade path.

### §4 Consistency Check

The benchmark results are internally consistent. The 50-item synthetic corpus takes 1.60s with BGE-small (32ms/doc), which scales linearly to 500 items = 16.1s — matching the measured 16.30s (within noise). The actual corpus throughput (177ms/doc) is higher than synthetic throughput (34.5ms/doc) as expected given document length. No contradictions were found across measurements.

One potential inconsistency: MiniLM's cached load time was measured at 0.50s in the second benchmark and 0.503s in the third — these agree. BGE cached load is 0.68s in benchmark 2 and 0.676s in benchmark 3. All figures are stable across repeated measurements.

The GitHub code search rate limit (10 req/min) is corroborated by both GitHub Docs and the GitHub Changelog item from March 2023. No contradictions with other sources.

### §5 Depth and Breadth Expansion

**Technical lens — truncation as a mitigation:** The 5× slower embedding of real research items (vs. synthetic) is due to document length. Truncating input to the first 256–300 tokens before embedding is a standard practice in retrieval systems where the query-relevant content is typically front-loaded (title, abstract, key findings). For research items, the title + executive summary + key findings are the semantically dense sections. Truncating to these sections would reduce embedding time per item from ~177ms to ~50–70ms, bringing a 100-item corpus well under 10s for BGE-small.

**Economic lens — git storage cost:** JSON format at 7.74 KB/doc adds ~1.5 MB for 200 items. Over a 5-year research programme producing 400 items (a high estimate for personal use), this would be ~3 MB added to the git history. Git compresses JSON efficiently (float arrays with many repeated digits compress well with zlib). The binary numpy format reduces this further to ~0.6 MB for 400 items. Neither figure presents a meaningful repository size concern.

**Operational lens — model version management:** Pre-computed embeddings introduce a coupling between stored vectors and the exact model version used. This constraint already exists implicitly (queries must use the same embedding space as the index), but becomes explicit and observable when vectors are committed to git. A migration script (`regen_embeddings.py`) should be a first-class deliverable alongside any embedding model change, and the model name + version should be stored in a sidecar metadata file.

**Comparison with prior research findings on Model2Vec:** The `2026-03-02-semantic-full-text-search.md` item found Model2Vec (potion-base-8M) achieves ~200x CPU speedup vs MiniLM. Applied to the rebuild scenario: at 177ms/doc for real research items with BGE-small, Model2Vec at ~0.9ms/doc would rebuild 500 items in under 1 second — making per-request stateless rebuild viable at any practical corpus size without pre-computed storage. Model2Vec has no PyTorch dependency and loads from a ~30–50 MB model file. This is a stronger alternative than MiniLM for stateless deployment, though it trades some retrieval accuracy (91–93% of MiniLM's MTEB score).

**Serverless cold-start context:** Python Lambda cold starts with heavy dependencies (PyTorch, transformers) are 1.9–2.7s before any model load occurs. LanceDB with lean Python (no LangChain) achieves 400–700ms cold start from a study of AWS Lambda deployments (johal.in). Adding a 0.68s model load on top puts BGE-small at ~1.1–1.4s baseline before any documents are embedded. For pre-computed embeddings, this baseline is the entire startup cost.

### §6 Synthesis

**Executive summary:**

The embedding model is the bottleneck in LanceDB rebuild: LanceDB write operations consume under 1% of total startup time at all tested corpus sizes. BAAI/bge-small-en-v1.5 takes 11.5s to rebuild the current 61-item corpus from full Markdown text (10.8s embedding, 0.68s model load), exceeding the 5s target. Pre-computed embeddings stored as JSON in git reduce startup to under 0.2s regardless of corpus size, making stateless deployment viable at any practical corpus scale. Model2Vec (identified in prior research) would enable per-request rebuild without pre-computed storage at under 1s for 500 items, and should be evaluated as the production embedding model.

**Key findings:**

1. LanceDB write operations take under 30ms even at 1000 documents; the embedding model accounts for 99%+ of cold-start rebuild time.
2. BAAI/bge-small-en-v1.5 loads from disk cache in 0.68s; all-MiniLM-L6-v2 loads in 0.50s.
3. BGE-small embeds at ~34.5ms/doc (synthetic short texts) but ~177ms/doc for real research items — document length dominates due to BERT's O(n²) attention cost.
4. At current corpus size (61 items, full Markdown), cold-start rebuild takes 11.5s with BGE-small — already over the 5–10s target.
5. Pre-computed embeddings in JSON (7.74 KB/doc, 384-dim) load and write to LanceDB in under 0.2s for 1000 documents; this is the only strategy that reliably meets sub-second startup at any corpus size.
6. JSON storage cost is 7.74 MB for 1000 documents; for a personal corpus of 200–300 items this is under 2.5 MB — acceptable in git.
7. MiniLM-L6-v2 is 2× faster than BGE-small for embedding but does not change the fundamental scaling: at 500 real items MiniLM would still take ~20s+ to rebuild.
8. GitHub code search (rate-limited to 10 req/min, keyword-only, max 100 results, possible incomplete results) is not a viable semantic search fallback; it is a supplementary keyword layer only.
9. Model2Vec (potion-base-8M, ~200x faster than MiniLM per prior research) would reduce rebuild time to under 1s for 500 items, enabling per-request stateless rebuild without pre-computed storage.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| LanceDB write <30ms at 1000 docs | Direct benchmark (lancedb v0.29.2) | high | Reproducible; LanceDB write is O(n) columnar append |
| BGE-small cached load = 0.68s | Direct benchmark | high | Consistent across 3 runs |
| MiniLM cached load = 0.50s | Direct benchmark | high | Consistent across 2 runs |
| BGE-small ~34.5ms/doc (synthetic) | Direct benchmark, 10–1000 items | high | Linear scaling confirmed |
| BGE-small ~177ms/doc (real items) | Direct benchmark, 61 items | high | Explains actual corpus latency |
| Actual 61-item corpus = 11.5s cold start | Direct benchmark | high | Measured against /Research/completed/ |
| JSON 7.74 KB/doc at 384 dims | Direct measurement | high | Deterministic from dim count |
| JSON load+write 0.13s at 1000 docs | Direct benchmark | high | Dominated by JSON parse |
| MiniLM 2× faster embedding than BGE | Direct benchmark | high | Consistent across corpus sizes |
| GitHub code search 10 req/min limit | GitHub Docs + GitHub Changelog (Mar 2023) | high | Two independent sources |
| GitHub code search keyword-only | GitHub API docs | high | Official documentation |
| Model2Vec ~200x faster than MiniLM | Research/completed/2026-03-02-semantic-full-text-search.md | high | Prior research item, high-confidence finding |

**Assumptions:**

- **Assumption:** Benchmark environment (GitHub Actions CPU runner) is representative of free-tier deployment targets. **Justification:** GitHub Actions runners use 2-core Intel/AMD CPUs and 7 GB RAM, comparable to Fly.io free tier (1 vCPU / 256 MB) — though the free tier has considerably less RAM, which may slow PyTorch model load.
- **Assumption:** Document length in synthetic benchmarks (50 words) vs. real items (2000-char truncated) captures the realistic range. **Justification:** Research items are structured Markdown with prose; most are under 5000 characters. Truncation to 2000 chars reflects the semantically dense portion.
- **Assumption:** Pre-computed JSON embeddings would be committed alongside `.md` files as part of the `add_memory` write path. **Justification:** This is the natural implementation; the alternative (separate batch job) introduces synchronisation complexity.

**Analysis:**

The benchmark results resolve the research question unambiguously: rebuild from text is not viable for per-request stateless deployment at the current corpus size and above. The 5s target is already exceeded with 61 real items (11.5s), and the corpus will only grow. The switching cost between rebuild strategies is low — both pre-computed JSON and Model2Vec are code changes confined to the `mcp_server.py` write path — so the deployment model should shift now rather than after the corpus grows further.

Pre-computed embeddings are the most conservative and immediately viable solution. They eliminate the embedding bottleneck entirely, are model-agnostic at query startup time (only the stored vectors matter), and have a predictable storage cost. The main operational cost is the model-version coupling, which is manageable at personal-project scale.

Model2Vec represents the more elegant long-term solution: it removes the need for pre-computed storage while enabling sub-second rebuild. The prior research item (`2026-03-02-semantic-full-text-search.md`) recommends Model2Vec for Phase 2 of the search system, which aligns with this finding. However, Model2Vec has not been benchmarked against LanceDB specifically in this item — that is an open gap.

**Risks, gaps, uncertainties:**

- Model2Vec's actual rebuild time against real research item text has not been directly measured; the 200× speedup figure is from MTEB benchmarking contexts and may vary with document structure and length.
- The benchmark was run on a GitHub Actions runner, not on a Fly.io free tier (1 vCPU, 256 MB RAM). Memory-constrained environments may experience additional latency loading PyTorch and the model weights.
- JSON embedding storage in git has not been tested with the actual `add_memory` write path; the integration requires a code change that is outside scope for this research item.
- LanceDB v0.29.2 may have different performance characteristics from earlier or later versions; results should be re-validated if the version changes significantly.

**Open questions:**

1. What is Model2Vec (potion-base-8M) actual rebuild time for the current 61-item research corpus? This would confirm whether per-request rebuild becomes viable without pre-computed storage.
2. What is the memory footprint of Model2Vec vs. bge-small on a Fly.io 256 MB instance? RAM is more constrained than CPU on free tiers.
3. Should embeddings be stored as JSON (human-readable, 5× larger) or numpy binary in git? The answer depends on whether the embedding files need to be readable/diffable in the git web UI.
4. How should the `add_memory` write path be modified to compute and persist embeddings alongside the `.md` file? This is the implementation question for W-0015 in the Memory-System backlog.

### §7 Recursive Review

All sections contain substantive content. Every claim in §2 is labelled [fact], [inference], or [assumption]. Every [fact] has a source (direct benchmark, official docs, or prior research). The evidence map in §6 covers all nine key findings. The three assumptions are explicitly stated in §6 and trace to §2. Contradictions: none found (§4). Open questions (§5, §6) are scoped to items genuinely outside this research's scope. The key recommendation (pre-computed embeddings as immediate solution, Model2Vec as the next investigation) is directly supported by the benchmark data and prior research.

One limitation: the "200× faster" claim for Model2Vec is sourced from prior research rather than direct measurement in this item. It is labelled [high confidence] in the evidence map because the prior item is itself a high-confidence completed research item with primary sources. A Model2Vec benchmark against LanceDB remains an open gap.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

The embedding model — not LanceDB — is the bottleneck in cold-start index rebuilds: LanceDB write operations consume under 1% of total startup time at all tested corpus sizes. BAAI/bge-small-en-v1.5 takes 11.5s to rebuild the current 61-item research corpus from Markdown text (10.8s embedding, 0.68s model load), already exceeding the 5–10s target. Pre-computed embeddings stored as JSON in git reduce startup to under 0.2s regardless of corpus size, making stateless deployment viable immediately. Model2Vec (identified in prior semantic-search research as ~200× faster than MiniLM on CPU) would enable per-request rebuild without pre-computed storage and should be evaluated as the production embedding model.

### Key Findings

1. LanceDB write operations take under 30ms even at 1000 documents; the embedding model accounts for 99%+ of cold-start rebuild time at every tested corpus size. [high]

2. BAAI/bge-small-en-v1.5 loads from disk cache in 0.68s; the model file is 133 MB, giving a first-download load time of ~2.25s from HuggingFace Hub on a typical connection. [high]

3. BGE-small-en-v1.5 embeds at ~34.5ms/doc for short synthetic texts but ~177ms/doc for real research items; BERT's O(n²) attention cost means document length — not document count — is the primary driver of embedding time. [high]

4. At the current corpus size of 61 items with full Markdown text, cold-start rebuild takes 11.5s with BGE-small, already exceeding the 5–10s target and with no improvement path as the corpus grows. [high]

5. Pre-computed embeddings stored as JSON in git (7.74 KB per 384-dim document) load and write into LanceDB in under 0.2s for 1000 documents, making startup time effectively O(1) with respect to corpus size. [high]

6. JSON storage cost for pre-computed BGE-small embeddings is 7.74 MB for 1000 documents; for a personal research corpus of 200–300 items, this is under 2.5 MB, an acceptable git repository size. [high]

7. all-MiniLM-L6-v2 is approximately 2× faster than BGE-small at embedding (16.4ms/doc vs 34.5ms/doc for short texts) but does not change the fundamental scaling failure: at 500 real research items, MiniLM would still require over 20s to rebuild. [high]

8. GitHub code search is rate-limited to 10 requests per minute, is keyword-only with no semantic understanding, and may return incomplete results for large queries; it is not a viable replacement for vector search and only useful as a supplementary lexical search layer. [high]

9. Model2Vec (potion-base-8M), identified in prior semantic-search research as ~200× faster than MiniLM on CPU with 91–93% of MiniLM's MTEB accuracy and no PyTorch dependency, would reduce rebuild time to under 1s for 500 items — making per-request stateless rebuild viable without pre-computed embedding storage. [medium — requires direct LanceDB benchmark to confirm]

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| LanceDB write <30ms at 1000 docs | Direct benchmark, lancedb v0.29.2 | high | Reproducible; O(n) columnar append |
| BGE-small cached load = 0.68s | Direct benchmark | high | Consistent across 3 measurements |
| MiniLM cached load = 0.50s | Direct benchmark | high | Consistent across 2 measurements |
| BGE-small ~34.5ms/doc (synthetic) | Direct benchmark, 10–1000 items | high | Linear scaling confirmed across range |
| BGE-small ~177ms/doc (real items) | Direct benchmark, 61 items | high | 5× slowdown explained by doc length |
| Current 61-item corpus = 11.5s cold start | Direct benchmark | high | Measured against Research/completed/ |
| JSON 7.74 KB/doc at 384 dims | Direct measurement | high | Deterministic from float32 × 384 dims |
| JSON load+write 0.13s at 1000 docs | Direct benchmark | high | Dominated by JSON parse |
| MiniLM 2× faster embedding than BGE | Direct benchmark | high | Consistent across all corpus sizes |
| GitHub code search 10 req/min limit | GitHub Docs; GitHub Changelog Mar 2023 | high | Two independent authoritative sources |
| GitHub code search keyword-only | GitHub API docs (github.apidog.io) | high | Official documentation |
| Model2Vec ~200× faster than MiniLM | Research/completed/2026-03-02-semantic-full-text-search.md | high | Prior research; primary MTEB benchmarks cited |

### Assumptions

- **Assumption:** GitHub Actions runner hardware is representative of free-tier deployment targets. **Justification:** GitHub Actions 2-core runners are comparable to Fly.io free tier CPU; RAM (7 GB vs 256 MB) differs and may slow PyTorch model load on memory-constrained targets.
- **Assumption:** Document content truncated to 2000 characters per file represents a reasonable upper bound for embedding input length in this corpus. **Justification:** Research items are structured Markdown; semantic content is front-loaded in title, executive summary, and key findings.
- **Assumption:** Pre-computed JSON embeddings would be committed alongside `.md` files as part of the `add_memory` write path. **Justification:** The natural implementation; any other approach (separate batch job) introduces synchronisation complexity between stored files and their embeddings.

### Analysis

The benchmark data makes a clear recommendation. The rebuild-from-text approach fails the target at the current corpus size and degrades further as the corpus grows — there is no configuration of the current stack (batch size, model choice within bge/MiniLM family) that fixes this without switching to a fundamentally faster embedding approach.

Pre-computed embeddings eliminate the bottleneck at the cost of a model-version coupling constraint (all stored embeddings must be regenerated if the model changes). For a single-owner personal project, this cost is low and manageable. The storage overhead (~2.5 MB for 300 items) is negligible in git terms.

Model2Vec represents a possible third path — one that avoids both the storage overhead of pre-computed embeddings and the latency of bge-small/MiniLM. Given that prior research already recommends Model2Vec for Phase 2 of the semantic search system, evaluating it for the LanceDB rebuild path simultaneously would be efficient. The recommendation is to pursue both paths in parallel: implement pre-computed embeddings as the near-term fix (eliminates the latency problem immediately), and benchmark Model2Vec against LanceDB as an input to the production embedding model decision.

### Risks, Gaps, and Uncertainties

- Model2Vec's rebuild time in the LanceDB context has not been directly benchmarked; the 200× speedup is well-sourced but measured in a different evaluation context.
- Fly.io free tier (1 vCPU, 256 MB RAM) may exhibit worse model load times than the GitHub Actions runner due to RAM pressure during PyTorch initialisation.
- The pre-computed JSON approach requires a code change to `mcp_server.py` that is not implemented; the benchmark demonstrates feasibility, not production readiness.
- JSON float precision (default Python repr) may introduce minor rounding differences vs the model's native float32 output; this is unlikely to affect retrieval quality but has not been tested.

### Open Questions

1. What is Model2Vec (potion-base-8M) actual rebuild time for the current 61-item research corpus? Should become a backlog item for the Memory-System.
2. Should embeddings be stored as JSON (human-readable, diffable in GitHub web UI) or numpy binary (5× smaller)? Decision depends on operational tooling preferences.
3. How should the `add_memory` write path in `mcp_server.py` be modified to persist embeddings as a JSON sidecar alongside each `.md` file? This is the concrete implementation question for W-0015.
4. What is the RAM footprint of Model2Vec on a 256 MB Fly.io instance during inference?

---

## Output

- Type: knowledge, backlog-item
- Description: Concrete benchmarks establishing that LanceDB write is never the bottleneck; bge-small-en-v1.5 cold-start rebuild already exceeds the 5–10s target at 61 items; pre-computed JSON embeddings in git reduce startup to <0.2s at any corpus size; Model2Vec warrants evaluation as the production embedding model for the LanceDB rebuild path.
- Links:
  - https://lancedb.github.io/lancedb/ (LanceDB documentation)
  - https://huggingface.co/BAAI/bge-small-en-v1.5 (BGE-small model card)
  - https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api (GitHub API rate limits)