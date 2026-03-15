# Session log: prompt injection backlog item

**Date:** 2026-03-15
**Slug:** prompt-injection-backlog
**Issue:** New research backlog item — prompt injection threat landscape

## Summary

Added a new research backlog item for prompt injection. The issue requested research into:
- Who is exploiting prompt injection in agentic AI systems
- Who is building defences
- What current research is happening

## What was done

Created `Research/backlog/2026-03-15-prompt-injection-threat-landscape.md`.

**Priority:** `high` — prompt injection in agentic systems is a strategically urgent security threat with clear downstream impact on agent architecture decisions. Agents with real-world action capabilities (file writes, API calls, email) face qualitatively higher risk than chatbot-era systems.

**Connections to existing research:**
- Builds directly on `2026-02-28-ai-strategy-security-focus.md` which identified prompt injection as one attack vector in the broader AI system security taxonomy — this item goes deep on injection specifically.
- Relates to `2026-03-10-adversarial-agents-shared-goals-multi-perspective.md` — the adversarial collaboration design pattern is vulnerable to indirect injection attacks that can subvert agent goals from the environment.

**Key framing choices:**
- Scoped to 2023–2025 to focus on the agentic AI era where injection consequences escalated from nuisance to real-world action.
- Distinguished direct (user-controlled input) vs. indirect (environment-sourced: web pages, docs, tool outputs) injection — the indirect variant is the high-priority threat for agents.
- Starting sources include OWASP LLM Top 10 v2, MITRE ATLAS, Simon Willison's injection catalogue, Greshake et al. foundational indirect injection paper, and vendor red-team disclosures.

## No code changes made

This is a research item addition only. No source code, workflows, or configuration was changed.
