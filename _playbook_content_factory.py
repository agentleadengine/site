#!/usr/bin/env python3
"""Content factory: generates 15 modules for a playbook from a profession spec.
Some modules are standard (2, 3, 14), most are customized per-profession."""


def generate_modules(spec):
    """
    spec = {
      'profession': 'Real Estate Agent',
      'short': 'real estate',
      'audience_description': 'buyers and sellers in [your market]',
      'revenue_model': 'commission-based',
      'legal_concerns': 'state real estate commission rules, fair housing, RESPA',
      'typical_client': 'homeowners selling, first-time buyers, investors',
      'common_channels': ['Facebook', 'Instagram', 'YouTube', 'LinkedIn'],
      'primary_asset_types': ['listing copy', 'neighborhood guides', 'market updates'],
      'compliance_notes': ['Fair Housing language', 'MLS rules', 'state licensing rules'],
    }
    """
    profession = spec['profession']
    short = spec['short']
    audience = spec['audience_description']
    legal = spec['legal_concerns']
    typical_client = spec['typical_client']
    channels = ', '.join(spec['common_channels'])
    compliance = spec['compliance_notes']
    profession_lower = profession.lower()

    modules = []

    # ============================================================
    # MODULE 1 - Why Claude
    # ============================================================
    m1 = f"""
<p>Before you write a single prompt, understand what Claude is actually good at for {profession_lower}s and where it falls short. Skipping this module costs you a week of bad outputs while you figure out why the model keeps producing generic, vanilla marketing.</p>

<h2>What Claude is good at</h2>
<ul>
<li><strong>First drafts.</strong> {', '.join(spec['primary_asset_types'])}, social posts, email sequences, ads. Blank page to working draft in 60 seconds.</li>
<li><strong>Rewriting.</strong> Your rough voice memo or bullet notes to polished copy.</li>
<li><strong>Variations.</strong> One post, ten versions. One email, five different subject lines to test.</li>
<li><strong>Translating jargon.</strong> {short.capitalize()} industry terms into plain language your clients understand.</li>
<li><strong>Personalization at scale.</strong> Custom first lines for 50 prospects in 10 minutes.</li>
</ul>

<h2>What Claude is not good at</h2>
<ul>
<li><strong>Current market data.</strong> Don't let it quote specific prices, rates, or live inventory. It will make them up.</li>
<li><strong>Your voice, first try.</strong> Out of the box it writes generic. You'll teach it your voice via samples.</li>
<li><strong>Compliance catch-all.</strong> It has general awareness of {legal}, but won't catch every state-specific rule.</li>
<li><strong>Sensitive client data.</strong> Don't paste PII, financial info, or confidential client situations into a consumer model.</li>
</ul>

<h2>Why it beats your current options</h2>
<p>You probably already tried:</p>
<ul>
<li>Writing marketing yourself - takes hours, never gets done</li>
<li>Paying a marketing agency - $1500-5000/month for generic copy</li>
<li>Using templates from your brokerage/platform - every other {profession_lower} has the same ones</li>
<li>Hiring a VA - quality varies, training takes forever</li>
</ul>

<p>Claude compresses "write my own content" from three hours to fifteen minutes. That's the arbitrage.</p>

<h2>The economics</h2>
<p>Claude Pro is $20/month. Compared to:</p>
<ul>
<li>Freelance marketer: $100-400 per piece</li>
<li>Agency retainer: $1,500-5,000/month</li>
<li>Your own time at your billable rate: more than you want to calculate</li>
</ul>

<p>For a {profession_lower} producing a blog post a week, a dozen social posts, and a monthly newsletter, Claude pays for itself several times over on day one.</p>

<h2>The mindset shift</h2>
<p>Think of Claude as a senior marketing associate who works at any speed, never gets tired, has read every book on marketing - but has never sold a [thing your profession sells]. They produce great first drafts if briefed well. Their drafts are never final. You're the editor, expert, and compliance backstop.</p>

<div class="callout">
<div class="callout-title">The rule</div>
<p>Everything Claude writes gets read before publishing. Every claim, number, name. The model hallucinates plausible-sounding stuff that isn't true. You are the filter.</p>
</div>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item">
<input type="checkbox" id="m1-1" data-key="{short}-m1-1">
<label for="m1-1">Sign up for Claude.ai (free) or Claude Pro ($20/month).</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m1-2" data-key="{short}-m1-2">
<label for="m1-2">Spend 15 minutes chatting with it. Ask it to explain [core concept in your profession] to a client.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m1-3" data-key="{short}-m1-3">
<label for="m1-3">Identify the marketing task you hate most. That's the one to tackle first.</label>
</div>
</div>
"""
    modules.append({
        "slug": "module-01",
        "title": f"Why Claude for {short} marketing",
        "tag": "Module 1",
        "subtitle": f"What Claude actually does for {profession_lower}s, and where it falls short.",
        "body": m1,
    })

    # ============================================================
    # MODULE 2 - Setting up
    # ============================================================
    m2 = f"""
<p>Ten minutes of setup now saves six months of mediocre outputs. Give Claude the context it needs about you, your market, and your voice.</p>

<h2>Step 1: Pick your plan</h2>
<ul>
<li><strong>Free (claude.ai):</strong> Fine for experimenting.</li>
<li><strong>Claude Pro ($20/month):</strong> Higher limits, latest models. Right for any {profession_lower} doing regular marketing.</li>
</ul>

<h2>Step 2: Build your Agent Context</h2>

<div class="prompt-box">
<div class="prompt-box-label">Agent context template</div>
<button class="copy-btn">Copy</button>
<pre>You are my marketing associate. Before you write anything:

ABOUT ME:
- Name: [Your name]
- Business: [Your business]
- License/credentials: [relevant]
- Market/area: [geography]
- Years in the business: [number]

MY IDEAL CLIENT:
- Type: {typical_client}
- Location: [specific]
- Stage/situation: [what they're going through]
- Top concerns: [what keeps them up]

MY DIFFERENTIATION:
- What makes me different: [specific]
- The one thing I'm known for: [specific]

MY VOICE:
- Tone: [warm, direct, no jargon]
- Phrases I use: [list 3-5]
- Phrases I'd never use: [list]

COMPLIANCE (do NOT):
- {compliance[0] if compliance else 'make guarantees about outcomes'}
- Use superlatives like "best" or "cheapest"
- Quote specific live numbers without disclaimers

Write like a person respecting the reader's time. Short sentences. Specific examples.

Ready?</pre>
</div>

<h2>Step 3: Save 3 voice samples</h2>
<p>Grab an email, a social post, and a voicemail you've actually sent. Paste them when you ask Claude to "write like me."</p>

<h2>Step 4: Privacy rules</h2>
<div class="callout warning">
<div class="callout-title">Never paste into Claude</div>
<p>Client names with identifiable details, financial data, property addresses without consent, {legal}-regulated information, anything confidential.</p>
</div>

<h2>Step 5: Create two Projects in Claude</h2>
<ul>
<li><strong>"My Marketing"</strong> with the Agent Context as custom instructions</li>
<li><strong>"Client Scenarios"</strong> for anonymized situations (keeps marketing separate)</li>
</ul>

<div class="callout success">
<div class="callout-title">Why this matters</div>
<p>Most {profession_lower}s skip setup and get outputs 70% as good as they could be. Fifteen minutes of context puts you at 95%.</p>
</div>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item">
<input type="checkbox" id="m2-1" data-key="{short}-m2-1">
<label for="m2-1">Fill in the Agent Context template.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m2-2" data-key="{short}-m2-2">
<label for="m2-2">Collect 3 voice samples.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m2-3" data-key="{short}-m2-3">
<label for="m2-3">Set up the two Projects in Claude.</label>
</div>
</div>
"""
    modules.append({
        "slug": "module-02",
        "title": "Setting up Claude",
        "tag": "Module 2",
        "subtitle": "The 10-minute setup that makes every future prompt 3x better.",
        "body": m2,
    })

    # ============================================================
    # MODULE 3 - The 10 prompt patterns
    # ============================================================
    m3 = f"""
<p>Ninety percent of effective prompts are variations of ten patterns. Learn these once; reuse them forever.</p>

<h2>Pattern 1: The Briefed Writer</h2>
<div class="prompt-box"><div class="prompt-box-label">Pattern 1</div><button class="copy-btn">Copy</button><pre>Write [asset type] for [audience] about [topic].
Goal: [what action]
Tone: [from voice samples]
Length: [word count]
Must include: [points]
Must NOT include: [forbidden]
Output just the copy.</pre></div>

<h2>Pattern 2: The Angle Generator</h2>
<div class="prompt-box"><div class="prompt-box-label">Pattern 2</div><button class="copy-btn">Copy</button><pre>I'm writing [asset] about [topic] for [audience].
Give me 10 different angles. Each: one-sentence hook, specific promise, distinct from the others.
I'll pick one.</pre></div>

<h2>Pattern 3: The Rewrite</h2>
<div class="prompt-box"><div class="prompt-box-label">Pattern 3</div><button class="copy-btn">Copy</button><pre>Rewrite the text below:
- Clearer for [audience]
- Shorter by [%]
- In my voice
- Jargon-free
Preserve substance.
[Paste source]</pre></div>

<h2>Pattern 4: The Multi-Version</h2>
<div class="prompt-box"><div class="prompt-box-label">Pattern 4</div><button class="copy-btn">Copy</button><pre>Core idea: [idea]
Give me versions for:
1. 150-word Facebook post
2. 250-word LinkedIn post
3. 60-second video script
4. 50-word SMS
5. Blog post intro
Match each channel's conventions.</pre></div>

<h2>Pattern 5: The Counter-Draft</h2>
<div class="prompt-box"><div class="prompt-box-label">Pattern 5</div><button class="copy-btn">Copy</button><pre>Draft: [paste]
Write 3 alternatives:
A. More specific (replace abstract claims with numbers/scenes)
B. Story-opener (first 50 words = a scene)
C. Contrarian (challenges common belief)
Don't soften.</pre></div>

<h2>Pattern 6: The Critic</h2>
<div class="prompt-box"><div class="prompt-box-label">Pattern 6</div><button class="copy-btn">Copy</button><pre>Read the copy as:
1. A skeptical {typical_client.split(',')[0]}
2. A compliance officer
3. A cynical marketer
For each, list 3 things that would make them stop or push back. Blunt.
[Paste copy]</pre></div>

<h2>Pattern 7: The Persona Interview</h2>
<div class="prompt-box"><div class="prompt-box-label">Pattern 7</div><button class="copy-btn">Copy</button><pre>Roleplay as [ideal client persona].
Details: [age, family, income, location, what they're thinking about]
I'll interview you about [topic]. Answer in first person with specific worries.
First question: [yours]</pre></div>

<h2>Pattern 8: The Specific Translator</h2>
<div class="prompt-box"><div class="prompt-box-label">Pattern 8</div><button class="copy-btn">Copy</button><pre>Every vague claim in the copy below, replace with a number, name, time, or example.
If I can't back a specific claim, flag it.
[Paste copy]</pre></div>

<h2>Pattern 9: The Hook Farm</h2>
<div class="prompt-box"><div class="prompt-box-label">Pattern 9</div><button class="copy-btn">Copy</button><pre>Topic: [idea]
Audience: [who]
Format: [post / blog intro / email subject]
Give me 10 hooks. Just the first 15 words. Different patterns: contrarian, specific number, question, confession, news, warning, character, unusual observation, reframe, direct pain.</pre></div>

<h2>Pattern 10: The Compliance Pre-Check</h2>
<div class="prompt-box"><div class="prompt-box-label">Pattern 10</div><button class="copy-btn">Copy</button><pre>Review for {short} compliance issues:
- Superlatives ("best," "cheapest")
- Specific guarantees
- {compliance[0] if compliance else 'Required disclaimers'}
- Competitor claims
- Rate specifics that could go stale
Return flags + revised version.
[Paste copy]</pre></div>

<h2>Chaining patterns</h2>
<p>Real marketing tasks combine 2-3 patterns:</p>
<ul>
<li>Blog post: Pattern 2 (angles) → Pattern 1 (write) → Pattern 6 (critic) → Pattern 8 (specifics) → Pattern 10 (compliance)</li>
<li>Social post: Pattern 9 (hooks) → Pattern 1 (write) → Pattern 5 (counter-drafts)</li>
<li>Video script: Pattern 7 (persona) → Pattern 1 (write) → Pattern 8 (specifics)</li>
</ul>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item"><input type="checkbox" id="m3-1" data-key="{short}-m3-1"><label for="m3-1">Run each pattern once on a low-stakes topic.</label></div>
<div class="checklist-item"><input type="checkbox" id="m3-2" data-key="{short}-m3-2"><label for="m3-2">Save the 10 patterns for easy copy-paste.</label></div>
</div>
"""
    modules.append({
        "slug": "module-03",
        "title": "The 10 prompt patterns",
        "tag": "Module 3",
        "subtitle": "Ninety percent of effective prompts are variations of ten patterns.",
        "body": m3,
    })

    # ============================================================
    # MODULES 4-13 - profession-specific (supplied in spec)
    # ============================================================
    for m in spec.get('custom_modules', []):
        modules.append(m)

    # ============================================================
    # MODULE 14 - weekly system
    # ============================================================
    m14 = f"""
<p>Every module so far is individually useful. The real win is tying them into a weekly rhythm.</p>

<h2>The 2-hour weekly block</h2>
<p>One 2-hour block per week, same time every week:</p>

<h3>0:00-0:15 - Review</h3>
<ul>
<li>Last week's numbers: engagement, replies, leads, clients booked</li>
<li>What worked, what didn't (one sentence each)</li>
</ul>

<h3>0:15-0:45 - Create content</h3>
<p>One asset per week, rotating:</p>
<ul>
<li>Week 1: Social posts for the week</li>
<li>Week 2: One blog post</li>
<li>Week 3: FAQ video batch</li>
<li>Week 4: Monthly newsletter</li>
</ul>

<h3>0:45-1:15 - Prospecting + follow-up</h3>
<ul>
<li>Send this week's outreach</li>
<li>Reply to warm conversations</li>
<li>Update CRM</li>
</ul>

<h3>1:15-1:30 - Review responses + referrals</h3>
<ul>
<li>Respond to any new reviews</li>
<li>Make 1-2 referral asks</li>
</ul>

<h3>1:30-2:00 - Schedule + publish</h3>
<ul>
<li>Schedule all content via Buffer/Later/Meta Business Suite</li>
<li>Queue emails</li>
<li>Adjust ads</li>
</ul>

<h2>The monthly + quarterly blocks</h2>
<p>Once a month, add 1 hour for: ad performance review, next month's newsletter topic, client education document, referral partner check-ins.</p>

<p>Once a quarter, add 2 hours for: full content audit, goal reset, Claude context refresh.</p>

<h2>The truth about consistency</h2>
<p>Most {profession_lower}s start marketing systems and abandon them in 3 weeks. Keep the rhythm simple enough you'll do it on a bad week:</p>
<ul>
<li>Same day, same time</li>
<li>Phone off, calendar blocked</li>
<li>Even if you don't feel it, sit down and run the prompts</li>
<li>Even a mediocre output is better than no output</li>
</ul>

<p>Month 1 is messy. Month 2 feels natural. Month 3 you have a content machine.</p>

<h2>Monday review prompt</h2>
<div class="prompt-box"><div class="prompt-box-label">Weekly planning</div><button class="copy-btn">Copy</button><pre>Weekly marketing planning. Last week:
- Social engagement: [describe]
- Email replies: [number]
- Ads: [if running]
- Leads/meetings: [number]

Based on this:
1. What to double down on?
2. What to stop?
3. 3 experiments to run
4. Highest-leverage task for 2 hours?

Practical.</pre></div>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item"><input type="checkbox" id="m14-1" data-key="{short}-m14-1"><label for="m14-1">Block the 2-hour weekly time on your calendar. Next 12 weeks.</label></div>
<div class="checklist-item"><input type="checkbox" id="m14-2" data-key="{short}-m14-2"><label for="m14-2">Run the first Monday review.</label></div>
<div class="checklist-item"><input type="checkbox" id="m14-3" data-key="{short}-m14-3"><label for="m14-3">Pick 1 metric you'll track weekly.</label></div>
</div>
"""
    modules.append({
        "slug": "module-14",
        "title": "The weekly marketing system",
        "tag": "Module 14",
        "subtitle": "A 2-hour weekly rhythm that produces a month of marketing output.",
        "body": m14,
    })

    # ============================================================
    # MODULE 15 - compliance (profession-specific)
    # ============================================================
    compliance_html = "\n".join([f"<li>{c}</li>" for c in compliance])
    m15 = f"""
<p>Everything in this playbook is worthless if your marketing lands you in front of regulators, licensing boards, or your brokerage/employer. Claude speeds creation, which means it speeds mistakes if you're not careful.</p>

<h2>Who regulates {profession_lower}s</h2>
<ul>
{compliance_html}
</ul>

<h2>Universal red flags to scan for</h2>
<ul>
<li>Superlatives you can't prove: "best," "cheapest," "top-rated"</li>
<li>Guaranteed outcomes: "guaranteed to [result]"</li>
<li>Comparison claims naming competitors</li>
<li>Specific rates, prices, or figures without disclaimers</li>
<li>Urgency that isn't real</li>
<li>Testimonials without proper disclaimers (some states restrict entirely)</li>
<li>Statistics without citation</li>
</ul>

<h2>The pre-publish checklist</h2>
<div class="checklist">
<div class="checklist-item"><input type="checkbox" id="m15-1" data-key="{short}-m15-1"><label for="m15-1">Ran the compliance pre-check prompt</label></div>
<div class="checklist-item"><input type="checkbox" id="m15-2" data-key="{short}-m15-2"><label for="m15-2">Searched for "best," "cheapest," "guaranteed," "always," "never"</label></div>
<div class="checklist-item"><input type="checkbox" id="m15-3" data-key="{short}-m15-3"><label for="m15-3">Every number has a defensible source</label></div>
<div class="checklist-item"><input type="checkbox" id="m15-4" data-key="{short}-m15-4"><label for="m15-4">Required disclaimers present and readable</label></div>
<div class="checklist-item"><input type="checkbox" id="m15-5" data-key="{short}-m15-5"><label for="m15-5">License/credentials visible</label></div>
<div class="checklist-item"><input type="checkbox" id="m15-6" data-key="{short}-m15-6"><label for="m15-6">Submitted to brokerage/compliance review where required</label></div>
<div class="checklist-item"><input type="checkbox" id="m15-7" data-key="{short}-m15-7"><label for="m15-7">No confidential client data in the content</label></div>
<div class="checklist-item"><input type="checkbox" id="m15-8" data-key="{short}-m15-8"><label for="m15-8">Archived for compliance (3-5 years depending on jurisdiction)</label></div>
</div>

<h2>The red phrase scanner</h2>
<div class="prompt-box">
<div class="prompt-box-label">Red phrase scanner</div>
<button class="copy-btn">Copy</button>
<pre>Scan for compliance red flags in {profession_lower} marketing.

Flag every:
- Superlative
- Specific numeric claim
- Competitor comparison
- Urgency claim - is it real?
- Missing disclaimer
- Implied endorsement
- Claim about outcomes that vary

For each flag: suggest a compliant rewrite. Then give the cleaned version.

Jurisdiction: [state]
[Paste copy]</pre>
</div>

<h2>Record-keeping</h2>
<p>Keep every marketing piece for 3-5 years:</p>
<ul>
<li>/Marketing Archive /[Year] /[Month] - every published piece</li>
<li>Include any compliance approval emails</li>
<li>Include date and platform published</li>
</ul>

<div class="callout">
<div class="callout-title">The rule</div>
<p>If you wouldn't want a regulator, your brokerage compliance officer, and a skeptical client all reading this piece - rewrite it until you would.</p>
</div>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item"><input type="checkbox" id="m15-task-1" data-key="{short}-m15-task-1"><label for="m15-task-1">Bookmark your state/industry regulator's marketing rules page. Read it once.</label></div>
<div class="checklist-item"><input type="checkbox" id="m15-task-2" data-key="{short}-m15-task-2"><label for="m15-task-2">Identify who reviews your copy (brokerage, compliance officer, etc.).</label></div>
<div class="checklist-item"><input type="checkbox" id="m15-task-3" data-key="{short}-m15-task-3"><label for="m15-task-3">Set up the marketing archive folder.</label></div>
</div>
"""
    modules.append({
        "slug": "module-15",
        "title": "Compliance checklist",
        "tag": "Module 15",
        "subtitle": f"The compliance discipline that runs alongside every module for {profession_lower}s.",
        "body": m15,
    })

    return modules


