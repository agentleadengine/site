#!/usr/bin/env python3
"""Insurance playbook content — Part 3: Modules 11-15 + Prompt Library."""
from _build_insurance import write_playbook_page


# ============================================================
# MODULE 11 — Newsletter
# ============================================================

m11 = """
<p>A monthly newsletter is the most underrated marketing asset an insurance agent can run. A list of 500 people who opted in to hear from you, getting one email a month, produces more policies than most agents realize. Claude compresses the writing from a 3-hour task to 30 minutes.</p>

<h2>What a good insurance newsletter is (and isn't)</h2>

<p><strong>Is:</strong></p>
<ul>
<li>Short enough to read on a phone in 90 seconds</li>
<li>Personal voice (not "Your Smith Agency Newsletter")</li>
<li>One big thing + a couple short items</li>
<li>Useful or interesting on its own, even without selling</li>
<li>From a real person with a real photo</li>
</ul>

<p><strong>Isn't:</strong></p>
<ul>
<li>A roundup of carrier press releases</li>
<li>"Did you know October is Cybersecurity Awareness Month?"</li>
<li>A pitch for their next policy</li>
<li>Stock-photo-heavy and designed within an inch of its life</li>
<li>Sent from "marketing@agency.com"</li>
</ul>

<h2>The one-big-thing newsletter format</h2>
<p>The format that works: one substantive section + 2-3 quick items. Total 400-600 words. Sent from your personal email-like address (sam@agency.com, not info@).</p>

<div class="prompt-box">
<div class="prompt-box-label">Newsletter: one-big-thing format</div>
<button class="copy-btn">Copy</button>
<pre>Write a monthly newsletter email for my [insurance line] clients.

Audience: my existing clients and warm leads who opted in.
Topic this month: [pick one — a recent event, change, question, or insight]

Structure:
- Subject line: 5-7 words, feels like a personal note
- Open: one sentence that sounds like me writing to a friend
- Main section (250-400 words): the "one big thing" — explain it clearly, use a specific example, end with what it means for them
- "Quick hits" section (3-5 bullets, 1-2 sentences each): small, useful items — a policy deadline, a reminder, a resource, a link
- Close: 1-2 sentences, warm, maybe a personal note about what's going on in my world

Tone: a letter from a knowledgeable friend, not a broadcast. Use "you" a lot. Use "I" or "we" naturally.

Do NOT:
- Sound like a newsletter template
- Include corporate sign-offs ("Warm regards, The [Agency] Team")
- Pitch a specific product unless it's the main topic
- Use stock-photo or graphic-heavy layout (plain text or very simple HTML)

End with my name and a P.S. line that adds a specific small thing.</pre>
</div>

<h2>Topic ideas for every month</h2>

<div class="prompt-box">
<div class="prompt-box-label">12-month topic calendar</div>
<button class="copy-btn">Copy</button>
<pre>Give me a 12-month newsletter topic calendar for an agent focused on [your lines] serving [your audience].

Rules:
- Each month has a primary topic tied to something relevant (season, regulation deadline, life-stage trigger, common question at that time of year)
- Avoid generic "awareness months" unless there's a real reason
- Mix of: educational, seasonal, personal-reflection, practical-reminder

Format:
Month — Primary topic — Why this month — One angle for the main section

Example:
September — Medicare Open Enrollment prep — 30 days out, people start thinking about it — angle: "what to actually review in your current plan before October 15"

Give me 12 months with specific angles, not generic themes.</pre>
</div>

<h2>Repurposing your newsletter</h2>
<p>The newsletter you write for email can be repurposed into a blog post, 3 social posts, and a video script. Don't write once; publish five times.</p>

<div class="prompt-box">
<div class="prompt-box-label">Newsletter-to-multi-channel</div>
<button class="copy-btn">Copy</button>
<pre>Take the newsletter below and produce:

1. A blog post version (800-1200 words — expand on the main section with more depth, add H2s)
2. Three social posts based on the core insight (Facebook, LinkedIn, Instagram caption)
3. A 60-second video script based on the main section

Each version should be adapted to the channel's conventions (short-form for social, scannable for blog, spoken-word for video) — not just copy-pasted.

[Paste your newsletter]</pre>
</div>

<h2>The welcome sequence (new subscribers)</h2>

<div class="prompt-box">
<div class="prompt-box-label">Welcome email sequence</div>
<button class="copy-btn">Copy</button>
<pre>Someone just subscribed to my newsletter (or filled out a lead magnet form). Write a 4-email welcome sequence.

Email 1 (sent immediately): Welcome, what to expect, who I am in 3 sentences, where to find me. Under 150 words.

Email 2 (day 2): One useful thing they can do today related to [my line]. Specific, actionable. Under 200 words.

Email 3 (day 5): A short case study or client story. Anonymized. Shows me in action. Under 250 words.

Email 4 (day 10): A direct but soft ask. "If you want to chat about your specific situation, here's how." Under 150 words. Low pressure.

Each email:
- Sent from me personally, not "the agency"
- Feels like a hand-written note, not a drip
- Signed with my name and one specific detail about me (I live in X, my dog's name is Y, whatever humanizes)</pre>
</div>

<h2>Writing the subject line</h2>

<div class="prompt-box">
<div class="prompt-box-label">Subject line tester</div>
<button class="copy-btn">Copy</button>
<pre>Write 10 subject lines for a newsletter about [topic].

Rules:
- 4-7 words
- Lowercase (feels personal)
- Mix of patterns: question, observation, specific detail, news, promise, personal
- NOT: "October Newsletter," "[Agency Name] October Update," generic teasers
- Match the tone of someone you'd actually want to hear from

Examples of the style I like:
- "a small change for october"
- "Medicare open enrollment: what actually matters"
- "the question every client asks me"

10 options. I'll pick one.</pre>
</div>

<h2>Tools</h2>
<p>A few newsletter platforms work well for insurance agents:</p>
<ul>
<li><strong>ConvertKit / Kit:</strong> built for creators. Good deliverability. $29-49/month for small lists.</li>
<li><strong>MailerLite:</strong> solid free tier, simple.</li>
<li><strong>Beehiiv:</strong> newer, creator-focused, strong free tier.</li>
<li><strong>ActiveCampaign:</strong> more complex, better automation. Overkill for simple newsletters.</li>
<li><strong>Your CRM (HubSpot, Salesforce, AgencyZoom):</strong> often has email built in. Use if it works.</li>
</ul>

<p>Avoid MailChimp and Constant Contact for insurance newsletters — they're dated and deliverability is mediocre.</p>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item">
<input type="checkbox" id="m11-1" data-key="m11-1">
<label for="m11-1">Generate the 12-month topic calendar. Lock in next 3 months.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m11-2" data-key="m11-2">
<label for="m11-2">Write this month's newsletter using the one-big-thing format.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m11-3" data-key="m11-3">
<label for="m11-3">If you don't have a list yet: set up ConvertKit or MailerLite. Add a signup form to your website.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m11-4" data-key="m11-4">
<label for="m11-4">Build the 4-email welcome sequence so new subscribers get warmed up automatically.</label>
</div>
</div>
"""

write_playbook_page(
    slug="module-11",
    title="Newsletter content",
    tag="Module 11",
    subtitle="A monthly email that keeps you top-of-mind for existing clients and prospects. Written in 30 minutes, not 3 hours.",
    body_html=m11,
)


# ============================================================
# MODULE 12 — Ads
# ============================================================

