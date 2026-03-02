---
title: "Context Mode: MCP tool output compression and the LLM context window management problem"
added: 2026-03-01
status: completed
priority: high
tags: [llm, context-window, mcp, claude-code, context-management, tooling]
started: 2026-03-01
completed: 2026-03-01
output: [knowledge]
---

# Context Mode: MCP tool output compression and the LLM context window management problem

## Research Question

What is Context Mode's architecture and actual effectiveness for compressing MCP tool outputs in Claude Code, what are its real-world limitations (especially regarding MCP tool interception), and what does it reveal about the broader unsolved problem of LLM context window management for AI coding agents?

## Scope

**In scope:**
- Context Mode architecture: sandboxed execution, SQLite FTS5 knowledge base, subagent routing
- Quantified compression ratios and session-length improvements
- Critical limitation: MCP tool response interception boundary
- The two-sided context problem (definitions vs outputs; Cloudflare Code Mode vs Context Mode)
- Broader context management frontier: pruning, backtracking, agentic context management
- Relevance to this repo's MCP tool usage

**Out of scope:**
- Deep implementation dive into Claude Code's internal architecture
- Training-level context compression (sliding window attention, etc.)

**Constraints:** Primary sources are the blog post and HN discussion thread; GitHub repo for technical detail.

## Context

Spawned from https://mksg.lu/blog/context-mode and HN discussion https://news.ycombinator.com/item?id=47193064. Context window exhaustion is an active bottleneck for long Claude Code sessions, directly relevant to how this repo uses Claude Code agent sessions with 10 MCP servers. Understanding the problem boundary (what Context Mode can and cannot intercept) informs practical decisions about MCP tool design.

## Approach

1. Read and extract architecture from the blog post and GitHub README
2. Extract limitations and edge cases from the HN discussion (empirical testing by commenters)
3. Map the two-sided context problem (input definitions vs output data)
4. Survey broader context management approaches surfaced in the discussion
5. Assess relevance to this repo's MCP configuration and agent session design

## Sources

- [x] https://mksg.lu/blog/context-mode — primary article
- [x] https://news.ycombinator.com/item?id=47193064 — HN discussion with empirical testing
- [x] https://github.com/mksglu/claude-context-mode — GitHub repo (architecture + README)
- [x] https://blog.cloudflare.com/code-mode-mcp/ — Cloudflare Code Mode (input-side compression)
- [ ] https://scottspence.com/posts/optimising-mcp-server-context-usage-in-claude-code — tool definition token counts (referenced but not directly consulted; figures cited via primary article)

---

## Findings

### Executive Summary

The LLM context window has two consumption fronts: tool *definitions* loaded at session start, and tool *outputs* returned during the session. Cloudflare's Code Mode addresses the definition side (99.9% token reduction via code-against-SDK rather than per-operation tools). Context Mode addresses the output side (98% reduction via sandboxed subprocess execution and SQLite FTS5 search). Together these compress what would otherwise be ~1.5 million tokens of overhead into tens of kilobytes. However, Context Mode's output compression has a hard architectural boundary: it cannot intercept responses from third-party MCP tools, which flow via JSON-RPC directly to the model with no hook available. The 98% savings apply only to built-in Claude Code tools and CLI wrappers. For MCP-heavy sessions this is the dominant unsolved case. The broader frontier — selective context pruning, backtracking, agentic self-management — remains open engineering territory.

### Key Findings

1. **The context problem is two-sided, and both sides are now being addressed.** Tool definitions (the input side) can consume the entire context window before a session begins. With 81+ tools active, 143K tokens (72% of a 200K context) are consumed by definitions alone before the first user message. Cloudflare's Code Mode collapses an entire API (e.g., 1.17M tokens of Cloudflare API definitions) into ~1,000 tokens by replacing per-operation tools with two tools — `search()` and `execute()` — that let the model write and run JavaScript against a typed SDK. Context Mode addresses the other direction: tool outputs returned during the session. A single Playwright snapshot is 56 KB; 20 GitHub issues are 59 KB; one access log is 45 KB. After 30 minutes of a typical session, 40% of remaining context is consumed by raw output.

