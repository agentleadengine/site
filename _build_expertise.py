#!/usr/bin/env python3
"""Generic expertise section builder - works for any /expertise/[slug]/ section."""
from pathlib import Path

SITE = Path(__file__).parent
YEAR = 2026

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'


def build_expertise_section(section_slug, section_name, sidebar_structure, pages, nav_total_label=None):
    """
    section_slug: dir name under /expertise/ (e.g., 'paid-ads')
    section_name: display name (e.g., 'Paid Advertising')
    sidebar_structure: list of (section_label, [(slug, page_label), ...])
    pages: dict of {slug: {'title', 'description', 'reading_time', 'body'}}
    """
    total = sum(len(items) for _, items in sidebar_structure)
    label = nav_total_label or f"{section_name} ({total} pages)"

    def head(title, description, rel_root):
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="author" content="Samuel Ochoa">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:site_name" content="Samuel Ochoa">
{FONTS}
<link rel="stylesheet" href="{rel_root}styles.css">
</head>
<body>'''

    def topbar(rel_root):
        return f'''<nav class="topbar"><div class="topbar-inner">
<a href="{rel_root}index.html" class="logo"><span class="dot"></span>Samuel Ochoa</a>
<div class="nav-links">
<a href="{rel_root}index.html">Home</a>
<a href="{rel_root}framework/index.html">Framework</a>
<a href="{rel_root}expertise/index.html" class="active">Expertise</a>
<a href="{rel_root}playbooks/index.html">Playbooks</a>
<a href="{rel_root}writing.html">Writing</a>
<a href="{rel_root}contact.html">Contact</a>
</div>
</div></nav>'''

    def footer(rel_root):
        return f'''<footer><div class="container">
<p>&copy; {YEAR} Samuel Ochoa &middot; <a href="https://www.linkedin.com/in/samuelochoa" target="_blank" rel="noopener">LinkedIn</a> &middot; <a href="{rel_root}expertise/index.html">Expertise</a></p>
</div></footer></body></html>'''

    def sidebar(active_slug):
        parts = ['<aside class="framework-sidebar">']
        parts.append(f'<h4>{label}</h4>')
        for section_label, items in sidebar_structure:
            parts.append(f'<h4>{section_label}</h4><ul>')
            for slug, item_label in items:
                href = "index.html" if slug == "index" else f"{slug}.html"
                active = slug == active_slug
                cls = ' class="active"' if active else ''
                parts.append(f'<li><a href="{href}"{cls}>{item_label}</a></li>')
            parts.append('</ul>')
        parts.append('</aside>')
        return "".join(parts)

    for slug, data in pages.items():
        depth = slug.count("/")
        rel_root = "../" * (depth + 2)
        if slug == "index":
            path = SITE / "expertise" / section_slug / "index.html"
        else:
            path = SITE / "expertise" / section_slug / f"{slug}.html"
        path.parent.mkdir(parents=True, exist_ok=True)

        # Breadcrumbs
        crumbs = [("Home", rel_root + "index.html"), ("Expertise", "../index.html")]
        if slug == "index":
            crumbs.append((section_name, None))
        else:
            crumbs.append((section_name, f"../{section_slug}/index.html" if depth == 0 else "../index.html"))
            crumbs.append((data['title'], None))

        b_parts = ['<div class="breadcrumbs">']
        for i, (lbl, href) in enumerate(crumbs):
            if i > 0: b_parts.append('<span class="sep">›</span>')
            if href and i < len(crumbs) - 1:
                b_parts.append(f'<a href="{href}">{lbl}</a>')
            else:
                b_parts.append(f'<span>{lbl}</span>')
        b_parts.append('</div>')

        meta = f'<div class="article-meta">'
        if 'reading_time' in data:
            meta += f'<span>📖 {data["reading_time"]} min read</span>'
        meta += f'<span>Updated 2026-04-19</span></div>'

        pn_html = ""
        if 'prev' in data or 'next' in data:
            pn = ['<div class="prev-next">']
            if data.get('prev'):
                pn.append(f'<a href="{data["prev"][1]}" class="prev"><div class="label">← Previous</div><div class="title">{data["prev"][0]}</div></a>')
            if data.get('next'):
                pn.append(f'<a href="{data["next"][1]}" class="next"><div class="label">Next →</div><div class="title">{data["next"][0]}</div></a>')
            pn.append('</div>')
            pn_html = "".join(pn)

        html = (
            head(f"{data['title']} | Samuel Ochoa", data.get('description', ''), rel_root=rel_root) +
            topbar(rel_root) +
            '<div class="framework-layout">' +
            sidebar(slug) +
            '<div class="framework-content">' +
            "".join(b_parts) +
            f'<h1 class="title">{data["title"]}</h1>' +
            meta +
            data['body'] +
            pn_html +
            '</div></div>' +
            footer(rel_root)
        )
        path.write_text(html, encoding="utf-8")
        print(f"✓ expertise/{section_slug}/{slug}.html")

    print(f"\n✓ {section_name}: {len(pages)} pages\n")
