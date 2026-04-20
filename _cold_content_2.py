#!/usr/bin/env python3
"""Cold Email content part 2: Lists + Targeting (6 pages)."""
from _build_cold import write_cold_page

DR_LINK = "../../direct-response"


write_cold_page(
    slug="lists/icp",
    title="Defining the ICP",
    description="Cold email quality is capped by list quality. List quality is capped by ICP definition. Here's how to write one that actually targets.",
    reading_time=5,
    body_html=f"""
<p class="lede">The ICP (Ideal Customer Profile) is the filter every prospect passes through before they get an email from you. A vague ICP produces a vague list, produces a vague campaign, produces disappointing results. A specific ICP produces a targeted list that converts. This is where cold email quality is actually decided.</p>

<h2>Why most ICPs fail</h2>
<p>Most teams write ICPs like: "B2B companies in North America, 50-500 employees, using HubSpot." That's a filter, not an ICP. It doesn't tell you <em>why</em> those companies need you, only <em>which</em> companies exist.</p>

<p>A real ICP answers: "Who has this problem acutely right now, has the budget to solve it, and can make the decision?"</p>

<h2>The layered definition</h2>

<h3>Layer 1: Firmographics</h3>
<ul>
  <li>Industry / vertical</li>
  <li>Company size (employees, revenue)</li>
  <li>Geography</li>
  <li>Growth stage</li>
  <li>Funding status</li>
  <li>Tech stack (if relevant)</li>
</ul>

<h3>Layer 2: Role / buyer</h3>
<ul>
  <li>Job title (specific, not just "decision-maker")</li>
  <li>Department</li>
  <li>Seniority level</li>
  <li>Whether they're the economic buyer, user, or both</li>
</ul>

<h3>Layer 3: Pain / situation</h3>
<ul>
  <li>What specific problem does this buyer have?</li>
  <li>What triggered the problem (or made it urgent)?</li>
  <li>What have they tried?</li>
  <li>What happens if they don't fix it?</li>
</ul>

<h3>Layer 4: Signals</h3>
<ul>
  <li>What observable events suggest the pain is active?</li>
  <li>Recent hiring (new VP Sales = pipeline push coming)</li>
  <li>Recent funding (budget for new tools)</li>
  <li>Job posting (specific role = specific need)</li>
  <li>Tech changes (adding tool X = needs complementary tool Y)</li>
  <li>Press announcements</li>
  <li>Public metrics (traffic, app installs, headcount)</li>
</ul>

<h2>The ICP template</h2>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Name:</strong> [Give the ICP a memorable name, e.g., "Mid-market VP Sales, Post-funding"]<br><br>
<strong>Company profile:</strong> [firmographics]<br>
<strong>Role:</strong> [specific title, seniority, authority]<br>
<strong>Current situation:</strong> [Monday morning, what's happening]<br>
<strong>The pain:</strong> [specific problem, measurable if possible]<br>
<strong>Trigger event:</strong> [what makes the pain active now]<br>
<strong>Already tried:</strong> [what didn't work for them]<br>
<strong>Budget:</strong> [range, authority]<br>
<strong>Decision cycle:</strong> [weeks? months?]<br>
<strong>Key objections:</strong> [3-5 likely pushbacks]<br>
<strong>Signals to target on:</strong> [observable events we can detect]<br>
<strong>The outcome they want:</strong> [in their words]<br>
<strong>The outcome we deliver:</strong> [in our language]
</blockquote>

<h2>The trap: too broad</h2>
<p>"Anyone could benefit from our tool." Nobody can be sold with cold email because the email can't say anything specific to them. The copy becomes generic. The list is 500K people. The conversion is 0.1%.</p>

<p>Narrow deliberately. Pick one specific ICP. Test copy against them. Scale. Then expand to adjacent ICPs.</p>

<h2>The trap: too narrow</h2>
<p>"Chief Revenue Officers of Series B SaaS companies in North America, with 80-120 AEs, using Gong, who closed Q3 at 85-92% of plan." Maybe 50 people in the world. Can't scale, can't test properly.</p>

<p>Test the ICP size: Apollo or Sales Navigator search for your criteria should return 5,000-50,000 matches. Below 5,000 is usually too narrow for cold email (warm outreach or events better). Above 50,000 is too broad - add qualifying filters.</p>

<h2>Multiple ICPs</h2>
<p>A maturing business has 2-4 ICPs, each with its own copy and campaign. Not one giant "everyone" ICP.</p>

<p>Example for a sales tool:</p>
<ul>
  <li>ICP A: VP Sales at 50-100 person B2B SaaS, growing pipeline</li>
  <li>ICP B: Founder at 10-30 person B2B startup, founder-led sales</li>
  <li>ICP C: Head of Revenue Operations at 200+ person B2B, operational efficiency</li>
</ul>

<p>Each gets targeted copy. Each has its own list. Each has its own sequence. Treating them as one dilutes everything.</p>

<h2>Validating the ICP</h2>
<p>Before investing in infrastructure and list building:</p>
<ol>
  <li>Find 10 people who match the ICP</li>
  <li>Do <a href="{DR_LINK}/leads/warm-outreach.html">warm outreach</a> or direct manual outreach to them</li>
  <li>Have real conversations. Does the pain match what you hypothesized?</li>
  <li>Does the offer resonate?</li>
  <li>If yes, scale the ICP into cold outreach</li>
  <li>If no, refine the ICP and repeat</li>
</ol>

<p>Do this before buying data and sending thousands of emails. One bad ICP → one burned campaign → one damaged reputation.</p>

<h2>Relating to the <a href="{DR_LINK}/market/dream-customer.html">dream customer</a></h2>
<p>The ICP is a summary; the <a href="{DR_LINK}/market/dream-customer.html">dream customer</a> is the story. The ICP tells you who to target; the dream customer tells you what to say. You need both. Build the ICP first for list building; build the dream customer doc for copy.</p>

<h2>ICP iteration</h2>
<p>The ICP evolves:</p>
<ul>
  <li>Positive replies tell you which sub-segments convert</li>
  <li>Objections tell you where the ICP is miscalibrated</li>
  <li>Closed deals tell you who actually buys (may differ from who you originally targeted)</li>
</ul>

<p>Review the ICP quarterly. Update based on actual data. The post-launch ICP is almost always different from the pre-launch hypothesis.</p>

<p style="margin-top:40px;">Next: <a href="databases.html">Lead databases</a>.</p>
""",
    prev=("Reply management", "../infra/reply-management.html"),
    nxt=("Lead databases", "databases.html"),
)


