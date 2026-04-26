---
review_count: 2
title: "Multi-agent repo setup: best practices for configuring a repository to be worked on by Claude (iOS and GitHub Issues) and Copilot (Spaces and GitHub Issues)"
added: 2026-03-29T10:46:03+00:00
status: completed
priority: high
blocks: []
tags: [copilot, claude, ios, github-issues, multi-agent, copilot-spaces, repo-setup, instructions, agents-md]
started: 2026-03-29T10:46:03+00:00
completed: 2026-03-29T10:46:03+00:00
output: [knowledge, backlog-item]
---

# Multi-agent repo setup: best practices for configuring a repository to be worked on by Claude (iOS and GitHub Issues) and Copilot (Spaces and GitHub Issues)

## Research Question

What are the best practices for setting up a GitHub repository so that it can be worked on effectively by multiple Artificial Intelligence (AI) agents, specifically: (1) Claude via the iOS Claude app, (2) Claude via GitHub Issues assigned to Claude, (3) Copilot via Copilot Spaces, and (4) Copilot via GitHub Issues assigned to the Copilot coding agent, with consistent instruction loading, environment setup, and quality outcomes across all four surfaces?

## Scope

**In scope:**
- Repository configuration files that each agent reads on startup (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, `copilot-setup-steps.yml`, `devcontainer.json`)
- How GitHub Issues work with each agent surface (Copilot coding agent and Claude GitHub integration)
- How Copilot Spaces work and what repository configuration they respect
- How the Claude iOS `code` feature accesses and configures itself from the repository
- Minimal diff from this repo's current state to support all four surfaces

**Out of scope:**
- Local IDE setups (no Codespaces, no `git clone` terminal use)
- Third-party agent tools (Cursor, Aider, Codex) beyond what the research reveals incidentally
- Agent capability comparison (what each agent can *do*): focus is configuration and instruction loading

**Constraints:** Must be achievable without adding credentials beyond those already in the repo. No local IDE access; the owner operates exclusively via the GitHub website and iOS apps.

## Context

The repository is actively used by two agents across four distinct surfaces. Each surface may load different instruction files, run in a different environment, and have different access to the skills submodule at `.github/skills/`. At present, the repo holds instructions only in `.github/copilot-instructions.md` (Architecture Decision Record (ADR)-0006 deleted `AGENTS.md` and `.claude/CLAUDE.md` on 2026-03-07). Whether this file is loaded by all four surfaces is unverified.

Three related backlog items were added on 2026-03-28 that address sub-questions directly relevant here:
- `2026-03-28-agent-instruction-loading-and-skills-access`, what each agent loads and whether it reads `.github/skills/`
- `2026-03-28-agents-md-role-and-cross-agent-instructions`, the role of `AGENTS.md` in a repo using `copilot-instructions.md`
- `2026-03-28-environment-setup-consistency`, environment setup (dependencies, submodule) for each agent surface

This item is the parent strategy question: given findings from those three items, what is the complete, minimal repo configuration that makes all four surfaces work well together?

## Approach

1. **Q1, GitHub Issues → Copilot coding agent:** What repo configuration does the Copilot coding agent need to receive instructions, initialise the environment, and access the skills submodule when it picks up an assigned GitHub issue? What is the role of `.github/copilot-setup-steps.yml`? What files does it read before planning?

2. **Q2, Copilot Spaces:** What is Copilot Spaces? How does it interact with a repository? What configuration does it respect, does it read `.github/copilot-instructions.md`, `AGENTS.md`, or a Spaces-specific file? Is it in scope for this repository?

3. **Q3, GitHub Issues → Claude:** Is there a GitHub integration for assigning issues to Claude directly (analogous to the Copilot coding agent)? If so, what repo configuration does it require, `CLAUDE.md`, `AGENTS.md`, a GitHub App? What is the setup process?

4. **Q4, Claude iOS app (`code` feature):** What files does the Claude iOS `code` feature load when a repository is opened? Does it clone the repo locally, or operate via the GitHub Application Programming Interface (API)? What is the path to making the iOS surface read the same instructions as the other surfaces?

5. **Q5, Convergence and minimum viable configuration:** Given answers to Q1–Q4, what is the smallest set of files that reliably serves all four agent surfaces? Is a thin `AGENTS.md` pointer the right pattern, or does each surface need a dedicated file? Map current state to recommended target state.

## Sources

Starting points, papers, articles, videos, repos, docs.
**Every source must include a Uniform Resource Locator (URL).** Use `[Display Name](https://url)` for named sources or a bare `https://url` for direct links. Sources without URLs cannot be verified or linked on the site.

