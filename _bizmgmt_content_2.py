#!/usr/bin/env python3
"""Business Management content — Finance + Strategy (10 pages)."""
from _build_bizmgmt import write_bm_page


# ============================================================
# FINANCE + ECONOMICS (5 pages)
# ============================================================

write_bm_page(
    slug="finance/three-numbers",
    title="The three numbers every operator should know",
    description="Most operators can't tell you their three most important numbers in under ten seconds. If you can't, you don't run the business — it runs you.",
    reading_time=6,
    body_html="""
<p class="lede">Most operators can't tell you their three most important numbers in under ten seconds. If you can't, you don't run the business — it runs you. The job of an operator is to find the three numbers that matter most this quarter and make them visible enough that every decision flows downstream from them.</p>

<h2>Why three</h2>
<p>Not one — one number hides trade-offs. Not ten — ten is a dashboard, not a priority. Three is the number a team can hold in their head during a hallway conversation. Three is enough to triangulate (you move one, the other two move in response). Three forces you to cut.</p>

<h2>The three-numbers framework</h2>
<p>Every business, at every stage, has three numbers that matter most <em>right now</em>:</p>
<ol>
  <li><strong>Input.</strong> The thing you do — demos booked, leads generated, units shipped, trials started. Leading indicator.</li>
  <li><strong>Conversion.</strong> The efficiency — close rate, trial-to-paid, lead-to-SQL. How well inputs turn into outcomes.</li>
  <li><strong>Outcome.</strong> The money — MRR, cash collected, gross profit. Lagging indicator.</li>
</ol>
<p>These aren't the only metrics you track. They're the metrics the team operates against. Everything else is context.</p>

<h2>Picking yours</h2>
<p>The three change as the business changes. Ask: <em>"If I could only move three numbers next quarter, which three would most improve the outcome I want?"</em></p>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Example — early B2B SaaS, pre-PMF:</strong><br>
1. Discovery calls per week<br>
2. % of calls that reveal a real paying problem<br>
3. Design partners signed
</blockquote>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Example — services firm with capacity constraint:</strong><br>
1. Utilization rate (% of billable hours / available hours)<br>
2. Effective bill rate (revenue / hours)<br>
3. Net revenue retention
</blockquote>

<h2>How to make them operate the business</h2>
<ul>
  <li><strong>Post them.</strong> At the top of every <a href="../operating-systems/weekly-business-review.html">weekly business review</a>. In Slack. On the wall if you have a wall.</li>
  <li><strong>Put one person on each.</strong> No ambiguity about who's accountable.</li>
  <li><strong>Review weekly, set quarterly.</strong> Targets for the quarter, progress reviewed every Monday.</li>
  <li><strong>Change them rarely.</strong> Once a quarter at most. If you change them monthly, you don't have priorities — you have mood swings.</li>
</ul>

<h2>The trap to avoid</h2>
<p>The trap is picking vanity numbers — website visitors, social followers, press mentions — because they're easy to move. A number that doesn't directly connect to cash, conversion, or customer outcomes is a distraction. If your three numbers all went up 50% and you couldn't tell whether the business was healthier, they're the wrong three.</p>

<h2>What good looks like</h2>
<ul>
  <li>Every person on the leadership team can recite the three numbers, their current value, and last week's delta — cold.</li>
  <li>The three numbers are written down somewhere durable (not a Slack thread).</li>
  <li>When someone proposes a new project, the first question is: <em>"Which of the three does this move?"</em> If it doesn't move any of them, it doesn't get done.</li>
</ul>

<p style="margin-top:40px;">Related: <a href="pnl-literacy.html">P&amp;L literacy</a> · <a href="unit-economics.html">Unit economics</a> · <a href="../strategy/okrs.html">OKRs without the cult</a></p>
""",
    prev=("Firing well", "../people/firing-well.html"),
    nxt=("P&L literacy", "pnl-literacy.html"),
)


