#!/usr/bin/env python3
"""Builder for the Insurance Agent Claude Playbook (interactive)."""
from pathlib import Path

SITE = Path(__file__).parent
YEAR = 2026
LINKEDIN = "https://www.linkedin.com/in/samuelochoa"

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'

MODULES = [
    ("index", "Start here", "Overview"),
    ("module-01", "Why Claude for insurance marketing", "Module 1"),
    ("module-02", "Setting up Claude", "Module 2"),
    ("module-03", "The 10 prompt patterns", "Module 3"),
    ("module-04", "Prospecting emails", "Module 4"),
    ("module-05", "Social media content", "Module 5"),
    ("module-06", "Blog posts + SEO", "Module 6"),
    ("module-07", "Video scripts", "Module 7"),
    ("module-08", "Direct mail", "Module 8"),
    ("module-09", "Referral requests", "Module 9"),
    ("module-10", "Review responses", "Module 10"),
    ("module-11", "Newsletter content", "Module 11"),
    ("module-12", "Facebook + Google ads", "Module 12"),
    ("module-13", "Client education material", "Module 13"),
    ("module-14", "The weekly marketing system", "Module 14"),
    ("module-15", "Compliance checklist", "Module 15"),
    ("prompt-library", "Prompt library", "Library"),
]


