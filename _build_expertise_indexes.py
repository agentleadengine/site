#!/usr/bin/env python3
"""Generate index.html for every expertise/<section>/<subsection>/ that lacks one.

Each generated page lists child HTML files as cards with title + intro snippet.
Nav markup is added by _rebuild_nav.py afterwards.
"""
import re
from pathlib import Path
import html as htmllib

ROOT = Path("/Users/ble/Desktop/sams site")
EXPERTISE = ROOT / "expertise"

SECTION_LABELS = {
    "seo": "SEO",
    "agents": "AI Agents",
    "rag": "RAG",
    "direct-response": "Direct Response",
    "paid-ads": "Paid Advertising",
    "cold-email": "Cold Email",
    "growth-marketing": "Growth Marketing",
    "email-marketing": "Email Marketing",
    "cro": "CRO",
    "business-management": "Business Management",
}

SUB_LABELS = {
    # SEO
    "foundations": "Foundations", "keywords": "Keyword Research", "on-page": "On-Page",
    "technical": "Technical SEO", "links": "Link Building", "content": "Content SEO",
    "local": "Local SEO", "international": "International", "ecommerce": "Ecommerce SEO",
    "advanced": "Advanced", "analytics": "Analytics",
    # Agents
    "frameworks": "Frameworks", "patterns": "Patterns", "tools": "Tool Use",
    "memory": "Memory", "loops": "Agent Loops", "multi": "Multi-Agent",
    "eval": "Evaluation", "prod": "Production",
    # RAG
    "embeddings": "Embeddings", "vectors": "Vector Stores", "chunking": "Chunking",
    "retrieval": "Retrieval", "docs": "Documents", "cases": "Case Studies",
    # Direct response
    "market": "The Market", "offer": "The Offer", "copy": "Copywriting",
    "letters": "Sales Letters", "leads": "Lead Generation", "followup": "Follow-Up",
    "testing": "Testing", "scaling": "Scaling",
    # Paid ads
    "creative": "Creative", "meta": "Meta Ads", "google": "Google Ads",
    "youtube": "YouTube Ads", "tiktok": "TikTok Ads", "linkedin": "LinkedIn Ads",
    "measurement": "Measurement",
    # Cold email
    "infra": "Infrastructure", "deliverability": "Deliverability",
    "lists": "List Building", "sequences": "Sequences", "plays": "Plays",
    # Growth
    "acq": "Acquisition", "activation": "Activation", "retention": "Retention",
    "revenue": "Revenue", "experiments": "Experiments", "process": "Process",
    # Email marketing
    "list": "List Growth", "broadcasts": "Broadcasts",
    "automations": "Automations", "commerce": "Commerce", "saas": "SaaS",
    # CRO
    "research": "Research", "pages": "Landing Pages", "conversion": "Conversion Copy",
    # Business management
    "strategy": "Strategy", "operating-systems": "Operating Systems",
    "leadership": "Leadership", "people": "People", "execution": "Execution",
    "sales": "Sales", "finance": "Finance", "risk": "Risk",
}

TITLE_RE = re.compile(r"<title>([^<]+)</title>", re.IGNORECASE)
DESC_RE = re.compile(r'<meta\s+name="description"\s+content="([^"]+)"', re.IGNORECASE)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.IGNORECASE | re.DOTALL)


def extract_card(path: Path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    title = None
    m = TITLE_RE.search(text)
    if m:
        title = m.group(1).split("|")[0].strip()
    if not title:
        m = H1_RE.search(text)
        if m:
            title = re.sub(r"<[^>]+>", "", m.group(1)).strip()
    if not title:
        title = path.stem.replace("-", " ").title()
    desc = ""
    m = DESC_RE.search(text)
    if m:
        desc = m.group(1).strip()
    return title, desc


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Samuel Ochoa</title>
<meta name="description" content="{meta_desc}">
<meta name="author" content="Samuel Ochoa">
<meta property="og:type" content="article">
<meta property="og:title" content="{title} | Samuel Ochoa">
<meta property="og:description" content="{meta_desc}">
<meta property="og:site_name" content="Samuel Ochoa">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}styles.css">
<link rel="icon" type="image/png" href="{root}logo.png">
</head>
<body>
<nav class="topbar"><div class="topbar-inner">
<a href="{root}index.html" class="logo"><img class="brand-logo" src="{root}logo.png" alt="Samuel Ochoa"></a>
<div class="nav-links"><a href="{root}index.html">Home</a></div>
</div></nav>

<section class="hero hero-compact" style="padding:60px 0 40px;">
<div class="container">
<p class="eyebrow" style="color:var(--primary-purple); font-weight:700; letter-spacing:0.15em; text-transform:uppercase; font-size:13px;"><a href="{root}expertise/index.html" style="color:inherit;">Expertise</a> / <a href="{root}expertise/{section}/index.html" style="color:inherit;">{section_label}</a></p>
<h1 style="margin:12px 0 16px;">{title}.</h1>
<p class="lead" style="max-width:720px;">{lead}</p>
</div>
</section>

<section class="block">
<div class="container">
<div class="cards">
{cards}
</div>
</div>
</section>

<footer>
<div class="container">
<p>&copy; 2026 Samuel Ochoa. <a href="{root}index.html">Home</a> . <a href="{root}expertise/index.html">Expertise</a> . <a href="{root}contact.html">Contact</a></p>
</div>
</footer>
</body>
</html>
"""


def build():
    created = 0
    for section_dir in sorted(EXPERTISE.iterdir()):
        if not section_dir.is_dir():
            continue
        section = section_dir.name
        section_label = SECTION_LABELS.get(section, section.replace("-", " ").title())

        for sub_dir in sorted(section_dir.iterdir()):
            if not sub_dir.is_dir():
                continue
            idx = sub_dir / "index.html"
            if idx.exists():
                continue

            sub_label = SUB_LABELS.get(sub_dir.name, sub_dir.name.replace("-", " ").title())
            root = "../../../"  # three levels up to site root
            children = sorted(p for p in sub_dir.glob("*.html") if p.name != "index.html")

            if not children:
                continue

            card_html_parts = []
            for child in children:
                ctitle, cdesc = extract_card(child)
                ctitle_e = htmllib.escape(ctitle)
                cdesc_e = htmllib.escape(cdesc or "Read the guide.")
                card_html_parts.append(
                    f'<a href="{child.name}" class="card"><h3>{ctitle_e}</h3><p>{cdesc_e}</p></a>'
                )
            cards = "\n".join(card_html_parts)

            lead = f"Every page in the {sub_label.lower()} section of my {section_label.lower()} knowledge base."
            meta_desc = f"{sub_label} guides in the {section_label} knowledge base by Samuel Ochoa. {len(children)} in-depth pages."

            page = PAGE_TEMPLATE.format(
                title=htmllib.escape(sub_label),
                section=section,
                section_label=htmllib.escape(section_label),
                root=root,
                cards=cards,
                lead=htmllib.escape(lead),
                meta_desc=htmllib.escape(meta_desc),
            )
            idx.write_text(page, encoding="utf-8")
            created += 1

    print(f"Created {created} expertise subsection index pages")


if __name__ == "__main__":
    build()
