---
title: "Simple process for adding a research item"
added: 2026-03-02T08:23:20+00:00
status: completed
priority: high
tags: [process, workflow, tooling]
started: 2026-03-02T08:23:20+00:00
completed: 2026-03-02T08:23:20+00:00
output: [tool, knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Simple process for adding a research item

## Question / Hypothesis

What is the minimum-friction workflow for adding a new research item so that good ideas get captured before they are lost?

## Context

Without a fast capture process, high-value research ideas get lost or deferred indefinitely. The current process (copy template, rename file, fill in fields, commit) has several manual steps. There may be a better approach — CLI command, GitHub issue template, voice note → text, etc.

## Scope

**In scope:**
- Evaluating CLI-based item creation (`python -m src.main research add "<title>"`)
- Evaluating GitHub issue templates as a capture mechanism
- Mobile-friendly capture options

**Out of scope:**
- Full research management UI

## Approach

1. Review how similar tools (Zettelkasten apps, research notebooks) handle quick capture
2. Prototype the CLI command approach (maps to `BACKLOG.md` Epic 1.1)
3. Evaluate trade-offs: CLI vs issue template vs direct file edit

## Sources

- [x] Zettelkasten quick-capture patterns
- [x] GitHub issue template docs — https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests

## Findings

### Executive Summary

The minimum-friction capture path splits by actor: agents use `python -m src.main research add "<title>"`, which already exists and requires a single argument. The repository owner, who operates exclusively via GitHub website and iOS app, has no usable fast-capture path today. A GitHub issue form template paired with a GitHub Actions workflow that converts a new issue into a committed backlog file closes this gap. The canonical Zettelkasten principle — capture now, structure later — validates deferring all metadata except the title to the `research start` step.

### Key Findings

1. `python -m src.main research add "<title>"` is fully implemented in `src/research/cli.py`. It creates a dated backlog file with a template, requiring only a title. This is the lowest-friction path for any agent or automated process.
2. The repository owner operates exclusively via GitHub website and iOS app; the CLI is inaccessible without a terminal. A capture mechanism that works from any browser is required for the owner.
3. GitHub issue forms (`.github/ISSUE_TEMPLATE/*.yml`) render as structured, mobile-responsive web forms — accessible from the iOS GitHub app and any browser without any local tooling.
4. A GitHub Actions workflow triggered on `issues: [opened]` with a specific label can parse the issue title and body, then call `python -m src.main research add` (or directly commit a new backlog file), automating the issue-to-file conversion.
5. Zettelkasten systems converge on a two-phase model: (a) instant frictionless capture into a single inbox with minimal metadata, and (b) batch structuring during a later review pass. Forcing structure at capture increases abandonment.
6. The existing template already supplies all default metadata (`status: backlog`, `priority: medium`, `started: ~`, `completed: ~`). Only `title` is needed at capture time; all other fields can be populated when the item is started.
7. GitHub's issue form schema supports `input`, `textarea`, `dropdown`, and `checkboxes` fields, and renders correctly on mobile. A minimal form with only a title field and an optional context textarea is sufficient for research capture.
8. Direct file creation via the GitHub website file editor is possible but high-friction: it requires navigating to the correct folder, naming the file with the correct date-slug convention, and pasting the template — typically 6–8 manual steps.
9. The two-capture-path design (CLI for agents, issue form for owner) requires no breaking changes to the existing workflow and the existing CLI command serves as the implementation target for the Actions automation.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| `cmd_add` is implemented requiring only a title | `src/research/cli.py` (inspected) | high | Creates dated backlog file; template supplies all other fields |
| Owner uses GitHub website / iOS only, no terminal | `AGENTS.md` § Working Environment | high | Explicit constraint |
| GitHub issue forms render as mobile-responsive web forms | [GitHub Docs: Syntax for Issue Forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms) | high | YAML `.yml` files in `.github/ISSUE_TEMPLATE/` |
| `issues: [opened]` Actions event can trigger file commits | [GitHub Docs: Using GitHub CLI in workflows](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-github-cli) | high | Standard pattern; `GITHUB_TOKEN` sufficient |
| Zettelkasten principle: capture now, structure later | [The Simple Zettelkasten](https://deepread.com/the-simple-zettelkasten/) | high | Consistent across multiple sources |
| Forcing metadata at capture increases abandonment | [Zettelkasten Method Step By Step Tutorial](https://www.mindswiftly.com/blog/zettelkasten-method-step-by-step-tutorial-unlocking-your-creative-workflow) | medium | Principle-level claim; validated by multiple secondary sources |
| Direct file creation via GitHub website requires 6–8 steps | Observed by inspecting current process | medium | Manual step count; exact number varies |
| Issue form iOS compatibility | [GitHub Docs: Configuring issue templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository) | high | GitHub renders forms in its web UI; iOS app opens web issues |

### Assumptions

- **Assumption:** The `GITHUB_TOKEN` auto-provided in Actions is sufficient to commit a new file to `main`. **Justification:** The token has repository write access by default for standard Actions workflows on the same repo.
- **Assumption:** The owner creates issues via the GitHub iOS app or website, not via API. **Justification:** Working environment constraint in `AGENTS.md`.
- **Assumption:** A single-field form (title only) is sufficient for capture; context is optional. **Justification:** Zettelkasten inbox principle — process atomicity happens later, not at capture.

### Analysis

Two capture paths are needed because the actors are different. Agents (including the research loop workflow) already have a working path via `research add`. The gap is entirely on the owner side, where the only tools are a web browser and the iOS GitHub app.

GitHub issue forms are the right solution for the owner path because: (a) they work natively on iOS via the GitHub app, (b) they are already part of the GitHub workflow the owner uses for other interactions (issue comments, PR reviews), and (c) a triggered Actions workflow can close the loop by converting the issue to a committed backlog file automatically — requiring zero follow-up steps from the owner after submitting the form.

The alternative of owner direct-file-creation via the GitHub web editor was rejected because it requires manual adherence to date-slug naming conventions and template structure. One transcription error breaks the CLI's file parsing. An issue form abstracts those implementation details.

The alternative of a voice note → text pipeline was considered but depended on external tooling (AI transcription services) not currently available in the credential table and would introduce a new external dependency requiring owner approval. It remains an open question.

### Risks, Gaps, and Uncertainties

- The Actions workflow that converts issues to backlog files does not yet exist. This finding identifies the approach; implementation is a separate backlog item.
- If the issue form is submitted with an empty title, the slug function will produce an unhelpful filename. The form should mark title as `required: true`.
- Label-based routing (using a specific label to distinguish "research capture" issues from other issue types) needs agreement on the label name (e.g., `research-capture`).
- The iOS GitHub app renders issue forms via an in-app web view; complex field types (multi-select dropdowns) may have inconsistent mobile UX. Keeping the form to `input` and `textarea` fields avoids this.

### Open Questions

- Should the Actions workflow close the issue after creating the backlog file, or leave it open for discussion? Closing reduces noise; leaving open allows comments.
- Would a voice-to-research-item path (e.g., using a GitHub Action that calls a speech-to-text API on an audio attachment) be worth evaluating? Depends on whether an API credential can be added.
- Should the issue form pre-populate a `priority` dropdown, or default all captures to `medium` and let the owner triage separately?

---

## Output

- Type: knowledge
- Description: Recommended two-path capture design — CLI for agents, GitHub issue form + Actions workflow for owner. Documents existing `research add` CLI command and the gap it does not close.
- Links:
  - https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms
  - https://deepread.com/the-simple-zettelkasten/
  - https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository