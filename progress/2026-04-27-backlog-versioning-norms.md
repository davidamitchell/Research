# 2026-04-27 — Add backlog items W-0038 and W-0039: research item versioning norms

**Completed:**
- `BACKLOG.md` — appended W-0038 and W-0039 (highest prior item was W-0037)

**W-0038: Academic publishing norms for research item versioning**
Research item to validate the proposed pragmatic versioning model (same file path, git history as diff, frontmatter `versions:` array) against academic pre-print norms (arXiv, SSRN, OSF) and PKM (Personal Knowledge Management) systems (Zettelkasten, Obsidian Publish, Roam). Also evaluates whether `replicates` and `corrects` relationship types should be added to the `## Related Items` edge vocabulary. Spawned from a design session on immutability and academic norms for completed research items.

**W-0039: Implement frontmatter version tracking for completed research items**
Implementation item for the pragmatic versioning design: `versions:` array in `Research/_template.md`, `ResearchItem` dataclass update, immutability rule in `.github/copilot-instructions.md`, version history table in `scripts/build_site.py`, and test coverage. Blocked on W-0038 under Option A; can proceed independently under Option B.

## Mini-Retro

1. **Did the process work?** Yes. The issue content was clear and self-contained. W-numbers were verified against `BACKLOG.md` (highest was W-0037); new items are W-0038 and W-0039 as specified.

2. **What slowed down or went wrong?** Nothing significant. Pre-existing `TAVILY_API_KEY` test failure in `tests/test_mcp_config.py` was noted — this is a known environment constraint unrelated to this session.

3. **What single change would prevent this next time?** Nothing to change — the append-backlog-items workflow is clean and well-documented.

4. **Is this a pattern?** No new patterns identified.

5. **Does any documentation need updating?** No — the backlog items are self-contained and reference the design decisions made in the spawning session.

6. **Do the default instructions need updating?** No — the immutability rule and versioning design will be documented as part of W-0039 implementation, not here.
