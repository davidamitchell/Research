# Session Log: oh-my-codex Patterns Research

**Date:** 2026-04-03
**Slug:** oh-my-codex-patterns
**Issue:** Oh my codex (#davidamitchell/Research)

## What Was Done

- Researched oh-my-codex (OMX) and the AGENTS.md ecosystem
- Surveyed similar projects: AGENTS.md standard, CLAUDE.md, GEMINI.md, SKILL.md patterns
- Audited current davidamitchell repo setup (Research, Skills, Multi-Agent-Testing, Agent-Evaluation)
- Created and completed research item: `Research/completed/2026-04-03-oh-my-codex-patterns.md`
- Followed full research workflow: backlog → in-progress → reviewing → completed

## Key Findings

1. OMX's layered architecture (AGENTS.md operating contract + narrower role prompts) is transferable
2. The CPEV workflow pattern (Clarify, Plan, Execute, Verify) prevents scope drift
3. AGENTS.md is a cross-agent standard adopted by 15+ tools; copilot-instructions.md is Copilot-specific
4. Three-tier boundary statements (always/ask first/never) outperform prose constraints empirically
5. The Skills submodule (16 skills) has no discoverability index
6. Model routing and persistent state are absent from the current setup

## Improvement Candidates (for backlog)

- Add root AGENTS.md to each active davidamitchell repo
- Add three-tier boundary section to copilot-instructions.md
- Add a scope-clarification skill for ambiguous research questions
- Add model routing guidance to copilot-instructions.md
- Add skills index to davidamitchell/Skills README

## Mini-Retro

**What went well:** Research was thorough; sources were verifiable with URLs; all claim labels applied; no em-dashes.

**What could improve:** The Agent-Evaluation repo contents were not fully inspected due to API access limitations; a follow-up backlog item to audit its findings would strengthen the recommendations.

**Patterns noted:** The recurring pattern of "Copilot-specific vs cross-agent" is the central tension across all active repos and will be a recurring theme in future sessions.
