#!/usr/bin/env python3
"""Inject the shared sketch.js library + handwriting fonts into every HTML page.

What this adds to each page, idempotently:
  1. A <script defer src="{root}js/sketch.js"></script> tag right before </head>
  2. Kalam + Caveat to the Google Fonts URL so every page can render sketches
     without adding a per-page link tag.
"""
import re
from pathlib import Path

ROOT = Path("/Users/ble/Desktop/sams site")
MARKER = "sketch.js"
FONT_MARKER = "Kalam"

def rel_prefix(html_path: Path) -> str:
    rel = html_path.relative_to(ROOT)
    depth = len(rel.parts) - 1
    return "../" * depth

scanned = 0
patched = 0

for html in ROOT.rglob("*.html"):
    scanned += 1
    text = html.read_text(encoding="utf-8")
    orig = text

    # 1. Fonts: add Kalam and Caveat to the Google Fonts URL if not present.
    if FONT_MARKER not in text:
        # Patch any Google Fonts CSS2 URL to include Kalam + Caveat
        def add_families(m):
            url = m.group(0)
            if 'family=Kalam' in url:
                return url
            # Append &family=Kalam:wght@400;700&family=Caveat:wght@500;700 before &display or closing
            if '&display=' in url:
                return url.replace('&display=',
                    '&family=Kalam:wght@400;700&family=Caveat:wght@500;700&display=')
            if url.endswith('"') or url.endswith("'"):
                # URL inside a quoted attribute - insert before closing quote
                q = url[-1]
                return url[:-1] + '&family=Kalam:wght@400;700&family=Caveat:wght@500;700' + q
            return url + '&family=Kalam:wght@400;700&family=Caveat:wght@500;700'

        text = re.sub(
            r'https://fonts\.googleapis\.com/css2\?[^"\'\s>]+',
            add_families,
            text,
            count=1,
        )

    # 2. Script: inject <script defer src="...js/sketch.js"></script> before </head>
    if MARKER not in text:
        R = rel_prefix(html)
        tag = f'<script defer src="{R}js/sketch.js"></script>\n'
        if '</head>' in text:
            text = text.replace('</head>', tag + '</head>', 1)

    if text != orig:
        html.write_text(text, encoding="utf-8")
        patched += 1

print(f"Scanned {scanned} pages, patched {patched}")
