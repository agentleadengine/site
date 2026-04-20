#!/usr/bin/env python3
"""Rebuild the site-wide top nav: fresh markup + init JS on every HTML page.

Replaces whatever <nav class="topbar">...</nav> block currently exists and the
nav-init <script> block that was previously injected.
"""
import re
from pathlib import Path

ROOT = Path("/Users/ble/Desktop/sams site")

# -----------------------------------------------------------------------------
# Nav structure. Each entry is (label, href, submenu).
#   submenu for simple dropdowns = list of (label, href) pairs.
#   submenu for the mega menu = list of (section_label, section_href, [(label, href), ...]).
# -----------------------------------------------------------------------------

FRAMEWORK = [
    ("Overview", "framework/index.html"),
    ("What is Autonomous AI", "framework/what-is-autonomous-ai.html"),
    ("Autonomy Spectrum", "framework/the-autonomy-spectrum.html"),
    ("Claude (model)", "framework/claude/index.html"),
    ("Claude Code (harness)", "framework/claude-code/index.html"),
    ("MCP", "framework/mcp/index.html"),
    ("Plugins", "framework/plugins/index.html"),
    ("Agent Patterns", "framework/patterns/index.html"),
    ("Going Autonomous", "framework/autonomous/index.html"),
    ("Build Guides", "framework/build/index.html"),
    ("Tools", "framework/tools/index.html"),
    ("Glossary", "framework/glossary.html"),
]

PLAYBOOKS = [
    ("All Playbooks", "playbooks/index.html"),
    ("Insurance", "playbooks/insurance/index.html"),
    ("Real Estate", "playbooks/real-estate/index.html"),
    ("Mortgage", "playbooks/mortgage/index.html"),
    ("Financial Advisor", "playbooks/financial-advisor/index.html"),
    ("Personal Trainer", "playbooks/personal-trainer/index.html"),
    ("Coach", "playbooks/coach/index.html"),
    ("Dentist", "playbooks/dentist/index.html"),
    ("Chiropractor", "playbooks/chiropractor/index.html"),
    ("CPA", "playbooks/cpa/index.html"),
    ("Restaurant", "playbooks/restaurant/index.html"),
    ("Agency", "playbooks/agency/index.html"),
    ("Ecommerce", "playbooks/ecommerce/index.html"),
    ("SaaS", "playbooks/saas/index.html"),
    ("Podcaster", "playbooks/podcaster/index.html"),
    ("Author", "playbooks/author/index.html"),
]

