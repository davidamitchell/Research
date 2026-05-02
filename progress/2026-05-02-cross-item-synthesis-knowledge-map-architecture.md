# 2026-05-02 -- Research Loop (cross-item-synthesis-knowledge-map-architecture)

**Completed:**

Research item:
- `Research/completed/2026-05-02-cross-item-synthesis-knowledge-map-architecture.md` -- completed; the item recommends a hybrid file-based architecture that separates deterministic structure generation from selective Large Language Model (LLM) synthesis. The recommendation centers on graph JSON plus a Data-Driven Documents (D3) map for navigation, summary and cluster artifacts for retrieval, scheduled distillation for active insight generation, and `workflow_dispatch` synthesis for ad hoc questions.

Sources consulted:
- https://arxiv.org/abs/2402.14207 (STORM multi-perspective synthesis method)
- https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/ (document-summary retrieval pattern)
- https://d3js.org/d3-force/simulation (static force-layout graph rendering guidance)

## Mini-Retro

1. **Did the process work?** Yes. The review loop caught a few citation-discipline and confidence-calibration issues, but the core architecture recommendation held through all passes.
2. **What slowed down or went wrong?** Two avoidable review failures: I initially treated `§0 Initialise` status lines as ordinary prose instead of fragment-only metadata, and I missed `D3` in the acronym audit.
3. **What single change would prevent this next time?** Add `D3` to the acronym checklist and explicitly tell future sessions to write `§0` status lines as fragment-only metadata such as `Question: ...` and `Scope: ...`.
4. **Is this a pattern?** Yes. The acronym miss matches the existing recurring review-failure pattern, and the `§0` metadata issue looks like a narrower variant of the same citation-discipline class.

## Applied improvements

- Updated `research-prompt.md` to add `D3` to the acronym checklist.
- Updated `research-prompt.md` to state that `§0` workflow-metadata lines should be written as pure metadata fragments such as `Question: ...`, `Scope: ...`, and `Constraints: ...`.

## Pending skill improvements

- Mirror the new `D3` acronym example and the `§0` fragment-only metadata reminder into `.github/skills/research/SKILL.md` when the skills submodule is available again.
