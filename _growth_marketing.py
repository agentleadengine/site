#!/usr/bin/env python3
"""Growth Marketing expertise - 45 pages."""
from _build_expertise import build_expertise_section


SIDEBAR = [
    ("Foundations", [
        ("index", "Overview"),
        ("foundations/what-is-growth", "What is growth marketing?"),
        ("foundations/north-star-metric", "The North Star Metric"),
        ("foundations/growth-loops", "Growth loops vs funnels"),
        ("foundations/retention-first", "Retention first"),
    ]),
    ("Acquisition", [
        ("acq/channel-fit", "Channel-market fit"),
        ("acq/paid-vs-organic", "Paid vs organic"),
        ("acq/content-seo", "Content + SEO"),
        ("acq/viral-loops", "Viral loops"),
        ("acq/product-led", "Product-led acquisition"),
        ("acq/partnerships", "Partnerships"),
    ]),
    ("Activation", [
        ("activation/aha-moment", "The aha moment"),
        ("activation/onboarding-design", "Onboarding design"),
        ("activation/time-to-value", "Time to value"),
        ("activation/empty-states", "Empty states"),
        ("activation/early-wins", "Early wins"),
    ]),
    ("Retention", [
        ("retention/cohort-analysis", "Cohort analysis"),
        ("retention/churn-diagnostics", "Churn diagnostics"),
        ("retention/re-engagement", "Re-engagement"),
        ("retention/habit-formation", "Habit formation"),
        ("retention/feature-adoption", "Feature adoption"),
    ]),
    ("Revenue", [
        ("revenue/pricing", "Pricing"),
        ("revenue/upsell-expansion", "Upsell + expansion"),
        ("revenue/conversion-rate", "Conversion rate"),
        ("revenue/referrals", "Referrals"),
        ("revenue/ltv-expansion", "LTV expansion"),
    ]),
    ("Analytics", [
        ("analytics/event-tracking", "Event tracking"),
        ("analytics/funnels", "Funnels"),
        ("analytics/cohorts", "Cohort dashboards"),
        ("analytics/attribution", "Attribution"),
        ("analytics/north-star-dashboards", "North Star dashboards"),
    ]),
    ("Experimentation", [
        ("experiments/ab-testing", "A/B testing"),
        ("experiments/holdout-tests", "Holdout tests"),
        ("experiments/multivariate", "Multivariate"),
        ("experiments/statistical-significance", "Statistical significance"),
        ("experiments/velocity", "Experiment velocity"),
    ]),
    ("Teams + Process", [
        ("process/growth-team-structure", "Growth team structure"),
        ("process/growth-models", "Growth models"),
        ("process/ice-scoring", "ICE scoring"),
        ("process/sprint-rhythm", "Sprint rhythm"),
    ]),
    ("Playbooks", [
        ("plays/saas-growth", "SaaS growth"),
        ("plays/dtc-growth", "DTC growth"),
        ("plays/marketplace", "Marketplaces"),
        ("plays/b2b-plg", "B2B PLG"),
        ("plays/content-flywheel", "Content flywheel"),
    ]),
]


def p(title, desc, body, rt=3, prev=None, nxt=None):
    return {'title': title, 'description': desc, 'body': body, 'reading_time': rt, 'prev': prev, 'next': nxt}


def quick(title, desc, intro, sections):
    """Generate a compact page with intro + numbered sections."""
    html = f'<p class="lede">{intro}</p>'
    for h, body in sections:
        html += f'<h2>{h}</h2>'
        if isinstance(body, list):
            html += '<ul>' + ''.join(f'<li>{i}</li>' for i in body) + '</ul>'
        else:
            html += f'<p>{body}</p>'
    return p(title, desc, html)