write_cold_page(
    slug="lists/databases",
    title="Lead databases",
    description="Apollo, ZoomInfo, LinkedIn Sales Navigator, Lusha, Seamless. Here's how the major B2B data providers differ and which to pick when.",
    reading_time=5,
    body_html="""
<p class="lede">Your list comes from somewhere. B2B data providers are the primary sources: databases of companies, roles, emails, and firmographic data that power most cold outbound. The quality and freshness varies dramatically by provider and by segment. Here's what I actually reach for.</p>

<h2>The big categories</h2>

<h3>Full-data platforms</h3>
<p>Apollo, ZoomInfo, Cognism, SalesIntel. Comprehensive B2B databases with contact info, company data, intent signals, technographics.</p>

<h3>LinkedIn-based tools</h3>
<p>Sales Navigator (for finding prospects), plus scrapers like Wiza, Evaboot, that extract emails from Nav searches.</p>

<h3>Email finders</h3>
<p>Lusha, Hunter, Anymail Finder, Findymail, Seamless. Take a name + company and return likely email addresses.</p>

<h3>Enrichment platforms</h3>
<p>Clay, Rocketreach, Bouncer. Enrich existing lists with additional data.</p>

<h2>The main providers</h2>

<h3>Apollo</h3>
<p>Most popular for cold outbound in 2026. Large database, reasonable pricing, includes sequencing tool (so it's an all-in-one).</p>
<ul>
  <li>Strengths: huge database, decent email accuracy, built-in outreach</li>
  <li>Weaknesses: data quality varies; some industries sparse</li>
  <li>Price: $49-149/user/month for typical tiers</li>
</ul>

<h3>ZoomInfo</h3>
<p>Enterprise-grade. Most accurate for direct-dial phone numbers and senior contacts. Expensive.</p>
<ul>
  <li>Strengths: data quality, enterprise contact coverage</li>
  <li>Weaknesses: expensive, often 6-figure contracts</li>
  <li>Price: quote-based, typically $15K-100K+/year</li>
</ul>

<h3>LinkedIn Sales Navigator</h3>
<p>The most current and accurate source of job titles and company data - because people update their own LinkedIn. Not an email source by itself; pair with Evaboot or Wiza to extract emails.</p>
<ul>
  <li>Strengths: freshest data, best role filtering, strong ICP definition via filters</li>
  <li>Weaknesses: no emails natively; must pair with email finder</li>
  <li>Price: $99/user/month for Core, more for Advanced</li>
</ul>

<h3>Cognism</h3>
<p>Strong for EU coverage. GDPR-compliant by design. Good B2B mobile numbers.</p>
<ul>
  <li>Strengths: EU data, mobile coverage, compliance focus</li>
  <li>Weaknesses: US data less deep than ZoomInfo</li>
  <li>Price: quote-based, usually $12K-40K/year</li>
</ul>

<h3>Lusha</h3>
<p>Popular Chrome extension for on-the-fly contact lookup. Used often for lower-volume or research-heavy workflows.</p>
<ul>
  <li>Price: $29-95/user/month, pay-per-credit model</li>
</ul>

<h3>Hunter.io</h3>
<p>Email finder and verifier. Straightforward. Good for small-scale or specific lookups.</p>
<ul>
  <li>Price: $49-199/month</li>
</ul>

<h3>Clay</h3>
<p>Not a database per se - an enrichment platform that chains data sources. More on this in <a href="clay.html">Clay and enrichment</a>.</p>

<h2>Database accuracy reality</h2>
<p>No provider has 100% accurate data. Typical accuracy:</p>
<ul>
  <li>Company data (industry, size): 70-90% accurate</li>
  <li>Job titles: 60-85% accurate (people leave, change roles)</li>
  <li>Email addresses: 70-85% accurate</li>
  <li>Phone numbers: 40-70% accurate</li>
</ul>

<p>Never send without <a href="verification.html">verifying email addresses</a>. Never assume titles are current without checking LinkedIn.</p>

<h2>Segment-by-segment recommendations</h2>

<h3>US B2B SaaS, mid-market+</h3>
<p>Apollo as primary, Sales Nav + Evaboot for key accounts, ZoomInfo for enterprise.</p>

<h3>EU / UK</h3>
<p>Cognism or Apollo with EU focus. GDPR compliance is critical.</p>

<h3>SMB services (agencies, consultants)</h3>
<p>Apollo, Sales Nav + email finder. Less need for enterprise-grade databases.</p>

<h3>Specific niche industries</h3>
<p>Niche databases exist for specific verticals (healthcare, legal, construction, manufacturing). Research per-vertical for best results.</p>

<h3>Local / SMB / brick-and-mortar</h3>
<p>Google Maps scrapers, Yelp data, industry-specific directories. Major databases are weak here.</p>

<h2>The list-building workflow</h2>

<h3>Workflow 1: Apollo-direct</h3>
<ol>
  <li>Filter Apollo by ICP criteria</li>
  <li>Export contacts</li>
  <li>Verify emails</li>
  <li>Upload to cold email tool</li>
</ol>

<p>Fast. Good enough for most campaigns.</p>

<h3>Workflow 2: Sales Nav + enrichment</h3>
<ol>
  <li>Build a search in Sales Navigator</li>
  <li>Export via Wiza or Evaboot</li>
  <li>Enrich with Clay for company data, signals</li>
  <li>Verify emails</li>
  <li>Upload to cold email tool</li>
</ol>

<p>Slower but better data quality and more signal-driven targeting.</p>

<h3>Workflow 3: Clay-orchestrated</h3>
<ol>
  <li>Clay table as the source of truth</li>
  <li>Multiple enrichment providers (Apollo, Clearbit, LinkedIn)</li>
  <li>Data waterfall: try providers in order, use first match</li>
  <li>Custom enrichment (scraping, AI-generated fields)</li>
  <li>Push to cold email tool via integration</li>
</ol>

<p>Most flexible. Highest data quality. Covered in <a href="clay.html">Clay and enrichment</a>.</p>

<h2>Data freshness</h2>
<p>All databases have stale data. A title from 6 months ago might be wrong today. Strategies:</p>
<ul>
  <li>Pull recent data (prefer "last updated" within 90 days if shown)</li>
  <li>Re-enrich before each major campaign</li>
  <li>Check LinkedIn directly for high-priority targets</li>
  <li>Monitor bounce rates - sudden spike may signal stale data</li>
</ul>

<h2>Legal / ethical considerations</h2>
<ul>
  <li>GDPR: sourcing personal data from databases has compliance implications in the EU. Most major providers claim compliance but verify for your use case.</li>
  <li>Purchased lists from unknown sources: avoid. Reputation and legal risk.</li>
  <li>Opt-out: even with purchased data, honor opt-outs and maintain a suppression list.</li>
</ul>

<h2>The cost reality</h2>
<p>Expect to spend $200-2000/month on data for a cold outbound operation. At enterprise scale, $20K-100K/year is normal.</p>

<p>This cost pays back many times over when the data is good. It's a complete write-off when the data is bad (bounces, wrong targets, no responses). Invest in data as seriously as you invest in copy.</p>

<p style="margin-top:40px;">Next: <a href="clay.html">Clay and enrichment</a>.</p>
""",
    prev=("Defining the ICP", "icp.html"),
    nxt=("Clay and enrichment", "clay.html"),
)


