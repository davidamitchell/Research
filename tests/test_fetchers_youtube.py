"""Tests for the YouTube transcript fetcher.

All network calls are mocked — no real HTTP or YouTube API requests are made.
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import httpx

from src.fetchers import FetchedItem
from src.fetchers.youtube import (
    YouTubeFetcher,
    _parse_channel_feed,
    _video_id_from_url,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

SAMPLE_ATOM_FEED = """\
<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:yt="http://www.youtube.com/xml/schemas/2015"
      xmlns:media="http://search.yahoo.com/mrss/">
  <entry>
    <yt:videoId>abc123</yt:videoId>
    <title>Video One</title>
    <link rel="alternate" href="https://www.youtube.com/watch?v=abc123"/>
    <media:group>
      <media:description>Description of video one.</media:description>
    </media:group>
  </entry>
  <entry>
    <yt:videoId>def456</yt:videoId>
    <title>Video Two</title>
    <link rel="alternate" href="https://www.youtube.com/watch?v=def456"/>
    <media:group>
      <media:description>Description of video two.</media:description>
    </media:group>
  </entry>
</feed>
"""

# ---------------------------------------------------------------------------
# _video_id_from_url
# ---------------------------------------------------------------------------


def test_video_id_from_youtu_be_url() -> None:
    assert _video_id_from_url("https://youtu.be/HYUoS0GkGCs") == "HYUoS0GkGCs"


def test_video_id_from_watch_url() -> None:
    assert _video_id_from_url("https://www.youtube.com/watch?v=HYUoS0GkGCs") == "HYUoS0GkGCs"


def test_video_id_bare_id_passthrough() -> None:
    assert _video_id_from_url("HYUoS0GkGCs") == "HYUoS0GkGCs"


# ---------------------------------------------------------------------------
# _parse_channel_feed
# ---------------------------------------------------------------------------


def test_parse_channel_feed_returns_entries() -> None:
    entries = _parse_channel_feed(SAMPLE_ATOM_FEED, max_videos=5)
    assert len(entries) == 2


def test_parse_channel_feed_respects_max_videos() -> None:
    entries = _parse_channel_feed(SAMPLE_ATOM_FEED, max_videos=1)
    assert len(entries) == 1


def test_parse_channel_feed_extracts_video_id() -> None:
    entries = _parse_channel_feed(SAMPLE_ATOM_FEED, max_videos=5)
    assert entries[0]["video_id"] == "abc123"


def test_parse_channel_feed_extracts_title() -> None:
    entries = _parse_channel_feed(SAMPLE_ATOM_FEED, max_videos=5)
    assert entries[0]["title"] == "Video One"


def test_parse_channel_feed_extracts_description() -> None:
    entries = _parse_channel_feed(SAMPLE_ATOM_FEED, max_videos=5)
    assert "Description of video one" in entries[0]["description"]


# ---------------------------------------------------------------------------
# YouTubeFetcher — channel mode
# ---------------------------------------------------------------------------


def test_fetch_channel_returns_items() -> None:
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.text = SAMPLE_ATOM_FEED
    mock_response.raise_for_status = MagicMock()

    mock_client = MagicMock(spec=httpx.Client)
    mock_client.get.return_value = mock_response

    with patch("src.fetchers.youtube.YouTubeTranscriptApi") as mock_cls:
        instance = mock_cls.return_value
        snippet = MagicMock()
        snippet.text = "transcript text"
        instance.fetch.return_value = [snippet]

        fetcher = YouTubeFetcher(channel_id="UC_test", max_videos=2, http_client=mock_client)
        items = fetcher.fetch()

    assert len(items) == 2
    assert all(isinstance(i, FetchedItem) for i in items)
    assert items[0].title == "Video One"
    assert "transcript text" in items[0].content


def test_fetch_channel_uses_description_fallback() -> None:
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.text = SAMPLE_ATOM_FEED
    mock_response.raise_for_status = MagicMock()

    mock_client = MagicMock(spec=httpx.Client)
    mock_client.get.return_value = mock_response

    with patch("src.fetchers.youtube.YouTubeTranscriptApi") as mock_cls:
        instance = mock_cls.return_value
        instance.fetch.side_effect = Exception("transcript blocked")

        fetcher = YouTubeFetcher(channel_id="UC_test", max_videos=1, http_client=mock_client)
        items = fetcher.fetch()

    assert len(items) == 1
    assert "Description of video one" in items[0].content


def test_fetch_channel_skips_on_feed_error() -> None:
    mock_client = MagicMock(spec=httpx.Client)
    mock_client.get.side_effect = httpx.ConnectError("network error")

    fetcher = YouTubeFetcher(channel_id="UC_test", http_client=mock_client)
    items = fetcher.fetch()

    assert items == []


# ---------------------------------------------------------------------------
# YouTubeFetcher — single video mode
# ---------------------------------------------------------------------------


def test_fetch_video_returns_item() -> None:
    mock_client = MagicMock(spec=httpx.Client)  # not called in transcript path

    with patch("src.fetchers.youtube.YouTubeTranscriptApi") as mock_cls:
        instance = mock_cls.return_value
        snippet = MagicMock()
        snippet.text = "single video transcript"
        instance.fetch.return_value = [snippet]

        fetcher = YouTubeFetcher(
            video_urls=["https://youtu.be/HYUoS0GkGCs"], http_client=mock_client
        )
        items = fetcher.fetch()

    assert len(items) == 1
    assert items[0].source_id == "HYUoS0GkGCs"
    assert "single video transcript" in items[0].content


def test_fetch_video_uses_description_fallback() -> None:
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.text = '<meta name="description" content="Page description fallback">'
    mock_response.raise_for_status = MagicMock()

    mock_client = MagicMock(spec=httpx.Client)
    mock_client.get.return_value = mock_response

    with patch("src.fetchers.youtube.YouTubeTranscriptApi") as mock_cls:
        instance = mock_cls.return_value
        instance.fetch.side_effect = Exception("transcript blocked")

        fetcher = YouTubeFetcher(
            video_urls=["https://youtu.be/HYUoS0GkGCs"], http_client=mock_client
        )
        items = fetcher.fetch()

    assert len(items) == 1
    assert "Page description fallback" in items[0].content


def test_fetch_video_returns_empty_on_no_content() -> None:
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.text = "<html>no description here</html>"
    mock_response.raise_for_status = MagicMock()

    mock_client = MagicMock(spec=httpx.Client)
    mock_client.get.return_value = mock_response

    with patch("src.fetchers.youtube.YouTubeTranscriptApi") as mock_cls:
        instance = mock_cls.return_value
        instance.fetch.side_effect = Exception("transcript blocked")

        fetcher = YouTubeFetcher(
            video_urls=["https://youtu.be/HYUoS0GkGCs"], http_client=mock_client
        )
        items = fetcher.fetch()

    assert items == []
