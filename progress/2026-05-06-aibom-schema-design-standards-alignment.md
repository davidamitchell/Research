# 2026-05-06 -- Research Loop (aibom-schema-design-standards-alignment)

**Completed:**

Research item:
- `Research/completed/2026-05-06-aibom-schema-design-standards-alignment.md` -- completed; the item concludes that the minimal declared AI bill-of-materials schema should stay inside CycloneDX and SPDX rather than fork them, with CycloneDX as the near-term serialization target and an SPDX extension profile as the cleaner long-term formalization path. It identifies a six-property agentic extension layer, semantic class, mutability, determinism, context binding, snapshot strategy, and approval-scope reference, and provides a worked schema example covering model, prompt, retrieval snapshot, memory schema, tool manifest, and orchestration config.

Sources consulted:
- https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json (CycloneDX reference schema and extension surfaces)
- https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/ (SPDX AI package class and package-centric limits)
- https://arxiv.org/abs/2510.07070 (AIBOM standards-extension experience report)

## Mini-Retro

1. **Did the process work?** Yes, the research-review loop caught a few precision problems, and the standards sources were strong enough to converge on a concrete schema design.
2. **What slowed down or went wrong?** The review workflow auto-pass path still reported substantive violations in the logs, so the item needed manual log inspection and a final polish even after `review_count` reached 2.
3. **What single change would prevent this next time?** Add an explicit pre-draft check in `research-prompt.md` that first-use domain terms such as "AIBOM", "RAG", and "agentic" must either be source-linked on first use or rewritten into plain language before the first review run.
4. **Is this a pattern?** Yes, it matches the known pattern that citation-discipline failures and review-log-only failures recur even when the workflow conclusion looks successful.

## Applied improvements

- Extended `learnings.md` Thread 19 with the schema-design corollary that authoritative AI knowledge supply chains need a standards-aligned declared graph, not only a conceptual one.
- Updated `research-prompt.md` to require an explicit first-use source-link or plain-language rewrite for recurring domain terms such as "AIBOM", "RAG", and "agentic workloads" before the first review run.

## Pending skill improvements

- Mirror the new first-use domain-term rule into the `research` and `citation-discipline` skill guidance in the Skills submodule, since those checks currently surface too late in the workflow.
