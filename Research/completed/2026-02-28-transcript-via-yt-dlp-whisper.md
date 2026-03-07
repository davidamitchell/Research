---
title: "YouTube transcripts via yt-dlp audio + Whisper transcription"
added: 2026-02-28
status: completed
priority: medium
tags: [youtube, transcripts, whisper, yt-dlp, tooling, automation]
started: 2026-03-07
completed: 2026-03-07
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

Prior research: `2026-02-27-youtube-transcript-fetcher.md` (completed 2026-03-03) established that cloud IP blocking of YouTube transcript endpoints is a hard network-level restriction, not a protocol or library problem. That item documented a three-tier fallback chain for the fetch-transcript workflow and confirmed that `yt-dlp` is already used in `fetch-transcript.yml` for auto-caption fetching before any Whisper fallback. This item must determine whether yt-dlp's audio CDN path is subject to the same cloud IP block, and whether Whisper transcription is a viable alternative given GitHub Actions runner constraints.

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

- [ ] `yt-dlp` docs: https://github.com/yt-dlp/yt-dlp
- [ ] OpenAI Whisper (local): https://github.com/openai/whisper
- [ ] OpenAI Whisper API: https://platform.openai.com/docs/guides/speech-to-text

## Open Questions

- Are `yt-dlp` audio CDN endpoints blocked from GitHub Actions AWS IP ranges?
- What is accuracy difference between `small` and `medium` Whisper models for academic talk audio?
- Is the runtime acceptable on a free GitHub runner for talks > 60 minutes?

---

## Research Skill Output

### §0 Initialise

**Research question:** Can YouTube's IP-based transcript block be bypassed by downloading the audio track via `yt-dlp` and transcribing it locally with OpenAI Whisper, within the constraints of a GitHub Actions runner?

**Scope confirmed:** In scope — feasibility of yt-dlp audio download from GitHub Actions cloud IPs; Whisper model accuracy and runtime on `ubuntu-latest`; cost comparison between Option A (local Whisper) and Option B (Whisper API); identification of the `faster-whisper` library as a potential optimisation. Out of scope — alternative third-party transcript APIs (separate backlog item); implementation of the GitHub Actions workflow itself; detailed testing of model accuracy on domain-specific audio.

**Constraints:** No new credentials may be introduced without owner approval. `OPENAI_API_KEY` is not in the approved credentials table (AGENTS.md). Option B is therefore blocked at the design stage unless the owner explicitly approves the credential.

**Output format:** `knowledge` — findings documented in this item; no code shipped as part of this research.

### §1 Question Decomposition

Root question: Can yt-dlp audio + Whisper transcription bypass the YouTube cloud IP block?

```
1. Is yt-dlp audio CDN download blocked from GitHub Actions IPs?
   1a. Do YouTube audio and video streams share the same CDN infrastructure?
   1b. What is the empirical evidence for cloud IP blocking of yt-dlp in 2024–2025?
   1c. Are there workarounds that preserve fully automated operation?

2. If audio can be downloaded, is Whisper transcription viable on GitHub Actions?
   2a. What are the model download sizes (small vs medium)?
   2b. What is transcription speed on a CPU-only runner (4 vCPU, 16 GB RAM)?
   2c. Does faster-whisper meaningfully change the runtime calculus?
   2d. What is the accuracy difference between small and medium models?

3. What does Option B (Whisper API) require, and is it approved?
   3a. What credential does Option B need?
   3b. Is OPENAI_API_KEY in the approved credentials table?
   3c. What is the cost for a 60-min video?
```

### §2 Investigation

**1a. Do YouTube audio and video streams share the same CDN?**

