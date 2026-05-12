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
    config/sources.yaml gemini.gemini_model — starting model for the cascade.
    Defaults to the first entry in _MODEL_CASCADE (gemini-3-flash).
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
import subprocess
import sys
from pathlib import Path

import yaml  # type: ignore[import-untyped]

# ---------------------------------------------------------------------------
# Bootstrap path so we can import src.pipeline even when run as a script.
# ---------------------------------------------------------------------------
_REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(_REPO_ROOT))

from src.logger import get_logger  # noqa: E402
from src.pipeline._gemini import _MODEL_CASCADE, _ModelCascade, make_gemini_client  # noqa: E402

logger = get_logger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

COMPLETED_DIR = _REPO_ROOT / "Research" / "completed"
CONFIG_PATH = _REPO_ROOT / "config" / "sources.yaml"

# Controlled vocabulary of high-level AI research themes.
_AI_THEMES: list[str] = [
    "agentic-ai",  # AI agents, tool use, autonomous systems
    "llm-reasoning",  # reasoning, chain-of-thought, structured output
    "memory-context",  # memory management, context windows, compression
    "multi-agent",  # multi-agent orchestration, coordination patterns
    "rag-retrieval",  # retrieval-augmented generation, vector search
    "governance-policy",  # AI governance, regulation, ethics, risk frameworks
    "benchmarks-eval",  # evaluation, benchmarks, metrics, measurement
    "security-risk",  # adversarial, security, operational risk
    "knowledge-graphs",  # knowledge graphs, ontologies, taxonomies
    "consciousness-cognition",  # consciousness, cognitive science, neuroscience
    "ai-architecture",  # model architecture, training, fine-tuning
    "tools-infrastructure",  # MCP, tooling, developer infrastructure, pipelines
    "mlops-deployment",  # deployment, MLOps, production systems
    "workforce-skills",  # workforce impact, skills gaps, capability building
    "cost-performance",  # cost optimisation, efficiency, performance tradeoffs
    "knowledge-management",  # PKM, information architecture, wiki, synthesis
]

_THEME_LIST_STR = "\n".join(f"  - {t}" for t in _AI_THEMES)

# Commit every N enriched items to create safe checkpoints.
_COMMIT_BATCH = 20

# Default RPM for rate limiting (Gemini free-tier is 15 RPM).
_DEFAULT_RPM = 15


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
    yaml_block = text[3:end].lstrip("\n")
    body = text[end + 4 :].lstrip("\n")
    return "---", yaml_block, body


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
    return yaml_block.rstrip() + "\n" + themes_yaml


def _reconstruct(yaml_block: str, body: str) -> str:
    return f"---\n{yaml_block}\n---\n\n{body}"


# ---------------------------------------------------------------------------
# Gemini prompt
# ---------------------------------------------------------------------------


def _build_prompt(title: str, tags: str, summary: str) -> str:
    return (
        "You are classifying an AI research item into high-level themes.\n\n"
        f"Title: {title}\n"
        f"Tags: {tags}\n"
        f"Summary: {summary}\n\n"
        "Choose 3–5 themes from this controlled vocabulary:\n"
        f"{_THEME_LIST_STR}\n\n"
        "You may add 1–2 novel themes (lowercase, hyphenated) not in the list "
        "if the item genuinely requires them.\n\n"
        "Respond with ONLY a compact JSON array of strings, e.g.:\n"
        '["agentic-ai", "memory-context", "governance-policy"]'
    )


def _parse_themes(raw: str) -> list[str] | None:
    """Parse Gemini response into a list of theme strings."""
    raw = raw.strip()
    # Strip code fences.
    raw = re.sub(r"^```(?:json)?\s*", "", raw, flags=re.MULTILINE)
    raw = re.sub(r"```\s*$", "", raw, flags=re.MULTILINE)
    raw = raw.strip()
    # Direct parse.
    try:
        parsed = json.loads(raw)
        if isinstance(parsed, list) and all(isinstance(t, str) for t in parsed):
            return [t.strip().lower() for t in parsed if t.strip()]
    except json.JSONDecodeError:
        pass
    # Extract first [...] block.
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
    clean = re.sub(r"\[([^\]]*)\]\([^)]+\)", r"\1", source)
    clean = re.sub(r"\*{1,3}([^*]+)\*{1,3}", r"\1", clean)
    clean = re.sub(r"`[^`]+`", "", clean)
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean[:max_chars]


