# 2026-03-08 — Fix wiki link order (issue #28)

**Completed:**

Bug fix:
- `src/wiki/publish.py` — fixed `wiki_link()`: GitHub wiki `[[A|B]]` uses A as display text and B as the page URL target; the function was generating `[[slug|title]]` (wrong order) causing every wiki link to show an ugly slug as text and resolve to a non-existent title-based URL (404). Swapped to `[[title|slug]]` so display is human-readable and the link target hits the actual page. Updated docstring to document correct syntax.
- `tests/test_wiki.py` — updated two test assertions (`test_wiki_link_plain`, `test_wiki_link_in_table_escapes_pipe`) to match the corrected link format; added assertion in `test_generate_home_contains_item_link` that the title (not slug) appears at the start of the `[[...]]` link.

Conflict reduction:
- `PROGRESS.md` — stripped Work Log section and "Last updated:" lines; now static (no per-commit edits needed).
- `progress/archive.md` — archived all previous Work Log entries.
- `progress/` pattern established — each commit creates a new file here instead of editing `PROGRESS.md`.
- `research-prompt.md` — updated step 9 to create `progress/YYYY-MM-DD-{slug}.md` instead of editing `PROGRESS.md`.
- `.github/copilot-instructions.md` — updated all "Update PROGRESS.md" references to use `progress/` pattern.

## Mini-Retro

1. **Did the process work?** Yes. Root cause (wrong `[[A|B]]` order) was identified immediately by inspecting rendered wiki HTML vs raw Markdown.
2. **What slowed down or went wrong?** PROGRESS.md merge conflicts were a latent issue baked in from the start — every commit prepending to the same file guaranteed conflicts between PRs and the research loop.
3. **What single change would prevent this next time?** The `progress/` pattern: each session creates a new file, so no two commits ever touch the same line. Done in this session.
4. **Is this a pattern?** Yes — any high-frequency shared file that multiple concurrent writers prepend to will produce conflicts. The fix is always the same: move to per-entry files.
