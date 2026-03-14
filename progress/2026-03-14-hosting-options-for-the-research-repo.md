# 2026-03-14 — Research Loop (hosting-options-for-the-research-repo)

**Completed:**

Research item:
- `Research/completed/2026-03-12-hosting-options-for-the-research-repo.md` — completed; GitHub Pages with MkDocs Material and Pagefind is the recommended free hosting stack for this repository's research content, requiring only the already-approved GITHUB_TOKEN with `contents: write`. All cloud vector and graph database free tiers require new API credentials not in the approved table, making them a hard stop without owner approval.

Sources consulted:
- https://squidfunk.github.io/mkdocs-material/publishing-your-site/ (MkDocs Material GitHub Pages deployment recipe)
- https://pagefind.app/docs/ (Pagefind v1.0 static search documentation)
- https://qdrant.tech/documentation/cloud/ (Qdrant Cloud free tier — 1 GB forever, but requires new API credential)

## Mini-Retro

1. **Did the process work?** Yes. The research loop ran end-to-end without blocking issues. The approved-credentials constraint cleanly narrowed the decision space: everything requiring a new API key was ruled out early, leaving a well-defined recommendation.

2. **What slowed down or went wrong?** Two acronym expansion violations (`CI` and `PoPs`) were found during the companion skill checks after the full draft was written. The `edit` tool failed on those lines due to Unicode characters (em-dashes, curly quotes) in the surrounding text, requiring a Python line-replacement workaround. The review workflow also took longer to register than the default 20-second sleep, requiring a manual status check at the start of the resumed session.

3. **What single change would prevent this next time?** Run the acronym expansion audit incrementally (per section) as each §2 sub-question is written rather than as a single pass at the end. Finding violations earlier avoids edit-tool failures on completed prose.

4. **Is this a pattern?** Yes — acronym expansion failures are the most common review failure (19+ items). This matches the known recurring pattern documented in the research-prompt.md. No new pattern identified; the mitigation (earlier inline audit) is the incremental application of the existing rule.