PLAYBOOK_CSS = """
<style>
/* Playbook-specific styles */
.playbook-layout {
    display: grid;
    grid-template-columns: 280px 1fr;
    gap: 0;
    min-height: calc(100vh - 80px);
    max-width: 1400px;
    margin: 0 auto;
    background: #fff;
}
.playbook-sidebar {
    background: #fafafa;
    border-right: 1px solid #e5e5ea;
    padding: 32px 24px;
    position: sticky;
    top: 80px;
    height: calc(100vh - 80px);
    overflow-y: auto;
}
.playbook-sidebar h4 {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: var(--gray-500, #8e8e93);
    margin: 0 0 12px 0;
}
.playbook-progress {
    background: #fff;
    border: 1px solid #e5e5ea;
    border-radius: 6px;
    padding: 14px;
    margin-bottom: 24px;
}
.playbook-progress-bar {
    height: 6px;
    background: #f0f0f5;
    border-radius: 3px;
    overflow: hidden;
    margin-top: 8px;
}
.playbook-progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #4a00e0, #7c3aed);
    transition: width 0.3s;
}
.playbook-progress-text {
    font-size: 12px;
    color: var(--gray-500, #666);
    display: flex;
    justify-content: space-between;
}
.playbook-progress-text strong {
    color: #4a00e0;
}
.playbook-sidebar ul {
    list-style: none;
    padding: 0;
    margin: 0 0 24px 0;
}
.playbook-sidebar li {
    margin: 2px 0;
}
.playbook-sidebar a {
    display: flex;
    align-items: center;
    padding: 8px 12px;
    font-size: 14px;
    color: #333;
    text-decoration: none;
    border-radius: 6px;
    transition: all 0.15s;
    position: relative;
}
.playbook-sidebar a:hover {
    background: #fff;
    color: #4a00e0;
}
.playbook-sidebar a.active {
    background: #4a00e0;
    color: #fff;
    font-weight: 500;
}
.playbook-sidebar a.completed::before {
    content: "✓";
    margin-right: 8px;
    color: #10b981;
    font-weight: 700;
}
.playbook-sidebar a.active.completed::before {
    color: #fff;
}
.playbook-content {
    padding: 48px 56px;
    max-width: 820px;
}
.playbook-header {
    margin-bottom: 48px;
    padding-bottom: 24px;
    border-bottom: 1px solid #e5e5ea;
}
.playbook-module-label {
    display: inline-block;
    background: #f3f0ff;
    color: #4a00e0;
    padding: 4px 12px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 12px;
}
.playbook-content h1.title {
    font-size: 36px;
    line-height: 1.2;
    margin: 0 0 8px 0;
}
.playbook-subtitle {
    font-size: 18px;
    color: var(--gray-500, #666);
    margin: 0;
}
.playbook-content h2 {
    font-size: 24px;
    margin: 40px 0 16px 0;
    padding-top: 8px;
}
.playbook-content h3 {
    font-size: 18px;
    margin: 28px 0 12px 0;
}
.playbook-content p, .playbook-content li {
    font-size: 16px;
    line-height: 1.7;
}
.playbook-content ul, .playbook-content ol {
    padding-left: 24px;
}
.playbook-content li {
    margin: 6px 0;
}

/* Prompt template blocks */
.prompt-box {
    background: #1a1a2e;
    color: #e4e4e7;
    border-radius: 10px;
    padding: 20px 24px;
    margin: 20px 0;
    position: relative;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13.5px;
    line-height: 1.6;
    overflow: hidden;
}
.prompt-box pre {
    margin: 0;
    white-space: pre-wrap;
    word-wrap: break-word;
    font-family: inherit;
    font-size: inherit;
    line-height: inherit;
}
.prompt-box-label {
    display: inline-block;
    background: #4a00e0;
    color: #fff;
    padding: 3px 10px;
    border-radius: 4px;
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 12px;
    font-family: 'Inter', sans-serif;
}
.copy-btn {
    position: absolute;
    top: 16px;
    right: 16px;
    background: rgba(255,255,255,0.1);
    color: #fff;
    border: 1px solid rgba(255,255,255,0.2);
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 12px;
    cursor: pointer;
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    transition: all 0.15s;
}
.copy-btn:hover {
    background: rgba(255,255,255,0.2);
    border-color: rgba(255,255,255,0.35);
}
.copy-btn.copied {
    background: #10b981;
    border-color: #10b981;
}

/* Callout boxes */
.callout {
    background: #f3f0ff;
    border-left: 4px solid #4a00e0;
    padding: 16px 20px;
    margin: 20px 0;
    border-radius: 0 8px 8px 0;
}
.callout.warning {
    background: #fff7ed;
    border-left-color: #f97316;
}
.callout.success {
    background: #f0fdf4;
    border-left-color: #10b981;
}
.callout-title {
    font-weight: 700;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 6px;
    color: #4a00e0;
}
.callout.warning .callout-title {
    color: #ea580c;
}
.callout.success .callout-title {
    color: #059669;
}
.callout p {
    margin: 0 0 8px 0;
}
.callout p:last-child {
    margin-bottom: 0;
}

/* Insurance-type tabs */
.tabs {
    display: flex;
    gap: 4px;
    margin: 24px 0 16px;
    border-bottom: 2px solid #e5e5ea;
    padding-bottom: 0;
    overflow-x: auto;
}
.tab-btn {
    background: none;
    border: none;
    padding: 10px 18px;
    font-size: 14px;
    font-weight: 500;
    color: #666;
    cursor: pointer;
    position: relative;
    font-family: inherit;
    white-space: nowrap;
}
.tab-btn:hover { color: #4a00e0; }
.tab-btn.active {
    color: #4a00e0;
    font-weight: 600;
}
.tab-btn.active::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    right: 0;
    height: 2px;
    background: #4a00e0;
}
.tab-content { display: none; }
.tab-content.active { display: block; }

/* Expandable sections */
.expandable {
    border: 1px solid #e5e5ea;
    border-radius: 8px;
    margin: 12px 0;
    overflow: hidden;
}
.expandable-toggle {
    width: 100%;
    background: #fafafa;
    border: none;
    padding: 14px 18px;
    font-size: 15px;
    font-weight: 500;
    text-align: left;
    cursor: pointer;
    font-family: inherit;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.expandable-toggle:hover { background: #f0f0f5; }
.expandable-toggle::after {
    content: '+';
    font-size: 22px;
    font-weight: 400;
    color: #4a00e0;
    transition: transform 0.2s;
}
.expandable.open .expandable-toggle::after {
    transform: rotate(45deg);
}
.expandable-body {
    display: none;
    padding: 16px 18px;
}
.expandable.open .expandable-body { display: block; }

/* Checklist with persistence */
.checklist {
    background: #fafafa;
    border: 1px solid #e5e5ea;
    border-radius: 8px;
    padding: 20px 24px;
    margin: 24px 0;
}
.checklist-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 6px 0;
    cursor: pointer;
}
.checklist-item input[type=checkbox] {
    margin-top: 4px;
    width: 18px;
    height: 18px;
    accent-color: #4a00e0;
    cursor: pointer;
    flex-shrink: 0;
}
.checklist-item label {
    cursor: pointer;
    font-size: 15px;
    line-height: 1.6;
    user-select: none;
}
.checklist-item input[type=checkbox]:checked + label {
    color: #8e8e93;
    text-decoration: line-through;
}

/* Module complete button */
.module-complete {
    margin-top: 48px;
    padding-top: 24px;
    border-top: 1px solid #e5e5ea;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    flex-wrap: wrap;
}
.btn-complete {
    background: #4a00e0;
    color: #fff;
    border: none;
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    font-family: inherit;
    transition: all 0.15s;
}
.btn-complete:hover { background: #3b0a8a; }
.btn-complete.done {
    background: #10b981;
    cursor: default;
}
.module-nav {
    display: flex;
    gap: 12px;
}
.module-nav a {
    padding: 10px 16px;
    border: 1px solid #e5e5ea;
    border-radius: 8px;
    color: #333;
    text-decoration: none;
    font-size: 14px;
    font-weight: 500;
}
.module-nav a:hover {
    border-color: #4a00e0;
    color: #4a00e0;
}

/* Search + filter for prompt library */
.library-search {
    display: flex;
    gap: 12px;
    margin: 24px 0;
    flex-wrap: wrap;
}
.library-search input {
    flex: 1;
    min-width: 240px;
    padding: 12px 16px;
    border: 1px solid #e5e5ea;
    border-radius: 8px;
    font-size: 15px;
    font-family: inherit;
}
.library-filter {
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
    margin: 16px 0 24px;
}
.filter-chip {
    background: #fff;
    border: 1px solid #e5e5ea;
    color: #333;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 13px;
    cursor: pointer;
    font-family: inherit;
    font-weight: 500;
}
.filter-chip:hover { border-color: #4a00e0; color: #4a00e0; }
.filter-chip.active {
    background: #4a00e0;
    color: #fff;
    border-color: #4a00e0;
}
.library-prompt {
    border: 1px solid #e5e5ea;
    border-radius: 10px;
    padding: 20px;
    margin: 16px 0;
    background: #fff;
}
.library-prompt.hidden { display: none; }
.library-prompt-title {
    font-size: 17px;
    font-weight: 600;
    margin: 0 0 4px 0;
}
.library-prompt-meta {
    display: flex;
    gap: 8px;
    font-size: 12px;
    color: #666;
    margin-bottom: 12px;
    flex-wrap: wrap;
}
.library-tag {
    background: #f3f0ff;
    color: #4a00e0;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 600;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.library-count {
    color: #666;
    font-size: 14px;
    margin-bottom: 16px;
}

/* Hero / landing */
.playbook-hero {
    background: linear-gradient(135deg, #4a00e0 0%, #7c3aed 100%);
    color: #fff;
    padding: 64px 56px;
    margin: -48px -56px 48px -56px;
    border-radius: 0;
}
.playbook-hero h1 {
    font-size: 42px;
    margin: 0 0 12px 0;
    color: #fff;
    line-height: 1.15;
}
.playbook-hero-subtitle {
    font-size: 20px;
    opacity: 0.95;
    max-width: 600px;
}
.playbook-hero-stats {
    display: flex;
    gap: 32px;
    margin-top: 32px;
    flex-wrap: wrap;
}
.playbook-stat strong {
    display: block;
    font-size: 28px;
    font-weight: 800;
    line-height: 1;
}
.playbook-stat span {
    font-size: 13px;
    opacity: 0.85;
    text-transform: uppercase;
    letter-spacing: 1px;
}

@media (max-width: 900px) {
    .playbook-layout { grid-template-columns: 1fr; }
    .playbook-sidebar {
        position: static;
        height: auto;
        border-right: none;
        border-bottom: 1px solid #e5e5ea;
    }
    .playbook-content { padding: 32px 24px; }
    .playbook-hero { padding: 40px 24px; margin: -32px -24px 32px -24px; }
    .playbook-hero h1 { font-size: 30px; }
}
</style>
"""


