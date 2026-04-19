#!/usr/bin/env python3
"""Direct Response — Lead Generation + Sales Letters (10 pages)."""
from _build_drm import write_drm_page


# ============================================================
# LEAD GENERATION (5 pages)
# ============================================================

write_drm_page(
    slug="leads/core-four",
    title="The core four",
    description="Hormozi's core four: the four categories of lead generation that cover nearly every possible way to get a lead. Master all four and the 'where do we find customers' problem is solved.",
    reading_time=7,
    body_html="""
<p class="lede">Alex Hormozi's core four is the cleanest map of lead generation anyone has drawn. It divides every possible way to get a lead into four categories — and the categories are exhaustive. Learn all four. Pick your primary. Pick your second. Operate them both as disciplines. You will never again have the "where do we get customers" problem.</p>

<h2>The matrix</h2>
<p>Two dimensions. Two levels each. Four quadrants.</p>
<ul>
  <li><strong>Dimension 1:</strong> How many people you're reaching — one at a time, or one-to-many.</li>
  <li><strong>Dimension 2:</strong> Warm (they know you) vs. cold (they don't).</li>
</ul>

<pre style="background:#f5f5f7; padding:16px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:12px;">
                WARM                         COLD
               ┌────────────────────────┬────────────────────────┐
ONE-TO-ONE     │  1. Warm outreach       │  3. Cold outreach     │
               │  (people you know)      │  (cold DMs, cold      │
               │                         │   email, cold calls)  │
               ├────────────────────────┼────────────────────────┤
ONE-TO-MANY    │  2. Content            │  4. Paid ads           │
               │  (posts to your        │  (ads on platforms     │
               │   audience)            │   to strangers)        │
               └────────────────────────┴────────────────────────┘
</pre>

<h2>Quadrant 1 — Warm outreach</h2>
<p>Reach out one-to-one to people who already know you. Friends, family, past colleagues, LinkedIn connections, past customers, people who've attended your events.</p>
<ul>
  <li><strong>Cost:</strong> free (time only)</li>
  <li><strong>Speed:</strong> fast — responses in hours</li>
  <li><strong>Conversion rate:</strong> highest of any channel</li>
  <li><strong>Scale ceiling:</strong> limited by your network size</li>
  <li><strong>Best for:</strong> new businesses, testing new offers, early validation</li>
</ul>
<p>Most founders underuse this because it feels embarrassing. The embarrassment is the cost, and it's small compared to the revenue generated. See <a href="warm-outreach.html">warm outreach</a>.</p>

<h2>Quadrant 2 — Content (one-to-many, warm)</h2>
<p>Post content to audiences that follow you — newsletter, LinkedIn posts, podcast, YouTube, Twitter, blog. The audience has opted in to hear from you.</p>
<ul>
  <li><strong>Cost:</strong> time + sometimes production cost</li>
  <li><strong>Speed:</strong> slow to build; compounds over years</li>
  <li><strong>Conversion rate:</strong> medium (depends on trust built)</li>
  <li><strong>Scale ceiling:</strong> very high; top creators reach millions</li>
  <li><strong>Best for:</strong> authority-based businesses, long-term brand, recurring customer acquisition</li>
</ul>
<p>Content is the most leveraged of the four quadrants — once it exists, it can be consumed infinitely without more work — but takes the longest to start paying.</p>

<h2>Quadrant 3 — Cold outreach (one-to-one, cold)</h2>
<p>Contact people you don't know. Cold email, cold DMs, cold calls, prospecting LinkedIn messages.</p>
<ul>
  <li><strong>Cost:</strong> low dollar, high time (or tooling/VA cost)</li>
  <li><strong>Speed:</strong> fast — responses in days</li>
  <li><strong>Conversion rate:</strong> low but compounds with volume and targeting</li>
  <li><strong>Scale ceiling:</strong> high; can reach tens of thousands per week</li>
  <li><strong>Best for:</strong> B2B, high-ticket offers, niche targeting</li>
</ul>
<p>Cold outreach is most operators' second-best channel after warm outreach — faster to start than content, more predictable than paid. See <a href="cold-outreach.html">cold outreach</a>.</p>

<h2>Quadrant 4 — Paid ads (one-to-many, cold)</h2>
<p>Facebook, Instagram, Google, YouTube, TikTok, LinkedIn — pay to put your message in front of strangers.</p>
<ul>
  <li><strong>Cost:</strong> dollars, often significant</li>
  <li><strong>Speed:</strong> fast — traffic in hours</li>
  <li><strong>Conversion rate:</strong> variable; dependent on creative, offer, and targeting</li>
  <li><strong>Scale ceiling:</strong> enormous; the biggest channel when it works</li>
  <li><strong>Best for:</strong> validated offers, predictable unit economics, scale</li>
</ul>
<p>Paid ads are most effective <em>after</em> the other three have proven the offer converts. Running ads with an unvalidated offer is lighting money on fire.</p>

<h2>The sequence — why you shouldn't start with paid</h2>
<p>Most founders jump to paid ads first because they feel like "real marketing." This is almost always a mistake. The correct progression:</p>
<ol>
  <li><strong>Warm outreach</strong> — validate the offer with people who give you honest feedback</li>
  <li><strong>Cold outreach</strong> — test whether the offer works with strangers in your ICP</li>
  <li><strong>Content</strong> — start building long-term leverage (even if it pays off in year 2)</li>
  <li><strong>Paid ads</strong> — once unit economics are proven, scale with dollars</li>
</ol>

<h2>Each quadrant amplifies the others</h2>
<p>When all four run together:</p>
<ul>
  <li>Warm outreach generates testimonials → used in content</li>
  <li>Content builds trust → makes cold outreach warmer</li>
  <li>Cold outreach produces data → informs paid ad targeting and copy</li>
  <li>Paid ads drive audience → that audience consumes content → cold outreach converts them</li>
</ul>

<h2>The rule of 100</h2>
<p>Hormozi's discipline: do 100 units of one of these per day for 100 days before you judge whether it works.</p>
<ul>
  <li>100 warm outreach messages</li>
  <li>100 cold emails</li>
  <li>1 piece of content (100 over 100 days)</li>
  <li>$100/day in ads (or 100 creatives tested)</li>
</ul>
<p>Most channels fail not because the channel doesn't work but because the operator doesn't operate the channel long enough or with enough volume. The rule of 100 kills that excuse.</p>

<h2>How to pick your primary</h2>
<ol>
  <li><strong>What's your current asset?</strong> If you have a network, warm outreach. If you have a voice, content. If you have money, paid. If you have time, cold outreach.</li>
  <li><strong>What does your ICP do?</strong> B2B enterprise = cold outreach + content. B2C impulse = paid. Services = warm + content.</li>
  <li><strong>What's your timeline?</strong> Need revenue in 30 days = warm + cold outreach. Building for year 2+ = content + paid.</li>
  <li><strong>What will you actually do?</strong> The best channel is the one you'll run disciplined. A "perfect" channel you won't execute is worse than a mediocre one you will.</li>
</ol>

<h2>The mature setup — running all four</h2>
<p>A fully-operating business runs all four at different scales:</p>
<ul>
  <li>1 FTE doing warm outreach + personal network (CEO, founder, top AE)</li>
  <li>Content engine producing 1–5 pieces per week</li>
  <li>Cold outreach team running 500–5000+ messages per week</li>
  <li>Paid team managing CAC and creative against LTV</li>
</ul>
<p>Early, you can only run one. By year 2 you should have two. By year 3 you should have three or four. This is the gradient.</p>

<p style="margin-top:40px;">Related: <a href="lead-magnets.html">Lead magnets</a> · <a href="warm-outreach.html">Warm outreach</a> · <a href="cold-outreach.html">Cold outreach</a> · <a href="paid-ads.html">Paid ads</a></p>
""",
    prev=("Fascination bullets", "../copy/bullets.html"),
    nxt=("Lead magnets", "lead-magnets.html"),
)


