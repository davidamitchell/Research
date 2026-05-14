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

**Next:** W-0073 (graph page in GitHub Pages, blocked on W-0072 — now unblocked). Requires ADR before implementation (new JS library dependency).
