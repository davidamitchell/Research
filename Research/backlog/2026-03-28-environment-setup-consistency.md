---
title: "Environment setup consistency: what each agent sees when it starts work in this repo and how to make it consistent"
added: 2026-03-28
status: backlog
priority: high
blocks: []
tags: [copilot, claude, ios, devcontainer, copilot-setup-steps, environment, github-issues]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# Environment setup consistency: what each agent sees when it starts work in this repo and how to make it consistent

## Question / Hypothesis

Given the two primary agent entry points — (A) assigning a GitHub issue to the Copilot coding agent, and (B) using the Claude iOS `code` feature — what environment does each agent start in, and what controls that environment? Does `.devcontainer/devcontainer.json` (currently absent despite W-0004) or `.github/copilot-setup-steps.yml` (absent) solve the problem? How do we ensure both agents run `make dev-install && git submodule update --init .github/skills` before starting work?

### Q1 — Copilot coding agent environment (issue-assigned work)

- What runtime does the Copilot coding agent use when it picks up an assigned GitHub issue? What OS and Python version are available by default?
- What is `.github/copilot-setup-steps.yml`? What is its exact schema? Does it run before the agent starts planning? Does it support `pip install -e ".[dev]"` and `git submodule update --init`?
- If `copilot-setup-steps.yml` does not exist, what setup does the agent perform itself? Does it discover and run `make dev-install` from the Makefile automatically?
- Does `devcontainer.json` affect the Copilot coding agent's container environment, or only Codespaces?

### Q2 — Claude iOS `code` feature environment

- When the Claude iOS `code` feature is used against this repo, does Claude operate on the live GitHub repo (via Application Programming Interface (API)), or does it clone the repo into a sandbox?
- Does Claude iOS run any setup steps (install dependencies, init submodules) before starting work? If not, what does it lack at the start of a session?
- Can Claude iOS be made to respect a setup configuration file — `devcontainer.json`, `copilot-setup-steps.yml`, or a `SETUP.md`? What mechanism, if any, causes it to run `make dev-install` or `git submodule update --init .github/skills` before starting?
- How should `.github/copilot-instructions.md` describe setup steps so Claude iOS follows them — as a plain prose instruction ("before starting work, run...") or as a structured block?

### Q3 — Consistency: is a single setup declaration possible?

- Is there a single file both agents respect as the environment setup declaration? Or do they need separate files?
- What is the correct `postCreateCommand` for `devcontainer.json` given the submodule requirement?
- What is the minimal addition to `.github/copilot-instructions.md` that causes Claude iOS to run the correct setup steps?
- Does restoring `devcontainer.json` close W-0004 entirely, or does `copilot-setup-steps.yml` also need to be created?

## Context

This repo has three agent entry points: (1) Copilot coding agent via GitHub Issues, (2) Claude iOS `code` feature, (3) `research-loop.yml` workflow. Each currently handles environment setup differently. `.devcontainer/devcontainer.json` is absent — W-0004 was incorrectly marked done and has been reopened. Every `research-loop.yml` workflow step currently re-runs Python setup inline, creating duplication. The skills submodule at `.github/skills/` must be initialised before any agent can apply skills.

Blocked on `2026-03-28-agent-instruction-loading-and-skills-access.md` (W-0035) — need to know what each agent reads before specifying what to write into those files.

## Assumptions

- **Assumption:** `copilot-setup-steps.yml` is a real GitHub feature with a defined schema. **Justification:** Referenced in GitHub Copilot documentation. Schema and behaviour unverified for this repo's use case.
- **Assumption:** `devcontainer.json` does not affect the Copilot coding agent's container. **Justification:** Prior research on Codespaces suggests devcontainer is Codespaces-scoped. Needs confirmation.

## Analysis

*(Research agent to complete)*

## Risks, Gaps, and Uncertainties

- `copilot-setup-steps.yml` schema may not support submodule initialisation.
- Claude iOS may not run any local setup steps at all — it may be read-only against the GitHub API.
- The answer may require separate mechanisms for each agent surface.

## Open Questions

- Does `.github/copilot-setup-steps.yml` run before the Copilot coding agent reads instructions or after?
- Does Claude iOS `code` feature clone the repo or operate via GitHub API?
- Can a single `devcontainer.json` serve both Codespaces and the Copilot coding agent?

---

## Research Skill Output

*(Research agent to complete)*

## Findings

*(Research agent to complete)*

## Output

- Type: knowledge, backlog-item
- Description: Confirmed environment setup behaviour for both agents; devcontainer.json spec; copilot-setup-steps.yml spec; what to add to copilot-instructions.md. Directly informs W-0036 implementation.
- Links:
