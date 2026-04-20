#!/usr/bin/env python3
"""Business Management content - Leadership + Risk (7 pages)."""
from _build_bizmgmt import write_bm_page


# ============================================================
# LEADERSHIP + CULTURE (4 pages)
# ============================================================

write_bm_page(
    slug="leadership/memo-culture",
    title="Memo culture",
    description="The default mode of most companies is verbal decisions made in meetings that nobody writes down. The alternative - memo culture - forces clearer thinking, better decisions, and a durable record of why.",
    reading_time=6,
    body_html="""
<p class="lede">The default mode of most companies is verbal decisions made in meetings that nobody writes down. Six months later nobody remembers what was decided, why, or who decided it. Memo culture is the alternative: written thinking precedes important decisions, and the writing itself becomes the record. It's slower up front. It compounds.</p>

<h2>Why memos beat decks</h2>
<p>Amazon famously banned PowerPoint in leadership meetings. The reason is not aesthetic; it's epistemic:</p>
<ul>
  <li><strong>Bullets hide logic.</strong> A deck lets you assert without reasoning. A memo forces you to connect claims.</li>
  <li><strong>Narrative exposes gaps.</strong> When you can't write the sentence connecting two points, you don't actually understand them.</li>
  <li><strong>Memos scale.</strong> Anyone can read the memo asynchronously. Decks require the presenter.</li>
  <li><strong>Memos are durable.</strong> You can read it in a year and understand what was decided and why.</li>
</ul>

<h2>The standard memo structure</h2>
<ol>
  <li><strong>Context</strong> - what's the situation, why now?</li>
  <li><strong>Problem / opportunity</strong> - what are we trying to decide?</li>
  <li><strong>Options considered</strong> - at least 2, usually 3</li>
  <li><strong>Recommendation</strong> + reasoning</li>
  <li><strong>What we'd need to believe</strong> - assumptions that, if wrong, change the recommendation</li>
  <li><strong>Risks + open questions</strong></li>
  <li><strong>Appendix</strong> - data, detail, supporting analysis</li>
</ol>
<p>Length: 1-6 pages. If it's under 1 page, it's an email. If it's over 6, it's two memos.</p>

<h2>The meeting format</h2>
<p>The canonical memo-driven meeting:</p>
<ol>
  <li><strong>Memo circulated</strong> 24 hours in advance (or read silently for first 15 minutes of meeting - the Amazon model)</li>
  <li><strong>Silent read</strong> + note-taking</li>
  <li><strong>Discussion</strong> - every attendee has context, so discussion goes to substance immediately</li>
  <li><strong>Decision</strong> recorded in <a href="../operating-systems/decision-logs.html">decision log</a></li>
</ol>
<p>The first time you run this, it feels slow. By meeting three, you wonder how you ever made decisions any other way.</p>

<h2>The classes of memo</h2>

<h3>Decision memo</h3>
<p>Proposing a specific decision. Uses the structure above. Most common.</p>

<h3>Strategy memo</h3>
<p>Laying out a strategic thesis. Typically longer (5-15 pages). Context + thesis + implications + bets + risks.</p>

<h3>Post-mortem memo</h3>
<p>After an incident, launch, or killed project. What happened, what we learned, what we'll do differently.</p>

<h3>FAQ memo</h3>
<p>Anticipates questions before they're asked. Useful for product launches, pricing changes, or org changes. "Frequently asked questions" format, but written adversarially - what's the hardest thing someone could ask?</p>

<h3>6-pager / narrative memo</h3>
<p>Amazon's ritual. 6-page maximum. No bullets. Full sentences and paragraphs. Surprisingly hard to write, which is the point.</p>

<h2>Writing well enough for a memo</h2>
<ul>
  <li><strong>Lead with the conclusion.</strong> If the reader only gets through paragraph 1, they should know what you're recommending.</li>
  <li><strong>Specific &gt; abstract.</strong> "Increase pricing for enterprise tier from $50K to $75K" not "consider pricing adjustments."</li>
  <li><strong>One idea per paragraph.</strong> If a paragraph contains three ideas, it's three paragraphs.</li>
  <li><strong>Show your work.</strong> If your recommendation is backed by a calculation, include it.</li>
  <li><strong>Steelman the alternatives.</strong> Every option you considered gets its strongest case made, not a strawman.</li>
</ul>

<h2>What memo culture changes</h2>
<ul>
  <li>Decisions get better because the decider sees the reasoning, not just the ask</li>
  <li>Remote/async work becomes feasible because decisions don't require everyone in a room</li>
  <li>Onboarding gets cheaper because a new hire can read the last 20 memos and know what was decided and why</li>
  <li>Reversing decisions gets honest - you can read the original assumptions and see whether they held</li>
</ul>

<h2>What memo culture costs</h2>
<ul>
  <li>Time to write. A good memo takes 4-8 hours.</li>
  <li>Resistance from people who "think better verbally" (usually they think less clearly but faster)</li>
  <li>Discipline to enforce - if half the team writes memos and half doesn't, you don't have memo culture</li>
</ul>

<h2>What good looks like</h2>
<ul>
  <li>Every meeting with &gt; 3 attendees + a decision has a pre-read</li>
  <li>Memos are archived somewhere searchable (Notion, Google Drive, dedicated memo system)</li>
  <li>Senior leaders write their own memos - don't delegate the thinking</li>
  <li>Reading memos is a protected activity (calendar blocks, not "catch up in between meetings")</li>
</ul>

<p style="margin-top:40px;">Related: <a href="../operating-systems/decision-logs.html">Decision logs</a> · <a href="../strategy/decision-frameworks.html">Decision frameworks</a> · <a href="../operating-systems/meetings.html">Meetings that don't waste time</a></p>
""",
    prev=("SLAs + SLOs", "../execution/slas-and-slos.html"),
    nxt=("Radical candor", "radical-candor.html"),
)