write_bm_page(
    slug="finance/pnl-literacy",
    title="P&L literacy for operators",
    description="You don't need an accounting degree to read a P&L, but you need to know it well enough to catch when the story the numbers tell contradicts the story your team is telling you.",
    reading_time=7,
    body_html="""
<p class="lede">You don't need an accounting degree to read a P&amp;L, but you need to read it well enough to catch when the story the numbers tell contradicts the story your team is telling you. The P&amp;L is the single most important document in the business. Most operators glance at it. A few actually understand it.</p>

<h2>The structure</h2>
<p>Every P&amp;L reads top to bottom, largest number to smallest:</p>
<ul>
  <li><strong>Revenue</strong> — what customers paid you</li>
  <li><strong>Cost of Goods Sold (COGS)</strong> — what it cost to deliver what customers paid for</li>
  <li><strong>Gross Profit</strong> = Revenue − COGS</li>
  <li><strong>Operating Expenses (OpEx)</strong> — salaries, marketing, rent, software</li>
  <li><strong>EBITDA</strong> = Gross Profit − OpEx</li>
  <li><strong>Depreciation &amp; Amortization</strong> — non-cash, spreading past spend over time</li>
  <li><strong>Operating Income</strong> = EBITDA − D&amp;A</li>
  <li><strong>Interest + Taxes</strong></li>
  <li><strong>Net Income</strong> — the bottom line</li>
</ul>

<h2>The lines that actually matter</h2>

<h3>Gross margin %</h3>
<p>Gross Profit ÷ Revenue. This tells you whether the core business model works. A B2B SaaS company with 45% gross margin has a structural problem — the industry is 70–85%. A services firm at 65% is doing well. Know your benchmark and track this monthly. A declining gross margin means your business is getting worse even if revenue is going up.</p>

<h3>Operating margin (EBITDA %)</h3>
<p>EBITDA ÷ Revenue. This tells you whether the business makes money <em>as it's actually run today</em> — before financial engineering. Positive EBITDA + growth = sustainable. Negative EBITDA requires a coherent story about when + how it turns positive.</p>

<h3>% of revenue by line</h3>
<p>Take every OpEx line and divide by revenue. This is how you spot creep. S&amp;M at 45% of revenue tells you a different story than S&amp;M at 12% of revenue. Salaries at 60% means you're a services business whether you call yourself that or not.</p>

<h2>P&L vs cash</h2>
<p>The P&amp;L is accrual-based. Revenue is recognized when earned, expenses when incurred — not when cash moves. This means a "profitable" company can run out of cash; an unprofitable one can sit on a pile of it. Always pair the P&amp;L with the <a href="cash-flow.html">cash flow statement</a>.</p>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Real example.</strong> A SaaS company sells a 1-year contract for $120K, annual upfront. The P&amp;L shows $10K/month in revenue (recognized ratably). The bank account shows $120K on day one. Both are right. They tell different stories.
</blockquote>

<h2>How to actually read one</h2>
<ol>
  <li><strong>Compare to prior period.</strong> MoM and YoY. Absolute numbers are noise; trends are signal.</li>
  <li><strong>Compare to plan.</strong> What did we think revenue would be? COGS? OpEx? Where did we miss?</li>
  <li><strong>Look at % of revenue.</strong> Every cost line. Which are growing faster than revenue? Those are where leverage is disappearing.</li>
  <li><strong>Investigate the big movers.</strong> Anything that moved more than ~10% vs plan or vs prior period needs a one-sentence explanation in the review.</li>
</ol>

<h2>Red flags in a P&amp;L</h2>
<ul>
  <li>Gross margin deteriorating quarter over quarter</li>
  <li>OpEx growing faster than revenue for more than two quarters</li>
  <li>A single customer &gt; 20% of revenue</li>
  <li>"One-time" adjustments showing up every quarter</li>
  <li>Revenue classified weirdly — reclassifying refunds, deferred revenue games</li>
</ul>

<h2>What good looks like</h2>
<ul>
  <li>You review the P&amp;L within 10 business days of month close</li>
  <li>You can explain every line that moved &gt;10% vs plan</li>
  <li>You know your gross margin %, EBITDA %, and net margin % cold</li>
  <li>Your team understands the difference between revenue, bookings, and cash</li>
</ul>

<p style="margin-top:40px;">Related: <a href="three-numbers.html">The three numbers</a> · <a href="unit-economics.html">Unit economics</a> · <a href="cash-flow.html">Cash flow forecasting</a></p>
""",
    prev=("The three numbers", "three-numbers.html"),
    nxt=("Unit economics", "unit-economics.html"),
)


write_bm_page(
    slug="finance/unit-economics",
    title="Unit economics",
    description="If you can't explain how one more customer makes you more profitable or less, you don't have a business model — you have a pile of transactions.",
    reading_time=8,
    body_html="""
<p class="lede">If you can't explain how one more customer makes you more profitable or less, you don't have a business model — you have a pile of transactions. Unit economics is the discipline of reducing the entire business down to what happens with one additional customer, one additional job, one additional unit sold. Everything else — fundraising, hiring, strategy — is downstream of this.</p>

<h2>The core equation</h2>
<p>For a subscription business:</p>
<pre style="background:#f5f5f7; padding:16px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:14px;">LTV / CAC

where
  LTV = (ARPU × Gross Margin %) ÷ Monthly Churn %
  CAC = (Sales + Marketing spend) ÷ New Customers Acquired</pre>
<p>Rule of thumb: <strong>LTV/CAC ≥ 3</strong> to be venture-scale. ≥ 1 to not be actively losing money. Below 1 means you lose money on every customer and "make it up in volume" — the oldest lie in business.</p>

<h2>For a services business</h2>
<p>The equation changes shape, but the principle is the same:</p>
<ul>
  <li><strong>Gross margin per engagement</strong> — revenue minus the direct cost of delivery</li>
  <li><strong>Utilization rate</strong> — what % of paid hours are billable</li>
  <li><strong>Effective bill rate</strong> — revenue per consultant hour</li>
  <li><strong>Cost of acquisition</strong> per engagement</li>
</ul>
<p>You want an answer to: <em>"If I added one more client like my average client, what would it do to cash, margin, and capacity?"</em></p>

<h2>CAC — the trap</h2>
<p>Most teams underestimate CAC. The common mistakes:</p>
<ul>
  <li><strong>Excluding salaries.</strong> If your marketer earns $120K/year and generates 100 customers, your CAC is $1,200 higher than "ad spend divided by customers."</li>
  <li><strong>Counting organic wrong.</strong> Inbound leads that closed themselves aren't free. Your content, SEO, and brand all cost money.</li>
  <li><strong>Blended vs new-logo CAC.</strong> If you report expansion revenue as "new customers," your CAC looks artificially low.</li>
  <li><strong>Payback period confusion.</strong> LTV/CAC ratio matters, but so does how long until you've recouped the CAC in gross profit. &lt; 12 months is healthy; &gt; 24 months creates a cash problem even with a good LTV ratio.</li>
</ul>

<h2>LTV — the trap</h2>
<ul>
  <li><strong>Ignoring churn.</strong> A business with 2% monthly churn has a max LTV of 50 months of ARPU. Feels like a lot until you realize that's 4 years, and your product might not exist in 4 years.</li>
  <li><strong>Using revenue, not gross profit.</strong> LTV should use gross profit, not revenue. Otherwise you're counting dollars you have to spend to deliver.</li>
  <li><strong>Averaging across segments.</strong> Enterprise LTV and SMB LTV are wildly different. A blended number hides the fact that one segment is amazing and the other is losing money.</li>
</ul>

<h2>Segmented unit economics</h2>
<p>Almost always, the aggregate LTV/CAC hides the real story. Segment by:</p>
<ul>
  <li><strong>Channel</strong> — paid search vs referral vs outbound</li>
  <li><strong>Customer size</strong> — SMB vs mid-market vs enterprise</li>
  <li><strong>Product line</strong> — core product vs add-ons</li>
  <li><strong>Cohort</strong> — by quarter signed</li>
</ul>
<p>The action is always the same: double down on the channel/segment/product where economics are strong; starve or reprice the ones where they're not.</p>

<h2>When to care obsessively</h2>
<p>Unit economics matter most when:</p>
<ul>
  <li>You're raising money (investors will model this to the decimal)</li>
  <li>You're scaling paid acquisition (bad unit economics × more ad spend = faster bleed)</li>
  <li>You're making a pricing change</li>
  <li>You're evaluating a new market or segment</li>
</ul>

<h2>What good looks like</h2>
<ul>
  <li>You can quote LTV, CAC, and LTV/CAC by segment from memory</li>
  <li>Payback period is tracked monthly</li>
  <li>Your CAC calculation includes all fully-loaded costs</li>
  <li>When the marketing team pitches a new channel, you model it in unit economics terms before approving spend</li>
</ul>

<p style="margin-top:40px;">Related: <a href="pricing.html">Pricing frameworks</a> · <a href="../sales/funnel-math.html">Funnel math</a> · <a href="../sales/churn-diagnostics.html">Churn diagnostics</a></p>
""",
    prev=("P&L literacy", "pnl-literacy.html"),
    nxt=("Pricing frameworks", "pricing.html"),
)


