---
description: Find similar quotes, cross-references, and conference mentions
argument-hint: [quote, phrase, or topic] (e.g., "I will go and do" or "charity never faileth")
allowed-tools: WebSearch, WebFetch, Read, Write, Bash
---

# Quote and Reference Lookup

Find similar quotes and references for: **$ARGUMENTS**

## Local Scripture Database

Use the local scripture search tool first for fast lookups:
```bash
# Search for phrases across all scriptures
uv run --project tools/scripture-search scripture-search search "I will go and do"

# Filter by volume
uv run --project tools/scripture-search scripture-search search "charity" -v book-of-mormon

# Get verse with context
uv run --project tools/scripture-search scripture-search context "Moroni 7:47" -b 2 -a 2
```

## Search Process

### 1. Exact Phrase Search
If a specific phrase is provided:
- Use scripture-search to find exact matches across all scriptures
- Find variations of the phrase in different scriptures
- Note the original source and any quotations of it

### 2. Topical Search
Identify the core topic/principle and find:
- Related scriptures from Topical Guide categories
- Parallel teachings in different books
- Progressive revelation on the topic

### 3. Conference Talk Mentions
Search for General Conference talks that:
- Quote this scripture or phrase
- Teach on this topic
- Provide prophetic commentary

### 4. Cross-References
For scripture references, provide:
- Footnote cross-references
- Topical Guide connections
- Related entries from Bible Dictionary/Guide to the Scriptures
- Institute manual references

### 5. Phrase Parallels
Find similar phrasing or concepts in:
- Other scriptures (including different translations/versions)
- Hymns and Primary songs
- Temple language (where appropriate for discussion)
- Other LDS standard works

## Output Format

```markdown
## Lookup: "[Quote/Topic]"

### Original Source
**Reference**: [Book Chapter:Verse]
**Full Text**: "[Complete verse or passage]"
**Context**: [Brief context]

### Similar Phrases in Scripture

#### [Reference 1]
> "[Quote]"
**Connection**: [How it relates]

#### [Reference 2]
> "[Quote]"
**Connection**: [How it relates]

### Conference Talk Mentions

#### "[Talk Title]" - [Speaker] ([Date])
> "[How they used/referenced this]"
**Link**: [URL]

### Topical Connections
- **[Topic 1]**: [Related scriptures]
- **[Topic 2]**: [Related scriptures]

### Related Hymns/Songs
- "[Hymn Title]" (#[number]) - [relevant line]

### Study Trail
Suggested order to study these connections:
1. [First passage and why]
2. [Second passage and why]
3. [Third passage and why]
```

## After Lookup

Offer to:
1. Deep dive into any of the found passages with `/study`
2. Compare similar passages with `/compare`
3. Find parallels to interests with `/parallels`
4. Save the research to notes
5. Explore a specific conference talk further
