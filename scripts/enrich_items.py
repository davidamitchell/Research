#!/usr/bin/env python3
"""Enrich completed research items with AI theme tags via Gemini.

For each completed item that lacks an ``ai_themes`` frontmatter field, this
script calls Gemini to identify 3–5 high-level AI research themes and writes
them back into the file.  The run is idempotent: items that already carry
``ai_themes`` are skipped.

Usage:
    # Backfill all items that lack ai_themes (up to --max-items):
    python scripts/enrich_items.py --backfill

    # Enrich a single specific item:
    python scripts/enrich_items.py --item Research/completed/2026-05-09-foo.md

    # Dry run (print what would happen, no writes):
    python scripts/enrich_items.py --backfill --dry-run

Required env var:
    GEMINI_API_KEY — Google Generative AI API key.

Optional env var / config:
    config/sources.yaml gemini.gemini_model — preferred model (overrides the
    cascade head).  Defaults to the cascade built by build_cascade().
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import yaml  # type: ignore[import-untyped]

# ---------------------------------------------------------------------------
# Bootstrap path so we can import src.pipeline even when run as a script.
# ---------------------------------------------------------------------------
_REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(_REPO_ROOT))

from src.pipeline._gemini import _MODEL_CASCADE, build_cascade, generate_with_fallback  # noqa: E402

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

COMPLETED_DIR = _REPO_ROOT / "Research" / "completed"
CONFIG_PATH = _REPO_ROOT / "config" / "sources.yaml"

# Controlled vocabulary of high-level AI research themes.
_AI_THEMES: list[str] = [
    "agentic-ai",          # AI agents, tool use, autonomous systems
    "llm-reasoning",       # reasoning, chain-of-thought, structured output
    "memory-context",      # memory management, context windows, compression
    "multi-agent",         # multi-agent orchestration, coordination patterns
    "rag-retrieval",       # retrieval-augmented generation, vector search
    "governance-policy",   # AI governance, regulation, ethics, risk frameworks
    "benchmarks-eval",     # evaluation, benchmarks, metrics, measurement
    "security-risk",       # adversarial, security, operational risk
    "knowledge-graphs",    # knowledge graphs, ontologies, taxonomies
    "consciousness-cognition",  # consciousness, cognitive science, neuroscience
    "ai-architecture",     # model architecture, training, fine-tuning
    "tools-infrastructure",# MCP, tooling, developer infrastructure, pipelines
    "mlops-deployment",    # deployment, MLOps, production systems
    "workforce-skills",    # workforce impact, skills gaps, capability building
    "cost-performance",    # cost optimisation, efficiency, performance tradeoffs
    "knowledge-management",# PKM, information architecture, wiki, synthesis
]

_THEME_LIST_STR = "\n".join(f"  - {t}" for t in _AI_THEMES)

# Commit every N enriched items to create safe checkpoints.
_COMMIT_BATCH = 20


# ---------------------------------------------------------------------------
# Frontmatter helpers
# ---------------------------------------------------------------------------


def _split_frontmatter(text: str) -> tuple[str, str, str]:
    """Split a markdown file into (opening_fence, yaml_block, body).

    Returns ("", "", text) if no frontmatter is present.
    """
    if not text.startswith("---"):
        return "", "", text
    end = text.find("\n---", 3)
    if end == -1:
        return "", "", text
    fence_open = "---"
    yaml_block = text[3:end].lstrip("\n")
    body = text[end + 4 :].lstrip("\n")
    return fence_open, yaml_block, body


def _has_ai_themes(yaml_block: str) -> bool:
    return re.search(r"^ai_themes\s*:", yaml_block, re.MULTILINE) is not None


def _insert_ai_themes(yaml_block: str, themes: list[str]) -> str:
    """Insert ``ai_themes`` after the ``tags:`` line (or at the end)."""
    themes_yaml = "ai_themes: [" + ", ".join(themes) + "]"

    # Insert after tags: line if present.
    tags_match = re.search(r"^(tags\s*:.*(?:\n  -.*)*)", yaml_block, re.MULTILINE)
    if tags_match:
        insert_pos = tags_match.end()
        return yaml_block[:insert_pos] + "\n" + themes_yaml + yaml_block[insert_pos:]

    # Otherwise append at the end.
    return yaml_block.rstrip() + "\n" + themes_yaml


def _reconstruct(yaml_block: str, body: str) -> str:
    return f"---\n{yaml_block}\n---\n\n{body}"


# ---------------------------------------------------------------------------
# Gemini prompt
# ---------------------------------------------------------------------------


def _build_prompt(title: str, tags: str, summary: str) -> str:
    return f"""You are classifying an AI research item into high-level themes.

