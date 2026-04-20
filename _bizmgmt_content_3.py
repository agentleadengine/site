#!/usr/bin/env python3
"""Business Management content - Sales + GTM + Execution (9 pages)."""
from _build_bizmgmt import write_bm_page


# ============================================================
# SALES + GTM (5 pages)
# ============================================================

write_bm_page(
    slug="sales/funnel-math",
    title="Funnel math that matters",
    description="Most sales dashboards are theater - charts that track activity, not outcomes. Funnel math, done right, answers one question: where is the bottleneck, and what's it worth to fix?",
    reading_time=7,
    body_html="""
<p class="lede">Most sales dashboards are theater - charts that track activity, not outcomes. Funnel math, done right, answers one question: <em>where is the bottleneck, and what's it worth to fix?</em> Every operator should be able to look at their funnel and within 5 minutes know the highest-leverage conversion rate to work on this quarter.</p>

<h2>The stages</h2>
<p>Every sales funnel - B2B, B2C, transactional or consultative - reduces to roughly the same structure:</p>
<ol>
  <li><strong>Suspects</strong> - addressable market you've reached in some way (impressions, reached leads)</li>
  <li><strong>Leads</strong> - expressed some interest (opened email, visited site, filled form)</li>
  <li><strong>Qualified</strong> - matches ICP, has real need, decision authority confirmed</li>
  <li><strong>Opportunity</strong> - specific deal in discussion, budget confirmed</li>
  <li><strong>Proposal</strong> - offer presented</li>
  <li><strong>Closed-Won</strong> - signed</li>
</ol>
<p>Whatever you call them in your CRM, these are the 6 stages. Collapse adjacent stages if they're the same in your business, but don't add more.</p>

<h2>The rates that matter</h2>
<p>Five conversion rates, one per stage transition. This is your funnel:</p>
<pre style="background:#f5f5f7; padding:16px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
Suspect → Lead:        Top-of-funnel effectiveness
Lead → Qualified:      Lead quality / qualification rigor
Qualified → Opp:       Discovery effectiveness
Opp → Proposal:        Solution fit / stakeholder management
Proposal → Closed-Won: Close rate / pricing effectiveness
</pre>
<p>Multiply them together and you have overall funnel conversion. Divide 1 / (overall conversion) and you have how many suspects you need per deal.</p>

<h2>Where to look for the bottleneck</h2>
<p>The bottleneck is whichever stage has:</p>
<ul>
  <li>The lowest conversion rate relative to industry benchmark</li>
  <li>AND has moved materially versus prior periods (deterioration)</li>
  <li>OR is the earliest stage where you're losing outsized volume</li>
</ul>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Example.</strong> You have 1,000 suspects/month, 30% convert to leads, 40% qualify, 50% become opps, 60% get proposals, 30% close. That's 1,000 × 0.3 × 0.4 × 0.5 × 0.6 × 0.3 = 10.8 deals/month.<br><br>
If you double qualified→opp from 50% to 100%, you double total deals - that's the highest-leverage fix. If you improve proposal→close from 30% to 35% (which is much harder), you gain 1.8 deals. Work the bottleneck.
</blockquote>

<h2>Time in stage</h2>
<p>Conversion rate isn't enough. Track <strong>time in stage</strong> too:</p>
<ul>
  <li>Deals that sit in "Qualified" for &gt; 60 days almost never close - they're dead</li>
  <li>Deals in "Proposal" for &gt; 30 days have usually lost momentum</li>
  <li>Average time in stage by stage gives you cycle length</li>
</ul>
<p>Cycle length × number of deals in motion = how much pipeline you need at any moment. If cycle = 90 days and you need 30 closed deals/quarter, your pipeline needs to be 30 / close rate worth of active opportunities at any given time.</p>

<h2>Pipeline coverage ratio</h2>
<p>How much pipeline do I need to hit my quarter's number?</p>
<pre style="background:#f5f5f7; padding:16px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:14px;">Pipeline coverage = Weighted pipeline ÷ Quarterly quota</pre>
<p>Rule of thumb: 3x coverage for a predictable SaaS business. 4-5x for longer sales cycles or newer products. Below 3x = you'll miss.</p>

<h2>The trap: stuffing the top</h2>
<p>When the number is at risk, the instinct is to pump up top-of-funnel volume. If your qualified→opp rate is 15%, doubling leads doubles waste before it doubles deals. Fix the conversion stage before turning the volume knob.</p>

<h2>Segmentation</h2>
<p>Always segment your funnel rates:</p>
<ul>
  <li><strong>By channel</strong> - inbound vs outbound vs partner referral have wildly different conversion</li>
  <li><strong>By segment</strong> - SMB vs enterprise</li>
  <li><strong>By rep</strong> - your top reps have very different close rates than your bottom reps; the top rates are achievable with training</li>
  <li><strong>By product</strong> - different SKUs convert at different rates</li>
</ul>

<h2>What good looks like</h2>
<ul>
  <li>The team knows the 5 stage-to-stage conversion rates cold</li>
  <li>Pipeline coverage ratio reviewed weekly</li>
  <li>The bottleneck is identified explicitly each quarter and someone owns fixing it</li>
  <li>Stale deals get cleaned out (moved to Lost or restarted) every 30 days</li>
</ul>

<p style="margin-top:40px;">Related: <a href="pipeline-design.html">Pipeline design</a> · <a href="../finance/unit-economics.html">Unit economics</a> · <a href="churn-diagnostics.html">Churn diagnostics</a></p>
""",
    prev=("Decision frameworks", "../strategy/decision-frameworks.html"),
    nxt=("Pipeline design", "pipeline-design.html"),
)


