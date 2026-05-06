# 2026-05-06 — Add fact-checking and Barnum statements research backlog items (fact-checking-barnum-backlog-intake)

**Completed:**

- `Research/backlog/2026-05-06-openfactcheck-ai-fact-checking-pipeline.md` — added from issue; asks what the architecture and practical applicability of OpenFactCheck is as an automated, claim-level fact-checking pipeline; priority high; blocks synthesis item
- `Research/backlog/2026-05-06-loki-fact-checking-journalists-moderation.md` — added from issue; asks what capabilities, architectural assumptions, and deployment constraints Loki has as an MIT-licensed fact-checking tool for journalists and content moderators; priority high; blocks synthesis item
- `Research/backlog/2026-05-06-factscore-precision-scoring-atomic-claims.md` — added from issue; asks how FActScore (Factual precision Scoring) operationalises atomic-level factual precision scoring for large language model (LLM) outputs and what its cross-domain performance characteristics are; priority high; blocks synthesis item
- `Research/backlog/2026-05-06-gpt-oss-safeguard-policy-enforcement-open-weight.md` — added from issue; asks how open-weight policy enforcement reasoning models (exemplified by gpt-oss-safeguard) classify text against customisable policies and what their deployment trade-offs are; priority high; blocks synthesis item
- `Research/backlog/2026-05-06-barnum-statements-ai-responses-theory-practice.md` — added from issue; asks what Barnum statements (Forer Effect statements) are, how they manifest in AI-generated text, and what methods exist to identify and remove them from research outputs; priority high; blocks synthesis item
- `Research/backlog/2026-05-06-fact-checking-tools-research-quality-improvement.md` — added from issue; synthesis item asking how findings from the above five items can be synthesised into concrete improvements to the automated review process in this repository; priority medium; cites all five prerequisite items; must not start until all five are complete

**Addressing:** GitHub issue requesting new research backlog items on OpenFactCheck, Loki, FActScore, gpt-oss-safeguard, Barnum statements, and a synthesis question on improving research review quality.

**Dependency graph established:**
- Items 1–5 (OpenFactCheck, Loki, FActScore, gpt-oss-safeguard, Barnum) each carry `blocks: [2026-05-06-fact-checking-tools-research-quality-improvement]`
- Synthesis item (item 6) carries `cites:` and `related:` pointing to all five prerequisite items
- All six items carry `related:` cross-references to each other

**Checks run:**
- `make check` — passed (ruff lint + format clean)
- `python -m pytest tests/ -q` — 411 passed, 1 pre-existing failure (TAVILY_API_KEY not set in sandbox environment; unrelated to this change)

## Mini-Retro

1. **Did the process work?** Yes. The issue provided a clear list of five tools/topics plus an explicit synthesis question, which mapped cleanly onto six backlog items. The theory-first, synthesis-last ordering follows the same pattern used for the AIBOM series and is well-supported by the `blocks:` dependency field.

2. **What slowed down or went wrong?** Nothing significant. The main decision work was in scoping each item to a single answerable question — particularly for gpt-oss-safeguard (potential model name disambiguation required) and Loki (multiple tools share this name; the item's approach section explicitly flags this risk). Sources required care: the FActScore and OpenFactCheck items share several common sources, which were handled by including them in the relevant item only.

3. **What single change would prevent this next time?** Nothing material to change. The constraint note in the synthesis item ("This item must not start until all five prerequisite items are completed") is intentional belt-and-suspenders beyond the `blocks:` field, given that the blocks field only marks individual pairwise dependencies and does not currently enforce "all of the above must be complete before this starts".

4. **Is this a pattern?** Yes — the "five tools + one synthesis" structure is a clean, recurring intake pattern for multi-tool investigation series. The AIBOM series used the same approach (theory items block practice items; one cross-cutting synthesis item at the end). The format works.

5. **Does any documentation need updating?** No. This is purely new backlog content with no changes to existing code, prompts, or documentation.

6. **Do the default instructions need updating?** No new conventions emerged from this session.