write_drm_page(
    slug="leads/lead-magnets",
    title="Lead magnets",
    description="A lead magnet is what turns a stranger into a lead. The best ones are hyper-specific, deliver a concrete outcome, and pre-qualify the prospect for what comes next.",
    reading_time=6,
    body_html="""
<p class="lede">A lead magnet is the free thing you offer in exchange for contact information. Done right, it turns a stranger into a qualified lead while simultaneously demonstrating that you know what you're doing. Done wrong, it fills your list with tire-kickers who will never buy.</p>

<h2>The four jobs of a lead magnet</h2>
<ol>
  <li><strong>Attract the right person.</strong> Qualify by specificity — the prospect only wants it if they fit the ICP.</li>
  <li><strong>Deliver concrete value.</strong> Usable, specific, and better than they expected for free.</li>
  <li><strong>Pre-sell the mechanism.</strong> Demonstrate that your approach works — prime them for the paid offer.</li>
  <li><strong>Start a conversation.</strong> Provide a natural transition to the next step.</li>
</ol>

<h2>Lead magnet formats</h2>

<h3>The checklist / cheat sheet</h3>
<p>One page, high density. "The 14-point checklist for launching a paid ads campaign in 2026." Fast to create, fast to consume, easy to title. High perceived value relative to effort.</p>

<h3>The template / swipe file</h3>
<p>Directly usable. "The exact cold email template we used to book 240 demos." Readers love these because the outcome is immediately applicable.</p>

<h3>The toolkit / kit</h3>
<p>Multiple artifacts bundled. "The onboarding kit: email templates, first-30-days playbook, and Notion database." High perceived value because it's a bundle.</p>

<h3>The guide / mini-course</h3>
<p>Longer-form. Video course, PDF, email series. Requires more consumption effort from the prospect — but also filters for more-committed leads.</p>

<h3>The assessment / audit</h3>
<p>Interactive. Prospect inputs data, gets a personalized result. "Take the 5-minute funnel audit." Highest engagement but requires tooling.</p>

<h3>The calculator / tool</h3>
<p>A simple interactive tool that produces an answer. "Our CAC-payback calculator." Works for life — people come back to use it. High SEO value.</p>

<h3>The case study</h3>
<p>A specific, detailed story of a customer outcome. "How we took [client] from $1M to $8M in 14 months." Works well for high-ticket services.</p>

<h3>The free trial / tier</h3>
<p>For SaaS. Free access to a core feature. The most "hands-on" form of lead magnet.</p>

<h3>The free consultation / audit call</h3>
<p>A 15–30 minute call with you or your team. Highest qualification, lowest volume. Works for high-ticket.</p>

<h2>The specificity principle</h2>
<p>Generic magnets attract generic leads. Specific magnets attract specific leads who fit your ICP.</p>
<ul>
  <li>Weak: "Marketing tips for entrepreneurs"</li>
  <li>Strong: "The 8-email sequence we send to every new ecommerce signup (and why open rates stay above 60%)"</li>
</ul>
<p>The right prospect reads the strong version and says "that's exactly what I need." The wrong prospect scrolls past. Both outcomes are wins.</p>

<h2>Format guidelines</h2>
<ul>
  <li><strong>Consumable in under 15 minutes.</strong> Longer lead magnets have lower consumption rates. Low consumption = low engagement = low conversion downstream.</li>
  <li><strong>Specific outcome.</strong> By the end, the reader has accomplished something concrete.</li>
  <li><strong>Ship quality.</strong> A sloppy lead magnet is worse than none — it tells prospects your paid product is sloppy too.</li>
  <li><strong>Designed well enough.</strong> Doesn't have to be gorgeous. Does have to not look like a Word doc from 1998.</li>
  <li><strong>Ends with a clear next step.</strong> Not "contact us" — a specific offer or invitation.</li>
</ul>

<h2>The landing page</h2>
<p>A lead magnet needs a single-purpose landing page. Structure:</p>
<ol>
  <li>Headline — what they'll get (benefit, not title)</li>
  <li>Subhead — who it's for + why it matters</li>
  <li>Bullet list of what's inside (5–10 specifics)</li>
  <li>Social proof (testimonials, download count, logos)</li>
  <li>Form (minimal — email, maybe one more field)</li>
  <li>Button (CTA with specific outcome)</li>
</ol>
<p>That's it. No menu bar, no footer with 12 links, no distractions. One page, one decision.</p>

<h2>The form length</h2>
<p>Every field drops conversion:</p>
<ul>
  <li>Email only — highest conversion, lowest lead quality</li>
  <li>Email + first name — slight drop, slight lead-quality improvement</li>
  <li>Email + name + company + role — significant drop, qualified leads</li>
  <li>Email + name + company + role + team size + "what are you trying to solve" — low conversion, highly qualified leads</li>
</ul>
<p>Match form length to downstream need. If your next step is a $100 product, take just email. If your next step is a $50K consulting engagement, qualify heavily on the form.</p>

<h2>What happens after they download</h2>
<p>This is where most lead magnets fail. Download → silence → cold lead in 90 days.</p>
<p>The correct flow:</p>
<ol>
  <li>Instant delivery — the magnet in their inbox or on-screen within seconds</li>
  <li>"Thank you" page with a specific next step — watch a video, book a call, consume a related piece of content</li>
  <li>Email 1 (within the hour): personal tone, congratulating them for taking the step, reinforcing the value of the magnet</li>
  <li>Email 2–6 over the next 1–2 weeks: see <a href="../followup/email-sequences.html">email sequences</a></li>
  <li>Email 7+: start segmenting by engagement — hot leads get offer; cold leads get more education</li>
</ol>

<h2>Measurement</h2>
<ul>
  <li><strong>Conversion rate</strong> of landing page (10–30% typical for cold traffic; 30–50%+ for warm)</li>
  <li><strong>Consumption rate</strong> — % who actually opened/watched/read</li>
  <li><strong>Email sequence engagement</strong> — opens, clicks over the first 14 days</li>
  <li><strong>Conversion to paid</strong> — % of leads who buy within 30, 60, 90 days</li>
  <li><strong>LTV of leads from this magnet</strong> — not all lead sources produce equal customers</li>
</ul>
<p>The number that matters is the last one. A lead magnet with 50% download conversion but 0.5% purchase conversion is worse than one with 25% download and 3% purchase.</p>

<h2>When to retire a lead magnet</h2>
<ul>
  <li>Conversion rate declining month-over-month for 3+ months</li>
  <li>Consumption rate dropping (content feels stale)</li>
  <li>Your ICP or offer has materially shifted</li>
  <li>A new magnet has proven higher downstream conversion</li>
</ul>
<p>Treat lead magnets like any other creative — test new ones, rotate out dying ones.</p>

<p style="margin-top:40px;">Related: <a href="core-four.html">The core four</a> · <a href="../followup/email-sequences.html">Email sequences</a> · <a href="../copy/the-stack.html">The copywriting stack</a></p>
""",
    prev=("The core four", "core-four.html"),
    nxt=("Warm outreach", "warm-outreach.html"),
)


