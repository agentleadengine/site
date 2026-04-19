#!/usr/bin/env python3
"""Direct Response — The Offer + Copywriting (13 pages)."""
from _build_drm import write_drm_page


# ============================================================
# THE OFFER (6 pages)
# ============================================================

write_drm_page(
    slug="offer/value-equation",
    title="The value equation",
    description="Alex Hormozi's value equation is the single most useful one-line framework in modern direct response. Every time an offer underperforms, one of its four variables is out of whack.",
    reading_time=7,
    body_html="""
<p class="lede">Alex Hormozi's value equation is the single most useful one-line framework in modern direct response. Once you've internalized it, you stop guessing at why offers convert or don't — you diagnose the equation.</p>

<h2>The equation</h2>
<pre style="background:#f5f5f7; padding:20px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:15px; text-align:center;">
             Dream Outcome  ×  Perceived Likelihood
Value   =   ────────────────────────────────────────────
               Time Delay   ×   Effort &amp; Sacrifice
</pre>

<p>Value, as perceived by the buyer, is the ratio of what they'll get times how likely they'll get it, divided by how long it takes and how hard it is. Four variables. Every offer lives or dies on all four.</p>

<h2>Variable 1 — Dream outcome</h2>
<p>The outcome the prospect actually wants. Not what you sell; what <em>they</em> want. "A faster website" is a feature. "Your site never goes down during Black Friday again" is a dream outcome.</p>
<p>Moves that increase dream outcome:</p>
<ul>
  <li>Describe the end state in the prospect's language</li>
  <li>Specify what changes in their life, not in your product</li>
  <li>Paint sensory detail — what will Monday morning look like?</li>
  <li>Stack multiple outcomes when honest (main outcome + adjacent wins)</li>
</ul>

<h2>Variable 2 — Perceived likelihood of achievement</h2>
<p>The prospect's belief that the outcome will actually happen <em>for them</em>. Every prospect has seen promises fail. Their default is skepticism. Your job is to raise perceived likelihood without lying.</p>
<p>Moves that increase perceived likelihood:</p>
<ul>
  <li>Specific case studies with names, numbers, timeframes</li>
  <li>Social proof — testimonials, logos, usage metrics</li>
  <li>Concrete mechanism (see <a href="../market/sophistication.html">stage 3+ sophistication</a>)</li>
  <li>Guarantees (see <a href="guarantees.html">guarantees + risk reversal</a>)</li>
  <li>Credentials — your track record, your team's credentials</li>
  <li>Demonstrations — let them see it work before buying</li>
</ul>

<h2>Variable 3 — Time delay</h2>
<p>How long until they get the outcome. <em>Perceived</em> delay, not actual. If they believe it'll take 6 months, it takes 6 months in the equation, even if results start in week 1.</p>
<p>Moves that decrease time delay:</p>
<ul>
  <li>Specify when they'll see the first win (day 1, day 3, day 7)</li>
  <li>Break the outcome into early wins and final wins</li>
  <li>Offer "quick start" onboarding that produces a result fast</li>
  <li>Show before/after case studies with timeframes attached</li>
  <li>Deliver intermediate artifacts (the strategy doc on day 2, the full system in week 6)</li>
</ul>

<h2>Variable 4 — Effort &amp; sacrifice</h2>
<p>What the prospect has to do, give up, or endure to get the outcome. Work they'll do. Habits they'll change. People they'll upset. Risks they'll take.</p>
<p>Moves that decrease effort &amp; sacrifice:</p>
<ul>
  <li>Done-for-you instead of done-with-you, where possible</li>
  <li>Onboarding that removes friction (you set it up, not them)</li>
  <li>Pre-built templates, not blank pages</li>
  <li>Clear step-by-step — "just do these three things"</li>
  <li>Remove requirements ("no technical skills required," "no cold calls required")</li>
  <li>Bundle the ugly parts of the process into your service</li>
</ul>

<h2>Using the equation to diagnose weak offers</h2>
<p>Whenever an offer isn't converting, one of the four variables is the culprit. Run through the diagnostic:</p>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>The offer isn't converting — why?</strong><br>
1. <strong>Dream outcome</strong> — is what we're promising actually what they want? Or are we describing features?<br>
2. <strong>Perceived likelihood</strong> — do they believe it will work for them? What proof are they missing?<br>
3. <strong>Time delay</strong> — does it feel too slow? Can we reframe what they'll see in week 1?<br>
4. <strong>Effort</strong> — does this feel like more work than they can take on? What can we remove or take off their plate?
</blockquote>

<h2>The multiplicative property</h2>
<p>Each variable is a multiplier. Doubling dream outcome doubles value. Cutting effort in half doubles value. But zeroing out <em>any</em> variable zeros out the whole equation.</p>
<ul>
  <li>Zero dream outcome → no demand, no matter how easy or certain</li>
  <li>Zero perceived likelihood → nobody believes it, so nobody buys</li>
  <li>Infinite time delay → the benefit is too far away to motivate action</li>
  <li>Infinite effort → no one's willing to do the work</li>
</ul>
<p>The strongest offers don't maximize one variable — they optimize all four.</p>

<h2>Counterintuitive applications</h2>

<h3>Higher price can increase perceived likelihood</h3>
<p>"Free" products are associated with low-quality. A premium price signals quality and commitment. Raising price sometimes increases conversion because it raises perceived likelihood.</p>

<h3>Requiring effort can increase perceived outcome</h3>
<p>"Gym membership" that requires showing up is more valued than "pill that requires nothing." When prospects must invest effort, they believe the outcome more.</p>
<p>This doesn't contradict the equation — it's a case where one variable (effort) rises but another (perceived likelihood) rises more, net improving the value.</p>

<h2>Applying the equation to your next offer</h2>
<ol>
  <li>Write your offer.</li>
  <li>Score each variable on 1–10 from the prospect's perspective.</li>
  <li>Pick the lowest-scoring variable. That's where to invest effort.</li>
  <li>Ship the improved version. Re-score. Re-iterate.</li>
</ol>
<p>Most offers double conversion in 2–3 iterations of this loop. The equation is diagnostic. Use it.</p>

<p style="margin-top:40px;">Related: <a href="grand-slam.html">Grand slam offers</a> · <a href="bonuses.html">Bonuses that stack</a> · <a href="guarantees.html">Guarantees</a></p>
""",
    prev=("Picking a market", "../market/market-selection.html"),
    nxt=("Grand slam offers", "grand-slam.html"),
)


write_drm_page(
    slug="offer/grand-slam",
    title="Grand slam offers",
    description="Hormozi's grand slam offer: an offer so good prospects feel stupid saying no. Here's how it's actually constructed — and why most offers in the wild don't qualify.",
    reading_time=7,
    body_html="""
<p class="lede">Alex Hormozi's definition of a grand slam offer: <em>"an offer so good people feel stupid saying no."</em> It's not a gimmick. It's a deliberate construction. Most offers in the wild aren't grand slams — they're just products with prices. Turning the former into the latter is the highest-leverage move in direct response.</p>

<h2>What makes an offer "grand slam"</h2>
<p>A grand slam offer achieves:</p>
<ul>
  <li>The prospect can't reasonably decline at the price</li>
  <li>Conversion rates are materially higher than the category baseline (often 2–5x)</li>
  <li>Close rates at higher prices than the market usually supports</li>
  <li>The offer itself becomes a differentiator — not the product, the <em>offer</em></li>
</ul>

<h2>The construction</h2>

<h3>Step 1 — Nail the dream outcome</h3>
<p>Not "access to our tool." "The weekly report that shows you exactly which customers are about to cancel, with specific outreach scripts — delivered every Monday." The outcome is concrete and the prospect can see themselves using it.</p>

<h3>Step 2 — Stack bonuses that solve the obstacles</h3>
<p>List every objection a prospect might have. "I don't have time to set it up" → include white-glove onboarding. "I don't know how to do the strategy" → include templates. "I won't remember to use it" → include weekly accountability calls. Each bonus neutralizes a specific friction. See <a href="bonuses.html">bonuses that stack</a>.</p>

<h3>Step 3 — Reverse the risk</h3>
<p>A guarantee strong enough that the prospect's downside is near zero. "If you don't see X result in 90 days, full refund and keep the bonuses." If you can, go stronger — conditional refunds, performance-based guarantees, better-than-money-back. See <a href="guarantees.html">guarantees</a>.</p>

<h3>Step 4 — Justify the price</h3>
<p>Show the math. "The competitor pricing for just the strategy alone is $5K/mo. The template library would cost $3K to build in-house. The onboarding is worth $2K. Total value: $42K/year. Your price: $12K/year." The price becomes a concession, not an ask.</p>

<h3>Step 5 — Add urgency</h3>
<p>A real reason to buy now. Cohort closing, bonuses expiring, price increasing, capacity filling. Urgency without substance is manipulation; urgency with substance is professional courtesy. See <a href="urgency-scarcity.html">urgency + scarcity</a>.</p>

<h2>The offer stack</h2>
<p>A grand slam offer isn't one item — it's a stack. Hormozi's template:</p>
<ul>
  <li>Core product / service (what you actually deliver)</li>
  <li>Bonus 1 — solves the #1 objection</li>
  <li>Bonus 2 — solves the #2 objection</li>
  <li>Bonus 3 — accelerates time to first result</li>
  <li>Bonus 4 — reduces the work / effort required</li>
  <li>Bonus 5 — fast-action incentive (only if they buy today)</li>
  <li>The guarantee</li>
  <li>The urgency</li>
</ul>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Example — B2B SaaS offer.</strong><br>
<strong>Core:</strong> 12 months of our sales pipeline tool ($12K)<br>
<strong>Bonus 1:</strong> White-glove implementation + CRM integration ($4K value)<br>
<strong>Bonus 2:</strong> Custom playbook built for your vertical ($3K)<br>
<strong>Bonus 3:</strong> 90-day "done-for-you" pipeline review with our CEO ($10K)<br>
<strong>Bonus 4:</strong> Quarterly check-ins with our top customer-success lead (priceless, but $6K if billed)<br>
<strong>Bonus 5 (fast action):</strong> Free enterprise SSO &amp; SOC 2 artifact package, if signed by Friday ($5K)<br>
<strong>Guarantee:</strong> If pipeline hasn't 2x'd in 6 months, you get a full refund plus $5K for your trouble<br>
<strong>Urgency:</strong> We onboard 4 clients a month. 2 slots left for this cohort.<br>
<strong>Total stack value:</strong> $40K+<br>
<strong>Your investment:</strong> $12K
</blockquote>

<h2>What most people get wrong</h2>

<h3>They price based on cost, not value</h3>
<p>Cost-plus pricing leaves money on the table. Price on value — what it's worth to the customer — then justify it with the stack. See <a href="pricing-psychology.html">pricing psychology</a>.</p>

<h3>They add bonuses that don't solve objections</h3>
<p>Random bonuses feel like filler. Each bonus must neutralize a specific thing preventing the sale. "Solves a pain point I actually have" beats "more stuff."</p>

<h3>They skip the guarantee</h3>
<p>Without a guarantee, the prospect carries all the risk. That's why most offers don't convert. A strong guarantee shifts risk from the prospect to you — and the data shows the refund rate stays manageable when the product delivers.</p>

<h3>They make it too long</h3>
<p>A grand slam offer should fit on one page. The stack should be scannable. If you need 4 paragraphs to explain each bonus, the offer is overbuilt.</p>

<h3>They forget the "feel stupid saying no" threshold</h3>
<p>Ask yourself: would <em>you</em> buy this today, in the prospect's shoes, at this price? If the answer is "maybe," the offer isn't grand slam yet. Keep building.</p>

<h2>Grand slam for services, products, and SaaS</h2>
<ul>
  <li><strong>Services:</strong> stack on templates, done-for-you components, guaranteed deliverables by date</li>
  <li><strong>Products:</strong> stack on complementary products, training, lifetime access, extended warranty</li>
  <li><strong>SaaS:</strong> stack on implementation, training, custom integrations, dedicated success manager</li>
</ul>

<h2>The test</h2>
<p>Present the offer to 5 prospects who fit your ICP. Watch their reaction.</p>
<ul>
  <li>If they say "that's interesting, let me think about it" — not grand slam yet</li>
  <li>If they say "I need to compare to other options" — not grand slam</li>
  <li>If they say "wait, what's the catch?" — you're close</li>
  <li>If they pull out a credit card in the conversation — it's a grand slam</li>
</ul>

<p style="margin-top:40px;">Related: <a href="value-equation.html">Value equation</a> · <a href="bonuses.html">Bonuses that stack</a> · <a href="guarantees.html">Guarantees</a> · <a href="pricing-psychology.html">Pricing psychology</a></p>
""",
    prev=("The value equation", "value-equation.html"),
    nxt=("Bonuses that stack", "bonuses.html"),
)