write_bm_page(
    slug="leadership/radical-candor",
    title="Radical candor",
    description="The reason most teams tolerate mediocrity is that feedback is expensive to give. Radical candor is the discipline of caring enough about someone to tell them the truth.",
    reading_time=6,
    body_html="""
<p class="lede">The reason most teams tolerate mediocrity is that feedback is expensive to give. It's socially uncomfortable. It risks the relationship. And the alternative - saying nothing - is painless in the short term. Radical candor, coined by Kim Scott, is the discipline of being willing to pay the short-term cost because the long-term cost of not is much higher.</p>

<h2>The two axes</h2>
<ul>
  <li><strong>Care personally</strong> - do you genuinely care about this person's success, growth, and well-being?</li>
  <li><strong>Challenge directly</strong> - are you willing to tell them hard truths they don't want to hear?</li>
</ul>
<p>The 2x2:</p>
<pre style="background:#f5f5f7; padding:16px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:12px;">
                  CHALLENGE DIRECTLY (high)
                  ┌───────────────────────┬────────────────────┐
                  │   Obnoxious           │   Radical          │
                  │   Aggression          │   Candor           │
                  ├───────────────────────┼────────────────────┤
                  │   Manipulative        │   Ruinous          │
                  │   Insincerity         │   Empathy          │
                  └───────────────────────┴────────────────────┘
                   CARE (low)              CARE (high)
</pre>

<h2>The four quadrants, named</h2>

<h3>Ruinous Empathy</h3>
<p>You care about the person but won't tell them the truth. Most common quadrant. Looks kind. Actually cruel - the person never gets to fix the problem, and eventually gets fired for something they didn't know was a problem.</p>

<h3>Manipulative Insincerity</h3>
<p>Low care, low candor. Says what will land well. Politician mode. The worst quadrant because nothing you say can be trusted.</p>

<h3>Obnoxious Aggression</h3>
<p>High challenge, low care. The "truth-teller" who's just a bully. Delivers hard feedback without any evidence they care about the person. Destructive.</p>

<h3>Radical Candor</h3>
<p>High care, high challenge. You genuinely care about this person AND you tell them the truth. The goal.</p>

<h2>What radical candor looks like in practice</h2>

<h3>Specific, not general</h3>
<ul>
  <li>Not: "Your communication is a problem."</li>
  <li>Yes: "In Tuesday's stakeholder meeting, when Alex asked about the timeline, you cut him off and talked over him for 3 minutes. It shut down the conversation and Alex hasn't contributed since."</li>
</ul>

<h3>Behavior, not identity</h3>
<ul>
  <li>Not: "You're disorganized."</li>
  <li>Yes: "The last three project updates have been sent after the deadline. That creates a downstream problem for product marketing."</li>
</ul>

<h3>Impact, not intent</h3>
<ul>
  <li>Not: "You shouldn't feel that way."</li>
  <li>Yes: "I hear you didn't mean it that way, but here's how it landed on the team."</li>
</ul>

<h3>Private for critical; public for praise</h3>
<ul>
  <li>Criticism in private, always. Even small public corrections damage trust.</li>
  <li>Praise in public (or at least openly). Private praise feels like begrudging acknowledgment.</li>
</ul>

<h2>The solicit-give-receive flow</h2>
<ol>
  <li><strong>Solicit first.</strong> Ask for feedback on yourself before giving feedback to others. "What could I do better?" - then genuinely consider the answer. Builds the credibility to give feedback back.</li>
  <li><strong>Give.</strong> Specific, behavioral, caring, timely.</li>
  <li><strong>Receive.</strong> When feedback comes back, thank the person, don't defend. Model what you expect.</li>
</ol>

<h2>The timing rule</h2>
<p>Feedback must be timely. Within 24 hours for small things, within the week for bigger. The longer you wait, the harder it becomes to give, and the less actionable it is to receive. If you find yourself saving feedback for a quarterly review, you've waited too long.</p>

<h2>Why this is hard</h2>
<ul>
  <li><strong>Social tax.</strong> Telling someone something they don't want to hear costs you, and your brain treats it like a threat.</li>
  <li><strong>Asymmetric feedback.</strong> You remember giving feedback that landed badly; you don't remember the feedback you withheld that should've been given.</li>
  <li><strong>Imposter syndrome.</strong> "Who am I to give this feedback?" The answer: their manager, peer, or colleague who cares about their success.</li>
</ul>

<h2>What good looks like</h2>
<ul>
  <li>Feedback happens within days of the behavior, not months</li>
  <li>Leaders solicit feedback on themselves more often than they give it</li>
  <li>When someone on the team is underperforming, they know it; it's not a surprise at review time</li>
  <li>People grow visibly quarter-over-quarter because they're being told what to fix</li>
</ul>

<p style="margin-top:40px;">Related: <a href="accountability.html">Accountability without micromanagement</a> · <a href="../people/one-on-ones.html">One-on-ones</a> · <a href="../people/performance-reviews.html">Performance reviews</a></p>
""",
    prev=("Memo culture", "memo-culture.html"),
    nxt=("Accountability without micromanagement", "accountability.html"),
)


