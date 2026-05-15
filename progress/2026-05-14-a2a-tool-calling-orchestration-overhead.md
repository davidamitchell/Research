# 2026-05-14 -- Research Loop (a2a-tool-calling-orchestration-overhead)

**Completed:**

Research item:
- `Research/completed/2026-05-13-a2a-tool-calling-orchestration-overhead.md` -- completed; the item concludes that tool-calling is usually the lower-overhead default for internal hierarchical delegation, while a dedicated Agent-to-Agent (A2A) layer is justified mainly when remote agents need independent interoperability, asynchronous task state, or governance boundaries. It also finds that current public evidence supports the overhead conclusion more strongly than the reasoning-accuracy conclusion, because planning and topology benchmarks are available but a direct A2A-versus-tool benchmark was not found.

Sources consulted:
- https://a2a-protocol.org/latest/specification/ (A2A protocol mechanics, task model, Agent Card, and interoperability scope)
- https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents (official guidance on coordination cost, latency, and when multi-agent boundaries are justified)
- https://openreview.net/forum?id=Oljnxmf4pc (benchmark evidence separating planning quality from function-execution quality)

## Mini-Retro

1. **Did the process work?** Yes. The workflow surfaced citation-scope and confidence-calibration problems early enough to tighten the claims before final completion.
2. **What slowed down or went wrong?** The public evidence base is stronger on adjacent orchestration trade-offs than on direct A2A-versus-tool comparisons, so confidence had to be trimmed after review.
3. **What single change would prevent this next time?** Nothing beyond the existing review loop; it already caught the only overstatements that mattered.
4. **Is this a pattern?** Yes. It matches the existing pattern that synthesis claims often need narrower wording and lower confidence than first-pass drafting suggests.