write_drm_page(
    slug="offer/bonuses",
    title="Bonuses that stack",
    description="The right bonus isn't a freebie — it's a targeted tool that removes a specific objection, accelerates a result, or raises the perceived value of the core offer.",
    reading_time=6,
    body_html="""
<p class="lede">A bonus isn't a bribe to buy. A well-designed bonus does one specific thing: it removes a friction between the prospect and the purchase. The best bonuses aren't extras — they're load-bearing. Without them, the offer wouldn't close.</p>

<h2>What bonuses actually do</h2>
<ul>
  <li><strong>Remove objections.</strong> "I don't have time" → done-for-you setup. "I don't know how to use it" → onboarding call.</li>
  <li><strong>Accelerate time to first result.</strong> A quick-start template, a live session that produces an artifact, a 24-hour response queue.</li>
  <li><strong>Reduce effort.</strong> Templates, checklists, swipe files, automations.</li>
  <li><strong>Increase perceived likelihood.</strong> Success playbooks, case study access, community of peers.</li>
  <li><strong>Justify price.</strong> Visible value stacks that make the price feel like a concession.</li>
</ul>

<h2>The bonus design process</h2>

<h3>Step 1 — List every objection</h3>
<p>Before designing bonuses, list every reason the prospect might say no:</p>
<ul>
  <li>Too expensive</li>
  <li>Not sure it works for me</li>
  <li>No time to implement</li>
  <li>Don't trust the company</li>
  <li>Have tried similar before; didn't work</li>
  <li>Needs approval from someone else</li>
  <li>Timing is wrong</li>
  <li>Need technical help I don't have</li>
</ul>
<p>Every bonus in your stack should neutralize at least one item on this list.</p>

<h3>Step 2 — Match bonus to objection</h3>
<table style="width:100%; border-collapse:collapse; margin:20px 0;">
  <tr style="background:#f5f5f7;"><th style="padding:10px; text-align:left; border:1px solid #e5e5ea;">Objection</th><th style="padding:10px; text-align:left; border:1px solid #e5e5ea;">Bonus that addresses it</th></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Too expensive</td><td style="padding:10px; border:1px solid #e5e5ea;">Stack of bonuses that make price a bargain</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Not sure it works for me</td><td style="padding:10px; border:1px solid #e5e5ea;">Case studies, guarantees, free audit</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">No time to implement</td><td style="padding:10px; border:1px solid #e5e5ea;">Done-for-you setup, white-glove onboarding</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Don't trust the company</td><td style="padding:10px; border:1px solid #e5e5ea;">Founder's direct line, public customer list, transparent operations</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Tried similar before, didn't work</td><td style="padding:10px; border:1px solid #e5e5ea;">Diagnostic session that proves the mechanism works for them</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Needs approval from others</td><td style="padding:10px; border:1px solid #e5e5ea;">ROI calculator, executive summary, reference calls</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Timing is wrong</td><td style="padding:10px; border:1px solid #e5e5ea;">Flexible start dates, pause/freeze policy</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Needs technical help</td><td style="padding:10px; border:1px solid #e5e5ea;">Integration assistance, engineering hours, templates</td></tr>
</table>

<h2>The bonus hierarchy</h2>
<p>Not every bonus is equal. Rank yours:</p>

<h3>Tier 1 — Bonuses that close deals</h3>
<p>Remove the #1 and #2 objections. Without these, the deal doesn't happen.</p>

<h3>Tier 2 — Bonuses that raise perceived value</h3>
<p>Don't directly close, but make the price feel small. Complementary templates, training libraries, community access.</p>

<h3>Tier 3 — Fast-action bonuses</h3>
<p>Only available if the prospect buys by a deadline. Creates urgency without requiring artificial scarcity. "Buy by Friday and we'll include the implementation workshop (normally $2K, free for fast-action buyers)."</p>

<h2>Pricing bonuses</h2>
<p>Every bonus gets a price tag, even if the prospect would never pay that price for it alone. The price anchors perceived value. A bonus "worth $2,000" that you can credibly defend is worth far more than a vague "extra templates."</p>
<p>How to price bonuses credibly:</p>
<ul>
  <li>What would it cost to buy this elsewhere?</li>
  <li>What would it cost in billable hours to build?</li>
  <li>What's the outcome worth to the prospect?</li>
</ul>
<p>If you can't defend the price, lower it or drop the bonus.</p>

<h2>The 10x rule</h2>
<p>Hormozi's guideline: the total stack value should be 10x the price. A $1K offer should have $10K of stacked value. A $10K offer should have $100K. This sounds absurd until you build one — and see the math work.</p>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
The 10x rule isn't a marketing trick. It's a reframing discipline. If you can't find $10K worth of value to provide for a $1K price, you don't have a good offer — you have a commoditized product. The exercise of stacking forces you to find the value.
</blockquote>

<h2>Common bonus mistakes</h2>

<h3>Vague bonus descriptions</h3>
<p>"Bonus training materials" is weak. "The 43-page Pipeline Playbook — exactly how our top customer went from $200K to $2M ARR in 14 months" is strong. Specific &gt; general.</p>

<h3>Bonuses that aren't valuable</h3>
<p>Adding a worthless bonus ("PDF of our blog posts!") dilutes the stack. Fewer, better bonuses beat more, worse ones.</p>

<h3>Bonuses that are orthogonal to the core offer</h3>
<p>If the core is sales pipeline software, a free stock photo library doesn't fit. Bonuses should be inside the same universe as the core outcome.</p>

<h3>Bonuses that undercut the core offer</h3>
<p>If a bonus is so good it cannibalizes the core — the prospect wants the bonus, not the product — you've built the wrong stack.</p>

<h2>Sequencing bonuses</h2>
<p>On the offer page, list bonuses in this order:</p>
<ol>
  <li>The most emotionally compelling / desired bonus first</li>
  <li>The bonuses that solve the top 2–3 objections next</li>
  <li>The fast-action bonus last (tied to urgency)</li>
</ol>
<p>The first bonus captures attention. The middle bonuses neutralize hesitation. The last one creates pressure to act now.</p>

<p style="margin-top:40px;">Related: <a href="grand-slam.html">Grand slam offers</a> · <a href="guarantees.html">Guarantees + risk reversal</a> · <a href="urgency-scarcity.html">Urgency + scarcity</a></p>
""",
    prev=("Grand slam offers", "grand-slam.html"),
    nxt=("Guarantees", "guarantees.html"),
)


