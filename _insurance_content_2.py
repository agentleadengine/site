#!/usr/bin/env python3
"""Insurance playbook content - Part 2: Modules 6-10."""
from _build_insurance import write_playbook_page


# ============================================================
# MODULE 6 - Blog posts + SEO
# ============================================================

m6 = """
<p>A blog is the longest-lasting marketing asset you can build. Unlike a social post that dies in 48 hours or an email that's read once, a blog post that ranks for the right search drives leads for years. This module: how to use Claude to generate blog content that actually ranks, brings in local search traffic, and converts visitors into calls.</p>

<h2>What kind of blog posts to write</h2>
<p>Not "5 Tips for Insurance Savings." Those posts already exist, rank well, and are written by companies with more SEO authority than you. Pick topics where you can win:</p>

<ul>
<li><strong>Local intent:</strong> "Medicare Advantage plans in [your city]" / "best home insurance in [state] for older homes"</li>
<li><strong>Specific scenarios:</strong> "Life insurance for diabetics" / "How much coverage does a small restaurant really need?"</li>
<li><strong>Decision-stage questions:</strong> "Should I stay on Medicare Advantage or switch to Original Medicare?" / "Final expense vs. whole life for a 68-year-old"</li>
<li><strong>Compare-and-contrast:</strong> "HDHP vs. PPO for a family of four" / "Term vs. permanent life for a 40-year-old homeowner"</li>
<li><strong>Your actual expertise:</strong> If you specialize (teachers, contractors, real estate agents, diabetics, high-net-worth), write for that niche specifically</li>
</ul>

<h2>Step 1: Find the actual queries people search</h2>

<div class="prompt-box">
<div class="prompt-box-label">Keyword + question generator</div>
<button class="copy-btn">Copy</button>
<pre>I sell [insurance line] to [audience] in [geography].

Generate 30 specific search queries a potential client might type into Google when they're researching this topic. Include:

- 10 "question" queries ("how much life insurance should I have at 45?")
- 10 local-intent queries ("Medicare advisor in [city]" style)
- 5 "comparison" queries ("whole life vs term for a parent")
- 5 "problem" queries ("can I get life insurance with type 2 diabetes?")

Then group them by search intent: informational, commercial investigation, transactional.

For each group, suggest 3 blog post titles that could serve that intent cluster.</pre>
</div>

<p>Take the titles Claude generates, verify a few in Google to see what already ranks, and pick 3-5 to write.</p>

<h2>Step 2: The blog post outline</h2>

<div class="prompt-box">
<div class="prompt-box-label">Blog post outline</div>
<button class="copy-btn">Copy</button>
<pre>Write an outline for a blog post titled "[your title]".

Audience: [specific - "40-60 year old parents in [state] who have term life coming up for renewal"]
Search intent: [informational / comparison / transactional]
Primary keyword: [the main phrase from keyword research]
Secondary keywords: [3-5 related phrases]

Outline structure:
- H1 (title, keyword naturally included)
- Intro (2 paragraphs, set up the reader's actual question)
- 4-6 H2 sections covering the reader's real questions in order
- Each H2 gets 2-3 H3s
- Conclusion: summary + CTA (book call / get quote / learn more)

Notes on angle:
- Where a specific number, local detail, or personal experience would strengthen a section, flag it with "[INSERT: ...]" so I can add it
- Anticipate the 3 objections or follow-up questions a reader would have and make sure the outline covers them
- Think about what a competitor article is missing - that's where we win

Just the outline, not the full post yet.</pre>
</div>

<h2>Step 3: Write the post from the outline</h2>

<div class="prompt-box">
<div class="prompt-box-label">Blog post writer</div>
<button class="copy-btn">Copy</button>
<pre>Using the outline above, write the full blog post.

Length: 1200-1800 words (whatever the topic actually needs - don't pad)
Voice: [see voice samples; plainspoken, no fluff]
Formatting:
- Short paragraphs (2-4 sentences)
- Use H2 and H3 for structure (readability and SEO)
- Bullet lists where comparison matters
- Bold the single most important sentence in each section
- Include at least one concrete example or anonymized scenario
- End with a clear CTA

Don't:
- Say "in today's fast-paced world" or similar padding
- Use "when it comes to" as a transition
- Start paragraphs with "However," "Furthermore," "Moreover"
- Make claims I can't back (keep claims conservative and specific)

At the end, flag:
- Places I need to add local data or my own example
- Any statistics you used that I should verify before publishing
- Compliance issues to review (use the compliance pre-check pattern)</pre>
</div>

<h2>The on-page SEO checklist</h2>
<p>Claude can help, but the publishing step matters. When you publish:</p>

<div class="checklist">
<div class="checklist-item">
<input type="checkbox" id="m6-seo-1" data-key="m6-seo-1">
<label for="m6-seo-1">Title tag ≤ 60 characters, keyword near the front</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m6-seo-2" data-key="m6-seo-2">
<label for="m6-seo-2">Meta description 140-160 characters, keyword included, written to drive clicks</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m6-seo-3" data-key="m6-seo-3">
<label for="m6-seo-3">URL slug is short and keyword-rich (not /post-123)</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m6-seo-4" data-key="m6-seo-4">
<label for="m6-seo-4">Primary keyword in H1, first 100 words, at least one H2</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m6-seo-5" data-key="m6-seo-5">
<label for="m6-seo-5">Internal links to 2-3 other pages on your site</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m6-seo-6" data-key="m6-seo-6">
<label for="m6-seo-6">One external link to an authoritative source (CMS, NAIC, state DOI, carrier - not a competitor)</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m6-seo-7" data-key="m6-seo-7">
<label for="m6-seo-7">Author bio at the top or bottom with your name, title, state(s) licensed</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m6-seo-8" data-key="m6-seo-8">
<label for="m6-seo-8">Schema markup (use Yoast, Rank Math, or equivalent - "Article" or "LocalBusiness" schema)</label>
</div>
</div>

<p>Get the meta title and description from Claude:</p>

<div class="prompt-box">
<div class="prompt-box-label">Meta title + description</div>
<button class="copy-btn">Copy</button>
<pre>For the blog post below, write:

1. A title tag: 55-60 characters, primary keyword near the front, compelling enough to click
2. A meta description: 140-160 characters, includes primary keyword, promises value, has implicit or explicit CTA
3. 5 potential URL slugs (short, keyword-rich, lowercase-with-hyphens)

Give me 3 options for title and 3 for description so I can choose.

[Paste the full post]</pre>
</div>

<h2>Local SEO: the thing insurance agents win at</h2>
<p>Unlike big insurance companies with national authority, you have one advantage: local intent. Write for your city, your county, your state. Every blog post should mention your location specifically - in the title when relevant, in the body, in the CTA, in the author bio.</p>

<div class="prompt-box">
<div class="prompt-box-label">Local content angle finder</div>
<button class="copy-btn">Copy</button>
<pre>I serve clients in [specific geography]. My base topic is [topic].

Give me 10 blog post ideas that tie the base topic to my specific location. Ideas that would rank for "[topic] + [location]" searches.

Examples of local angles:
- Specific regulatory quirks in my state
- Demographic trends in my city/county
- Local employers with particular benefits situations
- Climate/geography-specific issues (hurricane, flood, wildfire)
- Local community events/demographics

Each idea should include:
- Proposed post title
- Primary local keyword phrase
- Why this post would win locally (what's missing in current results)</pre>
</div>

<h2>The "content cluster" strategy</h2>
<p>Single posts are fine. Clusters rank better. A cluster = one "pillar" post (broad) + 5-10 "supporting" posts (specific), all linking to each other.</p>

<div class="prompt-box">
<div class="prompt-box-label">Cluster builder</div>
<button class="copy-btn">Copy</button>
<pre>Build a content cluster for my site around the topic "[broad topic]".

Output:
- 1 pillar post title + brief description (the broad, authoritative post)
- 8 supporting post titles, each covering a specific narrow sub-topic
- For each supporting post, note which sections it would link TO in the pillar

Structure should look like a hub-and-spoke. The pillar links out to all supporting posts; each supporting post links back to the pillar and 1-2 other related supporting posts.

Topic: [your topic]
Audience: [your audience]
Geography: [if applicable]</pre>
</div>

<p>Write the pillar first. Then write 1-2 supporting posts per month. After 6 months, you have a content cluster that collectively outranks any single-post competitor.</p>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item">
<input type="checkbox" id="m6-1" data-key="m6-1">
<label for="m6-1">Run the keyword generator for your primary insurance line + location. Pick 1 blog post topic.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m6-2" data-key="m6-2">
<label for="m6-2">Generate the outline. Review, add your specific angles and local details.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m6-3" data-key="m6-3">
<label for="m6-3">Generate the full post. Edit. Add your own examples. Publish.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m6-4" data-key="m6-4">
<label for="m6-4">Build the on-page SEO (title, meta, schema). Request Google indexing via Search Console.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m6-5" data-key="m6-5">
<label for="m6-5">Commit to 1 blog post per week for 12 weeks. See what happens to organic traffic.</label>
</div>
</div>
"""

