#!/usr/bin/env python3
"""Enrich the 89 expertise subsection index pages.

Each one was auto-generated with a generic intro "Every page in the ___
section of my ___ knowledge base." Replace that with the topic-specific
description from _rewrite_expertise_hubs.py, and add a small diagram
showing where this subsection fits in its parent topic.
"""
import re
from pathlib import Path

ROOT = Path("/Users/ble/Desktop/sams site")

# Map from (topic_slug, subsection_slug) to (topic_name, subsection_name, description).
# Topic_name and subsection_name match the hub's display names.
# Descriptions are from _rewrite_expertise_hubs.py.
SUBSECTIONS = {
    # SEO
    ('seo','foundations'):        ('SEO', 'Foundations',         'How search engines work, ranking factors, and the E-E-A-T signals Google cares about in 2026.'),
    ('seo','keywords'):            ('SEO', 'Keyword Research',   'Finding the words real people type into Google, sized by intent, volume, and difficulty.'),
    ('seo','on-page'):             ('SEO', 'On-Page SEO',        'Title tags, headings, internal links, and all the editable signals on a page itself.'),
    ('seo','technical'):           ('SEO', 'Technical SEO',      'Crawling, speed, mobile, structured data - the under-the-hood plumbing that unlocks rankings.'),
    ('seo','links'):               ('SEO', 'Link Building',      'Earning backlinks that actually move rankings. The last durable ranking factor.'),
    ('seo','content'):             ('SEO', 'Content SEO',        'Strategy, topic clusters, pruning, AI-generated content, semantic and entity SEO.'),
    ('seo','local'):               ('SEO', 'Local SEO',          'Google Business Profile, NAP, reviews, citations - ranking for local intent queries.'),
    ('seo','ecommerce'):           ('SEO', 'E-commerce SEO',     'Product pages, category pages, faceted navigation, product schema - ecommerce-specific tactics.'),
    ('seo','international'):       ('SEO', 'International SEO',  'Hreflang, localization vs translation, domain strategy for multi-country sites.'),
    ('seo','analytics'):           ('SEO', 'Analytics',          'GA4, Search Console, rank tracking, and the reports that actually inform SEO decisions.'),
    ('seo','advanced'):            ('SEO', 'Advanced / Emerging','AI + SEO, Search Generative Experience, the frontier of search.'),

    # Agents
    ('agents','foundations'):      ('AI Agents', 'Foundations',  'What makes an agent an agent. Agentic vs reactive, the autonomy spectrum, the loop.'),
    ('agents','frameworks'):       ('AI Agents', 'Frameworks',   'LangChain, CrewAI, AutoGen, LangGraph. Which to use when, and why.'),
    ('agents','patterns'):         ('AI Agents', 'Patterns',     'ReAct, plan-execute, reflection, self-consistency - the canonical shapes.'),
    ('agents','tools'):            ('AI Agents', 'Tool Use',     'Function calling, MCP, and how to design tools agents can actually use reliably.'),
    ('agents','memory'):           ('AI Agents', 'Memory',       'Short-term context, long-term stores, persistent state across runs.'),
    ('agents','loops'):            ('AI Agents', 'Agent Loops',  'ReAct loop mechanics, drift, stop conditions, preventing runaways.'),
    ('agents','multi'):            ('AI Agents', 'Multi-Agent',  'Orchestrator-worker, role-based setups - and when multi-agent backfires.'),
    ('agents','eval'):             ('AI Agents', 'Evaluation',   'How to test an agent, not just its outputs. The discipline that separates demos from production.'),
    ('agents','prod'):             ('AI Agents', 'Production',   'Observability, cost, reliability, the engineering work that keeps agents running.'),

    # RAG
    ('rag','foundations'):         ('RAG', 'Foundations',      'What RAG is, why it beats fine-tuning in most cases, open-book vs closed-book modes.'),
    ('rag','embeddings'):          ('RAG', 'Embeddings',       'Turning text into vectors. Models, dimensions, trade-offs, and when to update them.'),
    ('rag','vectors'):             ('RAG', 'Vector Stores',    'Pinecone, Weaviate, pgvector, and picking the right store for your scale.'),
    ('rag','chunking'):            ('RAG', 'Chunking',         'The single biggest quality lever in RAG. How to split documents right.'),
    ('rag','retrieval'):           ('RAG', 'Retrieval',        'Semantic, keyword (BM25), hybrid, and reranking - getting the relevant context back.'),
    ('rag','docs'):                ('RAG', 'Documents',        'PDFs, HTML, code, structured data. Ingestion patterns that handle the mess.'),
    ('rag','eval'):                ('RAG', 'Evaluation',       'How to know your RAG is actually working, not just producing confident-sounding output.'),
    ('rag','advanced'):            ('RAG', 'Advanced',         'Multi-hop retrieval, query decomposition, agentic RAG patterns.'),
    ('rag','prod'):                ('RAG', 'Production',       'Caching, latency, cost, and keeping the index fresh as your docs change.'),
    ('rag','cases'):               ('RAG', 'Case Studies',     'Real RAG systems and what they taught us. Honest post-mortems included.'),

    # Direct Response
    ('direct-response','foundations'): ('Direct Response', 'Foundations',  'What direct response is, its history, the four horsemen of modern copywriting.'),
    ('direct-response','market'):      ('Direct Response', 'The Market',   'Dream customer, pain, levels of awareness and sophistication. Before you write, understand.'),
    ('direct-response','offer'):       ('Direct Response', 'The Offer',    'The value equation, guarantees, stacking, urgency, scarcity. The thing behind the copy.'),
    ('direct-response','copy'):        ('Direct Response', 'Copywriting',  'Headlines, leads, bullets, closes. The craft that sells.'),
    ('direct-response','letters'):     ('Direct Response', 'Sales Letters','VSLs, long-form, landing pages. Structure that works.'),
    ('direct-response','leads'):       ('Direct Response', 'Lead Generation','Core four channels, lead magnets, and how to qualify so the sales team survives.'),
    ('direct-response','followup'):    ('Direct Response', 'Follow-Up',    'Email sequences, retargeting, and long-cycle nurture.'),
    ('direct-response','testing'):     ('Direct Response', 'Testing',      'Scientific testing, controls, and what to actually A/B (and what not to).'),
    ('direct-response','scaling'):     ('Direct Response', 'Scaling',      'When to pour gasoline, when to fix the funnel first.'),

    # Paid Ads
    ('paid-ads','foundations'):    ('Paid Advertising', 'Foundations','The economics: CPM, CPC, CPA, ROAS, CAC. What breakeven actually looks like.'),
    ('paid-ads','creative'):       ('Paid Advertising', 'Creative',   'The 80% of paid that isn\'t targeting - it\'s the ad itself.'),
    ('paid-ads','meta'):           ('Paid Advertising', 'Meta Ads',   'Facebook and Instagram. Still the biggest platform.'),
    ('paid-ads','google'):         ('Paid Advertising', 'Google Ads', 'Search intent, Shopping, Performance Max - the old reliable.'),
    ('paid-ads','youtube'):        ('Paid Advertising', 'YouTube Ads','Skippable vs non, video creative, direct response on YouTube.'),
    ('paid-ads','tiktok'):         ('Paid Advertising', 'TikTok Ads', 'Organic-native creative, Spark Ads, and the fastest-growing platform.'),
    ('paid-ads','linkedin'):       ('Paid Advertising', 'LinkedIn Ads','B2B specifically. ABM, sponsored content, Account Audiences.'),
    ('paid-ads','measurement'):    ('Paid Advertising', 'Measurement','Attribution, MMM, incrementality - knowing what actually drives sales.'),

    # Cold Email
    ('cold-email','foundations'):  ('Cold Email', 'Foundations',    'When cold email works, the ethics, the legal constraints.'),
    ('cold-email','infra'):        ('Cold Email', 'Infrastructure', 'Sending domains, SPF/DKIM/DMARC, warmup, IP setup.'),
    ('cold-email','deliverability'): ('Cold Email', 'Deliverability','Staying out of spam - the game inside the game.'),
    ('cold-email','lists'):        ('Cold Email', 'List Building',  'ICP to data sources to verification to segmentation.'),
    ('cold-email','copy'):         ('Cold Email', 'Copywriting',    'Subject lines, opens, replies. The tight-word discipline.'),
    ('cold-email','sequences'):    ('Cold Email', 'Sequences',      'Cadence, number of touches, when to stop.'),
    ('cold-email','plays'):        ('Cold Email', 'Plays',          'Named-account outbound, event-based, competitor-switcher, and more.'),
    ('cold-email','testing'):      ('Cold Email', 'Testing',        'Testing methodology for the unique constraints of cold email.'),

    # Growth Marketing
    ('growth-marketing','foundations'):  ('Growth Marketing', 'Foundations', 'The AARRR model, growth vs marketing, picking a north-star metric.'),
    ('growth-marketing','acq'):          ('Growth Marketing', 'Acquisition', 'Channels, CAC, and scaling acquisition efficiently.'),
    ('growth-marketing','activation'):   ('Growth Marketing', 'Activation',  'Turning signups into engaged users. The step that makes retention possible.'),
    ('growth-marketing','retention'):    ('Growth Marketing', 'Retention',   'What keeps users coming back. The real growth lever.'),
    ('growth-marketing','revenue'):      ('Growth Marketing', 'Revenue',     'Pricing, upsells, expansion.'),
    ('growth-marketing','experiments'):  ('Growth Marketing', 'Experiments', 'A/B testing, growth experiments, prioritization.'),
    ('growth-marketing','analytics'):    ('Growth Marketing', 'Analytics',   'Tracking, attribution, building the data foundation growth runs on.'),
    ('growth-marketing','process'):      ('Growth Marketing', 'Process',     'How growth teams actually operate week to week.'),
    ('growth-marketing','plays'):        ('Growth Marketing', 'Plays',       'Proven growth experiments across industries.'),

    # Email Marketing
    ('email-marketing','foundations'):    ('Email Marketing', 'Foundations',   'Why email still wins. Owned list as an asset.'),
    ('email-marketing','list'):           ('Email Marketing', 'List Growth',   'Lead magnets, popups, content upgrades, community-driven growth.'),
    ('email-marketing','deliverability'): ('Email Marketing', 'Deliverability','Domain authentication, warmup, engagement signals, inbox placement.'),
    ('email-marketing','broadcasts'):     ('Email Marketing', 'Broadcasts',    'Newsletters, launches, one-off sends. Cadence and segmentation.'),
    ('email-marketing','automations'):    ('Email Marketing', 'Automations',   'Welcome flows, abandonment, winback, behavioral triggers.'),
    ('email-marketing','commerce'):       ('Email Marketing', 'Commerce',      'Abandoned cart, post-purchase, retention - ecommerce-specific email.'),
    ('email-marketing','saas'):           ('Email Marketing', 'SaaS',          'Trial, onboarding, activation sequences.'),
    ('email-marketing','testing'):        ('Email Marketing', 'Testing',       'What to A/B and what not to, and how to know what actually moved the needle.'),
    ('email-marketing','tools'):          ('Email Marketing', 'Tools',         'ESPs compared, tech stack, integrations.'),

    # CRO
    ('cro','foundations'):   ('CRO', 'Foundations', 'What CRO is and where the wins actually come from.'),
    ('cro','research'):      ('CRO', 'Research',    'Heuristics, surveys, session recordings, user interviews - understanding why users don\'t convert.'),
    ('cro','frameworks'):    ('CRO', 'Frameworks',  'PXL, ICE, LIFT - prioritizing tests under real constraints.'),
    ('cro','pages'):         ('CRO', 'Landing Pages','The anatomy of pages that actually convert.'),
    ('cro','conversion'):    ('CRO', 'Conversion Copy','Copywriting for the moment of yes/no.'),
    ('cro','testing'):       ('CRO', 'Testing',     'Statistical significance, sample sizes, what to actually test.'),
    ('cro','analytics'):     ('CRO', 'Analytics',   'Tagging, funnels, cohorts - the data you need to run CRO well.'),
    ('cro','tools'):         ('CRO', 'Tools',       'Testing platforms, heatmaps, session recordings. The stack.'),

    # Business Management
    ('business-management','strategy'):          ('Business Management', 'Strategy',          'Positioning, focus, what to kill, decision frameworks.'),
    ('business-management','operating-systems'): ('Business Management', 'Operating Systems', 'EOS, OKRs, scorecards, weekly rhythms.'),
    ('business-management','leadership'):        ('Business Management', 'Leadership',        'Motivation, compensation, the leadership fundamentals.'),
    ('business-management','people'):            ('Business Management', 'People',            'Hiring, performance, firing, culture.'),
    ('business-management','execution'):         ('Business Management', 'Execution',         'Planning cadences, pre-mortems, process mapping.'),
    ('business-management','sales'):             ('Business Management', 'Sales',             'Sales org design, pipelines, forecasting, enablement.'),
    ('business-management','finance'):           ('Business Management', 'Finance',           'P&L literacy, unit economics, pricing, runway.'),
    ('business-management','risk'):              ('Business Management', 'Risk',              'Cybersecurity, legal, insurance, continuity.'),
}

