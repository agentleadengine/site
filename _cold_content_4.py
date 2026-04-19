#!/usr/bin/env python3
"""Cold Email content part 4: Testing (4) + Playbooks (6) = 10 pages."""
from _build_cold import write_cold_page

DR_LINK = "../../direct-response"


# ============================================================
# TESTING (4 pages)
# ============================================================

write_cold_page(
    slug="testing/methodology",
    title="Testing methodology",
    description="How to A/B test cold email campaigns properly. Sample sizes, variables, confidence, and the common mistakes.",
    reading_time=4,
    body_html=f"""
<p class="lede">Cold email testing is the same as any direct response testing: one variable at a time, large enough sample, long enough window, measurement that reflects real outcomes. Most teams A/B test badly, declare winners early, and optimize toward noise.</p>

<h2>The basics</h2>

<ul>
<li><strong>One variable at a time.</strong> Test subject OR first line OR CTA, never all three.</li>
<li><strong>Sample size:</strong> minimum 500 per variant for reply-rate tests, 1000+ for positive reply rate (much rarer event).</li>
<li><strong>Duration:</strong> minimum 7 days to capture day-of-week variation.</li>
<li><strong>Statistical significance:</strong> use a calculator (AB Test Guide, Optimizely) — don't eyeball.</li>
</ul>

<h2>The split</h2>

<p>50/50 split by default. For risky challengers (new copy that could tank reply rate), 70/30 in favor of the control until you see early signal.</p>

<h2>Running the test</h2>

<ol>
<li>Define hypothesis: "Subject line A will outperform B because [reason]"</li>
<li>Randomly split prospects 50/50 (cold email tools do this automatically)</li>
<li>Keep everything else identical</li>
<li>Send during same window</li>
<li>Track reply rate + positive reply rate for at least 7 days after send</li>
<li>Run significance calculator</li>
<li>Declare winner or inconclusive</li>
</ol>

<h2>The significance trap</h2>

<p>500 emails × 3% reply rate = 15 replies per variant. A 1-reply difference between variants is noise, not signal. For small-sample cold email tests, you need large differences (50%+ lift) before you can confidently say one variant won.</p>

<p>Rule of thumb: if your test produced under 10 replies per variant, you don't have enough data. Keep running or increase volume.</p>

<h2>Primary metric: positive reply rate</h2>

<p>Overall reply rate includes "unsubscribe," "wrong person," "not interested." These aren't conversions. Positive reply rate (interested, want to talk, send me more info) is the metric that correlates to pipeline.</p>

<p>Track both — overall reply rate tells you about deliverability and subject line effectiveness, positive reply rate tells you about offer/copy quality.</p>

<h2>Common testing mistakes</h2>

<h3>Testing too many variables</h3>
<p>"Let's test new subject + new first line + new CTA." Result: you don't know which change moved the needle. Can't scale what worked.</p>

<h3>Declaring winners too early</h3>
<p>Day 2 variant A has 5% vs variant B's 3%. "A wins!" Run to full sample. Often the gap closes or reverses.</p>

<h3>Ignoring sample size</h3>
<p>Testing on 100 prospects and acting on the results. You're optimizing toward noise.</p>

<h3>Changing mid-test</h3>
<p>Tweaking copy partway through invalidates results. Wait for test completion before iterating.</p>

<h3>Not running a control</h3>
<p>Launching a new campaign without a control to compare against. You can't tell if it's working compared to what.</p>

<h2>Related</h2>
<p>Covered in more depth on <a href="{DR_LINK}/testing/scientific.html">scientific testing</a> in the direct response section — the same principles apply to cold email, VSLs, landing pages, and ads.</p>
""",
    prev=("Sequence length", "../sequences/length.html"),
    nxt=("What to test", "what-to-test.html"),
)


