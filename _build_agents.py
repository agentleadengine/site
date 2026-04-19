#!/usr/bin/env python3
"""Builder for the AI Agents expertise section."""
from pathlib import Path

SITE = Path(__file__).parent
YEAR = 2026

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'

SIDEBAR = [
    ("Foundations", [
        ("index", "Overview"),
        ("foundations/what-is-an-agent", "What is an AI agent?"),
        ("foundations/agent-vs-workflow", "Agent vs workflow"),
        ("foundations/when-not-to-use", "When not to use agents"),
        ("foundations/architecture", "The agent architecture map"),
    ]),
    ("Loops + Reasoning", [
        ("loops/react", "ReAct"),
        ("loops/tool-use", "Tool use"),
        ("loops/planning", "Planning loops"),
        ("loops/reflection", "Reflection"),
        ("loops/self-correction", "Self-correction"),
    ]),
    ("Tools + Actions", [
        ("tools/tool-design", "Tool design"),
        ("tools/tool-descriptions", "Tool descriptions matter"),
        ("tools/error-handling", "Tool error handling"),
        ("tools/parallel-tools", "Parallel tool calls"),
        ("tools/tool-budgets", "Tool budgets + limits"),
    ]),
    ("Memory", [
        ("memory/short-term", "Short-term memory"),
        ("memory/long-term", "Long-term memory"),
        ("memory/episodic", "Episodic memory"),
        ("memory/procedural", "Procedural memory"),
        ("memory/memory-systems", "Memory system design"),
    ]),
    ("Multi-agent", [
        ("multi/orchestrator-worker", "Orchestrator-worker"),
        ("multi/peer-agents", "Peer agents"),
        ("multi/debate", "Debate + consensus"),
        ("multi/handoffs", "Agent handoffs"),
        ("multi/routing", "Agent routing"),
    ]),
    ("Evaluation", [
        ("eval/why-eval-agents", "Why eval agents"),
        ("eval/task-completion", "Task completion"),
        ("eval/trajectory-eval", "Trajectory evaluation"),
        ("eval/regression", "Regression testing"),
    ]),
    ("Production", [
        ("prod/observability", "Observability + tracing"),
        ("prod/cost-control", "Cost control"),
        ("prod/latency", "Latency optimization"),
        ("prod/safety", "Safety + guardrails"),
        ("prod/human-in-loop", "Human-in-the-loop"),
    ]),
    ("Patterns", [
        ("patterns/research-agent", "Research agent"),
        ("patterns/coding-agent", "Coding agent"),
        ("patterns/customer-support", "Customer support agent"),
        ("patterns/data-analyst", "Data analyst agent"),
        ("patterns/browser-agent", "Browser agent"),
        ("patterns/email-agent", "Email agent"),
    ]),
    ("Frameworks", [
        ("frameworks/claude-agent-sdk", "Claude Agent SDK"),
        ("frameworks/langgraph", "LangGraph"),
        ("frameworks/crewai", "CrewAI"),
        ("frameworks/autogen", "AutoGen"),
        ("frameworks/picking", "Picking a framework"),
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


def sidebar_html(active_slug):
    parts = ['<aside class="framework-sidebar">']
    total = sum(len(items) for _, items in SIDEBAR)
    parts.append(f'<h4>AI Agents ({total} pages)</h4>')
    for section, items in SIDEBAR:
        parts.append(f'<h4>{section}</h4><ul>')
        for slug, label in items:
            href = "index.html" if slug == "index" else f"{slug}.html"
            active = slug == active_slug
            cls = ' class="active"' if active else ''
            parts.append(f'<li><a href="{href}"{cls}>{label}</a></li>')
        parts.append('</ul>')
    parts.append('</aside>')
    return "".join(parts)


def write_page(slug, title, description, body_html, reading_time=None, prev=None, nxt=None):
    depth = slug.count("/")
    rel_root = "../" * (depth + 2)
    if slug == "index":
        path = SITE / "expertise" / "agents" / "index.html"
    else:
        path = SITE / "expertise" / "agents" / f"{slug}.html"
    path.parent.mkdir(parents=True, exist_ok=True)

    crumbs = [("Home", rel_root + "index.html"), ("Expertise", "../index.html")]
    if slug == "index":
        crumbs.append(("AI Agents", None))
    else:
        crumbs.append(("AI Agents", "../agents/index.html" if depth == 0 else "../index.html"))
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
    meta_parts.append(f'<span>Updated 2026-04-19</span>')
    meta_html = '<div class="article-meta">' + "".join(meta_parts) + '</div>'

    pn_html = ""
    if prev or nxt:
        pn = ['<div class="prev-next">']
        if prev: pn.append(f'<a href="{prev[1]}" class="prev"><div class="label">← Previous</div><div class="title">{prev[0]}</div></a>')
        if nxt: pn.append(f'<a href="{nxt[1]}" class="next"><div class="label">Next →</div><div class="title">{nxt[0]}</div></a>')
        pn.append('</div>')
        pn_html = "".join(pn)

    active_slug = "index" if slug == "index" else slug

    html = (
        head(f"{title} | Samuel Ochoa", description, rel_root=rel_root) +
        topbar(rel_root=rel_root) +
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
    print(f"✓ expertise/agents/{slug}.html")
