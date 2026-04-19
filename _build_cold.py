#!/usr/bin/env python3
"""Builder for the Cold Email expertise section."""
from pathlib import Path

SITE = Path(__file__).parent
YEAR = 2026
LINKEDIN = "https://www.linkedin.com/in/samuelochoa"

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'

COLD_SIDEBAR = [
    ("Foundations", [
        ("index", "Overview"),
        ("foundations/what-is-cold-email", "What is cold email?"),
        ("foundations/spam-vs-cold", "Cold email vs spam"),
        ("foundations/legal", "Legal landscape"),
        ("foundations/when-it-works", "When cold email works"),
    ]),
    ("Deliverability", [
        ("deliverability/why-it-matters", "Why deliverability is everything"),
        ("deliverability/dns", "SPF, DKIM, DMARC"),
        ("deliverability/sending-domains", "Sending domain strategy"),
        ("deliverability/warming", "Inbox warming"),
        ("deliverability/ip-reputation", "IP reputation"),
        ("deliverability/spam-triggers", "Content that triggers spam filters"),
        ("deliverability/monitoring", "Monitoring inbox placement"),
    ]),
    ("Infrastructure", [
        ("infra/sending-tools", "Sending tools"),
        ("infra/multi-inbox", "Multi-inbox rotation"),
        ("infra/warming-tools", "Warming tools"),
        ("infra/crm-integration", "CRM and data integration"),
        ("infra/reply-management", "Reply management"),
    ]),
    ("Lists + Targeting", [
        ("lists/icp", "Defining the ICP"),
        ("lists/databases", "Lead databases"),
        ("lists/clay", "Clay and enrichment"),
        ("lists/verification", "Verification + hygiene"),
        ("lists/intent-signals", "Intent signals"),
        ("lists/segmentation", "Segmentation strategy"),
    ]),
    ("Copy", [
        ("copy/anatomy", "Cold email anatomy"),
        ("copy/subject-lines", "Subject lines"),
        ("copy/first-lines", "First lines"),
        ("copy/the-pitch", "The pitch"),
        ("copy/ctas", "CTAs for cold"),
        ("copy/signatures", "Signatures"),
        ("copy/personalization", "Personalization at scale"),
    ]),
    ("Sequences", [
        ("sequences/multi-touch", "Multi-touch sequences"),
        ("sequences/cadence", "Cadence and timing"),
        ("sequences/breakup", "The breakup email"),
        ("sequences/multi-channel", "Multi-channel orchestration"),
        ("sequences/length", "Sequence length"),
    ]),
    ("Testing", [
        ("testing/methodology", "Testing methodology"),
        ("testing/what-to-test", "What to test"),
        ("testing/reply-metrics", "Reply rate vs positive reply"),
        ("testing/iteration", "The iteration loop"),
    ]),
    ("Playbooks", [
        ("plays/b2b-saas", "B2B SaaS outbound"),
        ("plays/agency", "Agency + services outbound"),
        ("plays/founder-led", "Founder-led outbound"),
        ("plays/sdr-led", "SDR-led outbound"),
        ("plays/link-building", "Cold email for SEO"),
        ("plays/recruiting", "Recruiting outreach"),
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
    parts.append('<h4>Cold Email (45 pages)</h4>')
    for section, items in COLD_SIDEBAR:
        parts.append(f'<h4>{section}</h4><ul>')
        for slug, label in items:
            href = "index.html" if slug == "index" else f"{slug}.html"
            active = slug == active_slug
            cls = ' class="active"' if active else ''
            parts.append(f'<li><a href="{href}"{cls}>{label}</a></li>')
        parts.append('</ul>')
    parts.append('</aside>')
    return "".join(parts)


def write_cold_page(slug, title, description, body_html, reading_time=None, prev=None, nxt=None):
    depth = slug.count("/")
    rel_root = "../" * (depth + 2)
    if slug == "index":
        path = SITE / "expertise" / "cold-email" / "index.html"
        active_slug = "index"
    else:
        path = SITE / "expertise" / "cold-email" / f"{slug}.html"
        active_slug = slug
    path.parent.mkdir(parents=True, exist_ok=True)

    crumbs = [("Home", rel_root + "index.html"), ("Expertise", "../index.html")]
    if slug == "index":
        crumbs.append(("Cold Email", None))
    else:
        crumbs.append(("Cold Email", "../cold-email/index.html" if depth == 0 else "../index.html"))
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
        head(f"{title} | Samuel Ochoa", description, rel_root=rel_root) +
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
    print(f"✓ expertise/cold-email/{slug}.html")


if __name__ == "__main__":
    print("Cold email builder loaded.")
