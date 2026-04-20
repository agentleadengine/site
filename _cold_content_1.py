#!/usr/bin/env python3
"""Cold Email content part 1: Hub + Foundations + Deliverability + Infrastructure (17 pages)."""
from _build_cold import write_cold_page

# Cross-section links to DR copywriting
DR_LINK = "../../direct-response"

# ============================================================
# HUB
# ============================================================

hub_body = f"""
<p class="lede">Cold email is the highest-leverage outbound channel in B2B. When it works, it produces predictable pipeline at a cost that beats paid ads and a velocity that beats content. When it breaks, it quietly damages your domain, your brand, and your future ability to send anything. Most teams run cold email badly. The ones who run it well treat it as a four-part discipline: deliverability, lists, copy, and sequences - each a craft of its own.</p>

<p>This section is 45 pages on running cold email the way it actually works in 2026. The copy sections connect directly to the <a href="{DR_LINK}/index.html">direct response section</a> - cold email is direct response applied to the inbox, and the classical copywriting principles still apply.</p>

<h2>The eight sections</h2>

<div class="cards" style="margin-top:32px;">
  <a href="foundations/what-is-cold-email.html" class="card"><h3>Foundations</h3><p>What cold email actually is, how it's different from spam, the legal landscape, and when it works.</p></a>
  <a href="deliverability/why-it-matters.html" class="card"><h3>Deliverability</h3><p>DNS records, sending domains, warming, IP reputation, spam triggers. The single most important area most teams ignore.</p></a>
  <a href="infra/sending-tools.html" class="card"><h3>Infrastructure</h3><p>Instantly, Smartlead, Lemlist, multi-inbox rotation, warming, reply management.</p></a>
  <a href="lists/icp.html" class="card"><h3>Lists + Targeting</h3><p>Defining the ICP, sourcing leads, enriching with Clay, verification, intent signals, segmentation.</p></a>
  <a href="copy/anatomy.html" class="card"><h3>Copy</h3><p>Subject lines, first lines, pitches, CTAs, signatures. Direct response applied to the inbox.</p></a>
  <a href="sequences/multi-touch.html" class="card"><h3>Sequences</h3><p>Multi-touch cadence, timing, breakup emails, multi-channel orchestration.</p></a>
  <a href="testing/methodology.html" class="card"><h3>Testing</h3><p>What to test, how to measure positive reply rates, the iteration loop.</p></a>
  <a href="plays/b2b-saas.html" class="card"><h3>Playbooks</h3><p>B2B SaaS, agency, founder-led, SDR-led, link building, recruiting. Specific patterns by use case.</p></a>
</div>

<h2 style="margin-top:56px;">The priority order</h2>
<p>Most teams obsess over copy and ignore everything else. This is exactly wrong. The actual order of importance:</p>
<ol>
  <li><strong>Deliverability</strong>. If your emails land in spam, nothing else matters.</li>
  <li><strong>List quality</strong>. Sending to bad data wastes domains and budget.</li>
  <li><strong>Offer</strong>. The offer in the email has to matter to the reader.</li>
  <li><strong>Copy</strong>. How you say it, once 1-3 are right.</li>
  <li><strong>Sequence</strong>. How many times and when you follow up.</li>
</ol>
<p>Work them in this order. A great email sent to a bad list from a bad domain gets zero replies. A mediocre email sent to a great list from a warmed-up domain gets meetings.</p>

<h2 style="margin-top:40px;">How this connects to direct response</h2>
<p>Cold email is direct response at 50 words. Every principle from the <a href="{DR_LINK}/index.html">direct response section</a> applies: <a href="{DR_LINK}/copy/headlines.html">headlines</a> become subject lines, <a href="{DR_LINK}/copy/the-lead.html">leads</a> become first lines, <a href="{DR_LINK}/offer/value-equation.html">the value equation</a> still decides whether someone responds. The only difference is that cold email has strict length and deliverability constraints that shape how the principles get applied.</p>
"""

write_cold_page(
    slug="index",
    title="Cold Email",
    description="A 45-page reference on modern cold email: deliverability, lists, copy, sequences, testing, and playbooks. Direct response applied to the inbox.",
    reading_time=3,
    body_html=hub_body,
    prev=None,
    nxt=("What is cold email?", "foundations/what-is-cold-email.html"),
)


# ============================================================
# FOUNDATIONS (4 pages)
# ============================================================

write_cold_page(
    slug="foundations/what-is-cold-email",
    title="What is cold email?",
    description="Cold email is one-to-one B2B outreach to prospects who haven't opted in. Here's the working definition and why it's still the strongest B2B channel when done right.",
    reading_time=4,
    body_html=f"""
<p class="lede">Cold email is one-to-one outreach via email to a specific prospect who hasn't opted in, with a specific offer and a specific ask. It's not broadcast marketing. It's not newsletters. It's not transactional. It's a sales motion that happens to use the email protocol.</p>

<h2>The working definition</h2>
<p>Cold email has four defining properties:</p>
<ol>
  <li><strong>One-to-one shaped.</strong> Even when automated at volume, each message is addressed to a specific person with a specific personalization.</li>
  <li><strong>Not opted in.</strong> The recipient didn't subscribe, didn't fill a form, doesn't know your company.</li>
  <li><strong>B2B.</strong> Cold email to consumers in most jurisdictions is illegal and technically harder. This section is entirely about B2B.</li>
  <li><strong>Specific offer + specific ask.</strong> Not "let's chat sometime" or "want to see our newsletter." A concrete value proposition and a clear next step.</li>
</ol>

<h2>Why cold email still works</h2>
<p>Every few years someone declares cold email dead. Every year it quietly produces more B2B pipeline than most other channels combined. Reasons:</p>
<ul>
  <li>Email is universal. Every B2B decision-maker checks email.</li>
  <li>It's cheap. No ad spend, no CPC, no platform cut.</li>
  <li>It's scalable. A single sender can reach thousands per week at reasonable deliverability.</li>
  <li>It's measurable. Open rates, reply rates, meeting book rates are all tracked.</li>
  <li>It's predictable. Once a campaign is tuned, outputs are consistent.</li>
</ul>

<h2>Where cold email fits in the Core Four</h2>
<p>In the <a href="{DR_LINK}/leads/core-four.html">core four lead channels</a>, cold email is <em>one-to-one, cold</em>. It sits between warm outreach (higher conversion, lower volume) and paid ads (higher volume, higher cost). For most B2B businesses, it's the first channel that actually scales predictably.</p>

<h2>The prerequisites</h2>
<p>Cold email works when:</p>
<ul>
  <li>Your ICP has email accessibility (they check email, their role can be identified)</li>
  <li>Your offer has enough value to justify a stranger's attention</li>
  <li>Deal size supports the cost structure (generally $3K+ ACV for sustainable ROI)</li>
  <li>Your deliverability is solid</li>
</ul>

<p>Cold email doesn't work when:</p>
<ul>
  <li>Targeting consumers (legal and deliverability issues)</li>
  <li>Selling a commodity with no differentiation</li>
  <li>Small deal sizes (can't afford the CAC)</li>
  <li>Long sales cycles with no near-term signal</li>
  <li>Using it as the only channel (needs a system around it)</li>
</ul>

<h2>The misconceptions that waste money</h2>

<h3>"Cold email is dead"</h3>
<p>Repeated every year, always wrong. Deliverability gets harder, tactics evolve, the core channel remains. What is dead: spammy blasts of 10,000 emails from one domain. What works: targeted, personalized, well-deliverable outreach.</p>

<h3>"Cold email is spam"</h3>
<p>Spam is unsolicited bulk commercial email with no value. Cold email is <a href="spam-vs-cold.html">different in a specific legal and technical sense</a> when done correctly.</p>

<h3>"We just need great copy"</h3>
<p>The most common mistake. Copy is 20% of cold email success. Deliverability and list quality together are 60%. You can have perfect copy and still get zero replies if your emails land in spam folders.</p>

<h3>"We'll just buy a list and blast"</h3>
<p>Fastest way to burn your sending domains and generate zero results. Quality lists built manually or through enrichment beat purchased lists ten times out of ten.</p>

<h2>The cold email system</h2>
<p>A functioning cold email system has these components, all of which this section covers:</p>
<ol>
  <li>Sending infrastructure (domains, DNS, tools)</li>
  <li>Warmed inboxes</li>
  <li>Targeted lead list</li>
  <li>Verified email addresses</li>
  <li>Multi-touch sequence</li>
  <li>Personalized copy</li>
  <li>Reply management process</li>
  <li>Measurement and iteration</li>
</ol>

<p>Skip any one and the system underperforms. Skip two and it fails.</p>

<p style="margin-top:40px;">Next: <a href="spam-vs-cold.html">Cold email vs spam</a>.</p>
""",
    prev=("Overview", "../index.html"),
    nxt=("Cold email vs spam", "spam-vs-cold.html"),
)


write_cold_page(
    slug="foundations/spam-vs-cold",
    title="Cold email vs spam",
    description="Cold email and spam look similar but are categorically different legally, technically, and strategically. Here's what separates them.",
    reading_time=4,
    body_html="""
<p class="lede">Email providers, regulators, and recipients all treat cold email and spam differently. The difference isn't "my email is good, spam is bad." It's a specific set of properties that determine whether a message is legal, gets delivered, and gets replied to.</p>

<h2>The legal distinction</h2>
<p>Under US CAN-SPAM (the controlling law for US-recipient cold email):</p>
<ul>
  <li>Commercial email is legal if it complies with specific requirements</li>
  <li>Deception in headers, subject lines, or sender identity is not</li>
  <li>Missing unsubscribe or valid physical address is not</li>
  <li>Failure to honor unsubscribe within 10 business days is not</li>
</ul>

<p>Cold email complying with CAN-SPAM is legal in the US even without prior consent. Spam is what breaks these rules.</p>

<p>Other jurisdictions differ. See <a href="legal.html">legal landscape</a>.</p>

<h2>The technical distinction</h2>
<p>Email providers (Google, Microsoft, Apple, etc.) use machine learning to classify incoming mail. They don't care about your intent; they care about signals:</p>

<h3>Signals that say "spam"</h3>
<ul>
  <li>Low sender reputation</li>
  <li>High send volume from a new domain</li>
  <li>Content patterns matching known spam (lots of links, spammy phrases, all caps)</li>
  <li>Low engagement (no opens, no replies, high delete rate)</li>
  <li>Recipient complaints or "mark as spam" clicks</li>
  <li>Bounces, invalid addresses</li>
  <li>Missing SPF, DKIM, DMARC</li>
  <li>Image-heavy or all-image emails</li>
</ul>

<h3>Signals that say "legitimate"</h3>
<ul>
  <li>Established sender reputation</li>
  <li>Steady, reasonable volume</li>
  <li>Plain-text or simple HTML</li>
  <li>High open and reply rates</li>
  <li>Low complaint rate</li>
  <li>Clean DNS setup</li>
  <li>Consistent sending patterns</li>
</ul>

<p>A well-run cold campaign produces legitimate signals. A blast of unverified addresses from a new domain produces spam signals. Same physical act (send email to someone who didn't opt in), wildly different classifications.</p>

<h2>The strategic distinction</h2>
<p>Spam is one-way: attacker sends, recipient deletes. Cold email is one-to-one sales: you research a specific prospect, you write a relevant offer, you expect a dialog.</p>

<p>The strategic markers:</p>
<ul>
  <li><strong>Targeting</strong>: spam hits millions; cold hits thousands of specific fits</li>
  <li><strong>Personalization</strong>: spam is identical; cold is tailored</li>
  <li><strong>Offer relevance</strong>: spam doesn't care; cold is specifically valuable to the recipient's role</li>
  <li><strong>Response expected</strong>: spam doesn't expect a reply; cold is a conversation starter</li>
  <li><strong>Follow-up behavior</strong>: spam sends then moves on; cold has polite multi-touch and stops when told to</li>
</ul>

<h2>The trust economy</h2>
<p>Email is built on trust. Every sender develops a reputation with every provider. Good senders earn inbox placement; bad senders earn filters.</p>

<p>Cold email is legitimate when it respects this economy. You send reasonable volume, you keep bounce and complaint rates low, you stop when people ask you to, you maintain sender hygiene.</p>

<p>Spam violates the economy. It extracts short-term attention at the cost of sender reputation, which is why spammers burn through domains.</p>

<h2>The "it's cold email vs spam" test</h2>
<p>A few quick tests:</p>
<ol>
  <li>Could you defend this email to the recipient in person? "We sent you this because you're a VP of Sales at a 50-person SaaS in B2B and we specifically help that exact segment." Yes = cold email. "We sent it because you're on a list we bought" = spam.</li>
  <li>If the recipient replies "stop emailing me," do you stop? Yes = cold email.</li>
  <li>Is the offer genuinely relevant to their role and likely timely? Yes = cold email.</li>
  <li>Would a reasonable recipient find the outreach at least mildly useful even if they don't buy? Yes = cold email.</li>
</ol>

<p>If you pass these, you're in cold email territory. If you don't, you're in spam territory, and no tactics will save you from consequences.</p>

<h2>The "cold email is spam" argument</h2>
<p>Some people argue any unsolicited commercial email is spam. This is a moral position, not a legal or technical one. Under US and most B2B-focused law, targeted compliant B2B outreach is legal and is not spam. Reasonable people disagree about the ethics. This section assumes you've made a judgment that compliant cold B2B outreach is acceptable, and focuses on doing it well.</p>

<p>If you disagree with that premise, that's a valid position - but this section isn't for you. Warm outreach, content, and paid ads are alternate <a href="../../direct-response/leads/core-four.html">core four</a> channels that don't involve cold outreach.</p>

<p style="margin-top:40px;">Next: <a href="legal.html">Legal landscape</a>.</p>
""",
    prev=("What is cold email?", "what-is-cold-email.html"),
    nxt=("Legal landscape", "legal.html"),
)