write_cold_page(
    slug="testing/what-to-test",
    title="What to test",
    description="Not every variable is worth testing. Here's the priority order, ranked by expected impact.",
    reading_time=4,
    body_html="""
<p class="lede">Test the things that move the needle. Skip the cosmetic stuff. Here's the rough priority order by impact on reply rates and pipeline.</p>

<h2>Tier 1: highest impact (10-50%+ lift possible)</h2>

<h3>Subject line</h3>
<p>Single biggest driver of open rates. Can swing opens by 30-60%. Test one new subject line per week against the control.</p>

<h3>First line (personalization)</h3>
<p>The make-or-break for reply rate. A truly personal first line vs a generic one can 2-3x replies.</p>

<h3>Offer / angle</h3>
<p>The specific angle you're pitching. Same product, different framing can double positive reply rate. E.g., "help your AEs ramp faster" vs "improve forecast accuracy" — different buyers care about different problems.</p>

<h3>Sender identity</h3>
<p>Who the email is "from." Founder vs SDR vs fictional-persona email can shift reply rates. Test this cautiously — sender reputation builds slowly.</p>

<h2>Tier 2: medium impact (5-20%)</h2>

<h3>Email length</h3>
<p>Very short (40 words) vs standard (80-100) vs longer (150+). Typical B2B sweet spot is 70-110 words.</p>

<h3>CTA structure</h3>
<p>Specific times ("Tue 2pm or Thu 10am") vs open ("What works?") vs content offer ("want the summary?"). Different CTAs serve different prospect states.</p>

<h3>Day of week</h3>
<p>Tuesday-Thursday mornings work best for most B2B. Monday and Friday underperform. Test within the window.</p>

<h3>Time of day</h3>
<p>Recipient-local 8-11am vs 1-3pm. Both work; specific audience may prefer one.</p>

<h3>Sequence length</h3>
<p>5-touch vs 7-touch. See <a href="../sequences/length.html">sequence length</a>.</p>

<h2>Tier 3: small impact (under 5%)</h2>

<h3>Email signature</h3>
<p>Minimal vs expanded. Usually doesn't matter much, but heavily marketing-ized signatures hurt.</p>

<h3>Send volume per mailbox</h3>
<p>30/day vs 50/day. Deliverability-related, not copy-related.</p>

<h3>Greeting style</h3>
<p>"Hey [name]" vs "Hi [name]" vs "[name],". Rarely meaningful differences.</p>

<h3>Formatting</h3>
<p>Plain text vs minimal HTML. Plain text wins for cold — but the margin is small.</p>

<h2>Don't bother testing</h2>

<ul>
<li>Font in email (unless you're using something weird)</li>
<li>Button color (you probably shouldn't have a button in cold email)</li>
<li>Exact greeting punctuation</li>
<li>Minor word changes ("sale" → "special offer")</li>
<li>Order of 2 sentences mid-email</li>
</ul>

<p>These changes at typical cold email volumes produce differences smaller than the noise in the data. Optimization theater.</p>

<h2>The experiment pipeline</h2>

<p>Maintain a running list of hypotheses. Each week or two, test the highest-leverage one. Keep a log:</p>

<ul>
<li>Hypothesis tested</li>
<li>Variable changed</li>
<li>Result (winner / loser / inconclusive)</li>
<li>Size of effect</li>
<li>What you rolled forward</li>
</ul>

<p>Over 6 months you build a proprietary testing archive worth more than any playbook. The knowledge is specific to your audience, your offer, your voice.</p>

<h2>Rapid iteration without full tests</h2>

<p>For small-volume campaigns (under 500 sends), you can't A/B test cleanly. Instead, use qualitative iteration:</p>

<ol>
<li>Send 200 emails of version A</li>
<li>Read the replies (both positive and negative)</li>
<li>Rewrite based on what you learned</li>
<li>Send 200 of version B</li>
<li>Compare directionally, not statistically</li>
</ol>

<p>Faster than formal testing. Good for early-stage campaigns where you're still figuring out the pitch.</p>
""",
    prev=("Testing methodology", "methodology.html"),
    nxt=("Reply rate vs positive reply", "reply-metrics.html"),
)


write_cold_page(
    slug="testing/reply-metrics",
    title="Reply rate vs positive reply rate",
    description="Overall reply rate lies. Positive reply rate is the metric that correlates to pipeline.",
    reading_time=3,
    body_html="""
<p class="lede">Cold email tools show you reply rate. That number includes unsubscribes, OOO replies, wrong-person responses, and "not interested." It's directional but misleading. Positive reply rate — replies that indicate interest — is the metric that actually predicts meetings and pipeline.</p>

<h2>The reply taxonomy</h2>

<p>Every reply falls into one of these buckets:</p>

<ul>
<li><strong>Positive:</strong> interested, want more info, willing to book call</li>
<li><strong>Interested later:</strong> not now, try again in X months</li>
<li><strong>Wrong person:</strong> refer to someone else</li>
<li><strong>Objection:</strong> have a concern, not a "no"</li>
<li><strong>Not interested / polite no:</strong> clear pass</li>
<li><strong>Unsubscribe / hostile:</strong> remove me, stop emailing</li>
<li><strong>OOO / auto-reply:</strong> out of office</li>
<li><strong>Ambiguous:</strong> "?"  or single-word responses</li>
</ul>

<h2>Calculating positive reply rate</h2>

<p>Positive reply rate = (positive + interested-later + wrong-person-with-referral) / emails delivered.</p>

<p>Wrong-person WITH a referral counts because it leads to pipeline via a warmer contact. Wrong-person without referral counts as noise.</p>

<h2>Typical ratios</h2>

<p>For a well-run B2B cold campaign:</p>
<ul>
<li>Overall reply rate: 8-15%</li>
<li>Of replies, positive intent: 15-30%</li>
<li>Positive reply rate (absolute): 1.5-4.5%</li>
<li>Of positive, meetings booked: 40-70%</li>
<li>Of meetings, opportunities created: 30-60%</li>
</ul>

<p>Full funnel: 1000 emails → ~120 replies → ~30 positive → ~15 meetings → ~7 opportunities → ~2-3 closed deals.</p>

<p>Your ratios will differ by ICP and offer, but this gives you a sense of the math.</p>

<h2>Why overall reply rate lies</h2>

<p>Two campaigns:</p>
<ul>
<li>Campaign A: 10% overall reply rate, 5% positive</li>
<li>Campaign B: 18% overall reply rate, 1.5% positive</li>
</ul>

<p>Campaign B looks better on the dashboard. Campaign A actually produces more pipeline — because the replies it generates are more likely to be interested buyers. Campaign B is probably generating lots of "remove me" and "wrong person" noise.</p>

<p>Always optimize for positive reply rate, not total reply rate.</p>

<h2>The classification workflow</h2>

<p>Two options:</p>

<h3>Manual</h3>
<p>Read each reply, tag it by type. Works for small volume (under 100 replies/week). Most accurate.</p>

<h3>AI-assisted</h3>
<p>Use Claude or similar to classify replies automatically. Feed the reply text, get back a classification. 90-95% accurate. Saves time at volume.</p>

<div class="prompt-box">
<div class="prompt-box-label">Reply classifier prompt</div>
<button class="copy-btn">Copy</button>
<pre>Classify this cold email reply into one of:
- POSITIVE (interested, wants to talk, engaged)
- INTERESTED_LATER (not now, try again in X)
- WRONG_PERSON (redirects to someone else)
- OBJECTION (has concern, not a no)
- NOT_INTERESTED (polite pass)
- UNSUBSCRIBE (remove me, hostile)
- OOO (auto-reply)
- AMBIGUOUS (unclear)

Reply text:
[paste reply]

Output just the category name.</pre>
</div>

<h2>The dashboard setup</h2>

<p>At minimum, track weekly:</p>
<ul>
<li>Emails sent</li>
<li>Bounces (under 2%)</li>
<li>Unsubscribes (under 1%)</li>
<li>Overall reply rate</li>
<li>Positive reply rate</li>
<li>Meetings booked</li>
<li>Meetings held (not all bookings get held)</li>
</ul>

<p>Plus per-campaign and per-mailbox breakdowns. Anomalies in any single mailbox (sudden spam spike, low replies) signal deliverability problems.</p>

<h2>The feedback loop</h2>

<p>Positive reply content is gold for copy iteration. Read the positive replies:</p>
<ul>
<li>What did they agree with?</li>
<li>What did they ask for?</li>
<li>What language do they use?</li>
<li>What objections did they raise?</li>
</ul>

<p>Feed these insights into the next campaign's copy. The prospects' own words outperform anything you invent.</p>
""",
    prev=("What to test", "what-to-test.html"),
    nxt=("The iteration loop", "iteration.html"),
)


