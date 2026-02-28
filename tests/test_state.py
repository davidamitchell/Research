"""Tests for src/state.py — StateStore."""

from __future__ import annotations

import json
from pathlib import Path

from src.fetchers import FetchedItem
from src.state import StateStore

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _item(
    url: str = "https://youtu.be/abc123", title: str = "Test", source_id: str = "youtube"
) -> FetchedItem:
    return FetchedItem(url=url, title=title, content="content", source_id=source_id)


# ---------------------------------------------------------------------------
# Construction / loading
# ---------------------------------------------------------------------------


def test_empty_when_file_absent(tmp_path: Path) -> None:
    store = StateStore(tmp_path / "index.json")
    assert store.processed_urls() == set()


def test_loads_existing_state(tmp_path: Path) -> None:
    path = tmp_path / "index.json"
    path.write_text(
        json.dumps(
            {
                "processed": {
                    "https://youtu.be/existing": {
                        "fetched_at": "2026-02-28T00:00:00+00:00",
                        "title": "Existing",
                        "source_id": "youtube",
                    }
                }
            }
        )
    )
    store = StateStore(path)
    assert store.is_processed("https://youtu.be/existing")


def test_empty_when_file_corrupt(tmp_path: Path) -> None:
    path = tmp_path / "index.json"
    path.write_text("not valid json {{{")
    store = StateStore(path)
    assert store.processed_urls() == set()


def test_empty_when_file_not_a_dict(tmp_path: Path) -> None:
    path = tmp_path / "index.json"
    path.write_text("[1, 2, 3]")  # valid JSON but not a dict
    store = StateStore(path)
    assert store.processed_urls() == set()


# ---------------------------------------------------------------------------
# is_processed
# ---------------------------------------------------------------------------


def test_is_processed_false_for_unknown_url(tmp_path: Path) -> None:
    store = StateStore(tmp_path / "index.json")
    assert not store.is_processed("https://youtu.be/unknown")


def test_is_processed_true_after_record(tmp_path: Path) -> None:
    store = StateStore(tmp_path / "index.json")
    item = _item()
    store.record(item)
    assert store.is_processed(item.url)


# ---------------------------------------------------------------------------
# record
# ---------------------------------------------------------------------------


def test_record_persists_to_disk(tmp_path: Path) -> None:
    path = tmp_path / "index.json"
    store = StateStore(path)
    item = _item(url="https://youtu.be/vid1", title="My Video")
    store.record(item)

    data = json.loads(path.read_text())
    assert "https://youtu.be/vid1" in data["processed"]
    entry = data["processed"]["https://youtu.be/vid1"]
    assert entry["title"] == "My Video"
    assert entry["source_id"] == "youtube"
    assert "fetched_at" in entry


def test_record_creates_parent_directory(tmp_path: Path) -> None:
    path = tmp_path / "nested" / "dir" / "index.json"
    store = StateStore(path)
    store.record(_item())
    assert path.exists()


def test_record_multiple_items(tmp_path: Path) -> None:
    path = tmp_path / "index.json"
    store = StateStore(path)
    store.record(_item(url="https://youtu.be/a"))
    store.record(_item(url="https://youtu.be/b"))
    store.record(_item(url="https://youtu.be/c"))

    assert store.is_processed("https://youtu.be/a")
    assert store.is_processed("https://youtu.be/b")
    assert store.is_processed("https://youtu.be/c")


def test_record_overwrites_existing_entry(tmp_path: Path) -> None:
    path = tmp_path / "index.json"
    store = StateStore(path)
    store.record(_item(url="https://youtu.be/vid", title="Old Title"))
    store.record(_item(url="https://youtu.be/vid", title="New Title"))

    data = json.loads(path.read_text())
    assert data["processed"]["https://youtu.be/vid"]["title"] == "New Title"


# ---------------------------------------------------------------------------
# processed_urls
# ---------------------------------------------------------------------------


def test_processed_urls_returns_all_recorded(tmp_path: Path) -> None:
    store = StateStore(tmp_path / "index.json")
    urls = {"https://youtu.be/a", "https://youtu.be/b"}
    for url in urls:
        store.record(_item(url=url))
    assert store.processed_urls() == urls


def test_processed_urls_empty_on_new_store(tmp_path: Path) -> None:
    store = StateStore(tmp_path / "index.json")
    assert store.processed_urls() == set()


# ---------------------------------------------------------------------------
# Reload — state survives round-trip
# ---------------------------------------------------------------------------


def test_state_survives_reload(tmp_path: Path) -> None:
    path = tmp_path / "index.json"
    store1 = StateStore(path)
    store1.record(_item(url="https://youtu.be/persist"))

    store2 = StateStore(path)
    assert store2.is_processed("https://youtu.be/persist")
