#!/usr/bin/env python3
"""20 essays to cap the site at 1000+ pages."""
from _build_writing import build_writing


def E(slug, title, subtitle, topic, date, body):
    return {'slug': slug, 'title': title, 'subtitle': subtitle, 'topic': topic, 'date': date, 'body': body}


ESSAYS = [
    E("why-i-write-everything", "Why I write everything down",
      "The people I know who do the most also write the most. The connection is not what I thought it was.",
      "Productivity", "2026-04-02",
      """<p>There's a correlation I can't stop noticing. The people I know who build the most, ship the most, think the clearest, and stay calmest under pressure are, without exception, the people who write things down constantly. Not just important things. Every thing.</p>

<p>For a long time I assumed the writing was a byproduct of their thinking. Smart people who happen to write. The causality felt one-directional.</p>

<p>I was wrong.</p>

<h2>The causal arrow runs the other way</h2>

<p>Writing isn't evidence of thinking. Writing <em>is</em> thinking. The act of getting an idea onto the page is what clarifies it. Until you've written something, you don't actually know what you believe about it. You have impressions, gut reactions, vibes. You don't have a position.</p>

<p>The first time I tried to write down a decision I'd already "made," I discovered I hadn't actually made it. I'd just been circling it. The moment I forced myself to commit words to the page, three unresolved tensions became visible. Tensions I would have happily ignored for another week if I'd never tried to write them down.</p>

<h2>The second-order effect</h2>

<p>Writing also changes what you remember. Not just what you captured - what you carry. I used to think of my best ideas as reliably accessible. I could almost always produce them on demand. But I've now watched enough of my own unwritten ideas decay to know they aren't.</p>

<p>An idea you can access today, you probably can't access in six months. Unless you wrote it down.</p>

<h2>What writing everything down actually means</h2>

<p>It doesn't mean polished essays. It means:</p>

<ul>
<li>Voice memos transcribed after every walk</li>
<li>A file for every active project with a running log</li>
<li>Notes after every meeting, within an hour</li>
<li>A daily log: what I did, what I learned, what I'm stuck on</li>
<li>A running document for every thesis I'm developing, even the weak ones</li>
</ul>

<p>None of this is published. Most of it will never be read by anyone, including me. The value isn't in the artifact. The value is in the act of writing.</p>

<h2>The overhead objection</h2>

<p>When people hear this, they usually say: "that sounds like a lot of overhead."</p>

<p>It is. And it's a rounding error compared to the overhead of circling the same problem for three weeks because you never wrote down what you actually thought about it.</p>

<p>The people who write everything down look slower in any given hour. Over a quarter, they ship more. Over a year, they look like they're living in a different universe.</p>"""),

    E("the-cheap-part-is-execution", "The cheap part is execution",
      "Everyone thinks execution is the hard part. It's not. Picking what to execute is.",
      "Strategy", "2026-03-25",
      """<p>Every founder I know who's been at it for more than a few years eventually lands on the same reluctant conclusion: the execution was never the hard part.</p>

<p>The hard part was picking the right thing to execute on.</p>

<h2>Why this is counterintuitive</h2>

<p>In the moment, execution always feels hard. The product is broken, the hire quit, the campaign is bleeding, the investor passed. Every day is a grind.</p>

<p>But the grind is trackable. The steps are known. You ship, you measure, you iterate. Hard work, but the process is clear.</p>

<p>Picking the right thing is the opposite. There's no process. You're trying to decide between options whose outcomes you can't know in advance. And unlike execution, nobody can do it for you.</p>

<h2>The decision spike</h2>

<p>Most people I know who've built successful things have a similar trajectory: a long period of average progress, then a decision point, then a sharp rise. The average progress is execution. The sharp rise isn't - it's the compound effect of picking something with actual leverage.</p>

<p>If you look only at the sharp rise, you see extraordinary execution. If you look at the decision point, you see a different story entirely.</p>

<h2>What this changes</h2>

<p>Once I accepted this, I started spending more time on decisions and less on execution. Not because execution doesn't matter - it does - but because my execution was already pretty good, and my decision-making was pretty bad.</p>

<p>For most ambitious people, this is the asymmetry. You've been rewarded your whole life for good execution. You're good at it. It feels productive.</p>

<p>But it's the cheap part.</p>"""),

    E("the-honest-feedback-problem", "The honest feedback problem",
      "The people most willing to give you honest feedback are usually the people least qualified to. And vice versa.",
      "Leadership", "2026-03-18",
      """<p>There's a specific asymmetry in receiving feedback that took me years to see.</p>

<p>The people most willing to give you unfiltered, hard-to-hear feedback are usually people who don't actually know your situation well. They have strong opinions. They're confident. They're often wrong.</p>

<p>The people most qualified to give you feedback - the ones who deeply understand your context, your constraints, your history - are usually the most reluctant. They're reluctant because they <em>understand</em>. They know how much their words would weigh.</p>

<h2>The implication</h2>

<p>If you want good feedback, you have to drag it out of the qualified people. And you have to filter hard against the unqualified people.</p>

<p>Both are hard.</p>

<p>Dragging it out of qualified people requires creating a container they can give it in. Explicit invitation. Explicit permission. Specific questions. Gratitude afterward, even when the feedback stings. Over time, they trust that telling you the truth won't cost them the relationship.</p>

<p>Filtering unqualified people is harder because their confidence is infectious. They say things with the authority of people who've thought about it deeply. They usually haven't.</p>

<h2>The signal</h2>

<p>The best diagnostic: did the feedback surprise you?</p>

<p>Feedback that matches your internal model too closely is probably confirmation. Feedback that contradicts your model in unexpected ways - not in predictable contrarian ways, but in ways you can't quite dismiss - is usually where the signal is.</p>"""),

    E("why-most-meetings-fail", "Why most meetings fail",
      "Meetings don't fail because they're meetings. They fail because they're held without the preconditions that make them useful.",
      "Operations", "2026-03-11",
      """<p>The meeting backlash has gone too far. Not all meetings are waste. Most are. But the solution isn't "fewer meetings." The solution is: meet when the preconditions are met, and don't when they aren't.</p>

<h2>The preconditions for a useful meeting</h2>

<ol>
<li>A specific decision to be made</li>
<li>Clear decision-maker</li>
<li>Pre-read that participants have actually read</li>
<li>Everyone needed is present</li>
<li>A time box</li>
</ol>

<p>Without all five, the meeting will extend to fill its time, produce no actual decisions, and leave everyone feeling vaguely productive because something happened.</p>

<h2>The pre-read gap</h2>

<p>The biggest single failure mode is the pre-read. People say they read the doc and then, in the meeting, demonstrate they didn't. The meeting becomes 40 minutes of catching up on the doc, and 5 minutes of the actual decision.</p>

<p>The fix I've seen work: silent reading at the start of the meeting. 10 minutes. Everyone reads. Then discuss. Ugly, but it works.</p>

<h2>The "we need to align" meeting</h2>

<p>Most alignment meetings exist because nobody wrote down the decision. The meeting is compensating for a documentation failure upstream. The solution isn't another meeting; it's a memo.</p>

<p>Every time someone says "we need to get everyone aligned," the question should be: aligned on what? If you can write it down in a paragraph, start with the paragraph.</p>"""),

    E("the-compound-interest-of-reputation", "The compound interest of reputation",
      "Reputation is one of the few assets that grows on its own if you don't damage it. Almost nobody treats it that way.",
      "Career", "2026-03-04",
      """<p>In financial compound interest, the magic happens because your returns earn returns. You don't have to do anything once the principal is in place. Time does the work.</p>

<p>Reputation works the same way. Every time you do what you said, deliver clean work, return a favor, you're not just building reputation - you're growing the pool of people who can vouch for you to other people. And those other people become vouchers themselves.</p>

<p>The function is exponential.</p>

<h2>The rare-event model</h2>

<p>What doesn't grow exponentially is damage. A reputation takes 5 years to build and 5 minutes to break. This is because vouchers only transmit positive signals by default. Negative signals get transmitted on rare events - when the voucher has to actively warn someone.</p>

<p>Those rare events tend to be triggered by specific betrayals: broken commitments, dishonesty, being caught in a lie, public rudeness.</p>

<p>The math of reputation therefore is: almost nothing you do makes it faster, but a small number of things you do can permanently slow it down.</p>

<h2>What this means practically</h2>

<p>The optimization isn't "build reputation." The optimization is "don't destroy it."</p>

<p>Which is counterintuitive because it means saying no to some short-term gains. Lying to get a deal. Shipping something you wouldn't ship if your name were on it. Stiffing a contractor because you technically can.</p>

<p>Each of these looks like a rational short-term choice. Each of them is a reputation event the long-term math can't absorb.</p>

<p>The people who win over 20-year horizons are almost always the people who refused to take those short-term deals.</p>"""),

    E("the-specific-claim-rule", "The specific claim rule",
      "Generic claims are weaker than specific ones, regardless of whether they're true. This is underappreciated.",
      "Writing", "2026-02-24",
      """<p>Pretend someone sends you an email that says "I help businesses grow." Now pretend a second email says "I helped [Company] go from 5 clients to 70 in 14 months."</p>

<p>The second one is more persuasive. This is not news.</p>

<p>What's less obvious: the second claim is more persuasive even if the first one is literally more impressive. The specificity of a claim carries more weight than the scope of it.</p>

<h2>Why specificity wins</h2>

<p>A specific claim is verifiable. A generic one isn't. Readers don't consciously verify - they don't contact the company and ask about the 70 clients. But their brain registers that the claim <em>could</em> be verified. A generic claim can't be verified; there's no specific thing to check.</p>

<p>That verifiability-in-principle translates directly to credibility. Specific = plausibly true. Generic = could be anything.</p>

<h2>The test</h2>

<p>Anywhere you've written a generic claim, ask: could I replace this with something specific and still defend it?</p>

<ul>
<li>"Fast growth" → "23% quarter-over-quarter"</li>
<li>"Satisfied customers" → "NPS of 52 after 18 months"</li>
<li>"Lots of experience" → "89 campaigns launched since 2019"</li>
</ul>

<p>If you can substitute, you should. If you can't substitute, the original claim is probably overstating reality.</p>"""),

    E("when-to-hire", "When to hire (and when not to)",
      "Hiring too early kills early companies. Hiring too late kills growing ones. The in-between is narrow and hard to find.",
      "Operations", "2026-02-18",
      """<p>The most common mistake I see founders make is hiring too early. The second-most-common is hiring too late. The window between the two is narrow.</p>

<h2>The "hire too early" symptoms</h2>

<ul>
<li>You haven't tried to do the role yourself yet</li>
<li>You don't know what the role should actually do</li>
<li>You think hiring someone will unlock growth</li>
<li>The pitch to the candidate is vague</li>
</ul>

<p>When you hire under these conditions, you get someone who spends their first 3-6 months figuring out what their job is. Those are months you're paying for with no clarity about what you're paying for.</p>

<h2>The "hire too late" symptoms</h2>

<ul>
<li>The founder (you) is the bottleneck for 3+ critical workflows</li>
<li>Progress is visibly decelerating</li>
<li>You're doing work that would be obviously better done by a specialist</li>
<li>You've been saying "I should hire for this" for 90+ days</li>
</ul>

<p>Here the damage isn't direct cost - it's opportunity cost. Everything downstream of the bottleneck stalls.</p>

<h2>The threshold</h2>

<p>The right time to hire is when: you've done the role yourself, you can articulate what success looks like, the work is predictable enough to explain, and the hire would obviously ship more per month than the cost.</p>

<p>If any of those is missing, the hire will probably disappoint.</p>"""),

    E("the-problem-with-frameworks", "The problem with frameworks",
      "Frameworks feel like insight. Usually they're the opposite.",
      "Thinking", "2026-02-10",
      """<p>I love frameworks. I also know they're dangerous.</p>

<p>A framework compresses complicated reality into a simple shape. This is helpful for communication, for teaching, for moving fast. It's also dangerous because the framework starts to do your thinking for you.</p>

<h2>The risk</h2>

<p>Once you know a framework, every problem starts looking like it fits. Maslow's hierarchy, SWOT, BCG matrix, AIDA, Five Whys, Jobs to be Done, whatever. Once the framework is in your head, you unconsciously map situations into it.</p>

<p>Usually they fit - kind of. Close enough that you feel like you've understood. But "close enough" hides the mismatch. The part of the situation that doesn't fit the framework is often where the interesting insight is.</p>

<h2>What to do instead</h2>

<p>Use frameworks as prompts, not verdicts. Apply them, then check for what doesn't fit. The residue - the facts the framework couldn't absorb - is usually where the learning is.</p>

<p>Frameworks are scaffolding for thought. They should be noticeably less intelligent than the thinker using them. When a framework starts producing insights you didn't work for, that's your signal to be skeptical.</p>"""),

    E("on-being-wrong", "On being wrong",
      "Being wrong is the default state. Recognizing it quickly is rare. Recovering without ego is rarer still.",
      "Thinking", "2026-02-02",
      """<p>Being wrong isn't embarrassing. It's the default state of working on anything hard.</p>

<p>What's embarrassing is the moment between knowing you're wrong and admitting it. Most people flinch in that moment. They reframe, they defend, they move the goalposts. They extend their public position long past the point where they privately believed it.</p>

<h2>The cost of the flinch</h2>

<p>Every time you defend a position you privately know is wrong, you're trading long-term trust for short-term ego. The trade is bad. People around you notice the flinch; it erodes their trust in you faster than admitting the error would have.</p>

<p>Over time, the people who flinch develop a pattern that's visible to everyone but them.</p>

<h2>What the good version looks like</h2>

<p>Updating fast, publicly, with specifics. "Two weeks ago I said X. Based on [new info], I now think Y. Here's what I'd do differently if I were making the call today."</p>

<p>This sounds weak. It's the opposite. Only people confident in their judgment can publicly revise it. The people who can't are advertising their fragility.</p>"""),

    E("what-you-dont-have-to-do", "What you don't have to do",
      "Ambitious people spend most of their time on things they don't have to do. This isn't a moral failing; it's a coordination problem.",
      "Productivity", "2026-01-27",
      """<p>Ambitious people have too much to do. This is by definition: ambition means pursuing more than the available time clearly supports.</p>

<p>The question isn't "how do I do more." It's "what don't I have to do?"</p>

<h2>The categories</h2>

<ul>
<li>Things I'm doing because I've always done them</li>
<li>Things I'm doing to signal effort</li>
<li>Things someone else could do</li>
<li>Things that matter less than they feel</li>
<li>Things I'm doing out of habit, not choice</li>
</ul>

<p>Every quarter, I walk through my calendar and my open projects and ask which of these buckets each one is in. The answers are always uncomfortable.</p>

<h2>The actual hard part</h2>

<p>The hard part isn't identifying what to drop. It's accepting the second-order effects.</p>

<p>Dropping an obligation usually means disappointing someone. Dropping a habit means not getting the small dopamine hit. Dropping "signaling effort" means looking less busy, which some people interpret as "not working hard enough."</p>

<p>These social costs are real. They're also smaller than the alternative: being diluted across 20 things and great at none of them.</p>"""),

    E("ai-isnt-going-to-replace-you", "AI isn't going to replace you",
      "AI is going to replace the parts of your job that are replaceable. Whether that's a problem depends entirely on what else you're doing.",
      "AI", "2026-01-20",
      """<p>The "AI will replace knowledge workers" framing is too broad to be useful. A more useful framing: AI is replacing specific sub-tasks, fast.</p>

<p>Drafting, summarizing, researching, basic coding, scheduling, data entry, first-pass analysis, initial outreach - all of these are now 5-10x faster than they were three years ago. If your job is 80% these tasks, you're about to have a very strange decade.</p>

<p>If your job is 20% these tasks and 80% judgment calls, strategic decisions, human relationships, original creative work - AI is about to make you dramatically more productive without threatening you.</p>

<h2>The skew matters</h2>

<p>This isn't just "keep the high-value work." The underlying asymmetry: the replaceable tasks were always the cheap part of any job. They felt productive because they kept your hands busy. They didn't compound.</p>

<p>The tasks AI can't easily do are the ones that compound: taste, judgment, relationships, original frameworks, hard decisions with incomplete information.</p>

<h2>What to do</h2>

<p>Audit your week. What percentage of what you did could a capable AI have done? Be honest. If it's over 50%, you have a timing problem - not necessarily a career problem, but a timing problem about what you're spending today on.</p>

<p>The people who'll do well aren't the ones who ignore AI. They're the ones who use it to compress their replaceable tasks and spend the freed hours on things that compound.</p>"""),

    E("the-list-im-not-on", "The list I'm not on",
      "Most progress comes from lists other people built. Understanding which lists you're on (and aren't) explains more of career outcomes than most other factors.",
      "Career", "2026-01-13",
      """<p>There's a list of people a given person will think of when an opportunity comes up. Whether you're on that list or not determines a huge amount of what happens in your career.</p>

<p>You are on that list because of some combination of: you've done relevant work, they've seen you do it, they trust you, you're top of mind.</p>

<p>If you're off the list, no amount of talent or preparation will surface you for that opportunity. The list is the bottleneck.</p>

<h2>How lists work</h2>

<p>Most people maintain short mental lists. Maybe 3-10 names per category. "Who would I recommend for X." "Who's doing interesting work in Y." "Who's someone I trust for Z."</p>

<p>Getting on a list takes specific work: doing the kind of work they respect, being visible about it, making yourself reachable, staying top of mind without being annoying.</p>

<p>Staying on a list is maintenance: updating, delivering, being present when it matters.</p>

<h2>The asymmetry of being on many lists</h2>

<p>Being on one person's list is a weak asset. Being on the lists of 20-50 credible people in your space is a career-changing one. Each list carries its own opportunity flow.</p>

<p>The compounding is nonlinear: 50 list-memberships isn't 50x 1 list-membership. It's more like 500x.</p>"""),

    E("the-calm-founder", "The calm founder",
      "The best founders I know aren't intense. They're calm. Pressure radiates through companies; so does calm.",
      "Leadership", "2026-01-06",
      """<p>The stereotype is the intense, driven founder. Everyone's seen the type. The best founders I know aren't that. They're calm.</p>

<p>Calm doesn't mean slow. It doesn't mean low standards. It means a specific emotional stability under stress that radiates through the people around them.</p>

<h2>Why calm matters</h2>

<p>Teams mirror their leader's emotional state. A founder panicking produces a panicking team. A founder calm in a crisis produces a team that operates through the crisis.</p>

<p>Over a year, the compound difference is enormous. Calm teams make clearer decisions. They recover from mistakes faster. They attract better talent.</p>

<h2>Where calm comes from</h2>

<p>Calm isn't just a personality trait. It's a practice:</p>

<ul>
<li>Sleep</li>
<li>Systems that remove small decisions from your day</li>
<li>Clarity about what you're building</li>
<li>Financial runway that doesn't force short-termism</li>
<li>Relationships outside work</li>
</ul>

<p>Founders who manage these things can be calm. Founders who don't can only pretend to be.</p>"""),

    E("the-discipline-of-not-knowing", "The discipline of not knowing",
      "The ability to sit with 'I don't know yet' is underrated. It's the gate that separates pattern-matchers from actual thinkers.",
      "Thinking", "2025-12-30",
      """<p>When someone asks you a question, the default response is to answer. When you don't know the answer, the default response is to produce one anyway, shaped by your existing beliefs, intuitions, and pattern-matching.</p>

<p>The discipline of saying "I don't know yet" is the discipline of not doing that.</p>

<h2>Why it's hard</h2>

<p>"I don't know" feels like weakness. In professional settings, it reads as unprepared or unconfident. There's strong social pressure to produce a take.</p>

<p>But the take you produce under pressure is almost always a cheap take. It's pattern-matched to something familiar. It doesn't actually engage with what's new about this specific question.</p>

<h2>The useful move</h2>

<p>When asked a question you haven't thought about enough:</p>

<p>"I don't know yet. Here's what I'd want to understand before forming a real view: [specific things]. My gut says [X] but I don't trust the gut here."</p>

<p>This is more useful than a confident guess. It shows you thought enough to identify your own uncertainty. It opens a conversation instead of closing one. It preserves the option to update.</p>

<p>The people I most trust on complicated questions are the people most willing to say they don't know.</p>"""),

    E("why-systems-beat-willpower", "Why systems beat willpower",
      "You will always have less willpower than you think. The systems you put in place when you have it determine what happens when you don't.",
      "Productivity", "2025-12-23",
      """<p>Willpower is a finite resource. Studies have argued about the details, but the practical experience is clear: you can push yourself through X amount of hard work per day, and after X, the quality degrades sharply.</p>

<p>The implication: the goal isn't to have more willpower. The goal is to need less.</p>

<h2>Systems do the work willpower can't</h2>

<p>Every automated habit is willpower you don't have to spend. Every pre-made decision is one you don't have to make today. Every routine is a decision tree you already walked.</p>

<p>The people who get the most done aren't the most disciplined. They're the ones who built the most systems when they were fresh, so they could operate on autopilot when they weren't.</p>

<h2>Examples</h2>

<ul>
<li>Decide your weekly priorities Sunday night, when you're rested</li>
<li>Set up meetings at the same time each week so they don't require scheduling willpower</li>
<li>Write tomorrow's priorities before ending today</li>
<li>Have a default response to common interruption types</li>
<li>Automate recurring decisions (meals, workouts, outfits at extremes)</li>
</ul>

<p>None of these are glamorous. Cumulatively they produce a different life.</p>"""),

    E("the-art-of-asking", "The art of asking",
      "Most people ask for help badly. The difference between a well-formed ask and a vague one is the difference between getting help and not.",
      "Communication", "2025-12-15",
      """<p>Most asks fail not because the person wouldn't help, but because the ask was unclear.</p>

<p>A bad ask puts the work of figuring out what you need on the person you're asking. "Hey, would you have time to chat about career stuff?" puts them in the position of figuring out what the conversation should be about.</p>

<p>A good ask does that work for them.</p>

<h2>The structure of a good ask</h2>

<ol>
<li>Context (why I'm asking you specifically)</li>
<li>The specific thing I'm trying to figure out</li>
<li>What I've already tried / thought about</li>
<li>The exact form of help I'm hoping for</li>
<li>A specific time commitment</li>
</ol>

<p>Example: "I'm thinking about moving from in-house to agency. I know you made that transition in 2022 and came out stronger. I've read [thing], talked to [people], and I'm still unsure about [specific uncertainty]. Would 20 minutes on the phone help me think this through? Here's my calendar."</p>

<h2>Why this works</h2>

<p>The person asked can say yes or no in 30 seconds. They know what they're being asked to do. They can estimate the effort. They feel valued because you treated them as a specific source of insight, not a generic time-donor.</p>

<p>Most "no" responses to asks are actually responses to cognitive load, not the ask itself. Removing the cognitive load flips many no's to yes's.</p>"""),

    E("the-50-percent-rule", "The 50% rule",
      "If you're at 50% certainty, you don't know. If you're at 80%, you might. If you're at 95%, you're probably wrong about at least one hidden assumption.",
      "Decisions", "2025-12-08",
      """<p>Calibration isn't a natural human skill. Most people are over-confident at the high end and under-confident at the low end. Practicing deliberate calibration changes how you make decisions.</p>

<h2>The scale</h2>

<p>At 50% certainty, you're flipping coins. You don't know. If you're pretending you do, you're fooling yourself.</p>

<p>At 80%, you have a reasonable view. You should act on it but keep your eye out for new information.</p>

<p>At 95%, you're confident enough that you should be alarmed by one thing: hidden assumptions. Very high confidence usually means you haven't thought about what could make you wrong. When you actually list the assumptions, many of them are less certain than your overall take.</p>

<p>At 99%, you're either genuinely right about something simple, or you're wrong and don't realize it.</p>

<h2>The exercise</h2>

<p>For any meaningful decision, force yourself to assign a probability. Write it down. Then - separately - list what would have to be true for the opposite to be the case.</p>

<p>If you confidently assigned 95%, and the opposite list has even one plausible item you hadn't deeply examined, your 95% was wrong. You meant 80%.</p>

<p>Over time, this practice recalibrates your gut.</p>"""),

    E("your-unique-combination", "Your unique combination",
      "Almost nobody is the best in the world at one thing. Everyone can be the best combination of three things.",
      "Career", "2025-12-01",
      """<p>The best-in-the-world path is available to roughly no one. For any given skill, there are thousands of people better than you. You'll spend your life chasing them.</p>

<p>But the best combination of three skills? That's a niche nobody else is filling.</p>

<h2>The Scott Adams frame</h2>

<p>Scott Adams wrote about this. He's not the funniest cartoonist. Not the best writer. Not the smartest business thinker. But he's the best combination of those three, which carved out a path nobody else was on.</p>

<p>The insight: the difficulty of being top 1% in three things you care about is much lower than being top 0.01% in one. And the combination is more defensible because it's rarer.</p>

<h2>How to find your combination</h2>

<p>Three questions:</p>

<ol>
<li>What skills have you genuinely invested in for years?</li>
<li>Which ones do you keep coming back to even when nobody's paying you?</li>
<li>Where do they intersect - what could only you produce given that combination?</li>
</ol>

<p>The answer to #3 is your career, if you're willing to see it. Most people aren't, because the combination feels less prestigious than any single top-tier skill would. The combination also happens to be more durable.</p>"""),

    E("the-best-email-is-short", "The best email is short",
      "Every word in an email is a tax on the reader. The best emails pay the minimum tax for the maximum value transferred.",
      "Communication", "2025-11-25",
      """<p>I've written and received a lot of email. The pattern is unambiguous: shorter emails get better responses.</p>

<p>This isn't because recipients are lazy. It's because the attention cost of a long email is real, and most long emails could be half as long without losing anything.</p>

<h2>The structure of a short email</h2>

<ol>
<li>Who I am, in one phrase (if we don't know each other)</li>
<li>Why I'm emailing (the specific reason)</li>
<li>What I'm asking for (specifically)</li>
<li>A time-bound or low-friction version of the ask</li>
</ol>

<p>Four to six sentences. Close.</p>

<h2>What to leave out</h2>

<ul>
<li>"I hope this email finds you well" (it's not doing anything)</li>
<li>Long backstory of why you're interesting</li>
<li>Multiple asks in the same email</li>
<li>"Happy to chat whenever, just let me know" (give me two specific times)</li>
<li>"I don't want to take too much of your time" (you already are, by saying this)</li>
</ul>

<h2>The test</h2>

<p>Reread your email. Cut every sentence that, if removed, wouldn't affect whether the recipient acts. You'll usually cut 30-50% without losing any content.</p>

<p>The remaining version is better.</p>"""),

    E("quality-is-a-schedule-decision", "Quality is a schedule decision",
      "Quality isn't about whether you care. It's about whether your schedule allows you to do the work well.",
      "Operations", "2025-11-18",
      """<p>"I care about quality" doesn't produce quality. What produces quality is giving yourself enough time to do the work well, with space to revise, iterate, and reject the first version.</p>

<p>Most quality failures aren't motivation failures. They're schedule failures. The deadline was tight, the bar was moved, the last third was rushed.</p>

<h2>The buffer principle</h2>

<p>High-quality work requires a buffer. Time between "done" and "needs to ship." In that buffer, you notice things. You revise. You have doubts. You talk to someone. You improve.</p>

<p>Rushed work skips that buffer. What ships is your first-pass output. First-pass output is rarely your best.</p>

<h2>The math nobody does</h2>

<p>Teams that schedule for 100% utilization ship more work volume, lower quality. Teams that schedule for 70% utilization ship less volume, much higher quality. Over a year, the 70% team's output is worth more - because the work is better and the rework is less.</p>

<p>Most teams don't do this math. They see 70% utilization as "unproductive" instead of "investing in quality."</p>

<h2>The implication</h2>

<p>If you care about quality, fight for time. Say no to commitments that don't leave a buffer. Your competitors won't, and the difference will show.</p>"""),
]

if __name__ == "__main__":
    build_writing(ESSAYS)
