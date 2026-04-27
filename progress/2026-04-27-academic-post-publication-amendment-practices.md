# 2026-04-27 -- Research Loop (academic-post-publication-amendment-practices)

**Completed:**

Research item:
- `Research/completed/2026-04-27-academic-post-publication-amendment-practices.md` -- completed; the item concludes that the minimal viable analogue for this repository is an immutable completed note plus a linked amendment record, not silent overwrite. It distinguishes correction, commentary, retraction, and living-update paths, recommends three reader-signal frontmatter fields on the original record, and narrows silent edits to broken-URL repair, tag updates, and citation-URL normalization.

Sources consulted:
- https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy (Nature correction, retraction, and commentary policy)
- https://info.arxiv.org/help/versions.html (arXiv permanent version-history and comment mechanics)
- https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals (Cochrane update versus new-protocol decision framework)

## Applied improvements

- Updated `research-prompt.md` to ban runtime-specific access-path prose such as "blocked in this runtime" from final Findings or Risks/Gaps, requiring source-qualification wording instead.

## Pending skill improvements

- Mirror the same "no runtime-specific access-path prose in final output" rule into the `research` skill once the skills submodule can be updated upstream in `davidamitchell/Skills`.

## Mini-Retro

1. **Did the process work?** Yes, the second review loop exposed a real prose-quality problem and the final item is stronger for fixing it instead of relying on the auto-pass alone.
2. **What slowed down or went wrong?** Runtime-specific access notes and undefined domain terms passed local inspection but failed the review workflow, which cost an extra fix cycle.
3. **What single change would prevent this next time?** Keep execution-path metadata out of final prose unless it can be rewritten as a source-qualification claim grounded in the accessible source, and encode that rule directly in the prompt.
4. **Is this a pattern?** Yes, it matches the broader recurring pattern that review failures often come from citation-discipline details rather than from the core synthesis itself.
