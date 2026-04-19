#!/usr/bin/env python3
"""40 pages of Business Management expertise content."""
from _build_bizmgmt import write_bm_page, BM_SIDEBAR


def page(slug, title, desc, body, prev=None, nxt=None, rt=3):
    write_bm_page(slug, title, desc, body, reading_time=rt, prev=prev, nxt=nxt)


# ==================== HUB ====================
hub_body_parts = ['<p class="lede">Business management — not theory, not MBA platitudes. The actual operating craft: how to build systems, hire well, read a P&L, make decisions under uncertainty, and run a team that ships.</p>']
hub_body_parts.append('<p style="color:var(--gray-500); font-size:14px;">40 pages · Approx. <strong>~20,000 words</strong> of operational craft.</p>')
for section_title, items in BM_SIDEBAR:
    hub_body_parts.append(f'<h2>{section_title}</h2>')
    hub_body_parts.append('<ul class="hub-list">')
    for slug, label in items:
        if slug == "index": continue
        hub_body_parts.append(f'<li><a href="{slug}.html"><span><span class="hub-title">{label}</span></span><span class="hub-arrow">→</span></a></li>')
    hub_body_parts.append('</ul>')
page("index", "Business Management — 40-Page Operator's Field Guide",
     "Practical business management — designing operating systems, hiring, finance, strategy, sales, execution, leadership. 40 pages of operator-grade content.",
     "\n".join(hub_body_parts), prev=None,
     nxt=("Designing the OS", "operating-systems/designing-the-os.html"), rt=2)


# ============================================================
# OPERATING SYSTEMS (5)
# ============================================================

page("operating-systems/designing-the-os",
     "Designing your business's operating system",
     "An operating system is the collection of meetings, scorecards, docs, and cadences that make a business run without heroics. Here's how to design one.",
     '''
<p class="lede">A business operating system (BOS) is the collection of recurring meetings, written documents, scorecards, and decision cadences that let a business run on rails instead of on heroics. Without one, every week is improvised. With one, the business compounds.</p>

<h2>Why every real operator cares</h2>
<p>The #1 reason founders hit a ceiling is they can't scale themselves. A personal brain isn't a system. An operating system is — and it's what lets the business grow past the founder's daily involvement.</p>

<h2>The five components</h2>
<ol>
  <li><strong>Meetings</strong> — the rhythm. Weekly, monthly, quarterly.</li>
  <li><strong>Scorecards</strong> — the numbers that say how it's going.</li>
  <li><strong>Accountability chart</strong> — who owns what.</li>
  <li><strong>Documents</strong> — SOPs, wikis, decision logs.</li>
  <li><strong>Decision protocols</strong> — how disagreements get resolved, how commitments get made.</li>
</ol>
<p>Miss any one and the others start leaking.</p>

<h2>Meeting rhythm (the backbone)</h2>
<ul>
  <li><strong>Daily standup</strong> — 10 min, team-level. "What I did, what I'm doing, what's blocked."</li>
  <li><strong>Weekly team meeting (L10 / WBR)</strong> — 60-90 min. Scorecard review, issue list, to-dos. See <a href="weekly-business-review.html">Weekly business review</a>.</li>
  <li><strong>Biweekly 1:1s</strong> — manager + direct report, 30-45 min. Not status updates — growth, blockers, feedback.</li>
  <li><strong>Monthly business review</strong> — leadership. KPIs vs. plan, budget, resource allocation.</li>
  <li><strong>Quarterly planning</strong> — 1 day offsite. Set next quarter's rocks/OKRs.</li>
  <li><strong>Annual planning</strong> — 2-3 days. Longer horizon, strategic bets.</li>
</ul>

<h2>Scorecards (the nervous system)</h2>
<p>Every seat has a scorecard. 5-7 measurable numbers per team that tell you if the work is working. Reviewed weekly. No discussion — just read the number. Green, yellow, red.</p>
<p>Without scorecards, you argue about feelings. With them, you argue about reality.</p>

<h2>Accountability chart (not an org chart)</h2>
<p>An accountability chart is a clear mapping of <em>seats</em> to <em>functions</em>. Each seat has 3-7 "accountabilities" — the actual things that seat owns. One name per seat. One seat per function.</p>
<p>Most orgs have 3 people all kind-of responsible for marketing, which means nobody is. The accountability chart forces clarity.</p>

<h2>Documents (the institutional memory)</h2>
<ul>
  <li><strong>SOPs</strong> — how we do this (see <a href="sops.html">SOPs</a>)</li>
  <li><strong>Decision logs</strong> — what we decided and why (see <a href="decision-logs.html">Decision logs</a>)</li>
  <li><strong>Company wiki</strong> — policies, benefits, culture</li>
  <li><strong>Strategic memo</strong> — annual refresh of "what are we doing and why"</li>
</ul>

<h2>Decision protocols</h2>
<p>Who makes which decisions? Without this, everything escalates to the founder. Define:</p>
<ul>
  <li>Decisions owned by individual contributors</li>
  <li>Decisions requiring manager approval</li>
  <li>Decisions requiring leadership sign-off</li>
  <li>Decisions requiring board-level approval</li>
</ul>
<p>Write it down. Tape it to the wall.</p>

<h2>The rollout</h2>
<ol>
  <li>Start with the weekly team meeting. Just that. Get good at it.</li>
  <li>Add scorecards once weekly is locked in.</li>
  <li>Add the accountability chart third.</li>
  <li>SOPs and decision logs accumulate naturally over 6-12 months.</li>
  <li>Quarterly planning emerges after you can see a quarter clearly.</li>
</ol>
<p>Trying to install the whole system at once collapses. Build it one layer at a time.</p>

<h2>Frameworks that work</h2>
<p>EOS/Traction, Scaling Up, Amazon's S-Team operating model, Bridgewater's principles — each is a published operating system. Pick one, modify, commit. Don't Frankenstein three of them.</p>
''', prev=("Business Management overview", "../index.html"),
     nxt=("Weekly business review", "weekly-business-review.html"), rt=4)


