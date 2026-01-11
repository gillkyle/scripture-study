# Scripture Search

Local scripture search tool using SQLite FTS5 for fast full-text search across all LDS standard works.

## Setup

The scripture database is pre-built in `data/scriptures.db`. If you need to rebuild it:

```bash
# Clone the source JSON (if not present)
git clone https://github.com/bcbooks/scriptures-json.git

# Run the import
uv run python -m scripture_search.import_db
```

## Usage

```bash
# Search for text
uv run scripture-search search "faith"

# Filter by volume
uv run scripture-search search "atonement" -v old-testament

# Look up a verse
uv run scripture-search verse "1 Nephi 3:7"

# Get verse with context
uv run scripture-search context "1 Nephi 3:7" -b 2 -a 2

# Get a chapter
uv run scripture-search chapter Genesis 1

# List volumes/books
uv run scripture-search list volumes
uv run scripture-search list books -v book-of-mormon

# Database stats
uv run scripture-search stats
```

## Database Contents

- Book of Mormon: 6,604 verses
- Doctrine and Covenants: 3,654 verses
- Pearl of Great Price: 635 verses
- Old Testament: 23,145 verses
- New Testament: 7,957 verses
- **Total: 41,995 verses**

## Source

Scripture text from [bcbooks/scriptures-json](https://github.com/bcbooks/scriptures-json).