write_bm_page(
    slug="finance/pricing",
    title="Pricing frameworks",
    description="Most companies price like they're afraid of their customers. Pricing is the highest-leverage lever in a business — a 1% improvement in price typically hits EBITDA harder than a 1% improvement in volume.",
    reading_time=7,
    body_html="""
<p class="lede">Most companies price like they're afraid of their customers. Pricing is the highest-leverage lever in a business — a 1% improvement in price typically hits EBITDA harder than a 1% improvement in volume and harder than a 1% reduction in cost. Every operator should spend more time on pricing than they do. Almost none do.</p>

<h2>The three ways to price</h2>

<h3>1. Cost-plus</h3>
<p>Figure out what it costs, add a margin. Simple. Almost always wrong. Cost-plus pricing leaves value on the table whenever the customer would pay more than your margin target — which is most of the time.</p>

<h3>2. Competitor-based</h3>
<p>Whatever the market is doing, ±10%. Also simple. Also leaves value on the table. You've delegated your pricing strategy to your competitor.</p>

<h3>3. Value-based</h3>
<p>What is this worth to the customer? Price at a defensible fraction of that value. Harder. Almost always more profitable. Requires you to actually know what problem you're solving and what it's worth to solve it.</p>

<h2>Value-based pricing, operationalized</h2>
<ol>
  <li><strong>Identify the value metric.</strong> What unit does the customer measure improvement in? Revenue gained? Hours saved? Errors avoided? Tickets deflected?</li>
  <li><strong>Quantify the value.</strong> $X per unit × Y units = Z total value created annually.</li>
  <li><strong>Set a value capture %.</strong> Typically 10–30% of value delivered. Higher for mission-critical; lower for commodity.</li>
  <li><strong>Test it.</strong> Present the price alongside the value math. Watch what happens in close rates.</li>
</ol>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Example.</strong> A tool that saves a 20-person sales team 4 hours/week/rep. At a $100K loaded cost per rep, that's 10% of each rep's time = $200K/year in recovered capacity. A 15% value capture gets you to a $30K/year contract — and you just priced on the value to the buyer, not on what it cost you to build.
</blockquote>

<h2>Packaging strategy</h2>
<p>Pricing is half the problem. Packaging is the other half:</p>
<ul>
  <li><strong>Good / Better / Best.</strong> Three tiers, not four or more. The middle tier usually sells best by design.</li>
  <li><strong>Anchor tier.</strong> The top tier makes the middle look reasonable.</li>
  <li><strong>Gating features, not usage.</strong> Gate on features (seats, workflows, integrations) rather than arbitrary usage caps — customers hate punitive overage charges.</li>
  <li><strong>Enterprise = call us.</strong> Above a certain point, don't publish pricing. Enterprise buyers don't self-serve.</li>
</ul>

<h2>When to raise prices</h2>
<p>The answer is usually: more often than you think, and by more than you think. You should be raising prices:</p>
<ul>
  <li>When inflation erodes effective price</li>
  <li>When you add features that add value</li>
  <li>When your close rates are too high (&gt; 50% on new pipeline means you're leaving money on the table)</li>
  <li>When your churn rate for new customers doesn't change after a price increase (means you weren't pricing on value before)</li>
</ul>

<h2>Grandfathering</h2>
<p>When you raise prices, decide your grandfathering policy before you raise. The spectrum:</p>
<ul>
  <li><strong>No grandfathering.</strong> Everyone moves to new price at renewal. Cleanest revenue model. Some churn risk.</li>
  <li><strong>Partial grandfathering.</strong> Existing customers keep price for 12 months, then move to new price. Typical balanced move.</li>
  <li><strong>Full grandfathering.</strong> Existing customers keep price forever. Builds legacy pricing tiers that haunt you for years.</li>
</ul>

<h2>What good looks like</h2>
<ul>
  <li>You know your average discount % on new deals</li>
  <li>You run a price increase at least every 18 months</li>
  <li>Your pricing page reflects a real packaging strategy, not whatever three prices you made up</li>
  <li>Sales knows what to concede on and what to hold firm on</li>
</ul>

<p style="margin-top:40px;">Related: <a href="../sales/negotiation.html">Pricing + negotiation</a> · <a href="unit-economics.html">Unit economics</a> · <a href="../sales/funnel-math.html">Funnel math</a></p>
""",
    prev=("Unit economics", "unit-economics.html"),
    nxt=("Cash flow forecasting", "cash-flow.html"),
)