write_cold_page(
    slug="lists/clay",
    title="Clay and enrichment",
    description="Clay changed the cold email data game. Here's how enrichment platforms work and the workflows that separate amateur targeting from the best operators.",
    reading_time=5,
    body_html="""
<p class="lede">Clay is the platform that turned cold email data from a static export into a programmable pipeline. Combined with multiple data sources, AI-generated enrichment, and custom scrapers, it lets you build lists that are dramatically higher quality than any single database can provide. If you're running serious cold outbound, Clay is probably already in your stack.</p>

<h2>What Clay is</h2>
<p>Think of Clay as a spreadsheet-meets-programmable-data-pipeline. You start with a list of companies or people. Clay enriches each row by calling external providers, scraping web pages, running AI prompts, and combining results.</p>

<p>Output: a fully enriched list with whatever fields you need - firmographics, tech stack, recent funding, LinkedIn activity, buying signals, AI-written first lines - all in a single table ready to push to your cold email tool.</p>

<h2>The core capabilities</h2>

<h3>1. Data waterfall</h3>
<p>Try multiple providers in order for each row. Clearbit for firmographics → Apollo if Clearbit missed → LinkedIn scraper if both missed. Use first successful result.</p>

<p>Dramatically improves coverage vs single-provider workflows.</p>

<h3>2. Multi-source enrichment</h3>
<p>Connect Apollo, Clearbit, LinkedIn, ZoomInfo, Rocketreach, People Data Labs, Lusha - all in one pipeline. Pull different fields from different providers.</p>

<h3>3. Web scraping</h3>
<p>Scrape company websites, job boards, news, SEC filings. Extract specific data points via CSS selectors or AI.</p>

<h3>4. AI prompts</h3>
<p>Use ChatGPT/Claude within cells to generate custom fields: summarize a company's recent press release, infer likely pain points, write personalized first lines, classify companies into segments.</p>

<h3>5. Custom logic</h3>
<p>Formulas, conditionals, HTTP requests to any API. Effectively a low-code data pipeline.</p>

<h2>The killer workflows</h2>

<h3>Signal-based targeting</h3>
<p>Start with a list of companies. Enrich each with signals:</p>
<ul>
  <li>Recent funding round (Crunchbase)</li>
  <li>Recent executive hire (LinkedIn)</li>
  <li>Job postings for specific roles</li>
  <li>Hiring velocity</li>
  <li>Tech stack changes (BuiltWith)</li>
  <li>Recent press mentions</li>
</ul>

<p>Filter down to companies with active signals indicating pain. Much higher conversion than blanket ICP filters.</p>

<h3>AI-generated personalization at scale</h3>
<p>For each prospect, have an AI summarize something relevant - recent LinkedIn post, company news, job change - into a personalized first line. The cold email template includes <code>{{personalized_line}}</code>, Clay fills it per row.</p>

<p>Result: each email has a genuinely personalized opening that would take 5 minutes of manual research to write, done at scale.</p>

<h3>Waterfall email finding</h3>
<p>For each contact, try multiple email finders in sequence:</p>
<ol>
  <li>Apollo</li>
  <li>Rocketreach</li>
  <li>Anymail Finder</li>
  <li>Hunter</li>
  <li>Findymail</li>
</ol>

<p>Coverage rises from ~75% with any single provider to 95%+ with a waterfall.</p>

<h3>Job-posting-triggered outreach</h3>
<p>Scrape job boards daily. Identify companies hiring for roles that indicate a pain you solve. (Hiring a "VP Sales" right now = pipeline pressure → your pipeline tool is relevant.) Auto-add to outbound campaigns.</p>

<h2>Clay pricing</h2>
<ul>
  <li>Starter: $149/month</li>
  <li>Pro: $349/month</li>
  <li>Enterprise: $$$</li>
</ul>

<p>Plus per-credit costs for enrichment calls. Can add up: a 10K-row table run through 5 providers might cost $200-500 in credits.</p>

<p>For teams doing serious cold outbound, Clay pays back in list quality. For solo operators or small volume, it may be overkill.</p>

<h2>Alternative enrichment platforms</h2>

<h3>Bardeen, Instantly Leads, Smartlead Enrich</h3>
<p>Lighter-weight enrichment. Less programmable but easier to start with.</p>

<h3>PhantomBuster</h3>
<p>Automation platform that can do enrichment workflows. Less structured than Clay but more flexible for automation.</p>

<h3>Zapier + multiple providers</h3>
<p>DIY approach. Works but gets complicated fast.</p>

<h2>The Clay learning curve</h2>
<p>Clay is powerful but not obvious. The first week feels steep. Workflows that seem complicated become automatic after you've built 5-10 tables.</p>

<p>Starting path:</p>
<ol>
  <li>Build a simple company-enrichment table (firmographics only)</li>
  <li>Add contact enrichment (name + email)</li>
  <li>Add one AI column for personalization</li>
  <li>Add an email waterfall for coverage</li>
  <li>Add signal enrichment (funding, hires, jobs)</li>
</ol>

<h2>The output pattern</h2>
<p>Clay tables feed into cold email tools via:</p>
<ul>
  <li>CSV export (simplest)</li>
  <li>Native integration with Instantly, Smartlead, etc.</li>
  <li>Webhook push to any sequencing tool</li>
</ul>

<p>Typically you keep Clay as the source of truth for list, with incremental syncs into the outreach tool.</p>

<h2>The quality improvement</h2>
<p>A Clay-enriched list vs raw Apollo export:</p>
<ul>
  <li>Coverage: 95%+ vs 75%</li>
  <li>Accuracy: higher because of cross-verification</li>
  <li>Signal: adds buying triggers that Apollo alone doesn't surface</li>
  <li>Personalization: per-prospect fields enable higher-quality copy</li>
</ul>

<p>Translated to outcomes: 20-50% higher positive reply rate from equivalent list sizes. That difference is the ROI on Clay.</p>

<h2>The common mistake</h2>
<p>Teams adopt Clay and over-enrich - every row has 30 columns of data, but the cold email only references 2 of them. The other 28 columns are waste.</p>

<p>Enrichment should be purposeful. Add a field only if:</p>
<ul>
  <li>You'll use it in email copy</li>
  <li>You'll filter on it</li>
  <li>You'll route / segment based on it</li>
</ul>

<p>Anything else is cost without return.</p>

<p style="margin-top:40px;">Next: <a href="verification.html">Verification and hygiene</a>.</p>
""",
    prev=("Lead databases", "databases.html"),
    nxt=("Verification + hygiene", "verification.html"),
)