# Expertise mega menu - each column is a category with its subpages.
EXPERTISE = [
    ("SEO", "expertise/seo/index.html", [
        ("Foundations", "expertise/seo/foundations/index.html"),
        ("Keyword Research", "expertise/seo/keywords/index.html"),
        ("On-Page", "expertise/seo/on-page/index.html"),
        ("Technical SEO", "expertise/seo/technical/index.html"),
        ("Link Building", "expertise/seo/links/index.html"),
        ("Content SEO", "expertise/seo/content/index.html"),
        ("Local SEO", "expertise/seo/local/index.html"),
        ("International", "expertise/seo/international/index.html"),
        ("Ecommerce SEO", "expertise/seo/ecommerce/index.html"),
        ("Advanced", "expertise/seo/advanced/index.html"),
        ("Analytics", "expertise/seo/analytics/index.html"),
    ]),
    ("AI Agents", "expertise/agents/index.html", [
        ("Foundations", "expertise/agents/foundations/index.html"),
        ("Frameworks", "expertise/agents/frameworks/index.html"),
        ("Patterns", "expertise/agents/patterns/index.html"),
        ("Tool Use", "expertise/agents/tools/index.html"),
        ("Memory", "expertise/agents/memory/index.html"),
        ("Agent Loops", "expertise/agents/loops/index.html"),
        ("Multi-Agent", "expertise/agents/multi/index.html"),
        ("Evaluation", "expertise/agents/eval/index.html"),
        ("Production", "expertise/agents/prod/index.html"),
    ]),
    ("RAG", "expertise/rag/index.html", [
        ("Foundations", "expertise/rag/foundations/index.html"),
        ("Embeddings", "expertise/rag/embeddings/index.html"),
        ("Vector Stores", "expertise/rag/vectors/index.html"),
        ("Chunking", "expertise/rag/chunking/index.html"),
        ("Retrieval", "expertise/rag/retrieval/index.html"),
        ("Documents", "expertise/rag/docs/index.html"),
        ("Evaluation", "expertise/rag/eval/index.html"),
        ("Advanced", "expertise/rag/advanced/index.html"),
        ("Production", "expertise/rag/prod/index.html"),
        ("Case Studies", "expertise/rag/cases/index.html"),
    ]),
    ("Direct Response", "expertise/direct-response/index.html", [
        ("Foundations", "expertise/direct-response/foundations/index.html"),
        ("The Market", "expertise/direct-response/market/index.html"),
        ("The Offer", "expertise/direct-response/offer/index.html"),
        ("Copywriting", "expertise/direct-response/copy/index.html"),
        ("Sales Letters", "expertise/direct-response/letters/index.html"),
        ("Lead Generation", "expertise/direct-response/leads/index.html"),
        ("Follow-Up", "expertise/direct-response/followup/index.html"),
        ("Testing", "expertise/direct-response/testing/index.html"),
        ("Scaling", "expertise/direct-response/scaling/index.html"),
    ]),
    ("Paid Advertising", "expertise/paid-ads/index.html", [
        ("Foundations", "expertise/paid-ads/foundations/index.html"),
        ("Creative", "expertise/paid-ads/creative/index.html"),
        ("Meta Ads", "expertise/paid-ads/meta/index.html"),
        ("Google Ads", "expertise/paid-ads/google/index.html"),
        ("YouTube Ads", "expertise/paid-ads/youtube/index.html"),
        ("TikTok Ads", "expertise/paid-ads/tiktok/index.html"),
        ("LinkedIn Ads", "expertise/paid-ads/linkedin/index.html"),
        ("Measurement", "expertise/paid-ads/measurement/index.html"),
    ]),
    ("Cold Email", "expertise/cold-email/index.html", [
        ("Foundations", "expertise/cold-email/foundations/index.html"),
        ("Infrastructure", "expertise/cold-email/infra/index.html"),
        ("Deliverability", "expertise/cold-email/deliverability/index.html"),
        ("List Building", "expertise/cold-email/lists/index.html"),
        ("Copywriting", "expertise/cold-email/copy/index.html"),
        ("Sequences", "expertise/cold-email/sequences/index.html"),
        ("Plays", "expertise/cold-email/plays/index.html"),
        ("Testing", "expertise/cold-email/testing/index.html"),
    ]),
    ("Growth Marketing", "expertise/growth-marketing/index.html", [
        ("Foundations", "expertise/growth-marketing/foundations/index.html"),
        ("Acquisition", "expertise/growth-marketing/acq/index.html"),
        ("Activation", "expertise/growth-marketing/activation/index.html"),
        ("Retention", "expertise/growth-marketing/retention/index.html"),
        ("Revenue", "expertise/growth-marketing/revenue/index.html"),
        ("Experiments", "expertise/growth-marketing/experiments/index.html"),
        ("Analytics", "expertise/growth-marketing/analytics/index.html"),
        ("Process", "expertise/growth-marketing/process/index.html"),
        ("Plays", "expertise/growth-marketing/plays/index.html"),
    ]),
    ("Email Marketing", "expertise/email-marketing/index.html", [
        ("Foundations", "expertise/email-marketing/foundations/index.html"),
        ("List Growth", "expertise/email-marketing/list/index.html"),
        ("Deliverability", "expertise/email-marketing/deliverability/index.html"),
        ("Broadcasts", "expertise/email-marketing/broadcasts/index.html"),
        ("Automations", "expertise/email-marketing/automations/index.html"),
        ("Commerce", "expertise/email-marketing/commerce/index.html"),
        ("SaaS", "expertise/email-marketing/saas/index.html"),
        ("Testing", "expertise/email-marketing/testing/index.html"),
        ("Tools", "expertise/email-marketing/tools/index.html"),
    ]),
    ("CRO", "expertise/cro/index.html", [
        ("Foundations", "expertise/cro/foundations/index.html"),
        ("Research", "expertise/cro/research/index.html"),
        ("Frameworks", "expertise/cro/frameworks/index.html"),
        ("Landing Pages", "expertise/cro/pages/index.html"),
        ("Conversion Copy", "expertise/cro/conversion/index.html"),
        ("Testing", "expertise/cro/testing/index.html"),
        ("Analytics", "expertise/cro/analytics/index.html"),
        ("Tools", "expertise/cro/tools/index.html"),
    ]),
    ("Business Management", "expertise/business-management/index.html", [
        ("Strategy", "expertise/business-management/strategy/index.html"),
        ("Operating Systems", "expertise/business-management/operating-systems/index.html"),
        ("Leadership", "expertise/business-management/leadership/index.html"),
        ("People", "expertise/business-management/people/index.html"),
        ("Execution", "expertise/business-management/execution/index.html"),
        ("Sales", "expertise/business-management/sales/index.html"),
        ("Finance", "expertise/business-management/finance/index.html"),
        ("Risk", "expertise/business-management/risk/index.html"),
    ]),
]