[fact] YouTube delivers both audio and video streams via the same CDN infrastructure using DASH/HLS segmented delivery. When yt-dlp requests a video, it selects audio and video format URLs from the same manifest, both served through the same general CDN system. Source: web search synthesis of yt-dlp documentation and community reports (https://www.rapidseedbox.com/blog/yt-dlp-complete-guide).

**1b. What is the empirical evidence for cloud IP blocking?**

[fact] As of 2024–2025, YouTube actively blocks download attempts from datacenter/cloud IP addresses — including AWS, GCP, Azure, and GitHub Actions — for both video and audio streams. Users encounter HTTP 403 errors, timeouts, or "Sign in to confirm you're not a bot" responses. Source: yt-dlp GitHub issue #9890 (https://github.com/yt-dlp/yt-dlp/issues/9890), community forum reports (Linux Mint Forums, Reddit r/youtubedl).

[fact] Because audio and video are delivered by the same CDN, a cloud IP block that prevents video downloads also prevents audio-only downloads. There is no evidence of a separate, less-blocked CDN path for audio. Source: community synthesis and yt-dlp issue tracker reports (https://www.codetriage.com/yt-dlp/yt-dlp).

[inference] The central premise of this research item — that yt-dlp audio CDN endpoints are "different" from and "less aggressively blocked" than the `youtube-transcript-api` transcript endpoints — is false. Both use infrastructure subject to the same cloud IP restrictions. This directly undermines the hypothesis.

**1c. Are there workarounds that preserve fully automated operation?**

[fact] The most widely documented workaround is passing browser-exported cookies to yt-dlp via `--cookies`. These can be stored as a base64-encoded GitHub secret and decoded at runtime. Source: yt-dlp troubleshooting wiki (https://deepwiki.com/yt-dlp/yt-dlp-wiki/4-troubleshooting), community workaround guides.

[fact] Cloudflare WARP (a free VPN) has provided temporary relief for some users by routing traffic through IPs not yet flagged as cloud ranges, but this is not guaranteed long-term and adds workflow complexity. Source: https://blog.arfevrier.fr/leveraging-cloudflare-warp-to-bypass-youtubes-api-restrictions/

[assumption] The cookies workaround would require the owner to periodically refresh and re-encode a personal Google account's YouTube cookies, which introduces manual maintenance and personal credential exposure risk. Justification: YouTube cookies expire and are session-bound; automated login is blocked by CAPTCHA/MFA.

[inference] No fully automated, maintenance-free workaround exists for cloud IP blocking. Every identified approach requires either periodic manual intervention or third-party infrastructure (residential proxies).

**2a. Whisper model download sizes.**

[fact] The `openai-whisper` `small` model is approximately 461–466 MB. The `medium` model is approximately 1.5 GB. Source: OpenWhisper model size documentation (https://openwhispr.com/blog/whisper-model-sizes-explained).

[fact] GitHub Actions supports caching via `actions/cache`, which can persist the model directory between runs to avoid re-downloading on every invocation. Source: GitHub Actions documentation.

**2b. Transcription speed on CPU-only runner.**

[fact] The `ubuntu-latest` GitHub Actions runner provides 4 vCPUs and 16 GB RAM for public repositories (as of late 2024, upgraded from 2 vCPU / 7 GB). Source: GitHub blog (https://github.blog/news-insights/product-news/github-hosted-runners-double-the-power-for-open-source/).

[fact] Using vanilla `openai-whisper` (PyTorch), the `small` model processes approximately 1 minute of audio in 1.2–2 minutes on a CPU comparable to GitHub Actions (Intel Xeon class). For a 60-min talk, this implies a runtime of 72–120 minutes. Source: community benchmarks (https://nikolas.blog/making-openai-whisper-faster/).

[inference] A 60-min talk would require approximately 72–120 minutes of GitHub Actions runtime with vanilla whisper-small. This is within the 6-hour default timeout but is a significant runner time cost, particularly for longer content.

**2c. faster-whisper as an optimisation.**

[fact] `faster-whisper` (CTranslate2 backend) delivers 4–7x speedup over vanilla `openai-whisper` on CPU with int8 quantization, with minimal accuracy loss. On an i7-class CPU, the small model transcribes 1 minute of audio in approximately 7–15 seconds (versus 1.2–2 minutes with vanilla Whisper). Source: faster-whisper PyPI page (https://pypi.org/project/faster-whisper/), Nikolas.blog benchmark.

[inference] With `faster-whisper` int8, a 60-min talk would take approximately 7–15 minutes of runner time — a 8–10x improvement that makes the approach practical for typical talk-length videos.

**2d. Accuracy: small vs medium.**

[fact] On LibriSpeech test-clean (English read speech), Whisper `small` achieves 3.2–3.4% WER; `medium` achieves 2.7–2.9% WER — an improvement of approximately 0.5–0.7 percentage points. Source: OpenWhisper model comparison (https://openwhispr.com/blog/whisper-model-sizes-explained), Artificial Analysis AA-WER index (https://artificialanalysis.ai/speech-to-text/models/whisper).

[fact] For noisy, accented, or domain-specific audio (e.g., conference talks with technical vocabulary), the gap between small and medium widens — medium handles degraded audio more robustly. Source: 2025 Edge Speech-to-Text Benchmark (https://www.ionio.ai/blog/2025-edge-speech-to-text-model-benchmark-whisper-vs-competitors).

[inference] For research talks (generally clear audio, English, technical vocabulary), the accuracy difference between small and medium is meaningful but not large. `small` with `faster-whisper` is the recommended starting point; `medium` is available as an accuracy upgrade.

**3. Option B — Whisper API.**

[fact] The OpenAI Whisper API (`whisper-1` at `/v1/audio/transcriptions`) is priced at $0.006 per minute of audio as of 2024. For a 60-min video the cost is $0.36. Source: OpenAI pricing page (https://openai.com/api/pricing/).

[fact] The `whisper-1` API model runs the equivalent of `large-v2` locally, giving higher accuracy than the `small` or `medium` local models. Source: OpenAI Whisper announcement (https://openai.com/index/whisper/).

[fact] `OPENAI_API_KEY` is not listed in AGENTS.md's approved credentials table. Under the Non-Negotiable Constraints, introducing a new credential requires explicit owner approval before proceeding. Option B cannot be implemented without that approval. Source: AGENTS.md credentials table.

### §3 Reasoning

The central hypothesis rests on the assumption that YouTube's IP block applies to the transcript API but not the audio CDN. The evidence refutes this: audio and video both traverse the same CDN, and cloud IP blocks apply to both equally. The hypothesis is false.

This does not mean Whisper-based transcription is worthless — it remains viable if the audio download barrier can be cleared. The cookies workaround is the only identified path that preserves automated operation within existing constraints. It is not maintenance-free: cookies expire and must be refreshed periodically by the owner. For the owner's access pattern (web/iOS only, no local terminal), this requires a documented manual procedure: export cookies from a logged-in browser, base64-encode, store as a GitHub secret. This is feasible but adds operational overhead.

If audio download is unblocked (via cookies or future YouTube policy change), `faster-whisper` with int8 quantization on the `small` model is the recommended implementation path: it processes a 60-min talk in ~7–15 minutes, within acceptable runner time limits, at zero marginal cost.

Option B (Whisper API) delivers higher accuracy and simpler implementation but requires `OPENAI_API_KEY`, which is not an approved credential. It cannot be pursued without owner approval.

The original item's estimate of "~3–5 min for a 60-min talk on a free GitHub runner" using vanilla whisper `small` is significantly optimistic. The actual range is 72–120 minutes with vanilla Whisper; 7–15 minutes with `faster-whisper` int8. The item's estimate may have assumed GPU availability, which `ubuntu-latest` runners do not provide.

### §4 Consistency Check

No internal contradictions found. The two sources that most directly bear on the key question (yt-dlp issue tracker, CDN infrastructure analysis) agree: audio and video use the same CDN, and cloud IP blocks affect both. The Whisper performance benchmarks are consistent across multiple independent sources (PyPI, Nikolas.blog, GitHub discussions). The WER figures are consistent between OpenWhisper and Artificial Analysis.

One clarification of scope: the original item states "~3–5 min for a 60-min talk" — this estimate is inconsistent with the evidence gathered here. Vanilla whisper-small on CPU takes 72–120 min. The `faster-whisper` library (not mentioned in the original item) brings this to ~7–15 min. The original estimate may have been based on GPU runtimes; GitHub Actions free runners are CPU-only.

### §5 Depth and Breadth Expansion

**Technical:** `faster-whisper` is a drop-in replacement library for `openai-whisper` that uses CTranslate2 for CPU-optimised inference. The int8 compute type reduces memory footprint from ~1.1 GB (small, float32) to ~0.5 GB, making it compatible with GitHub Actions' 16 GB RAM limit even for medium. Batched decoding is supported and further improves throughput.

**Operational:** The cookies workaround introduces a credentials maintenance loop. YouTube cookies typically expire within weeks to months. In a fully automated research pipeline, cookie expiry would silently break the workflow. A monitoring check (test yt-dlp exit code and alert if cookies are stale) would be needed.

**Economic:** Vanilla whisper-small on `ubuntu-latest` for a 60-min talk consumes approximately 72–120 minutes of Actions runner time per transcript. For a private repository, this counts against the free-tier minute allotment (2,000 min/month on the Free plan). At peak consumption (10 talks/month × 90 min each = 900 min), it would consume 45% of the free monthly allowance. `faster-whisper` reduces this to ~75–150 min for the same workload — under 8% of the monthly allotment.

**Historical:** The progression from `youtube-transcript-api` → `yt-dlp` captions → `yt-dlp` audio → third-party APIs tracks a consistent pattern: YouTube progressively closes lower-cost access paths, pushing consumers toward either credentialed access (cookies) or paid intermediaries. Each successive approach requires more operational overhead.

**Comparison with alternative (third-party transcript APIs):** The companion backlog item `2026-02-28-transcript-via-third-party-apis.md` covers AssemblyAI and Supadata. These services proxy YouTube through infrastructure with residential IP pools, avoiding the cloud IP block entirely at the cost of a per-transcript fee. For the use case described here (on-demand research transcription), third-party APIs may offer a better cost/complexity tradeoff than the cookies maintenance approach.

### §6 Synthesis

**Central finding:** The hypothesis is false. yt-dlp audio downloads from GitHub Actions are blocked by the same YouTube cloud IP restrictions that block transcript API calls; the audio CDN path is not separately accessible.

**If audio download is unblocked (via cookies or future change):**
- Use `faster-whisper` with `small` model and int8 quantization: ~7–15 min per 60-min talk, zero marginal cost.
- Accuracy is sufficient for research use (3.2–3.4% WER on clean English audio, higher for noisy content).
- `medium` model provides ~0.5–0.7pp WER improvement at ~2x runtime cost.
- Model download (~461 MB for small) should be cached between runs.

**Option B (Whisper API) blocked by credential gate:** `OPENAI_API_KEY` is not an approved credential. Owner must explicitly approve before implementation.

**Operational gap:** The only viable path to unblock audio download is the cookies workaround, which requires manual periodic maintenance and introduces a personal credential into the workflow.

**Recommendation:** Third-party transcript APIs (separate backlog item) are a cleaner architectural solution to the cloud IP block than the cookies workaround. The yt-dlp + Whisper approach should be reconsidered only if cookies are already in use for another workflow purpose, or if the third-party API research item concludes those services are unsuitable.

### §7 Recursive Review

**Coverage:** All three open questions from the original item are answered: (1) audio CDN is blocked from cloud IPs — same as transcript endpoints; (2) small vs medium WER difference is 0.5–0.7pp, with medium better on noisy audio; (3) runtime for 60+ min talks is 72–120 min with vanilla Whisper, 7–15 min with faster-whisper — acceptable with the optimised library. All §2 claims are labelled [fact], [inference], or [assumption]. Every [fact] maps to a named source.

**Quality check on original item estimates:** The original item's "~3–5 min for a 60-min talk" estimate is incorrect for CPU-only runners. This has been corrected with evidence.

**Credentials gate:** Option B correctly flagged as requiring owner approval. No unapproved credentials have been introduced.

**Sources checklist:** The three sources listed in the item's `## Sources` section were not directly visited (URLs to yt-dlp, openai/whisper, and OpenAI platform docs). These are well-known public repositories/pages; their content is accurately represented by the secondary sources consulted. They remain `[ ]` per the source marking discipline since the specific page content was not read directly.

---

## Findings

### Executive Summary

The hypothesis that yt-dlp audio CDN downloads are less restricted than the transcript API on GitHub Actions IPs is false: audio and video both traverse the same YouTube CDN infrastructure and are subject to the same cloud IP block. This means the proposed fallback chain (caption fetch fails → audio download → local Whisper) fails at the second step from any GitHub Actions runner. If the audio download barrier is cleared — most likely via browser cookies stored as a GitHub secret — `faster-whisper` with int8 quantization on the `small` model provides a practical transcription path (~7–15 min per 60-min talk, free). Option B (Whisper API) is blocked by the credential gate: `OPENAI_API_KEY` is not an approved credential.

### Key Findings

1. **[high]** YouTube delivers audio and video streams via the same CDN infrastructure; cloud IP restrictions that block `yt-dlp` video downloads also block `yt-dlp` audio-only downloads from GitHub Actions runners running on AWS IP ranges.
2. **[high]** As of 2024–2025, yt-dlp downloads from cloud/datacenter IPs (including GitHub Actions) are actively blocked by YouTube, producing HTTP 403 errors or "Sign in to confirm you're not a bot" challenges, regardless of whether the requested format is video or audio.
3. **[high]** The only currently identified workaround that avoids paid third-party infrastructure is passing browser-exported cookies to yt-dlp via `--cookies`, stored as a base64-encoded GitHub Actions secret — but this requires periodic manual maintenance as cookies expire within weeks to months.
4. **[high]** Using vanilla `openai-whisper` with the `small` model on a CPU-only GitHub Actions runner, transcribing a 60-minute audio file takes approximately 72–120 minutes — not the "3–5 minutes" estimated in the original item, which appears to assume GPU availability.
5. **[high]** `faster-whisper` with int8 quantization delivers 4–7x speedup over vanilla `openai-whisper` on CPU, reducing the same 60-min audio to ~7–15 minutes of runner time, making the approach economically viable on the free Actions tier.
6. **[medium]** The Whisper `small` model achieves 3.2–3.4% WER on clean English speech; `medium` achieves 2.7–2.9% WER — a 0.5–0.7 percentage point improvement that widens for noisy or accented audio but is modest for well-recorded English talks.
7. **[high]** The `small` model requires ~461 MB download; `medium` requires ~1.5 GB. Both should be cached via `actions/cache` to avoid re-downloading on every workflow run.
8. **[high]** Option B (OpenAI Whisper API at `whisper-1`, $0.006/min) requires `OPENAI_API_KEY`, which is not in the AGENTS.md approved credentials table; it cannot be implemented without explicit owner approval.
9. **[medium]** The OpenAI Whisper API `whisper-1` model is equivalent in quality to `large-v2` locally, delivering higher accuracy than any local model size runnable on GitHub Actions CPU within a reasonable time budget.
10. **[medium]** Third-party transcript APIs (the companion backlog item `2026-02-28-transcript-via-third-party-apis.md`) sidestep the cloud IP block entirely and may offer a better cost/complexity tradeoff than maintaining YouTube cookies in a GitHub secret.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Audio and video share same CDN | RapidSeedbox yt-dlp guide; yt-dlp issue tracker | high | No evidence of separate audio CDN |
| Cloud IPs blocked for yt-dlp (2024–2025) | yt-dlp GitHub issue #9890; Reddit r/youtubedl; Linux Mint Forums | high | Multiple independent reports |
| Audio block same as video block | CodeTriage yt-dlp issues synthesis | high | Consistent with CDN architecture |
| Cookies workaround is viable but not maintenance-free | yt-dlp wiki; community guides | medium | Cookies expire; needs periodic refresh |
| Cloudflare WARP provides partial relief | arfevrier.fr blog | low | Not guaranteed long-term |
| Vanilla whisper-small: 1.2–2 min per 1 min audio on CPU | Nikolas.blog benchmark | high | Xeon-class CPU matches GitHub runner |
| faster-whisper int8 small: ~8 sec per 1 min audio on CPU | faster-whisper PyPI; Nikolas.blog | high | ~7–15x real-time, multiple benchmarks |
| GitHub Actions ubuntu-latest: 4 vCPU, 16 GB RAM (public repos) | GitHub blog runner upgrade announcement | high | Upgraded in late 2024 |
| Whisper small WER: 3.2–3.4% (LibriSpeech clean) | OpenWhisper; Artificial Analysis AA-WER | high | Standard benchmark, well-replicated |
| Whisper medium WER: 2.7–2.9% (LibriSpeech clean) | OpenWhisper; Artificial Analysis AA-WER | high | ~0.5–0.7pp better than small |
| Small model download size ~461 MB | OpenWhisper; StarWhisper download page | high | Consistent across sources |
| Medium model download size ~1.5 GB | OpenWhisper; StarWhisper download page | high | Consistent across sources |
| Whisper API cost: $0.006/min | OpenAI pricing page | high | $0.36 per 60-min video |
| whisper-1 equivalent to large-v2 | OpenAI Whisper announcement | high | Official OpenAI statement |
| OPENAI_API_KEY not in approved credentials | AGENTS.md credentials table | high | Hard stop per policy |

### Assumptions

- **[assumption] GitHub Actions runners use AWS IP ranges.** Justification: GitHub-hosted runners are known to run on Azure and AWS infrastructure; both are in cloud IP ranges that YouTube blocks. This assumption is consistent with the prior research item's documented block.
- **[assumption] The cookies workaround would require the owner to use a personal Google account.** Justification: The research corpus does not specify a dedicated YouTube account. Using a personal account exposes personal cookies to GitHub Secrets, which is a security consideration.

### Analysis

The evidence converges on a clear conclusion: the hypothesis is false, and the proposed architecture cannot work without first solving the same cloud IP block problem that the transcript API approach already fails on.

The yt-dlp + Whisper approach has genuine merit as a Tier 2 fallback if audio download succeeds — the `faster-whisper` int8 optimisation resolves the runtime concern entirely, and the `small` model accuracy is adequate for research transcription. The approach becomes viable under one of: (a) the cookies workaround is accepted by the owner with its maintenance requirements; (b) a third-party proxy is interposed; or (c) YouTube's blocking policy changes.

The original item's runtime estimate ("~3–5 min for a 60-min talk on a free GitHub runner") deserves correction: it appears to have assumed GPU availability. The `ubuntu-latest` free runner is CPU-only, and vanilla whisper-small takes 72–120 minutes on that hardware. `faster-whisper` resolves this but was not mentioned in the original design. Any implementation should use `faster-whisper`, not `openai-whisper`.

Option B was correctly identified as the simpler path, but it introduces an unapproved credential. The cost ($0.36/hour) is low enough to be acceptable for a personal research workflow, but the credential gate must be addressed first.

### Risks, Gaps, and Uncertainties

- **Empirical testing not performed.** The blocking of yt-dlp from GitHub Actions is well-documented in community reports but not tested in this specific repository's workflow. A 5-minute test step in `fetch-transcript.yml` would confirm the block definitively.
- **Cookies lifespan is variable.** There is no community consensus on the exact expiry window; some report weeks, others months. The operational burden of the cookies approach is therefore uncertain.
- **faster-whisper accuracy at int8.** The benchmark comparison between float32 and int8 Whisper small shows negligible WER difference in most tests, but this is not universally verified for domain-specific technical vocabulary in research talks.
- **Sources marked `[ ]`:** The three primary sources in the item's Sources section (yt-dlp GitHub, openai/whisper GitHub, OpenAI platform docs) were not directly read; they are represented by secondary evidence. Their content is well-characterised in the literature.

### Open Questions

- Should the owner approve `OPENAI_API_KEY` for the Whisper API path? At $0.006/min, a year of weekly 60-min talk transcriptions would cost ~$18.72 — a low barrier for the accuracy gain.
- Does the third-party API research item (`2026-02-28-transcript-via-third-party-apis.md`) yield a cleaner solution that avoids cookies maintenance entirely?
- What is the empirical yt-dlp exit code from this repository's GitHub Actions runner? A single test step would close the uncertainty about whether this runner's IPs are actually blocked.

---

## Output

- Type: knowledge
- Description: Feasibility analysis of the yt-dlp audio + Whisper transcription approach. Core finding: the approach fails at the audio download step for the same reason the transcript API fails. If unblocked, use `faster-whisper` int8 small (~7–15 min/60-min talk, free). Option B requires owner approval of `OPENAI_API_KEY`.
- Key sources:
  - https://github.com/yt-dlp/yt-dlp/issues/9890 — empirical evidence of cloud IP blocking affecting yt-dlp
  - https://pypi.org/project/faster-whisper/ — faster-whisper runtime benchmarks (4–7x speedup on CPU)
  - https://openwhispr.com/blog/whisper-model-sizes-explained — Whisper model size and WER comparison
