#!/usr/bin/env python3
"""Paid Advertising expertise - 50 pages."""
from _build_expertise import build_expertise_section

SECTION_SLUG = "paid-ads"
SECTION_NAME = "Paid Advertising"

SIDEBAR = [
    ("Foundations", [
        ("index", "Overview"),
        ("foundations/how-paid-works", "How paid ads actually work"),
        ("foundations/unit-economics", "Unit economics"),
        ("foundations/channel-fit", "Channel-market fit"),
        ("foundations/when-to-run-paid", "When to run paid"),
    ]),
    ("Meta (Facebook + Instagram)", [
        ("meta/overview", "Meta Ads overview"),
        ("meta/account-structure", "Account structure"),
        ("meta/campaign-types", "Campaign types"),
        ("meta/audiences", "Audiences and targeting"),
        ("meta/creative-testing", "Creative testing"),
        ("meta/ios14-reality", "iOS 14+ reality"),
        ("meta/scaling", "Scaling campaigns"),
        ("meta/retargeting", "Retargeting"),
    ]),
    ("Google Ads", [
        ("google/overview", "Google Ads overview"),
        ("google/search-vs-display", "Search vs Display vs Pmax"),
        ("google/keyword-research", "Keyword research"),
        ("google/match-types", "Match types"),
        ("google/quality-score", "Quality Score"),
        ("google/rsa-copy", "Responsive Search Ad copy"),
        ("google/bidding", "Bidding strategies"),
        ("google/pmax", "Performance Max"),
    ]),
    ("TikTok Ads", [
        ("tiktok/overview", "TikTok Ads overview"),
        ("tiktok/creative-first", "Creative-first approach"),
        ("tiktok/spark-ads", "Spark Ads"),
        ("tiktok/ugc-production", "UGC production"),
        ("tiktok/when-tiktok-works", "When TikTok works"),
    ]),
    ("LinkedIn Ads", [
        ("linkedin/overview", "LinkedIn Ads overview"),
        ("linkedin/b2b-targeting", "B2B targeting"),
        ("linkedin/ad-formats", "Ad formats"),
        ("linkedin/cost-reality", "Cost reality"),
        ("linkedin/lead-gen-forms", "Lead gen forms"),
    ]),
    ("YouTube Ads", [
        ("youtube/overview", "YouTube Ads overview"),
        ("youtube/formats", "YouTube ad formats"),
        ("youtube/creative-patterns", "Creative patterns"),
        ("youtube/targeting", "Targeting options"),
        ("youtube/vs-meta", "YouTube vs Meta"),
    ]),
    ("Creative + Copy", [
        ("creative/hook-patterns", "Hook patterns"),
        ("creative/ugc-vs-produced", "UGC vs produced"),
        ("creative/creative-volume", "Creative volume"),
        ("creative/ad-copy", "Ad copy"),
        ("creative/landing-pages", "Landing pages"),
        ("creative/creative-fatigue", "Creative fatigue"),
        ("creative/hiring-creators", "Hiring creators"),
    ]),
    ("Attribution + Measurement", [
        ("measurement/why-attribution-broke", "Why attribution broke"),
        ("measurement/platform-attribution", "Platform attribution"),
        ("measurement/mer-blended", "MER and blended metrics"),
        ("measurement/incrementality", "Incrementality testing"),
        ("measurement/mmm", "Marketing mix modeling"),
        ("measurement/ltv-cac", "LTV:CAC"),
        ("measurement/dashboards", "Dashboards that matter"),
    ]),
]


def page(title, description, body, reading_time=4, prev=None, nxt=None):
    return {
        'title': title,
        'description': description,
        'body': body,
        'reading_time': reading_time,
        'prev': prev,
        'next': nxt,
    }