write_playbook_page(
    slug="module-06",
    title="Blog posts + SEO",
    tag="Module 6",
    subtitle="Blog content that ranks locally, answers what prospects actually search, and compounds into a traffic source that pays for years.",
    body_html=m6,
)


# ============================================================
# MODULE 7 - Video scripts
# ============================================================

m7 = """
<p>Video is the highest-converting marketing asset an insurance agent can make. Prospects build trust with a face and voice dramatically faster than with text alone. But most agents freeze when the camera turns on because they don't have a script. This module fixes that.</p>

<h2>Types of videos to make</h2>

<ul>
<li><strong>Explainer (60-90 seconds):</strong> One concept explained clearly. "What's the difference between Medicare Advantage and Supplement?" Post to YouTube, embed on blog, use in email.</li>
<li><strong>FAQ shorts (30-60 seconds):</strong> Answer one question per video. Built for TikTok, Instagram Reels, YouTube Shorts.</li>
<li><strong>Personal intro (90 seconds):</strong> Your "about" video. Runs on your website, email signature, LinkedIn.</li>
<li><strong>Case study (2-3 minutes):</strong> Anonymized client story. Long-form credibility.</li>
<li><strong>Loom for prospects (unscripted but structured):</strong> Record a personalized video for a specific prospect. Huge reply rates.</li>
</ul>

<h2>The explainer script (60-90 seconds)</h2>

<div class="prompt-box">
<div class="prompt-box-label">Explainer video script</div>
<button class="copy-btn">Copy</button>
<pre>Write a 60-90 second video script for me (licensed [line] agent in [state]).

Topic: [e.g., "How Medicare Advantage and Medicare Supplement actually differ"]

Format:
[0-5s] Hook - one sentence that earns the next 85 seconds
[5-15s] Set up the problem or question
[15-50s] The main content - 2-3 key points
[50-75s] What this means for the viewer
[75-90s] Soft CTA - "If you want to talk through your specific situation, link in bio / DM me / book a call"

Constraints:
- First-person, conversational - like I'm explaining to a friend
- Sentences short enough to say in one breath
- No insurance jargon without an instant plain-language translation
- Specific over general (use numbers, scenarios, named situations)
- Do NOT guarantee returns, quote specific rates, or compare competitors by name

Format the script with timestamps and any suggested B-roll or on-screen text in brackets.</pre>
</div>

<h2>FAQ shorts script</h2>
<p>For Reels, TikTok, Shorts. Very tight. 30-60 seconds max.</p>

<div class="prompt-box">
<div class="prompt-box-label">FAQ short script (30-60s)</div>
<button class="copy-btn">Copy</button>
<pre>Give me 10 FAQ-style short video scripts.

Each script:
- 30-60 seconds (roughly 70-140 spoken words)
- Hook in first 3 seconds - just the question, posed as the viewer would ask it
- Answer in plain language
- One specific concrete example or number
- Close with "Follow for more / DM if this applies to you"

Topic pool: [your insurance line]
Example question styles:
- "Can I get life insurance if I have [condition]?"
- "What's the real difference between X and Y?"
- "How much [coverage] do I really need?"
- "What happens if I [common scenario]?"

Number them 1-10. Each should be fully shootable without needing edits.</pre>
</div>

<h2>Personal intro video</h2>
<p>Every agent should have a 90-second "about me" video on their website and email signature. Here's the script.</p>

<div class="prompt-box">
<div class="prompt-box-label">Personal intro video</div>
<button class="copy-btn">Copy</button>
<pre>Write a 90-second personal intro video script for me.

My details (from context above): [name, lines, state, specialty, years, why I do this]

Structure:
[0-10s] Who I am, what I do (one sentence each)
[10-25s] The specific type of client I help best
[25-50s] Why I got into this - the moment, person, or reason that actually matters to me
[50-75s] How I work differently (the one or two things that separate me)
[75-90s] How to connect - specific next step

Tone: warm but not corny. Don't sound scripted. Contractions. Short sentences.

Do NOT include:
- "I am committed to providing..."
- "With years of experience..."
- Any phrase that sounds like a template
- Promises about specific outcomes or savings</pre>
</div>

<h2>Case study video</h2>

<div class="prompt-box">
<div class="prompt-box-label">Case study video (2-3 min)</div>
<button class="copy-btn">Copy</button>
<pre>Write a 2-3 minute video script telling an anonymized client story.

Their situation (I'll fill in): [describe the client and the problem]

Structure:
[0-15s] Hook: the problem in one sentence
[15-45s] Who the client was (general description, no identifying details)
[45-90s] What they'd tried that wasn't working
[90-150s] What we figured out and how
[150-180s] The outcome (realistic, not hyperbolic)

Do NOT:
- Name the client
- Give identifying details (company, condition, specific amounts if sensitive)
- Promise similar results for everyone
- Include testimonial quotes unless I paste them in

Include: a disclaimer line at the end - "Every situation is different. If you want to talk through yours, [contact info]."</pre>
</div>

<h2>Loom for prospects - the highest-converting video you'll make</h2>
<p>A personalized video for a specific prospect. Huge response rates. Not scripted word-for-word, but worth having a structure.</p>

<div class="prompt-box">
<div class="prompt-box-label">Personalized prospect Loom script</div>
<button class="copy-btn">Copy</button>
<pre>Give me a 5-bullet structure for a 90-second Loom video I'm sending to a specific prospect.

About the prospect:
- [Name, role, situation from LinkedIn or intake]
- [Trigger: why I'm reaching out now]
- [What I think they might need]

5-bullet structure:
1. Open with their name + one specific detail about their situation (5 seconds)
2. What I noticed that made me reach out (15 seconds)
3. The thing I think they might not have considered (30 seconds)
4. Not a pitch - an offer to be useful (20 seconds)
5. Specific next step (15 seconds, low-friction)

Also give me the 6-line email I'd send with the video embedded.</pre>
</div>

<h2>B-roll, captions, and on-screen text</h2>
<p>Modern short-form video needs captions (80% of social video is watched muted). Claude can generate captions from your script.</p>

<div class="prompt-box">
<div class="prompt-box-label">Caption generator</div>
<button class="copy-btn">Copy</button>
<pre>Take the video script below. Format as captions for on-screen text.

Rules:
- Each caption chunk: 3-6 words, one per visible frame
- Punctuation sparingly
- Match the rhythm of spoken delivery
- Separate each chunk with "|"

[Paste your script]</pre>
</div>

<h2>The hardest part isn't the script</h2>
<p>It's getting in front of the camera. Two tricks that help:</p>
<ul>
<li><strong>Batch record.</strong> Don't record one video at a time. Block an hour, record 5-8 short videos back-to-back. Same outfit, same lighting, different topics.</li>
<li><strong>Teleprompter app.</strong> Use BIGVU, Teleprompter Premium, or your phone's built-in teleprompter. Script the key sentences (hook, close) and improvise the middle.</li>
</ul>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item">
<input type="checkbox" id="m7-1" data-key="m7-1">
<label for="m7-1">Generate 10 FAQ short scripts using the prompt above.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m7-2" data-key="m7-2">
<label for="m7-2">Pick 3 you actually want to shoot this week. Block 30 minutes, record all three in a row.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m7-3" data-key="m7-3">
<label for="m7-3">Write your personal intro script. Shoot it. Put it on your website and LinkedIn.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m7-4" data-key="m7-4">
<label for="m7-4">Commit to one batched recording session per week for 6 weeks. Measure views and DMs.</label>
</div>
</div>
"""