write_cold_page(
    slug="testing/iteration",
    title="The iteration loop",
    description="Cold email isn't set-and-forget. Here's the weekly rhythm for getting better each cycle.",
    reading_time=3,
    body_html="""
<p class="lede">Cold email is a game of iteration. The first version is a draft. The 10th version is a product. The operators who win are the ones who run the feedback loop weekly and compound learnings over months.</p>

<h2>The weekly loop</h2>

<ol>
<li><strong>Monday — measure.</strong> Pull last week's numbers: sends, opens, replies, positive replies, meetings.</li>
<li><strong>Monday — read.</strong> Read every positive reply and objection. Extract patterns.</li>
<li><strong>Monday — decide.</strong> What's the one thing you'll change this week? (One variable.)</li>
<li><strong>Tuesday — ship.</strong> Launch the new variant.</li>
<li><strong>Friday — checkpoint.</strong> Early signal: is the new variant materially different, or same as control?</li>
<li><strong>Next Monday — call it.</strong> Winner, loser, inconclusive. Roll forward.</li>
</ol>

<p>15-30 minutes per week. Compound effect over 12 weeks is dramatic.</p>

<h2>What to change each cycle</h2>

<p>Rotate through your Tier 1 variables (see <a href="what-to-test.html">what to test</a>):</p>

<ul>
<li>Week 1: subject line</li>
<li>Week 2: first line approach</li>
<li>Week 3: offer angle</li>
<li>Week 4: CTA structure</li>
<li>Week 5: subject again (new challenger)</li>
<li>...</li>
</ul>

<p>Each cycle, keep the winners. Replace the losers. Over 12 weeks your control email is 12 improvements ahead of where you started.</p>

<h2>The monthly retro</h2>

<p>Once a month, step back:</p>
<ul>
<li>What's trending? (reply rate, positive rate, pipeline generated)</li>
<li>What's breaking? (deliverability drift, cold mailbox aging, list fatigue)</li>
<li>What's the biggest leverage move for next month?</li>
</ul>

<p>Sometimes the answer isn't copy. It's list quality, deliverability, or a new segment.</p>

<h2>Quarterly reset</h2>

<p>Every 90 days:</p>
<ul>
<li>Full review of current controls vs start-of-quarter controls</li>
<li>Kill campaigns that underperform</li>
<li>Invest more in campaigns that work</li>
<li>Explore a new ICP or angle if existing are saturating</li>
<li>Review infrastructure: new sending domains, retired mailboxes, warming cadence</li>
</ul>

<h2>The log</h2>

<p>Keep a running doc of every experiment. Format:</p>

<div class="prompt-box">
<div class="prompt-box-label">Experiment log entry</div>
<button class="copy-btn">Copy</button>
<pre>Date: [YYYY-MM-DD]
Campaign: [name]
Hypothesis: [what I thought would happen and why]
Variable changed: [one specific thing]
Control version: [exact text or ID]
Challenger version: [exact text or ID]
Sample size per variant: [number]
Duration: [days]
Result:
- Control: [reply rate, positive rate]
- Challenger: [reply rate, positive rate]
- Winner: [control / challenger / inconclusive]
- Effect size: [percentage lift]
What I rolled forward: [did challenger become new control?]
What I learned: [one-sentence takeaway]</pre>
</div>

<p>After 6 months you have an experimental archive specific to your audience. It's worth more than any playbook — it's the ground truth of what actually works for your segment.</p>

<h2>The honest truth about iteration</h2>

<p>Most experiments are inconclusive. Most changes don't materially move the needle. You find the 10% that do and scale them. The discipline is in running the process consistently, not in making every experiment a winner.</p>

<p>Operators who iterate for 90 days outperform operators who launch-and-forget by 3-5x on pipeline per email sent. The compounding is real.</p>
""",
    prev=("Reply rate vs positive reply", "reply-metrics.html"),
    nxt=("B2B SaaS outbound", "../plays/b2b-saas.html"),
)


