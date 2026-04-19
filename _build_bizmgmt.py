#!/usr/bin/env python3
"""Builder for the Business Management expertise section."""
from pathlib import Path

SITE = Path(__file__).parent
YEAR = 2026
LINKEDIN = "https://www.linkedin.com/in/samuelochoa"

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'

BM_SIDEBAR = [
    ("Operating Systems", [
        ("index", "Overview"),
        ("operating-systems/designing-the-os", "Designing the OS"),
        ("operating-systems/weekly-business-review", "Weekly business review"),
        ("operating-systems/meetings", "Meetings that don't waste time"),
        ("operating-systems/sops", "SOPs that get used"),
        ("operating-systems/decision-logs", "Decision logs"),
    ]),
    ("People + Hiring", [
        ("people/hiring-signal-vs-noise", "Hiring — signal vs noise"),
        ("people/role-scorecard", "The role scorecard"),
        ("people/onboarding", "Onboarding that compounds"),
        ("people/one-on-ones", "One-on-ones"),
        ("people/performance-reviews", "Performance reviews"),
        ("people/firing-well", "Firing well"),
    ]),
    ("Finance + Economics", [
        ("finance/three-numbers", "The three numbers"),
        ("finance/pnl-literacy", "P&L literacy"),
        ("finance/unit-economics", "Unit economics"),
        ("finance/pricing", "Pricing frameworks"),
        ("finance/cash-flow", "Cash flow forecasting"),
    ]),
    ("Strategy + Planning", [
        ("strategy/okrs", "OKRs without the cult"),
        ("strategy/planning-cadence", "Annual + quarterly planning"),
        ("strategy/what-to-kill", "What to kill"),
        ("strategy/pre-mortems", "Pre-mortems"),
        ("strategy/decision-frameworks", "Decision frameworks"),
    ]),
    ("Sales + GTM", [
        ("sales/funnel-math", "Funnel math that matters"),
        ("sales/pipeline-design", "Pipeline design"),
        ("sales/negotiation", "Pricing + negotiation"),
        ("sales/churn-diagnostics", "Churn diagnostics"),
        ("sales/customer-success-ops", "Customer success ops"),
    ]),
    ("Execution + Delivery", [
        ("execution/process-mapping", "Process mapping"),
        ("execution/automate-vs-hire", "Automate vs hire"),
        ("execution/vendor-management", "Vendor management"),
        ("execution/slas-and-slos", "SLAs + SLOs"),
    ]),
    ("Leadership + Culture", [
        ("leadership/memo-culture", "Memo culture"),
        ("leadership/radical-candor", "Radical candor"),
        ("leadership/accountability", "Accountability without micromanagement"),
        ("leadership/compensation", "Compensation design"),
    ]),
    ("Risk + Compliance", [
        ("risk/risk-management", "Risk management basics"),
        ("risk/data-and-ip", "Data + IP protection"),
        ("risk/insurance", "Business insurance"),
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
    parts.append('<h4>Business Management (38 pages)</h4>')
    for section, items in BM_SIDEBAR:
        parts.append(f'<h4>{section}</h4><ul>')
        for slug, label in items:
            href = "index.html" if slug == "index" else f"{slug}.html"
            active = slug == active_slug
            cls = ' class="active"' if active else ''
            parts.append(f'<li><a href="{href}"{cls}>{label}</a></li>')
        parts.append('</ul>')
    parts.append('</aside>')
    return "".join(parts)


def write_bm_page(slug, title, description, body_html, reading_time=None, prev=None, nxt=None):
    depth = slug.count("/")
    rel_root = "../" * (depth + 2)
    if slug == "index":
        path = SITE / "expertise" / "business-management" / "index.html"
        active_slug = "index"
    else:
        path = SITE / "expertise" / "business-management" / f"{slug}.html"
        active_slug = slug
    path.parent.mkdir(parents=True, exist_ok=True)

    crumbs = [("Home", rel_root + "index.html"), ("Expertise", "../index.html")]
    if slug == "index":
        crumbs.append(("Business Management", None))
    else:
        crumbs.append(("Business Management", "../business-management/index.html" if depth == 0 else "../index.html"))
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
    print(f"✓ expertise/business-management/{slug}.html")


if __name__ == "__main__":
    print("Business management builder loaded.")
