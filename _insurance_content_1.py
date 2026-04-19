#!/usr/bin/env python3
"""Insurance playbook content — Part 1: Landing + Modules 1-5."""
from _build_insurance import write_playbook_page


# ============================================================
# INDEX / LANDING
# ============================================================

index_body = """
<h2>What this is</h2>
<p>This is a working playbook for insurance agents who want to build their own marketing material using Claude. Not theory. Not "here's what AI could do." Specific prompts, specific templates, specific workflows you can use in the next hour to put out better marketing than you did yesterday.</p>

<p>It's written for the producer who runs their own book, the independent agent, the small agency owner, and the captive agent trying to differentiate inside a rigid system. The structure works across life, health, P&amp;C, Medicare, and commercial lines.</p>

<div class="callout">
<div class="callout-title">Who this is for</div>
<p>You write or post marketing content yourself (or want to stop outsourcing it for $1500/month). You have Claude, ChatGPT, or access to a decent model. You have 30 minutes per week to put into marketing. You want to stop staring at a blank page.</p>
</div>

<h2>How the playbook works</h2>
<p>Fifteen modules, each covering one type of marketing asset. Every module includes:</p>
<ul>
<li>What the asset does and when to use it</li>
<li>The 2-5 specific prompts you'll run Claude with</li>
<li>A worked example you can adapt</li>
<li>Compliance notes that apply to insurance specifically</li>
<li>A checklist of what to do this week</li>
</ul>

<p>Plus a <a href="prompt-library.html">searchable prompt library</a> with all 60+ prompts in one place, filterable by asset type and insurance line.</p>

<h2>The order to do them in</h2>
<ol>
<li><strong><a href="module-01.html">Module 1</a></strong> — Why Claude for insurance marketing (5 min read)</li>
<li><strong><a href="module-02.html">Module 2</a></strong> — Setting up Claude (10 min — do this once)</li>
<li><strong><a href="module-03.html">Module 3</a></strong> — The 10 prompt patterns (15 min — you'll reuse these forever)</li>
<li>Modules 4-13 — Pick the asset type you need this week. Do them in any order.</li>
<li><strong><a href="module-14.html">Module 14</a></strong> — The weekly marketing system (30 min — your new rhythm)</li>
<li><strong><a href="module-15.html">Module 15</a></strong> — Compliance checklist (read once, refer always)</li>
</ol>

<h2>Your progress is saved</h2>
<p>The sidebar tracks which modules you've completed. Your progress lives in your browser — no account needed. Hit "Mark module complete" at the end of each one. If you come back later, the sidebar remembers where you were.</p>

<div class="callout success">
<div class="callout-title">The honest take</div>
<p>Claude won't replace your judgment, your relationships, or your license. It will do the part of marketing you hate — the blank page, the formatting, the first draft — in a fraction of the time. The time you save goes into conversations with actual humans, which is where policies actually get sold.</p>
</div>

<h2>What you'll be able to do in an hour</h2>
<ul>
<li>Write 5 personalized prospecting emails</li>
<li>Draft a week of social media posts</li>
<li>Generate 3 blog post ideas with full outlines</li>
<li>Script a 60-second explainer video</li>
<li>Create a direct-mail postcard your printer can run</li>
<li>Respond to every Google review in your queue</li>
<li>Write your monthly newsletter</li>
</ul>

<p>If any single one of those takes you more than 20 minutes today, this playbook pays for itself (which is free — so call it pure upside).</p>

<p style="margin-top:48px;"><a href="module-01.html" style="display:inline-block;background:#4a00e0;color:#fff;padding:14px 28px;border-radius:8px;text-decoration:none;font-weight:600;font-size:15px;">Start Module 1 →</a></p>
"""

write_playbook_page(
    slug="index",
    title="The Insurance Agent's Claude Playbook",
    tag="",
    subtitle="A practical, hands-on guide to building your own marketing material with AI. Fifteen modules, sixty-plus prompts, zero fluff.",
    body_html=index_body,
    hero=True,
)


# ============================================================
# MODULE 1 — Why Claude
# ============================================================

