#!/usr/bin/env python3
"""Direct Response - Foundations + Market (10 pages)."""
from _build_drm import write_drm_page, DRM_SIDEBAR

# ============================================================
# HUB
# ============================================================

hub_body = """
<p class="lede">Direct response is the discipline of advertising that demands a measurable response from a specific person. No brand awareness campaigns. No "impressions." Every dollar out has a dollar in, traceable to the ad, the audience, and the offer. This section is a working operator's reference to the discipline as taught by its four most important teachers: <strong>Claude Hopkins</strong>, <strong>Dan Kennedy</strong>, <strong>Gary Halbert</strong>, and <strong>Alex Hormozi</strong>.</p>

<p>Almost every modern marketing practice - from Facebook ads to email sequences to $2,000 info products - traces back to their work. Most modern marketers have only absorbed it secondhand. The goal of this section is to go straight to the source material and rebuild it from first principles, with a 2026 operator's lens.</p>

<h2>The nine sections</h2>

<div class="cards" style="margin-top:32px;">

  <a href="foundations/what-is-direct-response.html" class="card">
    <h3>Foundations</h3>
    <p>What direct response actually is, the legacy of the four horsemen, Hopkins' scientific advertising, Kennedy's ten rules.</p>
  </a>

  <a href="market/starving-crowd.html" class="card">
    <h3>The Market</h3>
    <p>Starving crowd, sophistication levels, awareness stages, dream customer, market selection.</p>
  </a>

  <a href="offer/value-equation.html" class="card">
    <h3>The Offer</h3>
    <p>Hormozi's value equation, grand slam offers, bonuses that stack, guarantees, pricing, urgency + scarcity.</p>
  </a>

  <a href="copy/the-stack.html" class="card">
    <h3>Copywriting</h3>
    <p>Headlines, the lead, body copy, CTAs, AIDA/PAS/PASTOR, fascination bullets.</p>
  </a>

  <a href="leads/core-four.html" class="card">
    <h3>Lead Generation</h3>
    <p>The core four, lead magnets, warm outreach, cold outreach, paid ads.</p>
  </a>

  <a href="letters/structure.html" class="card">
    <h3>Sales Letters + VSLs</h3>
    <p>The classical sales letter structure, long vs short form, VSL pacing, story selling, Halbert letters.</p>
  </a>

  <a href="followup/direct-mail.html" class="card">
    <h3>Follow-up + Retention</h3>
    <p>Direct mail that still works, email sequences, soap opera sequence, customer indoctrination.</p>
  </a>

  <a href="testing/scientific.html" class="card">
    <h3>Testing</h3>
    <p>Hopkins' scientific method, what to test, controls + challengers, measurement.</p>
  </a>

  <a href="scaling/scale-winners.html" class="card">
    <h3>Scaling</h3>
    <p>Scaling what works, the value ladder, high ticket, info products.</p>
  </a>

</div>

<h2 style="margin-top:56px;">How to read this</h2>
<p>Start at <a href="foundations/what-is-direct-response.html">Foundations</a> if you're new. If you already run campaigns, jump straight to <a href="offer/value-equation.html">The Offer</a> - a better offer beats better copy every time, and most campaigns fail there, not in the creative. Everything else multiplies whatever your offer can produce.</p>
"""

write_drm_page(
    slug="index",
    title="Direct Response Marketing",
    description="A 45-page reference to direct response as taught by Claude Hopkins, Dan Kennedy, Gary Halbert, and Alex Hormozi - offers, copy, leads, funnels, testing, and scale.",
    reading_time=3,
    body_html=hub_body,
    prev=None,
    nxt=("What is direct response?", "foundations/what-is-direct-response.html"),
)


# ============================================================
# FOUNDATIONS (4 pages + hub)
# ============================================================

write_drm_page(
    slug="foundations/what-is-direct-response",
    title="What is direct response?",
    description="Direct response is advertising that demands a measurable response from a specific person. Here's what separates it from brand advertising - and why almost every profitable marketing campaign since 1900 has been direct response.",
    reading_time=6,
    body_html="""
<p class="lede">Direct response is advertising that demands a measurable response from a specific person. Every ad contains an offer. Every offer has a deadline. Every response is traceable. Every dollar out maps to a dollar in. It's the opposite of brand advertising, where you spend money hoping it does something vague to someone eventually.</p>

<h2>The definition, tightened</h2>
<p>Dan Kennedy's working definition: a direct-response ad is one that asks the reader to <em>do something specific, right now, that can be measured</em>. Call this number. Fill this form. Send back this card. Click this button. If you can't measure the response, you can't improve the ad - and you can't know whether it worked.</p>

<h2>Direct response vs brand advertising</h2>
<table style="width:100%; border-collapse:collapse; margin:20px 0;">
  <tr style="background:#f5f5f7;"><th style="padding:12px; text-align:left; border:1px solid #e5e5ea;">Brand</th><th style="padding:12px; text-align:left; border:1px solid #e5e5ea;">Direct response</th></tr>
  <tr><td style="padding:12px; border:1px solid #e5e5ea;">Awareness, sentiment, impressions</td><td style="padding:12px; border:1px solid #e5e5ea;">Leads, sales, trackable outcomes</td></tr>
  <tr><td style="padding:12px; border:1px solid #e5e5ea;">Soft measurement (brand lift)</td><td style="padding:12px; border:1px solid #e5e5ea;">Hard measurement (revenue per ad)</td></tr>
  <tr><td style="padding:12px; border:1px solid #e5e5ea;">No specific call to action</td><td style="padding:12px; border:1px solid #e5e5ea;">Always an offer, always a deadline</td></tr>
  <tr><td style="padding:12px; border:1px solid #e5e5ea;">Budgeted on "share of voice"</td><td style="padding:12px; border:1px solid #e5e5ea;">Budgeted on ROI per dollar</td></tr>
  <tr><td style="padding:12px; border:1px solid #e5e5ea;">Longer copy = wasteful</td><td style="padding:12px; border:1px solid #e5e5ea;">Longer copy often = more profitable</td></tr>
  <tr><td style="padding:12px; border:1px solid #e5e5ea;">Agency-friendly</td><td style="padding:12px; border:1px solid #e5e5ea;">Results-friendly</td></tr>
</table>

<h2>Why direct response wins</h2>
<ul>
  <li><strong>It's measurable.</strong> You know exactly what made money. That knowledge compounds: every campaign teaches you what to do next.</li>
  <li><strong>It's testable.</strong> Hopkins' insight from 1923: scientific testing turns advertising from an art into a disciplined process. Each test narrows what works.</li>
  <li><strong>It's self-funding.</strong> Good direct response pays for itself. Brand advertising requires reserves; direct response generates them.</li>
  <li><strong>It compounds.</strong> A working direct-response campaign becomes an asset. You can scale it, clone it, vary it.</li>
</ul>

<h2>The hallmarks of a direct response ad</h2>
<ol>
  <li><strong>A specific offer.</strong> Not "check out our brand" - "get X for Y by Z date."</li>
  <li><strong>A reason to respond now.</strong> Deadline, limited quantity, bonus expiring.</li>
  <li><strong>Clear instructions.</strong> Call this number. Click this button. Fill this form.</li>
  <li><strong>Tracked response.</strong> Unique phone, unique URL, coupon code. If you can't track it, you can't improve it.</li>
  <li><strong>Strong copy.</strong> Every word earns its place. More on this in the <a href="../copy/the-stack.html">copywriting section</a>.</li>
  <li><strong>Accountability.</strong> The ad has a number next to it. Either it produced or it didn't.</li>
</ol>

<h2>Where direct response lives in 2026</h2>
<p>The surface areas have changed; the principles haven't. What used to be:</p>
<ul>
  <li>Full-page newspaper ads → Facebook / Google / TikTok ads</li>
  <li>Direct mail → Email, SMS, retargeting</li>
  <li>Radio spots → Podcast host-reads, YouTube pre-roll</li>
  <li>Sales letters → VSLs and landing pages</li>
  <li>Coupons → Promo codes + UTM tracking</li>
  <li>Free sample → Free trial, freemium, lead magnet</li>
</ul>
<p>The headlines Hopkins wrote in 1910 still work on Facebook today. The value equation Hormozi wrote in 2021 describes what Halbert was doing in sales letters in the 1980s. This is a 120-year-old discipline with a stable core.</p>

<h2>The myths that kill profitable advertising</h2>
<ul>
  <li><em>"Long copy doesn't work anymore."</em> Long copy works when people are qualified and considering a real purchase. Short copy works for impulse. Both are wrong answers to the opposite question.</li>
  <li><em>"Nobody reads ads."</em> Prospects don't read ads. Interested buyers read ads. Your job isn't to force readers; it's to attract the right ones.</li>
  <li><em>"Direct response looks cheap."</em> Direct response looks the way it does because it works. The ads that "look nice" usually underperform the ones that "look like mail-order junk" - and the tracking proves it every time.</li>
  <li><em>"You can't measure modern advertising anymore."</em> You can measure almost everything that matters. Attribution is harder than it was in 2015; it's still more measurable than the 20th-century baseline Hopkins tested against.</li>
</ul>

<p style="margin-top:40px;">Next: <a href="four-horsemen.html">The four horsemen</a> - who Hopkins, Kennedy, Halbert, and Hormozi are, and which parts of this discipline each one pushed forward.</p>
""",
    prev=("Overview", "../index.html"),
    nxt=("The four horsemen", "four-horsemen.html"),
)