PAGES = {
    "index": p("Growth Marketing",
        "A 45-page reference on modern growth marketing: acquisition, activation, retention, revenue, analytics, experimentation.",
        """
<p class="lede">Growth marketing is the discipline of systematically improving the metrics that matter: acquisition, activation, retention, revenue, referral. It's not a collection of tricks; it's a set of frameworks and a culture of experimentation.</p>

<h2>The nine sections</h2>
<div class="cards" style="margin-top:32px;">
<a href="foundations/what-is-growth.html" class="card"><h3>Foundations</h3><p>North Star Metric, loops vs funnels, retention first.</p></a>
<a href="acq/channel-fit.html" class="card"><h3>Acquisition</h3><p>Channels, paid vs organic, viral, partnerships.</p></a>
<a href="activation/aha-moment.html" class="card"><h3>Activation</h3><p>Aha moments, onboarding, time to value.</p></a>
<a href="retention/cohort-analysis.html" class="card"><h3>Retention</h3><p>Cohorts, churn, habit formation.</p></a>
<a href="revenue/pricing.html" class="card"><h3>Revenue</h3><p>Pricing, upsell, conversion, referrals.</p></a>
<a href="analytics/event-tracking.html" class="card"><h3>Analytics</h3><p>Events, funnels, cohorts, attribution.</p></a>
<a href="experiments/ab-testing.html" class="card"><h3>Experimentation</h3><p>A/B, holdout, significance, velocity.</p></a>
<a href="process/growth-team-structure.html" class="card"><h3>Teams + Process</h3><p>Team structure, models, ICE, sprints.</p></a>
<a href="plays/saas-growth.html" class="card"><h3>Playbooks</h3><p>SaaS, DTC, marketplace, PLG, content.</p></a>
</div>
"""),

    "foundations/what-is-growth": quick("What is growth marketing?",
        "Growth marketing is systematic improvement of acquisition, activation, retention, revenue, referral across the full customer lifecycle.",
        "Growth marketing is the discipline of using data and experimentation to improve every stage of the customer journey, not just the top of the funnel. It emerged in the 2010s as SaaS companies needed more than traditional marketing could deliver.",
        [
            ("What it isn't", "Growth marketing isn't 'hacks' or viral schemes. It's disciplined experimentation across the full funnel."),
            ("The AARRR framework", ["Acquisition - how users find you", "Activation - first meaningful value", "Retention - users coming back", "Revenue - monetization", "Referral - users bringing others"]),
            ("Why it matters", "Traditional marketing optimized top-of-funnel. Growth marketing optimizes end-to-end - a 10% lift in retention often beats a 50% lift in acquisition."),
            ("Who does it", "Full-stack marketers, product managers, growth engineers. A hybrid role blending marketing, product, and data."),
        ]),

    "foundations/north-star-metric": quick("The North Star Metric",
        "One metric that captures the core value your product delivers. Everything aligns to it.",
        "The North Star Metric is the single metric that best captures the core value your product creates. It's the number you optimize above all others.",
        [
            ("Characteristics", ["Directly reflects customer value", "Leading indicator of revenue", "Measurable with your data", "Single number, not a ratio"]),
            ("Examples", ["Airbnb: nights booked", "Spotify: time listening", "Slack: messages sent within teams", "Amazon: monthly active buyers"]),
            ("How to pick", "Start with what customers actually do when they get value. Messages sent, photos shared, meetings booked. Not signups or logins."),
            ("Avoiding vanity", "Signups, downloads, page views are vanity. North Star should be measurable engagement with the core value."),
        ]),

    "foundations/growth-loops": quick("Growth loops vs funnels",
        "Funnels leak. Loops compound. Modern growth thinking shifts from funnel optimization to loop design.",
        "A funnel is linear: acquire → activate → retain → expand. A loop is circular: each acquired customer drives more acquisition via referrals, content, or network effects. Loops compound; funnels leak.",
        [
            ("Viral loops", "One user invites others who become users who invite others. Dropbox referral program was the classic."),
            ("Content loops", "Users create content, content attracts visitors, visitors convert to users who create more content. Pinterest, Quora, Stack Overflow."),
            ("Paid loops", "Revenue from acquired customers funds acquisition of more customers. Only works when LTV:CAC is strong."),
            ("Sales-led loops", "Sales close customers who refer more customers. B2B enterprise."),
            ("Why they beat funnels", "A funnel's output is a fraction of its input (decay). A loop's output grows its own input (compound)."),
        ]),

    "foundations/retention-first": quick("Retention first",
        "Retention is the most important metric. Without it, acquisition just fills a leaking bucket.",
        "Retention compounds. A 10% improvement in retention often outperforms a 50% improvement in acquisition because retained users contribute repeatedly and refer.",
        [
            ("The math", "If you retain 40% of users after month 1, you need to acquire constantly to grow. If you retain 70%, growth compounds."),
            ("Measuring", "Cohort retention: what % of users who signed up in month X are active in month X+1, X+3, X+6?"),
            ("The curve shape", ["Declining-then-flattening: sustainable", "Declining-to-zero: product-market-fit problem"]),
            ("Before investing in acquisition", "Get retention above benchmark for your category. Then scale acquisition."),
        ]),

    # ACQUISITION (6)
    "acq/channel-fit": quick("Channel-market fit",
        "Not every channel works for every product. Here's the framework for picking channels.",
        "Channel-market fit is whether the channel's audience and intent match your product. Wrong channel = wasted spend.",
        [
            ("Questions to ask", ["Is your ICP on this channel?", "What intent do they have when using it?", "Can you afford CACs on this channel given your LTV?"]),
            ("Channels by product type", ["Consumer visual: Meta, TikTok, Pinterest", "B2B with role targeting: LinkedIn, Google", "Local services: Google Search, Nextdoor", "Creator / audience-based: YouTube, podcasts", "Developer tools: GitHub, Hacker News, Reddit"]),
            ("Order of operations", "Pick the single most-obvious channel, validate, scale, then add second."),
            ("Avoid", "Being on every channel with weak presence. Focus beats spread."),
        ]),

    "acq/paid-vs-organic": quick("Paid vs organic",
        "Paid is fast but stops when you stop paying. Organic compounds but takes time. Most businesses need both.",
        "Paid and organic acquisition have opposite profiles. Paid produces predictable volume at ongoing cost. Organic (SEO, content, word-of-mouth) builds slower but compounds.",
        [
            ("Paid characteristics", ["Immediate traffic", "Ongoing cost", "Control over volume", "Stops when budget stops"]),
            ("Organic characteristics", ["Slow to start (3-12 months)", "Compounds", "Lower per-user cost over time", "Hard to control volume"]),
            ("When paid wins", "Validated offer, need fast test or scale, unit economics support it."),
            ("When organic wins", "Long-term moat building, compounds value, differentiated content or brand."),
            ("The pragmatic answer", "Run paid to validate and scale what works. Build organic in parallel for long-term defensibility."),
        ]),

    "acq/content-seo": quick("Content + SEO",
        "Content marketing is organic acquisition's workhorse. Here's the strategy that works in 2026.",
        "Content + SEO is still one of the highest-leverage acquisition channels. Well-ranked content compounds: a post ranking #1 brings traffic for years.",
        [
            ("The playbook", ["Target search intent, not just keywords", "Build topical authority via content clusters", "Write for humans first, optimize for SEO second", "Update old content regularly"]),
            ("Keyword targeting", "Focus on problem-aware and solution-aware queries. Avoid pure top-of-funnel informational unless you have SEO authority."),
            ("Frequency", "1-2 quality posts per week beats 5 mediocre. Compounding rewards quality."),
            ("AI-era considerations", "Generic AI-generated content ranks poorly. Original insight, specific examples, and expertise still win."),
        ]),

    "acq/viral-loops": quick("Viral loops",
        "Viral loops create compounding acquisition. Here's what makes them work.",
        "A viral loop: one user triggers more users to join. K-factor (invites × conversion rate) determines if it grows. K > 1 = true viral.",
        [
            ("Types", ["Incentive-based (refer-a-friend rewards)", "Utility-based (Dropbox - need to share files)", "Social (WhatsApp - need the other person to receive)", "Content-based (Reddit posts drive more users)"]),
            ("Rarely K > 1", "Most products claiming virality have sub-1 K-factors. They still benefit (lower CAC) but don't grow on their own."),
            ("Building", ["Make sharing the natural path", "Reward both sides (sender + receiver)", "Shorten the cycle (time from invite to active)", "Track K-factor explicitly"]),
            ("Common failure", "Adding a referral program to a product nobody shares organically. Fix the product first."),
        ]),

    "acq/product-led": quick("Product-led acquisition",
        "The product itself acquires users. Freemium, free trials, viral sharing.",
        "Product-led growth uses the product as the primary acquisition vehicle. Users find value before buying, share organically, drive adoption within teams.",
        [
            ("Common patterns", ["Freemium (Slack, Notion)", "Free trial (most SaaS)", "Open-core (many dev tools)", "Viral invites (Zoom, Calendly)"]),
            ("Requires", ["Self-serve onboarding", "Clear aha moment in free tier", "Natural expansion paths", "Sticky usage patterns"]),
            ("PLG metrics", ["Time to aha", "Freemium to paid conversion", "Self-serve revenue %", "Expansion MRR"]),
            ("Not for everyone", "PLG works for horizontal tools used by many. Doesn't fit enterprise with committee buying or complex custom needs."),
        ]),

    "acq/partnerships": quick("Partnerships",
        "Strategic partnerships unlock acquisition channels you can't build alone. Here's the playbook.",
        "Partnerships reach audiences you don't have access to. Done right, they're high-leverage. Done wrong, they're busywork.",
        [
            ("Types", ["Integration partnerships (Zapier, ecosystems)", "Content co-marketing (guest posts, webinars)", "Affiliate programs", "White-label", "Reseller / channel"]),
            ("Evaluation", ["Does partner audience overlap with your ICP?", "Is there mutual value (not just you getting leads)?", "What's the realistic volume?"]),
            ("Structure", ["Joint content / webinars", "Newsletter swaps", "Referral revenue share", "Product integrations"]),
            ("Common mistakes", ["Vague partnerships without clear deliverables", "Too many small partnerships spread thin", "Not tracking source of users"]),
        ]),

    # ACTIVATION (5)
    "activation/aha-moment": quick("The aha moment",
        "The aha moment is when a new user first experiences core product value. Everything before is setup; everything after is retention.",
        "The aha moment is the specific action or experience where a new user thinks 'I get it, this is valuable.' Finding and optimizing for the aha moment is the core of activation.",
        [
            ("Examples", ["Facebook: adding 7 friends in 10 days", "Slack: sending 2,000 messages in a team", "Dropbox: installing on 2+ devices", "Twitter: following 30 people"]),
            ("How to find yours", "Analyze retention by early actions. What did retained users do in week 1 that churned users didn't?"),
            ("Then", "Design onboarding to get new users to that action as fast as possible."),
            ("Common mistake", "Making the aha moment too hard to reach. Shorten the path relentlessly."),
        ]),

    "activation/onboarding-design": quick("Onboarding design",
        "New user onboarding is where activation happens. Design every step for speed to value.",
        "Onboarding is the span from signup to first meaningful value. Every friction point drops activation by a measurable percentage.",
        [
            ("Principles", ["Get to value in first session", "Progressive disclosure (don't show everything)", "One focused action per step", "Celebrate progress"]),
            ("Common patterns", ["Empty-state CTAs pushing to aha", "In-product guided tours (used sparingly)", "Pre-populated templates", "First-task wizards"]),
            ("Measurement", ["% reaching aha moment within X days", "% completing onboarding checklist", "Time from signup to first value"]),
            ("Avoid", ["Tutorial walls that block product use", "Video-only onboarding for tools (show, don't tell)", "Asking for everything upfront"]),
        ]),

    "activation/time-to-value": quick("Time to value",
        "The time between signup and first meaningful value. The shorter, the higher activation.",
        "Time to value (TTV) measures how long a new user takes to experience the product's core value. Lower TTV = higher activation = better retention.",
        [
            ("Targets", ["SaaS consumer: under 5 minutes", "SaaS B2B: under 30 minutes for first aha", "Enterprise: first week if onboarding-assisted"]),
            ("Shortening TTV", ["Pre-fill or import data", "Offer templates/defaults", "Hide advanced features", "Reduce required setup"]),
            ("Measurement", "Event tracking - timestamp signup, timestamp first-value event, measure the gap."),
            ("The friction audit", "Walk through onboarding as a new user. Every step that requires thinking or typing is potential removal."),
        ]),

    "activation/empty-states": quick("Empty states",
        "Empty states are what new users see before they've added data. Most are wasted. Good empty states drive action.",
        "Empty states are the most important UI surface for activation. A new user with no data sees empty states constantly; each one is a chance to guide the next action.",
        [
            ("Weak empty state", "'No items yet' with a shrug icon. Doesn't help."),
            ("Strong empty state", ["Clear explanation of what goes here", "One clear action button", "Optional: example or template", "Optional: brief why this matters"]),
            ("Common opportunity", "Every table, list, or dashboard has an empty state. Most are 'no data' placeholder. Each is an activation opportunity."),
            ("Measure", "Click-through rate on empty-state CTAs. Optimize the ones users hit most."),
        ]),

    "activation/early-wins": quick("Early wins",
        "The first small wins users experience in a product disproportionately predict retention.",
        "Early wins are the small moments of success a new user experiences in their first sessions. More early wins → higher retention.",
        [
            ("Examples", ["Sending the first message", "Creating the first project", "Getting the first response", "Seeing first data", "Completing first task"]),
            ("Design for", "Build onboarding around achieving multiple small wins in the first session - not one big win at the end."),
            ("Celebrating wins", "Acknowledge wins: confetti, notification, progress bar. Minor dopamine hits reinforce."),
            ("Avoid fake wins", "Don't congratulate users for achievements that aren't real. Users feel condescension."),
        ]),

    # RETENTION (5)
    "retention/cohort-analysis": quick("Cohort analysis",
        "Cohort analysis tracks users grouped by signup time to see how retention evolves.",
        "Cohort analysis groups users by their signup period and tracks behavior over time. Reveals trends that aggregate metrics hide.",
        [
            ("What it shows", ["Is retention improving cohort-over-cohort?", "When does decay stabilize?", "Are newer cohorts retaining differently?"]),
            ("Standard view", "Y-axis: cohort (signup month). X-axis: months since signup. Cell value: % retained."),
            ("Healthy curves", "Sharp initial drop (users who never activate), then flatten into a retention plateau."),
            ("Tools", ["Mixpanel, Amplitude cohort reports", "Google Analytics 4 (basic)", "Custom SQL for tailored views"]),
        ]),

    "retention/churn-diagnostics": quick("Churn diagnostics",
        "Churn is the symptom. Here's how to find the cause.",
        "Understanding why users leave is as important as reducing churn. Surface-level fixes without root-cause analysis rarely work.",
        [
            ("Segments", ["Churn by signup cohort", "By plan tier", "By acquisition channel", "By usage pattern"]),
            ("Qualitative", ["Exit surveys (short, at cancel)", "Churn interviews (5-10 users, phone)", "Support tickets review"]),
            ("Common causes", ["Price sensitivity", "Missing feature", "Poor onboarding", "Better alternative found", "Business situation changed"]),
            ("Actionable output", "Categorize 100 churned users. Top 2 causes become focus for retention work."),
        ]),

    "retention/re-engagement": quick("Re-engagement",
        "Inactive users can often be re-activated. Here's when and how.",
        "Users who go inactive haven't necessarily churned. Re-engagement campaigns can recover some - if done right.",
        [
            ("Timing", "Sweet spot is usually 7-30 days of inactivity. Too soon feels intrusive; too late they've moved on."),
            ("Channels", ["Email (most common)", "Push notifications (app users)", "SMS (use rarely)", "Retargeting ads (for larger cohorts)"]),
            ("Message patterns", ["What's new / what you missed", "Specific new feature", "Discount or promo (last resort)", "Question to re-engage"]),
            ("Measure", "% re-engaged within 14 days. Don't just count opens."),
        ]),

    "retention/habit-formation": quick("Habit formation",
        "Products that form habits retain better. Here's how habit design works.",
        "A user habit is regular, triggered, rewarding behavior. Products that establish habits in users retain dramatically better.",
        [
            ("The hook cycle (Nir Eyal)", ["Trigger (external or internal)", "Action (minimal friction)", "Variable reward", "Investment (data, config, social)"]),
            ("Product examples", ["Duolingo: streak + notification", "Instagram: scroll + variable content", "Wordle: once per day ritual"]),
            ("Investment matters", "Users who invest (customize, add data, connect accounts) retain much better than users who passively consume."),
            ("Ethical guardrails", "Habits that serve users win long-term. Dark-pattern habits generate churn and brand damage eventually."),
        ]),

    "retention/feature-adoption": quick("Feature adoption",
        "Adoption of key features predicts retention. Here's how to drive it.",
        "Not every feature retains equally. Understanding which features predict retention, then nudging users toward them, is retention leverage.",
        [
            ("Find your sticky features", "Analyze retention by which features users adopted. Some features are strongly correlated with retention; others aren't."),
            ("Then nudge", ["Empty-state CTAs", "In-app recommendations", "Email nudges for users who haven't tried the feature", "Onboarding updates to surface the feature"]),
            ("Avoid", ["Feature promotion for sake of engagement metric", "Annoying prompts users ignore", "Celebrating shallow feature touches (open doesn't = adoption)"]),
        ]),

    # REVENUE (5)
    "revenue/pricing": quick("Pricing",
        "Pricing is the single highest-leverage lever in a business. Most companies price too low.",
        "Every 1% improvement in pricing drops ~10% to the bottom line in most businesses. Yet pricing gets less attention than any other metric.",
        [
            ("Three approaches", ["Cost-plus (weak): cost + margin", "Competitor-based (lazy): what others charge", "Value-based (best): fraction of value delivered"]),
            ("Signals to raise price", ["Close rate above 50% (leaving money on table)", "Low price sensitivity in sales objections", "Meaningful LTV without equivalent CAC justification"]),
            ("Packaging", ["Good-better-best often outperforms single-price", "Anchor with premium tier", "Most customers pick middle (by design)"]),
            ("Testing", "A/B test price on signup page. Watch not just conversion but revenue per visitor."),
        ]),

    "revenue/upsell-expansion": quick("Upsell + expansion",
        "Growing revenue from existing customers is cheaper than acquiring new ones. Here's how.",
        "Expansion MRR (net new revenue from existing customers) is one of the best growth levers. Net Revenue Retention >100% means your customer base grows revenue even without new customers.",
        [
            ("Paths", ["Usage expansion (more seats, more volume)", "Tier upgrades", "Additional products (cross-sell)", "Price increases on renewal"]),
            ("Timing", ["Annual review for tier upgrades", "Usage-triggered prompts when limits hit", "Launch windows for new products"]),
            ("Process", ["Dedicated CS/AM role for expansion", "Product-triggered in-app prompts", "Usage-based pricing (auto-expansion)"]),
        ]),

    "revenue/conversion-rate": quick("Conversion rate",
        "Conversion rate optimization is the practice of improving % of visitors who convert.",
        "Conversion rate directly affects revenue per visitor. Tiny improvements compound with traffic.",
        [
            ("Benchmarks", ["E-commerce: 2-4% typical, 5%+ strong", "SaaS free trial: 15-25% to paid", "B2B demo-to-customer: 15-30%"]),
            ("Levers", ["Landing page copy and design", "Form length and friction", "Pricing clarity", "Social proof", "Trust signals", "CTA placement"]),
            ("Process", "A/B test continuously. Hypothesize → test → measure → keep winners."),
            ("Avoid", ["Testing trivial changes (button color alone)", "Testing without enough traffic", "Over-optimizing at the cost of quality"]),
        ]),

    "revenue/referrals": quick("Referrals",
        "Referrals are the highest-quality, lowest-cost acquisition. Here's how to engineer them.",
        "Referred customers retain better, pay more, and cost less to acquire. Most businesses get some referrals; few engineer them.",
        [
            ("Non-programmatic", "Some products generate referrals organically (Slack, Dropbox). Most don't."),
            ("Referral programs", ["Incentive both sides (referrer + referee)", "Make referring easy", "Time limits drive action", "Track attribution"]),
            ("B2B referrals", "Ask explicitly after delivering value. Structured ask: 'who else do you know who has [X problem]?'"),
            ("Measurement", ["% new customers referred", "CAC of referred vs other", "LTV of referred vs other"]),
        ]),

    "revenue/ltv-expansion": quick("LTV expansion",
        "LTV isn't fixed. Deliberate LTV growth programs extend every customer's value.",
        "Increasing LTV has compound effects: every acquisition pays back more, referrals grow, unit economics improve.",
        [
            ("Levers", ["Reduce churn", "Increase purchase frequency", "Increase average order value", "Extend relationship duration", "Add new products/services"]),
            ("Cohort analysis", "Measure LTV by cohort. Do newer cohorts show higher LTV? If not, retention work."),
            ("LTV per segment", "Don't use blended LTV. Segment by channel, product, customer size. Some segments have 5x LTV of others."),
        ]),

    # ANALYTICS (5)
    "analytics/event-tracking": quick("Event tracking",
        "Event tracking is the foundation of growth analytics. Without clean events, you can't measure anything.",
        "Events are actions users take: signup, create project, invite teammate, upgrade. Every growth metric derives from events.",
        [
            ("What to track", ["Core value events (the aha moment)", "Conversion events (signup, upgrade)", "Retention events (returning actions)", "Friction events (errors, abandonment)"]),
            ("Naming conventions", ["Verb-noun (create_project, send_message)", "Consistent casing", "Avoid future-tense or vague names"]),
            ("Properties matter", "Attach properties to events: plan, device, source. Filter and segment later."),
            ("Don't overtrack", "Tracking everything is noise. Track purposefully."),
        ]),

    "analytics/funnels": quick("Funnels",
        "Funnel analysis shows where users drop off between key steps.",
        "A funnel is a sequence of steps. Funnel analysis measures conversion between each step, revealing bottlenecks.",
        [
            ("Example", "Visit → Signup → Activate → Paid = drop-off at each step."),
            ("Funnel insights", ["Which step loses most users?", "Do different segments have different conversion?", "How has it changed over time?"]),
            ("Optimize the worst step first", "Biggest loss = biggest opportunity."),
            ("Multi-step paths", "Real user journeys aren't linear. Supplement funnels with path analysis."),
        ]),

    "analytics/cohorts": quick("Cohort dashboards",
        "Cohort dashboards track retention, revenue, and behavior by cohort. Core growth instrument.",
        "Cohort dashboards show how groups of users behave over time. Trend analysis, not snapshots.",
        [
            ("Key views", ["Retention by cohort", "Revenue per user by cohort", "Feature adoption by cohort", "LTV cumulative by cohort"]),
            ("What to look for", ["Improvement cohort-over-cohort", "Anomalies (sudden drop)", "Segment differences"]),
        ]),

    "analytics/attribution": quick("Attribution",
        "Attribution is which channels get credit for conversions. Post-privacy, it's noisy.",
        "Attribution models assign credit to touchpoints in the customer journey. Multi-touch attribution is ideal; reality post-privacy is multi-touch plus MMM plus holdouts.",
        [
            ("Models", ["Last-click (simple, biased toward bottom of funnel)", "First-click (biased toward top)", "Linear (equal across all touches)", "Data-driven (algorithmic)"]),
            ("Tools", ["Platform self-report (biased)", "GA4 data-driven", "MMM for macro view", "Holdout tests for ground truth"]),
            ("Pragmatic approach", "Use platform data directionally, MER for truth, holdouts for validation."),
        ]),

    "analytics/north-star-dashboards": quick("North Star dashboards",
        "A dashboard built around your North Star Metric keeps the team focused.",
        "Your most important dashboard shows North Star Metric + supporting indicators. Everyone sees it; everyone aligns to it.",
        [
            ("Components", ["North Star value (current)", "7-day and 30-day trend", "Supporting leading indicators (what drives it)", "Segment breakdowns"]),
            ("Keep it simple", "10 tiles max. More than that and no one reads it."),
            ("Display publicly", "Team room display or always-open tab builds shared awareness."),
        ]),

    # EXPERIMENTS (5)
    "experiments/ab-testing": quick("A/B testing",
        "A/B testing compares two variants to determine which performs better. Standard growth tool.",
        "A/B tests split traffic between variant A and variant B, measure outcomes, pick winner. The core unit of experimentation.",
        [
            ("Setup", ["Clear hypothesis before running", "Single variable changed", "Sufficient sample size", "Fixed duration"]),
            ("Sample size", "Use calculator (VWO, Optimizely). Below-significance results are noise."),
            ("Run time", "At least one full week to cover weekly cycles."),
        ]),

    "experiments/holdout-tests": quick("Holdout tests",
        "Holdout tests exclude a segment from a treatment to measure true incremental impact.",
        "Classical A/B has confounds. Holdouts are cleaner: half the audience gets the feature/message, half doesn't. Compare.",
        [
            ("Examples", ["Geo holdout for paid ads", "User holdout for a retention email", "Feature holdout for rollouts"]),
            ("Why better than A/B", "Can measure incrementality - what wouldn't have happened without the treatment."),
            ("Cost", "Holdout group gets worse experience (no new feature). Minimize duration."),
        ]),

    "experiments/multivariate": quick("Multivariate testing",
        "Test multiple variables simultaneously. More complex than A/B, needs more traffic.",
        "Multivariate testing varies multiple elements (headline, image, CTA) at once. Reveals interaction effects but requires significant traffic.",
        [
            ("When to use", "You have enough traffic for 4-8 variants and suspect interactions between variables."),
            ("When not", "Low-traffic pages where you can barely get one A/B to significance."),
            ("Analysis", "Statistical models to isolate main effects and interactions. More complex than comparing two numbers."),
        ]),

    "experiments/statistical-significance": quick("Statistical significance",
        "The threshold that tells you your test result isn't random noise.",
        "Statistical significance tells you the observed difference is unlikely to be random. 95% confidence is standard.",
        [
            ("Key concepts", ["p-value: probability the result is random", "Confidence interval: range of likely true values", "Sample size: larger = narrower confidence"]),
            ("Common mistakes", ["Stopping tests early (p-hacking)", "Running too many tests without correction", "Interpreting non-significance as 'no effect'"]),
            ("Pragmatic threshold", "95% confidence, minimum sample size for effect size of interest."),
        ]),

    "experiments/velocity": quick("Experiment velocity",
        "Number of experiments per week. Higher velocity = more learning = more wins.",
        "Experiment velocity is the rate of running tests. High velocity compounds learning over time. Low velocity means slow progress.",
        [
            ("Typical velocity", ["Early stage: 1-2 tests per week", "Mature growth team: 5-10+ per week", "Top teams: 20+ per week"]),
            ("Building velocity", ["Templates for common test types", "Experimentation infrastructure (Optimizely, Split, LaunchDarkly)", "Backlog of hypotheses", "Regular planning cadence"]),
            ("Quality vs quantity", "Bad tests at high velocity is wasted effort. Good hypotheses + discipline beat noise."),
        ]),

    # PROCESS (4)
    "process/growth-team-structure": quick("Growth team structure",
        "Growth teams sit between product, marketing, and engineering. Here's how to structure them.",
        "Growth team structure depends on company stage and what you're optimizing. Common models: embedded in product, embedded in marketing, or standalone.",
        [
            ("Roles", ["Head of Growth / VP Growth", "Growth PM", "Growth marketer", "Growth engineer", "Data analyst"]),
            ("Models", ["Standalone team (owns full funnel)", "Embedded in product (activation/retention)", "Embedded in marketing (acquisition)", "Matrix (reports into both)"]),
            ("Early stage", "Single full-stack person. As scale grows, split into specialties."),
        ]),

    "process/growth-models": quick("Growth models",
        "A growth model quantifies the levers that drive your key metrics.",
        "A growth model is a spreadsheet or diagram showing how inputs (traffic, conversion, retention) connect to outputs (MRR, revenue).",
        [
            ("Purpose", ["Prioritize levers by impact", "Forecast outcomes of changes", "Align team on what matters"]),
            ("Components", ["Inputs: traffic, conversion rates, retention, LTV, CAC", "Formulas linking them", "Outputs: MRR, revenue, users"]),
            ("Simple version", "Even a 20-cell spreadsheet showing channels → visitors → signups → activations → paid → MRR is valuable."),
        ]),

    "process/ice-scoring": quick("ICE scoring",
        "A simple prioritization framework: Impact × Confidence × Ease.",
        "ICE is a lightweight way to prioritize growth experiments. Rate each 1-10 on Impact, Confidence, Ease. Score = product. Pick highest scores.",
        [
            ("Variables", ["Impact: how big if it works", "Confidence: how sure you are it'll work", "Ease: how simple to build and test"]),
            ("Usage", "Backlog every week. Rank by ICE. Top-scoring tests go first."),
            ("Critiques", "Subjective scoring. Use for ranking relative priority, not absolute decisions."),
        ]),

    "process/sprint-rhythm": quick("Sprint rhythm",
        "Growth experimentation benefits from a consistent weekly rhythm.",
        "Weekly cadence beats sporadic experimentation. Consistent rhythm: plan, ship, measure, learn, repeat.",
        [
            ("Typical week", ["Monday: review last week, plan this week", "Tuesday-Thursday: ship tests", "Friday: measure running tests, write up learnings"]),
            ("Growth retrospective", "Monthly or quarterly: what worked, what didn't, what's next."),
        ]),

    # PLAYBOOKS (5)
    "plays/saas-growth": quick("SaaS growth playbook",
        "The playbook for growing a SaaS product.",
        "SaaS growth has specific mechanics: recurring revenue, compounding retention, expansion. Classic plays work.",
        [
            ("Sequence", ["PMF first (qualitative + 40% rule)", "Activation tuning", "Retention bar-raising", "Scale acquisition", "Expansion + pricing"]),
            ("Key metrics", ["MRR", "Net Revenue Retention", "CAC payback", "Free-to-paid conversion", "Churn"]),
            ("Levers", ["Onboarding → activation", "Feature adoption → retention", "Pricing + packaging → expansion"]),
        ]),

    "plays/dtc-growth": quick("DTC growth playbook",
        "Growth for direct-to-consumer brands.",
        "DTC growth revolves around paid acquisition economics, retention via email/SMS, and LTV expansion.",
        [
            ("Flywheel", ["Paid acquisition (Meta, Google, TikTok)", "First purchase activation", "Email/SMS retention", "Subscription or repeat purchase", "Referral + UGC"]),
            ("Unit economics", ["CAC < 1/3 LTV", "Payback under 12 months", "MER > 3x"]),
            ("Creative is king", "Creative volume drives paid performance more than any other lever."),
        ]),

    "plays/marketplace": quick("Marketplace growth",
        "Two-sided marketplaces have unique growth challenges: cold-start, network effects, liquidity.",
        "Marketplaces need supply AND demand. Growth = solving cold start then building liquidity, then scale.",
        [
            ("Cold start", ["Pick a narrow niche", "Fake one side if needed (manual concierge, curated inventory)", "Grow one side first"]),
            ("Liquidity metrics", ["Match rate", "Time to match", "Supply/demand balance"]),
            ("Network effects", "Each new user makes the product more valuable for others - the moat."),
        ]),

    "plays/b2b-plg": quick("B2B product-led growth",
        "B2B PLG: freemium or self-serve, bottom-up adoption, expansion to teams.",
        "B2B PLG reaches users before the buyer. User loves product, brings it into team, team adopts, enterprise deal follows.",
        [
            ("Examples", ["Slack", "Figma", "Notion", "Loom"]),
            ("Stages", ["Individual user adopts", "Invites teammate", "Team buys plan", "Company-wide enterprise"]),
            ("Motion requirements", ["Self-serve onboarding", "Immediate value in free tier", "Natural expansion paths", "Enterprise sales team for deals above certain size"]),
        ]),

    "plays/content-flywheel": quick("Content flywheel",
        "Content compounds into an acquisition moat. Here's the playbook.",
        "Content marketing is slow but compounds. Well-executed content flywheels generate organic traffic for years and become competitive moats.",
        [
            ("Structure", ["Pillar topics in your space", "Supporting content clusters", "Internal linking for authority", "Regular publishing cadence"]),
            ("Quality bar", "One genuinely-good post beats 10 mediocre. Invest."),
            ("Distribution", "Great content isn't enough. Distribute via email, social, partnerships, SEO."),
            ("Patience", "6-12 months for compounding effects. Year 2-3 is when flywheels really spin."),
        ]),
}


if __name__ == "__main__":
    build_expertise_section("growth-marketing", "Growth Marketing", SIDEBAR, PAGES)