page("operating-systems/weekly-business-review",
     "The weekly business review (WBR)",
     "The single most important meeting in any operating system. What goes on the agenda, what stays off, and why skipping it silently breaks companies.",
     '''
<p class="lede">The Weekly Business Review — also called the L10, the staff meeting, the WBR — is the heartbeat of a running business. 60-90 minutes a week. Same agenda. Same people. Non-negotiable. Every operator I respect runs one.</p>

<h2>Why weekly</h2>
<p>Monthly is too slow — problems compound for 30 days before they surface. Daily is too frequent — not enough changes day-to-day to warrant leadership time. Weekly is the right cadence: problems surface within a week, get addressed, status changes tracked.</p>

<h2>The canonical agenda (EOS/L10 format — use it)</h2>
<ul>
  <li><strong>Segue</strong> (5 min) — quick personal + professional bests</li>
  <li><strong>Scorecard review</strong> (5 min) — read the numbers, flag off-track</li>
  <li><strong>Rock review</strong> (5 min) — quarterly priorities status: on track / off track</li>
  <li><strong>Customer/employee headlines</strong> (5 min) — meaningful wins + issues</li>
  <li><strong>To-do list review</strong> (5 min) — previous week's to-dos complete/not</li>
  <li><strong>IDS (Identify, Discuss, Solve)</strong> (60 min) — the issue list, worked through one at a time</li>
  <li><strong>Conclude</strong> (5 min) — recap, ratings, close</li>
</ul>
<p>Total: 90 min. Hard stop.</p>

<h2>The issue list</h2>
<p>The main work happens here. Throughout the week, anyone adds items to a shared issue list. In the meeting, the group picks the most important one, works through Identify → Discuss → Solve, then the next.</p>
<ul>
  <li><strong>Identify:</strong> what's the real problem? (Often 5 minutes of clarification reveals the issue is different than first stated.)</li>
  <li><strong>Discuss:</strong> short. Don't re-litigate.</li>
  <li><strong>Solve:</strong> a to-do assigned to one person with a deadline. Or a decision made and documented.</li>
</ul>

<h2>Rules that keep it tight</h2>
<ul>
  <li><strong>Start on time. End on time.</strong> Same day and hour every week.</li>
  <li><strong>Same people every week.</strong> Substitutes break the rhythm.</li>
  <li><strong>No status updates.</strong> Status goes in a written doc before the meeting. Meeting time is for issues, not reports.</li>
  <li><strong>To-dos are owned by one person with a date.</strong> "The team will look into it" = no one is doing it.</li>
  <li><strong>If an issue takes more than 10 min, it's probably a separate working session.</strong></li>
</ul>

<h2>Anti-patterns</h2>
<ul>
  <li>Meeting canceled "because we're busy" — you're busy because meetings get canceled</li>
  <li>Status updates that no one reads beforehand</li>
  <li>Issue list that grows but never shrinks</li>
  <li>To-dos that roll over week after week (accountability break)</li>
  <li>Side conversations that swallow the agenda</li>
</ul>

<h2>The discipline of the pre-read</h2>
<p>Amazon's famous version: 6-page memo, read silently for the first 15-20 minutes of the meeting. Everyone starts with full context. No "what's the status?" questions. The rest of the meeting is discussion.</p>
<p>Worth emulating for monthly and quarterly reviews. For weekly, a shorter pre-read (dashboard + scorecard) is usually enough.</p>

<h2>When the WBR is working</h2>
<p>Signs of a functioning WBR:</p>
<ul>
  <li>Issues get resolved, not just discussed</li>
  <li>The issue list oscillates, doesn't only grow</li>
  <li>Scorecard metrics trend up over months</li>
  <li>Same problems don't reappear</li>
  <li>Team attendance is voluntary + high</li>
</ul>

<h2>When it's broken</h2>
<ul>
  <li>Meeting is dominated by one person (usually the founder)</li>
  <li>Issues are discussed forever, decided never</li>
  <li>To-dos complete rate under 70%</li>
  <li>People bring personal grievances disguised as "issues"</li>
  <li>Meeting is canceled more than twice per quarter</li>
</ul>

<h2>Scaling the WBR</h2>
<p>Each team/department should run its own L10. The exec team runs an L10 above those. Issues that can't be solved at team-level roll up. Prevents the founder's calendar from becoming everyone's issue list.</p>
''', prev=("Designing the OS", "designing-the-os.html"),
     nxt=("Meetings that don't waste time", "meetings.html"), rt=4)


page("operating-systems/meetings",
     "Meetings that don't waste time",
     "Most meetings are broken. Here's the discipline that makes the few you keep actually productive — and the rest safely cancelable.",
     '''
<p class="lede">Most meetings shouldn't exist. Of the ones that should, most are run poorly. The art isn't "more meetings" or "no meetings" — it's knowing which need to happen, what makes them work, and killing the rest.</p>

<h2>The test: does this need to be a meeting?</h2>
<p>Before scheduling anything, ask:</p>
<ol>
  <li>Is this a decision that requires real-time debate? (Meeting yes.)</li>
  <li>Does this need creative collaboration — whiteboard, brainstorm? (Meeting yes.)</li>
  <li>Does this need high-bandwidth social connection — relationship, culture? (Meeting yes.)</li>
  <li>Is this information that could be an email, memo, or doc? (Meeting NO.)</li>
  <li>Is this status updates? (Async in writing.)</li>
</ol>
<p>Default: no. Make people justify "why a meeting."</p>

<h2>Meeting types + their formats</h2>

<h3>Decision meetings</h3>
<p>A real decision needs to be made. Format:</p>
<ul>
  <li>Clear decision stated at top ("should we hire person X?")</li>
  <li>Pre-read with context + options (sent ≥24h before)</li>
  <li>Discussion</li>
  <li>Decision + decision-maker named (not a vote)</li>
  <li>Documented in the decision log</li>
</ul>

<h3>Brainstorming / working sessions</h3>
<ul>
  <li>Pre-read: problem statement + constraints</li>
  <li>Max 5-6 people</li>
  <li>Facilitator keeps time + captures outputs</li>
  <li>End with action items</li>
</ul>

<h3>1:1s</h3>
<p>See <a href="../people/one-on-ones.html">One-on-ones</a>. Not status. Growth, blockers, feedback.</p>

<h3>Standups</h3>
<p>10 min max. Team-level. Three questions: What'd I do, what am I doing, what's blocked. If it takes 30 min, you have the wrong format or wrong size group.</p>

<h3>All-hands</h3>
<p>Monthly or quarterly. One-way + Q&A. Keep at 60 min max. Async recording for anyone who missed.</p>

<h2>Rules that save hours</h2>

<h3>Defaults</h3>
<ul>
  <li>30 min, not 60 min</li>
  <li>15 min standups, not 30</li>
  <li>End 5 minutes early every time (respect the calendar)</li>
  <li>Cameras on (video teams); trade some meetings for async loom videos</li>
</ul>

<h3>The agenda rule</h3>
<p>No agenda, no meeting. If someone can't write a 3-line agenda, the meeting isn't ready to happen.</p>

<h3>The pre-read</h3>
<p>For decision/review meetings, required. Shared ≥24h before. First 5-15 min of the meeting is silent reading if the pre-read wasn't consumed. Forces prep or forces waiting — either way, nobody wings it.</p>

<h3>Notes + action items</h3>
<p>Every meeting ends with:</p>
<ul>
  <li>What was decided</li>
  <li>Who owns what action, by when</li>
  <li>Where it's documented</li>
</ul>
<p>Without this, the meeting didn't happen.</p>

<h3>No-laptop rule</h3>
<p>In-room meetings: laptops closed unless you're the note-taker. Nobody "multitasks well" in a meeting; they just check out.</p>

<h2>Killing standing meetings</h2>
<p>Once a quarter, audit every recurring meeting:</p>
<ul>
  <li>What's the purpose? Still valid?</li>
  <li>Is the output used?</li>
  <li>Could this be async?</li>
  <li>Who would miss this if canceled?</li>
</ul>
<p>Kill the unclear ones. Canceling 30% of your recurring meetings rarely breaks anything.</p>

<h2>Async alternatives</h2>
<ul>
  <li><strong>Status updates:</strong> shared doc or Slack/Notion weekly thread</li>
  <li><strong>Announcements:</strong> written memo, not all-hands</li>
  <li><strong>FYI/heads-up:</strong> Slack DM or email</li>
  <li><strong>Walk-through/demo:</strong> Loom video, watched at 1.5x speed</li>
  <li><strong>Brainstorming:</strong> some of it works async via shared docs</li>
</ul>

<h2>The annual meeting audit</h2>
<p>At year-end, tally: how many hours did this team spend in meetings this year? What was the output? Start the next year with a 30% budget cut on meeting time and see what happens. (Almost nothing breaks.)</p>
''', prev=("Weekly business review", "weekly-business-review.html"),
     nxt=("SOPs that get used", "sops.html"), rt=4)


