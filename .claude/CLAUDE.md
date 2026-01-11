# Scripture Study System

This is Kyle's personal scripture study workspace for studying the Old Testament (Come Follow Me 2025), the Book of Mormon, and General Conference talks.

## Purpose

Support deep, meaningful scripture study by:
- Providing historical and linguistic context
- Extracting and connecting themes across scriptures
- Drawing parallels to personal interests and experiences
- Facilitating reflective, Socratic-style study sessions
- Organizing insights into searchable markdown notes

## Kyle's Interests for Parallels

When drawing connections to gospel principles, consider these areas:

### Anime & Manga
- Character redemption arcs (e.g., Zuko from Avatar, Vegeta from DBZ)
- Sacrifice themes (Fullmetal Alchemist's equivalent exchange vs. grace)
- Friendship and loyalty (Naruto's bonds, One Piece's nakama)
- The hero's journey and becoming something greater

### Lord of the Rings / Tolkien
- Tolkien's Catholic themes woven throughout
- Providence and eucatastrophe (unexpected grace)
- The corrupting nature of power (the Ring)
- Mercy toward enemies (Gollum, Saruman)
- Small and simple things accomplishing great purposes (hobbits)
- Fellowship and the importance of companions on the journey

### Programming & Software Development
- Debugging as repentance (finding and fixing errors)
- Refactoring as sanctification (improving without changing core purpose)
- Design patterns as gospel principles
- Version control as the Atonement (ability to revert, branch, merge)
- Tests as covenants (defining expected behavior)
- Clean code principles and spiritual clarity

### Literature & Poetry
- Classic works with gospel parallels
- Poetic devices in scripture (chiasmus, parallelism)
- The power of story and narrative
- Symbolism and metaphor

### Science & Nature
- Natural laws reflecting divine order
- Creation themes and stewardship
- Patterns in nature reflecting gospel truths
- The cosmos as testimony of God

## Note-Taking Conventions

### File Naming
- Old Testament: `notes/old-testament/YYYY-MM-DD-book-chapter.md`
- Book of Mormon: `notes/book-of-mormon/YYYY-MM-DD-book-chapter.md`
- Conference: `notes/conference/YYYY-MM-speaker-title.md`
- Parallels: `notes/parallels/YYYY-MM-DD-topic.md`

### Note Structure
```markdown
# [Scripture Reference or Topic]

## Context
[Historical, cultural, linguistic context]

## Key Themes
- Theme 1
- Theme 2

## Cross-References
- Related scripture 1
- Related scripture 2

## Parallels
### [Interest Area]
[Connection to personal interests]

## Personal Application
[How this applies to my life]

## Questions to Ponder
- Question 1
- Question 2
```

## Local Scripture Database

A local SQLite database with full-text search is available for fast scripture lookups. **Use this instead of web searches for scripture text.**

### Usage

```bash
# Search for text across all scriptures (uses FTS5 full-text search)
uv run --project tools/scripture-search scripture-search search "keyword or phrase"

# Filter by volume
uv run --project tools/scripture-search scripture-search search "keyword" -v old-testament
# Volumes: book-of-mormon, old-testament, new-testament, doctrine-and-covenants, pearl-of-great-price

# Look up a specific verse
uv run --project tools/scripture-search scripture-search verse "1 Nephi 3:7"

# Get verse with surrounding context
uv run --project tools/scripture-search scripture-search context "reference" -b 3 -a 3

# Get an entire chapter
uv run --project tools/scripture-search scripture-search chapter Genesis 1

# List available books
uv run --project tools/scripture-search scripture-search list books

# Database stats
uv run --project tools/scripture-search scripture-search stats
```

### Database Contents
- **Book of Mormon**: 6,604 verses
- **Doctrine and Covenants**: 3,654 verses
- **Pearl of Great Price**: 635 verses
- **Old Testament**: 23,145 verses
- **New Testament**: 7,957 verses
- **Total**: 41,995 verses

### Source
Scripture text from [bcbooks/scriptures-json](https://github.com/bcbooks/scriptures-json), stored in `scriptures-json/` and indexed in `data/scriptures.db`.

## Come Follow Me 2025

This year's study focuses on the Old Testament. Key books and themes:
- Genesis: Creation, covenants, patriarchs
- Exodus: Deliverance, law, tabernacle
- Leviticus: Holiness, sacrifice, atonement types
- Numbers: Wilderness journey, faith and murmuring
- Deuteronomy: Covenant renewal, Moses's farewell
- Historical books: Judges, Samuel, Kings
- Wisdom literature: Psalms, Proverbs, Ecclesiastes
- Prophets: Isaiah, Jeremiah, Ezekiel, Daniel, minor prophets

## Available Commands

- `/study [passage]` - Deep dive study of a scripture passage
- `/themes [text]` - Extract themes from text
- `/parallels [topic]` - Find connections to personal interests
- `/conference [topic]` - Search General Conference talks
- `/interview` - Guided reflective study session
- `/compare [passages]` - Compare multiple scriptures
- `/lookup [quote/topic]` - Find similar quotes and references
- `/meaningful-questions [passage/topic]` - Generate difficult questions that challenge and stretch

## Study Workflow Options

1. **Deep Dive**: Use `/study` for thorough passage analysis
2. **Thematic**: Use `/themes` then `/lookup` to explore a topic across scriptures
3. **Comparative**: Use `/compare` to see how different scriptures address the same theme
4. **Reflective**: Use `/interview` for Socratic dialogue and personal application
5. **Connected**: Use `/parallels` to bridge scripture with personal interests
6. **Research**: Use `/conference` to find prophetic commentary on passages
7. **Wrestling**: Use `/meaningful-questions` to generate hard questions, then explore them with other commands

## Tone

Approach study with:
- Reverence for sacred texts
- Intellectual curiosity
- Personal application focus
- Joy in discovering connections
- Humility in interpretation
