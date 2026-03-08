# 2026-03-08 — Research Loop (lancedb-index-rebuild-from-git)

**Completed:**

Research item:
- `Research/completed/2026-03-08-lancedb-index-rebuild-from-git.md` — completed; the embedding model (not LanceDB) is the bottleneck, consuming 99%+ of rebuild time. At the current 61-item corpus with full Markdown text, BGE-small cold-start rebuild takes 11.5s, already exceeding the 5–10s target. Pre-computed JSON embeddings in git (7.74 KB/doc, load+write in <0.2s at 1000 docs) are the recommended near-term solution; Model2Vec warrants evaluation as the production embedding model.

Sources consulted:
- https://lancedb.github.io/lancedb/ (LanceDB Python API reference)
- https://huggingface.co/BAAI/bge-small-en-v1.5 (BGE-small-en-v1.5 model card)
- https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api (GitHub REST API rate limits)