page("operating-systems/sops",
     "SOPs that actually get used",
     "Standard Operating Procedures fail when they're written by people who don't do the work, stored where nobody looks, and updated never. Here's how to make them useful.",
     '''
<p class="lede">SOPs — Standard Operating Procedures — are the documented "how we do this." They exist on paper at most businesses and in reality at few. The gap between the two is where quality, training time, and institutional knowledge all leak out.</p>

<h2>Why SOPs matter</h2>
<ul>
  <li><strong>Onboarding</strong> — new hires get up to speed on specific processes without hours of 1:1 time</li>
  <li><strong>Consistency</strong> — the 100th customer gets the same quality as the 1st</li>
  <li><strong>Delegation</strong> — you can hand work off without reinventing the explanation</li>
  <li><strong>Quality control</strong> — deviations from SOP get noticed and investigated</li>
  <li><strong>Company value</strong> — documented operations are worth more when you sell</li>
</ul>

<h2>Why most SOPs fail</h2>
<ul>
  <li>Written by a consultant who doesn't do the job</li>
  <li>So generic they don't help</li>
  <li>Outdated within 3 months</li>
  <li>Stored somewhere nobody looks</li>
  <li>No one's accountable for keeping them current</li>
  <li>Too long to read before just asking someone</li>
</ul>

<h2>The rules of useful SOPs</h2>

<h3>1. Written by the person who does the job</h3>
<p>The person with the fingers on the keyboard is the only one who actually knows the steps. The manager writes a framework; the operator fills in the details.</p>

<h3>2. Short > complete</h3>
<p>A 2-page SOP someone reads beats a 50-page SOP nobody opens. When in doubt, cut.</p>

<h3>3. Actionable, not theoretical</h3>
<p>"Monitor customer satisfaction" is not a step. "At the end of every onboarding call, send this survey link" is.</p>

<h3>4. Include screenshots, videos, real examples</h3>
<p>Text alone doesn't cut it for software-mediated work. Loom videos where you perform the task beat 40 bullet points every time.</p>

<h3>5. Versioned + dated</h3>
<p>Every SOP has: last-updated date, owner, review date. Older than a year without review? Probably stale.</p>

<h3>6. One place to live</h3>
<p>Notion page. Wiki. SharePoint. Pick one. Everyone finds SOPs the same way. "Which Google Drive folder was the onboarding SOP in again?" = SOPs aren't being used.</p>

<h2>The SOP template</h2>
<pre><code>TITLE: [What this SOP covers]
OWNER: [Who maintains this]
LAST UPDATED: [Date]
NEXT REVIEW: [Date]

WHEN TO USE THIS SOP
[One-paragraph description of the situation this covers]

OUTCOME
[What "done" looks like]

STEPS
1. [Specific action]
2. [Specific action]
   - Sub-step or nuance
3. [Specific action]
...

COMMON ISSUES + FIXES
- Problem X → do Y
- Problem Z → escalate to [person]

RELATED SOPs
- Link
- Link</code></pre>

<h2>The adoption loop</h2>
<ol>
  <li><strong>Write it</strong> — the operator drafts, the manager reviews, one round of edits.</li>
  <li><strong>Test it</strong> — someone else follows the SOP to complete the task. Notes every place they had to ask a question.</li>
  <li><strong>Update based on test</strong> — fill in the gaps found.</li>
  <li><strong>Publish</strong> — land in the wiki, link from relevant onboarding docs.</li>
  <li><strong>Review quarterly</strong> — the owner confirms it's still accurate. If they can't, someone else inherits.</li>
</ol>

<h2>When to create an SOP</h2>
<ul>
  <li>The second time you're about to explain the same thing</li>
  <li>Before onboarding a new person to a role</li>
  <li>When a process spans 3+ people or 3+ steps</li>
  <li>When there's a compliance or safety element</li>
  <li>When the person who does the work might leave</li>
</ul>

<h2>When NOT to create one</h2>
<ul>
  <li>Truly one-off tasks</li>
  <li>Creative work that varies per instance</li>
  <li>Work that's changing rapidly (write a rough doc, wait until it stabilizes)</li>
</ul>

<h2>Signs your SOP library is working</h2>
<ul>
  <li>New hires reach productivity faster</li>
  <li>Manager time spent on "how do I…" questions drops</li>
  <li>Handoffs don't lose quality</li>
  <li>Audit trails exist when something goes wrong</li>
</ul>

<h2>Signs it's not</h2>
<ul>
  <li>SOP library exists but nobody references it</li>
  <li>Same questions get asked repeatedly</li>
  <li>SOPs are drastically different from actual practice</li>
  <li>Nobody knows who owns updating them</li>
</ul>
''', prev=("Meetings that don't waste time", "meetings.html"),
     nxt=("Decision logs", "decision-logs.html"), rt=4)


page("operating-systems/decision-logs",
     "Decision logs",
     "Most companies forget why they made the decisions they made. Decision logs fix that — one line in a shared doc can save months of re-litigation.",
     '''
<p class="lede">A decision log is a chronological record of significant decisions the business makes — what was decided, why, by whom, with what reasoning. Takes 2 minutes per decision to maintain. Saves months of rework, re-litigation, and "wait, why did we do it that way?" conversations.</p>

<h2>Why decision logs matter</h2>
<p>In a growing company, decisions happen faster than anyone can remember. Six months later, a new hire asks "why do we do X?" — and nobody remembers. The reasons get re-invented poorly, or the decision gets unmade and redone (usually worse).</p>
<p>A decision log is institutional memory. It survives people leaving, meetings forgotten, context lost.</p>

<h2>What belongs in a decision log</h2>
<p>Not every small call. The ones that:</p>
<ul>
  <li>Affect how the business operates going forward</li>
  <li>Involved meaningful debate or trade-offs</li>
  <li>Would be hard to reverse</li>
  <li>Someone might reasonably question in 6 months</li>
</ul>
<p>Examples: pricing changes, org structure shifts, major tool/vendor choices, policy changes, product direction shifts, market entry/exit.</p>

<h2>The entry template</h2>
<pre><code>DATE: [When decided]
DECISION: [One-sentence summary]
OWNER: [Who made the call]
CONTEXT: [What prompted this]
OPTIONS CONSIDERED:
  - A: [pros/cons]
  - B: [pros/cons]
  - C: [chosen — why]
REASONING: [Why C over A and B]
REVISIT: [When or under what conditions to re-evaluate, if applicable]</code></pre>
<p>Total: 3-8 lines. Takes 2 minutes to fill in after a decision meeting.</p>

<h2>Where it lives</h2>
<p>One shared doc. Notion page, Google Doc, Confluence, whatever. Chronological. Searchable. Readable by the relevant leadership circle.</p>
<p>Not every decision needs to be visible to every employee. Scope the log to who needs to know.</p>

<h2>Why the "reasoning" field is the magic</h2>
<p>Future-you or a new team member will see the decision. They need to know <em>why</em>. Without reasoning, the decision is floating in the air — easy to question, easy to unmake.</p>
<p>Good reasoning documents the constraints at the time:</p>
<ul>
  <li>"We chose X because A, B, and C were true in Q2 2026."</li>
  <li>"If those become less true, re-evaluate."</li>
</ul>
<p>This gives future-you permission to change course when the conditions change.</p>

<h2>The revisit field</h2>
<p>Some decisions are clearly conditional:</p>
<ul>
  <li>"Revisit when we hit $1M ARR"</li>
  <li>"Revisit if the vendor changes pricing"</li>
  <li>"Revisit in 6 months regardless"</li>
</ul>
<p>Calendar reminders on revisit dates mean decisions get re-evaluated, not just forgotten.</p>

<h2>Who maintains it</h2>
<p>An operations lead, EA, or founder's chief of staff. Low overhead — they attend meetings, take 2 minutes to log each major decision, keep the doc current.</p>

<h2>Common mistakes</h2>
<ul>
  <li>Logging every decision — too noisy. Stick to significant ones.</li>
  <li>Writing only what was decided, not why — strips the utility.</li>
  <li>Making it private to the CEO — defeats institutional memory.</li>
  <li>Starting a log during a crisis — you need the discipline built before you need it.</li>
  <li>Treating it as a historical record only — use it in decision meetings: "we decided X last quarter, why is this back up?"</li>
</ul>

<h2>The related doc: assumption log</h2>
<p>A cousin of the decision log. Tracks the assumptions your strategy rests on.</p>
<pre><code>"We assumed X was true. If X turns false, Y part of the plan breaks."</code></pre>
<p>Review quarterly. When an assumption turns false, you know which decisions to revisit.</p>

<h2>Decision velocity vs. quality</h2>
<p>Companies often choose: move fast and decide poorly, or decide well and move slowly. A decision log lets you do both — because you can revisit and fix yesterday's mistakes instead of pretending they didn't happen.</p>

<h2>What operators learn from keeping one</h2>
<p>Six months into keeping a decision log, patterns emerge:</p>
<ul>
  <li>Which types of decisions you consistently get wrong</li>
  <li>Which reasoning shortcuts mislead you</li>
  <li>Which "obvious" calls weren't obvious in hindsight</li>
</ul>
<p>This is the meta-skill: learning from your own decision history. Impossible without records.</p>
''', prev=("SOPs that get used", "sops.html"),
     nxt=("Hiring — signal vs noise", "../people/hiring-signal-vs-noise.html"), rt=4)


