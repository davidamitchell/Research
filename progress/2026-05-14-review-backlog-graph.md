# 2026-05-14 -- Review backlog and begin graph work (W-0071, W-0072)

**Completed:**
- `BACKLOG.md` — W-0071 marked done; backlog construction outputs (W-0072–W-0075) already existed as sequenced implementation epics; added notes documenting the dependency chain.
- `scripts/build_site.py` — Added `build_graph_json()` function (schema 1.0) and `GRAPH_DATA_DIR` constant. Wired into `main()` after singleton-tag filter runs and `slug_to_item` is ready, writing `docs/data/graph.json` on every site build.
- `tests/test_build_site.py` — 21 new tests covering: valid JSON, schema fields, node fields, edge fields, weight=1, cites/related/tag-overlap edge production, tag-overlap deduplication, canonical direction (source < target), orphan-slug skipping, determinism, sort order, and provenance.
- `BACKLOG.md` — W-0072 marked done with implementation notes.

**Graph schema (1.0):**
- Nodes: `slug`, `title`, `type`, `url`
- Edges: `source`, `target`, `weight` (1), `rel` (cites|related|tag-overlap), `evidence` (field name or tag list), `provenance` (declaring item slug)
- Output sorted: nodes by slug, edges by (source, target, rel)

## Mini-Retro

1. **Did the process work?** Yes. TDD red→green→refactor followed strictly. Reading `load_links()` and `main()` first before designing the function prevented re-deriving the graph from scratch (W-0072's explicit warning). The function slots cleanly into existing code.

2. **What slowed down or went wrong?** Nothing significant. The `datetime.now(tz=UTC)` call in `build_graph_json` means the `generated` field changes every run, which makes the full JSON output non-deterministic across runs (though the structure and data are deterministic). The determinism test only checks that two calls in the same test produce identical output — it passes — but two builds on different days will differ on `generated`. This is acceptable for a build artifact but worth noting.

3. **What single change would prevent this next time?** The `generated` timestamp making two separate runs produce different top-level JSON is inherent to the design. If strict byte-for-byte reproducibility across builds were required, `generated` would need to be derived from git HEAD or omitted. No action needed now — the current behaviour is correct for an artifact.

4. **Is this a pattern?** No — this is the first graph artifact. No recurring friction.

5. **Does any documentation need updating?** No. The function has a clear docstring; W-0072 notes in BACKLOG.md capture the implementation. The copilot-instructions.md does not need updating.

6. **Do the default instructions need updating?** No new conventions emerged.

**Next:** W-0073, W-0074, W-0075 — see continuation below.

---

## Continuation: W-0073, W-0074, W-0075

**Completed:**
- `docs-adr/0016-graph-visualization-approach.md` — ADR for graph visualization. Rejected D3/Cytoscape (new external dependency + CDN risk); chose vanilla-JS force-directed layout embedded inline. No new dependencies of any kind.
- `docs-adr/README.md` — ADR index updated with entry for 0016.
- `scripts/build_site.py`:
  - `_validate_graph(graph) -> list[str]` — validates edge references, required fields, count consistency; called from `build_graph_json()` which raises `ValueError` on failure.
  - `build_graph_page()` — generates `docs/graph.html` with canvas, 300-tick force simulation, pan/zoom, click-to-inspect provenance panel, legend, and stats line. `_GRAPH_JS` constant holds ~200 lines of vanilla ES5 JS.
  - `html_nav()` updated: Graph link added between Search and GitHub.
  - `GRAPH_DATA_DIR` constant added; `main()` now writes `docs/graph.html` alongside `docs/data/graph.json`.
  - `build_graph_json()` weighting updated: `cites`=4, `related`=3, `tag-overlap`=N (shared tag count, min 1). Rationale documented in docstring table.
- `tests/test_build_site.py` — 16 new tests for W-0073/74 (graph page, nav link, validate_graph) + 6 for W-0075 (weighting). Total: 37 graph tests; 470 pass.
- `BACKLOG.md` — W-0073, W-0074, W-0075 marked done with implementation notes.

## Mini-Retro

1. **Did the process work?** Yes. TDD applied throughout. ADR written before any implementation code — the decision to use vanilla JS rather than D3 was the right call; it eliminated all dependency concerns and kept `build_site.py` as the single source of truth. All four items (W-0072/73/74/75) are done and tested.

2. **What slowed down or went wrong?** One small friction: the test file imported `html_head` when the nav function is actually `html_nav` — caught immediately on the first red run. Minor.

3. **What single change would prevent this next time?** Check the exact function names in `build_site.py` before writing tests that import them — `grep -n "^def "` is a one-second check.

4. **Is this a pattern?** Not a recurring one — it was a fast catch. No action needed.

5. **Does any documentation need updating?** ADR-0016 written and indexed. BACKLOG.md updated. No other docs need changing.

6. **Do the default instructions need updating?** No new conventions emerged. The pattern of embedding JS as a plain string constant in a Python template (to avoid f-string escaping conflicts) is worth noting mentally but not a convention change.

**State at close:** W-0071 through W-0075 are all done. The graph pipeline is complete end-to-end: `build_graph_json` exports the artifact, `_validate_graph` enforces integrity, `build_graph_page` renders it with traceable edges, and the weighting algorithm gives meaningful edge strengths.
