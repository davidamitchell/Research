"""Process evaluation harness.

Randomly samples completed research items and runs them through a specified
process step (e.g., research-prompt.md §0.5b Perspective Discovery step) to
produce a reusable prompt bundle.  When pre-computed Large Language Model
(LLM) responses are provided via ``--responses-dir``, the harness also scores
each response against the original item using deterministic metrics (no live
LLM call required).

Purpose
-------
New or modified process steps (such as the research-prompt.md §0.5b
Perspective Discovery step added to ``research-prompt.md``) can be evaluated
by:

1. Running this script to generate prompts from N random past items.
2. Pasting each prompt into any LLM (or automating via ``--llm-provider``).
3. Saving each response as ``<slug>.txt`` into a responses directory.
4. Re-running with ``--responses-dir`` to compute comparison scores.

The report is written as JSON + Markdown to ``state/eval_reports/``.

Usage
-----
::

    # Generate prompt bundle for 5 random items (perspective-discovery)
    python scripts/eval_harness.py --process perspective-discovery --n 5

    # Reproduce the same sample
    python scripts/eval_harness.py --process perspective-discovery --n 5 --seed 42

    # Score against pre-computed LLM responses
    python scripts/eval_harness.py --process perspective-discovery --n 5 --seed 42 \\
        --responses-dir /tmp/responses/

    # List available processes
    python scripts/eval_harness.py --list-processes
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

# Make src/ importable when running the script directly from the repo root.
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.logger import get_logger

logger = get_logger(__name__)

# ---------------------------------------------------------------------------
# Process step registry
# ---------------------------------------------------------------------------

_PERSPECTIVE_DISCOVERY_TEMPLATE = """\
You are conducting research. Your task is to complete §0.5b Perspective Discovery
before beginning investigation on the following research question.

Research Question:
{question}

Tags (topic area): {tags}

---

### §0.5b Perspective Discovery

Before §1 Question Decomposition, generate exactly four non-overlapping research
perspectives for the question above. Use these four slots:

1. **Basic facts lens** — what a broad factual writer must cover first.
2. **Mechanism or implementation lens** — how the thing works, is built, or fails operationally.
3. **Stakeholder or decision-impact lens** — who is affected, who decides, and what trade-offs matter.
4. **Failure-mode or critic lens** — what could be missing, misleading, risky, or overstated.

For each perspective, output exactly:
- Perspective: <short role label>
- Distinct coverage added: <one sentence on what this lens sees that the others may miss>
- Seed question: <one concrete research question this lens would ask first>
- Evidence to seek: <the kind of source most likely to answer that question>

Constraints:
- Prefer non-overlap over stylistic variety — if two perspectives collapse into the
  same question class, rewrite one.
- Keep every seed question specific enough that it can be decomposed into atomic sub-questions.
- Do not answer the questions yet.

Output only the four perspectives, nothing else.
"""

_QUESTION_DECOMPOSITION_TEMPLATE = """\
You are conducting research. Your task is to complete §1 Question Decomposition
for the following research question.

Research Question:
{question}

Approach sub-questions from the item:
{approach}

Tags (topic area): {tags}

---

### §1 Question Decomposition

Recursively break the Approach sub-questions into atomic questions — each
answerable with a single evidence-based claim. For each atomic question, note:
- The parent Approach sub-question it belongs to
- Whether it is a factual, definitional, comparative, or evaluative question

Output the full decomposition tree. Do not answer the questions yet.
"""

_ADVERSARIAL_CHALLENGE_TEMPLATE = """\
You are conducting research. Your task is to complete §4.5 Adversarial Challenge
on the following draft key findings.

Research Question:
{question}

Draft Key Findings:
{key_findings}

Tags (topic area): {tags}

---

### §4.5 Adversarial Challenge

Adopt the position of a sceptic or an adjacent-domain expert. Generate at least
two objections to the draft findings — what would a domain expert challenge or
dispute?

For each objection:
1. State the objection clearly.
2. Determine whether the evidence gathered resolves it. If yes, explain how.
3. If the objection is unresolved, mark it with the label ``[unresolved objection]``.