# ============================================================
# PEOPLE + HIRING (6)
# ============================================================

page("people/hiring-signal-vs-noise",
     "Hiring — signal vs noise",
     "Most hiring processes measure the wrong things. Here's the honest breakdown of what actually predicts performance and what doesn't.",
     '''
<p class="lede">Hiring is the single highest-leverage activity in a company — and the one most managers do worst. The cost of a bad hire is 3-5x their salary when you count ramp, lost output, team drag, and eventual severance. Yet most interview processes measure charisma, not performance.</p>

<h2>What predicts job performance (validated research)</h2>
<p>Meta-analyses of hiring-success predictors, ranked by correlation with actual performance:</p>
<ul>
  <li><strong>Work sample tests</strong> — having them do the actual job (r ≈ 0.54)</li>
  <li><strong>Structured interviews</strong> — same questions, scored rubric (r ≈ 0.51)</li>
  <li><strong>Cognitive ability tests</strong> — r ≈ 0.51</li>
  <li><strong>Integrity tests</strong> — r ≈ 0.41</li>
  <li><strong>Reference checks</strong> (done well) — r ≈ 0.26</li>
  <li><strong>Years of experience</strong> — r ≈ 0.18 (weak)</li>
  <li><strong>Unstructured interviews</strong> — r ≈ 0.14 (shockingly weak)</li>
  <li><strong>Age</strong> — r ≈ 0.01 (no predictive value)</li>
</ul>
<p>What most companies do: unstructured interviews + vibe. What they should do: work samples + structured interviews.</p>

<h2>The core principle: predict work by watching work</h2>
<p>The best interviews are ones where the candidate does something that looks like the actual job. An engineer pairs on real code. A marketer drafts a real email. A salesperson runs a simulated call. The signal is enormous compared to "tell me about a time when you…"</p>

<h2>The hiring process that works</h2>

<h3>Stage 1: Role scorecard (before posting)</h3>
<p>What does success look like in this seat after 90 days? 1 year? If you can't write this in 1 page, you're not ready to hire. See <a href="role-scorecard.html">The role scorecard</a>.</p>

<h3>Stage 2: Sourcing</h3>
<p>Inbound only = slow + biased toward people who see your post. Best hires are often passive candidates sourced directly. Invest in sourcing, not just application review.</p>

<h3>Stage 3: Screen (20-30 min)</h3>
<p>Recruiter or hiring manager. Goals: confirm baseline fit, compensation alignment, motivation. Avoid elaborate questions — this is a filter, not an interview.</p>

<h3>Stage 4: Hiring manager interview (45-60 min)</h3>
<p>Structured. Same questions for every candidate. Scored rubric. Topics:</p>
<ul>
  <li>Deep-dive on a past project relevant to the role</li>
  <li>Situational: "here's a scenario, walk me through how you'd approach it"</li>
  <li>Tradeoff questions that reveal thinking style</li>
</ul>

<h3>Stage 5: Work sample (60-120 min)</h3>
<p>Paid — always. Something concrete they'd actually do in the job. Bonus: do it together so you see their working style, not just the output.</p>

<h3>Stage 6: Panel interviews (60 min each)</h3>
<p>3-5 people from the team. Each person owns 1-2 specific dimensions. Post-interview, each writes their evaluation BEFORE talking to anyone else. Group discussion after — no anchoring.</p>

<h3>Stage 7: References</h3>
<p>Do them. Back-channel even more than front-channel. Ask specific questions: "On a scale of 1-10, where was [candidate] in your team?" "Would you hire them again?" "What was the hardest thing for them?"</p>

<h3>Stage 8: Offer</h3>
<p>Fast. Move decisively. A week to decide + extend beats 3 weeks of deliberation. Top candidates have options; speed matters.</p>

<h2>The "no hire" is cheaper</h2>
<p>When the team is split, default to "no hire." A bad hire costs 3-5x salary. A missed good hire costs... you keep looking. The asymmetry is massive.</p>

<h2>Interview questions that actually reveal something</h2>
<ul>
  <li>"Walk me through the most complex project you've run, end to end."</li>
  <li>"Tell me about a conflict with a peer. What did you do?"</li>
  <li>"What's a decision you made that you later realized was wrong?"</li>
  <li>"Who are the 3 best people you've worked with? What made them great?"</li>
  <li>"If I called [specific former manager], what would they say are your strengths and weaknesses?"</li>
</ul>

<h2>Red flags</h2>
<ul>
  <li>Blames past employers / teammates for problems</li>
  <li>Can't describe their impact in concrete numbers</li>
  <li>Over-polished answers (rehearsed)</li>
  <li>No mistakes in their work history (evasion)</li>
  <li>Over-indexed on credentials vs. outcomes</li>
  <li>Won't share specifics (confidentiality excuse is sometimes real, often a dodge)</li>
</ul>

<h2>Green flags</h2>
<ul>
  <li>Describes failures + what they learned</li>
  <li>Credits team members for wins</li>
  <li>Asks substantive questions about the role + business</li>
  <li>Articulates tradeoffs + uncertainty</li>
  <li>Can describe their impact in numbers</li>
  <li>References check out with specifics</li>
</ul>

<h2>The most underrated signal</h2>
<p>How do they treat the receptionist, coordinator, and anyone not in the interview? The real personality shows up when nobody's "watching."</p>
''', prev=("Decision logs", "../operating-systems/decision-logs.html"),
     nxt=("The role scorecard", "role-scorecard.html"), rt=5)