write_bm_page(
    slug="finance/cash-flow",
    title="Cash flow forecasting",
    description="Profitable companies go bankrupt. Unprofitable ones can run for years. The difference is cash — and whether you saw the crunch coming.",
    reading_time=7,
    body_html="""
<p class="lede">Profitable companies go bankrupt. Unprofitable ones can run for years. The difference is cash — and whether you saw the crunch coming. Cash flow forecasting is the most underrated operator skill. It takes an afternoon to set up and saves businesses every month.</p>

<h2>Cash is not profit</h2>
<p>A reminder of why this matters:</p>
<ul>
  <li>You invoice a customer $100K. The P&amp;L shows $100K revenue. Bank shows $0. Net 60 terms mean cash arrives in 2 months.</li>
  <li>You sign an annual contract for $120K collected upfront. Cash arrives day one. P&amp;L recognizes $10K/month.</li>
  <li>You buy a server for $50K. Cash out day one. P&amp;L shows $50K ÷ 3 years = $16K/year in depreciation.</li>
</ul>
<p>All three distort the relationship between what's "earned" and what's in the bank. A cash flow forecast is how you translate between them.</p>

<h2>The 13-week cash flow</h2>
<p>The standard operator tool. A rolling weekly forecast of cash in, cash out, and ending balance for the next 13 weeks (one quarter). Updated every Monday.</p>

<pre style="background:#f5f5f7; padding:16px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px; overflow-x:auto;">
Week:                W1    W2    W3    W4    ...   W13
Starting cash:       500   610   640   590
+ Receivables:       250   300   200   180   ...
+ New sales cash:    200   150   250   300
- Payroll:           (180) (0)   (180) (0)
- Rent:              (50)  (0)   (0)   (0)
- Vendors:           (80)  (120) (90)  (110)
- Taxes / other:     (30)  (0)   (230) (0)
Ending cash:         610   640   590   960   ...
</pre>

<h2>Inputs — receivables</h2>
<p>Pull your accounts receivable aging. For each invoice, assign a collection week based on terms + history:</p>
<ul>
  <li>Net 30 invoice sent Week 1 → cash Week 5 or 6 (customers pay late)</li>
  <li>Net 60 invoice sent Week 1 → cash Week 9 or 10</li>
  <li>Habitual slow-payer → add 2 weeks</li>
</ul>

<h2>Inputs — payables</h2>
<p>The out-flows are more predictable:</p>
<ul>
  <li><strong>Payroll</strong> — biweekly on fixed dates. Known to the penny.</li>
  <li><strong>Rent</strong> — monthly on the 1st</li>
  <li><strong>Vendors</strong> — scheduled by your AP terms</li>
  <li><strong>Taxes</strong> — quarterly estimates, payroll taxes, sales tax remittance</li>
  <li><strong>Known one-offs</strong> — annual software renewal, a piece of equipment</li>
</ul>

<h2>The cash runway calculation</h2>
<p>If the business is burning cash, runway = current cash ÷ monthly burn. The forecast turns this from a rough estimate into a specific date.</p>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Example.</strong> Current cash $800K. Monthly burn $100K. Rough runway = 8 months. But the forecast shows a $200K tax payment in month 3 and a $100K annual software renewal in month 5. Actual runway = 6 months, not 8. Six-month plans look very different from eight-month plans.
</blockquote>

<h2>Stress testing</h2>
<p>Once the base forecast is set up, run three cases every time you update:</p>
<ol>
  <li><strong>Base</strong> — what you expect</li>
  <li><strong>Downside</strong> — top customer delays payment 60 days, no new deals close this quarter, one bad-debt write-off</li>
  <li><strong>Disaster</strong> — top customer churns, new sales drop 50%, one key payable gets called immediately</li>
</ol>
<p>The question isn't "will we hit base?" — it's "where are we on disaster, and what do we do if that materializes?"</p>

<h2>What good looks like</h2>
<ul>
  <li>A 13-week cash flow spreadsheet that gets updated every Monday</li>
  <li>Receivables aging reviewed weekly — any invoice &gt; 60 days old has a collection action</li>
  <li>You know your cash runway to the week, not to the month</li>
  <li>You have a "trigger plan" — if cash drops below X, here are the three cuts we make in order</li>
</ul>

<p style="margin-top:40px;">Related: <a href="pnl-literacy.html">P&amp;L literacy</a> · <a href="three-numbers.html">The three numbers</a> · <a href="../risk/risk-management.html">Risk management</a></p>
""",
    prev=("Pricing frameworks", "pricing.html"),
    nxt=("OKRs without the cult", "../strategy/okrs.html"),
)


# ============================================================
# STRATEGY + PLANNING (5 pages)
# ============================================================