write_bm_page(
    slug="sales/pipeline-design",
    title="Pipeline design",
    description="Pipeline is how you manufacture revenue. Like any manufacturing line, it needs designed capacity, named stations, quality gates, and throughput targets.",
    reading_time=7,
    body_html="""
<p class="lede">Pipeline is how you manufacture revenue. Like any manufacturing line, it needs designed capacity, named stations, quality gates, and throughput targets. Most sales orgs run their pipeline like a box of loose deals; the good ones run it like an assembly line.</p>

<h2>Design vs. measurement</h2>
<p><a href="funnel-math.html">Funnel math</a> is about measuring what's happening. Pipeline design is about deliberately building the pipeline you need. Four inputs:</p>
<ol>
  <li><strong>The revenue goal.</strong> $X in new ARR this quarter.</li>
  <li><strong>The conversion rate you know to be true.</strong> Historically, 1 in N qualified opportunities close.</li>
  <li><strong>The cycle time.</strong> Average days from Qualified to Closed-Won.</li>
  <li><strong>The average deal size.</strong></li>
</ol>
<p>From these you back out: how many qualified opps you need now, how many qualified opps you need to generate per week, and how many suspects/leads you need to feed qualification.</p>

<h2>Stage definitions</h2>
<p>The most common pipeline failure: stages that mean different things to different reps. Each stage must have an <strong>exit criteria</strong> - a specific, verifiable condition that must be true to advance:</p>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Example stage definitions.</strong><br>
<strong>Discovery:</strong> Exit when (1) pain validated, (2) authority confirmed, (3) budget range discussed.<br>
<strong>Technical Validation:</strong> Exit when (1) solution fit confirmed by technical buyer, (2) integration plan outlined.<br>
<strong>Commercial:</strong> Exit when (1) pricing proposed, (2) procurement contact known, (3) decision criteria agreed.<br>
<strong>Legal:</strong> Exit when (1) MSA in redline, (2) close date committed by buyer.<br>
<strong>Closed-Won:</strong> Contract signed.
</blockquote>

<h2>MEDDIC / MEDDPICC - the qualification scaffold</h2>
<p>A time-tested qualification framework. For each opportunity, validate and record:</p>
<ul>
  <li><strong>M</strong>etrics - how will the buyer measure success?</li>
  <li><strong>E</strong>conomic Buyer - who signs?</li>
  <li><strong>D</strong>ecision Criteria - what must be true to choose us?</li>
  <li><strong>D</strong>ecision Process - how does the decision get made?</li>
  <li><strong>P</strong>aper Process - what are the legal/procurement steps?</li>
  <li><strong>I</strong>dentified Pain - what's the cost of inaction?</li>
  <li><strong>C</strong>hampion - who on the inside is selling for us?</li>
  <li><strong>C</strong>ompetition - who else are they evaluating?</li>
</ul>
<p>If more than 2-3 of these are "unknown" at Stage 3, the deal is a forecast fantasy.</p>

<h2>The forecast categories</h2>
<p>Every opp in pipeline fits into one of four categories:</p>
<ul>
  <li><strong>Commit</strong> - we're signing this quarter; all blockers known and manageable</li>
  <li><strong>Best Case</strong> - likely this quarter; identifiable risk that could slip</li>
  <li><strong>Pipeline</strong> - active but unlikely to close this quarter</li>
  <li><strong>Omitted / Worst Case</strong> - dead or dormant; pull forward only if miracle</li>
</ul>
<p>Rep forecasts against these. Manager rolls up. The goal: <strong>Commit + 50% of Best Case ≥ Quota</strong>. That's your baseline conviction level.</p>

<h2>Pipeline hygiene</h2>
<p>A clean pipeline lies less. Rules:</p>
<ul>
  <li>Every opp has a next step scheduled with the prospect</li>
  <li>Close dates are moved, not deleted - slippage is data</li>
  <li>If no activity for 30 days, opp gets flagged stale</li>
  <li>If no activity for 60 days, opp is auto-demoted to Pipeline category</li>
  <li>Weekly pipeline scrub: manager + rep walk every Commit + Best Case deal</li>
</ul>

<h2>The pipeline council</h2>
<p>Weekly, 60 minutes, the sales leader + top reps + RevOps:</p>
<ol>
  <li>Review pipeline coverage ratio by segment</li>
  <li>Walk each Commit deal - what's the next step, what could go wrong, what do we need?</li>
  <li>Walk each Best Case deal similarly</li>
  <li>Identify deals that should be promoted or demoted</li>
  <li>Flag capacity issues - is anyone over-quota in pipeline or dangerously under?</li>
</ol>

<h2>What good looks like</h2>
<ul>
  <li>Stage exit criteria are written down and reps know them</li>
  <li>Pipeline coverage &gt; 3x quota per rep</li>
  <li>Manager can explain the forecast with evidence, not vibes</li>
  <li>Closed-Lost reviews happen monthly and feed back into ICP + qualification</li>
</ul>

<p style="margin-top:40px;">Related: <a href="funnel-math.html">Funnel math</a> · <a href="negotiation.html">Pricing + negotiation</a> · <a href="customer-success-ops.html">Customer success ops</a></p>
""",
    prev=("Funnel math", "funnel-math.html"),
    nxt=("Pricing + negotiation", "negotiation.html"),
)


