# Session: Citation-discipline fixes across 11 research files

**Date:** 2026-03-10  
**Issues addressed:** #88, #89, #90, #92, #93, #94, #97, #99, #100, #101, #106

## What was done

Fixed citation-discipline violations in research markdown files. Two categories of violations were addressed:

1. **Acronym expansion at first use** — added "Full Name (ABBR)" pattern on the first occurrence of each unexpanded acronym
2. **Epistemic labels** — changed `[fact]` to `[inference]` for claims sourced from unverifiable web search synthesis; added missing `[inference]` labels on inferential claims

## Files changed (8)

| File | Changes |
|---|---|
| `bbc-five-case-model.md` | 9× `[fact]` → `[inference]` for web-search-only sourced claims |
| `telegram-bot-memory-capture-retrieval.md` | ARM expansion fixed; E6 `[fact]` → `[inference]` |
| `formal-spec-intent-alignment-agentic-coding.md` | Expand LLM, RL, METR, PLDI at first use |
| `interface-and-delivery.md` | Expand YAML at first use |
| `ai-concept-classification-taxonomy.md` | Expand DIKW, LLM, MECE, OWASP, RLHF, PII, KV at first use |
| `agent-evaluation-cross-repo-analysis.md` | Expand LLM, CI, OWASP, OSS, ADK at first use |
| `dikw-transformation-functions.md` | Expand LLM, MDL, LSA, GDPR; add `[inference]` to epistemic hubris claim |
| `language-for-llm-agent-output.md` | Expand PLDI, MBPP; add `[inference]` to 40-year history and EU AI Act claims |

## Files requiring no changes (3)

- `slack-bot-memory-capture-retrieval.md` — all violations fixed in prior commit a0d3558
- `transcript-via-third-party-apis.md` — CDN/SDK/FAQ already expanded; Supadata 2a already `[inference]`
- `adversarial-agents-shared-goals-multi-perspective.md` — all acronyms already expanded

## Key rule applied

> Acronym expansion = change ONLY the first occurrence to "Full Term (ABBR)". All subsequent uses remain as the bare acronym.
