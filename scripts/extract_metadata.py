#!/usr/bin/env python3
"""Extract metadata from Research/completed/*.md files into state/content_metadata.json.

Produces:
  state/content_metadata.json  — named_concepts, source_urls, key_claims per item

Usage:
  python scripts/extract_metadata.py

Requires: PyYAML
"""

from __future__ import annotations

import datetime as _dt
import json
import re
from collections import Counter
from datetime import UTC
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.parent
COMPLETED_DIR = REPO_ROOT / "Research" / "completed"
STATE_DIR = REPO_ROOT / "state"

# ---------------------------------------------------------------------------
# Stopwords
# ---------------------------------------------------------------------------

STOPWORDS: frozenset[str] = frozenset(
    [
        # Function words
        "a",
        "an",
        "the",
        "and",
        "or",
        "but",
        "in",
        "on",
        "at",
        "to",
        "for",
        "of",
        "with",
        "by",
        "from",
        "as",
        "is",
        "are",
        "was",
        "were",
        "be",
        "been",
        "being",
        "have",
        "has",
        "had",
        "do",
        "does",
        "did",
        "will",
        "would",
        "could",
        "should",
        "may",
        "might",
        "must",
        "can",
        "it",
        "its",
        "this",
        "that",
        "these",
        "those",
        "which",
        "who",
        "whom",
        "what",
        "when",
        "where",
        "why",
        "how",
        "not",
        "no",
        "nor",
        "so",
        "yet",
        "both",
        "either",
        "neither",
        "each",
        "few",
        "more",
        "most",
        "other",
        "some",
        "such",
        "than",
        "then",
        "too",
        "very",
        "just",
        "into",
        "through",
        "during",
        "before",
        "after",
        "above",
        "below",
        "between",
        "out",
        "off",
        "over",
        "under",
        "again",
        "further",
        "once",
        "any",
        "all",
        "also",
        "only",
        "own",
        "same",
        "while",
        "about",
        "across",
        "within",
        "without",
        "up",
        "down",
        "if",
        "else",
        "their",
        "they",
        "them",
        "we",
        "our",
        "you",
        "your",
        "my",
        "me",
        "he",
        "she",
        "his",
        "her",
        "our",
        "us",
        "i",
        "ii",
        "iii",
        "iv",
        # Research-specific stop words
        "research",
        "inference",
        "fact",
        "assumption",
        "high",
        "medium",
        "low",
        "source",
        "evidence",
        "item",
        "items",
        "note",
        "notes",
        "section",
        "key",
        "finding",
        "findings",
        "result",
        "results",
        "approach",
        "method",
        "methods",
        "data",
        "use",
        "used",
        "using",
        "based",
        "new",
        "given",
        "shows",
        "show",
        "used",
        "well",
        "also",
        "approach",
        "provide",
        "provides",
        "provided",
        "include",
        "includes",
        "including",
        "support",
        "supports",
        "allow",
        "allows",
        "enable",
        "enables",
        "ensure",
        "ensures",
        "require",
        "requires",
        "provide",
        "make",
        "makes",
        "made",
        "take",
        "takes",
        "taken",
        "get",
        "gets",
        "set",
        "sets",
        "see",
        "seen",
        "need",
        "needs",
        "work",
        "works",
        "working",
        "like",
        "likely",
        "across",
        "between",
        "within",
        "however",
        "therefore",
        "thus",
        "hence",
        "although",
        "though",
        "since",
        "because",
        "while",
        "whereas",
        "rather",
        "often",
        "typically",
        "generally",
        "specifically",
        "particularly",
        "effectively",
        "efficiently",
        "significantly",
        "substantially",
        "potentially",
        "approximately",
        "relatively",
        "currently",
        "multiple",
        "various",
        "different",
        "similar",
        "specific",
        "particular",
        "overall",
        "primary",
        "secondary",
        "main",
        "major",
        "minor",
        "large",
        "small",
        "long",
        "short",
    ]
)

# ---------------------------------------------------------------------------
# Parsing helpers (duplicated from build_site.py to keep this script standalone)
# ---------------------------------------------------------------------------

# Regex to strip bold confidence-level prefixes from key-finding lines,
# e.g. "**High confidence.**", "**Medium confidence:**", "**Low confidence.**"
_CONFIDENCE_LABEL_RE = re.compile(
    r"\*\*(high|medium|low)\s+confidence[.:]\*\*\s*",
    re.IGNORECASE,
)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Split YAML front matter and body. Returns (meta, body)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    yaml_src = text[3:end].strip()
    body = text[end + 4 :].lstrip("\n")
    try:
        meta = yaml.safe_load(yaml_src) or {}
    except yaml.YAMLError:
        meta = {}
    return meta, body


def normalise_tags(raw: object) -> list[str]:
    """Normalise tags field to a list of lowercase strings."""
    if isinstance(raw, list):
        return [str(t).strip().lower() for t in raw if t]
    if isinstance(raw, str):
        return [t.strip().lower() for t in re.split(r"[,\s]+", raw) if t.strip()]
    return []