write_drm_page(
    slug="offer/guarantees",
    title="Guarantees + risk reversal",
    description="A guarantee moves the risk of the transaction from the buyer to the seller. A strong guarantee is the single most powerful conversion lever available — and most businesses still don't use it.",
    reading_time=7,
    body_html="""
<p class="lede">A guarantee moves the risk of the transaction from the buyer to the seller. Done right, it's the single most powerful conversion lever available — often adding 30–100% to close rates. Done wrong, it adds refund liability and nothing else. Hopkins, Kennedy, Halbert, and Hormozi all taught guarantees. The specifics matter.</p>

<h2>Why guarantees work</h2>
<p>Every purchase involves risk. The prospect isn't sure it'll work for them. They're not sure the company will deliver. They're not sure they'll be able to return if it doesn't. A guarantee neutralizes that risk — moving it to the seller — which is where, by every ethical and commercial argument, it belongs.</p>

<h2>The guarantee ladder</h2>
<p>Weak to strong:</p>

<h3>1. No guarantee</h3>
<p>"All sales final." Prospect carries all risk. Lowest conversion. Used where it has to be (time-sensitive services already rendered), otherwise avoid.</p>

<h3>2. Standard money-back</h3>
<p>"30-day money back if not satisfied." Better than nothing. Unremarkable in 2026 — it's table stakes.</p>

<h3>3. Extended money-back</h3>
<p>"90 days or 6 months or 1 year money-back." Counterintuitive insight: extending the guarantee often <em>lowers</em> refund rates. Longer guarantees signal confidence, attract more buyers, and give customers time to integrate the product into their lives. Kennedy taught this aggressively.</p>

<h3>4. Conditional / performance</h3>
<p>"If you don't see X specific result in Y time, full refund." Much stronger than generic satisfaction guarantees because it's measurable. Requires the product to actually produce the result, which is why it works: only sellers with confidence offer it.</p>

<h3>5. Better-than-money-back</h3>
<p>"Not only do we refund, we pay you $500 for your time." Or "refund + keep the bonuses." Or "refund + a free month of our best competitor." Dramatically raises perceived value. Refund rates rarely increase proportionally.</p>

<h3>6. Keep-it-all</h3>
<p>"Try it free for 30 days. If you cancel, you keep everything — the courseware, the templates, the community access." Highest conversion. Works only for products with low marginal cost per user.</p>

<h3>7. Pay-for-results</h3>
<p>"You only pay when X happens." The strongest form. Often used in agencies and high-ticket services. Drastically changes the sales conversation — it's no longer "will it work" but "how quickly will we hit the milestone."</p>

<h2>The guarantee premium</h2>
<p>You can charge more with a strong guarantee. A $1,000 product with a weak guarantee competes with everything. A $3,000 product with a better-than-money-back guarantee is in a category of one.</p>

<h2>Designing your guarantee</h2>

<h3>Step 1 — Identify the real fear</h3>
<p>What specifically is the prospect afraid of? Not "it won't work" — that's too vague. Specifically:</p>
<ul>
  <li>"I'll pay and you'll disappear"</li>
  <li>"I'll pay, try it, and it'll take too long to see results"</li>
  <li>"I'll pay, try it, and decide it's not right for me — and be stuck"</li>
  <li>"It'll work for others but not for my situation"</li>
</ul>

<h3>Step 2 — Design the guarantee to address the specific fear</h3>
<ul>
  <li>"I'll pay and you'll disappear" → offer refund escrow, payment on delivery, or milestone-based pricing</li>
  <li>"Take too long to see results" → offer money-back within X days if first milestone isn't hit</li>
  <li>"Decide it's not right and be stuck" → generous cancellation / refund window</li>
  <li>"Won't work for my situation" → pre-purchase fit call, partial refund if determined not a fit in first 30 days</li>
</ul>

<h3>Step 3 — State it specifically</h3>
<p>Vague guarantees don't work. "We stand behind our product" isn't a guarantee. "If you don't achieve X by day 90, email us and we'll refund you within 3 business days — no questions asked" is a guarantee.</p>

<h2>Common guarantee mistakes</h2>

<h3>Requiring proof of effort</h3>
<p>"Money back if you completed all exercises" sounds reasonable and kills conversion. Every barrier you put on the guarantee raises prospect suspicion. Prospects read "money back" and mean it; they read "money back, if..." as "money back, probably not."</p>

<h3>Too short a window</h3>
<p>A 7-day guarantee isn't long enough to use most products meaningfully. Most refund requests come in the first 10 days; a 30-day guarantee doesn't meaningfully raise refund rate over a 7-day.</p>

<h3>Not stating it prominently</h3>
<p>The guarantee should be on the offer page, in the order form, in the email follow-up, and sometimes in the product itself. Prospects forget guarantees if they're only mentioned once in fine print.</p>

<h3>Hedging the language</h3>
<p>"Satisfaction guarantee*" with an asterisk destroys trust. Either the guarantee is clear or it's not. If you need an asterisk, rewrite the guarantee until you don't.</p>

<h2>The refund rate reality</h2>
<p>Operators fear guarantees will flood them with refunds. Empirically, across most categories:</p>
<ul>
  <li>Strong guarantees increase sales by 20–100%</li>
  <li>Refund rates typically stay at 3–8%</li>
  <li>Net revenue after refunds rises sharply</li>
  <li>A small percentage of refunders become customers of different products later</li>
</ul>
<p>The only exception: low-quality products where the guarantee exposes the quality gap. In that case, the answer isn't a weaker guarantee — it's a better product.</p>

<h2>Stacking guarantees</h2>
<p>You can stack multiple guarantees. Hormozi's frequent structure:</p>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Guarantee 1:</strong> If you attend every session and don't see X result, full refund.<br>
<strong>Guarantee 2:</strong> If at any point you feel we're not delivering, full refund of any unused time.<br>
<strong>Guarantee 3:</strong> If you qualify but we can't help, we'll pay for you to work with our top competitor.
</blockquote>
<p>Each guarantee addresses a different fear. Together they compress prospect risk to near zero.</p>

<h2>Refund request handling</h2>
<p>When someone asks for a refund:</p>
<ol>
  <li>Process it fast (within 3 business days; same day is better)</li>
  <li>Don't interrogate or guilt</li>
  <li>Ask one neutral question: "Is there anything we could have done differently?" (for learning, not to argue)</li>
  <li>Process the refund</li>
  <li>Thank them</li>
</ol>
<p>A well-handled refund often converts into a future customer or a referral. A poorly handled one generates online complaints that cost 10x the refund amount in lost future sales.</p>

<p style="margin-top:40px;">Related: <a href="value-equation.html">Value equation</a> · <a href="grand-slam.html">Grand slam offers</a> · <a href="pricing-psychology.html">Pricing psychology</a></p>
""",
    prev=("Bonuses that stack", "bonuses.html"),
    nxt=("Pricing psychology", "pricing-psychology.html"),
)


write_drm_page(
    slug="offer/pricing-psychology",
    title="Pricing psychology",
    description="Price is signal, not just cost. Move the price and you move perceived quality, effort expected, customer profile, and retention — all before anyone buys.",
    reading_time=7,
    body_html="""
<p class="lede">Price is signal, not just cost. How you price changes which prospects show up, what they expect, how they treat the relationship, and how they use the product. Operators who think of price only as "what the market will bear" are leaving everything else on the table.</p>

<h2>What price signals</h2>
<ul>
  <li><strong>Quality.</strong> Higher price = higher assumed quality, absent contradicting evidence.</li>
  <li><strong>Scarcity.</strong> Expensive = fewer available; cheap = commodity.</li>
  <li><strong>Customer profile.</strong> A $97 product attracts price-sensitive buyers; a $9,700 product attracts investment-oriented ones. Same product, different customers.</li>
  <li><strong>Commitment.</strong> Higher-priced customers use the product more (sunk-cost effect — but the healthy version).</li>
  <li><strong>Effort expected.</strong> Cheap implies easy / quick; expensive implies substantive and effortful.</li>
</ul>

<h2>The price-quality heuristic</h2>
<p>When prospects can't fully evaluate quality (most complex purchases), price becomes a proxy. "Cheap wine," "discount lawyer," "budget surgeon" — all concepts that carry real weight. Sometimes dropping price <em>decreases</em> sales because prospects conclude you're lower quality.</p>

<h2>Anchoring</h2>
<p>The first price a prospect sees sets the reference point. Every subsequent price is evaluated relative to it.</p>
<ul>
  <li>Show the "full value" price first, then your price. Your price feels smaller.</li>
  <li>Offer three tiers. The middle tier sells most; the top tier makes the middle feel reasonable.</li>
  <li>Compare to the cost of <em>not</em> solving the problem. "You lose $5K/month to this right now. Our price is $500/month."</li>
</ul>

<h2>The three-tier structure</h2>
<p>Good / Better / Best. Standard for a reason:</p>
<ul>
  <li><strong>Good</strong> — entry-level, addresses the core need. Often sold at break-even to get customers in the door.</li>
  <li><strong>Better</strong> — the "recommended" tier. Most customers pick this. Price it to be the profit engine.</li>
  <li><strong>Best</strong> — premium tier. Lower volume. Makes Better look reasonable. Often the profit ceiling.</li>
</ul>
<p>Not more than three tiers. Four tiers fragment the decision. One tier removes comparison and forces the prospect to compare to alternatives outside your store — usually not your favor.</p>

<h2>Decoy pricing</h2>
<p>Dan Ariely's famous insight: a third option that's intentionally worse-value makes the "good" option look like a bargain. Classic example — Economist magazine:</p>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Without decoy:</strong><br>
Online only: $59<br>
Print + online: $125<br>
Sales: 68% online-only, 32% print+online.<br><br>
<strong>With decoy (print-only at $125):</strong><br>
Online only: $59<br>
Print only: $125<br>
Print + online: $125<br>
Sales: 16% online-only, 0% print-only, 84% print+online.<br><br>
The decoy doesn't have to sell. It has to make the intended option look like the obvious choice.
</blockquote>

<h2>Charm pricing</h2>
<p>$.99, $X97, $X99. Research is mixed. Usually works in consumer markets where the buyer is price-sensitive. Usually doesn't work — and can even hurt — in premium B2B markets where it reads as discount-focused.</p>
<p>Rule: charm pricing fits mass-market products; round pricing ($5,000, not $4,997) fits premium / high-consideration purchases.</p>

<h2>Payment structures</h2>
<p>Not just the number, the structure:</p>
<ul>
  <li><strong>One-time payment</strong> — simple, higher up-front commitment, better for products with finite delivery</li>
  <li><strong>Monthly subscription</strong> — lower entry friction, recurring revenue, works for ongoing value</li>
  <li><strong>Pay-in-four / installments</strong> — reduces perceived price, common in info products and high-ticket courses</li>
  <li><strong>Performance-based</strong> — "pay when you see results" — highest conversion but highest operational complexity</li>
  <li><strong>Annual upfront with discount</strong> — trades a % discount for 12 months of cash + retention</li>
</ul>
<p>The right structure depends on what the customer wants. Monthly subscriptions feel cheap; annual feels committed. Pay-in-four feels flexible; one-time feels clean.</p>

<h2>Raising prices</h2>
<p>The most underused lever in operator tool-kits. Prices should rise:</p>
<ul>
  <li>As the product improves</li>
  <li>As your brand grows</li>
  <li>As your list of case studies grows</li>
  <li>When your close rates are too high (above ~50% on qualified leads means you're underpriced)</li>
  <li>When churn is low enough that a price increase won't materially raise it</li>
</ul>
<p>The playbook: raise prices for new customers first. Watch conversion. If conversion holds, raise again. Grandfather existing customers (or migrate them with meaningful notice and honest communication). Repeat every 12–18 months.</p>

<h2>Discounts — use carefully</h2>
<p>Discounts generate short-term cash at the cost of long-term brand damage. Rules:</p>
<ul>
  <li>Never discount for no reason. Every discount needs a story ("spring cohort," "new customer bonus," "referral reward")</li>
  <li>Never normalize discount-driven buying. If every buyer waits for a promo, your pricing is wrong</li>
  <li>Prefer bonuses over discounts. Bonuses add perceived value; discounts destroy it</li>
  <li>Discount for a reason that doesn't repeat — not because "that customer pushed hard"</li>
</ul>

<h2>The price-anchoring in copy</h2>
<p>Before revealing price, anchor with value:</p>
<ol>
  <li>"What's the problem worth to solve?" — reader answers in their head</li>
  <li>"What would this cost to solve another way?" — comparison anchor</li>
  <li>"Here's everything you get" — stack, with each line priced</li>
  <li>"Total value: $X" — anchor</li>
  <li>"Your price today: $Y" — reveal, where Y is 20–50% of X</li>
</ol>
<p>The reader's first emotional response to Y is "wait, that's a lot less than X." That's the effect you want.</p>

<p style="margin-top:40px;">Related: <a href="value-equation.html">Value equation</a> · <a href="grand-slam.html">Grand slam offers</a> · <a href="urgency-scarcity.html">Urgency + scarcity</a></p>
""",
    prev=("Guarantees", "guarantees.html"),
    nxt=("Urgency + scarcity", "urgency-scarcity.html"),
)