write_cold_page(
    slug="foundations/legal",
    title="Legal landscape",
    description="CAN-SPAM, GDPR, CASL, PECR. Cold email is legal in most jurisdictions if you follow specific rules. Here's the short version for each.",
    reading_time=5,
    body_html="""
<p class="lede">Cold email legality depends on where your recipient is located, not where you are. Each jurisdiction has its own rules. None of these are optional. I'm not a lawyer and this isn't legal advice - consult one for your specific situation - but here's the operator's summary of the landscape.</p>

<h2>United States - CAN-SPAM (2003)</h2>

<h3>What it allows</h3>
<p>Commercial email without prior consent is legal as long as you comply with the requirements.</p>

<h3>What it requires</h3>
<ul>
  <li>Accurate "From," "Reply-To," and routing information (no spoofing)</li>
  <li>Subject lines that reflect email content (no deception)</li>
  <li>Disclosure that the email is advertising (can be implied by context for cold sales outreach)</li>
  <li>A valid physical postal address in the email</li>
  <li>A clear, working unsubscribe mechanism</li>
  <li>Honoring opt-outs within 10 business days</li>
  <li>Not transferring the email address after opt-out</li>
</ul>

<h3>Penalties</h3>
<p>Up to $51,744 per violation. FTC actively enforces. In practice, penalties hit spammers sending millions; targeted B2B cold rarely triggers FTC action unless combined with other violations.</p>

<h2>Canada - CASL (2014)</h2>
<p>Strictest major commercial email law. Requires <strong>prior consent</strong> (express or implied) in most cases.</p>

<h3>Implied consent</h3>
<p>Can be claimed in limited B2B scenarios:</p>
<ul>
  <li>Existing business relationship (past customer within 2 years)</li>
  <li>Inquiry made within last 6 months</li>
  <li>Published business email address without a "no CEMs" notice</li>
</ul>

<h3>The B2B exemption</h3>
<p>As of 2017, email between organizations is exempt from some CASL requirements if:</p>
<ul>
  <li>Both parties are engaged in commercial activity</li>
  <li>Message is relevant to recipient's role</li>
  <li>Organizations have existing business relationship</li>
</ul>

<p>In practice: targeting a business-role email at a Canadian company with a relevant offer has legal paths. Targeting personal addresses of Canadians does not.</p>

<h3>Penalties</h3>
<p>Up to $1M per violation for individuals, $10M for organizations. Private right of action available.</p>

<h2>European Union - GDPR + ePrivacy Directive</h2>

<h3>GDPR</h3>
<p>Cold email to EU individuals requires a lawful basis for processing personal data. Options:</p>
<ul>
  <li><strong>Consent</strong>: prior opt-in. Generally not available for cold.</li>
  <li><strong>Legitimate interest</strong>: the usual basis claimed for B2B cold email in the EU. Requires balancing test, transparency, and opt-out.</li>
</ul>

<h3>ePrivacy Directive (soft opt-in)</h3>
<p>Unsolicited commercial email to individuals generally requires consent. Business-to-business allowances vary by member state:</p>
<ul>
  <li>Germany: strict - consent required even for B2B</li>
  <li>UK (under PECR): legitimate interest OK for B2B corporate addresses</li>
  <li>France, Italy, Spain, Netherlands: varying</li>
</ul>

<h3>Practical B2B approach for EU</h3>
<ul>
  <li>Target corporate-role email addresses (not personal)</li>
  <li>Document legitimate interest rationale</li>
  <li>Include clear opt-out + privacy policy link</li>
  <li>Honor unsubscribes immediately</li>
  <li>Do not target Germany without local legal advice</li>
</ul>

<h3>Penalties</h3>
<p>Up to 4% of global annual revenue or €20M. Enforcement varies by member state.</p>

<h2>United Kingdom - PECR + UK GDPR</h2>
<p>Post-Brexit, similar to EU. B2B cold email to corporate subscribers (companies, partnerships) has "soft opt-in" basis. B2B to sole traders and non-corporate businesses is treated like consumer email (requires consent).</p>

<h2>Australia - SPAM Act 2003</h2>
<p>Requires consent (express or inferred). Inferred consent available for business-relationship contexts. Strict unsubscribe requirements.</p>

<h2>The operator's compliance checklist</h2>
<p>To stay compliant across most jurisdictions with B2B cold email:</p>
<ol>
  <li>Target business email addresses, not personal</li>
  <li>Target companies that logically could use your service</li>
  <li>Personalize enough to demonstrate relevance</li>
  <li>Include a physical business address in every email</li>
  <li>Include a clear, working unsubscribe option</li>
  <li>Honor unsubscribes immediately (not 10 days)</li>
  <li>Maintain a global unsubscribe list across all sending tools</li>
  <li>Don't email recipients in jurisdictions where your approach isn't legal (Germany, especially)</li>
  <li>Keep records of opt-outs and targeting rationale</li>
  <li>Review your approach with an attorney annually or before major changes</li>
</ol>

<h2>What unsubscribe should look like</h2>
<p>Two acceptable patterns in cold B2B email:</p>

<h3>Explicit unsubscribe link</h3>
<p>"If you'd prefer I stop reaching out, unsubscribe here: [link]" - makes the email look like marketing, may hurt deliverability.</p>

<h3>Plain-language opt-out</h3>
<p>"If you're not the right person or prefer I don't reach out, just reply and let me know." Works in B2B, feels personal, doesn't trigger spam filters. Legally sufficient if you actually honor replies.</p>

<p>The plain-language version is more common in modern B2B cold. The explicit link is safer legally. Many teams use the plain-language version plus a physical address in the signature to satisfy CAN-SPAM.</p>

<h2>The "corporate subscriber" concept</h2>
<p>Many B2B-friendly exemptions hinge on emailing a "corporate subscriber" - i.e., a role at a company rather than a person. The address info@, sales@, or role-based addresses at a company are generally safer than personal addresses (firstname.lastname@). In practice, most cold email tools target firstname.lastname@, and this is the grey area most B2B cold operates in.</p>

<h2>The reputation risk beyond legality</h2>
<p>Even legal cold email can hurt your reputation if done carelessly. Legal compliance is the floor, not the ceiling. Respect recipients, stop when told, send less than you could, and prioritize quality of targeting over volume.</p>

<p style="margin-top:40px;">Next: <a href="when-it-works.html">When cold email works</a>.</p>
""",
    prev=("Cold email vs spam", "spam-vs-cold.html"),
    nxt=("When cold email works", "when-it-works.html"),
)


write_cold_page(
    slug="foundations/when-it-works",
    title="When cold email works",
    description="Cold email isn't universal. Here's the fit test - when it's the right channel and when it isn't.",
    reading_time=4,
    body_html=f"""
<p class="lede">Cold email works brilliantly for some businesses and fails reliably for others. The difference isn't tactics; it's fit. Before investing in infrastructure and list building, run the fit test.</p>

<h2>Where cold email excels</h2>

<h3>B2B with deal sizes above $3K ACV</h3>
<p>Cold email costs money: tools, data, labor, domain warming. For it to pay back, the lifetime value per closed deal needs to cover acquisition cost. Below $3K ACV, the math gets tight. Above $10K ACV, it's the highest-leverage channel most teams have.</p>

<h3>Clearly-defined ICPs</h3>
<p>When your ideal customer is findable by role and firmographics ("VP Sales at B2B SaaS companies with 50-200 employees in North America"), cold email scales. When your ICP is fuzzy ("decision-makers"), results collapse.</p>

<h3>Urgent, named problems</h3>
<p>Cold email works when you can pattern-match to a specific pain the prospect already feels. "You're running paid ads at $150 CAC, we cut ours to $45" works because the pain is named. "We have an AI platform that helps teams collaborate" doesn't, because there's no specific problem being addressed.</p>

<h3>Short decision cycles</h3>
<p>If a prospect can decide to engage in weeks rather than years, cold email produces pipeline at usable velocity. For multi-year sales cycles (enterprise deals with 18-month procurement), cold email is a top-of-funnel touch that won't close anything alone.</p>

<h3>Markets where LinkedIn and trade publications identify decision-makers</h3>
<p>Cold email requires email addresses. Markets where Sales Navigator and enrichment tools work well (tech, SaaS, marketing, services, finance) are easy to target. Markets where the buyer is harder to identify (contractors, local SMBs, specific trades) are harder.</p>

<h2>Where cold email struggles</h2>

<h3>Pure B2C</h3>
<p>Consumer email outreach is illegal in most jurisdictions without consent. And even where legal, consumer gmail accounts have stricter spam filtering than corporate inboxes.</p>

<h3>Small-ticket products</h3>
<p>A $49/month tool can't afford CAC that includes cold email costs. Self-serve signup via paid or content is better.</p>

<h3>Commodity offers</h3>
<p>If what you sell is indistinguishable from 20 competitors, the prospect has no reason to engage with your cold email over the other 19.</p>

<h3>Vague or awareness-stage offers</h3>
<p>If your offer requires 45 minutes of education before the value is clear, cold email can't do that work. You need a content or paid ads path that educates first, then cold can pick up in-market prospects.</p>

<h3>Regulated industries with strict outreach rules</h3>
<p>Healthcare, financial advising, and legal services have additional regulations beyond general email law. Cold email may still work but requires industry-specific legal review.</p>

<h3>Hyper-local services</h3>
<p>A plumber serving one ZIP code won't build a business on cold email. The targeting overhead exceeds the deal value.</p>

<h2>The fit matrix</h2>
<p>Score your business on:</p>
<ol>
  <li>ACV above $3K?</li>
  <li>Can you name the ICP by role, company size, and industry?</li>
  <li>Is the pain you solve specific and identifiable in advance?</li>
  <li>Can prospects be identified via LinkedIn or enrichment tools?</li>
  <li>Decision cycle under 6 months?</li>
  <li>Target is business, not consumer?</li>
</ol>

<p>6/6: cold email should be your primary channel.</p>
<p>4-5/6: cold email will work, may need to complement with content or paid.</p>
<p>2-3/6: cold email is a secondary channel, not a primary bet.</p>
<p>0-1/6: use other channels.</p>

<h2>The hidden prerequisites</h2>
<p>Beyond fit, cold email requires:</p>
<ul>
  <li><strong>Offer clarity.</strong> You can articulate why someone would care in 2-3 sentences.</li>
  <li><strong>Proof.</strong> Case studies, logos, or specific results. Cold prospects are maximally skeptical.</li>
  <li><strong>Capacity to handle replies.</strong> If you generate 30 booked meetings/week and can only handle 5, you're wasting leads.</li>
  <li><strong>Patience.</strong> A campaign takes 6-12 weeks to show true performance after infrastructure setup.</li>
</ul>

<h2>The alternatives when cold email isn't the right fit</h2>
<p>If the fit test says no, you're still in the <a href="{DR_LINK}/leads/core-four.html">core four</a>:</p>
<ul>
  <li><strong><a href="{DR_LINK}/leads/warm-outreach.html">Warm outreach</a></strong>: smaller volume but higher conversion</li>
  <li><strong>Content</strong>: slow to build but compounds</li>
  <li><strong><a href="{DR_LINK}/leads/paid-ads.html">Paid ads</a></strong>: faster if unit economics work</li>
</ul>

<p>Cold email is one tool. Use it where it fits. Don't force it where it doesn't.</p>

<h2>The time investment reality</h2>
<p>Most teams underestimate the setup cost of cold email:</p>
<ul>
  <li>Domain setup and DNS: 1 day</li>
  <li>Warming new inboxes: 2-4 weeks before real volume</li>
  <li>List building and verification: ongoing, but 1-2 weeks for initial launch list</li>
  <li>Copy testing: 2-4 weeks to find what works</li>
  <li>Sequence iteration: ongoing</li>
</ul>

<p>Budget 4-8 weeks from "let's start cold email" to "first meetings booked." Teams that expect week-1 results usually give up before the system ramps.</p>

<p style="margin-top:40px;">Next: <a href="../deliverability/why-it-matters.html">Why deliverability is everything</a>.</p>
""",
    prev=("Legal landscape", "legal.html"),
    nxt=("Why deliverability is everything", "../deliverability/why-it-matters.html"),
)


# ============================================================
# DELIVERABILITY (7 pages)
# ============================================================