def rel_prefix(html_path: Path) -> str:
    rel = html_path.relative_to(ROOT)
    depth = len(rel.parts) - 1
    return "../" * depth


def build_nav(R: str) -> str:
    lines = [
        '<nav class="topbar"><div class="topbar-inner">',
        f'<a href="{R}index.html" class="logo"><img class="brand-logo" src="{R}logo.png" alt="Samuel Ochoa"></a>',
        '<button class="hamburger" type="button" aria-label="Toggle menu" aria-expanded="false"><span></span><span></span><span></span></button>',
        '<div class="nav-links">',
        f'<a href="{R}index.html" class="nav-link">Home</a>',
        # Framework dropdown
        '<div class="nav-group">',
        f'<a href="{R}framework/index.html" class="nav-link nav-has-submenu">Framework</a>',
        '<div class="nav-submenu">',
    ]
    for label, href in FRAMEWORK:
        lines.append(f'<a href="{R}{href}">{label}</a>')
    lines.append('</div></div>')

    # Expertise mega dropdown - 2-col: category list (left) + active cat's subpages (right).
    # Children hidden until user hovers a category (menu-inside-menu).
    lines.append('<div class="nav-group nav-group-wide">')
    lines.append(f'<a href="{R}expertise/index.html" class="nav-link nav-has-submenu">Expertise</a>')
    lines.append('<div class="nav-submenu nav-mega">')
    lines.append('<div class="nav-mega-cats">')
    for i, (section_label, section_href, _subpages) in enumerate(EXPERTISE):
        cat_id = f"cat{i}"
        active = ' is-active' if i == 0 else ''
        lines.append(
            f'<a href="{R}{section_href}" class="nav-cat{active}" data-cat="{cat_id}">'
            f'<span>{section_label}</span>'
            f'<span class="nav-cat-arrow">›</span>'
            f'</a>'
        )
    lines.append('</div>')  # nav-mega-cats
    lines.append('<div class="nav-mega-content">')
    for i, (section_label, section_href, subpages) in enumerate(EXPERTISE):
        cat_id = f"cat{i}"
        active = ' is-active' if i == 0 else ''
        lines.append(f'<div class="nav-cat-panel{active}" data-cat="{cat_id}">')
        lines.append(f'<a href="{R}{section_href}" class="nav-cat-panel-head">{section_label}. Section overview →</a>')
        lines.append('<div class="nav-cat-panel-list">')
        for sub_label, sub_href in subpages:
            lines.append(f'<a href="{R}{sub_href}">{sub_label}</a>')
        lines.append('</div>')
        lines.append('</div>')
    lines.append('</div>')  # nav-mega-content
    lines.append('</div></div>')

    # Playbooks dropdown
    lines.append('<div class="nav-group">')
    lines.append(f'<a href="{R}playbooks/index.html" class="nav-link nav-has-submenu">Playbooks</a>')
    lines.append('<div class="nav-submenu">')
    for label, href in PLAYBOOKS:
        lines.append(f'<a href="{R}{href}">{label}</a>')
    lines.append('</div></div>')

    # Simple links
    lines.append(f'<a href="{R}writing.html" class="nav-link">Writing</a>')
    lines.append(f'<a href="{R}about.html" class="nav-link">About</a>')
    lines.append(f'<a href="{R}contact.html" class="nav-link">Contact</a>')

    lines.append('</div>')  # nav-links
    lines.append('</div></nav>')
    return "\n".join(lines)