write_bm_page(
    slug="leadership/accountability",
    title="Accountability without micromanagement",
    description="Most managers oscillate between over-involvement and abandonment. Good accountability is neither - it's a structured agreement about what, when, and how, with the manager stepping in only when the system signals trouble.",
    reading_time=6,
    body_html="""
<p class="lede">Most managers oscillate between two failure modes: over-involvement (checking constantly, approving everything, re-doing work) and abandonment (delegating and disappearing, surprised when things go wrong). Good accountability is neither. It's a structured agreement about what, when, and how - with the manager stepping in only when the system signals trouble.</p>

<h2>The accountability equation</h2>
<p>For any piece of work, four things must be clear:</p>
<ol>
  <li><strong>What outcome</strong> is expected (not what activity)</li>
  <li><strong>By when</strong> (with milestones, not just a final date)</li>
  <li><strong>How progress will be visible</strong> (what gets reported, how often)</li>
  <li><strong>What triggers escalation</strong> (what would cause the manager to intervene)</li>
</ol>
<p>Get those right, and the delegated work runs itself. The manager is on call, not on the ball.</p>

<h2>Outcomes, not activities</h2>
<p>"Manage the launch" is an activity. "Launch with &lt; 10 P1 bugs, &gt; 80% feature adoption within 30 days, no compliance issues" is an outcome. The manager specifies outcomes. The operator picks the activities.</p>
<p>When you find yourself specifying activities, it's a sign you don't trust the operator or you haven't thought carefully about what you actually want.</p>

<h2>Milestones, not final dates</h2>
<p>"Deliver Q2 plan by June 30" is useless. By June 29 you'll find out it didn't happen. Break it:</p>
<ul>
  <li>Week 1 - draft v1 with 3 candidate approaches</li>
  <li>Week 2 - stakeholder review + feedback</li>
  <li>Week 4 - v2 with recommended approach</li>
  <li>Week 6 - board review version</li>
</ul>
<p>Each milestone is a decision point. If milestone 2 is off-track, you know 5 weeks earlier than you otherwise would.</p>

<h2>Visibility, not surveillance</h2>
<p>The difference between accountability and micromanagement is the <em>frequency</em> and <em>format</em> of visibility:</p>
<ul>
  <li><strong>Healthy visibility</strong>: weekly written update (what got done, what's next, what's blocked)</li>
  <li><strong>Healthy visibility</strong>: shared dashboard with the outcome metric</li>
  <li><strong>Healthy visibility</strong>: pre-scheduled 30-minute check-in</li>
  <li><strong>Unhealthy surveillance</strong>: ad-hoc Slack DMs asking "how's it going?"</li>
  <li><strong>Unhealthy surveillance</strong>: watching every commit/ticket in real time</li>
  <li><strong>Unhealthy surveillance</strong>: requiring approval for every sub-decision</li>
</ul>

<h2>The escalation trigger</h2>
<p>The single most important tool: pre-agreed conditions under which the operator must escalate. Without this, either they escalate too much (micromanagement) or not enough (surprise failures).</p>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Example triggers (for a product launch):</strong><br>
- Any P1 bug found in QA<br>
- Any slip in launch date of more than 1 week<br>
- Any customer-facing issue during beta<br>
- Any budget overrun &gt; 10%<br>
- Any scope change from the original spec<br><br>
Anything else - handle it.
</blockquote>

<h2>The manager's job, with this in place</h2>
<ol>
  <li>Help set the outcome and milestones clearly at kickoff</li>
  <li>Review the weekly update; intervene only if a milestone is at risk</li>
  <li>Respond fast when an escalation comes - operator needs a yes/no quickly</li>
  <li>Remove blockers the operator can't remove themselves</li>
  <li>Evaluate performance against the outcome, not the activity</li>
</ol>

<h2>When to intervene</h2>
<p>Even with the structure, managers still need judgment on when to step in:</p>
<ul>
  <li><strong>Step in</strong>: repeated missed milestones, a critical stakeholder in distress, a decision about to be made that has irreversible consequences</li>
  <li><strong>Stay out</strong>: the operator's approach differs from yours but is still on track, small mistakes the operator can learn from, decisions that can be reversed</li>
</ul>
<p>The cost of intervening too early is real - you teach the operator that you don't trust them, and that any setback brings you in. They stop trying to solve hard things.</p>

<h2>What good looks like</h2>
<ul>
  <li>Every major piece of delegated work has a written outcome, milestones, and escalation triggers</li>
  <li>Weekly updates are brief, structured, and consistent</li>
  <li>Managers know about serious problems before they blow up, because of pre-agreed triggers</li>
  <li>Operators feel trusted to execute without constant check-ins</li>
  <li>Performance conversations focus on outcomes achieved, not activities undertaken</li>
</ul>

<p style="margin-top:40px;">Related: <a href="../people/one-on-ones.html">One-on-ones</a> · <a href="../people/performance-reviews.html">Performance reviews</a> · <a href="radical-candor.html">Radical candor</a></p>
""",
    prev=("Radical candor", "radical-candor.html"),
    nxt=("Compensation design", "compensation.html"),
)