write_drm_page(
    slug="offer/urgency-scarcity",
    title="Urgency + scarcity",
    description="Urgency moves prospects from 'someday' to 'today.' Scarcity moves them from 'comparing' to 'choosing.' Both are ethical when the reason is real — and manipulative when it isn't.",
    reading_time=6,
    body_html="""
<p class="lede">Urgency answers the question "why now?" Scarcity answers "why this?" Together they're the second-most-powerful conversion lever after the <a href="guarantees.html">guarantee</a> — when used honestly. The line between ethical urgency and manipulative urgency is sharp, and modern prospects can tell the difference immediately.</p>

<h2>Urgency vs. scarcity</h2>
<ul>
  <li><strong>Urgency</strong> — time-based. The price or offer changes at a specific time.</li>
  <li><strong>Scarcity</strong> — quantity-based. There are a limited number of X.</li>
</ul>
<p>Both address "I'll think about it" — the #1 killer of direct response campaigns.</p>

<h2>The prospect's default</h2>
<p>Every prospect, unchallenged, will delay. Delay is psychologically cheap. The brain treats "I'll decide later" as resolving the tension. A campaign that doesn't force a decision now gets no decision at all.</p>
<p>Urgency and scarcity break the delay pattern. They tell the prospect: not deciding <em>is</em> deciding.</p>

<h2>Real reasons for urgency</h2>
<ol>
  <li><strong>Cohort launch.</strong> You open the course 4x/year. Miss this one, wait 3 months.</li>
  <li><strong>Price increase.</strong> Price rises $500 on Monday. Real because the price actually rises.</li>
  <li><strong>Bonus expiring.</strong> The bonus is only included if signed by Friday. Real because the bonus has cost to provide.</li>
  <li><strong>Capacity.</strong> You onboard X clients/month. This month's slots close when full.</li>
  <li><strong>External deadline.</strong> "Q1 planning season — need to be onboarded by Jan 15 to impact Q1."</li>
  <li><strong>Seasonal.</strong> "Tax filing deadline in 6 weeks." The deadline isn't yours; it exists in the world.</li>
  <li><strong>Inventory.</strong> Limited supply. Real because once it's gone it's gone.</li>
</ol>

<h2>Real reasons for scarcity</h2>
<ol>
  <li><strong>Service capacity.</strong> You can only serve N customers without degrading quality.</li>
  <li><strong>Physical inventory.</strong> Hard-limited stock.</li>
  <li><strong>Licensed / exclusive.</strong> "Only 10 companies per industry."</li>
  <li><strong>Skill-dependent.</strong> "I can only personally work with 6 clients."</li>
  <li><strong>Cohort size.</strong> Quality of program requires group size under X.</li>
</ol>

<h2>The manufactured kind — avoid</h2>
<p>Fake urgency destroys trust. Examples:</p>
<ul>
  <li>"Countdown timer" that resets if you leave and come back</li>
  <li>"Only 3 spots left" that stays at 3 for weeks</li>
  <li>"Price going up Monday" every Monday for a year</li>
  <li>"Limited edition" with unlimited quantity</li>
</ul>
<p>Prospects are pattern-matchers. They see the fake urgency pattern and file your brand under "not trustworthy" immediately. Conversion lifts in the short term; trust crashes in the long term. Not worth it.</p>

<h2>How to use urgency honestly</h2>

<h3>State the reason</h3>
<p>"Price rises to $5,000 on Friday at 5pm EST" is 10x stronger than "limited-time pricing." The specific reason makes it believable.</p>

<h3>Make it specific</h3>
<p>"Ends Friday at midnight" beats "ends this week." Specific deadlines feel real.</p>

<h3>Actually honor it</h3>
<p>If you say the price rises Friday, it rises Friday. If a prospect emails Monday asking for the old price, you say no politely. Once you break the deadline, all future deadlines become noise. Your word is the only thing that makes urgency work.</p>

<h3>Repeat it</h3>
<p>Mention the deadline in every touch — email, sales call, landing page, order form. Repetition isn't manipulation; it's information. Many prospects genuinely haven't noticed.</p>

<h2>How to use scarcity honestly</h2>

<h3>Tie it to capacity</h3>
<p>"We take on 3 new clients a month. After that, the next opening is October." You're not manipulating — you're describing real operational capacity.</p>

<h3>Show the counter</h3>
<p>"2 of 10 spots remaining" is powerful when it's real. Show the current number; update it in real time; let the buyer see the scarcity happen.</p>

<h3>Explain why it's limited</h3>
<p>"Our onboarding process requires 8 hours of our team's time per client, which is why we cap at 10 new clients monthly." The why makes the scarcity credible.</p>

<h2>The urgency sequence</h2>
<p>For a time-limited offer:</p>
<ol>
  <li><strong>Announce</strong> — 7 days before deadline. Explain the offer and the deadline.</li>
  <li><strong>Remind</strong> — 3 days before. Quick reminder + social proof of who's signed.</li>
  <li><strong>Last chance</strong> — 24 hours before. Clear subject line: "24 hours left."</li>
  <li><strong>Final hours</strong> — 6 hours before. Shorter, punchier.</li>
  <li><strong>Final hour</strong> — 1 hour before. One last email; one last push.</li>
  <li><strong>Closed</strong> — after deadline. Announce closure. Offer waitlist for the next cohort.</li>
</ol>
<p>A significant portion of revenue comes from the last 24 hours. That's not manipulation — it's prospects finally deciding.</p>

<h2>Urgency without a hard deadline</h2>
<p>Sometimes a hard deadline isn't honest. Options:</p>
<ul>
  <li><strong>Rolling urgency.</strong> "Price rises the day after your first call." Prospect-specific deadline — real because the policy applies.</li>
  <li><strong>Cost-of-waiting.</strong> "Every month you delay is $X lost. Here's the math." Urgency from the prospect's own problem, not from you.</li>
  <li><strong>Milestone-based.</strong> "To hit your Q2 goal, you'd need to start by March 15. Today is March 10." Math-driven.</li>
</ul>

<h2>The ethical test</h2>
<p>Two questions:</p>
<ol>
  <li>If a prospect asked "why this deadline?" — could I answer honestly, on the record, in a way they'd find reasonable?</li>
  <li>If a prospect missed the deadline and came back, would I actually say no?</li>
</ol>
<p>If yes to both, the urgency is real. If no to either, you're manufacturing, and the short-term lift isn't worth the long-term brand cost.</p>

<p style="margin-top:40px;">Related: <a href="grand-slam.html">Grand slam offers</a> · <a href="guarantees.html">Guarantees</a> · <a href="../foundations/ten-rules.html">Kennedy's 10 rules</a></p>
""",
    prev=("Pricing psychology", "pricing-psychology.html"),
    nxt=("The copywriting stack", "../copy/the-stack.html"),
)


# ============================================================
# COPYWRITING (7 pages)
# ============================================================

write_drm_page(
    slug="copy/the-stack",
    title="The copywriting stack",
    description="Great direct-response copy isn't a single skill — it's a stack of layered moves. Master the stack and you can dissect any winning ad and understand why it works.",
    reading_time=7,
    body_html="""
<p class="lede">Every piece of direct-response copy that works is working at multiple levels simultaneously — headline, lead, body, close, CTA, P.S. — each doing a specific job. Master the stack and you stop thinking about copy as inspiration and start producing it on schedule.</p>

<h2>The stack, top to bottom</h2>
<ol>
  <li><strong>Headline</strong> — gets attention, promises value, earns the next sentence</li>
  <li><strong>Pre-header / deck</strong> — qualifies the audience, deepens the headline promise</li>
  <li><strong>Lead</strong> — the first 50–100 words; hooks emotionally, defines the problem</li>
  <li><strong>Body</strong> — substance, proof, mechanism, benefits</li>
  <li><strong>Bullets</strong> — the scan-able benefit claims (the "fascinations")</li>
  <li><strong>Offer</strong> — what's being sold, at what price, with what bonuses + guarantee</li>
  <li><strong>CTA</strong> — the specific next action</li>
  <li><strong>P.S.</strong> — restates the core value + deadline; second most-read element</li>
</ol>

<h2>Each layer's job</h2>

<h3>Headline — "should I keep reading?"</h3>
<p>The headline's only job is to earn the next line. Halbert's rule: 80% of the success of an ad is in the headline. See <a href="headlines.html">headlines</a>.</p>

<h3>Lead — "is this about me?"</h3>
<p>The lead is where the prospect decides whether the copy is speaking to them. The lead agitates a problem, describes a moment, or makes a promise so specific that the right prospect sees themselves in it. See <a href="the-lead.html">the lead</a>.</p>

<h3>Body — "why should I believe this?"</h3>
<p>Body copy is the proof layer. Mechanism (why your solution works). Evidence (case studies, data). Social proof (testimonials). Reason-why (Hopkins' term). Every claim is earned, not asserted. See <a href="body-copy.html">body copy</a>.</p>

<h3>Bullets — "what specifically do I get?"</h3>
<p>Bullets are the scan layer. Prospects who won't read the body will read bullets. Each bullet is a punchy benefit claim — specific, intriguing, and often a tiny mystery (the "fascination"). See <a href="bullets.html">fascination bullets</a>.</p>

<h3>Offer — "what's the deal?"</h3>
<p>The offer stack — core product, bonuses, guarantee, urgency. See the <a href="../offer/grand-slam.html">offer section</a>.</p>

<h3>CTA — "what do I do next?"</h3>
<p>The specific next action, stated clearly. Not "learn more" — "Click below to book your strategy call before Friday." See <a href="ctas.html">CTAs</a>.</p>

<h3>P.S. — "the second read"</h3>
<p>After the headline, the P.S. is the most-read element on long-form copy. Used to restate the offer, the deadline, or to introduce a final reason to act. Halbert used the P.S. heavily.</p>

<h2>Principles that apply at every layer</h2>

<h3>One person, one conversation</h3>
<p>Every piece of copy is written to one reader. Not "dear customers." Not "businesses." One person. In their voice. About their problem. The illusion of one-to-one is what copy is doing — even when it's being read by 100,000 people.</p>

<h3>Specificity beats generality</h3>
<p>Hopkins' rule. Every abstract claim becomes a concrete one. "Fast" becomes "returns in 4.2 hours." "Popular" becomes "used by 2,341 teams." "Effective" becomes "47% reduction in churn in 90 days."</p>

<h3>Benefits, not features</h3>
<p>A feature is what it is. A benefit is what it does for the reader. A feature + benefit pair connects them: "[feature], which means [benefit], so you [outcome]."</p>

<h3>Prove every claim</h3>
<p>Every claim is followed by proof. Specific number → source. Testimonial → name + title + result. Case study → before / after with timeframe. Unproven claims are skipped by sophisticated prospects.</p>

<h3>Show, don't describe</h3>
<p>Whenever possible, demonstrate rather than claim. A screenshot of the dashboard beats "clean UI." A before/after case study beats "great results." A live video beats "easy setup."</p>

<h3>Write to the skeptic</h3>
<p>Assume the reader is reasonably skeptical. Every claim has to survive a raised eyebrow. Writing for the easy case (the believer) leaves conversion on the table; writing for the skeptic brings both along.</p>

<h3>Rhythm and readability</h3>
<p>Short sentences. Short paragraphs. Bullets, bold, callouts. Prospects skim first, then read. Make the skim rewarding enough to pull them into the read.</p>

<h2>Common stack failures</h2>

<h3>Great headline, weak lead</h3>
<p>Prospect clicks in and gets a generic intro paragraph. Mismatch. They leave. The lead must deliver on the headline's promise immediately.</p>

<h3>Strong lead, weak body</h3>
<p>Prospect is hooked but doesn't get the proof to believe. Conversion leaks in the body. Fix by adding case studies, mechanism, and social proof.</p>

<h3>Strong body, weak offer</h3>
<p>Reader is convinced the problem is real and the solution works. Offer is too generic, too expensive without stack, or poorly presented. Convinced prospects don't buy bad offers.</p>

<h3>Strong offer, weak CTA</h3>
<p>Reader wants to buy. The CTA is ambiguous or multi-step. "Fill out our contact form" when the prospect is ready to pay. Mismatch between prospect readiness and next action.</p>

<h2>The order of operations</h2>
<p>When writing a new piece of copy:</p>
<ol>
  <li>Draft 10 headlines (see <a href="headlines.html">headlines</a>)</li>
  <li>Write the lead under the best 2–3 headlines</li>
  <li>Outline body: what proof, what mechanism, what case studies</li>
  <li>Write 20 bullets (you'll use 10–15)</li>
  <li>Write the offer stack (see <a href="../offer/grand-slam.html">grand slam offers</a>)</li>
  <li>Write the CTA</li>
  <li>Write the P.S.</li>
  <li>Read the whole thing aloud. Cut anything that makes you cringe.</li>
  <li>Show to someone who fits the ICP. Listen to their reactions.</li>
  <li>Revise. Ship.</li>
</ol>

<p style="margin-top:40px;">Related: <a href="headlines.html">Headlines</a> · <a href="the-lead.html">The lead</a> · <a href="body-copy.html">Body copy</a> · <a href="formulas.html">AIDA, PAS, PASTOR</a></p>
""",
    prev=("Urgency + scarcity", "../offer/urgency-scarcity.html"),
    nxt=("Headlines", "headlines.html"),
)


