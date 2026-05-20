# 2026-05-20 -- Research Loop (align-strategic-relevance-with-low-effort-knowledge-pathways)

**Completed:**

Research item:
- `Research/completed/2026-05-19-align-strategic-relevance-with-low-effort-knowledge-pathways.md` -- completed; the item argues that strategically relevant knowledge becomes the default path only when institutions reduce search, access, interpretation, and social-risk costs together. It synthesises transaction-cost theory, information-processing theory, information foraging, and psychological safety into a practical design model built around clear ownership, permission-coherent systems, trusted defaults, and review-by-exception.

Sources consulted:
- https://doi.org/10.1287/inte.4.3.28 (Galbraith on reducing information-processing demand versus increasing capacity)
- https://doi.org/10.1037/0033-295X.106.4.643 (Pirolli and Card on Information Foraging Theory and information scent)
- https://www.cambridge.org/core/books/governing-the-commons/7AB7AE11BADA84409C34815CC288CD79 (Ostrom on local-rule fit and durable coordination)

## Mini-Retro

1. **Did the process work?** Yes, the research loop and review workflow surfaced the exact claim-shape problems that needed tightening.
2. **What slowed down or went wrong?** The review workflow repeatedly flagged meta-evaluation prose about evidence strength and comparative design rankings that looked reasonable in draft but were too strong for the repository's citation discipline.
3. **What single change would prevent this next time?** Add a self-review rule to `research-prompt.md` that bans self-referential evidence-ranking sentences and unsupported comparative design rankings before the first draft commit.
4. **Is this a pattern?** Yes. It is adjacent to the repo's existing citation-discipline failures: once the evidence is good, the remaining errors are often about how the synthesis is phrased rather than missing sources.

## Pending skill improvements

- The `research` skill should explicitly warn against author-methodology sentences such as "the strongest evidence in this item..." or "I weighted X more heavily..." unless they are rewritten as metadata or removed.

## Applied improvements

- Added a new self-review rule to `research-prompt.md` that bans self-referential evidence-ranking and author-methodology sentences unless they are rewritten as metadata or supported as narrow inferences.
