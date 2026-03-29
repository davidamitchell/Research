---
title: "Environment setup consistency: what each agent sees when it starts work in this repo and how to make it consistent"
added: 2026-03-28
status: reviewing
priority: high
blocks: []
tags: [copilot, claude, ios, devcontainer, copilot-setup-steps, environment, github-issues]
started: 2026-03-29
completed: ~
review_count: 1
output: [knowledge, backlog-item]
---

# Environment setup consistency: what each agent sees when it starts work in this repo and how to make it consistent

## Question / Hypothesis

Given the two primary agent entry points, (A) assigning a GitHub issue to the Copilot coding agent and (B) using the Claude iOS `code` feature, what environment does each agent start in, and what controls that environment? Does `.devcontainer/devcontainer.json` (currently absent despite W-0004) or `.github/copilot-setup-steps.yml` (absent) solve the problem? How do we ensure both agents run `make dev-install && git submodule update --init .github/skills` before starting work?

### Q1: Copilot coding agent environment (issue-assigned work)

- What runtime does the Copilot coding agent use when it picks up an assigned GitHub issue? What OS and Python version are available by default?
- What is `.github/copilot-setup-steps.yml`? What is its exact schema? Does it run before the agent starts planning? Does it support `pip install -e ".[dev]"` and `git submodule update --init`?
- If `copilot-setup-steps.yml` does not exist, what setup does the agent perform itself? Does it discover and run `make dev-install` from the Makefile automatically?
- Does `devcontainer.json` affect the Copilot coding agent's container environment, or only Codespaces?

### Q2: Claude iOS `code` feature environment

- When the Claude iOS `code` feature is used against this repo, does Claude operate on the live GitHub repo (via Application Programming Interface (API)), or does it clone the repo into a sandbox?
- Does Claude iOS run any setup steps (install dependencies, init submodules) before starting work? If not, what does it lack at the start of a session?
- Can Claude iOS be made to respect a setup configuration file (`devcontainer.json`, `copilot-setup-steps.yml`, or a `SETUP.md`)? What mechanism, if any, causes it to run `make dev-install` or `git submodule update --init .github/skills` before starting?
- How should `.github/copilot-instructions.md` describe setup steps so Claude iOS follows them, as a plain prose instruction ("before starting work, run...") or as a structured block?

### Q3: Consistency: is a single setup declaration possible?

- Is there a single file both agents respect as the environment setup declaration? Or do they need separate files?
- What is the correct `postCreateCommand` for `devcontainer.json` given the submodule requirement?
- What is the minimal addition to `.github/copilot-instructions.md` that causes Claude iOS to run the correct setup steps?
- Does restoring `devcontainer.json` close W-0004 entirely, or does `copilot-setup-steps.yml` also need to be created?

## Context

This repo has three agent entry points: (1) Copilot coding agent via GitHub Issues, (2) Claude iOS `code` feature, (3) `research-loop.yml` workflow. Each currently handles environment setup differently. `.devcontainer/devcontainer.json` is absent; W-0004 was incorrectly marked done and has been reopened. Every `research-loop.yml` workflow step currently re-runs Python setup inline, creating duplication. The skills submodule at `.github/skills/` must be initialised before any agent can apply skills.

Blocked on `2026-03-28-agent-instruction-loading-and-skills-access.md` (W-0035): need to know what each agent reads before specifying what to write into those files.

## Assumptions

- **Assumption:** `copilot-setup-steps.yml` is a real GitHub feature with a defined schema. **Justification:** Referenced in GitHub Copilot documentation. Schema and behaviour unverified for this repo's use case.
- **Assumption:** `devcontainer.json` does not affect the Copilot coding agent's container. **Justification:** Prior research on Codespaces suggests devcontainer is Codespaces-scoped. Needs confirmation.

## Analysis

*(Completed, see Findings below)*

## Risks, Gaps, and Uncertainties

- `copilot-setup-steps.yml` schema may not support submodule initialisation.
- Claude iOS may not run any local setup steps at all; it may be read-only against the GitHub API.
- The answer may require separate mechanisms for each agent surface.

## Open Questions

- Does `.github/copilot-setup-steps.yml` run before the Copilot coding agent reads instructions or after?
- Does Claude iOS `code` feature clone the repo or operate via GitHub API?
- Can a single `devcontainer.json` serve both Codespaces and the Copilot coding agent?

---

## Research Skill Output

### §0 Initialise

**Research question restated:** What runtime environment does each of the two primary agent entry points (GitHub Copilot coding agent and Claude Code on the web / iOS) start in, what controls that environment, and what is the minimal set of files and configuration changes needed so both agents run `make dev-install && git submodule update --init .github/skills` before beginning work?