# ============================================================
# PLAYBOOKS (6 pages)
# ============================================================

write_cold_page(
    slug="plays/b2b-saas",
    title="B2B SaaS outbound",
    description="Cold email for B2B SaaS. ICP, sequences, offers, and what's different about tech buyers.",
    reading_time=4,
    body_html="""
<p class="lede">B2B SaaS outbound is the most-run cold email play in the world, which means targets are the most jaded. What works: tight ICP, signal-triggered timing, and a pitch that acknowledges you're not special — you just solve a specific thing specifically well.</p>

<h2>The ICP</h2>

<ul>
<li>Specific role at specific company size</li>
<li>Specific tech stack (often signal for need or fit)</li>
<li>Specific growth stage (funded, scaling, repositioning)</li>
<li>Specific vertical if you go niche</li>
</ul>

<p>Avoid: "B2B SaaS, 50-500 employees" — too broad. Better: "B2B SaaS companies 50-200 people, who raised Series A-B in last 18 months, with AEs but no dedicated RevOps."</p>

<h2>Best signals</h2>

<ul>
<li>Recent funding round (30-90 days fresh)</li>
<li>Executive hire (new CRO = pipeline push)</li>
<li>Job postings (new VP Sales = reorg, AE hiring)</li>
<li>Tech stack changes (added tool X, likely needs Y)</li>
<li>G2 / review site activity</li>
<li>Product launches or major releases</li>
</ul>

<h2>Typical offers</h2>

<ul>
<li>15-minute discovery call</li>
<li>Free audit / teardown (of their funnel, emails, onboarding)</li>
<li>Industry-specific benchmark report</li>
<li>Short demo focused on one specific problem (not full product)</li>
</ul>

<h2>The pitch template</h2>

<div class="prompt-box">
<div class="prompt-box-label">B2B SaaS cold email</div>
<button class="copy-btn">Copy</button>
<pre>Subject: [specific observation, 3-5 words]

[first line: specific trigger from LinkedIn / news / hiring]

We work with [specific role] at [company size] B2B SaaS teams on [specific problem].

Specifically, the spot where [pain scenario]. [Named client] went from [before state] to [after state].

Worth 15 min next week? Tue 2pm or Thu 10am ET?

Sam</pre>
</div>

<h2>Sequence tips for SaaS</h2>

<ul>
<li>5-touch standard, 22-day window</li>
<li>Email 3 (reframe) works particularly well as a free teardown offer: "Want me to send a 10-minute Loom breaking down your signup flow?"</li>
<li>Email 4 (case study) hits hardest when the client is in the same specific vertical or growth stage</li>
<li>Breakup (email 5) explicitly names a future trigger: "if AE ramp becomes a priority in Q2..."</li>
</ul>

<h2>What NOT to do</h2>

<ul>
<li>Don't pitch the platform. Pitch one angle.</li>
<li>Don't list features. Name a specific outcome.</li>
<li>Don't "I'd love to chat." Propose specific times.</li>
<li>Don't name-drop generic logos. Name clients in their vertical.</li>
<li>Don't pretend to have found them magically. Reference the real trigger.</li>
</ul>

<h2>Volume targets</h2>

<p>Typical SaaS cold operation:</p>
<ul>
<li>30-50 mailboxes, 1000-2000 emails/day</li>
<li>0.5-2% positive reply rate (higher = tighter targeting)</li>
<li>5-20 meetings booked per week</li>
<li>CAC of $400-2000 per closed customer at standard SaaS ACV</li>
</ul>

<h2>The common mistakes</h2>

<ul>
<li>Too broad ICP → low relevance → low reply rate</li>
<li>Pitching the whole product → nobody cares about 10 features in an 80-word email</li>
<li>No specific trigger → email feels mass-sent even if it isn't</li>
<li>Not iterating → same email for 6 months, reply rate decays</li>
<li>Ignoring deliverability → great copy in spam folder</li>
</ul>
""",
    prev=("The iteration loop", "../testing/iteration.html"),
    nxt=("Agency + services outbound", "agency.html"),
)


