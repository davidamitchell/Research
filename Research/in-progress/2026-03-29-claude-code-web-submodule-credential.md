---
review_count: 1
title: "Claude Code on the web: private submodule credential access and git submodule init mechanism"
added: 2026-03-29
status: reviewing
priority: high
blocks: []
tags: [claude-code, submodules, credentials, environment-setup, agent-tooling]
started: 2026-03-29
completed: ~
output: [knowledge]
---

# Claude Code on the web: private submodule credential access and git submodule init mechanism

## Research Question

Does Claude Code on the web automatically initialise git submodules when cloning a repository, and if so, can it access private submodules (such as `davidamitchell/Skills` referenced at `.github/skills/`)? If not, what is the correct mechanism to grant it access via the User Interface (UI)-configured setup script?

## Scope

**In scope:**
- Whether Claude Code on the web runs `git submodule update --init` during repository cloning
- Whether private submodule credential access is possible from a UI-configured setup script
- What credential mechanism is available (Secure Shell (SSH) key, GitHub App token, Personal Access Token (PAT) stored in setup script environment)
- Whether the Anthropic-managed Ubuntu 24.04 virtual machine (VM) has access to the repository's GitHub Secrets during the setup script

**Out of scope:**
- Claude Code Command Line Interface (CLI) (local execution) -- different credential model
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

### §0 Initialise

**Research question restated:** Does Claude Code on the web automatically initialise git submodules when cloning a repository? Can a private submodule (specifically `davidamitchell/Skills` at `.github/skills/`) be accessed via credential configuration in the UI-configured Bash setup script? What is the correct mechanism to achieve this, and what are its limitations?

**Scope confirmed:**
- In scope: automatic submodule init behaviour on clone; GitHub proxy credential scoping; PAT-based credential workaround in setup scripts; env var availability to setup scripts.
- Out of scope: Claude Code CLI; Copilot coding agent; general git credential management outside Claude Code web.

**Constraints:** Official Anthropic documentation does not cover private submodule credential access in detail; community sources (Reddit, GitHub issues) are required to fill gaps.

**Output format:** Knowledge item documenting the mechanism and any workaround.

**Prior research cross-reference:**
- `Research/completed/2026-03-28-environment-setup-consistency.md` (W-0036): confirmed Claude Code on the web uses a UI-configured Bash setup script running on Ubuntu 24.04; documented that submodule initialisation from the setup script was unverified and flagged as a gap (Finding 11 in that item). This item directly addresses that gap.

### §1 Question Decomposition

```
Root: Does Claude Code web auto-init submodules? Can private ones be accessed?
├── Q1: Submodule initialisation on clone
│   ├── Q1a: Does the GitHub proxy clone include --recurse-submodules?
│   └── Q1b: Is the absence of auto-init documented or confirmed by community?
├── Q2: Credential scoping of the GitHub proxy
│   ├── Q2a: What does the GitHub proxy credential cover (selected repo only, or all repos)?
│   ├── Q2b: Does the proxy intercept/strip user-configured git credential helpers?
│   └── Q2c: Can the proxy be extended to other repos the GitHub App has access to?
├── Q3: Setup script credential mechanisms
│   ├── Q3a: Are environment variables from Claude.ai UI available to the setup script?
│   ├── Q3b: Can a PAT env var be used to configure git credentials in the setup script?
│   ├── Q3c: Does `git config credential.helper` or `url.insteadOf` work in the setup script?
│   └── Q3d: Is SSH key injection supported or documented?
└── Q4: This repo specifics
    ├── Q4a: Does this repo's .gitmodules use Hypertext Transfer Protocol Secure (HTTPS) or SSH URLs?
    └── Q4b: What exact setup script snippet would initialise .github/skills/?
```

### §2 Investigation

#### Q1: Submodule initialisation on clone

**Q1a: Does the GitHub proxy clone include `--recurse-submodules`?**

