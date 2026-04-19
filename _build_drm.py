#!/usr/bin/env python3
"""Builder for the Direct Response Marketing expertise section."""
from pathlib import Path

SITE = Path(__file__).parent
YEAR = 2026
LINKEDIN = "https://www.linkedin.com/in/samuelochoa"

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'

DRM_SIDEBAR = [
    ("Foundations", [
        ("index", "Overview"),
        ("foundations/what-is-direct-response", "What is direct response?"),
        ("foundations/four-horsemen", "Influences"),
        ("foundations/scientific-advertising", "Scientific advertising (Hopkins)"),
        ("foundations/ten-rules", "The 10 rules (Kennedy)"),
    ]),
    ("The Market", [
        ("market/starving-crowd", "The starving crowd"),
        ("market/sophistication", "Market sophistication"),
        ("market/awareness-stages", "Awareness stages"),
        ("market/dream-customer", "The dream customer"),
        ("market/market-selection", "Picking a market"),
    ]),
    ("The Offer", [
        ("offer/value-equation", "The value equation"),
        ("offer/grand-slam", "Grand slam offers"),
        ("offer/bonuses", "Bonuses that stack"),
        ("offer/guarantees", "Guarantees + risk reversal"),
        ("offer/pricing-psychology", "Pricing psychology"),
        ("offer/urgency-scarcity", "Urgency + scarcity"),
    ]),
    ("Copywriting", [
        ("copy/the-stack", "The copywriting stack"),
        ("copy/headlines", "Headlines"),
        ("copy/the-lead", "The lead (first 100 words)"),
        ("copy/body-copy", "Body copy"),
        ("copy/ctas", "Calls to action"),
        ("copy/formulas", "AIDA, PAS, PASTOR"),
        ("copy/bullets", "Fascination bullets"),
    ]),
    ("Lead Generation", [
        ("leads/core-four", "The core four"),
        ("leads/lead-magnets", "Lead magnets"),
        ("leads/warm-outreach", "Warm outreach"),
        ("leads/cold-outreach", "Cold outreach"),
        ("leads/paid-ads", "Paid ads"),
    ]),
    ("Sales Letters + VSLs", [
        ("letters/structure", "Sales letter structure"),
        ("letters/long-form", "Long form vs short form"),
        ("letters/vsls", "VSLs"),
        ("letters/story-selling", "Story selling"),
        ("letters/halbert-letters", "The Halbert letters"),
    ]),
    ("Follow-up + Retention", [
        ("followup/direct-mail", "Direct mail that still works"),
        ("followup/email-sequences", "Email sequences"),
        ("followup/soap-opera", "The soap opera sequence"),
        ("followup/indoctrination", "Customer indoctrination"),
    ]),
    ("Testing", [
        ("testing/scientific", "Scientific testing"),
        ("testing/what-to-test", "What to test"),
        ("testing/controls", "Controls + challengers"),
        ("testing/measurement", "Measurement"),
    ]),
    ("Scaling", [
        ("scaling/scale-winners", "Scaling what works"),
        ("scaling/value-ladder", "The value ladder"),
        ("scaling/high-ticket", "High ticket"),
        ("scaling/info-products", "Info products"),
    ]),
]


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


def topbar(active, rel_root):
    def cls(name): return ' class="active"' if active == name else ''
    return f'''<nav class="topbar"><div class="topbar-inner">
<a href="{rel_root}index.html" class="logo"><span class="dot"></span>Samuel Ochoa</a>
<div class="nav-links">
<a href="{rel_root}index.html"{cls('home')}>Home</a>
<a href="{rel_root}framework/index.html"{cls('framework')}>Framework</a>
<a href="{rel_root}expertise/index.html"{cls('expertise')}>Expertise</a>
<a href="{rel_root}writing.html"{cls('writing')}>Writing</a>
<a href="{rel_root}about.html"{cls('about')}>About</a>
<a href="{rel_root}contact.html"{cls('contact')}>Contact</a>
</div>
</div></nav>'''


def footer(rel_root):
    return f'''<footer><div class="container">
<p>&copy; {YEAR} Samuel Ochoa &middot; <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a> &middot; <a href="{rel_root}expertise/index.html">Expertise</a></p>
</div></footer></body></html>'''


def sidebar_html(active_slug):
    parts = ['<aside class="framework-sidebar">']
    parts.append('<h4>Direct Response Marketing (45 pages)</h4>')
    for section, items in DRM_SIDEBAR:
        parts.append(f'<h4>{section}</h4><ul>')
        for slug, label in items:
            href = "index.html" if slug == "index" else f"{slug}.html"
            active = slug == active_slug
            cls = ' class="active"' if active else ''
            parts.append(f'<li><a href="{href}"{cls}>{label}</a></li>')
        parts.append('</ul>')
    parts.append('</aside>')
    return "".join(parts)


def write_drm_page(slug, title, description, body_html, reading_time=None, prev=None, nxt=None):
    depth = slug.count("/")
    rel_root = "../" * (depth + 2)
    if slug == "index":
        path = SITE / "expertise" / "direct-response" / "index.html"
        active_slug = "index"
    else:
        path = SITE / "expertise" / "direct-response" / f"{slug}.html"
        active_slug = slug
    path.parent.mkdir(parents=True, exist_ok=True)

    crumbs = [("Home", rel_root + "index.html"), ("Expertise", "../index.html")]
    if slug == "index":
        crumbs.append(("Direct Response", None))
    else:
        crumbs.append(("Direct Response", "../direct-response/index.html" if depth == 0 else "../index.html"))
        crumbs.append((title, None))

    b_parts = ['<div class="breadcrumbs">']
    for i, (label, href) in enumerate(crumbs):
        if i > 0: b_parts.append('<span class="sep">›</span>')
        if href and i < len(crumbs) - 1:
            b_parts.append(f'<a href="{href}">{label}</a>')
        else:
            b_parts.append(f'<span>{label}</span>')
    b_parts.append('</div>')
    breadcrumb_html = "".join(b_parts)

    meta_parts = []
    if reading_time: meta_parts.append(f'<span>📖 {reading_time} min read</span>')
    meta_parts.append(f'<span>Updated 2026-04-18</span>')
    meta_html = '<div class="article-meta">' + "".join(meta_parts) + '</div>'

    pn_html = ""
    if prev or nxt:
        pn = ['<div class="prev-next">']
        if prev: pn.append(f'<a href="{prev[1]}" class="prev"><div class="label">← Previous</div><div class="title">{prev[0]}</div></a>')
        if nxt: pn.append(f'<a href="{nxt[1]}" class="next"><div class="label">Next →</div><div class="title">{nxt[0]}</div></a>')
        pn.append('</div>')
        pn_html = "".join(pn)

    html = (
        head(f"{title} — Samuel Ochoa", description, rel_root=rel_root) +
        topbar("expertise", rel_root=rel_root) +
        '<div class="framework-layout">' +
        sidebar_html(active_slug) +
        '<div class="framework-content">' +
        breadcrumb_html +
        f'<h1 class="title">{title}</h1>' +
        meta_html +
        body_html +
        pn_html +
        '</div></div>' +
        footer(rel_root=rel_root)
    )
    path.write_text(html, encoding="utf-8")
    print(f"✓ expertise/direct-response/{slug}.html")


if __name__ == "__main__":
    print("Direct Response builder loaded.")