m1 = """
<p>Before you write a single prompt, understand what Claude is actually good at and what it isn't. Skipping this module will cost you a week of bad outputs while you figure out why the model keeps giving you generic, vanilla marketing that sounds like every other agent's.</p>

<h2>What Claude is good at</h2>
<ul>
<li><strong>First drafts.</strong> Emails, blog posts, ad copy, scripts, newsletter sections. It goes from blank page to working draft in 60 seconds.</li>
<li><strong>Rewriting.</strong> Take your rough voice memo or bullet list, turn it into polished copy.</li>
<li><strong>Variations.</strong> One email, ten subject line tests. One post, five platform-specific versions.</li>
<li><strong>Compliance-aware language.</strong> Claude knows what FINRA, CMS, and state DOIs tend to flag — if you tell it what line you're writing for.</li>
<li><strong>Translating jargon into plain English.</strong> You explain IUL to the model, it writes the version your 62-year-old client understands.</li>
<li><strong>Rewriting carrier material.</strong> Take a dense carrier one-pager, produce something your client can actually read.</li>
</ul>

<h2>What Claude is not good at (yet)</h2>
<ul>
<li><strong>Knowing your specific carriers.</strong> It doesn't know your product shelf. You have to tell it.</li>
<li><strong>Current rate or premium specifics.</strong> Never let it quote premiums or dates that matter. It will make them up.</li>
<li><strong>Your voice, first try.</strong> Out of the box it writes "agent voice." You'll need to teach it how you actually talk.</li>
<li><strong>State-specific rules.</strong> It has general compliance awareness but will not catch everything your state DOI cares about.</li>
<li><strong>Real clients' names, claims, or data.</strong> You should not paste PHI or NPI into a general-purpose model.</li>
</ul>

<h2>Why it beats a "do it yourself" approach</h2>
<p>You already know marketing matters. You've probably tried:</p>
<ul>
<li>Writing it yourself — takes hours, you push it off, it doesn't get done</li>
<li>Paying an agency or freelancer — $1,500-5,000/month, they don't understand insurance, the copy is generic</li>
<li>Using a pre-built content library from your IMO/FMO — every other agent has the same stuff</li>
<li>Hiring a VA — quality varies wildly, training them takes forever</li>
</ul>

<p>Claude doesn't replace any of those fully, but it compresses "agent writing their own content" from three hours to fifteen minutes. That's the arbitrage.</p>

<h2>The economics</h2>
<p>Claude Pro is $20/month. Claude.ai free tier is workable for low volume. Compared to:</p>
<ul>
<li>Freelancer blog post: $100-400 per post</li>
<li>Monthly content retainer: $1,500-5,000</li>
<li>Your own time at your $/hour billing rate: probably more than you want to think about</li>
</ul>

<p>For an agent writing a blog post a week, a dozen social posts, and a monthly newsletter, Claude pays for itself several times over on day one.</p>

<h2>The mindset shift</h2>
<p>Stop thinking of Claude as "generate me a marketing email." Start thinking of it as <em>a senior marketing associate who works at any speed, never gets tired, and has read every book on insurance marketing but has never actually sold a policy</em>. They'll produce great first drafts if you brief them well. Their drafts are never the final version. You're still the editor, the subject matter expert, and the compliance backstop.</p>

<div class="callout">
<div class="callout-title">The rule</div>
<p>Everything Claude writes gets read before it goes public. Every claim, every number, every name. The model will hallucinate plausible-sounding stuff that turns out to be wrong. You are the filter.</p>
</div>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item">
<input type="checkbox" id="m1-1" data-key="m1-1">
<label for="m1-1">Sign up for Claude.ai (free tier) or Claude Pro ($20/month). Go to claude.ai and create an account.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m1-2" data-key="m1-2">
<label for="m1-2">Spend 15 minutes just chatting with it. Ask it to explain Indexed Universal Life to a 45-year-old. Then ask it to explain it to a 65-year-old. Notice the differences.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m1-3" data-key="m1-3">
<label for="m1-3">Identify the marketing task you hate most. Whatever comes to mind first — that's the one Claude will help with most.</label>
</div>
</div>
"""

write_playbook_page(
    slug="module-01",
    title="Why Claude for insurance marketing",
    tag="Module 1",
    subtitle="What Claude is good at, what it isn't, and why it compresses the worst parts of your marketing from hours to minutes.",
    body_html=m1,
)


# ============================================================
# MODULE 2 — Setting up Claude
# ============================================================

