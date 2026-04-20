#!/usr/bin/env python3
"""Paid Ads remaining: Google, TikTok, LinkedIn, YouTube, Creative, Measurement (37 pages)."""
from _paid_ads_content import SIDEBAR
from _build_expertise import build_expertise_section


def p(title, desc, body, rt=3, prev=None, nxt=None):
    return {'title': title, 'description': desc, 'body': body, 'reading_time': rt, 'prev': prev, 'next': nxt}


PAGES = {
    # GOOGLE ADS (8)
    "google/overview": p("Google Ads overview",
        "Google Ads has Search, Shopping, Display, YouTube, and Performance Max. Here's what each is for.",
        """
<p class="lede">Google Ads isn't one product - it's a collection of properties under one billing system: Search, Shopping, Display, Video (YouTube), Discovery, and Performance Max. Each has different intent and different best-fit products.</p>

<h2>The properties</h2>
<ul>
<li><strong>Search</strong>: text ads on search results. Highest intent. The most valuable.</li>
<li><strong>Shopping</strong>: product ads with image + price. For e-commerce.</li>
<li><strong>Display</strong>: banner ads on 2M+ websites. Low intent, cheap CPMs.</li>
<li><strong>Video</strong>: YouTube ads. Covered in YouTube section.</li>
<li><strong>Discovery</strong>: image ads in Gmail, YouTube feed, Discover.</li>
<li><strong>Performance Max</strong>: AI-run campaign using all inventory. Growing dominant.</li>
</ul>

<h2>Where most money should go</h2>
<p>For most B2B and service businesses: Search first. High intent, clear conversion path. For e-commerce: Shopping + Performance Max. For brand-building: Display and YouTube complement Search.</p>

<h2>Account structure basics</h2>
<ul>
<li>Account → Campaign → Ad Group → Ad + Keywords</li>
<li>One campaign per major objective or product line</li>
<li>Ad groups group tightly-related keywords</li>
<li>3-5 ads per ad group for variation</li>
</ul>

<h2>Where to start</h2>
<ol>
<li>Set up conversion tracking (GA4 + Google Ads conversions)</li>
<li>One Search campaign targeting your highest-intent keywords</li>
<li>$50-100/day for 2-3 weeks</li>
<li>Measure. Iterate.</li>
</ol>
""",
        prev=("Retargeting", "../meta/retargeting.html"),
        nxt=("Search vs Display vs Pmax", "search-vs-display.html")),

    "google/search-vs-display": p("Google: Search vs Display vs Performance Max",
        "These three properties have different economics and use cases. Here's when to use each.",
        """
<p class="lede">Google Search, Display, and Performance Max are often confused. Each works for specific situations and fails in others.</p>

<h2>Search</h2>
<p>User types a query; your text ad appears. High intent - they're actively looking.</p>
<ul>
<li>Best for: direct response, lead gen, services, B2B</li>
<li>Cost: higher CPC (competitive keywords hit $50-100+)</li>
<li>Conversion rate: higher than other properties</li>
</ul>

<h2>Display</h2>
<p>Banner ads on websites across the Google Display Network.</p>
<ul>
<li>Best for: retargeting, brand awareness, cheap reach</li>
<li>Cost: very low CPMs ($1-5)</li>
<li>Conversion rate: very low - usually just supports other channels</li>
</ul>

<h2>Performance Max (Pmax)</h2>
<p>AI-driven campaign that runs across all Google inventory. You provide assets and conversion goals; the algorithm decides placements, audiences, creative combinations.</p>
<ul>
<li>Best for: e-commerce with product catalog, mature advertisers with good data</li>
<li>Cost: variable, often competitive</li>
<li>Conversion rate: depends on feed quality and creative</li>
</ul>

<h2>The decision</h2>
<ul>
<li><strong>Services / B2B / high-intent</strong>: Search only, at least initially</li>
<li><strong>E-commerce with catalog</strong>: Pmax + Search brand-defense</li>
<li><strong>Brand</strong>: Display + YouTube for reach</li>
<li><strong>Retargeting</strong>: Display works but Meta is often better</li>
</ul>

<h2>The Pmax warning</h2>
<p>Performance Max is a black box. You lose granular control. Works when your product is clear and feed is good. Fails when your data is noisy or your product has complex positioning.</p>
""",
        prev=("Google Ads overview", "overview.html"),
        nxt=("Keyword research", "keyword-research.html")),

    "google/keyword-research": p("Keyword research",
        "Finding the keywords that actually produce revenue, not just traffic.",
        """
<p class="lede">Keyword research for paid is different from SEO keyword research. You're not optimizing for volume - you're finding intent-matched queries where you can profitably buy clicks.</p>

<h2>The intent hierarchy</h2>
<ul>
<li><strong>Transactional</strong>: "buy X", "X near me", "hire X consultant" - highest value</li>
<li><strong>Commercial</strong>: "best X for Y", "X vs Y" - evaluation stage</li>
<li><strong>Informational</strong>: "what is X", "how does X work" - mostly SEO, expensive paid</li>
<li><strong>Brand</strong>: your brand name or competitors' - cheap, highest conversion</li>
</ul>

<p>Focus paid budget on transactional and commercial. Informational is for content/SEO.</p>

<h2>Tools</h2>
<ul>
<li>Google Keyword Planner (free, built into Google Ads)</li>
<li>Ahrefs, Semrush - for competitive research</li>
<li>Search term report from your own campaigns - best source</li>
</ul>

<h2>The competitor angle</h2>
<p>What keywords are your competitors bidding on? Their paid keywords reveal what's working in your space. Ahrefs and Semrush have paid-keyword intelligence.</p>

<h2>Negative keywords</h2>
<p>Just as important as positive keywords. Start with:</p>
<ul>
<li>"free" (tire-kickers)</li>
<li>"jobs", "career", "salary" (not buyers)</li>
<li>Irrelevant uses of your terms (e.g., if you sell "apple products", exclude "apple fruit")</li>
</ul>

<h2>Volume isn't everything</h2>
<p>A high-volume generic keyword with 1% conversion costs more than a low-volume intent keyword with 10% conversion. Buy intent, not volume.</p>

<h2>Geographic modifiers</h2>
<p>For local services, "[service] + [city]" or "[service] near me" are usually the highest ROI keywords. Bid on them specifically.</p>
""",
        prev=("Search vs Display vs Pmax", "search-vs-display.html"),
        nxt=("Match types", "match-types.html")),

    "google/match-types": p("Google Ads match types",
        "Exact, phrase, broad. Match type determines which searches trigger your ad. Picking wrong wastes budget.",
        """
<p class="lede">Match types tell Google how closely a search must match your keyword for your ad to show. Broad is the widest; exact is the narrowest. Picking wrong either starves you of volume or wastes spend on irrelevant clicks.</p>

<h2>The match types</h2>

<h3>Exact match</h3>
<p>Search must match your keyword or a close variant. Most control, least volume.</p>
<p>Keyword: [red running shoes] → matches "red running shoes", "running shoes red" - similar intent.</p>

<h3>Phrase match</h3>
<p>Search must include your phrase (or close variant) as a subset. Medium control.</p>
<p>Keyword: "red running shoes" → matches "buy red running shoes", "red running shoes for marathon" - phrase in there.</p>

<h3>Broad match</h3>
<p>Search includes anything Google thinks is related. Widest reach, least control. Modern broad match uses AI to find related intent.</p>
<p>Keyword: red running shoes → matches "running gear", "jogging footwear", "athletic shoes red" - loosely related.</p>

<h2>When to use each</h2>
<ul>
<li><strong>Exact</strong>: tightly-proven high-intent keywords. Scales slowly but predictably.</li>
<li><strong>Phrase</strong>: extended reach with some control. Often the sweet spot.</li>
<li><strong>Broad</strong>: exploration; finding new queries. Always pair with smart bidding (Target CPA or ROAS) - without it, broad is chaos.</li>
</ul>

<h2>The modern recommendation</h2>
<p>Google has nudged advertisers toward broad match + smart bidding. Works when:</p>
<ul>
<li>Your conversion tracking is solid</li>
<li>You have enough conversion volume for the algorithm to optimize</li>
<li>You have negative keywords in place</li>
</ul>
<p>Without those, broad match burns budget.</p>

<h2>Negative keywords with broad</h2>
<p>Broad match discovers irrelevant queries constantly. Weekly: review the search terms report, add negatives for queries that don't fit.</p>

<h2>The hybrid approach</h2>
<p>Run exact match for your proven high-ROI keywords (tight control) + broad match with smart bidding for discovery (find new queries). Exact match gets priority when both could trigger.</p>
""",
        prev=("Keyword research", "keyword-research.html"),
        nxt=("Quality Score", "quality-score.html")),

    "google/quality-score": p("Google Ads Quality Score",
        "Quality Score affects your CPC. Understanding it can cut your costs 30-50%.",
        """
<p class="lede">Quality Score (1-10) is Google's assessment of your ad's relevance to the query and landing page. Higher Quality Score = lower CPC for the same position. It compounds: 30% cheaper CPC on a $10K/month budget = $3K/month in savings.</p>

<h2>The three components</h2>
<ul>
<li><strong>Expected CTR</strong>: will people click this ad?</li>
<li><strong>Ad Relevance</strong>: does the ad match the keyword?</li>
<li><strong>Landing Page Experience</strong>: does the page match what was promised?</li>
</ul>
<p>Each scored average, above average, below average. Combined into Quality Score.</p>

<h2>How to improve Expected CTR</h2>
<ul>
<li>Keyword in headline</li>
<li>Specific, concrete benefit</li>
<li>Numbers, prices, specific details</li>
<li>Strong CTA</li>
<li>Ad extensions (sitelinks, callouts, structured snippets)</li>
</ul>

<h2>How to improve Ad Relevance</h2>
<ul>
<li>Tight ad groups (10-20 tightly-related keywords per ad group)</li>
<li>Keyword in headline and/or description</li>
<li>One ad group per specific intent, not "everything" ad groups</li>
</ul>

<h2>How to improve Landing Page</h2>
<ul>
<li>Landing page matches the ad promise</li>
<li>Fast load time (under 3 seconds)</li>
<li>Mobile-friendly</li>
<li>Clear CTA matching the ad's action</li>
<li>Relevant content (not your homepage)</li>
</ul>

<h2>The compounding effect</h2>
<p>Quality Score 7 → Quality Score 9 can cut CPC 40%+. Combined with better CTR from relevance, your effective cost per conversion can halve.</p>

<h2>Common Quality Score killers</h2>
<ul>
<li>Sending all traffic to homepage</li>
<li>Running 50 keywords in one ad group with generic ad copy</li>
<li>Landing page has nothing to do with the search query</li>
<li>Slow mobile load time</li>
<li>No ad extensions</li>
</ul>
""",
        prev=("Match types", "match-types.html"),
        nxt=("Responsive Search Ad copy", "rsa-copy.html")),

    "google/rsa-copy": p("Responsive Search Ad copy",
        "RSAs are the current ad format. You give Google headlines and descriptions; it mixes and matches. Here's how to write them.",
        """
<p class="lede">Responsive Search Ads (RSAs) replaced Expanded Text Ads. You provide up to 15 headlines and 4 descriptions; Google combines them dynamically. Writing for RSAs requires a different approach than old-style ads.</p>

<h2>The constraints</h2>
<ul>
<li>Up to 15 headlines, 30 characters each</li>
<li>Up to 4 descriptions, 90 characters each</li>
<li>Google picks combinations based on what will perform best per query</li>
<li>Pin headlines to specific positions if needed (but generally don't)</li>
</ul>

<h2>Writing principles</h2>

<h3>Diversity</h3>
<p>Don't write 15 variations of the same thing. Cover different angles:</p>
<ul>
<li>Keyword-match (keyword in headline)</li>
<li>Benefit-led</li>
<li>Feature-led</li>
<li>CTA-led</li>
<li>Social proof</li>
<li>Urgency/scarcity (if real)</li>
<li>Specific detail (number, timeframe)</li>
</ul>

<h3>Each headline can stand alone</h3>
<p>Google may show your headline without the others. Each must make sense on its own, not depend on being paired.</p>

<h3>Character efficiency</h3>
<p>30 characters is tight. Cut every unnecessary word. "Get the Best Deals on Running Shoes" (34) fails; "Running Shoe Deals - 40% Off" (28) works.</p>

<h2>Descriptions</h2>
<p>90 characters each. Use them to:</p>
<ul>
<li>Expand on the offer</li>
<li>Add proof</li>
<li>Include unique selling points</li>
<li>Call to action</li>
</ul>

<h2>Pinning</h2>
<p>Pin a headline to position 1 if it's critical (brand name, required disclaimer). Otherwise, let Google optimize. Heavy pinning removes the algorithm's ability to optimize.</p>

<h2>Ad Strength indicator</h2>
<p>Google rates your ad "Poor", "Average", "Good", or "Excellent". Target Good or Excellent. Higher Ad Strength correlates with better performance.</p>

<h2>Common mistakes</h2>
<ul>
<li>Only 3-5 headlines (use more)</li>
<li>All headlines say basically the same thing</li>
<li>Headlines that only work with a specific description</li>
<li>Missing CTA headlines</li>
<li>No keyword match in any headline</li>
</ul>
""",
        prev=("Quality Score", "quality-score.html"),
        nxt=("Bidding strategies", "bidding.html")),

    "google/bidding": p("Google Ads bidding strategies",
        "Manual, Maximize Conversions, Target CPA, Target ROAS. Here's which bidding strategy for which situation.",
        """
<p class="lede">Google offers a dozen bidding strategies. They fall into two camps: manual (you control bids) and smart/automated (algorithm controls bids based on goals). Modern best practice is automated - but only when you have the right data.</p>

<h2>Automated strategies</h2>

<h3>Maximize Conversions</h3>
<p>Algorithm spends budget to get the most conversions. Good starting point when you're proving the channel.</p>

<h3>Target CPA</h3>
<p>Bid to hit a target cost per acquisition. Best when you know your target CAC and have 30+ conversions/month of data.</p>

<h3>Target ROAS</h3>
<p>Bid to hit a target return on ad spend. Best for e-commerce with revenue tracking.</p>

<h3>Maximize Conversion Value</h3>
<p>Algorithm maximizes total value, not number of conversions. Good when conversions have different values (high vs low ticket).</p>

<h3>Maximize Clicks</h3>
<p>For traffic-focused campaigns. Not usually what you want for direct response.</p>

<h2>Manual strategies</h2>

<h3>Manual CPC</h3>
<p>You set max CPC per keyword. Full control. Lower ceiling. Use when you don't have enough data for smart bidding.</p>

<h3>Enhanced CPC (eCPC)</h3>
<p>Manual with algorithmic adjustment. Half-and-half. Transitional.</p>

<h2>When to use each</h2>
<ul>
<li><strong>Brand new account</strong>: Manual CPC or Maximize Clicks initially, just to get spend</li>
<li><strong>Getting conversion data</strong>: Maximize Conversions</li>
<li><strong>30+ conversions/month</strong>: switch to Target CPA</li>
<li><strong>E-commerce with revenue tracking</strong>: Target ROAS</li>
<li><strong>Large brands with multiple objectives</strong>: portfolios of bidding strategies</li>
</ul>

<h2>The smart bidding reality</h2>
<p>Smart bidding needs data. Below 30 conversions in the last 30 days per campaign, the algorithm can't optimize. Starting below that threshold forces manual or Maximize Conversions until you have data.</p>

<h2>Bid adjustments</h2>
<p>Adjust bids by device, location, time of day, audience. Useful for narrowing or scaling. Less needed with smart bidding (it does this automatically).</p>
""",
        prev=("Responsive Search Ad copy", "rsa-copy.html"),
        nxt=("Performance Max", "pmax.html")),

    "google/pmax": p("Google Performance Max",
        "Pmax is Google's all-AI campaign type. Powerful when it works, opaque when it doesn't. Here's when to use it.",
        """
<p class="lede">Performance Max is Google's automated campaign type that uses all Google inventory (Search, Shopping, Display, YouTube, Discover) from one campaign. The algorithm decides where to show, who to show to, and what creative combinations to use. Powerful but opaque.</p>

<h2>How it works</h2>
<p>You provide: conversion goal, budget, asset groups (headlines, images, videos, descriptions), audience signals (optional). Pmax does the rest.</p>

<h2>When Pmax wins</h2>
<ul>
<li>E-commerce with a product feed (Shopping + others)</li>
<li>Mature advertisers with rich first-party data</li>
<li>Broad consumer audiences</li>
<li>Accounts with good conversion tracking</li>
</ul>

<h2>When Pmax doesn't work</h2>
<ul>
<li>Low conversion volume (algo can't optimize)</li>
<li>Niche B2B or complex positioning</li>
<li>Brand-sensitive advertisers (you have less control over placements)</li>
<li>When you need granular attribution</li>
</ul>

<h2>The controls you have</h2>
<ul>
<li>Conversion goal</li>
<li>Budget</li>
<li>Asset groups (creative)</li>
<li>Audience signals (hints, not hard targeting)</li>
<li>Account-level exclusions</li>
</ul>

<h2>What you don't control</h2>
<ul>
<li>Which placements your ads show on</li>
<li>Which keywords trigger ads</li>
<li>How budget splits across inventory types</li>
<li>Creative combinations</li>
</ul>

<h2>The Pmax + Search combination</h2>
<p>Running Pmax + a separate Search campaign is common. Search handles explicit brand/high-intent queries; Pmax handles discovery and Shopping. The two coordinate via Google's system.</p>

<h2>Common Pmax mistakes</h2>
<ul>
<li>Low asset variety (Google needs lots of creative combinations)</li>
<li>No negative keywords at account level</li>
<li>Starting before conversion tracking is solid</li>
<li>Treating it like set-and-forget (it still needs iteration)</li>
</ul>
""",
        prev=("Bidding strategies", "bidding.html"),
        nxt=("TikTok Ads overview", "../tiktok/overview.html")),

    # TIKTOK (5)
    "tiktok/overview": p("TikTok Ads overview",
        "TikTok is creative-first. Running it like Meta fails. Here's what's different.",
        """
<p class="lede">TikTok Ads works fundamentally differently from Meta or Google. It's creative-first: the creative determines everything. Targeting barely matters compared to whether your ad looks native to the feed. Running TikTok like Meta is the #1 way advertisers lose money there.</p>

<h2>Why TikTok is different</h2>
<ul>
<li>Users scroll for entertainment, not intent</li>
<li>Native creative (looks like a regular TikTok) outperforms polished ads 10-50x</li>
<li>The algorithm is so good at targeting that broad + native beats narrow + polished</li>
<li>Creative fatigue happens in days, not weeks</li>
</ul>

<h2>Ad formats</h2>
<ul>
<li><strong>In-Feed Ads</strong>: regular ads in the For You feed</li>
<li><strong>Spark Ads</strong>: boost an organic TikTok post as an ad (highest performing)</li>
<li><strong>TopView</strong>: full-screen video at app open. Premium, brand-focused.</li>
<li><strong>Branded Hashtag Challenge</strong>: UGC campaign around a hashtag</li>
</ul>

<h2>The creative requirement</h2>
<ul>
<li>Vertical video (9:16)</li>
<li>First 1-2 seconds must hook (users swipe fast)</li>
<li>Sound on (TikTok is a sound-on platform)</li>
<li>Text on screen (captions help retention)</li>
<li>Fast cuts, energy, authenticity</li>
<li>Looks like a TikTok, not an ad</li>
</ul>

<h2>Where to start</h2>
<ol>
<li>Install TikTok Pixel / Events API</li>
<li>Have 5-10 pieces of TikTok-native creative (record or partner with creators)</li>
<li>One campaign, broad targeting, $50-100/day</li>
<li>Optimize for Conversions</li>
<li>Let run 7 days, iterate creative weekly</li>
</ol>

<h2>When TikTok works</h2>
<ul>
<li>Consumer products with visual demo potential</li>
<li>Brands with creator partnerships</li>
<li>Products aimed at 18-34 audiences (though older demos growing)</li>
<li>Categories where TikTok trend relevance exists</li>
</ul>

<h2>When it doesn't</h2>
<ul>
<li>B2B enterprise (wrong audience)</li>
<li>Products requiring long explanation</li>
<li>Advertisers without creative capacity</li>
<li>High-consideration purchases ($1K+ consumer)</li>
</ul>
""",
        prev=("Performance Max", "../google/pmax.html"),
        nxt=("Creative-first approach", "creative-first.html")),

    "tiktok/creative-first": p("TikTok creative-first approach",
        "On TikTok, creative is 80% of performance. Here's what native creative looks like.",
        """
<p class="lede">On most platforms, creative is 40-50% of performance. On TikTok, it's 70-80%. A brand can have perfect targeting and budget and still fail if the creative doesn't look native to the feed.</p>

<h2>Native vs produced</h2>
<p>Native = looks like something a regular user would post. Shaky, casual, conversational, trend-aware.</p>
<p>Produced = professional lighting, polished editing, brand-forward. This is what worked on Facebook 2015. It fails on TikTok 2026.</p>

<h2>What native looks like</h2>
<ul>
<li>Vertical, phone-shot</li>
<li>Talking head or walking-and-talking</li>
<li>Native music, trending sounds</li>
<li>Text overlays that react to what's being said</li>
<li>Jump cuts, not smooth transitions</li>
<li>A person, not a brand voice</li>
</ul>

<h2>The hook problem</h2>
<p>First 1-2 seconds. Users swipe instantly if bored. Hooks that work:</p>
<ul>
<li>Strong claim ("You've been doing X wrong")</li>
<li>Question ("Did you know about this?")</li>
<li>Character-led ("My friend tried this and...")</li>
<li>Visual pattern interrupt</li>
<li>Direct address ("If you have...")</li>
</ul>

<h2>Production volume</h2>
<p>TikTok burns creative. Weekly new creative is the minimum. Serious advertisers ship 10-50 new ads per week.</p>

<h2>Sources of creative</h2>
<ul>
<li>Your own team (fastest iteration)</li>
<li>UGC platforms (Billo, Insense, TrendHERO)</li>
<li>Partner creators (paid per video)</li>
<li>Repurpose organic TikToks via Spark Ads</li>
</ul>

<h2>Do not</h2>
<ul>
<li>Repurpose Meta creative (it looks like an ad)</li>
<li>Use stock footage</li>
<li>Over-brand (logo large, brand-forward tone)</li>
<li>Make it longer than 30s without strong reason</li>
<li>Run horizontal video</li>
</ul>
""",
        prev=("TikTok Ads overview", "overview.html"),
        nxt=("Spark Ads", "spark-ads.html")),

    "tiktok/spark-ads": p("TikTok Spark Ads",
        "Spark Ads promote existing organic TikToks. They outperform regular ads on many metrics.",
        """
<p class="lede">Spark Ads let you promote an existing organic TikTok (yours or a creator's) as paid inventory. They look completely native because they are native. Outperform In-Feed ads on retention, engagement, and conversion on most campaigns.</p>

<h2>How it works</h2>
<ol>
<li>Find or create an organic TikTok (yours or a creator partner's)</li>
<li>Creator gives you permission via Spark Ad code</li>
<li>You boost it as an ad</li>
<li>Engagement (likes, comments, shares) accumulates on the original post</li>
</ol>

<h2>Why they outperform</h2>
<ul>
<li>Look exactly like native content</li>
<li>Benefit from existing organic engagement</li>
<li>Comments are real (social proof)</li>
<li>Users trust creator-led content over branded ads</li>
</ul>

<h2>The creator partnership</h2>
<p>Creator posts organically, you boost. Pay creator fixed fee + Spark Ad allowance. Win-win:</p>
<ul>
<li>Creator gets reach and fee</li>
<li>You get native creative with creator credibility</li>
</ul>

<h2>The creator marketplaces</h2>
<ul>
<li>TikTok Creator Marketplace (official)</li>
<li>Insense</li>
<li>Billo</li>
<li>Direct DM to creators</li>
</ul>

<h2>The contract essentials</h2>
<ul>
<li>Video usage rights for paid advertising</li>
<li>Spark Ad authorization period</li>
<li>Content guidelines (what they can/can't say)</li>
<li>FTC disclosure (they must mark #ad or #sponsored)</li>
</ul>

<h2>Testing with Spark</h2>
<p>Boost multiple organic posts at once, see which scale. Cheaper than producing new creative. The winners become your core ads.</p>

<h2>When Spark loses</h2>
<ul>
<li>When original post is too niche to scale</li>
<li>Ad requires specific claims creator can't make</li>
<li>When branded messaging is non-negotiable</li>
</ul>
""",
        prev=("Creative-first approach", "creative-first.html"),
        nxt=("UGC production", "ugc-production.html")),

    "tiktok/ugc-production": p("TikTok UGC production",
        "Sourcing, directing, and managing UGC creators for TikTok ads at scale.",
        """
<p class="lede">Most TikTok ad success comes from UGC - creator-shot content that looks native. Building a UGC production pipeline is how serious advertisers compound creative output.</p>

<h2>The UGC sources</h2>

<h3>Platform marketplaces</h3>
<ul>
<li><strong>Insense</strong>: pay per video, vetted creators, US/global</li>
<li><strong>Billo</strong>: similar, smaller roster</li>
<li><strong>TrendHERO</strong>: Spark-Ad focus</li>
<li><strong>Fiverr</strong>: cheap but variable quality</li>
</ul>

<h3>Direct creator outreach</h3>
<p>Find creators with 10K-500K followers in your niche. DM them. Often better rates than marketplaces for repeat partnerships.</p>

<h3>In-house team</h3>
<p>Hire creators on staff. Maximum control and volume but fixed cost.</p>

<h2>The brief</h2>
<p>What a UGC creator needs to deliver on:</p>
<ul>
<li>Core message and angle</li>
<li>Key claims to include</li>
<li>Claims to NOT make (compliance)</li>
<li>Call-to-action at end</li>
<li>Format specs (9:16, 15-30 seconds)</li>
<li>Brand mentions (name, not logo overlay)</li>
<li>Deadline</li>
</ul>

<h2>Iteration with creators</h2>
<p>First video is rarely perfect. Pattern: one revision round, specific feedback. Don't micromanage - the whole point is their native style.</p>

<h2>Variations from one creator</h2>
<p>Ask for 3-5 variations of the same core message:</p>
<ul>
<li>Different hooks</li>
<li>Different CTAs</li>
<li>Different lengths</li>
<li>Different angles</li>
</ul>

<h2>Cost expectations</h2>
<ul>
<li>Marketplace UGC: $50-300 per video</li>
<li>Mid-tier creator: $200-1000 per video</li>
<li>Established creator: $500-5000 per video</li>
<li>Celebrity or top creator: $10K+</li>
</ul>

<h2>Volume targets</h2>
<p>To run TikTok seriously, you need 5-20 new creatives per week. Build the pipeline - it's not optional.</p>
""",
        prev=("Spark Ads", "spark-ads.html"),
        nxt=("When TikTok works", "when-tiktok-works.html")),

    "tiktok/when-tiktok-works": p("When TikTok Ads work",
        "TikTok isn't for everyone. Here's who wins and who shouldn't bother.",
        """
<p class="lede">TikTok Ads work spectacularly for some businesses and fail reliably for others. Knowing which camp you're in saves months of wasted spend.</p>

<h2>Where TikTok wins</h2>

<h3>Visual consumer products</h3>
<p>Products that demo well in video. Apparel, beauty, home goods, gadgets, supplements, food.</p>

<h3>Younger-skewing audiences</h3>
<p>18-34 is the strongest, though older demos (35-55) are growing.</p>

<h3>Brands comfortable with creative velocity</h3>
<p>If you can produce or source 10+ new creatives per week, TikTok compounds. If not, skip.</p>

<h3>Products with native content appeal</h3>
<p>Products that creators would post about organically. If your product fits trend content, TikTok amplifies.</p>

<h3>DTC brands with under $200 AOV</h3>
<p>Impulse purchases work. High-consideration ($500+) products convert worse.</p>

<h2>Where TikTok doesn't work</h2>

<h3>Enterprise B2B</h3>
<p>Wrong audience. Even if decision-makers are on TikTok personally, they don't buy enterprise software there.</p>

<h3>Complex, expensive products</h3>
<p>Luxury goods, financial products, high-ticket services. Intent and context don't fit.</p>

<h3>Brands without creative capacity</h3>
<p>You can't run TikTok with 3 polished videos. Without pipeline, don't start.</p>

<h3>Brands requiring brand control</h3>
<p>UGC and creators dilute brand voice. If your brand is precise-tone, TikTok fights you.</p>

<h3>Regulated industries</h3>
<p>Some compliance restrictions make native-looking ads hard (pharma, finance, alcohol in certain markets).</p>

<h2>The signal test</h2>
<p>Look at organic TikTok search for your product category. Are there native videos about it? Are creators already making content in your space?</p>
<ul>
<li>Yes, lots → TikTok Ads will probably work</li>
<li>No, empty space → TikTok Ads probably won't work</li>
</ul>

<h2>Start small</h2>
<p>$5-10K total test budget over 3-4 weeks. Iterate creative. Measure positive signal. Scale only if proven.</p>
""",
        prev=("UGC production", "ugc-production.html"),
        nxt=("LinkedIn Ads overview", "../linkedin/overview.html")),

    # LINKEDIN (5)
    "linkedin/overview": p("LinkedIn Ads overview",
        "LinkedIn is the B2B workhorse. Expensive clicks, high-intent audience. Here's the basics.",
        """
<p class="lede">LinkedIn Ads is the default paid channel for B2B targeting professionals by role, company, and industry. CPCs are high ($5-20+) but intent is strong. Used right, it's one of the few channels where you can reach specific executives at named companies.</p>

<h2>Key advantages</h2>
<ul>
<li>Target by job title, role, company size, industry, seniority</li>
<li>Account-based targeting (upload named accounts)</li>
<li>Professional context (people aren't doom-scrolling for entertainment)</li>
<li>Integrates with Sales Navigator data</li>
</ul>

<h2>Ad formats</h2>
<ul>
<li><strong>Sponsored Content</strong>: feed ads (image, video, carousel)</li>
<li><strong>Sponsored InMail / Message Ads</strong>: direct message to inbox</li>
<li><strong>Text Ads</strong>: rail ads, cheap but low performance</li>
<li><strong>Lead Gen Forms</strong>: form-fill directly in LinkedIn</li>
<li><strong>Dynamic Ads</strong>: personalized with profile data</li>
</ul>

<h2>Objectives</h2>
<ul>
<li>Brand Awareness</li>
<li>Website Visits</li>
<li>Engagement</li>
<li>Video Views</li>
<li>Lead Generation (LinkedIn form)</li>
<li>Website Conversions</li>
<li>Job Applicants</li>
</ul>

<h2>The cost reality</h2>
<ul>
<li>CPC $5-20 for most B2B roles</li>
<li>CPM $50-100+ for executive targeting</li>
<li>Cost per lead $50-200 for quality leads</li>
<li>Minimum daily spend for useful data: $100+</li>
</ul>

<h2>When LinkedIn works</h2>
<ul>
<li>B2B with deal size $10K+ (unit economics support high CPC)</li>
<li>Role-specific targeting (VP Sales, Head of Marketing, etc.)</li>
<li>Account-Based Marketing (named account lists)</li>
<li>Professional services (consultants, lawyers, accountants)</li>
</ul>

<h2>When it doesn't</h2>
<ul>
<li>B2C (wrong audience)</li>
<li>Low-ticket B2B (CPC can't pay back)</li>
<li>Urgent/same-day purchases (LinkedIn audience is in research mode)</li>
</ul>

<h2>Where to start</h2>
<ol>
<li>Install LinkedIn Insight Tag</li>
<li>Define tight ICP (role + company size + industry)</li>
<li>Start with Sponsored Content or Lead Gen Form campaign</li>
<li>$100-200/day minimum</li>
<li>2-4 weeks before judging</li>
</ol>
""",
        prev=("When TikTok works", "../tiktok/when-tiktok-works.html"),
        nxt=("B2B targeting", "b2b-targeting.html")),

    "linkedin/b2b-targeting": p("LinkedIn B2B targeting",
        "LinkedIn's targeting is more precise than any other platform. Here's how to use it.",
        """
<p class="lede">LinkedIn's targeting is its moat. Job title, company size, industry, seniority, skills, past employers, schools - all self-reported by professionals. No other platform has targeting this precise for B2B.</p>

<h2>Targeting attributes</h2>
<ul>
<li><strong>Job Title</strong>: exact titles (fewer matches) or title categories (wider)</li>
<li><strong>Job Function</strong>: broader - "Sales", "Marketing", "Engineering"</li>
<li><strong>Seniority</strong>: Entry, Senior, Manager, Director, VP, C-suite, Owner</li>
<li><strong>Company Size</strong>: by employee count</li>
<li><strong>Industry</strong>: from LinkedIn's taxonomy</li>
<li><strong>Years of Experience</strong></li>
<li><strong>Company Name</strong>: named account lists (ABM)</li>
<li><strong>Skills</strong>: what people list on their profile</li>
<li><strong>Groups</strong>: LinkedIn groups members</li>
</ul>

<h2>Targeting recipes</h2>

<h3>Typical SaaS ICP</h3>
<ul>
<li>Job Function: Marketing OR Sales</li>
<li>Seniority: Director+</li>
<li>Company Size: 201-1000</li>
<li>Industry: Software + Internet + SaaS</li>
</ul>

<h3>Account-Based (ABM)</h3>
<ul>
<li>Upload named account list</li>
<li>Layer on role/seniority filters</li>
</ul>

<h3>Broad awareness</h3>
<ul>
<li>Job Function only</li>
<li>Larger geography</li>
</ul>

<h2>Audience size targets</h2>
<ul>
<li>Under 20K: too narrow, high CPM, won't scale</li>
<li>20K-300K: sweet spot for most B2B</li>
<li>300K+: broader, lower CPM but less targeted</li>
</ul>

<h2>Audience Expansion</h2>
<p>LinkedIn's lookalike-like feature. Tells the algorithm to find similar people. Works, but sometimes drifts outside your ICP. Test both on and off.</p>

<h2>Matched Audiences</h2>
<ul>
<li>Upload contact list (emails)</li>
<li>Upload company list</li>
<li>Website retargeting (via Insight Tag)</li>
</ul>

<h2>Exclusions</h2>
<ul>
<li>Exclude current customers</li>
<li>Exclude unqualified roles (interns, not buyers)</li>
<li>Exclude own employees</li>
</ul>

<h2>Common LinkedIn targeting mistakes</h2>
<ul>
<li>Targeting "decision makers" without role specifics (too vague)</li>
<li>Only targeting job title (misses people with variant titles)</li>
<li>Over-stacking filters (audience too small to deliver)</li>
<li>Ignoring Company Size (tiny companies have different buyers)</li>
</ul>
""",
        prev=("LinkedIn Ads overview", "overview.html"),
        nxt=("Ad formats", "ad-formats.html")),

    "linkedin/ad-formats": p("LinkedIn ad formats",
        "Sponsored Content, InMail, Carousels, Dynamic Ads. Each works for specific use cases.",
        """
<p class="lede">LinkedIn offers a handful of ad formats. Picking the right one for your goal is half the battle. Here's when to use each.</p>

<h2>Sponsored Content</h2>
<p>Single image, carousel, or video in the feed. The workhorse format.</p>
<ul>
<li><strong>Best for</strong>: thought leadership, lead gen, awareness</li>
<li><strong>Creative</strong>: professional image or video, headline, description</li>
<li><strong>CTR benchmark</strong>: 0.3-0.8%</li>
</ul>

<h2>Sponsored InMail / Message Ads</h2>
<p>Direct message to someone's LinkedIn inbox. Must come from a real LinkedIn profile (usually a sender you authorize).</p>
<ul>
<li><strong>Best for</strong>: high-consideration offers, event invites, personal outreach feel</li>
<li><strong>Conversion rate</strong>: higher than feed ads when done well</li>
<li><strong>Pricing</strong>: cost per send, not per click</li>
</ul>

<h2>Lead Gen Forms</h2>
<p>Form-fill inside LinkedIn - pre-populated with the user's profile data. Very low friction.</p>
<ul>
<li><strong>Best for</strong>: webinar signups, whitepaper downloads, demo requests</li>
<li><strong>Conversion advantage</strong>: 2-5x website form conversion</li>
<li><strong>Tradeoff</strong>: leads stay in LinkedIn until you sync to CRM</li>
</ul>

<h2>Carousel Ads</h2>
<p>2-10 slides in one ad. User swipes through.</p>
<ul>
<li><strong>Best for</strong>: case studies, multi-feature walkthroughs, step-by-step</li>
</ul>

<h2>Video Ads</h2>
<p>Native video in feed. Autoplay with sound off.</p>
<ul>
<li><strong>Best for</strong>: storytelling, product demos, testimonials</li>
<li><strong>First 3 seconds</strong>: hook matters since autoplay is silent</li>
</ul>

<h2>Dynamic Ads</h2>
<p>Personalized using the viewer's profile info. "Hi [Name], see how [Role]s like you..."</p>
<ul>
<li><strong>Best for</strong>: role-based positioning, job recruiting</li>
<li><strong>Caveat</strong>: can feel creepy if over-done</li>
</ul>

<h2>Text Ads</h2>
<p>Tiny rail ads. Cheap but low-impact.</p>
<ul>
<li><strong>Best for</strong>: mostly retargeting or awareness supplements</li>
<li><strong>Not recommended</strong> as primary format</li>
</ul>

<h2>The recommendation</h2>
<ol>
<li>Start with Sponsored Content (single image or video)</li>
<li>Add Lead Gen Forms for direct-response objectives</li>
<li>Test Message Ads for high-ticket offers</li>
<li>Carousel for nuanced messages</li>
</ol>
""",
        prev=("B2B targeting", "b2b-targeting.html"),
        nxt=("Cost reality", "cost-reality.html")),

    "linkedin/cost-reality": p("LinkedIn Ads cost reality",
        "LinkedIn CPCs are $5-30. Here's how to make the math work and when it doesn't.",
        """
<p class="lede">LinkedIn is expensive. CPCs routinely run 5-10x what you'd pay on Meta or Google for the same person. The question isn't whether it's expensive - it's whether the audience quality justifies the premium.</p>

<h2>The CPC ranges</h2>
<ul>
<li>Broad targeting (large audience): $3-8 CPC</li>
<li>Targeted mid-level professional: $8-15 CPC</li>
<li>Director+ at specific company sizes: $15-25 CPC</li>
<li>C-suite at named accounts: $25-50+ CPC</li>
</ul>

<h2>CPM benchmarks</h2>
<ul>
<li>$30-50 CPM for broad B2B</li>
<li>$75-150 CPM for executive targeting</li>
<li>$150+ CPM for C-suite or niche roles</li>
</ul>

<h2>When the math works</h2>
<p>High-ticket B2B where one customer is worth $10K-1M+. A $200 cost per lead and 10% close rate = $2K CAC. On a $50K annual contract, that's 25x ROI over the first year.</p>

<h2>When the math doesn't</h2>
<p>Low-ticket B2B (under $5K ACV). A $200 CAC can't pay back on a $2K annual product. Meta or Google Search usually works better at that price point.</p>

<h2>Optimization levers</h2>

<h3>Reduce CPC</h3>
<ul>
<li>Broader targeting (if quality holds)</li>
<li>Better creative (higher CTR lowers effective CPC)</li>
<li>Off-peak hours (lower auction pressure)</li>
</ul>

<h3>Improve conversion rate</h3>
<ul>
<li>Native LinkedIn forms instead of sending to website</li>
<li>Match landing page to ad promise</li>
<li>Personalize by audience</li>
</ul>

<h3>Raise LTV</h3>
<ul>
<li>Don't just count first-year revenue - multi-year value supports higher CAC</li>
<li>Referral + expansion revenue</li>
</ul>

<h2>Budget minimums</h2>
<p>Below $3K/month, LinkedIn doesn't get enough data to optimize and you can't iterate. If your budget is under that, skip LinkedIn and run Meta/Google until you have scale.</p>

<h2>Alternative: Sales Navigator + cold email</h2>
<p>For some B2B, using Sales Navigator for targeting + cold email or LinkedIn DM outreach (manual or automated) produces similar quality leads at a fraction of the cost. LinkedIn Ads is for when you need scale.</p>
""",
        prev=("Ad formats", "ad-formats.html"),
        nxt=("Lead gen forms", "lead-gen-forms.html")),

    "linkedin/lead-gen-forms": p("LinkedIn Lead Gen Forms",
        "Lead Gen Forms convert 2-5x higher than external landing pages. Here's how and when to use them.",
        """
<p class="lede">Lead Gen Forms are forms that live on LinkedIn. When a user clicks, a form opens with fields pre-filled from their profile (name, title, company, email). Friction drops; conversion rates jump 2-5x over sending traffic to your landing page.</p>

<h2>How they work</h2>
<ol>
<li>User sees ad in feed</li>
<li>Clicks "Download", "Register", "Request"</li>
<li>Form opens with pre-filled fields (user confirms)</li>
<li>User submits</li>
<li>Lead data available via LinkedIn or synced to CRM</li>
</ol>

<h2>Field options</h2>
<ul>
<li>First Name, Last Name, Email (pre-filled)</li>
<li>Job Title, Company (pre-filled)</li>
<li>Phone (not pre-filled)</li>
<li>Custom questions</li>
</ul>
<p>More fields = lower conversion. Keep it short.</p>

<h2>Best use cases</h2>
<ul>
<li>Whitepaper / ebook / report downloads</li>
<li>Webinar registrations</li>
<li>Demo requests</li>
<li>Newsletter subscriptions</li>
<li>Trial signups (partial - LinkedIn form captures lead, then you send setup email)</li>
</ul>

<h2>Integration with CRM</h2>
<p>LinkedIn integrates natively with HubSpot, Salesforce, Marketo, and others. Set up sync so leads hit your CRM in real time, not via manual download.</p>

<h2>Follow-up is critical</h2>
<p>Lead Gen Forms generate leads fast but conversion depends on follow-up. Within 5 minutes:</p>
<ul>
<li>Send the promised resource</li>
<li>Queue for SDR follow-up</li>
<li>Add to nurture sequence</li>
</ul>

<h2>Quality concerns</h2>
<p>Lower friction means more curiosity-clickers alongside real intent. Quality varies. Some patterns:</p>
<ul>
<li>Qualify in the form (add a "what's your team size" custom question)</li>
<li>Follow up fast and filter by responsiveness</li>
<li>Score by role - intern filling out a VP's form is a pattern</li>
</ul>

<h2>The conversion math</h2>
<p>LinkedIn Lead Gen Form:</p>
<ul>
<li>CPC: $10</li>
<li>Click-to-lead conversion: 30-50%</li>
<li>Cost per lead: $20-35</li>
</ul>
<p>Website form:</p>
<ul>
<li>Same CPC: $10</li>
<li>Click-to-lead: 5-15%</li>
<li>Cost per lead: $65-200</li>
</ul>
<p>Lead Gen Forms win on cost per lead but watch lead quality.</p>
""",
        prev=("Cost reality", "cost-reality.html"),
        nxt=("YouTube Ads overview", "../youtube/overview.html")),

    # YOUTUBE (5)
    "youtube/overview": p("YouTube Ads overview",
        "YouTube is video at scale. Here's the formats and when YouTube Ads make sense.",
        """
<p class="lede">YouTube Ads lets you reach the world's biggest video audience. Different intent modes (search vs recommended vs pre-roll), different formats. Best for brands that have video creative capacity and want scale.</p>

<h2>Ad formats</h2>
<ul>
<li><strong>Skippable In-Stream</strong>: 5-second skip button. Most common. Pay per view (30s+ or completed).</li>
<li><strong>Non-Skippable In-Stream</strong>: 15-20s forced. Pay per impression.</li>
<li><strong>Bumper Ads</strong>: 6s non-skippable. Awareness-focused.</li>
<li><strong>In-Feed (Discovery) Ads</strong>: appear in search and recommendations. User-initiated. Higher intent.</li>
<li><strong>Masthead</strong>: homepage takeover. Premium only.</li>
<li><strong>YouTube Shorts Ads</strong>: vertical short-form, like TikTok.</li>
</ul>

<h2>Where to start</h2>
<p>Most advertisers: Skippable In-Stream with Video View or Conversion objective. Pay per view means you only pay for engaged viewers (didn't skip).</p>

<h2>Targeting</h2>
<ul>
<li>Demographics</li>
<li>Interests (similar to Meta)</li>
<li>Keywords (videos about X topic)</li>
<li>Topics</li>
<li>Placements (specific channels or videos)</li>
<li>Remarketing audiences</li>
<li>Custom intent (based on searches)</li>
</ul>

<h2>Creative basics</h2>
<ul>
<li>Hook in first 5 seconds (before skip is available)</li>
<li>Ad still works if user skips at 5s (state the core value quickly)</li>
<li>Horizontal 16:9 for traditional, vertical 9:16 for Shorts</li>
<li>Sound matters (YouTube plays with sound)</li>
</ul>

<h2>When YouTube wins</h2>
<ul>
<li>Visual/demo products</li>
<li>Brand-building with video-capable creative team</li>
<li>Longer consideration purchases benefiting from video explanation</li>
<li>Audiences that YouTube already reaches (most of them)</li>
</ul>

<h2>When it doesn't</h2>
<ul>
<li>Urgent high-intent conversions (Search is better)</li>
<li>Low creative budget (video costs more than static)</li>
<li>Hyper-niche B2B (LinkedIn better)</li>
</ul>
""",
        prev=("Lead gen forms", "../linkedin/lead-gen-forms.html"),
        nxt=("YouTube ad formats", "formats.html")),

    "youtube/formats": p("YouTube ad formats in depth",
        "The detailed breakdown of each YouTube ad format and when to use which.",
        """
<p class="lede">YouTube has more ad formats than any other platform. Each optimizes for different outcomes. Picking the right format for your goal determines whether YouTube is a channel for you.</p>

<h2>Skippable In-Stream Ads</h2>
<ul>
<li>Appears before, during, or after a video</li>
<li>User can skip after 5 seconds</li>
<li>Advertiser pays when user watches 30+ seconds or engages</li>
<li>Length: usually 30-60 seconds (can be longer)</li>
<li><strong>Best for</strong>: performance, lead gen, conversions</li>
</ul>

<h2>Non-Skippable In-Stream</h2>
<ul>
<li>15-20 seconds, forced viewing</li>
<li>Pay per impression (CPM)</li>
<li>High completion rate (100%)</li>
<li><strong>Best for</strong>: reach + brand messaging with a clear, short message</li>
</ul>

<h2>Bumper Ads</h2>
<ul>
<li>6 seconds max, non-skippable</li>
<li>CPM model</li>
<li>Forces concise creative</li>
<li><strong>Best for</strong>: brand awareness, reminders, supplementary to longer campaigns</li>
</ul>

<h2>In-Feed Video Ads (formerly Discovery)</h2>
<ul>
<li>Appears in YouTube search results, recommended, homepage</li>
<li>User clicks thumbnail to watch</li>
<li>Pay per view</li>
<li><strong>Best for</strong>: higher-intent viewers, educational content, product demos</li>
</ul>

<h2>Masthead Ads</h2>
<ul>
<li>Homepage hero placement</li>
<li>Huge reach</li>
<li>Very expensive (reserved buy)</li>
<li><strong>Best for</strong>: big brand launches or massive reach plays</li>
</ul>

<h2>YouTube Shorts Ads</h2>
<ul>
<li>Vertical video, between organic Shorts</li>
<li>Swipe-away possible</li>
<li>Similar to TikTok dynamics</li>
<li><strong>Best for</strong>: TikTok-style creative, younger audiences</li>
</ul>

<h2>Overlay Ads</h2>
<ul>
<li>Text/banner overlay on video</li>
<li>Non-intrusive</li>
<li>Low-cost</li>
<li><strong>Best for</strong>: supporting video campaigns, retargeting</li>
</ul>

<h2>Picking by goal</h2>
<ul>
<li>Conversions → Skippable In-Stream</li>
<li>Brand reach → Bumpers + Non-Skippable</li>
<li>High-intent research audience → In-Feed</li>
<li>Huge launch → Masthead</li>
<li>Short-form / younger → Shorts</li>
</ul>
""",
        prev=("YouTube Ads overview", "overview.html"),
        nxt=("Creative patterns", "creative-patterns.html")),

    "youtube/creative-patterns": p("YouTube creative patterns",
        "Hook, story, CTA. Here's the structure that works for YouTube ads specifically.",
        """
<p class="lede">YouTube creative is longer-form than TikTok or Meta. You have 30-60 seconds typically. The patterns that work optimize for the 5-second skip moment: hook hard, then deliver.</p>

<h2>The 5-second rule</h2>
<p>Users skip at 5 seconds if not hooked. The first 5 seconds must:</p>
<ul>
<li>State who this is for</li>
<li>Promise a specific benefit</li>
<li>Create enough curiosity to keep watching</li>
</ul>

<h2>Hook patterns</h2>

<h3>Question hook</h3>
<p>"Have you ever wondered why..."</p>

<h3>Claim hook</h3>
<p>"In the next 30 seconds I'll show you..."</p>

<h3>Problem hook</h3>
<p>"If you're still doing X, you're losing [money/time/customers]."</p>

<h3>Curiosity hook</h3>
<p>"The one thing nobody tells you about [topic]..."</p>

<h3>Demonstration hook</h3>
<p>Start with visual demo of the product in action.</p>

<h2>The middle (5-40s)</h2>
<p>Develop the promise made in the hook. Common structures:</p>
<ul>
<li>Problem-solution-demo</li>
<li>Before-after-how</li>
<li>3-step process</li>
<li>Story with payoff</li>
</ul>

<h2>The CTA (last 10-20s)</h2>
<p>Specific next action. Show the URL or CTA button. State it verbally.</p>

<h2>Pattern: "Even if user skips at 5s"</h2>
<p>Design so users who skip have still absorbed the core message. First 5 seconds state: who it's for + what the product is + what it does.</p>

<h2>Production values</h2>
<p>YouTube tolerates (and sometimes prefers) higher production quality than TikTok. Talking-head with good lighting beats shaky phone video on YouTube (unlike TikTok). But don't overdo it - authentic beats over-produced.</p>

<h2>Testing variations</h2>
<p>Like Meta: multiple creatives testing different hooks. 5-10 variants per campaign.</p>

<h2>The end card</h2>
<p>Last 5 seconds: clear CTA with clickable end card. Include the URL verbally and visually.</p>

<h2>Common YouTube ad mistakes</h2>
<ul>
<li>Slow intro (users skip)</li>
<li>No CTA</li>
<li>Repurposed horizontal TV ad that doesn't fit the YouTube context</li>
<li>Brand logo for first 3 seconds (waste of hook opportunity)</li>
<li>Over-long - 30-45s is the sweet spot for most performance goals</li>
</ul>
""",
        prev=("YouTube ad formats", "formats.html"),
        nxt=("YouTube targeting", "targeting.html")),

    "youtube/targeting": p("YouTube targeting options",
        "YouTube has rich targeting, including keywords and placements. Here's how to use them.",
        """
<p class="lede">YouTube targeting inherits from Google Ads plus YouTube-specific options. Keywords (based on video searches), topics, placements (specific channels or videos), audiences.</p>

<h2>Audience options</h2>
<ul>
<li><strong>Demographics</strong>: age, gender, parental status, income</li>
<li><strong>Affinity</strong>: broad interests (sports fans, tech enthusiasts)</li>
<li><strong>In-Market</strong>: actively researching a category</li>
<li><strong>Life Events</strong>: major moments (moving, graduating)</li>
<li><strong>Custom Audiences</strong>: keywords, URLs, apps they've engaged with</li>
<li><strong>Remarketing</strong>: past site visitors, past video viewers</li>
<li><strong>Similar Audiences</strong>: lookalikes from your first-party data</li>
</ul>

<h2>Content targeting</h2>

<h3>Keywords</h3>
<p>Target videos matching keywords. "Running shoe review" targets videos whose titles/descriptions match.</p>

<h3>Topics</h3>
<p>Broader than keywords. Categories like "Home &amp; Garden" or "Sports".</p>

<h3>Placements</h3>
<p>Specific channels, videos, apps, or websites. Most granular control.</p>

<h2>The layering approach</h2>
<p>Combine audience + content for precision:</p>
<ul>
<li>Audience: in-market for running shoes</li>
<li>Content: running-related videos</li>
<li>Result: runners watching running content</li>
</ul>

<h2>Exclusions</h2>
<ul>
<li>Kids content (unless appropriate)</li>
<li>News and sensitive content (brand safety)</li>
<li>Specific topics that don't fit your brand</li>
</ul>

<h2>Custom Intent</h2>
<p>Based on search terms - "target people who recently searched for X on Google". Powerful for capturing intent.</p>

<h2>Remarketing video viewers</h2>
<p>Create remarketing lists based on video engagement:</p>
<ul>
<li>People who watched 25%, 50%, 75%, 100% of a video</li>
<li>Channel subscribers</li>
<li>People who engaged (liked, commented)</li>
</ul>
<p>Retarget these with follow-up ads.</p>

<h2>Geographic + language</h2>
<p>Standard. Narrow when local, broad otherwise.</p>

<h2>Common targeting mistakes</h2>
<ul>
<li>Audience only, no content (ads show in unrelated videos)</li>
<li>Content only, no audience (video match but wrong viewer)</li>
<li>Too narrow (audience too small to optimize)</li>
<li>No exclusions (kids content, brand-unsafe)</li>
</ul>
""",
        prev=("Creative patterns", "creative-patterns.html"),
        nxt=("YouTube vs Meta", "vs-meta.html")),

    "youtube/vs-meta": p("YouTube vs Meta",
        "Both are video ad platforms. Here's when to pick one over the other.",
        """
<p class="lede">YouTube and Meta are the two biggest video ad platforms for most brands. They're genuinely different, not redundant. Picking the right one (or running both) depends on goals, creative, and audience.</p>

<h2>Core differences</h2>

<h3>YouTube</h3>
<ul>
<li>Sound-on platform</li>
<li>Longer watch times (minutes)</li>
<li>Traditional TV-style formats</li>
<li>Higher production expectations</li>
<li>Intent mode (search + recommended)</li>
</ul>

<h3>Meta (Facebook + Instagram)</h3>
<ul>
<li>Sound-off by default</li>
<li>Shorter watch times (seconds)</li>
<li>Feed scroll / story formats</li>
<li>Authentic creative often wins over produced</li>
<li>Interruption mode (feed scrolling)</li>
</ul>

<h2>When YouTube wins</h2>
<ul>
<li>Your creative works with sound-on</li>
<li>You have 30+ seconds of content worth watching</li>
<li>Your audience uses YouTube search/recommendations for research</li>
<li>Visual-demo products</li>
<li>Brand building at scale</li>
</ul>

<h2>When Meta wins</h2>
<ul>
<li>Your creative is feed-native (short, punchy)</li>
<li>DTC / consumer products</li>
<li>Quick impulse purchases</li>
<li>Testing velocity (Meta's creative iteration is faster)</li>
<li>Younger demographics on IG</li>
</ul>

<h2>The "both" answer</h2>
<p>For brands with video production capacity, running both usually wins. They reach different audience states:</p>
<ul>
<li>Meta catches scrolling, distracted audience</li>
<li>YouTube catches research / entertainment-focused audience</li>
</ul>

<h2>The creative portability question</h2>
<p>Can the same video run on both? Sometimes. Mostly no.</p>
<ul>
<li>Meta: 15-30s, vertical, fast-cut, captions</li>
<li>YouTube: 30-60s, horizontal (or 9:16 for Shorts), storytelling</li>
</ul>
<p>Usually you need versions per platform.</p>

<h2>Budget allocation</h2>
<p>For most DTC: 60-70% Meta, 20-30% YouTube, rest testing new channels.</p>
<p>For enterprise B2B: flip - YouTube content campaigns + LinkedIn, less Meta.</p>

<h2>The attribution comparison</h2>
<p>YouTube has better attribution because it's in the Google ecosystem (same GA4 tracking). Meta's attribution is more noise post-iOS 14. Take both with a grain of salt; compare to blended metrics.</p>
""",
        prev=("YouTube targeting", "targeting.html"),
        nxt=("Hook patterns", "../creative/hook-patterns.html")),

    # CREATIVE + COPY (7)
    "creative/hook-patterns": p("Hook patterns for paid ads",
        "The first 3 seconds decide everything. Here are the hook patterns that consistently work.",
        """
<p class="lede">On Meta, TikTok, YouTube, everywhere - the first 3 seconds decide whether anyone watches the rest. Hook patterns are the proven openings that earn the next 27 seconds.</p>

<h2>The 10 hook patterns</h2>

<h3>1. Contrarian claim</h3>
<p>"Everyone tells you to do X. They're wrong."</p>

<h3>2. Specific number</h3>
<p>"I spent $47K testing 12 ad platforms. Here's what I learned."</p>

<h3>3. Direct question</h3>
<p>"Are you still [old way of doing X]?"</p>

<h3>4. Pattern interrupt</h3>
<p>Visual gag, weird sound, or unexpected scene in the first frame.</p>

<h3>5. Personal confession</h3>
<p>"I was running ads wrong for 2 years. Here's what I finally figured out."</p>

<h3>6. News / urgency</h3>
<p>"Meta just changed this. Here's what it means for you."</p>

<h3>7. Warning</h3>
<p>"If you're doing X, stop immediately."</p>

<h3>8. Specific character</h3>
<p>"Meet Sarah. She runs a $10M DTC brand and does something weird every Monday."</p>

<h3>9. Observation hook</h3>
<p>"I noticed something about successful agencies you don't see anywhere else."</p>

<h3>10. Reframe</h3>
<p>"What everyone calls [X] is actually [Y]."</p>

<h2>What doesn't work</h2>
<ul>
<li>Slow intro music with logo</li>
<li>"Hi, I'm X from Y..." (who cares yet)</li>
<li>"Let me tell you about..." (get to the point)</li>
<li>Generic benefit statement ("Save time!")</li>
<li>Feature-first ("Our new software...")</li>
</ul>

<h2>Testing hooks</h2>
<p>Keep the body of the ad the same, test 5-10 different hooks. The hook is usually the single biggest variable you can A/B.</p>

<h2>The match between hook and audience</h2>
<p>Different audiences respond to different hooks:</p>
<ul>
<li>Cold: contrarian, pattern interrupt, curiosity</li>
<li>Warm: specific number, personal confession, news</li>
<li>Hot: direct CTA, offer-forward</li>
</ul>

<h2>Hook + first 10 seconds = the full promise</h2>
<p>Your hook sets expectations. The next 10 seconds must pay them off, or viewers leave.</p>
""",
        prev=("YouTube vs Meta", "../youtube/vs-meta.html"),
        nxt=("UGC vs produced", "ugc-vs-produced.html")),

    "creative/ugc-vs-produced": p("UGC vs produced creative",
        "User-generated-style content has taken over paid ads. Here's when produced still wins.",
        """
<p class="lede">UGC (user-generated content) style ads have largely replaced produced ads in most performance channels. Authentic beats polished. But it's not absolute - produced content still wins in specific contexts.</p>

<h2>UGC characteristics</h2>
<ul>
<li>Shot on phone (or looks like it)</li>
<li>Single person talking to camera</li>
<li>Casual, conversational tone</li>
<li>Vertical format</li>
<li>Natural lighting (often)</li>
<li>Real person, not actor or voiceover</li>
</ul>

<h2>Produced characteristics</h2>
<ul>
<li>Professional lighting and audio</li>
<li>Multiple camera angles</li>
<li>Scripted dialogue or voiceover</li>
<li>Graphics, motion design</li>
<li>Brand-forward visuals</li>
</ul>

<h2>When UGC wins</h2>
<ul>
<li>Meta feed ads (especially IG)</li>
<li>TikTok (always)</li>
<li>Consumer products</li>
<li>Young/mainstream audiences</li>
<li>Testimonial and authenticity angles</li>
<li>Cost-sensitive budgets</li>
</ul>

<h2>When produced wins</h2>
<ul>
<li>YouTube longer-form ads</li>
<li>Brand awareness campaigns</li>
<li>Luxury products</li>
<li>Complex demo requiring clean visuals</li>
<li>Premium B2B</li>
<li>Masthead or big-budget placements</li>
</ul>

<h2>The hybrid approach</h2>
<p>Many brands do both - UGC for performance, produced for brand. Budget allocation: ~70% UGC, ~30% produced for most DTC. Flip for luxury or B2B.</p>

<h2>The "UGC-style" loop</h2>
<p>Some brands produce "UGC-style" content - professionally-shot but designed to look native. This can work but often falls in an uncanny valley where viewers sense it's not quite real.</p>

<h2>Cost comparison</h2>
<ul>
<li>UGC: $50-500 per video</li>
<li>Produced: $5K-50K+ per video</li>
</ul>
<p>UGC lets you test 100 variations for the cost of one produced piece.</p>

<h2>The quality bar is shifting</h2>
<p>UGC quality is rising. Creators know what works. The best UGC is nearly as polished as produced - but the casual feel is maintained. Find creators who understand the medium.</p>
""",
        prev=("Hook patterns", "hook-patterns.html"),
        nxt=("Creative volume", "creative-volume.html")),

    "creative/creative-volume": p("Creative volume",
        "Modern paid ads require creative volume. Here's what the production pipeline looks like at scale.",
        """
<p class="lede">One piece of creative per month used to work. Today, scaling paid ads means shipping 5-50 new creatives per week. Volume is the input; winning creatives are the output. Brands without volume can't compete.</p>

<h2>Why volume matters</h2>
<ul>
<li>Creative fatigue hits fast (days to weeks)</li>
<li>Algorithms reward fresh creative</li>
<li>Most creatives fail; you need volume to find winners</li>
<li>Different angles resonate with different segments</li>
</ul>

<h2>Volume targets by channel</h2>
<ul>
<li><strong>TikTok</strong>: 10-30 new creatives per week</li>
<li><strong>Meta</strong>: 5-15 new creatives per week</li>
<li><strong>YouTube</strong>: 2-5 new creatives per week (longer form)</li>
<li><strong>LinkedIn</strong>: 2-5 per week</li>
</ul>
<p>Scaling accounts go higher - 50+ per week at enterprise scale.</p>

<h2>The production pipeline</h2>

<h3>In-house team</h3>
<ul>
<li>Creative lead (ideation, strategy)</li>
<li>Editor(s) (production, post)</li>
<li>Copywriter (ad copy, scripts)</li>
<li>UGC producer (creator management)</li>
</ul>

<h3>Outsourced</h3>
<ul>
<li>UGC marketplaces for variable creators</li>
<li>Agencies for produced work</li>
<li>Freelancers for editing/design</li>
</ul>

<h3>Hybrid (most common)</h3>
<ul>
<li>Strategy + brief: in-house</li>
<li>Shooting: creators (UGC marketplace or in-house team)</li>
<li>Editing: in-house or freelance</li>
</ul>

<h2>Modular creative</h2>
<p>One shoot produces many ads:</p>
<ul>
<li>Different hooks cut from same raw footage</li>
<li>Different CTAs</li>
<li>Different lengths</li>
<li>Different angles/formats</li>
</ul>
<p>4x the output from 1x the shoot.</p>

<h2>AI-assisted creative</h2>
<p>In 2026, AI accelerates several steps:</p>
<ul>
<li>Script generation for UGC creators</li>
<li>Voiceover (ElevenLabs etc.)</li>
<li>Image generation for statics</li>
<li>Video editing automation</li>
<li>Captions and text overlay</li>
</ul>

<h2>The process discipline</h2>
<ol>
<li>Weekly creative plan (what to test this week)</li>
<li>Brief production (in-house, UGC, or vendor)</li>
<li>Review and QA</li>
<li>Launch</li>
<li>Measure after 5-7 days</li>
<li>Scale winners, kill losers</li>
<li>Feed learnings into next week's plan</li>
</ol>
""",
        prev=("UGC vs produced", "ugc-vs-produced.html"),
        nxt=("Ad copy", "ad-copy.html")),

    "creative/ad-copy": p("Ad copy for paid",
        "Short copy, specific claims, clear CTA. Ad copy rules for every major platform.",
        """
<p class="lede">Paid ad copy is short, specific, and action-oriented. It's direct response compressed into 50-150 words. Each element - hook, body, CTA - does a specific job.</p>

<h2>The structure</h2>
<ol>
<li><strong>Hook</strong>: first line, stops the scroll</li>
<li><strong>Body</strong>: 1-3 sentences developing the promise</li>
<li><strong>Proof</strong>: a specific number, case study, or credential (optional but strong)</li>
<li><strong>CTA</strong>: specific action</li>
</ol>

<h2>Character limits by platform</h2>
<ul>
<li><strong>Meta Feed</strong>: 125 chars primary text before truncation</li>
<li><strong>Meta Story</strong>: headline in overlay, short primary</li>
<li><strong>Google RSA</strong>: 30-char headlines × 15, 90-char descriptions × 4</li>
<li><strong>LinkedIn Sponsored Content</strong>: 150 char intro</li>
<li><strong>TikTok / Reels</strong>: minimal copy, visual-first</li>
<li><strong>YouTube</strong>: 70-100 char headline + 100 char description</li>
</ul>

<h2>Copy rules</h2>

<h3>Specificity beats generality</h3>
<p>"Save money" = dead. "$47/month" = alive. Numbers, named things, specific outcomes.</p>

<h3>One angle per ad</h3>
<p>Don't cram 5 benefits. Pick one angle (price, speed, quality, outcome) and commit.</p>

<h3>Active voice</h3>
<p>"Get X" beats "X can be obtained." Short sentences. Imperative voice for CTAs.</p>

<h3>No jargon without translation</h3>
<p>Industry jargon alienates the 90% not in the inner circle.</p>

<h3>Read like a text, not a pitch</h3>
<p>Especially on Meta. "Just saw this and thought of you" feels personal. "Introducing our revolutionary..." feels corporate.</p>

<h2>CTAs that work</h2>
<ul>
<li>"Shop now" for commerce</li>
<li>"Learn more" for content-led</li>
<li>"Get the guide" for lead magnets</li>
<li>"Try free" for SaaS</li>
<li>"Book call" for services</li>
</ul>

<h2>Emojis</h2>
<p>Platform-dependent:</p>
<ul>
<li>Meta: 1-2 emojis can help CTR</li>
<li>LinkedIn: emojis at top flag as sales-y; avoid</li>
<li>TikTok: fine, feels native</li>
<li>Google: don't bother</li>
</ul>

<h2>The P.S. move</h2>
<p>On longer-form platforms (Meta body, LinkedIn Sponsored), add a "P.S." at the end. Proven to lift CTR - it's the second-most-read line.</p>

<h2>Testing copy</h2>
<p>Hold creative constant, test 3-5 copy variations. Each tests a different angle (price, outcome, pain, story).</p>
""",
        prev=("Creative volume", "creative-volume.html"),
        nxt=("Landing pages", "landing-pages.html")),

    "creative/landing-pages": p("Landing pages for paid",
        "The landing page converts or burns budget. Here's what actually works.",
        """
<p class="lede">Landing pages are where the majority of paid budget is lost. Great ad, bad landing page = 80% drop-off. The landing page's job is to convert the click into a qualified lead or customer.</p>

<h2>The rules</h2>

<h3>Match the ad</h3>
<p>Headline of landing page matches headline of ad. Promise of ad = promise of page. Mismatch = bounce.</p>

<h3>One goal per page</h3>
<p>One primary CTA. Not "sign up OR learn more OR read blog." One.</p>

<h3>Above-the-fold clarity</h3>
<p>In 5 seconds, visitor knows: what you are, what you offer, what to do next.</p>

<h3>Mobile-first</h3>
<p>60-80% of traffic is mobile. Design for mobile first; verify desktop second.</p>

<h3>Fast load</h3>
<p>Under 3 seconds. Ideally under 2. Every second of delay = 10%+ drop in conversion.</p>

<h2>The structure</h2>
<ol>
<li><strong>Above the fold</strong>: headline, subhead, primary CTA, hero image/video</li>
<li><strong>Benefits (not features)</strong>: 3-5 key benefits as you scroll</li>
<li><strong>Social proof</strong>: logos, testimonials, review stars</li>
<li><strong>How it works</strong>: brief process or demo</li>
<li><strong>FAQ</strong>: objection handling</li>
<li><strong>Second CTA</strong></li>
<li><strong>Footer</strong>: basic links</li>
</ol>

<h2>Headline</h2>
<p>The most important element. Should:</p>
<ul>
<li>Match ad promise</li>
<li>Include core benefit</li>
<li>Under 12 words</li>
<li>Readable in under 2 seconds</li>
</ul>

<h2>The form</h2>
<p>For lead gen:</p>
<ul>
<li>Ask only what you need</li>
<li>Every field drops conversion 5-15%</li>
<li>Name + email = baseline</li>
<li>Phone + company = qualifying but lowers conversion</li>
<li>Multi-step forms often beat single long forms</li>
</ul>

<h2>The CTA button</h2>
<ul>
<li>Specific text ("Get my free plan", not "Submit")</li>
<li>High-contrast color</li>
<li>Above fold + at bottom</li>
<li>Visible without hunting</li>
</ul>

<h2>Social proof</h2>
<ul>
<li>Named testimonials with photo (not "John D.")</li>
<li>Logos of known clients</li>
<li>Specific numbers ("4,000+ customers")</li>
<li>Review stars from external platform</li>
</ul>

<h2>Common landing page mistakes</h2>
<ul>
<li>Sending traffic to homepage instead of dedicated page</li>
<li>Multiple CTAs competing</li>
<li>Slow load time</li>
<li>Generic hero image (stock photo)</li>
<li>No social proof</li>
<li>Form with 12 fields</li>
<li>Mismatched ad-to-page messaging</li>
</ul>
""",
        prev=("Ad copy", "ad-copy.html"),
        nxt=("Creative fatigue", "creative-fatigue.html")),

    "creative/creative-fatigue": p("Creative fatigue",
        "Every ad dies. Creative fatigue is when yours stops working. Here's how to manage it.",
        """
<p class="lede">Creative fatigue is inevitable. The same ad, shown to the same audience, stops working over time. The question isn't whether - it's when and how fast. Managing fatigue is the difference between a winning account and a plateauing one.</p>

<h2>Symptoms of fatigue</h2>
<ul>
<li>CTR declining over days/weeks</li>
<li>Frequency rising (same users seeing ad repeatedly)</li>
<li>CPC rising</li>
<li>Conversion rate dropping</li>
<li>Negative feedback (hide ad, report as irrelevant)</li>
</ul>

<h2>The decay curve</h2>
<p>Typical fatigue timeline:</p>
<ul>
<li>Week 1: honeymoon, strong performance</li>
<li>Week 2-3: stable or slight decline</li>
<li>Week 4+: noticeable decline</li>
<li>Week 6+: meaningful underperformance</li>
</ul>
<p>TikTok fatigue is much faster - days to a week.</p>

<h2>What causes fatigue</h2>
<ul>
<li>Audience saturation (everyone in target pool has seen it)</li>
<li>Habituation (viewers stop noticing it)</li>
<li>Platform derankings (algorithm surfaces fresh content)</li>
<li>Competitive creative eroding novelty</li>
</ul>

<h2>Preventive strategies</h2>

<h3>Rotate creatives</h3>
<p>Don't run same ad forever. Fresh creative in rotation keeps overall performance stable.</p>

<h3>Monitor frequency</h3>
<p>Frequency > 3-4 per week is fatigue warning. Refresh creative or narrow audience.</p>

<h3>Expand audience</h3>
<p>Sometimes fatigue is audience exhaustion. New audiences with same creative can re-perform.</p>

<h3>Modular creative</h3>
<p>Recut winning creative with new hooks, new CTAs. Keeps core working, freshens wrapper.</p>

<h2>The rescue playbook</h2>
<ol>
<li>Identify fatigued ad via metric decline</li>
<li>Ship 3-5 fresh variants</li>
<li>Test variants against the fatigued ad</li>
<li>Let winners replace the old</li>
<li>Kill the fatigued ad</li>
</ol>

<h2>Sometimes creative isn't fatigued - the platform is</h2>
<p>If all your ads decline simultaneously, it's likely a platform-level issue (Meta algorithm update, seasonal shift). Don't panic-replace creative; diagnose platform first.</p>

<h2>The winner's ceiling</h2>
<p>Even a great creative has a ceiling. At scale, winners cap out. More budget on the same ad = more fatigue, more frequency, worse ROAS. Diversify creative, diversify audiences, move past the ceiling.</p>
""",
        prev=("Landing pages", "landing-pages.html"),
        nxt=("Hiring creators", "hiring-creators.html")),

    "creative/hiring-creators": p("Hiring creators for ads",
        "Finding UGC creators, negotiating rates, managing the pipeline.",
        """
<p class="lede">For brands that depend on UGC or creator content, managing a creator pipeline is as important as managing media buying. Here's what the process looks like.</p>

<h2>Finding creators</h2>

<h3>Platforms</h3>
<ul>
<li><strong>Insense</strong>: vetted creators, structured contracts</li>
<li><strong>Billo</strong>: similar, often cheaper</li>
<li><strong>TrendHERO</strong>: TikTok focus</li>
<li><strong>Collabstr</strong>: broader creator discovery</li>
<li><strong>TikTok Creator Marketplace</strong>: official TikTok platform</li>
</ul>

<h3>Direct</h3>
<p>DM creators in your niche with 10K-500K followers. Ask for rates. Often cheaper than platforms.</p>

<h3>Your customers</h3>
<p>Existing customers who use your product can make authentic UGC. Offer fee or product.</p>

<h2>Rate ranges</h2>
<ul>
<li>Marketplace creators: $50-300 per video</li>
<li>Mid-tier direct: $200-1000 per video</li>
<li>Established: $500-5000 per video</li>
<li>Celebrity: $10K+</li>
</ul>

<h2>Contract essentials</h2>
<ul>
<li>Deliverables (number of videos, revisions)</li>
<li>Usage rights (where you can use the content, how long)</li>
<li>Exclusivity (can they work with competitors?)</li>
<li>Spark Ad authorization if boosting organic posts</li>
<li>FTC disclosure requirements</li>
<li>Payment terms</li>
</ul>

<h2>The brief</h2>
<p>What creators need:</p>
<ul>
<li>Core message</li>
<li>Key claims to include</li>
<li>Claims NOT to make (compliance)</li>
<li>CTA</li>
<li>Format specs</li>
<li>Brand mentions</li>
<li>Examples of successful videos</li>
<li>Deadline</li>
</ul>

<h2>Managing the pipeline</h2>
<ul>
<li>Maintain active roster of 10-30 creators</li>
<li>Commission 5-20 videos per week across the roster</li>
<li>Track winners; invest more in creators who perform</li>
<li>Drop creators whose content consistently underperforms</li>
</ul>

<h2>Scale challenges</h2>
<ul>
<li>Coordination overhead (who's shooting what when)</li>
<li>Quality variation</li>
<li>Creator reliability</li>
<li>IP and legal across many contracts</li>
</ul>

<h2>The in-house option</h2>
<p>Some brands hire full-time UGC creators. Trade flexibility for consistency. Makes sense at $50K+/month in creator costs.</p>
""",
        prev=("Creative fatigue", "creative-fatigue.html"),
        nxt=("Why attribution broke", "../measurement/why-attribution-broke.html")),

    # MEASUREMENT (7)
    "measurement/why-attribution-broke": p("Why attribution broke",
        "iOS 14, third-party cookies, privacy shifts. Here's the state of ad attribution in 2026.",
        """
<p class="lede">Ad attribution in 2026 is less accurate than it was in 2020. iOS 14, cookie deprecation, and privacy regulation broke the old model. Advertisers who didn't adapt are operating blind. Those who did have new tools and frameworks.</p>

<h2>What broke</h2>

<h3>iOS 14.5 (2021)</h3>
<p>App Tracking Transparency gave users a choice to opt out of tracking. Most chose opt out. Pixel data from iOS users became incomplete.</p>

<h3>Third-party cookies (phased out)</h3>
<p>Chrome finally deprecated third-party cookies in 2024-2025. Cross-site tracking that powered retargeting died.</p>

<h3>Privacy regulation</h3>
<p>GDPR, CCPA, and successor laws make tracking more restricted and disclosure-heavy.</p>

<h3>Safari and Firefox</h3>
<p>Always ahead of Chrome on privacy. Strict third-party cookie blocking for years.</p>

<h2>The consequences</h2>
<ul>
<li>Platform-reported conversions undercount real conversions by 20-50%</li>
<li>Multi-channel attribution is noisy</li>
<li>Retargeting audiences shrank dramatically</li>
<li>Lookalike audiences built on partial data are less precise</li>
<li>Incrementality harder to verify</li>
</ul>

<h2>The adaptations</h2>

<h3>Server-side tracking (CAPI)</h3>
<p>Send events server-to-server instead of relying on pixel. Meta CAPI, Google Enhanced Conversions.</p>

<h3>First-party data</h3>
<p>Build and use your own data (email lists, CRM, user behavior on your site) rather than third-party tracking.</p>

<h3>Blended metrics</h3>
<p>MER, ROAS overall, not per-channel. Accept that platform-specific numbers are directional.</p>

<h3>Incrementality testing</h3>
<p>Holdout tests - turn a channel off and measure revenue change. Truer than platform reports.</p>

<h3>Marketing Mix Modeling</h3>
<p>Statistical modeling of total spend vs total revenue. Doesn't need user-level tracking.</p>

<h2>What it means for day-to-day</h2>
<ul>
<li>Stop chasing exact platform-reported CAC; use directional signal</li>
<li>Look at total blended CAC as the truth</li>
<li>Invest in first-party data infrastructure</li>
<li>Creative becomes more important (targeting is less precise)</li>
<li>Build relationships with customers for data-sharing consent</li>
</ul>
""",
        prev=("Hiring creators", "../creative/hiring-creators.html"),
        nxt=("Platform attribution", "platform-attribution.html")),

    "measurement/platform-attribution": p("Platform attribution",
        "Each platform has its own attribution model. Here's what they measure and what they miss.",
        """
<p class="lede">Meta, Google, TikTok each have their own attribution systems. They report different numbers for the same conversions. Understanding what each captures (and misses) keeps you from over-trusting any one.</p>

<h2>Meta attribution</h2>
<ul>
<li><strong>Default</strong>: 7-day click, 1-day view</li>
<li><strong>Alternatives</strong>: 1-day click only (iOS-friendly)</li>
<li><strong>Includes</strong>: conversions attributed to clicks within window + view-through</li>
<li><strong>Missing</strong>: iOS users without tracking, users in incognito, cross-device</li>
</ul>
<p>Typical underreporting: 20-40% of real conversions.</p>

<h2>Google Ads attribution</h2>
<ul>
<li><strong>Default</strong>: data-driven attribution (DDA)</li>
<li><strong>Older</strong>: last-click, first-click, linear</li>
<li><strong>Includes</strong>: conversions up to 30 days after click</li>
<li><strong>Better than Meta</strong> because of Google's better identity signals (logged-in users)</li>
</ul>

<h2>TikTok attribution</h2>
<ul>
<li>7-day click, 1-day view by default</li>
<li>Newer system, still maturing</li>
<li>Often underreports significantly</li>
</ul>

<h2>The overlap problem</h2>
<p>User sees Meta ad, then Google ad, then converts. Both platforms claim the conversion. If you believe both reports, you double-count. Your real-world total revenue doesn't match.</p>

<h2>The fix: blended measurement</h2>
<ul>
<li>Total ad spend across all channels</li>
<li>Total new customers</li>
<li>Blended CAC = total spend / total customers</li>
</ul>
<p>This is the truth. Channel-specific numbers are directional.</p>

<h2>The MER metric</h2>
<p>Media Efficiency Ratio = Total revenue / Total ad spend. Blended, simple, true. Most mature advertisers track this alongside channel-specific metrics.</p>

<h2>How to use platform attribution</h2>
<ul>
<li>For relative comparison: "is this campaign better or worse than yesterday?" Platform attribution works.</li>
<li>For absolute truth: "how much are we spending per customer?" Use blended.</li>
<li>For budget allocation: use platform data plus lift tests.</li>
</ul>
""",
        prev=("Why attribution broke", "why-attribution-broke.html"),
        nxt=("MER + blended metrics", "mer-blended.html")),

    "measurement/mer-blended": p("MER and blended metrics",
        "Media Efficiency Ratio is the truth metric. Here's how to use it.",
        """
<p class="lede">MER (Media Efficiency Ratio) is Total Revenue / Total Ad Spend. It's blended across all channels, can't be faked by platforms, and reflects real business outcomes. For most DTC brands, it's the single most important metric.</p>

<h2>MER calculation</h2>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px;">
MER = Total Revenue / Total Ad Spend (same period)

If you spent $100K on ads and made $300K in revenue:
MER = 3.0x
</pre>

<h2>Why MER beats per-channel ROAS</h2>
<ul>
<li>Can't be faked by platform double-counting</li>
<li>Reflects actual business</li>
<li>Accounts for synergies between channels</li>
<li>Aligns with P&L numbers</li>
</ul>

<h2>Blended CAC</h2>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px;">
Blended CAC = Total Ad Spend / New Customers (same period)
</pre>
<p>Same idea - blend across channels for truth.</p>

<h2>Target MER by business stage</h2>
<ul>
<li><strong>Early DTC</strong>: 2-3x MER while finding PMF</li>
<li><strong>Growth DTC</strong>: 3-5x MER</li>
<li><strong>Mature DTC</strong>: 5-10x MER</li>
<li><strong>Subscription</strong>: often break-even on first purchase, compound via LTV</li>
</ul>

<h2>MER vs per-channel</h2>
<p>Use both. MER for truth. Per-channel for optimization:</p>
<ul>
<li>MER tells you if overall is working</li>
<li>Per-channel tells you where to allocate</li>
</ul>
<p>When per-channel doesn't match MER, MER wins.</p>

<h2>The tracking setup</h2>
<p>For MER you need:</p>
<ul>
<li>Total ad spend from every channel</li>
<li>Total revenue from all channels including organic</li>
<li>Clean time windows (match spend and revenue to same period)</li>
</ul>
<p>Dashboard these weekly.</p>

<h2>What MER can't tell you</h2>
<ul>
<li>Which channel to cut (needs channel data + incrementality)</li>
<li>Which creative works (per-creative data)</li>
<li>Attribution for complex multi-touch journeys</li>
</ul>
<p>MER is one number, not the whole story. But the one number that matters most.</p>
""",
        prev=("Platform attribution", "platform-attribution.html"),
        nxt=("Incrementality testing", "incrementality.html")),

    "measurement/incrementality": p("Incrementality testing",
        "Platform reports over-claim. Incrementality tests show the real impact of ad spend.",
        """
<p class="lede">Meta says it drove 1,000 conversions. But how many would have happened anyway? Incrementality testing measures the real lift your ads create - the conversions that wouldn't have happened without them. It's the closest thing to truth in ad measurement.</p>

<h2>The simple test: geo holdout</h2>
<ol>
<li>Split your market into "ad" and "no-ad" geos of comparable size</li>
<li>Run ads in the "ad" geo, pause in "no-ad" geo</li>
<li>Measure revenue in both over 2-4 weeks</li>
<li>Lift = (ad-geo revenue) - (no-ad geo revenue, adjusted for size)</li>
</ol>

<h2>Why this works</h2>
<p>Controls for everything except ad spend. If ad-geo had 20% more revenue than no-ad geo, ads drove that 20% lift.</p>

<h2>Platform-supported tests</h2>

<h3>Meta Lift Study</h3>
<p>Meta splits users into test and control. Official holdout. Works if budget is high enough.</p>

<h3>Google Conversion Lift</h3>
<p>Similar. Google-run holdout.</p>

<h2>The truth reveals</h2>
<p>Most brands doing incrementality tests find:</p>
<ul>
<li>Meta reports 20-50% more conversions than it actually drives</li>
<li>Retargeting drives far fewer incremental conversions than reported (often 20-40% of what platform claims)</li>
<li>Branded search largely captures conversions that would happen anyway</li>
<li>Top-of-funnel channels (YouTube, TikTok) often drive more incremental than reported</li>
</ul>

<h2>How often to test</h2>
<ul>
<li>Quarterly or semi-annually for major channels</li>
<li>Before big budget increases</li>
<li>When MER and platform reports diverge</li>
</ul>

<h2>Cost of testing</h2>
<p>You "waste" ad dollars in holdout periods. The learning is worth it - accurate measurement changes budget allocation.</p>

<h2>The realpolitik</h2>
<p>Many platforms and agencies resist incrementality testing because it reveals they over-claim. Do the tests anyway. The results inform where to invest next dollar.</p>
""",
        prev=("MER + blended metrics", "mer-blended.html"),
        nxt=("Marketing mix modeling", "mmm.html")),

    "measurement/mmm": p("Marketing mix modeling (MMM)",
        "MMM is statistical modeling that infers channel contribution without user-level tracking. Here's when it's worth it.",
        """
<p class="lede">Marketing Mix Modeling uses historical data (spend and revenue by channel over time) to statistically estimate each channel's contribution. Privacy-safe (no user-level data), but requires scale and sophistication to set up.</p>

<h2>How MMM works</h2>
<ol>
<li>Collect historical data: spend by channel, total revenue, external factors (seasonality, competitors, weather)</li>
<li>Statistical model fits the relationship: revenue = f(spend by channel, factors)</li>
<li>Output: estimated marginal contribution per dollar of each channel</li>
<li>Used to allocate future budget</li>
</ol>

<h2>What MMM is good at</h2>
<ul>
<li>Privacy-safe (no user tracking)</li>
<li>Accounts for all channels (including TV, podcast, OOH)</li>
<li>Captures diminishing returns (channels saturate)</li>
<li>Long-term view (not just last-click)</li>
</ul>

<h2>What MMM struggles with</h2>
<ul>
<li>Requires 2+ years of data ideally</li>
<li>Need scale (small data = noisy models)</li>
<li>Can't detect sudden changes (creative launches, platform shifts)</li>
<li>Expensive to build and maintain</li>
</ul>

<h2>Who should use MMM</h2>
<ul>
<li>Brands spending $5M+/year on paid media</li>
<li>Multi-channel (4+ channels with meaningful spend)</li>
<li>Has data infrastructure to support it</li>
<li>Businesses seeing attribution chaos across channels</li>
</ul>

<h2>Who shouldn't yet</h2>
<ul>
<li>Sub-scale advertisers</li>
<li>Brands with few channels (just Meta + Google)</li>
<li>Pre-product-market-fit (need to iterate faster than MMM responds)</li>
</ul>

<h2>Tools</h2>
<ul>
<li><strong>Open-source</strong>: Meta Robyn, Google Meridian, LightweightMMM</li>
<li><strong>Commercial</strong>: Analytic Partners, Neustar, Ekimetrics</li>
<li><strong>New</strong>: Recast, ProfitMetrics, automated MMM platforms</li>
</ul>

<h2>MMM vs incrementality testing</h2>
<p>Complementary:</p>
<ul>
<li>MMM for ongoing strategic allocation (quarterly, annual)</li>
<li>Incrementality tests for validating specific channels (ad hoc)</li>
<li>Platform attribution for tactical optimization (weekly, daily)</li>
</ul>
<p>Mature measurement uses all three.</p>
""",
        prev=("Incrementality testing", "incrementality.html"),
        nxt=("LTV:CAC", "ltv-cac.html")),

    "measurement/ltv-cac": p("LTV:CAC",
        "Lifetime Value to Customer Acquisition Cost ratio. The unit economic that determines whether paid ads work.",
        """
<p class="lede">LTV:CAC is whether the customers you acquire are worth more than what you paid to acquire them. It's the single most important unit economic for paid advertising businesses. Below 3:1 you're fragile; above 5:1 you can scale profitably.</p>

<h2>Definitions</h2>

<h3>LTV (Lifetime Value)</h3>
<p>Total gross profit a customer generates over their relationship with you.</p>
<pre>LTV = Gross profit per customer × years as customer</pre>

<h3>CAC (Customer Acquisition Cost)</h3>
<p>Total cost to acquire one customer, including ad spend + any associated costs.</p>
<pre>CAC = Total ad spend / Customers acquired</pre>

<h2>Target ratios by business type</h2>
<ul>
<li><strong>DTC single-purchase</strong>: 3:1 minimum, 5:1 healthy</li>
<li><strong>DTC subscription</strong>: 4-10:1 range</li>
<li><strong>SaaS</strong>: 3:1 minimum, aim for 5:1+</li>
<li><strong>B2B high-ticket</strong>: 5-10:1</li>
<li><strong>Marketplace</strong>: variable; depends on take rate and repeat</li>
</ul>

<h2>Why 3:1 minimum</h2>
<p>LTV is gross profit, not revenue. From 3x gross profit, you need to cover:</p>
<ul>
<li>Overhead, salaries, infrastructure</li>
<li>Product development</li>
<li>Non-ad marketing spend</li>
<li>Profit/dividends</li>
</ul>
<p>1:1 or 2:1 means you're paying for customers without leaving room for the business to exist.</p>

<h2>Payback period</h2>
<p>How quickly you recover CAC. Rule of thumb:</p>
<ul>
<li>Under 6 months: healthy</li>
<li>6-12 months: acceptable</li>
<li>12-24 months: risky (needs strong retention)</li>
<li>24+ months: break-even on acquisition, all profit from retention</li>
</ul>

<h2>Improving LTV:CAC</h2>

<h3>Reduce CAC</h3>
<ul>
<li>Better creative → lower CPC, higher conversion</li>
<li>Better landing pages</li>
<li>Less expensive channels</li>
</ul>

<h3>Increase LTV</h3>
<ul>
<li>Upsells and cross-sells</li>
<li>Subscription (higher retention)</li>
<li>Raise prices</li>
<li>Reduce churn</li>
<li>Expand offering</li>
</ul>

<h2>The segmentation reveal</h2>
<p>Blended LTV:CAC often hides truth. Segment:</p>
<ul>
<li>By channel (Meta CAC vs Google CAC)</li>
<li>By customer type</li>
<li>By product/offer</li>
<li>By cohort</li>
</ul>
<p>Often some segments are 1.5:1 while others are 8:1. Shifting budget into the 8:1 segments is where growth comes from.</p>
""",
        prev=("Marketing mix modeling", "mmm.html"),
        nxt=("Dashboards that matter", "dashboards.html")),

    "measurement/dashboards": p("Dashboards that matter",
        "What to track daily, weekly, monthly. The dashboards that actually drive decisions.",
        """
<p class="lede">Many paid advertisers have 40-tile dashboards nobody reads. A few metrics, updated regularly, beat comprehensive dashboards ignored. Here are the dashboards that actually move the business.</p>

<h2>The daily dashboard</h2>
<p>Check every morning:</p>
<ul>
<li>Total ad spend yesterday (all channels)</li>
<li>Total revenue yesterday</li>
<li>MER yesterday</li>
<li>Anomalies (channel up/down more than 30% vs 7-day average)</li>
</ul>
<p>Goal: catch problems early. Not comprehensive - early warning.</p>

<h2>The weekly dashboard</h2>
<p>Review every Monday:</p>
<ul>
<li>Week-over-week: spend, revenue, MER, new customers</li>
<li>By channel: spend, conversions, CAC, ROAS</li>
<li>Creative performance: top 5, bottom 5</li>
<li>Landing page conversion rates</li>
<li>Inventory of campaigns with issues</li>
</ul>
<p>Goal: set this week's priorities.</p>

<h2>The monthly dashboard</h2>
<p>Full strategic review:</p>
<ul>
<li>Monthly MER trend</li>
<li>Blended CAC vs target</li>
<li>LTV:CAC (actual, not projected)</li>
<li>Cohort retention</li>
<li>Channel mix trends</li>
<li>Creative output (how many ads shipped)</li>
<li>Incrementality lift test results (if done)</li>
</ul>
<p>Goal: evaluate strategy. Are we on track?</p>

<h2>Tools</h2>
<ul>
<li><strong>Triple Whale</strong>: DTC-focused, aggregates Meta, Google, TikTok + Shopify</li>
<li><strong>Northbeam, Rockerbox</strong>: attribution + MER</li>
<li><strong>Looker Studio / Tableau</strong>: custom dashboards from data warehouse</li>
<li><strong>Spreadsheet</strong>: for early-stage or small operations, a Google Sheet is enough</li>
</ul>

<h2>What not to dashboard</h2>
<ul>
<li>Vanity metrics (impressions, reach - unless explicitly optimizing for them)</li>
<li>Platform-reported numbers without blended context</li>
<li>Per-ad metrics at the daily level (too noisy)</li>
<li>Too many metrics - pick the 5-10 that drive decisions</li>
</ul>

<h2>The action orientation</h2>
<p>Every dashboard tile should answer: "what action would I take if this number moves?" If no action follows, drop the tile.</p>
""",
        prev=("LTV:CAC", "ltv-cac.html"),
        nxt=None),
}


from _paid_ads_content import SIDEBAR
from _build_expertise import build_expertise_section

build_expertise_section("paid-ads", "Paid Advertising", SIDEBAR, PAGES)
print("\n✓ Paid Ads: 37 additional pages (50 total)")
