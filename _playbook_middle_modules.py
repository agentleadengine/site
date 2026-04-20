#!/usr/bin/env python3
"""Generates modules 4-13 (the meat) for any playbook given a profession spec."""


def middle_modules(spec):
    """
    Requires in spec:
      'profession', 'short', 'audience_description', 'typical_client',
      'email_example' (str describing a cold email scenario for this profession),
      'social_topic_examples' (list of 3-5 topic ideas),
      'blog_topic_examples' (list of 3-5 blog topics),
      'video_topic_examples' (list),
      'direct_mail_use' (str),
      'referral_triggers' (list),
      'review_platforms' (list),
      'newsletter_topic_examples' (list),
      'ad_platforms' (list),
      'client_ed_docs' (list),
    """
    profession = spec['profession']
    short = spec['short']
    typical = spec['typical_client']
    audience = spec['audience_description']

    out = []

    # ============================================================
    # Module 4 - Prospecting emails
    # ============================================================
    m4 = f"""
<p>Prospecting emails are the workhorse of modern marketing. Done right, they produce real conversations at the cost of time. Done wrong, they land in spam and never get opened.</p>

<h2>The anatomy</h2>
<ol>
<li><strong>Subject line</strong> - 3-5 words, lowercase, personal</li>
<li><strong>First line</strong> - specific to this person</li>
<li><strong>The bridge</strong> - connects their situation to your relevance</li>
<li><strong>The pitch</strong> - one specific angle, 2-3 sentences</li>
<li><strong>Proof</strong> - one specific result or detail</li>
<li><strong>The ask</strong> - clear specific next step</li>
</ol>

<h2>Target length: 70-110 words total.</h2>

<h2>Cold email for {short}</h2>

<div class="prompt-box">
<div class="prompt-box-label">Cold prospecting email</div>
<button class="copy-btn">Copy</button>
<pre>Write a cold prospecting email to a [specific audience]:
{spec['email_example']}

Goal: book a 15-min call / start a conversation.
- Under 90 words
- Subject: 4-6 words, lowercase
- First line: specific trigger
- One angle, not full pitch
- One proof point
- Specific CTA time
- Minimal signature

Do NOT use "Hope this finds you well," "I wanted to reach out," or "Take a look at our comprehensive suite."

3 versions with different hooks.</pre>
</div>

<h2>The 5-touch follow-up sequence</h2>

<div class="prompt-box">
<div class="prompt-box-label">Sequence builder</div>
<button class="copy-btn">Copy</button>
<pre>Given the first email [paste], write 5-touch sequence:
- Email 2 (day 3): bump, under 50 words
- Email 3 (day 7): soft reframe, lower-friction ask
- Email 4 (day 12): case study, anonymized, under 100 words
- Email 5 (day 20): breakup, under 40 words

Same tone. Vary openings. No "circling back" or "bumping this up."</pre>
</div>

<h2>Personalization at scale</h2>

<div class="prompt-box">
<div class="prompt-box-label">Custom first lines</div>
<button class="copy-btn">Copy</button>
<pre>For each prospect below, write ONE first line (12-20 words) that references something specific to them:
- No "hope you're well"
- No "I came across your profile"
- Be specific

PROSPECTS:
1. [Name, situation, trigger]
2. [Name, situation, trigger]
...</pre>
</div>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item"><input type="checkbox" id="m4-1" data-key="{short}-m4-1"><label for="m4-1">Generate 3 versions of a prospecting email.</label></div>
<div class="checklist-item"><input type="checkbox" id="m4-2" data-key="{short}-m4-2"><label for="m4-2">Build the 5-email sequence.</label></div>
<div class="checklist-item"><input type="checkbox" id="m4-3" data-key="{short}-m4-3"><label for="m4-3">Send to 20 prospects this week. Track replies.</label></div>
</div>
"""

    out.append({"slug": "module-04", "title": "Prospecting emails", "tag": "Module 4",
                "subtitle": "Cold email that doesn't look like cold email.", "body": m4})

    # ============================================================
    # Module 5 - Social media
    # ============================================================
    social_topics = '\n'.join([f"<li>{t}</li>" for t in spec['social_topic_examples']])
    m5 = f"""
<p>Social media for {short}s is usually generic. Recycled graphics. "Happy Monday!" posts. Nobody engages, the algorithm punishes it. Here's how to produce content that actually builds an audience.</p>

<h2>The content mix</h2>
<p>Over 10 posts:</p>
<ul>
<li>6 educational</li>
<li>2 personal</li>
<li>1 social proof</li>
<li>1 direct ask</li>
</ul>

<h2>Topic ideas for your practice</h2>
<ul>
{social_topics}
</ul>

<h2>Generate a week of posts in 15 minutes</h2>

<div class="prompt-box">
<div class="prompt-box-label">Weekly social generator</div>
<button class="copy-btn">Copy</button>
<pre>Generate 7 social media posts for this week.

Platform: [Facebook / LinkedIn / Instagram]
Audience: [from context]
Theme: [one theme]

Mix:
- 4 educational
- 1 personal
- 1 social proof
- 1 direct ask

Each post:
- 80-180 words
- First line = hook
- Plain language
- End with question or CTA
- No emojis unless they add meaning

Vary opening patterns: question, story, contrarian, number, confession. Don't use the same opening twice.

Number 1-7 with day-of-week.</pre>
</div>

<h2>The "common mistake" post</h2>

<div class="prompt-box">
<div class="prompt-box-label">Common mistake post</div>
<button class="copy-btn">Copy</button>
<pre>Write a "common mistake" post about [topic].
- Line 1: state the mistake
- Lines 2-4: why most people believe it
- Lines 5-8: the actual truth
- Last line: what to do instead

130 words. End with "Reply or DM with questions."</pre>
</div>

<h2>The repurpose trick</h2>

<div class="prompt-box">
<div class="prompt-box-label">One idea, multi-channel</div>
<button class="copy-btn">Copy</button>
<pre>Core insight: [paste]
Turn into:
1. Facebook post (120w, warm)
2. LinkedIn post (300w, pro)
3. Newsletter section (200w)
4. 60s video script
5. Tweet (240 chars)
6. SMS to a client (60w)

Adapt each to channel conventions.</pre>
</div>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item"><input type="checkbox" id="m5-1" data-key="{short}-m5-1"><label for="m5-1">Generate a full week of posts.</label></div>
<div class="checklist-item"><input type="checkbox" id="m5-2" data-key="{short}-m5-2"><label for="m5-2">Schedule them all in one sitting.</label></div>
<div class="checklist-item"><input type="checkbox" id="m5-3" data-key="{short}-m5-3"><label for="m5-3">Commit to this rhythm for 4 weeks.</label></div>
</div>
"""
    out.append({"slug": "module-05", "title": "Social media content", "tag": "Module 5",
                "subtitle": "Posts that build an audience, not recycled graphics nobody engages with.", "body": m5})

    # ============================================================
    # Module 6 - Blog + SEO
    # ============================================================
    blog_topics = '\n'.join([f"<li>{t}</li>" for t in spec['blog_topic_examples']])
    m6 = f"""
<p>A blog is the longest-lasting marketing asset you can build. A blog post that ranks drives {short} leads for years.</p>

<h2>What to write about</h2>
<ul>
{blog_topics}
</ul>

<h2>Step 1: Find queries people actually search</h2>

<div class="prompt-box">
<div class="prompt-box-label">Keyword + question generator</div>
<button class="copy-btn">Copy</button>
<pre>I'm a {short} serving [audience] in [geography].

Generate 30 search queries they might type:
- 10 question queries
- 10 local-intent queries
- 5 comparison queries
- 5 problem queries

Group by intent. For each group, suggest 3 blog titles.</pre>
</div>

<h2>Step 2: Outline before writing</h2>

<div class="prompt-box">
<div class="prompt-box-label">Blog outline</div>
<button class="copy-btn">Copy</button>
<pre>Outline for "[title]".
Audience: [specific]
Intent: [info/comparison/transactional]
Primary keyword: [phrase]

Structure:
- H1
- Intro (2 paragraphs)
- 4-6 H2 sections, each with 2-3 H3s
- Conclusion + CTA

Flag where I need local data or specific examples. Anticipate 3 objections.</pre>
</div>

<h2>Step 3: Write from the outline</h2>

<div class="prompt-box">
<div class="prompt-box-label">Blog writer</div>
<button class="copy-btn">Copy</button>
<pre>Using the outline, write the full post.
Length: 1200-1800 words
Voice: [from samples]
- Short paragraphs
- H2/H3 structure
- Bullet lists for comparisons
- Bold 1 sentence per section
- Concrete example
- Clear CTA

Avoid "in today's fast-paced world" and paragraph starts of "however/furthermore/moreover."

Flag: local data placeholders, stats to verify.</pre>
</div>

<h2>SEO basics checklist</h2>
<div class="checklist">
<div class="checklist-item"><input type="checkbox" id="m6-seo-1" data-key="{short}-m6-seo-1"><label for="m6-seo-1">Title tag under 60 characters, keyword near front</label></div>
<div class="checklist-item"><input type="checkbox" id="m6-seo-2" data-key="{short}-m6-seo-2"><label for="m6-seo-2">Meta description 140-160 characters</label></div>
<div class="checklist-item"><input type="checkbox" id="m6-seo-3" data-key="{short}-m6-seo-3"><label for="m6-seo-3">Keyword in H1, first 100 words, one H2</label></div>
<div class="checklist-item"><input type="checkbox" id="m6-seo-4" data-key="{short}-m6-seo-4"><label for="m6-seo-4">2-3 internal links</label></div>
<div class="checklist-item"><input type="checkbox" id="m6-seo-5" data-key="{short}-m6-seo-5"><label for="m6-seo-5">1 authoritative external link</label></div>
<div class="checklist-item"><input type="checkbox" id="m6-seo-6" data-key="{short}-m6-seo-6"><label for="m6-seo-6">Schema markup (Article or LocalBusiness)</label></div>
</div>

<h2>Local SEO angle</h2>
<p>Your competitive advantage: local intent. Every post should mention your geography.</p>

<div class="prompt-box">
<div class="prompt-box-label">Local content finder</div>
<button class="copy-btn">Copy</button>
<pre>I serve [geography]. Base topic: [topic].
10 blog ideas that would rank for "[topic] + [location]".
Each: title, primary local keyword, why it wins locally.</pre>
</div>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item"><input type="checkbox" id="m6-1" data-key="{short}-m6-1"><label for="m6-1">Run keyword generator. Pick 1 topic.</label></div>
<div class="checklist-item"><input type="checkbox" id="m6-2" data-key="{short}-m6-2"><label for="m6-2">Generate outline, review, write full post.</label></div>
<div class="checklist-item"><input type="checkbox" id="m6-3" data-key="{short}-m6-3"><label for="m6-3">Publish. Request indexing via Search Console.</label></div>
<div class="checklist-item"><input type="checkbox" id="m6-4" data-key="{short}-m6-4"><label for="m6-4">Commit to 1 post per week for 12 weeks.</label></div>
</div>
"""
    out.append({"slug": "module-06", "title": "Blog posts + SEO", "tag": "Module 6",
                "subtitle": "Blog content that ranks locally and brings leads for years.", "body": m6})

    # ============================================================
    # Module 7 - Video scripts
    # ============================================================
    video_topics = '\n'.join([f"<li>{t}</li>" for t in spec['video_topic_examples']])
    m7 = f"""
<p>Video builds trust faster than text. Most {short}s freeze when the camera turns on because they don't have a script. Claude fixes that.</p>

<h2>Types of video to make</h2>
<ul>
<li><strong>Explainer (60-90s)</strong> - one concept, post to YouTube / embed on blog</li>
<li><strong>FAQ shorts (30-60s)</strong> - for Reels / TikTok / Shorts</li>
<li><strong>Personal intro (90s)</strong> - for website, email signature, LinkedIn</li>
<li><strong>Case study (2-3 min)</strong> - anonymized client story</li>
</ul>

<h2>Topic ideas for your practice</h2>
<ul>
{video_topics}
</ul>

<h2>Explainer script</h2>

<div class="prompt-box">
<div class="prompt-box-label">Explainer video script (60-90s)</div>
<button class="copy-btn">Copy</button>
<pre>Write a 60-90s video script.
Topic: [topic]

[0-5s] Hook
[5-15s] Problem setup
[15-50s] 2-3 key points
[50-75s] What this means for viewer
[75-90s] Soft CTA

First person, short sentences, no jargon. Include B-roll cues and on-screen text.</pre>
</div>

<h2>FAQ shorts (10 scripts)</h2>

<div class="prompt-box">
<div class="prompt-box-label">FAQ shorts generator</div>
<button class="copy-btn">Copy</button>
<pre>10 FAQ-style short scripts.
Each: 30-60s, hook in first 3 seconds, plain-language answer, one concrete example, "Follow for more / DM if this applies" close.

Topic pool: [common {short} questions]

Numbered 1-10.</pre>
</div>

<h2>Personal intro video</h2>

<div class="prompt-box">
<div class="prompt-box-label">90s personal intro</div>
<button class="copy-btn">Copy</button>
<pre>90s personal intro video.

[0-10s] Who I am / what I do
[10-25s] Specific type of client
[25-50s] Why I do this (specific moment)
[50-75s] How I'm different
[75-90s] How to connect

Warm, not corny. Contractions. Short sentences.</pre>
</div>

<h2>Pro tip: batch record</h2>
<p>Don't record one at a time. Block an hour, shoot 5-8 in a row. Same outfit, same lighting.</p>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item"><input type="checkbox" id="m7-1" data-key="{short}-m7-1"><label for="m7-1">Generate 10 FAQ short scripts.</label></div>
<div class="checklist-item"><input type="checkbox" id="m7-2" data-key="{short}-m7-2"><label for="m7-2">Block 30 min. Record 3.</label></div>
<div class="checklist-item"><input type="checkbox" id="m7-3" data-key="{short}-m7-3"><label for="m7-3">Write personal intro. Record it.</label></div>
</div>
"""
    out.append({"slug": "module-07", "title": "Video scripts", "tag": "Module 7",
                "subtitle": "Scripts for explainers, shorts, intros, case studies.", "body": m7})

    # ============================================================
    # Module 8 - Direct mail
    # ============================================================
    m8 = f"""
<p>Direct mail isn't dead - it's that everyone else quit. For {short}, {spec['direct_mail_use']}, it still works.</p>

<h2>When to use direct mail</h2>
<ul>
<li>High-ticket prospects where print cost is worth it</li>
<li>{spec['direct_mail_use']}</li>
<li>Re-activation of old clients/leads</li>
<li>Local neighborhoods or specific ZIP codes</li>
<li>Business owners whose email is overloaded</li>
</ul>

<h2>Format options</h2>
<ul>
<li><strong>Standard postcard (4x6, 6x9)</strong> - cheapest, limited copy</li>
<li><strong>Oversized postcard (6x11, 9x12)</strong> - more visible, more copy room</li>
<li><strong>Sales letter (1-2 page letter in #10 envelope)</strong> - classic direct response</li>
<li><strong>Lumpy mail (padded envelope with small item)</strong> - expensive, unbeatable open rate</li>
</ul>

<h2>Postcard copy</h2>

<div class="prompt-box">
<div class="prompt-box-label">Postcard copy</div>
<button class="copy-btn">Copy</button>
<pre>Write copy for a 6x11 postcard for {short} prospecting.

Target: [specific audience]
Offer: [specific]

Front: 1 headline + 1 supporting line. Under 15 words.

Back: 4-6 short sections
1. Short opening - why you're mailing them
2. The problem you solve
3. What's different about you
4. One specific local detail
5. The offer
6. CTA: tracked phone + URL

Write mail-from-a-person tone. Include required disclaimers for {short}.</pre>
</div>

<h2>Sales letter format</h2>

<div class="prompt-box">
<div class="prompt-box-label">1-page sales letter</div>
<button class="copy-btn">Copy</button>
<pre>Write a 1-page sales letter for {short}.

Target: [audience]
Format: #10 envelope, typed letter, personal tone.

Structure:
- "Dear [Name]"
- Opening: specific observation or question
- Story: anonymized similar client
- Offer: what I'll do for them
- Proof: 2-3 defensible facts
- Urgency: real reason for now
- CTA: call or reply
- P.S.: restate offer + reason

250-400 words. Feel like a letter from a neighbor.</pre>
</div>

<h2>Envelope strategy</h2>
<p>The envelope is the first filter. Most direct mail dies unopened. Passes the "personal mail" test:</p>
<ul>
<li>Plain white envelope, no logo</li>
<li>Handwritten-style address</li>
<li>Real postage stamp</li>
<li>Interesting teaser (optional)</li>
</ul>

<h2>Tracking</h2>
<p>Every piece gets a unique phone number (CallRail) or URL. Without tracking you're guessing.</p>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item"><input type="checkbox" id="m8-1" data-key="{short}-m8-1"><label for="m8-1">Pick ONE campaign. Define audience + offer.</label></div>
<div class="checklist-item"><input type="checkbox" id="m8-2" data-key="{short}-m8-2"><label for="m8-2">Generate postcard and letter copy. Pick format.</label></div>
<div class="checklist-item"><input type="checkbox" id="m8-3" data-key="{short}-m8-3"><label for="m8-3">Set up call tracking number.</label></div>
<div class="checklist-item"><input type="checkbox" id="m8-4" data-key="{short}-m8-4"><label for="m8-4">Mail 500-1000 test batch. Measure. Iterate.</label></div>
</div>
"""
    out.append({"slug": "module-08", "title": "Direct mail", "tag": "Module 8",
                "subtitle": "Postcards and sales letters that still work in {short}.", "body": m8})

    # ============================================================
    # Module 9 - Referrals
    # ============================================================
    referral_triggers = '\n'.join([f"<li>{t}</li>" for t in spec['referral_triggers']])
    m9 = f"""
<p>Referrals are the highest-margin business you'll ever do. They close faster, cost nothing, retain better. Most {short}s are terrible at asking. This module fixes that.</p>

<h2>When to ask for referrals</h2>
<ul>
{referral_triggers}
</ul>

<p>At a moment the relationship is at a peak. Not random. Not "every quarter."</p>

<h2>The verbal ask</h2>

<div class="prompt-box">
<div class="prompt-box-label">Verbal referral ask</div>
<button class="copy-btn">Copy</button>
<pre>Write a 4-5 sentence verbal referral ask I can use after a positive interaction.

I help [specific niche].
The moment: [what just happened]

Should:
- Open with gratitude for the current moment (specific)
- Name exactly the type of person I can help
- Give a specific person/situation to think of
- Make handoff easy (I reach out, not them)
- Feel natural, not scripted

2 versions.</pre>
</div>

<h2>Warm intro email to client</h2>

<div class="prompt-box">
<div class="prompt-box-label">Forward-able intro</div>
<button class="copy-btn">Copy</button>
<pre>My client [Client] said I could reach [Prospect].

Section 1 (to client): thank again, I'll reach out in 1-2 days, offer forward-able intro.

Section 2 (to forward): from them to friend: why they thought of them, 1-sentence about me, suggest 15-min chat.

Under 200 words total.</pre>
</div>

<h2>Referral partner outreach</h2>
<p>The highest-leverage referral source isn't existing clients - it's other professionals who serve your same clients.</p>

<div class="prompt-box">
<div class="prompt-box-label">Partner outreach</div>
<button class="copy-btn">Copy</button>
<pre>Email to [complementary profession] in my market. Goal: referral relationship.

- Subject: about them, not me
- Open: specific detail about their work
- Bridge: client bases overlap because [specific]
- Offer: 20-min coffee/call
- What I bring (specific)
- Propose 2 times

Under 150 words. Peer-to-peer, not pitch.</pre>
</div>

<h2>Tracking referrals</h2>
<p>Set up a spreadsheet: Referrer, Trigger, Date asked, Names referred, Status, Outcome, Thank you sent.</p>
<p>Weekly 15-min review to keep it alive.</p>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item"><input type="checkbox" id="m9-1" data-key="{short}-m9-1"><label for="m9-1">Generate verbal referral ask. Practice it.</label></div>
<div class="checklist-item"><input type="checkbox" id="m9-2" data-key="{short}-m9-2"><label for="m9-2">Use it with 3 recent happy clients this week.</label></div>
<div class="checklist-item"><input type="checkbox" id="m9-3" data-key="{short}-m9-3"><label for="m9-3">Send outreach to 3 referral partners.</label></div>
</div>
"""
    out.append({"slug": "module-09", "title": "Referral requests", "tag": "Module 9",
                "subtitle": "Scripts and systems that turn referral generation into a weekly habit.", "body": m9})

    # ============================================================
    # Module 10 - Reviews
    # ============================================================
    review_platforms = '\n'.join([f"<li>{p}</li>" for p in spec['review_platforms']])
    m10 = f"""
<p>Online reviews are the modern referral. Before a prospect calls you, they search you. A review graveyard with no responses kills deals before you know they existed.</p>

<h2>Where reviews matter for {short}s</h2>
<ul>
{review_platforms}
</ul>

<h2>5-star response</h2>

<div class="prompt-box">
<div class="prompt-box-label">5-star response</div>
<button class="copy-btn">Copy</button>
<pre>Write 3-5 sentence response to this 5-star review.

- Thank by first name
- Reference something specific from their review
- Reinforce what I do
- End warmly, not saccharine

Avoid "it was our pleasure" / "strive to provide excellent service."

REVIEW: [paste]</pre>
</div>

<h2>Negative review response</h2>

<div class="prompt-box">
<div class="prompt-box-label">1-2 star response</div>
<button class="copy-btn">Copy</button>
<pre>Response to 1-2 star review.

- Acknowledge frustration, no arguing facts
- Do NOT reveal any client-specific details (privacy)
- Briefly note what I'd try to do to resolve
- Invite contact at [phone/email] privately
- No defensiveness, no apology-spiral
- 4-6 sentences

Future prospects watch how I handle pressure.

REVIEW: [paste]</pre>
</div>

<h2>Requesting reviews</h2>

<div class="prompt-box">
<div class="prompt-box-label">Review request</div>
<button class="copy-btn">Copy</button>
<pre>80-120 word email asking happy client for a review.

Context: [what we did]

- Open: specific recent interaction
- Ask: share experience on Google
- Direct link placeholder
- 60 seconds
- Offer to answer questions

Do NOT: offer incentive, specify 5 stars, pressure.</pre>
</div>

<h2>Weekly workflow</h2>
<ol>
<li>Pull reviews from last 7 days (all platforms)</li>
<li>Run through prompts, edit for tone</li>
<li>Post all at once</li>
</ol>

<p>15 min per week, every review responded to.</p>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item"><input type="checkbox" id="m10-1" data-key="{short}-m10-1"><label for="m10-1">Audit Google Business Profile. Respond to all unresponded.</label></div>
<div class="checklist-item"><input type="checkbox" id="m10-2" data-key="{short}-m10-2"><label for="m10-2">Set up weekly 15-min review response block.</label></div>
<div class="checklist-item"><input type="checkbox" id="m10-3" data-key="{short}-m10-3"><label for="m10-3">Send review request to 5 happy recent clients.</label></div>
</div>
"""
    out.append({"slug": "module-10", "title": "Review responses", "tag": "Module 10",
                "subtitle": "Response templates for every star rating. Reputation work that prospects watch.", "body": m10})

    # ============================================================
    # Module 11 - Newsletter
    # ============================================================
    newsletter_topics = '\n'.join([f"<li>{t}</li>" for t in spec['newsletter_topic_examples']])
    m11 = f"""
<p>A monthly newsletter is the most underrated marketing asset for {short}s. A list of 500 opt-in subscribers produces more business than most agencies realize.</p>

<h2>The one-big-thing format</h2>
<p>One substantive section + 2-3 quick items. 400-600 words total. Sent from your personal email.</p>

<div class="prompt-box">
<div class="prompt-box-label">Monthly newsletter</div>
<button class="copy-btn">Copy</button>
<pre>Write monthly newsletter for my {short} clients.

Topic: [pick one]

Structure:
- Subject: 5-7 words, personal
- Open: one sentence like writing to a friend
- Main section (250-400w): one big thing with specific example
- Quick hits: 3-5 bullets, 1-2 sentences each
- Close: 1-2 warm sentences
- P.S. with specific detail

Tone: knowledgeable friend, not broadcast. "You" a lot. "I" naturally.

Do NOT: sound templated, corporate sign-offs, stock-photo-heavy layout.</pre>
</div>

<h2>12-month topic calendar</h2>
<p>Topics tied to real triggers:</p>
<ul>
{newsletter_topics}
</ul>

<h2>Welcome sequence</h2>
<div class="prompt-box">
<div class="prompt-box-label">4-email welcome</div>
<button class="copy-btn">Copy</button>
<pre>4-email welcome sequence for new subscribers.

Email 1 (immediate): Welcome, who I am, what to expect. Under 150w.
Email 2 (day 2): One actionable thing. Under 200w.
Email 3 (day 5): Anonymized client story. Under 250w.
Email 4 (day 10): Soft direct ask. Under 150w.

From me personally. Hand-written feel.</pre>
</div>

<h2>Tools</h2>
<ul>
<li>ConvertKit / Kit - creators</li>
<li>MailerLite - free tier, simple</li>
<li>Beehiiv - newsletter-first</li>
<li>ActiveCampaign - more complex automation</li>
</ul>

<p>Avoid MailChimp and Constant Contact for cold/warm lists - dated, mediocre deliverability.</p>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item"><input type="checkbox" id="m11-1" data-key="{short}-m11-1"><label for="m11-1">Generate 12-month topic calendar. Lock next 3 months.</label></div>
<div class="checklist-item"><input type="checkbox" id="m11-2" data-key="{short}-m11-2"><label for="m11-2">Write this month's newsletter.</label></div>
<div class="checklist-item"><input type="checkbox" id="m11-3" data-key="{short}-m11-3"><label for="m11-3">Build 4-email welcome sequence.</label></div>
</div>
"""
    out.append({"slug": "module-11", "title": "Newsletter content", "tag": "Module 11",
                "subtitle": "Monthly email that keeps you top-of-mind. 30-minute task, not 3 hours.", "body": m11})

    # ============================================================
    # Module 12 - Ads
    # ============================================================
    ad_platforms = '\n'.join([f"<li>{p}</li>" for p in spec['ad_platforms']])
    m12 = f"""
<p>Paid ads are the scale lever when organic and referrals aren't producing enough pipeline. Done right, predictable leads. Done wrong, burned budget.</p>

<h2>Which platforms for {short}</h2>
<ul>
{ad_platforms}
</ul>

<h2>Before you run ads</h2>
<ul>
<li>Tracked phone number (CallRail)</li>
<li>Landing page (not homepage)</li>
<li>Target cost per lead known</li>
<li>Budget you can afford to lose in week 1</li>
</ul>

<h2>Facebook ad copy</h2>

<div class="prompt-box">
<div class="prompt-box-label">FB ad variants</div>
<button class="copy-btn">Copy</button>
<pre>Write 5 Facebook ad variants for {short}.

Target: [audience details]
Offer: [specific]
Landing page: [description]

Each variant:
- Primary text (90-150 words)
- Headline (25-40 chars)
- Description (30-45 chars)

Hook angles (one per variant):
1. Question-led
2. Contrarian
3. Specific detail / local
4. Story-led
5. Direct value

Avoid: fear tactics, fake urgency, "Act now!", emoji overload.

Include any required {short} disclaimers.</pre>
</div>

<h2>Google Search ads</h2>

<div class="prompt-box">
<div class="prompt-box-label">Google Search ads</div>
<button class="copy-btn">Copy</button>
<pre>Google Search ads for {short} in [city/state].

Keywords: [list 3-5]

For each:
- 3 RSA headlines (30 chars)
- 2 descriptions (90 chars)
- Display path
- 3 sitelinks

Include location, benefit, one differentiator per headline. Avoid superlatives.</pre>
</div>

<h2>Landing page copy</h2>

<div class="prompt-box">
<div class="prompt-box-label">Landing page</div>
<button class="copy-btn">Copy</button>
<pre>Landing page copy for [campaign].
Goal: [book call / get quote / download].

- Headline (matches ad promise)
- Sub-headline
- 3-4 "what you get" bullets
- Proof section
- Form: name, phone, email, qualifier
- Second CTA below fold
- 4-5 FAQ
- Trust signals
- "What happens next"</pre>
</div>

<h2>Tracking</h2>
<ul>
<li>GA4 on landing page</li>
<li>Meta pixel / Google tag</li>
<li>Call tracking number</li>
<li>UTM parameters</li>
</ul>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item"><input type="checkbox" id="m12-1" data-key="{short}-m12-1"><label for="m12-1">Pick ONE line, ONE objective. Don't run 5 campaigns at once.</label></div>
<div class="checklist-item"><input type="checkbox" id="m12-2" data-key="{short}-m12-2"><label for="m12-2">Generate 5 ad variants.</label></div>
<div class="checklist-item"><input type="checkbox" id="m12-3" data-key="{short}-m12-3"><label for="m12-3">Write landing page. Build it.</label></div>
<div class="checklist-item"><input type="checkbox" id="m12-4" data-key="{short}-m12-4"><label for="m12-4">Set up tracking. Launch at $25-50/day for 7-14 days before judging.</label></div>
</div>
"""
    out.append({"slug": "module-12", "title": "Facebook + Google ads", "tag": "Module 12",
                "subtitle": "Ad copy that converts plus the tracking that prevents wasted spend.", "body": m12})

    # ============================================================
    # Module 13 - Client education materials
    # ============================================================
    client_ed_list = '\n'.join([f"<li>{d}</li>" for d in spec['client_ed_docs']])
    m13 = f"""
<p>Educational material you give clients during and after the engagement does two jobs: helps the client, generates referrals. Most {short}s hand over generic brochures. Your own branded materials are a 10x improvement in an hour.</p>

<h2>What to build</h2>
<ul>
{client_ed_list}
</ul>

<h2>Plain-language glossary</h2>

<div class="prompt-box">
<div class="prompt-box-label">Glossary one-pager</div>
<button class="copy-btn">Copy</button>
<pre>1-page glossary for {short} clients. 12-15 terms.

Each:
- Term (as they see it on paperwork)
- 1-2 sentence plain-language definition
- 1 sentence why it matters to them

No jargon defining jargon. For a non-professional reader.

Format for Canva/Word.</pre>
</div>

<h2>The "what you actually got" summary</h2>

<div class="prompt-box">
<div class="prompt-box-label">Service summary one-pager</div>
<button class="copy-btn">Copy</button>
<pre>1-page "what you actually got" summary client keeps.

Structure:
1. One-sentence "what this is"
2. What it does for you (3-4 bullets)
3. What it does NOT cover / NOT include (3-4 bullets)
4. What to do with it (storage, reminders)
5. When to call me (specific triggers)
6. Space for: contact, date, reference info

Clear, respectful, plainspoken.</pre>
</div>

<h2>Branding the output</h2>
<p>Claude writes content. You format + brand it:</p>
<ul>
<li>Canva (free tier enough)</li>
<li>Google Docs</li>
<li>PowerPoint</li>
</ul>

<p>Export as PDF. Email after each new engagement, print for in-person meetings, post on your site (with PII placeholders) as free resources.</p>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item"><input type="checkbox" id="m13-1" data-key="{short}-m13-1"><label for="m13-1">Pick the ONE document that would impress clients most.</label></div>
<div class="checklist-item"><input type="checkbox" id="m13-2" data-key="{short}-m13-2"><label for="m13-2">Generate content. Design in Canva.</label></div>
<div class="checklist-item"><input type="checkbox" id="m13-3" data-key="{short}-m13-3"><label for="m13-3">Send to 10 most recent clients as follow-up.</label></div>
<div class="checklist-item"><input type="checkbox" id="m13-4" data-key="{short}-m13-4"><label for="m13-4">Add to new-client onboarding.</label></div>
</div>
"""
    out.append({"slug": "module-13", "title": "Client education material", "tag": "Module 13",
                "subtitle": "Glossaries, summaries, guides. Stuff that turns clients into advocates.", "body": m13})

    return out