write_drm_page(
    slug="foundations/four-horsemen",
    title="The four horsemen",
    description="Claude Hopkins, Dan Kennedy, Gary Halbert, and Alex Hormozi - the four people whose teaching contains about 90% of what you need to know about direct response.",
    reading_time=7,
    body_html="""
<p class="lede">Every useful idea in direct response was either discovered by one of these four or systematized by them. Learn what each one specifically contributed, and you can read the rest of the field - the Ogilvys, the Caples, the Schwartzes, the Brunsons, the Halligans - as commentary.</p>

<h2>Claude Hopkins (1866-1932)</h2>
<p><strong>The scientist.</strong> Hopkins wrote <em>Scientific Advertising</em> in 1923 - arguably the most influential marketing book ever written. David Ogilvy said "nobody should be allowed to have anything to do with advertising until they have read this book seven times." He's right.</p>

<p>Hopkins' core move: advertising as a measurable science, not art. He used <strong>keyed coupons</strong> - unique codes in each ad - to track exactly which newspaper, which headline, which offer produced sales. In an era where "advertising" meant random guessing, he was running controlled experiments.</p>

<p>His lasting contributions:</p>
<ul>
  <li><strong>Test everything.</strong> Never guess when you can measure.</li>
  <li><strong>Specificity beats generality.</strong> "Shoots sand 58 feet" beats "shoots sand far." A concrete claim is believable; an abstract one is noise.</li>
  <li><strong>Salesmanship in print.</strong> Every ad should sell as hard as a trained salesperson would, because it is one.</li>
  <li><strong>Reason-why copy.</strong> Tell the prospect why. Don't assert; explain.</li>
  <li><strong>Pre-emptive claims.</strong> When he wrote that Schlitz bottles were "steam-cleaned" (all brewers did this - no one had said it), Schlitz jumped from #5 to #1.</li>
  <li><strong>The free sample / risk-free trial.</strong> Let them try; let the product sell itself.</li>
</ul>

<h2>Dan Kennedy (1954-2024)</h2>
<p><strong>The systematizer.</strong> Kennedy took direct response - which had been fragmented across Hopkins, Halbert, Ogilvy, Schwartz - and built the operating system. His book <em>The Ultimate Sales Letter</em> is the template most modern sales letters still follow. His <em>Magnetic Marketing</em> is the playbook small businesses are still running in 2026 whether they know it or not.</p>

<p>His lasting contributions:</p>
<ul>
  <li><strong>The 10 rules of direct response.</strong> The scaffolding for all modern direct marketing. See <a href="ten-rules.html">the dedicated page</a>.</li>
  <li><strong>Niche marketing.</strong> The idea that every local business - dentists, chiropractors, contractors - should target a starving niche, not a broad market.</li>
  <li><strong>Multi-step, multi-touch campaigns.</strong> One ad isn't a campaign. A campaign is a sequence of 5-21 touches.</li>
  <li><strong>The information marketing business.</strong> The "toolkit / course / membership / mastermind" ladder most info entrepreneurs still use.</li>
  <li><strong>Copy as the asset.</strong> The sales letter, when written well, is the business's most valuable piece of intellectual property.</li>
  <li><strong>Premium pricing.</strong> Most entrepreneurs under-price. Kennedy's entire career was a case study in charging more and delivering proportionally more.</li>
</ul>

<h2>Gary Halbert (1938-2007)</h2>
<p><strong>The virtuoso.</strong> Halbert was the best pure copywriter of the four - the A-list copywriter who wrote controls that ran for decades. His <em>Gary Halbert Letter</em> (still free online at thegaryhalbertletter.com) is a graduate course in copy and direct mail. His "coat of arms" sales letter is one of the most profitable direct mail pieces ever written.</p>

<p>His lasting contributions:</p>
<ul>
  <li><strong>The A-pile / B-pile test.</strong> The stack of mail people open vs. the stack they toss. Your mailer has to look like A-pile - personal, interesting, urgent.</li>
  <li><strong>Headlines are 80% of the battle.</strong> "When you're through with your headline, you've blown 80% of your wad."</li>
  <li><strong>Fascination bullets.</strong> The punchy benefit claims - each one a tiny pitch - that drive response. See <a href="../copy/bullets.html">the bullets page</a>.</li>
  <li><strong>The 40/40/20 rule.</strong> Results = 40% list + 40% offer + 20% copy and creative.</li>
  <li><strong>The postscript.</strong> The P.S. is the second most-read element after the headline. Use it.</li>
  <li><strong>"A starving crowd"</strong> - the single most valuable thing in marketing isn't a product, it's an audience ready to buy.</li>
  <li><strong>Teaching the craft openly.</strong> His archived newsletter remains one of the best copywriting educations available.</li>
</ul>

<h2>Alex Hormozi (1992- )</h2>
<p><strong>The modernizer.</strong> Hormozi translated decades of direct-response wisdom into a 2020s vocabulary - and in doing so, he systematized offers and leads more explicitly than anyone before him. His two books, <em>$100M Offers</em> and <em>$100M Leads</em>, are the most useful compressions of the field written this decade.</p>

<p>His lasting contributions:</p>
<ul>
  <li><strong>The value equation.</strong> V = (Dream Outcome × Perceived Likelihood) / (Time Delay × Effort &amp; Sacrifice). A one-sentence framework for why offers convert. See <a href="../offer/value-equation.html">the value equation page</a>.</li>
  <li><strong>The grand slam offer.</strong> An offer so good they feel stupid saying no.</li>
  <li><strong>The core four.</strong> The four categories of lead generation: warm outreach, content, cold outreach, paid ads. See <a href="../leads/core-four.html">the core four</a>.</li>
  <li><strong>Rule of 100.</strong> Do 100 units of a lead-gen activity per day for 100 days. Discipline beats optimization at early stages.</li>
  <li><strong>Making boring fundamentals loud.</strong> Much of Hormozi's work is repackaged Kennedy, Halbert, Hopkins - but he's made the fundamentals visible to a generation that wouldn't have found the source material.</li>
</ul>

<h2>What they share</h2>
<p>Across 120 years of work, the four agree on the non-negotiables:</p>
<ul>
  <li>The market matters more than the product.</li>
  <li>The offer matters more than the copy.</li>
  <li>The copy matters more than the design.</li>
  <li>Measurement beats opinion.</li>
  <li>Write like you're writing to one person.</li>
  <li>Never run an ad without a reason to respond now.</li>
</ul>
<p>Everything in this section is built on those six ideas.</p>

<p style="margin-top:40px;">Related: <a href="scientific-advertising.html">Scientific advertising (Hopkins)</a> · <a href="ten-rules.html">The 10 rules (Kennedy)</a> · <a href="../offer/value-equation.html">Value equation (Hormozi)</a></p>
""",
    prev=("What is direct response?", "what-is-direct-response.html"),
    nxt=("Scientific advertising", "scientific-advertising.html"),
)


