---
description: Generate difficult, thought-provoking questions that challenge assumptions and invite deep wrestling with scripture
argument-hint: [passage or topic] (e.g., "Genesis 22" or "divine justice" or "Nephi killing Laban")
allowed-tools: Read, Write, Edit, WebSearch, WebFetch, Bash
---

# Meaningful Questions

Generate challenging questions about: **$ARGUMENTS**

## Local Scripture Database

Use the local scripture search tool to retrieve passages:
```bash
# Get a chapter for context
uv run --project tools/scripture-search scripture-search chapter Genesis 22

# Search for related passages
uv run --project tools/scripture-search scripture-search search "sacrifice Isaac"

# Get verse with surrounding context
uv run --project tools/scripture-search scripture-search context "1 Nephi 4:10" -b 3 -a 3
```

## Purpose

These are NOT Sunday School questions with easy answers. These are questions designed to:
- Challenge comfortable assumptions
- Surface tensions and paradoxes in the text
- Force genuine wrestling with difficult concepts
- Invite introspection that might be uncomfortable
- Explore implications we'd rather avoid
- Push beyond surface-level understanding

## Question Generation Process

### 1. Understand the Source Material
If a scripture reference is provided, retrieve the text. Identify what makes this passage difficult, controversial, or easily glossed over.

### 2. Generate Questions in These Categories

#### Theological Tensions
Questions that probe apparent contradictions or difficult doctrines:
- Where does this passage seem to conflict with other scriptures or principles?
- What does this imply about God's character that might be uncomfortable?
- How does this challenge popular or comfortable interpretations?

#### Moral Complexity
Questions that resist easy ethical answers:
- If you were in this situation, what would you actually do (not what you'd like to think you'd do)?
- What moral compromises does this narrative seem to accept or require?
- How do we reconcile this with modern ethical sensibilities—and should we?

#### Personal Confrontation
Questions that turn the mirror on the reader:
- Where have you failed to live this principle, and why?
- What excuse do you make for yourself that this passage won't allow?
- What would change in your life if you took this seriously?

#### Uncomfortable Implications
Questions about what the text demands if taken at face value:
- What does this passage require that you're not willing to give?
- What would it cost you to actually believe this?
- What comfortable belief does this undermine?

#### Wrestling with God
Questions about divine action and theodicy:
- Why would God allow/command/do this?
- What does this reveal about how God operates that's hard to accept?
- How do you reconcile this with a loving God?

#### Interpretive Honesty
Questions about our own reading:
- Are you reading this passage honestly, or finding ways to soften it?
- What are you importing into this text that isn't there?
- What would this mean if your preferred interpretation is wrong?

### 3. Format the Questions

Generate **8-12 questions** total across categories. Each question should:
- Be specific to the passage/topic, not generic
- Have no easy or obvious answer
- Require actual thought, not just recall
- Potentially change how the reader sees the text or themselves

## Output Format

```markdown
# Meaningful Questions: [Topic/Passage]

## The Difficult Core
[1-2 sentences identifying what makes this genuinely hard to grapple with]

## Questions to Wrestle With

### On the Text Itself
1. [Question]
2. [Question]

### On God's Character/Actions
3. [Question]
4. [Question]

### On Your Life
5. [Question]
6. [Question]

### On Your Assumptions
7. [Question]
8. [Question]

## Going Deeper
For each question, you might:
- Use `/study` to dig into the passage more thoroughly
- Use `/conference` to see how prophets have addressed this
- Use `/compare` to see how other scriptures speak to this tension
- Use `/interview` to work through your thoughts in dialogue
- Use `/parallels` to find connections in literature/life that illuminate the question
```

## Tone

Be direct. Don't hedge with "some might ask" or "it could be interesting to consider." Ask the hard question plainly. These questions should feel slightly uncomfortable—if they don't, they're not meaningful enough.

Avoid:
- Questions with obvious "right" answers
- Questions that affirm what the reader already believes
- Questions that can be answered with a scripture mastery verse
- Rhetorical questions that are really statements
- Questions that let the reader off the hook

Embrace:
- Questions that linger
- Questions you'd be nervous to discuss in a church setting
- Questions that require humility to engage honestly
- Questions that might change someone