write_cold_page(
    slug="deliverability/why-it-matters",
    title="Why deliverability is everything",
    description="You can have the best list, best copy, and best offer. If your emails land in spam, none of it matters. Deliverability is the first and most important lever.",
    reading_time=5,
    body_html="""
<p class="lede">Most teams running cold email don't know their actual inbox placement rate. They measure opens and replies and assume the rest is fine. It usually isn't. You can have the best copy in the world, but if 60% of your emails land in spam, you're working at 40% capacity with no way to tell.</p>

<h2>The scale of the problem</h2>
<p>Typical outcomes across teams:</p>
<ul>
  <li>Well-configured campaigns: 80-95% inbox placement</li>
  <li>Average campaigns: 50-70% inbox placement</li>
  <li>Naive campaigns with no deliverability work: 20-40% inbox placement</li>
  <li>Damaged domains: under 10%</li>
</ul>

<p>A naive team thinks their campaign produces 2% reply rate. In reality it's 2% reply rate on the 30% that actually reached the inbox. The underlying offer may produce 6% on the full audience.</p>

<h2>The four layers of deliverability</h2>

<h3>1. Technical setup</h3>
<p>DNS records (SPF, DKIM, DMARC). Sending domains separated from your primary domain. Proper MX and reverse DNS.</p>

<p>See <a href="dns.html">SPF, DKIM, DMARC</a> and <a href="sending-domains.html">sending domain strategy</a>.</p>

<h3>2. Sender reputation</h3>
<p>IP reputation, domain age, sending history, recipient engagement. Built over weeks of gradual volume and good behavior.</p>

<p>See <a href="ip-reputation.html">IP reputation</a> and <a href="warming.html">inbox warming</a>.</p>

<h3>3. Content</h3>
<p>Email content itself triggers filters. Too many links, spam-trigger phrases, image-only emails, overly HTML-heavy messages.</p>

<p>See <a href="spam-triggers.html">content that triggers spam filters</a>.</p>

<h3>4. Behavior signals</h3>
<p>Recipients who mark as spam, delete without reading, never open. These hurt reputation. Replies, forwards, and reads help.</p>

<h2>Why provider filtering is aggressive</h2>
<p>Gmail, Outlook, and other providers process trillions of emails daily. They use machine learning to classify. The models look for:</p>
<ul>
  <li>Sender reputation signals</li>
  <li>Content patterns matching known spam</li>
  <li>Volume anomalies</li>
  <li>Authentication failures</li>
  <li>Recipient signals (complaints, delete rates, engagement)</li>
</ul>

<p>The filters are not your friend, but they're not malicious. They're optimizing for their users' satisfaction. Your job is to look like a legitimate sender, consistently.</p>

<h2>The gmail primary vs promotions vs spam split</h2>
<p>Gmail has three outcomes for your email:</p>
<ol>
  <li><strong>Primary inbox</strong>: ideal. User sees it immediately.</li>
  <li><strong>Promotions tab</strong>: less ideal. User may check it but with lower intent.</li>
  <li><strong>Spam folder</strong>: invisible. User almost never checks.</li>
</ol>

<p>Cold email wants Primary placement. Promotions placement for a sales email is nearly as bad as spam for reply rate. Don't use promotional language, avoid excessive HTML/styling, and write like a real person writing to one recipient.</p>

<h2>What bad deliverability actually costs</h2>
<p>Consider a campaign with:</p>
<ul>
  <li>10,000 emails sent</li>
  <li>3% reply rate (targeted)</li>
  <li>20% positive reply rate among replies</li>
</ul>

<p>At 90% inbox placement: 300 replies, 60 positive responses.</p>
<p>At 40% inbox placement: 120 replies, 24 positive responses.</p>

<p>Same offer, same copy, same list. 60% of results lost to deliverability.</p>

<p>Over a year at scale, this is a life-or-death difference for a B2B company.</p>

<h2>The damaging feedback loop</h2>
<p>Bad deliverability creates a downward spiral:</p>
<ol>
  <li>Your emails land in spam</li>
  <li>Recipients don't see them, so nobody opens or replies</li>
  <li>Low engagement = worse reputation</li>
  <li>Worse reputation = more spam placement</li>
  <li>Eventually your sending domain is effectively dead</li>
</ol>

<p>This is why you can't "blast first, fix later." Once you've damaged a domain, recovery is painful - often cheaper to start over with new domains.</p>

<h2>The build-it-right-the-first-time approach</h2>
<p>The sequence that works:</p>
<ol>
  <li>Buy and configure dedicated sending domains</li>
  <li>Set up SPF, DKIM, DMARC properly</li>
  <li>Create mailboxes (usually 2-5 per domain)</li>
  <li>Warm each mailbox for 2-4 weeks before real sending</li>
  <li>Verify every email address before sending to it</li>
  <li>Start at low volume (20-30/day per mailbox) and scale gradually</li>
  <li>Monitor inbox placement continuously</li>
  <li>Rest and rotate mailboxes to prevent fatigue</li>
</ol>

<p>This section covers all of it. Skipping any step is how campaigns break.</p>

<h2>The one-minute deliverability check</h2>
<p>Right now, for any domain you're sending from:</p>
<ol>
  <li>Check MXToolbox or dmarcian for your SPF record (should pass)</li>
  <li>Check that DKIM is configured and passing</li>
  <li>Check your DMARC policy (should be at least p=none with reporting)</li>
  <li>Send a test email to mail-tester.com and check the score (aim for 10/10)</li>
  <li>Send a test to a Gmail address and check placement (Primary? Promotions? Spam?)</li>
</ol>

<p>If any of these fail, you have a deliverability problem. Stop sending cold email until you fix it.</p>

<p style="margin-top:40px;">Next: <a href="dns.html">SPF, DKIM, DMARC</a>.</p>
""",
    prev=("When cold email works", "../foundations/when-it-works.html"),
    nxt=("SPF, DKIM, DMARC", "dns.html"),
)


write_cold_page(
    slug="deliverability/dns",
    title="SPF, DKIM, DMARC",
    description="The three DNS records that tell receiving servers your email is legitimate. Here's exactly how to configure each and what breaks when you don't.",
    reading_time=5,
    body_html="""
<p class="lede">SPF, DKIM, and DMARC are DNS records that prove your email is actually from your domain. Without them, modern email providers treat your messages as suspicious. Proper configuration is a 20-minute task that most teams do wrong or not at all.</p>

<h2>SPF (Sender Policy Framework)</h2>

<h3>What it does</h3>
<p>Lists the servers authorized to send email on behalf of your domain. A TXT record on your domain that says "email from these IPs or hosts is legitimate."</p>

<h3>What it looks like</h3>
<pre style="background:#f5f5f7; padding:12px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
v=spf1 include:_spf.google.com include:sendgrid.net ~all
</pre>

<p>This says: Google Workspace's servers and SendGrid's servers can send from this domain. Everything else is "soft-fail" (flag but don't reject).</p>

<h3>Common misconfigurations</h3>
<ul>
  <li>Missing SPF entirely</li>
  <li>Multiple SPF records on same domain (must be one)</li>
  <li>SPF permerror from too many DNS lookups (over 10 = broken)</li>
  <li>Missing include for your sending tool</li>
  <li>Using -all (hard fail) without all senders included, causing legitimate mail to bounce</li>
</ul>

<h3>Setup</h3>
<p>Your sending tool (Instantly, Smartlead, whatever) will tell you what to include. Your email host (Google Workspace, Microsoft 365) will give you their include. Combine them in one record.</p>

<h2>DKIM (DomainKeys Identified Mail)</h2>

<h3>What it does</h3>
<p>Cryptographically signs every outgoing email with a key only your domain controls. Receiving servers verify the signature using a public key published in your DNS.</p>

<p>Provides two things: proof that the email really came from your domain, and proof it wasn't tampered with in transit.</p>

<h3>What it looks like</h3>
<p>A TXT record at a specific subdomain (typically <code>selector._domainkey.yourdomain.com</code>) containing the public key:</p>

<pre style="background:#f5f5f7; padding:12px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:12px;">
v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEB...[long key]...
</pre>

<h3>Setup</h3>
<p>Your sending tool generates the key and gives you the DNS record. You publish it. Most tools support this automatically for their sending domains.</p>

<h3>Common misconfigurations</h3>
<ul>
  <li>Missing DKIM</li>
  <li>Key not published or published on wrong subdomain</li>
  <li>Key rotated but old key still in DNS</li>
  <li>Multiple DKIM selectors for different tools (this is fine, but easy to mess up)</li>
</ul>

<h2>DMARC (Domain-based Message Authentication, Reporting, and Conformance)</h2>

<h3>What it does</h3>
<p>Tells receiving servers what to do with emails that fail SPF or DKIM checks. Also provides reporting so you can see who's sending as your domain.</p>

<h3>What it looks like</h3>
<pre style="background:#f5f5f7; padding:12px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
v=DMARC1; p=none; rua=mailto:dmarc-reports@yourdomain.com; pct=100
</pre>

<h3>The three policy levels</h3>
<ul>
  <li><strong>p=none</strong>: monitor only, don't reject. Start here.</li>
  <li><strong>p=quarantine</strong>: send failing mail to spam. Move here after you've validated all legitimate senders.</li>
  <li><strong>p=reject</strong>: reject failing mail outright. Strictest. Major brands use this to prevent spoofing.</li>
</ul>

<h3>Setup progression</h3>
<p>Month 1: publish DMARC with p=none and rua reporting. Watch who's sending as you.</p>
<p>Month 2-3: identify any legitimate senders failing SPF/DKIM. Fix.</p>
<p>Month 4+: move to p=quarantine, then p=reject once you're confident.</p>

<p>Many domains stay at p=none forever. For cold email sending domains, p=none is sufficient; the key benefit is authentication passing, not the policy enforcement.</p>

<h2>The full setup checklist</h2>
<ol>
  <li>Own the domain you're sending from</li>
  <li>SPF record published, includes all sending tools</li>
  <li>DKIM configured for each sending tool, public key published in DNS</li>
  <li>DMARC record with at least p=none and rua reporting</li>
  <li>Verify all three pass by sending a test to mail-tester.com</li>
  <li>Verify at Google Postmaster Tools (for Gmail delivery signals)</li>
  <li>Check at MXToolbox or dmarcian for any configuration issues</li>
</ol>

<h2>Common pitfalls by email provider</h2>

<h3>Google Workspace</h3>
<p>Default DKIM is disabled. You must enable it explicitly in admin console. Most workspaces don't.</p>

<h3>Microsoft 365</h3>
<p>SPF is configured automatically but DKIM requires explicit enablement per domain.</p>

<h3>External sending tools (SendGrid, Mailgun, SES, Postmark)</h3>
<p>Each requires its own DNS setup. Your SPF includes them; they each publish DKIM on your domain via CNAME or TXT records.</p>

<h3>Cold email tools (Instantly, Smartlead)</h3>
<p>These tools usually connect to mailboxes you own (via Google Workspace or Outlook). The DKIM and SPF you set up for the mailbox provider is what matters. The cold email tool just sends through your existing mailbox.</p>

<h2>BIMI (bonus, not required)</h2>
<p>Brand Indicators for Message Identification: displays your logo next to emails in supporting clients. Requires DMARC at p=quarantine or stricter plus a verified mark certificate. Nice-to-have, not relevant for most cold email.</p>

<h2>The real-time check</h2>
<p>Before sending anything, send a test email from the domain to mail-tester.com. Score should be 9+/10. If under, your configuration has problems. Fix before sending to real prospects.</p>

<p>Also check at Google Postmaster Tools (postmaster.google.com) after you've sent some volume. Provides spam rate, domain reputation, IP reputation, and authentication pass rates for Gmail specifically.</p>

<p style="margin-top:40px;">Next: <a href="sending-domains.html">Sending domain strategy</a>.</p>
""",
    prev=("Why deliverability is everything", "why-it-matters.html"),
    nxt=("Sending domain strategy", "sending-domains.html"),
)