write_bm_page(
    slug="strategy/okrs",
    title="OKRs without the cult",
    description="OKRs work when you use them to align a small number of things that matter. They fail when you use them as a reporting framework, a performance review tool, or a theater of strategy.",
    reading_time=7,
    body_html="""
<p class="lede">OKRs work when you use them to align a small number of things that matter. They fail when you use them as a reporting framework, a performance review tool, or a theater of strategy. Most OKR implementations I've seen are the latter — and the teams running them would be measurably better off without them.</p>

<h2>What OKRs actually are</h2>
<ul>
  <li><strong>Objective.</strong> A qualitative, directional statement. What you want to be true by the end of the period. One sentence.</li>
  <li><strong>Key Results.</strong> 2–4 measurable outcomes that tell you whether the objective was achieved. Numbers with deadlines.</li>
</ul>
<p>Objective = where we're going. Key results = how we'll know we got there.</p>

<h2>The rules that keep OKRs useful</h2>
<ol>
  <li><strong>Max 3 objectives per team, per quarter.</strong> Teams with 7 "priorities" have 0 priorities.</li>
  <li><strong>Key results are outcomes, not outputs.</strong> "Launch feature X" is not a KR — it's a task. "Increase activation rate from 40% to 55%" is a KR.</li>
  <li><strong>Cascade by negotiation, not decree.</strong> The CEO's objectives don't automatically become the VP's objectives. Each level chooses what they'll contribute.</li>
  <li><strong>Not tied to comp.</strong> The moment bonuses depend on hitting KRs, people sandbag targets. OKRs become commitments instead of stretches.</li>
  <li><strong>Review weekly, grade at end.</strong> Weekly: "where are we, what's off-track, what do we need?" End-of-quarter: "did we hit it? If not, why?"</li>
</ol>

<h2>How to write a good KR</h2>
<p>A good KR passes three tests:</p>
<ul>
  <li><strong>Measurable.</strong> A number with a source of truth. "Improve customer satisfaction" fails. "NPS from 32 to 45, measured by quarterly survey" passes.</li>
  <li><strong>Time-bound.</strong> By when? Usually end of quarter.</li>
  <li><strong>Causally connected.</strong> Achieving this KR would actually move the objective. (If you hit the KR and the objective still isn't achieved, you wrote the wrong KR.)</li>
</ul>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Good OKR example.</strong><br>
<strong>Objective:</strong> Make the onboarding experience so good that new customers get to value in the first session.<br>
<strong>KR1:</strong> Time-to-first-key-action: 18 min → 7 min<br>
<strong>KR2:</strong> % of new signups who complete onboarding: 52% → 72%<br>
<strong>KR3:</strong> Week-4 retention: 31% → 42%
</blockquote>

<h2>Ambitious vs committed</h2>
<p>Google popularized "moonshot" OKRs where grading 0.7/1.0 is a win. In practice, in real businesses:</p>
<ul>
  <li><strong>Committed OKRs</strong> — must hit. Usually revenue, customer-facing commitments, compliance. Graded binary: did / didn't.</li>
  <li><strong>Aspirational OKRs</strong> — try hard; 0.7/1.0 is good. Usually new initiatives, exploratory work, stretch goals.</li>
</ul>
<p>Mark which is which when you set them. The team needs to know which numbers they must hit and which ones are stretch.</p>

<h2>The most common failure modes</h2>

<h3>OKR theater</h3>
<p>Teams write OKRs, post them, never reference them again. The quarterly OKR review feels like a chore because nothing actually depends on it. Fix: link the <a href="../operating-systems/weekly-business-review.html">weekly business review</a> to OKR progress. Make it the first agenda item.</p>

<h3>Top-down cascade</h3>
<p>Executives write OKRs, then assign them down. Teams treat them like tasks, not goals. No ownership. Fix: executives set company-level objectives; teams choose their own contributing OKRs.</p>

<h3>Too many OKRs</h3>
<p>10 objectives per team, 5 KRs per objective = 50 tracked numbers. Nobody can hold that in their head. Fix: 3 objectives max, 2–4 KRs each.</p>

<h3>OKRs become a task list</h3>
<p>KRs read like: "Ship feature X. Run campaign Y. Hire 3 people." These are projects, not outcomes. Fix: for every KR that sounds like a task, ask <em>"which metric would improve if we did this?"</em> That's the real KR.</p>

<h2>What good looks like</h2>
<ul>
  <li>Every person on the team can recite the current quarter's company OKRs</li>
  <li>Weekly reviews reference progress on KRs, not just activity</li>
  <li>When new work arrives, it's evaluated against OKRs ("does this advance an objective, or are we just doing it?")</li>
  <li>Quarterly grading actually happens, and misses become inputs to the next quarter's planning</li>
</ul>

<p style="margin-top:40px;">Related: <a href="planning-cadence.html">Annual + quarterly planning</a> · <a href="what-to-kill.html">What to kill</a> · <a href="../operating-systems/weekly-business-review.html">Weekly business review</a></p>
""",
    prev=("Cash flow forecasting", "../finance/cash-flow.html"),
    nxt=("Annual + quarterly planning", "planning-cadence.html"),
)


