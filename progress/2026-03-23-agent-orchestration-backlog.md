# 2026-03-23 — Add research backlog item: agent orchestration — Anvil, Max, and multi-model gist

## Session summary

Added a new research backlog item covering agent orchestration patterns demonstrated by Burke Holland's
Anvil, the multi-agent orchestrator/planner/coder/designer gist, and Max (personal AI assistant).

## What was done

- Created `Research/backlog/2026-03-23-agent-orchestration-anvil-max.md`
  - Priority: high
  - Tags: agents, orchestration, personal-assistant, multi-model, copilot-sdk, verification, adversarial-review, skills
  - Output type: knowledge, backlog-item
  - Jump-off sources:
    - https://burkeholland.github.io/anvil/
    - https://github.com/burkeholland/anvil/tree/main
    - https://gist.github.com/burkeholland/0e68481f96e94bbb98134fa6efd00436
    - https://burkeholland.github.io/max/
    - https://github.com/burkeholland/max

## Research question captured

> What agent orchestration patterns, verification strategies, and multi-model delegation techniques are
> demonstrated by Burke Holland's Anvil, Max, and the orchestrator/planner/coder/designer multi-agent gist
> — and which of these can be directly applied or adapted to build a personal AI assistant that operates
> without a local IDE?

## Key dimensions scoped

1. Verification and trust (Anvil's SQL ledger, adversarial review, baseline snapshots)
2. Role specialisation and model routing (Opus → orchestration/planning, Codex → code, Gemini → design)
3. Parallelisation strategy by file-disjoint phases
4. Persistence and memory (SQLite-backed session memory vs. in-context)
5. Skill learning via skills.sh vs. this repo's skills submodule
6. No-local-IDE adaptation feasibility

## Outcome

Backlog item created and ready for prioritisation. Closely related to the existing
`Research/backlog/2026-03-22-agents-as-finishers-and-synthesisers.md` item — both concern
human-facing agent orchestration. They can be researched in parallel or sequenced with
this item feeding concrete implementation patterns into the finishers/synthesisers item.