write_bm_page(
    slug="leadership/compensation",
    title="Compensation design",
    description="Compensation is the most visible expression of a company's priorities. Done well, it aligns incentives and attracts the right people. Done casually, it generates resentment, turnover, and the wrong behaviors.",
    reading_time=7,
    body_html="""
<p class="lede">Compensation is the most visible expression of a company's priorities. Done well, it aligns incentives, attracts the right people, and makes retention cheap. Done casually, it generates resentment, turnover, and the wrong behaviors. Almost every early company I've seen starts with ad-hoc compensation decisions and spends years cleaning up the inequities those decisions created.</p>

<h2>The components</h2>
<ul>
  <li><strong>Base salary</strong> - predictable, non-negotiable-after-sign cash</li>
  <li><strong>Variable / bonus</strong> - performance-tied cash</li>
  <li><strong>Equity</strong> - stock options, RSUs, or profit sharing</li>
  <li><strong>Benefits</strong> - health, retirement match, PTO, other non-cash value</li>
  <li><strong>Non-monetary</strong> - remote flexibility, title, ownership, growth path</li>
</ul>
<p>Total compensation = all of the above. Candidates evaluate the full package. Compete on total comp, not on base.</p>

<h2>Building a compensation structure</h2>

<h3>1. Define levels</h3>
<p>Before any individual compensation decision, define the leveling system. For each function:</p>
<ul>
  <li>Individual contributor track: L3 (early career) → L4 (mid) → L5 (senior) → L6 (staff) → L7 (principal)</li>
  <li>Manager track: M3 (manager) → M4 (senior manager) → M5 (director) → M6 (VP)</li>
  <li>Each level has a written description of expectations - scope, autonomy, impact</li>
</ul>

<h3>2. Set bands by level</h3>
<p>For each level, a salary band: min, mid, max. Typical spread: mid ±15%. Every role in that level must fall within the band. No exceptions.</p>

<h3>3. Benchmark to market</h3>
<p>Use at least two data sources:</p>
<ul>
  <li>Third-party benchmarks (Pave, Radford, Mercer, Option Impact for equity)</li>
  <li>Your actual offer acceptance / decline data</li>
</ul>
<p>Target a market position: typically 50th-75th percentile of your comp market. Above 75th is expensive; below 50th means you lose candidates.</p>

<h3>4. Document the philosophy</h3>
<p>Write a one-page compensation philosophy. Answers: what percentile do we target? How do we weight cash vs equity? How much variable comp do we use? How do we handle raises? Publish it internally.</p>

<h2>Variable comp - the dangerous lever</h2>
<p>Variable compensation motivates whatever you measure. Pick wrong and people optimize for the wrong thing. Rules:</p>
<ul>
  <li><strong>Sales roles</strong> - variable comp should be meaningful (40-60% of OTE) and tied to closed revenue, not activities</li>
  <li><strong>Customer success</strong> - lean variable (10-20%) tied to retention + expansion</li>
  <li><strong>Engineers / PMs / designers</strong> - usually not variable, or minimal (5-10% company bonus). Variable comp in product teams tends to drive the wrong incentives</li>
  <li><strong>Executives</strong> - typically 20-40% tied to company-level outcomes (revenue, profitability)</li>
</ul>
<p>Whatever the comp plan rewards is what you'll get. If you reward bookings, you'll get bookings, even if they're bad deals.</p>

<h2>Equity - the long tail</h2>
<ul>
  <li><strong>Early stage</strong> - equity is usually the largest component of long-term value. Be generous with early hires; small equity differences compound massively</li>
  <li><strong>Refresh grants</strong> - after 2-3 years, initial grants are vesting out. Refresh grants keep people engaged. Budget for this</li>
  <li><strong>Vesting cliff</strong> - 1-year cliff is industry standard. Accelerate for terminations without cause, not for voluntary departures</li>
  <li><strong>Secondary opportunities</strong> - at later stages, allowing modest secondary sales reduces pressure to leave for liquidity</li>
</ul>

<h2>Raise cadence</h2>
<p>Raises happen on a schedule, not on who asks loudest:</p>
<ul>
  <li><strong>Annual</strong> - cost-of-living adjustments for all, tied to market data</li>
  <li><strong>Merit</strong> - performance-tied increases, concentrated in top performers (top 20% get 50% of the merit pool)</li>
  <li><strong>Promotion</strong> - when someone levels up, a compensation increase follows immediately, not at the next review</li>
  <li><strong>Out-of-cycle</strong> - when someone's comp has fallen significantly out of market (e.g., market moved, they've been underleveled) - fix it, don't wait</li>
</ul>

<h2>The transparency question</h2>
<p>How transparent should compensation be?</p>
<ul>
  <li><strong>Fully transparent</strong> - publish individual comp to the whole company (rare; requires extraordinary culture)</li>
  <li><strong>Structurally transparent</strong> - publish bands, levels, philosophy; individual comp is private (most common good answer)</li>
  <li><strong>Opaque</strong> - nothing published (causes resentment; employees compare notes anyway)</li>
</ul>
<p>Structurally transparent is the right answer for most companies. People need to know the system is fair; they don't need to know what their neighbor makes.</p>

<h2>The pay equity audit</h2>
<p>Annually, analyze comp by gender, race, tenure, and level. Questions:</p>
<ul>
  <li>Within a level, is there unexplained variance by demographic?</li>
  <li>Are people who joined more recently paid more than tenured people at the same level? (The "tenure tax")</li>
  <li>Are people who negotiated hard paid more than people who didn't, at the same level?</li>
</ul>
<p>Unexplained inequities get fixed. Not "noted for next cycle" - fixed.</p>

<h2>What good looks like</h2>
<ul>
  <li>Written compensation philosophy, levels, and bands</li>
  <li>Every offer maps to a level + band; no "special case" compensation</li>
  <li>Annual pay equity audit with specific actions taken on any findings</li>
  <li>Variable comp is tight: rewards the right outcomes, not activity proxies</li>
  <li>Retention offers never exceed what a proactive raise would've cost</li>
</ul>

<p style="margin-top:40px;">Related: <a href="../people/role-scorecard.html">Role scorecard</a> · <a href="../people/performance-reviews.html">Performance reviews</a> · <a href="../people/hiring-signal-vs-noise.html">Hiring</a></p>
""",
    prev=("Accountability without micromanagement", "accountability.html"),
    nxt=("Risk management basics", "../risk/risk-management.html"),
)


