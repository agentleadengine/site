#!/usr/bin/env python3
"""Fix sidebar paths in framework subdirectory pages (same bug as expertise)."""
import re
from pathlib import Path

ROOT = Path("/Users/ble/Desktop/sams site")
FRAMEWORK = ROOT / "framework"

SIDEBAR_RE = re.compile(
    r'(<aside class="framework-sidebar">)(.*?)(</aside>)',
    re.DOTALL
)
HREF_RE = re.compile(r'href="([^"]+)"')


def should_prefix(link: str) -> bool:
    if not link:
        return False
    if link.startswith(("http://", "https://", "mailto:", "tel:", "#", "/", "../")):
        return False
    return True


def fix_sidebar(sidebar_inner: str) -> str:
    def repl(m):
        link = m.group(1)
        if should_prefix(link):
            return f'href="../{link}"'
        return m.group(0)
    return HREF_RE.sub(repl, sidebar_inner)


fixed = 0
scanned = 0
for page in FRAMEWORK.rglob("*.html"):
    rel = page.relative_to(ROOT)
    # framework/<section>/<file>.html — len(parts) == 3
    if len(rel.parts) != 3:
        continue
    scanned += 1

    text = page.read_text(encoding="utf-8")
    m = SIDEBAR_RE.search(text)
    if not m:
        continue

    sidebar_inner = m.group(2)
    new_inner = fix_sidebar(sidebar_inner)
    if new_inner == sidebar_inner:
        continue

    new_text = text[:m.start(2)] + new_inner + text[m.end(2):]
    page.write_text(new_text, encoding="utf-8")
    fixed += 1

print(f"Framework subdir pages scanned: {scanned}, sidebar-fixed: {fixed}")
