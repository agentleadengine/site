#!/usr/bin/env python3
"""Fix broken sidebar links in expertise sub-subdirectory pages.

Pages at expertise/<section>/<subsection>/<page>.html have sidebars with
section-root-relative paths (e.g. href="foundations/what-is-seo.html") that
assume the page is at the section root. Since the page is one level deeper,
these resolve to expertise/<section>/<subsection>/foundations/what-is-seo.html
(doesn't exist). Prefix every relative link inside the sidebar with '../' so
they resolve correctly.
"""
import re
from pathlib import Path

ROOT = Path("/Users/ble/Desktop/sams site")
EXPERTISE = ROOT / "expertise"

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

for page in EXPERTISE.rglob("*.html"):
    rel = page.relative_to(ROOT)
    # expertise/<section>/<subsection>/<file>.html — len(parts) == 4
    if len(rel.parts) != 4:
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

print(f"Sub-subdir pages scanned: {scanned}, sidebar-fixed: {fixed}")