write_drm_page(
    slug="copy/headlines",
    title="Headlines",
    description="The headline is 80% of the battle. If you've read Halbert, Hopkins, or Caples, you know that. Here's how headlines actually work — and the patterns that keep winning 100 years later.",
    reading_time=8,
    body_html="""
<p class="lede">Gary Halbert: <em>"When you've written your headline, you've spent 80% of your wad."</em> John Caples (author of <em>Tested Advertising Methods</em>): changing a headline alone can increase response by 19x. Hopkins tested headlines against each other systematically starting in 1910. Every master of direct response has said the same thing: the headline is the ad. Everything else supports it.</p>

<h2>Why the headline does the work</h2>
<p>Prospects don't read ads. They scan. The headline is the gate: if it earns attention, they read. If it doesn't, they're gone. On any platform — newspaper, email subject line, YouTube thumbnail, Facebook ad, landing page — the same physics apply. Attention is the scarce resource; the headline is the currency.</p>

<h2>The headline's four jobs</h2>
<ol>
  <li><strong>Get attention.</strong> Stop the scroll or the scan.</li>
  <li><strong>Select the audience.</strong> Qualify — signal who this is for.</li>
  <li><strong>Deliver a big benefit.</strong> Name the value.</li>
  <li><strong>Pull them into the body.</strong> Make the next sentence feel necessary.</li>
</ol>
<p>A headline that does 3 of 4 can win. One that does 0 of 4 can't.</p>

<h2>The proven headline patterns</h2>

<h3>How to [desired outcome] without [feared cost]</h3>
<p>"How to lose 30 pounds without giving up bread." "How to hit quota without cold calling." Extraordinarily durable. Works because it names the outcome and removes the #1 objection simultaneously.</p>

<h3>The [number] [thing] that [result]</h3>
<p>"The 7 email subject lines that 10x our open rate." "The 3 questions that close 80% of our sales calls." Number = specific, scannable; result = benefit. Caples' test data showed number-led headlines consistently outperform.</p>

<h3>Warning / Announcing / Finally / Introducing</h3>
<p>"Warning: if you're on [common platform], read this before [common action]." "Announcing: the first [new thing]." "Finally: a [solution] that [does thing]." Attention-grabbers that work in the hands of experienced writers. Require substance to back up.</p>

<h3>Who else wants [benefit]?</h3>
<p>Caples' original. "Who else wants a whiter smile?" The "who else" presupposes others already want it, signaling social proof. Feels dated in 2026 but still tests well in select markets.</p>

<h3>They laughed when I sat down at the piano…</h3>
<p>Caples' most famous headline. Story-driven. A pattern interrupt. Promises a narrative the reader can't resist finishing. The modern version: any headline that opens a loop.</p>

<h3>If you [specific situation], [specific promise]</h3>
<p>"If you run paid ads on Meta and spend over $5K/month, here's an algorithm change costing you 20% right now." Hyper-qualifies the audience. Irrelevant to most; unmissable to the right few.</p>

<h3>[Unbelievable claim] — here's why</h3>
<p>"We cut our customer acquisition cost by 72%. Here's the one change." Curiosity + proof implied. Works at <a href="../market/sophistication.html">stage 3–4 markets</a>.</p>

<h3>The [expert] reveals [secret]</h3>
<p>"A former FBI negotiator reveals the 3 phrases that end any argument." Authority + curiosity. Works when the expert is credible and the secret is specific.</p>

<h2>The headline test — specificity</h2>
<p>For each headline, ask: could a competitor say this? If yes, it's too generic.</p>
<ul>
  <li>"Grow your business" — any competitor could say this</li>
  <li>"Grow your service business to $1M ARR in 18 months" — far fewer can</li>
  <li>"Grow your plumbing business from $400K to $1.5M in 14 months without adding trucks" — almost nobody</li>
</ul>
<p>The more specific, the more believable, the more it screams "this is for me" to the right person.</p>

<h2>Halbert's headline rules</h2>

<h3>1. News</h3>
<p>New things get attention. If your product genuinely has a new angle, lead with the news. "Announcing…" "Finally…" "New…" — but only when true.</p>

<h3>2. Benefit</h3>
<p>A direct promise of what the reader will get. Specific, concrete, and tied to a desire they already have.</p>

<h3>3. Curiosity</h3>
<p>An open loop that can only be closed by reading on. But — curiosity without relevance is clickbait and dies fast.</p>

<h3>4. Quickness / easiness</h3>
<p>How fast, how easy, how little effort. "In 5 minutes." "Without lifting a finger." "Automatically." Connects directly to the <a href="../offer/value-equation.html">value equation's</a> denominator.</p>

<h2>The headline writing process</h2>
<ol>
  <li>Write 20. Not one, not three — 20.</li>
  <li>Use different patterns: how-to, numbered list, story, warning, "if you…"</li>
  <li>For each, ask: does this pass the specificity test?</li>
  <li>Read them all aloud. Which ones make you want to read the next sentence?</li>
  <li>Pick the top 3.</li>
  <li>Test them against each other if you can.</li>
</ol>

<h2>Writing headlines for different channels</h2>

<h3>Email subject lines</h3>
<p>30–50 characters. Lowercase often feels more personal than title case. Specific ("Your Q3 numbers came in") > generic ("Q3 results"). Question format often works in B2B.</p>

<h3>Facebook / Instagram ads</h3>
<p>Headline pairs with image. The text and image must work together — one without the other is a broken ad. Use benefit-first, with qualifier.</p>

<h3>YouTube thumbnails / titles</h3>
<p>Titles are headlines for thumbnails. Clarity beats cleverness. Avoid clickbait — algorithms punish high-bounce content.</p>

<h3>Landing pages</h3>
<p>Usually a bigger, bolder headline plus a subhead that elaborates. Don't be clever — be clear.</p>

<h3>Sales letters / VSLs</h3>
<p>Longest headlines of any format — often 2-3 lines. Kennedy and Halbert wrote sales-letter headlines that were 30+ words because the reader has committed to the page and will tolerate more copy.</p>

<h2>Headline anti-patterns</h2>
<ul>
  <li><strong>Cute wordplay.</strong> "Mortgage? More-gage!" Kill it.</li>
  <li><strong>Pure brand mention.</strong> "Introducing FlowPilot v2." Means nothing to a new reader.</li>
  <li><strong>Vague benefit.</strong> "Elevate your business." Elevate is a word people use when they don't know what they're selling.</li>
  <li><strong>Clickbait without payoff.</strong> "You won't believe what happened next." Prospects now distrust this pattern on sight.</li>
  <li><strong>Too long, with no structure.</strong> Long is fine, but must be readable in one pass.</li>
</ul>

<h2>The best headline is boring if the market is sophisticated</h2>
<p>At <a href="../market/sophistication.html">stage 5 markets</a>, clever headlines look desperate. The winning move is often quieter: identification, tribal language, understatement. "For operators who've already tried the usual [tactics]." Let the headline qualify hard and the body do the selling.</p>

<p style="margin-top:40px;">Related: <a href="the-stack.html">The copywriting stack</a> · <a href="the-lead.html">The lead</a> · <a href="formulas.html">AIDA, PAS, PASTOR</a></p>
""",
    prev=("The copywriting stack", "the-stack.html"),
    nxt=("The lead (first 100 words)", "the-lead.html"),
)


