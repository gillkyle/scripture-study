"""High-level search functions for scripture lookup."""

from pathlib import Path
from typing import Optional

from .db import ScriptureDB, DEFAULT_DB_PATH


def _get_db(db_path: Optional[Path] = None) -> ScriptureDB:
    """Get database instance."""
    return ScriptureDB(db_path or DEFAULT_DB_PATH)


def search_verses(
    query: str,
    volume: Optional[str] = None,
    limit: int = 50,
    db_path: Optional[Path] = None
) -> list[dict]:
    """
    Search for verses containing the given query.

    Args:
        query: Search terms (supports FTS5 syntax)
        volume: Optional volume filter (book-of-mormon, old-testament, etc.)
        limit: Maximum results
        db_path: Optional custom database path

    Returns:
        List of matching verses with reference, text, book, chapter, verse, volume
    """
    with _get_db(db_path) as db:
        return db.search(query, volume, limit)


def get_verse(reference: str, db_path: Optional[Path] = None) -> Optional[dict]:
    """
    Get a specific verse by reference.

    Args:
        reference: Scripture reference (e.g., "1 Nephi 3:7", "Genesis 1:1")
        db_path: Optional custom database path

    Returns:
        Verse dict or None if not found
    """
    with _get_db(db_path) as db:
        return db.get_verse(reference)


def get_chapter(book: str, chapter: int, db_path: Optional[Path] = None) -> list[dict]:
    """
    Get all verses in a chapter.

    Args:
        book: Book name (e.g., "1 Nephi", "Genesis")
        chapter: Chapter number
        db_path: Optional custom database path

    Returns:
        List of verses in order
    """
    with _get_db(db_path) as db:
        return db.get_chapter(book, chapter)


def get_book_list(volume: Optional[str] = None, db_path: Optional[Path] = None) -> list[str]:
    """
    Get list of books.

    Args:
        volume: Optional volume filter
        db_path: Optional custom database path

    Returns:
        List of book names
    """
    with _get_db(db_path) as db:
        return db.get_books(volume)


def get_volumes(db_path: Optional[Path] = None) -> list[str]:
    """Get list of available volumes."""
    with _get_db(db_path) as db:
        return db.get_volumes()


def get_heading(reference: str, db_path: Optional[Path] = None) -> Optional[dict]:
    """
    Get heading/summary for a book or chapter.

    Args:
        reference: Book name or chapter reference
        db_path: Optional custom database path

    Returns:
        Heading dict or None
    """
    with _get_db(db_path) as db:
        return db.get_heading(reference)


def get_context(reference: str, before: int = 2, after: int = 2, db_path: Optional[Path] = None) -> list[dict]:
    """
    Get a verse with surrounding context.

    Args:
        reference: Scripture reference
        before: Number of verses before
        after: Number of verses after
        db_path: Optional custom database path

    Returns:
        List of verses including context
    """
    with _get_db(db_path) as db:
        verse = db.get_verse(reference)
        if not verse:
            return []

        book = verse["book"]
        chapter = verse["chapter"]
        verse_num = verse["verse"]

        # Get chapter verses
        chapter_verses = db.get_chapter(book, chapter)

        # Find range
        start = max(0, verse_num - before - 1)
        end = min(len(chapter_verses), verse_num + after)

        return chapter_verses[start:end]