write_cold_page(
    slug="lists/verification",
    title="Verification + hygiene",
    description="Sending to unverified addresses destroys domain reputation fast. Here's how to verify, when, and how strict to be.",
    reading_time=4,
    body_html="""
<p class="lede">Every email you send to a non-existent or invalid address is a hard bounce. Bounces are the #1 reputation destroyer in cold email. Email verification is the prerequisite to every send - and the step most teams skip when they're in a rush.</p>

<h2>What email verification does</h2>
<p>Checks whether an email address actually exists and will accept mail before you try to send. Methods:</p>
<ol>
  <li>Check syntax (is it formatted correctly?)</li>
  <li>Check domain MX records (does the domain accept email at all?)</li>
  <li>SMTP handshake (connect to the receiving server and check if the address exists, without actually sending)</li>
  <li>Additional checks: is the domain disposable, is it a catch-all, is the address role-based</li>
</ol>

<p>Output per address:</p>
<ul>
  <li>Valid - deliverable</li>
  <li>Invalid - will bounce</li>
  <li>Catch-all - domain accepts anything, uncertain</li>
  <li>Risky - syntactically okay but flagged</li>
  <li>Unknown - couldn't verify</li>
</ul>

<h2>Why verification matters</h2>
<p>Hard bounce rates damage sender reputation badly. Rule of thumb:</p>
<ul>
  <li>Under 2% bounce rate: safe</li>
  <li>2-3%: caution, clean the list</li>
  <li>Over 3%: actively damaging reputation</li>
  <li>Over 5%: Gmail/Outlook will start filtering you aggressively</li>
</ul>

<p>A single unverified list can push you from 1% to 6% bounce rate overnight. One campaign can damage infrastructure for weeks.</p>

<h2>Verification tools</h2>

<h3>Standalone verifiers</h3>
<ul>
  <li><strong>ZeroBounce</strong>: accurate, handles catch-alls well</li>
  <li><strong>NeverBounce</strong>: reliable, integrates with many tools</li>
  <li><strong>Million Verifier</strong>: cheap per-email at scale</li>
  <li><strong>Bouncer</strong>: strong enterprise option</li>
  <li><strong>MailTester / Emailable / Kickbox</strong>: alternatives with similar quality</li>
</ul>

<h3>Built into data providers</h3>
<p>Apollo, Clay, and some email finders include verification. Usually less rigorous than standalone verifiers. Good as first pass, but double-check with standalone for important campaigns.</p>

<h3>Built into cold email tools</h3>
<p>Instantly, Smartlead have built-in verification. Convenient, quality varies.</p>

<h2>The verification workflow</h2>
<ol>
  <li>Extract emails from your data source</li>
  <li>Run through a dedicated verifier (ZeroBounce or similar)</li>
  <li>Keep only "valid" results</li>
  <li>Optionally include "catch-all" if you're okay with higher bounce risk</li>
  <li>Drop "invalid," "unknown," "risky"</li>
  <li>Upload to cold email tool</li>
</ol>

<h2>The catch-all problem</h2>
<p>Some domains accept all email regardless of whether the specific address exists. Verifiers can't tell which specific addresses at catch-alls are real.</p>

<p>Options:</p>
<ul>
  <li>Include catch-alls, accept slightly higher bounce rate</li>
  <li>Exclude all catch-alls (safer but you lose coverage)</li>
  <li>Use advanced verifiers that score catch-all likelihood</li>
</ul>

<p>Pragmatic: include catch-alls for large corporate domains (likely real if pattern matches company convention), exclude for unknown small-domain catch-alls.</p>

<h2>Cost structure</h2>
<ul>
  <li>ZeroBounce: $16 per 10K addresses</li>
  <li>NeverBounce: $8 per 10K</li>
  <li>Million Verifier: $6 per 10K</li>
  <li>Bouncer: $7 per 10K</li>
</ul>

<p>At scale (100K+ addresses/month), sub-$100/month easily. Cheap insurance against reputation damage.</p>

<h2>List hygiene beyond verification</h2>

<h3>Dedupe</h3>
<p>Same person may appear multiple times across exports. Dedupe by email.</p>

<h3>Remove existing contacts</h3>
<p>Current customers, existing relationships, past positive replies should not be in cold lists.</p>

<h3>Remove unsubscribes</h3>
<p>Global DNC list applied before every campaign send.</p>

<h3>Remove bounced addresses from prior campaigns</h3>
<p>Don't re-bounce. If an address bounced once, it stays invalid until you have reason to think it changed.</p>

<h3>Remove role-based addresses if strict</h3>
<p>info@, sales@, contact@ - these get more spam complaints than personal addresses. Include only if specifically targeting that role.</p>

<h3>Remove irrelevant titles</h3>
<p>If the title doesn't match your ICP, remove. Sending to "intern" or "analyst" when your ICP is "VP" wastes volume.</p>

<h2>Staleness</h2>
<p>Addresses verified 6 months ago may now be invalid. People change jobs. Domains close. Re-verify high-value lists quarterly or before major campaigns.</p>

<h2>The verification-first discipline</h2>
<p>Never upload a list to a sending tool without running verification first. Even lists from Apollo or ZoomInfo. Even "verified" lists from Clay. Fresh verification before every campaign is cheap and protects the infrastructure.</p>

<h2>Monitoring bounce rate</h2>
<p>Watch bounce rate per campaign in the sending tool. Rules:</p>
<ul>
  <li>Over 3%: pause campaign, re-verify remaining list</li>
  <li>Over 5%: immediately stop, investigate, all future campaigns paused until resolved</li>
</ul>

<p>Don't continue campaigns with high bounce rates hoping it improves. It won't, and the damage compounds.</p>

<h2>The data source quality check</h2>
<p>If a data source consistently produces high bounce rates even after verification, that source is unreliable. Switch or stop using it.</p>

<p>Over time you build intuition: "Apollo accuracy for X segment is poor," "Clay+LinkedIn for Y segment is excellent." Use the right source for each segment.</p>

<p style="margin-top:40px;">Next: <a href="intent-signals.html">Intent signals</a>.</p>
""",
    prev=("Clay and enrichment", "clay.html"),
    nxt=("Intent signals", "intent-signals.html"),
)


