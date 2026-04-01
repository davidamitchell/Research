# Fix Incorrect Statements in Multi-Agent Repo Setup Research

## Session Summary

Fixed three factually incorrect statements in `Research/completed/2026-03-29-multi-agent-repo-setup.md` based on user-reported issues and web research verification.

## Issues Corrected

### 1. Claude iOS App Code Feature
**Incorrect statement (lines 183-185):** Research claimed Claude iOS GitHub integration is "a reading/analysis tool" and "not a coding agent"

**Correction:** Claude Code on iOS IS a full coding agent that can:
- Write code, review code, create commits, open pull requests
- Work autonomously in cloud-based sandboxed environments
- Perform the same coding tasks as the web version
- Discover and use `CLAUDE.md` and other instruction files during execution

**Sources:** 
- https://thetechportal.com/2025/10/21/anthropic-expands-ai-coding-assistant-claude-code-to-the-web-and-ios/
- https://www.engadget.com/ai/anthropic-brings-claude-code-to-ios-and-the-web-180023611.html
- https://venturebeat.com/ai/claude-code-comes-to-web-and-mobile-letting-devs-launch-parallel-jobs-on

### 2. Copilot Spaces Capabilities
**Incorrect statement (line 154):** Research claimed Copilot Spaces "does not write code to a pull request or execute tasks asynchronously"

**Correction:** While Copilot Spaces itself is primarily a Q&A tool for organizing knowledge, it CAN launch Copilot coding agent tasks that:
- Write code and create pull requests
- Execute asynchronously in GitHub Actions environments  
- Respect the repository's configuration files (`.github/copilot-instructions.md`, `AGENTS.md`)

**Sources:**
- https://www.ericksegaar.com/2025/12/08/enable-copilot-space-with-coding-agent/
- https://github.blog/changelog/2025-08-19-agents-panel-launch-copilot-coding-agent-tasks-anywhere-on-github-com/

### 3. Claude GitHub Integration Requirements
**Implicit overstatement:** Research focused heavily on `anthropics/claude-code-action` requiring extensive env vars (`ANTHROPIC_API_KEY`, GitHub App credentials)

**Clarification:** 
- The `anthropics/claude-code-action` workflow DOES require those credentials
- However, Claude assigned to GitHub Issues (per the user's example) uses a different mechanism via the installed GitHub App
- According to https://github.com/settings/installations/111267304, Claude can be assigned to issues directly without setting environment variables in the repository
- The research correctly identified the credential gap but focused on the wrong integration path

## Changes Made

Updated sections throughout the research item:
- §2 Investigation (Q4a-Q4d facts and inferences about Claude iOS)
- §2 Investigation (Q2a-Q2d facts and inferences about Copilot Spaces) 
- §3 Reasoning (updated inference about Spaces vs reading tools)
- §6 Synthesis (Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis)
- Findings section (Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis)

## Validation

- ✅ `make check` - All Ruff checks passed
- ✅ `python -m pytest tests/ -q` - 210 passed, 1 skipped, 1 expected failure (TAVILY_API_KEY not in env)

## Notes

The research item's overall recommendations remain valid (add `AGENTS.md`, `copilot-setup-steps.yml`, `CLAUDE.md`) but the categorization of surfaces was corrected to reflect:
- Claude Code on iOS: Full coding agent (not reading tool)
- Copilot Spaces: Q&A tool that can launch coding agents (not purely manual/read-only)