# ============================================================
# RISK + COMPLIANCE (3 pages)
# ============================================================

write_bm_page(
    slug="risk/risk-management",
    title="Risk management basics",
    description="Risk management is the practice of identifying what could break the business and deciding - explicitly - how much of each risk you're willing to carry. Most companies do it implicitly, and badly.",
    reading_time=7,
    body_html="""
<p class="lede">Risk management is the practice of identifying what could break the business and deciding - explicitly - how much of each risk you're willing to carry. Most companies do it implicitly, and badly. They discover a risk only when it materializes. Good operators keep a living risk register and revisit it every quarter.</p>

<h2>The risk register</h2>
<p>A simple table, maintained by whoever owns risk (COO, CFO, Head of Ops - someone senior, not a committee):</p>
<pre style="background:#f5f5f7; padding:16px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:12px; overflow-x:auto;">
Risk              | Likelihood | Impact | Score | Owner | Mitigation            | Status
------------------|------------|--------|-------|-------|-----------------------|--------
Top customer      |   Medium   | Critical| 12   |  CEO  | Diversify 2024 plan   | Active
churn             |            |        |       |       |                       |
Key engineer      |   Low      | High   |  6    |  CTO  | Knowledge transfer    | Active
departs           |            |        |       |       |                       |
Data breach       |   Low      | Critical|  9   |  CTO  | SOC 2, pen test       | Active
Regulatory change |   Medium   | Medium |  6    |  COO  | Monitor, counsel      | Active
</pre>
<p>Likelihood (1-4), Impact (1-4), Score = product. Scores &gt; 8 demand quarterly review. Scores &gt; 12 demand monthly.</p>

<h2>Categories to scan</h2>

<h3>Financial</h3>
<ul>
  <li>Runway / cash flow</li>
  <li>Customer concentration (single customer &gt; 15% of revenue)</li>
  <li>Currency exposure (international revenue)</li>
  <li>Bad debt / collection risk</li>
  <li>Cost inflation (key inputs, labor)</li>
</ul>

<h3>Operational</h3>
<ul>
  <li>Key person dependency (bus factor)</li>
  <li>Vendor dependency (single-source strategic vendors)</li>
  <li>Infrastructure / systems failure</li>
  <li>Supply chain disruption</li>
  <li>Data loss / backup failure</li>
</ul>

<h3>Security + Compliance</h3>
<ul>
  <li>Data breach / cybersecurity</li>
  <li>Regulatory violation (GDPR, SOC 2, HIPAA, etc.)</li>
  <li>IP theft / leakage</li>
  <li>Insider threat</li>
  <li>Third-party risk (vendor compromise)</li>
</ul>

<h3>Market + Strategic</h3>
<ul>
  <li>Competitor move (new entrant, major pivot)</li>
  <li>Platform risk (reliance on AWS / Apple / Google / LinkedIn)</li>
  <li>Market shift (buyer priorities change)</li>
  <li>Technology disruption</li>
</ul>

<h3>People</h3>
<ul>
  <li>Executive turnover</li>
  <li>Harassment / culture incidents</li>
  <li>Union / labor action</li>
  <li>Hiring capacity / ramp risk</li>
</ul>

<h3>External</h3>
<ul>
  <li>Macroeconomic downturn</li>
  <li>Geopolitical events</li>
  <li>Natural disasters / pandemic</li>
  <li>Legal action (lawsuit exposure)</li>
</ul>

<h2>The four responses to risk</h2>
<p>For each risk, pick one:</p>
<ol>
  <li><strong>Accept</strong> - the risk is low enough or the mitigation too expensive. Document the acceptance.</li>
  <li><strong>Avoid</strong> - don't do the thing that creates the risk. Exit the line of business, drop the vendor.</li>
  <li><strong>Mitigate</strong> - reduce the likelihood or impact. Invest in controls, backup plans, insurance.</li>
  <li><strong>Transfer</strong> - shift the risk to someone else. Insurance, contracts with indemnification, escrow.</li>
</ol>
<p>The act of classifying forces explicitness. "We chose to accept this risk" is a very different artifact than "we never talked about it."</p>

<h2>Early warning indicators</h2>
<p>For the top risks, define leading indicators:</p>
<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Risk:</strong> Top customer churn<br>
<strong>Leading indicators:</strong><br>
- Quarterly usage declining 3 months running<br>
- Executive sponsor departure<br>
- NPS drop &gt; 20 points<br>
- Support ticket escalation rate 2x baseline<br>
- No executive meeting for 90 days<br><br>
Any two simultaneously → escalate to CEO for intervention.
</blockquote>

<h2>Scenario planning</h2>
<p>Annually, run three scenarios:</p>
<ul>
  <li><strong>Base case</strong> - expected plan</li>
  <li><strong>Downside</strong> - revenue down 20%, top customer gone, key hire slipped 6 months</li>
  <li><strong>Black swan</strong> - business-defining event (lawsuit, recession, market collapse)</li>
</ul>
<p>For each scenario: what actions do we take? At what trigger? By whom? Writing this down now beats improvising when the scenario hits.</p>

<h2>The risk committee</h2>
<p>Quarterly, the top 3-5 leaders review the risk register. 90 minutes. Format:</p>
<ol>
  <li>New risks added this quarter</li>
  <li>Risks whose score changed</li>
  <li>Top 5 active risks - status of mitigation</li>
  <li>Any incidents since last review + what they teach</li>
</ol>
<p>The quarterly ritual is what makes risk management a discipline instead of a one-time exercise.</p>

<h2>What good looks like</h2>
<ul>
  <li>A living risk register exists and is reviewed quarterly</li>
  <li>Top 5 risks have named owners and mitigation plans</li>
  <li>Early warning indicators trigger specific actions</li>
  <li>After any incident, the register gets updated with what was missed</li>
  <li>Scenario planning happens annually and informs budget + plan</li>
</ul>

<p style="margin-top:40px;">Related: <a href="data-and-ip.html">Data + IP protection</a> · <a href="insurance.html">Business insurance</a> · <a href="../strategy/pre-mortems.html">Pre-mortems</a></p>
""",
    prev=("Compensation design", "../leadership/compensation.html"),
    nxt=("Data + IP protection", "data-and-ip.html"),
)