write_bm_page(
    slug="sales/negotiation",
    title="Pricing + negotiation",
    description="Every dollar conceded in a deal is a dollar of margin that's gone for the life of the contract. Negotiation isn't about winning - it's about giving away as little as possible to get the deal you need.",
    reading_time=7,
    body_html="""
<p class="lede">Every dollar conceded in a deal is a dollar of margin that's gone for the life of the contract. Most sales teams give away too much, too easily, too early - usually because they never agreed internally on what was worth trading for what. Good negotiation is 80% preparation, 20% at the table.</p>

<h2>Know your walk-away</h2>
<p>Before you enter negotiation, decide:</p>
<ul>
  <li><strong>Target</strong> - what would make this a great deal</li>
  <li><strong>Acceptable</strong> - the lower bound you'll still sign</li>
  <li><strong>Walk-away</strong> - the point below which you say no</li>
</ul>
<p>Without a walk-away, the negotiation has no floor. You'll keep moving because it "feels close." The walk-away is written down before the call - not invented during it.</p>

<h2>Know what you'll trade</h2>
<p>Four primary levers. Know the order you'll move them in:</p>
<ol>
  <li><strong>Price</strong> - always the last thing you cut</li>
  <li><strong>Term length</strong> - trade longer commit for better price</li>
  <li><strong>Scope / features</strong> - remove things from the deal</li>
  <li><strong>Payment terms</strong> - annual upfront vs quarterly</li>
</ol>
<p>The concession hierarchy matters: trading a price cut for no counter-concession teaches the buyer that your prices are negotiable. Trading a price cut for a multi-year commit or upfront payment teaches them that value-for-value is the deal.</p>

<h2>The concession rules</h2>
<ul>
  <li><strong>Never concede first.</strong> Let them make the ask.</li>
  <li><strong>Never concede twice in a row.</strong> Your concession gets a counter-concession, or the negotiation stops.</li>
  <li><strong>Make concessions smaller over time.</strong> $10K off, then $5K off, then $2K off - signals you're near the floor.</li>
  <li><strong>Never give without acknowledgment.</strong> "We can do that, in exchange for X" - price, term, scope, payment.</li>
  <li><strong>Nothing is agreed until everything is agreed.</strong> Don't let them checkbox each concession as "done" - hold them as a package until sign.</li>
</ul>

<h2>Tactics buyers will run</h2>

<h3>The "one more thing"</h3>
<p>After everything is settled, they come back for a final discount. Counter: "That would require us to reopen the deal. Are you sure you want to do that?" 80% of the time they back off.</p>

<h3>The "good cop / bad cop" procurement handoff</h3>
<p>After you've agreed with the business buyer, procurement comes in asking for 10% more off. Counter: never re-open price to procurement. Their job is redlining paper, not re-discounting.</p>

<h3>The "we need a quick answer"</h3>
<p>Fake urgency designed to prevent you from thinking. Counter: "I understand. Let me check and come back to you in 24 hours." Urgency is 95% tactical.</p>

<h3>The "your competitor is $X"</h3>
<p>Maybe true, maybe bluff. Counter: "I'd be surprised - our value vs theirs is materially different. But if that's the final ask I can't match it. If price is the only thing, you should go with them."</p>

<h2>The walk-away move</h2>
<p>The most powerful tool in negotiation is the ability to credibly walk. "We appreciate your consideration but we're not going to get to a deal" - said calmly, without emotion - often unlocks better terms immediately. Only works if you mean it. Only mean it if you've actually hit your walk-away.</p>

<h2>The discount ladder</h2>
<p>Pre-authorize discounts by size:</p>
<ul>
  <li><strong>0-10%</strong> - rep approval</li>
  <li><strong>10-20%</strong> - manager approval</li>
  <li><strong>20-30%</strong> - VP Sales approval + business justification</li>
  <li><strong>30%+</strong> - CEO/CRO approval; each one reviewed</li>
</ul>
<p>Every discount over 10% requires a written justification. If 60% of deals are getting over-10% discounts, your list price is wrong.</p>

<h2>Contract terms beyond price</h2>
<p>Things that matter more than the deal price:</p>
<ul>
  <li><strong>Auto-renewal</strong> - opt-out notice period. 30-day opt-out is standard; 90+ day opt-out is leverage for your renewal team.</li>
  <li><strong>Uptime SLA</strong> - know your cost if you commit to 99.99%.</li>
  <li><strong>Price protection / caps</strong> - never give unlimited renewal caps for multi-year.</li>
  <li><strong>Payment terms</strong> - Net 30 vs Net 60 is real money; procurement will push for Net 90.</li>
  <li><strong>Termination for convenience</strong> - if they can cancel anytime, the "annual contract" is a month-to-month.</li>
  <li><strong>MFN clauses</strong> - most-favored-nation pricing haunts you at scale.</li>
</ul>

<h2>What good looks like</h2>
<ul>
  <li>Every rep knows the walk-away before the first pricing call</li>
  <li>Concessions are traded 1:1, never given away</li>
  <li>The discount ladder is enforced, not waived</li>
  <li>Contract terms are reviewed for non-price liabilities before sign</li>
</ul>

<p style="margin-top:40px;">Related: <a href="../finance/pricing.html">Pricing frameworks</a> · <a href="pipeline-design.html">Pipeline design</a> · <a href="../finance/unit-economics.html">Unit economics</a></p>
""",
    prev=("Pipeline design", "pipeline-design.html"),
    nxt=("Churn diagnostics", "churn-diagnostics.html"),
)


