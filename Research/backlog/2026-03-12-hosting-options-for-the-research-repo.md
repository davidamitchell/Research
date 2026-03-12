---
title: "Hosting options for the Research repo"
added: 2026-03-12
status: backlog
priority: medium
blocks: []
tags: [hosting, static-site, search, vector-db, infrastructure, free-tier]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# Hosting options for the Research repo

## Research Question

What is the best free or very-low-cost hosting option for this research repository that supports full-text search, and optionally vector/graph database capabilities, without requiring SEO, custom DNS, or authentication?

## Scope

**In scope:**
- Free or very-low-cost hosting platforms (GitHub Pages, Cloudflare Pages, Netlify free tier, Vercel hobby, etc.)
- Static-site generators that convert Markdown to HTML (Jekyll, MkDocs, Docusaurus, Quartz, etc.)
- Client-side search options (Pagefind, Lunr.js, FlexSearch, Fuse.js, Orama) with domain/tag filtering
- Server-side or edge-hosted vector DBs on free tiers (LanceDB, ChromaDB, Qdrant Cloud, Weaviate Cloud)
- Graph database free tiers (Neo4j AuraDB free, FalkorDB, etc.)
- Hybrid approaches: static front-end + serverless/edge API for semantic search

**Out of scope:**
- SEO optimisation
- Custom domain / DNS setup
- Authentication or access control
- Paid hosting tiers above ~$5/month

**Constraints:** Must work with the existing GitHub-based workflow (push to main → deploy). No local build toolchain required from the owner; all builds run in GitHub Actions.

## Context

The research content in `Research/completed/` is growing. A hosted, searchable view would make findings easier to browse and reference — both for the owner and any collaborators. The wiki (current publish target) has limited search and no vector/semantic capability. A dedicated hosting approach could provide richer search (keyword + semantic) and structured navigation by tag, domain, or topic. The owner is comfortable with a static site if it includes JS-powered domain filtering.

## Approach

1. Survey free/low-cost static hosting platforms — features, build integration, bandwidth limits.
2. Evaluate static-site generators for Markdown-heavy research content (navigation, tagging, search plugins).
3. Assess client-side search libraries: keyword search + domain/tag filtering without a server.
4. Assess vector DB free tiers that could back a semantic search endpoint (edge function or serverless).
5. Assess graph DB free tiers for relationship-based navigation.
6. Identify the simplest end-to-end stack that meets the requirements and fits the existing GitHub Actions workflow.
7. Produce a recommendation with pros/cons and a concrete implementation sketch.

## Sources

- [ ] GitHub Pages docs — https://docs.github.com/en/pages
- [ ] Cloudflare Pages — https://pages.cloudflare.com
- [ ] Netlify free tier — https://www.netlify.com/pricing/
- [ ] Vercel hobby — https://vercel.com/pricing
- [ ] Quartz (Obsidian-style static site) — https://quartz.jzhao.xyz
- [ ] MkDocs Material — https://squidfunk.github.io/mkdocs-material/
- [ ] Pagefind (static search) — https://pagefind.app
- [ ] Orama (in-browser vector search) — https://orama.com
- [ ] LanceDB serverless — https://lancedb.github.io/lancedb/
- [ ] Qdrant Cloud free tier — https://qdrant.tech/pricing/
- [ ] Neo4j AuraDB free — https://neo4j.com/cloud/platform/aura-graph-database/

---

## Findings

*(Fill in when completing. Follow the research skill synthesis structure.)*

### Executive Summary

### Key Findings

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

- **Assumption:** ... **Justification:** ...

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

- Type:
- Description:
- Links:
