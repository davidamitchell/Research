---
title: "Claude Code on the web: private submodule credential access and git submodule init mechanism"
added: 2026-03-29
status: backlog
priority: high
blocks: []
tags: [claude-code, submodules, credentials, environment-setup, agent-tooling]
started: ~
completed: ~
output: [knowledge]
---

# Claude Code on the web: private submodule credential access and git submodule init mechanism

## Research Question

Does Claude Code on the web automatically initialise git submodules when cloning a repository, and if so, can it access private submodules (such as `davidamitchell/Skills` referenced at `.github/skills/`)? If not, what is the correct mechanism to grant it access via the UI-configured setup script?

## Scope

**In scope:**
- Whether Claude Code on the web runs `git submodule update --init` during repository cloning
- Whether private submodule credential access is possible from a UI-configured setup script
- What credential mechanism is available (SSH key, GitHub App token, PAT stored in setup script environment)
- Whether the Anthropic-managed Ubuntu 24.04 VM has access to the repository's GitHub Secrets during the setup script

**Out of scope:**
- Claude Code CLI (local execution) -- different credential model
- GitHub Copilot coding agent submodule access (covered in W-0036)
- General git credential management outside the Claude Code web context

**Constraints:** Limited official documentation; may require community sources or direct testing.

## Context

W-0036 (environment setup consistency) confirmed that Claude Code on the web uses a Bash setup script configured in the Claude.ai UI. The setup script can run `make dev-install` for Python dependencies, but it is not known whether private git submodules can be initialised in this context. The `.github/skills/` directory is a read-only private submodule pointing to `davidamitchell/Skills`. If Claude Code on the web cannot access this submodule, agent sessions will run without the skill files, relying on fallback mechanisms documented in `research-prompt.md`. Understanding this gap is prerequisite to deciding whether a Claude Code web setup script can fully close the environment consistency gap, or whether the fallback approach must be treated as permanent for that surface.

## Approach

1. Check Anthropic's official Claude Code on the web documentation for any mention of private repository or submodule access
2. Search community discussions (GitHub Discussions, Reddit, Anthropic Discord) for reports of private submodule use with Claude Code web
3. Determine what environment variables or secrets are available to the UI-configured setup script at runtime
4. Check if a PAT stored in the Claude.ai project configuration (if that feature exists) could be passed to the setup script for `git submodule update`
5. Document the conclusion: fully supported, partially supported (with workaround), or not supported with no current path

## Sources

- https://code.claude.com/docs/en/claude-code-on-the-web (official Claude Code on the web documentation)
- https://docs.anthropic.com/en/docs/claude-code/settings (Claude Code settings documentation)
- Community discussions on submodule support in Claude Code web

## Research Skill Output

_Populated during research._

## Findings

_Populated on completion._
