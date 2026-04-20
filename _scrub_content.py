#!/usr/bin/env python3
"""Scrub em-dashes and banned present-tense business phrases site-wide."""
import re
from pathlib import Path

ROOT = Path("/Users/ble/Desktop/sams site")

# Replacements for em-dashes and en-dashes
# Common patterns: " - ", "-", " - ", "-"
EM_REPLACEMENTS = [
    (" - ", ", "),
    (" - ", ", "),
    ("-", ", "),
    ("-", ", "),
]

# Replacements for banned phrases (case-insensitive where appropriate)
BANNED_REPLACEMENTS = [
    (re.compile(r"\bI run\b", re.IGNORECASE), "I write about"),
    (re.compile(r"\bmy team\b", re.IGNORECASE), "the team"),
    (re.compile(r"\bcurrently running\b", re.IGNORECASE), "running"),
]

em_fixed = 0
banned_fixed = 0
scanned = 0

for html in ROOT.rglob("*.html"):
    scanned += 1
    text = html.read_text(encoding="utf-8")
    orig = text

    # Em-dash scrub
    for a, b in EM_REPLACEMENTS:
        text = text.replace(a, b)

    had_em_change = text != orig
    pre_banned = text

    # Banned phrase scrub
    for pattern, repl in BANNED_REPLACEMENTS:
        text = pattern.sub(repl, text)

    had_banned_change = text != pre_banned

    if text != orig:
        html.write_text(text, encoding="utf-8")
        if had_em_change:
            em_fixed += 1
        if had_banned_change:
            banned_fixed += 1

print(f"Scanned {scanned} | em-dash files fixed: {em_fixed} | banned-phrase files fixed: {banned_fixed}")
