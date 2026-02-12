---
name: pil-diagrams
description: "Generate visual diagrams (flowcharts, architecture, workflows, comparisons) as PNG images using Python PIL/Pillow. No browser or external tools needed. Use when the user needs a visual explanation of a concept, workflow, or system."
---

# PIL Diagram Generation

Generate clean, professional diagrams as PNG images using Python Pillow. Works on any system with Python + Pillow installed. No browser, no external rendering tools.

## Prerequisites

```bash
pip install Pillow  # Usually pre-installed on most systems
```

Verify: `python3 -c "from PIL import Image; print('OK')"`

## Quick Start

```python
from PIL import Image, ImageDraw, ImageFont

# 1. Create canvas (960px wide fits Discord/mobile perfectly)
img = Image.new('RGB', (960, 400), '#ffffff')
d = ImageDraw.Draw(img)

# 2. Load fonts
font_b = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
font_m = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
font_s = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
font_xs = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)

# 3. Draw stuff
d.text((480, 20), "My Diagram", fill='#1e1e1e', font=font_b, anchor='mt')
d.rectangle([50, 60, 250, 120], fill='#d3f9d8', outline='#2f9e44', width=2)
d.text((150, 90), "Step 1", fill='#2f9e44', font=font_m, anchor='mm')

# 4. Save
img.save('/path/to/output.png', 'PNG')
```

## Color Palette

Use these consistently. Each has a light fill + dark stroke.

| Name | Fill (background) | Stroke (border/text) | Use for |
|------|-------------------|---------------------|---------|
| **Green** | `#d3f9d8` | `#2f9e44` | Live, active, success, done |
| **Yellow** | `#fff3bf` | `#f08c00` | Dev, in-progress, warning |
| **Red** | `#ffe3e3` | `#e03131` | Danger, critical, publish, blocked |
| **Blue** | `#dbe4ff` | `#1971c2` | Info, agents, processes |
| **Purple** | `#e5dbff` | `#9c36b5` | Preview, special |
| **Gray** | `#f1f3f5` | `#495057` | Neutral, containers |

Lighter background variants for large containers:

| Color | Container fill (30% opacity feel) |
|-------|----------------------------------|
| Blue container | `#edf5ff` |
| Gray container | `#f8f9fa` |
| Green container | `#ebfbee` |

Text colors: `#1e1e1e` (dark), `#495057` (medium), `#868e96` (light/subtle), `#666666` (muted).

## Font Loading (Robust)

Always try DejaVu (standard on Linux), fall back to default:

```python
def load_font(bold=False, size=14):
    paths = [
        f"/usr/share/fonts/truetype/dejavu/DejaVuSans{'-Bold' if bold else ''}.ttf",
        f"/usr/share/fonts/TTF/DejaVuSans{'-Bold' if bold else ''}.ttf",
    ]
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()

font_b  = load_font(bold=True, size=22)   # Titles
font_m  = load_font(bold=True, size=16)   # Section headers, box labels
font_s  = load_font(bold=False, size=14)  # Body text
font_xs = load_font(bold=False, size=11)  # Small notes, subtle text
```

## Drawing Elements

### Labeled Box

```python
# Basic box with centered label
x, y, w, h = 50, 100, 280, 70
d.rectangle([x, y, x+w, y+h], fill='#d3f9d8', outline='#2f9e44', width=2)
d.text((x + w//2, y + h//2), "My Label", fill='#2f9e44', font=font_m, anchor='mm')
```

### Multi-line Box

```python
x, y, w, h = 50, 100, 280, 90
d.rectangle([x, y, x+w, y+h], fill='#dbe4ff', outline='#1971c2', width=2)
d.text((x + w//2, y + 18), "Title", fill='#1971c2', font=font_m, anchor='mt')
d.text((x + w//2, y + 40), "Subtitle line", fill='#1e1e1e', font=font_s, anchor='mt')
d.text((x + w//2, y + 60), "Small detail", fill='#666666', font=font_xs, anchor='mt')
```

### Container Box (with title)

```python
# Large container that holds other elements
d.rectangle([30, 80, 430, 500], fill='#edf5ff', outline='#1971c2', width=2)
d.text((230, 95), "SECTION NAME", fill='#1971c2', font=font_m, anchor='mt')
# Then draw child boxes inside at higher y values
```

### Solid Arrow