m2 = """
<p>Ten minutes of setup now saves you from six months of mediocre prompt results. The goal of this module: give Claude the context it needs about you, your book, and your voice so that every prompt you run afterward is tuned to you specifically.</p>

<h2>Step 1: Pick your plan</h2>
<ul>
<li><strong>Free (claude.ai):</strong> Fine for experimenting and low volume. Usage limits resets after a few hours.</li>
<li><strong>Claude Pro ($20/month):</strong> Much higher usage, access to the newest models, longer context windows. Right for any agent doing regular marketing.</li>
<li><strong>Claude for Work (Team/Enterprise):</strong> If you have staff or want to manage usage across your agency. Overkill for a solo producer.</li>
</ul>

<p>Start with Free. Upgrade to Pro if you hit limits, which you will within about 3 weeks if you're working the playbook.</p>

<h2>Step 2: Build your "Agent Context" prompt</h2>
<p>The single highest-leverage setup move: write a one-page context about yourself that you paste at the start of every new conversation. Claude will write dramatically better once it knows who you are.</p>

<p>Copy this template, fill in the blanks, save it in a note-taking app, and paste it before any marketing prompt:</p>

<div class="prompt-box">
<div class="prompt-box-label">Agent context template</div>
<button class="copy-btn">Copy</button>
<pre>You are my marketing associate. Before you write anything, here's the context.

ABOUT ME:
- Name: [Your name]
- Agency: [Your agency name]
- State(s) licensed: [State abbreviations]
- Lines I sell: [e.g., Life, Medicare Supplement, Medicare Advantage, Final Expense, Indexed Universal Life]
- Years in the business: [Number]

MY IDEAL CLIENT:
- Age range: [e.g., 55-70]
- Life stage: [e.g., pre-retirement, empty-nester, business owner]
- Income/assets: [e.g., middle-class retirees with $200K-$1M saved]
- Geographic focus: [e.g., Harris County TX, specific city, nationwide]
- Key concerns in their life right now: [e.g., outliving savings, healthcare costs, leaving a legacy]

MY OFFER / DIFFERENTIATION:
- What makes me different: [e.g., "I work with 14 carriers so I shop the whole market," or "I specialize in business-owner life insurance strategies"]
- The one thing I want to be known for: [e.g., "the Medicare planning guy for retiring teachers"]

MY VOICE:
- Tone: [e.g., warm but direct, no jargon, conversational, plainspoken]
- Phrases I use often: [List 3-5 you actually say]
- Phrases I'd never use: [e.g., "synergy," "leverage," "let's circle back"]

COMPLIANCE NOTES:
- I am captive with [carrier] / I am independent
- My state requires [specific disclaimers you need]
- I do NOT want you to: mention specific premiums, quote rates, guarantee returns, use superlatives like "best" or "cheapest"

When you write for me, write like a human who respects the reader's time, never use AI-speak phrases like "in today's fast-paced world" or "when it comes to," and keep sentences short enough that a 70-year-old reading on their phone in a grocery store parking lot gets it.

Ready?</pre>
</div>

<p>That context is a force multiplier. Paste it at the top of any new conversation and every output is better.</p>

<h2>Step 3: Save your voice samples</h2>
<p>Claude writes generically until it sees how you write. Grab three things you've actually written — an old email to a client, a Facebook post, a voicemail transcript — and keep them in a note. At the start of any "write for me" prompt, paste one or two as voice samples.</p>

<div class="prompt-box">
<div class="prompt-box-label">Voice sample primer</div>
<button class="copy-btn">Copy</button>
<pre>Before you write anything for me, here are three examples of how I actually talk to clients and prospects. Match this voice.

SAMPLE 1 (email I sent last month):
[Paste 200-400 words of an email you actually wrote]

SAMPLE 2 (social post that got engagement):
[Paste a Facebook or LinkedIn post]

SAMPLE 3 (voicemail transcript):
[Paste or describe how you talk on the phone]

Study the pacing, sentence length, the specific phrases I use, the places where I drop formality. When you write, sound like this. Don't smooth it out, don't make it more "professional." Match me.</pre>
</div>

<h2>Step 4: Data and privacy rules</h2>

<div class="callout warning">
<div class="callout-title">Never paste into Claude</div>
<p>Client names with DOB/SSN. Health information (HIPAA). Beneficiary details. Policy numbers. Bank info. Anything protected under NPI, PHI, or state privacy laws.</p>
</div>

<p>Claude's free and paid consumer tiers are not HIPAA-compliant. If you need to discuss a specific client situation, anonymize it: "A 63-year-old retiree in Texas with $400K in IRA savings" instead of "John Smith, DOB 4/12/1961, $412,000 in Fidelity IRA."</p>

<h2>Step 5: The two Projects you should create</h2>
<p>Inside Claude.ai, "Projects" let you save context that persists across conversations. Set up two:</p>

<h3>Project: "My Marketing"</h3>
<p>Instructions (paste in the project's custom instructions): the Agent Context template from above. Now every conversation in this project starts pre-briefed.</p>

<h3>Project: "Client Scenarios"</h3>
<p>For anonymized client situations and quote comparisons. Keeps your marketing work separate from product/case work.</p>

<div class="callout success">
<div class="callout-title">Why this matters</div>
<p>Most agents skip setup and get Claude outputs that are 70% as good as they could be. Fifteen minutes of context setup puts you at 95%. The agents who do it well produce content that sounds like them, not like generic AI.</p>
</div>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item">
<input type="checkbox" id="m2-1" data-key="m2-1">
<label for="m2-1">Fill in the Agent Context template above with your specifics. Save it in Notes, Evernote, or wherever.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m2-2" data-key="m2-2">
<label for="m2-2">Collect 3 voice samples: an email, a social post, and a voicemail transcript or talk track.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m2-3" data-key="m2-3">
<label for="m2-3">Set up the "My Marketing" and "Client Scenarios" projects in Claude.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m2-4" data-key="m2-4">
<label for="m2-4">Test: open a new conversation, paste your context, ask it to "write me one paragraph explaining term life to a 40-year-old parent." Compare with-context vs without-context outputs.</label>
</div>
</div>
"""

write_playbook_page(
    slug="module-02",
    title="Setting up Claude",
    tag="Module 2",
    subtitle="The 10-minute setup that makes every future prompt 3x better. Context, voice samples, projects, and privacy rules.",
    body_html=m2,
)


# ============================================================
# MODULE 3 — The 10 prompt patterns
# ============================================================

