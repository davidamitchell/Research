---
title: "YouTube transcript fetcher for research"
added: 2026-02-27
status: backlog
priority: high
tags: [youtube, transcripts, fetching, tooling]
started: ~
completed: ~
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

- [ ] `davidamitchell/Latest-developments-/src/fetchers/youtube.py`
- [ ] `youtube-transcript-api` docs: https://github.com/jdepoix/youtube-transcript-api
- [ ] Known issue: transcripts blocked on GitHub Actions cloud IPs — see Latest-developments- deferred backlog

## Findings

*(to be filled in)*

## Output

- Type: tool, backlog-item
- Description: `src/fetchers/youtube.py`; backlog items in Epic 2