m12 = """
<p>Paid ads are the scale lever when organic and referral aren't producing enough pipeline. Done right, they bring qualified leads at predictable cost. Done wrong, they burn budget and damage your brand. Claude handles the copywriting; your job is to set up tracking and feedback properly. This module: the ad copy prompts that convert and the specifics for Facebook and Google.</p>

<h2>Before you run an ad</h2>
<ul>
<li>Have a tracked phone number (CallRail, CallTrackingMetrics)</li>
<li>Have a landing page (not your homepage) for each ad campaign</li>
<li>Know your target cost per lead by line (roughly $15-60 for Medicare, $25-80 for life, $40-120 for commercial)</li>
<li>Know your allowable cost per closed policy</li>
<li>Set a daily budget you can afford to lose (don't bet the farm on week 1)</li>
</ul>

<h2>Facebook ads — local insurance angle</h2>
<p>Facebook/Meta is still the dominant platform for Medicare, life, and final expense. Older audiences, highly targetable, visual-first.</p>

<div class="prompt-box">
<div class="prompt-box-label">Facebook ad copy — Medicare</div>
<button class="copy-btn">Copy</button>
<pre>Write 5 Facebook ad copy variants for a Medicare prospecting campaign.

Target: 63-68 year olds in [state], pre-Medicare or within first year.
Offer: a 20-minute no-pressure Medicare planning call.
Landing page: [brief description of what prospects see when they click]

Each variant:
- Primary text (90-150 words)
- Headline (25-40 chars)
- Description (30-45 chars)

Vary the hook angle:
1. Question-led (poses the question on their mind)
2. Contrarian (challenges a common belief)
3. Specific-detail-led (a concrete local stat)
4. Story-led (opens with a scenario)
5. Direct-value-led (leads with the specific offer)

CMS compliance requirements — MUST include in each:
- "Not affiliated with any government agency"
- Plan disclaimer appropriate for Medicare lead generation
- No specific plan names, carrier names, or guaranteed benefits
- No "free" or "100% free" unless there is truly no cost and no upsell

Do NOT use:
- Fear-based scare tactics
- "Act now" type urgency without real deadline
- "Limited spots" if there aren't actually limited spots
- Emojis at the start of every line

Keep it warm, local, and honest.</pre>
</div>

<div class="prompt-box">
<div class="prompt-box-label">Facebook ad copy — Life / Final Expense</div>
<button class="copy-btn">Copy</button>
<pre>Write 5 Facebook ad variants for final expense insurance.

Target: 55-75 year olds in [state], concerned about not leaving debt or burial costs to family.
Offer: a 10-minute rate check, no health exam required.

Each variant:
- Primary text (80-130 words)
- Headline
- Description

Hook angles (one per variant):
1. Specific pain: "Funeral costs average $X in [state]..."
2. Protection framing: "Not about you — about not leaving this for your kids"
3. Misconception bust: "Most people think they can't qualify..."
4. Simple process: "Rate in 10 minutes, no medical exam..."
5. Straight offer: "Locked rates for life, here's how to check yours"

Compliance:
- No specific premium quotes (varies by age/health)
- No guarantees about claim outcomes
- No comparison claims ("cheaper than...", "better than...")
- Include "Subject to underwriting" or similar appropriate disclaimer

Keep tone respectful, not morbid or fear-mongering. The audience has thought about this; don't condescend.</pre>
</div>

<div class="prompt-box">
<div class="prompt-box-label">Facebook ad copy — P&amp;C / Home + Auto</div>
<button class="copy-btn">Copy</button>
<pre>Write 5 Facebook ad variants for a home + auto bundle review campaign.

Target: 30-55 year old homeowners in [state/city].
Offer: a 10-minute policy review — send your dec page, we compare to 6 carriers, you see if you can save.

Variants should hit different angles:
1. Rate-increase pain (insurance costs are up everywhere)
2. Coverage gap (most standard policies miss [specific state coverage gap])
3. Time-convenience (10 minutes, email us your dec page)
4. Local angle (I'm in [city], I know [local insurance quirks])
5. Trust signal (X years, Y policies placed)

Each variant:
- Primary text (80-120 words)
- Headline
- Description

Do NOT:
- Claim "lowest rates" or "best coverage"
- Quote specific premiums
- Disparage other carriers by name
- Use urgency that isn't real

Include small trust signal in each (e.g., "Licensed in [state]" or similar).</pre>
</div>

<h2>Google Ads — search intent</h2>
<p>Google Ads work differently: people are searching, not scrolling. Copy is much shorter. Intent is higher.</p>

<div class="prompt-box">
<div class="prompt-box-label">Google Search ad copy</div>
<button class="copy-btn">Copy</button>
<pre>Write Google Search ad copy for [insurance line] in [city/state].

Target keywords: [list 3-5 you're bidding on, e.g., "medicare advisor near me", "life insurance quote [city]", "business insurance [state]"]

For each keyword, give me:
- 3 Responsive Search Ad headlines (30 chars each, each distinct)
- 2 descriptions (90 chars each)
- 1 display path suggestion
- 3 sitelinks that would make sense for this campaign

Headlines should:
- Include the keyword or a close variant
- Mention location where relevant
- Include a benefit or differentiator
- Vary: one question, one benefit-led, one specific-detail

Descriptions should:
- Expand the value proposition
- Include a clear CTA
- Fit the 90-char limit

Do NOT include:
- "Best" (Google disallows superlatives in some categories)
- Specific rates or guarantees
- Carrier-specific claims without authorization</pre>
</div>

<h2>The landing page for your ads</h2>
<p>Never send ad traffic to your homepage. Every campaign gets its own landing page. Claude can write the copy.</p>

<div class="prompt-box">
<div class="prompt-box-label">Landing page copy</div>
<button class="copy-btn">Copy</button>
<pre>Write landing page copy for a [campaign type] ad campaign.

Goal: book a 15-minute call / get a quote / download a resource.

Structure:
- Headline (7-12 words, matches the ad's promise)
- Sub-headline (1 sentence expanding the benefit)
- 3-4 "what you get" bullets
- A short proof section (my credentials or client logos/testimonial)
- The form: fields for name, phone, email, and one qualifying question
- A second CTA below the fold
- A brief FAQ (4-5 questions)
- Trust signals (licensed state, BBB if applicable, years)

Required compliance elements: [specific to the line]
Tone: matches the ad that brought them here.

Length: enough to answer their questions, not so much they bounce.

Include a "What happens next" section: exactly what they can expect after they click the button.</pre>
</div>

<h2>The tracking setup (not optional)</h2>
<p>Ads without tracking are gambling. Minimum setup:</p>

<ul>
<li>Google Analytics 4 on landing page</li>
<li>Meta pixel if running Facebook</li>
<li>Unique call tracking number per campaign</li>
<li>UTM parameters on every ad URL</li>
<li>Conversion tracking configured (form submit, phone call, appointment booked)</li>
</ul>

<p>Without these, you can't tell which ads work. Don't scale blind.</p>

<h2>Iteration: what to test</h2>

<div class="prompt-box">
<div class="prompt-box-label">Test variation generator</div>
<button class="copy-btn">Copy</button>
<pre>My current winning ad is below. Write 5 variations that test different elements:

1. Same body, different headline
2. Same headline, different first 25 words
3. Same copy, new hook angle
4. Same message, different tone (more/less formal)
5. Fresh creative direction entirely

[Paste current ad copy]

Each variation should be structured so I can A/B test against the current winner. Label each with what element it's testing.</pre>
</div>

<h2>Compliance across ad platforms</h2>

<div class="callout warning">
<div class="callout-title">Medicare especially</div>
<p>Meta and Google both have specific requirements for Medicare marketing. CMS requires specific disclaimers. Your IMO or carrier may have an "approved copy" process — use it. Running non-compliant ads can get your ad account shut down or lead to state-level action.</p>
</div>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item">
<input type="checkbox" id="m12-1" data-key="m12-1">
<label for="m12-1">Pick ONE line and ONE campaign objective. Don't run 5 campaigns at once on week 1.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m12-2" data-key="m12-2">
<label for="m12-2">Generate 5 ad copy variants using the appropriate prompt.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m12-3" data-key="m12-3">
<label for="m12-3">Write the landing page copy. Build it in ClickFunnels, Leadpages, Unbounce, Webflow, or your CRM.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m12-4" data-key="m12-4">
<label for="m12-4">Set up tracking (pixel, GA4, call tracking, UTM).</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m12-5" data-key="m12-5">
<label for="m12-5">Submit ad copy for compliance review (carrier/IMO) BEFORE launch.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m12-6" data-key="m12-6">
<label for="m12-6">Start small. $25-50/day. Let it run 7-14 days before judging.</label>
</div>
</div>
"""

write_playbook_page(
    slug="module-12",
    title="Facebook + Google ads",
    tag="Module 12",
    subtitle="Ad copy that converts for Medicare, life, and P&C — plus the tracking and compliance specifics that prevent shut-downs.",
    body_html=m12,
)


# ============================================================
# MODULE 13 — Client education
# ============================================================