m3 = """
<p>Ninety percent of effective prompts are variations of ten patterns. Learn these once and you can produce any marketing asset the rest of the playbook covers without memorizing a new prompt every time. This is the module that makes all the others work.</p>

<h2>Pattern 1: The Briefed Writer</h2>
<p>You give Claude context about what you want, who it's for, and constraints. It writes.</p>

<div class="prompt-box">
<div class="prompt-box-label">Pattern 1</div>
<button class="copy-btn">Copy</button>
<pre>Write [asset type] for [audience] about [topic].

Goal: [what you want the reader to do]
Tone: [from your voice samples]
Length: [word count or time]
Must include: [specific points]
Must NOT include: [forbidden claims, superlatives, specific rates]

Output just the copy, no explanations.</pre>
</div>

<h2>Pattern 2: The Angle Generator</h2>
<p>Before writing, ask Claude for a range of angles. Pick one, then write.</p>

<div class="prompt-box">
<div class="prompt-box-label">Pattern 2</div>
<button class="copy-btn">Copy</button>
<pre>I'm writing [asset type] about [topic] for [audience].

Give me 10 different angles I could take. Each angle should be:
- A one-sentence hook
- A specific promise to the reader
- Distinct from the others (no rephrases)

I'll pick one and we'll write from there.</pre>
</div>

<h2>Pattern 3: The Rewrite</h2>
<p>You already have copy (a rough draft, a voicemail transcript, a carrier one-pager). Claude sharpens it.</p>

<div class="prompt-box">
<div class="prompt-box-label">Pattern 3</div>
<button class="copy-btn">Copy</button>
<pre>Below is a [draft / transcript / document]. Rewrite it so it's:
- Clearer to a [audience description]
- Shorter by about [%]
- In my voice (see samples above)
- Free of jargon — anything a non-insurance-person wouldn't get, translate

Preserve the substance. Don't add claims I didn't make.

[Paste the source material]</pre>
</div>

<h2>Pattern 4: The Multi-Version</h2>
<p>One source idea, multiple formats. Fastest way to get a week of content from one insight.</p>

<div class="prompt-box">
<div class="prompt-box-label">Pattern 4</div>
<button class="copy-btn">Copy</button>
<pre>Take this core idea: [the idea]

Give me versions for each of these channels:
1. A 150-word Facebook post (warm, conversational, ends with a question)
2. A LinkedIn post (250 words, more professional but not corporate)
3. A 60-second video script (me on camera, first person, timestamped)
4. A 50-word SMS to a specific client
5. A subject line and opening paragraph for a blog post
6. A 3-line voicemail script

Same core message, different vehicles. Match each channel's conventions.</pre>
</div>

<h2>Pattern 5: The Counter-Draft</h2>
<p>First draft is usually "correct but bland." Ask Claude to push it.</p>

<div class="prompt-box">
<div class="prompt-box-label">Pattern 5</div>
<button class="copy-btn">Copy</button>
<pre>Here's the draft:
[paste draft]

Now write three alternative versions that each take a different risk:

Version A: More specific and concrete. Replace every abstract claim with a number, a scene, or a named situation.

Version B: Opens with a story. First 50 words should be a scene from someone's actual life.

Version C: Contrarian. Starts by challenging a common belief in my space.

Don't soften them. I want choices.</pre>
</div>

<h2>Pattern 6: The Critic</h2>
<p>Before publishing, have Claude review its own work like an outsider would.</p>

<div class="prompt-box">
<div class="prompt-box-label">Pattern 6</div>
<button class="copy-btn">Copy</button>
<pre>Read the copy below as if you were:
1. A 65-year-old prospect on Medicare who's skeptical of agents
2. A compliance officer at my carrier/IMO
3. A cynical marketer

For each, list the 3 things that would make them stop reading, push back, or flag the piece. Be blunt.

[Paste the copy]</pre>
</div>

<h2>Pattern 7: The Persona Interview</h2>
<p>Want to know what your ideal client is really worried about? Ask Claude to roleplay them.</p>

<div class="prompt-box">
<div class="prompt-box-label">Pattern 7</div>
<button class="copy-btn">Copy</button>
<pre>Roleplay as [ideal client persona]. Details:
- [Age, family situation, income, location]
- [What they're thinking about this week]
- [Their prior experience with agents]

I'm going to interview you about [topic: e.g., "how you think about life insurance for your kids"]. Answer in first person, with specific worries, phrases, and fears. Don't generalize — be specific to a real person in this situation.

Ready? First question: [your question]</pre>
</div>

<p>What comes back is raw material for every piece of copy you'll write for that persona — their actual language, their actual objections.</p>

<h2>Pattern 8: The Specific Translator</h2>
<p>Abstract beats nothing, specific beats abstract. This pattern forces specificity.</p>

<div class="prompt-box">
<div class="prompt-box-label">Pattern 8</div>
<button class="copy-btn">Copy</button>
<pre>Read this piece of copy. Every vague claim, replace with a specific number, name, time, or example.

Rules:
- "Save money" → "$X less per month on average"
- "Years of experience" → "14 years, 800+ policies placed"
- "A lot of options" → "23 carriers"
- "Soon" → "before December 7"

If I can't back up a specific claim, flag it and suggest a safer specific I could back up.

[Paste the copy]</pre>
</div>

<h2>Pattern 9: The Hook Farm</h2>
<p>For every post or email, generate 10 hooks. Pick one. Throw away the other nine.</p>

<div class="prompt-box">
<div class="prompt-box-label">Pattern 9</div>
<button class="copy-btn">Copy</button>
<pre>Topic: [the idea]
Audience: [who you're writing for]
Format: [Facebook post / blog intro / email subject line]

Give me 10 hooks. Each one is just the first 15 words — the line that earns the next sentence. Different patterns:
- Contrarian statement
- Specific number
- Question the reader can't ignore
- Personal confession
- Breaking news / news hook
- Warning
- Specific character
- Unusual observation
- Reframe of common belief
- Direct address to a specific pain

No explanations. Just the 10 hooks.</pre>
</div>

<h2>Pattern 10: The Compliance Pre-Check</h2>
<p>Not a substitute for your carrier's compliance review, but catches the obvious stuff.</p>

<div class="prompt-box">
<div class="prompt-box-label">Pattern 10</div>
<button class="copy-btn">Copy</button>
<pre>Review the copy below for potential compliance issues common in [insurance line: Medicare, life, health, P&C, etc.].

Flag:
- Superlatives that can't be backed ("best," "cheapest," "lowest")
- Guaranteed return language in life/annuity
- Medicare: CMS-prohibited terms, missing required disclaimers
- Claims about competitors
- Rate or premium specifics that could go stale
- Fear-based or high-pressure language
- Missing required disclosures

Return a list of flags with specific phrases to change. Then give me a revised version with fixes applied.

[Paste the copy]</pre>
</div>

<h2>How to use the patterns</h2>
<p>Most real marketing tasks chain 2-3 patterns:</p>
<ul>
<li><strong>Blog post:</strong> Pattern 2 (angles) → Pattern 1 (write) → Pattern 6 (critic) → Pattern 8 (specifics) → Pattern 10 (compliance)</li>
<li><strong>Social post:</strong> Pattern 9 (hooks) → Pattern 1 (write) → Pattern 5 (counter-drafts)</li>
<li><strong>Video script:</strong> Pattern 7 (persona interview for real fears) → Pattern 1 (write script) → Pattern 8 (specifics)</li>
</ul>

<p>Once you've run each pattern a few times, they become second nature. The rest of this playbook is just these patterns applied to specific asset types.</p>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item">
<input type="checkbox" id="m3-1" data-key="m3-1">
<label for="m3-1">Run each of the 10 patterns at least once, on a low-stakes topic. Get a feel for how they work.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m3-2" data-key="m3-2">
<label for="m3-2">Pattern 7 (persona interview) is the most underrated. Do it with your ideal client persona and save the output — you'll reference it all the time.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m3-3" data-key="m3-3">
<label for="m3-3">Save the 10 patterns somewhere easy to copy-paste from. You'll use them constantly.</label>
</div>
</div>
"""

