"""Tests for thread detection logic in scripts/build_site.py."""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

import pytest

# Make scripts/ importable
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from build_site import _cluster_overlap, detect_concept_threads, detect_threads

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_item(
    slug: str,
    tags: list[str],
    thread: str = "",
    added: date | None = None,
) -> dict:
    """Minimal item dict sufficient for thread detection."""
    return {
        "slug": slug,
        "tags": tags,
        "thread": thread,
        "added": added or date(2026, 1, 1),
        "title": slug,
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