write_bm_page(
    slug="strategy/planning-cadence",
    title="Annual + quarterly planning",
    description="The annual plan no one follows and the quarterly plan everyone ignores are the two most common artifacts of planning theater. A good planning cadence does exactly three things.",
    reading_time=7,
    body_html="""
<p class="lede">The annual plan no one follows and the quarterly plan everyone ignores are the two most common artifacts of planning theater. A good planning cadence does exactly three things: sets direction, forces trade-offs, and generates the commitments the rest of the operating system runs on. Everything else is optional.</p>

<h2>The three horizons</h2>
<ul>
  <li><strong>Annual</strong> — the direction, the bets, the budget envelope. Updated once a year; revisited midyear.</li>
  <li><strong>Quarterly</strong> — <a href="okrs.html">OKRs</a>, headcount, major initiatives. Updated every 90 days.</li>
  <li><strong>Weekly</strong> — the <a href="../operating-systems/weekly-business-review.html">WBR</a> against the quarter's plan.</li>
</ul>
<p>The weekly execution cascades from the quarterly plan. The quarterly plan cascades from the annual. If any link in that chain is broken, the whole thing is noise.</p>

<h2>The annual plan — what it must contain</h2>

<h3>1. Where we are</h3>
<p>One page. What happened last year. What worked, what didn't. Wins and misses. Not marketing — diagnosis.</p>

<h3>2. The world we see</h3>
<p>Market, competition, customers, regulatory environment. What's changing? What assumptions from last year turned out to be wrong?</p>

<h3>3. Where we're going</h3>
<p>The thesis. One paragraph that says: <em>"Because of X and Y, we're going to do Z. We believe this will produce outcome W by the end of the year."</em></p>

<h3>4. The 3–5 bets</h3>
<p>The major initiatives the year turns on. Each with: outcome, owner, budget, and a go/no-go date. Everything else in the company either supports one of these bets or is just maintenance.</p>

<h3>5. The financial frame</h3>
<p>Revenue target, operating budget, gross margin target, headcount plan. Not the full model — the top-line envelope that tells everyone what's affordable.</p>

<h3>6. The risks</h3>
<p>Three to five real risks with mitigation plans. Not boilerplate ("economy might slow down"). Real risks that would derail the plan.</p>

<h2>The quarterly plan — where the rubber hits the road</h2>
<p>The quarter is where planning becomes execution:</p>
<ol>
  <li><strong>Pre-read.</strong> Two weeks before the planning meeting, each team submits: last quarter's OKR grades, proposed next quarter's OKRs, headcount asks, budget asks.</li>
  <li><strong>Planning meeting.</strong> One day, offsite if possible. Morning = company-level priorities. Afternoon = team OKRs.</li>
  <li><strong>Negotiation phase.</strong> Week after planning meeting: teams iterate on OKRs with their managers. Final versions locked by end of week 2.</li>
  <li><strong>Kickoff.</strong> All-hands at start of quarter reviewing commitments.</li>
</ol>

<h2>Timeline example</h2>
<pre style="background:#f5f5f7; padding:16px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
Q4 (Oct-Dec)
  Oct 15:  Draft annual plan distributed for feedback
  Nov 1:   Board review of draft annual plan
  Nov 15:  Final annual plan published
  Dec 1:   Q1 planning pre-reads due
  Dec 10:  Q1 planning offsite
  Dec 20:  Q1 OKRs finalized
  Jan 5:   Q1 kickoff all-hands
</pre>

<h2>Common failure modes</h2>

<h3>Annual plan never referenced again</h3>
<p>Signed in January, filed away, until the next January. Fix: reference it in every quarterly planning session. The annual plan answers "what are we trying to do?" — which the quarterly plan has to serve.</p>

<h3>Quarterly planning that doesn't change anything</h3>
<p>Same OKRs every quarter, minor wording changes, no real trade-offs made. Fix: every quarter, force each team to say what they will <a href="what-to-kill.html">stop doing</a>.</p>

<h3>Plans that don't survive contact with reality</h3>
<p>The plan was for perfect conditions. Q1 hits headwinds. The plan doesn't update. Fix: mid-quarter review. Not every quarter — but when the business materially changes, re-plan.</p>

<h3>Death by planning</h3>
<p>Planning takes 6 weeks. Execution takes 6 weeks. You've already lost half the quarter before anyone did work. Fix: cap planning. One day for quarterly planning, one week of refinement, done.</p>

<h2>What good looks like</h2>
<ul>
  <li>The annual plan is 8–15 pages, not 80</li>
  <li>Quarterly planning produces real trade-offs — something gets killed, something gets elevated</li>
  <li>The plan is referenced weekly at the WBR, not just at planning time</li>
  <li>Revisions happen when reality demands them, not on a rigid calendar</li>
</ul>

<p style="margin-top:40px;">Related: <a href="okrs.html">OKRs without the cult</a> · <a href="what-to-kill.html">What to kill</a> · <a href="pre-mortems.html">Pre-mortems</a></p>
""",
    prev=("OKRs without the cult", "okrs.html"),
    nxt=("What to kill", "what-to-kill.html"),
)


write_bm_page(
    slug="strategy/what-to-kill",
    title="What to kill",
    description="The instinct of every operator is to keep adding. Add features, add hires, add initiatives, add pricing tiers. The hardest operator skill is deciding what to subtract.",
    reading_time=6,
    body_html="""
<p class="lede">The instinct of every operator is to keep adding. Add features, add hires, add initiatives, add pricing tiers. The hardest operator skill — and the one that separates excellent operators from good ones — is deciding what to subtract. What to kill. Good strategy is almost entirely about what you <em>won't</em> do.</p>

<h2>Why killing is hard</h2>
<ul>
  <li><strong>Sunk cost.</strong> Someone spent 6 months building this. Killing it feels like admitting waste.</li>
  <li><strong>Identity.</strong> People define themselves by what they own. Killing a project threatens identity.</li>
  <li><strong>Hope.</strong> "It just needs a little more time." It rarely does.</li>
  <li><strong>Political cost.</strong> Someone executive sponsored it. Killing it is a political act.</li>
  <li><strong>Absence of a forcing function.</strong> Nothing forces you to cut unless cash or capacity runs out. So most teams don't.</li>
</ul>

<h2>The kill criteria — set them in advance</h2>
<p>The single most effective move: <strong>write kill criteria before you launch.</strong> "This initiative will be killed if, by month 6, we haven't hit X or Y." Then when month 6 arrives, the decision has been made. You're just executing on it.</p>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Example kill criteria.</strong><br>
<em>Initiative: Launch new SMB self-serve tier.</em><br>
Kill if by month 6:<br>
- Conversion rate from free trial &lt; 4%<br>
- MRR from self-serve &lt; $20K<br>
- CAC payback &gt; 18 months<br>
Any single one of these triggers the kill conversation. Two or three = automatic shutdown.
</blockquote>

<h2>The quarterly kill review</h2>
<p>Once a quarter, the leadership team does a "kill review." The format:</p>
<ol>
  <li>List every active initiative &gt; 1 person-month of investment per quarter</li>
  <li>For each: impact to date, cost to date, cost to continue, signal on whether it's working</li>
  <li>Each leader proposes 1–2 to kill</li>
  <li>Discussion: kill, continue, or modify</li>
</ol>
<p>The rule: <strong>every leader must propose at least one kill.</strong> No exceptions. If you can't, you're not being honest with yourself.</p>

<h2>Categories of things that need to be killed</h2>

<h3>Zombie projects</h3>
<p>Still technically funded. No clear owner. Nobody remembers why it started. Shipping 0 value per quarter.</p>

<h3>Pet projects</h3>
<p>An executive sponsor loves it. Team hates it. Not actually connected to strategy. Continues only because the sponsor has political power.</p>

<h3>Things that were right a year ago</h3>
<p>Great idea in Q1 2024. World has changed. Still running on autopilot because no one has done the work of closing the loop.</p>

<h3>Scope creep within still-good projects</h3>
<p>The core initiative is fine. Three add-ons bolted onto it are not. Kill the add-ons, not the core.</p>

<h3>Small customers costing more to serve than they pay</h3>
<p>Usually 10–15% of a customer book. Kill by raising price or formally sunsetting.</p>

<h2>How to kill without trauma</h2>
<ul>
  <li><strong>Frame as a choice, not a failure.</strong> "We're redirecting this capacity to X" lands better than "this didn't work."</li>
  <li><strong>Credit the effort.</strong> The team on the killed project did the work. Publicly acknowledge it.</li>
  <li><strong>Explain the decision.</strong> People accept hard decisions when they understand the reasoning. They resent decisions handed down without context.</li>
  <li><strong>Offer the next job.</strong> Wherever possible, the team gets a clear next assignment immediately — not a layoff or limbo.</li>
  <li><strong>Document the learning.</strong> A killed project should generate a one-page post-mortem: what did we learn that we didn't know before we started?</li>
</ul>

<h2>The meta-discipline</h2>
<p>The highest-leverage thing you can do is build a culture where killing is normal. Where every project starts with "what would make us stop?" Where quarterly kill reviews are expected, not dramatic. Where proposing a kill doesn't make you disloyal — it makes you a good steward of capacity.</p>

<h2>What good looks like</h2>
<ul>
  <li>Every major initiative has written kill criteria at start</li>
  <li>Every quarter, at least one meaningful thing gets killed</li>
  <li>Killed projects produce a learning document, not a dead Jira board</li>
  <li>Teams accept kills without feeling punished</li>
</ul>

<p style="margin-top:40px;">Related: <a href="pre-mortems.html">Pre-mortems</a> · <a href="okrs.html">OKRs without the cult</a> · <a href="../operating-systems/decision-logs.html">Decision logs</a></p>
""",
    prev=("Annual + quarterly planning", "planning-cadence.html"),
    nxt=("Pre-mortems", "pre-mortems.html"),
)


