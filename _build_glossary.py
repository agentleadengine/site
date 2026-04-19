#!/usr/bin/env python3
"""Glossary builder - one page per term, searchable index."""
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
.gloss-layout {{ max-width: 960px; margin: 0 auto; padding: 48px 32px; }}
.gloss-term {{ font-size: 36px; font-weight: 800; margin: 0 0 8px 0; }}
.gloss-topic {{ display: inline-block; background: #f3f0ff; color: #4a00e0; padding: 4px 12px; border-radius: 4px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 12px; }}
.gloss-def {{ font-size: 18px; line-height: 1.7; color: #333; margin: 16px 0; }}
.gloss-detail {{ font-size: 16px; line-height: 1.7; color: #4a4a52; margin: 12px 0; }}
.gloss-related {{ margin-top: 32px; padding: 20px; background: #fafafa; border-radius: 8px; }}
.gloss-related h4 {{ font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px; color: #666; margin: 0 0 8px 0; }}
.gloss-related a {{ display: inline-block; margin-right: 8px; color: #4a00e0; text-decoration: none; }}
.gloss-related a:hover {{ text-decoration: underline; }}
.gloss-index {{ max-width: 1100px; margin: 0 auto; padding: 48px 32px; }}
.gloss-filter {{ display: flex; gap: 8px; margin: 16px 0 24px; flex-wrap: wrap; }}
.gloss-chip {{ padding: 6px 14px; background: #fff; border: 1px solid #e5e5ea; color: #333; border-radius: 999px; cursor: pointer; font-size: 13px; font-weight: 500; font-family: inherit; }}
.gloss-chip:hover {{ border-color: #4a00e0; color: #4a00e0; }}
.gloss-chip.active {{ background: #4a00e0; color: #fff; border-color: #4a00e0; }}
.gloss-search {{ margin: 16px 0; }}
.gloss-search input {{ width: 100%; padding: 12px 16px; border: 1px solid #e5e5ea; border-radius: 8px; font-size: 15px; font-family: inherit; }}
.gloss-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 12px; }}
.gloss-card {{ display: block; padding: 16px 18px; background: #fff; border: 1px solid #e5e5ea; border-radius: 8px; text-decoration: none; color: #333; transition: border-color 0.15s; }}
.gloss-card:hover {{ border-color: #4a00e0; }}
.gloss-card.hidden {{ display: none; }}
.gloss-card-term {{ font-weight: 600; font-size: 16px; color: #4a00e0; }}
.gloss-card-topic {{ font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #666; margin: 2px 0 6px 0; }}
.gloss-card-summary {{ font-size: 13px; color: #666; line-height: 1.5; }}
.gloss-count {{ color: #666; font-size: 14px; margin-bottom: 12px; }}
</style>
</head>
<body>'''


def topbar(rel_root):
    return f'''<nav class="topbar"><div class="topbar-inner">
<a href="{rel_root}index.html" class="logo"><span class="dot"></span>Samuel Ochoa</a>
<div class="nav-links">
<a href="{rel_root}index.html">Home</a>
<a href="{rel_root}framework/index.html">Framework</a>
<a href="{rel_root}expertise/index.html">Expertise</a>
<a href="{rel_root}playbooks/index.html">Playbooks</a>
<a href="{rel_root}glossary/index.html" class="active">Glossary</a>
<a href="{rel_root}writing.html">Writing</a>
<a href="{rel_root}contact.html">Contact</a>
</div>
</div></nav>'''


def footer(rel_root):
    return f'''<footer><div class="container">
<p>&copy; {YEAR} Samuel Ochoa &middot; <a href="https://www.linkedin.com/in/samuelochoa" target="_blank" rel="noopener">LinkedIn</a></p>
</div></footer></body></html>'''


def write_term(term_data, all_terms):
    """Write one glossary term page."""
    slug = term_data['slug']
    path = SITE / "glossary" / f"{slug}.html"
    path.parent.mkdir(parents=True, exist_ok=True)

    related_html = ""
    if term_data.get('related'):
        related_html = '<div class="gloss-related"><h4>Related terms</h4>'
        for r_slug in term_data['related']:
            r = next((t for t in all_terms if t['slug'] == r_slug), None)
            if r:
                related_html += f'<a href="{r_slug}.html">{r["term"]}</a>'
        related_html += '</div>'

    body = f'''<div class="gloss-layout">
<a href="index.html" style="color:#4a00e0; text-decoration: none; font-size: 14px;">← Glossary</a>
<span class="gloss-topic" style="margin-top: 24px;">{term_data['topic']}</span>
<h1 class="gloss-term">{term_data['term']}</h1>
<p class="gloss-def">{term_data['definition']}</p>
{term_data.get('detail', '')}
{related_html}
</div>'''

    html = head(f"{term_data['term']} | Glossary | Samuel Ochoa", term_data['definition'][:160], "../") + topbar("../") + body + footer("../")
    path.write_text(html, encoding="utf-8")


def write_index(all_terms):
    """Write the glossary index with search + filter."""
    topics = sorted(set(t['topic'] for t in all_terms))
    chips = '<button class="gloss-chip active" data-topic="all">All</button>'
    for t in topics:
        chips += f'<button class="gloss-chip" data-topic="{t}">{t}</button>'

    cards = ""
    for t in sorted(all_terms, key=lambda x: x['term'].lower()):
        cards += f'''<a href="{t['slug']}.html" class="gloss-card" data-topic="{t['topic']}" data-search="{t['term'].lower()} {t['definition'].lower()}">
<div class="gloss-card-term">{t['term']}</div>
<div class="gloss-card-topic">{t['topic']}</div>
<div class="gloss-card-summary">{t['definition'][:120]}{'...' if len(t['definition']) > 120 else ''}</div>
</a>'''

    body = f'''<div class="gloss-index">
<h1 style="font-size: 42px; margin: 0 0 8px 0;">Glossary</h1>
<p style="font-size: 17px; color: #666; margin: 0 0 24px 0;">Terms from AI, marketing, direct response, SEO, and business ops. Plain-language definitions.</p>

<div class="gloss-search"><input type="text" id="gloss-search" placeholder="Search terms..."></div>
<div class="gloss-filter">{chips}</div>
<p class="gloss-count"><span id="gloss-count">{len(all_terms)}</span> terms</p>

<div class="gloss-grid" id="gloss-grid">{cards}</div>
</div>

<script>
(function(){{
    const search = document.getElementById('gloss-search');
    const chips = document.querySelectorAll('.gloss-chip');
    const cards = document.querySelectorAll('.gloss-card');
    const count = document.getElementById('gloss-count');
    let activeTopic = 'all';

    function apply() {{
        const q = (search.value || '').toLowerCase().trim();
        let shown = 0;
        cards.forEach(c => {{
            const topic = c.dataset.topic;
            const text = c.dataset.search;
            const match = (activeTopic === 'all' || topic === activeTopic) && (!q || text.includes(q));
            c.classList.toggle('hidden', !match);
            if (match) shown++;
        }});
        count.textContent = shown;
    }}

    search.addEventListener('input', apply);
    chips.forEach(ch => {{
        ch.addEventListener('click', () => {{
            chips.forEach(c => c.classList.remove('active'));
            ch.classList.add('active');
            activeTopic = ch.dataset.topic;
            apply();
        }});
    }});
}})();
</script>'''

    path = SITE / "glossary" / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    html = head("Glossary | Samuel Ochoa", "Plain-language definitions of AI, marketing, direct response, SEO, and business ops terms.", "../") + topbar("../") + body + footer("../")
    path.write_text(html, encoding="utf-8")
    print(f"✓ glossary/index.html")


def build_glossary(terms):
    """Build all term pages plus index."""
    for t in terms:
        write_term(t, terms)
        print(f"✓ glossary/{t['slug']}.html")
    write_index(terms)
    print(f"\n✓ Glossary: {len(terms) + 1} pages")
