"""Import scripture JSON files into SQLite database."""

import json
import re
import sys
from pathlib import Path

from .db import ScriptureDB

# Map JSON filenames to volume names
VOLUMES = {
    "book-of-mormon-flat.json": "book-of-mormon",
    "doctrine-and-covenants-flat.json": "doctrine-and-covenants",
    "pearl-of-great-price-flat.json": "pearl-of-great-price",
    "old-testament-flat.json": "old-testament",
    "new-testament-flat.json": "new-testament",
}


def parse_reference(reference: str) -> tuple[str, int, int]:
    """
    Parse a scripture reference into book, chapter, verse.

    Examples:
        "1 Nephi 3:7" -> ("1 Nephi", 3, 7)
        "Genesis 1:1" -> ("Genesis", 1, 1)
        "D&C 76:22" -> ("D&C", 76, 22)
    """
    # Handle various reference formats
    # Pattern: book name (may include numbers/spaces), chapter:verse
    match = re.match(r'^(.+?)\s+(\d+):(\d+)$', reference)
    if match:
        book = match.group(1)
        chapter = int(match.group(2))
        verse = int(match.group(3))
        return book, chapter, verse

    raise ValueError(f"Could not parse reference: {reference}")


def import_flat_json(db: ScriptureDB, json_path: Path, volume: str):
    """Import a flat JSON scripture file."""
    print(f"Importing {volume} from {json_path.name}...")

    with open(json_path) as f:
        data = json.load(f)

    # Import verses
    verses = data.get("verses", [])
    for i, v in enumerate(verses):
        reference = v["reference"]
        text = v["text"]

        try:
            book, chapter, verse = parse_reference(reference)
            db.insert_verse(volume, book, chapter, verse, reference, text)
        except ValueError as e:
            print(f"  Warning: {e}")

        if (i + 1) % 1000 == 0:
            print(f"  Imported {i + 1}/{len(verses)} verses...")

    db.commit()
    print(f"  Imported {len(verses)} verses from {volume}")

    # Import headings
    headings = data.get("headings", [])
    for h in headings:
        db.insert_heading(volume, h["reference"], h["text"])

    db.commit()
    print(f"  Imported {len(headings)} headings from {volume}")


def main():
    """Main entry point for import script."""
    # Determine paths
    script_dir = Path(__file__).parent
    # script_dir is scripture_search/, go up: scripture-search/, tools/, scripture-study/
    project_root = script_dir.parent.parent.parent  # Up to scripture-study
    json_dir = project_root / "scriptures-json" / "flat"
    data_dir = project_root / "data"

    # Create data directory if needed
    data_dir.mkdir(exist_ok=True)
    db_path = data_dir / "scriptures.db"

    # Remove existing database to start fresh
    if db_path.exists():
        print(f"Removing existing database: {db_path}")
        db_path.unlink()

    print(f"Creating database: {db_path}")

    with ScriptureDB(db_path) as db:
        db.create_tables()

        # Import each volume
        for filename, volume in VOLUMES.items():
            json_path = json_dir / filename
            if json_path.exists():
                import_flat_json(db, json_path, volume)
            else:
                print(f"Warning: {json_path} not found, skipping {volume}")

        # Print summary
        print("\nImport complete!")
        print(f"Total verses: {db.get_verse_count()}")
        for volume in db.get_volumes():
            count = db.get_verse_count(volume)
            print(f"  {volume}: {count} verses")


if __name__ == "__main__":
    main()
