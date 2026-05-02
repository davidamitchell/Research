# 2026-05-02 -- Research Loop (terminal-bench-minimal-coding-agent-benchmarks)

**Completed:**

Research item:
- `Research/completed/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.md` -- completed; the item concludes that TerminalBench shows harness design materially affects coding-agent outcomes, but the public evidence does not support the stronger claim that minimal terminal-native harnesses consistently beat richer native harnesses. The strongest supported design rule is minimal-by-default and explicit-by-exception: keep the core terminal interaction surface small and inspectable, then justify richer helpers with measured gains on the target workload.

Sources consulted:
- https://arxiv.org/abs/2601.11868 (Terminal-Bench paper and benchmark mechanics)
- https://www.tbench.ai/leaderboard/terminal-bench/2.0 (public leaderboard rows for richer-versus-minimal harness comparisons)
- https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/ (practitioner argument about tool-surface overhead and direct shell use)

## Mini-Retro

1. **Did the process work?** Yes, the research loop and review workflow surfaced the remaining epistemic-label and confidence mismatches before completion.
2. **What slowed down or went wrong?** The review rubric is stricter than "official source equals high confidence," so several benchmark-mechanics claims needed confidence downgrades and inference relabeling late in the loop.
3. **What single change would prevent this next time?** Add an earlier explicit check that high confidence requires multiple independent sources, even when the underlying source is official.
4. **Is this a pattern?** Yes, it matches the repo's known pattern about confidence-evidence alignment for synthesis claims, so no new recurring-pattern entry is needed.