write_drm_page(
    slug="leads/warm-outreach",
    title="Warm outreach",
    description="Warm outreach is the fastest way to revenue and the most overlooked. Every founder has a network. Most refuse to use it. Here's how to do warm outreach without being weird.",
    reading_time=6,
    body_html="""
<p class="lede">Warm outreach is the fastest way to revenue and the most overlooked of Hormozi's core four. Every founder has a network. Most refuse to use it because asking feels embarrassing. The embarrassment is the cost; the revenue is the return. The math is always worth it.</p>

<h2>What warm outreach is</h2>
<p>One-to-one contact with people who already know you — directly, or through a shared connection strong enough to make the conversation natural. Not cold DMs. Not mass emails to your list. Individual, personal, context-specific messages to specific humans.</p>

<h2>Who's in your warm network</h2>
<p>More than you think. Before you write anyone off as "not relevant":</p>
<ul>
  <li>Current and former colleagues</li>
  <li>Current and former classmates</li>
  <li>Former customers (from this or a past business)</li>
  <li>People who attended your events / podcast / course / webinar</li>
  <li>LinkedIn first-degree connections you've actually interacted with</li>
  <li>Past investors / advisors / mentors</li>
  <li>Past vendors or partners</li>
  <li>Friends + family in adjacent industries</li>
  <li>People who've replied to your content</li>
  <li>People who've introduced themselves at conferences</li>
</ul>
<p>Typical founder warm list after real audit: 300–1500 people.</p>

<h2>The segmentation</h2>
<p>Not every warm contact gets the same message. Segment into three groups:</p>

<h3>Tier 1 — Close connections</h3>
<p>People who would answer the phone if you called. They already trust you. The message is personal, contextual, and asks directly: "Here's what I'm building. Does this sound like it'd help you? Would you know 3 people I should talk to?"</p>

<h3>Tier 2 — Familiar acquaintances</h3>
<p>People who know your name but you haven't spoken to recently. The message reconnects first: "Hey — I know it's been a while. Saw [specific thing they did]. Wanted to catch up and also get your take on [specific thing]." Rebuild connection before you ask.</p>

<h3>Tier 3 — Distant weak ties</h3>
<p>People who'd recognize you but haven't thought about you in years. Highest volume, lowest individual yield. Can be semi-templated but still personalized at the opening.</p>

<h2>The anti-templates</h2>
<p>Warm outreach fails the moment it feels templated. Avoid:</p>
<ul>
  <li>"Hope this finds you well" (doesn't sound like you, reads as mass)</li>
  <li>"I wanted to reach out about…" (passive, corporate)</li>
  <li>"Quick question" when the question isn't quick</li>
  <li>"I'd love to get your thoughts" when you want them to buy</li>
  <li>Immediately pitching in sentence one</li>
  <li>A long wind-up before the ask</li>
</ul>

<h2>The warm outreach structure</h2>

<h3>1. Personal opening (one specific line)</h3>
<p>Reference something real — a recent post, a shared project, a memory, their current role. One line, specific to them.</p>

<h3>2. Context (what you're doing)</h3>
<p>Two sentences max. What you're building / doing, why it might be relevant to them.</p>

<h3>3. The ask</h3>
<p>One clear ask. The three most useful:</p>
<ul>
  <li>"Does this sound like something you'd use?" (direct sales conversation)</li>
  <li>"Who do you know who has this problem?" (referrals)</li>
  <li>"Would you have 20 minutes to chat?" (relationship build)</li>
</ul>

<h3>4. Easy out</h3>
<p>"No worries if it's not a fit — just thought of you." Preserves the relationship regardless of response.</p>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Example — Tier 1 message</strong><br><br>
"Hey Mike — saw your post about hiring a second AE, nice. Finally ready for that.<br><br>
Quick update: I've been heads-down on something for the last 6 months. Software that tells operations teams which customers are about to churn 45 days before they do. A couple of SaaS founders have found it useful.<br><br>
Does anyone at [his company] own retention/expansion? Not trying to pitch you — mostly just wondering if this is a conversation for you or if I should point you at someone else. Happy to share the 3-minute demo either way.<br><br>
— Sam"
</blockquote>

<h2>The volume</h2>
<p>Warm outreach is a campaign, not a one-off. Plan:</p>
<ul>
  <li>Week 1: 50 Tier 1 messages</li>
  <li>Week 2: 100 Tier 2 messages</li>
  <li>Week 3: 200 Tier 3 messages</li>
  <li>Ongoing: reactivate Tier 1 quarterly, Tier 2 every 6 months</li>
</ul>
<p>Conversion: typical warm outreach converts to a meeting at 15–35% and to a sale at 5–20%. A 500-person warm outreach campaign typically produces 20–80 meetings and 5–30 sales.</p>

<h2>The asks that don't work</h2>
<ul>
  <li>"Can I pick your brain?" — no one likes this. Replace with a specific question.</li>
  <li>"Would you give me feedback on X?" — feels like free labor. Replace with trade ("20 min for 20 min").</li>
  <li>"Can you introduce me to anyone?" — too vague. Give specifics: "anyone who runs a team of 10+ reps?"</li>
  <li>"Just reaching out to say hi" — performative. Either have a real reason or don't message.</li>
</ul>

<h2>The asks that do work</h2>
<ul>
  <li>"Would the X you're dealing with at [company] improve if Y were solved?" — direct, specific</li>
  <li>"Worth 20 minutes on Zoom to compare notes?" — low-friction, mutual</li>
  <li>"Who's one person I should talk to this week?" — small, concrete ask</li>
  <li>"I built X to solve [their likely pain]. Want to see it?" — if you know they have the pain</li>
</ul>

<h2>The follow-up</h2>
<p>Most responses to warm outreach come to the second or third message. Rules:</p>
<ul>
  <li>Wait 5–7 days before nudge</li>
  <li>Nudge once; accept silence as a no</li>
  <li>Never guilt-trip ("just bumping this up")</li>
  <li>If they respond "not now" — schedule a reminder for 60–90 days later</li>
</ul>

<h2>The compounding effect</h2>
<p>Every warm outreach message does three things: tests the pitch, generates data on market resonance, and creates future referrals. Even the ones that don't convert today move relationships forward. This is why founders who do warm outreach for 90 days often see results continuing to roll in at month 6 and 12.</p>

<p style="margin-top:40px;">Related: <a href="core-four.html">The core four</a> · <a href="cold-outreach.html">Cold outreach</a> · <a href="lead-magnets.html">Lead magnets</a></p>
""",
    prev=("Lead magnets", "lead-magnets.html"),
    nxt=("Cold outreach", "cold-outreach.html"),
)


write_drm_page(
    slug="leads/cold-outreach",
    title="Cold outreach",
    description="Cold email, cold DMs, cold calls. Done right, the most scalable channel for B2B. Done wrong, a way to spend thousands of hours and produce nothing. The difference is in the details.",
    reading_time=8,
    body_html="""
<p class="lede">Cold outreach is the most scalable predictable channel for B2B direct response — when done right. "Done right" is a short list: targeted list, relevant angle, specific offer, tight copy, volume discipline. Most cold outreach fails on one of those five. Each one costs you.</p>

<h2>The four inputs that determine success</h2>
<ol>
  <li><strong>List quality</strong> — are you messaging the right people?</li>
  <li><strong>Relevance</strong> — does the message connect to something they actually care about?</li>
  <li><strong>Offer</strong> — is what you're asking for worth their time?</li>
  <li><strong>Volume + cadence</strong> — are you sending enough, consistently?</li>
</ol>
<p>The copy matters — but it matters 20%. The other 80% is these four.</p>

<h2>List quality</h2>
<p>Bad list = no amount of good copy saves you. A great list can carry mediocre copy to profitability.</p>

<h3>Sources</h3>
<ul>
  <li><strong>Apollo / ZoomInfo / Clay / Seamless</strong> — B2B database tools</li>
  <li><strong>LinkedIn Sales Navigator</strong> — targeted searches by role, company, signals</li>
  <li><strong>Scraped sources</strong> — Crunchbase, industry directories, conference attendee lists</li>
  <li><strong>Intent data</strong> — Bombora, G2, 6sense showing active buying signals</li>
  <li><strong>Community lists</strong> — Slack/Discord groups, past event attendees</li>
</ul>

<h3>Qualification criteria</h3>
<p>Before messaging anyone, they should pass:</p>
<ul>
  <li>In your ICP (role, industry, company size, tech stack)</li>
  <li>Has authority or influence over the decision you want</li>
  <li>Demonstrates signs of having the problem you solve</li>
  <li>Is reachable at the channel you're using</li>
</ul>
<p>A list of 500 qualified prospects outperforms a list of 5,000 unqualified ones every time.</p>

<h2>Relevance — the research layer</h2>
<p>The best cold emails aren't generic. They have one specific, relevant hook drawn from actual research:</p>
<ul>
  <li>A recent funding announcement (they have budget now)</li>
  <li>A specific hire (new VP of Sales = pipeline initiatives)</li>
  <li>A LinkedIn post they made (you've read their thinking)</li>
  <li>A technology they use (you know their stack)</li>
  <li>A competitor they just lost to (this is leverage)</li>
</ul>

<p>Typical research layer:</p>
<ol>
  <li>Pull LinkedIn for their recent activity</li>
  <li>Check company press for signals (funding, hires, product launches)</li>
  <li>Scan their website for their current positioning</li>
  <li>One specific detail surfaces for the opening line</li>
</ol>
<p>Time investment: 3–5 minutes per prospect for high-priority outreach. Tools like Clay can automate most of this.</p>

<h2>The message structure</h2>

<h3>Subject line</h3>
<ul>
  <li>5–7 words, lowercase, personal-sounding</li>
  <li>Question format often works: "quick question on [their project]"</li>
  <li>Specific over clever: "Re: your post on retention"</li>
  <li>Never all caps; never marketing-y</li>
</ul>

<h3>Opening line (personalization)</h3>
<p>One line that proves you've researched them. Specific. Not "Hope you're well."</p>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
"Saw your post yesterday about cutting CAC 40% in Q4 — impressive, especially the part about killing the bottom 3 ad sets."
</blockquote>

<h3>Pivot (relevance)</h3>
<p>Bridge from their situation to what you do. One sentence.</p>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
"We help teams in your spot apply that same cut-the-bottom logic to CS — identifying the 20% of accounts eating 80% of the hours."
</blockquote>

<h3>The proof (brief)</h3>
<p>One line of credibility. A specific result with a specific client.</p>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
"[Client name] used it to reclaim 31 hours/week across their CSM team without changing headcount."
</blockquote>

<h3>The ask (specific)</h3>
<p>One clear next step. Small. Low friction.</p>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
"Worth 15 min to compare notes? Or I can send the 3-slide summary — no call needed."
</blockquote>

<h3>Signature</h3>
<p>Simple. Name, title, one-line context. Not a wall of social links.</p>

<h2>The full example</h2>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Subject:</strong> cutting 80% of CS hours<br><br>
Hey Sara —<br><br>
Saw your post yesterday about cutting CAC 40% in Q4 — especially the part about killing the bottom 3 ad sets. Resonated.<br><br>
We help teams apply that same cut-the-bottom logic to CS — identifying the 20% of accounts eating 80% of the hours. [Client name] used it to reclaim 31 hours/week across their CSM team without changing headcount.<br><br>
Worth 15 min to compare notes? Or I can send the 3-slide summary — no call needed.<br><br>
— Sam<br>
Samuel Ochoa · [role] at [company]
</blockquote>

<h2>The volume math</h2>
<p>Cold outreach is a numbers game, but not random numbers.</p>
<ul>
  <li>Bad targeting, bad copy: 0.1% reply rate. Useless.</li>
  <li>Good targeting, ok copy: 1–2% reply rate. Workable.</li>
  <li>Good targeting, great copy: 5–10% reply rate. Engine.</li>
  <li>Great targeting, great copy, hyper-specific opener: 10–20%. Unicorn.</li>
</ul>
<p>At 5% reply, 30% of replies become meetings, 20% of meetings close: 5% × 30% × 20% = 0.3% prospect-to-customer. Need 333 messages per customer. To close 10/mo, send 3,300/mo.</p>

<h2>The follow-up sequence</h2>
<p>Most responses come after the first message. Rules:</p>
<ul>
  <li>3–5 touches over 2–3 weeks</li>
  <li>Each touch adds value — different angle, different proof point, different ask</li>
  <li>Never guilt-trip ("just bumping this up")</li>
  <li>Clear "break up" email after the last touch: "happy to drop off — just reply 'no' and I'll move on"</li>
</ul>

<h2>Deliverability</h2>
<p>If your emails land in spam, nothing else matters. Protect deliverability:</p>
<ul>
  <li>Use a dedicated outbound domain (e.g., getcompany.co for outbound, company.com for everything else)</li>
  <li>Warm up new domains for 2–4 weeks before high-volume sending</li>
  <li>Keep individual inbox volume under ~30 messages/day</li>
  <li>Avoid spam triggers: image-only emails, heavy HTML, links in first email, marketing phrases</li>
  <li>Use tools (Instantly, Smartlead, Lemlist) that rotate across multiple inboxes</li>
</ul>

<h2>Platforms beyond email</h2>

<h3>LinkedIn DMs</h3>
<p>Lower volume ceiling (InMails are limited) but higher reply rates when the profile looks credible. Good for senior / executive targets.</p>

<h3>Cold calls</h3>
<p>Still extremely effective for certain segments — particularly operational roles, trades, older B2B. Under-used because it feels harder than email.</p>

<h3>Twitter / X DMs</h3>
<p>Works for certain communities (tech, crypto, e-commerce, creators). Public engagement first ("warming up" the DM) outperforms cold.</p>

<h3>Multi-channel sequences</h3>
<p>Top-performing sequences combine channels: email → LinkedIn connection → LinkedIn message → email nudge → call. Reach the same prospect 5 different ways over 3 weeks.</p>

<p style="margin-top:40px;">Related: <a href="core-four.html">The core four</a> · <a href="warm-outreach.html">Warm outreach</a> · <a href="paid-ads.html">Paid ads</a></p>
""",
    prev=("Warm outreach", "warm-outreach.html"),
    nxt=("Paid ads", "paid-ads.html"),
)