write_drm_page(
    slug="copy/the-lead",
    title="The lead (first 100 words)",
    description="The headline earned the click. The lead earns the next five minutes. Lose the lead and no amount of body copy saves you — the prospect is already gone.",
    reading_time=6,
    body_html="""
<p class="lede">The headline earned the click. The lead — the first 100 words — earns the next five minutes. Lose the lead and no amount of body copy saves you. Every master copywriter talks about the lead as the second-most-important section after the headline, and Halbert explicitly said the first sentence's only job is to make the reader read the second sentence.</p>

<h2>What the lead must do</h2>
<ol>
  <li><strong>Deliver on the headline.</strong> If the headline promised a benefit, the lead starts delivering it.</li>
  <li><strong>Build connection.</strong> The reader recognizes themselves in the first lines.</li>
  <li><strong>Create momentum.</strong> Each sentence pulls into the next. Short, clear, declarative.</li>
  <li><strong>Establish trust.</strong> The lead is where skepticism peaks. A specific claim, a specific detail, or a concrete story lowers it.</li>
</ol>

<h2>The six lead types</h2>
<p>Mark Ford (a.k.a. Michael Masterson) codified the main lead types used in direct response. These have proven durable across a century of copy:</p>

<h3>1. Offer lead</h3>
<p>Open with the offer itself. "For $97, you can get the complete [thing]." Works when the prospect is already <a href="../market/awareness-stages.html">stage 5 — most aware</a>. Minimal persuasion, just information.</p>

<h3>2. Promise lead</h3>
<p>Open with the big benefit restated. "You're about to learn exactly how to [outcome]." Direct, simple. Works in stage 1–2 markets.</p>

<h3>3. Problem-solution lead</h3>
<p>Open with the problem the reader feels. "You've been told that [common belief]. It's wrong, and here's why." Works in most markets. Sets up a mechanism reveal later.</p>

<h3>4. Story lead</h3>
<p>Open with a scene. Specific character, specific moment. "At 11pm on a Tuesday, Sarah was staring at her dashboard…" Works when the story directly mirrors the reader's situation. Halbert used this constantly.</p>

<h3>5. Secret / curiosity lead</h3>
<p>Open with an intriguing claim or fact that demands explanation. "There's a specific 3-minute sequence that the top 1% of sales reps run. Most managers never teach it — most reps never discover it."</p>

<h3>6. Proclamation / news lead</h3>
<p>Announce something. "As of January 2026, the rules of paid acquisition on [platform] have changed — here's what it means for your business." Works when there's genuinely news.</p>

<h2>The "you" lead</h2>
<p>A rule across all lead types: lead with "you." The word "you" in sentence 1 pulls the reader in; "I" or "we" pushes them away. Most first-time copywriters write leads about themselves. Rewrite every self-referential sentence until "you" is the subject.</p>
<ul>
  <li>Weak: "We've helped 500 companies grow their pipelines."</li>
  <li>Strong: "If you've tried 3+ tactics to grow your pipeline and nothing stuck, you're not alone — 500 of our clients started in exactly that spot."</li>
</ul>

<h2>Lead structure — the 100-word budget</h2>
<p>Break the first 100 words into chunks:</p>
<ul>
  <li><strong>Words 1–20</strong> — the hook. A concrete scene, a specific claim, a problem-naming sentence.</li>
  <li><strong>Words 21–60</strong> — the setup. Why the hook matters, what the reader is feeling, what's at stake.</li>
  <li><strong>Words 61–100</strong> — the bridge. The transition into the body — a promise of what's coming next.</li>
</ul>
<p>This isn't a rigid template; it's a rhythm. Read winning direct-response copy and you'll see this shape repeatedly.</p>

<h2>The opening sentence's burden</h2>
<p>Halbert's test: <em>"The only job of the first sentence is to make you read the second sentence. The only job of the second sentence is to make you read the third."</em> Apply this literally. Audit your opening sentence — does it actually make the reader want the next one?</p>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Weak opening:</strong><br>
"Running a business is hard. There are many challenges."<br><br>
<strong>Strong opening:</strong><br>
"At 2:14am last Tuesday, Kevin's phone buzzed. Another refund request — the seventh this week."
</blockquote>

<h2>Lead patterns that work in 2026</h2>

<h3>Specificity and sensory detail</h3>
<p>Specific time, specific place, specific feeling. "Your CRM dashboard at 5pm on a Friday" beats "the end of a long week." Modern readers have seen every cliché. Specificity breaks through.</p>

<h3>The admission</h3>
<p>Admit something unexpected up front. "Most of what you've been told about [thing] is wrong — and I've been part of telling you." The unexpected candor earns trust.</p>

<h3>The unconventional claim</h3>
<p>State something that contradicts the market's default belief. "The best sales reps I've ever hired didn't go to college. Here's the pattern." Contrarian + specific.</p>

<h3>The direct question</h3>
<p>Ask a question the reader must answer in their head. "When's the last time you measured your customer acquisition cost — not blended, but by channel?" Engages the reader's mind in a way a statement doesn't.</p>

<h2>What to avoid in the lead</h2>
<ul>
  <li><strong>Setup paragraphs.</strong> "In today's fast-paced world…" Cut. The lead doesn't have room for warm-up.</li>
  <li><strong>Generic statements.</strong> "Marketing is important." The reader knows. Move on.</li>
  <li><strong>Autobiography before relevance.</strong> The reader doesn't care who you are yet. Make them care, then introduce yourself.</li>
  <li><strong>Too much context.</strong> Don't explain the entire market before the first benefit lands.</li>
</ul>

<h2>Rewriting a weak lead</h2>
<ol>
  <li>Cut the first paragraph. Seriously. 80% of the time your lead starts in paragraph 2.</li>
  <li>Put the reader's pain or situation in sentence 1.</li>
  <li>Use "you" before "I" or "we."</li>
  <li>Add one specific detail — a number, a moment, a scene.</li>
  <li>Read aloud. If you'd skim past it as a reader, rewrite again.</li>
</ol>

<p style="margin-top:40px;">Related: <a href="headlines.html">Headlines</a> · <a href="body-copy.html">Body copy</a> · <a href="formulas.html">AIDA, PAS, PASTOR</a> · <a href="../letters/story-selling.html">Story selling</a></p>
""",
    prev=("Headlines", "headlines.html"),
    nxt=("Body copy", "body-copy.html"),
)


write_drm_page(
    slug="copy/body-copy",
    title="Body copy",
    description="The body of a piece is where conversion is won or lost. Strong body copy doesn't describe — it builds belief, proves claims, and walks the reader from interest to wanting to buy.",
    reading_time=7,
    body_html="""
<p class="lede">The headline got the click. The lead earned the first minute. Body copy is where the sale is actually made — where belief gets built, objections get neutralized, and the reader moves from "this is interesting" to "I need this." Strong body copy doesn't describe. It proves.</p>

<h2>The job of body copy</h2>
<ul>
  <li><strong>Build belief.</strong> Turn "that sounds good" into "that's true, and here's why."</li>
  <li><strong>Neutralize objections.</strong> Anticipate and dissolve every reason the prospect might not buy.</li>
  <li><strong>Reveal the mechanism.</strong> Explain <em>why</em> the solution works, not just that it does.</li>
  <li><strong>Pace the emotional build.</strong> Move from problem → tension → possibility → solution → certainty.</li>
  <li><strong>Position the offer.</strong> Set up the price reveal with accumulated value.</li>
</ul>

<h2>The structure</h2>

<h3>1. Agitate the problem</h3>
<p>Make the reader feel the pain they already have. Not describe it clinically — feel it. Specific moments. Sensory details. Consequences of not solving it. <a href="formulas.html">PAS</a> (Problem-Agitate-Solution) is built on this.</p>

<h3>2. Introduce the tension</h3>
<p>The prospect knows they have a problem. Why haven't they solved it? Because the solutions they've tried don't work, or feel too hard, or didn't produce results. Name this. Validate it. Let the reader feel seen.</p>

<h3>3. Reveal the mechanism</h3>
<p>Here's the new mechanism, the insight, the approach. This is where the copy earns trust — by explaining <em>why</em> this solution is different. Not just "ours is better" but "the reason others fail is X; our approach addresses X specifically by doing Y."</p>

<h3>4. Proof</h3>
<p>Case studies, data, testimonials, demonstrations. Every claim is backed. Every number is sourced. Every testimonial has a name, title, and concrete outcome.</p>

<h3>5. Benefits stack</h3>
<p>Specific, scannable, benefit-driven bullets. See <a href="bullets.html">fascination bullets</a>.</p>

<h3>6. Objection handling</h3>
<p>Preemptively address: "what about X?" "what if Y?" "how is this different from Z?" Don't wait for objections to happen — embed them in the copy and resolve them.</p>

<h3>7. Offer stack + close</h3>
<p>The offer, the bonuses, the guarantee, the price, the deadline. See <a href="../offer/grand-slam.html">grand slam offers</a>.</p>

<h2>Benefits, not features</h2>
<p>Every feature statement has a benefit that follows from it. The feature-benefit chain:</p>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Feature:</strong> "Automatic transcription."<br>
<strong>Benefit:</strong> "So you don't lose the insights in meetings you can't attend."<br>
<strong>Outcome:</strong> "So you make better decisions without needing to be in every room."
</blockquote>
<p>A feature alone is inert. A feature + benefit is useful. A feature + benefit + outcome is persuasive.</p>

<h2>Reason-why copy</h2>
<p>Claude Hopkins' foundational principle. Every claim has a because. "The best wood for framing" is weak. "The best wood for framing because its fiber structure resists warping up to 40% better than pine, tested by X lab" is strong.</p>

<p>Writing reason-why copy:</p>
<ol>
  <li>Make a claim</li>
  <li>Immediately follow with "because…"</li>
  <li>Cite a specific mechanism, study, or track record</li>
</ol>

<h2>The mechanism reveal</h2>
<p>Halbert and Kennedy both taught this explicitly: at some point in the body, you <em>explain</em> why your thing works. This is where sophisticated readers lean in. They've seen claims. They haven't seen mechanisms. A clear, specific mechanism — even one they can't fully verify — dramatically raises belief.</p>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Without mechanism:</strong><br>
"Our software grows your business."<br><br>
<strong>With mechanism:</strong><br>
"Our software identifies the 12% of customers who are about to cancel — 60 days before they do — based on 40 usage signals. That early warning is what lets our customers save 73% of at-risk accounts vs the 31% industry average."
</blockquote>

<h2>Proof — the specific kinds</h2>

<h3>Case studies</h3>
<p>Before/after with a name, a number, a timeframe. "Kevin's HVAC business went from $400K to $1.3M in 11 months." Specific > impressive-but-vague.</p>

<h3>Testimonials</h3>
<p>Real names, real titles, real companies where possible. A testimonial without a name is essentially anonymous.</p>

<h3>Data</h3>
<p>Numbers you've measured. Conversion rates, time savings, revenue gains. Source the number if possible.</p>

<h3>Demonstrations</h3>
<p>Screenshots, video walkthroughs, live product footage. A 30-second product video often outperforms 500 words of description.</p>

<h3>Social proof counts</h3>
<p>"Used by 5,400 teams." "Processed $4.2B in transactions." "140,000 hours saved." Numbers that communicate scale.</p>

<h2>Writing for the skim</h2>
<p>Most readers skim before they read. Design for both:</p>
<ul>
  <li>Every paragraph is 1–3 sentences</li>
  <li>Bold key phrases so the skim still delivers the message</li>
  <li>Use subheads every 150–300 words</li>
  <li>Use bullets for lists of benefits</li>
  <li>Use callout boxes for key claims and testimonials</li>
  <li>Use images (screenshots, product shots, faces) at key points</li>
</ul>

<h2>The voice</h2>
<p>Write like one person talking to one other person. Contractions. Direct. Conversational. Second person ("you") dominant. Avoid corporate voice, passive constructions, and the word "utilize."</p>
<ul>
  <li>Weak: "The product can be utilized to optimize team workflows."</li>
  <li>Strong: "You use this to fix the thing that's been eating your Mondays."</li>
</ul>

<h2>Length — how long is long enough?</h2>
<p>Long enough to close the sale. Not a word longer. For cheap impulse purchases, a few paragraphs. For high-consideration purchases, long-form copy still wins in 2026 — often 3,000+ words on a sales page, or 20+ minute VSLs.</p>
<p>Long copy works because qualified buyers consume it. The unqualified skim past. The qualified read deeply and buy. Length isn't a writer's self-indulgence — it's a filter.</p>

<h2>Rewriting body copy</h2>
<ol>
  <li>Read it aloud. Every sentence that makes you cringe — cut or rewrite.</li>
  <li>Look for claims with no because. Add the because.</li>
  <li>Look for features with no benefit. Add the benefit.</li>
  <li>Look for "we" and "us" — convert to "you" wherever possible.</li>
  <li>Look for paragraphs longer than 3 sentences — break them.</li>
  <li>Look for abstract nouns — "solutions," "experience," "journey" — replace with concrete language.</li>
  <li>Have someone who fits the ICP read it. Watch where they skim, where they slow down, where they leave.</li>
</ol>

<p style="margin-top:40px;">Related: <a href="the-stack.html">The copywriting stack</a> · <a href="the-lead.html">The lead</a> · <a href="bullets.html">Fascination bullets</a> · <a href="formulas.html">AIDA, PAS, PASTOR</a></p>
""",
    prev=("The lead (first 100 words)", "the-lead.html"),
    nxt=("Calls to action", "ctas.html"),
)