2. **Context Mode's core mechanism is sandboxed subprocess execution, not summarisation.** Each `execute` call spawns an isolated subprocess. The script runs, captures stdout, and only that stdout enters the conversation. Raw data — log files, API responses, snapshots — never reaches the model's context. This is purely algorithmic; no LLM is invoked for compression. Eleven language runtimes are available (JavaScript, TypeScript, Python, Shell, Ruby, Go, Rust, PHP, Perl, R, Elixir). Authenticated CLIs (`gh`, `aws`, `gcloud`, `kubectl`, `docker`) work via credential passthrough — the subprocess inherits environment variables and config paths. When output exceeds 5 KB and an `intent` parameter is supplied, Context Mode switches to intent-driven filtering: it indexes the full output into an FTS5 knowledge base and returns only sections matching the intent.

3. **The knowledge base uses SQLite FTS5 with BM25 ranking, Porter stemming, and a three-layer search fallback.** The `index` tool chunks markdown content by headings (keeping code blocks intact) and stores chunks in a SQLite FTS5 virtual table. BM25 provides probabilistic relevance scoring (term frequency × inverse document frequency × document length normalisation). Porter stemming at index time ensures "running", "runs", and "ran" all match. Search uses a three-layer fallback: (1) Porter-stemmed FTS5 MATCH for standard term matching; (2) trigram substring matching for partial identifiers ("useEff" finds "useEffect"); (3) Levenshtein-based fuzzy correction for typos ("kuberntes" → "kubernetes"). Smart snippet extraction returns windows around matching query terms rather than arbitrary prefixes. Progressive search throttling blocks excessive individual calls after call 9, redirecting the model to `batch_execute`.

4. **Context Mode cannot intercept MCP tool responses — this is a hard architectural boundary, empirically confirmed.** The PreToolUse hook matches only `Bash|Read|Grep|Glob|WebFetch|WebSearch|Task`. MCP tool responses flow via JSON-RPC directly to the model context with no PostToolUse hook available for interception or compression. An HN commenter confirmed this empirically: calling an Obsidian MCP tool produced zero entries in Context Mode's FTS5 database; the full response went straight to context. The SKILL.md in the Context Mode repo itself acknowledges this with an "after-the-fact" decision tree for MCP output — but the context has already been consumed by that point. The 98% savings numbers are real and scoped to built-in Claude Code tools and CLI wrappers (anything replicable as a subprocess). For third-party MCP tools with unique capabilities, the only path is server-side implementation of the same pattern: return compact summaries, store full output in a queryable store, expose drill-down tools.

5. **Subagent routing is as important as the compression itself.** Context Mode includes a PreToolUse hook that injects routing instructions into subagent (Task tool) prompts, teaching them to use `batch_execute` as their primary tool and `search(queries: [...])` for follow-ups. Critically, it auto-upgrades `subagent_type: "Bash"` agents to `general-purpose` — without this upgrade, a Bash subagent cannot call MCP tools and all raw output floods the parent context. The batch execution dimension matters because individual tool calls add per-call overhead; batching multiple commands into one `batch_execute` call further reduces context usage (a repo research subagent went from 37 calls to 5).

6. **BM25 alone underperforms on tool outputs, which mix structured and natural-language data.** An HN commenter who built a hybrid retriever for a 15,800-file Obsidian vault (49,746 chunks, 83 MB) observed that BM25 keyword matching breaks down on JSON, tables, and config files — the structured half of typical tool outputs. Their solution: Model2Vec (potion-base-8M, 256-dimensional embeddings) + sqlite-vec for vector search + FTS5 for BM25, combined via Reciprocal Rank Fusion. RRF merges ranked lists from both retrieval methods without score calibration, providing BM25's exact-match precision on identifiers and function names plus vector search's semantic matching on descriptions and error context. Incremental indexing (hash-based, re-embed only changed chunks) keeps re-indexing under 10 seconds for typical daily changes.

