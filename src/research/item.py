"""Research item data model and file I/O."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path


@dataclass
class ResearchItem:
    """Represents a single research item loaded from a Markdown file."""

    path: Path
    title: str
    added: date
    status: str  # backlog | in-progress | completed
    priority: str  # low | medium | high
    tags: list[str] = field(default_factory=list)
    output: list[str] = field(default_factory=list)

    @classmethod
    def from_file(cls, path: Path) -> ResearchItem:
        """Load a ResearchItem from a Markdown file with YAML front matter."""
        import re

        text = path.read_text(encoding="utf-8")
        # Extract YAML front matter between --- delimiters
        match = re.match(r"^---\n(.+?)\n---", text, re.DOTALL)
        if not match:
            raise ValueError(f"No YAML front matter found in {path}")

        import yaml  # type: ignore[import-untyped]

        meta = yaml.safe_load(match.group(1))

        return cls(
            path=path,
            title=meta.get("title", path.stem),
            added=meta.get("added", date.today()),
            status=meta.get("status", "backlog"),
            priority=meta.get("priority", "medium"),
            tags=meta.get("tags") or [],
            output=meta.get("output") or [],
        )

    def state_dir_name(self) -> str:
        """Return the directory name corresponding to this item's status."""
        mapping = {
            "backlog": "backlog",
            "in-progress": "in-progress",
            "completed": "completed",
        }
        return mapping.get(self.status, "backlog")