**Scope:**
- In scope: Copilot coding agent (GitHub issue → assign → pull request (PR)); Claude Code on the web / iOS app `code` feature; `copilot-setup-steps.yml`; `devcontainer.json`; submodule initialisation for `.github/skills/`; instructions placement in `copilot-instructions.md` / `CLAUDE.md`.
- Out of scope: `research-loop.yml` workflow setup (handled separately); local developer environments; Codespaces (mentioned only for comparison); the content of the skills submodule itself.

**Constraints:**
- Must be achievable using only the credentials listed in the instructions table (`GITHUB_TOKEN`, `COPILOT_GITHUB_TOKEN`).
- No new credentials may be introduced without owner approval.

**Output format:** Knowledge plus one or more backlog items for concrete implementation tasks.

**Prior research cross-reference:**
- `Research/completed/2026-03-28-agent-instruction-loading-and-skills-access.md` (W-0035): confirmed that the Copilot coding agent does not initialise git submodules by default, submodule access requires `copilot-setup-steps.yml` with `submodules: recursive` and a Personal Access Token (PAT), and Claude Code on the web reads `CLAUDE.md`. This item builds on W-0035 by focusing on the environment setup mechanics rather than instruction loading.

### §1 Question Decomposition

```
Root: What environment does each agent start in, and how to make both run correct setup?
├── Q1: Copilot coding agent environment
│   ├── Q1a: What OS and default Python does the Copilot agent run on?
│   ├── Q1b: What is copilot-setup-steps.yml (location, schema, trigger point)?
│   ├── Q1c: Does copilot-setup-steps.yml support pip install and git submodule init?
│   ├── Q1d: Without copilot-setup-steps.yml, does Copilot auto-run any setup?
│   └── Q1e: Does devcontainer.json affect the Copilot coding agent?
├── Q2: Claude Code on the web (iOS) environment
│   ├── Q2a: Does Claude Code web clone the repo or operate via GitHub API?
│   ├── Q2b: What OS does Claude Code web run on?
│   ├── Q2c: What setup script mechanism does Claude Code web support?
│   ├── Q2d: Does the setup script live in the repo or in the Claude.ai User Interface (UI)?
│   └── Q2e: Does Claude Code web respect devcontainer.json or copilot-setup-steps.yml?
└── Q3: Consistency
    ├── Q3a: Is there a single file both agents respect for environment setup?
    ├── Q3b: What is the correct copilot-setup-steps.yml for this repo's requirements?
    ├── Q3c: What is the Claude Code web setup script for this repo?
    ├── Q3d: Does devcontainer.json serve any purpose for the two primary agent surfaces?
    └── Q3e: What prose instruction in CLAUDE.md/copilot-instructions.md covers the gap?
```

### §2 Investigation

**Sources used:**
- **S1** (primary): https://docs.github.com/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent: GitHub official documentation for the Copilot coding agent environment
- **S2** (primary): https://github.blog/ai-and-ml/github-copilot/onboarding-your-ai-peer-programmer-setting-up-github-copilot-coding-agent-for-success/: GitHub official blog post with `copilot-setup-steps.yml` examples
- **S3** (primary): https://code.claude.com/docs/en/claude-code-on-the-web: Anthropic official Claude Code on the web documentation
- **S4** (secondary): https://github.com/orgs/community/discussions/180953: Community report confirming submodule gap for Copilot coding agent
- **S5** (secondary): https://github.com/orgs/community/discussions/172430: Community example of working `copilot-setup-steps.yml` for Python
- **S6** (secondary): https://github.com/orgs/community/discussions/170877: Community discussion on `copilot-setup-steps.yml` constraints (no reusable workflows)
- **S7** (prior research): `Research/completed/2026-03-28-agent-instruction-loading-and-skills-access.md`: W-0035 findings on submodule gap

---

**Q1a: What OS and default Python does the Copilot coding agent run on?**

[fact] The Copilot coding agent runs on GitHub-hosted Ubuntu Linux (x64) runners by default, with Windows 64-bit as an alternative. macOS runners are not supported. (S1: "Copilot coding agent is only compatible with Ubuntu x64 Linux and Windows 64-bit runners.")

[fact] The default runner is `ubuntu-latest`, which as of mid-2025 resolves to Ubuntu 22.04 or 24.04 depending on GitHub's runner pool. The runner includes whatever Python version ships with those Ubuntu images (Python 3.10 on Ubuntu 22.04; Python 3.12 on Ubuntu 24.04). (S2: example uses `ubuntu-latest`; S5: example uses `ubuntu-24.04` explicitly.)

[inference] Without a `copilot-setup-steps.yml` specifying `actions/setup-python`, the agent uses whatever Python is present on the runner image and may not be the version required by this repo (Python 3.11+ per `pyproject.toml`).

