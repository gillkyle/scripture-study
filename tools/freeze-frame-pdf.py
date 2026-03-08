from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT

OUT = "/home/user/scripture-study/notes/old-testament/freeze-frame-game.pdf"

# Colors
NAVY   = HexColor("#1e3a5f")
GOLD   = HexColor("#c9a84c")
CREAM  = HexColor("#fdf8f0")
LIGHT  = HexColor("#eaf0f8")
STRIPE = HexColor("#d6e4f0")

doc = SimpleDocTemplate(
    OUT,
    pagesize=letter,
    leftMargin=0.75*inch,
    rightMargin=0.75*inch,
    topMargin=0.75*inch,
    bottomMargin=0.75*inch,
)

styles = getSampleStyleSheet()

def style(name, **kw):
    s = styles[name].clone(name + str(id(kw)))
    for k, v in kw.items():
        setattr(s, k, v)
    return s

title_s    = style("Title",     fontSize=22, textColor=NAVY,  spaceAfter=2,  fontName="Helvetica-Bold", alignment=TA_CENTER)
subtitle_s = style("Normal",    fontSize=11, textColor=GOLD,  spaceAfter=6,  fontName="Helvetica-BoldOblique", alignment=TA_CENTER)
h2_s       = style("Heading2",  fontSize=14, textColor=white, spaceAfter=4,  fontName="Helvetica-Bold", spaceBefore=12)
summary_s  = style("Normal",    fontSize=9.5, textColor=HexColor("#333333"), spaceAfter=6, leading=14, fontName="Helvetica")
label_s    = style("Normal",    fontSize=8,  textColor=NAVY, fontName="Helvetica-Bold", leading=11)
tip_s      = style("Normal",    fontSize=9,  textColor=HexColor("#444444"), fontName="Helvetica-Oblique", leading=13, leftIndent=8)
how_s      = style("Normal",    fontSize=9.5, textColor=HexColor("#222222"), leading=14, fontName="Helvetica", leftIndent=6)
footer_s   = style("Normal",    fontSize=8,  textColor=HexColor("#888888"), alignment=TA_CENTER, fontName="Helvetica-Oblique")

def section_header(text):
    """Colored banner for each story section."""
    data = [[Paragraph(text, h2_s)]]
    t = Table(data, colWidths=[7*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0,0), (-1,-1), NAVY),
        ("TOPPADDING",  (0,0), (-1,-1), 6),
        ("BOTTOMPADDING",(0,0),(-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
    ]))
    return t

def freeze_table(rows):
    """Table with alternating row colors: Moment | Call-out | Emotion."""
    header = [
        Paragraph("MOMENT IN THE STORY", label_s),
        Paragraph("CALL OUT TO CLASS", label_s),
        Paragraph("EXPECTED EMOTION", label_s),
    ]
    table_data = [header] + [
        [Paragraph(a, summary_s), Paragraph(b, summary_s), Paragraph(c, summary_s)]
        for a, b, c in rows
    ]
    col_w = [2.6*inch, 2.6*inch, 1.8*inch]
    t = Table(table_data, colWidths=col_w)
    ts = TableStyle([
        # Header row
        ("BACKGROUND",    (0,0), (-1,0), LIGHT),
        ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",      (0,0), (-1,0), 8),
        ("BOTTOMPADDING", (0,0), (-1,0), 6),
        ("TOPPADDING",    (0,0), (-1,0), 6),
        # Alternating body rows
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [white, STRIPE]),
        ("FONTSIZE",      (0,1), (-1,-1), 9),
        ("TOPPADDING",    (0,1), (-1,-1), 5),
        ("BOTTOMPADDING", (0,1), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 7),
        ("RIGHTPADDING",  (0,0), (-1,-1), 7),
        # Borders
        ("LINEBELOW",     (0,0), (-1,0), 1.5, NAVY),
        ("LINEBELOW",     (0,-1),(-1,-1), 0.5, HexColor("#cccccc")),
        ("INNERGRID",     (0,1), (-1,-1), 0.3, HexColor("#dddddd")),
        ("BOX",           (0,0), (-1,-1), 1,   NAVY),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
    ])
    t.setStyle(ts)
    return t

story1_rows = [
    (
        "The servant is alone in the desert, not sure if his prayer will work",
        '"Freeze — you\'re the servant, waiting and hoping. What\'s on your face?"',
        "Nervous, hopeful",
    ),
    (
        "Rebekah shows up and starts drawing water for the camels without being asked",
        '"Freeze — you\'re Rebekah, working hard to be kind. What\'s on your face?"',
        "Cheerful, determined",
    ),
    (
        "The servant realizes his prayer was already being answered",
        '"Freeze — you\'re the servant and you can\'t believe it. What\'s on your face?"',
        "Amazed, grateful",
    ),
    (
        "Rebekah\'s family asks: \"Will you leave home and go with this stranger?\"",
        '"Freeze — you\'re Rebekah. Everyone is waiting. What\'s on your face?"',
        "Brave, a little scared",
    ),
]