# Matches the hero-compact block we generated earlier:
#   <section class="hero hero-compact" style="..."><div class="container">
#   <p class="eyebrow" ...>Expertise / <topic></p>
#   <h1>...</h1>
#   <p class="lead" ...>Every page in the ... section of my ... knowledge base.</p>
#   </div></section>
HERO_RE = re.compile(
    r'(<section class="hero hero-compact"[^>]*>\s*<div class="container">\s*)'
    r'(<p class="eyebrow"[^>]*>.*?</p>\s*)'
    r'(<h1[^>]*>.*?</h1>\s*)'
    r'(<p class="lead"[^>]*>)(.*?)(</p>)',
    re.DOTALL,
)

rewrote = 0
skipped = []
for (topic_slug, sub_slug), (topic_name, sub_name, description) in SUBSECTIONS.items():
    path = ROOT / "expertise" / topic_slug / sub_slug / "index.html"
    if not path.exists():
        skipped.append(f"{topic_slug}/{sub_slug}")
        continue

    text = path.read_text(encoding="utf-8")

    m = HERO_RE.search(text)
    if not m:
        # Page structure different from expected - skip and report
        skipped.append(f"{topic_slug}/{sub_slug} (hero pattern mismatch)")
        continue

    # Replace just the lead paragraph's content with the new description.
    # Keep the surrounding structure intact.
    new_text = (
        text[: m.start(5)]      # everything up to the inside of <p class="lead">
        + description
        + text[m.end(5):]       # everything from </p> onward
    )

    path.write_text(new_text, encoding="utf-8")
    rewrote += 1

print(f"Rewrote {rewrote} subsection index pages.")
if skipped:
    print(f"Skipped: {len(skipped)}")
    for s in skipped[:20]:
        print(f"  {s}")
