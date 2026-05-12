# ADR-0015: Gemini AI theme enrichment pipeline

Date: 2026-05-11
Status: accepted

## Context

The `Research/completed/` corpus contains ~297 items. Each item has a `tags`
frontmatter field set by the researcher, but no machine-readable high-level
thematic classification. Without a controlled vocabulary of themes it is
impossible to filter or cluster items by research topic in the static site,
the knowledge graph, or future synthesis workflows.

Three changes are required simultaneously:

1. **New external dependency**: `google-genai >= 1.0.0` — the official Python
   SDK for Google's Generative AI API. This introduces a new outbound HTTP
   dependency and a new credential (`GEMINI_API_KEY`).
2. **New frontmatter field**: `ai_themes: [...]` — a list of 1–6 strings drawn
   from a 16-item controlled vocabulary. The field is written by the enrichment
   script and is never set manually.
3. **New autonomous workflow**: `enrich-items.yml` — a `workflow_dispatch`-
   triggered GitHub Actions workflow that calls Gemini and commits changes to
   `Research/completed/` items directly, without human review of each write.

The decision meets the "when to write an ADR" criteria on all three counts:
new external dependency, new frontmatter schema field, and new autonomous
workflow with write side-effects.

### Design constraints inherited from `davidamitchell/Latest-developments-`

The Gemini pipeline pattern (rate limiter, model cascade, header-capturing
transport) is already proven in the sibling `Latest-developments-` repository.
This implementation ports that pattern verbatim rather than inventing an
alternative, so the two repositories share the same operational mental model.

Key constraints from that pattern:

- Use `google-genai` SDK (`genai.Client`, `types.GenerateContentConfig`), not
  bare `httpx` REST calls. The SDK handles auth, retries, and response parsing.
- Wire a custom `httpx.Client` subclass (`_HeaderCapturingClient`) into the
  genai client via `HttpOptions(httpx_client=...)` so that every response's
  `x-ratelimit-*` headers are captured without patching the SDK.
- Use a model cascade that walks newest models first; advance when a model's
  daily quota is exhausted rather than failing the run.

## Decision

### 1. New Python package: `google-genai >= 1.0.0`

Added to `[project] dependencies` in `pyproject.toml`. No other dependency
manager change is required; the existing `pip install -e .[dev]` CI step picks
it up automatically.

### 2. New module: `src/pipeline/_gemini.py`

Ported from `davidamitchell/Latest-developments-/src/pipeline/_gemini.py`.
Provides:

- `_MODEL_CASCADE` — ordered list of Gemini model IDs to try:
  `["gemini-3-flash", "gemini-3.1-flash-lite", "gemini-2.5-flash", "gemini-2.5-flash-lite"]`
- `_HeaderCapturingClient(httpx.Client)` — records `x-ratelimit-*` headers
- `_RateLimiter` — adaptive pacer: triples interval when ≤ 3 requests remain;
  waits for the reset window when remaining == 0
- `_ModelCascade(starting_model, rpm, http_client)` — walks the cascade;
  resets the rate limiter and clears stale headers on each advance
- `make_gemini_client(api_key)` → `(genai_client, http_client)` factory

### 3. New script: `scripts/enrich_items.py`

Adds `ai_themes` frontmatter to completed items that lack it. Key design
choices:

- **Idempotent**: items with `ai_themes` already set are skipped.
- **Controlled vocabulary**: 16 themes (see `_AI_THEMES` in the script).
  The model may add 1–2 novel themes if the item genuinely requires them.
- **Dry-run mode**: `--dry-run` prints what would happen without writing files.
- **Batch commits**: `--commit` flag commits every 20 enriched items as safe
  checkpoints, so a mid-run failure does not lose all progress.
- **Starting model**: reads `config/sources.yaml gemini.gemini_model`; defaults
  to `gemini-3-flash` (head of cascade).

### 4. New workflow: `.github/workflows/enrich-items.yml`

`workflow_dispatch`-only trigger (no scheduled run; no push trigger) with
inputs:

- `mode`: `backfill` or `single`
- `item_path`: path for single-item mode
- `max_items`: 10 / 20 / 50 / 100 / 297

The workflow uses `GEMINI_API_KEY` from repository secrets and pushes enriched
files back to `main` using `GITHUB_TOKEN` (contents: write).

### 5. Config: `config/sources.yaml gemini.gemini_model`

Set to `gemini-3-flash` — the newest confirmed-working Gemini model as of
2026-05-11. This value is the starting point for the cascade; if the model
returns a quota error the cascade falls through to `gemini-3.1-flash-lite`,
then `gemini-2.5-flash`, then `gemini-2.5-flash-lite`.

### 6. New frontmatter field: `ai_themes`

Written after the `tags:` line. Format: `ai_themes: [theme-a, theme-b]`.
Always lowercase, hyphenated strings. Never set manually.

### 7. New credential: `GEMINI_API_KEY`

A Google Generative AI API key. Must be added to repository secrets
(Settings → Secrets and variables → Actions → New repository secret).
The credentials table in `.github/copilot-instructions.md` is updated to
reflect this addition.

## Consequences

### Positive

- All ~297 completed items gain a consistent, machine-readable theme
  classification after one backfill run.
- The controlled vocabulary enables theme-based filtering on the static site
  and future synthesis clustering without additional AI calls.
- The cascade pattern means the backfill survives model quota exhaustion
  without operator intervention.
- The `_RateLimiter` adapts to actual API headroom, so the backfill runs as
  fast as the API allows without triggering 429s.
- Unit test suite (47 tests) covers all pipeline components without requiring
  a live API key.

### Negative / Trade-offs

- New outbound HTTP dependency on Google's Generative AI API. If the API is
  unavailable, the backfill stalls (it does not retry across runs automatically
  — the operator re-runs the workflow).
- `GEMINI_API_KEY` must be added as a repository secret before the workflow
  can run. This is a new credential not previously in the approved table.
- The workflow commits directly to `main`. A bug in `_insert_ai_themes` could
  corrupt frontmatter for many items. Mitigated by: dry-run mode, batch
  commits (checkpoint every 20 items), idempotency guard (skip if already
  enriched), and the test suite.
- `google-genai >= 1.0.0` adds ~15 MB of transitive dependencies (`httpx`,
  `google-auth`, `protobuf`). Most are already present in the environment.

### Neutral

- The 16-theme controlled vocabulary is defined as a Python constant in
  `scripts/enrich_items.py`. Expanding the vocabulary requires editing the
  script and re-enriching affected items.
- Model IDs are pinned in `_MODEL_CASCADE` in `src/pipeline/_gemini.py`. When
  Google releases new Gemini models, add them to the head of the list and
  update `config/sources.yaml`.
- The `enrich-items.yml` workflow is `workflow_dispatch`-only; it does not
  run on `push`. If a new completed item should be enriched immediately, the
  operator triggers the workflow manually (single-item mode) or waits for the
  next backfill.