write_drm_page(
    slug="foundations/scientific-advertising",
    title="Scientific advertising (Hopkins)",
    description="Claude Hopkins' 1923 book is the foundational document of direct response. Its central claim: advertising is not art, it's a measurable science - and the measurement is what turns guesses into profits.",
    reading_time=7,
    body_html="""
<p class="lede">In 1923, Claude Hopkins wrote <em>Scientific Advertising</em>. Ninety-pages, no wasted words, and more durable business wisdom per page than most modern business books combined. The thesis: advertising is a measurable science. Everything that can be tested should be tested. Everything that can't should be suspicious.</p>

<h2>The core premise</h2>
<p>Before Hopkins, advertising was art - big creative agencies, clever slogans, no accountability. Hopkins ran tests. He used <strong>keyed coupons</strong> - little codes printed on each ad - so he could trace which newspaper, which city, which headline produced which number of orders. For the first time, an advertiser could say: "this ad produced 412 orders at a CPA of $2.18; this one produced 67 at $11.40." From there, you just run more of what works.</p>

<h2>Hopkins' principles (still valid in 2026)</h2>

<h3>1. Test, always</h3>
<p>Hopkins' only true rule. You don't know which of two headlines will win; run both and find out. You don't know whether coupon X or coupon Y pulls better; run both and find out. The act of testing is what separates practitioners from amateurs.</p>

<h3>2. Specificity beats generality</h3>
<p>"Shoots sand 58 feet" vs. "shoots sand far." One is a demonstrable claim; the other is a brag. Prospects trust specific claims because specificity implies you actually know. Generalities imply you're making it up.</p>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
Hopkins, on Pepsodent toothpaste: "Removes the film from your teeth." A specific mechanism, a specific benefit. The campaign built the brand that later became Colgate-Palmolive's Pepsodent.
</blockquote>

<h3>3. Salesmanship in print</h3>
<p>Every ad should sell as hard as a trained salesperson would. A salesperson in a suit doesn't rely on charm; they ask questions, uncover pain, present benefits, handle objections, close with urgency. An ad should do the same. If your ad doesn't, a better salesperson wouldn't run it.</p>

<h3>4. Reason-why copy</h3>
<p>Don't assert; explain. If you say the product is the best, the reader's next thought is "says you." If you say <em>why</em> it's the best - the specific chemistry, the specific process, the specific difference - the reader evaluates the claim on its merits.</p>

<h3>5. Pre-emptive claims</h3>
<p>Hopkins' most famous move: Schlitz beer. Every brewery at the time steam-cleaned its bottles. It was industry-standard. Nobody had <em>said</em> it in advertising. Hopkins wrote the campaign explaining the steam-cleaning process in detail. Schlitz went from #5 to #1.</p>
<p>The principle: whatever is true but unclaimed in your category, claim first. You don't have to do anything new - just say the thing everyone else takes for granted.</p>

<h3>6. Free samples and risk reversal</h3>
<p>Hopkins used free samples and money-back guarantees aggressively. Let the product sell itself. Remove the risk of trial. He was doing this in the 1910s; modern SaaS "free trials" are the same idea.</p>

<h3>7. Specific offers, not discounts</h3>
<p>A 10%-off sale is weaker than a specific, concrete offer. "Try it free for 30 days. If you don't see X, we refund you - and you keep the case." The shape of the offer matters more than the size of the discount.</p>

<h3>8. Single-focused campaigns</h3>
<p>An ad that tries to sell three things sells zero. An ad that tries to sell one thing to one person at one decision point sells. Multiple benefits are fine; multiple focus points aren't.</p>

<h2>What Hopkins got wrong (or has aged out)</h2>
<p>Hopkins is the closest thing marketing has to scripture, but not everything in the book is durable:</p>
<ul>
  <li>His distrust of humor has been overturned - humor sells plenty, especially to sophisticated markets (see <a href="../market/sophistication.html">market sophistication</a>).</li>
  <li>His reliance on coupons as the only trackable mechanism has been supplanted by every form of digital attribution.</li>
  <li>His era didn't contend with sophisticated audiences who have seen the same formula run a thousand times. The baseline level of skepticism is higher now.</li>
</ul>

<h2>How to apply Hopkins in 2026</h2>
<ol>
  <li><strong>Install testing as a default.</strong> Every campaign has at least two variants of headline, offer, or creative. Never run one-off.</li>
  <li><strong>Hunt for specific claims.</strong> Audit your copy. Replace every generality with a number, a name, a before/after, or a concrete detail.</li>
  <li><strong>Write every ad to sell, not to look good.</strong> If it wouldn't close a prospect on a sales call, it won't close them in an ad.</li>
  <li><strong>Give the reason why.</strong> For every claim, answer "because ___." Without the because, it's just noise.</li>
  <li><strong>Pre-empt.</strong> What's true about your product that everyone else does but doesn't say? Say it first.</li>
</ol>

<p style="margin-top:40px;">Related: <a href="../testing/scientific.html">Scientific testing</a> · <a href="../copy/the-stack.html">The copywriting stack</a> · <a href="ten-rules.html">Kennedy's 10 rules</a></p>
""",
    prev=("The four horsemen", "four-horsemen.html"),
    nxt=("The 10 rules (Kennedy)", "ten-rules.html"),
)


