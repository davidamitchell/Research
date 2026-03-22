# 2026-03-22 — Applied context engineering: agent skills and workflow best practices

**Issue:** More context engineering — deep dive into `muratcankoylan/Agent-Skills-for-Context-Engineering` and related public skills from awesome lists; incorporate prior repo research; focus on practical applications and workflow best practices for agent development.

## What was done

Created and completed research item `Research/completed/2026-03-22-applied-context-engineering-agent-workflows.md`.

**Sources consulted:**
- muratcankoylan/Agent-Skills-for-Context-Engineering — all 10+ skills read in full (context-fundamentals, context-degradation, multi-agent-patterns, memory-systems, tool-design, filesystem-context, evaluation, project-development)
- Meta Context Engineering (MCE) paper — Peking University State Key Laboratory of General Artificial Intelligence (2026), https://arxiv.org/pdf/2601.21557
- Prior repo research synthesised: 2026-03-08 (first principles), 2026-03-15 (compression/RAG, context layers), 2026-03-16 (declarative agents), 2026-03-17 (memory systems), 2026-03-18 (API context hubs/MCP, stateless agent failures), 2026-03-22 (coding agent skills survey)

## Key findings produced

1. Effective context capacity is 60–70% of advertised window; recall in the middle drops 10–40%
2. Five named degradation patterns (lost-in-middle, poisoning, distraction, confusion, clash) with mitigations
3. Multi-agent architectures cost ~15x single-agent chat; BrowseComp shows 80% of performance variance = token usage (model upgrades often better ROI than more agents)
4. Vercel case study: 17 specialised tools → 2 general-purpose tools improved agent performance (consolidation principle)
5. Letta filesystem agents (74% LoCoMo) beat Mem0 specialised tools (68.5%) — retrieval reliability > sophistication
6. File-system-as-state-machine implements idempotent side effects natively; composes with stateless-agent fix
7. Evaluation rubrics must separately score goal-level (accuracy, completeness) and token-level quality
8. Declarative agent manifests = infra-as-code for agents
9. MCE paper (Peking University 2026) positions muratcankoylan as foundational static skill work; dynamic evolution is research frontier
10. Primary public skill library gaps: MCP server design, human-in-the-loop patterns, multi-modal context management

## Six-part applied framework synthesised

(a) context assembly — attention-budget principles, 60-70% effective capacity ceiling
(b) architectural decisions — single vs. multi-agent, isolation vs. quality tradeoffs
(c) memory and state management — four-layer model, filesystem as primary persistent layer
(d) tool design — consolidation principle, description-as-prompt
(e) evaluation — multi-dimensional rubrics, BrowseComp token budget guidance
(f) project development workflow — acquire→prepare→process→parse→render pipeline

## New backlog items suggested (from open questions)

- MCP server design — how to expose APIs as structured agent-accessible tools
- Human-in-the-loop design patterns for high-stakes agent decisions
- Progressive disclosure for research loop (load item titles at startup, full content on demand)
