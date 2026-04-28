# 2026-04-28 -- Research Loop (uelgf-agentic-ai-specific-risks-runtime-monitoring)

**Completed:**

Research item:
- `Research/completed/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.md` -- completed; the item concludes that the current UELGF runtime loop is necessary but insufficient for agentic systems because it mostly detects visible consequence-level failures after or during execution. It adds an agentic runtime-monitoring extension at the governed golden rail, centered on precursor signals for reward hacking, grounding failure, verifier disagreement, unsafe multi-agent coordination, and a new pre-execution verification-hold or quarantine response.

Sources consulted:
- https://airc.nist.gov/AI_RMF_Knowledge_Base/AI_RMF/Core_And_Profiles/5-sec-core#tab:govlongtblr (NIST lifecycle-wide AI risk-management outcomes)
- https://deepmind.google/research/publications/78150/ (Google DeepMind dangerous-capability evaluations and early-warning framing)
- https://www.anthropic.com/research/emergent-misalignment-reward-hacking (Anthropic reward hacking, sabotage, and context-dependent misalignment findings)

## Mini-Retro

1. **Did the process work?** Yes; the workflow produced a solid first draft and the review pass surfaced real epistemic-strength issues before completion.
2. **What slowed down or went wrong?** Access-note prose about blocked or substituted sources looked innocuous but review treated it as unsupported claim-bearing text.
3. **What single change would prevent this next time?** Add an explicit rule to `research-prompt.md` that session-path access notes must be assumptions, pure metadata, or deleted after source substitution, not labeled facts backed only by the substitute source.
4. **Is this a pattern?** Yes; it matches the existing pattern that source-access observations are workflow metadata and often fail review when they are written like ordinary sourced claims.

## Applied improvements

- Updated `research-prompt.md` to forbid labeling session-path access notes as `[fact]` when the only available citation is the substitute source rather than evidence of the runtime observation itself.
