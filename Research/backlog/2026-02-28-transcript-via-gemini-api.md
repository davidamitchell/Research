---
title: "YouTube transcripts via Gemini API (native YouTube URL support)"
added: 2026-02-28
status: backlog
priority: high
tags: [youtube, transcripts, gemini, tooling, automation]
started: ~
completed: ~
output: [tool]
---

# YouTube transcripts via Gemini API (native YouTube URL support)

## Question / Hypothesis

Can we use the Gemini API (already configured in `davidamitchell/Latest-developments-`) to
extract full transcripts from YouTube videos without being blocked by YouTube's IP restrictions?

## Context

The `youtube-transcript-api` endpoint is permanently blocked from GitHub Actions cloud IP
ranges (AWS/GCP). Every workaround that routes through the same cloud runners hits the
same block.

**Gemini 1.5+ has native YouTube support**: the `fileData.fileUri` API parameter accepts
`https://www.youtube.com/watch?v=<id>` URLs directly. Gemini downloads and processes the
video server-side (not from the GitHub Actions IP), then returns whatever analysis was
requested — including a verbatim transcript.

The `davidamitchell/Latest-developments-` companion repo already has `GEMINI_API_KEY`
configured as a repository secret and uses Gemini for daily digest summarisation. The same
key should work here.

## Scope

**In scope:**
- Add `src/fetchers/transcript_gemini.py` — calls `google.generativeai` with a YouTube URL
  and a prompt asking for the full transcript
- Add `workflow_dispatch` or scheduled workflow that fetches and commits the transcript
- Investigate token limits (Gemini 1.5 Pro context window: 1M tokens; a 90-min talk
  transcript is ~15–20k tokens — well within limits)

**Out of scope:**
- Gemini summarisation of the transcript (separate concern)
- Bulk fetch of entire channels

## Approach

1. Test with a known video (HYUoS0GkGCs): call `gemini-1.5-pro` with
   `fileData.fileUri = "https://www.youtube.com/watch?v=HYUoS0GkGCs"` and prompt
   `"Return the full word-for-word transcript of this video."`
2. Evaluate output fidelity vs. the known secondary-source quotes in the research document
3. If quality is good, wrap in a `fetch_transcript_gemini(video_url, api_key)` function
4. Add a `workflow_dispatch` action that accepts a video URL and `GEMINI_API_KEY` secret

## Connection to Latest-developments-

The `davidamitchell/Latest-developments-` repo has:
- `GEMINI_API_KEY` as a GitHub Actions secret
- `google-generativeai` already in `requirements.txt`
- A working Gemini integration in `src/summariser.py`

This approach reuses that existing pattern — no new API sign-up required.

## Key risk

Gemini's "transcript" may be its own caption extraction, not the raw auto-generated captions.
Quality should be checked. For a professionally hosted talk like the Seth/Essentia video,
Gemini may have the video already indexed.

## Sources

- Gemini API docs — Files API + YouTube URL support:
  https://ai.google.dev/gemini-api/docs/vision#youtube-videos
- `davidamitchell/Latest-developments-/src/summariser.py` — existing Gemini integration
- `davidamitchell/Latest-developments-/requirements.txt` — `google-generativeai` version

## Open Questions

- What is the per-video token cost vs. the free-tier quota?
- Does Gemini return verbatim transcript or a paraphrase?
- Is the video already indexed by Google/Gemini for a major talk like this one?
