#!/usr/bin/env python3
"""Cold Email content part 3: Copy + Sequences (12 pages)."""
from _build_cold import write_cold_page

DR_LINK = "../../direct-response"


# ============================================================
# COPY (7 pages)
# ============================================================

write_cold_page(
    slug="copy/anatomy",
    title="Cold email anatomy",
    description="Every cold email has six parts. Each does a specific job. Here's the structure, in order.",
    reading_time=4,
    body_html=f"""
<p class="lede">Every effective cold email has six components in a specific order. Miss one and conversion drops. Master the shape and copy becomes iteration, not reinvention.</p>

<h2>The six parts</h2>
<ol>
<li><strong>Subject line</strong> — 3-5 words, lowercase, feels personal. Single job: get the reply.</li>
<li><strong>First line</strong> — specific to this person. The make-or-break.</li>
<li><strong>The bridge</strong> — connects their situation to your relevance. 1-2 sentences.</li>
<li><strong>The pitch</strong> — what you do, one specific angle. 2-3 sentences. Not full pitch.</li>
<li><strong>Proof</strong> — one specific number, client, or outcome.</li>
<li><strong>The ask</strong> — one clear next step. Specific time, specific action.</li>
</ol>

<h2>The 80-word target</h2>
<p>Total: 70-110 words. Longer than 110 and reply rates drop measurably. Shorter than 50 and you lack proof and clarity. The 80-word sweet spot forces you to cut fluff.</p>

<h2>The signature</h2>
<p>Minimal. Name, title, company. No LinkedIn, no phone, no legal disclaimer, no calendar link (the CTA is in the body, not the sig). Corporate signatures flag cold emails as marketing.</p>

<h2>The full example</h2>
<div class="prompt-box">
<div class="prompt-box-label">Example cold email (annotated)</div>
<button class="copy-btn">Copy</button>
<pre>SUBJECT: quick q on your Q3 pipeline

[FIRST LINE] Saw your post yesterday about the mid-market shift you're seeing this year.

[BRIDGE] We work with a few B2B teams in similar spots on the AE ramp side.

[PITCH] Specifically, the problem where newer reps hit 50% of quota while your two senior reps carry the team. We help close that gap using a specific discovery framework.

[PROOF] [Named Client] cut AE ramp-to-quota from 7 months to 4.

[ASK] Worth 15 min next week? Tue 2pm or Thu 10am ET?

Sam</pre>
</div>

<h2>What to avoid</h2>
<ul>
<li>"Hope this email finds you well" — marks the email as templated</li>
<li>"I wanted to reach out" — passive, self-referential</li>
<li>"Take a look at our comprehensive suite" — brochure talk</li>
<li>Multiple CTAs ("check out our site OR book a call OR download...")</li>
<li>Heavy HTML formatting, images, long signatures</li>
</ul>

<p>The anatomy works. The rest of this section: how to write each part well.</p>
""",
    prev=("Segmentation strategy", "../lists/segmentation.html"),
    nxt=("Subject lines", "subject-lines.html"),
)


write_cold_page(
    slug="copy/subject-lines",
    title="Subject lines",
    description="The subject line is whether your email gets opened at all. Here's what works in cold B2B in 2026.",
    reading_time=4,
    body_html=f"""
<p class="lede">Subject lines are the first gate. Bad subject line, zero opens. Good subject line, 40-60% open rates. In B2B cold, the rules are specific and nearly opposite to consumer email marketing.</p>

<h2>The rules</h2>
<ul>
<li><strong>3-5 words.</strong> Longer subject lines get cut off in mobile preview and feel marketing-y.</li>
<li><strong>Lowercase.</strong> Title Case Looks Like Marketing. lowercase feels like a colleague.</li>
<li><strong>No emojis.</strong> Instantly flags as promotional in B2B inboxes.</li>
<li><strong>No symbols or brackets.</strong> No [Re:], no ?, no !, no ().</li>
<li><strong>No questions unless very natural.</strong> "Quick question" is dead.</li>
<li><strong>Name-drop when relevant.</strong> "[Mutual connection] suggested I reach out" works.</li>
</ul>

<h2>Patterns that work</h2>

<h3>The specific observation</h3>
<p>"your post on retention"<br>
"saw your Q3 announcement"<br>
"re: your hiring push"</p>

<h3>The question format (short)</h3>
<p>"quick thought on pipeline"<br>
"thoughts on [specific topic]"</p>

<h3>The name-drop</h3>
<p>"[Mutual name] said to reach out"<br>
"from [company] to [their company]"</p>

<h3>The curiosity</h3>
<p>"odd question about [department]"<br>
"something you might've missed"</p>

<h3>The direct</h3>
<p>"15 min next week?"<br>
"introduction from [referrer]"</p>

<h2>Patterns that fail</h2>
<ul>
<li>"Exclusive offer for [Company]" — marketing</li>
<li>"Transform your pipeline" — ad</li>
<li>"FREE [anything]" — spam filter bait</li>
<li>"Last chance" — fake urgency</li>
<li>"Are you struggling with X?" — leading</li>
<li>"You won't believe this" — clickbait</li>
</ul>

<h2>Subject line generation</h2>
<div class="prompt-box">
<div class="prompt-box-label">Subject line generator</div>
<button class="copy-btn">Copy</button>
<pre>Generate 15 cold email subject lines for:
- Target: [role + industry]
- Email topic: [what the email is about]
- Context trigger (if any): [recent event]

Rules:
- 3-5 words max
- Lowercase
- No emojis, no symbols
- Should feel like a peer wrote them, not a marketer
- Mix: specific observation, curiosity, direct, name-drop

Just the subject lines, numbered.</pre>
</div>

<h2>Testing</h2>
<p>A/B test 2 subject lines per campaign at minimum. Split 50/50 for the first 200 sends. Keep the winner, test a new challenger against it. See <a href="../testing/what-to-test.html">what to test</a>.</p>

<p>Typical open rates by subject line quality:</p>
<ul>
<li>Weak (generic, long, promotional): 15-25%</li>
<li>Decent (short, lowercase, specific): 35-45%</li>
<li>Strong (specific observation + trigger): 55-70%</li>
</ul>

<p>With iOS 15+ inflating open rates through prefetching, treat opens as directional not absolute. Reply rate is the truer signal.</p>

<p>Related: <a href="{DR_LINK}/copy/headlines.html">headlines in direct response</a> — the same principles scale from email subjects to landing pages.</p>
""",
    prev=("Cold email anatomy", "anatomy.html"),
    nxt=("First lines", "first-lines.html"),
)


