---
description: Compare multiple scripture passages side-by-side
argument-hint: [passages] (e.g., "Isaiah 53 and Mosiah 14" or "faith in Alma 32 vs Hebrews 11")
allowed-tools: Read, Write, Edit, WebSearch, Bash
---

# Scripture Comparison

Compare the following passages or topics: **$ARGUMENTS**

## Local Scripture Database

Use the local scripture search tool to retrieve passages:
```bash
# Get a full chapter
uv run --project tools/scripture-search scripture-search chapter Isaiah 53
uv run --project tools/scripture-search scripture-search chapter Mosiah 14

# Get specific verses with context
uv run --project tools/scripture-search scripture-search context "Alma 32:21" -b 2 -a 2

# Search for thematic terms across volumes
uv run --project tools/scripture-search scripture-search search "faith" -v book-of-mormon
```

## Comparison Process

### 1. Retrieve Passages
Use scripture-search to retrieve each passage being compared.

### 2. Side-by-Side Analysis

Create a comparison examining:

#### Similarities
- Shared themes and messages
- Common vocabulary or imagery
- Parallel structure or phrasing
- Same doctrines taught

#### Differences
- Unique emphases in each passage
- Different audiences or contexts
- Varying perspectives on the same truth
- Progression or development of ideas

#### Context
- When was each written?
- Who was the author?
- What was the original audience?
- What circumstances prompted each?

### 3. Cross-Canon Insights

When comparing across different scriptures (OT, NT, BoM, D&C):
- How does the Book of Mormon illuminate the Old Testament?
- How does the New Testament fulfill or expand the Old?
- What unique restoration insights come from D&C?
- How do prophetic commentaries (BoM Isaiah chapters, etc.) help interpretation?

### 4. Thematic Synthesis

- What unified truth emerges from comparing these passages?
- How do they complement each other?
- What would be missed by studying only one?
- How does the comparison deepen understanding?

### 5. Visual Comparison (when helpful)

```markdown
| Aspect        | [Passage 1]           | [Passage 2]           |
|---------------|----------------------|----------------------|
| Author        | [author]             | [author]             |
| Context       | [context]            | [context]            |
| Key Theme     | [theme]              | [theme]              |
| Imagery       | [imagery]            | [imagery]            |
| Application   | [application]        | [application]        |
```

## Output Format

```markdown
## Comparison: [Passage 1] and [Passage 2]

### Overview
[Brief introduction to what's being compared and why it matters]

### The Passages
#### [Passage 1 Reference]
[Quote or summary]

#### [Passage 2 Reference]
[Quote or summary]

### Similarities
- [Similarity 1 with explanation]
- [Similarity 2 with explanation]

### Differences
- [Difference 1 with explanation]
- [Difference 2 with explanation]

### Synthesis
[What we learn by comparing these passages together]

### Study Questions
- [Question arising from the comparison]
- [Question arising from the comparison]
```

## After Comparison

Offer to:
1. Save the comparison to notes
2. Deep dive into one of the passages with `/study`
3. Find parallels to interests with `/parallels`
4. Search for conference talks on the shared themes with `/conference`
5. Explore related passages that connect to both