def slugify(name: str) -> str:
    """Convert a filename stem to a URL slug."""
    s = name.lower()
    s = re.sub(r"[\s\.]+", "-", s)
    s = re.sub(r"[^a-z0-9\-]", "", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def extract_section(body: str, section_name: str) -> str:
    """Extract content of a named ## section from markdown body."""
    lines = body.split("\n")
    in_section = False
    result: list[str] = []
    for line in lines:
        if re.match(r"^##\s+" + re.escape(section_name) + r"\s*$", line):
            in_section = True
            continue
        if in_section:
            if re.match(r"^##\s+", line):
                break
            result.append(line)
    return "\n".join(result).strip()


# ---------------------------------------------------------------------------
# Metadata extraction
# ---------------------------------------------------------------------------


def extract_named_concepts(text: str) -> list[str]:
    """Extract top-20 2-4 word noun phrases from text by frequency.

    Simple n-gram approach: tokenise into lowercase words, generate 2-4 word
    n-grams where no word is a stopword, count, return top 20 deduplicated.
    """
    # Clean text: remove markdown, URLs, punctuation except hyphens
    cleaned = re.sub(r"https?://\S+", "", text)
    cleaned = re.sub(r"```.*?```", "", cleaned, flags=re.DOTALL)
    cleaned = re.sub(r"`[^`]+`", "", cleaned)
    cleaned = re.sub(r"\*{1,3}([^*]+)\*{1,3}", r"\1", cleaned)
    cleaned = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", cleaned)
    cleaned = re.sub(r"[^a-zA-Z0-9\s\-]", " ", cleaned)

    words = [w.lower().strip("-") for w in cleaned.split() if w.strip("-")]
    words = [w for w in words if w and re.match(r"^[a-z][a-z0-9\-]*$", w)]

    ngram_counter: Counter[str] = Counter()
    for n in (2, 3, 4):
        for i in range(len(words) - n + 1):
            gram = words[i : i + n]
            if any(w in STOPWORDS for w in gram):
                continue
            if any(len(w) < 2 for w in gram):
                continue
            phrase = " ".join(gram)
            ngram_counter[phrase] += 1

    # Get top candidates
    top = [phrase for phrase, _ in ngram_counter.most_common(60)]

    # Deduplicate: remove phrases whose words are a subset of a higher-ranked phrase
    result: list[str] = []
    for phrase in top:
        phrase_words = set(phrase.split())
        dominated = False
        for kept in result:
            kept_words = set(kept.split())
            if phrase_words.issubset(kept_words) or kept_words.issubset(phrase_words):
                # Keep the longer phrase (higher ranked one is already kept)
                dominated = True
                break
        if not dominated:
            result.append(phrase)
        if len(result) >= 20:
            break

    return result


def extract_source_urls(sources_text: str, exclude_repo: str) -> list[str]:
    """Extract unique https URLs from Sources section markdown, excluding repo URL.

    Recognises:
      - Markdown links: [Name](https://...)
      - Label colon:    Label: https://...
      - Label em-dash:  Label — https://...
    """
    seen: set[str] = set()
    result: list[str] = []

    def _add(url: str) -> None:
        url = url.rstrip(".,;:!?)")
        if exclude_repo in url:
            return
        if url not in seen:
            seen.add(url)
            result.append(url)

    # Markdown link pattern: [Name](https://...)
    for m in re.finditer(r"\[([^\]]*)\]\((https://[^)]+)\)", sources_text):
        _add(m.group(2))

    # Label: https://... pattern (bullet or plain line)
    for m in re.finditer(r"(?:^|(?<=\n))[*\-]?\s*[^:\n]+?:\s+(https://\S+)", sources_text):
        _add(m.group(1))

    # Label — https://... pattern
    for m in re.finditer(r"(?:^|(?<=\n))[*\-]?\s*[^\n]+?\s+—\s+(https://\S+)", sources_text):
        _add(m.group(1))

    return result


def _extract_sources_from_line(line: str) -> list[str]:
    """Extract all https:// source URLs from [...] brackets or (...) parentheticals containing a 'source:' key.

    Handles both the prefix bracket format ``[inference; source: URL]`` and the
    suffix parenthetical format ``([inference]; medium confidence; source: URL)``.
    """
    sources: list[str] = []

    def _collect_urls(content: str) -> None:
        if not re.search(r"\bsource\s*:", content, re.IGNORECASE):
            return
        for url_match in re.finditer(r"https?://\S+", content):
            url = url_match.group(0).rstrip(".,;)")
            if url and url not in sources:
                sources.append(url)

    # Search in [...] brackets (prefix format: [inference; source: URL])
    for m in re.finditer(r"\[([^\]]+)\]", line):
        _collect_urls(m.group(1))

    # Search in (...) parentheticals (suffix format: ([inference]; confidence; source: URL))
    for m in re.finditer(r"\(([^)]+)\)", line):
        _collect_urls(m.group(1))

    return sources


def _extract_key_claims_fallback(findings_text: str) -> list[dict]:
    """Fallback: first sentence from * [inference] / * [fact] bullets in Executive Summary."""
    es_match = re.search(r"###\s+Executive Summary\b(.*?)(?=\n###|\Z)", findings_text, re.DOTALL)
    if not es_match:
        return []
    es_text = es_match.group(1)
    claims: list[dict] = []
    for line in es_text.split("\n"):
        if not re.match(r"^\s*\*\s+\[(inference|fact)\]", line, re.IGNORECASE):
            continue
        sources = _extract_sources_from_line(line)
        text = re.sub(r"^\s*\*\s+", "", line)
        text = re.sub(r"\[(inference|fact)[^\]]*\]\s*", "", text, flags=re.IGNORECASE)
        text = text.strip()
        parts = re.split(r"\.\s+", text)
        if parts:
            text = parts[0].strip().rstrip(".")
        if text:
            claims.append({"text": text, "sources": sources})
        if len(claims) >= 8:
            break
    return claims


def extract_key_claims(findings_text: str) -> list[dict]:
    """Extract key claims with source URLs from the ### Key Findings subsection.

    Handles four bullet formats produced by the research loop:
      1. ``1. **Claim text.** (confidence level)``  — older style
      2. ``1. **High confidence.** [source; URL] Claim text``  — mid-era style
      3. ``1. [source; URL] **Medium confidence:** Claim text``  — current style
      4. ``1. **Claim text.** ([inference]; medium confidence; source: URL)``  — suffix style

    Returns a list of dicts: ``{"text": str, "sources": [url, ...]}``.
    """
    # Find ### Key Findings subsection
    kf_match = re.search(r"###\s+Key Findings\b(.*?)(?=\n###|\Z)", findings_text, re.DOTALL)
    if not kf_match:
        return _extract_key_claims_fallback(findings_text)

    kf_text = kf_match.group(1)
    claims: list[dict] = []

    for line in kf_text.split("\n"):
        # Match any numbered or bulleted list item
        if not re.match(r"^\s*(\d+\.\s+|-\s+)", line):
            continue
        # Capture source URLs before stripping brackets/parens
        sources = _extract_sources_from_line(line)
        # Strip list marker
        text = re.sub(r"^\s*\d+\.\s+", "", line)
        text = re.sub(r"^\s*-\s+", "", text)
        # Strip all [...] source/evidence brackets (handles multi-URL brackets).
        # Brackets in Key Findings lines are never nested, so [^\]]* is sufficient.
        text = re.sub(r"\[[^\]]*\]", "", text)
        # Strip bold confidence-level prefixes, e.g. "**High confidence.**"
        text = _CONFIDENCE_LABEL_RE.sub("", text)
        # Strip any remaining bold markers
        text = re.sub(r"\*\*", "", text)
        # Strip trailing parenthetical confidence+source annotations.
        # Handles both the simple "(high confidence)" form and the suffix form
        # "(; medium confidence; source: URL1; URL2)" that remains after bracket removal
        # strips the embedded [inference] token.
        text = re.sub(
            r"\s*\([;,\s]*(?:high|medium|low)\s+confidence[^)]*\)\s*$",
            "",
            text,
            flags=re.IGNORECASE,
        )
        text = text.strip().rstrip(".")
        if text:
            claims.append({"text": text, "sources": sources})
        if len(claims) >= 8:
            break

    if not claims:
        return _extract_key_claims_fallback(findings_text)
    return claims


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

EXCLUDE_REPO_URL = "https://github.com/davidamitchell/Research"


def main() -> None:
    STATE_DIR.mkdir(exist_ok=True)

    total_concepts = 0
    total_urls = 0
    items_out: dict[str, dict] = {}

    for path in sorted(COMPLETED_DIR.glob("*.md"), reverse=True):
        name = path.name
        if name.lower() == "readme.md":
            continue
        if re.search(r"meta|infra", name, re.IGNORECASE):
            continue

        text = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)

        slug = slugify(path.stem)

        # Extract sections
        findings_text = extract_section(body, "Findings")
        tech_arch_text = extract_section(body, "Technical Architecture")
        sources_text = extract_section(body, "Sources")

        # Combine for concept extraction
        concept_text = "\n\n".join(filter(None, [findings_text, tech_arch_text]))
        named_concepts = extract_named_concepts(concept_text)

        source_urls = extract_source_urls(sources_text, EXCLUDE_REPO_URL)

        key_claims = extract_key_claims(findings_text)

        items_out[slug] = {
            "named_concepts": named_concepts,
            "source_urls": source_urls,
            "key_claims": key_claims,
        }

        total_concepts += len(named_concepts)
        total_urls += len(source_urls)

    output = {
        "extracted_at": _dt.datetime.now(tz=UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "items": items_out,
    }

    out_path = STATE_DIR / "content_metadata.json"
    out_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")

    print(
        f"{len(items_out)} items processed, {total_concepts} concepts extracted, {total_urls} source URLs found"
    )


if __name__ == "__main__":
    main()
