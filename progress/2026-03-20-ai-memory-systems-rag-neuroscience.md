# 2026-03-20 — Research Loop (ai-memory-systems-rag-neuroscience)

**Completed:**

Research item:
- `Research/completed/2026-03-17-ai-memory-systems-rag-neuroscience.md` — completed; the item concludes that current vendor memory features are scoped continuity aids rather than full durable-memory architectures, that GitHub Copilot currently has the clearest official answer to memory staleness through citation-backed verification, and that a stronger long-term design combines rationale-preserving episodic capture with semantic consolidation, context-sensitive retrieval, and governed revision.

Sources consulted:
- https://zakelfassi.com/how-do-you-want-to-remember (seed framing article and empirical rationale-recall example)
- https://docs.github.com/en/copilot/concepts/agents/copilot-memory (official GitHub Copilot Memory design and retention model)
- https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2023.1217093/full (memory stages, consolidation, reconsolidation, and cue-dependent retrieval)

## Mini-Retro

1. **Did the process work?** Yes. The queue selection, item start/draft/complete commands, and review workflow loop all worked end to end.
2. **What slowed down or went wrong?** The review workflow passed operationally but still surfaced citation-discipline violations, and the quality-review step itself took several minutes per pass.
3. **What single change would prevent this next time?** Tighten the default research-item template and prompt so `## Findings` always carries explicit epistemic labels and inline source URLs on the first draft.
4. **Is this a pattern?** Yes. Review failures continue to cluster around citation discipline and first-pass formatting of findings, which matches the known recurring review pattern in the repository instructions.
