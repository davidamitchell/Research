# 2026-03-10 — Research Loop (agent-evaluation-cross-repo-analysis)

**Completed:**

Research item:
- `Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md` — completed; surveyed 8 agent frameworks (AutoGen, CrewAI, LangGraph, Pydantic AI, Agno, OpenHands, and others) to identify universal/common/novel patterns and synthesised a 5-component minimal viable evaluation framework; key finding is that tool-mediated execution is the only universal pattern while trajectory capture is the foundational evaluation primitive, and that the measurement gap between desired holistic quality metrics and what CI actually measures (pass rate, latency, cost) is the core unsolved problem in the field.

Sources consulted:
- https://arxiv.org/abs/2503.16416 (Yehudai et al., Survey on Evaluation of LLM-based Agents, 2025)
- https://hamel.dev/blog/posts/evals/ (Hamel Husain — Your AI Product Needs Evals, practitioner guide)
- https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks (METR time-horizon metric)
- https://openhands.dev/blog/sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model (OpenHands inference-time scaling results)
- https://langfuse.com/blog/2025-03-19-ai-agent-comparison (Langfuse open-source agent framework comparison)