write_cold_page(
    slug="copy/first-lines",
    title="First lines",
    description="The first line is where you prove this isn't a mass email. Here's what earns the second sentence.",
    reading_time=4,
    body_html="""
<p class="lede">The first line is the most important sentence in a cold email. If it sounds templated, the reader deletes. If it shows you know something specific about them, they read on. This is where personalization either happens or fails.</p>

<h2>The bar</h2>
<p>A good first line is impossible for the recipient to ignore because it's clearly about them specifically. It references something that could only apply to this one prospect: their recent post, their role change, their company news, a specific detail.</p>

<h2>Sources of specificity</h2>

<h3>Their LinkedIn activity</h3>
<p>"Saw your post yesterday about [specific topic]"<br>
"Your comment on [X's] thread on [topic] — had been thinking the same thing"</p>

<h3>Their company news</h3>
<p>"Just saw the Series B — congrats"<br>
"Noticed you're hiring three AEs — usually means something specific about pipeline"</p>

<h3>Their role change</h3>
<p>"Saw you moved to [company] last month from [previous]"<br>
"Congrats on the VP of Marketing move"</p>

<h3>Their content</h3>
<p>"Read your piece on [topic] in [publication] last week"<br>
"Your podcast episode on [specific ep] — the part about [X] stuck with me"</p>

<h3>Industry context specific to them</h3>
<p>"Your vertical in [state] is getting hit hard this quarter with [specific change]"<br>
"Restaurants in [city] are dealing with [specific issue] — wanted to run something by you"</p>

<h2>What doesn't count as specific</h2>
<ul>
<li>"I see you're a VP of Sales at [Company]" (their title is not news)</li>
<li>"Your company is a leader in [industry]" (flattery, also generic)</li>
<li>"I noticed [Company] has [generic trait]" (obvious fact)</li>
<li>"Happy Tuesday!" (ask yourself why this belongs in a business email)</li>
</ul>

<h2>The first line at scale</h2>
<p>For 10 prospects, write custom lines by hand. For 100, use Claude + enrichment data (LinkedIn posts, company news). For 1000, use Clay or similar with an AI step to generate custom lines from structured data.</p>

<div class="prompt-box">
<div class="prompt-box-label">First line generator (structured input)</div>
<button class="copy-btn">Copy</button>
<pre>For each prospect below, write ONE first line of a cold email (12-20 words) that references something specific to them.

Rules:
- No "Hope you're well"
- No "I came across your profile"
- No generic congrats
- Reference the trigger specifically
- Feel like a peer writing, not a template

PROSPECTS:
1. [Name | Role | Company | Trigger detail]
2. [Name | Role | Company | Trigger detail]
...</pre>
</div>

<h2>The fallback when you have nothing specific</h2>
<p>If you truly can't find anything specific, don't pretend. A good second-tier opener:</p>
<ul>
<li>"We work with [Role]s at [Company size/type] on [specific problem]."</li>
<li>"Short version: [one-sentence pitch]. Wanted to run it by someone in your seat."</li>
</ul>

<p>Honest and brief beats fake personalization. The email does worse but doesn't actively burn trust.</p>

<h2>The craft</h2>
<p>Great first lines take 2-5 minutes of research per prospect. For high-value targets, worth every minute. At scale, AI-enriched data brings this down to seconds. But the underlying principle holds: specificity is the only thing that proves "this isn't a blast."</p>
""",
    prev=("Subject lines", "subject-lines.html"),
    nxt=("The pitch", "the-pitch.html"),
)


write_cold_page(
    slug="copy/the-pitch",
    title="The pitch",
    description="The pitch is 2-3 sentences. Not your company's pitch deck. One specific angle that matters to this prospect.",
    reading_time=4,
    body_html=f"""
<p class="lede">The pitch is where most cold emails bloat. Teams cram company overview, value props, and product features into 200 words of dense marketing copy. Cold email pitches are 2-3 sentences. One specific angle. Not your full pitch deck.</p>

<h2>The pitch's job</h2>
<p>The pitch doesn't sell. It creates enough curiosity that the prospect wants to talk. The sale happens on the call. In the email, you just need: "I help people like you with this specific problem, in this specific way."</p>

<h2>The 3-sentence structure</h2>
<ol>
<li><strong>The problem or observation</strong> — specific, relevant to them</li>
<li><strong>What you do about it</strong> — one concrete angle, not generic claims</li>
<li><strong>The mechanism</strong> — why your approach works (optional but strong)</li>
</ol>

<h2>Example (bad vs good)</h2>

<h3>Bad pitch (too broad)</h3>
<div class="prompt-box">
<div class="prompt-box-label">Too much, too generic</div>
<button class="copy-btn">Copy</button>
<pre>We're a leading provider of comprehensive sales enablement solutions that help companies transform their pipeline velocity, accelerate ramp time for new AE hires, improve forecasting accuracy, and drive measurable revenue growth through data-driven insights, personalized coaching, and best-in-class training content. Trusted by 500+ companies including [logo, logo, logo].</pre>
</div>

<h3>Good pitch (specific angle)</h3>
<div class="prompt-box">
<div class="prompt-box-label">One angle, specific</div>
<button class="copy-btn">Copy</button>
<pre>The specific problem: newer reps take 6-8 months to hit quota while your top 2 reps carry the team. We work on that specific gap using a structured first-call framework. [Client] cut ramp from 7 months to 4.</pre>
</div>

<p>One problem. One approach. One proof. 35 words vs 80.</p>

<h2>Framing the pitch to their role</h2>
<p>Same product, different pitch by role:</p>

<ul>
<li><strong>To VP Sales:</strong> "The problem where new reps ramp slowly while senior reps carry the team."</li>
<li><strong>To CFO:</strong> "The visibility gap between what AEs say will close and what actually books."</li>
<li><strong>To CEO:</strong> "The conversion plateau between lead and booked meeting."</li>
</ul>

<p>Pick the angle that matches the pain your specific recipient feels. Generic product pitches don't personalize; framed angles do.</p>

<h2>Proof in the pitch</h2>
<p>One concrete piece of evidence. Options:</p>
<ul>
<li><strong>Named client + specific outcome:</strong> "[Client] cut ramp from 7 to 4 months."</li>
<li><strong>Aggregate stat:</strong> "Across 40 clients, average AE ramp drops 30%."</li>
<li><strong>Your track record:</strong> "I've placed 140 [specific niche] policies in [state] in the last 18 months."</li>
<li><strong>Credible logos:</strong> "We work with [recognizable name in their space]."</li>
</ul>

<p>One is enough. More starts to feel like brochure copy.</p>

<h2>The pitch-writing discipline</h2>

<div class="prompt-box">
<div class="prompt-box-label">Pitch compressor</div>
<button class="copy-btn">Copy</button>
<pre>Take this company pitch [paste your full pitch / website copy].

Compress to 2-3 sentences for a cold email to [specific role] at [company type].

Rules:
- Name ONE specific problem this role feels
- Say what we do in one concrete sentence, no "best-in-class" / "comprehensive" / "solution"
- Include one proof point (named client or specific stat)
- Total: 35-60 words

Write 3 versions with different angles.</pre>
</div>

<h2>The "one thing" test</h2>
<p>Read your pitch back. If you can identify more than one benefit or feature, cut it until only one remains. Cold email is a single-angle medium. Broader sells go in the sales call.</p>

<p>Related: <a href="{DR_LINK}/copy/formulas.html">AIDA, PAS, PASTOR</a> — pitch structure in longer-form direct response.</p>
""",
    prev=("First lines", "first-lines.html"),
    nxt=("CTAs for cold", "ctas.html"),
)


