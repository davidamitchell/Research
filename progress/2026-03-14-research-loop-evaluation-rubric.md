# 2026-03-14 — Research Loop (research-loop-evaluation-rubric)

**Completed:**

Research item:
- `Research/completed/2026-03-10-research-loop-evaluation-rubric.md` — completed; a custom 9-dimension LLM-as-judge rubric using the GitHub Copilot CLI is the only feasible automated eval gate for this repository's research loop, given the no-new-credentials constraint that rules out DeepEval, Pydantic Evals, and agentevals; the rubric dimensions (claim sourcing, acronym expansion, hedge control, finding completeness, finding quality, evidence map coverage, assumption labelling, cross-section consistency, AI slop absence) each correspond to a distinct, observable failure mode in research output quality.

Sources consulted:
- https://ai.pydantic.dev/evals/ (Pydantic Evals documentation — framework features and usage)
- https://pydantic.dev/articles/llm-as-a-judge (Pydantic LLM-as-a-judge article — structured rubric design rationale)
- https://hamel.dev/blog/posts/evals/ (Hamel Husain evals guide — practitioner perspective on rubric design and calibration)
- https://www.confident-ai.com/blog/llm-agent-evaluation-complete-guide (DeepEval agent evaluation guide — framework comparison)
- https://github.com/langchain-ai/agentevals (agentevals README — LangSmith dependency and credential requirements)

## Mini-Retro

1. **Did the process work?** Yes. The full §0–§7 protocol produced a clear, implementable rubric and CI design. Review passed on the first attempt with no issues opened.
2. **What slowed down or went wrong?** The Tavily MCP server was unavailable (invalid API key in this Actions environment), requiring fallback to `web_fetch` and `web_search` for all external source retrieval. Context was also compacted mid-session, requiring careful resumption from the draft-and-push step.
3. **What single change would prevent this next time?** Nothing to fix for the Tavily issue — the fallback worked correctly. For context compaction: the session summary was accurate and complete; the resumption was clean.
4. **Is this a pattern?** The Tavily MCP unavailability in GitHub Actions is a recurring constraint (seen in prior sessions). The fallback to `web_fetch`/`web_search` is the established workaround. No new pattern to document.