write_bm_page(
    slug="strategy/pre-mortems",
    title="Pre-mortems",
    description="A post-mortem asks why the failure happened. A pre-mortem asks why the failure will happen — before the project starts. The difference is whether the learning is free or expensive.",
    reading_time=5,
    body_html="""
<p class="lede">A post-mortem asks why the failure happened. A pre-mortem asks why the failure <em>will</em> happen — before the project starts. The difference is whether the learning is free or expensive. Pre-mortems are one of the highest-leverage, lowest-cost tools in the operator toolkit. They take an hour. They save quarters.</p>

<h2>The exercise</h2>
<p>Before you commit to a significant initiative, run a 60-minute meeting. Whiteboard at the front. The facilitator opens:</p>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
"It's 12 months from now. We launched this initiative. It failed completely. The board is asking what happened. Take 10 minutes, by yourself, and write down every reason you can imagine for why it failed."
</blockquote>
<p>Silent individual writing first — critical. Then round-robin, each person reads one item. Build the list on the board. Discussion after. Resist the urge to defend or dismiss.</p>

<h2>Why this works</h2>
<ul>
  <li><strong>Reframes the question.</strong> "What could go wrong?" gets defensive answers. "Why did this fail?" — assumed past tense — gets more honest answers.</li>
  <li><strong>Permissions dissent.</strong> Saying "I think this will fail because X" in a kickoff meeting is socially expensive. Saying "one way this could have failed is X" in a pre-mortem is expected.</li>
  <li><strong>Surfaces assumptions.</strong> The most dangerous risks are the ones nobody questioned. Pre-mortems force them into the open.</li>
  <li><strong>Generates mitigations.</strong> Every failure mode is an opportunity to add a guardrail, an early warning, or a kill criterion.</li>
</ul>

<h2>Clustering the failure modes</h2>
<p>After the brainstorm, group the items into categories. Typical buckets:</p>
<ul>
  <li><strong>Market</strong> — customers didn't want it; the segment was wrong; competitors moved first</li>
  <li><strong>Execution</strong> — we shipped too late; scope ballooned; team wasn't strong enough</li>
  <li><strong>Technical</strong> — foundational tech decision wrong; scaling broke; integrations failed</li>
  <li><strong>Organizational</strong> — leadership didn't support it; teams didn't align; ownership unclear</li>
  <li><strong>Financial</strong> — ran out of runway; unit economics didn't work at scale</li>
  <li><strong>External</strong> — regulation changed; macro conditions changed; platform changed</li>
</ul>

<h2>From failure mode to action</h2>
<p>The most likely + most damaging failure modes each get:</p>
<ol>
  <li><strong>An early warning signal.</strong> What metric or event would tell us this is happening?</li>
  <li><strong>A prevention.</strong> What can we do now to reduce the probability?</li>
  <li><strong>A mitigation.</strong> If it happens anyway, what do we do to limit damage?</li>
  <li><strong>A decision-maker.</strong> Who has authority to pull the plug or change course?</li>
</ol>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Example.</strong><br>
<strong>Failure mode:</strong> "We built the wrong thing — customers didn't actually want it."<br>
<strong>Early warning:</strong> Design partners can't articulate value after 30 days.<br>
<strong>Prevention:</strong> 5 paid LOIs signed before engineering starts.<br>
<strong>Mitigation:</strong> Month-3 kill review; 50% pivot budget reserved.<br>
<strong>Decision-maker:</strong> CEO + product lead jointly.
</blockquote>

<h2>When to run a pre-mortem</h2>
<ul>
  <li>Before any initiative with &gt; 3 months runway or &gt; 2 FTE committed</li>
  <li>Before any irreversible decision (M&amp;A, hiring a senior exec, major platform switch)</li>
  <li>Before entering a new market</li>
  <li>Before a major pricing change</li>
</ul>
<p>Not for every sprint. You'd drown in pre-mortems. For the decisions that matter.</p>

<h2>The common mistake</h2>
<p>Running the pre-mortem, filing the notes, then never referencing them. The output has to feed somewhere — into the project's kill criteria, the WBR dashboard, the quarterly risk review. Otherwise you had a cathartic exercise that generated no durable value.</p>

<h2>What good looks like</h2>
<ul>
  <li>Every major initiative has a pre-mortem in its kickoff packet</li>
  <li>The top 3 failure modes each have an owner, an early warning, and a mitigation</li>
  <li>Pre-mortem outputs feed the <a href="../operating-systems/decision-logs.html">decision log</a> and the <a href="../risk/risk-management.html">risk register</a></li>
  <li>Teams bring up "we said this might happen in the pre-mortem" unprompted when it does happen</li>
</ul>

<p style="margin-top:40px;">Related: <a href="decision-frameworks.html">Decision frameworks</a> · <a href="what-to-kill.html">What to kill</a> · <a href="../risk/risk-management.html">Risk management</a></p>
""",
    prev=("What to kill", "what-to-kill.html"),
    nxt=("Decision frameworks", "decision-frameworks.html"),
)