write_playbook_page(
    slug="module-07",
    title="Video scripts",
    tag="Module 7",
    subtitle="Scripts for explainers, FAQ shorts, personal intros, case studies, and personalized Looms. The fastest way to build trust at scale.",
    body_html=m7,
)


# ============================================================
# MODULE 8 - Direct mail
# ============================================================

m8 = """
<p>Direct mail isn't dead - it's just that everyone else gave up on it, which is exactly why it works again. For Medicare, final expense, and local P&amp;C, a well-designed postcard or letter still produces leads when email and ads don't. Claude makes the copy part easy.</p>

<h2>When direct mail is worth running</h2>
<ul>
<li><strong>Medicare T-65 mailings:</strong> still very effective, even though every other agent is doing it. The difference is in the copy and list.</li>
<li><strong>Final expense to age 50-75:</strong> strong demographic fit with direct mail habits.</li>
<li><strong>Home/auto bundle at renewal triggers:</strong> when you can time it to their renewal month.</li>
<li><strong>Business owner commercial:</strong> oversized postcard or lumpy mail beats email for executives.</li>
<li><strong>Re-activation to old clients/leads:</strong> birthdays, policy anniversaries.</li>
</ul>

<h2>The format choices</h2>
<ul>
<li><strong>Standard postcard (4x6, 6x9):</strong> Cheapest. Gets opened because there's nothing to open. Limited copy space.</li>
<li><strong>Oversized postcard (6x11, 9x12):</strong> More visible in the mailbox stack. More copy room.</li>
<li><strong>Sales letter (1-2 page letter in #10 envelope):</strong> Classic direct response. Higher printing cost, much longer copy.</li>
<li><strong>Lumpy mail (padded envelope with small item):</strong> Expensive per piece, unbeatable open rate for commercial or high-value personal.</li>
</ul>

<h2>The copy structure that works</h2>

<div class="prompt-box">
<div class="prompt-box-label">Postcard copy (medicare T-65 example)</div>
<button class="copy-btn">Copy</button>
<pre>Write copy for a 6x11 postcard mailer for Medicare T-65 prospects.

Target: people turning 65 in the next 90 days, living in [state/county].

Required elements:
- Front: 1 headline + 1 supporting line. Under 15 words total.
- Back: 4-6 short sections

Front should stop them from throwing it away in 2 seconds.

Back sections:
1. Short opening - acknowledge they're getting a ton of Medicare mail
2. The problem with most of it (generic, pushes one plan)
3. What's different about me (shop multiple carriers, explain tradeoffs)
4. One specific local detail (e.g., "in [county], the top 3 MA plans vary wildly in Rx coverage")
5. The offer: 20-minute no-pressure call
6. CTA: phone number + URL with a call-tracking number

MUST include CMS compliance:
- "We do not offer every plan available in your area. Any information we provide is limited to those plans we do offer in your area. Please contact Medicare.gov or 1-800-MEDICARE to get information on all of your options."
- "Not affiliated with Medicare or any government agency."

Write it as if it's mail from a real person, not from a company. Warm tone, specific, zero fluff.</pre>
</div>

<h2>The sales letter format (longer form)</h2>

<div class="prompt-box">
<div class="prompt-box-label">1-page sales letter</div>
<button class="copy-btn">Copy</button>
<pre>Write a 1-page sales letter for [insurance line] to [audience].

Format: handwritten-style envelope, typed letter inside, personal tone throughout.

Structure (matches classical direct-response):
- Top: date + "Dear [Name]" (will be mail-merged)
- Opening paragraph: a specific observation or question the reader is likely thinking about
- Story paragraph: short, anonymized story of a similar person
- The offer: what you want to do for them
- Proof: 2-3 specific, defensible facts about you/your track record
- Urgency: a real reason for now (renewal season, enrollment window, life-stage trigger)
- CTA: call or reply
- P.S.: restate the core offer + most important reason to act now

Length: 250-400 words. Feel like a letter from a neighbor, not from an insurance company.

Include compliance disclaimers appropriate for [line].</pre>
</div>

<h2>The envelope matters</h2>
<p>The envelope is the first filter. Most direct mail dies in the envelope. Claude won't design your envelope, but it will write copy that can go on one.</p>

<div class="prompt-box">
<div class="prompt-box-label">Envelope teaser copy</div>
<button class="copy-btn">Copy</button>
<pre>Give me 5 different teaser copy options for the front of a #10 envelope mailing for [audience] about [topic].

Each teaser:
- Under 10 words
- Passes the "looks like personal mail, not ad" test
- Creates curiosity without being clickbait
- Is defensible (nothing that overpromises)

Examples of the style I'm going for:
- "A note about your Medicare options"
- "[Name], please open - not another marketing piece"
- "Regarding your October renewal"
- "[County] homeowners: specific question inside"

Give me 5 distinct angles.</pre>
</div>

<h2>The call-tracking piece</h2>
<p>Direct mail without tracked attribution is guessing. Every piece gets a unique phone number (use CallRail, CallTrackingMetrics, or similar) or URL. Claude can help with the UTM + short-URL content.</p>

<div class="prompt-box">
<div class="prompt-box-label">Trackable CTA variants</div>
<button class="copy-btn">Copy</button>
<pre>Give me 5 different CTAs for a direct mail piece, each with a slightly different framing:

1. "Call now" style - urgency-forward
2. "Request the free [resource]" style - lead magnet
3. "Get your personalized [thing]" style - benefit-forward
4. "Reply card" style - for a letter with a BRE
5. "Visit [URL] and answer 3 questions" style - website intent

Each should include a clear phone number placeholder and URL placeholder. Tone: neighborly, not pushy.</pre>
</div>

<h2>List quality matters more than copy quality</h2>
<p>For Medicare, working with a list house is standard: Target Marketing Services, Exclusive Solutions, LifeLine Lists. For final expense, same story. For P&amp;C, you're usually using your own CRM + renewal data or local data lists.</p>

<p>No amount of good copy saves a bad list. Before you invest in design and printing, validate the list has the right age/trigger/geography.</p>

<h2>Compliance notes specific to direct mail</h2>

<div class="callout warning">
<div class="callout-title">Medicare</div>
<p>CMS mandates specific disclaimers on every marketing piece. Every state DOI has its own rules. Your carrier's compliance team will review pieces before you mail - use that process, don't skip it.</p>
</div>

<div class="callout warning">
<div class="callout-title">Life and annuity</div>
<p>State DOIs have specific rules about guarantees, past-performance claims, and superlatives. When in doubt, say less. Claude's pattern 10 catches obvious issues but isn't a substitute for your compliance desk.</p>
</div>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item">
<input type="checkbox" id="m8-1" data-key="m8-1">
<label for="m8-1">Pick ONE campaign (Medicare T-65, final expense, home renewal, etc.). Define the audience and the offer.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m8-2" data-key="m8-2">
<label for="m8-2">Generate both postcard copy and letter copy using the prompts. Pick your format.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m8-3" data-key="m8-3">
<label for="m8-3">Set up call tracking with a unique number for this campaign.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m8-4" data-key="m8-4">
<label for="m8-4">Get compliance review from carrier/IMO before mailing.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m8-5" data-key="m8-5">
<label for="m8-5">Mail a test batch of 500-1000. Measure response. Iterate copy and list before scaling.</label>
</div>
</div>
"""