write_playbook_page(
    slug="module-03",
    title="The 10 prompt patterns",
    tag="Module 3",
    subtitle="Ninety percent of effective marketing prompts are variations of ten patterns. Learn these once; reuse them forever.",
    body_html=m3,
)


# ============================================================
# MODULE 4 — Prospecting emails
# ============================================================

m4 = """
<p>Prospecting emails are the workhorse of modern insurance marketing. Done right, they produce meetings at a cost of nothing except time. Done wrong, they land in spam and never get opened. This module: how to use Claude to write prospecting emails that actually get read.</p>

<h2>The anatomy of an insurance prospecting email</h2>
<ol>
<li><strong>Subject line</strong> — 3-5 words, lowercase, feels personal. Not "Protect Your Family With Our New Policy" — that's an ad.</li>
<li><strong>First line</strong> — a specific reason you're reaching out to <em>this</em> person. This is the make-or-break line.</li>
<li><strong>The pitch</strong> — 2-4 sentences naming the problem and hinting at your solution. Not a full pitch.</li>
<li><strong>Proof</strong> — one specific case or detail that makes you credible.</li>
<li><strong>The ask</strong> — a specific next step. Not "let me know if you're interested" — "15 minutes next Tuesday at 2pm?"</li>
<li><strong>Signature</strong> — your name, title, maybe one line on what you do. Not a giant corporate sig with five links.</li>
</ol>

<h2>Choose your insurance line</h2>
<div class="tabs" data-target=".m4-tabs">
<button class="tab-btn active" data-tab="life">Life / Final Expense</button>
<button class="tab-btn" data-tab="medicare">Medicare</button>
<button class="tab-btn" data-tab="health">Health / ACA</button>
<button class="tab-btn" data-tab="pnc">P&amp;C</button>
<button class="tab-btn" data-tab="commercial">Commercial</button>
</div>

<div class="m4-tabs">

<div class="tab-content active" data-tab="life">
<h3>Life insurance / Final expense</h3>
<p>Your audience is usually 35-75, thinking about family protection or final expenses. They're skeptical of agents. The email has to feel personal and specific.</p>

<div class="prompt-box">
<div class="prompt-box-label">Life prospecting email</div>
<button class="copy-btn">Copy</button>
<pre>Write a cold prospecting email to a homeowner, age 45-60, in [state]. They recently [had a kid / turned 50 / bought a home / got a raise / signed up for a life event newsletter — pick one trigger].

Goal: book a 15-minute discovery call about life insurance options.

The email should:
- Be under 90 words
- Subject line: 4-6 words, lowercase, feels personal (NOT salesy)
- First line: reference the trigger event specifically
- Offer one specific angle (e.g., "I help homeowners with kids figure out the right amount of coverage without over-insuring")
- Proof point: one specific number or outcome you can defend
- CTA: propose a specific 15-min call time
- Signature: just name, licensed-in state, phone

Do NOT use:
- "I hope this email finds you well"
- "I wanted to reach out"
- "Take a look at our comprehensive solutions"
- Any mention of specific premiums

Write three versions with different subject line angles.</pre>
</div>
</div>

<div class="tab-content" data-tab="medicare">
<h3>Medicare (Advantage / Supplement)</h3>
<p>Your audience is 63-75, thoughtful about healthcare, tired of being marketed to by Medicare agents. Respect their time; get to the point.</p>

<div class="prompt-box">
<div class="prompt-box-label">Medicare prospecting email (T-65)</div>
<button class="copy-btn">Copy</button>
<pre>Write a prospecting email to someone turning 65 in the next 90 days, living in [state]. They've probably been getting calls and mail about Medicare for months.

Goal: book a 20-minute Medicare planning call.

The email should:
- Subject line: 3-5 words, feels personal, NOT about "saving money" or "free review"
- Acknowledge briefly that they've been hearing from a lot of people (without naming competitors)
- Make one specific promise: you don't push one carrier, you explain the tradeoffs and they pick
- Include one specific detail about their local market (e.g., "in [city], the top three MA plans are wildly different on Rx coverage")
- CTA: two specific times
- Under 100 words

CMS compliance — this is a lead-generation email, not a marketing of a specific plan:
- Do NOT name specific plans or carriers
- Do NOT make claims about specific benefits or premiums
- Include "We do not offer every plan available in your area. Any information we provide is limited to those plans we do offer in your area. Please contact Medicare.gov or 1-800-MEDICARE to get information on all of your options."

Write 3 variants.</pre>
</div>
</div>

<div class="tab-content" data-tab="health">
<h3>Health / ACA / small-group</h3>
<p>Individual market prospects are price-sensitive and overwhelmed. Small-group decision-makers are HR or owners with limited time.</p>

<div class="prompt-box">
<div class="prompt-box-label">Small-group health email</div>
<button class="copy-btn">Copy</button>
<pre>Write a prospecting email to a small business owner (10-50 employees) in [state]. Target their pain: rising health insurance premiums at renewal.

Goal: book a 20-minute call to review their current plan and options.

Email should:
- Subject: 5-7 words, about renewal / rising costs
- Open with a specific data point about [state] small-group premium increases this year (if you don't have a real one, say "have seen" rather than "stat")
- Name the three things that usually move the needle (plan design changes, carrier comparison, ICHRA/QSEHRA alternatives)
- Propose a no-pressure 20-minute review
- Under 100 words

Write 3 versions, one more casual, one more data-driven, one with a short client story.</pre>
</div>
</div>

<div class="tab-content" data-tab="pnc">
<h3>Personal lines P&amp;C</h3>
<p>Home and auto. Your angle is usually either: they just had a life event, or they're paying too much at renewal.</p>

<div class="prompt-box">
<div class="prompt-box-label">P&amp;C cross-sell email</div>
<button class="copy-btn">Copy</button>
<pre>Write a prospecting email to a new homeowner (bought in the last 6 months) in [state].

Goal: quote their home and auto (bundle) and compare to their current carrier.

Email should:
- Subject: 4-5 words, about their new home (not "save money")
- Open by acknowledging the move (without being creepy about the data)
- Make one specific point about [state]-specific coverage people miss (e.g., "In Texas, most standard policies exclude foundation repair — did yours?")
- Offer a 10-minute quote with their existing dec page
- Under 80 words
- CTA: send dec page or book 10 min

Write 3 variants.</pre>
</div>
</div>

<div class="tab-content" data-tab="commercial">
<h3>Commercial lines</h3>
<p>Commercial is relationship-driven. Cold emails are harder here, but they work for specific vertical plays (contractors, restaurants, specific NAICS codes).</p>

<div class="prompt-box">
<div class="prompt-box-label">Vertical commercial email</div>
<button class="copy-btn">Copy</button>
<pre>Write a prospecting email to an owner of a [vertical: restaurant / contractor / medical practice / trucking company] in [state]. Their policy likely renews in [month].

Goal: book a 15-minute call 60-90 days before renewal to review their program.

Email should:
- Subject: vertical-specific, 5-7 words
- First line: one specific detail about their vertical's common coverage gap (research your vertical first — restaurant = assault &amp; battery, contractor = subcontractor exclusions, etc.)
- Position me as specialist in this vertical (I've placed X policies in this space)
- Acknowledge their broker may be fine but a pre-renewal shop costs them nothing
- CTA: 15 min, specific week
- Under 120 words

Do not disparage their current broker. Keep tone professional.</pre>
</div>
</div>

</div>

<h2>The follow-up sequence</h2>
<p>A single prospecting email is a waste. Most replies come to touch 3 or 4. Use Claude to generate the full sequence:</p>

<div class="prompt-box">
<div class="prompt-box-label">Sequence builder</div>
<button class="copy-btn">Copy</button>
<pre>Given the first email [paste it], write a 5-touch sequence.

- Email 2 (day 3): short nudge. Reference the first email. Add ONE new angle or data point. Under 50 words.
- Email 3 (day 7): soft reframe. Acknowledge no reply is a reply. Offer a lower-friction ask (a 1-page PDF, not a call).
- Email 4 (day 12): case study. Short story of a similar client outcome, anonymized. Under 100 words.
- Email 5 (day 20): breakup. "Closing the loop — I'll stop reaching out. If [situation] changes, feel free to reply or call." Under 40 words.

Keep each email in the same tone as email 1. Vary opening lines. Don't repeat the same hook.</pre>
</div>

<h2>Personalization at scale</h2>
<p>If you're sending at volume, the first line is the personalization. Claude + a spreadsheet of prospects = custom first lines at scale:</p>

<div class="prompt-box">
<div class="prompt-box-label">Custom first line generator</div>
<button class="copy-btn">Copy</button>
<pre>I'll paste a list of prospects below with a short note about each (their situation, recent trigger, or something specific to them). For each, write ONE first line of a cold email — 12-20 words — that references something specific to them and doesn't sound templated.

Don't use:
- "Hope you're well"
- "I came across your profile"
- "Congrats on the [generic thing]"

Be specific. Be human.

PROSPECTS:
1. [Name, situation, trigger]
2. [Name, situation, trigger]
...</pre>
</div>

<p>Paste in 20 prospects with trigger info, get 20 custom first lines. Assembly them with your email template in your cold email tool.</p>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item">
<input type="checkbox" id="m4-1" data-key="m4-1">
<label for="m4-1">Pick your highest-value insurance line. Generate 3 versions of a prospecting email using the appropriate prompt above.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m4-2" data-key="m4-2">
<label for="m4-2">Pick the best version. Build the 5-email sequence around it.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m4-3" data-key="m4-3">
<label for="m4-3">Send to 20 prospects this week. Track opens and replies. Iterate.</label>
</div>
</div>
"""

