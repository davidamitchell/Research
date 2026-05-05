# 2026-05-05 — W-0051: Synthesis Workflow Implementation

**Completed:**

- `Knowledge/.gitkeep` — created the Knowledge directory
- `Knowledge/_template.md` — synthesis item template with sections: Synthesis Question, Source Items, Perspectives Considered, Cross-Item Findings, Contradictions and Tensions, Confidence Map, Open Questions
- `synthesis-prompt.md` — 12-step synthesis agent prompt with false-consensus guard, cross-item citation requirements, and frontmatter population instructions
- `.github/workflows/synthesis-loop.yml` — manual-trigger (workflow_dispatch) workflow accepting `synthesis_question` and `source_items` inputs; feeds injected synthesis-prompt.md to Copilot CLI; commits to main
- `scripts/build_site.py` — updated to:
  - Add `KNOWLEDGE_DIR`, `KNOWLEDGE_DOCS_DIR`, `GITHUB_KNOWLEDGE_BASE` constants
  - Add synthesis-specific sections to `SECTIONS_ORDERED` and `SECTION_PATTERNS`
  - Update `get_findings_excerpt()` to fall back to Cross-Item Findings for synthesis items
  - Add `load_knowledge_items()` function
  - Add `_item_url()` helper for URL routing by item kind
  - Update `render_card()` to use item's `page_url` field
  - Update `_render_related()`, `_render_cites_related()`, and `build_item_page()` to use `_item_url()`
  - Add "Synthesis" nav link to `html_nav()`
  - Add `build_knowledge_index_page()` for `docs/knowledge/index.html`
  - Update `main()` to load, build, and route Knowledge/ items
  - Update JavaScript search to use `item.url` (supports both research and knowledge URLs)
  - Update `build_search_index()` to emit per-item `url` from `page_url`
- `.github/workflows/build_site.yml` — added `Knowledge/**` to push trigger paths
- `docs-adr/0014-knowledge-synthesis-directory.md` — ADR documenting the new directory, schema, routing, and workflow decisions
- `docs-adr/README.md` — ADR index updated
- `BACKLOG.md` — W-0051 marked as done; W-0052 block condition updated
- `tests/test_build_site.py` — 12 new tests for `_item_url()`, `render_card()` URL routing, `load_knowledge_items()`, and `build_knowledge_index_page()`

**Test results:** 411 passed, 1 pre-existing failure (TAVILY_API_KEY not set in sandbox), 1 skipped.

---

## Mini-Retro

1. **Did the process work?** Yes. The architecture research (2026-05-02-cross-item-synthesis-knowledge-map-architecture) provided clear decision support. The swe/tdd/code-review loop was followed mentally; the implementation was designed before coding and validated with tests before committing.

2. **What slowed down or went wrong?** The most friction was mapping all the places in `build_site.py` that hardcode `/Research/research/` URLs. There were 10 such locations (Python + JavaScript). A `_item_url()` helper centralised this cleanly.

3. **What single change would prevent this next time?** The URL routing pattern (store `page_url` in the item dict at load time, use a helper everywhere) should be documented as a convention so future item types (e.g., Outputs/) don't require a second sweep of URL hardcodes.

4. **Is this a pattern?** Yes — this is the same class of problem as hardcoded path strings that should be derived from item metadata. Already seen with `github_url`. The fix (store at load time, use helper at render time) is now established.

5. **Does any documentation need updating?** The copilot-instructions.md `Repository Layout` table should be updated to show `Knowledge/`. The `## Non-Negotiable Constraints` section should note that `Knowledge/` always contains `.gitkeep`.

6. **Do the default instructions need updating?** Yes — add `Knowledge/` to the layout table and add a constraint that `Knowledge/` items are stored in `Knowledge/` not `Research/`, and that `Knowledge/.gitkeep` must never be deleted.
