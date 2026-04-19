#!/usr/bin/env python3
"""Builder for comparison pages — 'X vs Y' content for SEO."""
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
.cmp-layout {{ max-width: 960px; margin: 0 auto; padding: 48px 32px; }}
.cmp-topic {{ display: inline-block; background: #f3f0ff; color: #4a00e0; padding: 4px 12px; border-radius: 4px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 12px; }}
.cmp-title {{ font-size: 36px; font-weight: 800; margin: 0 0 8px 0; }}
.cmp-subtitle {{ font-size: 17px; color: #666; margin: 0 0 32px 0; }}
.cmp-summary {{ font-size: 17px; line-height: 1.7; margin-bottom: 32px; padding: 20px; background: #fafafa; border-radius: 8px; border-left: 4px solid #4a00e0; }}
.cmp-matrix {{ overflow-x: auto; }}
.cmp-matrix table {{ width: 100%; border-collapse: collapse; margin: 24px 0; }}
.cmp-matrix th, .cmp-matrix td {{ padding: 12px 14px; text-align: left; border-bottom: 1px solid #e5e5ea; font-size: 14px; line-height: 1.5; }}
.cmp-matrix th {{ background: #fafafa; font-weight: 700; font-size: 12px; text-transform: uppercase; letter-spacing: 0.8px; }}
.cmp-verdict {{ background: #f3f0ff; border: 1px solid #e0d4ff; padding: 20px 24px; border-radius: 10px; margin: 32px 0; }}
.cmp-verdict h3 {{ margin-top: 0; color: #4a00e0; }}
.cmp-content h2 {{ font-size: 24px; margin: 32px 0 12px; }}
.cmp-content p, .cmp-content li {{ font-size: 16px; line-height: 1.7; }}
.cmp-index {{ max-width: 1100px; margin: 0 auto; padding: 48px 32px; }}
.cmp-filter {{ display: flex; gap: 8px; margin: 16px 0 24px; flex-wrap: wrap; }}
.cmp-chip {{ padding: 6px 14px; background: #fff; border: 1px solid #e5e5ea; color: #333; border-radius: 999px; cursor: pointer; font-size: 13px; font-weight: 500; font-family: inherit; }}
.cmp-chip:hover {{ border-color: #4a00e0; color: #4a00e0; }}
.cmp-chip.active {{ background: #4a00e0; color: #fff; border-color: #4a00e0; }}
.cmp-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 12px; }}
.cmp-card {{ display: block; padding: 16px 18px; background: #fff; border: 1px solid #e5e5ea; border-radius: 8px; text-decoration: none; color: #333; }}
.cmp-card:hover {{ border-color: #4a00e0; }}
.cmp-card.hidden {{ display: none; }}
.cmp-card-title {{ font-weight: 600; font-size: 16px; color: #4a00e0; }}
.cmp-card-topic {{ font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #666; margin: 2px 0 6px 0; }}
.cmp-card-summary {{ font-size: 13px; color: #666; line-height: 1.5; }}
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
<a href="{rel_root}glossary/index.html">Glossary</a>
<a href="{rel_root}compare/index.html" class="active">Compare</a>
<a href="{rel_root}writing.html">Writing</a>
</div>
</div></nav>'''


def footer(rel_root):
    return f'''<footer><div class="container">
<p>&copy; {YEAR} Samuel Ochoa &middot; <a href="https://www.linkedin.com/in/samuelochoa" target="_blank" rel="noopener">LinkedIn</a></p>
</div></footer></body></html>'''


def write_comparison(cmp):
    """Write a single comparison page."""
    path = SITE / "compare" / f"{cmp['slug']}.html"
    path.parent.mkdir(parents=True, exist_ok=True)

    # Matrix table
    matrix_rows = ""
    for row in cmp['matrix']:
        matrix_rows += f'<tr><th scope="row">{row[0]}</th><td>{row[1]}</td><td>{row[2]}</td></tr>'
    matrix_html = f'''<div class="cmp-matrix"><table>
<thead><tr><th></th><th>{cmp['a']}</th><th>{cmp['b']}</th></tr></thead>
<tbody>{matrix_rows}</tbody>
</table></div>'''

    body = f'''<div class="cmp-layout cmp-content">
<a href="index.html" style="color:#4a00e0; text-decoration: none; font-size: 14px;">← All comparisons</a>
<span class="cmp-topic" style="margin-top: 16px;">{cmp['topic']}</span>
<h1 class="cmp-title">{cmp['a']} vs {cmp['b']}</h1>
<p class="cmp-subtitle">{cmp['subtitle']}</p>

<div class="cmp-summary">{cmp['tldr']}</div>

<h2>At a glance</h2>
{matrix_html}

<h2>When to pick {cmp['a']}</h2>
{cmp['pick_a']}

<h2>When to pick {cmp['b']}</h2>
{cmp['pick_b']}

<div class="cmp-verdict">
<h3>My verdict</h3>
{cmp['verdict']}
</div>
</div>'''

    html = head(f"{cmp['a']} vs {cmp['b']} | Compare | Samuel Ochoa", cmp['subtitle'][:160], "../") + topbar("../") + body + footer("../")
    path.write_text(html, encoding="utf-8")


def write_index(comparisons):
    """Write the comparisons index."""
    topics = sorted(set(c['topic'] for c in comparisons))
    chips = '<button class="cmp-chip active" data-topic="all">All</button>'
    for t in topics:
        chips += f'<button class="cmp-chip" data-topic="{t}">{t}</button>'

    cards = ""
    for c in sorted(comparisons, key=lambda x: x['a'].lower()):
        cards += f'''<a href="{c['slug']}.html" class="cmp-card" data-topic="{c['topic']}" data-search="{c['a'].lower()} {c['b'].lower()}">
<div class="cmp-card-title">{c['a']} vs {c['b']}</div>
<div class="cmp-card-topic">{c['topic']}</div>
<div class="cmp-card-summary">{c['subtitle']}</div>
</a>'''

    body = f'''<div class="cmp-index">
<h1 style="font-size: 42px; margin: 0 0 8px 0;">Comparisons</h1>
<p style="font-size: 17px; color: #666; margin: 0 0 24px 0;">Head-to-head breakdowns of the tools and approaches I actually use and evaluate.</p>
<div class="cmp-filter">{chips}</div>
<p style="color: #666; font-size: 14px; margin-bottom: 12px;"><span id="cmp-count">{len(comparisons)}</span> comparisons</p>
<div class="cmp-grid" id="cmp-grid">{cards}</div>
</div>

<script>
(function(){{
    const chips = document.querySelectorAll('.cmp-chip');
    const cards = document.querySelectorAll('.cmp-card');
    const count = document.getElementById('cmp-count');
    let activeTopic = 'all';
    function apply() {{
        let shown = 0;
        cards.forEach(c => {{
            const topic = c.dataset.topic;
            const match = activeTopic === 'all' || topic === activeTopic;
            c.classList.toggle('hidden', !match);
            if (match) shown++;
        }});
        count.textContent = shown;
    }}
    chips.forEach(ch => ch.addEventListener('click', () => {{
        chips.forEach(c => c.classList.remove('active'));
        ch.classList.add('active');
        activeTopic = ch.dataset.topic;
        apply();
    }}));
}})();
</script>'''

    path = SITE / "compare" / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    html = head("Comparisons | Samuel Ochoa", "Head-to-head comparisons of tools and approaches.", "../") + topbar("../") + body + footer("../")
    path.write_text(html, encoding="utf-8")


def build_comparisons(comparisons):
    for c in comparisons:
        write_comparison(c)
    write_index(comparisons)
    print(f"✓ Comparisons: {len(comparisons) + 1} pages")