write_bm_page(
    slug="sales/churn-diagnostics",
    title="Churn diagnostics",
    description="You can grow through the front door as fast as you want - if the back door is leaking, you're filling a bathtub without a plug. Churn diagnostics is about finding the holes, not just patching them.",
    reading_time=7,
    body_html="""
<p class="lede">You can grow through the front door as fast as you want - if the back door is leaking, you're filling a bathtub without a plug. Churn is the second-most-important number in any recurring-revenue business after new bookings. And most teams don't diagnose it well enough to fix it.</p>

<h2>The two churn numbers</h2>
<ul>
  <li><strong>Logo churn</strong> - % of customers who leave, regardless of size</li>
  <li><strong>Revenue churn</strong> - % of recurring revenue that leaves, weighted by contract value</li>
</ul>
<p>Both matter. A business can have 10% logo churn but 2% revenue churn if only small accounts leave. The opposite is much worse: 2% logo churn but 20% revenue churn means you're losing your whales.</p>

<h2>Gross vs. net</h2>
<ul>
  <li><strong>Gross Revenue Retention (GRR)</strong> - starting ARR minus churn minus downgrades, divided by starting ARR. Max 100%.</li>
  <li><strong>Net Revenue Retention (NRR)</strong> - GRR + expansion from existing customers. Can exceed 100%.</li>
</ul>
<p>Benchmarks for SaaS:</p>
<ul>
  <li>GRR &gt; 90%: healthy. &gt; 95%: best in class.</li>
  <li>NRR &gt; 110%: strong. &gt; 120%: excellent.</li>
</ul>
<p>If GRR is strong but NRR is weak, your retention is good but expansion is broken. If both are weak, the product-market fit is in question.</p>

<h2>Voluntary vs. involuntary churn</h2>
<ul>
  <li><strong>Voluntary</strong> - customer chose to leave</li>
  <li><strong>Involuntary</strong> - payment failure, credit card declined, company went out of business</li>
</ul>
<p>Involuntary churn is often 20-40% of total churn and is fixable with dunning processes, card-updater services, and proactive billing outreach. The rest of this page is about voluntary churn.</p>

<h2>The five reasons customers leave</h2>
<ol>
  <li><strong>Didn't realize value.</strong> They never got to first value. Onboarding broke. Feature too hard to adopt.</li>
  <li><strong>Lost value.</strong> Their champion left. Their use case changed. Product stopped matching their workflow.</li>
  <li><strong>Found better alternative.</strong> Competitor gave them a better offer or a new capability you don't have.</li>
  <li><strong>Budget cut.</strong> Macro, company-level, or departmental. Not about you.</li>
  <li><strong>Bad relationship.</strong> Support failures, broken promises, account team turnover, outages.</li>
</ol>
<p>Each requires a different fix. Lumping them together as "churn" hides the root cause.</p>

<h2>The churn diagnostic process</h2>
<p>For every lost customer (above a threshold - say $10K ARR):</p>
<ol>
  <li><strong>Exit interview.</strong> Not by their AE - by customer success or a leader. 20 minutes, structured questions.</li>
  <li><strong>Root cause classification.</strong> One of the five reasons above.</li>
  <li><strong>Timeline reconstruction.</strong> When did the seeds of churn get planted? 30 days ago? 6 months ago? Day one?</li>
  <li><strong>Save attempt (if relevant).</strong> Sometimes a concession, a feature commit, or an executive call flips a churn decision.</li>
  <li><strong>Monthly aggregation.</strong> Categorize, count, look for patterns.</li>
</ol>

<h2>Leading indicators - catch it before they leave</h2>
<p>By the time a customer says "we're cancelling," you've lost. The fight is upstream. Track:</p>
<ul>
  <li><strong>Usage</strong> - active users, feature adoption, session frequency. Declining usage = risk.</li>
  <li><strong>Health scores</strong> - composite metric combining usage, support tickets, NPS, executive sponsor tenure.</li>
  <li><strong>Support ticket sentiment</strong> - escalated tickets, frustration tone, repeat issues.</li>
  <li><strong>Sponsor changes</strong> - if the person who bought you leaves, your renewal is at risk.</li>
  <li><strong>Business changes</strong> - acquisitions, layoffs, reorgs at the customer all raise churn risk.</li>
</ul>
<p>Customers go through three phases before cancellation: <em>quiet disengagement</em>, then <em>unhappy but still paying</em>, then <em>explicit cancellation</em>. The first two are where you intervene.</p>

<h2>Expansion vs. retention</h2>
<p>Expansion is usually more valuable than new logo acquisition (lower CAC, higher margin). But expansion and retention are different motions - retention is about preventing leaving; expansion is about deepening usage. Different playbooks. Usually different teams. If your CS team is measured only on retention, expansion will underperform.</p>

<h2>Cohort analysis</h2>
<p>Aggregate churn hides everything. Always look by cohort (sign-up month/quarter). Questions to answer:</p>
<ul>
  <li>Are newer cohorts churning faster or slower than older ones?</li>
  <li>Is there a "death month" - month 3, 6, 12 where churn spikes?</li>
  <li>Does churn differ by acquisition channel? By segment? By product tier?</li>
  <li>Is post-onboarding churn different from year-2 churn?</li>
</ul>

<h2>What good looks like</h2>
<ul>
  <li>GRR, NRR, and logo churn reported monthly</li>
  <li>Every lost account &gt; $X ARR has a documented root cause</li>
  <li>Health scores trigger proactive outreach before renewal conversations</li>
  <li>Churn root causes feed product roadmap, onboarding fixes, and ICP refinement</li>
</ul>

<p style="margin-top:40px;">Related: <a href="customer-success-ops.html">Customer success ops</a> · <a href="../finance/unit-economics.html">Unit economics</a> · <a href="funnel-math.html">Funnel math</a></p>
""",
    prev=("Pricing + negotiation", "negotiation.html"),
    nxt=("Customer success ops", "customer-success-ops.html"),
)


