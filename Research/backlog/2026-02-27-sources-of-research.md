---
title: "Sources of research: what to monitor and how"
added: 2026-02-27
status: backlog
priority: medium
tags: [sources, discovery, rss, youtube, arxiv]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# Sources of research: what to monitor and how

## Question / Hypothesis

What are the best sources for AI/ML research, and what is the right monitoring strategy for each — RSS, YouTube channels, arXiv, newsletters, GitHub?

## Context

Research quality depends heavily on source quality. The companion repo (`davidamitchell/Latest-developments-`) monitors a handful of YouTube channels and RSS feeds. This repo should have a broader, more intentional source strategy covering:

- Academic preprints (arXiv)
- YouTube channels (practitioners explaining new work)
- Newsletters and blogs
- GitHub (repos, issues, discussions)
- Podcasts and interviews

Each source type has different access patterns, freshness, signal/noise ratios, and tooling requirements.

## Scope

**In scope:**
- Cataloguing high-quality source types for AI/ML research
- Evaluating monitoring mechanisms for each
- Deciding what belongs in `config/sources.yaml`

**Out of scope:**
- Building the fetchers (separate items)

## Approach

1. Inventory current sources in `davidamitchell/Latest-developments-/config/sources.yaml`
2. Survey what other researchers use (arXiv RSS, Hugging Face Daily Papers, etc.)
3. Evaluate the `arxiv` MCP server for paper discovery
4. Write a recommended source list with monitoring approach for each

## Sources

- [ ] `davidamitchell/Latest-developments-/config/sources.yaml`
- [ ] Hugging Face Daily Papers: https://huggingface.co/papers
- [ ] arXiv RSS feeds: https://arxiv.org/help/rss
- [ ] `arxiv` MCP server: `@blazickjp/arxiv-mcp-server`

## Findings

*(Fill in when completing. Follow the research skill synthesis structure.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly.

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim.

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

Explicit assumptions made during the investigation and the justification for each.

- **Assumption:** ... **Justification:** ...

### Analysis

How the evidence was weighed, what trade-offs were identified, and how competing interpretations were resolved.

### Risks, Gaps, and Uncertainties

What is still unknown? Where does the evidence fall short? What could change the conclusion?

-

### Open Questions

Questions that surfaced during research but are out of scope for this item. Each may become a new backlog item.

-

---

## Output

- Type: knowledge, backlog-item
- Description: `config/sources.yaml` populated with curated source list; backlog items for fetchers