def _generate_themes(
    client: object,
    cascade: _ModelCascade,
    prompt: str,
    *,
    max_output_tokens: int = 500,
) -> tuple[list[str] | None, str]:
    """Call Gemini and parse the theme list.

    Returns (themes, model_used).  themes is None if the call failed or the
    response could not be parsed.
    """
    from google.genai import types  # noqa: PLC0415

    cascade.wait()
    try:
        # gemini-2.5-flash uses thinking tokens that count against
        # max_output_tokens. Disable thinking to avoid truncated JSON responses.
        model = cascade.model
        thinking_config = None
        if "2.5-flash" in model:
            thinking_config = types.ThinkingConfig(thinking_budget=0)
        response = client.models.generate_content(  # type: ignore[union-attr]
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                max_output_tokens=max_output_tokens,
                temperature=0.2,
                thinking_config=thinking_config,
            ),
        )
        model_used = model
        raw = response.text or ""
    except Exception as exc:
        # Check for quota exhaustion and advance the cascade.
        exc_module = type(exc).__module__
        if exc_module.startswith("google.genai"):
            is_quota = False
            try:
                from google.genai.errors import ClientError as _ClientError  # noqa: PLC0415

                if isinstance(exc, _ClientError):
                    status = getattr(exc, "status_code", None) or getattr(exc, "code", None)
                    is_quota = status in (429, 403)
            except ImportError:
                pass
            if is_quota:
                logger.warning(
                    "Quota/rate-limit error on %r — advancing cascade: %s",
                    cascade.model,
                    exc,
                )
                cascade.advance()
                return None, cascade.model
        logger.warning("Gemini call failed for model %r: %s", cascade.model, exc)
        cascade.advance()
        return None, cascade.model

    if cascade.check_daily_quota_header():
        cascade.advance()

    themes = _parse_themes(raw)
    if themes is None:
        logger.warning("Could not parse themes from response: %r", raw)
    return themes, model_used


def enrich_item(
    path: Path,
    client: object,
    cascade: _ModelCascade,
    *,
    dry_run: bool = False,
) -> bool:
    """Enrich one item.  Returns True if a change was made (or would be made)."""
    text = path.read_text(encoding="utf-8")
    fence, yaml_block, body = _split_frontmatter(text)

    if not fence:
        logger.debug("SKIP (no frontmatter): %s", path.name)
        return False
    if _has_ai_themes(yaml_block):
        logger.debug("SKIP (already enriched): %s", path.name)
        return False

    try:
        meta: dict = yaml.safe_load(yaml_block) or {}
    except yaml.YAMLError:
        meta = {}

    title = str(meta.get("title", path.stem))
    raw_tags = meta.get("tags", [])
    tags_str = ", ".join(str(t) for t in raw_tags) if isinstance(raw_tags, list) else str(raw_tags)
    summary = _extract_summary(body)
    prompt = _build_prompt(title, tags_str, summary)

    logger.info("Enriching: %s", path.name)

    if cascade.all_exhausted:
        logger.error("All models exhausted — cannot enrich %s", path.name)
        return False

    themes, model_used = _generate_themes(client, cascade, prompt)

    if themes is None:
        return False

    logger.info("  → %s  (via %s)", themes, model_used)

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
        return
    subprocess.run(["git", "commit", "-m", message], cwd=_REPO_ROOT, check=True)


# ---------------------------------------------------------------------------
# Config helper
# ---------------------------------------------------------------------------