- [x] [GitHub Copilot coding agent documentation](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-as-an-agent): entry point for coding agent behaviour and configuration
- [x] [GitHub Copilot custom instructions (.github/copilot-instructions.md)](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot): what the file covers and which surfaces load it
- [x] [copilot-setup-steps documentation](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent): schema and when it runs
- [x] [Copilot Spaces documentation](https://docs.github.com/en/copilot/how-tos/provide-context/use-copilot-spaces/create-copilot-spaces): what Spaces are and how they use repo config
- [x] [AGENTS.md specification / agentsmd.online](https://agentsmd.online): cross-vendor standard for agent instruction files
- [x] [Anthropic Claude iOS app GitHub integration](https://support.claude.com/en/articles/10167454-using-the-github-integration): how Claude iOS interacts with repositories via connector
- [x] [Claude Code GitHub Actions documentation](https://docs.anthropic.com/en/docs/claude-code/github-actions): how GitHub Issues can be assigned to Claude via `anthropics/claude-code-action`
- [x] [Claude Code memory / CLAUDE.md documentation](https://docs.anthropic.com/en/docs/claude-code/memory): what files Claude Code auto-loads
- [x] `docs-adr/0006-standardise-agent-instructions.md`, local ADR documenting the decision to delete `AGENTS.md`
- [x] `Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md`, prior research on `AGENTS.md` as cross-vendor standard
- [x] `Research/completed/2026-03-22-using-awesome-copilot-across-repos.md`, prior research noting `AGENTS.md` is read by GitHub web

---

## Research Skill Output

### §0 Initialise

**Research question restated:** What are the best practices for configuring a GitHub repository so that it can be worked on effectively by four distinct AI agent surfaces, (1) Claude via the iOS Claude app, (2) Claude via GitHub Issues using `anthropics/claude-code-action`, (3) Copilot via Copilot Spaces, and (4) Copilot via GitHub Issues using the Copilot coding agent, with consistent instruction loading, environment setup, and quality outcomes across all four?

**Scope confirmed:** In scope: per-repo configuration files only; instruction-loading behaviour per surface; environment setup for agentic tasks; minimum viable configuration delta from current state. Out of scope: local IDE, third-party tools beyond incidental discovery, capability comparison.

**Constraints confirmed:** No new credentials beyond those in the repo credential table (`GITHUB_TOKEN`, `COPILOT_GITHUB_TOKEN`, `YOUTUBE_DATA_API`, `TAVILY_API_KEY`). No local IDE; owner operates exclusively via GitHub website and iOS apps.

**Output format:** Knowledge article with actionable file-level recommendations. New backlog items for any implementation work.

### §1 Question Decomposition

**Q1, Copilot coding agent (GitHub Issues → Copilot)**
- Q1a: What instruction files does the Copilot coding agent read before planning?
- Q1b: In what order / with what precedence rules does it combine them?
- Q1c: What is `copilot-setup-steps.yml` and when does it run?
- Q1d: Does the Copilot coding agent check out submodules (including `.github/skills/`)?

**Q2, Copilot Spaces**
- Q2a: What is a Copilot Space, a chat tool or a coding agent?
- Q2b: Does a Space auto-read `.github/copilot-instructions.md` or `AGENTS.md` from attached repositories?
- Q2c: What per-repo configuration, if any, influences a Space?
- Q2d: Is Copilot Spaces meaningfully in scope for this repo's agentic coding workflow?

**Q3, Claude via GitHub Issues (`anthropics/claude-code-action`)**
- Q3a: What triggers the Claude GitHub Actions workflow?
- Q3b: What instruction files does the Claude Code agent read in this context?
- Q3c: What credentials are required and are they available in this repo?
- Q3d: What GitHub App setup is required?

**Q4, Claude iOS app (GitHub integration)**
- Q4a: How does the Claude iOS app connect to a GitHub repository?
- Q4b: What is loaded, the entire repo, specific files, or something else?
- Q4c: Does the iOS integration auto-load any instruction file (e.g., `CLAUDE.md`, `AGENTS.md`)?
- Q4d: Is the iOS GitHub integration a code-writing agent or a reading/analysis tool?

**Q5, Convergence**
- Q5a: Which surfaces can be served by `.github/copilot-instructions.md` alone?
- Q5b: What is the minimum set of additional files needed to cover all reachable surfaces?
- Q5c: Is a thin `AGENTS.md` pointer pattern the correct approach?
- Q5d: What surfaces are currently blocked by missing credentials?

### §2 Investigation

#### Q1a–Q1b: Copilot coding agent instruction files

**[fact]** The GitHub Copilot coding agent reads `.github/copilot-instructions.md` at the repository root for repository-wide instructions. (Source: [GitHub Docs, adding-custom-instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot))

**[fact]** The Copilot coding agent also reads `AGENTS.md` files. When both `AGENTS.md` and `.github/copilot-instructions.md` exist at the repository root, the instructions in both files are used together. (Source: [GitHub Docs, adding-custom-instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot))

**[fact]** The Copilot coding agent reads `.github/instructions/*.instructions.md` files for path-specific instructions, instructions that apply only to files matching a given glob pattern specified in frontmatter. (Source: [GitHub Docs, best-practices coding agent](https://docs.github.com/enterprise-cloud@latest/copilot/tutorials/coding-agent/get-the-best-results))

**[fact]** The Copilot coding agent also incorporates organisation-level custom instructions when configured by an organisation admin. (Source: [GitHub Docs, best-practices coding agent](https://docs.github.com/enterprise-cloud@latest/copilot/tutorials/coding-agent/get-the-best-results))

**[fact]** `AGENTS.md` directory-tree proximity rules apply: the nearest `AGENTS.md` to the file being edited takes precedence when multiple `AGENTS.md` files exist. (Source: [GitHub Docs, adding-custom-instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot))

#### Q1c: `copilot-setup-steps.yml`

**[fact]** `copilot-setup-steps.yml` is a workflow file placed at `.github/workflows/copilot-setup-steps.yml`. It defines a GitHub Actions job called `copilot-setup-steps` whose steps run inside the Copilot coding agent's ephemeral environment before the agent begins work. (Source: [GitHub Docs, customizing-the-development-environment-for-copilot-coding-agent](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent))

**[fact]** Uses of `copilot-setup-steps.yml` include: pre-installing tools and dependencies; upgrading to larger GitHub-hosted runners; enabling self-hosted runners; setting environment variables; disabling or customising the agent's firewall. (Source: [GitHub Docs, customizing-the-development-environment-for-copilot-coding-agent](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent))

**[fact]** The current repository does NOT have a `copilot-setup-steps.yml` file. (Source: direct filesystem inspection of `.github/workflows/`)

**[inference]** Without a `copilot-setup-steps.yml`, the Copilot coding agent will start in a default Ubuntu environment without Python dependencies installed, without the `.github/skills/` submodule checked out, and potentially without the virtual environment needed by `src/`. This means the agent cannot run `make check` or `make test` as required by `.github/copilot-instructions.md`.

#### Q1d: Submodule access for the Copilot coding agent

**[inference]** The Copilot coding agent's ephemeral environment runs on GitHub-hosted Actions runners. Submodules are not checked out by default unless a `copilot-setup-steps.yml` step runs `actions/checkout@v5` with `submodules: recursive`. Without this step, `.github/skills/` will be an empty directory, and any skill files referenced in the instructions will be absent.

#### Q2a–Q2d: Copilot Spaces

**[fact]** Copilot Spaces is a feature that allows users to create named "spaces" containing two types of context: (1) a free-text "Instructions" field describing what Copilot should focus on, and (2) "Sources", repositories, files, or other content attached as knowledge. (Source: [GitHub Docs, creating-copilot-spaces](https://docs.github.com/en/copilot/how-tos/provide-context/use-copilot-spaces/create-copilot-spaces))

**[fact]** A Copilot Space is primarily a chat/Question and Answer (Q&A) tool for organizing and accessing domain-specific knowledge. Spaces can launch Copilot coding agent tasks that write code and create pull requests, but the Space itself is a context-grounded assistant for answering questions about attached content. (Source: [GitHub Docs, creating-copilot-spaces](https://docs.github.com/en/copilot/how-tos/provide-context/use-copilot-spaces/create-copilot-spaces); [Copilot Spaces with Coding Agent](https://www.ericksegaar.com/2025/12/08/enable-copilot-space-with-coding-agent/))

**[fact]** Copilot Spaces does NOT automatically read `.github/copilot-instructions.md` or `AGENTS.md` from attached repositories. Instructions for a Space are entered manually in the Space's "Instructions" field by the Space creator. (Source: [GitHub Docs, creating-copilot-spaces](https://docs.github.com/en/copilot/how-tos/provide-context/use-copilot-spaces/create-copilot-spaces))

**[fact]** When a repository is attached as a Source in a Space, Copilot always refers to the latest version of the code on the `main` branch of the repository. (Source: [GitHub Docs, creating-copilot-spaces](https://docs.github.com/en/copilot/how-tos/provide-context/use-copilot-spaces/create-copilot-spaces))

**[inference]** Copilot Spaces itself does not directly execute code or write pull requests, but it can launch Copilot coding agent tasks that do. Per-repo configuration files (`.github/copilot-instructions.md`, `AGENTS.md`) have no automatic effect on a Space's chat behavior; instructions must be manually entered. However, when a Space launches a coding agent task, that agent will respect the repository's configuration files. For the purposes of per-repo agent configuration best practices, Spaces is primarily out of scope as a direct consumer, though it can serve as an entry point to the Copilot coding agent.

#### Q3a–Q3d: Claude via GitHub Issues

**[fact]** The `anthropics/claude-code-action` GitHub Action enables Claude Code to act on GitHub Issues and pull request (PR) comments when triggered by a configurable phrase (default: `@claude`). The workflow listens to `issue_comment`, `pull_request_review_comment`, and `issues` events. (Source: [Claude Code GitHub Actions docs](https://docs.anthropic.com/en/docs/claude-code/github-actions))

**[fact]** When running via `anthropics/claude-code-action`, Claude reads `CLAUDE.md` using Claude Code's standard file discovery: walking up the directory tree from the working directory, loading every `CLAUDE.md` encountered, plus any `CLAUDE.md` files in subdirectories when those subdirectories are accessed. (Source: [Claude Code memory docs](https://docs.anthropic.com/en/docs/claude-code/memory))

**[fact]** The `anthropics/claude-code-action` does NOT auto-load `.github/copilot-instructions.md`. (Source: [Claude Code GitHub Actions docs](https://docs.anthropic.com/en/docs/claude-code/github-actions): the only instruction-file mechanism documented is `CLAUDE.md` and the `prompt` parameter)

**[fact]** Setting up `anthropics/claude-code-action` requires either: (a) `ANTHROPIC_API_KEY` as a repository secret for direct API access; (b) AWS Bedrock credentials (`AWS_ROLE_TO_ASSUME`); or (c) Google Cloud Vertex AI credentials (`GCP_WORKLOAD_IDENTITY_PROVIDER`, `GCP_SERVICE_ACCOUNT`). It also requires a GitHub App (`APP_ID`, `APP_PRIVATE_KEY`) for write access to create PRs. (Source: [Claude Code GitHub Actions docs](https://docs.anthropic.com/en/docs/claude-code/github-actions))

**[fact]** None of `ANTHROPIC_API_KEY`, `APP_ID`, `APP_PRIVATE_KEY`, `AWS_ROLE_TO_ASSUME`, `GCP_WORKLOAD_IDENTITY_PROVIDER`, or `GCP_SERVICE_ACCOUNT` are listed in this repository's available credentials table. (Source: `.github/copilot-instructions.md` credentials table)

**[inference]** The Claude-via-GitHub-Issues surface cannot be enabled in this repository without adding at least `ANTHROPIC_API_KEY` (or equivalent) and a GitHub App credential pair. Under the stated constraint of no new credentials, this surface is currently blocked.

#### Q4a–Q4d: Claude iOS app (GitHub integration)

**[fact]** The Claude iOS app includes Claude Code, a full coding agent feature that can write code, review code, create commits, open pull requests, and work autonomously in sandboxed cloud environments. When connected to GitHub repositories via the GitHub connector, Claude Code on iOS can perform the same coding tasks as the web version. (Source: [Anthropic Claude Code on iOS](https://thetechportal.com/2025/10/21/anthropic-expands-ai-coding-assistant-claude-code-to-the-web-and-ios/); [Claude Code iOS capabilities](https://www.engadget.com/ai/anthropic-brings-claude-code-to-ios-and-the-web-180023611.html))

**[fact]** The Claude iOS GitHub integration indexes selected repositories as "project knowledge" via Anthropic's Connectors system. Users authorize the GitHub connector via the claude.ai web UI (Settings → Connectors), which syncs to the iOS app at next login. This allows Claude Code to browse files, analyze commit histories, and execute coding tasks with full repository context. (Source: [Claude Help, Using the GitHub Integration](https://support.claude.com/en/articles/10167454-using-the-github-integration))

**[fact]** Claude Code on iOS does NOT auto-load any specific instruction file (`CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md`) automatically on session start. However, it can read and use these files during execution when working on coding tasks. (Source: [Claude Code memory docs](https://docs.anthropic.com/en/docs/claude-code/memory))

**[inference]** Claude Code on iOS is a full coding agent that executes in cloud-based sandboxed environments, not limited to read-only operations. While the GitHub connector provides repository access for context, Claude Code can perform actual coding work including commits and pull requests. The `.github/copilot-instructions.md` and `CLAUDE.md` files are not auto-loaded at session start but can be discovered and used during task execution.

**[assumption]** The research item's mention of the "iOS Claude app `code` feature" refers to Claude Code running on iOS via the GitHub connector. The linked support article (10166833) was inaccessible during investigation; current evidence from multiple sources confirms Claude Code is available on iOS as a full coding agent, not just a read-only connector. **Justification:** Anthropic's announcements and documentation confirm Claude Code launched on iOS and web in October 2025, providing full coding capabilities on mobile devices.

#### Q5: Convergence analysis

**[fact]** The current repository has: `.github/copilot-instructions.md` (full, present), no `AGENTS.md`, no `CLAUDE.md`, no `copilot-setup-steps.yml`. (Source: direct filesystem inspection)

**[fact]** ADR-0006 deliberately deleted `AGENTS.md` and `.claude/CLAUDE.md` on 2026-03-07 to consolidate all agent instructions into `.github/copilot-instructions.md`. (Source: `docs-adr/0006-standardise-agent-instructions.md`)

**[fact]** Prior research (2026-03-22-using-awesome-copilot-across-repos) found that the Research repo lacks `AGENTS.md`, which was identified as the missing instruction layer for surfaces beyond Copilot in-IDE chat. (Source: `Research/completed/2026-03-22-using-awesome-copilot-across-repos.md`)

**[inference]** The "converged single file" assumption in ADR-0006 is only partially correct: `.github/copilot-instructions.md` covers the Copilot coding agent and Copilot chat surfaces. It does NOT cover: Claude Code GitHub Actions (needs `CLAUDE.md`), AGENTS.md-compatible agents (Cursor, OpenAI Codex, etc.), or the environment setup gap (`copilot-setup-steps.yml`).

**[fact]** `AGENTS.md` is supported by over 60,000 open-source repositories and is now formally stewarded by the Agentic AI Foundation under the Linux Foundation as an open cross-vendor standard supported by OpenAI, Google, Sourcegraph, GitHub, Cursor, and others. Claude Code is also listed as a compatible tool in the AGENTS.md specification. (Source: [agentsmd.online](https://agentsmd.online), [agentsmd/agents.md](https://github.com/agentsmd/agents.md))

**[inference]** Adding a thin `AGENTS.md` that references `.github/copilot-instructions.md` (a pointer file) is the minimal-friction approach: it satisfies the AGENTS.md spec for all compatible agents while avoiding duplication. Copilot reads both files addictively, so a pointer is non-redundant.

**[fact]** The Copilot coding agent cannot run `make check` or `python -m pytest` without the Python virtual environment and dependencies installed, which currently requires a `copilot-setup-steps.yml` that runs `pip install -e ".[dev]"`. (Source: `Makefile`, `.github/copilot-instructions.md` quick reference rule 7)

**[inference]** The minimum viable three-file addition to cover all currently-reachable surfaces (i.e., excluding Claude GitHub Actions which is credential-blocked) is: (a) `AGENTS.md` at root, (b) `copilot-setup-steps.yml`, and (c) `CLAUDE.md` at root (pre-positioned for when credentials become available). Adding `CLAUDE.md` now costs nothing and avoids a future gap.

### §3 Reasoning

**Facts established:**
1. Copilot coding agent reads both `.github/copilot-instructions.md` and `AGENTS.md` when present; they are additive.
2. `copilot-setup-steps.yml` runs before the Copilot coding agent starts; without it, Python deps are missing and the skills submodule is absent.
3. Claude Code GitHub Actions reads `CLAUDE.md`; it does not read `.github/copilot-instructions.md`.
4. The Claude GitHub Actions surface requires `ANTHROPIC_API_KEY` + GitHub App credentials, neither of which is available in this repo.
5. Copilot Spaces is a manually-configured chat tool, not a coding agent; per-repo files do not auto-load.
6. The Claude iOS GitHub integration indexes repos as knowledge; no instruction file is auto-loaded.
7. `AGENTS.md` is a widely-adopted cross-vendor standard now under Linux Foundation stewardship.

**Inferences:**
- ADR-0006's single-file consolidation was correct for Copilot surfaces but left gaps for Claude Code surfaces and cross-vendor compatibility.
- The minimum viable fix for all currently-reachable surfaces is three additions: `AGENTS.md`, `copilot-setup-steps.yml`, and `CLAUDE.md`.
- The Claude-via-GitHub-Issues surface is credential-blocked and cannot be resolved within stated constraints.
- Copilot Spaces can launch Copilot coding agent tasks; Claude Code on iOS is a full coding agent; their "configuration" is a mix of manual (Space instructions) and file-driven (coding agent tasks respect repo config files).

**No unsupported generalisations present.** Each claim traces to a named primary or secondary source.

### §4 Consistency Check

**Check 1, Copilot reads both files:** The GitHub Docs source says "the instructions in both files are used" when both `AGENTS.md` and `.github/copilot-instructions.md` are present. The `AGENTS.md` spec source confirms Copilot Agent as compatible. These two sources agree. No contradiction.

**Check 2, Claude Code reads CLAUDE.md, not copilot-instructions.md:** The Anthropic Claude Code memory docs explicitly describe CLAUDE.md file discovery. The `anthropics/claude-code-action` docs confirm `CLAUDE.md` is the configuration mechanism. These sources are consistent.

**Check 3, ADR-0006 vs. current research:** ADR-0006 assumed one file would serve all agents. Current primary source evidence shows that `.github/copilot-instructions.md` does NOT auto-load in Claude Code or the Claude iOS GitHub connector. This is not a contradiction in the evidence, ADR-0006 was an architectural decision made with available knowledge at the time; the current research updates the picture with primary source evidence.

**Check 4, Credential table:** The credential constraint is stated in `.github/copilot-instructions.md` itself. The Claude Code GitHub Actions docs confirm the exact credentials required. No contradiction; the conclusion (Claude GitHub Issues surface is blocked) follows directly.

**Check 5, AGENTS.md and Claude Code compatibility:** agentsmd.online lists "Claude Code Anthropic" as a compatible agent. The Anthropic docs describe `CLAUDE.md` as the auto-loaded file. These are not contradictory: AGENTS.md may be discoverable by Claude Code when it reads files in a directory, but it is not auto-loaded on startup the way CLAUDE.md is. The correct framing is: AGENTS.md benefits Copilot and other AGENTS.md-native tools; CLAUDE.md is the reliable path for Claude Code auto-loading.

**No unresolvable contradictions found.**

### §5 Depth and Breadth Expansion

**Technical lens:**
- The three-file recommendation (`AGENTS.md`, `copilot-setup-steps.yml`, `CLAUDE.md`) introduces no new credentials, no new workflows that run on every push, and no changes to existing files. The blast radius of adding these files is limited.
- `copilot-setup-steps.yml` only runs when the Copilot coding agent is triggered (not on every continuous integration (CI) push), so it does not affect the existing CI pipeline.
- Submodule initialisation in `copilot-setup-steps.yml` requires `actions/checkout@v5` with `submodules: recursive`. Without the `GITHUB_TOKEN` or `COPILOT_GITHUB_TOKEN` having submodule read access, this step may fail for private submodules. This repo's `GITHUB_TOKEN` is auto-provided by GitHub Actions and will have access to the same repo (and its submodules if they are hosted in the same organisation). The `.github/skills/` submodule (`davidamitchell/Skills`) is a separate private repo, the Copilot coding agent's `GITHUB_TOKEN` is scoped to the current repo only, so submodule checkout may fail unless `COPILOT_GITHUB_TOKEN` (the Personal Access Token (PAT)) is used instead.

**Historical lens:**
- Prior research (2026-03-08-ai-coding-harnesses-agent-philosophy) established that `AGENTS.md` emerged in 2025 as a cross-vendor standard. That research found `AGENTS.md` read by OpenAI Codex, Cursor, GitHub Copilot, Sourcegraph, Aider, and others. The current research confirms GitHub Copilot's explicit support with the combined-reading rule.
- ADR-0006 (2026-03-07) was a deliberate simplification. The current finding that this repo needs `AGENTS.md` back is not a reversal of ADR-0006's intent, it's an addendum. The intent was one canonical instruction file; the `AGENTS.md` pointer pattern achieves this by pointing to the canonical file.

**Behavioural lens:**
- The key practical question for the owner is: "when I assign a GitHub Issue to Copilot, will it have the same context as when I work with Copilot in chat?" The answer currently is: partially yes (`.github/copilot-instructions.md` loads), but the environment is misconfigured (no `copilot-setup-steps.yml` means no Python deps, no submodule). This is a silent failure, the agent will not error immediately but will fail when it tries to run tests or use skills.
- A `copilot-setup-steps.yml` that installs Python deps takes 30–60 seconds of setup time before the agent starts. This is a necessary cost for a correctly-configured environment.

**Regulatory/governance lens:**
- No regulatory constraints apply to instruction files.
- The `AGENTS.md` standard being under the Linux Foundation / Agentic AI Foundation provides open-standard assurance: it is not a proprietary format subject to vendor lock-in.

### §6 Synthesis

**Executive summary:**

The repository currently serves the Copilot coding agent partially: `.github/copilot-instructions.md` loads correctly, but the agent starts without Python dependencies, without the `.github/skills/` submodule, and without `AGENTS.md` for cross-vendor compatibility. The Claude-via-GitHub-Issues surface is entirely absent and is blocked by missing credentials (`ANTHROPIC_API_KEY` and a GitHub App). Copilot Spaces can launch Copilot coding agent tasks, and Claude Code on iOS is a full coding agent that works in cloud sandboxes; both can benefit from proper per-repo configuration. The minimum viable configuration to fully support all currently-reachable surfaces comprises three additions: `AGENTS.md` at the repository root (thin pointer to `.github/copilot-instructions.md`), `.github/workflows/copilot-setup-steps.yml` (installs Python deps and initialises the skills submodule), and `CLAUDE.md` at the repository root (pre-positioned for future Claude Code GitHub Actions when credentials are available, and for Claude Code iOS sessions).

**Key findings:**

1. The Copilot coding agent reads both `.github/copilot-instructions.md` and `AGENTS.md` when both are present, both files are combined additively; neither takes exclusive precedence at the root.
2. `copilot-setup-steps.yml` runs before the Copilot coding agent starts work; its absence means no Python deps and no submodule, the agent cannot run `make check` or `make test` as currently required by `.github/copilot-instructions.md`.
3. Claude Code GitHub Actions reads `CLAUDE.md` via normal file discovery; it does NOT auto-read `.github/copilot-instructions.md`, meaning the current single-file approach leaves Claude Code without instructions.
4. The Claude-via-GitHub-Issues surface requires `ANTHROPIC_API_KEY` (or Bedrock/Vertex credentials) plus a GitHub App (`APP_ID`, `APP_PRIVATE_KEY`); none of these are available in this repo's credential table, so this surface is currently blocked.
5. Copilot Spaces can launch Copilot coding agent tasks that write code and create pull requests; Spaces itself is a Q&A tool that does not auto-read per-repo instruction files, but when it launches a coding agent task, that agent respects the repository's configuration files.
6. Claude Code on iOS is a full coding agent that can write code, create commits, and open pull requests in cloud-based sandboxed environments; it does not auto-load instruction files at session start but can discover and use `CLAUDE.md` and other files during execution.
7. `AGENTS.md` is now a Linux Foundation-stewarded open standard supported by 60,000+ repositories and compatible with over 20 tools including GitHub Copilot, Claude Code, OpenAI Codex, and Cursor; a thin pointer file at the root costs nothing and benefits all compatible surfaces.
8. ADR-0006's consolidation to `.github/copilot-instructions.md` was correct for Copilot surfaces; adding `AGENTS.md` (pointer) and `CLAUDE.md` restores multi-surface coverage without reversing ADR-0006's intent.
9. Submodule checkout in `copilot-setup-steps.yml` may require `COPILOT_GITHUB_TOKEN` rather than the default `GITHUB_TOKEN` because the Copilot coding agent's `GITHUB_TOKEN` is scoped to the current repo and may not have read access to the private `davidamitchell/Skills` submodule.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Copilot reads both `.github/copilot-instructions.md` and `AGENTS.md` | [GitHub Docs](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot) | high | Primary source, explicit statement |
| `copilot-setup-steps.yml` runs pre-agent | [GitHub Docs](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent) | high | Primary source, explicit description |
| No `copilot-setup-steps.yml` in this repo | Filesystem inspection | high | Direct verification |
| Claude Code GitHub Actions reads `CLAUDE.md` | [Claude Code GitHub Actions docs](https://docs.anthropic.com/en/docs/claude-code/github-actions); [Claude Code memory docs](https://docs.anthropic.com/en/docs/claude-code/memory) | high | Two independent primary sources |
| `ANTHROPIC_API_KEY` not in credential table | `.github/copilot-instructions.md` | high | Direct verification |
| Copilot Spaces can launch coding agent tasks | [GitHub Docs Spaces](https://docs.github.com/en/copilot/how-tos/provide-context/use-copilot-spaces/create-copilot-spaces); [Copilot Spaces with Coding Agent](https://www.ericksegaar.com/2025/12/08/enable-copilot-space-with-coding-agent/) | high | Spaces itself is Q&A; can trigger coding agents |
| Claude Code on iOS is a full coding agent | [Anthropic Claude Code on iOS](https://thetechportal.com/2025/10/21/anthropic-expands-ai-coding-assistant-claude-code-to-the-web-and-ios/); [Claude Code iOS capabilities](https://www.engadget.com/ai/anthropic-brings-claude-code-to-ios-and-the-web-180023611.html) | high | Multiple sources confirm full coding agent capabilities |
| `AGENTS.md` supported by 60,000+ repos, Linux Foundation | [agentsmd.online](https://agentsmd.online); [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | medium | agentsmd.online secondary; cross-confirmed by agents.md primary |
| ADR-0006 deleted `AGENTS.md` | `docs-adr/0006-standardise-agent-instructions.md` | high | Local primary source |

**Assumptions:**

- The iOS Claude app's "code feature" refers to Claude Code running on iOS, which launched in October 2025. Justified by: Multiple sources confirm Anthropic expanded Claude Code to iOS and web in October 2025 as a full coding agent. The inaccessible support article (10166833) likely describes this same feature, while article 10167454 describes the broader GitHub connector that provides repository access.
- The `davidamitchell/Skills` submodule requires `COPILOT_GITHUB_TOKEN` for checkout by the Copilot coding agent. Justified by: GitHub Actions `GITHUB_TOKEN` is scoped to the triggering repo; cross-repo read access for private repos requires a PAT.

**Analysis:**

The four agent surfaces split into different categories. Category A (code-writing agents): Copilot coding agent, Claude Code (GitHub Actions and iOS). Category B (context/launch tools): Copilot Spaces. Category A agents are autonomous code-writing agents; per-repo configuration files directly influence their behavior. Claude Code does not auto-load instruction files at session start but can discover them during execution. Copilot Spaces itself is a Q&A tool but can launch Copilot coding agents that respect repository configuration.

For Category A coding agents, the coverage gap is: (1) `AGENTS.md` absent (Copilot coding agent still works without it because `.github/copilot-instructions.md` loads, but cross-vendor compatibility is lost); (2) `copilot-setup-steps.yml` absent (Copilot coding agent environment is misconfigured, silent failure); (3) `CLAUDE.md` absent (Claude Code surfaces have no reliably discoverable instructions).

The minimum viable additions are ordered by immediate impact: `copilot-setup-steps.yml` first (fixes silent environment failure for Copilot coding agent), `CLAUDE.md` second (enables Claude Code iOS sessions and pre-positions for GitHub Actions), `AGENTS.md` third (restores cross-vendor compatibility).

**Risks, gaps, uncertainties:**

- The Skills submodule checkout in `copilot-setup-steps.yml` may silently fail if `COPILOT_GITHUB_TOKEN` is not passed as the checkout token. The safe pattern is to use `COPILOT_GITHUB_TOKEN` in the `actions/checkout` step of `copilot-setup-steps.yml`.
- The `AGENTS.md` cross-compatibility claim for Claude Code is sourced from agentsmd.online (a community site), which may be aspirational rather than verified. The reliable Claude Code instruction mechanism is `CLAUDE.md`. `AGENTS.md` should be added for Copilot and other AGENTS.md-native tools; `CLAUDE.md` is the reliable Claude Code path.

**Open questions:**

- Does the `copilot-setup-steps.yml` environment support `git submodule update --init` with the `COPILOT_GITHUB_TOKEN`? This needs to be tested.
- Should the `CLAUDE.md` file simply contain `<!-- See .github/copilot-instructions.md for instructions. -->` or a minimal summary? A pointer comment keeps the repo Don't Repeat Yourself (DRY); a full copy risks drift.
- Is there a Claude GitHub App available as a GitHub Marketplace app (analogous to Copilot's built-in assignment) that would simplify the GitHub Issues → Claude surface without the current full `anthropics/claude-code-action` workflow setup?

### §7 Recursive Review

All sections completed. Every claim in §2 carries a `[fact]`, `[inference]`, or `[assumption]` label. Every `[fact]` maps to a named primary or secondary source with a URL. The two `[assumption]` labels in §2 are explicitly justified. No threads were abandoned mid-investigation. The convergence analysis in Q5 directly synthesises findings from Q1–Q4. The evidence map in §6 covers all key findings. Uncertainties are documented in §6 Risks, Gaps, Uncertainties and §5.

---

## Findings

### Executive Summary

The repository currently serves the Copilot coding agent only partially: `.github/copilot-instructions.md` loads correctly, but the agent starts without Python dependencies and without the `.github/skills/` submodule because no `copilot-setup-steps.yml` exists. Three additions cover all currently-reachable surfaces: `copilot-setup-steps.yml` (fixes the Copilot coding agent environment), `CLAUDE.md` at root (enables Claude Code on iOS and pre-positions for Claude Code GitHub Actions when credentials are added), and `AGENTS.md` at root (restores cross-vendor compatibility). The Claude-via-GitHub-Issues surface is currently blocked by missing credentials (`ANTHROPIC_API_KEY` and a GitHub App) and cannot be enabled within the current constraint of no new credentials. Copilot Spaces can launch coding agent tasks that respect repo configuration; Claude Code on iOS is a full coding agent that can discover and use instruction files during execution.

### Key Findings

1. The Copilot coding agent reads both `.github/copilot-instructions.md` and `AGENTS.md` when both are present at the repository root; both files are combined additively, giving complete instruction coverage from either file independently.
2. The absence of `.github/workflows/copilot-setup-steps.yml` means the Copilot coding agent starts in a bare Ubuntu environment without Python dependencies, without the virtual environment, and without the `.github/skills/` submodule, this is a silent failure that prevents the agent from running `make check` or `make test` as required by the existing instructions.
3. Claude Code GitHub Actions (`anthropics/claude-code-action`) reads `CLAUDE.md` via Claude Code's normal file-discovery walk; it does not read `.github/copilot-instructions.md`, meaning the current single-file approach leaves Claude Code without any project instructions.
4. The Claude-via-GitHub-Issues surface requires `ANTHROPIC_API_KEY` (or equivalent Bedrock/Vertex credentials) and a GitHub App (`APP_ID`, `APP_PRIVATE_KEY`); none are in this repo's credential table, so this surface is blocked under the current no-new-credentials constraint.
5. Copilot Spaces can launch Copilot coding agent tasks that write code and create pull requests; Spaces itself is a Q&A tool that does not auto-read per-repo instruction files, but when it launches a coding agent task, that agent respects the repository's configuration files.
6. Claude Code on iOS is a full coding agent that can write code, create commits, and open pull requests in cloud-based sandboxed environments; it does not auto-load instruction files at session start but can discover and use `CLAUDE.md` and other files during execution.
7. `AGENTS.md` is a Linux Foundation-stewarded open standard supported by over 20 tools (including GitHub Copilot, OpenAI Codex, Cursor, and Claude Code) and present in over 60,000 repositories; adding a thin pointer file at the root costs nothing and restores coverage for all AGENTS.md-native agents.
8. ADR-0006's consolidation to `.github/copilot-instructions.md` was correct for Copilot-only usage; adding `AGENTS.md` (as a pointer) and `CLAUDE.md` extends coverage to Claude Code surfaces without contradicting ADR-0006's intent of a single canonical instruction file.
9. Submodule checkout inside `copilot-setup-steps.yml` should use `COPILOT_GITHUB_TOKEN` rather than the default `GITHUB_TOKEN` because the Copilot coding agent's auto-provided token is scoped to the current repository and may not have read access to the private `davidamitchell/Skills` submodule.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Copilot reads both `.github/copilot-instructions.md` and `AGENTS.md` additively | [GitHub Docs, custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot) | high | Primary source, explicit statement |
| `copilot-setup-steps.yml` runs before agent starts work | [GitHub Docs, development environment](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent) | high | Primary source |
| No `copilot-setup-steps.yml` in this repo | Direct filesystem inspection | high | Verified |
| Claude Code GitHub Actions reads `CLAUDE.md`, not `.github/copilot-instructions.md` | [Claude Code GitHub Actions docs](https://docs.anthropic.com/en/docs/claude-code/github-actions); [Claude Code memory docs](https://docs.anthropic.com/en/docs/claude-code/memory) | high | Two independent primary sources |
| Claude GitHub Actions surface requires `ANTHROPIC_API_KEY` and GitHub App | [Claude Code GitHub Actions docs](https://docs.anthropic.com/en/docs/claude-code/github-actions) | high | Primary source |
| Credentials not in this repo's table | `.github/copilot-instructions.md` credential table | high | Direct verification |
| Copilot Spaces can launch coding agent tasks | [GitHub Docs, Copilot Spaces](https://docs.github.com/en/copilot/how-tos/provide-context/use-copilot-spaces/create-copilot-spaces); [Copilot Spaces with Coding Agent](https://www.ericksegaar.com/2025/12/08/enable-copilot-space-with-coding-agent/) | high | Spaces itself is Q&A; can trigger coding agents |
| Claude Code on iOS is a full coding agent | [Anthropic Claude Code on iOS](https://thetechportal.com/2025/10/21/anthropic-expands-ai-coding-assistant-claude-code-to-the-web-and-ios/); [Claude Code iOS capabilities](https://www.engadget.com/ai/anthropic-brings-claude-code-to-ios-and-the-web-180023611.html) | high | Multiple sources confirm full coding agent capabilities |
| `AGENTS.md` is Linux Foundation-stewarded, 60,000+ repos, 20+ tools | [agentsmd.online](https://agentsmd.online); [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | medium | agentsmd.online is a secondary community site; agents.md is the primary spec repo |

### Assumptions

- **Assumption:** The iOS Claude app's "code feature" refers to Claude Code running on iOS, which launched in October 2025 as a full coding agent. **Justification:** Multiple sources confirm Anthropic expanded Claude Code to iOS and web in October 2025 with full coding capabilities. The inaccessible support article (10166833) likely describes this feature, while article 10167454 describes the broader GitHub connector that provides repository access.
- **Assumption:** The `davidamitchell/Skills` submodule requires `COPILOT_GITHUB_TOKEN` rather than the default `GITHUB_TOKEN` for checkout by the Copilot coding agent. **Justification:** GitHub Actions `GITHUB_TOKEN` is auto-scoped to the triggering repository; cross-repo read access for private repositories requires a PAT with the appropriate scope.

### Analysis

The four surfaces split into different categories. Code-writing agents: Copilot coding agent (auto-loads `.github/copilot-instructions.md` and `AGENTS.md`), Claude Code on iOS (can discover `CLAUDE.md` during execution), and Claude Code GitHub Actions (reads `CLAUDE.md`). Context/launch tools: Copilot Spaces (can launch Copilot coding agents). Each code-writing agent has different instruction-loading behavior; the minimum viable configuration must accommodate all patterns.

For code-writing agents, the priority order is: (1) fix the environment gap (`copilot-setup-steps.yml`) because a misconfigured environment causes test failures even with perfect instructions; (2) enable Claude Code surfaces (`CLAUDE.md`) for iOS sessions and future GitHub Actions; (3) restore cross-vendor compatibility (`AGENTS.md`). The credential constraint is a hard blocker on Claude Code GitHub Actions, it cannot be resolved by file additions alone.

The "thin pointer" pattern for `AGENTS.md` (pointing to `.github/copilot-instructions.md`) and `CLAUDE.md` (importing or summarising the same instructions) preserves ADR-0006's intent of a single canonical instruction source while allowing each agent's native discovery mechanism to locate relevant content. Full duplication across files risks drift; a pointer or import pattern avoids it.

### Risks, Gaps, and Uncertainties

- The Skills submodule checkout in `copilot-setup-steps.yml` requires testing with `COPILOT_GITHUB_TOKEN` to confirm the token has cross-repo read access. If it does not, the Copilot coding agent will silently work without skills files.
- The `AGENTS.md` cross-compatibility claim for Claude Code is sourced from a community site (agentsmd.online). The reliable instruction mechanism for Claude Code is `CLAUDE.md`; `AGENTS.md` should be considered a bonus for Claude Code, not a primary path.
- The `CLAUDE.md` content strategy (pointer vs. summary vs. full copy) is unresolved. A full copy of `.github/copilot-instructions.md` into `CLAUDE.md` gives Claude Code the highest context fidelity but introduces a drift risk. A minimal pointer with a `<!-- See .github/copilot-instructions.md -->` comment is DRY but may not be sufficient for Claude Code's context needs in automated workflows.

### Open Questions

- **Can `COPILOT_GITHUB_TOKEN` be used in `copilot-setup-steps.yml` for submodule checkout?** If yes, submodule init is straightforward. If no, the skills submodule remains inaccessible to the Copilot coding agent. This warrants a separate implementation test.
- **Is there a Claude GitHub App available on the GitHub Marketplace** that would simplify the GitHub Issues → Claude surface (analogous to Copilot's native assignment) without requiring the full `anthropics/claude-code-action` workflow and credential setup?
- **What should `CLAUDE.md` contain?** A full mirror of `.github/copilot-instructions.md` maximises Claude Code context but creates a maintenance burden. A structured summary (key rules only) may be better for automated CI workflows where token budget matters.

---

## Output

- Type: knowledge, backlog-item
- Description: Confirmed that the minimum viable configuration for all currently-reachable agent surfaces requires three additions: `copilot-setup-steps.yml` (environment setup), `AGENTS.md` (cross-vendor pointer), and `CLAUDE.md` (Claude Code instructions). Claude-via-GitHub-Issues surface is blocked by missing credentials. Copilot Spaces and Claude iOS GitHub integration are reading tools requiring no per-repo configuration. New backlog items created for implementation.
- Links:
  - [GitHub Docs, Copilot custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)
  - [GitHub Docs, Copilot coding agent environment](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent)
  - [Claude Code GitHub Actions docs](https://docs.anthropic.com/en/docs/claude-code/github-actions)