write_bm_page(
    slug="sales/customer-success-ops",
    title="Customer success ops",
    description="Customer success is the function most often built on good intentions and bad systems. The teams that scale separate the human work (relationships) from the process work (automation) and build both deliberately.",
    reading_time=7,
    body_html="""
<p class="lede">Customer success is the function most often built on good intentions and bad systems. One CSM with 40 accounts, a Google sheet, and a lot of goodwill. The teams that scale separate the human work (relationships) from the process work (automation) and build both deliberately. The goal: the CSM spends their time on the conversations that drive retention and expansion, not on the busywork that could be automated.</p>

<h2>The CSM's job, clarified</h2>
<p>A CSM's job is to drive three outcomes:</p>
<ol>
  <li><strong>Adoption</strong> - the customer actually uses the product and gets value from it</li>
  <li><strong>Retention</strong> - they renew</li>
  <li><strong>Expansion</strong> - they expand (more seats, higher tier, additional products)</li>
</ol>
<p>Not: support tickets, billing issues, onboarding logistics, QBR slide-making. Those are support, billing, onboarding, and RevOps respectively. When CSMs get consumed by those, adoption + retention + expansion suffer.</p>

<h2>Segmentation - the foundation</h2>
<p>Not all customers deserve the same CSM attention. Segment by revenue and strategic value:</p>
<ul>
  <li><strong>Enterprise ($100K+ ARR)</strong> - named CSM, QBRs, executive sponsor, custom success plan</li>
  <li><strong>Commercial ($25K-$100K)</strong> - pooled CSMs, quarterly check-ins, standardized playbooks</li>
  <li><strong>SMB (&lt;$25K)</strong> - digital-only: in-app, email, shared CSM queue</li>
  <li><strong>Strategic (revenue-agnostic)</strong> - key logos, case study partners, analyst references - elevated treatment regardless of ARR</li>
</ul>
<p>The common mistake: giving SMB customers enterprise-level attention. They churn anyway; you just can't afford it.</p>

<h2>The success plan</h2>
<p>For every named-CSM account, write a success plan within 30 days of signing:</p>
<ul>
  <li><strong>What success looks like</strong> - the customer's definition, quantified</li>
  <li><strong>Milestones</strong> - 30, 60, 90 days, and the first annual goal</li>
  <li><strong>Stakeholders</strong> - executive sponsor, economic buyer, champion, technical lead, end users</li>
  <li><strong>Risks</strong> - what could derail adoption or retention</li>
  <li><strong>Expansion path</strong> - how this account grows if things go well</li>
</ul>
<p>Review it at every QBR. Update as reality evolves.</p>

<h2>The customer health score</h2>
<p>A composite number combining:</p>
<ul>
  <li><strong>Usage</strong> - monthly active, key feature adoption, trend</li>
  <li><strong>Sentiment</strong> - NPS, CSAT, support ticket patterns</li>
  <li><strong>Relationship</strong> - executive engagement, champion tenure, QBR attendance</li>
  <li><strong>Commercial</strong> - paid on time, contract health, renewal timing</li>
</ul>
<p>Output: Red / Yellow / Green. Updated weekly. Red = escalation; Yellow = proactive outreach; Green = expansion play.</p>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Simple scoring example.</strong><br>
Each dimension 0-10. Weighted sum. &gt;75 = Green, 50-75 = Yellow, &lt;50 = Red.<br>
Low usage + sponsor just left + open P1 ticket = 28/100 = Red. Trigger a save play today.
</blockquote>

<h2>The renewal playbook</h2>
<p>Renewals shouldn't be a surprise:</p>
<ul>
  <li><strong>Day -180</strong> - health score review; early-warning on at-risk accounts</li>
  <li><strong>Day -120</strong> - value recap document; quantify ROI delivered to date</li>
  <li><strong>Day -90</strong> - renewal conversation kickoff; begin expansion discussion</li>
  <li><strong>Day -60</strong> - commercial terms discussion</li>
  <li><strong>Day -30</strong> - contract in legal</li>
  <li><strong>Day 0</strong> - renewal signed; kick off year 2 success plan</li>
</ul>
<p>Renewals worked in the last 30 days are expensive (concessions made under pressure). Renewals worked at -120 days are cheap (you have leverage).</p>

<h2>The CS-Sales handoff</h2>
<p>Most churn is born in the sales cycle. If sales over-promised, CS inherits an impossible customer. Fix with a structured handoff:</p>
<ul>
  <li>Sales completes a handoff doc: customer goals, stakeholders, commitments made, known risks, expansion signals identified</li>
  <li>CSM + AE do a 30-minute handoff call with the customer included</li>
  <li>First CSM meeting within 10 days of signature</li>
</ul>

<h2>Tooling</h2>
<p>The minimum stack:</p>
<ul>
  <li>CRM (Salesforce/HubSpot) - accounts, opps, renewal forecasting</li>
  <li>Customer success platform (Gainsight, ChurnZero, or spreadsheets at small scale) - health scores, playbooks, alerts</li>
  <li>Product analytics (Mixpanel, Amplitude) - usage telemetry feeding health score</li>
  <li>Shared inbox / ticketing (Zendesk, Intercom) - support + CS visibility</li>
</ul>
<p>You don't need all of them early. You need the health score visible somewhere by the time you have 50 accounts.</p>

<h2>What good looks like</h2>
<ul>
  <li>Every named account has a success plan, reviewed quarterly</li>
  <li>Health scores exist and trigger action</li>
  <li>Renewal motion starts 180 days out, not 30</li>
  <li>CSM to managed-ARR ratio is known and defended ($2M-$5M per CSM is typical)</li>
</ul>

<p style="margin-top:40px;">Related: <a href="churn-diagnostics.html">Churn diagnostics</a> · <a href="pipeline-design.html">Pipeline design</a> · <a href="../execution/slas-and-slos.html">SLAs + SLOs</a></p>
""",
    prev=("Churn diagnostics", "churn-diagnostics.html"),
    nxt=("Process mapping", "../execution/process-mapping.html"),
)


# ============================================================
# EXECUTION + DELIVERY (4 pages)
# ============================================================

write_bm_page(
    slug="execution/process-mapping",
    title="Process mapping",
    description="Every business has a hundred processes it runs on. Most of them live in people's heads. When someone leaves, the process leaves with them. Process mapping is how you extract them onto paper.",
    reading_time=6,
    body_html="""
<p class="lede">Every business has a hundred processes it runs on. Most of them live in people's heads. When someone leaves, the process leaves with them. Process mapping is how you extract them onto paper - and once they're on paper, they become something you can improve, automate, delegate, or eliminate.</p>

<h2>Why map a process</h2>
<ul>
  <li><strong>Make it improvable.</strong> You can't optimize something invisible.</li>
  <li><strong>Make it transferable.</strong> New hire can pick it up without a month of shadowing.</li>
  <li><strong>Make it automatable.</strong> Every automated process starts as a manually mapped one.</li>
  <li><strong>Make it auditable.</strong> Regulators, customers, auditors all ask "show me how you do this" and deserve a real answer.</li>
</ul>

<h2>The level of detail</h2>
<p>Processes get mapped at different levels. Pick the right one:</p>
<ul>
  <li><strong>Level 1 (Overview).</strong> End-to-end, 5-8 high-level steps. Good for onboarding executives to the business.</li>
  <li><strong>Level 2 (Operational).</strong> Detailed enough that a trained operator could execute. 15-40 steps. Used for SOPs.</li>
  <li><strong>Level 3 (Technical).</strong> Every click, every input field, every decision branch. For automation specs and systems of record changes.</li>
</ul>
<p>Most process mapping exercises fail by aiming at Level 3 when Level 2 would've been enough. You get stuck in detail and lose the big picture.</p>

<h2>The five elements of a mapped process</h2>
<ol>
  <li><strong>Trigger</strong> - what starts this process?</li>
  <li><strong>Steps</strong> - the actions, in order</li>
  <li><strong>Actors</strong> - who does each step (role, not person)</li>
  <li><strong>Decisions</strong> - branch points, with the criteria</li>
  <li><strong>Outputs</strong> - what this process produces</li>
</ol>

<h2>Mapping technique - the interview</h2>
<p>The person doing the work maps the process. Not you. You facilitate:</p>
<ol>
  <li>"What starts this process?"</li>
  <li>"What do you do first?"</li>
  <li>"Then what?"</li>
  <li>"What if X happens?" (decision branches)</li>
  <li>"Who else touches this?" (handoffs)</li>
  <li>"When is it done?"</li>
</ol>
<p>Record on the fly. Don't pretty it up during the interview. A whiteboard or a Miro board beats a pre-built flowchart tool for first drafts.</p>

<h2>What to look for - the improvement hunt</h2>
<p>Once mapped, read the process with adversarial eyes:</p>
<ul>
  <li><strong>Unnecessary steps.</strong> "Why do we do this?" If the answer is "because we always have," investigate.</li>
  <li><strong>Handoffs.</strong> Every handoff between people or systems is a delay point and an error point. Can you reduce handoffs?</li>
  <li><strong>Loops + rework.</strong> Any step that often gets redone because the previous step was wrong.</li>
  <li><strong>Approvals.</strong> Who actually needs to approve vs. who's listed as an approver? Unnecessary approvers add days.</li>
  <li><strong>Manual transcription.</strong> Copying data from system A to system B. Almost always an integration opportunity.</li>
  <li><strong>Tribal knowledge.</strong> Any step that "only Maria knows" is a single point of failure.</li>
</ul>

<h2>Swim lanes - when you need them</h2>
<p>For processes with multiple roles, draw it as a swim-lane diagram:</p>
<pre style="background:#f5f5f7; padding:16px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:12px;">
                Lead arrives                         Prospect books meeting
 SDR    ────────[1. Enrich]────┐   ┌─────────────[4. Book]─────────┐
                               │   │                               │
Marketing ─[0. Campaign sent]──┘   │                               │
                                   │                               ▼
 AE                            [2. Contact]                  [5. Discovery]
                                   │                               │
RevOps                             └──[3. Assign]─────────────────┘
</pre>
<p>Swim lanes surface exactly where work crosses team lines. Those crossings are where processes break.</p>

<h2>From map to SOP</h2>
<p>A process map is the blueprint. The <a href="../operating-systems/sops.html">SOP</a> is the instruction manual. Maps are visual; SOPs are step-by-step. You almost always want both for any process you plan to standardize.</p>

<h2>What good looks like</h2>
<ul>
  <li>The 10 most-run processes in the business are mapped</li>
  <li>Maps are versioned and reviewed annually</li>
  <li>New hires receive relevant maps during onboarding</li>
  <li>Process improvements happen against the map, not instead of it</li>
</ul>

<p style="margin-top:40px;">Related: <a href="../operating-systems/sops.html">SOPs</a> · <a href="automate-vs-hire.html">Automate vs hire</a> · <a href="vendor-management.html">Vendor management</a></p>
""",
    prev=("Customer success ops", "../sales/customer-success-ops.html"),
    nxt=("Automate vs hire", "automate-vs-hire.html"),
)


