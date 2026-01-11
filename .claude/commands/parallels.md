---
description: Find parallels between scripture/gospel topics and personal interests
argument-hint: [topic or passage] (e.g., "repentance" or "Alma 36")
allowed-tools: Read, Write, Edit, WebSearch, Bash
---

# Interest Parallels

Find meaningful connections between **$ARGUMENTS** and Kyle's interests.

## Local Scripture Database

Use the local scripture search tool to retrieve scripture passages:
```bash
# Get a chapter
uv run --project tools/scripture-search scripture-search chapter Alma 36

# Search for related verses
uv run --project tools/scripture-search scripture-search search "repentance"

# Get verse with context
uv run --project tools/scripture-search scripture-search context "Alma 36:17" -b 2 -a 2
```

## Kyle's Interest Areas

Draw parallels from these domains:

### Anime & Manga
Consider connections to:
- **Character Arcs**: Zuko (Avatar), Vegeta (DBZ), Eren (Attack on Titan), characters who undergo transformation
- **Redemption Stories**: Characters who fall and rise again
- **Sacrifice Themes**: Fullmetal Alchemist's equivalent exchange vs. grace, characters who give everything
- **Bonds & Loyalty**: Naruto's friendships, One Piece's nakama, the power of connection
- **Becoming Greater**: Training arcs, unlocking potential, surpassing limits
- **Light vs. Dark**: The battle between good and evil, inner demons

### Lord of the Rings / Tolkien
Consider connections to:
- **Providence**: Eucatastrophe, unexpected deliverance, "meant to find the Ring"
- **Power & Corruption**: The Ring's temptation, Boromir's fall
- **Mercy**: Bilbo/Frodo sparing Gollum, consequences of mercy
- **Small Things**: Hobbits accomplishing what the great could not
- **Fellowship**: The importance of companions on the journey
- **Hope & Despair**: Sam's speech about stories worth telling
- **Sacrifice**: Frodo bearing the Ring, Gandalf facing the Balrog

### Programming & Code
Consider connections to:
- **Debugging as Repentance**: Finding errors, root cause analysis, fixing at the source
- **Refactoring as Sanctification**: Improving without changing purpose
- **Version Control**: The Atonement as ultimate "undo," branches and merges in life choices
- **Design Patterns**: Recurring solutions as gospel principles
- **Tests as Covenants**: Defining expected behavior, catching regressions
- **Clean Code**: Clarity, simplicity, removing cruft
- **Technical Debt**: Unresolved sins accumulating interest
- **Compilation**: Transformation from source to executable

### Literature & Poetry
Consider connections to:
- Classic works with similar themes
- Poetic and literary devices
- The hero's journey structure
- Symbolism and allegory
- Storytelling as teaching method

### Science & Nature
Consider connections to:
- Natural laws reflecting divine law
- Patterns in creation (fractals, Fibonacci, etc.)
- Ecological interdependence
- Light, water, and other natural symbols
- Cosmological wonder and testimony

## Output Format

For each relevant interest area:

```markdown
## [Interest Area] Parallels

### Connection: [Brief Title]

**Gospel Principle/Scripture**: [What you're connecting from]

**Parallel**: [The connection from the interest area]

**Why This Works**: [Explanation of how this illuminates the gospel concept]

**Reflection**: [A thought-provoking question or insight]
```

Provide at least 2-3 parallels from different interest areas. Go deep rather than broad - a single profound connection is better than many surface-level ones.

## Closing

After presenting parallels, offer to:
1. Save these connections to `notes/parallels/`
2. Explore the original passage deeper with `/study`
3. Find what prophets have said with `/conference`
4. Write up a more detailed essay on one parallel