write_cold_page(
    slug="deliverability/sending-domains",
    title="Sending domain strategy",
    description="Never send cold email from your primary domain. Here's the sending-domain architecture that protects your brand and scales safely.",
    reading_time=5,
    body_html="""
<p class="lede">The first rule of sending cold email at volume: never do it from your primary domain. If your cold campaign damages a domain's reputation, your transactional and sales emails from that domain suffer too. The architecture that protects you: dedicated sending domains, with your brand domain completely separate.</p>

<h2>The anti-pattern</h2>
<p>"Let's send cold email from sam@yourcompany.com because it has credibility."</p>
<p>Two months later: your CEO's emails are landing in spam. Your customer onboarding emails go to promotions. Your domain reputation is wrecked. Fixing it takes months.</p>

<p>This happens to every team that doesn't separate sending domains. Don't be them.</p>

<h2>The domain architecture</h2>

<h3>Primary domain</h3>
<p>Your brand: <code>yourcompany.com</code>. Used for:</p>
<ul>
  <li>Your website</li>
  <li>Transactional emails (signup, password reset)</li>
  <li>One-to-one business email (from known addresses, to known addresses)</li>
</ul>

<p>This domain should never send cold outreach at volume.</p>

<h3>Sending domains</h3>
<p>Additional domains purchased specifically for cold email: <code>yourcompany.io</code>, <code>getyourcompany.com</code>, <code>try-yourcompany.com</code>, <code>yourcompany-team.com</code>, etc.</p>

<p>Each sending domain:</p>
<ul>
  <li>Points to your brand (has a redirect to yourcompany.com, mentions "yourcompany" so recipients trust it)</li>
  <li>Has its own DNS setup (SPF, DKIM, DMARC)</li>
  <li>Hosts 1-5 mailboxes</li>
  <li>Sends at low volume per mailbox (20-50/day)</li>
</ul>

<h2>Why multiple domains</h2>
<p>One domain hits a per-domain sending ceiling (~1000-2000 emails/day before reputation starts degrading). Multiple domains let you scale horizontally.</p>

<p>Example: you want to send 1000 emails/day. You could use:</p>
<ul>
  <li>1 domain with 30 mailboxes sending 30-35/day each</li>
  <li>5 domains with 5 mailboxes each, sending 40/day</li>
  <li>10 domains with 3 mailboxes each, sending 35/day</li>
</ul>

<p>More domains = lower per-domain volume = better reputation = better deliverability. Cost: domain registration (usually $10-20/year each) and slightly more setup work.</p>

<h2>Domain naming</h2>

<h3>Do</h3>
<ul>
  <li>Variations of your brand: <code>getyourcompany.com</code>, <code>yourcompany.io</code>, <code>yourcompany-co.com</code></li>
  <li>Industry-relevant: <code>yourcompanyhq.com</code></li>
  <li>Short, memorable</li>
  <li>Redirect to your main site when visited</li>
</ul>

<h3>Don't</h3>
<ul>
  <li>Completely unrelated names that look like spoofing</li>
  <li>Misspellings of your brand (looks deceptive)</li>
  <li>Hyphens and numbers that look spammy (<code>your-company-2026.com</code>)</li>
  <li>Free domains (.tk, .ml etc.) - spam-tier from day one</li>
</ul>

<h2>The mailbox-per-domain ratio</h2>
<p>Best practices in 2026:</p>
<ul>
  <li>2-5 mailboxes per domain</li>
  <li>30-50 emails/day per mailbox</li>
  <li>150-250 emails/day per domain (total)</li>
</ul>

<p>Going above 500/day per domain accelerates reputation burn. Below 20/day per mailbox means you're paying for infrastructure you're not using.</p>

<h2>Domain age matters</h2>
<p>New domains are treated with suspicion for 2-4 weeks. Brand-new domains sending cold mail on day 1 get filtered aggressively.</p>

<p>Two patterns:</p>
<ul>
  <li><strong>Buy fresh, warm slowly</strong>: register domain, set up DNS, start warming mailboxes immediately but send cold volume only after 4+ weeks</li>
  <li><strong>Buy aged domains</strong>: purchase domains that have been registered for 6+ months (with clean history). More expensive but ready faster</li>
</ul>

<p>Most teams use fresh domains with proper warming. Aged domains are the exception for urgent launches.</p>

<h2>Redirects and brand trust</h2>
<p>When a prospect clicks your signature link or Googles the sending domain, they should land somewhere that looks legit. Minimum setup:</p>
<ul>
  <li>Sending domain redirects to your main site (301 redirect)</li>
  <li>Or a minimal landing page at the sending domain explaining "this is [yourcompany]'s outbound domain, main site is at yourcompany.com"</li>
</ul>

<p>A bare sending domain with no website is a red flag to sophisticated recipients.</p>

<h2>Workspace vs individual inbox</h2>
<p>Each sending domain needs email hosting. Two options:</p>

<h3>Google Workspace</h3>
<ul>
  <li>$6-18/user/month</li>
  <li>High deliverability to Gmail recipients (sender reputation boost)</li>
  <li>Easy to configure</li>
  <li>Standard for most cold email operators</li>
</ul>

<h3>Microsoft 365</h3>
<ul>
  <li>$6-22/user/month</li>
  <li>Strong for Outlook recipients</li>
  <li>Sometimes required for enterprise-facing campaigns</li>
</ul>

<h3>Dedicated SMTP providers</h3>
<p>(SendGrid, Mailgun, Amazon SES, Postmark)</p>
<ul>
  <li>Much cheaper at scale</li>
  <li>Lower deliverability to Gmail for cold</li>
  <li>Not recommended as primary cold-email infrastructure</li>
  <li>Fine for transactional, bad for cold outreach</li>
</ul>

<p>For cold email in 2026: use Google Workspace primarily, Microsoft 365 when targeting Outlook-heavy audiences.</p>

<h2>The launch cost math</h2>
<p>For a mid-sized cold operation targeting 1000-2000 emails/day:</p>
<ul>
  <li>10 domains × $15/year = $150/year</li>
  <li>30 Google Workspace mailboxes × $6/month = $2,160/year</li>
  <li>Cold email tool (Instantly, Smartlead): $100-500/month</li>
  <li>Warming tool: $50-200/month (often bundled)</li>
  <li>Data (Apollo, Clay): $300-1000/month</li>
</ul>

<p>Total: ~$800-2500/month for a full operation. The mailboxes are the biggest line item.</p>

<h2>The subdomain question</h2>
<p>Can you use subdomains (<code>outbound.yourcompany.com</code>) instead of separate root domains?</p>
<p>Technically yes, but subdomain reputation partially ties to root domain reputation. If outbound subdomain gets flagged, it can contaminate yourcompany.com's reputation. Use separate root domains instead.</p>

<h2>The checklist for a new sending domain</h2>
<ol>
  <li>Register the domain</li>
  <li>Set up DNS (use Cloudflare or similar for fast propagation)</li>
  <li>Add SPF, DKIM, DMARC records</li>
  <li>Configure email host (Google Workspace / Microsoft 365)</li>
  <li>Enable DKIM in the email host</li>
  <li>Set up redirect to your main site</li>
  <li>Create mailboxes</li>
  <li>Start warming each mailbox</li>
  <li>Wait 3-4 weeks before sending real volume</li>
  <li>Monitor Postmaster Tools and mail-tester scores</li>
</ol>

<p style="margin-top:40px;">Next: <a href="warming.html">Inbox warming</a>.</p>
""",
    prev=("SPF, DKIM, DMARC", "dns.html"),
    nxt=("Inbox warming", "warming.html"),
)


write_cold_page(
    slug="deliverability/warming",
    title="Inbox warming",
    description="A new mailbox is a new stranger to email providers. Warming teaches them that you're a real sender. Here's how it works and why you can't skip it.",
    reading_time=4,
    body_html="""
<p class="lede">A brand-new mailbox has zero sending reputation. If you fire off 50 cold emails on day one, 90% will land in spam and the mailbox's reputation is damaged before it started. Warming is the process of gradually building up legitimate sending volume and engagement signals before doing real work.</p>

<h2>What warming does</h2>
<p>Warming simulates the behavior of a real human using the inbox:</p>
<ul>
  <li>Sending modest volume to other warmed mailboxes</li>
  <li>Receiving reply-like interactions</li>
  <li>Getting emails marked as "not spam" when they accidentally go to spam</li>
  <li>Getting opens, replies, and forwards</li>
  <li>Gradual ramp-up over days and weeks</li>
</ul>

<p>This builds sender reputation at Google, Microsoft, and other providers. By week 4, your mailbox looks like an established sender, not a brand-new one.</p>

<h2>How warming tools work</h2>
<p>You connect your new mailbox to a warming tool (Mailwarm, Warmy, Instantly's built-in warming, Smartlead's built-in warming). The tool:</p>
<ol>
  <li>Connects your mailbox to a network of other warmed mailboxes</li>
  <li>Sends small numbers of automated "warming" emails</li>
  <li>Has those emails auto-replied to by the network</li>
  <li>Auto-marks warming emails as "not spam" if they land in spam</li>
  <li>Gradually increases volume day by day</li>
</ol>

<p>The whole process is invisible to you - you set it up, it runs for 2-4 weeks, your mailbox is ready.</p>

<h2>The warming schedule</h2>
<p>A reasonable ramp for a new Google Workspace mailbox:</p>

<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
Week 1: 5 warming emails/day
Week 2: 15/day
Week 3: 25/day
Week 4: 35/day
Week 5+: 40-50/day, sustained

Real cold email sending can start in week 4-5, at low volume,
ramping up while warming continues in background.
</pre>

<h2>The golden rule: don't skip</h2>
<p>Every team that skips warming regrets it. "We're in a rush" → emails land in spam → reply rates are terrible → you can't tell if it's copy, list, or deliverability → domain is damaged and recovery takes months.</p>

<p>Warming is 3-4 weeks of patience that saves 3-4 months of debugging.</p>

<h2>Continuous warming</h2>
<p>Warming isn't a one-time thing. Most cold email operators run warming continuously - even on production mailboxes - to offset the reputation hit of cold sending.</p>

<p>The pattern:</p>
<ul>
  <li>Each mailbox sends ~30-40 real cold emails/day</li>
  <li>Plus 10-20 warming emails/day in background</li>
  <li>Total mailbox volume: 40-60/day</li>
</ul>

<p>The warming helps neutralize the reputation pressure from cold sends.</p>

<h2>The engagement signal</h2>
<p>Warming isn't just about volume - it's about engagement. Email providers care about:</p>
<ul>
  <li>Emails that get opened</li>
  <li>Emails that get replied to</li>
  <li>Emails moved from spam to inbox</li>
  <li>Forwards</li>
</ul>

<p>Warming tools simulate all of these. Your warming emails get high engagement rates from the warming network.</p>

<h2>When to pause warming</h2>
<p>A few cases:</p>
<ul>
  <li>When your actual cold emails are showing strong engagement and you want to reduce noise in your inbox</li>
  <li>When you're taking a mailbox offline</li>
  <li>When testing a new creative and you want cleaner signal</li>
</ul>

<p>Most operators leave warming running all the time. The cost is low and the benefit is a steady reputation buffer.</p>

<h2>Warming tool comparison</h2>

<h3>Instantly (built-in)</h3>
<p>Instantly's warming network is large and free with the platform. Most common default. Works well for most operators.</p>

<h3>Smartlead (built-in)</h3>
<p>Similar; bundled with Smartlead accounts.</p>

<h3>Mailwarm / Warmy (standalone)</h3>
<p>Dedicated warming-only tools. More expensive standalone but sometimes better warming quality. Used when operators want warming separate from sending tools.</p>

<h3>TrulyInbox / Warmup Inbox</h3>
<p>Similar standalone options. Competitive features.</p>

<h2>Common warming mistakes</h2>

<h3>Skipping warming entirely</h3>
<p>Already covered. Most common, most costly.</p>

<h3>Warming but sending real cold volume too soon</h3>
<p>3-4 weeks of warming minimum. A week isn't enough.</p>

<h3>Jumping to high daily volume too fast</h3>
<p>Even after warming, start cold volume low (5-10/day) and ramp over the first week of real sending. Sudden volume spikes trigger reputation flags.</p>

<h3>Using a warming network that sends to known spammy mailboxes</h3>
<p>Cheap warming services sometimes include low-quality mailboxes in their network. Stick to reputable tools (Instantly, Smartlead, Mailwarm).</p>

<h3>Warming across different providers without understanding the signals</h3>
<p>Warming to Gmail-only helps Gmail reputation. Warming to a mix (Gmail + Outlook + custom domains) helps broader reputation. Reputable tools handle this automatically.</p>

<h2>The ongoing health check</h2>
<p>After warming, spot-check mailbox health:</p>
<ul>
  <li>Send a test email from the mailbox to mail-tester.com - expect 9+/10</li>
  <li>Send to a personal Gmail - check it lands in Primary</li>
  <li>Check Postmaster Tools for the domain - green across spam rate, reputation, authentication</li>
  <li>If any of these degrade, investigate before scaling volume</li>
</ul>

<p>Warming puts you on the starting line. Continuous monitoring keeps you there.</p>

<p style="margin-top:40px;">Next: <a href="ip-reputation.html">IP reputation</a>.</p>
""",
    prev=("Sending domain strategy", "sending-domains.html"),
    nxt=("IP reputation", "ip-reputation.html"),
)


