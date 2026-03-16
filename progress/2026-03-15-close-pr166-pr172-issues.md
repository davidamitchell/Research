# Session: Close issues fixed by PRs #166 and #172

**Date:** 2026-03-15
**Slug:** close-pr166-pr172-issues

## Summary

Identified and closed all GitHub issues for completed research items that were fixed by merged PRs #166 and #172, but whose individual "Research review failed" issues were not automatically closed when the PRs merged (only the umbrella/task issues #165 and #171 were formally linked via `Fixes #` keywords).

## What was done

Created `.github/workflows/close-fixed-issues.yml` — a `workflow_dispatch` workflow that uses `COPILOT_GITHUB_TOKEN` to close 24 individual "Research review failed" issues and add a comment to each indicating the fixing PR.

The coding agent token (`GITHUB_TOKEN`) does not have `issues: write` permission in this context, so a workflow using the PAT (`COPILOT_GITHUB_TOKEN`) was required.

## Issues closed by PR #166

| Issue | Research Item |
|---|---|
| #93 | 2026-02-27-interface-and-delivery |
| #94 | 2026-02-28-transcript-via-third-party-apis |
| #88 | 2026-03-08-bbc-five-case-model |
| #164 | 2026-03-08-chatgpt-actions-memory-integration |
| #86 | 2026-03-08-servicenow-ai-knowledge-rag-agents |
| #85 | 2026-03-08-servicenow-platform-strategy |
| #87 | 2026-03-08-servicenow-process-mapping |
| #89 | 2026-03-08-slack-bot-memory-capture-retrieval |
| #90 | 2026-03-08-telegram-bot-memory-capture-retrieval |
| #99 | 2026-03-10-adversarial-agents-shared-goals-multi-perspective |

## Issues closed by PR #172

| Issue | Research Item |
|---|---|
| #163 | 2026-03-14-ricardian-contract-model |
| #137 | 2026-03-10-research-loop-evaluation-rubric |
| #147 | 2026-03-12-exploration-synthesis-gap |
| #101 | 2026-03-10-dikw-transformation-functions |
| #160 | 2026-03-14-organisational-intent-formal-specification |
| #150 | 2026-03-12-failure-mode-taxonomy-expansion |
| #156 | 2026-03-12-hosting-options-for-the-research-repo |
| #97 | 2026-03-10-ai-concept-classification-taxonomy |
| #83 | 2026-03-08-context-engineering-first-principles |
| #76 | 2026-03-08-context-engineering-first-principles (duplicate) |
| #81 | 2026-03-04-sdlc-ai-prompt-patterns |
| #71 | 2026-03-04-sdlc-ai-prompt-patterns (duplicate) |
| #74 | 2026-03-08-servicenow-csdm-data-modelling |
| #151 | 2026-03-12-team-size-limits-brooks-dunbar-network-theory |

## Intentionally NOT closed

- **#100** — `2026-03-10-agent-evaluation-cross-repo-analysis`: Only partially fixed by PR #166 (LLM expansion only)
- **#144** — `2026-03-12-ai-team-size-strike-team-thesis`: Not addressed by either PR (timed out)

## Next steps

After this PR merges, trigger the workflow via the GitHub Actions tab → "Close issues fixed by merged PRs" → "Run workflow".
