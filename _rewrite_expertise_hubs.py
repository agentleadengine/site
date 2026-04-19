#!/usr/bin/env python3
"""Rewrite the intro (lede + word-count line) on each of the 10 expertise hub
pages with a teaching-depth paragraph + a sketch diagram of the subsections.

The existing subsection-list structure stays intact; we only touch the
intro block between the <h1 class="title"> and the first <h2>.
"""
import re
from pathlib import Path

ROOT = Path("/Users/ble/Desktop/sams site")

# Each entry: (slug, title, lede, diagram_subsections)
# The diagram_subsections is a list of (section_name, what_it_covers)
# tuples that will become a hand-drawn table in the hub.

HUBS = {
    "seo": {
        "title": "SEO",
        "lede": (
            "SEO is the discipline of showing up when people search for what you do. "
            "Built well, it's the cheapest customer acquisition channel there is, free "
            "traffic from Google that compounds over years. Built badly, it's a time sink "
            "that produces nothing. This section is the full walk from fundamentals to "
            "frontier: foundations, keyword research, on-page, technical, link building, "
            "content strategy, local, ecommerce, international, analytics, and what AI is "
            "doing to search in 2026. About 40,000 words across 100 pages. Pick a section "
            "or read front to back, but take it seriously, because the payoff takes months "
            "to materialize and years to compound."
        ),
        "sections": [
            ("Foundations", "how search engines work, ranking factors, E-E-A-T"),
            ("Keyword Research", "finding what people search for, by intent + volume + difficulty"),
            ("On-Page SEO", "title tags, headings, internal links, the editable basics"),
            ("Technical SEO", "crawling, speed, mobile, structured data, the plumbing"),
            ("Link Building", "earning backlinks that move rankings"),
            ("Content SEO", "strategy, clusters, pruning, AI content, semantic SEO"),
            ("Local SEO", "Google Business Profile, reviews, NAP, multi-location"),
            ("E-commerce SEO", "product/category pages, faceted nav, product schema"),
            ("International SEO", "hreflang, localization, domain strategy"),
            ("Analytics", "GA4, Search Console, rank tracking, reporting"),
            ("Advanced / Emerging", "AI + SEO, Search Generative Experience, the future"),
        ],
    },
    "agents": {
        "title": "AI Agents",
        "lede": (
            "Agents are the productization of LLMs — the layer that turns 'interesting "
            "chatbot' into 'software that actually does things for you.' This 90-page "
            "knowledge base covers the full stack: foundations (what makes an agent an "
            "agent), frameworks, the canonical patterns, tool use, memory, multi-agent "
            "orchestration, evaluation, and production deployment. It pairs naturally with "
            "the Framework section on this site (which is Claude-specific) — this one is "
            "more broadly about agents regardless of which model you use. If the future of "
            "software is 'it kind of runs itself,' this is where you learn to build it."
        ),
        "sections": [
            ("Foundations", "what an agent is, agentic vs reactive, autonomy spectrum"),
            ("Frameworks", "LangChain, CrewAI, AutoGen, LangGraph, choose wisely"),
            ("Patterns", "ReAct, plan-execute, reflection, self-consistency"),
            ("Tool Use", "function calling, MCP, designing tools agents can actually use"),
            ("Memory", "short-term, long-term, persistent state across runs"),
            ("Agent Loops", "ReAct loop mechanics, drift, stop conditions"),
            ("Multi-Agent", "orchestrator-worker, role-based, when it helps and when it doesn't"),
            ("Evaluation", "how to test an agent, not just its outputs"),
            ("Production", "observability, cost, reliability, going live"),
        ],
    },
    "rag": {
        "title": "RAG",
        "lede": (
            "Retrieval-Augmented Generation is how you turn an LLM into 'Claude, but "
            "with knowledge of YOUR data.' Instead of retraining the model (slow, expensive, "
            "stale), you give it a library to look things up in, and the model cites from "
            "what it finds. Every 'chat with your docs' product on earth is RAG under the "
            "hood. This 70-page section covers the full pipeline: foundations, embeddings, "
            "vector stores, chunking strategies, retrieval approaches, document handling, "
            "evaluation, production patterns, and real case studies. RAG looks simple in "
            "demos. Getting it production-grade is harder than you'd think, and this "
            "section is the map."
        ),
        "sections": [
            ("Foundations", "what RAG is, open-book mode, where it beats fine-tuning"),
            ("Embeddings", "turning text into vectors; models and trade-offs"),
            ("Vector Stores", "Pinecone, Weaviate, pgvector, picking the right one"),
            ("Chunking", "the single biggest quality lever in RAG"),
            ("Retrieval", "semantic, keyword (BM25), hybrid, reranking"),
            ("Documents", "PDFs, HTML, code, structured data; ingestion patterns"),
            ("Evaluation", "how to know your RAG is actually working"),
            ("Advanced", "multi-hop, query decomposition, agentic RAG"),
            ("Production", "caching, latency, cost, data freshness"),
            ("Case Studies", "real RAG systems and what they taught us"),
        ],
    },
    "direct-response": {
        "title": "Direct Response",
        "lede": (
            "Direct response is marketing that asks for a specific action now, and lets "
            "you see exactly whether it worked. It's the discipline behind every sales page, "
            "cold email, VSL, and lead-gen funnel that actually pays for itself. The "
            "copywriting craft has 100 years of accumulated wisdom from practitioners who "
            "had to sell or starve, and this section is that craft brought into 2026. "
            "Foundations, market understanding, offer design, copywriting, sales letters, "
            "lead generation, follow-up, testing, and scaling. If you've ever wondered "
            "why some ads convert 10x better than others while looking similar, the answer "
            "lives in here."
        ),
        "sections": [
            ("Foundations", "what direct response is, its history, the four horsemen"),
            ("The Market", "dream customer, pain, levels of awareness, sophistication"),
            ("The Offer", "value equation, guarantees, stacking, urgency/scarcity"),
            ("Copywriting", "headlines, leads, bullets, closes, the canonical formulas"),
            ("Sales Letters", "VSLs, long-form, landing pages, structure"),
            ("Lead Generation", "core four channels, lead magnets, qualification"),
            ("Follow-Up", "email sequences, retargeting, long-cycle nurture"),
            ("Testing", "scientific testing, controls, what to actually A/B"),
            ("Scaling", "when to pour gasoline vs when to fix the funnel"),
        ],
    },
    "paid-ads": {
        "title": "Paid Advertising",
        "lede": (
            "Paid ads are the fastest way to get traffic, and the fastest way to lose "
            "money doing it. Every platform has its own learning curve, its own targeting "
            "quirks, its own bidding algorithm, and its own failure modes. This 80-page "
            "section covers the big six (Meta, Google, YouTube, TikTok, LinkedIn) plus "
            "the creative discipline and measurement work that spans them all. The goal: "
            "know enough to run profitable paid traffic on any platform without being "
            "dependent on an agency you don't trust, and enough to hire a great agency if "
            "you decide you want one."
        ),
        "sections": [
            ("Foundations", "the economics: CPM, CPC, CPA, ROAS, CAC, breakeven math"),
            ("Creative", "the 80% of paid that isn't targeting, it's the ad itself"),
            ("Meta Ads", "Facebook and Instagram — still the biggest platform"),
            ("Google Ads", "search intent, shopping, Performance Max, the old reliable"),
            ("YouTube Ads", "video creative, skippable vs non, direct response on YT"),
            ("TikTok Ads", "organic-native creative, Spark Ads, the fastest-growing"),
            ("LinkedIn Ads", "B2B specifically, ABM, sponsored content"),
            ("Measurement", "attribution, MMM, incrementality, knowing what actually works"),
        ],
    },
    "cold-email": {
        "title": "Cold Email",
        "lede": (
            "Cold email is the highest-leverage outbound channel in B2B, and most people "
            "do it badly. The good version: predictable pipeline at a fraction of paid-ads "
            "cost, done for years without diminishing returns. The bad version: your domain "
            "ends up on blocklists, your deliverability tanks, and you can't recover for "
            "months. The difference is discipline across four dimensions: deliverability, "
            "lists, copy, and sequences. This 45-page section is the full system. "
            "Direct response applied to the inbox."
        ),
        "sections": [
            ("Foundations", "when cold email works, ethics, legal constraints"),
            ("Infrastructure", "sending domains, SPF/DKIM/DMARC, warmup, IP setup"),
            ("Deliverability", "staying out of spam — the game inside the game"),
            ("List Building", "ICP → data sources → verification → segmentation"),
            ("Copywriting", "subject lines, opens, replies, the few-word discipline"),
            ("Sequences", "cadence, number of touches, when to stop"),
            ("Plays", "named-account outbound, event-based, competitor-switcher, and more"),
            ("Testing", "methodology for the unique constraints of email"),
        ],
    },
    "growth-marketing": {
        "title": "Growth Marketing",
        "lede": (
            "Growth marketing is what you do when 'marketing' alone isn't enough. It "
            "spans the entire customer journey — acquisition, activation, retention, "
            "revenue, referral — and treats the whole funnel as one system to optimize. "
            "It's more analytical than traditional marketing, more experimental, and more "
            "cross-functional. This 80-page section covers the mental model, the metrics, "
            "the experimentation practice, and the plays. For anyone who feels constrained "
            "by the limits of 'pure' marketing, this is the upgrade path."
        ),
        "sections": [
            ("Foundations", "the AARRR model, growth vs marketing, north-star metric"),
            ("Acquisition", "channels, CAC, scaling efficiently"),
            ("Activation", "turning signups into engaged users"),
            ("Retention", "what keeps users coming back — the real growth lever"),
            ("Revenue", "pricing, upsell, expansion"),
            ("Experiments", "A/B testing, growth experiments, prioritization"),
            ("Analytics", "tracking, attribution, building the data foundation"),
            ("Process", "how growth teams actually operate week to week"),
            ("Plays", "proven growth experiments across industries"),
        ],
    },
    "email-marketing": {
        "title": "Email Marketing",
        "lede": (
            "Email marketing is the highest-ROI channel in most businesses, and the most "
            "neglected. Unlike paid ads (you rent the audience) or social (you rent the "
            "algorithm), email is the one channel you actually OWN. Your list is yours; "
            "your deliverability is yours; your relationship with subscribers is yours. "
            "This 90-page section covers list growth, deliverability, broadcast vs "
            "automation, e-commerce specifically, SaaS specifically, testing, and the "
            "tools. The first channel to fix in any business, and one of the last to fail."
        ),
        "sections": [
            ("Foundations", "why email still wins, list health, ownership"),
            ("List Growth", "lead magnets, popups, referrals, community"),
            ("Deliverability", "domain auth, warmup, engagement signals, inbox placement"),
            ("Broadcasts", "newsletters, launches, one-off sends"),
            ("Automations", "welcome flows, abandonment, winback, lifecycle"),
            ("Commerce", "abandoned cart, post-purchase, retention — ecommerce specifics"),
            ("SaaS", "trial, onboarding, activation sequences"),
            ("Testing", "what to A/B, what not to, and how to know what moved the needle"),
            ("Tools", "ESPs compared, tech stack, integrations"),
        ],
    },
    "cro": {
        "title": "CRO",
        "lede": (
            "Conversion Rate Optimization is the craft of turning more of your existing "
            "traffic into customers. It's usually the cheapest path to revenue growth: you "
            "already have traffic; you already have a product; fix the leaks in your funnel "
            "and the whole thing scales. This 70-page section covers research (understanding "
            "why users DON'T convert), frameworks (prioritizing what to test), landing "
            "pages, conversion copy, testing methodology, analytics, and the tools. CRO is "
            "detective work with math. When it's working, it compounds quietly; every "
            "future marketing dollar goes further."
        ),
        "sections": [
            ("Foundations", "what CRO is, where the wins come from"),
            ("Research", "heuristics, surveys, session recordings, user interviews"),
            ("Frameworks", "PXL, ICE, prioritization under constraints"),
            ("Landing Pages", "the anatomy of pages that actually convert"),
            ("Conversion Copy", "copywriting for the moment of yes/no"),
            ("Testing", "statistical significance, sample sizes, what to actually test"),
            ("Analytics", "tagging, funnels, cohorts, the data you need"),
            ("Tools", "testing platforms, heatmaps, session recordings, the stack"),
        ],
    },
    "business-management": {
        "title": "Business Management",
        "lede": (
            "Business management is every skill marketing books skip: strategy, operating "
            "systems, leadership, people, execution, sales, finance, risk. The stuff that "
            "separates businesses that grow smoothly from businesses that keep tripping "
            "over themselves. This 80-page section is what I wish I'd read before starting "
            "my first company. No fluff, no guru-speak. Practical frameworks from "
            "practitioners who ran real businesses. Marketing gets you customers. Business "
            "management is what keeps the company alive long enough to serve them."
        ),
        "sections": [
            ("Strategy", "positioning, focus, what to kill, decision frameworks"),
            ("Operating Systems", "EOS, OKRs, scorecards, weekly rhythms"),
            ("Leadership", "motivation, compensation, the fundamentals"),
            ("People", "hiring, performance, firing, culture"),
            ("Execution", "planning cadences, pre-mortems, process mapping"),
            ("Sales", "org design, pipelines, forecasting, enablement"),
            ("Finance", "P&L literacy, unit economics, pricing, runway"),
            ("Risk", "cybersecurity, legal, insurance, continuity"),
        ],
    },
}

