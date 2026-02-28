---
title: "YouTube transcripts via third-party transcript APIs (AssemblyAI / Supadata)"
added: 2026-02-28
status: backlog
priority: low
tags: [youtube, transcripts, assemblyai, supadata, tooling, automation]
started: ~
completed: ~
output: [tool]
---

# YouTube transcripts via third-party transcript APIs (AssemblyAI / Supadata)

## Question / Hypothesis

Can a third-party transcript API (AssemblyAI, Supadata, Kagi, or similar) retrieve YouTube
transcripts from a GitHub Actions runner, bypassing YouTube's IP-based block on the
internal transcript endpoint?

## Context

YouTube blocks the internal caption endpoint (`/api/timedtext`) from cloud IP ranges.
Third-party transcript services solve this by routing through their own infrastructure
(not GitHub Actions AWS/GCP IPs), then returning the transcript via their API.

This is the highest-reliability approach if a suitable service is affordable.

## Candidates

### Supadata
- Purpose-built YouTube transcript API: `GET /v1/youtube/transcript?videoId=<id>`
- Returns structured JSON with timestamped captions
- Free tier available; paid plans from ~$9/month
- Docs: https://supadata.ai/documentation/youtube/get-transcript

### AssemblyAI
- Accepts a YouTube URL directly: `{"audio_url": "https://www.youtube.com/..."}`
- Transcribes via their own AI models (not YouTube's captions)
- Free tier: 100 hours/month. Paid: ~$0.37/hour
- Useful if Whisper-quality transcription is needed (vs. auto-captions)
- Docs: https://www.assemblyai.com/docs

### Kagi Universal Summarizer API
- Accepts a YouTube URL, returns a structured summary that includes key quotes
- Not a verbatim transcript, but may suffice for research synthesis
- $0.03 per call (based on content length)
- Docs: https://help.kagi.com/kagi/api/summarizer.html

### Tactiq / Scribbr
- Browser-extension-first services; limited API access. Less suitable for automation.

## Recommended evaluation order

1. **Supadata** — cheapest for raw transcripts, purpose-built for YouTube
2. **AssemblyAI** — best transcription quality, works without captions
3. **Kagi** — if verbatim transcript not needed, just synthesis-quality content

## Implementation sketch

```python
# Supadata example
import httpx

def fetch_transcript_supadata(video_id: str, api_key: str) -> str:
    resp = httpx.get(
        "https://api.supadata.ai/v1/youtube/transcript",
        params={"videoId": video_id, "text": "true"},
        headers={"x-api-key": api_key},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["content"]
```

A `SUPADATA_API_KEY` repository secret would be required.

## Relationship to Latest-developments-

The `davidamitchell/Latest-developments-` repo does not use any third-party transcript
APIs — it uses `youtube-transcript-api` with the same limitation. This would be new
infrastructure specific to the research workflow.

## Sources

- Supadata: https://supadata.ai/documentation/youtube/get-transcript
- AssemblyAI: https://www.assemblyai.com/docs/guides/transcribing-audio-with-a-url
- Kagi Universal Summarizer: https://help.kagi.com/kagi/api/summarizer.html

## Open Questions

- Does Supadata's free tier cover the expected volume (a few videos per month)?
- Is verbatim transcript needed, or would a Kagi-quality structured summary suffice?
- How does transcript quality compare between Supadata (YouTube captions) and AssemblyAI
  (independent transcription)?