write_drm_page(
    slug="foundations/ten-rules",
    title="The 10 rules of direct response (Kennedy)",
    description="Dan Kennedy's ten rules are the scaffolding of modern direct response. Violate any one of them and the campaign leaks money. Follow all ten and the campaign runs itself.",
    reading_time=8,
    body_html="""
<p class="lede">Dan Kennedy built his career on a set of non-negotiable rules for direct response advertising. He repeated them in every book, every seminar, every newsletter. They're repetitive because they're load-bearing - violating any one of them leaks money. Follow all ten and the campaign runs itself.</p>

<h2>Rule 1 - There will always be an offer</h2>
<p>Every ad, email, letter, or page presents a specific offer. Not "learn more," not "visit our website," not "follow us on social." A specific <em>thing</em>, at a specific <em>price</em>, delivering a specific <em>benefit</em>, with a specific <em>next action</em>.</p>
<p>If your ad has no offer, it's brand advertising. Stop calling it direct response.</p>

<h2>Rule 2 - There will be a reason to respond now</h2>
<p>The enemy of direct response is "I'll think about it." Every offer ends with a deadline, a limit, a bonus expiring, a cohort closing. The reason doesn't have to be manufactured - it has to be real and specific. A vague "limited time" is weaker than "closes Friday, October 11 at 5pm EST or when the first 50 seats are claimed - whichever comes first."</p>

<h2>Rule 3 - There will be clear instructions</h2>
<p>Tell the reader exactly what to do, in order. "Click the button below, enter your email, and the video will arrive in your inbox within 2 minutes." Not: "get in touch." Assume the reader will take the path of least resistance; make the correct path the easiest one.</p>
<p>Most ads fail because they ask for a fuzzy action. A fuzzy action gets fuzzy compliance.</p>

<h2>Rule 4 - There will be tracking, measurement, and accountability</h2>
<p>Every campaign produces a known number. CPA, ROAS, leads-per-dollar, revenue-per-email. If you can't quote the number, you're running brand advertising and calling it direct response. The measurement happens <em>before</em> you scale, not after.</p>

<h2>Rule 5 - Only no-cost brand building</h2>
<p>Kennedy's rule: brand builds as a <em>byproduct</em> of direct response, not as a separate activity. You don't pay for brand advertising. Brand is what people remember you for after you sold them. Spending budget on pure awareness while the direct-response numbers are underwater is financial suicide.</p>
<p>This is the most-violated rule. Early-stage companies love paying for brand because it's socially prestigious and easy to explain to investors. It's also why so many of them run out of money.</p>

<h2>Rule 6 - There will be follow-up</h2>
<p>The ad generates the lead. The follow-up sells. Most sales happen on touch 5-12, not touch 1. A direct-response campaign without a follow-up sequence is leaving 60-90% of the revenue on the table.</p>
<p>Follow-up includes: email sequences, SMS, retargeting, phone calls, direct mail, in-product nudges. All of it, orchestrated. See the <a href="../followup/email-sequences.html">follow-up section</a>.</p>

<h2>Rule 7 - There will be strong copy</h2>
<p>Strong copy means: specific, concrete, benefit-driven, skimmable, honest, urgent. Not clever. Not "branded." Not word-count-optimized. Strong copy sounds like a person talking to one other person about something that matters to both of them. See <a href="../copy/the-stack.html">the copywriting stack</a>.</p>

<h2>Rule 8 - It will look like mail-order advertising</h2>
<p>The most controversial rule. Kennedy's claim: ads that look pretty, like modern agency work, tend to underperform ads that look like they were designed to sell - direct mail, long-form sales letters, VSLs. The ugly ad with the yellow highlighter and the red Johnson Box usually beats the tasteful ad with the nice font and the photograph.</p>
<p>Not because "ugly sells" - because direct-response design is optimized for reading, scanning, and clicking, not for design awards. Every design choice exists because it was tested and found to improve response.</p>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
You don't have to violate your taste. You do have to accept that what converts isn't always what you'd hang on your wall.
</blockquote>

<h2>Rule 9 - Results rule, period</h2>
<p>There is one measure of a campaign: did it produce the desired response at the desired cost? Not: was it beautiful, did the agency love it, did it win an award, did the CEO like it. Results are the only currency. Every opinion that contradicts the numbers is noise.</p>
<p>This is the rule that separates direct-response marketers from creative-department marketers. Both have their place; only one makes money predictably.</p>

<h2>Rule 10 - Tough-minded management</h2>
<p>Kennedy's final rule, and the one most often skipped. Direct response demands someone who will kill campaigns that don't perform, hold vendors accountable to numbers, and refuse to pay for activity that doesn't produce. Without that person, even a system that follows the other 9 rules will drift toward theater.</p>
<p>"Tough-minded" doesn't mean unkind. It means: the numbers decide. Not the opinions. Not the feelings. Not the politics. The numbers.</p>

<h2>How to use the 10 rules</h2>
<p>Print them. Put them on the wall of the marketing team's workspace. Every campaign gets a 10-rule pre-check:</p>
<ul>
  <li>What's the specific offer?</li>
  <li>What's the deadline/reason to respond now?</li>
  <li>What's the exact instruction?</li>
  <li>How will we track?</li>
  <li>What's the follow-up sequence?</li>
  <li>Did we write strong copy?</li>
  <li>What number defines success?</li>
</ul>
<p>Any campaign that fails the pre-check either gets fixed or doesn't ship. This is the "tough-minded management" rule in practice.</p>

<p style="margin-top:40px;">Related: <a href="scientific-advertising.html">Scientific advertising (Hopkins)</a> · <a href="../copy/the-stack.html">The copywriting stack</a> · <a href="../testing/scientific.html">Scientific testing</a></p>
""",
    prev=("Scientific advertising", "scientific-advertising.html"),
    nxt=("The starving crowd", "../market/starving-crowd.html"),
)


# ============================================================
# THE MARKET (5 pages)
# ============================================================