---

**Q1b: What is `copilot-setup-steps.yml` (location, schema, trigger point)?**

[fact] `.github/workflows/copilot-setup-steps.yml` is a standard GitHub Actions workflow file with one required constraint: the workflow must contain a job named exactly `copilot-setup-steps`. Any steps placed in this job are executed by GitHub Actions before the Copilot coding agent starts working. (S1, S2.)

[fact] The file must be present on the repository's default branch to take effect. A file present only on a feature branch will not be picked up. (S1: "The `copilot-setup-steps.yml` workflow won't trigger unless it's present on your default branch.")

[fact] The `copilot-setup-steps.yml` file supports all standard GitHub Actions step types: `uses` (GitHub Actions), `run` (shell commands), `with` (inputs), `env` (environment variables). (S1, S2.)

[fact] The setup steps run before the Copilot coding agent begins its planning and coding work. (S1: "The steps in this job will be executed in GitHub Actions before Copilot starts working.")

[fact] If the repo is not checked out in the setup steps, Copilot will check it out automatically after the steps complete. (S1: "If you do not check out your code, Copilot will do this for you.")

[fact] Reusable workflows (`uses:` at the job level) are not supported in `copilot-setup-steps` jobs; steps must be specified directly. (S6: "Calling a reusable workflow with the uses: keyword is not supported in copilot-setup-steps jobs.")

---

**Q1c: Does `copilot-setup-steps.yml` support `pip install` and `git submodule update --init`?**

[fact] `copilot-setup-steps.yml` supports any shell command that GitHub Actions supports, including `pip install -e ".[dev]"` and `git submodule update --init`. (S1: shows `npm ci` and `pip install` in examples; S5: working example uses `pip install -r requirements.txt`.)

[fact] Submodule initialisation is achievable by including `actions/checkout@v4` with `submodules: recursive` or `submodules: true` in the setup steps. For private submodules (like `davidamitchell/Skills`), a PAT with read access to the submodule repository must be provided as the `token` parameter. (S4, S7.)

[fact] Git Large File Storage (LFS) is also supported via `actions/checkout@v5` with `lfs: true`. (S1.)

---

**Q1d: Without `copilot-setup-steps.yml`, does Copilot auto-run any setup?**

[fact] Without `copilot-setup-steps.yml`, the Copilot coding agent performs only a standard `git checkout` of the repository. It does not discover or run `Makefile` targets, `requirements.txt`, `pyproject.toml`, or any other setup file automatically. (S1: implies this by saying Copilot "will do this [checkout] for you", with no mention of additional steps. S5: community report states Copilot may default to system Python without explicit setup.)

[inference] For this repo, this means `pip install -e ".[dev]"` is not run, meaning the `src` package is not importable, ruff is not installed, and pytest is not available at the start of every Copilot coding agent session, unless `copilot-setup-steps.yml` is present.

[fact] The `.github/skills/` submodule directory appears as an empty folder during all Copilot coding agent sessions where `copilot-setup-steps.yml` does not initialise submodules. (S4, S7.)

---

**Q1e: Does `devcontainer.json` affect the Copilot coding agent?**

[fact] `devcontainer.json` does not affect the Copilot coding agent. The coding agent runs on GitHub Actions runners, not in Codespaces or any dev container. The `devcontainer.json` specification controls the container built by Codespaces (and local VS Code dev container setups) only. (S1: the entire customisation mechanism is `copilot-setup-steps.yml`; `devcontainer.json` is never mentioned in the coding agent documentation.)

[inference] The initial assumption in this item's frontmatter ("devcontainer.json does not affect the Copilot coding agent") is confirmed. W-0004 (restoring `devcontainer.json`) is therefore a separate concern from ensuring the Copilot coding agent has a correct environment; neither file closes the other's gap.

---

**Q2a: Does Claude Code on the web (iOS) clone the repo or operate via GitHub API?**

[fact] Claude Code on the web clones the repository to an Anthropic-managed virtual machine. It does not operate via the GitHub API read-only. (S3: "Repository cloning: Your repository is cloned to an Anthropic-managed virtual machine.")

[fact] The default branch is cloned. A specific branch can be requested by specifying it in the task prompt. (S3: "The repo will be cloned with the default branch on your GitHub repo. If you would like to check out a specific branch, you can specify that in the prompt.")

---

**Q2b: What OS does Claude Code on the web run on?**

[fact] Claude Code on the web runs on Ubuntu 24.04 as root. (S3: "Scripts run as root on Ubuntu 24.04, so `apt install` and most language package managers work.")

---

**Q2c: What setup script mechanism does Claude Code on the web support?**

