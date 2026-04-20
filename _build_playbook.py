#!/usr/bin/env python3
"""Generic playbook builder - reuses the insurance playbook's interactive shell
for any profession's 17-module Claude playbook."""
from pathlib import Path
from _build_insurance import PLAYBOOK_CSS, PLAYBOOK_JS, FONTS

SITE = Path(__file__).parent
YEAR = 2026
LINKEDIN = "https://www.linkedin.com/in/samuelochoa"


def build_playbook(slug_dir, profession_name, hero_subtitle, modules_data, landing_body, extra_breadcrumb_label=None):
    """
    slug_dir: e.g., "real-estate" - the dir under /playbooks/
    profession_name: e.g., "The Real Estate Agent's Claude Playbook"
    hero_subtitle: copy for the landing hero
    modules_data: list of dicts: [{"slug":"module-01","title":"...","tag":"Module 1","subtitle":"...","body":"..."}]
    landing_body: HTML for the landing page content
    """
    base = SITE / "playbooks" / slug_dir
    base.mkdir(parents=True, exist_ok=True)

    # Construct MODULES list compatible with sidebar rendering
    MODULES = [("index", "Start here", "Overview")]
    for m in modules_data:
        MODULES.append((m["slug"], m["title"], m["tag"]))
    MODULES.append(("prompt-library", "Prompt library", "Library"))

    def _head(title, description, rel_root):
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
{PLAYBOOK_CSS}
</head>
<body>'''

    def _topbar(rel_root):
        return f'''<nav class="topbar"><div class="topbar-inner">
<a href="{rel_root}index.html" class="logo"><span class="dot"></span>Samuel Ochoa</a>
<div class="nav-links">
<a href="{rel_root}index.html">Home</a>
<a href="{rel_root}framework/index.html">Framework</a>
<a href="{rel_root}expertise/index.html">Expertise</a>
<a href="{rel_root}playbooks/index.html" class="active">Playbooks</a>
<a href="{rel_root}writing.html">Writing</a>
<a href="{rel_root}contact.html">Contact</a>
</div>
</div></nav>'''

    def _sidebar(active_slug):
        parts = ['<aside class="playbook-sidebar">']
        mod_count = len([m for m in MODULES if m[0] not in ("index", "prompt-library")])
        parts.append(f'''
<div class="playbook-progress">
<h4>Your progress</h4>
<div class="playbook-progress-text"><span>Modules done</span><strong>0 / {mod_count}</strong></div>
<div class="playbook-progress-bar"><div class="playbook-progress-fill" style="width:0%"></div></div>
</div>
''')
        parts.append('<h4>Modules</h4><ul>')
        for s, l, _ in MODULES:
            if s == "prompt-library": continue
            href = "index.html" if s == "index" else f"{s}.html"
            active_cls = ' active' if s == active_slug else ''
            parts.append(f'<li><a href="{href}" class="{active_cls.strip()}" data-module="{s}">{l}</a></li>')
        parts.append('</ul>')
        parts.append('<h4>Resources</h4><ul>')
        active_cls = ' active' if active_slug == "prompt-library" else ''
        parts.append(f'<li><a href="prompt-library.html" class="{active_cls.strip()}" data-module="prompt-library">📚 Prompt library</a></li>')
        parts.append('</ul>')
        parts.append('</aside>')
        return "".join(parts)

    def _footer(rel_root):
        return f'''<footer><div class="container">
<p>&copy; {YEAR} Samuel Ochoa &middot; <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></p>
</div></footer>
{PLAYBOOK_JS}
</body></html>'''

    def _module_nav(current_slug):
        slugs = [s for s, _, _ in MODULES if s not in ("index", "prompt-library")]
        if current_slug not in slugs:
            return None, None
        i = slugs.index(current_slug)
        prev = None
        nxt = None
        if i > 0:
            p_slug = slugs[i-1]
            p_title = next(l for s, l, _ in MODULES if s == p_slug)
            prev = (p_title, f"{p_slug}.html")
        if i < len(slugs) - 1:
            n_slug = slugs[i+1]
            n_title = next(l for s, l, _ in MODULES if s == n_slug)
            nxt = (n_title, f"{n_slug}.html")
        return prev, nxt

    def _write(slug, title, tag, subtitle, body_html, hero=False, prompt_count=None):
        rel_root = "../../"
        path = base / (f"{slug}.html" if slug != "index" else "index.html")
        path.parent.mkdir(parents=True, exist_ok=True)

        # Hero or header
        if hero:
            pc = prompt_count or 60
            header_html = f'''<div class="playbook-hero">
<h1>{title}</h1>
<p class="playbook-hero-subtitle">{subtitle}</p>
<div class="playbook-hero-stats">
<div class="playbook-stat"><strong>15</strong><span>Modules</span></div>
<div class="playbook-stat"><strong>{pc}+</strong><span>Prompt templates</span></div>
<div class="playbook-stat"><strong>All</strong><span>Copy-paste ready</span></div>
<div class="playbook-stat"><strong>0</strong><span>Fluff</span></div>
</div>
</div>'''
        else:
            header_html = f'''<div class="playbook-header">
<span class="playbook-module-label">{tag}</span>
<h1 class="title">{title}</h1>
<p class="playbook-subtitle">{subtitle}</p>
</div>'''

        footer_parts = []
        if slug not in ("index", "prompt-library"):
            prev, nxt = _module_nav(slug)
            complete_btn = f'<button class="btn-complete" data-module="{slug}">Mark module complete</button>'
            nav = '<div class="module-nav">'
            if prev: nav += f'<a href="{prev[1]}">← {prev[0]}</a>'
            if nxt: nav += f'<a href="{nxt[1]}">{nxt[0]} →</a>'
            nav += '</div>'
            footer_parts.append(f'<div class="module-complete">{complete_btn}{nav}</div>')

        html = (
            _head(f"{title} | {profession_name}", subtitle, rel_root) +
            _topbar(rel_root) +
            '<div class="playbook-layout">' +
            _sidebar(slug) +
            '<div class="playbook-content">' +
            header_html +
            body_html +
            "".join(footer_parts) +
            '</div></div>' +
            _footer(rel_root)
        )
        path.write_text(html, encoding="utf-8")
        print(f"✓ playbooks/{slug_dir}/{slug}.html")

    # Write landing
    _write("index", profession_name, "", hero_subtitle, landing_body, hero=True,
           prompt_count=sum(1 for _ in modules_data) * 4)

    # Write modules
    for m in modules_data:
        _write(m["slug"], m["title"], m["tag"], m["subtitle"], m["body"])

    # Write minimal prompt library (shows all module prompts)
    prompts_html_parts = []
    for m in modules_data:
        # naive extraction: each module mentions prompts in prompt-box blocks - we'll just link to them
        prompts_html_parts.append(f'''
<div class="library-prompt">
<h3 class="library-prompt-title">{m["title"]}</h3>
<div class="library-prompt-meta">
<span style="color:#4a00e0; font-weight:600;">{m["tag"]}</span>
</div>
<p>{m["subtitle"]}</p>
<p><a href="{m["slug"]}.html" style="color:#4a00e0; font-weight:500;">Open module →</a></p>
</div>
''')
    library_body = f'''
<p>Jump to any module below. Each module contains copy-paste prompts you can use with Claude.</p>
<div class="library-count">{len(modules_data)} modules</div>
{''.join(prompts_html_parts)}
'''
    _write("prompt-library", "Prompt library", "Resource",
           "All module prompts in one place, with links to the source module.",
           library_body)

    print(f"\n✓ Playbook built: {profession_name} ({len(modules_data) + 2} pages)\n")
