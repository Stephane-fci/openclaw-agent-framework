#!/usr/bin/env python3
"""
PIL Diagram Rendering Utilities
================================
High-level helpers for generating clean diagrams with Pillow.
Import this module or copy individual functions into your script.

Usage:
    from render import *
    img, d = create_canvas(960, 600)
    fonts = load_fonts()
    draw_box(d, 50, 50, 200, 60, BLUE['fill'], BLUE['stroke'], "My Box", fonts['font_m'])
    img.save("diagram.png")
"""

import math
from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# Color palette — each has 'fill' (light bg) and 'stroke' (dark border/text)
# ---------------------------------------------------------------------------
BLUE   = {"fill": "#dbe4ff", "stroke": "#1971c2"}
GREEN  = {"fill": "#d3f9d8", "stroke": "#2f9e44"}
YELLOW = {"fill": "#fff3bf", "stroke": "#f08c00"}
RED    = {"fill": "#ffe3e3", "stroke": "#e03131"}
PURPLE = {"fill": "#e5dbff", "stroke": "#9c36b5"}
GRAY   = {"fill": "#f1f3f5", "stroke": "#495057"}

# Convenience flat constants
WHITE = "#ffffff"
BLACK = "#212529"
LIGHT_GRAY = "#dee2e6"

# ---------------------------------------------------------------------------
# Font loading
# ---------------------------------------------------------------------------
_FONT_PATHS_BOLD = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",
]
_FONT_PATHS_REGULAR = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/TTF/DejaVuSans.ttf",
]


def _find_font(paths, size):
    """Try each path, fall back to default."""
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()


def load_fonts():
    """Return a dict with font_b (bold/titles), font_m (medium), font_s (small), font_xs (tiny)."""
    return {
        "font_b":  _find_font(_FONT_PATHS_BOLD, 22),
        "font_m":  _find_font(_FONT_PATHS_BOLD, 16),
        "font_s":  _find_font(_FONT_PATHS_REGULAR, 14),
        "font_xs": _find_font(_FONT_PATHS_REGULAR, 11),
    }


# ---------------------------------------------------------------------------
# Canvas
# ---------------------------------------------------------------------------
def create_canvas(width=960, height=600, bg="#ffffff"):
    """Create an Image + ImageDraw pair."""
    img = Image.new("RGB", (width, height), bg)
    d = ImageDraw.Draw(img)
    return img, d


# ---------------------------------------------------------------------------
# Drawing primitives
# ---------------------------------------------------------------------------
def draw_box(d, x, y, w, h, fill="#dbe4ff", outline="#1971c2",
             label="", font=None, text_color=None, radius=8):
    """Draw a rounded rectangle with a centered label."""
    text_color = text_color or outline
    d.rounded_rectangle([x, y, x + w, y + h], radius=radius, fill=fill, outline=outline, width=2)
    if label and font:
        cx = x + w // 2
        cy = y + h // 2
        d.text((cx, cy), label, fill=text_color, font=font, anchor="mm")


def draw_arrow(d, x1, y1, x2, y2, color="#495057", dashed=False, width=2, head_size=10):
    """Draw a line from (x1,y1)→(x2,y2) with an arrowhead at the end."""
    if dashed:
        _draw_dashed_line(d, x1, y1, x2, y2, color, width)
    else:
        d.line([(x1, y1), (x2, y2)], fill=color, width=width)
    # Arrowhead
    angle = math.atan2(y2 - y1, x2 - x1)
    lx = x2 - head_size * math.cos(angle - math.pi / 6)
    ly = y2 - head_size * math.sin(angle - math.pi / 6)
    rx = x2 - head_size * math.cos(angle + math.pi / 6)
    ry = y2 - head_size * math.sin(angle + math.pi / 6)
    d.polygon([(x2, y2), (lx, ly), (rx, ry)], fill=color)


def _draw_dashed_line(d, x1, y1, x2, y2, color, width, dash_len=10, gap_len=6):
    """Draw a dashed line between two points."""
    dx = x2 - x1
    dy = y2 - y1
    length = math.hypot(dx, dy)
    if length == 0:
        return
    ux, uy = dx / length, dy / length
    pos = 0
    while pos < length:
        end = min(pos + dash_len, length)
        sx, sy = x1 + ux * pos, y1 + uy * pos
        ex, ey = x1 + ux * end, y1 + uy * end
        d.line([(sx, sy), (ex, ey)], fill=color, width=width)
        pos = end + gap_len


def draw_container(d, x, y, w, h, title="", fill="#f1f3f5", outline="#495057",
                   font=None, text_color=None, radius=10):
    """Draw a container box with a title bar at the top."""
    text_color = text_color or outline
    d.rounded_rectangle([x, y, x + w, y + h], radius=radius, fill=fill, outline=outline, width=2)
    if title and font:
        d.text((x + 12, y + 10), title, fill=text_color, font=font, anchor="lt")
        # Divider line below title
        title_bottom = y + 34
        d.line([(x, title_bottom), (x + w, title_bottom)], fill=outline, width=1)


def draw_badge(d, x, y, text, fill="#d3f9d8", outline="#2f9e44", font=None, text_color=None):
    """Draw a small status badge (pill shape)."""
    text_color = text_color or outline
    if font is None:
        font = _find_font(_FONT_PATHS_REGULAR, 11)
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    pw, ph = 12, 4  # padding
    w = tw + pw * 2
    h = th + ph * 2
    d.rounded_rectangle([x, y, x + w, y + h], radius=h // 2, fill=fill, outline=outline, width=1)
    d.text((x + pw, y + ph), text, fill=text_color, font=font, anchor="lt")
    return w, h


def draw_divider(d, y, width=960, pad=30, color="#dee2e6", label="", font=None):
    """Draw a horizontal divider line, optionally with a centered label."""
    d.line([(pad, y), (width - pad, y)], fill=color, width=1)
    if label and font:
        d.text((width // 2, y - 10), label, fill="#868e96", font=font, anchor="mb")


# ---------------------------------------------------------------------------
# Text helpers
# ---------------------------------------------------------------------------
def text_width(font, text):
    """Get pixel width of text string."""
    bbox = font.getbbox(text)
    return bbox[2] - bbox[0]


def wrap_text(text, font, max_width):
    """Word-wrap text to fit within max_width pixels. Returns list of lines."""
    words = text.split()
    lines, current = [], ""
    for word in words:
        test = f"{current} {word}".strip()
        if text_width(font, test) <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines or [""]