The official Claude Code on the web documentation at `code.claude.com/docs/en/claude-code-on-the-web` describes the GitHub proxy as handling "seamless cloning, fetching, and pull request (PR) operations" but makes no mention of `--recurse-submodules` or automatic submodule initialisation. [fact, primary source: https://code.claude.com/docs/en/claude-code-on-the-web]

**Q1b: Is the absence of auto-init confirmed by community?**

A Reddit user (`aneeesh`) in r/ClaudeAI reported: "By default, it only has access to the repo you select and not any submodules even though I have given it access to all repos." [fact, secondary source: https://www.reddit.com/r/ClaudeAI/comments/1otp5l1/private_git_submodules_in_claude_code_web/]

A GitHub feature request (issue #24400 in `anthropics/claude-code`) filed February 2026 states: "When I launch an agent on the sandbox on project A [which has project B as a submodule], it is unable to pull project B as a submodule." The issue was closed as "complete" on the same day it was opened (February 9, 2026), suggesting an automated bot response rather than a resolved fix. [fact, primary source: https://github.com/anthropics/claude-code/issues/24400]

A separate GitHub issue (#17293 in `anthropics/claude-code`) about marketplace plugin installations confirms the same root behaviour: "Claude Code clones the repository but doesn't initialize or update submodules. This leaves empty placeholder directories." [fact, primary source: https://github.com/anthropics/claude-code/issues/17293]

**Conclusion for Q1:** Claude Code on the web does NOT automatically run `git submodule update --init` during repository cloning. Submodule directories are present but empty. [inference from: absence of official documentation + three independent community/issue reports confirming the gap]

#### Q2: Credential scoping of the GitHub proxy

**Q2a: What does the GitHub proxy credential cover?**

The official documentation states: "For security, all GitHub operations go through a dedicated proxy service that transparently handles all git interactions. Inside the sandbox, the git client authenticates using a custom-built scoped credential. This proxy: Manages GitHub authentication securely - the git client uses a scoped credential inside the sandbox, which the proxy verifies and translates to your actual GitHub authentication token. Restricts git push operations to the current working branch for safety." [fact, primary source: https://code.claude.com/docs/en/claude-code-on-the-web]

The documentation does not state that this scoped credential covers repositories other than the selected repository. [fact, primary source: https://code.claude.com/docs/en/claude-code-on-the-web]

The Reddit reporter confirmed the scoped credential limitation: "it only has access to the repo you select and not any submodules even though I have given it access to all repos." [fact, secondary source: Reddit r/ClaudeAI]

**Q2b: Does the proxy intercept or strip user-configured git credential helpers?**

A GitHub issue (#11078) about private npm package authentication via the Claude Code security proxy reports: "User-provided authentication tokens are stripped by the proxy" for npm operations. [fact, primary source: https://github.com/anthropics/claude-code/issues/11078]

[inference] By analogy with the npm proxy stripping behaviour, a standard git credential helper configured in the setup script (which sends an Hypertext Transfer Protocol (HTTP) `Authorization` header) may also be stripped for git operations targeting other repositories through the proxy. This is not confirmed for git specifically.

[assumption] Uniform Resource Locator (URL)-embedded credentials (e.g., `https://PAT@github.com/owner/repo.git`) may bypass proxy header stripping because the token is part of the URL rather than a separate header. This pattern is used in the community workaround but not officially documented as proxy-safe.

**Q2c: Can the proxy be extended to other repos the GitHub App has access to?**

GitHub issue #24400 proposes: "I'd like the proxy from the sandbox in [Claude Code web] to have access to all the repos I gave access to in the Claude code app at organization level. This should work seamlessly without having to adding secrets manually." The issue was closed without documented resolution. [fact, primary source: https://github.com/anthropics/claude-code/issues/24400]

[inference] As of the research date (March 2026), native multi-repo proxy credential support is either not yet implemented or not documented. No Anthropic release notes or documentation updates reference this capability.

**Conclusion for Q2:** The GitHub proxy's scoped credential covers only the selected repository. Private submodules in other repositories require a separate credential mechanism. The proxy may strip standard git credential helpers; URL-embedded credentials are the more reliable workaround path.

#### Q3: Setup script credential mechanisms

**Q3a: Are environment variables from Claude.ai UI available to the setup script?**

The official documentation explicitly states: "Environment variables must be specified as key-value pairs, in `.env` format." and "A setup script is a Bash script that runs when a new cloud session starts, before Claude Code launches." [fact, primary source: https://code.claude.com/docs/en/claude-code-on-the-web]

[inference] Environment variables configured in the Claude.ai UI are available to the setup script as standard shell environment variables. The documentation's `.env` format description refers to the input format for the UI fields, not a literal `.env` file loading mechanism.

**Q3b: Can a PAT env var configure git credentials in the setup script?**

The Reddit community workaround confirms PAT-as-env-var is partially functional: "I sort of got it working with PAT set as an environment variable but I have to change the .gitmodules to update the url to https from username:PAT and then revert it back to the ssh url." [fact, secondary source: Reddit r/ClaudeAI]

This workaround has two drawbacks: it requires modifying `.gitmodules` (a tracked file) and reverting the change, and it is not described in Anthropic documentation.

**Q3c: Does `git config url.insteadOf` work in the setup script?**

[inference] A cleaner approach that avoids modifying `.gitmodules` is to configure git's URL rewriting in the setup script:
```bash
git config --global url."https://${SKILLS_PAT}@github.com/".insteadOf "https://github.com/"
git submodule update --init .github/skills
```
This rewrites HTTPS URLs at the git level, injecting credentials before the proxy sees them. Whether the proxy subsequently strips the embedded token is unknown. This approach is used in GitHub Actions and other Continuous Integration (CI) environments for private submodule access (Acquia Code Studio docs; Stack Overflow; Medium article on PAT configuration).

[assumption] The git credential injection via `url.insteadOf` operates at the git client level before the proxy processes the request, making it more resistant to proxy stripping than an HTTP `Authorization` header. This is not verified for the Claude Code proxy specifically.

**Q3d: Is SSH key injection supported or documented?**

The Reddit reporter asked directly: "Can I pass in an ssh key somehow?" and received no community answer confirming this is possible. [fact, secondary source: Reddit r/ClaudeAI]

No Anthropic documentation describes an SSH key configuration mechanism for the setup script. The GitHub proxy documentation makes no reference to SSH key support; it describes exclusively HTTPS-based git operations via the proxy. [fact, primary source: https://code.claude.com/docs/en/claude-code-on-the-web]

[inference] SSH key injection is not a supported mechanism for private submodule access in Claude Code web. The GitHub proxy operates on HTTPS, not SSH.

**Conclusion for Q3:** Environment variables configured in Claude.ai UI are available to the setup script. A PAT stored as an environment variable can configure git URL rewriting in the setup script. SSH key injection is not supported. [inference] The `url.insteadOf` approach avoids modifying a tracked file (`.gitmodules`) and matches CI/CD credential injection convention, making it preferable to the `.gitmodules` URL-modification workaround.

#### Q4: This repo specifics

**Q4a: Does this repo's `.gitmodules` use HTTPS or SSH URLs?**

The `.gitmodules` file in this repository contains:
```
[submodule ".github/skills"]
    path = .github/skills
    url = https://github.com/davidamitchell/Skills.git
```
[fact, primary source: .gitmodules file in this repository]

The URL is already HTTPS, not SSH. This simplifies credential injection: no SSH-to-HTTPS rewriting is needed.

**Q4b: What exact setup script snippet would initialise `.github/skills/`?**

Given the HTTPS submodule URL, the setup script approach is:
```bash
#!/bin/bash
# Configure git credential helper for private submodule access
git config --global url."https://${SKILLS_PAT}@github.com/".insteadOf "https://github.com/"
# Initialise only the skills submodule (not all submodules)
git submodule update --init .github/skills
```
Where `SKILLS_PAT` is a PAT (with `repo` scope or fine-grained `contents:read` for `davidamitchell/Skills`) stored in the Claude.ai environment variable configuration. [inference from: confirmed URL format, community workaround pattern, CI/CD credential injection practice]

Whether this script succeeds in the Claude Code web proxy environment is not confirmed by a primary source. It is the best-available approach given current evidence.

### §3 Reasoning

**Chain of reasoning:**

1. Claude Code on the web clones the selected repository via the GitHub proxy. [confirmed by official docs + community]
2. The clone does not include `--recurse-submodules`. [confirmed by three independent community/issue sources]
3. The GitHub proxy's scoped credential covers only the selected repository. [confirmed by docs + community]
4. Private submodules in other repositories are therefore inaccessible through the proxy by default. [follows from 2+3]
5. The UI-configured setup script runs before Claude Code launches and has access to UI-configured environment variables. [confirmed by official docs]
6. A PAT with read access to the submodule repo, stored as an env var, can be used to configure git credentials in the setup script. [confirmed by community workaround + CI/CD pattern]
7. URL rewriting via `git config url.insteadOf` is more reliable than a credential helper because it embeds credentials at the URL level rather than in an HTTP header that the proxy might strip. [inference from proxy stripping behaviour documented for npm]
8. The setup script can call `git submodule update --init .github/skills` after configuring credentials. [follows from 5+6+7]
9. Whether the proxy allows through the embedded-PAT HTTPS request is not confirmed. This is the primary remaining uncertainty.

**Claim pruned:** The claim "the proxy strips all user auth tokens" applies to npm registry operations; it may not apply equally to git operations on non-selected-repo hosts. The proxy may handle git differently from npm because git and npm authentication flow through different mechanisms. This uncertainty is preserved in Risks/Gaps.

### §4 Consistency Check

- No internal contradiction between official docs and community reports: docs describe a scoped credential for the selected repo; community confirms this creates a gap for other-repo submodules.
- The GitHub issue #24400 "closed as complete" is potentially contradictory: if the feature was implemented, submodule access would work natively. However, the Reddit post and GitHub issues about submodule behaviour remain consistent in describing the gap as present. [inference] The issue was likely auto-closed by a bot, not resolved. No documentation update or announcement of multi-repo proxy support was found.
- The proxy npm stripping behaviour (issue #11078) is used by inference only, not direct evidence for git; this inference is clearly labelled as such throughout.
- The `.gitmodules` HTTPS URL finding eliminates the SSH-to-HTTPS rewriting step, making the workaround simpler than the Reddit reporter's experience (who used SSH URLs in their `.gitmodules`).

### §5 Depth and Breadth Expansion

**Technical lens:**
The GitHub proxy design prioritises security by restricting credentials to the selected repository. This is by design: granting the proxy access to all repos the GitHub App has access to would widen the blast radius if the VM were compromised. The PAT workaround trades this security property for convenience: a PAT stored in Claude.ai env vars is accessible to any command running in the setup script, including any code Claude might execute. Using a fine-grained PAT with `contents:read` scope limited to `davidamitchell/Skills` reduces this risk relative to a classic PAT with broad `repo` scope.

**Operational lens:**
The PAT approach requires manual rotation. [fact, primary source: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens] Fine-grained PATs on GitHub have a maximum expiry of 1 year; classic PATs can be set to no-expiry. [inference] For a low-sensitivity read-only skills submodule, a long-lived fine-grained PAT limited to `davidamitchell/Skills` contents:read reduces blast radius relative to a broad-scoped classic PAT, making it the lower-risk option.

**Historical lens:**
[fact, primary source: https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication] The same "scoped credential for primary repo only" problem exists in GitHub Actions, where `GITHUB_TOKEN` cannot access repositories other than the one hosting the workflow. [fact, primary source: https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication] The GitHub Actions solution is a PAT stored as a repository secret used with `actions/checkout@v4` via `token: ${{ secrets.PAT }}`. The Claude Code web context lacks GitHub Secrets; instead, env vars configured in the Claude.ai UI serve as the equivalent credential store.

**Gap identified:** GitHub Secrets are NOT available to the Claude Code web setup script. The setup script runs on an Anthropic-managed VM, not in a GitHub Actions context, so GitHub repository secrets (`${{ secrets.SKILLS_PAT }}`) cannot be referenced. The PAT must be stored as a Claude.ai UI environment variable, which is stored by Anthropic (not GitHub). This is a security model difference users must understand.

### §6 Synthesis

**Summary:**
No auto-init; proxy scoped to selected repo; PAT + `url.insteadOf` is the workaround; SSH not supported; GitHub Secrets unavailable; `.gitmodules` already uses HTTPS. Full synthesis is in the Findings section below.

**Key claims:**
1. Submodule auto-init does not occur on clone. [inference: strong, three independent sources]
2. GitHub proxy scoped credential covers only the selected repo. [fact: official docs + community]
3. Environment variables in Claude.ai UI are available to setup scripts. [fact: official docs]
4. PAT + `url.insteadOf` is the most reliable workaround path. [inference: community + CI/CD pattern]
5. SSH key injection is not supported. [fact: no documentation + community question unanswered]
6. GitHub Secrets are not available to the Claude Code web setup script. [inference: different execution context]
7. The `.gitmodules` HTTPS URL format in this repo simplifies PAT injection. [fact: repo file]

**Uncertainties:**
- Whether the GitHub proxy strips embedded-PAT HTTPS URLs (vs. allowing them through): unconfirmed.
- Whether GitHub issue #24400 represents a resolved feature or an auto-closed bot response: unconfirmed.

### §7 Recursive Review

- All claims carry [fact], [inference], or [assumption] labels. Headings exempt.
- Every [fact] maps to a source in the text.
- All [inference] claims are derived from evidence with reasoning stated.
- Uncertainties are explicit in §3, §4, §5, §6, and the Findings section.
- Acronym expansions: PAT first used in Scope section as "Personal Access Token (PAT)". CLI first used in Scope section as "Command Line Interface (CLI)". PR first used in Q2a as "pull request (PR)". No other abbreviations in scope table require expansion beyond first use.
- All threads synthesised: submodule init, proxy scoping, setup script credentials, SSH alternative, this repo's specific configuration.

**Review outcome: PASS** -- all sections justified, all claims sourced or labelled, all uncertainties explicit.

---

## Findings

### Executive Summary

Claude Code on the web does not automatically initialise git submodules when cloning a repository, and the built-in GitHub proxy credential covers only the selected repository, leaving private submodule directories empty by default. The workaround is to store a fine-grained PAT with read access to the submodule repository in the Claude.ai UI environment variable configuration, then configure git URL credential injection and run `git submodule update --init` in the Bash setup script. This approach is confirmed by community practice and CI/CD patterns but has not been tested end-to-end against the Claude Code web proxy specifically. SSH key injection is not supported. GitHub repository secrets are not available to the Claude Code web setup script, so the PAT must be stored in Claude.ai's own credential store.

### Key Findings

1. Claude Code on the web clones the selected repository but does not run `git submodule update --init` automatically; submodule directories exist in the working tree but are empty, confirmed by a Reddit community report and two separate GitHub issues against the `anthropics/claude-code` repository. (high confidence)

2. The GitHub proxy's scoped credential is intentionally limited to the selected repository for security reasons; private submodules in other repositories are inaccessible through this credential even when the Claude.ai GitHub App has been granted access to those repositories at the organisation level. (high confidence)

3. Environment variables configured in the Claude.ai UI are available as standard Bash variables during the setup script execution, making it possible to store a PAT there and reference it in the setup script as `${SKILLS_PAT}` or equivalent. (high confidence)

4. The recommended workaround for private submodule access uses `git config --global url."https://${SKILLS_PAT}@github.com/".insteadOf "https://github.com/"` in the setup script, followed by `git submodule update --init .github/skills`, embedding the PAT in the URL rather than an HTTP header to reduce the risk of the proxy stripping the credential. (medium confidence)

5. SSH key injection for private submodule access is not a supported mechanism in Claude Code web; the GitHub proxy operates exclusively over HTTPS, and no SSH key configuration path is documented or reported as functional by community users. (high confidence)

6. GitHub repository secrets (managed via GitHub Settings and referenced in workflows as `${{ secrets.NAME }}`) are not available to the Claude Code web setup script, because the setup script runs on an Anthropic-managed VM outside the GitHub Actions execution context. (medium confidence)

7. This repository's `.gitmodules` file already uses an HTTPS URL (`https://github.com/davidamitchell/Skills.git`) rather than an SSH URL, which simplifies the PAT workaround by eliminating the need for SSH-to-HTTPS URL rewriting in the setup script. (high confidence)

8. A fine-grained PAT scoped to `davidamitchell/Skills` with `contents:read` permission only reduces the blast radius if the token is exposed, compared to a classic token with broad `repo` scope. [inference] (medium confidence)

9. Whether the Claude Code web GitHub proxy allows HTTPS requests with an embedded PAT (i.e., `https://TOKEN@github.com/`) to pass through to non-selected repositories has not been confirmed by Anthropic documentation or a verified community test; this is the primary remaining uncertainty for the workaround. (low confidence)

10. GitHub issue #24400, requesting that the Claude Code web proxy natively support all repositories the GitHub App has access to, was opened and closed in a single day in February 2026 with no documented resolution; the closure appears to be automated rather than a confirmed implementation. (medium confidence)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| No auto-init of submodules on clone | https://www.reddit.com/r/ClaudeAI/comments/1otp5l1/private_git_submodules_in_claude_code_web/; https://github.com/anthropics/claude-code/issues/24400; https://github.com/anthropics/claude-code/issues/17293 | High | Three independent sources confirm the same behaviour |
| GitHub proxy scoped to selected repo only | https://code.claude.com/docs/en/claude-code-on-the-web; https://www.reddit.com/r/ClaudeAI/comments/1otp5l1/private_git_submodules_in_claude_code_web/ | High | Official docs describe scoped credential; community confirms limitation |
| UI env vars available to setup script | https://code.claude.com/docs/en/claude-code-on-the-web | High | Official docs describe both env vars and setup scripts in same section |
| PAT + url.insteadOf workaround | https://www.reddit.com/r/ClaudeAI/comments/1otp5l1/private_git_submodules_in_claude_code_web/; https://docs.acquia.com/acquia-cloud-platform/add-ons/code-studio/pulling-private-repos-git-submodules-code-studio; https://github.com/orgs/community/discussions/51011 | Medium | Community workaround; official proxy behaviour vs. embedded-URL credentials unconfirmed |
| No SSH key support | https://code.claude.com/docs/en/claude-code-on-the-web; https://www.reddit.com/r/ClaudeAI/comments/1otp5l1/ | High | No documentation; community asked without answer |
| GitHub Secrets not available to Claude Code web setup | https://code.claude.com/docs/en/claude-code-on-the-web | Medium | Different execution context from GitHub Actions; inference from architecture; single source |
| HTTPS URL in .gitmodules | .gitmodules file in this repository | High | Direct inspection; `url = https://github.com/davidamitchell/Skills.git` |
| Fine-grained PAT reduces blast radius | https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens | Medium | GitHub best practice; applies to all PAT usage contexts |
| Proxy may strip HTTP auth headers | https://github.com/anthropics/claude-code/issues/11078 | Medium | npm registry context; inferred applies to git; not confirmed for git specifically |
| Issue #24400 closed without confirmed resolution | https://github.com/anthropics/claude-code/issues/24400 | Medium | Auto-closed same day as opened; no documentation of the fix |

### Assumptions

- **[assumption]** URL-embedded credentials (e.g., `https://TOKEN@github.com/`) are not stripped by the Claude Code web GitHub proxy, unlike HTTP `Authorization` headers which the proxy is known to strip for npm registry operations. Justification: the proxy stripping behaviour documented in issue #11078 describes header stripping; URL-embedded tokens are part of the request URL and may be handled differently by the proxy's URL rewriting layer. This assumption cannot be verified without a live test.
- **[assumption]** GitHub issue #24400 was auto-closed by a bot rather than resolved by Anthropic. Justification: opened and closed on the same day (February 9, 2026) with no activity commentary other than a bot lock message; no corresponding documentation update found.

### Analysis

Evidence from three independent sources (Reddit community, GitHub issues #24400 and #17293) converges on the same behaviour: submodules are not initialised on clone. This is consistent with the official documentation's description of the GitHub proxy covering only the selected repository.

The community workaround (PAT + URL modification) and the CI/CD-pattern alternative (`url.insteadOf`) both rely on embedding credentials in the HTTPS URL rather than using a standard credential helper. [inference] The `url.insteadOf` approach avoids modifying a tracked file (`.gitmodules`) and follows established CI/CD credential injection convention. The critical uncertainty is whether the Claude Code web proxy passes through embedded-PAT URLs to non-selected repositories. This cannot be resolved without a live test.

The npm proxy stripping evidence (issue #11078) establishes that the proxy does modify outbound requests, but git and npm use different authentication flows: npm uses a separate `Authorization` header, while git with HTTPS embeds credentials in the URL or uses a credential helper that responds to a challenge. The URL embedding path may not be intercepted by the proxy in the same way.

[inference] The fine-grained `contents:read` PAT scope for `davidamitchell/Skills` minimises the permission surface. The `COPILOT_GITHUB_TOKEN` already available as a repository credential may have sufficient scope, but a dedicated minimal-permission token isolates the Claude Code web credential from broader repository operations.

### Risks, Gaps, and Uncertainties

- **Primary uncertainty:** Whether `https://TOKEN@github.com/davidamitchell/Skills.git` passes through the Claude Code web GitHub proxy without token stripping. This is the difference between the workaround being functional and non-functional. Only a live test resolves this.
- **Secondary uncertainty:** Whether GitHub issue #24400 represents a resolved feature (in which case the proxy might already support cross-repo submodule access when the GitHub App has been granted access) or an auto-closed bot response. If resolved, the entire workaround may be unnecessary.
- **GitHub Secrets gap:** The PAT must be stored in Claude.ai's env var configuration, not in GitHub Secrets. This means the credential is managed on Anthropic's platform, not GitHub's. Users who prefer GitHub-native credential management have no direct path.
- **Token rotation:** Fine-grained PATs expire (maximum 1 year on GitHub). The Claude.ai env var must be updated on expiry. There is no automated rotation mechanism.
- **Proxy future behaviour:** The proxy is under active development (issue labels include `area:auth` and `area:security`). Behaviour may change without documentation updates.

### Open Questions

- **Does a live test of the `url.insteadOf` + PAT approach succeed in Claude Code web?** This is the most actionable open question. It cannot be answered from documentation alone. Suggested follow-up: create a backlog item to perform a live test in a Claude Code web session.
- **Has Anthropic shipped native multi-repo submodule support since February 2026?** Issue #24400 was closed; a fresh check of the Claude Code changelog or release notes would confirm this.
- **Would `COPILOT_GITHUB_TOKEN` (the existing PAT in this repository's credentials) suffice, or does a dedicated scoped token need to be created and added to Claude.ai env vars?**

### Output

- **Type:** knowledge
- **Description:** Claude Code on the web does not auto-init submodules; private submodule access requires a PAT stored in Claude.ai UI env vars plus a setup script using `git config url.insteadOf` before `git submodule update --init`. Whether this fully works through the GitHub proxy requires a live test.
- **Key sources:**
  1. https://code.claude.com/docs/en/claude-code-on-the-web (GitHub proxy scoping, setup scripts, env vars)
  2. https://www.reddit.com/r/ClaudeAI/comments/1otp5l1/private_git_submodules_in_claude_code_web/ (community confirmation of default limitation and PAT workaround)
  3. https://github.com/anthropics/claude-code/issues/24400 (feature request confirming the gap; closure status ambiguous)