write_cold_page(
    slug="copy/ctas",
    title="CTAs for cold",
    description="The CTA is where interested readers commit or drop. Here's what works in cold email specifically.",
    reading_time=4,
    body_html=f"""
<p class="lede">The CTA is the last sentence of a cold email and the most-read (after the first line). Vague CTAs get vague responses. Specific CTAs get bookings or clear nos. Either is better than silence.</p>

<h2>The CTA continuum</h2>

<h3>Highest friction (rare for cold)</h3>
<ul>
<li>"Let's schedule a 45-minute deep dive"</li>
<li>"Book a demo" (if they don't know you)</li>
</ul>

<h3>Standard friction (good default)</h3>
<ul>
<li>"15 minutes next week? Tue 2pm or Thu 10am ET?"</li>
<li>"Worth a quick call to compare notes?"</li>
</ul>

<h3>Low friction (for cold audiences)</h3>
<ul>
<li>"Want me to send the 3-slide summary? No call needed."</li>
<li>"Quick yes/no — should I share how [Client] handled it?"</li>
<li>"Worth keeping in your back pocket for [specific future trigger]?"</li>
</ul>

<h3>Interest probes (when the full ask is too heavy)</h3>
<ul>
<li>"Is this a priority in the next quarter, or better to follow up later?"</li>
<li>"If I'm in the wrong quarter, let me know a better time to check in."</li>
</ul>

<h2>What matters in a cold CTA</h2>

<h3>Specific times, not "let me know when"</h3>
<p>Vague: "When works for you?"<br>
Better: "Tue 2pm or Thu 10am ET?"</p>

<p>Offering 2-3 times reduces the recipient's decision cost. Pick-from-list is easier than volunteer-a-time. Calendar links work too but feel slightly marketing-y for the first email.</p>

<h3>Short duration</h3>
<p>"15 minutes" converts better than "30 minutes" converts better than "a call." The implied commitment decides whether they reply.</p>

<h3>Escape hatches</h3>
<p>"Or I can send the summary — no call needed" tells the reader there's a lower-commitment path. Increases reply rate even from people who end up wanting the call.</p>

<h3>One CTA only</h3>
<p>Never "book a call OR download our guide OR connect on LinkedIn OR reply." Choose one primary action. Secondary options dilute.</p>

<h2>CTAs by sequence position</h2>

<h3>Email 1</h3>
<p>Direct call ask with specific times.</p>

<h3>Email 2 (bump)</h3>
<p>Lower-friction variant. "Too busy this week? Want me to send the 3-slide version?"</p>

<h3>Email 3</h3>
<p>Case study email. CTA is "Want the full writeup?"</p>

<h3>Email 4</h3>
<p>Reframe CTA. "Is timing the issue or is this not a priority?"</p>

<h3>Email 5 (breakup)</h3>
<p>Clear exit. "Closing the loop. If [trigger] changes, reply or call."</p>

<h2>Generator</h2>

<div class="prompt-box">
<div class="prompt-box-label">CTA generator by sequence step</div>
<button class="copy-btn">Copy</button>
<pre>For a 5-touch cold email sequence to [role] about [topic], write 5 different CTAs — one per email.

Constraints:
- Email 1: direct call ask, specific times
- Email 2: lower friction, escape hatch
- Email 3: content-driven (case study, summary)
- Email 4: interest probe (not just "bumping this up")
- Email 5: clean breakup

Each under 30 words. No "circling back," no "touching base," no "reaching out again."</pre>
</div>

<h2>The calendar-link question</h2>
<p>Sharing a calendar link (Calendly, Chili Piper) is efficient but can feel cold early in the relationship. Options:</p>
<ul>
<li><strong>Email 1:</strong> two specific times, no calendar link (more human).</li>
<li><strong>Email 2+:</strong> add "Or grab any time that works: [calendar link]."</li>
</ul>

<p>This balances personal tone with convenience. Jumping straight to calendar link in cold email 1 converts worse than proposing times.</p>

<p>Related: <a href="{DR_LINK}/copy/ctas.html">CTAs in direct response</a> — the principles scale to landing pages, VSLs, and long-form.</p>
""",
    prev=("The pitch", "the-pitch.html"),
    nxt=("Signatures", "signatures.html"),
)


