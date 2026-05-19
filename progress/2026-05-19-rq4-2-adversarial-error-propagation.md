# 2026-05-19 -- Research Loop (rq4-2-adversarial-error-propagation)

**Completed:**

Research item:
- `Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md` -- completed; the item concludes that adversarial inputs propagate mainly by corrupting the loop state reused by later strategy and verification steps, so generic same-model verification is not an independent check. It formalises the result as an amplification process where path-dependent branching, tool use, and memory preserve or grow semantic error unless an external verifier or control layer removes it.

Sources consulted:
- https://arxiv.org/abs/2302.12173 (foundational indirect prompt-injection paper)
- https://arxiv.org/abs/2310.01798 (intrinsic self-correction limits)
- https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/ (cross-session memory-poisoning proof of concept)

## Mini-Retro

1. **Did the process work?** Yes. The review loop caught a handful of overstated comparative claims, but the evidence base and formal model held up.
2. **What slowed down or went wrong?** The main friction was review sensitivity to comparative phrasing and first-use definition requirements inside Findings, which needed two tightening passes.
3. **What single change would prevent this next time?** Nothing immediate; the current review workflow already exposed the remaining issues before completion.
4. **Is this a pattern?** Not a new one. It matches the existing pattern that synthesis language can drift from inference into fact if comparative wording is not kept explicit.
