# 2026-05-06 -- Research Loop (aibom-identity-delegation-trust-theory)

**Completed:**

Research item:
- `Research/completed/2026-05-06-aibom-identity-delegation-trust-theory.md` -- completed; the item concludes that an Artificial Intelligence Bill of Materials (AIBOM) needs a typed identity graph, explicit delegation edges, edge-bound permission manifests, trust-boundary metadata, credential policy, and attribution requirements to preserve "who authorized what" across multi-agent systems. It also distinguishes the roles of OpenID Connect for human identity, RFC 8693 for delegation semantics, and SPIFFE for workload identity, and shows why no single standard covers the full attribution problem by itself.

Sources consulted:
- https://www.rfc-editor.org/rfc/rfc8693 (formal delegation and impersonation semantics)
- https://csrc.nist.gov/pubs/sp/800/207/final (Zero Trust Architecture subject and least-privilege model)
- https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/ (workload identity, SVIDs, and trust bundles)

## Mini-Retro

1. **Did the process work?** Yes, the research loop, external review, and one final cleanup pass were enough to get the item to a defensible completed state.
2. **What slowed down or went wrong?** The review workflow did not increment `review_count` on the first failing pass, and the second pass still surfaced a few citation-discipline edge cases that were easier to fix after reading the raw log than from the workflow annotation alone.
3. **What single change would prevent this next time?** Nothing new; the existing instruction to inspect `OVERALL` and `VIOLATION` lines directly in the review log already addresses the main failure mode.
4. **Is this a pattern?** Yes, it matches the known pattern that the review workflow conclusion and annotations are less reliable than the underlying log lines for deciding whether an item is actually clean.