write_cold_page(
    slug="copy/signatures",
    title="Signatures",
    description="Email signatures are a surprisingly strong signal. Marketing signatures flag cold emails as mass blasts. Peer signatures slip through.",
    reading_time=3,
    body_html="""
<p class="lede">Your email signature is the last thing the reader sees. It's also the first thing spam filters scan for "marketing email." A minimal, human-looking signature helps deliverability and conversion. A corporate signature with logo, banners, social icons, and disclaimers does the opposite.</p>

<h2>The minimal signature</h2>
<p>What works for cold B2B in 2026:</p>

<div class="prompt-box">
<div class="prompt-box-label">Minimal signature</div>
<button class="copy-btn">Copy</button>
<pre>Sam

Sam Ochoa
[Title], [Company]
[City, State]</pre>
</div>

<p>Four lines. Name, title, company, location. Nothing else.</p>

<h2>Why this works</h2>
<ul>
<li><strong>Feels like a person.</strong> Colleagues don't email each other with 12-line corporate signatures.</li>
<li><strong>Deliverability.</strong> Signature blocks with logos, banners, social icons, legal disclaimers trigger promotional/marketing classifiers.</li>
<li><strong>No distraction.</strong> The CTA is in the email body, not competing with "Follow me on LinkedIn!" links.</li>
</ul>

<h2>What to leave out</h2>
<ul>
<li><strong>Logo</strong> — image in email = higher spam score. Text-only.</li>
<li><strong>Banner ads</strong> — "Check out our latest webinar" below the signature = marketing flag.</li>
<li><strong>Legal disclaimers</strong> — "This email is confidential..." — if required by your role, keep brief; it's a spam signal.</li>
<li><strong>Phone number</strong> — most cold reply paths go through email, not phone. Add to follow-ups if useful.</li>
<li><strong>Social icons</strong> — sophisticated LinkedIn icons, Twitter icons, etc. flag as marketing.</li>
<li><strong>Quote of the day</strong> — no.</li>
<li><strong>Award badges</strong> — no.</li>
</ul>

<h2>Progressive signatures across sequence</h2>
<p>A small technique: add one element per email across the sequence to signal continuity without cluttering:</p>
<ul>
<li>Email 1: minimal (name, title, company, location)</li>
<li>Email 2-3: add phone number</li>
<li>Email 4+: add a link to one relevant resource (case study or LinkedIn profile)</li>
</ul>

<h2>The "replying from phone" trick</h2>
<p>"Sent from my phone — excuse brevity and typos" at the end of cold emails feels personal and explains casual tone. Do not overuse. Legitimate when you are on phone; fake when everyone does it.</p>

<h2>For regulated industries</h2>
<p>Some industries require specific disclaimers in email (financial services, healthcare, legal). Keep them brief, use small grey text, and place after a line break:</p>

<div class="prompt-box">
<div class="prompt-box-label">Compliant minimal signature</div>
<button class="copy-btn">Copy</button>
<pre>Sam

Sam Ochoa
Licensed Agent | [Company]
[City, State]

---
Securities offered through [Broker Dealer]. Member FINRA/SIPC.</pre>
</div>

<p>Where compliance requires more, work with your firm's compliance team — never trim legal requirements to optimize deliverability.</p>

<h2>The one-line description</h2>
<p>Some operators add a single line of "what I do" under their title:</p>

<div class="prompt-box">
<div class="prompt-box-label">Signature with one-line positioning</div>
<button class="copy-btn">Copy</button>
<pre>Sam Ochoa
Pipeline & ramp consultant for B2B SaaS teams
San Francisco, CA</pre>
</div>

<p>Works when your positioning is clear and specific. Skip if it sounds like a tagline.</p>

<h2>The recipient's test</h2>
<p>Read your signature as a recipient. Does it look like a peer emailed you, or does it look like a marketing email? If there's any question, trim.</p>
""",
    prev=("CTAs for cold", "ctas.html"),
    nxt=("Personalization at scale", "personalization.html"),
)


write_cold_page(
    slug="copy/personalization",
    title="Personalization at scale",
    description="Custom first lines for 1000 prospects sound impossible. Here's how modern tooling makes it routine.",
    reading_time=4,
    body_html=f"""
<p class="lede">Personalization used to mean "Hi [First Name]." Modern cold email uses enriched data, signal scraping, and AI to generate custom first lines at scale. Done right, every email feels hand-written even at 1000 sends per week.</p>

<h2>The three tiers</h2>

<h3>Tier 1: Token replacement</h3>
<p>Basic merge fields: first name, company, role, industry. Bare minimum. Doesn't actually read as personal.</p>

<h3>Tier 2: Structured enrichment</h3>
<p>Pull LinkedIn posts, company news, funding events, hiring signals, tech stack changes. Build a "trigger" field per prospect. Reference in first line.</p>

<h3>Tier 3: AI-generated custom lines</h3>
<p>For each prospect, feed structured data (LinkedIn activity, news, role) to an LLM. Get a unique first line per prospect. Routine with Clay + OpenAI/Claude integration.</p>

<h2>The Clay workflow</h2>
<p>The dominant stack in 2026:</p>

<ol>
<li>Export prospects from Sales Navigator, Apollo, or ZoomInfo to Clay</li>
<li>Enrich each row with: LinkedIn activity, company news, hiring signals, tech stack</li>
<li>Add AI column with prompt: "Write a 15-word first line referencing [most interesting trigger]"</li>
<li>Push to cold email tool (Instantly, Smartlead) with personalized first line merged in</li>
</ol>

<p>Result: every prospect gets a unique, specific first line. The rest of the email is a template with merge fields.</p>

<h2>The AI first-line prompt</h2>

<div class="prompt-box">
<div class="prompt-box-label">Clay AI column prompt</div>
<button class="copy-btn">Copy</button>
<pre>Given the following data about a prospect, write ONE first line of a cold email — 12-18 words — that references something specific and doesn't sound templated.

PROSPECT DATA:
- Name: {{{{name}}}}
- Role: {{{{role}}}} at {{{{company}}}}
- Recent LinkedIn post: {{{{latest_post}}}}
- Company news: {{{{company_news}}}}
- Hiring signal: {{{{job_posting}}}}

Rules:
- Pick the MOST specific trigger (not just the most recent)
- Sound like a peer, not a marketer
- No "Hope you're well" / "I came across"
- No generic congrats
- Reference the specific trigger by name or detail

Output: just the first line, nothing else.</pre>
</div>

<h2>The templated-but-personal email body</h2>
<p>First line is per-prospect. Body is a template with 2-3 variable fields (role, company, industry pain).</p>

<div class="prompt-box">
<div class="prompt-box-label">Templated body with merge fields</div>
<button class="copy-btn">Copy</button>
<pre>Subject: {{{{subject}}}}

{{{{first_line}}}}

We work with {{{{role_plural}}}} at {{{{company_size}}}} B2B teams on the specific problem of {{{{role_specific_pain}}}}.

{{{{proof_point_for_segment}}}}

Worth 15 min next week? Tue 2pm or Thu 10am ET?

Sam</pre>
</div>

<p>Four merge fields: subject, first_line, role-specific pitch, proof point. Everything else is a template. Each email reads as if written for them.</p>

<h2>The quality tiers of enrichment</h2>

<h3>Fast, cheap</h3>
<ul>
<li>Apollo enriched data (firmographics, contact info)</li>
<li>Rough LinkedIn scraping (recent activity)</li>
</ul>

<h3>Medium</h3>
<ul>
<li>Clay with multiple waterfalls</li>
<li>LinkedIn Sales Nav + Evaboot</li>
<li>News API (Crunchbase, company press)</li>
</ul>

<h3>High-quality, slower</h3>
<ul>
<li>Clay + AI enrichment pass + verification</li>
<li>Manual review of AI-generated lines before sending</li>
<li>Signal-triggered outreach only</li>
</ul>

<p>For enterprise targets ($50K+ ACV), tier 3 is worth it. For SMB volume plays, tier 2 is the right balance. Tier 1 doesn't work at all in 2026.</p>

<h2>The quality check</h2>
<p>Before scaling a personalization workflow to 1000+ prospects, spot-check 50 generated first lines manually. If more than 3 feel generic or wrong, fix the prompt. AI-generated spam at scale destroys more than unpersonalized sends.</p>

<h2>The honest limit</h2>
<p>No matter how good the AI is, real human review beats automation for top prospects. For your 20 most important targets per month, write the first line yourself. Save AI personalization for tiers below.</p>

<p>Related: <a href="{DR_LINK}/leads/cold-outreach.html">cold outreach in direct response</a>.</p>
""",
    prev=("Signatures", "signatures.html"),
    nxt=("Multi-touch sequences", "../sequences/multi-touch.html"),
)


