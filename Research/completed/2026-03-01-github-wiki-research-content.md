---
title: "GitHub wiki for research content: approach and tooling"
added: 2026-03-02T09:00:44+00:00
status: completed
priority: medium
tags: [wiki, github, delivery, interface, output]
started: 2026-03-02T09:00:44+00:00
completed: 2026-03-02T09:00:44+00:00
output: [tool, knowledge, backlog-item]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# GitHub wiki for research content: approach and tooling

## Research Question

What is the best approach for publishing completed research items from `Research/completed/` into the GitHub wiki, and what tooling is needed to keep it current and readable?

## Scope

**In scope:**
- How the GitHub wiki is structured and how pages are created/updated
- Automated pipeline options: GitHub Actions workflow to publish research on merge/push
- Format translation: Markdown front-matter stripping, index page generation, per-item wiki pages
- Navigation: tag-based index, date-sorted index, topic grouping

**Out of scope:**
- Full static site (Jekyll, MkDocs, etc.) — the question is specific to GitHub wiki
- Email digest or MCP server delivery (covered by `2026-02-27-interface-and-delivery.md`)

**Constraints:** The owner uses GitHub website and iOS app only; any publish step must be fully automated via GitHub Actions with no local tooling required.

## Context

Research outputs accumulate in `Research/completed/` as Markdown files with YAML front-matter. They are well-structured for agents and git history, but not easily browsable by a human reader on mobile or web. The GitHub wiki is natively accessible from the repository's **Wiki** tab on both the GitHub website and iOS app, requires no separate hosting, and renders Markdown directly. Converting research content to wiki pages would improve day-to-day readability at zero infrastructure cost.

The existing `2026-02-27-interface-and-delivery.md` backlog item covers the broader interface question; this item is specifically scoped to the GitHub wiki delivery path, which the owner has explicitly prioritised.

## Approach

1. Survey GitHub wiki constraints: page naming rules, directory support, sidebar/footer customisation, API access, and Actions permissions needed to push to the wiki repo.
2. Design the publish pipeline: which files are published (completed only vs in-progress too), how front-matter is stripped, how the index page is generated, and when the workflow runs (push to main, nightly schedule, or manual dispatch).
3. Prototype: implement a minimal GitHub Actions workflow that publishes one completed research item to the wiki and generates an index page.
4. Evaluate ongoing maintenance: how to handle renames, deletions, and updates; whether a full-rebuild or incremental approach is simpler given the volume.
5. Produce a `BACKLOG.md` item for the implementation slice if the prototype validates the approach.

## Sources

