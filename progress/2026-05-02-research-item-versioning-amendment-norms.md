# 2026-05-02 -- Research Loop (research-item-versioning-amendment-norms)

**Completed:**

Research item:
- `Research/completed/2026-05-02-research-item-versioning-amendment-norms.md` -- completed; the item concludes that this repository's `versions:` array plus git history is sufficient if it is treated as a visible append-only version chain with full commit SHAs and progress-log links. It recommends explicit correction-versus-revision thresholds, adds support for a `corrects:` relationship edge, rejects `replicates:` for now, and supersedes the earlier broader amendment-practices recommendation for separate amendment files.

Sources consulted:
- https://info.arxiv.org/help/versions.html (official arXiv versioning policy)
- https://help.osf.io/article/113-advanced-actions-registrations (official OSF update workflow)
- https://git-scm.com/docs/user-manual#object-name (official git commit identity guidance)

## Mini-Retro

1. **Did the process work?** Mostly yes. The review loop surfaced a few over-strong epistemic labels and wording issues that were easy to fix once the violations were explicit.
2. **What slowed down or went wrong?** The most persistent friction was research-review sensitivity to unlabeled access notes and mixed fact-plus-inference sentences, especially where repository-specific conclusions were packed into one line.
3. **What single change would prevent this next time?** Treat access-note prose as something to delete or rewrite immediately into source-backed evidence-gap language instead of leaving raw workflow observations in `§2`.
4. **Is this a pattern?** Yes. It is the same class of review friction as earlier citation-discipline failures: process metadata that looks harmless still gets audited as claim-bearing prose.
5. **Does any documentation need updating?** No additional documentation changes were warranted beyond updating `learnings.md`, because the item refines an existing governance thread rather than changing the repository workflow itself.
6. **Do the default instructions need updating?** No. The current instructions already call out access-note and citation-discipline failure modes clearly enough; the main need was to apply them more aggressively during drafting.

## Applied improvements

- Rewrote repository-design conclusions from `[fact]` to `[inference]` where the evidence supported a judgment rather than a direct quoted rule.
- Removed raw access-note prose and replaced the surviving evidence-gap language with narrower, source-backed wording.

## Related

- `Research/completed/2026-05-02-research-item-versioning-amendment-norms.md`
- `Research/completed/2026-04-27-academic-post-publication-amendment-practices.md`
- `docs-adr/0013-research-item-frontmatter-schema-extension.md`