write_playbook_page(
    slug="module-08",
    title="Direct mail",
    tag="Module 8",
    subtitle="Postcards, sales letters, and envelope teasers that actually get opened. Direct response still works - especially because everyone else quit.",
    body_html=m8,
)


# ============================================================
# MODULE 9 - Referral requests
# ============================================================

m9 = """
<p>Referrals are the highest-margin business you'll ever write. They close faster, cost nothing to acquire, and retain better. Most agents are terrible at asking for them - not because they don't know they should, but because they don't know exactly what to say and when. This module fixes that.</p>

<h2>The psychology of a good referral ask</h2>
<p>Bad referral asks feel awkward because they put the client on the spot with a vague request. "Do you know anyone who needs insurance?" - impossible to answer. The brain shuts down.</p>

<p>Good referral asks do three things:</p>
<ol>
<li>Specify exactly who you help (so the client can pattern-match)</li>
<li>Ask in a moment when the client is feeling gratitude or pride</li>
<li>Make it easy to say yes (warm intro script, specific names to think of)</li>
</ol>

<h2>When to ask</h2>
<ul>
<li>Right after a claim gets paid or handled well</li>
<li>Right after a policy delivers (new business)</li>
<li>Right after annual review if it went well</li>
<li>Right after you saved them money or improved coverage</li>
<li>Right after a life event where you were useful (new baby, home purchase, retirement)</li>
</ul>

<p>Not random. Not "every quarter." At a moment when the relationship is at a peak.</p>

<h2>The in-person / phone ask</h2>

<div class="prompt-box">
<div class="prompt-box-label">Verbal referral ask</div>
<button class="copy-btn">Copy</button>
<pre>Write me a 4-5 sentence referral ask I can use verbally (phone or in-person) with a client right after a positive interaction.

Details:
- I help [specific niche - e.g., "retiring teachers with Medicare decisions" or "small business owners with key-person life"]
- The moment: [e.g., we just completed their annual review, or we just paid out a claim]

The ask should:
- Start with gratitude for the current client moment (specific, not generic)
- Name exactly the type of person I can help
- Give them a specific person or situation to think of ("a friend whose spouse is turning 65," "another business owner in your network")
- Make the handoff easy - ask for permission to reach out, not for them to do the selling
- Feel natural, not scripted

Write 2 versions with slightly different framings so I can pick what feels right.</pre>
</div>

<h2>The follow-up email after getting a name</h2>

<div class="prompt-box">
<div class="prompt-box-label">Warm intro email to client</div>
<button class="copy-btn">Copy</button>
<pre>My client [Client First Name] said I could reach out to [Prospect First Name], a [relationship - friend, family, colleague].

Write a short email for me to send to [Client First Name] confirming the handoff and giving them a template to forward.

Section 1 (to my client):
- Thank them again
- Confirm I'll reach out in the next day or two
- Offer them a forward-able intro

Section 2 (for them to forward - a separate block they can copy):
- Short, from them to their friend
- Says why they thought of them (one sentence)
- Introduces me in one sentence
- Suggests their friend connect with me for a 15-minute chat (no pressure)

Total: under 200 words. Very low-friction.</pre>
</div>

<h2>The cold-to-the-referred-person email</h2>

<div class="prompt-box">
<div class="prompt-box-label">Introduction email to the referred prospect</div>
<button class="copy-btn">Copy</button>
<pre>Write an email I send to a person who was referred to me by [Referring Client First Name].

Context: [Referring Client] is my client, they mentioned [Prospect First Name] might benefit from talking to me about [specific topic: e.g., Medicare, life insurance for kids, business coverage].

Structure:
- Subject: mention [Referring Client's] name
- First line: name the referrer and the specific reason they thought of this person
- 2-3 sentences: what I do, briefly
- 1-2 sentences: no pressure, just want to say hi and see if there's a fit
- Soft CTA: offer a 15-minute call - make two specific times available

80-120 words. Tone: warm, casual, zero pressure. This is a warm intro, not a cold pitch.</pre>
</div>

<h2>The "thank the referrer" thank-you</h2>

<div class="prompt-box">
<div class="prompt-box-label">Thank-you note for referrer</div>
<button class="copy-btn">Copy</button>
<pre>Write a short handwritten-style thank-you note (6-10 sentences) I'll send to my client who referred [Prospect First Name] to me.

Structure:
- Specific thank you for the referral
- One line about what made the connection feel right
- Reference something specific about my client (not generic "you're such a good client")
- Note that the meeting with [Prospect] went well OR is scheduled
- No gifts or incentives mentioned (many states restrict gifting for referrals - I'll send separately if compliant)
- Close with something warm

This goes on actual paper in the mail. Feels personal, not corporate.</pre>
</div>

<h2>The referral partner outreach (other professionals)</h2>
<p>The highest-leverage referral source isn't existing clients - it's other professionals who work with your ideal clients: CPAs, estate attorneys, financial advisors, real estate agents, HR consultants, benefit brokers. Claude can help script those outreaches.</p>

<div class="prompt-box">
<div class="prompt-box-label">Referral partner outreach</div>
<button class="copy-btn">Copy</button>
<pre>Write an email to a [profession: CPA / estate attorney / real estate agent / HR consultant] in my local market. Goal: build a reciprocal referral relationship.

Structure:
- Subject: specific, suggests the email is about them, not me
- Open: a specific detail about their work or firm (something you'd actually research)
- The bridge: why our client bases overlap ([insurance line] clients often need [their service], or vice versa)
- The offer: a 20-minute coffee or call to explore if a referral relationship makes sense
- What I bring to the table: specific (e.g., "I work with 14 Medicare carriers so your retiring clients get real options")
- Soft CTA: propose 2 specific times

Under 150 words. Not a pitch for my services. A peer-to-peer outreach.</pre>
</div>

<h2>Systematic referrals at scale</h2>
<p>Once you have the scripts, the challenge is consistency. Claude can help you build the tracking system:</p>

<div class="prompt-box">
<div class="prompt-box-label">Referral tracking template</div>
<button class="copy-btn">Copy</button>
<pre>Give me a simple spreadsheet structure I can use in Google Sheets or Airtable to track referrals.

Columns I need:
- Referrer (client name)
- Referral trigger (what prompted the ask)
- Date asked
- Names referred
- Contact info
- Outreach status (planned, contacted, meeting booked, closed, declined)
- Thank you sent (Y/N)
- Outcome (policy written, no policy, still working)
- Next touch date (if still working)

Also give me a 3-sentence description of a weekly 15-minute routine to keep this system alive - when to review it, what to act on.</pre>
</div>

<h2>Compliance notes</h2>
<div class="callout warning">
<div class="callout-title">State rules on compensation</div>
<p>Most states prohibit paying non-licensed people for insurance referrals. Some states allow nominal gifts. Check your state's Department of Insurance rules before offering any kind of referral fee or incentive. When in doubt, the referral should be based on relationship, not compensation.</p>
</div>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item">
<input type="checkbox" id="m9-1" data-key="m9-1">
<label for="m9-1">Generate the verbal referral ask. Practice saying it out loud. Refine until it feels natural.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m9-2" data-key="m9-2">
<label for="m9-2">Pick 3 clients you've had a positive interaction with recently. Call or meet, use the ask.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m9-3" data-key="m9-3">
<label for="m9-3">Set up the referral tracking spreadsheet. Block 15 minutes weekly to review and act.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m9-4" data-key="m9-4">
<label for="m9-4">Identify 3 referral partner targets (CPA, estate attorney, etc.). Send the outreach email this week.</label>
</div>
</div>
"""