page("people/role-scorecard",
     "The role scorecard",
     "Before you post a job, write a scorecard. It's the highest-ROI document in hiring — and the cheapest to skip.",
     '''
<p class="lede">A role scorecard is a 1-page document defining exactly what success in the seat looks like. Objective. Measurable. 3-5 outcomes. If you can't write one, you're not ready to hire — and anyone you hire will be set up to fail.</p>

<h2>The core insight</h2>
<p>Most job descriptions list responsibilities ("manage the team, drive results, own the pipeline"). Those are activities, not outcomes. Scorecards describe outcomes — what the person will have produced by month 12.</p>

<h2>The template</h2>
<pre><code>ROLE: [Title]
REPORTS TO: [Manager]
START DATE: [Date]

MISSION (1-2 sentences):
Why this seat exists. What it's for.

OUTCOMES (3-5, specific + measurable):
1. [By when] — [what specifically, with number]
2. [By when] — [what specifically, with number]
3. [By when] — [what specifically, with number]
4. (optional)
5. (optional)

COMPETENCIES (5-8, behavioral):
- [Behavior X the person must exhibit]
- [Behavior Y the person must exhibit]
- ...

CULTURAL FIT (3-5):
- [Our values they must embody]
- ...

DEAL-BREAKERS:
- [Things that would make us pass regardless of skill]</code></pre>

<h2>Outcomes — the heart</h2>

<h3>Bad outcome</h3>
<p>"Grow the sales team." (Not measurable. Not time-bound.)</p>

<h3>Better</h3>
<p>"Within 9 months, grow the team from 3 to 8 quota-carrying reps, maintaining &gt;80% attainment."</p>

<h3>Best</h3>
<p>"By month 12, the sales team has 8 quota-carriers producing $200K/month in new ARR, with &lt;10% first-year churn."</p>
<p>Notice: measurable, time-bound, tied to business outcome.</p>

<h2>3-5 outcomes is the magic number</h2>
<ul>
  <li>Fewer than 3: the role isn't meaty enough</li>
  <li>More than 5: you haven't decided what matters</li>
</ul>

<h2>Competencies</h2>
<p>Specific behaviors the person needs to demonstrate. Not skills/knowledge (those are trainable) — behavioral patterns.</p>
<ul>
  <li>"Moves fast under ambiguity"</li>
  <li>"Gives direct feedback, including upward"</li>
  <li>"Proactively documents decisions"</li>
  <li>"Sees around corners — anticipates 2-3 moves ahead"</li>
</ul>
<p>During interviews, you're testing for these — not just for answers to skill questions.</p>

<h2>Cultural fit</h2>
<p>Specific, not vague. "Must love dogs" isn't culture. "Must default to writing" (for a memo-culture company) or "must be comfortable with radical candor" are cultural fit filters.</p>

<h2>Deal-breakers</h2>
<p>Upfront honesty about things that would make you pass. Examples:</p>
<ul>
  <li>"Must be willing to travel 25%"</li>
  <li>"Must relocate to NYC within 6 months"</li>
  <li>"Must be open to early mornings (working with Asia)"</li>
</ul>
<p>Saves weeks of mutual time.</p>

<h2>Process</h2>
<ol>
  <li>Hiring manager drafts (15-30 min)</li>
  <li>Team review (30 min) — does this match reality?</li>
  <li>CEO/exec review for senior roles</li>
  <li>Lock before posting</li>
</ol>

<h2>How to use the scorecard</h2>

<h3>In sourcing</h3>
<p>The outcomes become your sourcing filter. If the candidate's last role didn't hit similar outcomes, they probably can't hit yours.</p>

<h3>In interviews</h3>
<p>Every question maps to an outcome or competency. "Outcome 1 is $200K/month ARR by month 12 — walk me through how you'd approach the first 90 days."</p>

<h3>In the offer</h3>
<p>Share the scorecard with the finalist. "Here's exactly what success looks like. Any concerns before you sign?" Aligns expectations from day one.</p>

<h3>In onboarding</h3>
<p>First 1:1 starts with the scorecard. "Does this match what you understood the role to be? Anything missing?"</p>

<h3>In performance reviews</h3>
<p>Scorecard IS the review. "At month 3/6/12, here's how you're tracking against the outcomes we set." Less subjective. Less fighting.</p>

<h2>Why most companies skip this</h2>
<ul>
  <li>Feels like extra work upfront</li>
  <li>Forces clarity that managers might not have</li>
  <li>Makes it harder to hire someone who'd been "close enough"</li>
  <li>Makes performance problems visible sooner</li>
</ul>
<p>Every reason is actually a benefit.</p>

<h2>Real example — Sales Leader scorecard</h2>
<pre><code>ROLE: Head of Sales
REPORTS TO: CEO
START: Q2 2026

MISSION: Build the sales org that takes us from $500K to $5M ARR in 18 months.

OUTCOMES:
1. By month 3 — hire + onboard 2 AEs with validated pipeline
2. By month 6 — team runs at 80%+ quota attainment
3. By month 9 — $1.5M ARR closed (from $500K baseline)
4. By month 12 — sales org of 6 producing predictable $200K/mo
5. By month 18 — $5M ARR, repeatable playbook, 2 managers coaching directly

COMPETENCIES:
- Has built a sales team from &lt;5 to &gt;15 before
- Comfortable running process + pipeline reviews weekly
- Coaches reps directly — joins calls, runs role-plays
- Writes the playbook as the team scales
- Data-literate; uses CRM pipeline data daily

FIT:
- Comfortable with radical candor
- Writing-first communicator

DEAL-BREAKERS:
- Won't relocate to NYC HQ
- Doesn't want to be hands-on in first 90 days</code></pre>
''', prev=("Hiring — signal vs noise", "hiring-signal-vs-noise.html"),
     nxt=("Onboarding that compounds", "onboarding.html"), rt=5)


