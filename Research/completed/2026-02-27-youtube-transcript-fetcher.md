---
title: "YouTube transcript fetcher for research"
added: 2026-02-27
status: completed
priority: high
tags: [youtube, transcripts, fetching, tooling]
started: 2026-03-03
completed: 2026-03-03
output: [tool, backlog-item]
---

# YouTube transcript fetcher for research

## Question / Hypothesis

Can we port the YouTube transcript fetcher from `davidamitchell/Latest-developments-` to this repo and adapt it for research use (bulk fetch, save transcripts, not just email digest)?

## Context

The companion repo (`davidamitchell/Latest-developments-`) has a working YouTube transcript fetcher (`src/fetchers/youtube.py`) that:
- Discovers videos via a channel's Atom feed (no API key needed)
- Fetches transcripts via `youtube-transcript-api`
- Falls back to the video description if the transcript is blocked (which it often is on GitHub Actions cloud IPs)

For research purposes, we want to:
- Fetch transcripts on demand (not just for digest emails)
- Save raw transcripts to disk for later processing
- Support bulk fetch for a channel's backlog

## Scope

**In scope:**
- Port `src/fetchers/youtube.py` with minimal changes
- Add CLI: `python -m src.main fetch youtube <channel_id>`
- Save transcript to `Research/in-progress/` or a configurable output path

**Out of scope:**
- AI summarisation of transcripts (separate research item)
- Transcript search / indexing

## Approach

1. Review current implementation in `davidamitchell/Latest-developments-/src/fetchers/youtube.py`
2. Identify what needs to change for a research context (output format, bulk support)
3. Port with minimal changes; write tests
4. Add ADR if the approach differs significantly

## Sources

- [x] `davidamitchell/Latest-developments-/src/fetchers/youtube.py`
- [x] `youtube-transcript-api` docs: https://github.com/jdepoix/youtube-transcript-api
- [x] Known issue: transcripts blocked on GitHub Actions cloud IPs — see Latest-developments- deferred backlog

## Findings

### Executive Summary

The YouTube transcript fetcher port is complete and fully operational. `src/fetchers/youtube.py` supports both channel-based bulk fetch (via YouTube Atom feed, no API key required for discovery) and single-video fetch by URL or ID, with a three-tier fallback chain for cloud IP transcript blocks. All 18 unit tests pass and all four BACKLOG slices (W-0016 through W-0019) are marked done. The implementation improves on the companion repo by using the Atom feed for discovery rather than the YouTube Data API v3, eliminating the API quota cost for channel scanning.

### Key Findings

1. `src/fetchers/youtube.py` is implemented and passes all 18 tests (`pytest tests/test_fetchers_youtube.py`); the port is complete.
2. Channel discovery uses the YouTube Atom feed (`https://www.youtube.com/feeds/videos.xml?channel_id=<id>`) — no API key needed for feed-based discovery, unlike the companion repo which requires `YOUTUBE_API_KEY` for the search endpoint.
3. Single-video fetch uses `python -m src.main fetch youtube --video <url>` and accepts full YouTube URLs, `youtu.be` short URLs, or bare video IDs.
4. The fetcher implements a three-tier fallback when transcripts are blocked: (1) `youtube-transcript-api`, (2) YouTube Data API v3 description (if `YOUTUBE_DATA_API` env var is set), (3) `og:description` meta tag scraped from the watch page.
5. The CLI (`python -m src.main fetch youtube`) outputs transcript content to stdout; saving to `Research/transcripts/` is handled by the `fetch-transcript.yml` GitHub Actions workflow, which uses `yt-dlp` and commits the file to the repo.
6. Transcript requests from GitHub Actions cloud IPs (AWS/GCP ranges) are blocked by YouTube at the network level. This is a hard restriction with no reliable workaround from a cloud runner; the workflow commits step-by-step manual instructions when automated fetch fails.
7. Bulk channel fetch is limited to recent videos. The Atom feed returns approximately the last 15 videos; the `--max-videos` flag can cap this further. Historical backlog fetch beyond the feed window is not supported via this approach.
8. URL deduplication via `StateStore` (`state/index.json`) prevents reprocessing already-fetched items across runs.
9. The `youtube-transcript-api` library (v1.2.4 as of this writing) is installed; it requires no API key and works without a headless browser.
10. The implementation differs from the companion repo's design: companion uses `YouTubeConfig` dataclass and `with_backoff` retry utility; this repo uses direct `httpx.Client` injection and inline retry logic, making it more testable in isolation.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Port complete, 18 tests pass | `tests/test_fetchers_youtube.py` (local run) | high | All 18 passed in 6.13s |
| Atom feed used for discovery | `src/fetchers/youtube.py:_CHANNEL_FEED_URL` | high | No API key in channel path |
| Three-tier transcript fallback | `src/fetchers/youtube.py:_fetch_video()` | high | Code inspection |
| CLI outputs to stdout | `src/main.py:_fetch_youtube()` | high | Code inspection |
| Workflow saves to `Research/transcripts/` | `.github/workflows/fetch-transcript.yml` | high | Full workflow reviewed |
| Cloud IP block is hard restriction | `.github/workflows/fetch-transcript.yml` comments + `fetch-transcript.yml` fallback README generation | high | Documented in workflow |
| Atom feed limited to ~15 recent videos | YouTube documentation (known feed behaviour) | medium | Feed design; not configurable |
| `youtube-transcript-api` v1.2.4 installed | `pip show youtube-transcript-api` | high | Verified in environment |
| Deduplication via StateStore | `src/main.py:_fetch_youtube()`, `src/state.py` | high | Code inspection |
| BACKLOG slices W-0016–W-0019 done | `BACKLOG.md` | high | All marked `status: done` |