write_drm_page(
    slug="market/starving-crowd",
    title="The starving crowd",
    description="Gary Halbert's most famous teaching: if you had to open a hamburger stand and could have any advantage, what would you choose? The only correct answer is 'a starving crowd.'",
    reading_time=6,
    body_html="""
<p class="lede">Gary Halbert used to ask a question to his copywriting students: "If you and I both had a hamburger stand - and we had to compete to see who could sell the most hamburgers - what advantages would you most like to have on your side?" Students said the best beef, the best location, the best price, the best recipe. Halbert said: none of those. <em>"I'd only want one advantage: a starving crowd."</em></p>

<h2>The principle</h2>
<p>The market you sell to matters more than the product you sell. A mediocre product sold to a market that's actively looking for a solution beats a world-class product sold to people who don't care. Starving crowds buy. Well-fed crowds don't, no matter how good the food is.</p>

<p>This is the single most important strategic decision in direct response. If you pick a bad market, no amount of copywriting, offer engineering, or ad optimization will save you. If you pick a great market, you'll make money with amateur execution.</p>

<h2>What makes a crowd "starving"</h2>
<ol>
  <li><strong>Pain or desire already present.</strong> You don't have to create the want - it's there. They already feel the problem or the aspiration, and they're willing to act.</li>
  <li><strong>Money to spend.</strong> Wanting isn't buying. The market must have budget or be willing to prioritize spend.</li>
  <li><strong>Willingness to buy solutions.</strong> Some markets have pain + money but cultural resistance to paying for the kind of solution you offer.</li>
  <li><strong>Reachable.</strong> You can identify them, target them, and get a message in front of them without burning your margin in acquisition costs.</li>
  <li><strong>Recurring or scalable.</strong> Either the same customer buys repeatedly, or there are enough prospects that the market doesn't saturate.</li>
</ol>

<h2>How to tell if your market is starving</h2>
<ul>
  <li>They already pay for related products or services (competitors exist and are profitable)</li>
  <li>They spontaneously post about the problem online, search for solutions, join communities</li>
  <li>They'll book a call or consume a free lead magnet about it without hesitation</li>
  <li>Close rates on well-qualified prospects run 20%+ without heavy convincing</li>
  <li>Referrals happen organically</li>
</ul>

<h2>How to tell your market isn't starving</h2>
<ul>
  <li>You have to explain the problem before you can explain the solution</li>
  <li>Prospects say "interesting" but never buy</li>
  <li>Close rates are under 5% even on qualified leads</li>
  <li>Customer acquisition costs keep climbing as you scale</li>
  <li>You're educating, not selling</li>
</ul>
<p>If you're educating, you're in the wrong market - or you're earlier in the market than you can profitably serve. See <a href="sophistication.html">market sophistication</a>.</p>

<h2>The corollary: focus on the crowd, not the recipe</h2>
<p>Most entrepreneurs make the same mistake: they fall in love with their product and try to find a market for it. The order is wrong. Find a starving market, then build (or acquire, or repackage) the product the market wants.</p>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Hormozi's version.</strong> "Go where people are already spending money. If someone is already paying $X for a solution to problem Y, that market is pre-qualified. You don't have to convince them they have a problem. You just have to convince them your solution is better."
</blockquote>

<h2>Examples of starving crowds (2026)</h2>
<ul>
  <li>Small business owners trying to automate admin work - high pain, high budget, already paying for SaaS</li>
  <li>E-commerce brands fighting CAC inflation - actively hunting for retention and LTV plays</li>
  <li>Professionals preparing for competitive certifications (CPA, bar exam, CFA) - fixed deadline creates urgency</li>
  <li>People with chronic conditions not fully served by mainstream medicine - will pay premium for specific relief</li>
  <li>Parents wanting specific outcomes for their kids (athletic, academic, college admissions) - "best product" isn't the question; "what works for my kid" is</li>
</ul>

<h2>Examples of well-fed (wrong) crowds</h2>
<ul>
  <li>"Everyone" - the broader the target, the more fed the crowd</li>
  <li>Mature markets with entrenched $0.01-CPC-incumbents</li>
  <li>Audiences with a generic want but no acute pain ("everyone wants to be healthier")</li>
  <li>Markets where the buyer is not the user (enterprise IT buying for internal end-users whose problems the buyer doesn't feel)</li>
</ul>

<h2>The decision framework</h2>
<p>Before building a product, before writing a single ad, answer:</p>
<ol>
  <li>Who specifically is in this crowd? Name them. Describe what they do Monday morning.</li>
  <li>What are they currently spending money on to solve the problem?</li>
  <li>Are they spending the money happily, grudgingly, or desperately?</li>
  <li>How do I reach them at a sane cost?</li>
  <li>How much is solving the problem worth to them in dollars per year?</li>
</ol>
<p>If you can't answer any of these clearly, you don't have a starving crowd yet. Find one before you write the first ad.</p>

<p style="margin-top:40px;">Related: <a href="sophistication.html">Market sophistication</a> · <a href="dream-customer.html">The dream customer</a> · <a href="market-selection.html">Picking a market</a></p>
""",
    prev=("The 10 rules (Kennedy)", "../foundations/ten-rules.html"),
    nxt=("Market sophistication", "sophistication.html"),
)


