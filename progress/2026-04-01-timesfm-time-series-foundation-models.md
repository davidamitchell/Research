# 2026-04-01 -- Research Loop (timesfm-time-series-foundation-models)

**Completed:**

Research item:
- `Research/completed/2026-04-01-timesfm-time-series-foundation-models.md` -- completed; TimesFM is Google's 200 M-parameter decoder-only transformer pretrained on 100B+ time points, achieving near-supervised-model zero-shot accuracy across retail, energy, traffic, healthcare, and financial domains. A competitive TSFM landscape has emerged (Chronos, MOIRAI-2, Lag-Llama, UniTS) with no single dominant architecture. GFMs for graph and tree data are less mature because graphs lack a natural tokenisation unit equivalent to sequence patching.

Sources consulted:
- https://arxiv.org/abs/2310.10688 (TimesFM primary paper: Das et al. 2024)
- https://arxiv.org/abs/2403.07815 (Chronos primary paper: Ansari et al. 2024)
- https://github.com/google-research/timesfm/ (TimesFM GitHub repository)
- https://docs.cloud.google.com/bigquery/docs/timesfm-model (BigQuery ML TimesFM documentation)
- https://research.google/blog/a-decoder-only-foundation-model-for-time-series-forecasting/ (Google Research Blog)
- https://github.com/microsoft/ProbTS/blob/main/docs/benchmark/foundation_model/README.md (ProbTS TSFM benchmarking)
- https://proceedings.neurips.cc/paper_files/paper/2024/hash/c23ccf9eedf87e4380e92b75b24955bb-Abstract-Conference.html (GFT NeurIPS 2024)
- https://research.google/blog/graph-foundation-models-for-relational-data/ (Google GFM for relational data)
- https://arxiv.org/abs/2505.15116 (GFM Comprehensive Survey 2025)

## Mini-Retro

1. **Did the process work?** Yes. The §0-§7 structure provided clear scaffolding for covering all three sub-questions (use cases, competing models, graphs/trees) without losing focus. The acronym expansion audit at §7 caught ARIMA and GARCH, which could have failed review.
2. **What slowed down or went wrong?** No direct arXiv paper for MOIRAI-2 was found; architecture details had to be drawn from Hugging Face model cards and secondary sources. The confidence level for MOIRAI-2 claims is therefore medium rather than high.
3. **What single change would prevent this next time?** For models where an arXiv paper is cited in secondary sources but not easily located, explicitly note in §2 that a primary paper was searched for but not found, rather than leaving it implicit in the confidence column.
4. **Is this a pattern?** Yes -- this matches the pattern of secondary sources claiming a primary paper exists for a model without providing the DOI or arXiv number. This has occurred before in TSFM comparisons. Mitigation: always record the search query and "not found" outcome explicitly in §2.