write_cold_page(
    slug="lists/intent-signals",
    title="Intent signals",
    description="Most cold email goes to people who aren't thinking about your category. Intent signals help you find the few who are - and they convert 5-10x better.",
    reading_time=4,
    body_html="""
<p class="lede">A cold list of 10,000 people in your ICP has maybe 200 people actively thinking about your category right now. The other 9,800 aren't wrong - they're just not in-market. Intent signals help you find the in-market 200 before the competition does. It's the highest-leverage targeting upgrade available.</p>

<h2>What counts as intent</h2>
<p>Any observable event that suggests a prospect is thinking about the problem you solve. Categories:</p>

<h3>Hiring signals</h3>
<ul>
  <li>Hiring a VP Sales → pipeline / sales tech needs likely</li>
  <li>Hiring a Head of Marketing → martech decisions coming</li>
  <li>Hiring engineers with specific stack expertise → they may need tools in that stack</li>
  <li>Recent executive hire → new leader making decisions, fresh priorities</li>
</ul>

<h3>Funding signals</h3>
<ul>
  <li>Series A/B/C raised in last 90 days → budget released, hiring + tools</li>
  <li>Specific round sizes that signal specific stages</li>
</ul>

<h3>Technology signals</h3>
<ul>
  <li>Just added tool X → needs complementary tools (BuiltWith, Wappalyzer data)</li>
  <li>Just removed tool Y → evaluating alternatives</li>
  <li>Job postings listing specific tools → commitment to a stack</li>
</ul>

<h3>Content / research signals</h3>
<ul>
  <li>Looking at review sites (G2, Capterra) - Bombora, G2 data</li>
  <li>Downloading research about your category</li>
  <li>Attending industry events / webinars</li>
</ul>

<h3>Public signals</h3>
<ul>
  <li>Launch announcements</li>
  <li>Press coverage</li>
  <li>Quarterly earnings mentioning pain points</li>
  <li>Job postings mentioning specific metrics they want to improve</li>
</ul>

<h3>Behavioral signals on your site</h3>
<ul>
  <li>Visited pricing page</li>
  <li>Downloaded content</li>
  <li>Signed up for newsletter</li>
  <li>Visited from specific company domain (IP-based, tools like Clearbit Reveal)</li>
</ul>

<h2>Where to get signals</h2>

<h3>Public web</h3>
<p>Job boards (scrape or API), press releases, Crunchbase, LinkedIn activity, company websites. Free but manual or scripted.</p>

<h3>Commercial intent data</h3>
<ul>
  <li><strong>Bombora</strong>: B2B intent surges based on content consumption</li>
  <li><strong>G2 Buyer Intent</strong>: who's researching specific tools on G2</li>
  <li><strong>6sense</strong>: account-based intent and engagement</li>
  <li><strong>Demandbase</strong>: similar, enterprise ABM focus</li>
</ul>

<h3>Platform-specific</h3>
<ul>
  <li>LinkedIn activity (posts, engagement)</li>
  <li>Twitter/X mentions</li>
  <li>Reddit / forum discussions</li>
</ul>

<h3>Tooling that packages signals</h3>
<p>Clay pulls many of these together. Userled, Common Room, Koala compile signals for you.</p>

<h2>How to act on signals</h2>

<h3>Signal-triggered outreach</h3>
<p>Instead of blast campaigns to the whole ICP, build automations:</p>
<ol>
  <li>Monitor signal source (job board, funding news, tool change)</li>
  <li>When a company matches your ICP + shows signal, auto-add to outreach</li>
  <li>Reference the signal in the first line</li>
</ol>

<p>Example:</p>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Generic cold opener:</strong> "Saw you're VP of Sales at Acme. Thought I'd reach out about our pipeline tool."<br><br>
<strong>Signal-triggered opener:</strong> "Saw you posted a VP Sales role last week. Usually when companies expand sales leadership, there's pipeline pressure. Here's how [similar company] handled the exact same moment."
</blockquote>

<p>The second gets dramatically higher reply rates because it's timely and relevant.</p>

<h2>The signal quality hierarchy</h2>
<p>From strongest to weakest:</p>
<ol>
  <li><strong>Direct behavior on your site</strong>: visited pricing 3 times in a week = hot</li>
  <li><strong>G2 / review site research</strong>: actively comparing tools</li>
  <li><strong>Specific role hiring</strong>: named function expansion</li>
  <li><strong>Funding + strategic announcement</strong>: money + intent</li>
  <li><strong>Tech stack changes</strong>: specific dependency triggers</li>
  <li><strong>Generic company growth signals</strong>: hiring, press, etc.</li>
</ol>

<p>Top-tier signals are ~5-10x higher conversion. Bottom-tier still better than pure cold ICP filter.</p>

<h2>Signal-based sequence pacing</h2>
<p>Hot signals (top 2-3 tiers): email immediately, keep sequence tight (3-4 touches over 7-10 days). The window closes fast.</p>

<p>Warmer signals (4-6 tiers): normal sequence pacing (5-7 touches over 14-21 days).</p>

<h2>Common mistakes</h2>

<h3>Signal without relevance</h3>
<p>"I saw you got funded" → "Anyway, let me pitch my generic tool." The signal opens the door; the offer still has to match.</p>

<h3>Stale signals</h3>
<p>Funding news from 8 months ago isn't a signal anymore. Time-bound signal reach. Usually 30-90 day window.</p>

<h3>Too many signal categories at once</h3>
<p>Building "perfect" signal-triggered automations for 10 different signal types at once. Start with one or two that matter most. Scale from there.</p>

<h3>Ignoring signals that don't fit tools</h3>
<p>The best signal might not be in any commercial database - it might be a specific event in your industry. Build monitors (Google Alerts, RSS feeds, custom scrapers) for the signals no one else is watching.</p>

<h2>The quality-over-quantity shift</h2>
<p>Traditional cold email: 5,000 emails/week to a broad ICP.<br>
Signal-based: 500 emails/week to prospects with active signals.</p>

<p>Same or better pipeline, lower volume, much higher reputation, less infrastructure needed. This is where advanced cold operators are heading.</p>

<p style="margin-top:40px;">Next: <a href="segmentation.html">Segmentation strategy</a>.</p>
""",
    prev=("Verification + hygiene", "verification.html"),
    nxt=("Segmentation strategy", "segmentation.html"),
)