```python
import math

def draw_arrow(d, x1, y1, x2, y2, color='#495057', width=2, head=10):
    d.line([(x1, y1), (x2, y2)], fill=color, width=width)
    angle = math.atan2(y2 - y1, x2 - x1)
    lx = x2 - head * math.cos(angle - math.pi/6)
    ly = y2 - head * math.sin(angle - math.pi/6)
    rx = x2 - head * math.cos(angle + math.pi/6)
    ry = y2 - head * math.sin(angle + math.pi/6)
    d.polygon([(x2, y2), (lx, ly), (rx, ry)], fill=color)

# Usage: horizontal arrow
draw_arrow(d, 300, 150, 500, 150, color='#2f9e44')
# Vertical arrow
draw_arrow(d, 200, 200, 200, 300, color='#e03131')
```

### Dashed Arrow

```python
def draw_dashed_line(d, x1, y1, x2, y2, color, width=2, dash=10, gap=6):
    dx, dy = x2 - x1, y2 - y1
    length = math.hypot(dx, dy)
    if length == 0: return
    ux, uy = dx/length, dy/length
    pos = 0
    while pos < length:
        end = min(pos + dash, length)
        d.line([(x1 + ux*pos, y1 + uy*pos), (x1 + ux*end, y1 + uy*end)], fill=color, width=width)
        pos = end + gap

# Draw dashed line + arrowhead
draw_dashed_line(d, 200, 300, 200, 400, '#9c36b5')
# Add arrowhead manually at endpoint
d.polygon([(195, 395), (200, 405), (205, 395)], fill='#9c36b5')
```

### Bidirectional Sync Arrow

```python
# Line
d.line([(390, 150), (570, 150)], fill='#2f9e44', width=2)
# Right arrowhead
d.polygon([(560, 145), (570, 150), (560, 155)], fill='#2f9e44')
# Left arrowhead
d.polygon([(400, 145), (390, 150), (400, 155)], fill='#2f9e44')
# Label
d.text((480, 138), "auto-sync", fill='#2f9e44', font=font_xs, anchor='mt')
```

### Status Badge

```python
# Small colored pill
text = "LIVE"
bbox = font_xs.getbbox(text)
tw = bbox[2] - bbox[0]
px, py = 8, 3  # padding
bx, by = 100, 50
d.rounded_rectangle([bx, by, bx + tw + px*2, by + 18], radius=9, fill='#d3f9d8', outline='#2f9e44')
d.text((bx + px, by + py), text, fill='#2f9e44', font=font_xs)
```

## Text Anchors

PIL text anchors save you from manual centering math:

| Anchor | Meaning | Use for |
|--------|---------|---------|
| `'mt'` | Middle-top | Center-aligned titles, headings |
| `'mm'` | Middle-middle | Text centered inside a box |
| `'lt'` | Left-top | Left-aligned body text, lists |
| `'mb'` | Middle-bottom | Labels above a line |

```python
d.text((x, y), "Centered title", font=font_b, anchor='mt')   # x is center point
d.text((x, y), "Left aligned", font=font_s, anchor='lt')       # x is left edge
d.text((cx, cy), "Box label", font=font_m, anchor='mm')        # cx,cy is box center
```

## Layout Guidelines

| Setting | Value | Why |
|---------|-------|-----|
| Canvas width | **960px** | Fits Discord embeds, mobile screens |
| Canvas height | Calculate based on content | Don't hardcode — measure your elements |
| Side padding | **30px** | Breathing room from edges |
| Container padding | **15-20px** inside containers | Space between container edge and children |
| Element gap | **20-30px** between boxes | Readable spacing |
| Section gap | **40-50px** between sections | Clear visual separation |

## Complete Example: Workflow Diagram