# ============================================================
# SEQUENCES (5 pages)
# ============================================================

write_cold_page(
    slug="sequences/multi-touch",
    title="Multi-touch sequences",
    description="A single cold email rarely converts. The multi-touch sequence is how real pipeline gets built.",
    reading_time=4,
    body_html="""
<p class="lede">Most reply rates look like this: email 1 produces 1-3%, email 2 another 1-2%, email 3 another 1-2%, and so on. Across a 5-touch sequence, aggregate reply rate commonly hits 8-15%. Without follow-ups, you leave 60-80% of pipeline on the table.</p>

<h2>Why follow-ups work</h2>
<p>Prospects are busy. They opened email 1, thought "I'll reply later," then forgot. They saw email 2 three days later and replied out of courtesy. They saw email 3 and actually engaged because it offered a lower-friction path. The sequence catches different prospects at different moments.</p>

<h2>The 5-touch default</h2>

<ul>
<li><strong>Email 1 (day 0):</strong> The pitch email.</li>
<li><strong>Email 2 (day 3-4):</strong> Bump. Short, references email 1, adds one new angle.</li>
<li><strong>Email 3 (day 7-9):</strong> Reframe. Lower friction ask (content, not call).</li>
<li><strong>Email 4 (day 13-15):</strong> Case study. Specific proof about a similar client.</li>
<li><strong>Email 5 (day 20-25):</strong> Breakup. Closes the loop, clear exit.</li>
</ul>

<p>Total window: 3-4 weeks. Aggregate reply rate 8-15%.</p>

<h2>The full sequence template</h2>

<div class="prompt-box">
<div class="prompt-box-label">Generate full 5-touch sequence</div>
<button class="copy-btn">Copy</button>
<pre>Given the first cold email below, write the full 5-touch sequence.

EMAIL 1: [paste your email 1]

Generate:
- Email 2 (day 3): short nudge. Reference email 1 casually. Add ONE new angle or data point. Under 60 words.
- Email 3 (day 8): soft reframe. Acknowledge no reply isn't a no. Offer lower-friction path ("want me to send the 2-slide summary instead?"). Under 80 words.
- Email 4 (day 13): case study. Specific anonymized client outcome. Under 120 words. CTA: "want the full writeup?"
- Email 5 (day 22): breakup. "Closing the loop. If [specific trigger changes], reply or call." Under 50 words.

Constraints:
- Same tone as email 1
- Vary opening lines (no "bumping this up," "circling back," "touching base")
- Each email is standalone-readable — don't require reading prior emails
- Progressive lowering of ask (call → content → binary yes/no)</pre>
</div>

<h2>What makes a sequence work</h2>

<h3>Each email stands alone</h3>
<p>Never assume they read email 1. Each message must make sense on its own.</p>

<h3>New information every time</h3>
<p>Don't just repeat. Add an angle, a case study, a new hook.</p>

<h3>Lowering friction across touches</h3>
<p>Email 1 asks for a call. Email 3 asks for a lower commitment (send content). Email 5 asks for a simple yes/no or the honest no.</p>

<h3>No guilt-tripping</h3>
<p>"Just circling back" / "In case you missed this" / "Don't want to keep bothering you but..." all read as passive-aggressive. Stop.</p>

<h3>Clean breakup</h3>
<p>The final email gives the prospect a graceful exit. Often generates replies from people who would have ghosted otherwise.</p>

<h2>The 5 email anatomy</h2>

<h3>Email 1 — The pitch</h3>
<p>80-100 words. First line specific. Pitch + proof + specific CTA.</p>

<h3>Email 2 — The bump</h3>
<p>40-60 words. Reference email 1 casually. Add one angle or new data point. Same CTA or slightly simpler.</p>

<h3>Email 3 — The reframe</h3>
<p>60-80 words. Acknowledge no reply is common. Offer lower-friction alternative. "Want me to send the summary instead?"</p>

<h3>Email 4 — The case study</h3>
<p>100-120 words. Specific anonymized client. Named outcome. CTA: "want the full writeup?"</p>

<h3>Email 5 — The breakup</h3>
<p>30-50 words. Closing loop. Clean exit. "If [trigger] changes, feel free to reply."</p>

<h2>Breakup emails are gold</h2>
<p>The last email in a sequence often gets the highest reply rate. Why: the prospect reads "this is your last email from me" and feels either urgency ("actually I should reply") or relief ("I can say no politely"). Both responses are good.</p>

<h2>When to stop sending</h2>
<ul>
<li>After email 5 if no reply (standard)</li>
<li>Immediately after any reply (positive or negative)</li>
<li>Immediately after unsubscribe or "remove me"</li>
<li>Immediately after OOO (let it expire, resume 2-3 days after their return date)</li>
</ul>

<p>Never continue past email 5 in a single sequence. Re-engage in 3-6 months with a different angle if they remain in ICP.</p>
""",
    prev=("Personalization at scale", "../copy/personalization.html"),
    nxt=("Cadence and timing", "cadence.html"),
)