write_drm_page(
    slug="market/sophistication",
    title="Market sophistication",
    description="Eugene Schwartz's five stages of market sophistication explain why a copy approach that killed last year fails now, and what to do when your market moves to stage 5.",
    reading_time=7,
    body_html="""
<p class="lede">Eugene Schwartz's <em>Breakthrough Advertising</em> (1966) introduced the five stages of market sophistication. Kennedy and Halbert both taught this material as foundational. Once you understand it, you stop being confused about why the same campaign stops working after 12 months - and what to do about it.</p>

<h2>The premise</h2>
<p>A market isn't static. Over time, as customers see more advertising for a given category, they become <em>more sophisticated</em>. The same claim that excited them in year 1 bores them in year 3 and repels them in year 5. Your copy has to match their current sophistication level.</p>

<h2>Stage 1 - Market is naive</h2>
<p>Nobody has ever made a claim like yours. A direct, simple claim wins. "I lost 30 pounds." "Make $50,000 from your couch." Short copy. Bold promise. Specificity.</p>
<p>Rare in 2026. Maybe in a newly-invented category for 6 months.</p>

<h2>Stage 2 - Direct claim has been made, amplify</h2>
<p>Competitors have made the direct claim. You win by amplifying: bigger promise, faster result, easier path. "I lost 60 pounds in 30 days." "Make $50,000 a month."</p>

<h2>Stage 3 - Claims are saturated, introduce a mechanism</h2>
<p>The market has heard every size of claim. Bigger promises aren't believable. The winner introduces a <em>new mechanism</em> - a reason this particular solution works where others didn't. "The keto diet" replaced "low fat." "Intermittent fasting" replaced generic calorie counting. Not a new result - a new <em>reason</em>.</p>

<h2>Stage 4 - Mechanism is now saturated, elaborate</h2>
<p>The mechanism itself has been commoditized. Every weight-loss product now claims "keto." You win by <em>elaborating</em> the mechanism: naming a new sub-mechanism, a refinement, a specific pathway. "Ketosis without the keto flu." "Keto for women over 40." "The 14/10 window (not 16/8) is why most people fail intermittent fasting."</p>

<h2>Stage 5 - Prospect is cynical, shift to identification</h2>
<p>The prospect has seen every claim, every mechanism, every elaboration. They're burned out. At stage 5, promises are discounted automatically. What sells now: <strong>identification</strong>.</p>
<p>The prospect wants to see <em>themselves</em> in the ad. Not a promise. Not a mechanism. A story, a persona, a tribal signal. "The guide for developers who hate conventional diets." "For founders who've tried everything." At stage 5, the message is about <em>who</em> the product is for, not <em>what</em> it does.</p>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Example across all 5 stages - weight loss.</strong><br>
<em>Stage 1 (early 1900s):</em> "Be thinner."<br>
<em>Stage 2:</em> "Be thinner faster - 20 pounds in 30 days."<br>
<em>Stage 3:</em> "Low-fat eating melts pounds." (new mechanism)<br>
<em>Stage 4:</em> "Keto - burn fat, not sugar, by staying under 20g carbs." (refined mechanism)<br>
<em>Stage 5:</em> "For busy women over 40 who have tried everything and are done being told to 'just eat less.'" (identification)
</blockquote>

<h2>How to diagnose your market's stage</h2>
<ol>
  <li>Look at competitor ads. Are they making direct claims? New mechanisms? Refined sub-mechanisms?</li>
  <li>Listen to prospects. Do they express interest, or do they say "I've tried everything and nothing works"?</li>
  <li>Check search data. What are people searching? Basic claims ("how to lose weight") = earlier stages. Hyper-specific phrases = later stages.</li>
  <li>Notice your own close rate. If direct claims are failing, the market has moved past them.</li>
</ol>

<h2>The operator's playbook for each stage</h2>
<ul>
  <li><strong>Stage 1-2:</strong> Make the claim. Be specific. Be bold. Win on breadth and volume.</li>
  <li><strong>Stage 3:</strong> Introduce or borrow a differentiated mechanism. Get technical; explain <em>why</em> yours works.</li>
  <li><strong>Stage 4:</strong> Elaborate further. Identify the precise sub-mechanism, the specific pathway, the under-exploited angle.</li>
  <li><strong>Stage 5:</strong> Identify a specific tribe. Become the go-to for a narrow slice of the market. Use story, voice, and identity more than claims.</li>
</ul>

<h2>Why markets move forward (and rarely back)</h2>
<p>Customers don't get less sophisticated. Exposure is cumulative. Once they've seen 500 direct claims, they can't un-see them. The only exceptions are:</p>
<ul>
  <li>Genuinely new categories (a few months of stage 1 before the wave of imitators)</li>
  <li>A new generation entering the market who hasn't seen the historical claims</li>
  <li>A major external event resetting conventional wisdom (a scandal, new research, regulatory change)</li>
</ul>

<h2>The stage-5 trap</h2>
<p>Most markets worth selling to are at stage 4 or 5 right now. Operators who try to win with stage-1 tactics (big claims, direct promises) in a stage-5 market underperform dramatically. The winning move at stage 5 looks strange at first - more story, less claim; more identity, less benefit - but it's what works when the market has heard it all.</p>

<p style="margin-top:40px;">Related: <a href="awareness-stages.html">Awareness stages</a> · <a href="../copy/headlines.html">Headlines</a> · <a href="../copy/formulas.html">AIDA, PAS, PASTOR</a></p>
""",
    prev=("The starving crowd", "starving-crowd.html"),
    nxt=("Awareness stages", "awareness-stages.html"),
)


write_drm_page(
    slug="market/awareness-stages",
    title="Awareness stages",
    description="Eugene Schwartz's five awareness stages - unaware, problem-aware, solution-aware, product-aware, most aware - tell you what to say in an ad based on what the prospect already knows.",
    reading_time=6,
    body_html="""
<p class="lede">Eugene Schwartz's second foundational framework, alongside <a href="sophistication.html">market sophistication</a>. Awareness stages describe what the prospect already knows - about the problem, the solution, and you. The right copy for a prospect at stage 1 is catastrophically wrong for a prospect at stage 5, and vice versa.</p>

<h2>Stage 1 - Unaware</h2>
<p>The prospect doesn't know they have a problem. They're not searching, not complaining, not thinking about it. Copy to an unaware prospect has to <em>start at the beginning</em> - identify the symptom they've been feeling but haven't named.</p>
<ul>
  <li>Angle: "Here's a problem you didn't know you had."</li>
  <li>Length: longer - you're educating before selling</li>
  <li>Format: story-driven, content-heavy, educational</li>
  <li>Channel: content marketing, podcasts, broad-reach paid social, not search</li>
</ul>

<h2>Stage 2 - Problem-aware</h2>
<p>They feel the pain. They can name the problem. They don't yet know that solutions exist. Copy speaks to the felt problem and introduces the idea that it can be solved.</p>
<ul>
  <li>Angle: "You're not crazy - this is a real problem, and it has a name."</li>
  <li>Copy leans on empathy and validation before selling</li>
  <li>Channel: communities, forums, problem-specific content</li>
</ul>

<h2>Stage 3 - Solution-aware</h2>
<p>They know solutions exist. They haven't yet picked a category. A "diet" or "CRM" or "copywriter." They're researching <em>approaches</em>.</p>
<ul>
  <li>Angle: "Of all the ways to solve this, here's why this category is the right one."</li>
  <li>Copy positions the category, not the product</li>
  <li>Channel: comparison articles, category-level search</li>
</ul>

<h2>Stage 4 - Product-aware</h2>
<p>They know your category. They may know you or your competitors. They're comparing specific products. Copy is about <em>why yours</em>.</p>
<ul>
  <li>Angle: "Of the [category] options, here's why [yours] is best for [your situation]."</li>
  <li>Specific claims, specific mechanism, specific differentiators</li>
  <li>Channel: branded search, comparison pages, review sites</li>
</ul>

<h2>Stage 5 - Most aware</h2>
<p>They already know and trust you. They're ready to buy - they just need a reason and a path. The only job of copy here is to close: offer, deadline, clear CTA.</p>
<ul>
  <li>Angle: "Here's the offer. Here's how to buy."</li>
  <li>Short, direct, minimal persuasion - just information and action</li>
  <li>Channel: email to your list, retargeting, direct outreach to existing customers</li>
</ul>

<h2>Match the copy to the stage</h2>
<p>The single most common paid-ads failure: running stage-5 copy ("Get 30% off - today only!") to a stage-1 or stage-2 audience. They don't know who you are. They haven't admitted the problem. The discount is irrelevant. They scroll past.</p>

<p>The equally common failure: running stage-1 copy (long educational content about the problem) to existing customers who are ready to buy. They don't need the lecture. They need the offer.</p>

<h2>The matrix: awareness × channel</h2>
<table style="width:100%; border-collapse:collapse; margin:20px 0;">
  <tr style="background:#f5f5f7;"><th style="padding:10px; text-align:left; border:1px solid #e5e5ea;">Channel</th><th style="padding:10px; text-align:left; border:1px solid #e5e5ea;">Typical stage</th></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Facebook / Instagram / TikTok paid</td><td style="padding:10px; border:1px solid #e5e5ea;">Stage 1-2 (interruption)</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">YouTube pre-roll</td><td style="padding:10px; border:1px solid #e5e5ea;">Stage 1-2</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Google Search (problem queries)</td><td style="padding:10px; border:1px solid #e5e5ea;">Stage 2</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Google Search (solution queries)</td><td style="padding:10px; border:1px solid #e5e5ea;">Stage 3</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Google Search (branded queries)</td><td style="padding:10px; border:1px solid #e5e5ea;">Stage 4</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Retargeting / email to list</td><td style="padding:10px; border:1px solid #e5e5ea;">Stage 4-5</td></tr>
  <tr><td style="padding:10px; border:1px solid #e5e5ea;">Direct outreach to existing customers</td><td style="padding:10px; border:1px solid #e5e5ea;">Stage 5</td></tr>
</table>

<h2>What changes at each stage</h2>
<ul>
  <li><strong>Headline</strong> - at stage 1, names the symptom; at stage 5, names the offer</li>
  <li><strong>Proof</strong> - at stage 1, softer and more general; at stage 4, specific and comparative</li>
  <li><strong>Length</strong> - longer at earlier stages, shorter at later ones</li>
  <li><strong>CTA</strong> - at stage 1, "learn more"; at stage 5, "buy now"</li>
  <li><strong>Offer structure</strong> - at stage 1, often a lead magnet; at stage 5, the full purchase</li>
</ul>

<h2>The campaign design implication</h2>
<p>A mature campaign runs <em>different creative at different stages</em>, moving prospects down the awareness ladder over time:</p>
<ol>
  <li>Stage 1 content → attract unaware prospects</li>
  <li>Stage 2 lead magnet → convert to problem-aware</li>
  <li>Stage 3 email sequence → introduce the solution category</li>
  <li>Stage 4 case studies and comparison content → position the product</li>
  <li>Stage 5 offer + deadline → close</li>
</ol>
<p>One campaign, one prospect, five pieces of copy. This is why one-ad-fits-all strategies underperform well-constructed sequences.</p>

<p style="margin-top:40px;">Related: <a href="sophistication.html">Market sophistication</a> · <a href="../copy/headlines.html">Headlines</a> · <a href="../followup/email-sequences.html">Email sequences</a></p>
""",
    prev=("Market sophistication", "sophistication.html"),
    nxt=("The dream customer", "dream-customer.html"),
)


