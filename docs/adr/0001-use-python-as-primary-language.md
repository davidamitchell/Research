# ADR-0001: Use Python as Primary Language

Date: 2026-02-27
Status: Accepted

## Context

The research tooling needs to:
- Fetch YouTube transcripts
- Parse and process web content
- Provide a CLI for managing research items
- Potentially call AI APIs for synthesis and summarisation
- Run inside GitHub Codespaces

Multiple languages could accomplish this. The choice affects library availability, developer familiarity, and alignment with the companion repository (`davidamitchell/Latest-developments-`).

## Decision

Use **Python 3.11+** as the sole implementation language.

## Consequences

### Positive
- All required libraries (`youtube-transcript-api`, `httpx`, `PyYAML`) have mature Python packages
- GitHub Actions runners have Python 3.11 available by default; no custom runtime setup needed
- Aligns with `davidamitchell/Latest-developments-`, enabling direct code reuse (YouTube fetcher, retry logic, etc.)
- Strong ecosystem for likely extension points: `google-genai` for AI, `trafilatura` for web extraction, `sqlite3` (stdlib) for local storage

### Negative / Trade-offs
- Python is slower than compiled languages, but irrelevant for research tooling with low throughput requirements
- GIL limits true parallelism, but fetchers can use `asyncio` or `concurrent.futures` if needed

### Neutral
- Type hints (`mypy` / `pyright`) are used to compensate for Python's dynamic typing
- `ruff` provides fast linting and formatting consistent with the companion repo