write_bm_page(
    slug="risk/data-and-ip",
    title="Data + IP protection",
    description="Your data and IP are probably your most valuable assets and your most poorly protected ones. A few hours of deliberate work at the right moments prevents years of pain later.",
    reading_time=7,
    body_html="""
<p class="lede">Your data and IP are probably your most valuable assets and - in most small companies - your most poorly protected ones. A few hours of deliberate work at the right moments prevents years of pain later. The things to get right aren't complicated. They're just easy to defer until after something bad happens.</p>

<h2>IP - what you actually own</h2>
<p>In a normal company, your IP includes:</p>
<ul>
  <li>Source code</li>
  <li>Product designs, specs, research</li>
  <li>Customer lists, sales playbooks, pricing data</li>
  <li>Trademarks, brand</li>
  <li>Trade secrets (internal processes, proprietary methods)</li>
  <li>Data you've collected</li>
</ul>
<p>Whether you actually own all of it depends on whether the paper trail says so.</p>

<h2>The foundational IP documents</h2>

<h3>1. IP assignment agreements</h3>
<p>Every employee and contractor must sign an agreement assigning IP they create to the company. Without this, an employee technically owns what they built, and they can take it with them.</p>

<h3>2. Contractor agreements (not handshakes)</h3>
<p>Contractors are the highest-risk category. Freelancer wrote a feature? Without signed IP assignment, you might not own it. Sign agreements <strong>before</strong> work starts, not after.</p>

<h3>3. Founder IP assignment</h3>
<p>The IP assignment founders sign at company formation. Critical for fundraising and acquisition.</p>

<h3>4. NDAs</h3>
<p>Standard mutual NDA for customer/partner conversations. Asymmetric NDAs where appropriate. Don't be shy about asking - anyone who refuses to sign a standard NDA is telling you something.</p>

<h3>5. Non-compete / non-solicit</h3>
<p>Varies wildly by state + country (California invalid; other states enforce). Know what's enforceable and structure accordingly.</p>

<h2>Trademark basics</h2>
<ul>
  <li>Search USPTO (or relevant registry) before committing to a name</li>
  <li>Register your name + logo in your primary markets</li>
  <li>Register in product categories you actually operate in + adjacent ones you plan to</li>
  <li>Monitor for infringement; the law protects what you actively defend</li>
</ul>

<h2>Data protection - the separate problem</h2>
<p>IP is "what you create." Data is "what you collect." Both need protection but with different frameworks.</p>

<h3>Classify your data</h3>
<p>Not all data is equally sensitive:</p>
<ul>
  <li><strong>Public</strong> - marketing site, published content</li>
  <li><strong>Internal</strong> - company data not public but not sensitive if leaked</li>
  <li><strong>Confidential</strong> - business-sensitive (financial, strategy, salaries)</li>
  <li><strong>Restricted</strong> - customer PII, security keys, payment data</li>
</ul>
<p>Each tier gets progressively tighter access controls.</p>

<h3>Access controls</h3>
<ul>
  <li><strong>Least privilege</strong> - default to no access; grant access per role</li>
  <li><strong>SSO everywhere</strong> - single sign-on with MFA enforced</li>
  <li><strong>Offboarding checklist</strong> - within 1 business day of termination, all access revoked</li>
  <li><strong>Quarterly access review</strong> - each system's admin reviews who has access</li>
</ul>

<h3>Encryption</h3>
<ul>
  <li>At rest - databases, file storage, backups</li>
  <li>In transit - TLS everywhere, never plaintext</li>
  <li>Key management - not stored in the same place as the data</li>
</ul>

<h3>Backups</h3>
<p>3-2-1 rule: 3 copies, 2 different media types, 1 offsite. Test restores quarterly - a backup you can't restore from isn't a backup.</p>

<h2>Compliance frameworks</h2>
<p>If you sell to enterprises or handle regulated data:</p>
<ul>
  <li><strong>SOC 2 Type II</strong> - standard for B2B SaaS selling mid-market+</li>
  <li><strong>ISO 27001</strong> - international alternative</li>
  <li><strong>HIPAA</strong> - if you touch healthcare PHI</li>
  <li><strong>PCI DSS</strong> - if you handle card data</li>
  <li><strong>GDPR</strong> - if you have EU customers/users</li>
  <li><strong>CCPA / CPRA</strong> - California consumer data</li>
</ul>
<p>Start the compliance work 6 months before you need the certification. The readiness work itself surfaces risks.</p>

<h2>Incident response plan</h2>
<p>Before you have an incident, write the plan:</p>
<ul>
  <li>Who declares an incident? (SRE on-call, CISO)</li>
  <li>Who's on the incident team? (exec sponsor, technical lead, communications)</li>
  <li>What's the communication tree? (internal Slack channel, customer email template, regulator notification)</li>
  <li>What's the legal / PR playbook?</li>
  <li>Who notifies customers, and when?</li>
</ul>
<p>Then run a tabletop exercise - simulate an incident and walk through the plan. The first time you execute it should not be in production.</p>

<h2>Regulatory notification windows</h2>
<p>GDPR: 72 hours to notify authorities after discovery. CCPA: "without unreasonable delay." State breach laws vary. Know the clocks before you need them.</p>

<h2>What good looks like</h2>
<ul>
  <li>Every employee and contractor has signed IP assignment</li>
  <li>Data is classified, access is role-based, SSO+MFA everywhere</li>
  <li>Backups tested quarterly with documented restore</li>
  <li>Written incident response plan, practiced at least annually</li>
  <li>Compliance certifications appropriate for stage + customer base</li>
</ul>

<p style="margin-top:40px;">Related: <a href="risk-management.html">Risk management basics</a> · <a href="insurance.html">Business insurance</a> · <a href="../execution/vendor-management.html">Vendor management</a></p>
""",
    prev=("Risk management basics", "risk-management.html"),
    nxt=("Business insurance", "insurance.html"),
)