write_cold_page(
    slug="plays/agency",
    title="Agency + services outbound",
    description="Cold email for agencies and consultancies. Higher deal values, longer cycles, different copy patterns.",
    reading_time=4,
    body_html="""
<p class="lede">Agency cold email has different dynamics than SaaS: higher deal value, relationship-driven, longer cycles, and buyers who've seen a hundred agency pitches. What works: niche specificity, proof over promises, and an offer that respects the buyer's time.</p>

<h2>The ICP challenge</h2>

<p>Agencies that pitch "marketing services to SMBs" fail because the ICP is too generic. Winning agency outbound is niched:</p>

<ul>
<li>By vertical ("marketing for DTC supplement brands")</li>
<li>By growth stage ("SEO for Series B B2B SaaS")</li>
<li>By specific service ("paid acquisition audit for $10M+ ecommerce")</li>
<li>By specific outcome ("we cut CAC for DTC brands from $X to $Y")</li>
</ul>

<p>The narrower, the higher the close rate. Agencies that try to do everything for everyone close nothing cold.</p>

<h2>The pitch pattern</h2>

<p>Agency cold pitches work best when they offer specific value upfront, not a discovery call:</p>

<ul>
<li>"Teardown" (audit of their current ads / emails / site)</li>
<li>"Benchmark report" for their segment</li>
<li>"Strategy memo" — 2-3 pages of specific recommendations</li>
<li>"Sample deliverable" — show what working with you looks like</li>
</ul>

<div class="prompt-box">
<div class="prompt-box-label">Agency cold email</div>
<button class="copy-btn">Copy</button>
<pre>Subject: [observation about their specific marketing]

[first line: specific thing you noticed about their work]

We work exclusively with [narrow niche] on [specific service]. Usually on the problem where [specific pain] — which you might be hitting given [trigger].

Happy to send a 3-slide teardown of what I'd do first. No call needed unless it's useful.

[Named client] in your space went from [before] to [after].

Worth the teardown?

Sam</pre>
</div>

<h2>Why this works</h2>

<ul>
<li>Offers value upfront instead of asking for their time</li>
<li>Shows specificity about their situation (not mass-sent)</li>
<li>Low friction ("no call needed")</li>
<li>Proof comes from their space, not random logos</li>
</ul>

<h2>The follow-up that closes</h2>

<p>After positive reply and teardown sent:</p>
<ul>
<li>Email: "Here's the teardown. If any of this resonates, worth a 15-min conversation."</li>
<li>Typical conversion: 40-60% of teardown recipients book a call</li>
<li>Of calls, 20-40% convert to paid engagement</li>
</ul>

<h2>Deal values and sequences</h2>

<ul>
<li>Agency retainers typical $5K-$50K/month</li>
<li>Projects $10K-$250K one-time</li>
<li>Sequence length: 5-7 touches, 4-6 weeks</li>
<li>Decision cycles: 2-8 weeks</li>
<li>ROI math supports high-touch outbound per-prospect</li>
</ul>

<h2>What fails</h2>

<ul>
<li>"We help businesses grow" — generic, nobody cares</li>
<li>"Check out our case studies" — nobody clicks your link</li>
<li>"Let's schedule a 30-minute discovery call" — high friction</li>
<li>Pitching service menu rather than one specific problem</li>
<li>Not showing vertical-specific knowledge in first email</li>
</ul>

<h2>The long game</h2>

<p>Agency buyers remember you even if they don't buy now. Clean outreach → branded memory → inbound 6 months later when their current provider fails. Play long. Don't burn the relationship with spammy follow-up.</p>
""",
    prev=("B2B SaaS outbound", "b2b-saas.html"),
    nxt=("Founder-led outbound", "founder-led.html"),
)


write_cold_page(
    slug="plays/founder-led",
    title="Founder-led outbound",
    description="Cold email from the founder. Different from SDR outbound in tone, volume, and leverage.",
    reading_time=4,
    body_html="""
<p class="lede">Founder-led cold email outperforms SDR outbound on reply rates but caps at low volume. When a founder sends, it signals "this matters to the company." When an SDR sends, it signals "you're one of 500 on our list." Different dynamics, different playbook.</p>

<h2>Why founder email converts better</h2>

<ul>
<li>Social proof of the title itself</li>
<li>Signals commitment to the relationship</li>
<li>Implies the prospect can skip 2-3 layers of qualification</li>
<li>Feels personal even when it isn't fully</li>
<li>Enterprise buyers especially respond to founder outreach</li>
</ul>

<p>Typical reply rate uplift: 30-60% over SDR-authored equivalent.</p>

<h2>The constraints</h2>

<ul>
<li>Can't send 1000/day without destroying your time or reputation</li>
<li>Replies land in your personal inbox; you own handling them</li>
<li>Your domain and email are used for everything else — can't burn it</li>
<li>Takes real time per prospect</li>
</ul>

<p>Realistic volume: 50-200 emails/week from the founder. Higher and it becomes fake.</p>

<h2>The positioning</h2>

<p>Founder-led works best when you name the role directly:</p>

<div class="prompt-box">
<div class="prompt-box-label">Founder cold email</div>
<button class="copy-btn">Copy</button>
<pre>Subject: [observation specific to them]

[first line: specific and clearly-researched]

I'm Sam, I started [company]. We work with [specific role] at [company type] on [specific problem].

Reaching out directly because [reason this matters to me / the company]. [One specific angle that requires founder attention.]

Happy to jump on a 15-min call. Tue 2pm or Thu 10am ET?

Sam
Founder, [Company]</pre>
</div>

<h2>The signature</h2>

<p>Lean into the founder identity:</p>
<ul>
<li>"Sam, Founder & CEO"</li>
<li>"Sam — Founder, [Company]"</li>
</ul>

<p>The title is the proof. Sending from founder@company.com or sam@company.com (not sales@) reinforces it.</p>

<h2>The "I rarely do this" move</h2>

<p>One pattern that works: explicitly note this isn't mass outreach.</p>

<ul>
<li>"I hand-send about 10 of these a week."</li>
<li>"Not something I do at scale — but your [specific trigger] made me want to reach out."</li>
</ul>

<p>Honest version: if you're sending 50-100/week personally, it's still rare by cold email standards. The framing is truthful and stands out.</p>

<h2>The CEO-to-CEO angle</h2>

<p>If your prospect is also a founder/CEO, peer-to-peer language works:</p>

<ul>
<li>"Founder to founder"</li>
<li>"CEO to CEO"</li>
<li>"Thought this might land better from me directly"</li>
</ul>

<p>Avoid if it sounds performative. Works when natural.</p>

<h2>Handling replies personally</h2>

<p>Founder email means founder reply handling. Rules:</p>

<ul>
<li>Respond to every positive reply within hours (same-day ideal)</li>
<li>Hand off to an AE only after the first call, not before</li>
<li>The handoff email must be written by you, not the AE: "I had Sam reach out, he'll handle the deep dive"</li>
<li>Expect the first 10-20 meetings per week yourself</li>
</ul>

<p>Founder outbound falls apart if you pitch as the founder and then hand off to a junior rep for the first call. The prospect expected you.</p>

<h2>When to graduate from founder-led</h2>

<ul>
<li>When you're booking more meetings than you can take</li>
<li>When the company has real brand (founder title less critical)</li>
<li>When the ICP is broad enough to need volume</li>
<li>When you can hire an AE who can deliver the call as well as you can</li>
</ul>

<p>Many founders transition slowly: start 100% founder-led, move to 50/50 (founder for enterprise, SDR for mid-market), then mostly SDR as the company scales.</p>

<h2>Common mistakes</h2>

<ul>
<li>Pitching "as the founder" but using an automation tool without personalization — looks fake</li>
<li>Using founder email then handing to junior rep for first call</li>
<li>Not responding personally to replies (spoils the whole dynamic)</li>
<li>Treating it like SDR volume play (doesn't scale)</li>
</ul>
""",
    prev=("Agency + services outbound", "agency.html"),
    nxt=("SDR-led outbound", "sdr-led.html"),
)