write_bm_page(
    slug="execution/automate-vs-hire",
    title="Automate vs hire",
    description="Every operator faces the same fork: we need capacity - do we hire a person or automate the work? The answer depends on variability, volume, and reversibility more than on cost.",
    reading_time=6,
    body_html="""
<p class="lede">Every operator faces the same fork: we need capacity - do we hire a person or automate the work? Most teams default to hiring because hiring feels safer and automation feels speculative. In reality, the answer depends on three variables - variability, volume, and reversibility - more than it depends on cost.</p>

<h2>The three variables</h2>

<h3>Variability</h3>
<p>How much does the work vary between instances? High variability favors humans. Low variability favors automation.</p>
<ul>
  <li><strong>Low variability</strong> - same inputs, same outputs, same steps every time → automate</li>
  <li><strong>Medium variability</strong> - same steps but inputs vary → automate with human in loop, or AI-assisted</li>
  <li><strong>High variability</strong> - every instance looks different → hire</li>
</ul>

<h3>Volume</h3>
<p>How many instances per unit time?</p>
<ul>
  <li><strong>High volume</strong> (hundreds/day+) → automate almost regardless of complexity</li>
  <li><strong>Medium volume</strong> (dozens/day) → automate if variability is manageable</li>
  <li><strong>Low volume</strong> (handful/week) → usually hire; automation ROI isn't there</li>
</ul>

<h3>Reversibility</h3>
<p>How bad is a mistake?</p>
<ul>
  <li><strong>Reversible</strong> - customer email gets typo'd → automate with retry</li>
  <li><strong>Expensive</strong> - wrong invoice sent → automate with audit trail</li>
  <li><strong>Irreversible</strong> - firing someone, signing a deal, sending a refund → human in the loop, always</li>
</ul>

<h2>The decision matrix</h2>
<pre style="background:#f5f5f7; padding:16px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:12px;">
                    HIGH VOLUME              LOW VOLUME
                 ┌──────────────────────┬──────────────────────┐
HIGH VARIABILITY │  Hire + use tools    │  Hire                │
                 │  (e.g. senior CSM)   │  (e.g. executive)    │
                 ├──────────────────────┼──────────────────────┤
LOW VARIABILITY  │  Automate            │  Contract / offshore │
                 │  (e.g. data entry)   │  (e.g. quarterly     │
                 │                      │   reports)           │
                 └──────────────────────┴──────────────────────┘
</pre>

<h2>The costs people forget</h2>

<h3>Costs of hiring</h3>
<ul>
  <li>Recruitment (3-6 months work, 20-30% of salary if using recruiter)</li>
  <li>Onboarding (2-3 months to productivity)</li>
  <li>Management overhead (~20% of a manager's time per direct report)</li>
  <li>Benefits + overhead (40% load on top of salary)</li>
  <li>Opportunity cost of the seat (someone else could have been hired)</li>
</ul>

<h3>Costs of automation</h3>
<ul>
  <li>Upfront build (weeks to months of engineering)</li>
  <li>Maintenance (10-30% of build cost annually)</li>
  <li>Brittleness when the underlying process changes</li>
  <li>Edge-case handling complexity</li>
  <li>Tooling + infrastructure subscription costs</li>
</ul>

<h2>The hybrid path - the best answer most of the time</h2>
<p>Most real work doesn't neatly automate or fully require a human. The hybrid answer:</p>
<ul>
  <li><strong>Automate the 80%</strong> - the repetitive, low-variance parts</li>
  <li><strong>Escalate the 20%</strong> - exceptions, judgment calls, customer-facing complexity</li>
  <li><strong>Human reviews automation output</strong> before final action on anything irreversible</li>
</ul>
<p>A single CSM with good automation serves 3x the accounts of a CSM without it. The question isn't "automate vs hire" - it's "what's the right ratio of automated work to human work?"</p>

<h2>The automation staircase</h2>
<p>Automation isn't binary. The ladder:</p>
<ol>
  <li><strong>Documented</strong> - process is written down</li>
  <li><strong>Standardized</strong> - same steps every time, different people can run it</li>
  <li><strong>Templated</strong> - inputs and outputs use shared templates</li>
  <li><strong>Tool-assisted</strong> - software does part of the work (e.g., pulls data, generates drafts)</li>
  <li><strong>Semi-automated</strong> - pipeline runs; human reviews and triggers</li>
  <li><strong>Fully automated</strong> - no human intervention except for alerts/exceptions</li>
</ol>
<p>Climb the staircase. Skipping levels breaks things.</p>

<h2>When to hire despite the math</h2>
<ul>
  <li><strong>Customer-facing roles</strong> where presence matters (enterprise CSM, exec sales)</li>
  <li><strong>Roles requiring judgment</strong> under uncertainty (hiring, strategic partnerships)</li>
  <li><strong>Roles that generate the automation</strong> (ops engineer, RevOps, automation engineer)</li>
  <li><strong>When the business is early</strong> and process is still being discovered - automating too early calcifies a bad process</li>
</ul>

<h2>What good looks like</h2>
<ul>
  <li>Hiring requests include a "why can't this be automated?" answer</li>
  <li>Automation projects include a "what's the human escalation path?" answer</li>
  <li>An automation backlog exists with ROI estimates for top candidates</li>
  <li>Ratios like revenue per employee are tracked quarterly</li>
</ul>

<p style="margin-top:40px;">Related: <a href="process-mapping.html">Process mapping</a> · <a href="vendor-management.html">Vendor management</a> · <a href="../people/hiring-signal-vs-noise.html">Hiring - signal vs noise</a></p>
""",
    prev=("Process mapping", "process-mapping.html"),
    nxt=("Vendor management", "vendor-management.html"),
)


