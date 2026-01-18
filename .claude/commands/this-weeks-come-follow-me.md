---
description: Get this week's Come Follow Me scripture readings based on the current date
argument-hint: [optional: "next week" or "upcoming"]
allowed-tools: Read, Bash, Write, Edit, WebSearch
---

# This Week's Come Follow Me

Look up the current week's Come Follow Me scripture readings for 2026 (Old Testament).

## Date Logic

Today's date determines which week to show:

1. **Read the schedule** from `data/cfm-2026-schedule.json`
2. **Determine the current week**:
   - Find the week where today's date falls between `start_date` and `end_date`
   - **If today is Sunday**: Default to showing the week that just ended (the past 7 days of study) UNLESS the user says "next week" or "upcoming"
   - If the user says "next week" or "upcoming" in their request, show the following week instead
3. **Handle edge cases**:
   - If before the schedule starts (before Dec 29, 2025), show Week 1
   - If after the schedule ends (after Dec 27, 2026), show Week 52

## User Arguments

Check `$ARGUMENTS` for modifiers:
- If contains "next" or "upcoming" or "next week": Show the NEXT week's readings
- Otherwise: Show the current week (on Sunday, the week just completed)

## Output Format

Present the week's information clearly:

```
## Come Follow Me: [Week Title]

**Week [#]** | [Start Date] - [End Date]

### Scripture Readings
- [List each reading]

### Theme
[The theme/focus of this week's study]

---

**Ready to study?** Here are some options:
- `/study [specific passage]` - Deep dive into a passage
- `/themes [topic from readings]` - Explore themes
- `/meaningful-questions [passage]` - Generate thought-provoking questions
```

## Local Scripture Database

After showing the week, offer to pull up scripture text using the local database:

```bash
# Get a chapter
uv run --project tools/scripture-search scripture-search chapter Genesis 1

# Get a specific verse
uv run --project tools/scripture-search scripture-search verse "Genesis 1:1"
```

## Implementation

1. Read the JSON schedule file
2. Parse today's date and find the matching week
3. Apply Sunday logic and user arguments
4. Display the week information
5. Offer to begin studying with other commands