write_cold_page(
    slug="plays/sdr-led",
    title="SDR-led outbound",
    description="How SDR teams run cold email at scale. Team structure, quotas, and the operational reality.",
    reading_time=4,
    body_html="""
<p class="lede">Once a company has scaled past founder-led outbound, cold email shifts to an SDR team. The playbook changes: volume goes up, personalization per email goes down, operational rigor goes way up. This is how SDR-led cold email actually runs.</p>

<h2>Team structure</h2>

<p>Typical SDR team running cold email:</p>
<ul>
<li>1 SDR manager</li>
<li>4-12 SDRs</li>
<li>1 RevOps / cold email operator (tools, lists, infrastructure)</li>
<li>1 data analyst (for mid-to-large orgs)</li>
</ul>

<p>Smaller orgs combine roles; larger split further (list builder, email writer, reply handler all distinct).</p>

<h2>Quota reality</h2>

<ul>
<li>150-300 emails per SDR per day</li>
<li>Across a 10-SDR team: 1500-3000 emails/day</li>
<li>50-100 meetings booked per SDR per month (target)</li>
<li>Conversion meetings → opportunities: 30-50%</li>
</ul>

<p>SDRs spend most of their day on list research, reply handling, and meeting booking — not on writing emails. Writing is a once-a-week batched task.</p>

<h2>The ownership model</h2>

<h3>Option A: SDR owns list + copy + sends + replies</h3>
<p>Full ownership per rep. Works for small teams. Breaks down at scale (copy quality varies, no shared learnings).</p>

<h3>Option B: Centralized copy, SDR-specific lists</h3>
<p>RevOps or marketing writes the emails. SDRs get assigned lists and send the approved copy. Standard for mid-to-large teams.</p>

<h3>Option C: Full specialization</h3>
<p>List builder → copy team → send + reply specialists → AE handoff. Enterprise model.</p>

<h2>Infrastructure for scale</h2>

<ul>
<li>50-150 sending mailboxes</li>
<li>10-30 sending domains</li>
<li>Instantly / Smartlead / Salesloft / Outreach as core tool</li>
<li>Apollo / ZoomInfo + Clay for data</li>
<li>CRM (Salesforce) for pipeline</li>
<li>Call tracking if phone is in the mix</li>
</ul>

<h2>The copy reality at scale</h2>

<p>SDR-led cold email can't do deep per-prospect personalization at 300/day. Compromise:</p>

<ul>
<li>Heavily templated body with 2-3 merge fields</li>
<li>AI-generated first lines (per-prospect) via Clay</li>
<li>Segmented templates (different copy per ICP segment)</li>
</ul>

<p>Reply rates are lower per email than founder-led (1-3% vs 3-8%) but total volume produces more meetings.</p>

<h2>The cadence discipline</h2>

<p>SDR teams need rigid cadences or the system collapses:</p>

<ul>
<li>Monday AM: list review, ICP validation</li>
<li>Monday-Friday: 150-300 emails/day sent on schedule</li>
<li>Continuous reply handling (within 24 hours)</li>
<li>Friday: weekly performance review, copy iteration</li>
</ul>

<h2>Common failure modes</h2>

<h3>SDR burnout</h3>
<p>Cold email is psychologically tough. Rep turnover in SDR roles is notoriously high (12-18 months). Mitigate with career progression, training, manageable quotas.</p>

<h3>Copy decay</h3>
<p>Same email template for 6 months → reply rate drops 50%. Mandate monthly copy refresh.</p>

<h3>Deliverability death spiral</h3>
<p>No one owns deliverability → sender reputation degrades → replies drop → team panics → volume increases → reputation worsens. Need dedicated RevOps ownership.</p>

<h3>Bad handoffs</h3>
<p>SDR books meeting, AE doesn't read notes, prospect feels dropped. Standardize handoff process: structured notes, briefing time, joint AE+SDR calls for critical prospects.</p>

<h2>Measurement</h2>

<p>Weekly per-SDR metrics:</p>
<ul>
<li>Emails sent</li>
<li>Positive reply rate</li>
<li>Meetings booked</li>
<li>Meetings held (shows reliability of bookings)</li>
<li>Meetings → opportunities</li>
<li>Opportunities → closed (lagging but matters)</li>
</ul>

<h2>Compensation</h2>

<ul>
<li>SDR base: $45K-$75K depending on region</li>
<li>Variable: $15K-$30K tied to meetings booked + meetings held</li>
<li>Accelerators on meetings that convert to closed deals</li>
</ul>

<p>Variable should weight meetings-held and meetings-converting, not just bookings (prevents booking junk meetings to hit quota).</p>
""",
    prev=("Founder-led outbound", "founder-led.html"),
    nxt=("Cold email for SEO", "link-building.html"),
)


