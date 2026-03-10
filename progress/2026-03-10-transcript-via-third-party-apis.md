# 2026-03-10 — Research Loop (transcript-via-third-party-apis)

**Completed:**

Research item:
- `Research/completed/2026-02-28-transcript-via-third-party-apis.md` — completed; Supadata is the only candidate that bypasses YouTube's cloud IP block AND returns verbatim transcript text; AssemblyAI's original premise (direct YouTube URL support) is incorrect — it requires yt-dlp pre-download, reintroducing the IP block; Kagi bypasses the block but returns summaries only. Supadata's free tier (100 credits/month) is sufficient for research use.

Sources consulted:
- https://deepwiki.com/supadata-ai/supadata-docs/4.1.1-transcript-service (Supadata transcript service modes and routing architecture)
- https://www.assemblyai.com/docs/faq/how-can-i-transcribe-youtube-videos (AssemblyAI primary source confirming YouTube URLs not supported in audio_url)
- https://help.kagi.com/kagi/api/summarizer.html (Kagi Universal Summarizer API documentation including YouTube support and pricing)