page("people/onboarding",
     "Onboarding that compounds",
     "First 30/60/90 days determine whether a hire becomes an A-player or limps toward mediocrity. Most onboardings are vibes. Here's what works.",
     '''
<p class="lede">Onboarding is the window where new hires form their model of how the company works, what's expected, and whether they'll succeed. A bad onboarding takes 6 months to recover from (if ever). A good one compounds for the entire tenure.</p>

<h2>The goal of onboarding</h2>
<p>At the end of onboarding, the new hire should:</p>
<ol>
  <li>Know exactly what they're expected to accomplish</li>
  <li>Understand how the company operates (not just the culture talk)</li>
  <li>Have relationships with the people they need</li>
  <li>Have produced something of real value</li>
  <li>Feel confident, not overwhelmed</li>
</ol>

<h2>The 30/60/90 framework</h2>

<h3>First 30 days — context + relationships</h3>
<p>Goals:</p>
<ul>
  <li>Understand the business — products, customers, unit economics</li>
  <li>Understand the team — who does what, how decisions flow</li>
  <li>Build rapport with 10-15 key people across functions</li>
  <li>Read the essential docs (strategy memos, SOPs for their role, last few board decks)</li>
  <li>Produce one small, visible win (document something, fix something small, attend a customer call + write notes)</li>
</ul>
<p>What NOT to do: ship major features, make big bets, judge existing systems aloud.</p>

<h3>60 days — scoped contribution</h3>
<p>Goals:</p>
<ul>
  <li>Own one meaningful project end-to-end</li>
  <li>Contribute in their team meetings — have opinions, not just questions</li>
  <li>Begin to push back on things they disagree with (but still learning the nuance)</li>
  <li>Have produced at least one artifact (doc, ship, deal, hire) they're proud of</li>
</ul>

<h3>90 days — operating at pace</h3>
<p>Goals:</p>
<ul>
  <li>Running their full scope</li>
  <li>Delivering outcomes roughly at expectation</li>
  <li>Identified 1-2 systemic improvements to propose</li>
  <li>Clear on any gaps + how to close them</li>
</ul>

<h2>The scaffolding that makes this work</h2>

<h3>Day-one setup</h3>
<p>Day-one friction tells the new hire how the company operates. Every failure (missing laptop, no access, no seat, HR paperwork chaos) sends a signal.</p>
<p>Pre-day-one checklist:</p>
<ul>
  <li>Laptop shipped + configured</li>
  <li>Email, Slack, calendar, all tools invited</li>
  <li>GSuite + document access granted</li>
  <li>Desk/workspace assigned (if in-office)</li>
  <li>Welcome email from manager with day-1 schedule</li>
  <li>Team notified</li>
  <li>Lunch or coffee scheduled with key people for week 1</li>
</ul>

<h3>Week 1 schedule</h3>
<ul>
  <li>Day 1 — HR, tools, manager kickoff, light reading</li>
  <li>Day 2-3 — stakeholder meetings (5-10, 30 min each)</li>
  <li>Day 4-5 — attend live team meetings, start reading docs, small first task</li>
</ul>

<h3>Buddy + manager</h3>
<p>Manager owns performance. Buddy owns daily navigation — answers "where's the deck template?" questions so the new hire doesn't feel like they're bothering the manager.</p>

<h3>Reading lists</h3>
<p>A curated list of 10-20 documents — key strategy memos, operating docs, customer case studies, org structure. Read in first 2 weeks. Prevents learning-by-ambush.</p>

<h3>Explicit 30/60/90 plan</h3>
<p>Written. Signed off by manager + new hire. Revisited every 2 weeks. Clear what "on track" means.</p>

<h2>What managers get wrong</h2>

<h3>Over-promising ambiguous responsibilities</h3>
<p>"Just jump in, run with it." The new hire runs in five directions, accomplishes nothing.</p>
<p>Fix: the scorecard from the hiring process IS their 90-day plan. Concrete outcomes, clear ownership.</p>

<h3>Zero ramp-up structure</h3>
<p>"Figure it out — we're busy." New hire spends 3 months lost, produces nothing, everyone blames them.</p>
<p>Fix: budget 5-10 hours of manager time for first 2 weeks. That investment pays back 100x.</p>

<h3>Trial by fire as policy</h3>
<p>Some cultures think "throw them in the deep end" is a feature. It's not. It filters for swimmers — who would've done fine with onboarding too — at the cost of talented people who needed just a little structure.</p>

<h2>Onboarding + culture transmission</h2>
<p>The first 30 days is when new hires encode the culture. What they see is what they'll do.</p>
<ul>
  <li>Watch people push back respectfully? They'll learn it's safe.</li>
  <li>Watch managers micromanage? They'll micromanage.</li>
  <li>Hear leaders blame instead of own? They'll blame.</li>
</ul>
<p>Treat onboarding as cultural curation, not just a checklist.</p>

<h2>90-day review</h2>
<p>Formal. Real. Two-way. Questions:</p>
<ul>
  <li>What's going well?</li>
  <li>What's hard?</li>
  <li>What should we (manager + company) be doing differently?</li>
  <li>On the original scorecard, where are you?</li>
</ul>
<p>If clear gaps exist at 90 days, call them out. The 90-day mark is when mismatches are cheap to fix — and painful to ignore.</p>

<h2>What good onboarding produces</h2>
<ul>
  <li>Faster time to productivity</li>
  <li>Higher retention (people who feel set up stay)</li>
  <li>Better cultural alignment</li>
  <li>Earlier identification of misfits (and clean exits when needed)</li>
  <li>Trust — new hires see the company operate competently from day one</li>
</ul>
''', prev=("The role scorecard", "role-scorecard.html"),
     nxt=("One-on-ones", "one-on-ones.html"), rt=5)


page("people/one-on-ones",
     "One-on-ones done right",
     "The most important manager meeting — and the one most managers run worst. What 1:1s are for, what they're not, and how to run one that changes the relationship.",
     '''
<p class="lede">One-on-ones between manager and direct report are the most important recurring meeting in management. They're also the most frequently misrun. Done well, they build trust, surface issues early, and accelerate the person's growth. Done as status updates, they waste an hour a week.</p>

<h2>What 1:1s are NOT</h2>
<ul>
  <li><strong>Not status updates.</strong> Status goes in writing. 1:1s are for things status reports can't carry.</li>
  <li><strong>Not task assignment.</strong> Send a Slack message.</li>
  <li><strong>Not informational updates.</strong> Email.</li>
  <li><strong>Not performance reviews.</strong> Different meeting.</li>
</ul>

<h2>What 1:1s ARE for</h2>
<ul>
  <li><strong>The human relationship.</strong> Check-in on the person, not just the work.</li>
  <li><strong>Surfacing blockers.</strong> What's hard right now? What can I help with?</li>
  <li><strong>Growth.</strong> Coaching, feedback, development.</li>
  <li><strong>Context transfer.</strong> What's the direct report missing that I know?</li>
  <li><strong>Feedback — both directions.</strong> What should I be doing differently as your manager?</li>
  <li><strong>Career conversations.</strong> Where do you want to go? What's the path?</li>
</ul>

<h2>Frequency + length</h2>
<ul>
  <li><strong>Default:</strong> 30-45 min, every week</li>
  <li><strong>Senior reports:</strong> 60 min every 2 weeks</li>
  <li><strong>New hires:</strong> 30 min weekly for first 3 months (maybe more frequent first month)</li>
</ul>
<p>Don't cancel these. Ever. Reschedule if needed. Canceling sends the message that they matter less than every other meeting.</p>

<h2>Who owns the agenda</h2>
<p>The direct report. They bring topics. The manager can suggest, but the direct report's time gets priority.</p>
<p>In practice: shared doc. Both parties add bullets during the week. Revisit at the start.</p>

<h2>The default agenda (when they didn't bring one)</h2>
<ol>
  <li>How are you? (Actually. Not "fine.")</li>
  <li>What's going well this week?</li>
  <li>What's hard?</li>
  <li>What do you want my help with?</li>
  <li>Feedback for me?</li>
  <li>Anything I should know that I might not?</li>
</ol>

<h2>Questions that actually surface signal</h2>

<h3>Instead of "How's it going?"</h3>
<ul>
  <li>"What's been the hardest part of your week?"</li>
  <li>"What decisions are you sitting on right now?"</li>
  <li>"Where's your head at on [project X]?"</li>
  <li>"What would you change about how the team's operating?"</li>
</ul>

<h3>For growth</h3>
<ul>
  <li>"What's a thing you want to get better at?"</li>
  <li>"When were you most energized this week?"</li>
  <li>"When were you least energized?"</li>
  <li>"Where do you see yourself in 18 months?"</li>
</ul>

<h3>For context</h3>
<ul>
  <li>"What don't I know that I should?"</li>
  <li>"Anything about your scope that doesn't make sense?"</li>
  <li>"Who on the team do you wish you worked with more?"</li>
</ul>

<h2>Notes</h2>
<p>Keep a shared doc. Each meeting has a section. Notes include:</p>
<ul>
  <li>Key topics discussed</li>
  <li>Action items (with owner + date)</li>
  <li>Anything to revisit next time</li>
</ul>
<p>Revisit last week's notes first. Otherwise nothing persists.</p>

<h2>Red flags in 1:1s</h2>
<ul>
  <li>Consistently short — you're not going deep</li>
  <li>Direct report brings no agenda — they don't feel ownership</li>
  <li>Only status updates — the format has degenerated</li>
  <li>Manager does most of the talking — reverse it</li>
  <li>No feedback (either direction) — trust isn't there yet</li>
  <li>Repeated cancellations — subtle disrespect</li>
</ul>

<h2>When the relationship is new (first 6-12 weeks)</h2>
<p>Extra investment in rapport + understanding:</p>
<ul>
  <li>Share your operating style: how you like to work, decide, communicate</li>
  <li>Ask theirs</li>
  <li>Share expectations explicitly</li>
  <li>Normalize giving/receiving feedback early (before any crisis)</li>
</ul>

<h2>When things are going badly</h2>
<p>The 1:1 is where you address it. Not email. Not Slack. Not a surprise performance review.</p>
<ul>
  <li>Be specific: "In the meeting yesterday, I noticed [behavior]. Here's what I'd prefer: [behavior]."</li>
  <li>Check for their view: "Does that land? What's your perspective?"</li>
  <li>Agree on next steps</li>
</ul>

<h2>Feedback both directions</h2>
<p>"Is there anything I should do differently as your manager?" — ask every meeting, or at least monthly. Expect the answer to be "no" the first few times. Build trust. They'll eventually tell you.</p>
<p>When they do, take it. Don't defend. Reflect. Come back next week with what you changed.</p>

<h2>The payoff of doing 1:1s well</h2>
<ul>
  <li>Retention goes up</li>
  <li>Performance issues get caught early — cheap to fix</li>
  <li>You see blind spots in the org</li>
  <li>Direct reports feel invested in</li>
  <li>Your reputation as a manager becomes an asset, not a liability</li>
</ul>
''', prev=("Onboarding that compounds", "onboarding.html"),
     nxt=("Performance reviews", "performance-reviews.html"), rt=5)