### Assumptions

- **Assumption:** The companion repo's Atom-feed approach (rather than its YouTube Data API search approach) is preferred for research use. **Justification:** No API quota cost for discovery; the research use case is on-demand rather than scheduled polling, making quota conservation less critical but still desirable.
- **Assumption:** Saving transcripts to `Research/transcripts/` via the GitHub Actions workflow (rather than the CLI) satisfies the "save to disk" requirement. **Justification:** The owner has no local environment; all file saves must go through GitHub, making the workflow the natural persistence layer.

### Analysis

The research question is answered in the affirmative: the port succeeded and is production-ready. The key design divergence from the companion repo is the switch from YouTube Data API search (quota-consuming) to the Atom feed (free) for channel discovery. This trade-off sacrifices metadata richness (the Atom feed returns fewer fields than the API snippet) but eliminates the dependency on a paid/quota-limited credential for the most common operation.

The three-tier fallback is the correct response to the cloud IP block problem. It degrades gracefully: transcript text (ideal) → video description (acceptable for research context) → page description (minimal but better than nothing). The workflow's fallback to human-readable instructions is appropriate for the owner's web-only access pattern.

The one gap against the original scope is bulk historical backlog fetch. The Atom feed is limited to ~15 recent videos per channel. If the use case requires fetching a channel's older content, a different approach is needed (YouTube Data API with `pageToken` pagination, or a third-party tool). Three backlog items already address this gap (`2026-02-28-transcript-via-gemini-api.md`, `2026-02-28-transcript-via-yt-dlp-whisper.md`, `2026-02-28-transcript-via-third-party-apis.md`).

### Risks, Gaps, and Uncertainties

- YouTube's Atom feed is an unofficial/undocumented endpoint; it could be deprecated without notice.
- The Atom feed returns only the most recent ~15 videos. Historical backlog fetch for a channel requires a different approach (backlog items exist for this).
- The `youtube-transcript-api` library may break when YouTube changes its internal API (it has broken before). The three-tier fallback mitigates this but does not eliminate the risk.
- The `YOUTUBE_DATA_API` env var is optional; without it, the second fallback tier is unavailable and the fetcher drops to the og:description scrape immediately.

### Open Questions

- Should the CLI gain a `--output-dir` flag to save transcripts directly to disk (e.g., `Research/transcripts/`), removing the dependency on the GitHub Actions workflow for persistence?
- Is Atom feed pagination needed, or is the Gemini/yt-dlp/third-party approach the right path for bulk historical fetch?

---

## Output

- Type: tool, backlog-item
- Description: `src/fetchers/youtube.py`; supporting CLI in `src/main.py`; `fetch-transcript.yml` workflow for GitHub Actions persistence. Bulk historical fetch remains as open backlog items.
- Key sources:
  - https://github.com/jdepoix/youtube-transcript-api — library documentation and changelog
  - https://github.com/davidamitchell/Research/blob/main/src/fetchers/youtube.py — ported implementation
  - https://github.com/davidamitchell/Research/blob/main/.github/workflows/fetch-transcript.yml — workflow for disk persistence