write_cold_page(
    slug="sequences/cadence",
    title="Cadence and timing",
    description="When you send and how often matters as much as what you send. Here's the pacing that works.",
    reading_time=3,
    body_html="""
<p class="lede">Send too often and you're spam. Send too slowly and they forget. Good cadence is respectful enough to feel human and frequent enough to stay top of mind. The defaults below work in B2B.</p>

<h2>The standard cadence</h2>
<p>For a 5-touch sequence over 22-25 days:</p>

<ul>
<li><strong>Email 1:</strong> Day 0</li>
<li><strong>Email 2:</strong> Day 3 (bump)</li>
<li><strong>Email 3:</strong> Day 8 (reframe)</li>
<li><strong>Email 4:</strong> Day 13 (case study)</li>
<li><strong>Email 5:</strong> Day 22 (breakup)</li>
</ul>

<h2>Day of week</h2>

<h3>Best days (by open and reply rate)</h3>
<ul>
<li>Tuesday morning (best for most B2B)</li>
<li>Wednesday morning</li>
<li>Thursday morning</li>
</ul>

<h3>Worst days</h3>
<ul>
<li>Monday morning (inbox overload)</li>
<li>Friday afternoon (weekend mode)</li>
<li>Any weekend (lowest open rates)</li>
</ul>

<p>For high-volume sequences, spread sends across Tuesday/Wednesday/Thursday to avoid your entire campaign competing with itself in the inbox.</p>

<h2>Time of day</h2>

<h3>Best times (recipient local time)</h3>
<ul>
<li>7-8am (catches them checking email before the workday)</li>
<li>10-11am (morning flow, prime inbox time)</li>
<li>1-2pm (post-lunch recovery, return to email)</li>
</ul>

<h3>Worst times</h3>
<ul>
<li>Between 3pm-5pm (deep work, meeting-heavy)</li>
<li>After 6pm (skipped or deferred)</li>
<li>Before 6am (looks automated)</li>
</ul>

<h2>The local-time trap</h2>
<p>Sending from Pacific time to Eastern prospects at 8am PT = 11am ET. Late morning for the recipient — fine. Sending from Pacific at 8am ET = 5am PT. You're awake at 5am? It looks automated.</p>

<p>Good cold email tools (Instantly, Smartlead) support recipient-timezone sending. Use it. Every email hits at the recipient's 9am regardless of where you are.</p>

<h2>Daily volume per mailbox</h2>

<p>Covered in detail on <a href="../infra/multi-inbox.html">multi-inbox rotation</a>. Limits:</p>
<ul>
<li>New mailbox (warmed &lt; 8 weeks): 10-20/day</li>
<li>Established mailbox: 30-50/day</li>
<li>Never above 80/day on a single mailbox</li>
</ul>

<h2>Frequency caps</h2>
<p>The prospect should never get two emails from you in one day. The sequence automatically handles this, but if you run multiple campaigns, ensure global frequency caps so one prospect doesn't receive email 3 of Campaign A and email 1 of Campaign B on the same day.</p>

<h2>Weekly volume distribution</h2>
<p>For a 1,500 email/week operation:</p>
<ul>
<li>Monday: 200 (light)</li>
<li>Tuesday: 400 (strong)</li>
<li>Wednesday: 400 (strong)</li>
<li>Thursday: 350 (solid)</li>
<li>Friday: 150 (light)</li>
<li>Weekend: 0</li>
</ul>

<h2>Holidays and slow weeks</h2>
<ul>
<li><strong>US Thanksgiving week</strong> — skip Thursday and Friday</li>
<li><strong>Christmas and New Year's</strong> — pause entire sequences from Dec 22 - Jan 2</li>
<li><strong>July 4 week</strong> — lower volume, skip Friday</li>
<li><strong>Last week of August</strong> — reduced engagement; lower volume</li>
</ul>

<p>Emails sent in these periods either get buried or land when your prospect returns to a backed-up inbox. Pause, resume when attention returns.</p>

<h2>The A/B test on cadence</h2>
<p>Default cadences (3-5 day gaps) work. But for your specific audience, test:</p>
<ul>
<li>Faster: 2-day gaps (total sequence 10-12 days)</li>
<li>Slower: 5-7 day gaps (total sequence 25-30 days)</li>
</ul>

<p>Enterprise buyers with long decision cycles often tolerate and respond better to slower cadences. SMB impulse buyers often respond better to faster.</p>
""",
    prev=("Multi-touch sequences", "multi-touch.html"),
    nxt=("The breakup email", "breakup.html"),
)


