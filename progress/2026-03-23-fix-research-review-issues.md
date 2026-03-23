---
date: 2026-03-23
slug: fix-research-review-issues
status: completed
---

# Session: Fix Research Review Issues

## Objective

Close 50–100 open "Research review failed" issues by:
1. Identifying stale issues (files moved from `in-progress/` to `completed/`)
2. Fixing citation-discipline violations in completed files that still had open issues

## Analysis

Of the 100 open issues examined:

| Category | Count | Action |
|---|---|---|
| Stale: file moved from `in-progress/` to `completed/` | 83 | Closed via PR merge (Closes #NNN) |
| Active: file still exists with violations | 11 | Fixed + closed via PR merge |
| Non-review infrastructure issues | 6 | Left open (different type) |

## Files Fixed

Eight completed research files had remaining citation-discipline violations that were corrected:

| File | Changes |
|---|---|
| `2026-03-08-bbc-five-case-model.md` | 9× `[fact]` → `[inference]` for web-search-only claims |
| `2026-03-08-telegram-bot-memory-capture-retrieval.md` | ARM expanded; Oracle Cloud `[fact]` → `[inference]` |
| `2026-03-10-formal-spec-intent-alignment-agentic-coding.md` | LLM, RL, METR, PLDI acronyms expanded at first use |
| `2026-02-27-interface-and-delivery.md` | YAML expanded at first use |
| `2026-03-10-ai-concept-classification-taxonomy.md` | DIKW, LLM, MECE, OWASP, RLHF, PII, KV acronyms expanded |
| `2026-03-10-agent-evaluation-cross-repo-analysis.md` | LLM, CI, OWASP, OSS, ADK acronyms expanded |
| `2026-03-10-dikw-transformation-functions.md` | LLM, MDL, LSA, GDPR expanded; `[inference]` added to epistemic hubris claim |
| `2026-03-10-language-for-llm-agent-output.md` | PLDI, MBPP expanded; `[inference]` added to unlabeled claims |

Three files had violations already fixed in prior commits:
- `2026-03-08-slack-bot-memory-capture-retrieval.md`
- `2026-02-28-transcript-via-third-party-apis.md`
- `2026-03-10-adversarial-agents-shared-goals-multi-perspective.md`

## Issues Left Open

Six non-citation-review issues were intentionally left open:
- #157: New research backlog item suggestion
- #135, #134, #132: Workflow regression investigations
- #129: TAVILY_API_KEY rotation needed
- #107: Peer review skill feature request

## Pattern Notes

The most common citation-discipline violations were:
1. **Acronym expansion** — first use of abbreviated terms without the full form
2. **Weak citation labels** — `[fact]` on claims sourced only to "web search" (which is not independently verifiable); correct label is `[inference]`
3. **Missing epistemic labels** — evaluative or causal claims without `[fact]`/`[inference]`/`[assumption]`

The 83 stale issues arose because the research review workflow creates issues on FAIL but does not automatically close them when files pass review and are moved to `completed/`. Future improvement: add a close-on-complete workflow step.