def std_landing(profession, short, tagline):
    """Standard landing page body."""
    return f"""
<h2>What this is</h2>
<p>This is a working playbook for {short}s who want to build their own marketing material using Claude. Not theory. Specific prompts, specific templates, specific workflows you can use in the next hour to put out better marketing than you did yesterday.</p>

<div class="callout">
<div class="callout-title">Who this is for</div>
<p>{tagline}</p>
</div>

<h2>How the playbook works</h2>
<p>Fifteen modules. Each covers one type of marketing asset, with:</p>
<ul>
<li>What the asset does and when to use it</li>
<li>The specific prompts you'll run Claude with</li>
<li>A worked example you can adapt</li>
<li>Compliance notes specific to {short}</li>
<li>A checklist for this week</li>
</ul>

<p>Plus a <a href="prompt-library.html">prompt library</a> with every prompt in one place.</p>

<h2>The order to do them in</h2>
<ol>
<li><a href="module-01.html">Module 1</a> - Why Claude for {short} marketing</li>
<li><a href="module-02.html">Module 2</a> - Setting up Claude (do this once)</li>
<li><a href="module-03.html">Module 3</a> - The 10 prompt patterns</li>
<li>Modules 4-13 - pick whatever asset you need this week</li>
<li><a href="module-14.html">Module 14</a> - The weekly marketing system</li>
<li><a href="module-15.html">Module 15</a> - Compliance checklist</li>
</ol>

<h2>Your progress is saved</h2>
<p>The sidebar tracks completed modules. Stored in your browser - no account needed.</p>

<p style="margin-top:48px;"><a href="module-01.html" style="display:inline-block;background:#4a00e0;color:#fff;padding:14px 28px;border-radius:8px;text-decoration:none;font-weight:600;font-size:15px;">Start Module 1 →</a></p>
"""


def custom_module(slug, title, tag, subtitle, body):
    """Helper to create a custom module dict."""
    return {"slug": slug, "title": title, "tag": tag, "subtitle": subtitle, "body": body}