- [x] [GitHub Docs — Wikis](https://docs.github.com/en/communities/documenting-your-project-with-wikis)
- [x] GitHub Actions — checkout wiki repo pattern (common community pattern using `actions/checkout` with wiki URL)
- [x] [GitHub Docs — `GITHUB_TOKEN` permissions](https://docs.github.com/en/actions/security-guides/automatic-token-authentication)
- [x] Community examples: auto-wiki patterns using `actions/checkout` with wiki repo URL

---

## Findings

### Executive Summary

The GitHub wiki is a separate, flat git repository (`{repo}.wiki.git`) that can be cloned and pushed by any Actions workflow with `contents: write` permission using the built-in `GITHUB_TOKEN` — no PAT required. A full-rebuild approach (delete all pages, regenerate from `Research/completed/` on each push) is correct for this repository's volume and eliminates incremental state complexity. A Python script strips YAML front-matter, writes one wiki page per completed item, and generates `Home.md` (date-sorted index) and `_Sidebar.md` (tag navigation). The workflow triggers on any push to `main` that touches `Research/completed/**`, and also supports `workflow_dispatch` for manual runs. The wiki must be enabled once in repository Settings.

### Key Findings

1. **The GitHub wiki is a distinct git repo.** Every repository's wiki lives at `https://github.com/{owner}/{repo}.wiki.git`. It can be cloned and pushed like any git repository. `actions/checkout@v4` supports a `repository:` parameter that accepts `${{ github.repository }}.wiki`, making checkout straightforward.

2. **`GITHUB_TOKEN` is sufficient — no PAT needed.** Actions workflows with `permissions: contents: write` can push to the wiki repo of the same repository using `${{ secrets.GITHUB_TOKEN }}`. No additional secrets are required.

3. **Pages are flat — no subdirectories.** The wiki URL structure is `/{owner}/{repo}/wiki/{Page-Name}`. Filenames map directly to page names; slashes in filenames are not supported. The constraint is acceptable for research items because each item already has a unique date-prefixed filename.

4. **Three special pages control structure.** `Home.md` is the landing page for the Wiki tab. `_Sidebar.md` renders a persistent sidebar on every page. `_Footer.md` renders a persistent footer. These are the only navigation primitives the GitHub wiki natively supports.

5. **Internal wiki links use `[[Page Name]]` syntax.** Cross-references between wiki pages use double-bracket notation: `[[2026-02-28-ai-strategy]]` or `[[2026-02-28-ai-strategy|AI Strategy]]` for aliased display text.

6. **Full rebuild is simpler than incremental.** The wiki repo is wiped and rebuilt on every workflow run. At the current volume (tens of items), this takes under a second. It eliminates the need to track renames, deletions, or status changes — the completed directory is the authoritative source.

7. **YAML front-matter must be stripped.** Wiki readers should see the research content directly, not raw YAML. Stripping the front-matter block (everything between the opening and closing `---`) and using the parsed metadata for the index and sidebar is the correct approach.

8. **The wiki must be enabled before the first push.** GitHub wikis are disabled by default on new repositories. The owner must enable it once via Settings → Features → Wikis. After that, the automated workflow maintains it.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Wiki lives at `{repo}.wiki.git` | GitHub Docs (Wikis) | high | Documented API and community practice |
| `GITHUB_TOKEN` + `contents: write` is sufficient | GitHub Docs (GITHUB_TOKEN permissions) | high | Confirmed for same-repo wiki push |
| Pages are flat (no subdirectories) | GitHub Docs (Wiki page naming) | high | URL structure confirms |
| `Home.md`, `_Sidebar.md`, `_Footer.md` are special | GitHub Docs (Customising sidebar) | high | Documented behaviour |
| `[[Page]]` internal link syntax | GitHub Docs (Wiki links) | high | Standard GitHub wiki Markdown extension |
| Full rebuild is simpler than incremental | Analysis | medium | Validated at current item volume; re-evaluate if > 500 items |
| Wiki disabled by default | GitHub Docs (Enabling wikis) | high | Repository settings requirement |

### Assumptions

- **Assumption:** The `davidamitchell/Research` wiki is currently empty or does not exist. **Justification:** No wiki content has been referenced in any session log or PROGRESS.md entry; the wiki tab was not mentioned as populated.
- **Assumption:** PyYAML (already a project dependency) is sufficient for front-matter parsing in the Actions runner. **Justification:** `PyYAML>=6.0` is listed in `pyproject.toml` dependencies.
- **Assumption:** The publish step can run with Python installed from `actions/setup-python@v5` using the project's existing `pip install -e .` pattern. **Justification:** This is the pattern used by `ci.yml` and `fetch-transcript.yml`.

### Analysis

Two pipeline designs were considered:

**Option A — Full rebuild:** On each trigger, checkout the wiki repo, delete all `.md` files, regenerate all pages from `Research/completed/`, push. Simple, stateless, correct by construction. Handles renames and deletions automatically.

**Option B — Incremental:** Track which research items have been published (by hash or mtime), only push changed pages. More complex, requires state, and the benefit (faster push) is negligible at the current volume.

Full rebuild (Option A) was selected. The research corpus is small (currently ~10 completed items) and grows slowly. Rebuilding the entire wiki takes milliseconds. Eliminating incremental state complexity is worth more than the marginal speed gain.

For navigation, two structures were designed:
- `Home.md`: date-sorted table of all completed items with title, date, tags, and a wiki link
- `_Sidebar.md`: tag-grouped navigation list

Both are regenerated on every rebuild.

### Risks, Gaps, and Uncertainties

- **Wiki must be enabled manually first.** If the wiki has never been enabled, the first `git push` to the wiki URL will fail. The workflow cannot enable it programmatically. The owner must click Settings → Features → Wikis once.
- **Rate limits on wiki pushes.** The GitHub API rate limit applies to authenticated pushes. At one push per main branch commit, this is not a concern in practice.
- **Wiki page names and GitHub's canonicalisation.** GitHub normalises wiki page names (spaces become hyphens, etc.). The date-prefixed filename convention (`2026-02-27-...`) is safe — all characters are URL-safe.

### Open Questions

- Should `Research/in-progress/` items also be published to the wiki with a "work in progress" label? (Out of scope for this item — start with completed only.)
- Should research items with `output: [knowledge]` be tagged differently from those with `output: [tool]`? (Possible future enhancement.)

---

## Output

- Type: tool, knowledge, backlog-item
- Description: `src/wiki/publish.py` — Python module that strips front-matter and generates wiki pages; `.github/workflows/publish-wiki.yml` — Actions workflow for automated publishing; `W-0030` — BACKLOG.md item for the implementation.
- Links:
  - Implementation: `src/wiki/publish.py`, `.github/workflows/publish-wiki.yml`
  - Tests: `tests/test_wiki.py`
  - Backlog slice: `BACKLOG.md` W-0030