write_cold_page(
    slug="deliverability/ip-reputation",
    title="IP reputation",
    description="Every IP has a reputation score with every email provider. Here's what affects it and how shared vs dedicated IPs change your strategy.",
    reading_time=4,
    body_html="""
<p class="lede">IP reputation is a per-IP score that email providers maintain. It influences whether messages from that IP get inbox placement, promotions placement, or spam folder. Understanding shared vs dedicated IPs and how reputation builds changes how you architect sending.</p>

<h2>How IP reputation is built</h2>
<p>Gmail, Outlook, and others track every sending IP's:</p>
<ul>
  <li>Volume over time (sudden spikes look spammy)</li>
  <li>Bounce rate (high bounces = bad list)</li>
  <li>Complaint rate (high complaints = spam)</li>
  <li>Engagement (opens, replies, forwards)</li>
  <li>Unsubscribe rate</li>
  <li>Content patterns</li>
  <li>Authentication pass rate</li>
</ul>

<p>The score is invisible to you. What you see: inbox placement dropping, spam rate rising, Postmaster Tools showing reputation at "Low" or "Bad."</p>

<h2>Shared vs dedicated IPs</h2>

<h3>Shared IP (default for most cold email)</h3>
<p>When you use Google Workspace, Microsoft 365, or most cold email tools, your outbound traffic goes through IPs shared with other senders. The provider manages the pool.</p>

<p>Pros:</p>
<ul>
  <li>No setup</li>
  <li>Reputation is established (assuming the pool is well-managed)</li>
  <li>Lower volume per sender = less likely to hit rate limits</li>
</ul>

<p>Cons:</p>
<ul>
  <li>Your reputation is partly tied to other senders in the pool</li>
  <li>If a major spammer uses the same pool, you suffer</li>
  <li>You have no direct control</li>
</ul>

<p>For Google Workspace mailboxes sending cold email, you're on shared IPs and generally that's fine. Google's pool management is strong.</p>

<h3>Dedicated IP (SMTP providers, high volume)</h3>
<p>Paid SMTP providers (SendGrid, Mailgun, SES with dedicated IP) give you an IP used only by you. Your reputation is entirely your own.</p>

<p>Pros:</p>
<ul>
  <li>Your reputation is purely a function of your behavior</li>
  <li>No contamination from other senders</li>
  <li>Higher volume ceilings</li>
</ul>

<p>Cons:</p>
<ul>
  <li>Starts with zero reputation - must warm like a new mailbox</li>
  <li>Requires sustained volume to maintain reputation (low volume = slow degradation)</li>
  <li>Higher cost</li>
  <li>More operational complexity</li>
</ul>

<p>Dedicated IPs make sense when you're sending 50K+ emails/day from one system. For typical cold email operations (1000-5000/day across 10 mailboxes), shared IPs are usually fine.</p>

<h2>The cold email reality in 2026</h2>
<p>Most successful cold email operations use:</p>
<ul>
  <li>Google Workspace or Microsoft 365 (shared IP, managed by provider)</li>
  <li>Multiple mailboxes across multiple domains</li>
  <li>Volume capped at ~30-50/day per mailbox</li>
  <li>Warming running continuously</li>
</ul>

<p>This approach doesn't need dedicated IPs. The complexity would outweigh the benefit.</p>

<h2>IP reputation vs domain reputation</h2>
<p>Both exist. They're related but distinct:</p>
<ul>
  <li>IP reputation: about the sending server</li>
  <li>Domain reputation: about your from-domain</li>
</ul>

<p>Gmail weights domain reputation heavily. Outlook/Microsoft weights IP reputation heavily. Both matter. Bad behavior damages both.</p>

<h2>How to check IP reputation</h2>
<ul>
  <li><strong>Google Postmaster Tools</strong>: shows IP and domain reputation for Gmail</li>
  <li><strong>Microsoft SNDS (Smart Network Data Services)</strong>: shows IP reputation for Outlook/Hotmail</li>
  <li><strong>Talos Intelligence</strong>: Cisco's database, shows IP reputation</li>
  <li><strong>MXToolbox blacklist check</strong>: shows if the IP is listed on spam blacklists</li>
  <li><strong>Spamhaus</strong>: the most-respected spam blacklist database</li>
</ul>

<h2>Blacklists</h2>
<p>Being on a blacklist means some providers will reject or filter emails from that IP or domain. Major blacklists:</p>
<ul>
  <li>Spamhaus (SBL, XBL, PBL, CSS)</li>
  <li>Barracuda</li>
  <li>SpamCop</li>
  <li>Invaluement</li>
  <li>SORBS</li>
</ul>

<p>If you end up on a blacklist, follow the de-listing process for that service. It's usually free but slow (days to weeks). Prevention is much cheaper than recovery: maintain low bounce rates, low complaint rates, and clean lists.</p>

<h2>How to protect IP reputation</h2>
<p>The list is short:</p>
<ul>
  <li>Verify every email address before sending</li>
  <li>Keep bounce rate under 2%</li>
  <li>Keep complaint rate under 0.1%</li>
  <li>Remove unengaged recipients after ~3-6 months of no interaction</li>
  <li>Honor unsubscribes immediately</li>
  <li>Don't buy lists of unknown quality</li>
  <li>Don't send to role-based addresses (info@, sales@) that often get complained about</li>
  <li>Don't send from new IPs/domains without warming</li>
  <li>Maintain consistent volume (don't spike)</li>
</ul>

<h2>When IP reputation damages you</h2>
<p>Signs your IP reputation is suffering:</p>
<ul>
  <li>Open rates dropping week over week with no copy change</li>
  <li>Reply rates dropping</li>
  <li>Postmaster Tools showing "Low" or "Bad" reputation</li>
  <li>Bounces climbing even though list quality is same</li>
  <li>Spam folder placement rising (check mail-tester or seed addresses)</li>
</ul>

<p>Actions:</p>
<ol>
  <li>Pause cold sending for 1-2 weeks</li>
  <li>Continue warming to rebuild reputation</li>
  <li>Resume at 30-50% of previous volume</li>
  <li>If no recovery in 4-6 weeks, switch to new sending domains and mailboxes</li>
</ol>

<h2>The alternative: retire bad infrastructure</h2>
<p>If a domain or IP has been badly damaged, the fastest path forward is usually not to fix it - it's to switch to new infrastructure. Register a new domain, provision new mailboxes, warm them, resume.</p>

<p>This is why experienced operators always have a second set of domains ready. Infrastructure is disposable. Your offer, list, and copy are the durable assets.</p>

<p style="margin-top:40px;">Next: <a href="spam-triggers.html">Content that triggers spam filters</a>.</p>
""",
    prev=("Inbox warming", "warming.html"),
    nxt=("Content that triggers spam filters", "spam-triggers.html"),
)


write_cold_page(
    slug="deliverability/spam-triggers",
    title="Content that triggers spam filters",
    description="Spam filters read your content. Certain words, structures, and patterns immediately raise flags. Here's what to avoid and why.",
    reading_time=4,
    body_html="""
<p class="lede">Deliverability isn't only about infrastructure. Email content itself triggers filters. A well-authenticated, warmed, reputation-clean sender can still land in spam because of content patterns that match spam fingerprints. The safer your content, the better your placement.</p>

<h2>The two filter types</h2>

<h3>Bayesian / ML filters</h3>
<p>Look at the whole email and score likelihood of spam based on patterns learned from billions of examples. The more spam-like your content, the higher the score.</p>

<h3>Rule-based filters</h3>
<p>Check for specific flags: certain phrases, structural patterns, link ratios. Older but still active.</p>

<p>Both exist. Both matter.</p>

<h2>The phrases that flag</h2>

<h3>Money and urgency</h3>
<ul>
  <li>"Free," "FREE," "100% free"</li>
  <li>"Guaranteed," "risk-free"</li>
  <li>"Act now," "urgent," "limited time"</li>
  <li>"Click here," "click below," "click now"</li>
  <li>"Cash," "money back," "earn money"</li>
  <li>"$," "$$$," "cheap"</li>
  <li>"Hurry," "expires"</li>
</ul>

<h3>Sales-y language</h3>
<ul>
  <li>"Call now"</li>
  <li>"Don't miss"</li>
  <li>"Order today"</li>
  <li>"Special promotion"</li>
  <li>"Buy now"</li>
  <li>"Huge savings"</li>
</ul>

<h3>Generic openings</h3>
<ul>
  <li>"Dear friend"</li>
  <li>"Dear sir/madam"</li>
  <li>"To whom it may concern"</li>
</ul>

<h3>Overused cold email openers</h3>
<p>Ironically, patterns that became common in cold email are now flagged:</p>
<ul>
  <li>"Quick question"</li>
  <li>"Hope this finds you well"</li>
  <li>"I came across your profile"</li>
  <li>"Hope you're having a great week"</li>
</ul>

<p>These aren't always fatal, but overuse patterns them as templated outreach.</p>

<h2>Structural triggers</h2>

<h3>All caps</h3>
<p>"SAVE BIG NOW!" = instant spam signal. Use normal capitalization. Emphasis via bold is fine; all-caps isn't.</p>

<h3>Excessive punctuation</h3>
<p>"Click now!!!" Every extra punctuation mark adds spam score. One exclamation maximum per email.</p>

<h3>Too many links</h3>
<p>More than 2-3 links in a short cold email triggers filters. Especially bad: multiple links to different domains.</p>

<h3>Image-heavy emails</h3>
<p>An email that's 90% image with minimal text signals spam (images can hide spammy content from text-based filters). For cold email, stick to plain text or very light HTML.</p>

<h3>HTML-heavy templates</h3>
<p>A marketing-style HTML template (logo, images, multi-column layouts, footer graphics) signals bulk email. Cold email should look like a person typing a personal message.</p>

<h3>Link-to-text ratio</h3>
<p>If the ratio of link text to body text is high, filters flag it. A 40-word email with 5 links is suspicious. A 150-word email with 1 link is fine.</p>

<h3>URL shorteners</h3>
<p>bit.ly, tinyurl, even t.co in emails triggers filters (spammers use them to hide destinations). Use direct URLs.</p>

<h3>Tracking pixels and extensive tracking</h3>
<p>Single tracking pixel is fine. Multiple pixels, unusual tracking parameters, or obvious open-tracking can flag.</p>

<h2>The "natural" email test</h2>
<p>Write your cold email. Now imagine printing it and mailing it. Does it look like something a real person writes to another real person? Or does it look like a flyer?</p>

<p>If flyer: strip design, shorten, remove marketing language, make it plain text.</p>

<h2>Plain text vs HTML</h2>
<p>For cold B2B, plain text or very minimal HTML (one link, one bold emphasis) consistently outperforms designed HTML emails on:</p>
<ul>
  <li>Deliverability</li>
  <li>Open rate</li>
  <li>Reply rate</li>
</ul>

<p>The reason: plain text signals "person writing to me" not "marketing broadcast."</p>

<h2>Subject line triggers</h2>
<p>Subject lines are the first filter-check point. Triggers:</p>
<ul>
  <li>All caps</li>
  <li>Excessive punctuation</li>
  <li>Emojis (mixed - some filter networks flag them)</li>
  <li>Dollar signs</li>
  <li>Certain phrases ("free," "urgent," "limited offer")</li>
  <li>Too long (over 50 chars reduces open rate and can increase spam risk)</li>
</ul>

<p>See <a href="../copy/subject-lines.html">subject lines</a> for positive patterns.</p>

<h2>Attachment handling</h2>
<p>Attachments in cold email:</p>
<ul>
  <li>Increase spam likelihood significantly</li>
  <li>Executable attachments (zip, exe, .docm with macros) almost always land in spam</li>
  <li>Even PDFs trigger filters if size is large or sender is new</li>
</ul>

<p>Don't attach files to cold emails. If you need to share a document, link to a cloud-hosted version or mention you'll send it after reply.</p>

<h2>Spammy structures</h2>

<h3>Footer boilerplate</h3>
<p>Long legal disclaimers, unsubscribe instructions with multiple links, privacy policy boilerplate - mark emails as marketing-style. Keep footers brief: name, title, company, optional brief unsubscribe sentence.</p>

<h3>Identical messages at scale</h3>
<p>Sending the exact same email to thousands of recipients pattern-matches spam. Use spintax (variable text) to ensure each message is slightly different, even for the same campaign.</p>

<h3>Signature with too many links</h3>
<p>Signatures with LinkedIn, Twitter, website, phone, calendar - looks corporate/marketing. Simpler signatures win.</p>

<h2>Testing your content</h2>

<h3>Mail-tester.com</h3>
<p>Send your email to a given address. Get a score 1-10 with breakdown of issues. Aim for 9+.</p>

<h3>Gmass Inbox Inspector, GlockApps</h3>
<p>Test placement across multiple providers. Shows inbox/promotions/spam for each.</p>

<h3>Seed addresses</h3>
<p>Create test email addresses at Gmail, Outlook, Yahoo, etc. Add them to your test sends. Check placement for each.</p>

<h2>The spam-triggers checklist</h2>
<ol>
  <li>No ALL CAPS</li>
  <li>One exclamation max</li>
  <li>No free/urgent/click-now language</li>
  <li>No URL shorteners</li>
  <li>Plain text or very light HTML</li>
  <li>Under 150 words</li>
  <li>One link maximum</li>
  <li>Personal tone</li>
  <li>No attachments</li>
  <li>Minimal signature</li>
  <li>Variation across campaigns (spintax)</li>
</ol>

<h2>The "does it look like sales spam" test</h2>
<p>Close your laptop. Imagine opening an email inbox. Would the email you just wrote make you pause or make you delete immediately?</p>

<p>If it would make you pause as a recipient: probably good content. If it looks like every other "hope this email finds you well" cold pitch you delete without reading: rewrite.</p>

<p style="margin-top:40px;">Next: <a href="monitoring.html">Monitoring inbox placement</a>.</p>
""",
    prev=("IP reputation", "ip-reputation.html"),
    nxt=("Monitoring inbox placement", "monitoring.html"),
)


