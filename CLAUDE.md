# Claude Code — Research Repo Orientation

## First: read the instructions

`.github/copilot-instructions.md` is the source of truth for ALL conventions in this
repository. Read it at the start of every session. It governs naming, testing, ADRs,
session logs, credentials, and git workflow. The rules below are a short-form reminder
only — the full text in copilot-instructions takes precedence.

## Skills submodule

The `.github/skills/` directory is a git submodule. If it appears empty, init it:

```bash
git submodule update --init .github/skills
```

Available skills (use via the skill-author pattern or directly in session):
`adr`, `backlog-manager`, `backlog-worker`, `citation-discipline`, `decisions`,
`inline-citation`, `peer-reviewer`, `research`, `research-question`, `research-reviewer`,
`remove-ai-slop`, `speculation-control`, `swe`, `tdd`, `technical-writer`

## Non-negotiables (from copilot-instructions)

| Rule | Detail |
|---|---|
| Session log | `progress/YYYY-MM-DD-{slug}.md` with Mini-Retro — not optional |
| ADR required | New external dependency, new autonomous workflow, schema change |
| Quality gate | `make check` (ruff) + `pytest` must pass before every commit |
| Credentials | Never commit secrets; check the approved table before using any credential |
| Backlog | Repo tasks → `BACKLOG.md`; research tasks → `Research/backlog/` |
| Tags | Use `docs/tag-vocabulary.md`; run `scripts/canonicalise_tags.py` if uncertain |
| Skills submodule | Read-only — never edit `.github/skills/`; changes go to `davidamitchell/Skills` |
| Commit style | `feat:` / `fix:` / `docs:` / `backlog:` / `research:` prefixes |

## Gemini API — free-tier quota pools (per model, independent)

Each model has its own daily quota. The cascade in `src/pipeline/_gemini.py` walks
through models newest-first and advances when a model's daily quota is exhausted.
Per-model RPM is set in `_MODEL_RATES`; never guess or use a single global default.

Cascade priority order (highest capability → highest throughput):

| Priority | Model | RPM | RPD | Notes |
|---|---|---|---|---|
| 1 | `gemini-3.1-pro` | — | — | Check aistudio.google.com |
| 2 | `gemini-2.5-pro` | — | — | Check aistudio.google.com |
| 3 | `gemini-3-flash` | — | — | Check aistudio.google.com |
| 4 | `gemini-2.5-flash` | 5 | 20 | Confirmed from aistudio dashboard (2026-05-14); thinking model |
| 5 | `gemini-3.1-flash-lite` | — | — | Check aistudio.google.com |
| 6 | `gemini-2.5-flash-lite` | 10 | 1 500 | Confirmed free tier (2026-05-12) |

Cascade advances on **daily quota exhaustion only**. RPM backoff is handled by
the adaptive rate limiter — it reads `x-ratelimit-*` headers and waits for the
reset window without advancing the cascade. Model IDs are discovered at runtime
via `client.models.list()` — never hard-coded or guessed.

Starting model is configured in `config/sources.yaml → gemini.gemini_model`.

## Key file locations

```
.github/copilot-instructions.md   ← full rules (always authoritative)
.github/skills/                   ← skills submodule (read-only)
BACKLOG.md                        ← engineering work items (W-XXXX)
Research/backlog/                 ← research question items
docs/tag-vocabulary.md            ← canonical tag vocabulary
scripts/canonicalise_tags.py      ← rewrite tags to canonical form
scripts/enrich_items.py           ← add ai_themes via Gemini
src/pipeline/_gemini.py           ← Gemini client, rate limiter, model cascade
config/sources.yaml               ← starting model config
```
