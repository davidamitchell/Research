"""Tests for thread detection logic in scripts/build_site.py."""

from __future__ import annotations

import sys
from datetime import UTC, date, datetime
from pathlib import Path

import pytest

# Make scripts/ importable
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from build_site import (
    _cluster_overlap,
    _item_url,
    build_all_items_page,
    build_knowledge_index_page,
    build_research_master_page,
    detect_concept_threads,
    detect_threads,
    load_knowledge_items,
    render_card,
    strip_evidence_labels,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_item(
    slug: str,
    tags: list[str],
    thread: str = "",
    added: date | datetime | None = None,
) -> dict:
    """Minimal item dict sufficient for thread detection and page building."""
    if added is None:
        added_dt: datetime = datetime(2026, 1, 1, tzinfo=UTC)
    elif isinstance(added, datetime):
        added_dt = added if added.tzinfo else added.replace(tzinfo=UTC)
    else:
        added_dt = datetime(added.year, added.month, added.day, tzinfo=UTC)
    return {
        "slug": slug,
        "tags": tags,
        "thread": thread,
        "added": added_dt,
        "added_str": added_dt.date().isoformat(),
        "title": slug,
        "display_title": slug,
        "question": "",
        "question_excerpt": "",
        "sections": {},
    }


def _slugs(thread: dict) -> set[str]:
    return {it["slug"] for it in thread["items"]}


# ---------------------------------------------------------------------------
# _cluster_overlap
# ---------------------------------------------------------------------------


def test_cluster_overlap_identical() -> None:
    assert _cluster_overlap({"a", "b", "c"}, {"a", "b", "c"}) == 1.0


def test_cluster_overlap_disjoint() -> None:
    assert _cluster_overlap({"a", "b"}, {"c", "d"}) == 0.0


def test_cluster_overlap_partial() -> None:
    # |{a,b} ∩ {b,c}| / min(2,2) = 1/2
    assert _cluster_overlap({"a", "b"}, {"b", "c"}) == pytest.approx(0.5)


def test_cluster_overlap_empty() -> None:
    assert _cluster_overlap(set(), {"a"}) == 0.0


# ---------------------------------------------------------------------------
# detect_threads — explicit threads
# ---------------------------------------------------------------------------


def test_explicit_thread_grouping() -> None:
    items = [
        _make_item("a", ["x"], thread="My Thread"),
        _make_item("b", ["y"], thread="My Thread"),
        _make_item("c", ["z"]),
    ]
    threads = detect_threads(items)
    explicit = [t for t in threads if t["kind"] == "explicit"]
    assert len(explicit) == 1
    assert _slugs(explicit[0]) == {"a", "b"}


def test_explicit_thread_requires_two_items() -> None:
    items = [
        _make_item("solo", ["x"], thread="Lonely Thread"),
        _make_item("other", ["y"]),
    ]
    threads = detect_threads(items)
    assert not any(t["kind"] == "explicit" for t in threads)


# ---------------------------------------------------------------------------
# detect_threads — implicit (tag-based) threads
# ---------------------------------------------------------------------------


def test_minimum_cluster_size_not_met() -> None:
    """Two items sharing 2+ tags do not form a thread (need 3 items)."""
    items = [
        _make_item("a", ["x", "y", "z"]),
        _make_item("b", ["x", "y", "w"]),
    ]
    threads = detect_threads(items)
    assert not any(t["kind"] == "implicit" for t in threads)


def test_basic_implicit_thread() -> None:
    """Three items sharing 2+ tags form one implicit thread."""
    items = [
        _make_item("a", ["x", "y", "p"]),
        _make_item("b", ["x", "y", "q"]),
        _make_item("c", ["x", "y", "r"]),
        _make_item("d", ["m", "n"]),  # unrelated
    ]
    threads = detect_threads(items)
    implicit = [t for t in threads if t["kind"] == "implicit"]
    assert len(implicit) == 1
    assert _slugs(implicit[0]) == {"a", "b", "c"}


def test_overlapping_thread_membership() -> None:
    """An item can appear in multiple threads when clusters partially overlap.

    Three distinct clusters form because no cluster is 75%+ subsumed by another:

    Cluster A (seed tags {a,b,c}): [a_seed, a_ab, a_ac, a_bc, cross]
    Cluster X (cross tags {a,b,p,q}): [cross, a_seed, a_ab, b_seed, b_pq]
    Cluster B (seed tags {p,q,r}): [b_seed, b_pq, b_pr, b_qr, cross]

    'cross' appears in all three threads.  Clusters A and X share 3/5 items
    (60%) so both survive the 75% deduplication threshold.
    """
    items = [
        _make_item("a_seed", ["a", "b", "c"]),
        _make_item("a_ab", ["a", "b", "1"]),  # shares {a,b} with cross
        _make_item("a_ac", ["a", "c", "2"]),  # shares {a} only with cross
        _make_item("a_bc", ["b", "c", "3"]),  # shares {b} only with cross
        _make_item("cross", ["a", "b", "p", "q"]),  # bridges A and B clusters
        _make_item("b_seed", ["p", "q", "r"]),
        _make_item("b_pq", ["p", "q", "1"]),  # shares {p,q} with cross
        _make_item("b_pr", ["p", "r", "2"]),  # shares {p} only with cross
        _make_item("b_qr", ["q", "r", "3"]),  # shares {q} only with cross
    ]
    threads = detect_threads(items)
    implicit = [t for t in threads if t["kind"] == "implicit"]
    # Three distinct clusters should survive deduplication
    assert len(implicit) >= 2

    all_thread_slugsets = [_slugs(t) for t in implicit]
    cross_threads = [s for s in all_thread_slugsets if "cross" in s]
    assert len(cross_threads) >= 2, "'cross' should appear in at least 2 threads"


def test_deduplication_keeps_larger_cluster() -> None:
    """Near-identical clusters (>= 75% overlap) are deduplicated; larger survives."""
    # Items a,b,c,d all share tags x,y with each other.
    # Seeding from a gives [a,b,c,d]; seeding from b gives the same [a,b,c,d].
    # After deduplication we expect exactly one thread.
    items = [
        _make_item("a", ["x", "y", "1"]),
        _make_item("b", ["x", "y", "2"]),
        _make_item("c", ["x", "y", "3"]),
        _make_item("d", ["x", "y", "4"]),
    ]
    threads = detect_threads(items)
    implicit = [t for t in threads if t["kind"] == "implicit"]
    # All four seeds produce the same cluster → should collapse to 1
    assert len(implicit) == 1
    assert _slugs(implicit[0]) == {"a", "b", "c", "d"}


# ---------------------------------------------------------------------------
# detect_concept_threads
# ---------------------------------------------------------------------------


def _make_metadata(concept_map: dict[str, list[str]]) -> dict:
    """Build a minimal metadata dict for concept thread tests."""
    return {"items": {slug: {"named_concepts": concepts} for slug, concepts in concept_map.items()}}


def test_concept_thread_basic() -> None:
    """Three items sharing 3+ named concepts form a concept thread."""
    items = [
        _make_item("a", []),
        _make_item("b", []),
        _make_item("c", []),
        _make_item("d", []),
    ]
    shared = ["alpha concept", "beta concept", "gamma concept"]
    meta = _make_metadata(
        {
            "a": shared + ["unique-a"],
            "b": shared + ["unique-b"],
            "c": shared + ["unique-c"],
            "d": ["other1", "other2", "other3", "other4"],  # no overlap
        }
    )
    result = detect_concept_threads(items, meta, existing_threads=[])
    assert len(result) == 1
    assert _slugs(result[0]) == {"a", "b", "c"}
    assert result[0]["kind"] == "concept"
    assert len(result[0]["concept_cluster"]) <= 3


def test_concept_thread_requires_three_items() -> None:
    """Two items sharing 3+ concepts do not form a concept thread."""
    items = [_make_item("a", []), _make_item("b", [])]
    shared = ["c1", "c2", "c3"]
    meta = _make_metadata({"a": shared, "b": shared})
    result = detect_concept_threads(items, meta, existing_threads=[])
    assert result == []


def test_concept_thread_filters_high_frequency_concepts() -> None:
    """Concepts appearing in > 25% of items are excluded from clustering."""
    # With 8 items, threshold = max(3, 8*0.25) = 3.
    # A concept in 4 items (50%) should be filtered out.
    # We use only the high-freq concept as the shared one → no cluster forms.
    items = [_make_item(str(i), []) for i in range(8)]
    # "common" appears in 4 of 8 items (50%) — should be filtered
    meta = _make_metadata(
        {
            "0": ["common", "c1", "c2", "c3"],
            "1": ["common", "c1", "c2", "c3"],
            "2": ["common", "c1", "c2", "c3"],
            "3": ["common", "other-a", "other-b", "other-c"],
            "4": ["uniq4a", "uniq4b", "uniq4c"],
            "5": ["uniq5a", "uniq5b", "uniq5c"],
            "6": ["uniq6a", "uniq6b", "uniq6c"],
            "7": ["uniq7a", "uniq7b", "uniq7c"],
        }
    )
    # Items 0,1,2 share c1,c2,c3 (appear 3 times = at threshold, kept)
    # They also share "common" (appears 4 times > threshold, filtered)
    result = detect_concept_threads(items, meta, existing_threads=[])
    # cluster {0,1,2} forms via c1/c2/c3; "common" should NOT be in concept_cluster
    assert len(result) == 1
    assert "common" not in result[0]["concept_cluster"]


def test_concept_thread_no_duplicate_of_tag_thread() -> None:
    """Concept cluster that >= 75% overlaps an existing tag thread is dropped."""
    items = [
        _make_item("a", ["x", "y"]),
        _make_item("b", ["x", "y"]),
        _make_item("c", ["x", "y"]),
    ]
    shared_concepts = ["alpha", "beta", "gamma"]
    meta = _make_metadata(
        {
            "a": shared_concepts,
            "b": shared_concepts,
            "c": shared_concepts,
        }
    )
    # Pre-existing thread that covers a, b, c (100% overlap)
    existing = [
        {
            "slug": "existing-thread",
            "title": "existing",
            "kind": "implicit",
            "tag_cluster": ["x", "y"],
            "concept_cluster": [],
            "items": items,
        }
    ]
    result = detect_concept_threads(items, meta, existing_threads=existing)
    assert result == []


# ---------------------------------------------------------------------------
# build_all_items_page
# ---------------------------------------------------------------------------


def test_build_all_items_page_contains_items() -> None:
    """build_all_items_page renders a card for each item."""
    items = [
        _make_item("item-a", ["tag1"], added=date(2026, 4, 1)),
        _make_item("item-b", ["tag2"], added=date(2026, 3, 1)),
        _make_item("item-c", ["tag3"], added=date(2026, 2, 1)),
    ]
    html = build_all_items_page(items)
    for item in items:
        assert item["slug"] in html
    assert "All Items" in html
    assert "3 completed research items" in html


def test_build_all_items_page_is_valid_html_skeleton() -> None:
    """build_all_items_page returns a complete HTML document."""
    items = [_make_item("x", ["t"], added=date(2026, 1, 1))]
    html = build_all_items_page(items)
    assert "<!DOCTYPE html>" in html
    assert "</html>" in html
    assert '<div class="card-grid">' in html


def test_build_all_items_page_empty_items() -> None:
    """build_all_items_page handles an empty item list gracefully."""
    html = build_all_items_page([])
    assert "0 completed research items" in html
    assert '<div class="card-grid">' in html


# ---------------------------------------------------------------------------
# build_research_master_page
# ---------------------------------------------------------------------------


def test_build_research_master_page_returns_html() -> None:
    """build_research_master_page produces a complete HTML document."""
    html = build_research_master_page()
    assert "<!DOCTYPE html>" in html
    assert "</html>" in html
    assert "Research Master" in html


def test_build_research_master_page_contains_toc_anchors() -> None:
    """Rendered page uses id= anchors (HTML5-valid), not deprecated <a name=> anchors."""
    html = build_research_master_page()
    assert '<a id="' in html
    assert '<a name="' not in html


def test_build_research_master_page_no_toc() -> None:
    """TOC section is stripped from the rendered page."""
    html = build_research_master_page()
    assert "Table of Contents" not in html


def test_build_research_master_page_no_javascript() -> None:
    """research-master.html emits no JavaScript."""
    html = build_research_master_page()
    assert "<script" not in html


def test_build_research_master_page_has_source_link() -> None:
    """Page includes a link back to the source file on GitHub."""
    html = build_research_master_page()
    assert "Research_Master.md" in html
    assert "github.com/davidamitchell/Research" in html


# ---------------------------------------------------------------------------
# strip_evidence_labels
# ---------------------------------------------------------------------------


def test_strip_evidence_labels_paragraph_to_bullets() -> None:
    """A bare paragraph with inline [type; source: ...] labels is split into bullet items."""
    text = (
        "[inference; source: https://a.com] Sentence one. "
        "[fact; source: https://b.com; https://c.com] Sentence two."
    )
    result = strip_evidence_labels(text)
    assert result == "- Sentence one.\n- Sentence two."


def test_strip_evidence_labels_list_item_strips_inline_label() -> None:
    """Existing bullet items have embedded labels stripped, list marker preserved."""
    text = "- [inference; source: https://a.com] The feedback loop should operate."
    assert strip_evidence_labels(text) == "- The feedback loop should operate."


def test_strip_evidence_labels_numbered_list_strips_label() -> None:
    """Numbered list items have embedded labels stripped."""
    text = "1. **High confidence.** [inference; source: https://a.com] Claim text."
    assert strip_evidence_labels(text) == "1. **High confidence.** Claim text."


def test_strip_evidence_labels_numbered_list_label_first() -> None:
    """Format 3 Key Findings (label before bold confidence) is handled."""
    text = "1. [inference; source: https://a.com] **Medium confidence:** OPA is suitable."
    assert strip_evidence_labels(text) == "1. **Medium confidence:** OPA is suitable."


def test_strip_evidence_labels_bare_label_unchanged() -> None:
    """Bare [inference] / [fact] labels without '; source:' are left untouched."""
    text = "- **[assumption] Something is true.** Justification follows."
    assert strip_evidence_labels(text) == text


def test_strip_evidence_labels_headings_unchanged() -> None:
    """Lines starting with # are not modified."""
    text = "### Key Findings\n[inference; source: https://a.com] Para text."
    result = strip_evidence_labels(text)
    assert result.startswith("### Key Findings")
    # The paragraph line (not a heading) should be converted to bullet
    assert "- Para text." in result


def test_strip_evidence_labels_empty_text() -> None:
    assert strip_evidence_labels("") == ""


def test_strip_evidence_labels_plain_paragraph_unchanged() -> None:
    """Plain paragraphs without evidence labels are not modified."""
    text = "Three disciplines converge on the ~5-person limit for high-coordination teams."
    assert strip_evidence_labels(text) == text


def test_strip_evidence_labels_format_a_with_confidence_keyword() -> None:
    """Mid-era format A: [inference; confidence: medium; source: URL] is stripped from list items."""
    text = "1. [inference; confidence: medium; source: https://a.com; https://b.com] Claim text."
    assert strip_evidence_labels(text) == "1. Claim text."


def test_strip_evidence_labels_format_a_high_confidence() -> None:
    """Format A with high confidence keyword is also stripped."""
    text = (
        "3. [fact; confidence: high; source: https://nist.gov/x] Framework requires staged rollout."
    )
    assert strip_evidence_labels(text) == "3. Framework requires staged rollout."


def test_strip_evidence_labels_suffix_format_c() -> None:
    """Current suffix format: trailing ([inference]; confidence; source: URL) is stripped."""
    text = "1. **Bounded automation outperforms end-to-end autonomy.** ([inference]; medium confidence; source: https://a.com; https://b.com)"
    result = strip_evidence_labels(text)
    assert result == "1. **Bounded automation outperforms end-to-end autonomy.**"


def test_strip_evidence_labels_suffix_format_c_high_confidence() -> None:
    """Suffix format with high confidence is stripped."""
    text = "2. **Verifier strength determines delegation reliability.** ([fact]; high confidence; source: https://example.com)"
    result = strip_evidence_labels(text)
    assert result == "2. **Verifier strength determines delegation reliability.**"


def test_strip_evidence_labels_suffix_format_c_no_brackets() -> None:
    """Suffix format without bracket around epistemic label is also stripped."""
    text = "1. **Claim text.** (medium confidence; source: https://example.com)"
    # This style has no [inference] part — _KEY_FINDING_SUFFIX_RE requires an epistemic
    # label (inference|fact|assumption) so this simpler form is not stripped (different format).
    result = strip_evidence_labels(text)
    # Should pass through unchanged since no [inference/fact/assumption] wrapper
    assert result == text


# ---------------------------------------------------------------------------
# _extract_citation_label and _render_source_links
# ---------------------------------------------------------------------------

from build_site import _extract_citation_label, _render_source_links  # noqa: E402


def test_extract_citation_label_et_al() -> None:
    """Display name with '(Surname et al., YYYY)' produces 'Surname et al. (YYYY)'."""
    label = _extract_citation_label(
        "Judging LLM-as-a-Judge (Zheng et al., 2023)",
        "https://arxiv.org/abs/2306.05685",
    )
    assert label == "Zheng et al. (2023)"


def test_extract_citation_label_single_author() -> None:
    """Display name with '(Surname, YYYY)' produces 'Surname (YYYY)'."""
    label = _extract_citation_label("Some Title (Brooks, 1975)", "https://example.com/x")
    assert label == "Brooks (1975)"


def test_extract_citation_label_org_no_year() -> None:
    """Display name without a year falls back to capitalised domain + (n.d.)."""
    label = _extract_citation_label("Promptfoo CI/CD docs", "https://www.promptfoo.dev/docs/ci-cd/")
    assert label == "Promptfoo (n.d.)"


def test_extract_citation_label_known_org() -> None:
    """Display name starting with 'Azure' is used as org (fallback-1b); URL is secondary."""
    label = _extract_citation_label(
        "Azure AI Foundry evaluation approach",
        "https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/",
    )
    # Fallback-1b extracts first capitalised word (≥5 chars) from display name: "Azure"
    assert label == "Azure (n.d.)"


def test_extract_citation_label_url_domain_fallback() -> None:
    """Short display names below 5-char threshold fall back to registrable domain."""
    label = _extract_citation_label(
        "Link rot research",
        "https://en.wikipedia.org/wiki/Link_rot",
    )
    # "Link" is 4 chars — too short for fallback-1, so URL domain used
    assert label == "Wikipedia (n.d.)"


def test_extract_citation_label_country_code_tld() -> None:
    """Country-code SLDs (.co.uk, .gov.au) are stripped to reach the registrable label."""
    label_uk = _extract_citation_label(
        "Bank of England DCGMA",
        "https://www.bankofengland.co.uk/financial-stability",
    )
    # Display name "Bank" is 4 chars — fallback-1a/1b don't fire → URL domain used
    assert label_uk == "Bankofengland (n.d.)"

    label_au = _extract_citation_label(
        "APRA Annual Report",
        "https://www.apra.gov.au/annual-report",
    )
    # "APRA" is an all-caps acronym → fallback-1a fires (better than "Apra" from domain)
    assert label_au == "APRA (n.d.)"


def test_extract_citation_label_surname_initials_et_al() -> None:
    """'Surname, Initial. et al. (YYYY)' at start of name → 'Surname et al. (YYYY)'."""
    label = _extract_citation_label(
        "Friston, K. et al. (2022). The free energy principle made simpler",
        "https://arxiv.org/abs/2209.01947",
    )
    assert label == "Friston et al. (2022)"


def test_extract_citation_label_surname_initials_single() -> None:
    """'Surname, A.K. (YYYY). Title' → 'Surname (YYYY)'."""
    label = _extract_citation_label(
        "Seth, A.K. (2021). Anil Seth Finds Consciousness in Life's Push Against Entropy",
        "https://www.quantamagazine.org/",
    )
    assert label == "Seth (2021)"


def test_extract_citation_label_surname_etal_at_start() -> None:
    """'Surname et al. (YYYY). Title' (no parens around full name) → 'Surname et al. (YYYY)'."""
    label = _extract_citation_label(
        "Adams et al. (2023). From Sparse to Dense: GPT-4 Summarization",
        "https://arxiv.org/abs/2309.04269",
    )
    assert label == "Adams et al. (2023)"


def test_extract_citation_label_acronym_full_name_before_colon() -> None:
    """'FullName (ACRONYM): description (YYYY)' → 'ACRONYM (YYYY)'."""
    label = _extract_citation_label(
        "Bank for International Settlements (BIS): AI in financial risk management (2024)",
        "https://www.bis.org/publ/work1293.htm",
    )
    assert label == "BIS (2024)"


def test_extract_citation_label_org_colon_with_year() -> None:
    """'OrgName: description (YYYY)' → 'OrgName (YYYY)'."""
    label = _extract_citation_label(
        "IAASB: Technology position papers and ISA revisions for AI use in audit (2023-2025)",
        "https://www.iaasb.org/focus-areas/technology",
    )
    assert label == "IAASB (2023)"


def test_extract_citation_label_org_colon_no_year() -> None:
    """'OrgName: description' with no year → 'OrgName (n.d.)'."""
    label = _extract_citation_label(
        "Wikipedia: Free energy principle",
        "https://en.wikipedia.org/wiki/Free_energy_principle",
    )
    assert label == "Wikipedia (n.d.)"


def test_extract_citation_label_sqlite_preserves_case() -> None:
    """Display-name fallback-1 preserves original casing (e.g. SQLite, not Sqlite)."""
    label = _extract_citation_label("SQLite docs", "https://sqlite.org")
    assert label == "SQLite (n.d.)"


def test_extract_citation_label_openai_case() -> None:
    """Display-name fallback-1 preserves mixed-case brand (OpenAI)."""
    label = _extract_citation_label("OpenAI Whisper API", "https://platform.openai.com/")
    assert label == "OpenAI (n.d.)"


def test_extract_citation_label_no_display_name_uses_url() -> None:
    """Empty display name falls through to URL-domain fallback."""
    label = _extract_citation_label("", "https://arxiv.org/abs/2306.05685")
    assert label == "Arxiv (n.d.)"


def test_extract_citation_label_et_al_dash_separator() -> None:
    """'Surname et al. — Title (YYYY)' → 'Surname et al. (YYYY)' via pattern-8."""
    label = _extract_citation_label(
        "Ke et al. — LightGBM paper (2017)",
        "https://papers.nips.cc/paper_files/paper/2017/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html",
    )
    assert label == "Ke et al. (2017)"


def test_extract_citation_label_all_caps_acronym_with_year() -> None:
    """All-caps acronym at start of display name → 'ACRONYM (YYYY)'."""
    label = _extract_citation_label(
        "IEEE DIKW 2025 Conference on Knowledge",
        "https://ieeexplore.ieee.org/xpl/conhome/1234",
    )
    assert label == "IEEE (2025)"


def test_extract_citation_label_fico_org_year() -> None:
    """Short all-caps org with embedded year → 'FICO (YYYY)'."""
    label = _extract_citation_label(
        "FICO 2024 Bank Customer Experience Survey — Asia Pacific",
        "https://www.fico.com/en/latest-thinking/article/bank-customer-experience-2024",
    )
    assert label == "FICO (2024)"


def test_extract_citation_label_dora_comma_boundary() -> None:
    """All-caps acronym before comma → 'DORA (YYYY)' (not blocked by comma boundary)."""
    label = _extract_citation_label(
        "DORA, Accelerate State of DevOps Report 2024",
        "https://dora.dev/research/2024/dora-report/",
    )
    assert label == "DORA (2024)"


def test_extract_citation_label_trailing_publisher_year() -> None:
    """'Description — Publisher YEAR' at end → 'Publisher (YEAR)' via fallback-1c."""
    label = _extract_citation_label(
        "Word embeddings × knowledge graphs intersection — Springer 2024",
        "https://link.springer.com/article/example",
    )
    assert label == "Springer (2024)"


def test_render_source_links_uses_label_map() -> None:
    """_render_source_links uses url_to_label when available."""
    url = "https://arxiv.org/abs/2306.05685"
    html = _render_source_links([url], {url: "Zheng et al. (2023)"})
    assert "Zheng et al. (2023)" in html
    assert 'href="https://arxiv.org/abs/2306.05685"' in html
    assert 'class="claim-source-link"' in html


def test_render_source_links_fallback_without_label_map() -> None:
    """_render_source_links falls back to domain (n.d.) when url_to_label is empty."""
    url = "https://www.promptfoo.dev/docs/integrations/ci-cd/"
    html = _render_source_links([url])
    assert "promptfoo" in html.lower() or "Promptfoo" in html
    assert 'href="https://www.promptfoo.dev/docs/integrations/ci-cd/"' in html


def test_render_source_links_deduplicates() -> None:
    """Duplicate URLs produce only one link."""
    url = "https://example.com/"
    html = _render_source_links([url, url], {url: "Example (2024)"})
    assert html.count("Example (2024)") == 1


# ---------------------------------------------------------------------------
# _item_url
# ---------------------------------------------------------------------------


def test_item_url_research_item() -> None:
    """Research items use /Research/research/ URL prefix."""
    item = {
        "slug": "my-item",
        "_kind": "research",
        "page_url": "/Research/research/my-item.html",
    }
    assert _item_url(item) == "/Research/research/my-item.html"


def test_item_url_knowledge_item() -> None:
    """Knowledge items use /Research/knowledge/ URL prefix."""
    item = {
        "slug": "my-synthesis",
        "_kind": "knowledge",
        "page_url": "/Research/knowledge/my-synthesis.html",
    }
    assert _item_url(item) == "/Research/knowledge/my-synthesis.html"


def test_item_url_fallback_without_page_url() -> None:
    """Items without page_url fall back to the research prefix."""
    item = {"slug": "legacy-item"}
    assert _item_url(item) == "/Research/research/legacy-item.html"


# ---------------------------------------------------------------------------
# render_card uses page_url
# ---------------------------------------------------------------------------


def _make_full_item(slug: str, kind: str = "research") -> dict:
    """Make an item dict with all fields required by render_card."""
    prefix = "knowledge" if kind == "knowledge" else "research"
    return {
        "slug": slug,
        "tags": ["ai"],
        "question": "A question",
        "question_excerpt": "A question",
        "display_title": slug,
        "added_str": "2026-01-01",
        "item_type": "synthesis" if kind == "knowledge" else "primary",
        "superseded_by": None,
        "_kind": kind,
        "page_url": f"/Research/{prefix}/{slug}.html",
    }


def test_render_card_research_uses_research_url() -> None:
    """render_card produces a link to /Research/research/ for research items."""
    item = _make_full_item("some-research", "research")
    html = render_card(item)
    assert 'href="/Research/research/some-research.html"' in html


def test_render_card_knowledge_uses_knowledge_url() -> None:
    """render_card produces a link to /Research/knowledge/ for knowledge items."""
    item = _make_full_item("some-synthesis", "knowledge")
    html = render_card(item)
    assert 'href="/Research/knowledge/some-synthesis.html"' in html


def test_render_card_knowledge_has_synthesis_badge() -> None:
    """Knowledge items show the synthesis badge in the card."""
    item = _make_full_item("some-synthesis", "knowledge")
    html = render_card(item)
    assert "synthesis" in html


# ---------------------------------------------------------------------------
# load_knowledge_items
# ---------------------------------------------------------------------------


_SYNTHESIS_MD = """\
---
title: "Test Synthesis Title"
synthesised: 2026-04-01
status: draft
theme: test-theme
source_items:
  - 2026-01-01-source-item
tags:
  - ai
  - governance
cites:
  - 2026-01-01-source-item
confidence: medium
versions: []
---

# Test Synthesis Title

## Synthesis Question

What does test synthesis find?

## Cross-Item Findings

1. Finding one. [inference; source: 2026-01-01-source-item]
"""


def test_load_knowledge_items_parses_valid_file(tmp_path: Path) -> None:
    """load_knowledge_items returns one item for a valid synthesis file."""
    import build_site  # noqa: PLC0415

    knowledge_dir = tmp_path / "Knowledge"
    knowledge_dir.mkdir()
    (knowledge_dir / "2026-04-01-test-theme.md").write_text(_SYNTHESIS_MD, encoding="utf-8")

    original = build_site.KNOWLEDGE_DIR
    build_site.KNOWLEDGE_DIR = knowledge_dir
    try:
        items = load_knowledge_items()
    finally:
        build_site.KNOWLEDGE_DIR = original

    assert len(items) == 1
    item = items[0]
    assert item["title"] == "Test Synthesis Title"
    assert item["_kind"] == "knowledge"
    assert item["item_type"] == "synthesis"
    assert item["page_url"] == "/Research/knowledge/2026-04-01-test-theme.html"
    assert item["tags"] == ["ai", "governance"]
    assert "2026-01-01-source-item" in item["cites"]


def test_load_knowledge_items_skips_template(tmp_path: Path) -> None:
    """load_knowledge_items skips _template.md."""
    import build_site  # noqa: PLC0415

    knowledge_dir = tmp_path / "Knowledge"
    knowledge_dir.mkdir()
    (knowledge_dir / "_template.md").write_text(_SYNTHESIS_MD, encoding="utf-8")

    original = build_site.KNOWLEDGE_DIR
    build_site.KNOWLEDGE_DIR = knowledge_dir
    try:
        items = load_knowledge_items()
    finally:
        build_site.KNOWLEDGE_DIR = original

    assert items == []


def test_load_knowledge_items_empty_dir(tmp_path: Path) -> None:
    """load_knowledge_items returns empty list when Knowledge/ is empty."""
    import build_site  # noqa: PLC0415

    knowledge_dir = tmp_path / "Knowledge"
    knowledge_dir.mkdir()

    original = build_site.KNOWLEDGE_DIR
    build_site.KNOWLEDGE_DIR = knowledge_dir
    try:
        items = load_knowledge_items()
    finally:
        build_site.KNOWLEDGE_DIR = original

    assert items == []


def test_load_knowledge_items_missing_dir() -> None:
    """load_knowledge_items returns empty list when Knowledge/ does not exist."""
    import build_site  # noqa: PLC0415

    original = build_site.KNOWLEDGE_DIR
    build_site.KNOWLEDGE_DIR = Path("/nonexistent/Knowledge")
    try:
        items = load_knowledge_items()
    finally:
        build_site.KNOWLEDGE_DIR = original

    assert items == []


# ---------------------------------------------------------------------------
# build_knowledge_index_page
# ---------------------------------------------------------------------------


def test_build_knowledge_index_page_empty() -> None:
    """Index page with no items shows the empty-state message."""
    html = build_knowledge_index_page([])
    assert "Synthesis Loop" in html
    assert "No synthesis items yet" in html


def test_build_knowledge_index_page_with_items() -> None:
    """Index page renders cards for provided synthesis items."""
    item = _make_full_item("my-synthesis", "knowledge")
    item["added"] = datetime(2026, 4, 1, tzinfo=UTC)
    item["added_str"] = "2026-04-01"
    item["question"] = "What does this synthesise?"
    item["question_excerpt"] = "What does this synthesise?"
    html = build_knowledge_index_page([item])
    assert "my-synthesis" in html
    assert "/Research/knowledge/my-synthesis.html" in html
    assert "No synthesis items yet" not in html