write_cold_page(
    slug="deliverability/monitoring",
    title="Monitoring inbox placement",
    description="If you can't see where your emails land, you can't improve. Here's the monitoring stack that tells you what's actually happening.",
    reading_time=4,
    body_html="""
<p class="lede">Open rates are a lie. They're based on pixel tracking that's been heavily obscured by iOS 15+ and Apple Mail Privacy. Reply rates are more honest but still reflect what happens after emails reach the inbox. To know what's actually happening upstream, you need dedicated inbox placement monitoring.</p>

<h2>Why open rates mislead</h2>
<p>Since iOS 15 (2021), Apple privately prefetches email content on behalf of users, which triggers tracking pixels even if the user never opens the email. This inflates open rates artificially.</p>

<p>Typical impact: reported open rates 50-80% when real human opens are 15-25%. You can't tell from opens whether emails are reaching the inbox or just being prefetched in the spam folder.</p>

<p>Reply rate is more honest. But reply rate can't distinguish between "nobody wanted what I offered" and "half my emails never reached a human."</p>

<h2>The monitoring stack</h2>

<h3>1. Google Postmaster Tools</h3>
<p>Free. Register your sending domain. Provides:</p>
<ul>
  <li>Spam rate (% marked as spam by Gmail users)</li>
  <li>IP reputation</li>
  <li>Domain reputation</li>
  <li>Authentication pass rates (SPF, DKIM, DMARC)</li>
  <li>Delivery errors</li>
  <li>Encryption usage</li>
</ul>

<p>Only shows Gmail data. But Gmail is usually 40-60% of your B2B send volume, so it's representative.</p>

<p>Check weekly. Reputation dropping = warning signal.</p>

<h3>2. Microsoft SNDS</h3>
<p>Free. Microsoft's equivalent for Outlook/Hotmail/Office 365. Shows IP reputation and complaint rates. Less intuitive UI but important data for B2B (where Outlook is heavily represented).</p>

<h3>3. Seed address testing</h3>
<p>Create inboxes at major providers: Gmail, Outlook, Yahoo, iCloud, major corporate providers. Include these addresses in your normal sends. Manually check where each email lands.</p>

<p>DIY version: 5-10 seed addresses you check manually weekly.</p>

<p>Automated version: services like GlockApps, MailReach, Gmass Inbox Inspector route test emails through real inboxes and report placement.</p>

<h3>4. Blacklist monitoring</h3>
<p>Tools like MXToolbox monitoring or Barracuda Reputation Checker alert you if your domain or sending IPs get listed. Respond immediately - delisting is slow.</p>

<h3>5. Reply-rate monitoring per campaign</h3>
<p>Your cold email tool (Instantly, Smartlead, Lemlist) tracks reply rates per campaign. Sudden drops signal deliverability problems, not copy problems.</p>

<h3>6. Bounce rate</h3>
<p>Track hard bounce rate per campaign. Above 3% = list quality problem. Above 5% = actively damaging your reputation. Stop and fix.</p>

<h2>Key metrics and thresholds</h2>

<h3>Spam rate (Gmail Postmaster)</h3>
<ul>
  <li>Under 0.1%: excellent</li>
  <li>0.1-0.3%: normal</li>
  <li>0.3-0.5%: warning</li>
  <li>Over 0.5%: critical, reputation damage likely</li>
</ul>

<h3>Bounce rate</h3>
<ul>
  <li>Under 2%: fine</li>
  <li>2-3%: caution, clean the list</li>
  <li>Over 3%: stop and fix immediately</li>
</ul>

<h3>Domain reputation (Postmaster)</h3>
<ul>
  <li>High: ideal</li>
  <li>Medium: acceptable</li>
  <li>Low: warning, reduce volume</li>
  <li>Bad: critical, probably need to retire the domain</li>
</ul>

<h3>Reply rate</h3>
<p>Varies by campaign, but watch for trends within a single campaign:</p>
<ul>
  <li>Week 1-2 reply rate as baseline</li>
  <li>Sudden drops without copy change = deliverability issue</li>
  <li>Gradual decline over months = reputation drift or list fatigue</li>
</ul>

<h2>Setting up the dashboard</h2>
<p>Create a weekly review routine:</p>
<ol>
  <li>Check Gmail Postmaster for each sending domain (spam rate, reputation)</li>
  <li>Check SNDS for key sending IPs</li>
  <li>Review reply rate per campaign and per mailbox</li>
  <li>Check bounce rate per campaign</li>
  <li>Run a seed address test on active campaigns</li>
  <li>Check any blacklist alerts</li>
</ol>

<p>15-30 minutes per week. Catches issues early.</p>

<h2>What to do when metrics degrade</h2>

<h3>Spam rate climbing</h3>
<ul>
  <li>Reduce daily volume by 50%</li>
  <li>Review recent copy for spam triggers</li>
  <li>Verify list quality (bounces, unverified addresses)</li>
  <li>Check content patterns (too many links, spammy phrases)</li>
  <li>Run warming at higher intensity</li>
</ul>

<h3>Reply rate dropping</h3>
<ul>
  <li>First rule out deliverability (seed test placement)</li>
  <li>If inbox placement is fine, it's copy, list, or market fatigue</li>
  <li>A/B test new angles</li>
  <li>Refresh list (new segments)</li>
</ul>

<h3>Bounce rate spike</h3>
<ul>
  <li>Stop sending immediately</li>
  <li>Re-verify list</li>
  <li>Resume at lower volume with verified addresses only</li>
</ul>

<h3>Blacklist listing</h3>
<ul>
  <li>Stop sending from affected IP/domain</li>
  <li>Diagnose cause (what changed?)</li>
  <li>Follow blacklist's delisting process</li>
  <li>In parallel, provision new infrastructure as backup</li>
</ul>

<h2>The feedback loop</h2>
<p>Monitoring feeds into decisions:</p>
<ul>
  <li>Which mailboxes are healthy? Send more from them.</li>
  <li>Which domains are degrading? Reduce volume, warm more.</li>
  <li>Which lists have high bounce? Re-verify or retire.</li>
  <li>Which copy has high spam rate? Rewrite.</li>
</ul>

<p>Without the feedback loop, you're flying blind. With it, cold email becomes an engineering discipline.</p>

<h2>The simplest monitoring that works</h2>
<p>If the full stack feels like overhead:</p>
<ol>
  <li>Sign up for Postmaster Tools once. Check it weekly.</li>
  <li>Have 3-5 seed addresses. Glance at them weekly.</li>
  <li>Watch reply rate per campaign in your sending tool.</li>
</ol>

<p>Even this minimum catches the majority of deliverability emergencies before they become disasters.</p>

<p style="margin-top:40px;">Next: <a href="../infra/sending-tools.html">Sending tools</a>.</p>
""",
    prev=("Content that triggers spam filters", "spam-triggers.html"),
    nxt=("Sending tools", "../infra/sending-tools.html"),
)


# ============================================================
# INFRASTRUCTURE (5 pages)
# ============================================================

write_cold_page(
    slug="infra/sending-tools",
    title="Sending tools",
    description="Instantly, Smartlead, Lemlist, Salesloft. Here's how the major cold email platforms differ and which one to use when.",
    reading_time=4,
    body_html="""
<p class="lede">Cold email tools handle sequence automation, mailbox rotation, reply detection, and reporting. The market has consolidated around a few major players. Here's how they compare and what I actually reach for.</p>

<h2>The three tiers</h2>

<h3>Tier 1: Volume-optimized cold email tools</h3>
<p>Built specifically for cold outbound at scale. Support multi-inbox, warming, spintax, deep reporting.</p>
<ul>
  <li>Instantly</li>
  <li>Smartlead</li>
  <li>Lemlist</li>
  <li>Woodpecker</li>
  <li>Reply.io</li>
</ul>

<h3>Tier 2: Sales engagement platforms</h3>
<p>Built for SDR teams. Email is one channel among many (phone, LinkedIn, tasks). Heavier, more expensive, more features.</p>
<ul>
  <li>Salesloft</li>
  <li>Outreach</li>
  <li>Apollo (combined data + sequences)</li>
  <li>Gong Engage (formerly Groove)</li>
  <li>HubSpot Sales Hub</li>
</ul>

<h3>Tier 3: Marketing-adjacent tools</h3>
<p>Not built for cold but sometimes used: Mailchimp, ConvertKit, ActiveCampaign. Avoid for cold B2B. Poor deliverability for outbound use cases.</p>

<h2>The Tier 1 comparison</h2>

<h3>Instantly</h3>
<p>Most popular in 2026. Strong multi-inbox support, generous free warming network, reasonable pricing, clean UI. Unified inbox for reply management across all mailboxes.</p>
<ul>
  <li>Pricing: $37-97/month for most users</li>
  <li>Best for: agencies, high-volume cold operations, teams who need a lot of mailboxes</li>
  <li>Weaknesses: fewer integrations than enterprise alternatives</li>
</ul>

<h3>Smartlead</h3>
<p>Close competitor to Instantly. Similar feature set. Slightly more polished integrations, sometimes cheaper at scale.</p>
<ul>
  <li>Pricing: $33-94/month</li>
  <li>Best for: similar to Instantly; choice often comes down to UI preference</li>
</ul>

<h3>Lemlist</h3>
<p>Pioneer of personalized cold email (LinkedIn data, image personalization). Feature-rich but more expensive. Good for teams doing heavy personalization.</p>
<ul>
  <li>Pricing: $59-135/month</li>
  <li>Best for: personalization-heavy campaigns, smaller teams, creative outreach</li>
  <li>Weaknesses: less ideal for pure volume plays</li>
</ul>

<h3>Woodpecker</h3>
<p>Veteran tool. Reliable, less flashy. Smaller market share now but still used.</p>
<ul>
  <li>Pricing: $49-199/month</li>
  <li>Best for: teams prioritizing stability</li>
</ul>

<h3>Reply.io</h3>
<p>Multi-channel sequence platform (email, LinkedIn, calls). More enterprise-focused than Instantly.</p>
<ul>
  <li>Pricing: $60-130/month</li>
  <li>Best for: multi-channel sequences, more structured outbound teams</li>
</ul>

<h2>The Tier 2 comparison</h2>

<h3>Salesloft</h3>
<p>Standard for enterprise SDR teams. Full sales engagement platform. Phone, email, LinkedIn, tasks, coaching, analytics.</p>
<ul>
  <li>Pricing: $125-165/user/month + add-ons</li>
  <li>Best for: enterprise SDR teams, managed programs, pipeline coaching</li>
  <li>Weaknesses: expensive, over-featured for small teams, less deliverability-focused than Tier 1</li>
</ul>

<h3>Outreach</h3>
<p>Direct competitor to Salesloft. Similar positioning. Platform is deep, often complex to deploy.</p>
<ul>
  <li>Pricing: comparable to Salesloft, usually custom</li>
  <li>Best for: same as Salesloft</li>
</ul>

<h3>Apollo</h3>
<p>Data + sequencing in one. The database is the main draw; sequencing is included. Popular for cost-conscious teams that want an all-in-one.</p>
<ul>
  <li>Pricing: $49-149/user/month for most tiers</li>
  <li>Best for: teams that want data + outreach in one tool</li>
  <li>Weaknesses: sequencing is good but not as deliverability-optimized as Tier 1</li>
</ul>

<h3>HubSpot Sales Hub</h3>
<p>Integrated with HubSpot CRM. Modest sequencing capabilities. Fine if you're already on HubSpot, not worth switching to.</p>

<h2>How to choose</h2>

<h3>Solo founder / small team doing cold outbound</h3>
<p>Instantly or Smartlead. Most affordable per mailbox, strong deliverability focus, clean UI for single-person operators.</p>

<h3>Agency running cold for multiple clients</h3>
<p>Instantly (was built for this). Strong multi-workspace support.</p>

<h3>5-20 person SDR team</h3>
<p>Apollo for integrated data + sequencing, or Salesloft/Outreach if you want structured management and coaching.</p>

<h3>Enterprise SDR org (50+ reps)</h3>
<p>Salesloft or Outreach. The platforms are built for this scale.</p>

<h3>Personalization-heavy, lower volume</h3>
<p>Lemlist. The personalization features are genuinely stronger than others.</p>

<h2>The mailbox connection model</h2>
<p>All Tier 1 tools and most Tier 2 tools connect to your own mailboxes (Google Workspace or Microsoft 365). The tool logs into your inbox via OAuth or IMAP/SMTP and sends through it.</p>

<p>This is essential for deliverability. Sending through the tool's own infrastructure (SMTP services) has worse deliverability because the "from" domain doesn't match the sending server.</p>

<h2>What to evaluate when choosing</h2>
<ul>
  <li>Multi-inbox rotation support (how many mailboxes in one campaign?)</li>
  <li>Built-in warming network quality</li>
  <li>Unified inbox (can you reply to all campaigns from one place?)</li>
  <li>Spintax / dynamic content features</li>
  <li>Reply detection accuracy</li>
  <li>CRM integrations</li>
  <li>Reporting depth</li>
  <li>Cost per mailbox at your volume</li>
  <li>Support quality and response time</li>
</ul>

<h2>My default pick in 2026</h2>
<p>For most cold email operations: Instantly. Well-priced, deliverability-focused, good community. Switch to Salesloft/Outreach only when the team has grown past Instantly's sweet spot and needs structured SDR management.</p>

<p>For heavy personalization: Lemlist. The personalization features justify the price premium.</p>

<p style="margin-top:40px;">Next: <a href="multi-inbox.html">Multi-inbox rotation</a>.</p>
""",
    prev=("Monitoring inbox placement", "../deliverability/monitoring.html"),
    nxt=("Multi-inbox rotation", "multi-inbox.html"),
)