LEDE_AND_DIAGRAM_RE = re.compile(
    # Match from h1.title through to the first <h2> OR <div class="cards" ...>.
    r'(<h1[^>]*class="title"[^>]*>[^<]*</h1>)(.*?)(<h2>|<div class="cards"[^>]*>)',
    re.DOTALL,
)


def build_sections_diagram(hub_slug, sections):
    """Build the sketch.js table diagram showing subsections."""
    rows_js = []
    for name, desc in sections:
        # JS string literal — escape quotes
        name_js = name.replace("'", "\\'")
        desc_js = desc.replace("'", "\\'")
        rows_js.append(f"      ['{name_js}', '{desc_js}']")
    rows_block = ",\n".join(rows_js)

    return f'''<div class="sketch" data-viewbox="0 0 900 {max(240, 80 + len(sections) * 38)}" id="dg-hub-{hub_slug}">
  <svg></svg>
  <div class="sketch-caption">~ the sections of this knowledge base ~</div>
</div>
<script>
document.addEventListener('sketch:ready', function() {{
  var wrap = document.getElementById('dg-hub-{hub_slug}');
  if (!wrap || wrap.dataset.drawn) return;
  wrap.dataset.drawn = '1';
  var svg = wrap.querySelector('svg');
  var rc = sketch.rc(svg);
  sketch.table(svg, rc, {{
    x: 20, y: 30,
    cols: [
      {{ title: 'Section', w: 230 }},
      {{ title: 'What it covers', w: 620 }}
    ],
    rows: [
{rows_block}
    ]
  }});
}});
</script>'''


rewrote = 0
skipped = []

for hub_slug, hub_data in HUBS.items():
    # Each expertise hub lives at expertise/<slug>/index.html
    path = ROOT / "expertise" / hub_slug / "index.html"
    if not path.exists():
        skipped.append(hub_slug)
        continue

    text = path.read_text(encoding="utf-8")

    m = LEDE_AND_DIAGRAM_RE.search(text)
    if not m:
        print(f"WARN: could not find title/h2 boundary in {hub_slug}")
        continue

    h1_open = m.group(1)
    first_h2 = m.group(3)

    # Build new intro: keep h1, new lede + diagram, then first h2
    diagram = build_sections_diagram(hub_slug, hub_data["sections"])
    new_intro = (
        h1_open
        + f'\n<p class="lede">{hub_data["lede"]}</p>\n'
        + diagram
        + "\n"
        + first_h2
    )

    new_text = text[: m.start()] + new_intro + text[m.end():]
    path.write_text(new_text, encoding="utf-8")
    rewrote += 1
    print(f"✓ {hub_slug}")

print(f"\nRewrote {rewrote}/{len(HUBS)} expertise hubs.")
if skipped:
    print(f"Skipped (file not found): {skipped}")