write_drm_page(
    slug="leads/paid-ads",
    title="Paid ads",
    description="Paid ads are the scale lever. They're also the fastest way to burn money if the offer isn't validated first. Here's how direct response has always thought about paid — and what changes in 2026.",
    reading_time=7,
    body_html="""
<p class="lede">Paid advertising is the scale lever in direct response — when the offer has been validated through the other three quadrants of the <a href="core-four.html">core four</a>. Run paid before validation and you burn money. Run paid after, and you can scale a profitable unit into a real business in months.</p>

<h2>When paid ads are the right move</h2>
<ul>
  <li>Your offer has converted with warm and cold outreach — you have data on what works</li>
  <li>Your unit economics are known (CAC, LTV, payback period)</li>
  <li>You can afford to run the test (typically $5K–$25K before conclusive data)</li>
  <li>You have bandwidth to iterate creative and landing pages weekly</li>
  <li>Your sales/fulfillment can handle volume if it works</li>
</ul>

<h2>When paid ads are a mistake</h2>
<ul>
  <li>Pre-product-market-fit — you're paying to find out what you should have found free</li>
  <li>Your LTV is under ~3x your likely CAC in the channel</li>
  <li>You don't have conversion tracking set up</li>
  <li>You can't dedicate an operator to creative testing</li>
</ul>

<h2>The core metrics</h2>
<ul>
  <li><strong>CPM</strong> — cost per thousand impressions. Platform / audience priced.</li>
  <li><strong>CTR</strong> — click-through rate. Creative quality proxy.</li>
  <li><strong>CPC</strong> — cost per click. Function of CPM and CTR.</li>
  <li><strong>CVR</strong> — conversion rate. Landing page / offer quality.</li>
  <li><strong>CAC</strong> — cost per acquisition. CPC ÷ CVR.</li>
  <li><strong>ROAS</strong> — return on ad spend. Revenue ÷ spend.</li>
  <li><strong>Payback period</strong> — time to recoup CAC in gross profit.</li>
</ul>
<p>Track all of them. Optimize the one that moves others when it moves.</p>

<h2>The platforms, by use case</h2>

<h3>Meta (Facebook + Instagram)</h3>
<p>Best for: consumer products, info products, services with clear visual hooks. Interruption channel — prospects aren't searching; they're scrolling. Creative-driven; creative fatigue is the main failure mode.</p>

<h3>Google Search</h3>
<p>Best for: high-intent queries, B2B SaaS, local services. Prospect has already named the problem. Higher CPCs but much higher intent.</p>

<h3>YouTube</h3>
<p>Best for: info products, high-ticket services needing storytelling, brand-adjacent video. Long-form selling works. Best for creative-heavy teams.</p>

<h3>TikTok</h3>
<p>Best for: consumer products with visual appeal, creator-led brands. Creative cadence is brutal (weekly at minimum).</p>

<h3>LinkedIn</h3>
<p>Best for: B2B, high-ticket, professional services. High CPMs offset by buyer quality.</p>

<h3>Reddit, Quora, podcast ads, niche publications</h3>
<p>Specialized but powerful when the ICP lives there. Lower volume, higher quality.</p>

<h2>The creative stack</h2>
<p>One ad can't carry the channel. You need:</p>
<ul>
  <li><strong>3–5 hook variants</strong> — different opening promises, different angles</li>
  <li><strong>3–5 creative formats</strong> — video, static, carousel, UGC-style</li>
  <li><strong>Weekly testing cadence</strong> — new creatives every week, winners scaled, losers killed</li>
</ul>
<p>The creative fatigue cycle is real. A winning ad on Meta usually has a 4–12 week shelf life before frequency and CTR decay force new creative.</p>

<h2>The hook-promise-proof-close structure</h2>
<p>Short-form paid ads compress the full stack into 15–60 seconds / 3 paragraphs:</p>
<ol>
  <li><strong>Hook</strong> — pattern interrupt, first 2 seconds. A surprising claim, a specific moment, a face looking at the camera.</li>
  <li><strong>Promise</strong> — what they'll get if they engage. 5–10 seconds.</li>
  <li><strong>Proof</strong> — one specific case or statistic. 10–20 seconds.</li>
  <li><strong>Close</strong> — the CTA. Specific action. 5 seconds.</li>
</ol>

<h2>The landing page</h2>
<p>An ad alone doesn't convert. Ad → landing page → offer. The landing page is where most paid campaigns fail:</p>
<ul>
  <li>Message match — the ad's headline should echo the landing page's headline</li>
  <li>Speed — every second of load time costs conversion</li>
  <li>Mobile-first — most paid traffic is mobile</li>
  <li>Single goal — one CTA, one offer</li>
  <li>Proof density — testimonials, logos, case studies, specific numbers</li>
  <li>Form friction — only the fields you actually need</li>
</ul>

<h2>The testing discipline</h2>
<p>Paid is the ultimate Hopkins territory — everything can and should be tested:</p>
<ol>
  <li>Test one variable at a time: headline OR creative OR landing page, not all three</li>
  <li>Give each test enough budget to reach statistical significance (generally 3,000–5,000 clicks minimum)</li>
  <li>Name a clear winner; kill the loser</li>
  <li>Roll the winner into the control; test a new challenger against it</li>
  <li>Keep a running document of what's been tested and what won</li>
</ol>

<h2>The scaling playbook</h2>
<p>Once you've found a winning ad + landing page + offer:</p>

<h3>Horizontal scale</h3>
<p>Run the same creative on new audiences, new platforms, new geographies. Same creative, new pools of people.</p>

<h3>Vertical scale</h3>
<p>Increase budget on the winning setup. Algorithms punish sudden budget jumps — scale by 20–30% every 2–3 days, not 10x overnight.</p>

<h3>Creative scale</h3>
<p>Produce 10 variations of the winning creative — different hooks, different first frames, different end cards. Rotate them to fight fatigue.</p>

<h3>Funnel optimization</h3>
<p>Once spend is high, small improvements in conversion compound. 5% better landing page conversion = 5% more customers at same CAC. Ruthlessly optimize.</p>

<h2>The attribution problem (2026)</h2>
<p>iOS 14, third-party cookie deprecation, and multi-touch customer journeys mean pure platform attribution under-reports. What to do:</p>
<ul>
  <li>Rely on platform attribution for directional signals, not absolute truth</li>
  <li>Track a ground-truth metric — actual customers, actual revenue — weekly</li>
  <li>Use UTMs consistently for your own reporting</li>
  <li>Run "marketing lift tests" — pause a channel for 2 weeks, see what revenue drops</li>
  <li>Consider MMM (marketing mix modeling) for multi-channel attribution once scale is large enough</li>
</ul>

<h2>The discipline — weekly cadence</h2>
<p>A healthy paid program runs a consistent weekly cycle:</p>
<ul>
  <li>Monday — review last week's numbers (spend, conversions, CAC, LTV signals)</li>
  <li>Tuesday — identify winning / losing creatives; prep new tests</li>
  <li>Wednesday–Thursday — launch new tests, kill underperformers</li>
  <li>Friday — report out; document what's worked</li>
</ul>
<p>Without the cadence, paid drifts. Creatives go stale, CAC drifts up, and by the time you notice, you've burned $50K.</p>

<p style="margin-top:40px;">Related: <a href="core-four.html">The core four</a> · <a href="../testing/scientific.html">Scientific testing</a> · <a href="../copy/headlines.html">Headlines</a></p>
""",
    prev=("Cold outreach", "cold-outreach.html"),
    nxt=("Sales letter structure", "../letters/structure.html"),
)