write_bm_page(
    slug="strategy/decision-frameworks",
    title="Decision frameworks",
    description="Most bad decisions aren't bad judgment — they're the right judgment applied to the wrong kind of decision. Knowing which framework to use is half the skill.",
    reading_time=7,
    body_html="""
<p class="lede">Most bad decisions aren't bad judgment — they're the right judgment applied to the wrong kind of decision. A reversible, cheap choice deserves a different process than an irreversible, expensive one. Knowing which framework to use is half the skill. Executing it is the other half.</p>

<h2>The first question: Type 1 or Type 2?</h2>
<p>Bezos's framing. Two categories:</p>
<ul>
  <li><strong>Type 1 — one-way door.</strong> Irreversible or nearly so. Hiring a senior exec. Selling the company. Signing a 5-year lease. Deliberate, analytical, high-conviction.</li>
  <li><strong>Type 2 — two-way door.</strong> Reversible with low cost. Launching a feature. Trying a new marketing channel. Hiring a junior. Fast, biased toward action.</li>
</ul>
<p>The mistake most orgs make: treating Type 2 decisions like Type 1 (too slow), and Type 1 decisions like Type 2 (too careless). Get the type right first. Then pick the framework.</p>

<h2>Framework 1 — RAPID (for cross-functional decisions)</h2>
<p>For decisions that span teams. Name each role explicitly:</p>
<ul>
  <li><strong>R</strong>ecommend — proposes the decision, does the analysis</li>
  <li><strong>A</strong>gree — people whose sign-off is required (regulatory, legal, etc.)</li>
  <li><strong>P</strong>erform — who executes once decided</li>
  <li><strong>I</strong>nput — people consulted for information</li>
  <li><strong>D</strong>ecide — the single person who chooses</li>
</ul>
<p>The critical thing is that <strong>D is a single person</strong>. Not a committee. Not a consensus. One name.</p>

<h2>Framework 2 — Expected value</h2>
<p>When you can assign rough probabilities and values to outcomes:</p>
<pre style="background:#f5f5f7; padding:16px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:14px;">EV = Σ (probability of outcome × value of outcome)</pre>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Example.</strong> Should we pursue this $2M deal?<br>
- 30% chance we close at $2M → +$600K<br>
- 40% chance we close at $1M (discounted) → +$400K<br>
- 30% chance we lose → $0<br>
EV = $1M.<br>
Cost to pursue: ~$150K (sales engineering, exec time). EV/cost = 6.6x. Pursue.
</blockquote>
<p>The numbers are rough. The discipline is forcing yourself to actually assign probabilities instead of "it feels like a good opportunity."</p>

<h2>Framework 3 — Inversion</h2>
<p>From Charlie Munger. Instead of asking <em>"how do we succeed?"</em>, ask <em>"how do we guarantee failure?"</em> Then don't do those things. Often easier to generate a list of ways to fail than a list of ways to succeed.</p>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Example.</strong> How do we guarantee our product launch fails?<br>
- Launch without doing any customer discovery<br>
- Target a segment we've never sold to<br>
- Don't write positioning before building<br>
- Assume virality<br>
- Don't staff support<br>
Now: are we doing any of those?
</blockquote>

<h2>Framework 4 — Regret minimization</h2>
<p>When the expected-value math is too noisy to trust. Ask: <em>"In 10 years, which choice will I regret more?"</em> Particularly useful for career + life-scale decisions, but also for bet-the-company moves.</p>

<h2>Framework 5 — 70% rule</h2>
<p>General Jim Mattis's rule: <em>"If you have 70% of the information, go."</em> Waiting for 90% information usually means you've missed the window. 70% + good judgment beats 90% + late every time. For Type 2 decisions especially.</p>

<h2>Framework 6 — Pre-mortem</h2>
<p>Covered in detail: <a href="pre-mortems.html">Pre-mortems</a>. For high-stakes Type 1 decisions, always.</p>

<h2>The decision memo</h2>
<p>For any meaningful decision, write 1–2 pages before the decision. Template:</p>
<ul>
  <li><strong>Decision to be made</strong> (one sentence)</li>
  <li><strong>Context</strong> (why now?)</li>
  <li><strong>Options</strong> considered (usually 3)</li>
  <li><strong>Recommendation</strong> + reasoning</li>
  <li><strong>Risks</strong> + what would change the answer</li>
  <li><strong>Reversibility</strong> (Type 1 or 2?)</li>
</ul>
<p>The memo goes in the <a href="../operating-systems/decision-logs.html">decision log</a>. When you're in the situation six months later wondering "what were we thinking?" — this is the answer.</p>

<h2>What good looks like</h2>
<ul>
  <li>Every Type 1 decision produces a written memo before execution</li>
  <li>The decision-maker is always a single named person</li>
  <li>The team can distinguish Type 1 from Type 2 decisions and treat them accordingly</li>
  <li>Regular retros revisit past decisions against outcomes — not to blame, to learn</li>
</ul>

<p style="margin-top:40px;">Related: <a href="pre-mortems.html">Pre-mortems</a> · <a href="what-to-kill.html">What to kill</a> · <a href="../operating-systems/decision-logs.html">Decision logs</a></p>
""",
    prev=("Pre-mortems", "pre-mortems.html"),
    nxt=("Funnel math that matters", "../sales/funnel-math.html"),
)

print("\n✓ Finance + Strategy (10 pages)")