m13 = """
<p>The educational materials you hand clients during and after the sale do two jobs: they help the client remember what they bought, and they generate referrals. Most agents hand clients the carrier brochure and hope for the best. Claude can help you produce your own — branded, plain-language, way more useful — in an hour.</p>

<h2>What to build</h2>
<ul>
<li><strong>"Glossary" one-pager:</strong> plain-language definitions of 10-20 terms that come up in your line</li>
<li><strong>"What you actually bought" summary:</strong> a non-jargon recap of the policy you just delivered</li>
<li><strong>Claim filing guide:</strong> step-by-step what to do if something happens</li>
<li><strong>Annual review checklist:</strong> what to think about each year that might change your coverage needs</li>
<li><strong>Life event triggers:</strong> situations that should prompt them to call you</li>
<li><strong>Beneficiary update reminder:</strong> when/why to update beneficiaries</li>
<li><strong>"Explain this to your family" guide:</strong> one-pager the client can hand to a spouse or adult child</li>
</ul>

<h2>The glossary one-pager</h2>

<div class="prompt-box">
<div class="prompt-box-label">Plain-language glossary</div>
<button class="copy-btn">Copy</button>
<pre>Create a 1-page glossary for [insurance line] clients.

Include 12-15 terms that come up most often in conversations with my clients. For each term:
- The term (as they might see it on paperwork)
- 1-2 sentence plain-language definition
- 1 sentence on why it matters to them specifically

No jargon defining jargon. Explain as if to a 65-year-old who's not an insurance professional.

Format the output so I can drop it into a Canva or Word document and brand it.

Topic: [Medicare, Life Insurance, Home Insurance, etc.]</pre>
</div>

<h2>Policy summary ("what you actually bought")</h2>

<div class="prompt-box">
<div class="prompt-box-label">Policy summary one-pager</div>
<button class="copy-btn">Copy</button>
<pre>Write a 1-page "what you actually bought" summary a client can keep.

Client situation (anonymized): [type of policy, general benefit structure — DO NOT include client-specific details with PHI]

Structure:
1. The one-sentence "what this is" (plain language)
2. "What this policy does for you" — 3-4 bullet points
3. "What it does NOT cover" — 3-4 bullet points (so they're not surprised)
4. "What you should do with this" — where to keep it, who to tell about it, when to review
5. "When to call me" — specific triggers (life events, changes in health/job/family)
6. Space for: policy number, carrier, effective date, renewal/review date, my contact info

Tone: clear, respectful, like I'm sitting across the table from them.

Do NOT include specific dollar figures or rates (those should be filled in per client, not in the template).</pre>
</div>

<h2>Claim filing guide</h2>

<div class="prompt-box">
<div class="prompt-box-label">Claim guide</div>
<button class="copy-btn">Copy</button>
<pre>Write a one-page "what to do if you need to file a claim" guide for [insurance line].

Structure:
- "Before anything, take a breath" opener (especially for life insurance / disability / major claims)
- Step 1: What to do immediately
- Step 2: Documents/info you'll need
- Step 3: How to contact the carrier (the process, not specific phone numbers — those go in customization)
- Step 4: How to contact me (I should be in the loop, even if the claim goes direct to carrier)
- What NOT to do (common mistakes that slow down claims)
- Typical timeline for this type of claim
- What to do if the claim is delayed or denied

Plain language throughout. Assume the reader is stressed, maybe grieving. Be human.

Line of business: [specify]</pre>
</div>

<h2>Annual review checklist</h2>

<div class="prompt-box">
<div class="prompt-box-label">Annual review self-checklist</div>
<button class="copy-btn">Copy</button>
<pre>Create a 1-page annual review checklist that a client can use to think about whether their coverage still fits.

For [insurance line], generate 8-12 questions. Each question should:
- Be yes/no or simple fill-in
- Point to a life situation that might trigger a coverage change
- Be written in client language, not insurance language

Examples of what works:
- "Has anyone been added to your household this year?"
- "Did your income change by more than 15%?"
- "Has anyone's health status changed significantly?"
- "Have you bought a new vehicle, home, or major asset?"

Also include:
- At the top: "If you say yes to any of these, let's schedule a 20-minute review call"
- At the bottom: my contact info + scheduling link placeholder

Output in a format I can paste into Canva or Google Docs and brand.</pre>
</div>

<h2>Life event triggers</h2>

<div class="prompt-box">
<div class="prompt-box-label">"Call me when..." card</div>
<button class="copy-btn">Copy</button>
<pre>Write a pocket-card-sized piece of content: "Events that should make you call me before you do anything else."

For [insurance line] clients. 6-10 specific triggers, each one line.

Examples of the right level of specificity:
- "You're about to buy a house"
- "Your kid is turning 26 and going off your plan"
- "You got diagnosed with something new"
- "You're thinking about retiring in the next 2 years"

Not: "When your life situation changes" (too vague)

Format: bullet list, can be printed as a business-card-sized keepsake or refrigerator magnet.</pre>
</div>

<h2>The family handoff</h2>

<div class="prompt-box">
<div class="prompt-box-label">"Give this to your family" one-pager</div>
<button class="copy-btn">Copy</button>
<pre>Write a 1-page document my life insurance or annuity client can give to their adult children or spouse. It's what they need to know if the client passes away or becomes incapacitated.

Structure:
- "What to do first" (notify carrier, contact me, don't panic)
- "Where the documents are" (placeholder for client to fill in)
- "Who to call" (me, carrier claims department)
- "What to bring" (death certificate, policy documents, ID)
- "What NOT to do" (cancel automatic payments, make major changes without professional advice)
- "What happens next" (general overview of the process, typical timeline)
- My contact info section

Tone: calm, respectful, plainspoken. The audience is someone in grief or panic. Make it easy.

Do NOT include specific benefit amounts (those vary by policy and should be filled in per client).</pre>
</div>

<h2>Branding the output</h2>
<p>Claude writes the content. You format and brand it. Tools that work:</p>
<ul>
<li><strong>Canva:</strong> free tier is enough. Templates for one-pagers.</li>
<li><strong>Google Docs:</strong> simpler, less polished, fine for PDF export.</li>
<li><strong>PowerPoint / Keynote:</strong> use a slide as a one-pager format.</li>
<li><strong>InDesign:</strong> if you already have a designer.</li>
</ul>

<p>Save as a PDF, then:</p>
<ul>
<li>Email to clients after each new policy or annual review</li>
<li>Print copies for in-person meetings</li>
<li>Post (with PII placeholders) on your website as free resources</li>
<li>Link from your email signature</li>
</ul>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item">
<input type="checkbox" id="m13-1" data-key="m13-1">
<label for="m13-1">Pick the ONE document that would save you the most time or impress clients most. Generate it.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m13-2" data-key="m13-2">
<label for="m13-2">Design it in Canva or Google Docs. Branded but clean.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m13-3" data-key="m13-3">
<label for="m13-3">Send it to your 10 most recent clients as a "thought you'd find this useful" follow-up.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m13-4" data-key="m13-4">
<label for="m13-4">Add it to your new-client onboarding so every new policy comes with this document.</label>
</div>
</div>
"""

write_playbook_page(
    slug="module-13",
    title="Client education material",
    tag="Module 13",
    subtitle="Glossaries, policy summaries, claim guides, and handoff documents. The stuff that turns clients into advocates.",
    body_html=m13,
)


# ============================================================
# MODULE 14 — The weekly marketing system
# ============================================================

m14 = """
<p>Every module so far is individually useful. The real win is tying them into a weekly rhythm that produces marketing output consistently without you having to decide what to do each day. This is your weekly operating system.</p>

<h2>The 2-hour weekly block</h2>
<p>One 2-hour block per week. Same time every week. Phone off, calendar blocked, door closed. Here's what fits in those 2 hours.</p>

<h3>0:00-0:15 — Reset + review</h3>
<ul>
<li>Review last week's performance: social engagement, email replies, ad metrics, booked meetings</li>
<li>Note what worked and what didn't (one sentence each)</li>
<li>Pull up your content calendar</li>
</ul>

<h3>0:15-0:45 — Create the week's content</h3>
<p>Run one prompt, one asset per week:</p>
<ul>
<li>Week 1: Social posts for the week (Module 5)</li>
<li>Week 2: One blog post (Module 6)</li>
<li>Week 3: One FAQ video batch (Module 7)</li>
<li>Week 4: Monthly newsletter (Module 11)</li>
</ul>

<p>Rotate through the 4-week cycle. End of the month, you have: 28 social posts, 4 blog posts, 4 video batches, 1 newsletter. More content than most agencies produce for clients.</p>

<h3>0:45-1:15 — Prospecting + follow-up</h3>
<ul>
<li>Send this week's prospecting emails (Module 4)</li>
<li>Check reply queue, reply to anyone warm</li>
<li>Update CRM with any new leads, wins, losses</li>
</ul>

<h3>1:15-1:30 — Review responses + referrals</h3>
<ul>
<li>Respond to any new Google/Facebook reviews (Module 10)</li>
<li>Look at the client list: who should I ask for a referral this week? (Module 9)</li>
<li>Send 1-2 warm referral asks or follow-ups</li>
</ul>

<h3>1:30-2:00 — Schedule + publish</h3>
<ul>
<li>Schedule all content through Buffer, Later, Meta Business Suite, or your preferred scheduler</li>
<li>Queue any emails/newsletter in your email tool</li>
<li>Close loop on any ad copy changes or campaign adjustments</li>
</ul>

<p>Done. Two hours, marketing for the week is out.</p>

<h2>The monthly block (additional 1 hour)</h2>
<p>Once a month, add one hour for bigger-picture work:</p>

<ul>
<li>Review ad performance and adjust budget/copy (Module 12)</li>
<li>Pick next month's newsletter topic (Module 11)</li>
<li>Refresh any landing pages or lead magnets</li>
<li>Check in with 1-2 referral partners (Module 9)</li>
<li>Write one client education document (Module 13) and add to onboarding</li>
</ul>

<h2>The quarterly block (additional 2 hours)</h2>
<ul>
<li>Full content audit: what's working, what isn't, what to cut</li>
<li>Update your Claude context and voice samples with new examples</li>
<li>Review compliance approvals, update templates</li>
<li>Set quarterly goals for lead flow and conversion</li>
<li>Read the top 3 pieces of content in your space — what's changed, what's new</li>
</ul>

<h2>The prompts that run your week</h2>

<div class="prompt-box">
<div class="prompt-box-label">Monday marketing review</div>
<button class="copy-btn">Copy</button>
<pre>I'm doing my weekly marketing planning. Here's what happened last week:

- Social engagement: [briefly describe what posts did well/poorly]
- Email replies: [number, any notable ones]
- Ads: [spend, leads, cost per lead if running]
- Meetings booked: [number, source]
- Pipeline activity: [relevant notes]

Based on this:
1. What should I double down on this week?
2. What should I stop or change?
3. Suggest 3 specific experiments to run this week.
4. What's the single highest-leverage thing I can do with my marketing time this week?

Keep it practical. I have 2 hours.</pre>
</div>

<div class="prompt-box">
<div class="prompt-box-label">Content calendar builder</div>
<button class="copy-btn">Copy</button>
<pre>Build a content calendar for me for the next 30 days.

My line: [from context]
Audience: [from context]
This month's focus: [pick one theme]

Output a calendar with:
- 4 newsletter-quality "big ideas" (one per week) that become the hub content
- 4 blog post titles tied to those big ideas
- 16 social posts (4/week) that support or tease the big ideas
- 4 video scripts (1/week)
- 2 prospecting email angles

Format as a table with columns: Date, Channel, Title/Topic, Status (draft/scheduled/published).

Include any time-sensitive topics (e.g., open enrollment, tax season, end of year) for this month.</pre>
</div>

<h2>The honest truth about consistency</h2>
<p>Most agents start marketing systems and abandon them within 3 weeks. The playbook doesn't fail; the rhythm fails. Keep the rhythm simple enough that you'll do it even on a bad week:</p>

<ul>
<li>Same day, same time each week (Monday 8am, whatever works)</li>
<li>Phone off, door closed, calendar blocked</li>
<li>Even if you don't feel it, you sit down and run the prompts</li>
<li>Even a bad output is better than no output</li>
</ul>

<p>Month 1 is messy. Month 2 feels natural. Month 3 you have a content machine. Month 6 you can look back at a real library of work.</p>

<h2>Sustainability check</h2>
<p>If you're trying to do all 15 modules every week, you'll burn out in a month. The goal is compound output over quarters, not heroics. A realistic cadence:</p>

<ul>
<li><strong>Weekly:</strong> social posts, 1 blog post OR video batch, prospecting emails, review responses</li>
<li><strong>Biweekly:</strong> referral asks, ad copy refreshes</li>
<li><strong>Monthly:</strong> newsletter, client education doc, referral partner check-ins</li>
<li><strong>Quarterly:</strong> full audit, goal reset</li>
</ul>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item">
<input type="checkbox" id="m14-1" data-key="m14-1">
<label for="m14-1">Block the 2-hour weekly marketing time on your calendar. Recurring. Next 12 weeks minimum.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m14-2" data-key="m14-2">
<label for="m14-2">Run your first "Monday marketing review" prompt to plan this week.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m14-3" data-key="m14-3">
<label for="m14-3">Build the 30-day content calendar using the prompt above.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m14-4" data-key="m14-4">
<label for="m14-4">Pick 1 metric you'll track weekly (booked meetings from marketing is the most useful).</label>
</div>
</div>
"""

