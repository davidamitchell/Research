# ADR-0016: Graph visualization approach for GitHub Pages

Date: 2026-05-14
Status: accepted

## Context

W-0073 requires a browser-rendered graph view on the GitHub Pages (GH Pages) site that:

1. Loads the `docs/data/graph.json` artifact produced by W-0072.
2. Renders nodes and edges with a force-directed layout.
3. Makes edges traceable — clicking an edge reveals its `rel`, `evidence`, and `provenance` fields and links back to the source and target item pages.
4. Works without external services or runtime credentials (no server, no API key).
5. Is generated entirely by `scripts/build_site.py` so the `build_site.yml` workflow is the sole write path for `docs/`.

The copilot-instructions.md mandates an Architecture Decision Record (ADR) whenever a new external dependency is introduced. Rendering an interactive graph in a browser typically requires a JavaScript (JS) visualization library (D3.js, Sigma.js, Cytoscape.js, vis.js, or equivalent). Each of these is a new external dependency that triggers the ADR requirement.

### Constraints

- **GitHub Pages is static** — no Node.js server, no WebSockets, no server-side rendering.
- **No CDN runtime dependencies** — the page must be fully usable if the CDN is unavailable or rate-limited.
- **`docs/` is auto-generated** — any JS asset written to `docs/` must be produced by `build_site.py` at build time, not committed manually.
- **Corpus size** — approximately 300 nodes (research + synthesis items) and several hundred to a few thousand edges. The renderer must remain interactive at this scale.
- **No new pip package** — adding a Python dependency solely to download a JS library at build time is disproportionate to the problem.

### Options considered

**Option A — D3.js (v7), vendored at build time**

D3.js is the de-facto standard for browser-based data visualization. The force simulation (`d3-force`) provides a high-quality, well-tested layout engine. The full v7 bundle is ~272 KB minified. Vendoring requires either embedding the source inline (making `build_site.py` ~10,000 lines larger) or downloading it from `unpkg.com` or `jsDelivr` during the site build (adds a network dependency to CI).

- (+) Proven force layout; large community and documentation.
- (−) 272 KB minified source embedded in `build_site.py` is unwieldy.
- (−) Downloading from a CDN at build time adds a network dependency to CI; fails if CDN is unreachable.
- (−) Introduces a new external JS dependency requiring tracking and updates.

**Option B — Cytoscape.js, vendored at build time**

Cytoscape.js is a purpose-built graph library (~200 KB minified). Similar vendoring challenges as D3.

- (+) Graph-specific API; built-in layouts.
- (−) Same vendoring trade-offs as Option A (~200 KB inline or CDN download at build time).
- (−) New external dependency.

**Option C — Vanilla JS force-directed layout, no library**

Implement a lightweight force-directed graph renderer (~250 lines) using the HTML5 Canvas API and vanilla JavaScript, embedded inline in the page template. No library required. The force simulation uses pairwise repulsion (Coulomb-like) and spring attraction along edges, with velocity damping for convergence.

- (+) Zero new external dependencies — no pip packages, no CDN, no JS bundles.
- (+) Fully self-contained: the page works offline and without CDN.
- (+) Entire implementation lives in `build_site.py` as a template string — no separate asset files.
- (+) Canvas rendering is performant at 300 nodes (≤ 90,000 pair operations per tick; converges in ~150 frames at 60 fps).
- (−) Custom simulation is less polished than D3's Barnes-Hut approximation; O(n²) per tick is the dominant cost.
- (−) No community support or documentation for the custom code.
- (−) Maintaining the simulation logic requires JS knowledge in a Python-primary codebase.

## Decision

**Option C — Vanilla JS force-directed layout, no library.**

The decision is driven by the constraints: no CDN runtime dependency, no new external pip dependency, and `docs/` generated entirely by `build_site.py`. A custom ~250-line force simulation embedded inline satisfies all constraints with no new dependency surface. At the corpus size (≤ 500 nodes) the O(n²) repulsion calculation completes in under 5 ms per frame in modern browsers, which is acceptable. The simulation runs for a fixed number of ticks then freezes, reducing CPU use after layout convergence.

### Implementation notes

- Force simulation: pairwise Coulomb repulsion (strength 8000 / distance²) + Hookean spring attraction along edges (rest length proportional to edge weight). Velocity damping 0.85 per tick. Runs 300 ticks then halts.
- Rendering: HTML5 Canvas with pan (drag) and zoom (scroll wheel). Nodes as filled circles, edges as lines, node labels drawn at zoom ≥ 0.6.
- Provenance panel: clicking a node or edge opens an information panel below the canvas showing all metadata fields (`rel`, `evidence`, `provenance`) and links to source/target item pages.
- Navigation: a "Graph" nav link is added to `html_head()` in `build_site.py`.

### Migration trigger

If the corpus grows beyond ~1,000 nodes and the O(n²) simulation becomes perceptibly slow, revisit this decision. At that scale, Option A (D3 + Barnes-Hut) or a WebWorker-based layout would be warranted. Write a superseding ADR.

## Consequences

### Positive
- No new external dependencies of any kind (no pip, no npm, no CDN).
- `build_site.py` remains the single source of truth for all site output.
- Page works offline and in restricted network environments.
- All graph logic is version-controlled alongside the site generator.

### Negative / Trade-offs
- O(n²) simulation is slower than Barnes-Hut at large scale; acceptable at ≤ 500 nodes.
- Custom force simulation code must be maintained in-house; no community documentation.
- Embedding ~250 lines of JS in a Python string requires careful escaping.

### Neutral
- The Canvas API is universally supported in modern browsers; no polyfill needed.
- Layout seed is not fixed — graph positions differ between page loads. This is standard for force-directed graphs and does not affect traceability.