# ============================================================
# SALES LETTERS + VSLS (5 pages)
# ============================================================

write_drm_page(
    slug="letters/structure",
    title="Sales letter structure",
    description="The classical direct-response sales letter hasn't changed in 60 years because the structure works. Here's the canonical template — and why each section is load-bearing.",
    reading_time=8,
    body_html="""
<p class="lede">The classical direct-response sales letter has 12+ canonical sections in a specific order, and the order matters. Kennedy formalized it; Halbert perfected it; Hormozi's modern versions (and every high-converting VSL on YouTube today) still follow it. Change the structure and response drops. Follow it and you have a template that's worked for 60 years.</p>

<h2>The full structure</h2>
<ol>
  <li>Pre-head (qualifier)</li>
  <li>Headline</li>
  <li>Sub-headline / deck</li>
  <li>Lead (the opening story or problem reveal)</li>
  <li>Agitation of the problem</li>
  <li>Introduction — who you are, credibility</li>
  <li>The promise (the big outcome)</li>
  <li>Reveal of the mechanism</li>
  <li>Proof stack (case studies, testimonials, data)</li>
  <li>Bullets (fascinations — what they get)</li>
  <li>The offer stack (core + bonuses)</li>
  <li>Price reveal + justification</li>
  <li>Guarantee</li>
  <li>Urgency / scarcity</li>
  <li>Call to action</li>
  <li>P.S. — restate offer + urgency</li>
  <li>FAQ — handle residual objections</li>
  <li>Secondary CTA</li>
</ol>

<h2>Section-by-section — what each does and how to write it</h2>

<h3>1. Pre-head (qualifier)</h3>
<p>Small text above the headline that qualifies the audience. "For operators scaling from $1M to $10M ARR who've hit a plateau they can't explain." The pre-head tells the wrong prospect to leave before they read.</p>

<h3>2. Headline</h3>
<p>Covered in <a href="../copy/headlines.html">headlines</a>. The biggest, boldest element. 80% of the work.</p>

<h3>3. Sub-headline / deck</h3>
<p>Under the headline, a longer paragraph that deepens the promise. This is where you can afford 2–3 sentences of specific benefit detail.</p>

<h3>4. Lead — the opening</h3>
<p>See <a href="../copy/the-lead.html">the lead</a>. The first 100 words earn the next 1,000.</p>

<h3>5. Agitation of the problem</h3>
<p>2–4 paragraphs making the problem feel acute. Specific, sensory, consequential. The reader has to feel the problem before they'll pay to solve it.</p>

<h3>6. Introduction / credibility</h3>
<p>Not "about us." Not a résumé. One or two sentences: why should the reader listen to <em>you</em> on this specific problem? Specific credentials, specific track record, specific experience.</p>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
"Over the past four years, I've worked with 73 SaaS companies on this exact transition. 41 of them crossed $1M ARR. 12 crossed $10M. Here's what I've seen repeatedly."
</blockquote>

<h3>7. The promise</h3>
<p>The big outcome, stated boldly. What will be true for the reader if they engage with the offer? This is where you paint the picture of the future state — concrete and vivid.</p>

<h3>8. Mechanism reveal</h3>
<p>The core intellectual content. Why does this approach work when others haven't? What's different? This is where you earn the right to ask for money. Specific, concrete, and — critically — novel or at least reframed.</p>

<h3>9. Proof stack</h3>
<p>Multiple layers of proof:</p>
<ul>
  <li>Named case studies with numbers</li>
  <li>Testimonials (name, photo, title, specific outcome)</li>
  <li>Quantified claims — "transacted $4.2M in pipeline," "47 clients this year"</li>
  <li>Media mentions, publications, speaking credentials</li>
  <li>Screenshots, demonstrations</li>
</ul>

<h3>10. Bullets</h3>
<p>See <a href="../copy/bullets.html">fascination bullets</a>. 20–40 on a long-form sales letter. Each a tiny pitch.</p>

<h3>11. Offer stack</h3>
<p>See <a href="../offer/grand-slam.html">grand slam offers</a>. Core product + bonuses, each priced to defensively justify the total value.</p>

<h3>12. Price reveal + justification</h3>
<p>Before the price: "Here's what all this is worth: [stack total]." Then the price: "Your investment today: [price]." The anchor + reveal pattern makes the price feel like a concession.</p>

<h3>13. Guarantee</h3>
<p>See <a href="../offer/guarantees.html">guarantees</a>. State it specifically. Frame it as taking the risk off the buyer's shoulders.</p>

<h3>14. Urgency / scarcity</h3>
<p>See <a href="../offer/urgency-scarcity.html">urgency + scarcity</a>. Real deadline, real reason, real next step if they miss it.</p>

<h3>15. Call to action</h3>
<p>See <a href="../copy/ctas.html">calls to action</a>. Specific, benefit-framed, visually distinct.</p>

<h3>16. P.S.</h3>
<p>Halbert's secret weapon. The P.S. is the second most-read element after the headline. Use it to restate the core value, the deadline, or a final reason to act.</p>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
"P.S. — Enrollment closes Friday at 5pm EST. If you're on the fence: the guarantee means the worst case is you lose nothing. Book your call today and we can walk through whether this is actually a fit for your business. If it's not, I'll tell you directly and we'll both save time."
</blockquote>

<h3>17. FAQ</h3>
<p>Handle objections that didn't fit naturally into the body. Common questions:</p>
<ul>
  <li>"Who is this not for?"</li>
  <li>"How long does it take to see results?"</li>
  <li>"What if I've tried X before?"</li>
  <li>"What if I don't have time?"</li>
  <li>"What happens after I buy?"</li>
</ul>
<p>Each FAQ is an objection killer. Write them to address real objections you've heard from prospects, not imaginary ones.</p>

<h3>18. Secondary CTA</h3>
<p>After the FAQ, another chance to convert. Some prospects read the whole letter but don't click until after the FAQ.</p>

<h2>Section emphasis by audience</h2>
<p>Not every section needs equal weight for every audience:</p>
<ul>
  <li><strong>Unaware / problem-aware prospects</strong> — heavy on sections 4–5 (lead, agitation); lighter on 12 (price) until later</li>
  <li><strong>Solution-aware</strong> — heavier on section 8 (mechanism) — why yours vs theirs</li>
  <li><strong>Product-aware</strong> — heavier on section 9–10 (proof + bullets), lighter on 5–7</li>
  <li><strong>Most aware</strong> — go straight to sections 11–15 (offer, guarantee, CTA)</li>
</ul>
<p>Segment your traffic and send them to the right version of the letter, or write one letter that rewards skippers (scannable with clear section breaks) so advanced readers can navigate to the offer directly.</p>

<h2>Length</h2>
<p>Classical direct-response sales letters were 6–12 pages in print; modern ones are 3,000–10,000+ words on a landing page. Length isn't a goal — it's the output of including every needed section.</p>
<p>The question isn't "how long should this be?" The question is "what does the prospect need to believe before they'll buy?" Then: how many words does that take?</p>

<h2>The test</h2>
<p>Show a draft to someone in your ICP. Watch them read. Three tests:</p>
<ul>
  <li>Where do they skim? (Section too long or irrelevant)</li>
  <li>Where do they slow down? (Section doing real work — don't touch)</li>
  <li>Where do they stop reading? (Critical friction — fix immediately)</li>
</ul>

<p style="margin-top:40px;">Related: <a href="long-form.html">Long form vs short form</a> · <a href="vsls.html">VSLs</a> · <a href="story-selling.html">Story selling</a> · <a href="halbert-letters.html">The Halbert letters</a></p>
""",
    prev=("Paid ads", "../leads/paid-ads.html"),
    nxt=("Long form vs short form", "long-form.html"),
)