page("people/performance-reviews",
     "Performance reviews that actually work",
     "Most performance reviews are surprise-filled, documentation-theater, and leave both parties worse off. Here's a system that doesn't.",
     '''
<p class="lede">Traditional performance reviews — once a year, with surprises, anchored on a rating, delivered in dread — are a broken ritual. The fix isn't better review forms. It's real-time feedback all year, with reviews as a formal summary, not the only time honest conversations happen.</p>

<h2>The design principle</h2>
<p>"No surprises" at the review. If there's something negative in the review, the person heard it in conversation months ago. If there's something positive, same. The review formalizes what's been discussed, doesn't introduce it.</p>

<h2>What reviews should actually do</h2>
<ul>
  <li>Summarize performance against agreed outcomes</li>
  <li>Reinforce strengths</li>
  <li>Highlight growth areas with specific actions</li>
  <li>Calibrate compensation decisions</li>
  <li>Align on goals for the next period</li>
  <li>Document, for legal + HR record</li>
</ul>

<h2>What they should NOT do</h2>
<ul>
  <li>Deliver surprise bad news</li>
  <li>Be the first time feedback is given</li>
  <li>Replace ongoing coaching</li>
  <li>Reduce a person's performance to a number</li>
</ul>

<h2>Cadence</h2>
<ul>
  <li>Annual comprehensive review (aligned with comp planning)</li>
  <li>Mid-year check-in (shorter, adjust course)</li>
  <li>Weekly 1:1s provide ongoing feedback (the real engine)</li>
  <li>Monthly or quarterly outcomes-based conversation (tied to the scorecard)</li>
</ul>

<h2>The review structure</h2>

<h3>1. Self-assessment (employee, 1 week prior)</h3>
<ul>
  <li>What you accomplished (vs. objectives)</li>
  <li>What went well</li>
  <li>What was hard</li>
  <li>Growth areas you see</li>
  <li>Goals for next period</li>
</ul>

<h3>2. Manager's review draft</h3>
<ul>
  <li>Strengths (3-5 specific examples, not generic)</li>
  <li>Growth areas (2-3 specific + actionable)</li>
  <li>Performance against outcomes (the scorecard)</li>
  <li>Rating (if your company uses them)</li>
  <li>Compensation recommendation</li>
  <li>Development plan</li>
</ul>

<h3>3. Peer/cross-functional input</h3>
<p>360-style feedback from 3-5 colleagues. Structured — "what does X do well? where could X improve?" — not open-ended.</p>

<h3>4. Calibration meeting (peer managers)</h3>
<p>Before sharing reviews with employees, managers sit together and calibrate. Is Joe's "exceeds expectations" the same as Maria's "exceeds"? Without calibration, ratings drift by manager, creating unfairness.</p>

<h3>5. Review conversation (60-90 min)</h3>
<p>Not a recitation. Discussion.</p>
<ul>
  <li>Open with the self-assessment — ask how they see their year</li>
  <li>Share your view — acknowledge what aligns + diverges</li>
  <li>Focus most time on 2-3 things: what they did best + what would help them grow most</li>
  <li>Discuss compensation if that's decided</li>
  <li>Co-author goals for next period</li>
</ul>

<h3>6. Written summary</h3>
<p>You write it. Shared with the employee. Signed by both. Filed.</p>

<h2>Ratings — use or skip?</h2>
<p>Companies split on this. Arguments:</p>

<h3>For ratings</h3>
<ul>
  <li>Calibration across teams requires a shared scale</li>
  <li>Compensation decisions are harder without them</li>
  <li>Legal/HR record benefits</li>
  <li>Forces managers to actually decide on performance</li>
</ul>

<h3>Against ratings</h3>
<ul>
  <li>One number hides nuance</li>
  <li>Ratings anchor conversations on the number, not the content</li>
  <li>Forced distributions (bell curves) breed politics</li>
  <li>Demoralizing for most employees (who rate themselves higher than the manager rates them)</li>
</ul>
<p>Middle path: use ratings for calibration + comp, but don't center the conversation on them. Ratings are the tax documents of performance reviews — necessary, not the point.</p>

<h2>Delivering hard feedback</h2>
<ul>
  <li><strong>Specific.</strong> "In the Q2 retro, you interrupted Ann three times. I'd like you to hold off until she finishes next time." Not "you interrupt people."</li>
  <li><strong>Recent.</strong> Examples from the last 3-6 months, not 11 months ago.</li>
  <li><strong>Forward-looking.</strong> "Here's what I'd like to see next period" beats "here's what you should have done."</li>
  <li><strong>Paired with support.</strong> "Here's what you could do + here's what I'll do to help."</li>
</ul>

<h2>The compensation conversation</h2>
<ul>
  <li>Clear on how comp is determined (market, performance, company performance)</li>
  <li>Decided BEFORE the review — don't negotiate during</li>
  <li>Delivered with honest context (why this raise, why not more, what would change it)</li>
</ul>

<h2>For poor performance</h2>
<p>If someone is failing, the review isn't where you surface it. That conversation happened weeks or months ago. The review is the formal documentation.</p>
<p>Performance improvement plans (PIPs) are legitimate tools — but only if the problem was raised real-time, the PIP has specific outcomes, and you're actually willing to support the person through it.</p>

<h2>For high performers</h2>
<ul>
  <li>Recognize specific contributions</li>
  <li>Don't neglect growth areas — A-players need coaching too</li>
  <li>Invest in career conversations: where do they want to go?</li>
  <li>Pay competitively + visibly (top performers always know their market rate)</li>
</ul>

<h2>Managers get reviewed too</h2>
<p>Upward reviews (360 or direct) where reports give honest input on their manager. Critical for catching toxic managers early + for manager development.</p>

<h2>Real honest take</h2>
<p>A performance review process is a reflection of a company's communication culture. If honest feedback happens all year, the review is a summary. If it doesn't, the review is where the feedback avoidance catches up — and it's ugly. Fix the year-round culture, not just the review forms.</p>
''', prev=("One-on-ones", "one-on-ones.html"),
     nxt=("Firing well", "firing-well.html"), rt=5)