write_drm_page(
    slug="copy/ctas",
    title="Calls to action",
    description="The CTA is where all the persuasion converts into action or evaporates. A great CTA tells the reader exactly what to do, removes every friction, and justifies the click.",
    reading_time=5,
    body_html="""
<p class="lede">The CTA is where persuasion converts into action — or evaporates. After hundreds of dollars of ad spend, hours of copy, and a reader's time, the CTA is the moment the reader decides whether they move forward or close the tab. Bad CTAs leak revenue; great ones unlock it.</p>

<h2>What a great CTA does</h2>
<ol>
  <li><strong>Tells the reader exactly what to do.</strong> Not "learn more." Specific next action, in specific words.</li>
  <li><strong>Frames the next step as low-friction.</strong> "Book a 15-minute call" feels smaller than "schedule a consultation."</li>
  <li><strong>Reaffirms the benefit.</strong> The button label says what the reader gets, not what the button does.</li>
  <li><strong>Removes risk or hesitation.</strong> Reminds them of the guarantee or the low commitment.</li>
  <li><strong>Appears at every decision point.</strong> Not just at the end. Throughout the page.</li>
</ol>

<h2>Button text — what to say</h2>
<p>The button label should describe what the reader gets on the other side, not the mechanic of the click.</p>
<table style="width:100%; border-collapse:collapse; margin:20px 0;">
  <tr style="background:#f5f5f7;"><th style="padding:10px; text-align:left; border:1px solid #e5e5ea;">Weak</th><th style="padding:10px; text-align:left; border:1px solid #e5e5ea;">Stronger</th></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Submit</td><td style="padding:10px; border:1px solid #e5e5ea;">Send me the playbook</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Buy now</td><td style="padding:10px; border:1px solid #e5e5ea;">Claim my 90-day trial</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Learn more</td><td style="padding:10px; border:1px solid #e5e5ea;">Show me how it works</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Sign up</td><td style="padding:10px; border:1px solid #e5e5ea;">Start my free account</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Contact us</td><td style="padding:10px; border:1px solid #e5e5ea;">Book my 15-min strategy call</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Download</td><td style="padding:10px; border:1px solid #e5e5ea;">Send me the 37-page guide</td></tr>
</table>

<h2>The "I" frame</h2>
<p>First-person button text ("Start my free trial" vs. "Start your free trial") has tested better in many studies. The reader mentally claims the action as their own. Not a silver bullet, but a default worth testing.</p>

<h2>The micro-commitment ladder</h2>
<p>Every CTA asks for a commitment. Size the ask to where the reader is on the journey:</p>
<ul>
  <li><strong>Cold — unaware / problem-aware:</strong> low-commitment asks. "Watch the 2-minute video." "Read the article."</li>
  <li><strong>Warm — solution-aware:</strong> medium commitment. "Download the checklist." "Take the quiz."</li>
  <li><strong>Hot — product-aware / ready:</strong> high commitment. "Book a call." "Start your free trial." "Buy."</li>
</ul>
<p>Asking a cold reader to book a call fails. Asking a hot reader to watch a video fails differently — they want to buy, and you're slowing them down.</p>

<h2>Placement</h2>

<h3>Above the fold</h3>
<p>A CTA visible without scrolling. The reader who's already sold doesn't need to read the page.</p>

<h3>After major sections</h3>
<p>Every 500–1000 words of body copy, another CTA. The reader who's convinced mid-page shouldn't have to hunt for the button.</p>

<h3>At the close</h3>
<p>After the offer + guarantee. The primary close.</p>

<h3>In the P.S.</h3>
<p>One more CTA, often with urgency. "P.S. — the cohort closes Friday. If you're even 80% sure, book your call today. [button]"</p>

<h3>Sticky / repeated</h3>
<p>On long pages, a sticky header or side bar with a CTA that scrolls with the reader.</p>

<h2>What to put around the button</h2>
<ul>
  <li><strong>Subtext</strong> below the button that reduces friction. "No credit card required." "30-day free trial." "Cancel anytime."</li>
  <li><strong>Social proof</strong> near the CTA. "Joined by 4,200+ operators this year."</li>
  <li><strong>Guarantee echo</strong> next to the button. "Backed by our 90-day money-back guarantee."</li>
  <li><strong>Urgency reminder</strong>. "Offer closes Friday at 5pm EST."</li>
</ul>

<h2>The second-choice offer</h2>
<p>Next to the primary CTA, offer a lower-friction alternative:</p>
<ul>
  <li>Primary: "Start my free trial"</li>
  <li>Secondary: "Not ready? Read the case studies"</li>
</ul>
<p>Catches the reader who isn't quite ready. Don't put two equivalent CTAs — that splits attention. Put one clearly dominant CTA and one clearly secondary.</p>

<h2>Form friction</h2>
<p>Every field on the form drops conversion. Typical drop:</p>
<ul>
  <li>Email only: baseline</li>
  <li>Email + name: -10 to -20%</li>
  <li>Email + name + phone: another -20 to -40%</li>
  <li>Email + name + phone + company + title: brutal</li>
</ul>
<p>Only ask for what you need <em>to take the next step</em>. A sales call booking needs more than a content download. Size the form to the ask.</p>

<h2>Button design</h2>
<ul>
  <li>High contrast with the page background. The button must be findable in 2 seconds.</li>
  <li>Size — large enough to tap on mobile (minimum 44x44px).</li>
  <li>One primary button per view. Two primaries = no primary.</li>
  <li>Arrow or icon helps slightly. Not required.</li>
  <li>Color — the "red button converts best" myth is mostly myth. What matters is contrast, not color.</li>
</ul>

<h2>Common CTA failures</h2>
<ul>
  <li><strong>Too generic.</strong> "Submit," "Click here." Dead on arrival.</li>
  <li><strong>Too many.</strong> Five different CTAs above the fold. Reader picks none.</li>
  <li><strong>Mismatched.</strong> "Book a demo" on a page selling a $29 product. Too heavy an ask.</li>
  <li><strong>Hidden.</strong> CTA buried in text, not visually distinct.</li>
  <li><strong>No subtext.</strong> Button alone without risk-reversal or friction-removal language nearby.</li>
</ul>

<p style="margin-top:40px;">Related: <a href="body-copy.html">Body copy</a> · <a href="../offer/grand-slam.html">Grand slam offers</a> · <a href="../foundations/ten-rules.html">Kennedy's 10 rules</a></p>
""",
    prev=("Body copy", "body-copy.html"),
    nxt=("AIDA, PAS, PASTOR", "formulas.html"),
)