7. **Context Mode's "never let it in" approach preserves prompt caching; post-hoc pruning does not.** The compressed output returned from the sandbox is deterministic for the same query — if the underlying data hasn't changed, the summary is stable. The raw tool output would differ across runs (timestamps, ordering). This means prompt cache entries remain valid across sessions when Context Mode is active, because the big payload never enters the conversation history. Post-hoc context pruning (removing content already in context) invalidates cache entries and requires re-computing cached prefixes, making it expensive to apply retroactively. Pre-filtering at the output boundary is the architecturally cleaner approach.

8. **The broader context management problem — selective pruning, backtracking, agentic self-management — remains open.** The HN discussion surfaced several complementary directions: (a) *backtracking*: once a bug is fixed, the failed attempts in context are noise; pruning them to a stub ("completed fix X") plus a drill-down reference would recover that space without losing the result; (b) *context trees*: treating context like a git undo tree (cherry-pick, rebase) to allow branching debug sessions; (c) *agentic context management*: giving the model a "prune" tool and letting it remove irrelevant context autonomously; (d) *subprocess isolation*: spawning all "work" calls as subprocesses that return a 4-part structured summary (answer, approach, failed attempts, learnings) rather than a raw transcript; (e) *local model summarisation*: running a small local model on log output and feeding only the summary to the powerful model. These approaches are complementary rather than competing.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| 143K tokens (72%) consumed by tool definitions with 81+ tools active | [mksg.lu/blog/context-mode](https://mksg.lu/blog/context-mode), citing [scottspence.com](https://scottspence.com/posts/optimising-mcp-server-context-usage-in-claude-code) | high | Independent third-party measurement cited in primary article |
| 315 KB of session output → 5.4 KB (98% reduction); session from ~30 min to ~3 hours | [mksg.lu/blog/context-mode](https://mksg.lu/blog/context-mode) | medium | Validated across 11 real-world scenarios per author; single-author measurement without independent replication |
| Per-tool compression ratios (Playwright 56 KB → 299 B; git log 153 commits → 107 B) | [github.com/mksglu/claude-context-mode README](https://github.com/mksglu/claude-context-mode) | medium | Plausible given the mechanism; not independently replicated |
| Cloudflare Code Mode compresses 1.17M token API definitions to ~1,000 tokens (99.9%) | [blog.cloudflare.com/code-mode-mcp](https://blog.cloudflare.com/code-mode-mcp) | high | Primary source; methodology described in detail |
| Context Mode cannot intercept MCP tool responses (JSON-RPC bypass) | [HN comment #47202616](https://news.ycombinator.com/item?id=47193064) | high | Empirically tested; confirmed by inspection of PreToolUse hook source |
| BM25 underperforms on structured data (JSON, tables) in tool outputs | [HN comment #47203790](https://news.ycombinator.com/item?id=47193064) | high | Well-known IR limitation; independently observed and addressed |
| Hybrid retrieval (Model2Vec + sqlite-vec + FTS5 + RRF) for 49K-chunk Obsidian vault | [HN comment #47203790](https://news.ycombinator.com/item?id=47193064) | medium | Single practitioner; plausible and consistent with IR literature |
| Prompt cache preserved by "never let it in" vs busted by post-hoc pruning | [mksg.lu/blog/context-mode](https://mksg.lu/blog/context-mode), [HN comment #47200261](https://news.ycombinator.com/item?id=47193064) | high | Mechanistically sound; follows from how prompt caching works |

### Assumptions

- **Assumption:** The compression ratios in the primary article are representative of typical Claude Code sessions. **Justification:** The author validated across 11 scenarios including diverse output types (snapshots, logs, CSVs, git logs, test suites). The figures are plausible given the mechanism. Independent replication would strengthen this.
- **Assumption:** The HN commenter's empirical test of the MCP interception boundary is accurate. **Justification:** The commenter read the source code (PreToolUse hook), tested empirically (called their Obsidian MCP, observed zero FTS5 entries), and cited the specific hook match pattern. The architectural reasoning (JSON-RPC bypass, no PostToolUse hook) is consistent with publicly documented Claude Code architecture.
- **Assumption:** The "no PostToolUse hook in Claude Code" constraint is current as of March 2026. **Justification:** Stated and confirmed in the HN discussion by multiple commenters including the author. This could change in future Claude Code releases.

### Analysis

Context Mode is a practically valuable tool for Claude Code sessions dominated by built-in tool and CLI output. The mechanism is architecturally clean — subprocess isolation with stdout-only passthrough is a well-understood pattern, and the SQLite FTS5 knowledge base is a sensible choice for local full-text retrieval without additional service dependencies. The compression ratios (98%) are credible given the mechanism.

The critical limitation is the MCP interception boundary. For sessions that use MCP heavily — which is the direction the ecosystem is moving — Context Mode's gains are smaller than the headline figures suggest. A session that uses only `gh`, `curl`, `playwright`, and filesystem tools benefits enormously; a session that uses Obsidian, calendar, email, or other third-party MCP tools does not. The HN discussion makes this boundary clear: MCP authors must implement the pattern server-side if they want compressed output. This creates an ecosystem coordination problem — individual MCP server authors have little incentive to compress output unless their users specifically request it.

The BM25 limitation for structured data is real and the hybrid retrieval approach (BM25 + vector + RRF) is a well-established improvement. The question is whether the added complexity and embedding model dependency is warranted for most use cases. For a general-purpose tool that processes diverse outputs, the trigram fallback layer in Context Mode's three-layer search partially addresses the structured-data case for exact identifier matching, but semantic similarity on structured content (e.g., "find the config block that sets the timeout") is not well-served by any keyword approach.

The prompt caching argument is compelling and underappreciated. Post-hoc pruning is attractive conceptually (remove what's no longer needed) but mechanically expensive (cache invalidation). Pre-filtering is cheaper and cleaner. The broader insight — that context architecture should be designed around immutability and cache-preservation, not post-hoc cleanup — has implications for how MCP server authors should design their tool outputs.

The broader context management frontier (backtracking, trees, agentic self-management) is the right long-term direction, but requires either model-level changes or infrastructure that doesn't yet exist in Claude Code. The subprocess isolation pattern (all work calls spawn subprocesses with structured 4-part summaries) is the most immediately practical of these approaches and doesn't require any platform support beyond what's available today.

### Risks, Gaps, and Uncertainties

- The MCP interception boundary may be addressed in future Claude Code releases. If Anthropic adds a PostToolUse hook, the architectural limitation disappears and Context Mode's compression can apply to all tool types.
- The compression benchmarks assume the model writes correct summarisation code on the first attempt. The HN criticism is valid: if the model writes `git log --oneline | wc -l` when specific commit messages were needed, that information is irretrievably gone from context. The cost of wrong extraction scripts is higher than the cost of raw output in context.
- The three-layer search fallback and smart snippet extraction add complexity. The correctness of these layers for all tool output types has not been independently verified.
- The subagent routing hook's effectiveness depends on how reliably Claude Code respects injected routing instructions. This is a prompt-level intervention, not a hard constraint.

### Open Questions

- Will Anthropic add a PostToolUse hook to Claude Code? This would be the architectural fix that removes the MCP interception limitation.
- Is the hybrid retrieval approach (Model2Vec + sqlite-vec + FTS5 + RRF) worth the added dependency for most Claude Code users, or is the three-layer FTS5 fallback sufficient for the 80% case?
- What is the right design pattern for MCP server authors who want to implement output compression? A standard "compact summary + queryable store + drill-down tool" pattern would enable ecosystem-wide adoption but requires coordination.
- How does Context Mode interact with Claude Code's native context compaction? Does compaction undo the gains, or do they compose?
- Is agentic context self-management (giving the model a "prune" tool) safe? The model could prune context it still needs.

---

## Output

- Type: knowledge
- Description: Structured findings on Context Mode architecture, the two-sided context consumption problem, the MCP interception boundary, and the broader context management frontier for AI coding agents.
- Links:
  - https://mksg.lu/blog/context-mode
  - https://github.com/mksglu/claude-context-mode
  - https://blog.cloudflare.com/code-mode-mcp/
  - https://news.ycombinator.com/item?id=47193064
