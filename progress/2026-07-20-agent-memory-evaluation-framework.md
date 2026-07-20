# 2026-07-20 -- Research Loop (agent-memory-evaluation-framework)

**Completed:**

Research item:
- `Research/completed/2026-07-20-agent-memory-evaluation-framework.md` -- completed; found that no single existing public benchmark (LongMemEval, LoCoMo, MemoryAgentBench, GraphRAG-Bench) or production system measures agentic memory quality across recall, freshness, conflict resolution, provenance, governance, and downstream task outcome together. Provenance fidelity and governance correctness (adversarial scoping tests) are demonstrated only in GitHub Copilot's production memory system, not in any academic benchmark reviewed. A decision-useful evaluation framework must combine a fixed recall/reasoning dataset, an incremental conflict-resolution benchmark, a provenance-verification check, an adversarial governance stress test, and live task-outcome measurement.

Sources consulted:
- https://arxiv.org/abs/2410.10813 (LongMemEval paper abstract; five core memory abilities)
- https://github.com/snap-research/LoCoMo (LoCoMo dataset repository README)
- https://github.com/GraphRAG-Bench/GraphRAG-Benchmark (GraphRAG-Bench repository; corrected from the seeded dead `microsoft/graphrag-bench` URL)
- https://arxiv.org/abs/2506.05690 (GraphRAG-Bench paper abstract)
- https://arxiv.org/abs/2511.08242 (Outcome-Oriented, Task-Agnostic evaluation paper; PDF body not renderable, corroborated via secondary summary)
- https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/ (production memory system: citation verification, adversarial stress testing, A/B test results)
- https://arxiv.org/abs/2507.05257 (MemoryAgentBench paper; added during investigation, not in the original seed list)
- https://aclanthology.org/W04-1013/ (ROUGE metric definition source; added during self-review to satisfy citation-discipline's domain-term-link requirement)

## Mini-Retro

1. **Did the process work?** Yes. Prior-work cross-reference, decomposition, evidence gathering, and the self-review checklist all ran as designed. The two-pass review cycle worked exactly as specified: pass 1 caught real fact/inference label-mismatch violations between §2 Investigation and the Findings mirror, I fixed them, and pass 2 auto-passed per the review cap.
2. **What slowed down or went wrong?** The seeded `github.com/microsoft/graphrag-bench` Source URL was dead (404); the real repository is under a different organisation (`GraphRAG-Bench/GraphRAG-Benchmark`). The `arxiv.org/pdf/2511.08242` fetch returned raw PDF bytes rather than text, forcing reliance on a secondary web-search summary for that one source. Two review passes were needed: pass 1 flagged five real violations (a `[fact]` label in a Key Finding that was more interpretive than the identical `[inference]`-labeled claim in the source `§2 Investigation` sentence, repeated four times across different Key Findings, plus one near-verbatim repeated sentence in Analysis).
3. **What single change would prevent this next time?** When writing Key Findings that summarize a multi-clause `§2 Investigation` sentence, split the summary into the same fact/inference clause boundaries as the source sentence rather than collapsing the whole clause into one label. Collapsing an interpretive clause into the same `[fact]` label as its supporting factual clause is the recurring failure this session hit four times in one pass.
4. **Is this a pattern?** Yes, a new instance of the "epistemic label mismatch between §2 Investigation and the Findings mirror" class already present in this repository's Known Recurring Failure Patterns table, but the specific sub-pattern here (a Key Finding merges a source-supported clause and an interpretive/derived clause under one label, when the identical content in §2 already correctly split them into two labeled sentences) is precise enough to warrant its own table row. Added below under Applied Improvements.

## Applied improvements

Added a new row to the Known Recurring Failure Patterns table in `.github/copilot-instructions.md`: when a Key Finding mirrors a `§2 Investigation` sentence that itself splits a factual clause from an interpretive clause with two different labels, the Findings mirror must preserve that same two-sentence, two-label split rather than merging both clauses under a single label matching only the stronger one.

## Pending skill improvements

None identified beyond the instructions-file update above; no change to `.github/skills/research/SKILL.md` or `.github/skills/citation-discipline/SKILL.md` appears necessary since the existing rules already require inline label binding per sentence, this session's violations were an execution gap (collapsing two already-correctly-labeled §2 sentences into one Key Finding sentence), not a rule gap.
