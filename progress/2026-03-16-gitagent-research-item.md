# Session: GitAgent Research Item

**Date:** 2026-03-16
**Slug:** gitagent-research-item
**Issue:** GitAgent — https://github.com/open-gitagent/gitagent

## What Was Done

Created a new research backlog item: `Research/backlog/2026-03-16-gitagent-declarative-agent-definition.md`

The item covers:
1. What GitAgent is and how it could be used in this repository
2. The concept of declarative agent definition as a design pattern
3. Cross-platform integration with Microsoft 365 (M365) Copilot, Amazon Web Services (AWS) Agent Core, and Azure AI Agent Service / Azure AI Foundry
4. Genealogy of declarative agent standards: OpenAI plugin manifests → Model Context Protocol (MCP) → platform-specific formats

## Conventions Followed

- Copied structure from `Research/_template.md`
- File named `YYYY-MM-DD-short-slug.md` in `Research/backlog/`
- All frontmatter fields present; `status: backlog`, `started: ~`, `completed: ~`
- Research Skill Output and Findings sections left blank for the research agent to fill
- Acronyms expanded on first use: Microsoft 365 (M365), Amazon Web Services (AWS), Model Context Protocol (MCP), Declarative Agent (DA), Azure AI Foundry
- Priority set to `high` — this repository already uses MCP servers (`.github/mcp.json`) and an autonomous research-loop workflow (`.github/workflows/research-loop.yml`); understanding the declarative agent landscape directly informs whether GitAgent could replace or complement these components
- `output: [knowledge, backlog-item]` — the research will produce knowledge and likely spawn follow-on repo improvement items

## Rationale for Scope Decisions

- GitAgent and declarative agent definition are treated as one item because GitAgent is a concrete instantiation of the broader declarative pattern. Separating them would force artificial boundaries and duplicate sources.
- M365, AWS, and Azure platforms are included in scope per the original issue request.
- Pricing, IAM deep-dives, and LLM fine-tuning are excluded to keep the item focused and researchable within the standard research-loop budget.