write_playbook_page(
    slug="module-09",
    title="Referral requests",
    tag="Module 9",
    subtitle="The scripts, emails, and tracking system that turn referral generation from 'when I remember' into 'every week.'",
    body_html=m9,
)


# ============================================================
# MODULE 10 - Review responses
# ============================================================

m10 = """
<p>Online reviews are the modern referral. Before a prospect calls you, they Google you. If they find 3 Google reviews and one of them is a complaint with no response, you lose them before the first call. Responding to every review - positive, neutral, or negative - is one of the highest-leverage reputation moves you can make. Claude makes it a 30-second task.</p>

<h2>Where reviews matter</h2>
<ul>
<li><strong>Google Business Profile:</strong> the most important. Shows up in local search.</li>
<li><strong>Facebook:</strong> Recommendations. Still matter, especially for older demographics.</li>
<li><strong>Yelp:</strong> less important for insurance specifically, but if you have a location, it matters.</li>
<li><strong>Trustpilot, BBB, industry-specific:</strong> sometimes worth attention depending on your niche.</li>
</ul>

<p>Set up Google alerts or a tool like Birdeye or Podium to notify you when a new review comes in.</p>

<h2>Responding to 5-star reviews</h2>

<div class="prompt-box">
<div class="prompt-box-label">5-star response</div>
<button class="copy-btn">Copy</button>
<pre>The review below is 5 stars from a client who I [specific interaction detail - e.g., helped with Medicare enrollment / placed a life policy after a chronic condition / handled a claim].

Write a 3-5 sentence response that:
- Thanks them by name (or first name only)
- References something specific from their review (not generic "thanks for the kind words")
- Briefly reinforces what I do (in case a future prospect reads it)
- Ends warmly without being saccharine

Don't say "it was our pleasure" or "we strive to provide excellent service." Sound like a real person.

REVIEW:
[Paste the review]</pre>
</div>

<h2>Responding to 4-star or neutral reviews</h2>

<div class="prompt-box">
<div class="prompt-box-label">4-star / neutral response</div>
<button class="copy-btn">Copy</button>
<pre>The review below is 3-4 stars. The client says nice things but also has constructive feedback or a mild complaint.

Write a response that:
- Thanks them for the honest feedback
- Acknowledges the specific thing they flagged, without defensiveness
- Explains what's changed or what I'd do differently (if applicable)
- Invites them to reach out directly if they want to discuss further
- Keeps it short (4-6 sentences)

Don't be defensive. Don't ignore their complaint. Don't over-apologize.

REVIEW:
[Paste the review]</pre>
</div>

<h2>Responding to 1-2 star reviews</h2>
<p>This is where most agents either panic or go silent. Both are wrong. A well-handled negative review response often does more for your brand than a dozen positive reviews. Prospects read how you respond under pressure.</p>

<div class="prompt-box">
<div class="prompt-box-label">1-2 star response</div>
<button class="copy-btn">Copy</button>
<pre>The review below is 1-2 stars and contains a complaint. It may be fair, partially fair, or unfair.

Write a public response that:
- Acknowledges their frustration without arguing facts
- Does NOT reveal any PHI or client-specific details (HIPAA/state privacy) - even if they revealed them in their review, I should NOT confirm them
- States briefly what I would try to do to resolve it (if applicable)
- Invites them to contact me directly at [phone or email] so we can address it privately
- Does not include superlatives, defensiveness, or apology-spirals
- 4-6 sentences, calm and professional

Consider: a future prospect reading this is watching how I handle pressure. That's the real audience.

REVIEW:
[Paste the review]</pre>
</div>

<div class="callout warning">
<div class="callout-title">HIPAA and state privacy</div>
<p>Never confirm a review writer is actually a client. Never acknowledge specific health conditions, claims, policies, or personal details they mentioned - even to defend yourself. Doing so can be a HIPAA violation or state privacy violation. Keep your public response general. Move specifics to a private conversation.</p>
</div>

<h2>When the review is clearly fake or from a non-client</h2>
<p>Don't engage the content. Flag it to the platform (Google, Yelp, Facebook all have dispute processes). If Google doesn't remove it, respond briefly:</p>

<div class="prompt-box">
<div class="prompt-box-label">Response to suspected fake/mistaken review</div>
<button class="copy-btn">Copy</button>
<pre>This review seems to be from a non-client or is factually unrelated to me. Write a short, professional response that:

- Politely notes I don't recognize this as a client interaction
- Invites them to contact me directly if there's been a mistake
- Does NOT accuse them of lying
- Does NOT engage the specific false claims
- 2-3 sentences max

Sound like someone who's genuinely puzzled, not defensive.</pre>
</div>

<h2>Generating reviews (without asking in a shady way)</h2>
<p>The flip side of responding is getting more reviews to begin with. The ask, again, has to happen at the right moment.</p>

<div class="prompt-box">
<div class="prompt-box-label">Review request email</div>
<button class="copy-btn">Copy</button>
<pre>Write a short email (80-120 words) asking a client to leave a Google review.

Context: [what we just did for them - specific]

Structure:
- Open with a reference to our specific recent interaction
- Ask simply: if they'd be willing to share their experience on Google
- Include the direct link placeholder
- Note it takes 60 seconds
- Offer to answer any questions, otherwise no pressure

Do NOT:
- Offer anything in exchange (compliance issue in most states for insurance)
- Ask them to rate 5 stars specifically (that's review gating and violates most platform TOS)
- Pressure or send multiple follow-ups

Simple and sincere.</pre>
</div>

<h2>The review batch workflow</h2>
<p>Don't respond to reviews one at a time. Batch them. Once a week:</p>

<ol>
<li>Pull all reviews from the last 7 days across platforms</li>
<li>Paste them (one at a time) into Claude using the appropriate prompt</li>
<li>Edit each response for tone (remove any AI-ish phrasing)</li>
<li>Post them all in one sitting</li>
</ol>

<p>15 minutes of your time, every review responded to, prospects see a responsive and attentive agent.</p>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item">
<input type="checkbox" id="m10-1" data-key="m10-1">
<label for="m10-1">Audit your current Google Business Profile. Any reviews unresponded to? Respond to all of them using the appropriate prompts.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m10-2" data-key="m10-2">
<label for="m10-2">Set up a weekly 15-minute "review response" block on your calendar.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m10-3" data-key="m10-3">
<label for="m10-3">Identify 5 clients from the last 30 days you had great interactions with. Send the review request email.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m10-4" data-key="m10-4">
<label for="m10-4">Set up Google Alerts or a review monitoring tool so you see new reviews within 24 hours.</label>
</div>
</div>
"""

write_playbook_page(
    slug="module-10",
    title="Review responses",
    tag="Module 10",
    subtitle="Response templates for 5-star, neutral, and negative reviews. The reputation work that prospects watch before they ever call.",
    body_html=m10,
)

print("\n✓ Insurance Playbook Part 2: Modules 6-10 (5 pages)")