write_cold_page(
    slug="sequences/breakup",
    title="The breakup email",
    description="The last email in a sequence. Short, honest, no guilt. Often the highest-replying message.",
    reading_time=3,
    body_html="""
<p class="lede">The breakup email closes the loop. It tells the prospect "I'm moving on unless you tell me otherwise." Done right, it's the highest-reply email in the sequence. Done wrong, it's a whiny "sorry to bother you" that burns trust.</p>

<h2>What a good breakup does</h2>
<ul>
<li>States you're closing the loop</li>
<li>Gives a specific trigger for future re-engagement</li>
<li>No guilt, no passive aggression, no plea</li>
<li>Short (30-50 words)</li>
<li>Leaves the relationship clean for future outreach</li>
</ul>

<h2>The template</h2>

<div class="prompt-box">
<div class="prompt-box-label">Breakup email template</div>
<button class="copy-btn">Copy</button>
<pre>Hey [first name],

Closing the loop on this thread — sounds like now isn't the right time.

If [specific future trigger], feel free to reach out. I'll stop reaching out until then.

[Name]</pre>
</div>

<h2>Variants by context</h2>

<h3>For a prospect who's been silent</h3>
<div class="prompt-box">
<div class="prompt-box-label">Silent prospect breakup</div>
<button class="copy-btn">Copy</button>
<pre>Hey [name],

Last one — no reply usually means "not right now" or "not for me." Either is fine.

If [trigger: e.g., "pipeline pressure hits again next quarter"] becomes a priority, reply or call.

Otherwise, good luck with [Q4 / the hire / whatever's relevant].

Sam</pre>
</div>

<h3>For a prospect who showed interest but stalled</h3>
<div class="prompt-box">
<div class="prompt-box-label">Stalled prospect breakup</div>
<button class="copy-btn">Copy</button>
<pre>Hey [name],

Read between the lines you've gone quiet — makes sense if priorities shifted.

Two options:
- Want to pick this up in [month]? Reply "ping me" and I'll circle back then.
- If it's dead, reply "pass" and I'll stop.

Either works. Sam</pre>
</div>

<h3>For a cold prospect (standard)</h3>
<div class="prompt-box">
<div class="prompt-box-label">Cold breakup</div>
<button class="copy-btn">Copy</button>
<pre>Hey [name],

Closing this loop. If [specific trigger: "AE ramp is still a priority in Q2"], my door is open.

Won't follow up further unless I hear from you.

Sam</pre>
</div>

<h2>What NOT to do in a breakup</h2>

<h3>Don't guilt trip</h3>
<p>"Sorry to keep bothering you" — don't.<br>
"I feel like I've been a nuisance" — don't.<br>
"I guess you're not interested" — don't.</p>

<p>Apologies and guilt make you sound weak and waste the prospect's time re-reassuring you.</p>

<h3>Don't attack</h3>
<p>"If you're not the right person, who is?" on the breakup email reads as aggressive. Move that ask to email 3 or 4.</p>

<h3>Don't beg</h3>
<p>"If you could just give me 5 minutes" — no. The breakup is about your dignity as a sender, not their pity.</p>

<h3>Don't re-pitch</h3>
<p>The breakup is not another chance to sell. If you haven't sold them in 4 emails, email 5 isn't the one that converts the pitch.</p>

<h2>Why breakups generate the highest reply rate</h2>
<p>Two reasons:</p>
<ol>
<li><strong>Urgency.</strong> Prospects who were thinking "I'll get to it" suddenly realize they won't get another email. Reply-now or never.</li>
<li><strong>Relief.</strong> Prospects who didn't want to engage feel comfortable saying "pass" when the sender signals the sequence is ending.</li>
</ol>

<p>Either response is a win. "Yes let's talk" is a meeting. "Not for us" is list hygiene (you remove them and save future send volume).</p>

<h2>The "ping me in X months" variant</h2>
<p>For prospects who say "not right now," the breakup plus a future re-engage signal:</p>

<div class="prompt-box">
<div class="prompt-box-label">Delay-for-timing breakup</div>
<button class="copy-btn">Copy</button>
<pre>Hey [name],

Sounds like timing isn't right.

I'll put a reminder to reach out in [specific month — Q2, September, whenever makes sense].

If something shifts before then, reply anytime.

Sam</pre>
</div>

<p>Then you actually put the reminder on your calendar. This turns cold-sequence ghosts into re-engageable warm prospects. Multi-year pipeline value.</p>
""",
    prev=("Cadence and timing", "cadence.html"),
    nxt=("Multi-channel orchestration", "multi-channel.html"),
)


write_cold_page(
    slug="sequences/multi-channel",
    title="Multi-channel orchestration",
    description="Email alone isn't the best sequence. Email + LinkedIn + phone outperforms any single channel.",
    reading_time=4,
    body_html="""
<p class="lede">Cold email reply rates cap out. Adding LinkedIn and phone to the sequence compounds reach and conversion. A multi-channel sequence reaches the same prospect 5-8 ways over 3 weeks, catching them on whatever channel they pay attention to.</p>

<h2>The case for multi-channel</h2>
<p>Some prospects check email first thing. Others check LinkedIn before email. Others answer phone calls but ignore both. Multi-channel hits them where they are, not where you prefer.</p>

<p>Typical outcome compared to email-only:</p>
<ul>
<li>Email only: 8-12% total reply rate across sequence</li>
<li>Email + LinkedIn: 12-18%</li>
<li>Email + LinkedIn + phone: 18-25%</li>
</ul>

<h2>The 3-channel default sequence</h2>

<ul>
<li><strong>Day 0:</strong> Email 1 + LinkedIn connection request</li>
<li><strong>Day 3:</strong> Email 2 (bump)</li>
<li><strong>Day 5:</strong> If LinkedIn connection accepted, send LinkedIn message (NOT a pitch — a short "great to connect")</li>
<li><strong>Day 8:</strong> Email 3 (reframe)</li>
<li><strong>Day 10:</strong> Phone call attempt (voicemail if no answer)</li>
<li><strong>Day 13:</strong> Email 4 (case study)</li>
<li><strong>Day 15:</strong> Second phone call attempt</li>
<li><strong>Day 20:</strong> LinkedIn DM (if connected)</li>
<li><strong>Day 22:</strong> Email 5 (breakup)</li>
</ul>

<p>Total: 5 emails, 2 LinkedIn touches, 2 phone attempts. Over 3 weeks.</p>

<h2>LinkedIn strategy</h2>

<h3>Connection request</h3>
<p>Personalized note, not blank.</p>

<div class="prompt-box">
<div class="prompt-box-label">LinkedIn connection note</div>
<button class="copy-btn">Copy</button>
<pre>Hi [name] - saw your post on [specific topic], wanted to connect. Not pitching anything, would be interested in comparing notes on [related area]. - Sam</pre>
</div>

<h3>Post-connection message</h3>
<p>Wait 2-3 days after accept. Then send a brief message referencing something about them. NOT a pitch.</p>

<div class="prompt-box">
<div class="prompt-box-label">LinkedIn post-connection</div>
<button class="copy-btn">Copy</button>
<pre>[name] - thanks for connecting. Wanted to share a quick thought on [topic from their post / profile] since it resonated. [One sentence of value.]

Happy to dig in further if useful. Otherwise looking forward to seeing your work pop up in my feed.</pre>
</div>

<h3>LinkedIn DM later in sequence</h3>
<p>If email sequence is mid-flight and no reply, a short LinkedIn DM as a "different channel" bump.</p>

<div class="prompt-box">
<div class="prompt-box-label">LinkedIn sequence bump</div>
<button class="copy-btn">Copy</button>
<pre>[name] - emailed a few times re: [topic], not sure it's landing. Probably easier to ask here: is [topic] even a priority this quarter? Either way is fine - just want to make sure I'm reaching you on the right channel.</pre>
</div>

<h2>Phone strategy</h2>

<p>Not everyone answers unknown numbers. But voicemail is a touch. Voicemail left with purpose = another impression.</p>

<h3>Voicemail script</h3>

<div class="prompt-box">
<div class="prompt-box-label">Cold voicemail</div>
<button class="copy-btn">Copy</button>
<pre>Hi [name], this is Sam from [company]. Trying to catch you before Friday on the [topic] thing I emailed about — the short version is [one sentence].

I'll follow up by email. If you want to cut the back-and-forth, my direct is [number]. Thanks [name].</pre>
</div>

<p>Key elements:</p>
<ul>
<li>Say their name at start and end (triggers attention when played back)</li>
<li>One-sentence purpose (not full pitch)</li>
<li>Set up the follow-up email</li>
<li>Leave direct number</li>
<li>Under 25 seconds</li>
</ul>

<h3>Second phone attempt</h3>
<p>5-7 days after first. Different time of day. If still no answer, stop calling — you've left your mark.</p>

<h2>The channel priority rules</h2>
<ul>
<li><strong>Email:</strong> workhorse. Most touches. Full pitch + ask.</li>
<li><strong>LinkedIn:</strong> warming layer. Soft touches. Builds familiarity.</li>
<li><strong>Phone:</strong> high-signal. Rarely converts cold but leaves a memorable impression.</li>
<li><strong>SMS:</strong> avoid for cold B2B. Feels invasive. Reserve for warm / known prospects.</li>
</ul>

<h2>The orchestration tooling</h2>
<p>Running multi-channel manually is a nightmare. Tools that handle it:</p>
<ul>
<li><strong>Salesloft, Outreach:</strong> enterprise SDR orchestration. Email + phone + tasks.</li>
<li><strong>Instantly, Smartlead:</strong> email-first but LinkedIn integrations improving.</li>
<li><strong>Reply.io, Apollo:</strong> native multi-channel.</li>
<li><strong>LinkedIn automation tools (Dux-Soup, Waalaxy):</strong> for the LinkedIn leg. Use carefully — LinkedIn aggressively limits automation.</li>
</ul>

<h2>The compliance angle</h2>
<p>Multi-channel doesn't escape compliance rules:</p>
<ul>
<li>Do-not-contact propagates across all channels. One unsubscribe = stop email, LinkedIn, phone.</li>
<li>Phone: follow TCPA rules (no auto-dial without consent in many cases).</li>
<li>LinkedIn: respect LinkedIn's own automation limits.</li>
</ul>

<p>Track opt-outs in one unified place. "Remove me" in email equals "don't message on LinkedIn" equals "don't call."</p>
""",
    prev=("The breakup email", "breakup.html"),
    nxt=("Sequence length", "length.html"),
)