write_cold_page(
    slug="plays/link-building",
    title="Cold email for SEO link building",
    description="Cold email for link building. Different audience (marketers, editors, writers), different pitch patterns.",
    reading_time=4,
    body_html="""
<p class="lede">Link building via cold email is a specialized subset of outbound. The target is other content creators, editors, and marketing ops. The offer isn't a sales call — it's a link placement, guest post, or content swap. Different playbook, same fundamentals.</p>

<h2>The audience</h2>

<ul>
<li>Marketing managers at companies with relevant blogs</li>
<li>Writers and editors of industry publications</li>
<li>Site owners with resource pages in your niche</li>
<li>Content operators at larger sites</li>
</ul>

<p>All are jaded. All get 50+ link-building pitches a week. Generic "your article about X missed my article about Y" emails die on arrival.</p>

<h2>The link-building offer types</h2>

<h3>Broken link replacement</h3>
<p>"Your [resource page / blog post] links to [dead URL]. I have [relevant replacement]. Want me to send details?"</p>

<p>Strong because you're solving their problem (broken link = bad UX).</p>

<h3>Resource addition</h3>
<p>"You have a resource page on [topic]. Our [resource] is relevant. Here's why it adds to yours, not just dupes."</p>

<p>Weaker. Only works if your resource is genuinely better/different.</p>

<h3>Guest post</h3>
<p>"I'd like to contribute a post on [specific topic]. Here are 3 angle options I've already thought through. Here's my most recent relevant writing."</p>

<p>Works when you bring expertise and have published work to prove it.</p>

<h3>Digital PR / data-driven</h3>
<p>"We ran a study on [topic]. Here's the writeup. Thought it'd fit your coverage of [beat]."</p>

<p>Highest-quality links. Requires having done actual research or data collection.</p>

<h3>Unlinked mention</h3>
<p>"You mentioned [Company / Product] in [URL]. Noticed it's not linked. If you'd like to link, happy to supply."</p>

<p>Works because you're asking for something trivial.</p>

<h2>The pitch</h2>

<div class="prompt-box">
<div class="prompt-box-label">Link building cold email (broken link)</div>
<button class="copy-btn">Copy</button>
<pre>Subject: broken link on your [topic] page

[first line: specific reference to the exact page and broken link]

Your resource page at [URL] links to [broken URL] for [topic]. Link's dead (404 confirmed).

I wrote an updated piece on [same topic] that might work as a replacement: [URL]. [One-sentence why it's a better fit than the dead link.]

Not pushy — just noticed it while researching [their space]. Thought you'd want to know.

Sam</pre>
</div>

<h2>What kills link building pitches</h2>

<ul>
<li>"I read your article and loved it" — sycophantic opening, nobody believes it</li>
<li>Generic praise of their site</li>
<li>No specific URL referenced</li>
<li>Asking for "thoughts" or "feedback" (cover for asking for a link)</li>
<li>Mass-sending the same email to 500 sites</li>
<li>Following up 6 times when ignored</li>
</ul>

<h2>Volume and expectations</h2>

<ul>
<li>Response rate on cold link building: 1-5% (lower than sales)</li>
<li>Of responses, conversion to links: 20-40%</li>
<li>Effective links per 1000 emails: 5-20</li>
</ul>

<p>Math works because each link is durable value. 20 high-quality links from a 1000-email campaign = months of ongoing SEO value.</p>

<h2>Tooling</h2>

<ul>
<li>List building: Ahrefs / Semrush for finding sites linking to competitors</li>
<li>Contact finding: Hunter, Apollo, manual site research</li>
<li>Sending: Pitchbox (specialized), Instantly, Smartlead</li>
<li>Tracking: Ahrefs Site Explorer for seeing which links actually land</li>
</ul>

<h2>The quality rule</h2>

<p>Don't mass-send to low-quality sites. Google penalizes unnatural link patterns. Focus on:</p>
<ul>
<li>Domain Rating / DA 40+</li>
<li>Relevant niche</li>
<li>Real editorial sites (not PBNs or link farms)</li>
<li>Actual traffic (not dead sites)</li>
</ul>

<p>Ten links from DR 60+ sites beats 200 links from DR 10- sites.</p>
""",
    prev=("SDR-led outbound", "sdr-led.html"),
    nxt=("Recruiting outreach", "recruiting.html"),
)