write_cold_page(
    slug="lists/segmentation",
    title="Segmentation strategy",
    description="One list isn't a strategy. Segmenting by ICP, intent, role, and stage produces campaigns that actually convert.",
    reading_time=4,
    body_html="""
<p class="lede">A single 10,000-person list with one email template will underperform. Segmentation splits the list into smaller groups, each with tailored copy. More work, dramatically better conversion. Most cold email operations leave 2-5x pipeline on the table by running one campaign where five would work.</p>

<h2>The segmentation dimensions</h2>

<h3>By ICP</h3>
<p>If you have multiple ICPs, each gets its own campaign. VP Sales and Founder need different angles.</p>

<h3>By company size</h3>
<ul>
  <li>Small (under 50 employees): founder-driven, fast decisions, budget constrained</li>
  <li>Mid-market (50-500): role-specific buyers, longer cycles</li>
  <li>Enterprise (500+): procurement involvement, multi-stakeholder, very long cycles</li>
</ul>

<p>Same product, three different conversations.</p>

<h3>By role</h3>
<p>Within a company, the VP Sales, CMO, and CFO all care about your product for different reasons. Separate campaigns, different value props.</p>

<h3>By vertical / industry</h3>
<p>Language, pain points, and objections vary by industry. Case studies land when they come from their own industry.</p>

<h3>By geography</h3>
<p>Time zones, business hours, cultural norms. Don't send Monday morning US emails to Europe (it's afternoon there and they have different cadence expectations).</p>

<h3>By intent signal</h3>
<p>Hot signal prospects get a different sequence than cold prospects (see <a href="intent-signals.html">intent signals</a>).</p>

<h3>By source</h3>
<p>Prospects from G2 Buyer Intent vs prospects from LinkedIn Nav search behave differently. Different sequences.</p>

<h3>By prior engagement</h3>
<ul>
  <li>Never contacted: full new sequence</li>
  <li>Contacted but no reply 6+ months ago: re-engagement sequence</li>
  <li>Replied but didn't close: opportunity re-warming</li>
  <li>Became customer: suppress from prospecting</li>
</ul>

<h2>The multi-campaign architecture</h2>
<p>A mature cold email operation runs 5-15 active campaigns simultaneously, each targeting a specific segment. Example:</p>

<ul>
  <li>Campaign A: VP Sales at 100-500 person B2B SaaS (ICP 1)</li>
  <li>Campaign B: Founder at under-50-person B2B SaaS (ICP 2)</li>
  <li>Campaign C: Any ICP 1 prospect with recent hiring signal</li>
  <li>Campaign D: Any ICP 2 prospect with recent funding signal</li>
  <li>Campaign E: ICP 1 prospects we contacted 6 months ago (re-engagement)</li>
  <li>Campaign F: Enterprise (500+) CROs (separate ICP 3)</li>
</ul>

<p>Each has tailored copy, custom sequence pacing, and segment-specific signals. Aggregate volume across all campaigns matches infrastructure capacity.</p>

<h2>The copy implications</h2>
<p>Segmentation without different copy is cosmetic. Each segment needs:</p>
<ul>
  <li>A subject line that pattern-matches their situation</li>
  <li>A first line referencing something specific to them</li>
  <li>An offer / value prop framed in their language</li>
  <li>Proof / case study from their segment</li>
  <li>A CTA sized for their decision cycle</li>
</ul>

<p>If your segments all use the same template with different tokens, you're not really segmenting.</p>

<h2>Managing segmentation overhead</h2>
<p>Running 10 campaigns is more work than running 1. Scaling tactics:</p>

<h3>Shared spine, variable specifics</h3>
<p>Use a base sequence template (3-5 touches, standard pacing). Variables: subject lines, first lines, pitch paragraphs - customized per segment.</p>

<h3>Campaign templates</h3>
<p>Once you've built one campaign for a segment, new campaigns for similar segments start from that template and modify.</p>

<h3>Automation of segment assignment</h3>
<p>Clay or similar tools can route new prospects into the right campaign automatically based on their attributes. No manual sorting.</p>

<h3>Measurement infrastructure</h3>
<p>With 10 campaigns, you need per-campaign metrics (reply rate, positive reply rate, cost per meeting). Dashboard these.</p>

<h2>The "seed and scale" pattern</h2>
<ol>
  <li>Pick one specific segment</li>
  <li>Build one campaign against it</li>
  <li>Iterate copy until positive reply rate is strong</li>
  <li>Scale that segment</li>
  <li>Pick the next segment, start over</li>
  <li>After 6 months, you have 5-8 tuned campaigns running</li>
</ol>

<p>This beats "let's launch 10 campaigns simultaneously." Sequential seeding lets you focus and actually optimize each.</p>

<h2>Anti-patterns</h2>

<h3>Over-segmentation</h3>
<p>50 segments, each with a tiny list. Too fragmented to optimize individual segments. Consolidate related segments.</p>

<h3>Under-segmentation</h3>
<p>One campaign for "all B2B companies." Copy can't be specific enough to convert.</p>

<h3>Static segments</h3>
<p>Prospects never move between segments even as their situation changes. Build re-segmentation logic for when prospects change jobs or companies.</p>

<h3>Segmentation without measurement</h3>
<p>Running 5 campaigns without tracking per-campaign performance. You can't tell which are working.</p>

<h2>The advanced segmentation: cohort-based</h2>
<p>At scale, treat each monthly batch of prospects as a cohort. Measure:</p>
<ul>
  <li>How cohorts convert over time (do old cohorts re-engage?)</li>
  <li>Whether newer cohorts convert better (signal that ICP or copy improved)</li>
  <li>Cohort LTV once they become customers</li>
</ul>

<p>This is enterprise-level analytics. Most teams don't need it. But it's the path to continuously improving a mature cold operation.</p>

<h2>The "start simple" recipe</h2>
<p>If you're starting cold email:</p>
<ol>
  <li>One ICP, one campaign</li>
  <li>Run for 4-6 weeks, iterate</li>
  <li>Add a second ICP or a signal-triggered variant</li>
  <li>Run both for another month</li>
  <li>Continue expanding</li>
</ol>

<p>Don't start with 10 campaigns on day 1. Start with 1. Grow.</p>

<p style="margin-top:40px;">Next: <a href="../copy/anatomy.html">Cold email anatomy</a>.</p>
""",
    prev=("Intent signals", "intent-signals.html"),
    nxt=("Cold email anatomy", "../copy/anatomy.html"),
)

print("\n✓ Cold Email Part 2: Lists (6 pages)")