```python
from PIL import Image, ImageDraw, ImageFont
import math

W, H = 960, 500
img = Image.new('RGB', (W, H), '#ffffff')
d = ImageDraw.Draw(img)

# Fonts
fb = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
fm = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
fs = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
fxs = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)

# Title
d.text((W//2, 20), "Deployment Workflow", fill='#1e1e1e', font=fb, anchor='mt')

# Step boxes
steps = [
    ("1. Build", "#dbe4ff", "#1971c2"),
    ("2. Test", "#fff3bf", "#f08c00"),
    ("3. Review", "#e5dbff", "#9c36b5"),
    ("4. Deploy", "#d3f9d8", "#2f9e44"),
]

bw, bh = 180, 70
start_x = 60
y = 80

for i, (label, fill, stroke) in enumerate(steps):
    x = start_x + i * 220
    d.rectangle([x, y, x+bw, y+bh], fill=fill, outline=stroke, width=2)
    d.text((x + bw//2, y + bh//2), label, fill=stroke, font=fm, anchor='mm')
    
    # Arrow to next step
    if i < len(steps) - 1:
        ax1, ax2 = x + bw + 5, x + 220 - 5
        ay = y + bh//2
        d.line([(ax1, ay), (ax2, ay)], fill='#495057', width=2)
        d.polygon([(ax2-8, ay-5), (ax2, ay), (ax2-8, ay+5)], fill='#495057')

# Description area
d.text((60, 180), "Details for each step:", fill='#1e1e1e', font=fm, anchor='lt')
details = [
    "Build — Agent generates code and pushes to feature branch",
    "Test — Changes appear on dev theme (invisible to customers)",
    "Review — Share preview URL with team for approval",
    "Deploy — Merge to main, auto-deploys to live site",
]
for i, detail in enumerate(details):
    d.text((60, 210 + i*24), detail, fill='#495057', font=fs, anchor='lt')

img.save('/tmp/workflow.png', 'PNG')
```

## Complete Example: Side-by-Side Comparison

```python
W, H = 960, 400
img = Image.new('RGB', (W, H), '#ffffff')
d = ImageDraw.Draw(img)

d.text((W//2, 20), "Option A vs Option B", fill='#1e1e1e', font=fb, anchor='mt')

# Left side
d.rectangle([30, 60, 460, 360], fill='#ebfbee', outline='#2f9e44', width=2)
d.text((245, 75), "Option A: GitHub Integration", fill='#2f9e44', font=fm, anchor='mt')
pros_a = ["+ Full version history", "+ Branch-based workflow", "+ Auto-sync both ways", "+ Familiar PR review"]
for i, p in enumerate(pros_a):
    d.text((50, 110 + i*28), p, fill='#333', font=fs, anchor='lt')

# Right side
d.rectangle([500, 60, 930, 360], fill='#fff3bf', outline='#f08c00', width=2)
d.text((715, 75), "Option B: API Only", fill='#f08c00', font=fm, anchor='mt')
pros_b = ["+ Simpler setup", "+ No GitHub app needed", "+ Direct API control", "+ Works immediately"]
for i, p in enumerate(pros_b):
    d.text((520, 110 + i*28), p, fill='#333', font=fs, anchor='lt')

img.save('/tmp/comparison.png', 'PNG')
```

## Sending the Diagram

After generating the PNG, send it using the message tool:

```python
img.save('/root/clawd/projects/my-project/diagram.png', 'PNG')
```

Then:
```
message(action="send", channel="discord", target="CHANNEL_ID", 
        message="Here's the diagram:", filePath="/root/clawd/projects/my-project/diagram.png")
```

## Helper Script

An optional `render.py` helper is included in this skill folder with reusable functions:
- `create_canvas(width, height, bg)` → Image + ImageDraw
- `load_fonts()` → dict of font sizes
- `draw_box(d, x, y, w, h, fill, outline, label, font)` — labeled box
- `draw_arrow(d, x1, y1, x2, y2, color, dashed, width)` — arrow with arrowhead
- `draw_container(d, x, y, w, h, title, fill, outline)` — container with title
- `draw_badge(d, x, y, text, fill, outline)` — status pill
- `draw_divider(d, y, width, label)` — horizontal separator
- Color constants: `BLUE`, `GREEN`, `YELLOW`, `RED`, `PURPLE`, `GRAY`

To use it, copy to your workspace or import directly:
```python
import sys; sys.path.insert(0, '/path/to/skills/pil-diagrams')
from render import *
```

## Tips

1. **Plan the layout on paper first** — Know what boxes go where before coding
2. **Calculate height dynamically** — Count your elements, multiply by spacing
3. **Use containers to group** — A light background box around related items
4. **Color = meaning** — Green for good, red for danger, yellow for caution
5. **Less is more** — Don't cram everything in. Whitespace is your friend.
6. **Test locally** — Generate, look at the image, adjust coordinates, regenerate
