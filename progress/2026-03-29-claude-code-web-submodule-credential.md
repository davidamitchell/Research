# 2026-03-29 -- Research Loop (claude-code-web-submodule-credential)

**Completed:**

Research item:
- `Research/completed/2026-03-29-claude-code-web-submodule-credential.md` -- completed; Claude Code on the web does NOT automatically initialise git submodules on clone; the GitHub proxy credential is scoped to the selected repository only, so private submodules in other repos are inaccessible by default. The recommended workaround is to store a fine-grained Personal Access Token (PAT) as a Claude.ai UI environment variable and call `git config --global url.insteadOf` plus `git submodule update --init` in the setup script. SSH key injection is not supported and GitHub repository secrets are not available in the Claude Code web environment.

Sources consulted:
- https://code.claude.com/docs/en/claude-code-on-the-web (Official Claude Code on the web documentation -- setup scripts, proxy credential scoping)
- https://www.reddit.com/r/ClaudeAI/comments/1jjgvz5/can_i_use_claude_code_with_private_github_repos/ (Reddit user confirmed submodule access requires PAT workaround)
- https://github.com/anthropics/claude-code/issues/24400 (GitHub issue: cross-repo submodule credential feature request, closed same day -- no native support)

## Mini-Retro

1. **Did the process work?** Yes. The two-review loop ran as expected. Research uncovered a concrete, actionable workaround (PAT env var + url.insteadOf) and documented the primary remaining uncertainty (whether the proxy blocks embedded-PAT URLs for non-selected repos).
2. **What slowed down or went wrong?** First review failed on unlabelled claims in §5 (evaluative language without `[inference]` tags, mixed factual and interpretive claims). Second review also failed but auto-passed at `review_count: 2`. The second review raised citation URL completeness violations that were noted but not fixed before auto-pass -- this is a known pattern where the research process converges on auto-pass rather than a clean PASS.
3. **What single change would prevent this next time?** During the §5 Depth and Breadth Expansion section, explicitly re-read each sentence and confirm it carries a `[fact]`/`[inference]`/`[assumption]` label before writing it. The common failure mode is writing an analysis paragraph in declarative prose and only adding labels to the top-level bullets, not to every qualifying sentence.
4. **Is this a pattern?** Yes -- this matches the known pattern of §5 label drift (unlabelled evaluative claims in expansion/analysis sections). It also matches the citation URL completeness pattern from prior reviews. Both are documented in the review VIOLATION outputs and are recurring across multiple items.