write_drm_page(
    slug="letters/long-form",
    title="Long form vs short form",
    description="The long copy / short copy debate has been settled for 90 years, but the framing keeps changing. Here's when long wins, when short wins, and why the answer is 'it depends' — but only in the specific ways that matter.",
    reading_time=6,
    body_html="""
<p class="lede">The "long copy vs short copy" debate has been litigated every decade since 1900. The answer: both work. Length isn't a preference — it's a function of prospect readiness, purchase complexity, price, and skepticism. Match length to the decision the prospect is actually making and both formats can convert. Mismatch and neither does.</p>

<h2>What determines optimal length</h2>
<ol>
  <li><strong>Price.</strong> The higher the price, the longer the copy needs to be. A $29 product sells in 200 words; a $29,000 program usually needs 3,000+.</li>
  <li><strong>Awareness stage.</strong> Unaware prospects need more setup; most-aware prospects need less.</li>
  <li><strong>Complexity of the offer.</strong> Simple, well-known product = short copy. Novel mechanism or multi-part offer = long copy.</li>
  <li><strong>Commitment level.</strong> Low-commitment actions (email opt-in) = short. High-commitment (paying $5K) = long.</li>
  <li><strong>Category skepticism.</strong> Distrust-heavy categories (financial advice, weight loss, info products) = long. Trust-established categories = shorter.</li>
</ol>

<h2>The short-form strengths</h2>
<ul>
  <li>Faster to write and iterate</li>
  <li>Better fit for mobile-first readers scrolling quickly</li>
  <li>Optimal for impulse purchases</li>
  <li>Cheaper to A/B test</li>
  <li>Matches ad → landing page traffic where intent is already high</li>
</ul>

<h2>The long-form strengths</h2>
<ul>
  <li>Handles complex decisions thoroughly</li>
  <li>Builds belief layer by layer</li>
  <li>Filters out unqualified buyers (they won't read; that's a feature)</li>
  <li>Handles more objections pre-emptively</li>
  <li>Usually out-converts short form for high-ticket, high-consideration purchases</li>
</ul>

<h2>The myth: "Nobody reads long copy anymore"</h2>
<p>Variants of this claim have been made every decade since 1910. They've always been wrong, for a specific reason: qualified buyers read long copy. Unqualified ones skim past either way. The metric that matters isn't "how many people read the whole thing" — it's "how many qualified buyers read enough to buy."</p>
<p>Long copy with a 4% bounce rate and 2% conversion outperforms short copy with a 1% bounce rate and 0.4% conversion. The former filters; the latter democratizes — and democratizing who sees your offer isn't the same as selling to them.</p>

<h2>The length matrix</h2>

<table style="width:100%; border-collapse:collapse; margin:20px 0;">
  <tr style="background:#f5f5f7;"><th style="padding:10px; text-align:left; border:1px solid #e5e5ea;">Scenario</th><th style="padding:10px; text-align:left; border:1px solid #e5e5ea;">Typical length</th></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Lead magnet landing page</td><td style="padding:10px; border:1px solid #e5e5ea;">300–800 words</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">$29–99 SaaS / info product</td><td style="padding:10px; border:1px solid #e5e5ea;">500–1,500 words</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">$200–500 course / ecom</td><td style="padding:10px; border:1px solid #e5e5ea;">1,500–3,000 words</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">$1K–5K course or tool</td><td style="padding:10px; border:1px solid #e5e5ea;">3,000–6,000 words</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">$5K+ service / program</td><td style="padding:10px; border:1px solid #e5e5ea;">Book a call (no buy online)</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Free trial signup</td><td style="padding:10px; border:1px solid #e5e5ea;">500–1,500 words</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Enterprise B2B</td><td style="padding:10px; border:1px solid #e5e5ea;">Short web copy + long sales collateral</td></tr>
</table>

<h2>Hybrid structures</h2>
<p>Modern landing pages often blend both:</p>
<ul>
  <li>Above-the-fold short-copy hero (for skimmers ready to buy)</li>
  <li>Long-form below the fold for readers who want to go deeper</li>
  <li>Multiple CTAs throughout — skimmers click the first one, readers click after reading</li>
</ul>
<p>This "two audiences, one page" design satisfies both types. You're not betting on one — you're serving both.</p>

<h2>VSLs: long-form video</h2>
<p>A 30-minute VSL is long-form copy delivered in video. Same structure, same sections, different medium. See <a href="vsls.html">VSLs</a>.</p>

<h2>How to decide for your offer</h2>
<ol>
  <li>What's the price point?</li>
  <li>How aware is the traffic arriving? (paid = cold; email = warm; retargeting = hot)</li>
  <li>How complex is the mechanism? Can you explain why it works in 3 sentences, or does it need paragraphs?</li>
  <li>How many objections typically come up in sales calls? Each one needs handling in copy.</li>
  <li>What does every competitor do? (Note: you don't have to match — contrarian sometimes wins — but know the norm.)</li>
</ol>

<h2>The rewrite test</h2>
<p>If you have long copy, try to write the short version. What's the one-paragraph pitch? One sentence?</p>
<p>If you can't make the short version, your long copy is padded.</p>
<p>If the short version already sells well, you don't need the long.</p>
<p>If both work for different audiences, run both on different traffic sources.</p>

<h2>The common mistakes</h2>

<h3>Making long copy long by padding</h3>
<p>Long copy doesn't earn its length by repeating the same points in different words. Every section does specific work: agitation, mechanism, proof, bullets, offer. If a section isn't doing work, cut it.</p>

<h3>Making short copy short by omitting proof</h3>
<p>Short copy earns brevity by being at the right place in the funnel. If your short copy is short because you don't have proof, that's not short copy — that's missing information.</p>

<h3>Mismatching length to traffic</h3>
<p>Sending cold paid traffic to 4-paragraph pages → low conversion. Sending hot email traffic to 6,000-word pages → wasted conversion (they'd buy in 500 words).</p>

<p style="margin-top:40px;">Related: <a href="structure.html">Sales letter structure</a> · <a href="vsls.html">VSLs</a> · <a href="../market/awareness-stages.html">Awareness stages</a></p>
""",
    prev=("Sales letter structure", "structure.html"),
    nxt=("VSLs", "vsls.html"),
)