write_playbook_page(
    slug="module-14",
    title="The weekly marketing system",
    tag="Module 14",
    subtitle="A 2-hour weekly rhythm that produces a month of marketing output. The operating system that ties every previous module together.",
    body_html=m14,
)


# ============================================================
# MODULE 15 — Compliance
# ============================================================

m15 = """
<p>Everything in this playbook is worthless if your marketing lands you in front of your state DOI, CMS, or carrier compliance. Claude speeds up creation, which means it also speeds up mistakes if you're not careful. This module: the compliance discipline to run alongside every other module.</p>

<h2>Who regulates what</h2>

<ul>
<li><strong>State Department of Insurance (DOI):</strong> every state has its own rules on life and P&amp;C marketing. Your state's rules are available on your DOI's website.</li>
<li><strong>NAIC Model Regulations:</strong> national templates that states adopt with variations. Useful baseline but not state-specific.</li>
<li><strong>CMS (Medicare):</strong> federal rules for all Medicare marketing. Updated annually. The most restrictive.</li>
<li><strong>FINRA:</strong> if you sell variable products, annuities, or anything registered.</li>
<li><strong>Your carrier/IMO/FMO compliance desk:</strong> most have an "approved copy" process. USE IT.</li>
<li><strong>Social media platform rules:</strong> Meta and Google have their own ad policies on insurance.</li>
</ul>

<h2>The universal red flags across all lines</h2>

<ul>
<li>Superlatives you can't prove: "best," "cheapest," "lowest," "top-rated"</li>
<li>Guaranteed outcomes: "guaranteed to save," "never lose money"</li>
<li>Comparison claims naming competitors negatively</li>
<li>Specific rates or premiums without massive disclaimers</li>
<li>Claims about specific benefits that vary by policy</li>
<li>Medical claims about products that aren't medically evaluated (including "boost your immunity")</li>
<li>Urgency that isn't real ("act now!" with no actual deadline)</li>
<li>Fear-based tactics about death, illness, losing family</li>
<li>Statistics without citation</li>
<li>Testimonials without proper disclaimers (some states prohibit testimonials altogether)</li>
</ul>

<h2>Medicare-specific compliance (CMS rules)</h2>

<div class="callout warning">
<div class="callout-title">Always required in Medicare marketing</div>
<p>"Not affiliated with any government agency" or equivalent, "We do not offer every plan available in your area" disclaimer, Medicare.gov / 1-800-MEDICARE reference, TTY number for hearing-impaired where applicable. CMS updates requirements annually — check current year's guidance.</p>
</div>

<h3>Medicare-specific don'ts</h3>
<ul>
<li>Don't use "Medicare" in your business name without proper clearance</li>
<li>Don't imply endorsement by the government</li>
<li>Don't offer gifts over $15 (2025 rule, check current)</li>
<li>Don't make cold calls to potential Medicare beneficiaries without a Scope of Appointment</li>
<li>Don't use prohibited terms like "free" when there's a condition, or superlatives</li>
<li>Don't reference specific plans in lead-generation marketing (different rules for marketing specific plans)</li>
</ul>

<h2>Life and annuity specific</h2>

<div class="callout warning">
<div class="callout-title">Life/annuity red flags</div>
<p>Guaranteed returns (especially on IUL, variable), past-performance claims, missing surrender charge disclosures, replacement activity without proper forms, suitability issues, gender or race-based pricing language.</p>
</div>

<h2>Property and casualty specific</h2>
<ul>
<li>No claims of lowest rate without evidence</li>
<li>No implied endorsement by carrier</li>
<li>Rate quotes: always subject to underwriting, binding</li>
<li>State-specific required disclosures (differs widely — Texas has windstorm specific language, Florida has hurricane specific, etc.)</li>
</ul>

<h2>The pre-publish checklist</h2>

<div class="checklist">
<div class="checklist-item">
<input type="checkbox" id="m15-1" data-key="m15-1">
<label for="m15-1">Ran the compliance pre-check prompt (Pattern 10 in Module 3)</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m15-2" data-key="m15-2">
<label for="m15-2">Searched the content for: "best," "cheapest," "lowest," "guaranteed," "always," "never"</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m15-3" data-key="m15-3">
<label for="m15-3">Every specific number or stat has a defensible source</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m15-4" data-key="m15-4">
<label for="m15-4">Required disclaimers are present and readable (not buried)</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m15-5" data-key="m15-5">
<label for="m15-5">Name, license, state(s) licensed visible on the piece</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m15-6" data-key="m15-6">
<label for="m15-6">For carrier-branded pieces: submitted to carrier compliance desk</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m15-7" data-key="m15-7">
<label for="m15-7">For Medicare: all CMS-required disclaimers included</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m15-8" data-key="m15-8">
<label for="m15-8">No PHI or client-specific health information (even with name changed)</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m15-9" data-key="m15-9">
<label for="m15-9">No testimonial that violates state rules (some states prohibit entirely)</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m15-10" data-key="m15-10">
<label for="m15-10">Keep a copy and the approval trail for 3+ years (some states require longer)</label>
</div>
</div>

<h2>The "red phrase" scanner prompt</h2>

<div class="prompt-box">
<div class="prompt-box-label">Red phrase scanner</div>
<button class="copy-btn">Copy</button>
<pre>Scan the copy below for compliance red flags specific to [insurance line].

Flag every instance of:
- Superlatives (best, cheapest, lowest, top-rated, guaranteed)
- Specific numeric claims (rates, savings percentages, returns)
- Competitor comparisons by name
- Urgency claims ("act now", "limited time", "only X left") — note whether real
- Missing required disclaimers for this line
- Implied endorsements (government, carrier, professional body)
- Claims about products varying by policy (coverage amounts, premiums, benefits)
- Fear-based language

For each flag, suggest a compliant rewrite.

Then give me the compliance-cleaned version of the whole piece.

Line: [specify]
Jurisdiction: [state(s)]

[Paste copy]</pre>
</div>

<h2>Record-keeping</h2>
<p>Most states require keeping marketing materials for 3-5 years. Set up a simple folder structure:</p>

<ul>
<li>/Marketing Archive /2026 /[Month] — drop every published piece here</li>
<li>Include the carrier/compliance approval email for anything reviewed</li>
<li>Include dates published and where</li>
</ul>

<p>If a state DOI ever asks, you have the trail.</p>

<h2>When in doubt, ask</h2>
<p>Claude cannot replace your compliance desk, your carrier's review process, or your own licensed judgment. When a piece feels edgy, it probably is. When it feels fine but you're not sure — run it by compliance. The 2 days of delay is always worth it.</p>

<div class="callout">
<div class="callout-title">The rule</div>
<p>If you wouldn't want a state DOI examiner, your carrier's compliance officer, and a skeptical prospect all reading this piece — rewrite it until you would.</p>
</div>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item">
<input type="checkbox" id="m15-task-1" data-key="m15-task-1">
<label for="m15-task-1">Bookmark your state DOI's marketing/advertising rules page. Actually read it once.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m15-task-2" data-key="m15-task-2">
<label for="m15-task-2">Identify who at your carrier or IMO reviews marketing copy. Establish the channel.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m15-task-3" data-key="m15-task-3">
<label for="m15-task-3">Print the pre-publish checklist. Run every piece through it before it goes out.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m15-task-4" data-key="m15-task-4">
<label for="m15-task-4">Set up the marketing archive folder structure.</label>
</div>
</div>
"""