PLAYBOOK_JS = """
<script>
(function(){
    const STORAGE_KEY = 'insurance_playbook_progress_v1';
    const CHECKBOX_KEY = 'insurance_playbook_checks_v1';

    function getProgress() {
        try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}'); }
        catch { return {}; }
    }
    function setProgress(p) {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(p));
    }
    function getChecks() {
        try { return JSON.parse(localStorage.getItem(CHECKBOX_KEY) || '{}'); }
        catch { return {}; }
    }
    function setChecks(c) {
        localStorage.setItem(CHECKBOX_KEY, JSON.stringify(c));
    }

    // Update sidebar indicators on load
    function updateSidebar() {
        const progress = getProgress();
        document.querySelectorAll('.playbook-sidebar a[data-module]').forEach(a => {
            const mod = a.dataset.module;
            if (progress[mod]) a.classList.add('completed');
            else a.classList.remove('completed');
        });
        // Progress bar
        const total = document.querySelectorAll('.playbook-sidebar a[data-module]').length - 2; // minus index + library
        const done = Object.keys(progress).filter(k => k.startsWith('module-')).length;
        const fill = document.querySelector('.playbook-progress-fill');
        const text = document.querySelector('.playbook-progress-text strong');
        if (fill && total > 0) {
            const pct = Math.min(100, Math.round((done / total) * 100));
            fill.style.width = pct + '%';
        }
        if (text) text.textContent = done + ' / ' + total;
    }

    // Copy to clipboard
    function setupCopy() {
        document.querySelectorAll('.copy-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                const box = btn.closest('.prompt-box');
                const text = box.querySelector('pre').innerText;
                navigator.clipboard.writeText(text).then(() => {
                    const old = btn.textContent;
                    btn.textContent = '✓ Copied';
                    btn.classList.add('copied');
                    setTimeout(() => {
                        btn.textContent = old;
                        btn.classList.remove('copied');
                    }, 1800);
                });
            });
        });
    }

    // Tabs
    function setupTabs() {
        document.querySelectorAll('.tabs').forEach(group => {
            const buttons = group.querySelectorAll('.tab-btn');
            const containerSelector = group.dataset.target || '.tab-group-' + group.dataset.group;
            buttons.forEach(btn => {
                btn.addEventListener('click', function() {
                    const target = btn.dataset.tab;
                    buttons.forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');
                    const parent = document.querySelector(containerSelector) || group.parentElement;
                    parent.querySelectorAll('.tab-content').forEach(c => {
                        c.classList.toggle('active', c.dataset.tab === target);
                    });
                });
            });
        });
    }

    // Expandable sections
    function setupExpandables() {
        document.querySelectorAll('.expandable-toggle').forEach(t => {
            t.addEventListener('click', function() {
                t.closest('.expandable').classList.toggle('open');
            });
        });
    }

    // Checklist persistence
    function setupChecklists() {
        const checks = getChecks();
        document.querySelectorAll('.checklist-item input[type=checkbox]').forEach(cb => {
            const key = cb.dataset.key;
            if (key && checks[key]) cb.checked = true;
            cb.addEventListener('change', function() {
                const c = getChecks();
                if (cb.checked) c[key] = true; else delete c[key];
                setChecks(c);
            });
        });
    }

    // Module complete button
    function setupCompleteButton() {
        const btn = document.querySelector('.btn-complete');
        if (!btn) return;
        const mod = btn.dataset.module;
        const progress = getProgress();
        if (progress[mod]) {
            btn.textContent = '✓ Completed';
            btn.classList.add('done');
        }
        btn.addEventListener('click', function() {
            const p = getProgress();
            if (!p[mod]) {
                p[mod] = Date.now();
                setProgress(p);
                btn.textContent = '✓ Completed';
                btn.classList.add('done');
                updateSidebar();
            }
        });
    }

    // Library search + filter
    function setupLibrary() {
        const search = document.getElementById('library-search-input');
        const chips = document.querySelectorAll('.filter-chip');
        const prompts = document.querySelectorAll('.library-prompt');
        const count = document.querySelector('.library-count');
        let activeTag = 'all';

        function apply() {
            const q = (search?.value || '').toLowerCase().trim();
            let shown = 0;
            prompts.forEach(p => {
                const tags = (p.dataset.tags || '').toLowerCase();
                const text = p.textContent.toLowerCase();
                const matchTag = activeTag === 'all' || tags.includes(activeTag);
                const matchSearch = !q || text.includes(q);
                const visible = matchTag && matchSearch;
                p.classList.toggle('hidden', !visible);
                if (visible) shown++;
            });
            if (count) count.textContent = shown + ' prompt' + (shown === 1 ? '' : 's');
        }

        if (search) search.addEventListener('input', apply);
        chips.forEach(c => {
            c.addEventListener('click', function() {
                chips.forEach(x => x.classList.remove('active'));
                c.classList.add('active');
                activeTag = c.dataset.tag;
                apply();
            });
        });
        apply();
    }

    document.addEventListener('DOMContentLoaded', function() {
        updateSidebar();
        setupCopy();
        setupTabs();
        setupExpandables();
        setupChecklists();
        setupCompleteButton();
        setupLibrary();
    });
})();
</script>
"""


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
{PLAYBOOK_CSS}
</head>
<body>'''


def topbar(rel_root):
    return f'''<nav class="topbar"><div class="topbar-inner">
