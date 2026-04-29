# 2026-04-29 -- Research Loop (knowledge-scaffolding-context-engineering)

**Completed:**

Research item:
- `Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md` -- completed; the item finds that "knowledge scaffolding" is not a stable mainstream term in current agent-engineering literature, even though the underlying practices are well established. The durable pattern is to name concrete mechanisms directly, such as retrieval, memory selection, progressive disclosure, compaction, note-taking, and context isolation, while reserving scaffolding language as a loose explanatory umbrella.

Sources consulted:
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (definition of context engineering and concrete staging patterns)
- https://www.langchain.com/blog/context-engineering-for-agents (mechanism taxonomy: write, select, compress, isolate)
- https://doi.org/10.30191/ets.202404_27(2).rp08 (direct "knowledge scaffolding" usage in pedagogical-agent literature)

## Applied improvements

- Updated `research-prompt.md` so self-review now states that first-use expansions and domain-term definitions must appear in audited prose, not only in `## Sources`.
- Updated `research-prompt.md` so Key Findings examples explicitly include epistemic labels, for example `([inference]; high confidence; source: URL)`.

## Mini-Retro

1. **Did the process work?** Yes, the research loop worked end to end once the item was fully populated and mirrored between `§6 Synthesis` and `## Findings`.
2. **What slowed down or went wrong?** The review checker is stricter than the older prompt examples about first-use definitions in prose and about epistemic labels inside Key Findings, so the first two review passes surfaced formatting-quality issues rather than evidence gaps.
3. **What single change would prevent this next time?** Make the self-review examples match the checker exactly for Key Findings labels and first-use term definitions in visible prose.
4. **Is this a pattern?** Yes, it matches the known recurring pattern that citation-discipline failures often come from acronym or terminology expansion gaps on first use, so tightening the prompt examples was warranted.
