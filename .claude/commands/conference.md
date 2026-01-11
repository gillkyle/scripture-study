---
description: Search General Conference talks by topic, speaker, or scripture
argument-hint: [topic, speaker, or scripture] (e.g., "faith" or "President Nelson" or "Mosiah 3:19")
allowed-tools: WebSearch, WebFetch, Read, Write
---

# General Conference Talk Search

Search for General Conference talks related to: **$ARGUMENTS**

## Search Strategy

### 1. Web Search
Search churchofjesuschrist.org for relevant talks using queries like:
- `site:churchofjesuschrist.org/study/general-conference [topic/speaker/scripture]`
- Include recent years (2020-2025) for current prophetic counsel
- Also search for classic talks on foundational topics

### 2. For Each Relevant Talk Found

Provide:
- **Title**: Full talk title
- **Speaker**: Name and calling at time of talk
- **Date**: Conference session (e.g., "October 2023 General Conference")
- **Link**: Direct URL to the talk
- **Summary**: 2-3 sentence overview of the talk's message
- **Key Quotes**: 1-2 memorable quotes from the talk
- **Scripture References**: Any scriptures the speaker emphasized

### 3. Synthesis

After listing talks:
- Identify common threads across the talks
- Note any progression in how the topic has been taught
- Highlight particularly powerful or unique perspectives

## Output Format

```markdown
## Conference Talks on [Topic]

### 1. "[Talk Title]"
**Speaker**: [Name], [Calling]
**Date**: [Conference Session]
**Link**: [URL]

**Summary**: [2-3 sentences]

**Key Quote**:
> "[Quote from the talk]"

**Related Scriptures**: [Any scriptures emphasized]

---

### 2. "[Talk Title]"
...

## Common Themes Across Talks
- [Theme 1]
- [Theme 2]

## Recommended Starting Point
[Which talk to read first and why]
```

## After Search

Offer to:
1. Fetch and summarize a specific talk in detail
2. Save a conference talk study to `notes/conference/`
3. Find parallels to Kyle's interests using `/parallels`
4. Study the scriptures referenced using `/study`
5. Compare teachings across multiple talks using `/compare`