write_cold_page(
    slug="infra/multi-inbox",
    title="Multi-inbox rotation",
    description="A single mailbox caps at ~50 emails/day. Multi-inbox rotation spreads volume across many mailboxes for higher throughput and better deliverability.",
    reading_time=4,
    body_html="""
<p class="lede">One mailbox can safely send 30-50 emails per day before reputation starts degrading. To scale cold email beyond that, you rotate across multiple mailboxes. Done right, this gives you higher volume with lower per-mailbox risk. Done wrong, it replicates bad sending patterns across all your mailboxes simultaneously.</p>

<h2>The math</h2>
<p>Suppose you want to send 1,000 emails/day. Options:</p>
<ul>
  <li>1 mailbox at 1,000/day: dead in a week</li>
  <li>10 mailboxes at 100/day: risky, above safe limits</li>
  <li>25 mailboxes at 40/day: safe, sustainable</li>
  <li>50 mailboxes at 20/day: very safe, but expensive infrastructure</li>
</ul>

<p>Most operators settle around 30-50 emails/day per mailbox. More mailboxes = lower per-mailbox load = better deliverability.</p>

<h2>How rotation works in cold email tools</h2>
<p>Tools like Instantly and Smartlead let you assign multiple mailboxes to a single campaign. The tool distributes sends across all connected mailboxes.</p>

<p>Distribution patterns:</p>
<ul>
  <li><strong>Round-robin</strong>: each new send uses the next mailbox in sequence</li>
  <li><strong>Random</strong>: mailbox selected randomly per send</li>
  <li><strong>Weighted</strong>: healthier mailboxes get more sends, damaged ones less</li>
  <li><strong>Sequential fill</strong>: fill mailbox A to daily limit, then B, then C</li>
</ul>

<p>Round-robin or random are standard. Weighted is advanced (requires tracking per-mailbox health).</p>

<h2>The domain-per-mailbox pattern</h2>
<p>Typical setup for scaling:</p>
<ul>
  <li>10 sending domains, each with 3-5 mailboxes</li>
  <li>30-50 total mailboxes across the operation</li>
  <li>Each mailbox sends 30-40/day</li>
  <li>Total volume: 1,000-2,000/day</li>
</ul>

<p>This gives you redundancy (one domain degrading doesn't kill the operation) and scale without hitting single-mailbox limits.</p>

<h2>Inbox-per-domain ratios</h2>

<h3>Too few (1 mailbox per domain)</h3>
<p>Infrastructure overhead per mailbox is high (separate domain registration, DNS, redirect). Not economical.</p>

<h3>Optimal (2-5 mailboxes per domain)</h3>
<p>Shares DNS/domain setup cost across mailboxes. Keeps per-domain volume manageable. Most common.</p>

<h3>Too many (10+ per domain)</h3>
<p>Aggregate domain volume gets high. If domain reputation degrades, all mailboxes suffer together.</p>

<h2>Naming strategy for mailboxes</h2>
<p>Mailboxes typically use first name + last name format:</p>
<ul>
  <li>sam.ochoa@sendingdomain.com</li>
  <li>alex.rivera@sendingdomain.com</li>
  <li>jordan.kim@sendingdomain.com</li>
</ul>

<p>These can all represent you, a team, or fictional personas - depending on your operation style.</p>

<h3>Personal vs persona</h3>
<ul>
  <li><strong>Personal</strong>: every mailbox is "you" under slightly different names. Simple. Some ethical concerns if recipients think they're each talking to different people.</li>
  <li><strong>Team personas</strong>: different names represent different team members. Honest if they're real people. Questionable if fictional.</li>
  <li><strong>Single identity across variants</strong>: all mailboxes are "Sam Ochoa" at different sending domains. Simplest honest approach.</li>
</ul>

<p>Most cold email operations use the third pattern - same sender identity across infrastructure variants. Recipients see one person even if the mail comes from different systems.</p>

<h2>Load balancing strategies</h2>

<h3>Even distribution</h3>
<p>Every mailbox gets roughly the same volume. Simplest.</p>

<h3>Healthy-weighted distribution</h3>
<p>Track per-mailbox reply rate, bounce rate, spam placement. Route more sends to healthier mailboxes. Parks underperformers for re-warming.</p>

<h3>Per-campaign distribution</h3>
<p>Different campaigns use different mailbox pools. Protects one campaign's reputation issues from bleeding into others.</p>

<h2>The rotation failure modes</h2>

<h3>Shared reputation pool collapse</h3>
<p>If all your domains are on the same shared IP pool (e.g., all Google Workspace), one bad domain can affect the pool. Usually not a real risk at small scale but worth knowing.</p>

<h3>Identical content across all mailboxes</h3>
<p>Sending the same exact email from 30 mailboxes to 30 recipients at the same company is obvious. Use spintax, vary timing, vary signature details.</p>

<h3>Same list hitting multiple mailboxes from same domain</h3>
<p>If your list has 20 contacts at one company and you send to all 20 from different mailboxes of the same sending domain, the company's email server sees 20 outbound emails from one domain and flags accordingly. Spread across different domains or space out sends.</p>

<h3>Missed replies in one mailbox while others stay active</h3>
<p>If you miss a reply in mailbox A but the campaign keeps hitting from mailboxes B, C, D, recipients get confused. Use unified inbox in your tool to catch replies across all mailboxes.</p>

<h2>Parking and rotation</h2>
<p>Mailbox reputation is a resource. Use it, it depletes. Rest it, it recovers.</p>

<p>Rotation strategy:</p>
<ul>
  <li>Run mailbox hard for 8-12 weeks</li>
  <li>Park it (reduce to warming only) for 2-4 weeks</li>
  <li>Return to active rotation</li>
</ul>

<p>At any time, 70-80% of your mailboxes are active and 20-30% are resting. Keeps the overall system healthy.</p>

<h2>Common mailbox count by operation size</h2>
<ul>
  <li>Solo founder starting out: 3-5 mailboxes</li>
  <li>Small team doing founder-led: 5-10</li>
  <li>Dedicated BDR/SDR: 10-20</li>
  <li>Agency managing multiple clients: 30-100+</li>
  <li>Enterprise outbound program: 100-1000+</li>
</ul>

<h2>The cost structure</h2>
<p>For a 30-mailbox operation:</p>
<ul>
  <li>10 domains × $15/year = $150/year</li>
  <li>30 mailboxes × $6/month (Google Workspace) = $2,160/year</li>
  <li>Cold email tool: $97/month = $1,164/year</li>
</ul>

<p>Total infrastructure: ~$3,500/year. Covers ~1,000-1,500 emails/day.</p>

<p>Scaling to 100 mailboxes roughly triples the cost but supports 3-5x the volume.</p>

<p style="margin-top:40px;">Next: <a href="warming-tools.html">Warming tools</a>.</p>
""",
    prev=("Sending tools", "sending-tools.html"),
    nxt=("Warming tools", "warming-tools.html"),
)


write_cold_page(
    slug="infra/warming-tools",
    title="Warming tools",
    description="Every cold email operation runs warming. Here's the landscape of tools, what they actually do, and how to evaluate them.",
    reading_time=4,
    body_html="""
<p class="lede">Warming tools are the unsung infrastructure of cold email. They run in the background, make your mailboxes look legitimate, and are the difference between campaigns that land and campaigns that don't. Most cold email tools now include warming; a few dedicated tools exist too.</p>

<h2>What warming tools do (recap)</h2>
<p>Covered in more detail on <a href="../deliverability/warming.html">inbox warming</a>:</p>
<ol>
  <li>Send small amounts of email from your mailbox to other warmed mailboxes</li>
  <li>Have the recipients auto-reply</li>
  <li>Move spam to inbox where needed</li>
  <li>Mark emails as "not spam" automatically</li>
  <li>Gradually increase volume over weeks</li>
</ol>

<p>This builds sender reputation with email providers without you needing to do anything manual.</p>

<h2>Bundled vs standalone</h2>

<h3>Bundled with cold email tools</h3>
<p>Instantly, Smartlead, Lemlist all include warming in the main product. One account, one dashboard, warming happens automatically alongside your campaigns.</p>

<p>Pros:</p>
<ul>
  <li>One tool, one bill</li>
  <li>Warming data integrated with campaign performance</li>
  <li>Easy to enable per mailbox</li>
</ul>

<p>Cons:</p>
<ul>
  <li>Quality depends on the tool's warming network</li>
  <li>Less control over warming behavior</li>
</ul>

<h3>Standalone warming tools</h3>
<p>Mailwarm, Warmy, MailReach, TrulyInbox. Dedicated to warming only.</p>

<p>Pros:</p>
<ul>
  <li>Often larger, more diverse warming networks</li>
  <li>More advanced features (custom message templates, bigger volume ramps)</li>
  <li>Can use with any sending tool</li>
</ul>

<p>Cons:</p>
<ul>
  <li>Extra subscription</li>
  <li>Separate dashboard</li>
</ul>

<h2>Tool comparison</h2>

<h3>Instantly (built-in)</h3>
<p>Free with Instantly subscriptions. Large network. Default for most Instantly users. Quality is good enough that most teams don't bother with standalone.</p>

<h3>Smartlead (built-in)</h3>
<p>Comparable to Instantly's warming. Similar quality.</p>

<h3>Lemlist (built-in)</h3>
<p>Included. Good. Less aggressive warming ramp - better for higher-quality lower-volume campaigns.</p>

<h3>Mailwarm</h3>
<p>Standalone, large network, dedicated warming. More expensive but often higher quality for advanced use cases.</p>
<ul>
  <li>Pricing: $69-199/month depending on mailboxes</li>
  <li>Best for: operators who need warming independent of their sending tool</li>
</ul>

<h3>Warmy</h3>
<p>Standalone. Detailed reporting on warming performance. AI-powered engagement patterns.</p>
<ul>
  <li>Pricing: $49-229/month</li>
  <li>Best for: operators who want visibility into warming quality metrics</li>
</ul>

<h3>MailReach</h3>
<p>Standalone. Strong reputation. Used by marketers and agencies.</p>
<ul>
  <li>Pricing: $25-99/mailbox/month</li>
</ul>

<h3>TrulyInbox</h3>
<p>Newer, competitive pricing.</p>
<ul>
  <li>Pricing: $29-299/month</li>
</ul>

<h2>What matters in a warming tool</h2>

<h3>Network size and diversity</h3>
<p>Bigger and more diverse = better warming signal. A warming network of 10 mailboxes is worthless. A network of 100,000 diverse mailboxes across providers is robust.</p>

<h3>Network quality</h3>
<p>Some warming networks include low-quality mailboxes (themselves damaged from overuse). Sending warming emails to those provides no benefit. Reputable tools curate their networks.</p>

<h3>Ramp configuration</h3>
<p>Good tools let you configure the daily volume ramp (start low, increase gradually). Default ramps are usually fine for most cases.</p>

<h3>Content variety</h3>
<p>Warming emails should look human and vary. All-identical warming content from 1,000 mailboxes to 1,000 mailboxes looks suspicious to spam filters (yes, providers watch this too).</p>

<h3>Cross-provider coverage</h3>
<p>Warming to Gmail only helps Gmail reputation. A good tool sends warming across Gmail, Outlook, Yahoo, and corporate domains.</p>

<h3>Spam folder recovery</h3>
<p>If your warming email accidentally lands in spam on the recipient end, the tool should mark it as "not spam." This signal is valuable.</p>

<h2>How many warming emails per day</h2>
<p>Typical configuration:</p>
<ul>
  <li>New mailbox: 5-10 warming emails/day, ramping to 20-40 over 4 weeks</li>
  <li>Active mailbox: 15-25 warming emails/day running continuously</li>
  <li>Recovering mailbox: reduce cold volume, increase warming to 30-50/day for 2-4 weeks</li>
</ul>

<h2>Warming cost structure</h2>

<h3>Bundled tools</h3>
<p>No additional cost beyond the cold email tool subscription.</p>

<h3>Standalone tools</h3>
<p>Typically $5-20/mailbox/month. For a 30-mailbox operation: $150-600/month extra.</p>

<p>For most teams, bundled warming is sufficient and avoids the extra cost. Switch to standalone only if you see deliverability issues that bundled warming isn't solving.</p>

<h2>When warming alone isn't enough</h2>
<p>Warming tools can't save:</p>
<ul>
  <li>Bad DNS configuration</li>
  <li>Sending to unverified addresses</li>
  <li>Spammy content</li>
  <li>Too-high volume</li>
  <li>Damaged domain reputation</li>
</ul>

<p>Warming is one tool in the deliverability stack. It's necessary but not sufficient.</p>

<h2>The warming discipline</h2>
<ol>
  <li>Enable warming on every mailbox from day one</li>
  <li>Wait 3-4 weeks before real cold sending</li>
  <li>Keep warming running alongside real sends forever</li>
  <li>Watch per-mailbox reputation weekly</li>
  <li>Pause cold sending + ramp warming when reputation drops</li>
  <li>Retire mailboxes that can't recover</li>
</ol>

<p>Warming is infrastructure, not a project. Think of it like continuous integration for your sender reputation.</p>

<p style="margin-top:40px;">Next: <a href="crm-integration.html">CRM and data integration</a>.</p>
""",
    prev=("Multi-inbox rotation", "multi-inbox.html"),
    nxt=("CRM and data integration", "crm-integration.html"),
)