write_bm_page(
    slug="risk/insurance",
    title="Business insurance",
    description="Insurance is the part of the business most operators ignore until they're in a situation where they wish they hadn't. A few standard policies prevent nearly all catastrophic outcomes.",
    reading_time=6,
    body_html="""
<p class="lede">Insurance is the part of the business most operators ignore until they're in a situation where they wish they hadn't. Insurance isn't about expecting to collect - it's about ensuring that one bad event doesn't end the company. A few standard policies prevent nearly all catastrophic outcomes. Get them in place early; adjust limits as the company grows.</p>

<h2>The essential policies</h2>

<h3>General Liability (GL)</h3>
<p>Covers bodily injury and property damage claims. Customer slips in your office. Visitor gets injured. Someone sues claiming your booth at a conference damaged their equipment. Usually $1M per occurrence / $2M aggregate is the starting point.</p>

<h3>Professional Liability / E&amp;O (Errors &amp; Omissions)</h3>
<p>Critical for anyone who provides a service, software, or advice. Covers claims that your product or service failed to perform, caused financial loss, or had errors. A customer claims your software caused them to lose money - E&amp;O covers the defense and potential settlement. $1M-$5M depending on customer profile.</p>

<h3>Cyber / Data Breach</h3>
<p>Covers costs of a data breach: forensics, customer notification, credit monitoring, regulatory fines, business interruption, ransomware recovery. If you store any customer data, this is non-optional. $1M-$10M+ depending on data volume and sensitivity. Be very careful about exclusions - many policies exclude social engineering or nation-state attacks.</p>

<h3>Directors &amp; Officers (D&amp;O)</h3>
<p>Protects directors and officers personally from claims by shareholders, employees, or regulators. Required before raising institutional capital. Becomes more important as the board grows. Without D&amp;O, you cannot recruit experienced board members.</p>

<h3>Employment Practices Liability (EPLI)</h3>
<p>Covers employment-related claims: wrongful termination, discrimination, harassment, wage/hour disputes. Claims frequency is higher than most operators expect - across a company's life, statistically one of these claims is almost guaranteed. Critical once you're over ~25 employees.</p>

<h3>Workers' Comp</h3>
<p>Mandatory in most states. Covers injuries that happen during work. Usually cheap; administrated through payroll.</p>

<h3>Employee Benefits (Health, Dental, 401k Fiduciary)</h3>
<p>If you offer benefits, the administrator role creates fiduciary exposure. Fiduciary liability insurance protects against claims of mismanagement.</p>

<h3>Business Interruption</h3>
<p>Covers lost revenue if operations are interrupted by a covered event (fire, natural disaster). Included in most property policies.</p>

<h3>Property Insurance</h3>
<p>If you own real estate or have material office equipment. Becomes less relevant in remote-first companies.</p>

<h3>Key Person</h3>
<p>Covers the company if a critical founder or executive dies or becomes disabled. Usually purchased when the company has institutional investors who demand it.</p>

<h2>What drives premium</h2>
<ul>
  <li><strong>Industry</strong> - high-risk industries (construction, healthcare, crypto) pay more</li>
  <li><strong>Revenue size</strong> - larger = higher premium (more exposure)</li>
  <li><strong>Claim history</strong> - past claims raise premiums</li>
  <li><strong>Controls</strong> - security posture for cyber; HR practices for EPLI</li>
  <li><strong>Deductible</strong> - higher deductible, lower premium</li>
  <li><strong>Limits</strong> - higher coverage, higher premium</li>
</ul>

<h2>Reading a policy - what to check</h2>
<ol>
  <li><strong>Named insured</strong> - is the legal entity name correct? Subsidiaries included?</li>
  <li><strong>Limits</strong> - per-occurrence and aggregate. Is the aggregate enough for multiple claims in a year?</li>
  <li><strong>Deductible / retention</strong> - what you pay before coverage kicks in</li>
  <li><strong>Territory</strong> - coverage worldwide or US-only?</li>
  <li><strong>Exclusions</strong> - read these. Often buried. Common exclusions: war, nuclear, intentional acts, pollution, prior acts</li>
  <li><strong>Claims-made vs. occurrence</strong> - claims-made policies only cover claims filed while the policy is active; need tail coverage when you switch insurers</li>
  <li><strong>Notification requirements</strong> - how fast must you notify of a potential claim? Missing the window voids coverage</li>
</ol>

<h2>Working with a broker</h2>
<p>Don't buy insurance direct from carriers. A good commercial insurance broker:</p>
<ul>
  <li>Shops multiple carriers for each policy</li>
  <li>Negotiates terms beyond just price (exclusions, endorsements)</li>
  <li>Advocates for you if a claim happens</li>
  <li>Reviews your coverage annually as the business changes</li>
</ul>
<p>Interview 2-3 brokers. Pick one who specializes in your industry + stage. Broker commissions are paid by carriers; you don't pay the broker directly.</p>

<h2>Claims process</h2>
<p>If something happens:</p>
<ol>
  <li>Document immediately (photos, logs, witnesses)</li>
  <li>Notify the broker within 24-48 hours</li>
  <li>Don't admit fault or settle anything without the broker's knowledge</li>
  <li>Preserve evidence - for cyber claims, don't wipe/rebuild systems until forensics team examines</li>
</ol>

<h2>Annual review</h2>
<p>Insurance needs change as the business changes. Every year, review:</p>
<ul>
  <li>Have revenue or headcount grown enough to raise limits?</li>
  <li>Any new lines of business creating new exposure?</li>
  <li>Any new countries or regulatory jurisdictions?</li>
  <li>Are customer contracts requiring higher limits than your current policies?</li>
  <li>Claims trends in the industry suggesting new policies needed?</li>
</ul>

<h2>What good looks like</h2>
<ul>
  <li>Core stack in place: GL, E&amp;O, Cyber, D&amp;O, EPLI, Workers' Comp</li>
  <li>Limits scaled to revenue and customer contract requirements</li>
  <li>Broker relationship with annual review</li>
  <li>Claims process documented so the first call happens within 24 hours</li>
  <li>Certificates of insurance can be issued to customers on same-day request</li>
</ul>

<p style="margin-top:40px;">Related: <a href="risk-management.html">Risk management basics</a> · <a href="data-and-ip.html">Data + IP protection</a> · <a href="../finance/cash-flow.html">Cash flow forecasting</a></p>
""",
    prev=("Data + IP protection", "data-and-ip.html"),
    nxt=None,
)

print("\n✓ Leadership + Risk (7 pages) - Business Management complete")
