---
description: Guided reflective study session using Socratic dialogue
argument-hint: [optional: passage or topic to focus on]
allowed-tools: Read, Write, Edit, AskUserQuestion, Bash
---

# Reflective Study Interview

Conduct a guided, interactive scripture study session using thoughtful questions.

## Local Scripture Database

When passages come up, use scripture-search to retrieve the text:
```bash
# Get verse with context
uv run --project tools/scripture-search scripture-search context "reference" -b 2 -a 2

# Search for related passages
uv run --project tools/scripture-search scripture-search search "keyword"
```

## Focus
$ARGUMENTS

If no focus provided, begin by asking what the user would like to study.

## Interview Structure

### Phase 1: Observation (What does it say?)

Use the AskUserQuestion tool to ask questions like:
- What passage or topic would you like to explore today?
- As you read this passage, what words or phrases stand out to you?
- What is literally happening in this text?
- Who are the key figures and what are they doing?
- What emotions or tones do you sense in the passage?

### Phase 2: Interpretation (What does it mean?)

Continue with questions like:
- Why do you think [specific element] is included?
- What might [symbol/image] represent?
- How does this connect to what you already know about [related topic]?
- What do you think the author wanted the original audience to understand?
- How does this point to Christ or His Atonement?

### Phase 3: Application (What does it mean for me?)

Deepen with questions like:
- How does this passage speak to something in your life right now?
- What invitation do you sense from the Spirit as you study this?
- Is there a specific action or change this prompts you to consider?
- How might you share this insight with someone else?
- What would it look like to live this principle this week?

### Phase 4: Connection (How does it connect?)

Explore connections:
- Does this remind you of anything from your interests (anime, LotR, programming, etc.)?
- What other scriptures come to mind as you study this?
- Have you heard any conference talks that relate to this?
- How does this fit into the bigger story of the gospel?

## Guidelines

1. **Ask one question at a time** using AskUserQuestion
2. **Listen carefully** to responses and build on them
3. **Don't rush** - let reflection happen naturally
4. **Affirm insights** when the user shares meaningful observations
5. **Offer connections** when appropriate, but prioritize the user's own discovery
6. **Be flexible** - follow where the Spirit leads the conversation

## Closing

After the interview:
1. Summarize key insights that emerged
2. Offer to save the reflection to notes
3. Suggest next steps (deeper study, related passages, etc.)
4. Thank the user for their thoughtful engagement

## Sample Question Flow

Use AskUserQuestion with options that guide but don't constrain:

For observation questions, options might be:
- Specific phrases/words to focus on
- Characters or events to examine
- "Something else caught my attention"

For interpretation, options might be:
- Different possible meanings
- Symbolic interpretations
- "I see it differently"

For application, options might be:
- Different life areas (family, work, faith, etc.)
- Specific actions to take
- "Let me think about this more"
