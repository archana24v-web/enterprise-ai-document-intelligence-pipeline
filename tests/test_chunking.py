import pytest

from src.chunking import chunk_text


def test_chunk_text_splits_long_text():
    chunks = chunk_text("a" * 30, chunk_size=10, overlap=2)
    assert len(chunks) == 4
    assert chunks[0] == "a" * 10


def test_chunk_text_rejects_invalid_overlap():
    with pytest.raises(ValueError):
        chunk_text("example", chunk_size=10, overlap=10)