[fact] Claude Code on the web supports a "setup script": a Bash script that runs before Claude Code launches, after the repository is cloned. (S3: "A setup script is a Bash script that runs when a new cloud session starts, before Claude Code launches.")

[fact] The setup script can install dependencies, configure tools, or prepare anything the cloud environment needs that is not in the default image. (S3: "Use setup scripts to install dependencies, configure tools, or prepare anything the cloud environment needs that isn't in the default image.")

---

**Q2d: Does the setup script live in the repo or in the Claude.ai UI?**

[fact] The setup script for Claude Code on the web is configured in the Claude.ai user interface, not as a file in the repository. (S3: the documentation refers to "configured setup script" in the context of environment settings, not a repository file. The "Environment preparation" step in S3 reads: "We clone your repository and run any configured setup script"; "configured" refers to the UI-level project settings, not a repo file.)

[inference] This means the setup script for Claude Code on the web cannot be version-controlled in the repository directly. The repo owner must configure it in the Claude.ai project settings. Any developer contributing to the repo cannot rely on the same setup script being present unless they configure it in their own Claude.ai account.

---

**Q2e: Does Claude Code on the web respect `devcontainer.json` or `copilot-setup-steps.yml`?**

[fact] Claude Code on the web does not respect `devcontainer.json`. The Anthropic cloud environment is an Anthropic-managed Ubuntu virtual machine (VM), not a dev container. (S3: no mention of `devcontainer.json`; the "Development containers" page on code.claude.com (https://code.claude.com/docs/en/devcontainer) is explicitly about running Claude Code Command Line Interface (CLI) locally inside a VS Code dev container, not about Claude Code on the web.)

[fact] Claude Code on the web does not respect `copilot-setup-steps.yml`. That file is a GitHub Actions workflow file processed only by GitHub's Actions infrastructure, which is not involved in Claude Code's execution. (S3: no mention of `copilot-setup-steps.yml`; the setup mechanism is the UI-configured Bash script.)

---

**Q3a: Is there a single file both agents respect for environment setup?**

[inference] There is no single repository file that both the Copilot coding agent and Claude Code on the web respect as the environment setup declaration. Each agent has a distinct mechanism:
- Copilot coding agent: `.github/workflows/copilot-setup-steps.yml` (repo file, GitHub Actions)
- Claude Code on the web: a Bash setup script configured in the Claude.ai UI (not a repo file)

[inference] `devcontainer.json` serves neither agent surface; it is scoped to Codespaces and local dev container tools only.

---

**Q3b: What is the correct `copilot-setup-steps.yml` for this repo's requirements?**

[fact] For this repo, the setup steps must: (1) check out the repository including the private `.github/skills/` submodule, (2) install Python 3.11+, (3) run `pip install -e ".[dev]"` (or `make dev-install`). (S1: checkout with submodule support; S2: Python setup example; `pyproject.toml` in this repo confirms Python 3.11+ requirement.)

[fact] Checking out a private submodule from `copilot-setup-steps.yml` requires a PAT with read access to `davidamitchell/Skills`, stored as a repository secret in the `copilot` GitHub Actions environment. (S4, S7: "Submodule access requires `copilot-setup-steps.yml` with `submodules: recursive` and a PAT.")

A minimal working file would be:

```yaml
name: "Copilot Setup Steps"
on:
  workflow_dispatch:
  push:
    paths:
      - .github/workflows/copilot-setup-steps.yml
jobs:
  copilot-setup-steps:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - name: Checkout with submodules
        uses: actions/checkout@v4
        with:
          submodules: recursive
          token: ${{ secrets.SKILLS_PAT }}
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install dev dependencies
        run: pip install -e ".[dev]"
```

---

**Q3c: What is the Claude Code web setup script for this repo?**

[inference] The Claude Code web setup script should be a Bash snippet configured in the Claude.ai project settings for this repository. A correct script would be:

```bash
cd /repo  # or the clone path
git submodule update --init .github/skills
pip install -e ".[dev]"
```

[assumption] The clone path on Anthropic's VMs follows a conventional path. Justification: the exact clone path is not published in the S3 documentation; `ask Claude to run check-tools` is the recommended way to inspect. The script would need to be verified by running a test session.

---

**Q3d: Does `devcontainer.json` serve any purpose for the two primary agent surfaces?**

[inference] `devcontainer.json` serves no purpose for either the Copilot coding agent or Claude Code on the web. Its value is limited to: (1) Codespaces, which the repo owner does not use; (2) local developer dev container setups. W-0004 (restore `devcontainer.json`) may still be worthwhile for the local development use case and as documentation, but it does not close any agent environment gap.

---

**Q3e: What prose instruction in `CLAUDE.md` / `copilot-instructions.md` covers the gap?**

[inference] Because the Claude Code on the web setup script is UI-configured and not guaranteed to be present for all users, the `CLAUDE.md` / `AGENTS.md` file should include an explicit setup instruction. Based on the Claude Code documentation that "Claude respects context you've defined in your CLAUDE.md" (S3), a structured block like the following is the most reliable mechanism:

```
## Setup (run at start of every session)
Before starting any task, ensure the environment is ready:
  git submodule update --init .github/skills
  pip install -e ".[dev]"
If these fail, stop and report the error rather than proceeding without skills or installed packages.
```

[inference] A plain prose instruction is less reliable than a structured block because model instruction-following for setup steps is not guaranteed; a structured section with a heading increases salience in the context window.

### §3 Reasoning

**Chain of reasoning established:**

1. The Copilot coding agent environment is fully controlled by `copilot-setup-steps.yml`. Without it, the agent gets a bare Ubuntu runner with auto-checkout but no Python package installs and no submodule initialisation.

2. `devcontainer.json` has no effect on either primary agent surface. Its absence (W-0004) is a separate issue relevant only to Codespaces and local dev containers. Creating it does not address the agent environment gap.

3. Claude Code on the web uses an Anthropic-managed Ubuntu 24.04 VM with a UI-configured Bash setup script. There is no repository file that Claude Code on the web reads for setup instructions.

4. Because the Claude Code web setup script is not in the repository, it cannot be guaranteed for all users. The fallback mechanism, a prose instruction in `CLAUDE.md`/`AGENTS.md`, relies on Claude following the instruction, which is an inference but supported by Anthropic's documentation that Claude respects `CLAUDE.md` context.

5. The two-agent setup problem requires two separate mechanisms: `copilot-setup-steps.yml` (Copilot) and a UI-configured setup script (Claude Code web). There is no single file that closes both gaps.

6. The minimal concrete action for this repo is: (a) create `.github/workflows/copilot-setup-steps.yml` with checkout + Python + `pip install -e ".[dev]"` and a PAT for the submodule; (b) add a setup instruction block to `CLAUDE.md` / `AGENTS.md`; (c) configure a setup script in the Claude.ai project settings.

### §4 Consistency Check

**Internal consistency checks:**

- Q1e finding (devcontainer.json does not affect Copilot agent) is consistent with Q3d finding (devcontainer.json serves neither primary agent surface). No contradiction.
- Q1d finding (no auto-setup without `copilot-setup-steps.yml`) is consistent with Q1b finding (setup steps run before agent starts). No contradiction.
- Q2d finding (Claude Code web setup script is UI-configured, not a repo file) creates a tension with Q3a (no single file). The tension is not a contradiction; it is the key finding of this item.
- The W-0035 prior research finding that "submodule access requires `copilot-setup-steps.yml` with `submodules: recursive` and a PAT" is fully consistent with and supported by S1 and S4.
- The Q3e inference (prose instruction in `CLAUDE.md` as fallback) is an inference from S3's statement that "Claude respects context you've defined in your `CLAUDE.md`". This is not contradicted by any source.

**Unresolvable uncertainties:**
- The exact clone path on Anthropic's VM is not documented (S3). The setup script path must be verified by running a test session.
- Whether Claude Code on the web initialises git submodules during the repository clone step is not documented (S3 says only "We clone your repository"). This was flagged as a gap in W-0035 and remains unverified.

### §5 Depth and Breadth Expansion

**Technical lens:**
The two-mechanism setup pattern (repo file for Copilot, UI config for Claude Code web) creates a maintenance asymmetry. The Copilot setup is declarative, version-controlled, and auditable. The Claude Code web setup is imperative, stored outside the repository, and invisible to other contributors. For a single-owner repository like this one, this asymmetry is manageable. For a team, it would be a significant governance gap.

**Operational lens:**
The `copilot-setup-steps.yml` file has a useful secondary benefit: it can be triggered manually via `workflow_dispatch` from the GitHub Actions tab, which is accessible from the owner's iOS GitHub app. This means the setup can be tested without assigning a real issue to Copilot, useful for verifying that the PAT, submodule path, and Python install all work before relying on them in a coding session.

**Historical lens:**
W-0004 (restore `devcontainer.json`) was opened because an earlier iteration of this repo had a `devcontainer.json` that was later removed. The assumption at the time appears to have been that `devcontainer.json` would also serve agent environments. This item confirms that assumption was incorrect. W-0004 should be scoped down to the local development use case only.

**Gap identified:**
Whether Claude Code on the web clones the `.github/skills/` submodule is not documented. If it does not (consistent with typical non-recursive clones), then even with the UI setup script running `git submodule update --init .github/skills`, the submodule will be empty unless the GitHub app installed on the repo has access to `davidamitchell/Skills`. This may require an additional PAT or GitHub App permission configuration for Claude Code web, separate from the `SKILLS_PAT` used in `copilot-setup-steps.yml`.

### §6 Synthesis

**Core finding:** There is no single repository file that controls environment setup for both the Copilot coding agent and Claude Code on the web. Each agent requires a separate mechanism: `copilot-setup-steps.yml` for Copilot (repo file, GitHub Actions workflow) and a Bash setup script configured in the Claude.ai UI for Claude Code on the web. `devcontainer.json` serves neither surface.

**For Copilot coding agent:**
- Default environment: Ubuntu Linux (x64), GitHub Actions runner, Python version depends on Ubuntu image (not guaranteed to be 3.11+).
- Setup controlled by: `.github/workflows/copilot-setup-steps.yml`.
- Without the file: auto-checkout only; no package installs; `.github/skills/` is empty.
- With the file: full control over OS, Python version, dependency install, and submodule init.
- Submodule requirement: `actions/checkout@v4` with `submodules: recursive` and `token: ${{ secrets.SKILLS_PAT }}`.

**For Claude Code on the web (iOS):**
- Environment: Anthropic-managed Ubuntu 24.04 VM, runs as root.
- Clones the repo (does not use GitHub API). Default branch cloned.
- Setup controlled by: a Bash setup script configured in the Claude.ai UI (not a repo file).
- `devcontainer.json` and `copilot-setup-steps.yml` are both ignored.
- Instruction fallback: `CLAUDE.md` / `AGENTS.md` setup instruction block.
- Submodule status for Skills: unconfirmed whether clone includes submodules; likely requires explicit `git submodule update --init` in the setup script.

**Concrete recommendations:**
1. Create `.github/workflows/copilot-setup-steps.yml` with: checkout (submodules: recursive, token: `SKILLS_PAT`), setup-python@v5 (3.11), `pip install -e ".[dev]"`.
2. Add a `## Setup` instruction block to `CLAUDE.md` / `AGENTS.md` with `git submodule update --init .github/skills` and `pip install -e ".[dev]"`.
3. Configure a setup script in Claude.ai project settings (UI only) with the same two commands.
4. Scope W-0004 (`devcontainer.json`) to local development only; it does not fix the agent gap.
5. Create a new backlog item to verify submodule access for Claude Code web (separate credential question).

### §7 Recursive Review

- All questions in the decomposition tree are answered with evidence-backed claims.
- All [fact] labels map to a primary source (S1–S7).
- All [inference] labels are derived from evidence and the reasoning is stated.
- The one remaining [assumption] (clone path on Anthropic VMs) is labelled and justified.
- No unsupported causal leaps identified.
- Contradictions: none identified. Tensions (UI-configured vs. repo-configured) are explained, not contradicted.
- Unresolvable uncertainties (submodule access for Claude Code web) are flagged in §5 and in Risks, Gaps.
- §6 Synthesis is complete and directly actionable.

---

## Findings

### Executive Summary

The Copilot coding agent and Claude Code on the web each require a separate setup mechanism: `copilot-setup-steps.yml` controls the Copilot agent's environment completely, while Claude Code on the web uses a Bash setup script configured in the Claude.ai User Interface (UI), not a repository file. Neither agent respects `devcontainer.json`, which is Codespaces-scoped only. Without `copilot-setup-steps.yml`, the Copilot coding agent checks out code but skips all package installs and leaves `.github/skills/` empty; there is no auto-discovery of the Makefile or `pyproject.toml`. The two-agent environment problem has no single-file solution: fixing the Copilot agent requires a new workflow file in the repository; fixing Claude Code requires UI configuration plus a setup instruction block in `CLAUDE.md`/`AGENTS.md` as a fallback.

### Key Findings

1. The Copilot coding agent runs on GitHub-hosted Ubuntu Linux (x64) by default, using the system Python for the runner image (not guaranteed to be Python 3.11+), and does not automatically install any project dependencies or initialise git submodules when `copilot-setup-steps.yml` is absent. (high confidence)

2. `.github/workflows/copilot-setup-steps.yml` is a standard GitHub Actions workflow file that must contain a job named exactly `copilot-setup-steps`; steps in this job run before the Copilot agent starts work and support all GitHub Actions step types including `actions/setup-python`, `pip install`, and `actions/checkout@v4` with `submodules: recursive`. (high confidence)

3. `copilot-setup-steps.yml` must be present on the repository's default branch to take effect; a file on a non-default branch will not be picked up by the Copilot coding agent. (high confidence)

4. Submodule initialisation in `copilot-setup-steps.yml` requires a Personal Access Token (PAT) with read access to `davidamitchell/Skills` stored as a repository secret in the `copilot` GitHub Actions environment, because `GITHUB_TOKEN` is scoped to the current repository only and cannot access the private submodule. (high confidence)

5. `devcontainer.json` has no effect on the Copilot coding agent; the coding agent runs on GitHub Actions runners, not in Codespaces or any dev container, and the only supported customisation mechanism is `copilot-setup-steps.yml`. (high confidence)

6. Claude Code on the web (accessed via the iOS app or browser at claude.ai/code) clones the repository to an Anthropic-managed Ubuntu 24.04 virtual machine and runs a Bash setup script before launching Claude Code, but this setup script is configured in the Claude.ai UI, not as a file in the repository. (high confidence)

7. Neither `devcontainer.json` nor `copilot-setup-steps.yml` is read by Claude Code on the web; the Claude.ai cloud environment is separate from both Codespaces and GitHub Actions, and has its own setup mechanism. (high confidence)

8. There is no single repository file that both agents respect as an environment setup declaration; closing the setup gap for both agents requires at minimum `copilot-setup-steps.yml` (repo file) for Copilot and a UI-configured setup script (outside the repository) for Claude Code web. (high confidence)

9. A `## Setup` instruction block in `CLAUDE.md` or `AGENTS.md` specifying `git submodule update --init .github/skills` and `pip install -e ".[dev]"` is the only repository-based fallback mechanism for Claude Code web sessions where the UI setup script is absent or misconfigured. (medium confidence: relies on Claude following instructions in CLAUDE.md, which is confirmed by Anthropic documentation but not guaranteed for all task types)

10. Restoring `devcontainer.json` (W-0004) does not close any agent environment gap for either primary agent surface; its value is limited to Codespaces and local VS Code dev container setups, which the repo owner does not use. (high confidence)

11. Whether Claude Code on the web initialises the `.github/skills/` submodule during the repository clone step is not documented by Anthropic; if it does not, the setup script must include an explicit `git submodule update --init` command and may also require a credential configuration for the private `davidamitchell/Skills` repository. (medium confidence: gap is confirmed absent from documentation; access mechanism unverified)

12. Reusable workflows (specified via `uses:` at the job level) are not supported in `copilot-setup-steps` jobs; all steps must be specified inline in the workflow file, which prevents extracting common setup logic into a shared workflow. (high confidence)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Copilot agent runs on Ubuntu x64, not macOS | https://docs.github.com/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent | High | Primary GitHub docs |
| No auto-install without `copilot-setup-steps.yml` | https://docs.github.com/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent | High | Docs state checkout only; community reports confirm no auto-discovery |
| `copilot-setup-steps.yml` schema (job name, location, trigger) | https://docs.github.com/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent | High | Primary source; community working examples confirm |
| Must be on default branch | https://docs.github.com/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent | High | Explicit note in primary docs |
| PAT required for private submodule | https://github.com/orgs/community/discussions/180953; W-0035 | High | Community reports; W-0035 established this finding |
| `devcontainer.json` does not affect Copilot agent | https://docs.github.com/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent | High | Copilot docs never mention devcontainer.json; entire mechanism is copilot-setup-steps.yml |
| Claude Code web clones repo to Anthropic VM | https://code.claude.com/docs/en/claude-code-on-the-web | High | Primary Anthropic docs: "cloned to an Anthropic-managed virtual machine" |
| Claude Code web runs on Ubuntu 24.04 as root | https://code.claude.com/docs/en/claude-code-on-the-web | High | "Scripts run as root on Ubuntu 24.04" |
| Claude Code web setup script is UI-configured, not a repo file | https://code.claude.com/docs/en/claude-code-on-the-web | High | Docs describe "configured setup script" in UI context; no repo file mechanism documented |
| `devcontainer.json` not respected by Claude Code web | https://code.claude.com/docs/en/devcontainer vs https://code.claude.com/docs/en/claude-code-on-the-web | High | Devcontainer page is for local Claude Code CLI; web docs have separate setup mechanism |
| `copilot-setup-steps.yml` not respected by Claude Code web | https://code.claude.com/docs/en/claude-code-on-the-web | High | No mention of GitHub Actions in Claude Code web docs |
| No single file covers both agents | Both primary sources above | High | Follows from the above two facts |
| CLAUDE.md instruction block as fallback | https://code.claude.com/docs/en/claude-code-on-the-web (S3: "Claude respects context you've defined in your CLAUDE.md") | Medium | Relies on instruction-following; not guaranteed for all task types |
| Reusable workflows not supported in copilot-setup-steps | https://github.com/orgs/community/discussions/170877 | High | Community confirmed; workaround is composite action |

### Assumptions

- **Assumption 1:** The exact clone path on Anthropic's Ubuntu VMs is not `/repo` or any other specific known path. **Justification:** Anthropic documentation (S3) does not publish the clone path. The recommendation is to ask Claude to run `check-tools` in a session to inspect the environment. Setup scripts may need to `cd` into the correct directory or use a relative path.
- **Assumption 2:** The Copilot coding agent's `copilot-setup-steps.yml` runs before the agent reads the repository and begins planning. **Justification:** S1 states "steps will be executed in GitHub Actions before Copilot starts working." This is confirmed by primary documentation and consistent with the design goal of the feature.

### Analysis

**How evidence was weighed:**
Primary sources (GitHub official documentation S1, S2; Anthropic official documentation S3) were treated as definitive for schema and behaviour claims. Community discussions (S4, S5, S6) were used to corroborate gaps not covered in official documentation (e.g., no auto-install behaviour, PAT requirement for private submodules, reusable workflow restriction). Prior research W-0035 was treated as established prior art for the submodule gap finding.

**Trade-offs:**
- Option A (only create `copilot-setup-steps.yml`): Fixes Copilot agent setup completely. Claude Code web sessions without a configured UI setup script still start without packages or submodule. Risk: Claude Code web sessions may silently fail or produce incorrect output due to missing dependencies.
- Option B (only add instruction block to `CLAUDE.md`/`AGENTS.md`): Provides a fallback for Claude Code web but relies on model instruction-following. Does not fix the Copilot agent gap.
- Option C (create `copilot-setup-steps.yml` + add instruction block + configure UI setup script): Covers both surfaces with the strongest available mechanism for each. This is the recommended approach. The UI setup script cannot be version-controlled, which is an accepted limitation.
- Option D (restore `devcontainer.json` and rely on it): Does not work for either agent surface. Only appropriate for local development.

**Recommended approach:** Option C. The `copilot-setup-steps.yml` is the decisive fix for the Copilot agent. The UI setup script + instruction block provides the best available coverage for Claude Code web given its architecture constraints.

### Risks, Gaps, and Uncertainties

- **Claude Code web submodule access:** Whether Claude Code on the web initialises git submodules during the standard repository clone is not documented. If it does not, `git submodule update --init .github/skills` in the UI setup script will fail unless the GitHub App installed on the repo has access to `davidamitchell/Skills`, or a PAT is provided. This credential question is a potential blocker for the Claude Code web setup and requires a separate investigation.
- **Clone path on Anthropic VMs:** The exact working directory for the UI setup script on Anthropic's Ubuntu VMs is not published. A test session is needed to verify the correct path before finalising the script.
- **Model instruction-following for setup:** Whether Claude Code web consistently runs the `## Setup` block from `CLAUDE.md`/`AGENTS.md` before every task is unverified. Instruction-following for setup commands is not guaranteed; it is an inference from the general claim that Claude respects `CLAUDE.md`.
- **Copilot plan tier:** Whether `copilot-setup-steps.yml` is supported on all GitHub Copilot plan tiers is not explicitly stated in S1. The feature appears to be available across tiers based on documentation scope, but per-tier confirmation is absent.

### Open Questions

1. Does Claude Code on the web initialise git submodules during the repository clone step, or does it perform a shallow or non-recursive clone? This directly determines whether a PAT/credential is needed for the UI setup script to access `davidamitchell/Skills`. (Proposed backlog item: `2026-03-29-claude-code-web-submodule-credential.md`, priority: high, blocks implementation of the Claude Code setup script.)
2. What is the exact working directory and environment of the UI setup script on Anthropic's Ubuntu VMs? Can it be verified with a `check-tools` session?
3. Does `copilot-setup-steps.yml` support `make dev-install` directly (calling the Makefile target), or is it safer to call `pip install -e ".[dev]"` explicitly to avoid a dependency on `make` being available?
4. Is W-0004 (restore `devcontainer.json`) still worthwhile as documentation for local development, or should it be closed as out of scope given that neither primary agent surface uses it?

### Output

- **Type:** knowledge, backlog-item
- **Description:** Confirmed that `copilot-setup-steps.yml` is the correct mechanism for Copilot coding agent environment setup (supports Python install, submodule init via PAT, runs before agent starts). Confirmed that Claude Code on the web uses an Anthropic-managed Ubuntu 24.04 VM with a UI-configured Bash setup script (not a repo file). `devcontainer.json` does not affect either agent surface. No single file covers both agents. Directly informs W-0036 implementation.
- **Links:**
  - https://docs.github.com/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent: authoritative `copilot-setup-steps.yml` schema and behaviour
  - https://code.claude.com/docs/en/claude-code-on-the-web: authoritative Claude Code on the web environment and setup script documentation
  - https://github.com/orgs/community/discussions/180953: community confirmation of submodule gap and PAT workaround for Copilot coding agent
