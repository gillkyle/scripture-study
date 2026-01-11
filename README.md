# Scripture Study System

A Claude Code-powered scripture study workspace for Come Follow Me 2025 (Old Testament), Book of Mormon, and General Conference study.

## Quick Start

1. Navigate to this directory:
   ```bash
   cd /Users/kyle/Documents/Study/scripture-study
   ```

2. Start Claude Code:
   ```bash
   claude
   ```

3. Use any of the study commands below.

## Available Commands

### `/study [passage]`
Deep dive into a scripture passage with context, cross-references, and application questions.

```
/study Genesis 1:1-5
/study 1 Nephi 3:7
/study Isaiah 53:3-5
```

### `/themes [passage or text]`
Extract and organize themes from scripture or pasted text.

```
/themes Exodus 3
/themes Alma 32
```

### `/parallels [topic or passage]`
Find connections to personal interests (anime, LotR, programming, literature, science).

```
/parallels repentance
/parallels Alma 36
/parallels the Atonement
```

### `/conference [topic, speaker, or scripture]`
Search General Conference talks.

```
/conference faith
/conference President Nelson
/conference Mosiah 3:19
```

### `/interview [optional topic]`
Start a guided, Socratic study session with reflective questions.

```
/interview
/interview Moses 1
/interview grace
```

### `/compare [passages]`
Compare multiple scripture passages side-by-side.

```
/compare Isaiah 53 and Mosiah 14
/compare faith in Alma 32 vs Hebrews 11
/compare 2 Nephi 2 and Moses 5
```

### `/lookup [quote or topic]`
Find similar quotes, cross-references, and conference mentions.

```
/lookup "I will go and do"
/lookup "charity never faileth"
/lookup covenant path
```

## Study Workflows

### Deep Dive Study
1. `/study [passage]` - Get full analysis
2. `/parallels [passage]` - Connect to your interests
3. `/conference [topic]` - Find prophetic commentary

### Thematic Study
1. `/themes [passage]` - Extract themes
2. `/lookup [theme]` - Find related scriptures
3. `/compare [related passages]` - See connections

### Reflective Study
1. `/interview [passage]` - Guided reflection
2. Answer questions thoughtfully
3. Save insights to notes

### Interest-Based Study
1. Start with an interest parallel you noticed
2. `/parallels [topic]` - Explore the connection
3. `/study [related scripture]` - Go deeper

## Directory Structure

```
scripture-study/
├── .claude/
│   ├── CLAUDE.md           # Project context
│   ├── commands/           # Study commands
│   └── agents/             # Study companion agent
├── notes/
│   ├── old-testament/      # OT study notes
│   ├── book-of-mormon/     # BoM study notes
│   ├── conference/         # Conference talk notes
│   └── parallels/          # Interest connection notes
└── README.md               # This file
```

## Note File Naming

- OT notes: `notes/old-testament/YYYY-MM-DD-book-chapter.md`
- BoM notes: `notes/book-of-mormon/YYYY-MM-DD-book-chapter.md`
- Conference: `notes/conference/YYYY-MM-speaker-title.md`
- Parallels: `notes/parallels/YYYY-MM-DD-topic.md`

## Tips

- Commands can be combined: study a passage, then find parallels, then search conference talks
- The `/interview` command adapts to your responses - there are no wrong answers
- Save notes regularly to build a searchable study library
- Interest parallels work best when you're specific about what you want to connect

## Come Follow Me 2025

This year focuses on the Old Testament. Key sections:
- Genesis: Creation, Fall, covenants, patriarchs
- Exodus: Deliverance, law, tabernacle
- Leviticus-Deuteronomy: Holiness, sacrifice, covenant renewal
- Historical books: Joshua through Esther
- Wisdom literature: Job, Psalms, Proverbs, Ecclesiastes
- Major prophets: Isaiah, Jeremiah, Ezekiel, Daniel
- Minor prophets: Hosea through Malachi