story2_rows = [
    (
        "Esau walks in starving after a long hunt and sees — and smells — the soup",
        '"Freeze — you\'re Esau and that soup smells amazing. What\'s on your face?"',
        "Hungry, desperate",
    ),
    (
        "Jacob says, \"I\'ll give you soup — if you give me your birthright\"",
        '"Freeze — you\'re Esau. That\'s a weird trade. What\'s on your face?"',
        "Confused, dismissive",
    ),
    (
        "Isaac feels Jacob\'s goat-skin arms and isn\'t quite sure who he\'s talking to",
        '"Freeze — you\'re Isaac, you\'re suspicious something is off. What\'s on your face?"',
        "Puzzled, uncertain",
    ),
    (
        "Esau comes in after the blessing is already given away and finds out",
        '"Freeze — you\'re Esau. The blessing is gone. What\'s on your face?"',
        "Heartbroken, furious",
    ),
    (
        "Jacob has to pack up and run away from home",
        '"Freeze — you got the blessing, but now you\'re leaving everything. What\'s on your face?"',
        "Guilty, scared",
    ),
]

story3_rows = [
    (
        "Jacob is alone in the dark desert, lying down on rocks with nothing",
        '"Freeze — it\'s cold and dark and you\'re by yourself. What\'s on your face?"',
        "Lonely, scared",
    ),
    (
        "He sees the ladder stretching all the way to heaven with angels on it",
        '"Freeze — you\'re Jacob and you can\'t believe what you\'re seeing. What\'s on your face?"',
        "Awestruck, wide-eyed",
    ),
    (
        "God speaks: \"I am with you everywhere you go\"",
        '"Freeze — God just told you He\'s been watching over you this whole time. What\'s on your face?"',
        "Relieved, peaceful",
    ),
    (
        "Jacob wakes up: \"God was HERE — and I didn\'t even know it!\"",
        '"Freeze — you\'re Jacob, just waking up. What\'s on your face?"',
        "Surprised, joyful",
    ),
]

tip_items = [
    "<b>Keep freezes short</b> — 3–5 seconds, then keep the story moving. Energy lives in the momentum.",
    "<b>Mirror them back</b> — \"I see some surprised faces — that\'s exactly how Jacob felt!\"",
    "<b>Older kids (8–11):</b> Ask them to name the emotion in one word instead of just making a face.",
    "<b>Sunbeams (ages 3–4):</b> Pick just one freeze per story — the most dramatic moment. Don\'t over-stop.",
]

story_blocks = [
    (
        "Story 1 — Rebekah at the Well  (Genesis 24)",
        "A servant travels to find a wife for Isaac. He prays at a well for a sign: "
        "whoever offers water to him AND his camels unprompted will be the one. "
        "Before he finishes praying, Rebekah arrives, draws water, and volunteers for the camels herself. "
        "When her family asks if she\'ll leave home to marry a stranger, she simply says: \"I will go.\"",
        story1_rows,
    ),
    (
        "Story 2 — Two Brothers, One Very Bad Trade  (Genesis 25 & 27)",
        "Esau (firstborn hunter) and Jacob (homebody cook) are twins. One day Esau comes home "
        "starving and trades his birthright — his sacred spiritual inheritance — for a bowl of Jacob\'s soup. "
        "Later, Jacob and Rebekah scheme to trick the blind Isaac into giving Jacob the formal family blessing. "
        "It works — but Esau is devastated, and Jacob has to flee his home, never seeing his mother again.",
        story2_rows,
    ),
    (
        "Story 3 — Jacob\'s Ladder  (Genesis 28)",
        "Jacob is alone in the desert at night — no tent, no bed, just a rock for a pillow. "
        "He dreams of a ladder reaching from earth to heaven with angels going up and down. "
        "God speaks at the top: \"I am with you. I will keep you everywhere you go.\" "
        "Jacob wakes astonished, stands up his rock as a monument, names the place Beth-el (House of God), "
        "and makes a covenant with the Lord.",
        story3_rows,
    ),
]

# ── Build story ──────────────────────────────────────────────────────────────
story = []

# Title block
story.append(Paragraph("Freeze Frame Game", title_s))
story.append(Paragraph("Jacob, Esau &amp; Rebekah  ·  Primary Lesson  ·  Genesis 24–33", subtitle_s))
story.append(HRFlowable(width="100%", thickness=2, color=GOLD, spaceAfter=8))

# How it works
story.append(Paragraph(
    "<b>How it works:</b>  Pause mid-story and call \"FREEZE!\". Name the character and ask kids to make "
    "a face showing how that character feels. Hold for 3–5 seconds, then continue. Quick, no wrong answers.",
    how_s
))
story.append(Spacer(1, 10))

# Story blocks
for title, summary, rows in story_blocks:
    story.append(section_header(title))
    story.append(Spacer(1, 6))
    story.append(Paragraph(summary, summary_s))
    story.append(Spacer(1, 4))
    story.append(freeze_table(rows))
    story.append(Spacer(1, 10))

# Tips
story.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceBefore=4, spaceAfter=8))
story.append(Paragraph("<b>Tips for Running It</b>", style("Normal", fontSize=11, textColor=NAVY, fontName="Helvetica-Bold", spaceAfter=6)))
for tip in tip_items:
    story.append(Paragraph(f"• {tip}", tip_s))
    story.append(Spacer(1, 3))

story.append(Spacer(1, 12))
story.append(Paragraph("Come Follow Me 2026 — Week 10  ·  \"Let God Prevail\"", footer_s))

doc.build(story)
print(f"PDF written to {OUT}")
