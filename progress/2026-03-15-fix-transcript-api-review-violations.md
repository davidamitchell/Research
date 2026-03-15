---
date: 2026-05-29
slug: fix-transcript-api-review-violations
status: complete
---

# Fix review violations in transcript-via-third-party-apis

## What was done

Applied targeted fixes to `Research/completed/2026-02-28-transcript-via-third-party-apis.md` addressing 14 violations across four review dimensions:

**citation-discipline (5 fixes)**
- Expanded CDN → Content Delivery Network (CDN) (§0, first occurrence)
- Expanded SDK → Software Development Kit (SDK) (§1, first occurrence)
- Expanded FAQ → Frequently Asked Questions (FAQ) (§2 sources, first occurrence)
- Changed `[fact]` → `[inference]` for Supadata Whisper model claim (§2 2a; source was web search synthesis, not a direct verifiable URL)
- Changed `[fact]` → `[inference]` for AssemblyAI architecture claim sourced from pricing page (§2 2b; citation-scope mismatch)

**speculation-control (5 fixes)**
- Added `[inference]` to Conclusion 3a "adequate" judgment
- Added `Opinion:` to "Supadata wins on both dimensions" (§5 Economic lens)
- Added `[inference]` to "correct implementation path" in §6 Executive summary and Findings Executive Summary
- Added `[inference]` to "sufficient indefinitely" in §6 Key Finding 6 and Findings Key Finding 6
- Added `Opinion:` to "This is not a minor detail" (Findings Analysis)

**remove-ai-slop (2 fixes)**
- Removed meta-framing sentence "The research question resolves to a service-selection decision with a clear winner." — content following it states the point directly
- Removed "The Gemini comparison is instructive:" framing sentence — paragraph opens directly with the substantive observation

## Commit

`799222e` — research: fix review violations in transcript-via-third-party-apis