write_playbook_page(
    slug="module-15",
    title="Compliance checklist",
    tag="Module 15",
    subtitle="The compliance discipline that runs alongside everything else. Specific rules for Medicare, life, P&C, and the universal red flags to scan for.",
    body_html=m15,
)


# ============================================================
# PROMPT LIBRARY — searchable index
# ============================================================

PROMPTS = [
    {"id": "p1", "title": "Agent context template", "module": "Module 2", "tags": ["setup", "all-lines"],
     "desc": "The one-page context you paste at the start of every Claude conversation. Foundational.",
     "prompt": """You are my marketing associate. Before you write anything, here's the context.

ABOUT ME:
- Name: [Your name]
- Agency: [Your agency name]
- State(s) licensed: [State abbreviations]
- Lines I sell: [e.g., Life, Medicare Supplement, Medicare Advantage, Final Expense, Indexed Universal Life]

MY IDEAL CLIENT:
- Age range: [e.g., 55-70]
- Life stage: [e.g., pre-retirement]
- Key concerns: [what keeps them up at night]

MY VOICE:
- Tone: [warm but direct, no jargon]
- Phrases I use: [list 3-5]
- Phrases I avoid: [list]

COMPLIANCE:
- Do NOT: mention specific premiums, guarantee returns, use superlatives.

Ready?"""},
    {"id": "p2", "title": "Voice sample primer", "module": "Module 2", "tags": ["setup", "voice", "all-lines"],
     "desc": "Paste this before any 'write for me' prompt to match your actual voice.",
     "prompt": """Before you write anything for me, here are three examples of how I actually talk.

SAMPLE 1 (email):
[Paste 200-400 words]

SAMPLE 2 (social post):
[Paste post]

SAMPLE 3 (voicemail):
[Paste]

When you write, sound like this. Don't smooth it out. Match me."""},
    {"id": "p3", "title": "The Briefed Writer", "module": "Module 3", "tags": ["patterns", "all-lines"],
     "desc": "The foundation prompt for any writing task.",
     "prompt": """Write [asset type] for [audience] about [topic].

Goal: [what you want the reader to do]
Tone: [from voice samples]
Length: [word count]
Must include: [specific points]
Must NOT include: [forbidden claims]

Output just the copy."""},
    {"id": "p4", "title": "Angle Generator (10 angles)", "module": "Module 3", "tags": ["patterns", "ideation", "all-lines"],
     "desc": "Before writing anything, generate 10 distinct angles and pick one.",
     "prompt": """I'm writing [asset type] about [topic] for [audience].

Give me 10 different angles. Each should be:
- A one-sentence hook
- A specific promise
- Distinct from the others

I'll pick one and we'll write from there."""},
    {"id": "p5", "title": "The Rewrite", "module": "Module 3", "tags": ["patterns", "editing", "all-lines"],
     "desc": "Turn rough drafts, voicemails, or carrier material into polished copy in your voice.",
     "prompt": """Rewrite the text below so it's:
- Clearer to a [audience]
- Shorter by [%]
- In my voice
- Jargon-free

Preserve substance. Don't add claims I didn't make.

[Paste source]"""},
    {"id": "p6", "title": "The Multi-Version", "module": "Module 3", "tags": ["patterns", "repurposing", "all-lines"],
     "desc": "One idea, multiple channels. Fastest way to get a week of content from one insight.",
     "prompt": """Take this core idea: [idea]

Give me versions for:
1. 150-word Facebook post
2. 250-word LinkedIn post
3. 60-second video script
4. 50-word SMS
5. Blog post intro
6. 3-line voicemail script

Match each channel's conventions."""},
    {"id": "p7", "title": "The Counter-Draft", "module": "Module 3", "tags": ["patterns", "editing", "all-lines"],
     "desc": "Take a bland first draft and push it with three alternative takes.",
     "prompt": """Here's the draft: [paste]

Write 3 alternative versions:

Version A: More specific. Replace abstract claims with numbers/scenes.
Version B: Opens with a story. First 50 words = a scene.
Version C: Contrarian. Challenges a common belief in my space.

Don't soften. I want choices."""},
    {"id": "p8", "title": "The Critic", "module": "Module 3", "tags": ["patterns", "review", "all-lines"],
     "desc": "Have Claude review copy as three skeptical personas before you publish.",
     "prompt": """Read the copy as:
1. A skeptical 65-year-old prospect
2. A compliance officer
3. A cynical marketer

For each, list 3 things that would make them stop, push back, or flag. Be blunt.

[Paste copy]"""},
    {"id": "p9", "title": "The Persona Interview", "module": "Module 3", "tags": ["patterns", "research", "all-lines"],
     "desc": "Roleplay your ideal client and surface their real worries in their own words.",
     "prompt": """Roleplay as [ideal client persona].

Details:
- [Age, family, income, location]
- [What they're thinking this week]
- [Prior experience with agents]

I'll interview you about [topic]. Answer in first person with specific worries. Be specific.

First question: [your question]"""},
    {"id": "p10", "title": "The Specific Translator", "module": "Module 3", "tags": ["patterns", "editing", "all-lines"],
     "desc": "Force every vague claim in a piece to become specific and defensible.",
     "prompt": """Every vague claim in the copy below, replace with a specific number, name, time, or example.

If I can't back a specific claim, flag it and suggest a safer specific.

[Paste copy]"""},
    {"id": "p11", "title": "The Hook Farm", "module": "Module 3", "tags": ["patterns", "ideation", "all-lines"],
     "desc": "Generate 10 hooks for any piece, pick the best.",
     "prompt": """Topic: [idea]
Audience: [who]
Format: [FB post / blog intro / email subject]

Give me 10 hooks. Just first 15 words. Different patterns:
- Contrarian
- Specific number
- Question
- Confession
- News hook
- Warning
- Specific character
- Unusual observation
- Reframe
- Direct pain address

No explanations."""},
    {"id": "p12", "title": "The Compliance Pre-Check", "module": "Module 3", "tags": ["patterns", "compliance", "all-lines"],
     "desc": "Scan any piece for common insurance compliance red flags before you publish.",
     "prompt": """Review for compliance issues for [insurance line].

Flag:
- Superlatives ("best," "cheapest")
- Guaranteed returns in life/annuity
- Medicare: CMS-prohibited terms
- Claims about competitors
- Rate specifics
- Fear-based language
- Missing disclosures

List flags with fixes. Then give revised version.

[Paste copy]"""},
    {"id": "p13", "title": "Life prospecting email (homeowner parent)", "module": "Module 4", "tags": ["email", "life", "prospecting"],
     "desc": "Cold prospecting email to homeowners 45-60 with a trigger event.",
     "prompt": """Write a cold prospecting email to a homeowner, age 45-60, in [state]. Trigger: [had a kid / turned 50 / bought a home].

Goal: book a 15-min discovery call.
- Under 90 words
- Subject: 4-6 words, lowercase
- Reference trigger specifically
- Offer one specific angle
- Defensible proof point
- Specific CTA time
- Signature: name, state, phone

No "I hope this finds you well" / "I wanted to reach out."

Write 3 versions."""},
    {"id": "p14", "title": "Medicare T-65 prospecting email", "module": "Module 4", "tags": ["email", "medicare", "prospecting"],
     "desc": "Cold email to someone turning 65 in 90 days, CMS-compliant.",
     "prompt": """Write a prospecting email to someone turning 65 in 90 days in [state].

Goal: book 20-min Medicare call.
- Subject: 3-5 words, personal
- Acknowledge they've been getting Medicare mail
- Promise: you don't push one carrier, explain tradeoffs
- Include local market detail
- Propose 2 specific times
- Under 100 words

CMS compliance:
- No specific plan names
- Include "We do not offer every plan available in your area..."
- "Not affiliated with Medicare or any government agency"

3 variants."""},
    {"id": "p15", "title": "Small-group health email", "module": "Module 4", "tags": ["email", "health", "prospecting", "commercial"],
     "desc": "Cold email to a small business owner about rising health premiums at renewal.",
     "prompt": """Write a prospecting email to a small business owner (10-50 employees) in [state].

Pain: rising health premium at renewal.
Goal: book 20-min review call.

- Subject: 5-7 words about renewal/rising costs
- Open with [state] small-group premium trend
- Three levers (plan design, carrier shop, ICHRA/QSEHRA)
- Propose no-pressure 20-min review
- Under 100 words

3 versions: casual, data-driven, story-led."""},
    {"id": "p16", "title": "P&C homeowner email", "module": "Module 4", "tags": ["email", "pnc", "prospecting"],
     "desc": "Cold email to a new homeowner for home + auto bundle review.",
     "prompt": """Write a prospecting email to a new homeowner (bought in last 6 months) in [state].

Goal: quote home+auto bundle.
- Subject: 4-5 words about new home
- Acknowledge move (not creepy)
- One [state] coverage gap most policies miss
- Offer 10-min quote with their dec page
- Under 80 words

3 variants."""},
    {"id": "p17", "title": "Commercial vertical email", "module": "Module 4", "tags": ["email", "commercial", "prospecting"],
     "desc": "Cold email to a commercial vertical (restaurant, contractor, medical) before renewal.",
     "prompt": """Write a prospecting email to a [restaurant/contractor/medical practice/trucking] owner in [state]. Renewal in [month].

Goal: book 15-min call 60-90 days pre-renewal.

- Subject: vertical-specific, 5-7 words
- First line: vertical-common coverage gap
- Position as specialist
- Acknowledge current broker may be fine
- Specific CTA week
- Under 120 words

Professional tone. No disparagement."""},
    {"id": "p18", "title": "5-touch follow-up sequence", "module": "Module 4", "tags": ["email", "sequence", "prospecting", "all-lines"],
     "desc": "Generate the full 5-email sequence from your first prospecting email.",
     "prompt": """Given this first email [paste], write a 5-touch sequence:

- Email 2 (day 3): short nudge, new angle, under 50 words
- Email 3 (day 7): soft reframe, lower-friction ask
- Email 4 (day 12): case study, anonymized, under 100 words
- Email 5 (day 20): breakup, closing loop, under 40 words

Same tone. Vary openings."""},
    {"id": "p19", "title": "Personalized first line generator", "module": "Module 4", "tags": ["email", "personalization", "prospecting"],
     "desc": "Generate custom first lines for 20+ prospects at once.",
     "prompt": """For each prospect, write ONE first line of a cold email (12-20 words) that references something specific and doesn't sound templated.

Avoid:
- "Hope you're well"
- "I came across your profile"
- Generic congrats

PROSPECTS:
1. [Name, situation, trigger]
2. [Name, situation, trigger]
..."""},
    {"id": "p20", "title": "Weekly social content generator", "module": "Module 5", "tags": ["social", "content", "all-lines"],
     "desc": "Generate 7 social posts with the right educational-to-pitch mix.",
     "prompt": """Generate 7 posts for this week:
- 4 educational
- 1 personal
- 1 social proof
- 1 direct ask

Platform: [FB/LinkedIn]
Audience: [from context]
Theme: [one theme]

Each 80-180 words. Hook in first line. Plain language. End with question or CTA. Vary openings.

Number with day-of-week."""},
    {"id": "p21", "title": "Common mistake post", "module": "Module 5", "tags": ["social", "content", "all-lines"],
     "desc": "\"Most people think X. It's actually Y.\" — one of the highest-engagement post patterns.",
     "prompt": """Write a "common mistake" FB post about [topic].

- Line 1: hook stating the mistake
- Lines 2-4: why most people believe it
- Lines 5-8: the actual truth
- Last line: what to do instead

130 words max. End with "Reply or DM with questions."""},
    {"id": "p22", "title": "Specific scenario post (LinkedIn)", "module": "Module 5", "tags": ["social", "linkedin", "all-lines"],
     "desc": "Anonymized client scenario that shows expertise and makes readers see themselves.",
     "prompt": """Write a LinkedIn post about an anonymized client scenario in [line].

- Line 1: "Had a call this week with [generic description]..."
- 3-4 sentences: situation and hidden problem
- 2-3 sentences: what we figured out
- Last line: broader lesson

180 words max. First person."""},
    {"id": "p23", "title": "LinkedIn insight post (long form)", "module": "Module 5", "tags": ["social", "linkedin", "all-lines"],
     "desc": "300-500 word thoughtful LinkedIn post when you have a real insight.",
     "prompt": """Write a LinkedIn post (300-500 words) about [topic].

- Hook line
- Context (2-3 sentences)
- Insight (3-5 short paragraphs)
- Named concrete example
- What it means for reader
- Question or CTA

Short paragraphs. Practitioner tone, not thought-leadership."""},
    {"id": "p24", "title": "One-to-many repurposer", "module": "Module 5", "tags": ["social", "repurposing", "all-lines"],
     "desc": "Take one insight and turn it into 7 different pieces of content across channels.",
     "prompt": """Core insight: [insight]

Turn into:
1. FB post (120w, warm)
2. LinkedIn post (300w, pro)
3. Newsletter section (200w)
4. 60s video script
5. 40s reel/TikTok script
6. Tweet (240 chars)
7. Text to prospect (60w)

Adapt structure to each channel."""},
    {"id": "p25", "title": "Keyword + question generator", "module": "Module 6", "tags": ["blog", "seo", "all-lines"],
     "desc": "30 search queries real prospects type before they call. Your blog topic bank.",
     "prompt": """I sell [line] to [audience] in [geo].

Generate 30 search queries:
- 10 question queries
- 10 local-intent
- 5 comparison
- 5 problem

Group by intent. For each group, suggest 3 blog titles."""},
    {"id": "p26", "title": "Blog post outline", "module": "Module 6", "tags": ["blog", "seo", "all-lines"],
     "desc": "Detailed outline with H2/H3s before you write the full post.",
     "prompt": """Outline for blog post titled "[title]".

Audience: [specific]
Intent: [info/comparison/transactional]
Primary keyword: [phrase]
Secondary keywords: [3-5]

- H1
- Intro (2 paragraphs)
- 4-6 H2s, each with 2-3 H3s
- Conclusion with CTA

Flag places to add local data or personal examples. Anticipate 3 objections."""},
    {"id": "p27", "title": "Blog post writer (from outline)", "module": "Module 6", "tags": ["blog", "seo", "all-lines"],
     "desc": "Write the full 1200-1800 word post from your approved outline.",
     "prompt": """Using the outline above, write the full post.

Length: 1200-1800 words
Voice: [from samples]
- Short paragraphs
- H2/H3 structure
- Bullet lists for comparisons
- Bold 1 sentence per section
- 1+ concrete example
- Clear CTA

Avoid "in today's fast-paced world," "however/furthermore/moreover" paragraph starts.

Flag places I need to add local data or examples, and any stats to verify."""},
    {"id": "p28", "title": "Meta title + description", "module": "Module 6", "tags": ["blog", "seo", "all-lines"],
     "desc": "Three title and description options for SEO.",
     "prompt": """For the post below:
1. Title tag (55-60 chars, keyword near front)
2. Meta description (140-160 chars)
3. 5 URL slug options

Give 3 options for each.

[Paste post]"""},
    {"id": "p29", "title": "Local content angle finder", "module": "Module 6", "tags": ["blog", "seo", "local", "all-lines"],
     "desc": "10 blog ideas that tie your topic to your specific city/state.",
     "prompt": """I serve [geography]. Base topic: [topic].

10 blog ideas that would rank for "[topic] + [location]".

Each:
- Title
- Primary local keyword
- Why it wins locally"""},
    {"id": "p30", "title": "Content cluster builder", "module": "Module 6", "tags": ["blog", "seo", "all-lines"],
     "desc": "Pillar + 8 supporting posts with an internal link plan.",
     "prompt": """Build a cluster around "[broad topic]".

- 1 pillar post + description
- 8 supporting posts
- For each, which pillar sections it links TO

Topic: [topic]
Audience: [audience]"""},
    {"id": "p31", "title": "Explainer video script (60-90s)", "module": "Module 7", "tags": ["video", "all-lines"],
     "desc": "One-concept video script with timestamps and B-roll cues.",
     "prompt": """Write a 60-90s video script for me (licensed [line] in [state]).

Topic: [topic]

Timestamps:
[0-5s] Hook
[5-15s] Problem
[15-50s] 2-3 key points
[50-75s] What it means for viewer
[75-90s] Soft CTA

First person, short sentences, no jargon. Include B-roll suggestions and on-screen text."""},
    {"id": "p32", "title": "FAQ shorts (10 scripts)", "module": "Module 7", "tags": ["video", "shorts", "all-lines"],
     "desc": "10 ready-to-shoot short video scripts for Reels/TikTok/Shorts.",
     "prompt": """Give me 10 FAQ-style short video scripts.

Each 30-60s (70-140 words). Hook in first 3 seconds. Plain-language answer. One concrete example. Close with "Follow for more / DM if this applies."

Topic pool: [line]
Styles: "Can I get coverage if..." "What's the difference between..." "How much do I really need..."

Number 1-10. Shootable as-is."""},
    {"id": "p33", "title": "Personal intro video (90s)", "module": "Module 7", "tags": ["video", "branding", "all-lines"],
     "desc": "Your \"about\" video for website, email signature, LinkedIn.",
     "prompt": """Write a 90s personal intro video script.

[0-10s] Who I am / what I do
[10-25s] Specific type of client
[25-50s] Why I do this (specific moment)
[50-75s] How I work differently
[75-90s] How to connect

Warm, not corny. Contractions. Short sentences. No "committed to providing excellent..."."""},
    {"id": "p34", "title": "Case study video (2-3min)", "module": "Module 7", "tags": ["video", "case-study", "all-lines"],
     "desc": "Anonymized client story in video form.",
     "prompt": """Write a 2-3 min anonymized client story video.

Situation: [describe]

[0-15s] Problem in one sentence
[15-45s] Who they were
[45-90s] What they'd tried
[90-150s] What we figured out
[150-180s] Realistic outcome

No identifying details. Add disclaimer at end."""},
    {"id": "p35", "title": "Personalized prospect Loom", "module": "Module 7", "tags": ["video", "prospecting", "all-lines"],
     "desc": "90-second personalized video for one specific prospect. High reply rates.",
     "prompt": """5-bullet structure for a 90s Loom to a prospect.

Prospect: [name, role, situation, trigger]

1. Name + specific detail (5s)
2. What made me reach out (15s)
3. The thing they might not have considered (30s)
4. Offer to be useful (not pitch, 20s)
5. Specific next step (15s)

Also: 6-line email with video embedded."""},
    {"id": "p36", "title": "Caption generator", "module": "Module 7", "tags": ["video", "all-lines"],
     "desc": "Convert a script into frame-by-frame captions for social video.",
     "prompt": """Format the script as captions.

- Each chunk: 3-6 words, one per frame
- Punctuation sparingly
- Match speaking rhythm
- Separate with "|"

[Paste script]"""},
    {"id": "p37", "title": "Medicare T-65 postcard copy", "module": "Module 8", "tags": ["direct-mail", "medicare"],
     "desc": "6x11 postcard for Medicare T-65 with CMS-required disclaimers.",
     "prompt": """Write copy for 6x11 postcard to Medicare T-65 prospects in [state/county].

Front: 1 headline + supporting line. Under 15 words.

Back:
1. Acknowledge tons of Medicare mail
2. Problem with most of it
3. What's different about me
4. Local detail
5. Offer: 20-min no-pressure call
6. CTA: tracked phone + URL

CMS compliance:
- "We do not offer every plan available in your area..."
- "Not affiliated with Medicare or any government agency."

Mail-from-a-person tone."""},
    {"id": "p38", "title": "1-page sales letter", "module": "Module 8", "tags": ["direct-mail", "all-lines"],
     "desc": "Classical direct-response sales letter format for any line.",
     "prompt": """Write 1-page sales letter for [line] to [audience].

- Date + "Dear [Name]"
- Opening: specific observation
- Story: anonymized similar person
- Offer: what I want to do
- Proof: 2-3 defensible facts
- Urgency: real reason for now
- CTA
- P.S.: restate offer + reason to act

250-400 words. Neighbor letter tone.

Include [line]-appropriate disclaimers."""},
    {"id": "p39", "title": "Envelope teaser copy", "module": "Module 8", "tags": ["direct-mail", "all-lines"],
     "desc": "5 envelope teasers that survive the first-pass mail sort.",
     "prompt": """5 teasers for front of #10 envelope for [audience] about [topic].

Each:
- Under 10 words
- Looks like personal mail, not ad
- Curiosity without clickbait
- Defensible

Examples I like:
- "A note about your Medicare options"
- "Regarding your October renewal"

5 distinct angles."""},
    {"id": "p40", "title": "Trackable CTA variants", "module": "Module 8", "tags": ["direct-mail", "all-lines"],
     "desc": "Five different trackable CTAs for direct mail.",
     "prompt": """5 CTAs for direct mail, different framings:

1. Call now (urgency)
2. Request the [resource] (lead magnet)
3. Get your personalized [thing] (benefit)
4. Reply card (BRE)
5. Visit [URL], answer 3 questions

Each: phone placeholder + URL placeholder. Neighborly tone."""},
    {"id": "p41", "title": "Verbal referral ask", "module": "Module 9", "tags": ["referral", "all-lines"],
     "desc": "4-5 sentence referral ask to use verbally after a positive interaction.",
     "prompt": """Write a 4-5 sentence verbal referral ask for after [positive client moment].

I help [specific niche].

Ask:
- Gratitude for current moment (specific)
- Name exactly type of person I help
- Specific person/situation to think of
- Make handoff easy (I reach out, not them)
- Natural, not scripted

2 versions."""},
    {"id": "p42", "title": "Warm intro email to client", "module": "Module 9", "tags": ["referral", "email", "all-lines"],
     "desc": "After a client gives you a name, this is the forward-able intro.",
     "prompt": """My client [Client] said I could reach out to [Prospect], their [relationship].

Write email to [Client]:

Section 1 (to client):
- Thank again
- I'll reach out in 1-2 days
- Offer forward-able intro

Section 2 (for them to forward):
- From them to friend
- Why they thought of them
- Intro me in 1 sentence
- Suggest 15-min chat

Under 200 words."""},
    {"id": "p43", "title": "Warm intro to referred prospect", "module": "Module 9", "tags": ["referral", "email", "all-lines"],
     "desc": "The email to the person who was referred to you.",
     "prompt": """Email to [Prospect] referred by [Referring Client] about [topic].

- Subject: mention referrer's name
- First line: referrer + specific reason
- 2-3 sentences: what I do
- 1-2 sentences: no pressure, just hi
- Soft CTA: 15-min call, 2 specific times

80-120 words. Warm, casual."""},
    {"id": "p44", "title": "Handwritten thank-you to referrer", "module": "Module 9", "tags": ["referral", "all-lines"],
     "desc": "Short thank-you note to send on actual paper to a client who referred.",
     "prompt": """6-10 sentence handwritten-style thank you.

- Specific thank for referral
- One line about connection
- Reference specific about client
- Note meeting with [Prospect] went well
- No incentives
- Warm close

Personal, not corporate."""},
    {"id": "p45", "title": "Referral partner outreach", "module": "Module 9", "tags": ["referral", "email", "partner", "all-lines"],
     "desc": "Peer-to-peer email to CPA, estate attorney, realtor, etc.",
     "prompt": """Email to [CPA/attorney/realtor/HR consultant] in my market. Goal: referral relationship.

- Subject: about them, not me
- Open: specific detail about their work
- Bridge: our client bases overlap
- Offer: 20-min coffee/call
- What I bring (specific)
- Propose 2 times

Under 150 words. Peer-to-peer, not pitch."""},
    {"id": "p46", "title": "5-star review response", "module": "Module 10", "tags": ["review", "all-lines"],
     "desc": "3-5 sentence thank-you response that strengthens the public record.",
     "prompt": """Write 3-5 sentence response to 5-star review.

Context: I [specific interaction].

- Thank by first name
- Reference specific from review
- Reinforce what I do
- End warmly, not saccharine

Avoid "it was our pleasure" / "strive to provide excellent service."

REVIEW: [paste]"""},
    {"id": "p47", "title": "4-star neutral review response", "module": "Module 10", "tags": ["review", "all-lines"],
     "desc": "Response to mixed feedback that doesn't get defensive.",
     "prompt": """Response to 3-4 star review with constructive feedback.

- Thank for honest feedback
- Acknowledge specific flag, no defensiveness
- What's changed or I'd do differently
- Invite to reach out directly
- 4-6 sentences

Not defensive, not over-apologizing."""},
    {"id": "p48", "title": "Negative review response (HIPAA-safe)", "module": "Module 10", "tags": ["review", "all-lines"],
     "desc": "Calm, professional response to 1-2 star reviews that future prospects will read.",
     "prompt": """Response to 1-2 star review.

- Acknowledge frustration, no arguing facts
- Do NOT reveal PHI / client-specific details
- What I'd try to resolve (if applicable)
- Invite contact at [phone/email] privately
- No superlatives, defensiveness, apology-spirals
- 4-6 sentences

Future prospects watch how I handle pressure.

REVIEW: [paste]"""},
    {"id": "p49", "title": "Suspected fake review response", "module": "Module 10", "tags": ["review", "all-lines"],
     "desc": "Short professional response when the review is clearly not from a real client.",
     "prompt": """Response to review that seems fake or from non-client.

- Politely note I don't recognize this interaction
- Invite them to contact directly if mistake
- Don't accuse
- Don't engage false claims
- 2-3 sentences

Puzzled, not defensive."""},
    {"id": "p50", "title": "Review request email", "module": "Module 10", "tags": ["review", "email", "all-lines"],
     "desc": "Ask a happy client for a Google review without gating.",
     "prompt": """80-120 word email asking client for Google review.

Context: [what we did]

- Open with specific recent interaction
- Ask: share experience on Google
- Direct link placeholder
- 60 seconds
- Offer to answer questions

Do NOT: offer incentive, specify 5 stars, pressure."""},
    {"id": "p51", "title": "Newsletter: one-big-thing", "module": "Module 11", "tags": ["newsletter", "email", "all-lines"],
     "desc": "Monthly newsletter in the one-big-thing-plus-quick-hits format.",
     "prompt": """Monthly newsletter for [line] clients.

Topic: [pick one]

- Subject: 5-7 words, personal note
- Open: like writing to a friend
- Main (250-400w): one big thing
- Quick hits (3-5 bullets, 1-2 sentences each)
- Close: 1-2 sentences, warm, personal
- P.S. with specific small thing

Letter from knowledgeable friend tone."""},
    {"id": "p52", "title": "12-month newsletter calendar", "module": "Module 11", "tags": ["newsletter", "planning", "all-lines"],
     "desc": "Full year of newsletter topics tied to real triggers.",
     "prompt": """12-month newsletter calendar for [lines] serving [audience].

Format per month:
Month - Primary topic - Why this month - One angle

Tied to: seasons, deadlines, life-stage triggers, common questions. No generic awareness months."""},
    {"id": "p53", "title": "Welcome email sequence", "module": "Module 11", "tags": ["newsletter", "email", "all-lines"],
     "desc": "4-email welcome sequence for new newsletter subscribers.",
     "prompt": """4-email welcome sequence after signup.

Email 1 (immediate): Welcome, who I am, what to expect. Under 150w.
Email 2 (day 2): One actionable thing. Under 200w.
Email 3 (day 5): Anonymized client story. Under 250w.
Email 4 (day 10): Soft direct ask. Under 150w.

From me personally. Hand-written feel."""},
    {"id": "p54", "title": "Newsletter subject line tester", "module": "Module 11", "tags": ["newsletter", "email", "all-lines"],
     "desc": "10 subject line options in different patterns.",
     "prompt": """10 subject lines for newsletter about [topic].

- 4-7 words
- Lowercase
- Mix: question, observation, detail, news, promise, personal

Avoid: "[Month] Newsletter," "[Agency] Update," generic teasers."""},
    {"id": "p55", "title": "Facebook ad — Medicare", "module": "Module 12", "tags": ["ads", "medicare", "facebook"],
     "desc": "Five FB ad variants with CMS compliance for Medicare campaigns.",
     "prompt": """5 FB ad variants for Medicare in [state], 63-68.

Offer: 20-min no-pressure call.

Each:
- Primary text (90-150w)
- Headline (25-40 char)
- Description (30-45 char)

Angles: question, contrarian, local detail, story, direct value.

CMS compliance in each:
- "Not affiliated with any government agency"
- Plan disclaimer
- No specific plan names / benefits
- No "free" without actual no-cost

No fear tactics, fake urgency, over-emoji."""},
    {"id": "p56", "title": "Facebook ad — Life / Final Expense", "module": "Module 12", "tags": ["ads", "life", "facebook"],
     "desc": "Five FB ad variants for final expense with appropriate disclaimers.",
     "prompt": """5 FB ad variants for final expense, 55-75 in [state].

Offer: 10-min rate check, no exam.

Angles: specific pain, protection framing, misconception, simple process, direct offer.

No specific premium quotes. Include "Subject to underwriting." Respectful tone, not fear-mongering."""},
    {"id": "p57", "title": "Facebook ad — P&C bundle", "module": "Module 12", "tags": ["ads", "pnc", "facebook"],
     "desc": "Home + auto bundle ad variants with coverage-gap angles.",
     "prompt": """5 FB ad variants for home + auto bundle, 30-55 homeowners in [state/city].

Offer: 10-min policy review, send dec page.

Angles: rate-increase, coverage gap, time convenience, local, trust.

No "lowest rates," no disparaging competitors. Include trust signal."""},
    {"id": "p58", "title": "Google Search ad copy", "module": "Module 12", "tags": ["ads", "google", "all-lines"],
     "desc": "Responsive Search Ad headlines, descriptions, sitelinks for your keywords.",
     "prompt": """Google Search ads for [line] in [city/state].

Keywords: [list]

For each keyword:
- 3 RSA headlines (30 char)
- 2 descriptions (90 char)
- Display path
- 3 sitelinks

Avoid superlatives, specific rates, unauthorized carrier claims."""},
    {"id": "p59", "title": "Landing page copy", "module": "Module 12", "tags": ["ads", "landing-page", "all-lines"],
     "desc": "Campaign landing page with the structure that converts paid traffic.",
     "prompt": """Landing page copy for [campaign].

Goal: [book call / get quote / download].

- Headline (7-12w, matches ad)
- Sub-headline
- 3-4 "what you get" bullets
- Proof section
- Form: name, phone, email, one qualifier
- Second CTA below fold
- 4-5 FAQ
- Trust signals
- "What happens next" section

Matches ad tone."""},
    {"id": "p60", "title": "Plain-language glossary", "module": "Module 13", "tags": ["client-ed", "all-lines"],
     "desc": "One-page glossary for clients with 12-15 terms in their language.",
     "prompt": """1-page glossary for [line] clients. 12-15 terms.

Each:
- Term (as on paperwork)
- 1-2 sentence plain-language def
- 1 sentence why it matters

For a 65-year-old non-professional. Format for Canva/Word."""},
    {"id": "p61", "title": "Policy summary one-pager", "module": "Module 13", "tags": ["client-ed", "all-lines"],
     "desc": "\"What you actually bought\" summary clients can keep.",
     "prompt": """1-page policy summary.

Structure:
1. One-sentence "what this is"
2. What it does (3-4 bullets)
3. What it does NOT cover (3-4 bullets)
4. What to do with it (storage, who to tell)
5. When to call me (life event triggers)
6. Space for: policy#, carrier, date, contact

No specific $ figures (fill per client)."""},
    {"id": "p62", "title": "Claim filing guide", "module": "Module 13", "tags": ["client-ed", "all-lines"],
     "desc": "One-page guide for clients on how to file a claim.",
     "prompt": """1-page claim guide for [line].

- "Take a breath" opener
- Step 1: immediate action
- Step 2: docs/info needed
- Step 3: carrier contact
- Step 4: how to contact me
- What NOT to do
- Typical timeline
- If delayed/denied

Human tone. Assume stressed reader."""},
    {"id": "p63", "title": "Annual review checklist", "module": "Module 13", "tags": ["client-ed", "all-lines"],
     "desc": "8-12 yes/no questions clients use to self-audit coverage.",
     "prompt": """1-page annual review checklist for [line]. 8-12 yes/no questions.

Each: life situation triggering coverage change. Client language.

Examples:
- "Has anyone been added to your household?"
- "Did income change by 15%+?"

Top: "If yes to any, let's schedule a review"
Bottom: contact + scheduling link placeholder."""},
    {"id": "p64", "title": "Family handoff one-pager", "module": "Module 13", "tags": ["client-ed", "life", "annuity"],
     "desc": "Document the client gives family for what to do if they pass away.",
     "prompt": """1-page doc client's family uses if client passes/becomes incapacitated.

- What to do first
- Where docs are (placeholder)
- Who to call (me + carrier)
- What to bring
- What NOT to do
- What happens next / timeline
- My contact

Calm, respectful, plainspoken. Audience is in grief/panic."""},
    {"id": "p65", "title": "Monday marketing review", "module": "Module 14", "tags": ["system", "planning", "all-lines"],
     "desc": "Weekly review prompt to plan your 2-hour marketing block.",
     "prompt": """Weekly marketing planning. Last week:

- Social engagement: [describe]
- Email replies: [number, notable]
- Ads: [spend, leads, CPL]
- Meetings booked: [number, source]
- Pipeline: [notes]

Based on this:
1. What to double down on?
2. What to stop?
3. 3 experiments to run
4. Highest-leverage marketing task for 2 hours?

Practical."""},
    {"id": "p66", "title": "30-day content calendar", "module": "Module 14", "tags": ["system", "planning", "all-lines"],
     "desc": "Full 30-day calendar of newsletter, blogs, socials, videos, prospecting angles.",
     "prompt": """30-day content calendar.

Line: [from context]
Audience: [from context]
Theme: [one]

- 4 newsletter big ideas (one per week)
- 4 blog post titles
- 16 social posts (4/week)
- 4 video scripts (1/week)
- 2 prospecting angles

Table: Date | Channel | Title | Status.

Include time-sensitive topics for this month."""},
    {"id": "p67", "title": "Red phrase scanner (compliance)", "module": "Module 15", "tags": ["compliance", "all-lines"],
     "desc": "Scan any piece for compliance red flags across lines.",
     "prompt": """Scan for compliance red flags for [line].

Flag:
- Superlatives
- Specific numeric claims
- Competitor comparisons
- Urgency claims (real?)
- Missing disclaimers
- Implied endorsements
- Product-varying claims
- Fear-based language

For each: suggest compliant rewrite. Then give cleaned version.

Line: [specify]
Jurisdiction: [state(s)]

[Paste]"""},
]


