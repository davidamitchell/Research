"""Fetchers package — protocol and shared types."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass
class FetchedItem:
    """A single piece of content fetched from a source."""

    url: str
    title: str
    content: str
    source_id: str


class Fetcher(Protocol):
    """Protocol that all fetchers must implement."""

    def fetch(self) -> list[FetchedItem]:
        """Fetch and return a list of items from the source."""
        ...