write_drm_page(
    slug="market/dream-customer",
    title="The dream customer",
    description="The dream customer isn't a demographic. It's the specific person your offer was built for - the one whose pain is acute, whose budget is present, whose objections are easy, and whose lifetime value is high.",
    reading_time=6,
    body_html="""
<p class="lede">Ask most founders who their customer is, and you'll get an answer like "businesses with 10-100 employees in North America." That's not a customer - it's a census tract. The dream customer is one <em>specific</em> human with specific problems at a specific moment in their life. Get this right and every other marketing decision becomes easier.</p>

<h2>Why demographics fail</h2>
<p>Demographics describe categories; they don't describe <em>reasons to buy</em>. Two "35-year-old male founders of 10-person SaaS companies in New York" can have completely different problems, budgets, and willingness to buy. Demographics are the weakest signal you have; psychographics (beliefs, fears, desires) are 10x stronger, and <em>situations</em> (the specific moment they're in) are 100x stronger.</p>

<h2>The layered definition</h2>

<h3>Layer 1 - Demographics</h3>
<p>Age, location, industry, company size, role. The background information. Necessary but not sufficient.</p>

<h3>Layer 2 - Psychographics</h3>
<ul>
  <li>What do they believe about the problem?</li>
  <li>What have they tried that didn't work?</li>
  <li>Who do they trust on this topic?</li>
  <li>What's their identity? (Self-image that a purchase would reinforce.)</li>
  <li>What are they afraid will happen if they do nothing?</li>
  <li>What are they afraid will happen if they buy and it fails?</li>
</ul>

<h3>Layer 3 - Situation</h3>
<p>The most important layer. A specific moment:</p>
<ul>
  <li>What happened in the last 30 days that made them more receptive?</li>
  <li>What deadline or event is coming up?</li>
  <li>What pain did they just feel acutely?</li>
  <li>What frustration pushed them to search?</li>
</ul>
<p>The situation is the trigger. Copy that speaks to the situation converts; copy that speaks to general desires doesn't.</p>

<h2>The dream customer template</h2>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Name:</strong> [Give them a name. "Jenna the operations manager."]<br>
<strong>Demographics:</strong> [Age, role, company, location]<br>
<strong>Where they are Monday morning:</strong> [Describe their day concretely]<br>
<strong>The pain they feel:</strong> [Specific, sensory, not abstract]<br>
<strong>What they've already tried:</strong> [List 2-4 previous attempts]<br>
<strong>Why those didn't work (in their view):</strong><br>
<strong>What they believe about solutions:</strong><br>
<strong>Who they trust on this topic:</strong><br>
<strong>What would make them open your ad:</strong><br>
<strong>What would make them click:</strong><br>
<strong>What would make them buy:</strong><br>
<strong>What would make them hesitate:</strong><br>
<strong>The dream outcome in their words:</strong>
</blockquote>

<h2>The interview</h2>
<p>The dream customer can't be invented from a conference room. Interview 10-15 real prospects or customers. Ask open questions. Let them talk. Record verbatim. The exact phrases they use become your ad copy - not the phrases your team came up with.</p>
<p>Questions that work:</p>
<ul>
  <li>"Walk me through the last time you really felt this problem."</li>
  <li>"What did you search for? What did you try first?"</li>
  <li>"Why didn't that work?"</li>
  <li>"If you woke up tomorrow and this was solved, what would be different?"</li>
  <li>"What would have to be true for you to hand over money today?"</li>
</ul>

<h2>Resist the temptation to serve everyone</h2>
<p>The biggest mistake new operators make: "we don't want to alienate anyone, so let's describe our customer broadly." Broad description = vague copy = low conversion from every segment.</p>
<p>The correct move: pick the narrowest dream customer that still supports your revenue goal, and write to <em>them</em> specifically. Adjacent people will self-identify anyway. Halbert used to say: "The dog that chases two rabbits catches none."</p>

<h2>How narrow is too narrow?</h2>
<p>Narrow is only too narrow when the total addressable market can't support your revenue target. Most operators err 10x in the other direction. A million-dollar business can be built selling to 1,000 customers paying $1,000 each. You don't need "everyone."</p>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Example.</strong><br>
Wrong: "Our customer is small business owners."<br>
Better: "Our customer is service-business owners."<br>
Good: "Our customer is HVAC shop owners in the South."<br>
Great: "Our customer is HVAC shop owners in the South with 3-10 trucks who are losing weekend calls because their after-hours answering service drops 1 in 4 calls."
</blockquote>
<p>Now you know: the pain is acute, the pain has a number, the prospect can be found (trade associations, specific magazines, local search terms), and the copy writes itself.</p>

<h2>The living document</h2>
<p>The dream customer profile isn't a one-time deliverable. It evolves:</p>
<ul>
  <li>After every 10 customer conversations, update the language</li>
  <li>After every campaign, update which angles worked</li>
  <li>As your product evolves, the dream customer may narrow or shift</li>
</ul>

<p style="margin-top:40px;">Related: <a href="starving-crowd.html">The starving crowd</a> · <a href="market-selection.html">Picking a market</a> · <a href="../copy/the-lead.html">The lead (first 100 words)</a></p>
""",
    prev=("Awareness stages", "awareness-stages.html"),
    nxt=("Picking a market", "market-selection.html"),
)