write_cold_page(
    slug="infra/crm-integration",
    title="CRM and data integration",
    description="Cold email doesn't live in a silo. Leads flow from the tool into CRM, replies sync back, analytics roll up. Here's how to wire it.",
    reading_time=4,
    body_html="""
<p class="lede">A cold email campaign that doesn't integrate with your CRM is a campaign that drops leads on the floor. Positive replies need to become opportunities. Bounces need to update lead records. Unsubscribes need to propagate globally. Here's the integration architecture that keeps outbound and CRM in sync.</p>

<h2>What needs to flow between systems</h2>

<h3>Outbound to CRM</h3>
<ul>
  <li>New leads created in outbound tool → CRM contact records</li>
  <li>Email sends/opens/replies → CRM activity log</li>
  <li>Positive replies → CRM opportunities</li>
  <li>Meeting booked → CRM next step</li>
  <li>Unsubscribes → CRM do-not-contact flag</li>
  <li>Bounces → CRM email validity flag</li>
</ul>

<h3>CRM to outbound</h3>
<ul>
  <li>New leads meeting ICP criteria → added to outbound campaigns</li>
  <li>Existing customers excluded from prospecting lists</li>
  <li>Unsubscribes from CRM propagate back to outbound</li>
  <li>Lifecycle stage changes suppress or re-enroll prospects</li>
</ul>

<h2>The common integrations</h2>

<h3>Salesforce</h3>
<p>Standard for enterprise B2B. Most cold email tools integrate natively (Instantly, Smartlead, Outreach, Salesloft, Apollo).</p>

<h3>HubSpot</h3>
<p>Popular mid-market. Good native integrations with major tools.</p>

<h3>Pipedrive</h3>
<p>Common for smaller teams. Integrated with most cold email tools.</p>

<h3>Close</h3>
<p>Built-in cold email capabilities. Sometimes the whole stack is Close.</p>

<h3>Attio, Folk, others</h3>
<p>Newer CRMs. Integrations via Zapier, Make, or native depending on the tool.</p>

<h2>Integration patterns</h2>

<h3>Native (best)</h3>
<p>Direct API integration built into the outbound tool. Two-way sync, minimal configuration. Use when available.</p>

<h3>Zapier/Make middleware</h3>
<p>When native doesn't exist. Set up workflows:</p>
<ul>
  <li>New positive reply in Instantly → Create deal in HubSpot</li>
  <li>Meeting booked → Assign to AE in CRM</li>
  <li>Unsubscribe in Instantly → Mark do-not-contact in CRM</li>
</ul>

<p>Adds latency and cost but flexible.</p>

<h3>Direct API</h3>
<p>Custom code. Most control, most maintenance. Reserved for advanced operations with specific needs.</p>

<h2>The do-not-contact list</h2>
<p>Critical and often neglected. A unified do-not-contact list (DNC) must propagate across:</p>
<ul>
  <li>All cold email tools</li>
  <li>CRM</li>
  <li>Marketing automation</li>
  <li>Any manual outreach</li>
</ul>

<p>When a prospect unsubscribes from campaign A, they shouldn't appear in campaign B from a different mailbox. When a customer signs, they shouldn't get prospecting emails.</p>

<p>Most cold email tools have a global suppression list. The job is to keep it synced with CRM.</p>

<h2>Data hygiene</h2>
<p>The integration works only as well as the underlying data:</p>
<ul>
  <li>Standardize company names (inconsistent spellings hide duplicate outreach)</li>
  <li>Unique email per record</li>
  <li>Email validity tracking (last bounce date)</li>
  <li>Last contacted date on every record</li>
  <li>Source tracking (know where each lead came from)</li>
</ul>

<h2>Lead routing</h2>
<p>When a positive reply comes in, who handles it? Typical patterns:</p>

<h3>Round-robin</h3>
<p>Replies distributed evenly across AEs.</p>

<h3>Territory-based</h3>
<p>Replies routed by region or industry.</p>

<h3>Size-based</h3>
<p>Large accounts → senior reps; smaller → junior.</p>

<h3>Source-based</h3>
<p>Cold outreach replies → dedicated handler; inbound → different handler.</p>

<p>Route automatically via CRM workflows when possible. Manual routing doesn't scale.</p>

<h2>Reporting across systems</h2>
<p>Unified reporting requires data consistency:</p>
<ul>
  <li>Cold email → meeting booked: tracked in outbound tool</li>
  <li>Meeting → opportunity: tracked in CRM</li>
  <li>Opportunity → closed won: tracked in CRM</li>
</ul>

<p>The full funnel view requires consistent IDs and timestamps across systems. UTM-style parameters (or custom IDs) on every lead help trace origin through the entire funnel.</p>

<h2>The common integration failures</h2>

<h3>Missing reply detection</h3>
<p>Cold email tool says "no reply" but reply came to a different mailbox or thread. Use unified inbox.</p>

<h3>Stale DNC</h3>
<p>Unsubscribes in old campaigns not reflected in new ones. Global suppression list across all tools.</p>

<h3>Duplicate outreach</h3>
<p>Same prospect gets emailed from two mailboxes on different domains (same operation) because the CRM has two records for them. Deduplicate by email.</p>

<h3>CRM cluttered with leads</h3>
<p>Every cold touch creates a CRM record. 90% never reply. CRM fills with inactive leads.</p>

<p>Fix: only create CRM records on reply (or qualified reply). Keep outbound "universe" in the outbound tool. Promote to CRM only when there's real engagement.</p>

<h2>The minimum viable integration</h2>
<p>If you do nothing else:</p>
<ol>
  <li>Global suppression list across all outbound tools</li>
  <li>Existing customers and past replies excluded from cold lists</li>
  <li>Positive replies automatically create CRM deals</li>
  <li>Meeting booking tool (Calendly) logs to CRM</li>
</ol>

<p>These four integrations catch most of the operational pain.</p>

<p style="margin-top:40px;">Next: <a href="reply-management.html">Reply management</a>.</p>
""",
    prev=("Warming tools", "warming-tools.html"),
    nxt=("Reply management", "reply-management.html"),
)


write_cold_page(
    slug="infra/reply-management",
    title="Reply management",
    description="Responses to cold email aren't just 'booked' or 'not interested.' Here's the taxonomy of replies and how to handle each.",
    reading_time=4,
    body_html="""
<p class="lede">The reply handling process is where cold campaigns translate into pipeline. Every positive reply that slips through the cracks is revenue lost. Every ambiguous response that's mishandled is a meeting never booked. Here's the discipline for managing cold email replies at scale.</p>

<h2>The reply taxonomy</h2>
<p>Replies fall into predictable categories:</p>

<h3>Positive (the goal)</h3>
<ul>
  <li>"Sure, let's talk" - book the meeting</li>
  <li>"Send more info" - respond with requested info and book</li>
  <li>"What's available next week?" - propose specific times</li>
</ul>

<h3>Interested but not now</h3>
<ul>
  <li>"Not a priority this quarter" - schedule nurture for next quarter</li>
  <li>"We're evaluating [competitor]" - follow up in 2-3 months</li>
  <li>"Check back in 6 months" - literal follow-up reminder</li>
</ul>

<h3>Wrong person</h3>
<ul>
  <li>"You want to talk to [name]" - pivot to the referred person, reference the referrer</li>
  <li>"I'm no longer at [company]" - update the record, find their replacement</li>
  <li>"I handle X, not Y" - reconsider ICP targeting; maybe their actual role isn't what you thought</li>
</ul>

<h3>Objection</h3>
<ul>
  <li>"Too expensive" - hand-off to AE for a proper conversation</li>
  <li>"We tried something like this" - address specifically</li>
  <li>"We built it in-house" - qualify whether they'd consider an alternative</li>
</ul>

<h3>Information request</h3>
<ul>
  <li>"Send pricing" - send pricing, propose a call</li>
  <li>"Do you integrate with X?" - answer clearly, propose a call</li>
</ul>

<h3>Not interested</h3>
<ul>
  <li>"Not interested" - move to DNC, stop sequence</li>
  <li>"Remove me" - unsubscribe immediately</li>
  <li>"Stop emailing me" - unsubscribe immediately, apologize briefly</li>
</ul>

<h3>Ambiguous / auto-reply</h3>
<ul>
  <li>OOO / vacation reply - don't respond, let sequence continue</li>
  <li>"I'll look into it" - treat as warm but low-urgency</li>
  <li>"?" - clarify, don't assume</li>
</ul>

<h2>The response time matters</h2>
<p>A positive reply replied to within 5 minutes books 60-70%. The same reply responded to in 24 hours books 20-30%. In a week? 5%.</p>

<p>Why: the reply comes when the prospect is in the headspace to engage. Let them move on and you lose them.</p>

<p>Build the infrastructure to respond fast:</p>
<ul>
  <li>Real-time notifications for replies</li>
  <li>On-call rotation for replies during business hours</li>
  <li>Templated responses for common reply types</li>
</ul>

<h2>The unified inbox</h2>
<p>If you're rotating across 30 mailboxes, you can't log into each one to check replies. Cold email tools (Instantly, Smartlead) have unified inboxes that aggregate replies across all your mailboxes into one interface.</p>

<p>Reply comes in to sam.ochoa@sendingdomain1.com → shows up in unified inbox → you reply → sent from the correct mailbox thread. The recipient never sees the multiplexing.</p>

<h2>Handoff patterns</h2>

<h3>Founder-led / solo</h3>
<p>You handle all replies. Fast, personal, limited by your bandwidth.</p>

<h3>SDR-qualified / AE-closed</h3>
<p>SDR handles initial reply, qualifies the prospect, books a meeting for the AE. AE owns from first meeting forward. Standard for B2B sales teams.</p>

<h3>Qualification automation</h3>
<p>Tools or LLMs pre-categorize replies (positive / interested / not) and route accordingly. Human reviews the edge cases.</p>

<h3>Full manual</h3>
<p>Every reply reviewed by a person. Best quality, least scalable.</p>

<p>Pick based on volume: under 20 replies/day, solo works. 20-100 replies/day, add SDRs. 100+ replies/day, add automation.</p>

<h2>Templates for common replies</h2>

<h3>Positive reply → book meeting</h3>
<pre style="background:#f5f5f7; padding:12px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:12px;">
"Great - here's my calendar: [link]. Tue 2pm, Wed 10am, and Thu
3pm EST are open if any of those work for you. Or pick whatever
fits your schedule. Quick 20-minute call, I'll come prepared with
3 specific ideas for [their situation]."
</pre>

<h3>Not right person → get referral</h3>
<pre style="background:#f5f5f7; padding:12px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:12px;">
"Appreciate the reply. Could you point me at the person who
does own [specific function]? Happy to cc you so you're not
caught off guard by my follow-up."
</pre>

<h3>Not now → reschedule</h3>
<pre style="background:#f5f5f7; padding:12px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:12px;">
"Understood - not the right quarter. Would it make sense to
reconnect in [specific future month]? I'll ping you then. If
anything changes before that, feel free to reach out."
</pre>

<h3>Objection → engage</h3>
<pre style="background:#f5f5f7; padding:12px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:12px;">
"Fair concern. Quick question: is [specific objection] the only
thing, or are there others? If we could address [objection],
would it be worth a 15-min conversation?"
</pre>

<h2>The do-not-continue cases</h2>
<p>Certain replies stop the sequence immediately:</p>
<ul>
  <li>Any unsubscribe request</li>
  <li>"Not interested" (despite any continued sequence logic)</li>
  <li>Explicitly hostile responses</li>
  <li>Legal threats</li>
</ul>

<p>Mark as DNC globally. Do not pursue further via any channel without explicit re-engagement.</p>

<h2>Capturing intelligence</h2>
<p>Replies contain market intelligence. Over 100 replies you learn:</p>
<ul>
  <li>What objections come up most</li>
  <li>Who the real buyer is (vs who you thought)</li>
  <li>What your ICP is actually worried about</li>
  <li>How they describe the problem in their words</li>
  <li>What competitors are in the conversation</li>
</ul>

<p>Log this. Use it to refine copy, targeting, and offer.</p>

<h2>Reply rate vs positive reply rate</h2>
<p>Your tool will show "reply rate" (any response, including negative and auto-replies). What matters is <em>positive reply rate</em> - qualified, intent-signaling responses.</p>

<p>Typical distribution:</p>
<ul>
  <li>Overall reply rate: 5-15%</li>
  <li>Of replies, positive intent: 15-30%</li>
  <li>Of positive, meetings booked: 40-70%</li>
</ul>

<p>Multiply: campaign converting 5% reply → 1% positive → ~0.5% meetings. At 1000 sends: 5 meetings/month.</p>

<p>Track positive reply rate specifically. It's the only number that correlates to pipeline.</p>

<p style="margin-top:40px;">Next: <a href="../lists/icp.html">Defining the ICP</a>.</p>
""",
    prev=("CRM and data integration", "crm-integration.html"),
    nxt=("Defining the ICP", "../lists/icp.html"),
)

print("\n✓ Cold Email Part 1: Hub + Foundations + Deliverability + Infrastructure (17 pages)")