write_drm_page(
    slug="letters/vsls",
    title="VSLs",
    description="The Video Sales Letter is the modern incarnation of the Kennedy-style long-form sales letter — built for 2026 attention spans but still following the 90-year-old direct-response structure.",
    reading_time=7,
    body_html="""
<p class="lede">The Video Sales Letter — VSL — is the modern incarnation of the long-form direct-response sales letter. 10 to 60 minutes of video selling a single offer. Structure-wise, it's Kennedy's sales letter in video form. Done well, it outconverts a text-based equivalent for most high-ticket offers in 2026. Done poorly, it's a long way to lose attention.</p>

<h2>Why VSLs work</h2>
<ul>
  <li>Video holds attention longer than text when well-paced</li>
  <li>Faces build trust in a way text can't</li>
  <li>Tone, rhythm, and emphasis carry additional persuasion</li>
  <li>Long-form structure in a medium audiences accept as "a video"</li>
  <li>No skipping ahead (if you use a locked player) forces sequential consumption</li>
</ul>

<h2>The structure — same as a sales letter</h2>
<ol>
  <li><strong>0:00–0:30 Hook.</strong> Pattern interrupt. A surprising claim, a specific scene, a direct question. Earn the next 30 seconds.</li>
  <li><strong>0:30–2:00 Promise.</strong> State the big promise — what they'll learn or be able to do by the end of the video / by buying.</li>
  <li><strong>2:00–5:00 Problem + agitation.</strong> The problem they're facing. Why it's worse than they thought. Consequences.</li>
  <li><strong>5:00–7:00 Introduction.</strong> Who you are, why you're qualified. Brief. Credibility, not autobiography.</li>
  <li><strong>7:00–15:00 Mechanism.</strong> The novel approach. Why this works when others don't. Explain the thing.</li>
  <li><strong>15:00–22:00 Proof.</strong> Case studies. Testimonials. Data. Screenshots. Specific outcomes.</li>
  <li><strong>22:00–28:00 Benefits / "here's what you get."</strong> The offer stack unfolded.</li>
  <li><strong>28:00–32:00 Price + bonuses.</strong> Value anchoring, reveal, bonus stack.</li>
  <li><strong>32:00–35:00 Guarantee.</strong> Risk reversal.</li>
  <li><strong>35:00–37:00 Urgency.</strong> Deadline, reason, consequence of waiting.</li>
  <li><strong>37:00–40:00 CTA + close.</strong> Specific next step. Clear button on the screen.</li>
</ol>
<p>The times are approximations — a tight VSL might be 18 minutes; a long one 60. Same sections, different pacing.</p>

<h2>Pacing rules</h2>
<ul>
  <li><strong>Every 30–60 seconds, a new beat.</strong> New claim, new story, new visual. Monotony kills retention.</li>
  <li><strong>Open loops.</strong> Promise something now; deliver later. "I'll show you the exact number in a minute." Keeps the viewer watching through the middle.</li>
  <li><strong>B-roll and text overlays.</strong> Not decoration — emphasis. When you make a key claim, it also appears on screen.</li>
  <li><strong>Pattern interrupts.</strong> Every few minutes, change tone, change setting, change medium. A voice-only segment, then a screen share, then a face-to-camera testimonial.</li>
  <li><strong>No filler words in the script.</strong> "Uh," "you know," "basically" all cut in edit.</li>
</ul>

<h2>Hook formulas that work</h2>
<ul>
  <li>"If you [specific situation], this is the most important video you'll watch this year."</li>
  <li>"I'm about to show you [unbelievable specific claim]. And I'm going to prove it to you in the next [X] minutes."</li>
  <li>"Most [audience] are making this specific mistake. Let me show you what it's costing them."</li>
  <li>"Two years ago, I was [specific low point]. Today, [specific win]. Here's exactly what changed."</li>
  <li>"Everything you've been told about [topic] is incomplete. Here's the part nobody explains."</li>
</ul>

<h2>The script</h2>
<p>VSLs are scripted. Word-for-word. Not ad-libbed. The reason: every sentence earns the next; there's no room for tangents, dead air, or self-editing in the moment.</p>
<p>Writing process:</p>
<ol>
  <li>Draft the full script — 8,000–15,000 words for a 30–45 minute VSL</li>
  <li>Read aloud. Time each section.</li>
  <li>Cut anything that doesn't directly move the viewer forward</li>
  <li>Mark in beats (visual cues, b-roll moments, on-screen text)</li>
  <li>Rehearse — 3–5 read-throughs before recording</li>
  <li>Record in takes; splice together</li>
</ol>

<h2>Production quality</h2>
<p>The bar has risen. What used to work (slide-based, faceless VSLs) now underperforms in most categories. Current norms:</p>
<ul>
  <li>Face-on-camera, not just slides</li>
  <li>Good audio (single most important production element)</li>
  <li>Decent lighting (natural light works; you don't need a studio)</li>
  <li>B-roll, screenshots, data visualizations cut in</li>
  <li>Captions / subtitles (many viewers watch muted)</li>
  <li>Logo/brand consistency throughout</li>
</ul>
<p>"Good enough" production now means: natural light, face visible, clear audio, reasonable cuts. You don't need a film crew; you do need to not look amateur.</p>

<h2>Delivery platforms</h2>
<ul>
  <li><strong>Embedded on landing page</strong> — the canonical play. Video + CTA below it.</li>
  <li><strong>Autoplay or click-to-play</strong> — click-to-play tends to perform better in 2026 (respects viewer choice)</li>
  <li><strong>Locked or skippable</strong> — locked VSLs feel manipulative to sophisticated audiences; skippable + timed CTAs tend to convert better</li>
  <li><strong>On webinar platforms</strong> — live and on-demand webinars are essentially scheduled VSLs</li>
</ul>

<h2>The CTA layer</h2>
<p>Under the video, clear CTAs:</p>
<ul>
  <li>Primary CTA — book call / buy / download</li>
  <li>Secondary CTA — "still have questions? here's how to reach us"</li>
  <li>Sticky button that appears after the price reveal</li>
</ul>
<p>Some VSLs have a "lock" where the CTA only appears at a certain timestamp. This forces viewing. Effective at scale but reads as manipulative — decide based on your audience.</p>

<h2>Metrics to track</h2>
<ul>
  <li><strong>View rate</strong> — % who start the video</li>
  <li><strong>Retention curve</strong> — % viewing at each timestamp</li>
  <li><strong>Drop-off points</strong> — where viewers leave</li>
  <li><strong>CTA click rate</strong> — % who click after watching</li>
  <li><strong>Conversion rate</strong> — % who complete the next step</li>
  <li><strong>Completed-view conversion</strong> — of those who watch the whole thing, what % buy (a specific sub-metric that tells you whether the problem is the video or the offer)</li>
</ul>

<h2>The iteration loop</h2>
<p>VSLs aren't one-and-done:</p>
<ol>
  <li>Ship v1</li>
  <li>Analyze retention curve — major drop-offs</li>
  <li>Rewrite problem sections</li>
  <li>A/B test hook variants</li>
  <li>Test price reveals at different timestamps</li>
  <li>Iterate every 30–60 days</li>
</ol>
<p>A mature VSL is usually on iteration 5+ before it hits its best conversion.</p>

<p style="margin-top:40px;">Related: <a href="structure.html">Sales letter structure</a> · <a href="long-form.html">Long form vs short form</a> · <a href="story-selling.html">Story selling</a></p>
""",
    prev=("Long form vs short form", "long-form.html"),
    nxt=("Story selling", "story-selling.html"),
)


write_drm_page(
    slug="letters/story-selling",
    title="Story selling",
    description="A story outperforms a pitch because the reader suspends skepticism to follow the narrative. Here's how to use story as the engine of a sales letter, VSL, or email — without sounding like you're just telling a story.",
    reading_time=6,
    body_html="""
<p class="lede">Prospects resist pitches. They don't resist stories. Put a claim into a story and the reader processes it differently — they're following the character instead of evaluating the claim. Story selling is the technique of using narrative structure as the backbone of a sales letter or VSL. Halbert built his letters around stories; Hormozi opens most of his content with one; every converting VSL has a story layer running through it.</p>

<h2>Why stories work</h2>
<ul>
  <li><strong>They suspend skepticism.</strong> A reader evaluates claims; they follow stories.</li>
  <li><strong>They build identification.</strong> "That sounds like my situation" hits harder than "this is the problem."</li>
  <li><strong>They deliver proof implicitly.</strong> "Here's what happened when [character] tried this" is proof without sounding like proof.</li>
  <li><strong>They pace emotion.</strong> Stories have rhythm — setup, tension, climax, resolution — which controls how the reader feels through the copy.</li>
  <li><strong>They're memorable.</strong> Prospects forget claims but remember stories.</li>
</ul>

<h2>The core story shapes</h2>

<h3>1. The founder origin</h3>
<p>"Two years ago, I was where you are." Personal story of the problem, the journey, the solution. Works because the reader identifies with the past-you, which makes them trust the current-you.</p>
<p>Structure:</p>
<ul>
  <li>Specific bad moment (where you were)</li>
  <li>What you tried that didn't work</li>
  <li>The turning point (insight, mentor, book, event)</li>
  <li>The mechanism you discovered</li>
  <li>What happened next</li>
  <li>Why you're sharing it now</li>
</ul>

<h3>2. The customer case</h3>
<p>"Kevin was a plumbing shop owner in Indianapolis. 6 trucks. $800K/year. Dying." Tell one specific customer's full story — setup, journey, outcome. Works because it's proof delivered as narrative.</p>

<h3>3. The discovery</h3>
<p>"I noticed something strange while looking at our top-performing clients. The 3% of them who did X also did Y, despite doing nothing else similar. When we tested it, everything changed." Frames insight as a story of discovery rather than as a claim.</p>

<h3>4. The anti-hero reversal</h3>
<p>"For years, I told my students to do X. Then I watched 12 of them fail. I realized I was wrong — and here's what I teach now." Admitting a past mistake builds more trust than claiming past infallibility.</p>

<h3>5. The industry story</h3>
<p>"The reason every small business gets sold this lie is…" Tells the story of the market, not a person. Useful for reframing prospect beliefs before presenting your alternative.</p>

<h2>What makes a story work in direct response</h2>

<h3>Specificity</h3>
<p>"Kevin" is 10x better than "a client." "A plumbing shop in Indianapolis" is better than "a trades business." Every specific detail adds credibility even when the detail seems irrelevant.</p>

<h3>Sensory detail</h3>
<p>"The fluorescent light flickered in his garage office" engages the reader differently than "He worked out of his garage." Small sensory details transport.</p>

<h3>Tension</h3>
<p>Every story needs a "but." Things were going well, <em>but</em>… Things were bad, <em>but</em>… Without tension there's no story.</p>

<h3>Turn</h3>
<p>The moment everything changes. Stories without turns are anecdotes. The turn is the insight, the event, the phone call, the realization.</p>

<h3>Specific outcome</h3>
<p>Story without outcome is sentimental. "He went from $800K to $2.7M in 11 months, without adding a single truck." Number, timeframe, context.</p>

<h2>Integrating story into the sales letter structure</h2>
<p>Stories don't replace the <a href="structure.html">sales letter structure</a> — they thread through it:</p>
<ul>
  <li><strong>Lead</strong> — open with a specific scene or moment (customer story or founder story)</li>
  <li><strong>Agitation</strong> — use the story to make the problem vivid ("this is what Kevin was feeling…")</li>
  <li><strong>Mechanism reveal</strong> — explain through the story's turn ("here's what happened when he tried it differently")</li>
  <li><strong>Proof</strong> — multiple customer stories, each with specifics</li>
  <li><strong>Close</strong> — call back to the opening story's resolution</li>
</ul>

<h2>Halbert's letter structure — the story-first letter</h2>
<p>Halbert's most famous letters often opened with 3–5 paragraphs of pure story before any pitch. The reader is hooked by the narrative; the pitch happens after identification is established. Modern equivalent: VSLs that open with 3–5 minutes of story.</p>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Halbert-style opening (modern translation):</strong><br><br>
"At 2:14am on a Tuesday last September, Kevin — a plumbing shop owner in Indianapolis — sat in his garage office staring at his screen.<br><br>
He'd just looked at the Q3 numbers. $187K in revenue. Second-worst quarter in three years. His best tech had just put in notice. His ex-wife had texted twice that day about the kid's school thing he'd forgotten. And the bank had sent a letter that afternoon he hadn't opened yet.<br><br>
If you'd asked Kevin on that Tuesday night whether his business was working, he'd have laughed. And if you'd asked him what he thought he was doing wrong — he'd have given you a list of things, none of them right.<br><br>
What happened to Kevin in the next 90 days was the kind of thing most operators would call impossible…"
</blockquote>
<p>The reader is 200 words in and hasn't been pitched once. The identification with Kevin does the work.</p>

<h2>Common story-selling mistakes</h2>

<h3>Stories that don't connect to the offer</h3>
<p>An entertaining story that doesn't support the specific claim you're making is indulgent. Every story beat should carry a piece of the persuasion.</p>

<h3>Stories that are too clean</h3>
<p>Perfect heroes and perfect outcomes feel fake. Include the friction — the moment of doubt, the thing that went wrong, the cost Kevin paid before the turn. Real beats clean.</p>

<h3>Generic story beats</h3>
<p>"We were struggling. Then we discovered X. Now we're thriving." The pattern is fine; the words are wrong. Every story needs its own specificity.</p>

<h3>Too many stories in one piece</h3>
<p>One anchor story + 2–3 supporting stories is the maximum. More than that and the reader loses the thread.</p>

<h2>The story library</h2>
<p>Maintain a library of stories you can draw from — founder stories, customer case stories, discovery stories. Every new sales letter, VSL, or email can pull the right story for the angle. This is one of the highest-leverage assets a direct-response business builds.</p>

<p style="margin-top:40px;">Related: <a href="halbert-letters.html">The Halbert letters</a> · <a href="structure.html">Sales letter structure</a> · <a href="../copy/the-lead.html">The lead</a></p>
""",
    prev=("VSLs", "vsls.html"),
    nxt=("The Halbert letters", "halbert-letters.html"),
)