write_drm_page(
    slug="market/market-selection",
    title="Picking a market",
    description="Most businesses that fail picked the wrong market. Most businesses that thrive picked the right one and then worked hard. Here's the framework for picking - before you commit a year of your life.",
    reading_time=7,
    body_html="""
<p class="lede">Most businesses that fail picked the wrong market. Most that thrive picked the right one and then worked hard. The asymmetry is brutal - you cannot outwork a bad market selection. Hormozi's version of this idea: "A great product with a bad market loses. A mediocre product with a great market wins. Find the market first."</p>

<h2>The four market criteria</h2>
<p>Hormozi's four traits of a great market:</p>
<ol>
  <li><strong>Massive pain.</strong> Prospects feel the problem acutely and often. "Mild annoyance" doesn't buy. "I can't sleep at night because of this" buys.</li>
  <li><strong>Purchasing power.</strong> The prospects have (or can justify) the money to solve it. B2B decision-makers, mid/high-income consumers, desperate people solving urgent problems.</li>
  <li><strong>Easy to target.</strong> You can reach them efficiently - a specific publication reads them, a specific keyword brings them, a specific association lists them.</li>
  <li><strong>Growing market.</strong> The category is expanding, not contracting. Prospects are entering faster than they leave.</li>
</ol>
<p>Miss any one and the business fights uphill. Miss two and it doesn't matter what you build.</p>

<h2>The "Three Rs" - Kennedy's version</h2>
<p>Dan Kennedy used a slightly different framing for picking niche markets:</p>
<ol>
  <li><strong>Reachable</strong> - a clear list, channel, or medium gives you access to them cheaply</li>
  <li><strong>Receptive</strong> - they're predisposed to buy solutions to this problem</li>
  <li><strong>Responsive</strong> - historical data (yours or competitors') shows they'll actually spend</li>
</ol>
<p>Kennedy focused on niche markets - dentists, chiropractors, printers, restaurant owners - because niches score high on all three Rs in a way broad markets rarely do.</p>

<h2>Concentration: the underrated lever</h2>
<p>A narrow market with 10,000 reachable prospects often beats a broad market with 10 million. Why: the narrow market has concentrated pain, concentrated channels, concentrated word-of-mouth. A single customer in a niche talks to 50 other prospects. A single customer in a broad market talks to nobody.</p>
<p>Niche advantages:</p>
<ul>
  <li>Lower CAC (you know exactly where to find them)</li>
  <li>Higher LTV (specialized solutions can charge more)</li>
  <li>Faster word-of-mouth (small communities talk)</li>
  <li>Competitive moat (big competitors can't afford to serve the niche)</li>
  <li>Easier copy (you can name specific pains and situations)</li>
</ul>

<h2>The TAM trap</h2>
<p>Investors want big TAMs. Early-stage marketing wants narrow focus. These are in tension. The right move for almost every early-stage company: <em>pick a niche, dominate it, then expand</em>.</p>
<p>Peter Thiel's version: "Start with a small market you can monopolize. Monopolies compound." Your pitch deck can describe a large market. Your go-to-market should be narrow.</p>

<h2>The evaluation scorecard</h2>
<p>Before committing to a market, score it (1-5 on each):</p>
<ul>
  <li>Pain intensity (how acute is it for a typical prospect?)</li>
  <li>Purchase frequency / size (annual value to you per customer)</li>
  <li>Purchasing power (do they have budget?)</li>
  <li>Targetability (can you reach them affordably?)</li>
  <li>Competitive landscape (crowded + commoditized, or under-served?)</li>
  <li>Growth (expanding, stable, or shrinking?)</li>
  <li>Personal fit (do you or your team actually understand this market?)</li>
</ul>
<p>Any market scoring below 3.5 average is probably wrong. A market scoring 4.5+ is where you want to spend the next 3 years.</p>

<h2>Signs you're in the wrong market</h2>
<ul>
  <li>You have to educate the prospect about the problem before you can sell</li>
  <li>Customers buy but don't come back or refer</li>
  <li>You're competing on price, not value</li>
  <li>CAC climbs every quarter while LTV stays flat</li>
  <li>You can't articulate your dream customer in one sentence</li>
  <li>Your close rate on qualified leads is under 10%</li>
  <li>Retention is worse than industry benchmarks</li>
</ul>
<p>If three or more apply, consider a market pivot. Sooner is cheaper than later.</p>

<h2>When to pivot markets</h2>
<p>The signal: the same product does substantially better with one segment than another. That segment is pulling the product toward itself. Follow the pull:</p>
<ol>
  <li>Look at your top 10 customers by revenue and retention. What do they have in common?</li>
  <li>Look at your top 10 most painful customers. What do they have in common?</li>
  <li>If there's a pattern - narrow industry, size, use case - reposition toward the good pattern and away from the bad.</li>
</ol>
<p>A pivot isn't a pivot of the product; it's a pivot of the market the product is sold into. Same product, different customer.</p>

<h2>Starting from zero: three paths</h2>

<h3>Path 1 - Follow pain you've lived</h3>
<p>You know the market because you've been in it. Highest probability of picking well. Low competitive risk if you're early.</p>

<h3>Path 2 - Follow money already flowing</h3>
<p>Find a niche where customers are already spending money - a sign the market is real. Build a better solution, faster delivery, or a more specific fit.</p>

<h3>Path 3 - Follow a wave</h3>
<p>A new technology, regulatory change, or cultural shift creates a window. First movers in the window get 12-24 months of easy market. Risky if you mistime it; high upside if you don't.</p>

<p style="margin-top:40px;">Related: <a href="starving-crowd.html">The starving crowd</a> · <a href="sophistication.html">Market sophistication</a> · <a href="dream-customer.html">The dream customer</a></p>
""",
    prev=("The dream customer", "dream-customer.html"),
    nxt=("The value equation", "../offer/value-equation.html"),
)

print("\n✓ Foundations + Market (10 pages)")