write_bm_page(
    slug="execution/vendor-management",
    title="Vendor management",
    description="Every vendor relationship is a managed outsourcing of a piece of your business. Treated casually, vendors cost more than necessary and deliver less than promised. Treated like managed relationships, they're leverage.",
    reading_time=6,
    body_html="""
<p class="lede">Every vendor relationship is a managed outsourcing of a piece of your business. Most teams sign vendor contracts, put them in a spreadsheet, and forget about them until renewal. Vendors know this. They price and serve accordingly. Treated like managed relationships instead, vendors are leverage - more capability per dollar than building in-house can deliver.</p>

<h2>The vendor spectrum</h2>
<ul>
  <li><strong>Commodity</strong> - many substitutes, low switching cost (e.g., most SaaS productivity tools)</li>
  <li><strong>Differentiated</strong> - few substitutes, meaningful switching cost (e.g., your CRM, your ERP)</li>
  <li><strong>Strategic</strong> - embedded in your business model; switching would take 6+ months and disrupt customers (e.g., payments processor, core hosting provider)</li>
</ul>
<p>Each requires a different management posture.</p>

<h2>Vendor inventory</h2>
<p>First move: create a vendor inventory. Every vendor with recurring spend:</p>
<ul>
  <li>Vendor name + category</li>
  <li>Annual spend</li>
  <li>Contract end date + auto-renewal notice period</li>
  <li>Owner (the internal person responsible)</li>
  <li>Criticality (commodity / differentiated / strategic)</li>
  <li>Last renewal date</li>
  <li>Renegotiation notes</li>
</ul>
<p>Sort by annual spend. The top 20% of vendors by spend usually represent 80% of the opportunity for management, both cost reduction and performance improvement.</p>

<h2>The renewal calendar</h2>
<p>Every vendor contract has a renewal date. Miss the renewal notice window and you auto-renew for another year at whatever price they set. Standard failure mode:</p>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
The contract auto-renews 60 days before the anniversary. The vendor emails a 10% price increase 45 days before anniversary. You're already locked in.
</blockquote>
<p>Set calendar reminders 120 days before every vendor renewal. Review active usage, alternatives, and value at 90 days. Negotiate at 60. Decide at 45.</p>

<h2>The quarterly vendor review</h2>
<p>For top 20 vendors:</p>
<ol>
  <li>Spend vs. contract</li>
  <li>Usage vs. contracted seats/volume</li>
  <li>SLA performance (see <a href="slas-and-slos.html">SLAs + SLOs</a>)</li>
  <li>Account manager responsiveness</li>
  <li>Product roadmap alignment</li>
  <li>Alternatives emerging in the market</li>
  <li>Renewal timeline + strategy</li>
</ol>
<p>If a vendor doesn't warrant a quarterly review, you probably don't need the vendor.</p>

<h2>Negotiating vendor contracts</h2>

<h3>At first signing</h3>
<ul>
  <li>Never sign list price on a software contract &gt; $10K/yr - discounts are always available</li>
  <li>Always negotiate multi-year with a fixed rate card, not open-ended renewals</li>
  <li>Negotiate termination for convenience or at least for material breach</li>
  <li>Negotiate a price cap on future years (CPI + X% is the standard)</li>
  <li>Negotiate SLA commitments and service credits for misses</li>
  <li>If it's strategic, negotiate source-code escrow or data-export rights</li>
</ul>

<h3>At renewal</h3>
<ul>
  <li>Always have an alternative identified, even if you're not switching - it's your leverage</li>
  <li>Know your actual utilization - if you're using 60% of seats, that's the conversation</li>
  <li>Ask for flat renewal or better before accepting any increase</li>
  <li>Escalate if stuck - the sales rep has limits; the account manager or RVP has more room</li>
</ul>

<h2>Vendor consolidation</h2>
<p>Annual exercise: map the overlaps in your vendor stack. Common patterns:</p>
<ul>
  <li>Three project management tools, each with different team preferences</li>
  <li>Two data warehouses because of an acquisition that never rationalized</li>
  <li>Five analytics tools each covering partially overlapping use cases</li>
  <li>Unused seats on three different HRIS tools from past iterations</li>
</ul>
<p>Consolidation saves money and, more importantly, reduces integration complexity.</p>

<h2>Dependence risk</h2>
<p>Some questions for your strategic vendors:</p>
<ul>
  <li>What happens if they 3x their price at renewal?</li>
  <li>What happens if they get acquired by a competitor?</li>
  <li>What happens if they have a 2-week outage?</li>
  <li>What happens if their CEO changes strategy and sunsets the product?</li>
</ul>
<p>For any answer that would materially hurt the business, you need a contingency - a second-source plan, a data-portability clause, or a reserve of the vendor's service in a local cache.</p>

<h2>What good looks like</h2>
<ul>
  <li>Vendor inventory is current and owned by finance or ops</li>
  <li>Top 20 vendors get a quarterly review</li>
  <li>No contract auto-renews by accident</li>
  <li>Known dependencies have documented contingency plans</li>
</ul>

<p style="margin-top:40px;">Related: <a href="automate-vs-hire.html">Automate vs hire</a> · <a href="slas-and-slos.html">SLAs + SLOs</a> · <a href="../risk/risk-management.html">Risk management</a></p>
""",
    prev=("Automate vs hire", "automate-vs-hire.html"),
    nxt=("SLAs + SLOs", "slas-and-slos.html"),
)