NAV_SCRIPT = """<script>
(function(){
  const bar = document.querySelector('nav.topbar');
  if (!bar || bar.dataset.navInit) return;
  bar.dataset.navInit = '1';

  const OPEN_DELAY = 120;   // ms - hover intent
  const CLOSE_DELAY = 450;  // ms - forgiving close
  const isMobile = () => window.matchMedia('(max-width: 960px)').matches;

  const hamb = bar.querySelector('.hamburger');
  const links = bar.querySelector('.nav-links');
  const groups = Array.from(bar.querySelectorAll('.nav-group'));

  // --- Mobile hamburger ---------------------------------------------------
  if (hamb && links) {
    hamb.addEventListener('click', function(e) {
      e.stopPropagation();
      const open = bar.classList.toggle('nav-open');
      hamb.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // --- Per-group hover-intent open/close ---------------------------------
  groups.forEach(function(group) {
    let openTimer = null;
    let closeTimer = null;

    const open = () => {
      clearTimeout(closeTimer); closeTimer = null;
      if (openTimer) return;
      openTimer = setTimeout(() => {
        groups.forEach(g => { if (g !== group) g.classList.remove('is-open'); });
        group.classList.add('is-open');
        openTimer = null;
      }, OPEN_DELAY);
    };
    const close = () => {
      clearTimeout(openTimer); openTimer = null;
      clearTimeout(closeTimer);
      closeTimer = setTimeout(() => {
        group.classList.remove('is-open');
        closeTimer = null;
      }, CLOSE_DELAY);
    };
    const cancelClose = () => { clearTimeout(closeTimer); closeTimer = null; };

    // Desktop: hover opens, mouseleave closes after delay
    group.addEventListener('mouseenter', () => { if (!isMobile()) open(); });
    group.addEventListener('mouseleave', () => { if (!isMobile()) close(); });
    // If cursor re-enters while closing, cancel the close
    group.addEventListener('pointerenter', () => { if (!isMobile()) cancelClose(); });

    // Click trigger: mobile toggles accordion; desktop follows the link
    const trigger = group.querySelector('.nav-has-submenu');
    if (trigger) {
      trigger.addEventListener('click', function(e) {
        if (isMobile()) {
          e.preventDefault();
          const wasOpen = group.classList.contains('is-open');
          groups.forEach(g => g.classList.remove('is-open'));
          if (!wasOpen) group.classList.add('is-open');
        }
      });
    }
  });

  // --- Expertise mega: swap right-panel content on category hover --------
  const megaCats = bar.querySelectorAll('.nav-mega-cats .nav-cat');
  const megaPanels = bar.querySelectorAll('.nav-mega-content .nav-cat-panel');
  let catTimer = null;
  megaCats.forEach(function(cat) {
    cat.addEventListener('mouseenter', function() {
      clearTimeout(catTimer);
      const id = cat.dataset.cat;
      catTimer = setTimeout(() => {
        megaCats.forEach(c => c.classList.toggle('is-active', c.dataset.cat === id));
        megaPanels.forEach(p => p.classList.toggle('is-active', p.dataset.cat === id));
      }, 80); // snappier than top-level hover intent
    });
  });

  // --- Close menu when a leaf link is clicked ----------------------------
  if (links) {
    links.querySelectorAll('a').forEach(function(a) {
      if (a.classList.contains('nav-has-submenu')) return;
      if (a.classList.contains('nav-cat')) return; // cat label also navigates, but don't auto-close
      a.addEventListener('click', function() {
        bar.classList.remove('nav-open');
        if (hamb) hamb.setAttribute('aria-expanded', 'false');
        groups.forEach(g => g.classList.remove('is-open'));
      });
    });
  }

  // --- Close on outside click ---------------------------------------------
  document.addEventListener('click', function(e) {
    if (!bar.contains(e.target)) {
      bar.classList.remove('nav-open');
      if (hamb) hamb.setAttribute('aria-expanded', 'false');
      groups.forEach(g => g.classList.remove('is-open'));
    }
  });

  // --- Escape key closes everything ---------------------------------------
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      bar.classList.remove('nav-open');
      if (hamb) hamb.setAttribute('aria-expanded', 'false');
      groups.forEach(g => g.classList.remove('is-open'));
    }
  });
})();
</script>"""


# Matches the full <nav class="topbar">...</nav> block, greedy across newlines.
NAV_RE = re.compile(r'<nav\s+class="topbar">.*?</nav>', re.DOTALL | re.IGNORECASE)

# Matches the existing nav-init <script>...</script> block.
# The script we previously injected contains the unique phrase "dataset.navInit".
SCRIPT_RE = re.compile(r'<script>\s*\(function\(\)\{[^<]*?dataset\.navInit[\s\S]*?</script>', re.IGNORECASE)

replaced_nav = 0
replaced_script = 0
scanned = 0

for html in sorted(ROOT.rglob("*.html")):
    scanned += 1
    text = html.read_text(encoding="utf-8")
    orig = text

    R = rel_prefix(html)
    new_nav = build_nav(R)

    if NAV_RE.search(text):
        text = NAV_RE.sub(lambda _m: new_nav, text, count=1)
        if text != orig:
            replaced_nav += 1

    # Replace any existing nav-init script.
    if SCRIPT_RE.search(text):
        text = SCRIPT_RE.sub(lambda _m: NAV_SCRIPT, text, count=1)
        replaced_script += 1
    else:
        # Inject nav script before </body> if no init script exists yet
        if "</body>" in text and "dataset.navInit" not in text:
            text = text.replace("</body>", NAV_SCRIPT + "\n</body>", 1)
            replaced_script += 1

    if text != orig:
        html.write_text(text, encoding="utf-8")

print(f"Scanned: {scanned} | nav replaced: {replaced_nav} | script replaced: {replaced_script}")
