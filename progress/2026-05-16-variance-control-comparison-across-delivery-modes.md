# 2026-05-16 -- Complete research item (variance-control-comparison-across-delivery-modes)

**Completed:**
- `Research/completed/2026-05-16-variance-control-comparison-across-delivery-modes.md` — completed the comparison between build-mode AI-assisted code and do-mode agent-executed business processes, concluding that public evidence supports a directional inference rather than a head-to-head measured failure-rate distribution.
- `learnings.md` — updated Thread 1 to capture the new comparative-delivery evidence that release gates filter more variance before impact than live agent execution.

**Most important sources:**
- [Google Site Reliability Engineering (SRE) Book: Testing Reliability](https://sre.google/sre-book/testing-reliability/)
- [DevOps Research and Assessment (DORA) (2024) Accelerate State of DevOps Report 2024](https://dora.dev/research/2024/dora-report/)
- [Zhou et al. (2024) WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854)

## Mini-Retro

1. **Did the process work?** Yes. The draft-review loop surfaced the remaining overstrong comparative claims early enough to tighten them before completion.
2. **What slowed down or went wrong?** The review workflow can finish operationally even when the log still contains real violations, so the log had to be treated as the actual review result.
3. **What single change would prevent this next time?** Make every cross-mode comparison default to `[inference]` unless one source directly makes the comparison, instead of tightening that only after review.
4. **Is this a pattern?** Yes. Comparative synthesis claims repeatedly arrive too fact-shaped on first pass when the evidence base is proxy-heavy rather than directly head-to-head.
5. **Does any documentation need updating?** No additional documentation update is needed beyond the `learnings.md` thread update already made in this session.
6. **Do the default instructions need updating?** Not yet. The existing review guidance already warned against overclaiming comparative synthesis; this session reinforced that rule rather than revealing a new one.