write_cold_page(
    slug="plays/recruiting",
    title="Recruiting outreach",
    description="Cold email for recruiting. Reaching passive candidates with messaging that respects their time.",
    reading_time=4,
    body_html="""
<p class="lede">Recruiting outreach is cold email for talent. Target: passive candidates who aren't actively job hunting but might consider a move for the right opportunity. The playbook is different from sales cold email — different tone, different offer, different cadence.</p>

<h2>The audience</h2>

<ul>
<li>Passive candidates (employed, not searching)</li>
<li>Typically receive 3-20 recruiter InMails per week</li>
<li>Experienced professionals with developed bullshit detectors</li>
<li>Value specificity about the role and company over generic pitch</li>
</ul>

<h2>What works</h2>

<h3>Specificity</h3>
<p>Name the company, role, team, and why this person specifically. Generic "we have an exciting opportunity" emails get deleted instantly.</p>

<h3>Compensation transparency</h3>
<p>Stating comp range in the first email dramatically improves reply rates. Most recruiters dance around it. Candidates hate that.</p>

<h3>Short</h3>
<p>60-100 words. Candidates have no patience for long recruiter pitches.</p>

<h3>Respectful of their time</h3>
<p>Low-friction ask: "Worth a 15-minute chat? If not, no hard feelings."</p>

<h2>The pitch</h2>

<div class="prompt-box">
<div class="prompt-box-label">Recruiting cold email</div>
<button class="copy-btn">Copy</button>
<pre>Subject: [their name or specific detail], not a blast

[first line: specific to their career]

I'm hiring a [role] for [company]. Series B, [city or remote], [comp range: e.g., $180-220K + equity].

Reaching out because of [specific: your work on X at Y, your post on Z, your background in A].

Team is [specific detail: founding engineer + 2 hires, ML team in SF, etc.]. The problem is [one sentence].

Worth a 15-min chat, or not the right fit? Either way, no pressure.

Sam</pre>
</div>

<h2>What kills recruiting emails</h2>

<ul>
<li>"Hope you're having a great week!"</li>
<li>Vague descriptions: "fast-growing startup"</li>
<li>Missing comp range</li>
<li>"Let me know if you'd like to hop on a call"</li>
<li>Blast-style: no reference to their specific background</li>
<li>Generic flattery: "Your profile caught my eye"</li>
</ul>

<h2>Sequence for passive candidates</h2>

<p>Shorter than sales sequences — 3 touches max:</p>

<ul>
<li><strong>Email 1:</strong> The pitch</li>
<li><strong>Email 2 (4-5 days later):</strong> "Adding one more thing: [specific technical or culture detail that matters]. If interested in a call, 2 times: Tue 2pm or Thu 10am."</li>
<li><strong>Email 3 (day 10-12):</strong> Clean breakup. "Closing the loop. If circumstances change, feel free to reach out. My line is open."</li>
</ul>

<p>Longer sequences for passive candidates feel desperate. 3 touches is the sweet spot.</p>

<h2>Volume</h2>

<ul>
<li>Experienced recruiters: 20-60 messages/day targeted</li>
<li>Reply rate on well-targeted: 10-20% (much higher than sales because candidates like to hear about relevant opportunities)</li>
<li>Meetings booked: 2-5 per 50 messages for senior roles</li>
</ul>

<h2>The LinkedIn angle</h2>

<p>LinkedIn InMail is the default channel for recruiting. But email outperforms InMail when you can find the address:</p>
<ul>
<li>Email reply rates typically 1.5-2x InMail</li>
<li>Email feels less recruiter-y</li>
<li>But finding personal emails takes work (Hunter, Apollo, github profiles)</li>
</ul>

<p>Best combo: InMail connection + email for the real pitch.</p>

<h2>Compensation disclosure reality</h2>

<p>In many US states (California, Colorado, Washington, NY state, etc.) it's now required to disclose comp ranges in job posts. Recruiting cold emails should follow the same norm even where not required. Candidates will self-select out if comp is too low, saving everyone's time.</p>

<h2>The handoff</h2>

<p>Once a candidate is interested:</p>
<ul>
<li>First call: hiring manager or founder (for senior roles)</li>
<li>Not handing off to a junior recruiter for the first real conversation</li>
<li>Same principles as founder-led sales: who reached out is who shows up</li>
</ul>

<h2>Common mistakes</h2>

<ul>
<li>Over-recruiting: pitching to people clearly not a fit</li>
<li>Not updating records: multiple recruiters from same company emailing the same candidate</li>
<li>No comp range: candidates filter these out as low-signal</li>
<li>Following up too much: aggressive recruiters damage company brand</li>
</ul>
""",
    prev=("Cold email for SEO", "link-building.html"),
    nxt=None,
)

print("\n✓ Cold Email Part 4: Testing (4) + Playbooks (6) = 10 pages. Cold Email COMPLETE (45 pages).")