<a href="{rel_root}index.html" class="logo"><span class="dot"></span>Samuel Ochoa</a>
<div class="nav-links">
<a href="{rel_root}index.html">Home</a>
<a href="{rel_root}framework/index.html">Framework</a>
<a href="{rel_root}expertise/index.html">Expertise</a>
<a href="{rel_root}playbooks/insurance/index.html" class="active">Playbooks</a>
<a href="{rel_root}writing.html">Writing</a>
<a href="{rel_root}contact.html">Contact</a>
</div>
</div></nav>'''


def sidebar_html(active_slug):
    parts = ['<aside class="playbook-sidebar">']
    parts.append('''
<div class="playbook-progress">
    <h4>Your progress</h4>
    <div class="playbook-progress-text"><span>Modules done</span><strong>0 / 15</strong></div>
    <div class="playbook-progress-bar"><div class="playbook-progress-fill" style="width:0%"></div></div>
</div>
''')
    parts.append('<h4>Modules</h4><ul>')
    for slug, label, _tag in MODULES:
        if slug == "prompt-library": continue
        href = "index.html" if slug == "index" else f"{slug}.html"
        active_cls = ' active' if slug == active_slug else ''
        parts.append(f'<li><a href="{href}" class="{active_cls.strip()}" data-module="{slug}">{label}</a></li>')
    parts.append('</ul>')
    parts.append('<h4>Resources</h4><ul>')
    href = "prompt-library.html"
    active_cls = ' active' if active_slug == "prompt-library" else ''
    parts.append(f'<li><a href="{href}" class="{active_cls.strip()}" data-module="prompt-library">📚 Prompt library</a></li>')
    parts.append('</ul>')
    parts.append('</aside>')
    return "".join(parts)


def footer(rel_root):
    return f'''<footer><div class="container">