Format each objection as:
**Objection N:** <statement>
**Resolution:** <resolved: explanation> OR <[unresolved objection]: explanation of why it remains open>

Output only the objections and resolutions, nothing else.
"""

# Perspective-slot patterns specific to perspective-discovery scoring.
# Stored here so that if the prompt template renames a lens, this list is
# updated in the same place.
_PERSPECTIVE_SLOT_PATTERNS = ["basic facts", "mechanism", "stakeholder", "failure"]

# Required patterns that must appear in a well-formed LLM response for each process.
# These are case-insensitive substring checks applied to the response text.
_REQUIRED_PATTERNS: dict[str, list[str]] = {
    "perspective-discovery": [
        "Perspective:",
        "Distinct coverage added:",
        "Seed question:",
        "Evidence to seek:",
    ],
    "question-decomposition": [
        "atomic",
        "sub-question",
    ],
    "adversarial-challenge": [
        "Objection",
        "Resolution:",
    ],
}

# Which section of the original item to compare the LLM response against.
_COMPARE_AGAINST: dict[str, str] = {
    "perspective-discovery": "approach",
    "question-decomposition": "approach",
    "adversarial-challenge": "key_findings",
}

PROCESSES: dict[str, dict[str, Any]] = {
    "perspective-discovery": {
        "description": (
            "§0.5b Perspective Discovery — four-slot STORM-grounded template (basic facts / "
            "mechanism / stakeholder / failure-mode) generates seed questions before §1 decomposition."
        ),
        "prompt_template": _PERSPECTIVE_DISCOVERY_TEMPLATE,
        "required_patterns": _REQUIRED_PATTERNS["perspective-discovery"],
        "compare_against": _COMPARE_AGAINST["perspective-discovery"],
        # Slot labels that must be present for a well-formed perspective-discovery response.
        # Kept here so scoring stays consistent with the prompt template.
        "perspective_slot_patterns": _PERSPECTIVE_SLOT_PATTERNS,
    },
    "question-decomposition": {
        "description": (
            "§1 Question Decomposition — recursively break Approach sub-questions into "
            "atomic questions, each answerable with a single evidence-based claim."
        ),
        "prompt_template": _QUESTION_DECOMPOSITION_TEMPLATE,
        "required_patterns": _REQUIRED_PATTERNS["question-decomposition"],
        "compare_against": _COMPARE_AGAINST["question-decomposition"],
    },
    "adversarial-challenge": {
        "description": (
            "§4.5 Adversarial Challenge — challenge draft findings from the perspective of a "
            "sceptic; unresolved objections are labelled [unresolved objection]."
        ),
        "prompt_template": _ADVERSARIAL_CHALLENGE_TEMPLATE,
        "required_patterns": _REQUIRED_PATTERNS["adversarial-challenge"],
        "compare_against": _COMPARE_AGAINST["adversarial-challenge"],
    },
}

# ---------------------------------------------------------------------------
# Text extraction helpers
# ---------------------------------------------------------------------------

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
_SECTION_RE = re.compile(r"^(#{1,3})\s+(.+)", re.MULTILINE)
# Matches any YAML key (word characters, hyphens, underscores followed by
# colon) at the start of a stripped line — used to detect the end of a
# YAML block-list value such as ``tags:`` or ``gaps:``.
_YAML_KEY_RE = re.compile(r"^[a-zA-Z_-][a-zA-Z0-9_-]*\s*:")
# Characters stripped from the edges of tokens during coverage scoring.
# Covers common English punctuation that should not form part of a word token.
_PUNCTUATION_TO_STRIP = ".,;:\"'"


def extract_frontmatter(text: str) -> str | None:
    """Return the raw YAML frontmatter string, or None if absent."""
    m = _FM_RE.match(text)
    return m.group(1) if m else None


def extract_frontmatter_tags(text: str) -> list[str]:
    """Return the ``tags:`` list from the YAML frontmatter."""
    fm = extract_frontmatter(text)
    if fm is None:
        return []
    # Match inline list: tags: [a, b, c]
    m = re.search(r"^tags\s*:\s*\[([^\]]*)\]", fm, re.MULTILINE)
    if m:
        inner = m.group(1)
        return [t.strip() for t in inner.split(",") if t.strip()]
    # Match block list
    tags: list[str] = []
    in_tags = False
    for line in fm.splitlines():
        stripped = line.strip()
        if re.match(r"^tags\s*:", stripped):
            in_tags = True
            continue
        if in_tags:
            if stripped.startswith("- "):
                tags.append(stripped[2:].strip())
            elif stripped.startswith("-"):
                tags.append(stripped[1:].strip())
            elif stripped and _YAML_KEY_RE.match(stripped):
                break
    return tags


def _extract_section(text: str, heading: str) -> str:
    """Return the content of a Markdown section with the given heading text.

    Extracts from after the heading line to just before the next heading at the
    same or higher level (fewer or equal ``#`` characters).  Returns an empty
    string if the section is not found.
    """
    # Find all headings and their positions
    headings = list(_SECTION_RE.finditer(text))
    target_idx: int | None = None
    target_level: int | None = None
    for i, m in enumerate(headings):
        if m.group(2).strip().lower() == heading.lower():
            target_idx = i
            target_level = len(m.group(1))
            break
    if target_idx is None or target_level is None:
        return ""

    # Content starts after the heading line
    start = headings[target_idx].end()
    # Content ends at the next heading of the same or higher level
    end = len(text)
    for m in headings[target_idx + 1 :]:
        if len(m.group(1)) <= target_level:
            end = m.start()
            break
    return text[start:end].strip()


def extract_question(text: str) -> str:
    """Return the ``## Research Question`` section body."""
    return _extract_section(text, "Research Question")


def extract_approach(text: str) -> str:
    """Return the ``## Approach`` section body."""
    return _extract_section(text, "Approach")


def extract_key_findings(text: str) -> str:
    """Return the ``### Key Findings`` section body."""
    return _extract_section(text, "Key Findings")


def extract_title_from_frontmatter(text: str) -> str:
    """Return the ``title:`` value from frontmatter, or empty string."""
    fm = extract_frontmatter(text)
    if fm is None:
        return ""
    m = re.search(r'^title\s*:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    return m.group(1).strip() if m else ""


# ---------------------------------------------------------------------------
# Sampling
# ---------------------------------------------------------------------------


def sample_items(completed_dir: Path, n: int, seed: int | None = None) -> list[Path]:
    """Return a random sample of N completed item paths.

    Parameters
    ----------
    completed_dir:
        Directory containing completed ``.md`` item files.
    n:
        Number of items to sample.  Clamped to the number of available items.
    seed:
        Optional random seed for reproducibility.

    Returns
    -------
    List of Path objects, one per sampled item.  Always sorted before sampling
    so that the same seed yields the same result regardless of filesystem order.
    """
    candidates = sorted(p for p in completed_dir.glob("*.md") if p.name != ".gitkeep")
    if not candidates:
        return []
    k = min(n, len(candidates))
    rng = random.Random(seed)
    return rng.sample(candidates, k)


# ---------------------------------------------------------------------------
# Prompt building
# ---------------------------------------------------------------------------


def build_process_prompt(process_name: str, context: dict[str, str]) -> str:
    """Fill in the process prompt template for the given context.

    Parameters
    ----------
    process_name:
        One of the keys in ``PROCESSES``.
    context:
        Dict with keys ``question``, ``approach``, ``key_findings``, ``tags``.
        Extra keys are ignored.

    Returns
    -------
    The filled prompt string.

    Raises
    ------
    KeyError
        If ``process_name`` is not a known process.
    """
    if process_name not in PROCESSES:
        raise KeyError(
            f"Unknown process '{process_name}'. Available: {', '.join(sorted(PROCESSES))}"
        )
    template = PROCESSES[process_name]["prompt_template"]
    return template.format(
        question=context.get("question", "(no question found)"),
        approach=context.get("approach", "(no approach found)"),
        key_findings=context.get("key_findings", "(no key findings found)"),
        tags=", ".join(context.get("tags_list", [])) or "(none)",
    )


# ---------------------------------------------------------------------------
# Scoring (deterministic — no LLM required)
# ---------------------------------------------------------------------------


def score_structural_completeness(response_text: str, required_patterns: list[str]) -> float:
    """Return the fraction of required patterns present in the response.

    Patterns are matched case-insensitively as substrings.

    Returns a float in ``[0.0, 1.0]``.
    """
    if not required_patterns:
        return 1.0
    lower = response_text.lower()
    found = sum(1 for p in required_patterns if p.lower() in lower)
    return found / len(required_patterns)


def score_coverage_overlap(generated_text: str, reference_text: str) -> float:
    """Return word-level Jaccard similarity between generated and reference text.

    Only words longer than 3 characters are included to reduce noise from
    stop words.  Returns ``0.0`` when both texts are empty or share no words.

    Returns a float in ``[0.0, 1.0]``.
    """

    def word_set(t: str) -> set[str]:
        return {w.lower().strip(_PUNCTUATION_TO_STRIP) for w in t.split() if len(w) > 3}

    gen_words = word_set(generated_text)
    ref_words = word_set(reference_text)
    union = gen_words | ref_words
    if not union:
        return 0.0
    return len(gen_words & ref_words) / len(union)


def score_perspective_slots(response_text: str) -> float:
    """Return the fraction of the four required perspective slots found.

    Checks whether each of the four mandatory STORM-style lens labels (stored
    in ``PROCESSES["perspective-discovery"]["perspective_slot_patterns"]``)
    appears in the response (case-insensitive).  Returns a float in
    ``[0.0, 1.0]``.
    """
    slot_patterns: list[str] = PROCESSES["perspective-discovery"].get(
        "perspective_slot_patterns", []
    )
    if not slot_patterns:
        return 0.0
    lower = response_text.lower()
    found = sum(1 for p in slot_patterns if p in lower)
    return found / len(slot_patterns)


# ---------------------------------------------------------------------------
# Item evaluation
# ---------------------------------------------------------------------------


def evaluate_item(
    item_path: Path,
    process_name: str,
    response_text: str | None = None,
) -> dict[str, Any]:
    """Evaluate a single item against a process step.

    Parameters
    ----------
    item_path:
        Path to the completed item ``.md`` file.
    process_name:
        Name of the process step to evaluate.
    response_text:
        Optional pre-computed LLM response.  When ``None``, only the prompt
        is built and scores are not computed.

    Returns
    -------
    A dict with keys: ``slug``, ``title``, ``tags``, ``question``,
    ``approach``, ``key_findings``, ``prompt``, ``response`` (or ``None``),
    ``scores`` (populated only when ``response_text`` is provided).
    """
    text = item_path.read_text(encoding="utf-8")
    slug = item_path.stem
    title = extract_title_from_frontmatter(text)
    tags = extract_frontmatter_tags(text)
    question = extract_question(text)
    approach = extract_approach(text)
    key_findings = extract_key_findings(text)

    context = {
        "question": question,
        "approach": approach,
        "key_findings": key_findings,
        "tags_list": tags,
    }
    prompt = build_process_prompt(process_name, context)

    result: dict[str, Any] = {
        "slug": slug,
        "title": title,
        "tags": tags,
        "question": question,
        "approach": approach,
        "key_findings": key_findings,
        "prompt": prompt,
        "response": response_text,
        "scores": None,
    }

    if response_text is not None:
        process_cfg = PROCESSES[process_name]
        compare_key = process_cfg["compare_against"]
        reference_text = context.get(compare_key, "")

        structural = score_structural_completeness(response_text, process_cfg["required_patterns"])
        coverage = score_coverage_overlap(response_text, reference_text)
        extra: dict[str, float] = {}
        if process_name == "perspective-discovery":
            extra["perspective_slots"] = score_perspective_slots(response_text)

        result["scores"] = {
            "structural_completeness": round(structural, 3),
            "coverage_overlap": round(coverage, 3),
            **{k: round(v, 3) for k, v in extra.items()},
        }

    return result


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------


def generate_eval_report(
    results: list[dict[str, Any]],
    process_name: str,
    n: int,
    seed: int | None,
) -> dict[str, Any]:
    """Build the full evaluation report dict.

    Parameters
    ----------
    results:
        List of per-item evaluation dicts from :func:`evaluate_item`.
    process_name:
        Name of the process step.
    n:
        Requested sample size.
    seed:
        Random seed used for sampling (or ``None``).

    Returns
    -------
    Report dict with top-level keys: ``meta`` and ``results``.
    The ``meta`` key contains summary statistics when scores are available.
    """
    has_scores = any(r["scores"] is not None for r in results)

    meta: dict[str, Any] = {
        "process": process_name,
        "process_description": PROCESSES[process_name]["description"],
        "n_requested": n,
        "n_sampled": len(results),
        "seed": seed,
        "generated_at": datetime.now(tz=UTC).isoformat(),
        "scored": has_scores,
    }

    if has_scores:
        scored_results = [r for r in results if r["scores"] is not None]
        all_structural = [r["scores"]["structural_completeness"] for r in scored_results]
        all_coverage = [r["scores"]["coverage_overlap"] for r in scored_results]
        meta["summary"] = {
            "mean_structural_completeness": (
                round(sum(all_structural) / len(all_structural), 3) if all_structural else 0.0
            ),
            "mean_coverage_overlap": (
                round(sum(all_coverage) / len(all_coverage), 3) if all_coverage else 0.0
            ),
        }
        if process_name == "perspective-discovery":
            all_slots = [r["scores"].get("perspective_slots", 0.0) for r in scored_results]
            meta["summary"]["mean_perspective_slots"] = (
                round(sum(all_slots) / len(all_slots), 3) if all_slots else 0.0
            )

    return {"meta": meta, "results": results}


def format_markdown_report(report: dict[str, Any]) -> str:
    """Return a human-readable Markdown string summarising the evaluation report."""
    meta = report["meta"]
    lines: list[str] = []

    lines.append(f"# Process Evaluation Report — {meta['process']}")
    lines.append("")
    lines.append(f"**Process:** {meta['process_description']}")
    lines.append(f"**Sampled:** {meta['n_sampled']} of {meta['n_requested']} requested")
    lines.append(f"**Seed:** {meta['seed'] if meta['seed'] is not None else '(random)'}")
    lines.append(f"**Generated:** {meta['generated_at']}")
    lines.append(f"**Scored:** {'yes' if meta['scored'] else 'no (responses not provided)'}")
    lines.append("")

    if "summary" in meta:
        lines.append("## Summary Scores")
        lines.append("")
        s = meta["summary"]
        lines.append("| Metric | Mean |")
        lines.append("| --- | --- |")
        lines.append(
            f"| Structural completeness | {s.get('mean_structural_completeness', 'n/a')} |"
        )
        lines.append(f"| Coverage overlap (Jaccard) | {s.get('mean_coverage_overlap', 'n/a')} |")
        if "mean_perspective_slots" in s:
            lines.append(f"| Perspective slots filled | {s['mean_perspective_slots']} |")
        lines.append("")

    lines.append("## Items")
    lines.append("")

    for i, result in enumerate(report["results"], 1):
        lines.append(f"### {i}. {result['slug']}")
        lines.append("")
        if result["title"]:
            lines.append(f"**Title:** {result['title']}")
            lines.append("")
        lines.append("**Research Question:**")
        lines.append("")
        q = result["question"] or "(not found)"
        lines.append(q[:500] + ("…" if len(q) > 500 else ""))
        lines.append("")
        lines.append("**Process Prompt:**")
        lines.append("")
        lines.append("```")
        lines.append(result["prompt"][:1500] + ("…" if len(result["prompt"]) > 1500 else ""))
        lines.append("```")
        lines.append("")
        if result["scores"] is not None:
            lines.append("**Scores:**")
            lines.append("")
            for k, v in result["scores"].items():
                lines.append(f"- `{k}`: {v}")
            lines.append("")
        if result["response"]:
            lines.append("**LLM Response (first 800 chars):**")
            lines.append("")
            lines.append("```")
            lines.append(result["response"][:800] + ("…" if len(result["response"]) > 800 else ""))
            lines.append("```")
            lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def main() -> None:  # noqa: C901
    parser = argparse.ArgumentParser(
        description=(
            "Process evaluation harness — sample past research items and run "
            "them through a specified process step."
        )
    )
    parser.add_argument(
        "--process",
        choices=list(PROCESSES),
        default="perspective-discovery",
        help="Process step to evaluate (default: perspective-discovery)",
    )
    parser.add_argument(
        "--n",
        type=int,
        default=5,
        help="Number of items to sample (default: 5)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random seed for reproducibility (default: random)",
    )
    parser.add_argument(
        "--completed-dir",
        type=Path,
        default=Path(__file__).parent.parent / "Research" / "completed",
        help="Path to Research/completed/ directory",
    )
    parser.add_argument(
        "--dump-prompts-dir",
        type=Path,
        default=None,
        help=(
            "Write each item's process prompt as <slug>.txt to this directory. "
            "Used by eval-loop.yml to feed individual prompts to Copilot one at a time."
        ),
    )
    parser.add_argument(
        "--responses-dir",
        type=Path,
        default=None,
        help=(
            "Directory containing pre-computed LLM responses as <slug>.txt files. "
            "When provided, responses are scored against the original item content."
        ),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).parent.parent / "state" / "eval_reports",
        help="Directory to write the JSON + Markdown report (default: state/eval_reports/)",
    )
    parser.add_argument(
        "--list-processes",
        action="store_true",
        help="List available process steps and exit",
    )
    args = parser.parse_args()

    if args.list_processes:
        print("Available process steps:")
        for name, cfg in sorted(PROCESSES.items()):
            print(f"  {name}")
            print(f"    {cfg['description']}")
        return

    completed_dir: Path = args.completed_dir.resolve()
    if not completed_dir.exists():
        logger.error("Completed directory not found: %s", completed_dir)
        sys.exit(1)

    logger.info(
        "Sampling %d item(s) from %s (seed=%s, process=%s)",
        args.n,
        completed_dir,
        args.seed,
        args.process,
    )

    sampled = sample_items(completed_dir, args.n, args.seed)
    if not sampled:
        logger.warning("No completed items found in %s", completed_dir)
        sys.exit(0)

    logger.info("Sampled %d item(s): %s", len(sampled), [p.stem for p in sampled])

    results: list[dict[str, Any]] = []
    for item_path in sampled:
        response_text: str | None = None
        if args.responses_dir is not None:
            response_file = args.responses_dir / f"{item_path.stem}.txt"
            if response_file.exists():
                response_text = response_file.read_text(encoding="utf-8")
                logger.info("Loaded response for %s", item_path.stem)
            else:
                logger.info(
                    "No response file found for %s at %s — skipping scoring",
                    item_path.stem,
                    response_file,
                )
        result = evaluate_item(item_path, args.process, response_text)
        results.append(result)

    # Dump individual prompt files if requested (used by eval-loop.yml).
    if args.dump_prompts_dir is not None:
        dump_dir: Path = args.dump_prompts_dir.resolve()
        dump_dir.mkdir(parents=True, exist_ok=True)
        for result in results:
            prompt_file = dump_dir / f"{result['slug']}.txt"
            prompt_file.write_text(result["prompt"], encoding="utf-8")
            logger.info("Wrote prompt: %s", prompt_file)
        logger.info("Dumped %d prompt(s) to %s", len(results), dump_dir)

    report = generate_eval_report(results, args.process, args.n, args.seed)

    output_dir: Path = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(tz=UTC).strftime("%Y-%m-%d")
    seed_tag = f"seed{args.seed}" if args.seed is not None else "seedrnd"
    stem = f"{timestamp}-{args.process}-n{len(sampled)}-{seed_tag}"

    json_path = output_dir / f"{stem}.json"
    md_path = output_dir / f"{stem}.md"

    json_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8",
    )
    md_path.write_text(format_markdown_report(report), encoding="utf-8")

    scored_count = sum(1 for r in results if r["scores"] is not None)
    logger.info(
        "Report written: %s (%d item(s) evaluated, %d scored)",
        json_path,
        len(results),
        scored_count,
    )
    logger.info("Markdown: %s", md_path)


if __name__ == "__main__":
    main()
