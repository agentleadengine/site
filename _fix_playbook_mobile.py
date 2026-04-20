#!/usr/bin/env python3
"""Make playbook index pages fit on a phone screen without endless scrolling.

Strategy (pure CSS/JS, no HTML content rewrites needed):
- On mobile, reorder so content shows before sidebar
- Compress the hero to ~1/3 its height
- Show the 15 modules as a 2-col card grid (not a plain list)
- Inject a prominent "Start Module 1" CTA right under the hero
- Collapse the long intro prose (h2 + following until next h2) behind
  a single "Read the full intro" toggle - text is still there, just out
  of the way

Applies to: playbooks/<pro>/index.html (15 files)
"""
from pathlib import Path

ROOT = Path("/Users/ble/Desktop/sams site")
PLAYBOOKS = ROOT / "playbooks"

MOBILE_CSS = """
/* === mobile compression (injected) === */
@media (max-width: 900px) {
    .playbook-layout {
        display: flex !important;
        flex-direction: column !important;
        grid-template-columns: 1fr !important;
        min-height: 0;
    }
    .playbook-content { order: 1 !important; padding: 16px !important; }
    .playbook-sidebar {
        order: 2 !important;
        position: static !important;
        height: auto !important;
        border-right: none !important;
        border-top: 1px solid #e5e5ea;
        padding: 20px 16px 32px !important;
        background: #fafafa !important;
    }
    /* Compact hero */
    .playbook-hero {
        padding: 22px 18px !important;
        margin: 0 0 16px 0 !important;
        border-radius: 14px !important;
    }
    .playbook-hero h1 {
        font-size: 22px !important;
        line-height: 1.2 !important;
        margin: 0 0 6px !important;
    }
    .playbook-hero-subtitle {
        font-size: 13px !important;
        line-height: 1.5 !important;
        margin-bottom: 12px !important;
    }
    .playbook-hero-stats { gap: 10px 14px !important; flex-wrap: wrap !important; }
    .playbook-hero-stats .playbook-stat strong { font-size: 20px !important; }
    .playbook-hero-stats .playbook-stat span { font-size: 10px !important; }

    /* Primary CTA right under hero */
    .playbook-content .mobile-start-cta {
        display: block;
        background: linear-gradient(135deg, #4a00e0, #7c3aed);
        color: #fff !important;
        text-align: center;
        padding: 14px 20px;
        border-radius: 10px;
        font-weight: 700;
        font-size: 14px;
        letter-spacing: 0.02em;
        text-decoration: none !important;
        margin: 0 0 20px 0;
        box-shadow: 0 8px 20px -6px rgba(74,0,224,0.4);
    }
    /* Show it only on mobile */
    .playbook-content .mobile-start-cta { display: block; }

    /* Collapsible intro prose: everything from first h2 onward,
       hidden by default; toggle button reveals. */
    .playbook-details-wrapper { margin-top: 24px; }
    .playbook-details-toggle {
        display: block;
        width: 100%;
        background: #fff;
        border: 1px solid #e5e5ea;
        padding: 12px 16px;
        border-radius: 10px;
        font-weight: 600;
        font-size: 13px;
        color: #4a00e0;
        cursor: pointer;
        text-align: left;
        font-family: inherit;
    }
    .playbook-details-toggle::after {
        content: ' ▸';
        font-weight: 400;
        color: #a1a1aa;
    }
    .playbook-details-wrapper.is-open .playbook-details-toggle::after { content: ' ▾'; }
    .playbook-details-body { display: none; padding-top: 16px; }
    .playbook-details-wrapper.is-open .playbook-details-body { display: block; }

    /* Sidebar modules as a 2-col card grid on mobile */
    .playbook-sidebar h4 { margin-top: 20px; font-size: 10px; }
    .playbook-sidebar h4:first-child { margin-top: 0; }
    .playbook-sidebar .playbook-progress { margin-bottom: 16px; padding: 12px; }
    .playbook-sidebar ul {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px !important;
        padding: 0;
        list-style: none;
    }
    .playbook-sidebar li { margin: 0 !important; }
    .playbook-sidebar li a {
        display: block;
        background: #fff;
        border: 1px solid #e5e5ea;
        padding: 12px 12px !important;
        border-radius: 10px;
        font-size: 12.5px;
        line-height: 1.3;
        min-height: 64px;
    }
    .playbook-sidebar li a.active {
        background: #4a00e0 !important;
        color: #fff !important;
        border-color: #4a00e0;
    }
}

/* Desktop: keep the mobile-only elements hidden */
@media (min-width: 901px) {
    .mobile-start-cta { display: none !important; }
    .playbook-details-toggle { display: none !important; }
    .playbook-details-body { display: contents; } /* Show all content normally on desktop */
}
"""

JS_SNIPPET = """<script>
(function(){
    // Wrap everything from the first <h2> onward in a collapsible block on mobile
    var content = document.querySelector('.playbook-content');
    if (!content) return;

    // Find all children, locate first h2
    var children = Array.from(content.children);
    var firstH2Idx = children.findIndex(function(el) { return el.tagName === 'H2'; });
    if (firstH2Idx === -1) return;

    // Insert mobile CTA before first h2 if we can find a module-01 link nearby
    var hero = content.querySelector('.playbook-hero');
    var firstModule = document.querySelector('.playbook-sidebar a[href^="module-01"]');
    if (hero && firstModule && !content.querySelector('.mobile-start-cta')) {
        var cta = document.createElement('a');
        cta.className = 'mobile-start-cta';
        cta.href = firstModule.getAttribute('href');
        cta.textContent = 'Start Module 1 →';
        hero.insertAdjacentElement('afterend', cta);
    }

    // Wrap h2 + all following siblings in a details wrapper
    if (!content.querySelector('.playbook-details-wrapper')) {
        var wrapper = document.createElement('div');
        wrapper.className = 'playbook-details-wrapper';
        var toggle = document.createElement('button');
        toggle.className = 'playbook-details-toggle';
        toggle.type = 'button';
        toggle.textContent = 'Read the full intro';
        var body = document.createElement('div');
        body.className = 'playbook-details-body';

        // Move all elements from first h2 onward into body
        var nodesToMove = children.slice(firstH2Idx);
        nodesToMove.forEach(function(n) { body.appendChild(n); });

        wrapper.appendChild(toggle);
        wrapper.appendChild(body);
        content.appendChild(wrapper);

        toggle.addEventListener('click', function() {
            wrapper.classList.toggle('is-open');
        });
    }
})();
</script>"""


fixed = 0
for idx in sorted(PLAYBOOKS.glob("*/index.html")):
    text = idx.read_text(encoding="utf-8")

    # Skip if already patched
    if "=== mobile compression (injected) ===" in text:
        continue

    # Inject CSS before the closing </style>
    if "</style>" in text:
        text = text.replace("</style>", MOBILE_CSS + "\n</style>", 1)

    # Inject JS before the nav-init <script> (so it runs on DOMContentLoaded time with the nav init)
    if "</body>" in text and JS_SNIPPET not in text:
        text = text.replace("</body>", JS_SNIPPET + "\n</body>", 1)

    idx.write_text(text, encoding="utf-8")
    fixed += 1

print(f"Patched {fixed} playbook index pages")
