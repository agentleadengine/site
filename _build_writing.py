#!/usr/bin/env python3
"""Writing/essays section - standalone posts."""
from pathlib import Path

SITE = Path(__file__).parent
YEAR = 2026

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'


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
<style>
.essay {{ max-width: 720px; margin: 0 auto; padding: 56px 32px; }}
.essay-meta {{ font-size: 13px; color: #8e8e93; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 12px; }}
.essay h1 {{ font-size: 42px; line-height: 1.15; margin: 0 0 16px 0; font-weight: 800; }}
.essay .subtitle {{ font-size: 19px; color: #4a4a52; margin: 0 0 48px 0; line-height: 1.5; }}
.essay h2 {{ font-size: 24px; margin: 40px 0 14px 0; font-weight: 700; }}
.essay h3 {{ font-size: 19px; margin: 28px 0 10px 0; font-weight: 600; }}
.essay p {{ font-size: 18px; line-height: 1.75; margin: 16px 0; color: #1a1a2e; }}
.essay ul, .essay ol {{ font-size: 18px; line-height: 1.75; padding-left: 28px; }}
.essay li {{ margin: 4px 0; }}
.essay blockquote {{ border-left: 4px solid #4a00e0; padding-left: 20px; margin: 24px 0; color: #4a4a52; font-style: italic; }}
.essay-foot {{ margin-top: 56px; padding-top: 32px; border-top: 1px solid #e5e5ea; font-size: 14px; color: #666; }}
.essays-index {{ max-width: 900px; margin: 0 auto; padding: 56px 32px; }}
.essays-index h1 {{ font-size: 48px; margin: 0 0 12px 0; }}
.essays-list {{ margin-top: 32px; }}
.essay-card {{ display: block; padding: 24px; border-bottom: 1px solid #e5e5ea; text-decoration: none; color: #333; transition: background 0.15s; }}
.essay-card:hover {{ background: #fafafa; }}
.essay-card-title {{ font-size: 22px; font-weight: 700; color: #1a1a2e; margin: 0 0 6px 0; }}
.essay-card-sub {{ font-size: 15px; color: #666; margin: 0 0 8px 0; }}
.essay-card-meta {{ font-size: 12px; color: #8e8e93; text-transform: uppercase; letter-spacing: 1px; }}
</style>
</head>
<body>'''


def topbar(rel_root):
    return f'''<nav class="topbar"><div class="topbar-inner">
<a href="{rel_root}index.html" class="logo"><span class="dot"></span>Samuel Ochoa</a>
<div class="nav-links">
<a href="{rel_root}index.html">Home</a>
<a href="{rel_root}expertise/index.html">Expertise</a>
<a href="{rel_root}playbooks/index.html">Playbooks</a>
<a href="{rel_root}glossary/index.html">Glossary</a>
<a href="{rel_root}compare/index.html">Compare</a>
<a href="{rel_root}writing/index.html" class="active">Writing</a>
</div>
</div></nav>'''


def footer(rel_root):
    return f'''<footer><div class="container">
<p>&copy; {YEAR} Samuel Ochoa &middot; <a href="https://www.linkedin.com/in/samuelochoa" target="_blank" rel="noopener">LinkedIn</a></p>
</div></footer></body></html>'''


def write_essay(e):
    path = SITE / "writing" / f"{e['slug']}.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    body = f'''<article class="essay">
<div class="essay-meta">{e['topic']} · {e['date']}</div>
<h1>{e['title']}</h1>
<p class="subtitle">{e['subtitle']}</p>
{e['body']}
<div class="essay-foot">
<a href="index.html" style="color:#4a00e0; text-decoration: none;">← All writing</a>
</div>
</article>'''
    html = head(f"{e['title']} | Samuel Ochoa", e['subtitle'][:160], "../") + topbar("../") + body + footer("../")
    path.write_text(html, encoding="utf-8")


def write_index(essays):
    cards = ""
    for e in essays:
        cards += f'''<a href="{e['slug']}.html" class="essay-card">
<h2 class="essay-card-title">{e['title']}</h2>
<p class="essay-card-sub">{e['subtitle']}</p>
<div class="essay-card-meta">{e['topic']} · {e['date']}</div>
</a>'''
    body = f'''<div class="essays-index">
<h1>Writing</h1>
<p style="font-size: 17px; color: #666; max-width: 680px;">Essays on AI, marketing, operations, and the compound effects of focused work. Not polished performance. Working notes I actually mean.</p>
<div class="essays-list">{cards}</div>
</div>'''
    path = SITE / "writing" / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    html = head("Writing | Samuel Ochoa", "Essays on AI, marketing, operations.", "../") + topbar("../") + body + footer("../")
    path.write_text(html, encoding="utf-8")


def build_writing(essays):
    for e in essays:
        write_essay(e)
    write_index(essays)
    print(f"✓ Writing: {len(essays) + 1} pages")