page("people/firing-well",
     "Firing well",
     "Firing is the hardest skill in management. Avoiding it costs more than doing it. Here's how to do it with integrity — for the person, the team, and the company.",
     '''
<p class="lede">Firing is the hardest skill in management — and the one managers avoid longest. Every manager I know has a story about someone they should have let go 6 months earlier. Each delay costs the company real money, the team morale, and — perversely — the person being kept around, who misses the chance to find a better fit.</p>

<h2>Why firing is worth doing well</h2>
<ul>
  <li><strong>Team performance.</strong> Tolerating low performance pulls the team down. Your A-players notice. They leave.</li>
  <li><strong>Culture.</strong> Culture is what you tolerate. Tolerating the wrong behaviors teaches them.</li>
  <li><strong>The person.</strong> Keeping someone in a role they're failing at is cruel, not kind. A clean exit is often a relief + a career unlock.</li>
  <li><strong>Legal exposure.</strong> Undocumented performance + surprise terminations = lawsuits. Documented + fair = safer.</li>
</ul>

<h2>Types of termination</h2>

<h3>1. Performance-based</h3>
<p>Someone isn't hitting their scorecard. Performance improvement plan (PIP) either turns it around or leads to separation.</p>

<h3>2. Conduct-based</h3>
<p>Someone violated policy, ethics, or safety. Often immediate termination for severe cases; progressive discipline for minor.</p>

<h3>3. Layoff / restructuring</h3>
<p>No performance issue — the role no longer exists or the business needs change. Fundamentally different from the above.</p>

<h3>4. Role mismatch / mutual</h3>
<p>Neither pure performance nor pure role change — the person was a B+ at the role but a D at the role the role became. Often resolved by moving the person to a different role or amicable exit.</p>

<h2>The progressive framework (performance cases)</h2>

<h3>Stage 1: Direct feedback</h3>
<p>Specific, timely, clear. "In your last 3 weeks, I've seen X, Y, Z. I need Q, R, S. What's getting in the way?" Give them 30-90 days to turn it around. No written plan yet.</p>

<h3>Stage 2: Formal performance improvement plan (PIP)</h3>
<p>If stage 1 doesn't produce change. Written plan:</p>
<ul>
  <li>Specific performance expectations (measurable, tied to scorecard)</li>
  <li>Timeline (typically 30-90 days)</li>
  <li>Support the manager will provide</li>
  <li>Consequences of not meeting expectations (termination)</li>
</ul>
<p>PIPs are signed by both parties. HR is looped in. Weekly check-ins during the PIP.</p>

<h3>Stage 3: Decision point</h3>
<p>At PIP end, clear outcome:</p>
<ul>
  <li>Performance has improved → close PIP, continue employment</li>
  <li>Partially improved, trajectory positive → extend PIP (rarely — usually delaying the inevitable)</li>
  <li>No improvement → termination</li>
</ul>

<h2>The termination conversation</h2>

<h3>Timing</h3>
<ul>
  <li>Day: usually Tuesday-Thursday (not Monday — ruins their week; not Friday — leaves them alone all weekend)</li>
  <li>Time: morning or early afternoon</li>
  <li>Duration: 15-20 min</li>
  <li>Private space</li>
  <li>Manager + HR (or second person if you're the HR function)</li>
</ul>

<h3>The conversation itself</h3>
<ul>
  <li>Open: "I have hard news. Your employment with [company] is ending today."</li>
  <li>Brief reasoning (not debate): "As we discussed in the PIP, [outcome] wasn't met. We've decided to end the employment."</li>
  <li>Logistics: last day, severance, benefits, return of equipment, references policy</li>
  <li>Pause for their response — listen, don't argue</li>
  <li>Don't apologize or over-explain</li>
  <li>Don't negotiate (if they push back)</li>
  <li>Wrap: "I'm sorry it didn't work out. I wish you the best."</li>
</ul>

<h3>What NOT to say</h3>
<ul>
  <li>"This is harder for me than for you." (No it isn't.)</li>
  <li>"If you'd just done X…" (Rehashing.)</li>
  <li>"Between you and me…" (Don't share private info about others.)</li>
  <li>"We had to, corporate said." (Take ownership.)</li>
  <li>"You'll thank me someday." (Maybe, but not now.)</li>
</ul>

<h2>Severance</h2>
<p>Offer severance whenever possible — not legally required in most US states, but ethically + strategically sound.</p>
<ul>
  <li>Typical: 2 weeks per year of tenure, minimum 2 weeks, often capped</li>
  <li>Plus: health coverage extension (COBRA subsidy or similar)</li>
  <li>Plus: paid time to job-search</li>
</ul>
<p>In exchange: a release of claims (signed by the employee, waiving right to sue). Standard. Have a lawyer template.</p>

<h2>Communication to the team</h2>
<p>Within 1-2 business days.</p>
<ul>
  <li>Short, respectful</li>
  <li>Don't share details ("why" stays private)</li>
  <li>Clear about how work transitions</li>
  <li>Don't disparage</li>
  <li>Acknowledge team will have reactions; make space for them</li>
</ul>

<h3>The announcement template</h3>
<blockquote style="border-left:3px solid var(--primary-purple); padding-left:20px; color:var(--gray-600); margin:16px 0;">
"I wanted to let you know that [Name] has left the company. [He/she] wasn't the right fit for the role we needed [him/her] to play, and after working through this together, we've made the decision to part ways. [His/her] last day was [date]. [Person X] will take on [responsibilities] in the interim; we'll update you on longer-term plans soon. Please direct any questions to me directly."
</blockquote>

<h2>Common mistakes</h2>
<ul>
  <li><strong>Firing without documented feedback.</strong> Legal risk + unfair to the person.</li>
  <li><strong>Firing via Slack or email.</strong> Never.</li>
  <li><strong>Walking around the company to announce before telling the person.</strong> Devastating if they hear from a peer.</li>
  <li><strong>Letting them find out via access revocation.</strong> Don't revoke until the conversation has happened.</li>
  <li><strong>Taking it back.</strong> Once it's decided, do it. Pulling back teaches everyone the process isn't real.</li>
</ul>

<h2>Firing with integrity</h2>
<p>The test: if they're telling the story of their departure in a year, is it a story they'd tell without bitterness? Were they treated fairly, with clarity + dignity?</p>
<p>Firing well doesn't mean the person leaves happy. It means they leave able to say "that was handled right."</p>

<h2>What most managers learn after firing well for the first time</h2>
<ul>
  <li>The team's productivity goes up — noticeably</li>
  <li>Other team members relax, because they see the standard is real</li>
  <li>The fired person often lands somewhere that suits them better</li>
  <li>You realize you should have done it 6 months earlier</li>
</ul>
<p>That last point is the one that every veteran manager agrees on.</p>
''', prev=("Performance reviews", "performance-reviews.html"),
     nxt=("The three numbers", "../finance/three-numbers.html"), rt=6)


print("\n✓ Operating Systems + People (11 pages)")