write_bm_page(
    slug="execution/slas-and-slos",
    title="SLAs + SLOs",
    description="Every service - internal or external - is either explicitly measured or implicitly evaluated on vibes. SLAs and SLOs are how you move from vibes to measured.",
    reading_time=6,
    body_html="""
<p class="lede">Every service - customer-facing, internal, vendor-provided - is either explicitly measured or implicitly evaluated on vibes. SLAs and SLOs are how you move from vibes to measured. Good ones align expectations; bad ones become legal liabilities; missing ones leave everyone disappointed for different reasons.</p>

<h2>The vocabulary</h2>
<ul>
  <li><strong>SLI</strong> (Service Level Indicator) - the actual metric. "Request latency p95." "Uptime %." "First-response time."</li>
  <li><strong>SLO</strong> (Service Level Objective) - your internal target. "p95 latency &lt; 300ms." "Uptime ≥ 99.9%." "First-response &lt; 1 business hour."</li>
  <li><strong>SLA</strong> (Service Level Agreement) - your external, contractual commitment. Usually looser than the SLO. "99.5% uptime, with service credits if missed."</li>
</ul>
<p>SLO is the target you manage to. SLA is the number you're willing to be sued over. Never commit your SLO target as your SLA.</p>

<h2>Why the gap matters</h2>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
SLO: 99.95% uptime internal target.<br>
SLA: 99.5% uptime contractual commitment.<br>
<br>
99.95% ≈ 21 minutes downtime/month.<br>
99.5% ≈ 3.6 hours downtime/month.<br>
<br>
Gap: ~3 hours of cushion per month. That's your error budget.
</blockquote>

<h2>Choosing SLIs</h2>
<p>Good SLIs measure the thing customers experience, not the thing easy to measure. For an API:</p>
<ul>
  <li><strong>Availability</strong> - % of requests that returned a valid response (not an HTTP error)</li>
  <li><strong>Latency</strong> - % of requests served below threshold</li>
  <li><strong>Correctness</strong> - % of responses matching expected output</li>
</ul>
<p>Don't measure CPU utilization or database connections as an SLI - those are system metrics, not customer-experience metrics.</p>

<h2>For support teams</h2>
<p>SLIs that matter:</p>
<ul>
  <li><strong>First response time</strong> - initial reply from human or automation</li>
  <li><strong>Resolution time</strong> - by severity (P1 &lt; 4 hours, P2 &lt; 1 business day, P3 &lt; 5 business days)</li>
  <li><strong>Customer satisfaction on resolution</strong> (CSAT)</li>
  <li><strong>Escalation rate</strong> - % of tickets escalated beyond first-line</li>
</ul>

<h2>For internal services</h2>
<p>Internal SLAs (sometimes called "XLAs" - internal service commitments) matter too:</p>
<ul>
  <li>Finance closes the books by day 10 of each month</li>
  <li>Recruiting presents first-pass candidates within 5 business days of job opening</li>
  <li>IT resolves laptop issues within 4 business hours</li>
  <li>Legal reviews standard NDA within 2 business days</li>
</ul>
<p>Internal teams without SLAs will always be the bottleneck. Internal SLAs force throughput expectations into the open.</p>

<h2>The error budget</h2>
<p>If your SLO is 99.9%, you have 0.1% of error budget - about 43 minutes of "downtime" per month. That budget is a resource:</p>
<ul>
  <li>Spend it on planned maintenance</li>
  <li>Spend it on deployments (riskier deploys that move the product forward)</li>
  <li>Spend it on experimentation (A/B tests that affect performance)</li>
</ul>
<p>When the budget is exhausted - stop. Freeze non-critical deploys. Focus on reliability until the budget recovers. This is the discipline that keeps engineering from shipping endlessly at the cost of stability.</p>

<h2>The review cadence</h2>
<ul>
  <li><strong>Weekly</strong> - engineering reviews SLI performance, reviews incidents, adjusts next week's priorities</li>
  <li><strong>Monthly</strong> - SLA performance reviewed with account teams; any customer-facing misses escalate</li>
  <li><strong>Quarterly</strong> - SLO targets reviewed; are they still right for the business stage?</li>
</ul>

<h2>The common mistakes</h2>
<ul>
  <li><strong>SLO = SLA.</strong> No cushion. First miss becomes a contractual breach.</li>
  <li><strong>Too aggressive.</strong> "100% uptime" is not a target; it's a fantasy.</li>
  <li><strong>Measuring averages.</strong> Use percentiles (p95, p99). Averages hide the worst customer experiences.</li>
  <li><strong>No consequences for missing.</strong> SLOs with no operational consequence are reports, not commitments.</li>
  <li><strong>Service credits that never get issued.</strong> If you miss the SLA and the customer has to fight to get their credit, you've lost them anyway.</li>
</ul>

<h2>What good looks like</h2>
<ul>
  <li>Customer-facing services have documented SLAs and internal SLOs</li>
  <li>Internal teams have committed response/resolution times for their consumers</li>
  <li>Error budgets are tracked and exhausted budgets trigger freeze</li>
  <li>SLI measurement is automated and visible on a live dashboard</li>
  <li>Missed SLAs trigger service credits automatically without customer intervention</li>
</ul>

<p style="margin-top:40px;">Related: <a href="vendor-management.html">Vendor management</a> · <a href="../risk/risk-management.html">Risk management</a> · <a href="../sales/customer-success-ops.html">Customer success ops</a></p>
""",
    prev=("Vendor management", "vendor-management.html"),
    nxt=("Memo culture", "../leadership/memo-culture.html"),
)

print("\n✓ Sales + Execution (9 pages)")