write_drm_page(
    slug="letters/halbert-letters",
    title="The Halbert letters",
    description="Gary Halbert's sales letters are case studies in virtuoso direct-response copy. Studying them — the coat-of-arms letter, the Tova letter, the seminar pitches — is the best copywriting education most writers will ever get.",
    reading_time=6,
    body_html="""
<p class="lede">Gary Halbert wrote controls that ran for decades. His letters are case studies in virtuoso direct-response copy — specific, personal, impossible to ignore. Studying them closely is the best copywriting education most writers will ever get. Start with three letters and reverse-engineer what he did.</p>

<h2>The coat-of-arms letter</h2>
<p>One of the most profitable direct-mail letters ever written. Halbert mailed an offer for a research report on the buyer's family name and coat of arms, to recipients who'd never asked. It generated millions. Every element was deliberately engineered.</p>

<h3>Why it worked</h3>
<ul>
  <li><strong>Hyper-personal opening.</strong> "I don't know if you realize it, but the last name [RECIPIENT'S NAME] has a rich history…" Personalized at a mass-mail scale using early mail-merge.</li>
  <li><strong>Curiosity trigger.</strong> Everyone is curious about their own name. Unanswerable headline of attention.</li>
  <li><strong>Specific research.</strong> The letter described (generically but convincingly) what the research included, hinting at discoveries the recipient would find compelling.</li>
  <li><strong>Mailed in a plain white envelope.</strong> Looked personal, not like junk mail. Passed the <a href="../followup/direct-mail.html">A-pile test</a>.</li>
  <li><strong>Handwritten-style signature.</strong> Reinforced the personal feel.</li>
  <li><strong>Low-ticket offer.</strong> $10 for the research. Easy yes.</li>
</ul>

<h3>What it teaches</h3>
<p>Personalization + curiosity + low-commitment offer + physical format that gets opened = a machine. The principles translate to modern email and direct mail.</p>

<h2>The Tova letter (Tova Borgnine perfume)</h2>
<p>Halbert wrote a long-form mail letter for Tova Borgnine's perfume in the 1980s. The letter opened with a story about Tova's search for the "perfect scent" — years of experimentation, specific ingredients, the breakthrough moment. Then the offer, with a specific risk-free trial.</p>

<h3>Why it worked</h3>
<ul>
  <li><strong>Story-driven.</strong> The entire top half was pure narrative. Hooked the reader before selling.</li>
  <li><strong>Celebrity credential.</strong> Tova Borgnine's name lent authority without bragging.</li>
  <li><strong>Reason-why copy.</strong> Specific ingredients, specific sources, specific process — made the product seem substantive.</li>
  <li><strong>Risk reversal.</strong> Try it free; keep it if you love it; send it back if you don't.</li>
  <li><strong>Long but earned its length.</strong> Each paragraph built belief or desire.</li>
</ul>

<h3>What it teaches</h3>
<p>A long letter for a consumer product works when the story is compelling, the risk is reversed, and the product is positioned as the answer to a specific search the founder undertook.</p>

<h2>The "nobody wants to read your stupid ad" principle</h2>
<p>Halbert repeated this constantly. Prospects don't want to read ads. They want to read stories, news, relevant-to-them content. The solution:</p>
<ol>
  <li>Disguise the ad as something the reader actually wants to consume</li>
  <li>Make the opening so specific, personal, or curious that it can't be ignored</li>
  <li>Every sentence earns the next</li>
  <li>The pitch appears only after identification is established</li>
</ol>
<p>This is why Halbert's letters often felt like personal letters from a friend, not like "advertising."</p>

<h2>Halbert's newsletter</h2>
<p>The Gary Halbert Letter — still free online — ran for years and contained hundreds of hours of copywriting education. Key themes that recur:</p>
<ul>
  <li>Test everything. Always. Repeatedly.</li>
  <li>80% of success is in the headline.</li>
  <li>The postscript is the second most-read element.</li>
  <li>A starving crowd > any product advantage.</li>
  <li>40% list + 40% offer + 20% copy.</li>
  <li>Passion is the invisible ingredient — a letter written with genuine enthusiasm outperforms the cleverest one written from detachment.</li>
</ul>

<h2>What to study specifically</h2>

<h3>Halbert's openings</h3>
<p>Pull 10 of his letters. Read only the first paragraph of each. Notice:</p>
<ul>
  <li>How specific the opening detail is</li>
  <li>How "you"-focused</li>
  <li>How fast you're pulled into the second sentence</li>
  <li>How little "marketing voice" is present</li>
</ul>

<h3>Halbert's bullets</h3>
<p>Many Halbert letters have 30–60 bullets in a row. Study them. Notice:</p>
<ul>
  <li>The specificity of each (numbers, names, moments)</li>
  <li>The hook verbs ("how," "why," "the")</li>
  <li>The open loops — each bullet implies content you can only get by buying</li>
  <li>The variation — he doesn't use the same structure twice in a row</li>
</ul>

<h3>Halbert's P.S.</h3>
<p>Note how much of the final pitch happens in the P.S. — often the most urgent, specific call in the letter. The P.S. isn't an afterthought; it's the second peak of the piece.</p>

<h2>The Halbert exercise</h2>
<ol>
  <li>Pick one Halbert letter from thegaryhalbertletter.com</li>
  <li>Read it in full</li>
  <li>Write out, from scratch, the same letter for <em>your</em> product or service</li>
  <li>Match the structure, pacing, and rhythm</li>
  <li>Send it. Or post it. Or test it.</li>
</ol>
<p>This is the fastest way to internalize Halbert's copywriting. You don't learn by reading — you learn by imitation, then by adaptation.</p>

<h2>What still works from Halbert in 2026</h2>
<ul>
  <li>The hyper-personal opening</li>
  <li>Story-driven leads</li>
  <li>Specificity as the first principle of belief</li>
  <li>Long-form for high-consideration purchases</li>
  <li>The 40/40/20 framing of where results come from</li>
  <li>The P.S. as load-bearing</li>
  <li>Testing as the only arbiter of what works</li>
</ul>

<h2>What's changed</h2>
<ul>
  <li>Direct mail is mostly dead; email and video have taken the format</li>
  <li>Readers are more sophisticated — purely direct claims feel dated</li>
  <li>Trust signals have shifted (reviews, social proof, peer validation)</li>
  <li>Attention spans have shortened for unengaged viewers, but qualified prospects still read long copy</li>
</ul>
<p>The changes are in format and surface; the deep structure is the same.</p>

<p style="margin-top:40px;">Related: <a href="structure.html">Sales letter structure</a> · <a href="story-selling.html">Story selling</a> · <a href="../copy/bullets.html">Fascination bullets</a></p>
""",
    prev=("Story selling", "story-selling.html"),
    nxt=("Direct mail that still works", "../followup/direct-mail.html"),
)

print("\n✓ Lead Gen + Sales Letters (10 pages)")