<p>&copy; {YEAR} Samuel Ochoa &middot; <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></p>
</div></footer>
{PLAYBOOK_JS}
</body></html>'''


def module_nav_links(current_slug):
    slugs = [s for s, _, _ in MODULES if s not in ("index", "prompt-library")]
    if current_slug not in slugs:
        return None, None
    i = slugs.index(current_slug)
    prev_slug = slugs[i - 1] if i > 0 else None
    next_slug = slugs[i + 1] if i < len(slugs) - 1 else None
    prev = (next((l for s, l, _ in MODULES if s == prev_slug), None), f"{prev_slug}.html") if prev_slug else None
    nxt = (next((l for s, l, _ in MODULES if s == next_slug), None), f"{next_slug}.html") if next_slug else None
    return prev, nxt


def write_playbook_page(slug, title, tag, subtitle, body_html, hero=False):
    rel_root = "../../"
    if slug == "index":
        path = SITE / "playbooks" / "insurance" / "index.html"
    else:
        path = SITE / "playbooks" / "insurance" / f"{slug}.html"
    path.parent.mkdir(parents=True, exist_ok=True)

    header_html = ""
    if hero:
        header_html = f'''<div class="playbook-hero">
<h1>{title}</h1>
<p class="playbook-hero-subtitle">{subtitle}</p>
<div class="playbook-hero-stats">
<div class="playbook-stat"><strong>15</strong><span>Modules</span></div>
<div class="playbook-stat"><strong>60+</strong><span>Prompt templates</span></div>
<div class="playbook-stat"><strong>5</strong><span>Insurance lines</span></div>
<div class="playbook-stat"><strong>0</strong><span>Fluff</span></div>
</div>
</div>'''
    else:
        header_html = f'''<div class="playbook-header">
<span class="playbook-module-label">{tag}</span>
<h1 class="title">{title}</h1>
<p class="playbook-subtitle">{subtitle}</p>
</div>'''

    # Module complete button + nav
    footer_parts = []
    if slug not in ("index", "prompt-library"):
        prev, nxt = module_nav_links(slug)
        complete_btn = f'<button class="btn-complete" data-module="{slug}">Mark module complete</button>'
        nav = '<div class="module-nav">'
        if prev: nav += f'<a href="{prev[1]}">← {prev[0]}</a>'
        if nxt: nav += f'<a href="{nxt[1]}">{nxt[0]} →</a>'
        nav += '</div>'
        footer_parts.append(f'<div class="module-complete">{complete_btn}{nav}</div>')

    html = (
        head(f"{title} | Insurance Agent Playbook", subtitle, rel_root=rel_root) +
        topbar(rel_root) +
        '<div class="playbook-layout">' +
        sidebar_html(slug) +
        '<div class="playbook-content">' +
        header_html +
        body_html +
        "".join(footer_parts) +
        '</div></div>' +
        footer(rel_root)
    )
    path.write_text(html, encoding="utf-8")
    print(f"✓ playbooks/insurance/{slug}.html")


if __name__ == "__main__":
    print("Insurance playbook builder loaded.")
