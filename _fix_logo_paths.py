#!/usr/bin/env python3
"""Fix broken relative paths to logo.png across all HTML pages."""
import re
from pathlib import Path

ROOT = Path("/Users/ble/Desktop/sams site")

def correct_depth(html_path: Path) -> int:
    """Count how many directory levels deep the file sits from ROOT."""
    rel = html_path.relative_to(ROOT)
    # parts includes filename; drop it
    return len(rel.parts) - 1

fixed = 0
scanned = 0
for html in ROOT.rglob("*.html"):
    scanned += 1
    depth = correct_depth(html)
    prefix = "../" * depth if depth > 0 else ""
    expected = f"{prefix}logo.png"

    text = html.read_text(encoding="utf-8")
    orig = text

    # Fix favicon: <link rel="icon" ... href="...logo.png">
    text = re.sub(
        r'(<link rel="icon"[^>]*href=")[^"]*logo\.png(")',
        lambda m: f'{m.group(1)}{expected}{m.group(2)}',
        text,
    )

    # Fix brand-logo img src
    text = re.sub(
        r'(<img class="brand-logo"[^>]*src=")[^"]*logo\.png(")',
        lambda m: f'{m.group(1)}{expected}{m.group(2)}',
        text,
    )

    if text != orig:
        html.write_text(text, encoding="utf-8")
        fixed += 1

print(f"Scanned: {scanned} pages, fixed: {fixed} pages")