Title: {title}
Tags: {tags}
Summary: {summary}

Choose 3–5 themes from this controlled vocabulary:
{_THEME_LIST_STR}

You may add 1–2 novel themes (lowercase, hyphenated) not in the list if the \
item genuinely requires them.

Respond with ONLY a compact JSON array of strings, e.g.:
["agentic-ai", "memory-context", "governance-policy"]
"""


def _extract_themes_from_response(raw: str) -> list[str] | None:
    """Parse Gemini's response into a list of theme strings.

    Handles:
      - Plain JSON array
      - JSON array wrapped in ```json ... ``` fences
      - Inline array embedded in prose
    """
    raw = raw.strip()

    # Strip code fences.
    raw = re.sub(r"^```(?:json)?\s*", "", raw, flags=re.MULTILINE)
    raw = re.sub(r"```\s*$", "", raw, flags=re.MULTILINE)
    raw = raw.strip()

    # Try direct parse first.
    try:
        parsed = json.loads(raw)
        if isinstance(parsed, list) and all(isinstance(t, str) for t in parsed):
            return [t.strip().lower() for t in parsed if t.strip()]
    except json.JSONDecodeError:
        pass

    # Fall back: extract first [...] block.
    m = re.search(r"\[([^\]]+)\]", raw)
    if m:
        try:
            parsed = json.loads("[" + m.group(1) + "]")
            if isinstance(parsed, list) and all(isinstance(t, str) for t in parsed):
                return [t.strip().lower() for t in parsed if t.strip()]
        except json.JSONDecodeError:
            pass

    return None


# ---------------------------------------------------------------------------
# Item processing
# ---------------------------------------------------------------------------


def _extract_summary(body: str, max_chars: int = 400) -> str:
    """Return the first max_chars characters of the Findings section (or body)."""
    findings_match = re.search(r"^##\s+Findings\b(.*?)(?=\n##|\Z)", body, re.DOTALL | re.MULTILINE)
    source = findings_match.group(1).strip() if findings_match else body
    # Strip markdown formatting for cleaner context.
    clean = re.sub(r"\[([^\]]*)\]\([^)]+\)", r"\1", source)  # links
    clean = re.sub(r"\*{1,3}([^*]+)\*{1,3}", r"\1", clean)   # bold/italic
    clean = re.sub(r"`[^`]+`", "", clean)                      # inline code
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean[:max_chars]


def enrich_item(
    path: Path,
    cascade: list[str],
    api_key: str,
    *,
    dry_run: bool = False,
    verbose: bool = True,
) -> bool:
    """Enrich one item.  Returns True if a change was made (or would be made)."""
    text = path.read_text(encoding="utf-8")
    fence, yaml_block, body = _split_frontmatter(text)

    if not fence:
        if verbose:
            print(f"  SKIP (no frontmatter): {path.name}")
        return False

    if _has_ai_themes(yaml_block):
        if verbose:
            print(f"  SKIP (already enriched): {path.name}")
        return False

    # Parse just enough of the frontmatter to build the prompt.
    try:
        meta: dict = yaml.safe_load(yaml_block) or {}
    except yaml.YAMLError:
        meta = {}

    title = str(meta.get("title", path.stem))
    raw_tags = meta.get("tags", [])
    if isinstance(raw_tags, list):
        tags_str = ", ".join(str(t) for t in raw_tags)
    else:
        tags_str = str(raw_tags)
    summary = _extract_summary(body)

    prompt = _build_prompt(title, tags_str, summary)

    if verbose:
        print(f"  Enriching: {path.name}")

    raw_response, model_used = generate_with_fallback(api_key, prompt, cascade)

    themes = _extract_themes_from_response(raw_response)
    if not themes:
        print(f"  WARNING: could not parse themes from response for {path.name}: {raw_response!r}")
        return False

    if verbose:
        print(f"    → {themes}  (via {model_used})")

    if not dry_run:
        new_yaml = _insert_ai_themes(yaml_block, themes)
        path.write_text(_reconstruct(new_yaml, body), encoding="utf-8")

    return True


# ---------------------------------------------------------------------------
# Commit helper
# ---------------------------------------------------------------------------


def _git_commit(message: str) -> None:
    subprocess.run(
        ["git", "add", "-A", "--", str(COMPLETED_DIR)],
        cwd=_REPO_ROOT,
        check=True,
    )
    result = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        cwd=_REPO_ROOT,
    )
    if result.returncode == 0:
        return  # nothing staged
    subprocess.run(
        ["git", "commit", "-m", message],
        cwd=_REPO_ROOT,
        check=True,
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def _load_preferred_model() -> str | None:
    """Read gemini.gemini_model from config/sources.yaml, if present."""
    if not CONFIG_PATH.exists():
        return None
    try:
        raw = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8")) or {}
        return raw.get("gemini", {}).get("gemini_model") or None
    except Exception:
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--backfill", action="store_true", help="Process all items missing ai_themes.")
    mode.add_argument("--item", metavar="PATH", help="Enrich a single item at PATH.")
    parser.add_argument("--max-items", type=int, default=50, metavar="N",
                        help="Max items to process per run in backfill mode (default: 50).")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without writing.")
    parser.add_argument("--model", metavar="MODEL_ID", help="Override preferred model (still cascades on failure).")
    parser.add_argument("--sleep", type=float, default=1.0, metavar="SECS",
                        help="Seconds to sleep between API calls (default: 1.0).")
    parser.add_argument("--commit", action="store_true",
                        help="Git-commit enriched items every --commit-batch items.")
    parser.add_argument("--commit-batch", type=int, default=_COMMIT_BATCH, metavar="N",
                        help=f"Items per commit when --commit is set (default: {_COMMIT_BATCH}).")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        print("ERROR: GEMINI_API_KEY environment variable is not set.", file=sys.stderr)
        return 1

    # Build the model cascade.
    print("Discovering available Gemini models via ListModels API...")
    cascade = build_cascade(api_key)

    # Honour explicit --model or config preference by putting it first.
    preferred = args.model or _load_preferred_model()
    if preferred and preferred not in cascade:
        cascade.insert(0, preferred)
    elif preferred and preferred != cascade[0]:
        cascade.remove(preferred)
        cascade.insert(0, preferred)

    print(f"Model cascade: {cascade}")

    if args.dry_run:
        print("DRY RUN — no files will be written.\n")

    # ------------------------------------------------------------------ #
    # Single-item mode                                                      #
    # ------------------------------------------------------------------ #
    if args.item:
        path = Path(args.item)
        if not path.is_absolute():
            path = _REPO_ROOT / path
        if not path.exists():
            print(f"ERROR: item not found: {path}", file=sys.stderr)
            return 1
        changed = enrich_item(path, cascade, api_key, dry_run=args.dry_run)
        if args.commit and changed and not args.dry_run:
            _git_commit(f"enrich: add ai_themes to {path.name}")
        return 0

    # ------------------------------------------------------------------ #
    # Backfill mode                                                         #
    # ------------------------------------------------------------------ #
    items = sorted(
        (p for p in COMPLETED_DIR.glob("*.md") if p.name.lower() not in ("readme.md",)),
        reverse=True,  # newest first
    )

    # Pre-filter to items that still need enrichment.
    pending = [
        p for p in items
        if not _has_ai_themes(_split_frontmatter(p.read_text(encoding="utf-8"))[1])
    ]

    total_pending = len(pending)
    to_process = pending[: args.max_items]
    print(f"Found {total_pending} items without ai_themes; processing {len(to_process)} this run.\n")

    enriched = 0
    batch_start = 0

    for i, path in enumerate(to_process):
        try:
            changed = enrich_item(path, cascade, api_key, dry_run=args.dry_run)
            if changed:
                enriched += 1
        except Exception as exc:
            print(f"  ERROR enriching {path.name}: {exc}")

        # Commit checkpoint.
        if (
            args.commit
            and not args.dry_run
            and enriched > 0
            and enriched % args.commit_batch == 0
        ):
            batch_end = i + 1
            _git_commit(
                f"enrich: add ai_themes to items {batch_start + 1}–{batch_end} of {len(to_process)}"
            )
            batch_start = batch_end

        if i < len(to_process) - 1:
            time.sleep(args.sleep)

    # Final commit for any remaining items.
    if args.commit and not args.dry_run and enriched > 0:
        _git_commit(f"enrich: add ai_themes — {enriched} items enriched ({total_pending - enriched} remaining)")

    print(f"\nDone. Enriched {enriched} / {len(to_process)} items.")
    if total_pending > len(to_process):
        remaining = total_pending - enriched
        print(f"Re-run to process the remaining ~{remaining} items.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
