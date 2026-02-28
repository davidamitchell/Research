---
title: "Interface and delivery: how to surface research outputs"
added: 2026-02-27
status: backlog
priority: low
tags: [interface, delivery, output, ux]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# Interface and delivery: how to surface research outputs

## Question / Hypothesis

Once research is complete and outputs are produced, how should they be surfaced and delivered to the people (or agents) who need them? What interfaces make research outputs most usable?

## Context

Research outputs currently live as Markdown files in `Research/completed/`. This is good for git history but poor for discovery and consumption. Better interfaces might include:

- **CLI**: query completed research, list by tag, search by keyword
- **Static site**: generated from `Research/completed/` for browsing
- **Email digest**: a weekly summary of newly completed research (using the Latest-developments- pattern)
- **Agent-readable knowledge base**: structured format that AI agents can query
- **MCP tool**: expose research items as an MCP server tool

The right answer depends on who the consumers are (human researcher, AI agent, or both).

## Scope

**In scope:**
- CLI interface for research queries (most immediate value)
- Agent-readable format (JSON or structured Markdown for MCP)
- Email digest as a future option

**Out of scope:**
- Full web app or SaaS product

## Approach

1. Define the consumers and their use patterns
2. Survey interface options: CLI vs static site vs email digest vs MCP
3. Prototype the CLI query interface (most immediate)
4. Evaluate MCP server approach for agent-readable research

## Sources

- [ ] `davidamitchell/Latest-developments-` — email digest pattern
- [ ] MCP tool creation docs: https://modelcontextprotocol.io/docs/concepts/tools

## Findings

*(to be filled in)*

## Output

- Type: knowledge, backlog-item
- Description: Interface strategy; CLI query commands; potential MCP server design
