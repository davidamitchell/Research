# 2026-04-27 -- Research Loop (agentic-ai-foundational-conditions-dependency-ordering)

**Completed:**

Research item:
- `Research/completed/2026-04-26-agentic-ai-foundational-conditions-dependency-ordering.md` -- completed; the item concludes that safe agentic deployment follows a staged dependency chain from coherent delegated-domain policy, to representable information architecture and access boundaries, to scoped machine identity, to permission-safe knowledge retrieval, and only then to deployment gating. It also concludes that no reviewed framework states that full five-layer order explicitly, so the ordering is a novel synthesis built from companion-item evidence plus zero-trust, operational-resilience, and AI-governance sources.

Sources consulted:
- https://davidamitchell.github.io/Research/research/2026-04-26-policy-coherence-machine-checkable-prerequisite.html (policy coherence prerequisite)
- https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html (permission-safe retrieval and access-model blocker)
- https://csrc.nist.gov/pubs/sp/800/207/final (zero-trust least-privilege and per-session access model)

## Mini-Retro

1. **Did the process work?** Yes, the synthesis held up after one review-cycle correction and the second automated review passed cleanly.
2. **What slowed down or went wrong?** I initially rated several synthesis findings as high confidence even though the direct support at the point of claim was mostly companion-item evidence rather than independent external sources.
3. **What single change would prevent this next time?** Add an explicit self-review rule that synthesis findings supported mainly by same-repository companion items default to medium confidence unless independent external evidence is cited.
4. **Is this a pattern?** Not yet, this looked like a specific synthesis-confidence miss rather than an established recurring pattern.

## Applied improvements

- Updated `research-prompt.md` to require confidence-evidence alignment for synthesis claims before draft commit.