write_cold_page(
    slug="sequences/length",
    title="Sequence length",
    description="3 emails? 5? 10? Here's how to think about the right number of touches.",
    reading_time=3,
    body_html="""
<p class="lede">The right number of emails in a sequence depends on deal size, cycle length, and your patience. Most B2B teams default to 5-7 touches. Below 3 and you leave money on the table. Above 10 and you annoy your ICP.</p>

<h2>The standard by context</h2>

<h3>SMB (under $3K ACV, short cycles)</h3>
<p>3-5 emails over 10-14 days. Impulse buyers decide fast. Long sequences waste tokens.</p>

<h3>Mid-market ($3K-$30K ACV)</h3>
<p>5-7 emails over 21-28 days. Standard default.</p>

<h3>Enterprise ($30K+, long cycles)</h3>
<p>7-12 emails over 6-10 weeks. Multiple stakeholders, longer decision windows.</p>

<h3>High-touch partnerships</h3>
<p>3-5 emails over 10-14 days, then pause. Re-engage 3-6 months later with new angle. Repeat.</p>

<h2>Reply rate by email position (B2B typical)</h2>

<ul>
<li>Email 1: 2-4% reply rate</li>
<li>Email 2: 1-2%</li>
<li>Email 3: 1-2%</li>
<li>Email 4: 1-2%</li>
<li>Email 5 (breakup): 2-4% (often highest)</li>
<li>Email 6+: diminishing returns, under 1%</li>
</ul>

<p>Aggregate 5-touch reply rate: 8-15%. Most teams stop adding touches after 5-7 because the yield drops sharply.</p>

<h2>The diminishing returns curve</h2>
<p>Adding email 6 to a 5-touch sequence adds about 0.5-1% more reply rate. Email 7: 0.2-0.5%. Email 8+: marginal.</p>

<p>But each additional email burns more sender reputation, more list goodwill, more annoyance risk. The ROI per touch drops dramatically after email 5-6.</p>

<h2>When longer sequences make sense</h2>

<ul>
<li>High-value targets ($100K+ ACV) where each reply is worth 6 months of pipeline</li>
<li>Named accounts in ABM motions (you're going to work them for a year anyway)</li>
<li>Enterprise cycles where multiple stakeholders need to see you reach out multiple times</li>
<li>Industries with slow decision-making (government, healthcare, education)</li>
</ul>

<h2>When shorter sequences make sense</h2>

<ul>
<li>Impulse B2C-adjacent offers (below $1K)</li>
<li>High-volume low-conversion plays (where the unit economics demand fast cycles)</li>
<li>Very targeted outreach with high intent signals (already researching, just need the nudge)</li>
<li>When your list is small and you want to re-engage in future instead of hammering now</li>
</ul>

<h2>The re-engagement strategy</h2>
<p>After the 5-touch sequence ends, don't delete non-responders. Wait 3-6 months. Re-engage with:</p>

<ul>
<li>New angle (different pain, new product feature, new case study)</li>
<li>New trigger (they just got funded, hired, changed roles)</li>
<li>Fresh sender identity (different first name if your team has multiple personas)</li>
</ul>

<p>Many deals close on re-engagement 8-12 months after first outreach.</p>

<h2>The "never-ending sequence" anti-pattern</h2>
<p>Some operators set up sequences that never end — automated bumps every 2 weeks forever. Don't.</p>

<ul>
<li>Annoyance compounds</li>
<li>Email gets marked as spam eventually</li>
<li>Your sender reputation suffers</li>
<li>The prospect remembers you negatively</li>
</ul>

<p>A clean 5-touch sequence, clean breakup, clean re-engagement 6 months later beats perpetual nagging every time.</p>

<h2>Testing sequence length</h2>

<div class="prompt-box">
<div class="prompt-box-label">A/B testing sequence length</div>
<button class="copy-btn">Copy</button>
<pre>Split 1000 prospects in half:
- Group A: 5-touch sequence
- Group B: 7-touch sequence

Measure:
- Total reply rate
- Positive reply rate
- Meetings booked
- Spam complaints
- Unsubscribe rate

Run 4-6 weeks. Calculate per-email marginal contribution. Pick the length where adding another email adds less than 0.5% reply rate and increases complaints or unsubscribes.</pre>
</div>
""",
    prev=("Multi-channel orchestration", "multi-channel.html"),
    nxt=("Testing methodology", "../testing/methodology.html"),
)

print("\n✓ Cold Email Part 3: Copy (7) + Sequences (5) = 12 pages")