def _load_starting_model() -> str:
    """Read gemini.gemini_model from config/sources.yaml, defaulting to cascade head."""
    if not CONFIG_PATH.exists():
        return _MODEL_CASCADE[0]
    try:
        raw = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8")) or {}
        return str(raw.get("gemini", {}).get("gemini_model") or _MODEL_CASCADE[0])
    except Exception:
        return _MODEL_CASCADE[0]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--backfill", action="store_true", help="Process all items missing ai_themes."
    )
    mode.add_argument("--item", metavar="PATH", help="Enrich a single item at PATH.")
    parser.add_argument(
        "--max-items",
        type=int,
        default=50,
        metavar="N",
        help="Max items per run in backfill mode (default: 50).",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print actions without writing.")
    parser.add_argument(
        "--model",
        metavar="MODEL_ID",
        help="Override starting model in the cascade (default: from config).",
    )
    parser.add_argument(
        "--rpm",
        type=int,
        default=_DEFAULT_RPM,
        metavar="N",
        help=f"Requests per minute for rate limiting (default: {_DEFAULT_RPM}).",
    )
    parser.add_argument(
        "--commit",
        action="store_true",
        help=f"Git-commit enriched items every {_COMMIT_BATCH} items.",
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug logging.")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format="%(levelname)s %(name)s %(message)s",
    )

    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        logger.error("GEMINI_API_KEY environment variable is not set.")
        return 1

    starting_model = args.model or _load_starting_model()
    logger.info("Building Gemini client — starting model: %s", starting_model)

    client, http_client = make_gemini_client(api_key)
    cascade = _ModelCascade(starting_model, rpm=args.rpm, http_client=http_client)

    logger.info("Model cascade: %s", cascade._models)

    if args.dry_run:
        logger.info("DRY RUN — no files will be written.")

    # ------------------------------------------------------------------ #
    # Single-item mode                                                      #
    # ------------------------------------------------------------------ #
    if args.item:
        path = Path(args.item)
        if not path.is_absolute():
            path = _REPO_ROOT / path
        if not path.exists():
            logger.error("Item not found: %s", path)
            return 1
        changed = enrich_item(path, client, cascade, dry_run=args.dry_run)
        if args.commit and changed and not args.dry_run:
            _git_commit(f"enrich: add ai_themes to {path.name}")
        return 0

    # ------------------------------------------------------------------ #
    # Backfill mode                                                         #
    # ------------------------------------------------------------------ #
    items = sorted(
        (p for p in COMPLETED_DIR.glob("*.md") if p.name.lower() != "readme.md"),
        reverse=True,
    )
    pending = [
        p for p in items if not _has_ai_themes(_split_frontmatter(p.read_text(encoding="utf-8"))[1])
    ]
    total_pending = len(pending)
    to_process = pending[: args.max_items]
    logger.info(
        "Found %d items without ai_themes; processing %d this run.",
        total_pending,
        len(to_process),
    )

    enriched = 0
    for i, path in enumerate(to_process):
        if cascade.all_exhausted:
            logger.error("All models in cascade exhausted — stopping backfill.")
            break
        try:
            changed = enrich_item(path, client, cascade, dry_run=args.dry_run)
            if changed:
                enriched += 1
        except Exception as exc:
            logger.error("Error enriching %s: %s", path.name, exc)

        if args.commit and not args.dry_run and enriched > 0 and enriched % _COMMIT_BATCH == 0:
            _git_commit(
                f"enrich: add ai_themes to items {i + 1 - _COMMIT_BATCH + 1}–{i + 1} "
                f"of {len(to_process)}"
            )

    if args.commit and not args.dry_run and enriched > 0:
        _git_commit(
            f"enrich: add ai_themes — {enriched} items enriched "
            f"({total_pending - enriched} remaining)"
        )

    logger.info("Done. Enriched %d / %d items.", enriched, len(to_process))
    if total_pending > len(to_process):
        logger.info("Re-run to process the remaining ~%d items.", total_pending - enriched)

    return 0


if __name__ == "__main__":
    sys.exit(main())