# Build the prompt library page
tag_counts = {}
for p in PROMPTS:
    for t in p["tags"]:
        tag_counts[t] = tag_counts.get(t, 0) + 1

# Sort tags by count, but put 'all-lines' first
sorted_tags = sorted(tag_counts.items(), key=lambda x: (-x[1], x[0]))

tag_chips_html = '<div class="library-filter">'
tag_chips_html += f'<button class="filter-chip active" data-tag="all">All ({len(PROMPTS)})</button>'
for t, c in sorted_tags:
    tag_chips_html += f'<button class="filter-chip" data-tag="{t}">{t} ({c})</button>'
tag_chips_html += '</div>'

prompts_html = ""
for p in PROMPTS:
    tag_html = ' '.join([f'<span class="library-tag">{t}</span>' for t in p["tags"]])
    prompts_html += f'''
<div class="library-prompt" data-tags="{' '.join(p['tags'])}">
<h3 class="library-prompt-title">{p["title"]}</h3>
<div class="library-prompt-meta">
<span style="color:#4a00e0; font-weight:600;">{p["module"]}</span>
{tag_html}
</div>
<p>{p["desc"]}</p>
<div class="prompt-box">
<div class="prompt-box-label">{p["id"].upper()}</div>
<button class="copy-btn">Copy</button>
<pre>{p["prompt"]}</pre>
</div>
</div>
'''

library_body = f"""
<p>Every prompt from all 15 modules in one searchable index. Use the filters to narrow by topic, or search the box to find a specific asset type. Click any prompt's Copy button to grab it. Fill in the bracketed placeholders with your specifics and run.</p>

<div class="library-search">
<input type="text" id="library-search-input" placeholder="Search prompts..." />
</div>

{tag_chips_html}

<p class="library-count">{len(PROMPTS)} prompts</p>

{prompts_html}
"""

write_playbook_page(
    slug="prompt-library",
    title="Prompt library",
    tag="Resource",
    subtitle=f"All {len(PROMPTS)} prompts from the playbook, searchable and filterable by type and insurance line.",
    body_html=library_body,
)

print("\n✓ Insurance Playbook Part 3: Modules 11-15 + Prompt Library (6 pages)")