write_drm_page(
    slug="copy/formulas",
    title="AIDA, PAS, PASTOR",
    description="The three copywriting formulas that cover 95% of direct response. Each has a specific use case. Knowing when to use which one — and when to break the template — is most of the skill.",
    reading_time=7,
    body_html="""
<p class="lede">Copywriting formulas aren't templates you fill in. They're scaffolds that organize persuasion into a sequence the reader can follow. The three most useful — AIDA, PAS, and PASTOR — cover 95% of direct response situations. Learn all three; use each where it fits.</p>

<h2>AIDA — Attention, Interest, Desire, Action</h2>
<p>The oldest copywriting formula, usually credited to Elias St. Elmo Lewis (1898). A classic for a reason.</p>

<ol>
  <li><strong>Attention.</strong> Get the reader to stop. Headline and opening lines.</li>
  <li><strong>Interest.</strong> Keep them. Show relevance to their situation. Hint at the benefit.</li>
  <li><strong>Desire.</strong> Make them want it. Build the case — benefits, proof, mechanism.</li>
  <li><strong>Action.</strong> Tell them exactly what to do next.</li>
</ol>

<h3>When to use AIDA</h3>
<ul>
  <li>Short-form direct response (landing pages, single ads)</li>
  <li>Cold audiences who need to be hooked and pulled through quickly</li>
  <li>Impulse or lower-consideration purchases</li>
</ul>

<h3>Example — B2B SaaS short-form landing page</h3>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>A — Attention:</strong> "The #1 reason your reps miss quota isn't what you think."<br>
<strong>I — Interest:</strong> "It's not leads. It's not tools. It's not motivation. It's the 14 minutes per day they spend on CRM hygiene — 67 hours a year, gone."<br>
<strong>D — Desire:</strong> "Our customers eliminated that time using a single automation. Their reps closed 31% more in Q3 than Q2 — same pipeline, same quota, 67 more hours of actual selling."<br>
<strong>A — Action:</strong> "Book a 15-minute demo. Walk through the automation. See if it fits your stack."
</blockquote>

<h2>PAS — Problem, Agitate, Solution</h2>
<p>Dan Kennedy's favorite. PAS goes deep on the problem before presenting the solution. The agitation creates the tension that the solution then releases.</p>

<ol>
  <li><strong>Problem.</strong> Name the problem the reader is experiencing. Concrete and specific.</li>
  <li><strong>Agitate.</strong> Make it worse — consequences, costs, emotional stakes. The reader feels the problem more vividly.</li>
  <li><strong>Solution.</strong> Present your solution as the release.</li>
</ol>

<h3>When to use PAS</h3>
<ul>
  <li>Markets where prospects haven't fully admitted the problem</li>
  <li>Services / offers where pain is the primary motivator</li>
  <li>Sales pages for categories with strong emotional stakes</li>
  <li>Email subject lines and cold outreach</li>
</ul>

<h3>Example — email to underperforming e-commerce operators</h3>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>P:</strong> "Your CAC went up 28% this year. You already know this. What you might not know — your top 3 SKUs now take 4 sessions to convert, not 2."<br><br>
<strong>A:</strong> "Each of those added sessions costs you another $0.82 in paid traffic, another hit to creative fatigue, another risk of the buyer discovering a cheaper competitor mid-consideration. Over the next 12 months, that compounds to six figures in lost margin — and your Q4 plan doesn't account for it."<br><br>
<strong>S:</strong> "The fix is a specific retention email sequence that caught 41% of those wandering buyers for our last 3 clients. We send it to you for free, no call required. Reply 'send' and it's in your inbox in 10 minutes."
</blockquote>

<h3>The agitation rule</h3>
<p>Don't just restate the problem louder. Agitation is about <em>consequences</em>. What happens if they don't fix it? What does Monday morning look like in 12 months? What do they feel at 11pm when the dashboard tells them the truth? Specificity in agitation is what separates PAS from whining.</p>

<h2>PASTOR — Problem, Amplify, Story, Transformation, Offer, Response</h2>
<p>Ray Edwards' expansion of PAS, designed for longer-form direct response — sales letters, VSLs, long emails.</p>

<ol>
  <li><strong>Problem.</strong> Same as PAS.</li>
  <li><strong>Amplify.</strong> Consequences of not solving.</li>
  <li><strong>Story / Solution.</strong> Tell the story of how the solution came to be — often autobiographical. The story proves the solution is earned, not theoretical.</li>
  <li><strong>Transformation / Testimony.</strong> What changes for the reader? Real customer cases showing the transformation.</li>
  <li><strong>Offer.</strong> The full offer stack — core product, bonuses, guarantee, price.</li>
  <li><strong>Response.</strong> The CTA — specific action, deadline, next step.</li>
</ol>

<h3>When to use PASTOR</h3>
<ul>
  <li>Long-form sales letters</li>
  <li>VSLs (video sales letters)</li>
  <li>High-ticket offers where the reader needs the full story before buying</li>
  <li>Coaching, courses, services — categories where trust and transformation matter</li>
</ul>

<h3>Why the story matters</h3>
<p>The "S" in PASTOR is the difference between a mediocre long-form piece and a great one. Readers believe stories more than they believe claims. A specific founder's journey — "I was in your situation two years ago, here's what happened" — builds identification in a way proof alone can't.</p>

<h2>Which to use when</h2>
<table style="width:100%; border-collapse:collapse; margin:20px 0;">
  <tr style="background:#f5f5f7;"><th style="padding:10px; text-align:left; border:1px solid #e5e5ea;">Context</th><th style="padding:10px; text-align:left; border:1px solid #e5e5ea;">Best formula</th></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Short ad, impulse purchase</td><td style="padding:10px; border:1px solid #e5e5ea;">AIDA</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Cold outreach email</td><td style="padding:10px; border:1px solid #e5e5ea;">PAS</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Social ad → landing page</td><td style="padding:10px; border:1px solid #e5e5ea;">AIDA</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">B2B problem-aware email</td><td style="padding:10px; border:1px solid #e5e5ea;">PAS</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Long-form sales letter (3000+ words)</td><td style="padding:10px; border:1px solid #e5e5ea;">PASTOR</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">VSL (20+ minutes)</td><td style="padding:10px; border:1px solid #e5e5ea;">PASTOR</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Course / coaching launch sequence</td><td style="padding:10px; border:1px solid #e5e5ea;">PASTOR</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Retargeting ad to warm audience</td><td style="padding:10px; border:1px solid #e5e5ea;">AIDA (shortened)</td></tr>
</table>

<h2>When to break the formula</h2>
<p>Formulas are training wheels. Eventually you internalize the underlying structure — attention → interest → belief → action — and compose in whatever order fits the specific reader's journey. A/B testing will tell you whether you've earned the right to break the formula; if the numbers don't support it, go back to the scaffold.</p>

<h2>The formulas don't replace thinking</h2>
<p>A formula-filled piece of copy with a weak offer or a wrong market still fails. The formula organizes persuasion; it doesn't create persuasion out of nothing. If you're hitting a wall on the copy, the problem is usually upstream — offer, market, or dream customer — not the formula.</p>

<p style="margin-top:40px;">Related: <a href="the-stack.html">The copywriting stack</a> · <a href="headlines.html">Headlines</a> · <a href="bullets.html">Fascination bullets</a></p>
""",
    prev=("Calls to action", "ctas.html"),
    nxt=("Fascination bullets", "bullets.html"),
)


write_drm_page(
    slug="copy/bullets",
    title="Fascination bullets",
    description="Halbert's magic bullets — each one a punchy benefit claim, a tiny open loop, a specific promise. Mastering bullets is one of the highest-leverage skills in direct response.",
    reading_time=6,
    body_html="""
<p class="lede">Bullets are the scan layer of direct response. Prospects who'd never read a full sales letter will scan bullets. Gary Halbert called them "fascinations" — each one a tiny complete pitch, a punchy benefit claim with a hint of mystery. Most writers bullet badly. The ones who don't separate themselves from the pack immediately.</p>

<h2>What a fascination bullet does</h2>
<ul>
  <li>Names a specific benefit in the reader's language</li>
  <li>Opens a curiosity loop — you want to know more</li>
  <li>Is short, punchy, and readable in 3 seconds</li>
  <li>Can't be fully delivered by the bullet alone — you need the product to get the answer</li>
  <li>Implies specificity (numbers, named things, specific people)</li>
</ul>

<h2>The anatomy</h2>
<p>Most fascination bullets have three elements:</p>
<ol>
  <li><strong>Hook word</strong> — "How," "The," "Why," "What," "When"</li>
  <li><strong>Specific subject</strong> — a named thing, a specific person, a number, a moment</li>
  <li><strong>Implicit benefit or mystery</strong> — the payoff that makes you want the answer</li>
</ol>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
Weak: "Learn how to write better emails."<br>
Better: "How to write an email subject line."<br>
Strong: "The 7-word subject line that 3x'd our open rate (and why most marketers reject it as too plain)."<br>
Strongest: "Why our boring 7-word subject line beats every clever one — and the exact phrase we've used 140+ times."
</blockquote>

<h2>The patterns that always work</h2>

<h3>The Number-Lead</h3>
<p>"The 3 words that open every one of our cold emails."<br>
"7 ways to spot a burnout before the churn."<br>
"The 13-minute process that replaces your entire weekly pipeline review."</p>

<h3>The Counterintuitive</h3>
<p>"Why asking for more money (not less) raises your close rate."<br>
"The one thing every marketer is told to do — that you should stop doing today."</p>

<h3>The Warning</h3>
<p>"The #1 mistake operators make when firing their first VP of Sales."<br>
"Warning: this tactic is great… unless your team has more than 5 reps."</p>

<h3>The Name-Drop</h3>
<p>"The specific question Jobs asked engineering candidates that exposed the fakers in 30 seconds."<br>
"Why Halbert mailed his coat-of-arms letter in a plain white envelope — and what it teaches about cold outreach."</p>

<h3>The Specific Moment</h3>
<p>"What to say when a prospect says 'send me a proposal and I'll run it by my team.'"<br>
"How to handle the 4th email after a deal has gone silent."</p>

<h3>The Before / After</h3>
<p>"How Kevin went from 40 demos a month (closing 2) to 12 demos a month (closing 8)."</p>

<h3>The "Do / Don't" Split</h3>
<p>"What to say in a discovery call (and the 3 things to never say)."<br>
"The 2 things every landing page needs — and the 1 thing every landing page has that you should remove."</p>

<h2>Specificity — the make-or-break</h2>
<p>Vague bullets fail. Specific bullets work. Rewrite every generic bullet until it has a number, a name, or a concrete detail.</p>

<table style="width:100%; border-collapse:collapse; margin:20px 0;">
  <tr style="background:#f5f5f7;"><th style="padding:10px; text-align:left; border:1px solid #e5e5ea;">Vague</th><th style="padding:10px; text-align:left; border:1px solid #e5e5ea;">Specific</th></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">How to write better emails</td><td style="padding:10px; border:1px solid #e5e5ea;">The 8-word first sentence that determines whether the rest of your email gets read</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">How to close more deals</td><td style="padding:10px; border:1px solid #e5e5ea;">The one question to ask in minute 23 of a discovery call that doubles your close rate</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Improve your hiring</td><td style="padding:10px; border:1px solid #e5e5ea;">The 4-question reference check that exposed 38% of our "no-hire" candidates we were about to offer</td></tr>
</table>

<h2>How many bullets</h2>
<p>Different contexts, different counts:</p>
<ul>
  <li><strong>Landing page "benefits" section:</strong> 6–10</li>
  <li><strong>Long-form sales letter — "here's what you get" section:</strong> 20–40</li>
  <li><strong>Email body:</strong> 3–7</li>
  <li><strong>Ad creative (single image):</strong> 3–5</li>
  <li><strong>Course / info product page:</strong> 30–60 (one of the highest-conversion elements — readers scan the list and keep finding bullets that hook them)</li>
</ul>

<h2>The bullet-writing process</h2>
<ol>
  <li>List every specific benefit, feature, chapter, insight, or moment in the product</li>
  <li>For each, ask: "what's the one thing about this that would make a reader in the ICP want to know more?"</li>
  <li>Write the bullet in the style of a tiny pitch — hook, subject, implied mystery</li>
  <li>Cut any bullet that's vague or repeats another</li>
  <li>Reorder: strongest 3 at the top, strongest 3 at the bottom, the rest in between</li>
  <li>Read the list aloud. Each one should make you curious.</li>
</ol>

<h2>The "bad bullet" detector</h2>
<p>A bullet fails if:</p>
<ul>
  <li>It could appear on a competitor's page unchanged</li>
  <li>It has no number or specific detail</li>
  <li>It restates a feature without the benefit</li>
  <li>It reveals everything — the reader doesn't need to open the product to get it</li>
  <li>It's longer than 20 words</li>
</ul>

<h2>Where Halbert's bullets went</h2>
<p>Halbert used bullets in everything — newsletter subscription pitches, coat-of-arms letters, copywriter training programs. His bullets were often long lists — 30–50 at a time — each carrying its own weight. A reader could fail to be convinced by any single bullet but still be pulled forward by the sheer density of specificity. That's the structural power of the bullet list.</p>

<p style="margin-top:40px;">Related: <a href="the-stack.html">The copywriting stack</a> · <a href="body-copy.html">Body copy</a> · <a href="headlines.html">Headlines</a></p>
""",
    prev=("AIDA, PAS, PASTOR", "formulas.html"),
    nxt=("The core four", "../leads/core-four.html"),
)

print("\n✓ Offer + Copywriting (13 pages)")
