---
title: "YouTube transcripts via yt-dlp audio + Whisper transcription"
added: 2026-02-28
status: backlog
priority: medium
tags: [youtube, transcripts, whisper, yt-dlp, tooling, automation]
started: ~
completed: ~
output: [tool]
---

# YouTube transcripts via yt-dlp audio + Whisper transcription

## Question / Hypothesis

Can we bypass YouTube's IP-based transcript block by downloading the **audio track** with
`yt-dlp` (a different endpoint from the transcript API) and then transcribing it with
OpenAI Whisper?

## Context

YouTube blocks the internal `/api/timedtext` and `youtube-transcript-api` endpoints from
cloud IP ranges. However, `yt-dlp` downloads the **audio/video stream** via a different
set of CDN endpoints. These CDN endpoints are less aggressively blocked (though not
guaranteed from all cloud IPs).

The `fetch-transcript.yml` workflow already uses `yt-dlp` to try fetching auto-captions.
If caption fetching is blocked, we can fall back to downloading the audio and transcribing
it locally with OpenAI's Whisper model (free, runs locally on the GitHub Actions runner).

## Approach

### Option A — Local Whisper (free, slower)
1. `yt-dlp --extract-audio --audio-format mp3 <url>` to download audio only (~5–15 MB for
   a 1-hour talk at 128kbps)
2. Run `openai-whisper` locally on the runner: `whisper audio.mp3 --model small --output_format txt`
   - `small` model: ~460 MB download, ~3–5 min for a 60-min talk on a free GitHub runner
   - `medium` model: ~1.5 GB, better accuracy but slower
3. Commit the `.txt` output

**Cost:** Free. GitHub Actions runner time: ~10 min for a 60-min talk on `ubuntu-latest`.

### Option B — OpenAI Whisper API (faster, costs $)
1. `yt-dlp --extract-audio --audio-format mp3` as above
2. Send audio to `https://api.openai.com/v1/audio/transcriptions` with `model=whisper-1`
3. Cost: $0.006/min → ~$0.36 for a 60-min video. Requires `OPENAI_API_KEY` secret.

## Key risk

YouTube CDN audio downloads may also be blocked from GitHub Actions IPs (same as caption
endpoints). This needs empirical testing. If both caption and audio downloads are blocked,
this approach will also fail without a proxy.

## Testing plan

1. Modify `fetch-transcript.yml` to add a Whisper fallback step after the caption attempt
2. If `yt-dlp --write-auto-sub` fails, try `yt-dlp --extract-audio`
3. If audio download succeeds, run local Whisper and commit the transcript
4. Document result

## Sources

- `yt-dlp` docs: https://github.com/yt-dlp/yt-dlp
- OpenAI Whisper (local): https://github.com/openai/whisper
- OpenAI Whisper API: https://platform.openai.com/docs/guides/speech-to-text

## Open Questions

- Are `yt-dlp` audio CDN endpoints blocked from GitHub Actions AWS IP ranges?
- What is accuracy difference between `small` and `medium` Whisper models for academic talk audio?
- Is the runtime acceptable on a free GitHub runner for talks > 60 minutes?