PAGES = {
    "index": page("Paid Advertising",
        "A 50-page reference on modern paid advertising: Meta, Google, TikTok, LinkedIn, YouTube. Strategy, creative, attribution.",
        """
<p class="lede">Paid advertising in 2026 is different from paid advertising in 2020. Attribution is noisy. Platforms are restrictive. Creative is the dominant lever. This section is 50 pages on what actually works now, platform by platform, plus the measurement and creative disciplines that make all of it compound.</p>

<h2>The eight sections</h2>
<div class="cards" style="margin-top:32px;">
<a href="foundations/how-paid-works.html" class="card"><h3>Foundations</h3><p>How auctions work, unit economics, channel-market fit.</p></a>
<a href="meta/overview.html" class="card"><h3>Meta Ads</h3><p>Facebook + Instagram: the workhorse of DTC and consumer.</p></a>
<a href="google/overview.html" class="card"><h3>Google Ads</h3><p>Search, Shopping, Performance Max: still the intent leader.</p></a>
<a href="tiktok/overview.html" class="card"><h3>TikTok Ads</h3><p>Creative-first platform. Different rules.</p></a>
<a href="linkedin/overview.html" class="card"><h3>LinkedIn Ads</h3><p>B2B workhorse, expensive per click, high intent.</p></a>
<a href="youtube/overview.html" class="card"><h3>YouTube Ads</h3><p>Video at scale. Skippable, long-form, demand-gen.</p></a>
<a href="creative/hook-patterns.html" class="card"><h3>Creative + Copy</h3><p>Hooks, UGC, ad copy, creative fatigue.</p></a>
<a href="measurement/why-attribution-broke.html" class="card"><h3>Measurement</h3><p>Attribution post-iOS 14, MER, incrementality, MMM.</p></a>
</div>
""",
        reading_time=3),

    # FOUNDATIONS
    "foundations/how-paid-works": page("How paid ads actually work",
        "Every major paid platform is an auction optimizing for the platform's objective. Understanding the mechanics changes how you run.",
        """
<p class="lede">Every major ad platform runs an auction. Advertisers bid; the platform picks winners based on bid + expected outcome + ad quality. Understanding this mechanism changes how you think about targeting, bidding, and creative.</p>

<h2>The auction in 60 seconds</h2>
<p>When a user triggers an ad slot, the platform looks at every advertiser who's eligible to show. For each, it computes:</p>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px;">Expected revenue to platform = bid × expected conversion rate × ad quality</pre>
<p>Highest expected revenue wins. The platform optimizes its own revenue, not yours.</p>

<h2>What this means for you</h2>
<ul>
<li><strong>Creative quality matters more than bid.</strong> A cheap ad with 3x the CTR beats an expensive ad with 1x CTR.</li>
<li><strong>The algorithm gets smarter with data.</strong> Early campaigns perform worse because the platform has no signal. Feed it conversions quickly.</li>
<li><strong>Targeting narrows the pool.</strong> Tight targeting raises costs per impression but should improve conversion rate. Broad targeting is cheaper per impression but conversion depends on creative.</li>
<li><strong>Budget pacing matters.</strong> Sudden budget increases spook the algorithm. Scale gradually.</li>
</ul>

<h2>The modern shift: creative over targeting</h2>
<p>Post-iOS 14 and signal loss, targeting is less precise. Platforms have shifted to creative-first: the creative itself does the targeting by resonating with the right audience. Broad targeting + great creative often beats narrow targeting + mediocre creative.</p>
""",
        prev=("Overview", "../index.html"),
        nxt=("Unit economics", "unit-economics.html")),

    "foundations/unit-economics": page("Unit economics",
        "Paid ads only work if the unit economics math works. Here are the numbers to know and how to size them.",
        """
<p class="lede">Paid ads aren't magical. They work when cost to acquire a customer is materially less than the customer's lifetime value. Before you spend a dollar, know the math.</p>

<h2>The core metrics</h2>
<ul>
<li><strong>CAC</strong>: cost to acquire one paying customer = spend / customers</li>
<li><strong>LTV</strong>: lifetime value of a customer (gross profit over their lifecycle)</li>
<li><strong>Payback period</strong>: how long until CAC is recovered in gross profit</li>
<li><strong>LTV:CAC</strong>: should be 3:1 or better to be sustainably profitable</li>
</ul>

<h2>The allowable CAC</h2>
<p>Your LTV, divided by your target LTV:CAC ratio, is your allowable CAC. If LTV is $600 and you target 3:1, allowable CAC is $200. Any campaign whose CAC runs above that is losing money.</p>

<h2>Payback period matters too</h2>
<p>LTV:CAC of 4:1 over 5 years looks great on paper but kills cash flow. You need 4 years of capital to fund it. Payback period under 12 months is healthy; under 18 is acceptable; over 24 is a business model problem.</p>

<h2>The blended vs marginal CAC</h2>
<p>Early dollars of ad spend find the easiest customers (cheap CAC). Later dollars find harder ones (expensive CAC). At scale, blended CAC rises. What matters: the next dollar's CAC, not the average.</p>

<h2>Unit economics by segment</h2>
<p>One tenant or product segment can have 10:1 LTV:CAC while another has 1.5:1. Blended looks fine; the mix hides a dying segment. Segment by acquisition channel, geography, product, cohort. Kill the losers.</p>
""",
        prev=("How paid ads work", "how-paid-works.html"),
        nxt=("Channel-market fit", "channel-fit.html")),

    "foundations/channel-fit": page("Channel-market fit",
        "Not every channel works for every business. Here's how to pick channels that actually fit your product and audience.",
        """
<p class="lede">Channel-market fit is whether the channel's audience and intent match your product. A great channel for DTC consumer often fails for enterprise B2B. Knowing this before spending saves months.</p>

<h2>Channel intent levels</h2>
<ul>
<li><strong>Google Search</strong>: high intent, prospect is actively looking</li>
<li><strong>Google Shopping</strong>: commercial intent, product-focused</li>
<li><strong>Meta</strong>: low intent interrupt, creative must create desire</li>
<li><strong>TikTok</strong>: very low intent, but strong discovery for the right product</li>
<li><strong>LinkedIn</strong>: medium B2B intent, audience known by role</li>
<li><strong>YouTube</strong>: varied - in-stream is interrupt, end-screen after search is high-intent</li>
</ul>

<h2>The product fit check</h2>
<ul>
<li>High-consideration, urgent → Google Search</li>
<li>Visual, lifestyle, discovery → Meta, TikTok, Pinterest</li>
<li>B2B with role-based targeting → LinkedIn, Google</li>
<li>Product-led SaaS, self-serve → content + Google Search retargeting</li>
<li>Local services → Google Local Services, Facebook local, Nextdoor</li>
</ul>

<h2>Channel start order</h2>
<p>Don't launch five channels at once. Validate one, scale, then add the next:</p>
<ol>
<li>Most obvious channel for your product</li>
<li>Validate unit economics and creative there</li>
<li>Add a second channel when you understand the first</li>
<li>Third only when the first two are stable</li>
</ol>

<h2>When to kill a channel</h2>
<ul>
<li>90 days of spend with CAC not trending toward allowable</li>
<li>Creative iterations (10+) haven't moved the needle</li>
<li>Your team doesn't know why it works when it does (unrepeatable)</li>
</ul>
""",
        prev=("Unit economics", "unit-economics.html"),
        nxt=("When to run paid", "when-to-run-paid.html")),

    "foundations/when-to-run-paid": page("When to run paid",
        "Paid ads aren't the right first move for every business. Here's the prerequisite checklist.",
        """
<p class="lede">Teams often start with paid ads when they should start with something else. Paid amplifies what works; it doesn't create what isn't there. Know the prerequisites before spending a dollar.</p>

<h2>Prerequisites</h2>
<ul>
<li><strong>You have a converting offer.</strong> Test with warm and cold outreach first. If it doesn't convert warm, paid won't save it.</li>
<li><strong>You have a landing page that converts.</strong> Direct-from-ad landing pages need to convert 2-5% at minimum for most categories.</li>
<li><strong>You have tracking set up.</strong> Pixel, conversions, UTMs, call tracking. Without measurement, paid is gambling.</li>
<li><strong>You have budget for learning.</strong> The first $5-20K is learning spend. If you can't afford to lose it, you can't afford paid.</li>
<li><strong>You have creative capacity.</strong> Creative production isn't optional. Creative fatigue is the #1 killer of paid campaigns.</li>
</ul>

<h2>When paid is premature</h2>
<ul>
<li>Pre-product-market-fit (you're paying to find out what you haven't figured out)</li>
<li>Weak offer (paid amplifies the weakness)</li>
<li>Bad landing page (high bounce rate burns budget)</li>
<li>No measurement infrastructure</li>
<li>Panic move because other channels stopped working</li>
</ul>

<h2>When paid wins</h2>
<ul>
<li>Validated offer, need to scale</li>
<li>Clear ICP with channel-match</li>
<li>Unit economics known and supportive</li>
<li>Team capable of weekly creative iteration</li>
<li>Enough budget to get through 60-90 days of learning</li>
</ul>
""",
        prev=("Channel-market fit", "channel-fit.html"),
        nxt=("Meta Ads overview", "../meta/overview.html")),

    # META ADS (8 pages)
    "meta/overview": page("Meta Ads overview",
        "Meta Ads (Facebook + Instagram) is the dominant DTC and consumer channel. Here's how it's organized and where to start.",
        """
<p class="lede">Meta Ads serves Facebook, Instagram, Messenger, and Audience Network from one system. It's the dominant paid channel for DTC, consumer products, local services, and many B2B plays. Post-iOS 14 it's harder but not dead.</p>

<h2>The hierarchy</h2>
<ul>
<li><strong>Account</strong>: your top-level ad account</li>
<li><strong>Campaign</strong>: defines the objective (traffic, conversions, etc.)</li>
<li><strong>Ad Set</strong>: audience, placement, budget, schedule</li>
<li><strong>Ad</strong>: the creative</li>
</ul>

<h2>Key objectives</h2>
<ul>
<li><strong>Sales</strong>: optimizing for purchases - most DTC uses this</li>
<li><strong>Leads</strong>: for form submits, appointments</li>
<li><strong>Awareness</strong>: reach-based; rarely worth it for direct response</li>
<li><strong>Traffic</strong>: sends clicks, cheaper CPMs but lower conversion</li>
<li><strong>Engagement</strong>: likes/comments - mostly for social proof building</li>
</ul>

<h2>What changed post-iOS 14</h2>
<ul>
<li>Pixel-based attribution lost 20-40% accuracy</li>
<li>Lookalike audiences work but are less precise</li>
<li>Advertisers moved to broad targeting with great creative</li>
<li>Aggregated Event Measurement limits conversion events (8 per domain)</li>
<li>CAPI (Conversions API) is mandatory for serious advertisers</li>
</ul>

<h2>Where to start</h2>
<ol>
<li>Set up conversion tracking (Pixel + CAPI)</li>
<li>One campaign, one ad set, 3-5 creatives</li>
<li>Broad targeting (US, your age range)</li>
<li>$50-100/day for 7-14 days</li>
<li>Optimize for purchase or lead conversion event</li>
<li>Iterate creative weekly</li>
</ol>

<h2>Don't start with</h2>
<ul>
<li>10 campaigns at once</li>
<li>Interest-based narrow targeting</li>
<li>Image-only static creative</li>
<li>Conversion events you haven't implemented yet</li>
</ul>
""",
        prev=("When to run paid", "../foundations/when-to-run-paid.html"),
        nxt=("Account structure", "account-structure.html")),

    "meta/account-structure": page("Meta account structure",
        "How to organize campaigns, ad sets, and ads for scale and clarity. The structure that works.",
        """
<p class="lede">Meta account structure either compounds learning or fragments it. The wrong structure has you running 47 ad sets with 5 conversions each - no signal anywhere. The right structure feeds the algorithm enough data to work.</p>

<h2>The principle: consolidate for data</h2>
<p>Meta's algorithm needs 50+ weekly conversions per ad set to optimize well. Splitting budget across too many ad sets starves all of them. Consolidate.</p>

<h2>Standard structure</h2>
<ul>
<li><strong>Campaign 1: Prospecting</strong> - new customers
<ul><li>Ad set 1: broad targeting - 5-10 creatives</li>
<li>Ad set 2: lookalike audience (1-3%) - 5-10 creatives</li></ul></li>
<li><strong>Campaign 2: Retargeting</strong> - people who visited or engaged
<ul><li>Ad set: website visitors + engaged users</li></ul></li>
<li><strong>Campaign 3: Customer reactivation</strong>
<ul><li>Ad set: past customers past 60 days</li></ul></li>
</ul>

<h2>CBO vs ABO</h2>
<ul>
<li><strong>CBO</strong> (Campaign Budget Optimization): budget at campaign level, algorithm distributes across ad sets</li>
<li><strong>ABO</strong> (Ad Set Budget Optimization): budget per ad set</li>
</ul>
<p>Modern default: CBO for scale, ABO for testing new audiences in isolation.</p>

<h2>Creative slots per ad set</h2>
<ul>
<li>5-10 creatives per ad set is the sweet spot</li>
<li>Fewer than 3: no diversity, creative fatigue hits fast</li>
<li>More than 15: algorithm can't distribute effectively</li>
</ul>

<h2>Naming conventions</h2>
<p>Use a consistent naming convention for reports:</p>
<pre>Campaign: [Stage]-[Objective]-[Date]
Ad set: [Audience]-[Placements]
Ad: [Hook]-[Format]-[Angle]-v[#]
Example: "Prospecting-Purchase-2026Q2" / "Broad-AllPlacements" / "Problem-UGC-PainPoint-v3"</pre>

<h2>The 5/5/5 rule</h2>
<p>Start simple: 5 campaigns max, 5 ad sets per campaign max, 5-10 creatives per ad set. If you have 50 ad sets, you have a complexity problem, not a scale problem.</p>
""",
        prev=("Meta Ads overview", "overview.html"),
        nxt=("Campaign types", "campaign-types.html")),

    "meta/campaign-types": page("Meta campaign types",
        "Each Meta campaign objective optimizes differently. Here's which objective for which use case.",
        """
<p class="lede">Picking the wrong campaign objective is one of the most common Meta mistakes. The objective tells Meta what to optimize for. Wrong objective = optimizing for the wrong outcome.</p>

<h2>The objectives in 2026</h2>
<ul>
<li><strong>Sales</strong>: optimize for purchases. Default for DTC.</li>
<li><strong>Leads</strong>: form submissions or calls.</li>
<li><strong>Engagement</strong>: likes, comments, messages. For content or community growth.</li>
<li><strong>Traffic</strong>: send clicks to your site. Low-intent but cheaper.</li>
<li><strong>App Promotion</strong>: installs for apps.</li>
<li><strong>Awareness</strong>: reach maximization. Rarely for direct response.</li>
</ul>

<h2>Pick by end goal</h2>
<ul>
<li>Product purchase → Sales</li>
<li>Lead form / demo request → Leads</li>
<li>Newsletter signup → Leads (with form) or Traffic (to landing page)</li>
<li>Content consumption → Traffic or Engagement</li>
<li>Brand awareness → Awareness (only if you have budget to burn)</li>
</ul>

<h2>The Sales campaign subtypes</h2>
<ul>
<li><strong>Conversions</strong>: optimize for purchases on your site</li>
<li><strong>Catalog Sales</strong>: for e-commerce with product catalog</li>
<li><strong>Dynamic Creative</strong>: algorithm mixes creative elements</li>
</ul>

<h2>Advantage+ Shopping Campaigns (ASC)</h2>
<p>Meta's automated DTC offering: one campaign, Meta picks audiences and creative combinations. Simpler setup. Works well for established DTC brands with proven creative. New accounts should learn fundamentals first.</p>

<h2>What not to do</h2>
<ul>
<li>Pick "Traffic" because it's cheap, then complain about no conversions</li>
<li>Pick "Engagement" hoping for sales - Meta doesn't optimize for purchases on an engagement campaign</li>
<li>Pick "Awareness" for a performance channel</li>
<li>Mix objectives in one campaign (you can't)</li>
</ul>
""",
        prev=("Account structure", "account-structure.html"),
        nxt=("Audiences and targeting", "audiences.html")),

    "meta/audiences": page("Meta audiences and targeting",
        "Post-iOS 14, Meta targeting is different. Broad targeting with great creative now often beats narrow interest targeting.",
        """
<p class="lede">Pre-2021, Meta targeting was surgical: obscure interests, narrow demographics, custom combinations. Post-iOS 14, signal loss has made broad targeting often win. The platform's AI now does most of the targeting - your creative does the rest.</p>

<h2>Audience types</h2>

<h3>Broad</h3>
<p>Country + age range. Let Meta's AI find the conversions. Post-iOS 14 best practice for most advertisers.</p>

<h3>Interest targeting</h3>
<p>Target people interested in specific pages, topics. Less precise than it once was. Still useful for niche products.</p>

<h3>Lookalike audiences (LAL)</h3>
<p>Meta finds people similar to your seed audience (customers, email list). 1-3% LALs are tightest; 4-10% broader. Still work but less precise than they used to.</p>

<h3>Custom audiences</h3>
<p>Your own data uploaded. Website visitors, customer list, video viewers, engaged IG/FB users.</p>

<h3>Saved audiences</h3>
<p>Combinations of interests + demographics you save for reuse.</p>

<h2>The broad vs narrow debate</h2>
<ul>
<li><strong>Broad + great creative</strong> = Meta AI finds buyers. Usually the winner.</li>
<li><strong>Narrow interest</strong> = you guess who buyers are. Usually worse.</li>
<li><strong>Exception</strong>: genuinely niche products (hobby-specific, B2B roles) where broad would waste impressions.</li>
</ul>

<h2>Exclusions</h2>
<ul>
<li>Exclude current customers from prospecting</li>
<li>Exclude recent purchasers (30-90 days) from retargeting</li>
<li>Exclude email subscribers from newsletter-signup campaigns</li>
</ul>

<h2>Geography</h2>
<p>Default to the country you ship to. Narrow further (state, city, radius) only if your offer is local or you've proven a geographic pattern.</p>

<h2>Demographics</h2>
<p>Age range, gender. Only narrow if you have real data that a demographic doesn't convert. Most advertisers over-narrow here and miss buyers.</p>

<h2>Placements</h2>
<p>Let Meta choose automatic placements 90% of the time. Manual placement selection usually limits the algorithm for no good reason.</p>
""",
        prev=("Campaign types", "campaign-types.html"),
        nxt=("Creative testing", "creative-testing.html")),

    "meta/creative-testing": page("Meta creative testing",
        "Creative is now the dominant lever. Here's how to test at volume without burning budget.",
        """
<p class="lede">Creative is 70%+ of paid ad performance in 2026. One winning creative can 5x results. Finding winners is iterative: test volume, identify patterns, scale winners.</p>

<h2>The testing volume</h2>
<p>Serious advertisers ship 5-20 new creative variants per week. Most die quickly. The 1 in 10 that works carries the account.</p>

<h2>What to vary in tests</h2>

<h3>Hook (first 3 seconds)</h3>
<p>Biggest lever. Test different opening lines, scenes, claims, questions.</p>

<h3>Format</h3>
<p>Video vs static, vertical vs square, UGC vs produced.</p>

<h3>Angle</h3>
<p>Problem/solution, testimonial, before/after, comparison, demo.</p>

<h3>Creator/face</h3>
<p>Different presenters resonate with different audiences.</p>

<h3>Copy</h3>
<p>Primary text, headline, description.</p>

<h2>Testing structure</h2>
<ul>
<li>One ad set, 5-10 creatives, broad targeting</li>
<li>Let run 3-5 days minimum before judging</li>
<li>Kill clear losers (below 50% of average CPA after meaningful spend)</li>
<li>Scale clear winners (above 150% of average CPA performance)</li>
</ul>

<h2>Creative learnings decay</h2>
<p>Every winning creative eventually fatigues. Refresh cadence: new creatives every 1-3 weeks at scale. Established winners stay in rotation but volume shifts.</p>

<h2>Hypothesis-driven tests</h2>
<p>Random variation is wasteful. Each test should answer a question:</p>
<ul>
<li>"Does problem-first hook beat benefit-first?"</li>
<li>"Does testimonial format beat demo format?"</li>
<li>"Does 15-second beat 30-second?"</li>
</ul>
<p>Answer the question, apply the learning to future creative.</p>

<h2>Common creative testing mistakes</h2>
<ul>
<li>Too many variants at once (no ad set gets enough data)</li>
<li>Killing creatives before statistical significance</li>
<li>Testing minor variations (button color, one word) instead of big angles</li>
<li>Not documenting learnings (same bad creative re-made 6 months later)</li>
</ul>
""",
        prev=("Audiences and targeting", "audiences.html"),
        nxt=("iOS 14+ reality", "ios14-reality.html")),

    "meta/ios14-reality": page("Meta iOS 14+ reality",
        "iOS 14.5 (2021) broke Meta attribution. Five years later, here's the state of things and how advertisers adapt.",
        """
<p class="lede">Apple's App Tracking Transparency (iOS 14.5, 2021) was the biggest disruption Meta advertising has ever faced. Pixel data became incomplete, attribution noisier, targeting less precise. In 2026 we have strategies that work despite this.</p>

<h2>What broke</h2>
<ul>
<li>Pixel events from iOS users who opted out of tracking stop flowing to Meta</li>
<li>Lookalike audiences built on partial data are less precise</li>
<li>Retargeting audiences shrank</li>
<li>Reported conversions under-count actual conversions (typically 20-40%)</li>
</ul>

<h2>The adaptations that work</h2>

<h3>Conversions API (CAPI)</h3>
<p>Server-to-server sending of conversion data bypasses pixel limitations. Every serious advertiser runs CAPI. Without it, you're losing 30-40% of your data.</p>

<h3>Broad targeting</h3>
<p>Narrow targeting needs precise data. Broad targeting + great creative works with noisy data.</p>

<h3>First-party data</h3>
<p>Email lists, CRM data. Upload to Meta for targeting. Owned data > platform data.</p>

<h3>Creative as targeting</h3>
<p>Creative self-selects audiences. Someone who watches 95% of your video is interested whether Meta knows their gender or not.</p>

<h3>MER (blended CAC)</h3>
<p>Stop trying to match Meta's reported CAC with reality. Use blended metrics (total ad spend / total customers) for truth. See the measurement section.</p>

<h2>Aggregated Event Measurement (AEM)</h2>
<p>Meta's iOS workaround: 8 conversion events per domain, prioritized. Purchase is usually priority 1. Lower-priority events don't fire at full fidelity.</p>

<h2>What it means for strategy</h2>
<ul>
<li>Attribution is directional, not precise</li>
<li>Creative is the dominant controllable variable</li>
<li>Broad targeting usually wins</li>
<li>First-party data compounds in value</li>
<li>Blended measurement over platform-specific</li>
</ul>
""",
        prev=("Creative testing", "creative-testing.html"),
        nxt=("Scaling campaigns", "scaling.html")),

    "meta/scaling": page("Meta scaling campaigns",
        "Going from $200/day to $2000/day isn't just multiplying budget. Here's how to scale without breaking performance.",
        """
<p class="lede">Scaling Meta campaigns is where most advertisers break. The budget goes up; CAC goes up more. Here's how to scale while keeping unit economics.</p>

<h2>The scale problem</h2>
<p>Early dollars find the cheapest customers. Later dollars find more expensive ones. Blended CAC rises with scale. The question: how to push volume without losing profitability.</p>

<h2>Horizontal vs vertical scaling</h2>

<h3>Vertical: increase budget on winners</h3>
<p>Take a winning campaign, raise budget 20-30% every 2-3 days. Don't double overnight - the algorithm enters re-learning and performance collapses.</p>

<h3>Horizontal: duplicate and diversify</h3>
<p>Copy winning setup to new audiences, new placements, new geos. Each copy has its own data but borrows from proven creative + targeting.</p>

<h2>The budget-jump rule</h2>
<p>Meta punishes big budget jumps by entering "learning phase" - a 7-day re-optimization period where performance drops. Scale by:</p>
<ul>
<li>20-30% increases every 2-3 days</li>
<li>Or: duplicate ad set at 2x budget, let old one burn off</li>
</ul>

<h2>Creative scale</h2>
<p>At higher budgets, creative fatigue hits faster. Plan for:</p>
<ul>
<li>10+ fresh creatives per week at $10K+/day spend</li>
<li>Dedicated creative production (agency, in-house, UGC network)</li>
<li>Weekly refresh cadence</li>
</ul>

<h2>Campaign Budget Optimization (CBO) at scale</h2>
<p>CBO lets Meta distribute budget across ad sets dynamically. At higher budgets, CBO usually outperforms ABO because the algorithm has enough data to work with.</p>

<h2>When scaling breaks</h2>
<ul>
<li>CAC rises to unsustainable level</li>
<li>Frequency climbs (same users see ads repeatedly)</li>
<li>CPM spikes (auction saturation)</li>
<li>Quality of leads/customers degrades (volume customers have lower LTV)</li>
</ul>
<p>Signals to pause vertical scaling and diversify horizontally instead.</p>
""",
        prev=("iOS 14+ reality", "ios14-reality.html"),
        nxt=("Retargeting", "retargeting.html")),

    "meta/retargeting": page("Meta retargeting",
        "Retargeting is the cheapest conversion you'll buy. Here's how to structure it without annoying your audience.",
        """
<p class="lede">Retargeting hits people who've already visited your site, engaged with your content, or started a checkout. Cheaper CAC than prospecting, but easy to overdo.</p>

<h2>Retargeting audiences</h2>
<ul>
<li><strong>All website visitors (30 days)</strong>: broadest retarget</li>
<li><strong>Cart abandoners</strong>: highest intent, highest conversion</li>
<li><strong>Specific product viewers</strong>: intent-matched creative</li>
<li><strong>Engaged IG/FB users</strong>: lower intent but wider reach</li>
<li><strong>Email subscribers not purchased</strong>: owned data retarget</li>
<li><strong>Past customers (60-180 days)</strong>: reactivation</li>
</ul>

<h2>Creative for retargeting</h2>
<p>Different creative than prospecting:</p>
<ul>
<li>Reminder of what they viewed</li>
<li>Social proof (reviews, testimonials)</li>
<li>Offers/discounts (if your margin allows)</li>
<li>Urgency (limited stock, deadline)</li>
<li>Answers to common objections</li>
</ul>

<h2>Frequency caps</h2>
<p>Seeing the same ad 20 times is annoying. Meta auto-caps but consider:</p>
<ul>
<li>Shorter retargeting windows (7-14 days instead of 30-60)</li>
<li>Multiple creative in rotation</li>
<li>Exclude people who've already converted</li>
</ul>

<h2>Budget allocation</h2>
<ul>
<li>Prospecting: 70-85% of budget</li>
<li>Retargeting: 15-30% of budget</li>
</ul>
<p>Retargeting scales with prospecting. More prospecting = bigger retargeting audience. Don't overspend on retargeting when your audience is small.</p>

<h2>The attribution gotcha</h2>
<p>Retargeting gets credit for conversions that would have happened anyway. True incrementality of retargeting is smaller than reported. Don't overfund it.</p>

<h2>Messenger/WhatsApp retargeting</h2>
<p>For certain categories (support-heavy, high-consideration purchases), conversations in Messenger or WhatsApp convert higher than web. Test if applicable.</p>
""",
        prev=("Scaling campaigns", "scaling.html"),
        nxt=("Google Ads overview", "../google/overview.html")),
}


# Build it
build_expertise_section(SECTION_SLUG, SECTION_NAME, SIDEBAR, PAGES)
print("\n✓ Paid Ads foundations + Meta (13 pages)")