write_playbook_page(
    slug="module-04",
    title="Prospecting emails",
    tag="Module 4",
    subtitle="Cold email that doesn't look like cold email. Specific prompts for life, Medicare, health, P&C, and commercial lines.",
    body_html=m4,
)


# ============================================================
# MODULE 5 — Social media
# ============================================================

m5 = """
<p>Social media for insurance agents is usually terrible. Recycled carrier graphics. "Happy Monday!" posts with stock photos. The same "Did you know?" facts every agent posts. Nobody cares, nobody engages, and the algorithm punishes it. This module: how to use Claude to produce social content that actually builds an audience.</p>

<h2>Which platforms matter</h2>
<ul>
<li><strong>Facebook:</strong> Still the workhorse for local insurance agents, especially Medicare and life. Older demographics live here.</li>
<li><strong>LinkedIn:</strong> Essential for commercial lines, business-owner life insurance, executive benefits. Also where referral partners live (CPAs, attorneys).</li>
<li><strong>Instagram:</strong> Good for P&amp;C agents targeting younger homeowners, some lifestyle-aligned life insurance. Rarely first priority.</li>
<li><strong>YouTube:</strong> Best long-term SEO moat. Covered more in <a href="module-07.html">Module 7</a>.</li>
<li><strong>TikTok:</strong> Only worth it if you're genuinely comfortable on camera and targeting younger buyers.</li>
</ul>

<p>Pick two. Run them deliberately. Don't try to be everywhere.</p>

<h2>The content mix</h2>
<p>Over any 10 posts, aim for roughly:</p>
<ul>
<li><strong>6 educational</strong> — explainers, common mistakes, myth-busting, glossary</li>
<li><strong>2 personal</strong> — your story, your why, your team, your community</li>
<li><strong>1 social proof</strong> — testimonial, case study (anonymized), milestone</li>
<li><strong>1 direct ask</strong> — "DM me if..." or "Reply with..." — the actual pitch</li>
</ul>

<p>All sell. Not all "ask for the sale." Educational posts build trust; direct-ask posts harvest it. Six-to-one ratio.</p>

<h2>Generate a week of posts in 15 minutes</h2>

<div class="prompt-box">
<div class="prompt-box-label">Weekly social content generator</div>
<button class="copy-btn">Copy</button>
<pre>Generate 7 social media posts for me this week. Mix:
- 4 educational
- 1 personal
- 1 social proof
- 1 direct ask

Platform: [Facebook / LinkedIn]
Audience: [your ideal client, from context]
My topic focus this week: [one theme, e.g., "Medicare open enrollment" or "why most people are underinsured"]

For each post:
- 80-180 words (LinkedIn on the higher end, Facebook on the lower)
- First line is a hook that earns the next sentence
- Uses plain language, no insurance jargon (or defines it inline)
- Ends with a question or clear CTA
- No emojis unless they add meaning

Mix up the opening patterns: question, story, contrarian claim, specific number, personal confession. Don't use the same opening structure twice.

Number them 1-7 with day-of-week suggestions.</pre>
</div>

<h2>The types of posts that work</h2>

<div class="expandable">
<button class="expandable-toggle">1. The "common mistake" post</button>
<div class="expandable-body">
<p>Pattern: "Most people think X. It's actually Y. Here's why."</p>
<div class="prompt-box">
<div class="prompt-box-label">Common mistake post</div>
<button class="copy-btn">Copy</button>
<pre>Write a "common mistake" Facebook post about [topic in my line].

Structure:
- Line 1: hook — state the common mistake as a question or claim
- Lines 2-4: explain why most people believe it
- Lines 5-8: the actual truth and why it matters
- Last line: what to do instead, or a question

130 words max. No emojis. End with "Reply or DM with questions — happy to explain for your specific situation" or similar.</pre>
</div>
</div>
</div>

<div class="expandable">
<button class="expandable-toggle">2. The "specific scenario" post</button>
<div class="expandable-body">
<p>Pattern: a concrete, named situation that shows your expertise and makes the reader think "that's me."</p>
<div class="prompt-box">
<div class="prompt-box-label">Specific scenario post</div>
<button class="copy-btn">Copy</button>
<pre>Write a LinkedIn post about a specific client scenario in [line of business]. Anonymize the client — no real names or identifying details.

Structure:
- Line 1: "Had a call this week with [generic description]..."
- 3-4 sentences: their situation and the problem they didn't know they had
- 2-3 sentences: what we figured out
- Last line: broader lesson for anyone in a similar situation

180 words max. First-person. No jargon. Make the reader see themselves in it.</pre>
</div>
</div>
</div>

<div class="expandable">
<button class="expandable-toggle">3. The "behind-the-scenes" post</button>
<div class="expandable-body">
<p>Pattern: show the human behind the license. People buy from people.</p>
<div class="prompt-box">
<div class="prompt-box-label">Personal post</div>
<button class="copy-btn">Copy</button>
<pre>Write a Facebook post that's personal but connected to my work.

Theme options: pick one and write it:
- Why I got into insurance (the specific moment or person)
- What I learned this week working with clients
- Something in my community I care about that shapes how I work
- A small daily ritual that keeps me going

No "grateful for my clients" / "Monday motivation" / generic content. Actual specifics from my life.

120 words. Warm but not saccharine. End with a small question to the reader.</pre>
</div>
</div>
</div>

<div class="expandable">
<button class="expandable-toggle">4. The "myth buster" post</button>
<div class="expandable-body">
<div class="prompt-box">
<div class="prompt-box-label">Myth buster post</div>
<button class="copy-btn">Copy</button>
<pre>Write a "myth vs. fact" post for Facebook about [topic].

Format:
"MYTH: [common belief]
REALITY: [what's actually true]
WHY IT MATTERS: [1-2 sentences on the consequences of believing the myth]"

Repeat for 3 myths. Under 180 words total.

Must NOT use:
- "Don't let [myth] cost you!"
- Superlatives
- Urgency language that's not real</pre>
</div>
</div>
</div>

<div class="expandable">
<button class="expandable-toggle">5. The "direct ask" post</button>
<div class="expandable-body">
<p>Once every 10 posts or so, make the direct ask. Specific, low-friction.</p>
<div class="prompt-box">
<div class="prompt-box-label">Direct ask post</div>
<button class="copy-btn">Copy</button>
<pre>Write a direct-ask social post.

The ask: [specific offer — e.g., "a 15-minute Medicare review before open enrollment closes," "a home/auto bundle quote," "free 'am I underinsured?' calculator"]

Structure:
- Line 1: specific situation the reader might be in
- Lines 2-3: describe the ask and what they get
- Last line: "Reply [specific word] or DM me if this is you"

90 words max. Should feel like a neighbor saying "by the way, if you ever need..." not a sales pitch.</pre>
</div>
</div>
</div>

<h2>LinkedIn-specific: the longer-form post</h2>
<p>LinkedIn rewards longer, more thoughtful content. When you have a real insight, use this pattern:</p>

<div class="prompt-box">
<div class="prompt-box-label">LinkedIn insight post</div>
<button class="copy-btn">Copy</button>
<pre>Write a LinkedIn post (300-500 words) about [topic].

Structure:
- Hook line (1 sentence that earns the scroll)
- Context (2-3 sentences setting up the problem or observation)
- The specific insight or lesson (body, 3-5 short paragraphs)
- Concrete example (one named scenario — anonymized)
- What this means for the reader
- A question or CTA

Formatting:
- Short paragraphs (1-3 sentences each)
- Space between paragraphs (LinkedIn rewards scannability)
- One or two bolded phrases if a word stands alone
- No emojis at the top (LinkedIn algorithm currently doesn't love them)

Sound like a practitioner, not a content marketer. Not "thought leadership" language. Just clear thinking.</pre>
</div>

<h2>Repurposing one idea into a week of content</h2>

<div class="prompt-box">
<div class="prompt-box-label">One-to-many repurposer</div>
<button class="copy-btn">Copy</button>
<pre>I have one core insight to share this week:
[paste the insight — 2-3 sentences]

Turn it into:
1. A Facebook post (120 words, warm tone)
2. A LinkedIn post (300 words, professional tone)
3. An email newsletter section (200 words)
4. A 60-second video script (first-person, timestamped)
5. A short reel/TikTok script (40 seconds, hook-heavy)
6. A tweet (240 chars max)
7. A text message to a specific prospect (60 words)

Same insight, different delivery for each channel. Don't just rephrase — adapt the structure to each platform's conventions.</pre>
</div>

<h2>This week's task</h2>
<div class="checklist">
<div class="checklist-item">
<input type="checkbox" id="m5-1" data-key="m5-1">
<label for="m5-1">Generate a full week of Facebook posts using the weekly generator prompt. 7 posts.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m5-2" data-key="m5-2">
<label for="m5-2">If you use LinkedIn, generate 3 longer-form insight posts for the week.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m5-3" data-key="m5-3">
<label for="m5-3">Schedule them all out in one sitting. Use Buffer, Later, Meta Business Suite, or whatever your scheduler is.</label>
</div>
<div class="checklist-item">
<input type="checkbox" id="m5-4" data-key="m5-4">
<label for="m5-4">Commit to this rhythm for 4 weeks before judging whether it's working. Consistency matters more than any single post.</label>
</div>
</div>
"""

write_playbook_page(
    slug="module-05",
    title="Social media content",
    tag="Module 5",
    subtitle="Facebook and LinkedIn posts that build an audience instead of the recycled carrier graphics nobody engages with.",
    body_html=m5,
)


print("\n✓ Insurance Playbook Part 1: Landing + Modules 1-5 (6 pages)")
