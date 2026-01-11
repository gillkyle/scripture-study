"""SQLite database for scripture storage and FTS5 search."""

import sqlite3
from pathlib import Path
from typing import Optional

# Path from scripture_search/db.py -> scripture-search/ -> tools/ -> scripture-study/ -> data/
DEFAULT_DB_PATH = Path(__file__).parent.parent.parent.parent / "data" / "scriptures.db"


class ScriptureDB:
    """Interface to the scripture SQLite database."""

    def __init__(self, db_path: Optional[Path] = None):
        self.db_path = db_path or DEFAULT_DB_PATH
        self._conn: Optional[sqlite3.Connection] = None

    @property
    def conn(self) -> sqlite3.Connection:
        if self._conn is None:
            self._conn = sqlite3.connect(self.db_path)
            self._conn.row_factory = sqlite3.Row
        return self._conn

    def close(self):
        if self._conn:
            self._conn.close()
            self._conn = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def create_tables(self):
        """Create the database schema with FTS5 for full-text search."""
        cursor = self.conn.cursor()

        # Main verses table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS verses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                volume TEXT NOT NULL,
                book TEXT NOT NULL,
                chapter INTEGER NOT NULL,
                verse INTEGER NOT NULL,
                reference TEXT NOT NULL UNIQUE,
                text TEXT NOT NULL
            )
        """)

        # Headings table (book/chapter summaries)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS headings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                volume TEXT NOT NULL,
                reference TEXT NOT NULL UNIQUE,
                text TEXT NOT NULL
            )
        """)

        # FTS5 virtual table for full-text search on verses
        cursor.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS verses_fts USING fts5(
                reference,
                text,
                content='verses',
                content_rowid='id'
            )
        """)

        # FTS5 virtual table for headings
        cursor.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS headings_fts USING fts5(
                reference,
                text,
                content='headings',
                content_rowid='id'
            )
        """)

        # Triggers to keep FTS index in sync
        cursor.execute("""
            CREATE TRIGGER IF NOT EXISTS verses_ai AFTER INSERT ON verses BEGIN
                INSERT INTO verses_fts(rowid, reference, text) VALUES (new.id, new.reference, new.text);
            END
        """)

        cursor.execute("""
            CREATE TRIGGER IF NOT EXISTS verses_ad AFTER DELETE ON verses BEGIN
                INSERT INTO verses_fts(verses_fts, rowid, reference, text) VALUES('delete', old.id, old.reference, old.text);
            END
        """)

        cursor.execute("""
            CREATE TRIGGER IF NOT EXISTS verses_au AFTER UPDATE ON verses BEGIN
                INSERT INTO verses_fts(verses_fts, rowid, reference, text) VALUES('delete', old.id, old.reference, old.text);
                INSERT INTO verses_fts(rowid, reference, text) VALUES (new.id, new.reference, new.text);
            END
        """)

        cursor.execute("""
            CREATE TRIGGER IF NOT EXISTS headings_ai AFTER INSERT ON headings BEGIN
                INSERT INTO headings_fts(rowid, reference, text) VALUES (new.id, new.reference, new.text);
            END
        """)

        # Indexes for common queries
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_verses_volume ON verses(volume)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_verses_book ON verses(book)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_verses_reference ON verses(reference)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_headings_volume ON headings(volume)")

        self.conn.commit()

    def insert_verse(self, volume: str, book: str, chapter: int, verse: int, reference: str, text: str):
        """Insert a single verse."""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO verses (volume, book, chapter, verse, reference, text) VALUES (?, ?, ?, ?, ?, ?)",
            (volume, book, chapter, verse, reference, text)
        )

    def insert_heading(self, volume: str, reference: str, text: str):
        """Insert a heading/summary."""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO headings (volume, reference, text) VALUES (?, ?, ?)",
            (volume, reference, text)
        )

    def commit(self):
        """Commit current transaction."""
        self.conn.commit()

    def search(self, query: str, volume: Optional[str] = None, limit: int = 50) -> list[dict]:
        """
        Full-text search for verses.

        Args:
            query: Search query (supports FTS5 syntax like "word1 word2", "word1 OR word2", etc.)
            volume: Optional filter by volume (e.g., "book-of-mormon", "old-testament")
            limit: Maximum results to return

        Returns:
            List of matching verses with reference and text
        """
        cursor = self.conn.cursor()

        if volume:
            cursor.execute("""
                SELECT v.reference, v.text, v.book, v.chapter, v.verse, v.volume
                FROM verses_fts fts
                JOIN verses v ON fts.rowid = v.id
                WHERE verses_fts MATCH ?
                AND v.volume = ?
                ORDER BY rank
                LIMIT ?
            """, (query, volume, limit))
        else:
            cursor.execute("""
                SELECT v.reference, v.text, v.book, v.chapter, v.verse, v.volume
                FROM verses_fts fts
                JOIN verses v ON fts.rowid = v.id
                WHERE verses_fts MATCH ?
                ORDER BY rank
                LIMIT ?
            """, (query, limit))

        return [dict(row) for row in cursor.fetchall()]

    def get_verse(self, reference: str) -> Optional[dict]:
        """Get a specific verse by reference (e.g., '1 Nephi 3:7')."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT reference, text, book, chapter, verse, volume FROM verses WHERE reference = ?",
            (reference,)
        )
        row = cursor.fetchone()
        return dict(row) if row else None

    def get_chapter(self, book: str, chapter: int) -> list[dict]:
        """Get all verses in a chapter."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT reference, text, verse FROM verses WHERE book = ? AND chapter = ? ORDER BY verse",
            (book, chapter)
        )
        return [dict(row) for row in cursor.fetchall()]

    def get_book_chapters(self, book: str) -> list[int]:
        """Get list of chapter numbers for a book."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT DISTINCT chapter FROM verses WHERE book = ? ORDER BY chapter",
            (book,)
        )
        return [row[0] for row in cursor.fetchall()]

    def get_books(self, volume: Optional[str] = None) -> list[str]:
        """Get list of books, optionally filtered by volume."""
        cursor = self.conn.cursor()
        if volume:
            cursor.execute(
                "SELECT DISTINCT book FROM verses WHERE volume = ? ORDER BY id",
                (volume,)
            )
        else:
            cursor.execute("SELECT DISTINCT book FROM verses ORDER BY id")
        return [row[0] for row in cursor.fetchall()]

    def get_volumes(self) -> list[str]:
        """Get list of available volumes."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT volume FROM verses ORDER BY id")
        return [row[0] for row in cursor.fetchall()]

    def get_heading(self, reference: str) -> Optional[dict]:
        """Get heading/summary for a book or chapter."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT reference, text, volume FROM headings WHERE reference = ?",
            (reference,)
        )
        row = cursor.fetchone()
        return dict(row) if row else None

    def get_verse_count(self, volume: Optional[str] = None) -> int:
        """Get total verse count, optionally filtered by volume."""
        cursor = self.conn.cursor()
        if volume:
            cursor.execute("SELECT COUNT(*) FROM verses WHERE volume = ?", (volume,))
        else:
            cursor.execute("SELECT COUNT(*) FROM verses")
        return cursor.fetchone()[0]
