#!/usr/bin/env python3
"""Rewrite the remaining 77 glossary entries (DR + Business + Marketing + Sales + SEO)
at the same teaching depth used for the AI glossary:
- def        - plain-English one-sentence answer
- explain    - paragraph that builds intuition
- example    - concrete, real scenario
- why        - why it matters / what to do with this

Uses the same .gloss-section-head / .gloss-explain / .gloss-example / .gloss-why
markup and CSS as the AI rewrite.
"""
import re
from pathlib import Path

ROOT = Path("/Users/ble/Desktop/sams site")
GLOSSARY = ROOT / "glossary"

# -----------------------------------------------------------------------------
# 77 terms, grouped by topic. Each in the same structure as the AI terms.
# -----------------------------------------------------------------------------
TERMS = {
    # ===================== DIRECT RESPONSE =====================
    "direct-response": {
        "term": "Direct Response",
        "topic": "Direct Response",
        "def": "Marketing that asks for a specific, measurable action right now. The opposite of 'brand awareness.'",
        "explain": (
            "Direct response is any marketing where you can tell, in real time, whether it worked. "
            "Someone sees your ad, reads your email, lands on your page, and either does the thing you "
            "asked for (buy, sign up, book a call) or they don't. The response is direct, measurable, "
            "and immediate. That makes it the opposite of 'brand marketing,' which works over years "
            "through vague effects."
        ),
        "example": (
            "An ad that says 'Download our free guide on cold email' with a form is direct response. "
            "You can see exactly how many downloads happened and whether the ad paid for itself. "
            "A billboard that says 'We make insurance simple' is NOT direct response, you can't measure it."
        ),
        "why": (
            "If you can't afford to wait years to see if marketing worked, you need direct response. "
            "It's how small businesses survive. Every dollar in, track every dollar out. The entire "
            "discipline of direct response is about making marketing accountable."
        ),
        "related": ["copywriting", "offer", "cta", "aida"],
    },
    "copywriting": {
        "term": "Copywriting",
        "topic": "Direct Response",
        "def": "The craft of writing words that sell. Not storytelling, persuading.",
        "explain": (
            "Copywriting is writing designed to drive a specific action. It's the headline that makes "
            "someone click, the email that makes them open, the sales page that makes them buy. "
            "Good copy reads like one friend talking to another about something important. It doesn't "
            "sound 'written.' It feels natural, but every word is there on purpose."
        ),
        "example": (
            "'Save up to 40% on your energy bill.' is copy. 'Our innovative energy solutions empower "
            "sustainable living.' is marketing speak nobody reads. The first one sells. The second one fills space."
        ),
        "why": (
            "Whatever business you're in, you'll need to write words that make someone do something. "
            "An email, a page, a text, a post. The better your copy, the cheaper every customer gets. "
            "This is the single highest-leverage skill in business."
        ),
        "related": ["headlines", "aida", "pas", "cta"],
    },
    "headlines": {
        "term": "Headline",
        "topic": "Direct Response",
        "def": "The first thing your prospect reads. It decides whether they read anything else.",
        "explain": (
            "The headline is a switch. Strong headline, the reader keeps reading. Weak headline, "
            "they're gone. You have maybe two seconds and a handful of words to make someone care "
            "enough to continue. The goal of a headline isn't to sell, it's to earn the next line of copy."
        ),
        "example": (
            "'How to get 10 new clients in 30 days, without cold calling' is a headline. "
            "'Welcome to Our Services' is not a headline, it's a tombstone. "
            "Same business. Different headline. Radically different response rate."
        ),
        "why": (
            "Legendary copywriter David Ogilvy said: 'When you have written your headline, you have "
            "spent eighty cents out of your dollar.' He wasn't exaggerating. Headlines account for most "
            "of the variance in marketing performance. Spend ten times as long on them as you think you should."
        ),
        "related": ["copywriting", "aida", "hooks"],
    },
    "hooks": {
        "term": "Hook",
        "topic": "Direct Response",
        "def": "The opening that grabs attention. The reason someone stops scrolling.",
        "explain": (
            "A hook is the first thing someone sees or hears. On social it's the first line. "
            "In a video it's the first three seconds. In an email it's the subject line plus "
            "preview text. A hook works by creating a pattern-break (unexpected), curiosity ('I need "
            "to know more'), or identification ('that's me'). Without a hook, nothing else you say matters."
        ),
        "example": (
            "'I made $50k last month. Here's exactly how.' is a hook, curiosity + identification + specificity. "
            "'Some thoughts on building a business' is not a hook, it commits to nothing and promises nothing."
        ),
        "why": (
            "In a world of endless scrolling, hooks are the entire game for the first three seconds. "
            "The best content with a weak hook gets seen by nobody. Bad content with a strong hook goes viral. "
            "The hook writes the check; the rest of the content cashes it."
        ),
        "related": ["headlines", "copywriting"],
    },
    "aida": {
        "term": "AIDA",
        "topic": "Direct Response",
        "def": "Attention → Interest → Desire → Action. A 100-year-old copy formula that still works.",
        "explain": (
            "AIDA is the structure of almost every piece of sales copy ever written. Get Attention "
            "(headline/hook). Build Interest (why this matters to you specifically). Create Desire "
            "(paint the picture of having this). Call to Action (tell them exactly what to do next). "
            "Not every piece follows AIDA explicitly, but the structure is hiding in almost all of it."
        ),
        "example": (
            "'Are you still paying for email tools you don't use? (A) Most small teams waste $200/mo "
            "on subscriptions they forgot about. (I) Imagine canceling five tools tomorrow without "
            "losing a single feature. (D) Try our free audit, 10 minutes, you'll see every unused "
            "subscription. (A)'"
        ),
        "why": (
            "AIDA is training wheels for copywriting. If you're writing a piece of sales copy and "
            "it's not working, check whether each section is doing its job. Missing an A, I, D, or A? "
            "That's usually where it breaks down."
        ),
        "related": ["pas", "pastor", "copywriting", "headlines"],
    },
    "pas": {
        "term": "PAS",
        "topic": "Direct Response",
        "def": "Problem → Agitate → Solve. The most direct-response of all copy formulas.",
        "explain": (
            "PAS starts by naming the prospect's problem, agitates it (makes them feel how painful it is), "
            "then offers your solution. It works because it mirrors how people actually think about "
            "buying: they're not buying a product, they're buying out of a problem. PAS forces you to "
            "describe the problem vividly enough that the reader pays attention, then offers the exit."
        ),
        "example": (
            "'You're losing leads because your follow-up is inconsistent. (P) Every week, 5 prospects "
            "go cold because nobody pinged them on day 3. Over a year, that's 260 lost deals. (A) Our "
            "follow-up system catches every one of them automatically. Here's how. (S)'"
        ),
        "why": (
            "PAS is tighter and more punchy than AIDA. For emails, ads, and short-form content, it "
            "usually outperforms. Use PAS when you need to be direct. Use AIDA when you have more room to unfold."
        ),
        "related": ["aida", "pastor", "copywriting"],
    },
    "pastor": {
        "term": "PASTOR",
        "topic": "Direct Response",
        "def": "Problem → Amplify → Story → Testimonial → Offer → Response. PAS for longer-form copy.",
        "explain": (
            "PASTOR expands PAS with three critical pieces: a Story (to make the solution real and "
            "emotional), a Testimonial (to provide social proof), and a clear Response ask (so they "
            "know exactly what to do next). It's designed for longer pieces, sales letters, VSLs, "
            "webinar scripts, where you have time to build the case."
        ),
        "example": (
            "A 20-minute webinar hitting each piece: the problem (your pipeline is unpredictable), "
            "amplify (here's what it costs you), story (Sarah was in the same spot; here's what happened), "
            "testimonial (Sarah and 200 others), offer ($197 program), response ('click here now')."
        ),
        "why": (
            "When someone says 'write me a sales page,' this is usually the structure. PASTOR's power "
            "is the Story and Testimonial slots, those do most of the persuasion. Weak story + weak "
            "testimonial = the page doesn't work, regardless of how good the problem and offer are."
        ),
        "related": ["aida", "pas", "copywriting", "sales-letter"],
    },
    "sales-letter": {
        "term": "Sales Letter",
        "topic": "Direct Response",
        "def": "A long-form written pitch, typically for a single product, with no distractions.",
        "explain": (
            "A sales letter is a webpage (or printed letter) designed to take a cold prospect from "
            "skeptical to sold on one page. No nav, no sidebar, no other links, just a headline, "
            "the body, and a single call-to-action repeated throughout. Usually 2,000 to 8,000 words. "
            "They're 'long' because they need to be; a high-price product can't be sold in a paragraph."
        ),
        "example": (
            "Most info-product landing pages are sales letters. You see a long scrolling page with "
            "testimonials, bullet points, a big guarantee, and a 'Buy now' button that appears "
            "several times. That structure works: long format converts cold traffic better than short "
            "format for anything over ~$100."
        ),
        "why": (
            "If you're selling anything at price where 'think about it' is a real risk, the sales "
            "letter is the canonical format. Master it and you can move any product you actually believe in."
        ),
        "related": ["copywriting", "vsl", "pastor", "offer"],
    },
    "vsl": {
        "term": "VSL (Video Sales Letter)",
        "topic": "Direct Response",
        "def": "A sales letter in video form. Most common format for high-ticket offers.",
        "explain": (
            "A VSL is typically a 5-30 minute video that pitches a single offer. Often it's just a "
            "voiceover with slides or text on screen, not a 'fancy' video. The format works because "
            "video holds attention longer than text does for most audiences, and you control the pace "
            "of information delivery."
        ),
        "example": (
            "An info-marketer selling a $2,000 course will often run ads to a VSL. The ad hooks you; "
            "you click; you land on a page that's mostly a video with a 'Buy Now' button that appears "
            "a few minutes in. The structure is pure PASTOR, just delivered in video."
        ),
        "why": (
            "For anything mid-to-high-ticket ($500+), VSLs consistently outperform text sales letters "
            "on cold traffic. They're also easier to record than write, for most people."
        ),
        "related": ["sales-letter", "copywriting", "offer"],
    },
    "offer": {
        "term": "Offer",
        "topic": "Direct Response",
        "def": "The specific thing the prospect gets, at what price, with what guarantees. The core of the sale.",
        "explain": (
            "Marketing people obsess over copy and ads. They should obsess over the offer. The offer "
            "is what you're actually giving the customer: the product, the price, the bonuses, the "
            "payment terms, the guarantee. A great offer can survive mediocre copy. Great copy can't "
            "save a weak offer. Before you tune anything else, tune the offer."
        ),
        "example": (
            "Weak offer: '$497 for my course.' Strong offer: '$497 for my course + three live coaching "
            "calls + a money-back guarantee if you don't get a client in 60 days + payment in 3 installments.' "
            "Same product, very different offer, very different conversion rate."
        ),
        "why": (
            "Most businesses 'have' an offer, but they've never actually engineered it. Spending a day "
            "just on your offer (what's included, what's bonus, what's the guarantee, what's the term) "
            "often moves conversion more than six months of copy tweaks."
        ),
        "related": ["value-equation", "guarantee", "sales-letter"],
    },
    "value-equation": {
        "term": "Value Equation",
        "topic": "Direct Response",
        "def": "How to measure the value of an offer: (Dream Outcome × Likelihood) ÷ (Time × Effort).",
        "explain": (
            "Alex Hormozi's framework from $100M Offers. The value of any offer is: the dream outcome "
            "the customer wants, times the likelihood they'll actually get it, divided by how long it "
            "takes and how much effort they have to put in. Maximize the top; minimize the bottom. "
            "Every 'grand slam' offer wins on all four variables."
        ),
        "example": (
            "'Lose 20 pounds in 90 days, eating whatever you want, with a 100% money-back guarantee' "
            "wins on all four: big dream outcome, high guarantee-backed likelihood, low time, low "
            "effort. Same product sold as 'try our meal plan' has a terrible value equation, it's "
            "vague on outcome, unsure on likelihood, unclear on time, and requires effort."
        ),
        "why": (
            "Before writing a single line of copy, run your offer through the value equation. If any "
            "number is bad, fix the offer, not the copy. This is the quickest diagnostic I know for "
            "why an offer isn't selling."
        ),
        "related": ["offer", "guarantee"],
    },
    "guarantee": {
        "term": "Guarantee",
        "topic": "Direct Response",
        "def": "An explicit promise that reduces the buyer's risk. The best ones shift risk entirely to the seller.",
        "explain": (
            "Every purchase has risk: 'what if this doesn't work for me?' A guarantee is how you "
            "address that risk explicitly. A weak guarantee ('30-day return') barely moves the needle. "
            "A strong guarantee ('results or your money back, plus $500') tells the buyer you believe "
            "in the product enough to stake your own money on it."
        ),
        "example": (
            "Domino's '30 minutes or it's free' is a classic. It made ordering pizza an easy yes, "
            "because the downside was capped. Gym memberships with 'no contract, cancel anytime' "
            "convert better than annual contracts even though annual usually has better unit economics."
        ),
        "why": (
            "The bolder the guarantee, the lower the buyer's perceived risk, the higher the conversion. "
            "People WAY over-weight risk. A strong guarantee often doesn't cost you much in refunds "
            "but boosts conversion meaningfully. Test this."
        ),
        "related": ["offer", "value-equation"],
    },
    "cta": {
        "term": "CTA (Call To Action)",
        "topic": "Direct Response",
        "def": "The exact thing you want the reader to do next. One per piece, clearly stated.",
        "explain": (
            "A CTA is the specific next step. Click a button. Fill a form. Call a number. Reply to this email. "
            "Good CTAs are specific ('Book your call'), one-action-only (not a menu of options), and "
            "repeated throughout longer pieces. Ambiguous CTAs ('learn more,' 'get in touch') confuse "
            "the reader and kill conversion."
        ),
        "example": (
            "'Book a 15-min call' is a good CTA, specific action, specific commitment, no ambiguity. "
            "'Let's chat' is a bad CTA, no specific action, no commitment, easy to procrastinate on."
        ),
        "why": (
            "Most marketing fails at the very end. You spent hours on the copy and then used 'Learn More' "
            "as the button. Hit the CTA harder than you think you should. The CTA isn't where you're "
            "polite, it's where you're direct. Tell them exactly what to do and why now."
        ),
        "related": ["copywriting", "aida", "cta"],
    },
    "urgency": {
        "term": "Urgency",
        "topic": "Direct Response",
        "def": "A reason to act now instead of later. Usually time-based.",
        "explain": (
            "Without urgency, prospects procrastinate and never buy. Urgency is any reason the decision "
            "needs to happen now: a deadline, a countdown timer, a 'this week only' sale. Urgency works "
            "because humans have infinite future-self optimism and finite attention today. If they can "
            "buy later, they'll buy never."
        ),
        "example": (
            "'This training goes back behind the paywall on Friday' is urgency. 'We're always here when "
            "you're ready' is the opposite, and it kills sales. Even a soft urgency ('enrolling this "
            "cohort only') beats no urgency."
        ),
        "why": (
            "Don't fake urgency; customers sense it and lose trust. But if you have real urgency (a "
            "cohort starts; the price goes up; bonuses expire), USE IT. It's the difference between a "
            "prospect thinking 'I'll come back to this' (and never coming back) and 'I need to decide today.'"
        ),
        "related": ["scarcity", "cta", "offer"],
    },
    "scarcity": {
        "term": "Scarcity",
        "topic": "Direct Response",
        "def": "A reason your offer is limited in quantity. The sibling of urgency.",
        "explain": (
            "Where urgency is about time ('before Friday'), scarcity is about quantity ('only 20 "
            "spots'). Both create a reason to decide now. Scarcity works because of loss aversion, "
            "humans hate missing out more than they love gaining. Genuine scarcity (capped cohorts, "
            "limited inventory, one-time releases) is powerful. Fake scarcity destroys trust."
        ),
        "example": (
            "'Only 20 seats in this cohort; 12 taken' is scarcity. 'Limited spots' without a real "
            "number is lazy scarcity. Truly scarce offerings (one-on-one coaching, limited edition "
            "products, cohort-based courses) convert better than unlimited ones, even at higher prices."
        ),
        "why": (
            "Scarcity creates decision pressure. Use only when real, and make the math obvious. 'Only "
            "X left of Y' is how you communicate scarcity without sounding like a used-car salesman."
        ),
        "related": ["urgency", "offer"],
    },
    "lead-magnet": {
        "term": "Lead Magnet",
        "topic": "Direct Response",
        "def": "A free resource you give in exchange for someone's email/contact info.",
        "explain": (
            "A lead magnet is how you convert traffic into leads. Someone lands on your page; you "
            "offer them something valuable for free (a guide, a template, a checklist, a tool); in "
            "exchange they give you their email. Now you can market to them over time via email. "
            "Without a lead magnet, most visitors leave and you never hear from them again."
        ),
        "example": (
            "'Download the free 2026 Email Marketing Template Library' in exchange for an email "
            "is a good lead magnet. So is 'Use our free ROAS calculator.' Generic 'subscribe to our "
            "newsletter' forms convert way worse, because they give nothing immediate in return."
        ),
        "why": (
            "Every visitor you don't capture is gone forever. Lead magnets are how you recover "
            "value from the 99% of visitors who aren't ready to buy today. Build a good one and your "
            "marketing gets compounding returns."
        ),
        "related": ["lead-gen", "offer"],
    },
    "lead-gen": {
        "term": "Lead Generation",
        "topic": "Direct Response",
        "def": "The practice of turning strangers into people who've given you permission to market to them.",
        "explain": (
            "Lead gen is the front door of direct response. You run ads, write content, send cold "
            "emails, whatever, all with one goal: get strangers to raise their hand and say 'tell me "
            "more.' Once they're leads (email, phone, form submission), you can market to them over "
            "time. Lead gen is about volume and cost, not immediate sales."
        ),
        "example": (
            "A Facebook ad driving to a free guide download is lead gen. So is a cold email asking "
            "for a 15-min call. In both cases, the immediate 'conversion' is capturing contact info, "
            "not making a sale. Sales happen later, in the follow-up."
        ),
        "why": (
            "Most B2B and higher-ticket businesses run on lead gen + nurture. If you're not capturing "
            "leads, you're renting attention from ads and then throwing it away. Build a real lead "
            "gen engine and your marketing economics improve forever."
        ),
        "related": ["lead-magnet", "prospecting", "offer", "cta"],
    },

    # ===================== BUSINESS =====================
    "arr": {
        "term": "ARR (Annual Recurring Revenue)",
        "topic": "Business",
        "def": "The total yearly revenue you can predict from subscriptions or contracts.",
        "explain": (
            "ARR is the dollar amount of subscription revenue you'd collect over the next 12 months "
            "if NOTHING changed, no new customers, no cancels. It's the headline metric for SaaS and "
            "any subscription business, because it smooths out monthly noise and captures the size of "
            "the recurring business."
        ),
        "example": (
            "100 customers paying $200/month = $20,000 MRR = $240,000 ARR. If you're growing, ARR is "
            "your run-rate, what the business is 'worth' on a revenue basis. Investors price SaaS by "
            "multiples of ARR (typically 5-15x for healthy companies)."
        ),
        "why": (
            "ARR is how SaaS talks to itself. If you're running or investing in a subscription business, "
            "you live in ARR. Month-to-month revenue matters less than whether ARR is growing, what the "
            "growth rate is, and what the retention looks like under the hood."
        ),
        "related": ["mrr", "nrr", "retention", "churn"],
    },
    "mrr": {
        "term": "MRR (Monthly Recurring Revenue)",
        "topic": "Business",
        "def": "The total predictable revenue each month from subscriptions.",
        "explain": (
            "MRR is ARR divided by 12. It's the monthly version, what you'd collect this month if "
            "nothing changed. MRR is how most SaaS dashboards show revenue, because monthly changes are "
            "visible faster than annual ones. Track MRR, new MRR, expansion MRR, churned MRR, net new "
            "MRR, each tells you something different."
        ),
        "example": (
            "If you added 20 new customers at $100/mo and lost 5 customers at $150/mo: new MRR +$2,000, "
            "churned MRR -$750, net new MRR $1,250. That's the vocabulary. Your MRR went from say "
            "$50,000 to $51,250."
        ),
        "why": (
            "MRR is the pulse of a subscription business. Spiking MRR means acquisition is working. "
            "Rising churn MRR means something's wrong with the product. Healthy expansion MRR means "
            "customers love you. One number at 30,000 feet; three or four numbers at ground level."
        ),
        "related": ["arr", "nrr", "churn", "retention"],
    },
    "nrr": {
        "term": "NRR (Net Revenue Retention)",
        "topic": "Business",
        "def": "How much recurring revenue you keep from existing customers over a year, accounting for expansion AND churn.",
        "explain": (
            "NRR = (starting revenue + expansions - churns - downgrades) / starting revenue. Over 100% "
            "means your existing customer base grew revenue even without new customers, they upgraded "
            "faster than they canceled. This is the holy grail of SaaS metrics. NRR > 120% means you "
            "could stop acquiring customers and still grow."
        ),
        "example": (
            "Start year with $10M ARR. Existing customers expand to $12M, but some churn to $11M by "
            "year-end. NRR = $11M / $10M = 110%. Best SaaS companies are 130-150% NRR. Under 100% means "
            "your bucket is leaking faster than customers are topping it up."
        ),
        "why": (
            "NRR is the single most important metric for long-term SaaS health. High NRR compounds: "
            "even mediocre acquisition plus great NRR produces huge businesses. Low NRR means you're "
            "stuck on an acquisition treadmill forever."
        ),
        "related": ["arr", "mrr", "churn", "retention"],
    },
    "churn": {
        "term": "Churn",
        "topic": "Business",
        "def": "The rate at which customers or revenue leaves your business. Lower is better.",
        "explain": (
            "Churn is the leakage. Customer churn = % of customers who cancel in a period. Revenue churn = "
            "% of revenue lost in a period (different from customer churn when customers downgrade). "
            "Track both, because they tell different stories. Losing one big customer and keeping many "
            "small ones looks fine by customer churn but terrible by revenue churn."
        ),
        "example": (
            "Month starts with 1,000 customers; 30 cancel. Customer churn = 3% monthly, 36% annualized. "
            "Most SaaS aims for <5% annual for enterprise, 3-7% monthly for SMB. If your churn is higher, "
            "your product, your target market, or both need rethinking."
        ),
        "why": (
            "Churn is the tax on every growth effort. High churn eats new acquisition. Unchecked churn "
            "kills businesses quietly; you grow through a valley and don't notice until revenue flatlines. "
            "Measure monthly. Investigate every cancel."
        ),
        "related": ["retention", "nrr", "mrr", "arr"],
    },
    "retention": {
        "term": "Retention",
        "topic": "Business",
        "def": "The opposite of churn: how many customers (or how much revenue) you keep over time.",
        "explain": (
            "Retention is the percentage of customers (or revenue) still with you at the end of a "
            "period. It's usually shown as a cohort curve: of customers who signed up in January, "
            "how many are still paying in February, March, April, etc. The shape of that curve tells "
            "you everything about your business's long-term health."
        ),
        "example": (
            "Of 100 people who signed up in January, 80 are still paying in February (80% retention). "
            "By month 12, 40 are still paying (40% retention). If that 40% is stable (not dropping), "
            "you have a real business. If it keeps dropping, you have a leaky bucket."
        ),
        "why": (
            "Retention is the single biggest lever on business valuation. Improving retention from 90% "
            "monthly to 95% monthly isn't 5% better, it's dramatically better, because it compounds "
            "over time. Investors value retention over growth for mature businesses."
        ),
        "related": ["churn", "nrr", "ltv"],
    },
    "kpi": {
        "term": "KPI (Key Performance Indicator)",
        "topic": "Business",
        "def": "The handful of metrics that tell you if the business is actually working.",
        "explain": (
            "KPIs are the specific numbers you track to know whether you're winning. Not all metrics "
            "are KPIs, that's the point. A KPI is a metric tied directly to a goal. For a SaaS company, "
            "KPIs might be MRR, churn, CAC, LTV. For a restaurant: revenue per seat, food cost %, "
            "table turn time. Picking the right 3-5 KPIs is harder than it sounds."
        ),
        "example": (
            "A growth-stage SaaS might track: (1) net new MRR, (2) NRR, (3) CAC payback, (4) gross margin. "
            "Those four numbers, updated weekly, tell you 90% of what matters. Dozens of other metrics "
            "are interesting; these four are the KPIs."
        ),
        "why": (
            "If everything is a KPI, nothing is. Teams with 20 'critical' dashboards are teams with no "
            "priorities. Pick the five that actually move decisions and ignore the rest. Your KPIs should "
            "determine what you do this week."
        ),
        "related": ["okr", "arr", "ltv"],
    },
    "okr": {
        "term": "OKR (Objectives + Key Results)",
        "topic": "Business",
        "def": "A goal-setting framework: a big qualitative goal plus 3-5 measurable outcomes that prove you hit it.",
        "explain": (
            "OKRs force you to commit to outcomes, not activities. Each OKR has one Objective (a "
            "direction, usually ambitious) and 3-5 Key Results (measurable outcomes that make the "
            "Objective concrete). Set them quarterly. Score them at the end. Adjust."
        ),
        "example": (
            "Objective: 'Become the category's most-loved product.' Key Results: (1) NPS from 40 to 65, "
            "(2) Organic mentions 10x quarter-over-quarter, (3) Product-led signup rate from 8% to 15%. "
            "Those three numbers tell you if the objective was hit."
        ),
        "why": (
            "OKRs are better than traditional goals because they force concreteness. 'Grow revenue' is "
            "a wish. 'Hit $5M ARR by Q4 end' is a KR. Good OKRs make the quarter visible; bad OKRs "
            "are quickly ignored. Invest time in writing them."
        ),
        "related": ["kpi"],
    },
    "burn-rate": {
        "term": "Burn Rate",
        "topic": "Business",
        "def": "The monthly cash loss of a company that isn't profitable yet.",
        "explain": (
            "Burn rate is how fast you're spending money faster than you're making it. Typically shown "
            "as a monthly dollar figure: 'we're burning $300k/month.' Paired with your cash-on-hand, "
            "this tells you your runway, how long until you run out. Every unprofitable startup obsesses "
            "over burn rate and runway."
        ),
        "example": (
            "You have $3M in the bank. You spend $500k/month, make $200k/month. Burn is $300k/month. "
            "Runway is $3M / $300k = 10 months. That's how long you have to either become profitable "
            "or raise more money. After that, the business dies."
        ),
        "why": (
            "Burn is the countdown. Most founders under-estimate it until they can see the wall. "
            "Know your burn to the dollar, your runway to the month. Revisit monthly. When burn creeps "
            "up faster than revenue, you have a problem worth solving this quarter, not next."
        ),
        "related": ["runway", "p-and-l"],
    },
    "runway": {
        "term": "Runway",
        "topic": "Business",
        "def": "How many months of cash you have left before you run out. Your oxygen.",
        "explain": (
            "Runway = cash-on-hand ÷ monthly burn. It's the simplest calculation in startup finance "
            "and the one you should know cold at all times. Healthy runway is 18+ months; you have "
            "time to experiment and build. Tight runway is under 6 months; every decision is about "
            "survival."
        ),
        "example": (
            "With $3M in the bank and $300k/month burn, runway is 10 months. If you can reduce burn "
            "to $200k/month, runway becomes 15 months. Conversely, if a bad decision adds $100k/month "
            "in costs, runway drops to 7.5 months, same cash, much less time."
        ),
        "why": (
            "Runway is the clock every startup lives by. You want to either reach profitability or "
            "raise your next round with at least 6 months still on the clock. Everything that isn't "
            "on the critical path of doing that is a distraction."
        ),
        "related": ["burn-rate", "p-and-l"],
    },
    "p-and-l": {
        "term": "P&L (Profit and Loss)",
        "topic": "Business",
        "def": "The statement showing revenue minus costs for a period. Are you making money or losing it?",
        "explain": (
            "The P&L (also called 'income statement') is one of the three basic financial statements. "
            "It shows: revenue, minus cost of goods, equals gross profit; minus operating expenses, "
            "equals operating profit; minus taxes and interest, equals net profit. Monthly and annual "
            "P&Ls are how you know whether the business is healthy."
        ),
        "example": (
            "Month's revenue: $100k. Cost of delivering that revenue: $30k (gross profit: $70k). "
            "Operating costs (salaries, rent, software): $50k (operating profit: $20k). Taxes: $5k. "
            "Net profit: $15k. That's a simple monthly P&L."
        ),
        "why": (
            "If you run a business, you should be able to read your own P&L without help. Most owners "
            "can't, which is why they make bad decisions. Spend the time to understand every line. "
            "The story of your business is in the P&L."
        ),
        "related": ["burn-rate", "runway"],
    },

    # ===================== MARKETING =====================
    "cac": {
        "term": "CAC (Customer Acquisition Cost)",
        "topic": "Marketing",
        "def": "The total cost to acquire one new paying customer. All-in, including salaries.",
        "explain": (
            "CAC = (total sales + marketing spend) ÷ (new customers acquired). Most teams calculate it "
            "too narrowly, just ad spend, and then wonder why their CAC looks great but their business "
            "struggles. True CAC includes salaries, software, content, everything you spent on "
            "acquisition. The broader you count, the more honest the number."
        ),
        "example": (
            "Quarter: $500k on sales + marketing (ads, salaries, tools). 200 new customers. CAC = $2,500. "
            "Whether that's good or bad depends entirely on how much those customers are worth (see LTV)."
        ),
        "why": (
            "CAC is half of the unit economics equation. Paired with LTV, it tells you whether your "
            "business can grow profitably. Without knowing both, you're flying blind. Every growth "
            "decision should start by asking: what's this do to CAC?"
        ),
        "related": ["ltv", "ltv-cac-ratio", "payback-period", "roas"],
    },
    "ltv": {
        "term": "LTV (Lifetime Value)",
        "topic": "Marketing",
        "def": "The total revenue (or profit) a customer generates over the entire time they're a customer.",
        "explain": (
            "LTV is how much a customer is worth to you, forever. Simple calculation: average monthly "
            "revenue × average customer lifespan in months (or: revenue / churn rate). If customers "
            "pay $100/mo and stick around 24 months on average, LTV = $2,400. Sometimes calculated on "
            "revenue, sometimes on gross profit (margin-adjusted LTV is more honest)."
        ),
        "example": (
            "Your SaaS: $100/mo revenue per customer, 3% monthly churn (so ~33-month average lifetime). "
            "LTV = $3,300 revenue, or ~$2,500 gross profit at 75% margins. That's how much you can "
            "afford to spend acquiring a customer."
        ),
        "why": (
            "LTV is the ceiling on what you can spend to get a customer. Spend more than LTV and you "
            "lose money on every sale. High-LTV businesses can afford aggressive acquisition; low-LTV "
            "businesses can't. This is the core math of customer-based businesses."
        ),
        "related": ["cac", "ltv-cac-ratio", "retention", "churn"],
    },
    "ltv-cac-ratio": {
        "term": "LTV:CAC Ratio",
        "topic": "Marketing",
        "def": "How many dollars of customer lifetime value you get per dollar of acquisition cost.",
        "explain": (
            "LTV:CAC = lifetime value ÷ customer acquisition cost. The single most important ratio in "
            "marketing. Under 1:1, you're losing money on every customer, unsustainable. 1:1 to 3:1 is "
            "survive mode. 3:1+ is healthy. 5:1+ you have a machine, pour fuel in. Above 8:1 you're "
            "probably under-investing in growth and should spend more."
        ),
        "example": (
            "LTV $3,000, CAC $1,000 → 3:1. That's the classic 'healthy SaaS' benchmark. LTV $500, CAC "
            "$300 → 1.67:1. That's tight, one bad quarter eats the margin. LTV $10k, CAC $800 → 12.5:1. "
            "Spend more; you can afford it."
        ),
        "why": (
            "This ratio tells you whether your business model works at all. Track it quarterly. If it's "
            "drifting down, either CAC is creeping up or retention is slipping. Both matter; both are "
            "fixable. Don't pretend the number doesn't exist."
        ),
        "related": ["cac", "ltv", "payback-period"],
    },
    "payback-period": {
        "term": "Payback Period",
        "topic": "Marketing",
        "def": "How long it takes a customer to 'pay back' what you spent to acquire them.",
        "explain": (
            "Payback = CAC ÷ monthly gross profit per customer. Tells you how many months of customer "
            "payments you need before you recover the cost of acquiring them. Shorter = better. Under "
            "12 months is healthy SaaS. Under 6 is elite. Over 18 is a warning sign, because it means "
            "you're fronting a lot of cash per new customer."
        ),
        "example": (
            "CAC $1,200. Monthly gross profit per customer $100. Payback = 12 months. Every customer "
            "costs you $1,200 upfront and makes you whole after a year. If your payback is longer than "
            "your average customer lifetime, your business is structurally unprofitable."
        ),
        "why": (
            "Payback period is how you manage the cash impact of growth. Even if LTV:CAC is great, a "
            "long payback means you need a LOT of cash to grow (because you're always ahead on "
            "acquisition costs). Shorten payback by raising price, lowering CAC, or moving to annual billing."
        ),
        "related": ["cac", "ltv", "ltv-cac-ratio"],
    },
    "roas": {
        "term": "ROAS (Return on Ad Spend)",
        "topic": "Marketing",
        "def": "Revenue generated per dollar of ad spend. The classic ad-accountability metric.",
        "explain": (
            "ROAS = revenue attributed to ads ÷ ad spend. If you spent $10k on Meta ads and attributed "
            "$30k of revenue to them, ROAS = 3. Paid-advertising teams live by this number. But revenue "
            "isn't profit, so ROAS can mislead. A 3x ROAS on a 20%-margin product means you're losing money."
        ),
        "example": (
            "Spend $5k on Google ads. 500 clicks. 20 sales at $100 each = $2,000 revenue. ROAS = 0.4, "
            "losing money. Spend $5k on a different campaign, same 20 sales at $500 each = $10,000 "
            "revenue. ROAS = 2. The second is better, same customers, better price."
        ),
        "why": (
            "ROAS is the standard unit for talking about ad performance. Know your target ROAS (usually "
            "3-5x for mid-margin businesses) and optimize campaigns against it. But ALWAYS cross-check "
            "against CAC, LTV, and margin, ROAS alone can make a losing business look great."
        ),
        "related": ["cac", "mer", "cpa", "conversion-rate"],
    },
    "mer": {
        "term": "MER (Marketing Efficiency Ratio)",
        "topic": "Marketing",
        "def": "Total revenue ÷ total marketing spend. ROAS but honest.",
        "explain": (
            "MER is ROAS computed across all marketing, not just attributed to specific channels. "
            "It includes revenue that wouldn't show up in any channel's ROAS (organic, word of mouth, "
            "branded search driven by ads). For holistic marketing performance, MER tells the truth "
            "while per-channel ROAS double-counts or misses things."
        ),
        "example": (
            "Month: $200k total marketing spend across ads, content, influencer, everything. $800k "
            "total revenue that month. MER = 4. That's your honest marketing-to-revenue efficiency "
            "at the business level, independent of attribution quirks."
        ),
        "why": (
            "ROAS by channel often lies (multi-touch attribution is hard). MER is harder to game, "
            "it's just total spend versus total revenue. Trend MER over time; it shows whether "
            "marketing is actually improving at the business level, not just in one dashboard."
        ),
        "related": ["roas", "attribution", "cac"],
    },
    "cpa": {
        "term": "CPA (Cost Per Acquisition)",
        "topic": "Marketing",
        "def": "What you paid for one conversion, whatever 'conversion' you defined.",
        "explain": (
            "CPA is ad spend divided by conversions. The conversion definition matters: CPA for a lead "
            "is different from CPA for a paying customer is different from CPA for a trial signup. Be "
            "specific about what 'acquisition' means. Often used interchangeably with CAC, but strictly "
            "CPA is per-conversion (any conversion event) while CAC is specifically per-customer."
        ),
        "example": (
            "Ran a campaign. Spent $5k. Got 200 email signups. CPA for signup = $25. Of those, 20 "
            "became paying customers. CAC (per customer) = $250. Both metrics matter, the ratio "
            "between them tells you about your funnel conversion."
        ),
        "why": (
            "CPA is useful at the campaign level when you're optimizing top-of-funnel. Compare CPA "
            "across campaigns to find the cheapest source of leads. But never optimize CPA without "
            "checking whether those leads convert to customers downstream."
        ),
        "related": ["cac", "cpc", "cpm", "conversion-rate"],
    },
    "cpc": {
        "term": "CPC (Cost Per Click)",
        "topic": "Marketing",
        "def": "What you pay for one ad click. The most basic paid-traffic metric.",
        "explain": (
            "CPC = ad spend ÷ clicks. Depends on platform, competition, and targeting. Search ads "
            "(Google) run $1-$20 CPC depending on keyword. Social ads (Meta, TikTok) run $0.30-$3 "
            "typical. Display is $0.10-$1. CPC isn't the goal, it's a lever. A cheap CPC on bad "
            "traffic is worse than an expensive CPC on great traffic."
        ),
        "example": (
            "Google keyword 'bankruptcy lawyer NYC': $40+ CPC. Facebook ad targeting 'dads who like "
            "grilling': $1 CPC. Both can be good investments, depending on what those clicks convert to."
        ),
        "why": (
            "Know your CPC per channel so you can reason about scale. But don't obsess over it; the "
            "real questions are CAC and ROAS. Cheap clicks that don't convert are worse than expensive "
            "clicks that do."
        ),
        "related": ["cpa", "cpm", "ctr"],
    },
    "cpm": {
        "term": "CPM (Cost Per Mille)",
        "topic": "Marketing",
        "def": "Cost per 1,000 ad impressions. How much you pay for reach, regardless of clicks.",
        "explain": (
            "CPM = ad spend ÷ (impressions / 1,000). Pronounced 'CPM' (the M is Latin 'mille' for "
            "thousand). It's how much you pay for 1,000 people to see your ad. Different platforms "
            "have very different CPMs: Google $5-20, Facebook $5-15, TikTok $2-10, LinkedIn $20-60+. "
            "CPM matters for brand campaigns and for comparing platforms' raw cost."
        ),
        "example": (
            "Spent $500 on Facebook, got 50,000 impressions. CPM = $10. Spent $1,000 on LinkedIn, got "
            "25,000 impressions. CPM = $40. LinkedIn is 4x more expensive per view, but maybe the "
            "audience is 4x more valuable for your B2B product."
        ),
        "why": (
            "CPM is the cost floor of any ad campaign. For direct-response campaigns, CPM is secondary, "
            "you care about downstream conversion. For brand campaigns, CPM is primary, you're buying "
            "attention, and cost-per-attention is the metric."
        ),
        "related": ["cpc", "cpa", "ctr"],
    },
    "ctr": {
        "term": "CTR (Click-Through Rate)",
        "topic": "Marketing",
        "def": "The % of people who saw your ad/email/link and clicked. A measure of how interesting your headline was.",
        "explain": (
            "CTR = (clicks ÷ impressions) × 100%. For ads, 1-3% is typical, 5%+ is great. For emails, "
            "2-10% is normal, 15%+ is excellent. CTR tests your creative: is the headline + image + "
            "CTA compelling? Low CTR means something about your ad isn't working, wrong audience, "
            "wrong hook, wrong copy, or boring creative."
        ),
        "example": (
            "Facebook ad: 10,000 impressions, 150 clicks. CTR = 1.5%. Above average. If CTR is 0.3%, "
            "the ad isn't doing its job, rewrite it before spending more. If CTR is 6%, scale."
        ),
        "why": (
            "CTR is a proxy for headline/hook quality. You can improve it dramatically with better "
            "creative. And higher CTR usually means lower CPC (platforms reward good ads with cheaper "
            "distribution). Fix CTR first, then worry about conversion."
        ),
        "related": ["cpc", "cpm", "conversion-rate"],
    },
    "conversion": {
        "term": "Conversion",
        "topic": "Marketing",
        "def": "Any moment where someone does the thing you wanted them to do.",
        "explain": (
            "A 'conversion' is any goal action: a purchase, a signup, a download, a form submission, a "
            "call booked. What counts as a conversion depends on the funnel stage. An ad-level "
            "conversion might be 'clicked and landed on the page.' A funnel conversion is 'submitted "
            "the form.' A business conversion is 'became a paying customer.' Be specific about which."
        ),
        "example": (
            "A Facebook ad's conversion = 100 people clicked, 15 submitted the form, 3 bought. Three "
            "conversion events, three different conversion rates. When someone says 'what's our "
            "conversion rate?', clarify WHICH conversion they mean."
        ),
        "why": (
            "Being sloppy about which conversion you're measuring leads to sloppy marketing decisions. "
            "Every dashboard should label the conversion event explicitly. 'Conversion rate = 2%' is "
            "meaningless without knowing the numerator and denominator."
        ),
        "related": ["conversion-rate", "cta", "funnel"],
    },
    "conversion-rate": {
        "term": "Conversion Rate",
        "topic": "Marketing",
        "def": "The % of people at one stage who move to the next stage.",
        "explain": (
            "Conversion rate = (conversions ÷ visitors or sessions) × 100%. Every step in your funnel "
            "has one. Homepage to pricing page: 20%. Pricing to checkout: 15%. Checkout to purchase: "
            "60%. These multiply: 20% × 15% × 60% = 1.8% overall conversion (homepage to paid). "
            "Where the funnel drops the steepest is where to improve."
        ),
        "example": (
            "E-commerce site: 10,000 visitors, 250 purchases. Overall conversion = 2.5%. Industry "
            "average is 2-3%, so roughly on track. Finding one step in the funnel that drops 80% is "
            "your highest-leverage optimization."
        ),
        "why": (
            "Improving conversion is often cheaper than increasing traffic. Doubling conversion = "
            "doubling customers at the same ad spend. CRO (conversion rate optimization) as a "
            "discipline exists for this reason."
        ),
        "related": ["conversion", "cro", "funnel"],
    },
    "cro": {
        "term": "CRO (Conversion Rate Optimization)",
        "topic": "Marketing",
        "def": "The practice of making more of your traffic convert into customers.",
        "explain": (
            "CRO is systematic experimentation on your site, funnel, and copy to lift conversion rates. "
            "It's research (what are users stuck on?) plus testing (A/B tests, multivariate tests) plus "
            "iteration. A CRO team might test headlines, button colors, form lengths, checkout flows, "
            "anything that might impact the conversion rate."
        ),
        "example": (
            "Your checkout converts at 60%. A CRO team finds the address form is too long, tests a "
            "simplified version, and lifts checkout conversion to 72%. That's a 20% lift on the last "
            "step of the funnel, meaningful."
        ),
        "why": (
            "CRO is usually the cheapest path to more revenue. You already have traffic; you already "
            "have a product; improving conversion is pure upside. Established businesses should have "
            "CRO as a standing function, not a project."
        ),
        "related": ["conversion-rate", "ab-test", "funnel"],
    },
    "ab-test": {
        "term": "A/B Test",
        "topic": "Marketing",
        "def": "A controlled experiment: half the visitors see A, half see B, measure which wins.",
        "explain": (
            "A/B testing (also called split testing) is how you know if a change actually worked. You "
            "randomly split traffic: 50% see the original (A), 50% see the variant (B). Same period, "
            "same audience, different experience. Whichever has the higher conversion rate (above a "
            "statistical threshold) wins. Without this, you're guessing."
        ),
        "example": (
            "Test: current button text 'Sign Up' (A) vs new text 'Start Free Trial' (B). Run for two "
            "weeks. A converts at 4.2%, B at 5.1%. B wins by 21%; that's significant over enough "
            "visitors. Ship B as the new default. Design the next test."
        ),
        "why": (
            "Intuition about what will convert is usually wrong. A/B testing replaces opinion with "
            "evidence. But: you need enough traffic to reach statistical significance (usually "
            "thousands of visitors per variant), and you can only test so many things at once. "
            "Prioritize tests by potential impact."
        ),
        "related": ["cro", "conversion-rate"],
    },
    "funnel": {
        "term": "Funnel",
        "topic": "Marketing",
        "def": "The step-by-step path a visitor takes from first contact to purchase.",
        "explain": (
            "The funnel is the sequence of stages a prospect moves through: awareness → interest → "
            "consideration → purchase → retention. Each stage has more people at the top than at "
            "the next stage, which is why it looks like a funnel. The gap between each stage is a "
            "conversion rate. Understanding your funnel is the foundation of most marketing work."
        ),
        "example": (
            "SaaS funnel: 10,000 visit the site. 500 sign up for the free trial. 100 become paying "
            "customers. 80 stay after 3 months. Stage conversions: 5%, 20%, 80%. The biggest leak is "
            "visit-to-trial (only 5%)-that's where to spend your CRO effort."
        ),
        "why": (
            "Every marketing decision happens inside a funnel. Knowing where your funnel leaks tells "
            "you what to fix next. Most teams don't map their funnel carefully, so they optimize the "
            "wrong steps. Start by mapping yours end-to-end before touching anything."
        ),
        "related": ["conversion-rate", "cro", "lead-gen"],
    },
    "icp": {
        "term": "ICP (Ideal Customer Profile)",
        "topic": "Marketing",
        "def": "A precise description of the company or person you most want as a customer.",
        "explain": (
            "The ICP is who you sell to, ideally. For B2B: industry, company size, role of the buyer, "
            "tech stack, signals that suggest they need you. For B2C: demographics, psychographics, "
            "behaviors, life stage. A good ICP is specific enough that you can look at any account and "
            "say 'in ICP' or 'out of ICP.' A vague ICP is a sign you haven't figured out who you sell to."
        ),
        "example": (
            "B2B ICP: 'SaaS companies, 20-200 employees, engineering-led, using Jira + GitHub, VP of "
            "Engineering is the buyer.' That's specific. You can target LinkedIn campaigns against it, "
            "score inbound leads against it, train your sales team against it."
        ),
        "why": (
            "Every hour spent marketing to non-ICP customers is wasted. Narrowing your ICP feels scary "
            "('we'll miss people!'), but it focuses your spend, sharpens your messaging, and shortens "
            "your sales cycle. Bigger target isn't better; more-right target is better."
        ),
        "related": ["persona", "prospecting", "lead-gen"],
    },
    "persona": {
        "term": "Persona",
        "topic": "Marketing",
        "def": "A fictional but grounded portrait of one type of ICP customer.",
        "explain": (
            "A persona is a character sketch of a real buyer type: what they do, what they care about, "
            "what they struggle with, where they hang out. It's not the ICP itself (which is the "
            "segment); it's one archetypal person in that segment. Named, backstoried, and memorable "
            "enough that your team can reference them."
        ),
        "example": (
            "ICP: VP of Eng at a SaaS company. Persona: 'Skeptical Sam', 38, been burned by bad "
            "tooling, cares about his team's velocity, reads Hacker News every morning, hates "
            "enterprise sales calls. Your copy writes for Sam; your product pitch addresses Sam's "
            "worries."
        ),
        "why": (
            "Personas make your ICP concrete. Instead of marketing to 'VPs of Engineering,' you're "
            "marketing to Sam. That specificity shapes copy, product decisions, even pricing. Without "
            "personas, marketing stays abstract and bland."
        ),
        "related": ["icp", "copywriting"],
    },
    "pmf": {
        "term": "PMF (Product-Market Fit)",
        "topic": "Marketing",
        "def": "The moment when your product clearly solves a problem people will pay to solve, repeatedly.",
        "explain": (
            "PMF is a binary: you have it or you don't. It's not '80% of the way there.' You know you "
            "have PMF when customers retain and expand without convincing, when they refer friends "
            "without prompting, when you can't keep up with demand. Until then, you're still searching. "
            "Companies often raise on 'traction' that isn't PMF yet and then get punished later."
        ),
        "example": (
            "Pre-PMF: churn is 15% monthly, most marketing dollars don't pay back. Post-PMF: churn "
            "drops to 3%, word of mouth drives 40% of new signups, the team can't process all the "
            "inbound. That's the feel of crossing the line."
        ),
        "why": (
            "Trying to scale a business without PMF is like pouring water into a bucket with a hole. "
            "Find PMF first; then add fuel. This sequencing is one of the most violated rules in "
            "startup-land."
        ),
        "related": ["retention", "churn", "icp"],
    },
    "attribution": {
        "term": "Attribution",
        "topic": "Marketing",
        "def": "The act of deciding which channel/touchpoint deserves credit for a conversion.",
        "explain": (
            "A customer sees your Facebook ad, searches Google, clicks an organic result, reads a "
            "blog, gets a retargeting ad, and finally buys. Which channel deserves credit? That's the "
            "attribution problem. Common models: first-touch (FB ad gets credit), last-touch "
            "(retargeting gets credit), linear (all equal), time-decay, position-based, and "
            "data-driven. Every model is wrong in some way."
        ),
        "example": (
            "Revenue of $1M. Last-touch attribution: Facebook 20%, Google ads 35%, email 25%, "
            "organic 20%. First-touch shows a totally different story: organic 40%, FB 30%, email "
            "15%, Google 15%. Same data, different slicing. Reality is somewhere in between."
        ),
        "why": (
            "Attribution tells you where to invest. Under-investing in early-funnel channels (because "
            "last-touch undercounts them) is the most common attribution mistake. Cross-check "
            "attribution models; use MER as the reality check; don't bet the business on one dashboard's view."
        ),
        "related": ["mer", "roas", "mmm", "incrementality"],
    },
    "mmm": {
        "term": "MMM (Marketing Mix Modeling)",
        "topic": "Marketing",
        "def": "A statistical technique to measure the impact of each marketing channel on revenue, without cookies.",
        "explain": (
            "MMM uses historical data, typically weekly or monthly spend and revenue, to statistically "
            "tease out how much each channel contributed. It doesn't rely on user tracking (which "
            "breaks in a privacy-focused world). Outputs: contribution curves, saturation points, and "
            "cross-channel effects. Good MMM tells you how much more revenue you'd get from an extra "
            "$100k in each channel."
        ),
        "example": (
            "MMM reveals: Facebook saturates around $50k/week (diminishing returns past that), Google "
            "still has room up to $100k/week, and podcast ads take 6 weeks to show impact. You "
            "rebalance spend based on the curves, not on last-touch attribution."
        ),
        "why": (
            "In a cookie-less, privacy-first world, click-level attribution is dying. MMM is making a "
            "comeback. It's expensive to do well (usually needs a data science team or an agency), but "
            "for businesses with real spend it's worth it."
        ),
        "related": ["attribution", "mer", "incrementality"],
    },
    "incrementality": {
        "term": "Incrementality",
        "topic": "Marketing",
        "def": "Did this marketing actually cause the sale? Or would the customer have bought anyway?",
        "explain": (
            "Incrementality asks the counterfactual question: if we hadn't run this campaign, would "
            "these sales still have happened? Because a lot of what attribution calls 'conversions' "
            "would've happened anyway. Retargeting ads 'attributed' to a sale that was already going "
            "to close are a classic case. You're just getting credit for inevitability."
        ),
        "example": (
            "Turn off brand search ads for two weeks. If revenue from branded terms drops 5%, that's "
            "the incremental contribution. The other 95% would have happened organically (customers "
            "typing your name into Google). You just saved 95% of that ad spend."
        ),
        "why": (
            "Incrementality is the honest question. Attribution often credits channels that aren't "
            "actually driving anything. Geo-holdout tests, randomized experiments, and MMM are ways "
            "to measure it. The truth is usually: you can cut 20-40% of ad spend without losing "
            "revenue."
        ),
        "related": ["attribution", "mmm", "roas"],
    },
    "utm": {
        "term": "UTM",
        "topic": "Marketing",
        "def": "URL parameters that track where a click came from. The plumbing of attribution.",
        "explain": (
            "UTMs (Urchin Tracking Module tags) are query parameters on URLs: "
            "<code>?utm_source=facebook&amp;utm_medium=cpc&amp;utm_campaign=winter-promo</code>. "
            "They let your analytics tool (Google Analytics, whatever) know where each visitor came "
            "from. Without UTMs, all paid traffic looks like 'referral from facebook.com' and you "
            "can't tell which campaign drove what."
        ),
        "example": (
            "Link in a LinkedIn ad: <code>yoursite.com/?utm_source=linkedin&amp;utm_medium=paid&amp;"
            "utm_campaign=q4-enterprise</code>. When someone clicks, your analytics knows 'this visit "
            "came from the q4-enterprise LinkedIn campaign.' Now ROAS, CPA, etc. can be computed per campaign."
        ),
        "why": (
            "Consistent UTM hygiene is non-negotiable for data-driven marketing. Every link in every "
            "campaign, every email, every social post, should have UTMs. Pick a naming convention and "
            "enforce it. Without UTMs, your attribution data is garbage."
        ),
        "related": ["attribution", "conversion"],
    },
    "prospecting": {
        "term": "Prospecting",
        "topic": "Marketing",
        "def": "The act of finding new potential customers and reaching out to them.",
        "explain": (
            "Prospecting is the top of the outbound funnel: researching accounts, finding contacts, "
            "crafting personalized outreach, sending cold emails or making cold calls. It's the "
            "'manufacturing' of pipeline when you don't have enough inbound yet. Prospecting is a "
            "numbers game AND a craft; doing it well means high response rates AND high volume."
        ),
        "example": (
            "SDR works a list of 200 target accounts. Researches each: who's the buyer, what's their "
            "problem, why would they care about your product. Writes 3-email sequences personalized "
            "per account. Sends 50/day. 5% reply. 1% book a demo. That's prospecting."
        ),
        "why": (
            "When you need pipeline now, prospecting is the faucet. Content marketing and SEO are "
            "slow; prospecting is fast. Most successful B2B companies run both, but early-stage "
            "companies lean heavily on prospecting while brand builds."
        ),
        "related": ["lead-gen", "icp", "cold-email", "outbound"],
    },
    "retargeting": {
        "term": "Retargeting",
        "topic": "Marketing",
        "def": "Ads shown to people who've already interacted with your brand. Following them around the internet.",
        "explain": (
            "Retargeting shows ads specifically to people who've visited your site, watched your "
            "video, or otherwise engaged. They're already somewhat aware, so they convert much higher "
            "than cold audiences. The cost: they can feel 'stalker-y' if overdone. Smart retargeting "
            "is frequency-capped and segmented (different messages for different funnel stages)."
        ),
        "example": (
            "Someone visits your pricing page and leaves. 24 hours later, they see your ad on Facebook "
            "saying 'Still thinking about it? Here's what 100 customers said about month one.' That's "
            "retargeting."
        ),
        "why": (
            "Retargeting typically has the best ROAS of any paid channel, because you're spending on "
            "people who are already warm. But it's a closing tool, not an acquisition tool; it can't "
            "grow the funnel, only convert what's already there. Balance with acquisition channels."
        ),
        "related": ["roas", "conversion-rate", "funnel"],
    },
    "lookalike": {
        "term": "Lookalike Audience",
        "topic": "Marketing",
        "def": "An audience built from people similar to your existing customers, used for ad targeting.",
        "explain": (
            "Lookalikes (on Meta, TikTok, Google) are generated by an algorithm: you give it a seed "
            "list (your customers, or high-value segments within them), and it finds people who look "
            "similar based on behavior, interests, and demographics. Lookalikes usually outperform "
            "interest-based targeting because they're built from signal, not guesses."
        ),
        "example": (
            "Upload a list of your top 1,000 customers to Facebook. It builds a 2M-person lookalike. "
            "You target your ads at the lookalike. Typical result: 2-3x better ROAS than targeting "
            "generic interests like 'small business owners.'"
        ),
        "why": (
            "Lookalikes scale what's already working. The best use: feed them your most-valuable "
            "customers (not all customers, your HIGH-LTV ones), and scale against that specific "
            "segment. The quality of your seed determines the quality of your lookalike."
        ),
        "related": ["icp", "cac", "roas"],
    },

    # ===================== SALES =====================
    "sdr": {
        "term": "SDR (Sales Development Representative)",
        "topic": "Sales",
        "def": "The salesperson who finds and qualifies leads, then hands them to an AE for closing.",
        "explain": (
            "SDRs do prospecting: researching accounts, sending cold outreach, making discovery calls, "
            "qualifying leads. They don't close deals themselves. They hand qualified opportunities to "
            "an AE (Account Executive), who takes over. The split exists because prospecting and "
            "closing are very different skills, one is volume + persistence, the other is deal "
            "shaping + relationship."
        ),
        "example": (
            "100 accounts in an SDR's weekly queue. They send 500 outbound emails and calls. 20 "
            "respond; 8 agree to an intro call; 3 become qualified opportunities. Those 3 go to AEs. "
            "The SDR's quota is meetings booked, not revenue closed."
        ),
        "why": (
            "The SDR-AE split is the backbone of B2B sales for deals over $10-20k. If your deals are "
            "smaller, self-service might beat SDRs. If larger, you probably want BDRs (outbound SDRs) "
            "AND inbound SDRs AND AEs, a small sales org already."
        ),
        "related": ["ae", "prospecting", "pipeline", "discovery-call"],
    },
    "ae": {
        "term": "AE (Account Executive)",
        "topic": "Sales",
        "def": "The salesperson who takes qualified leads and closes them. The closer.",
        "explain": (
            "The AE owns the deal from qualification to close. They run demos, do discovery, write "
            "proposals, handle objections, negotiate terms, get the contract signed. Their quota is "
            "revenue (not meetings). They usually work a handful of deals at a time, each in some "
            "stage of the pipeline."
        ),
        "example": (
            "AE's pipeline: 15 active deals, average size $50k, total ARR potential $750k. Quarterly "
            "quota: $250k in closed revenue. They work each deal via discovery calls, demos, "
            "proposals, stakeholder mapping, and closing. A few close; some slip; some die."
        ),
        "why": (
            "AEs are the revenue engine. Strong AE → close rate above ~25% on qualified pipeline. "
            "Weak AE → pipeline gets stuck. Most early-stage companies put their founder in this role "
            "until they hit enough volume to hire a real AE."
        ),
        "related": ["sdr", "pipeline", "discovery-call", "meddic", "quota"],
    },
    "pipeline": {
        "term": "Pipeline",
        "topic": "Sales",
        "def": "All the deals currently being worked, at various stages, with total dollar value.",
        "explain": (
            "Pipeline is the forward view of revenue. It's the sum of all active deals × their stage "
            "probability. A well-qualified pipeline lets you forecast next quarter with reasonable "
            "accuracy. A bad pipeline (full of stale deals or unqualified opportunities) produces "
            "misses. Good sales leadership spends more time on pipeline health than on any other metric."
        ),
        "example": (
            "Q4 pipeline: $3M total deal value. Broken into stages: $400k in discovery (10% close rate), "
            "$800k in demo (30%), $900k in proposal (50%), $400k in negotiation (75%), $500k committed "
            "(90%). Weighted pipeline: about $1.2M. You need 3-4x your quota in raw pipeline to forecast reliably."
        ),
        "why": (
            "Pipeline is how you see the future. If pipeline coverage is 1.5x quota, you're almost "
            "certainly going to miss. If it's 5x, you're probably fine but inefficient. Healthy is "
            "3-4x quota, with fresh inflow each week."
        ),
        "related": ["ae", "sdr", "forecast", "quota"],
    },
    "forecast": {
        "term": "Forecast",
        "topic": "Sales",
        "def": "Sales' prediction of how much revenue will close in a given period.",
        "explain": (
            "Forecasting is the practice of calling which deals will close this quarter and totaling "
            "them up. AEs forecast their own deals (often categorized: 'commit', 'best case', 'pipeline'), "
            "managers roll those up, and leadership gets a number. Good forecasting is ±5%. Bad "
            "forecasting is ±30%, and it destroys trust with the board."
        ),
        "example": (
            "Q3 forecast call: VP Sales tells CEO 'we'll hit $1.8M against a $2M quota.' If actual "
            "is $1.78M, that's accurate forecasting. If actual is $1.2M, the forecast was garbage "
            "and something's broken in the pipeline process."
        ),
        "why": (
            "Forecasting is how the company plans cash, hiring, and investor updates. If forecasts are "
            "unreliable, nothing else is. Good AEs and good managers forecast within a tight range "
            "and defend their calls with specifics. The rest guess."
        ),
        "related": ["pipeline", "quota", "ae"],
    },
    "quota": {
        "term": "Quota",
        "topic": "Sales",
        "def": "The revenue number a salesperson is expected to close in a period. Their target.",
        "explain": (
            "Quotas are set annually (sometimes quarterly), broken into monthly/quarterly chunks, and "
            "tracked obsessively. Typical quota is 4-6x the AE's fully-loaded cost, so a $150k/yr AE "
            "has a quota around $750k-$1M. Hitting quota triggers variable compensation (bonus + "
            "commission); missing it starts a performance conversation."
        ),
        "example": (
            "AE annual quota: $1M. Quarterly breakdown: $200k Q1, $250k Q2, $275k Q3, $275k Q4 "
            "(weighted toward end-of-year to match selling rhythm). Hit 100%, earn full OTE. Hit 120%+, "
            "earn accelerators (higher commission rate on the overage)."
        ),
        "why": (
            "Quota is the forcing function in sales. It aligns individual effort with company targets. "
            "Setting quotas too high demotivates; too low and you're paying bonuses for mediocre "
            "performance. Good sales leaders calibrate quotas annually against actual historical data."
        ),
        "related": ["ote", "pipeline", "forecast"],
    },
    "ote": {
        "term": "OTE (On-Target Earnings)",
        "topic": "Sales",
        "def": "The total compensation a salesperson earns if they hit 100% of quota.",
        "explain": (
            "OTE is base salary + target variable comp (bonus + commission) at 100% quota attainment. "
            "Typical split is 50/50 for AEs (half base, half variable), 60/40 for SDRs. Exceeding "
            "quota means earning above OTE, often with accelerated commission rates. Missing quota "
            "means earning below OTE, sometimes way below."
        ),
        "example": (
            "AE with $180k OTE: $90k base + $90k variable (at 100% quota attainment on $1M quota). "
            "Hit 120% of quota: base $90k + variable $90k + accelerated overage bonus = maybe $200k+ total. "
            "Miss at 70%: $90k base + $63k variable = $153k total."
        ),
        "why": (
            "OTE is how you recruit salespeople. It's the number candidates quote to each other. "
            "'I'm a $250k OTE AE' means something specific. Know the OTE range for your type of role "
            "at competitive companies; if you're below market, you won't hire well."
        ),
        "related": ["quota", "ae"],
    },
    "meddic": {
        "term": "MEDDIC",
        "topic": "Sales",
        "def": "A qualification framework for B2B deals: Metrics, Economic buyer, Decision criteria, Decision process, Identify pain, Champion.",
        "explain": (
            "MEDDIC is the checklist a good B2B AE runs through on every deal. Metrics: what measurable "
            "improvement does the customer expect? Economic buyer: who controls the budget? Decision "
            "criteria: what will drive their decision? Decision process: how does this company actually "
            "buy? Identify pain: what's broken and how badly? Champion: who inside the account is "
            "advocating for you?"
        ),
        "example": (
            "AE mid-deal: 'Metrics are clear (they want to cut onboarding time from 14 days to 3). "
            "Economic buyer is the VP Ops, I've met her. Decision criteria: price + security review. "
            "Decision process: legal review (2 weeks), procurement (1 week), signatures. Pain is real "
            "(their last solution broke and they're in crisis mode). Champion is the ops director, "
            "she's on every call and coaching us from inside.' That's a healthy deal."
        ),
        "why": (
            "Deals die because an AE thought they were further along than they were. MEDDIC forces "
            "specificity. Every missing letter is a risk. No identified champion? You'll lose. "
            "Unknown decision process? Expect surprises. Running MEDDIC on your pipeline monthly "
            "shows where deals are actually weak."
        ),
        "related": ["pipeline", "ae", "discovery-call"],
    },
    "discovery-call": {
        "term": "Discovery Call",
        "topic": "Sales",
        "def": "The first real sales conversation. The goal isn't to pitch, it's to understand.",
        "explain": (
            "A discovery call is 30-45 minutes of structured questions to understand the prospect's "
            "situation: what's their current state, what's broken, who's involved in the decision, "
            "what's the timeline, what's the budget. A good discovery call ends with clear next steps. "
            "A bad one ends with 'we'll think about it.'"
        ),
        "example": (
            "AE on discovery: 'Tell me about your current onboarding process. How long does it take? "
            "What breaks most often? Who's involved? Have you tried to solve this before, what happened? "
            "If we could cut that time in half, what would that be worth to you?' Note: no pitching yet. "
            "Just learning."
        ),
        "why": (
            "The single biggest AE mistake: pitching during discovery. Discovery is recon. Pitch "
            "comes in the next call, tailored to what you learned. An AE who pitches in the first "
            "call is saying 'I don't care about your situation, here's my thing anyway.' Customers "
            "feel that."
        ),
        "related": ["ae", "meddic", "pipeline"],
    },
    "inbound": {
        "term": "Inbound",
        "topic": "Sales",
        "def": "Leads that come TO you (via content, ads, referrals). The customer initiates.",
        "explain": (
            "Inbound is the opposite of outbound. Someone discovers you via content, search, social, "
            "a referral, an ad, and raises their hand: demo request, trial signup, pricing inquiry. "
            "They're self-qualified (they came to you; they have a real interest). Inbound leads "
            "typically close at higher rates than outbound but take longer to generate."
        ),
        "example": (
            "Marketing team publishes a blog post. It ranks on Google for 'best CRM for real estate.' "
            "200 visits per month land, 20 start a free trial, 4 become paying customers. That's pure "
            "inbound. The CAC is the content cost divided by the 4 customers, often much cheaper than "
            "outbound."
        ),
        "why": (
            "Inbound scales at a different shape than outbound. It's slower to start (content takes "
            "time to rank, brand takes time to build) but cheaper and more sustainable once working. "
            "Best companies have both: outbound for pipeline now, inbound for efficient growth over "
            "time."
        ),
        "related": ["outbound", "lead-gen", "sdr"],
    },
    "outbound": {
        "term": "Outbound",
        "topic": "Sales",
        "def": "Leads generated by you reaching out to them first. The seller initiates.",
        "explain": (
            "Outbound is cold outreach: cold emails, cold calls, LinkedIn DMs, direct mail. You "
            "target prospects who haven't asked to hear from you, but fit your ICP. Done well, it's "
            "a fast, controllable way to generate pipeline. Done poorly, it's spam that damages your "
            "brand. SDRs are often the outbound engine."
        ),
        "example": (
            "SDR targets 500 VPs of Engineering at mid-market SaaS companies. Personalized email "
            "referencing a recent hire or product launch. 5% reply. 1% book a demo. From 500 outbound: "
            "5 meetings. That's the volume math."
        ),
        "why": (
            "Outbound is how early-stage companies generate pipeline before they have content or "
            "brand. It's also how enterprise companies reach specific named accounts. Know when to "
            "use it: accounts too high-value to wait for inbound, ICP that doesn't hang out online, "
            "or you just need pipeline NOW."
        ),
        "related": ["inbound", "sdr", "prospecting", "lead-gen"],
    },

    # ===================== SEO =====================
    "seo": {
        "term": "SEO (Search Engine Optimization)",
        "topic": "SEO",
        "def": "The practice of ranking higher in Google's organic search results.",
        "explain": (
            "SEO is making your website show up when people search. It's a mix of technical ("
            "Google can crawl and understand your site), content ('the right' content to rank for "
            "your target keywords), and authority (other sites link to you, which Google reads as "
            "credibility). Organic traffic from SEO compounds, which makes it one of the most "
            "valuable long-term channels."
        ),
        "example": (
            "Plumbing company ranks #1 on Google for 'plumber near me' and '[their city] emergency "
            "plumber.' They get 500 organic visits a week from people actively looking to hire a "
            "plumber. That traffic is free (no per-click cost) and converts well because intent is high."
        ),
        "why": (
            "SEO is the cheapest customer acquisition channel once it's working, but it takes 6-18 "
            "months to build. Most local businesses and content sites should take SEO seriously as "
            "a long-term play. Ignoring it for short-term channels is a common regret."
        ),
        "related": ["keyword", "ranking", "backlink", "on-page-seo"],
    },
    "keyword": {
        "term": "Keyword",
        "topic": "SEO",
        "def": "A word or phrase people type into Google. The atomic unit of SEO.",
        "explain": (
            "Keywords are what users search for. Every SEO strategy starts with keyword research: "
            "what are potential customers typing, how many times per month, how competitive is each "
            "one? Keywords have 'intent' (informational, navigational, transactional, commercial), "
            "and the intent determines what kind of content ranks. 'How to fix a leaky faucet' wants "
            "a how-to. '[brand] review' wants a review."
        ),
        "example": (
            "A mattress company targets keywords like 'best mattress for back pain' (commercial intent, "
            "high-value) and 'memory foam vs spring mattress' (informational intent, top of funnel). "
            "Different content types for each."
        ),
        "why": (
            "Picking the wrong keywords is the #1 SEO failure mode. High-volume keywords are "
            "competitive; low-volume keywords don't drive traffic. The sweet spot is medium-volume "
            "keywords where you can realistically rank and where the users actually want what you sell."
        ),
        "related": ["search-volume", "keyword-difficulty", "ranking", "serp"],
    },
    "search-volume": {
        "term": "Search Volume",
        "topic": "SEO",
        "def": "The estimated number of times a keyword is searched on Google per month.",
        "explain": (
            "Search volume tells you how big an opportunity is. 'Insurance' has hundreds of thousands "
            "of searches per month; 'auto insurance Peoria' might have hundreds. Higher volume = more "
            "traffic potential, but usually also = more competition. Search volume numbers from tools "
            "(Ahrefs, SEMrush) are estimates; directional, not exact."
        ),
        "example": (
            "'Cold email' has ~40,000 global monthly searches. 'Cold email templates' has ~8,000. "
            "'Cold email open rate benchmarks' has ~500. Each represents a different keyword strategy "
            "(big pillar content vs specific how-to vs ultra-specific expert content)."
        ),
        "why": (
            "Without knowing search volume, you're guessing at opportunity size. Target keywords with "
            "enough volume to matter but not so much that you can't rank. The 500-5,000 monthly range "
            "is often the sweet spot for new sites."
        ),
        "related": ["keyword", "keyword-difficulty"],
    },
    "keyword-difficulty": {
        "term": "Keyword Difficulty",
        "topic": "SEO",
        "def": "How hard it is to rank on page 1 for a given keyword. Higher = harder.",
        "explain": (
            "Keyword difficulty (KD) is a 0-100 score estimating how competitive a keyword is. Tools "
            "(Ahrefs, SEMrush) calculate it from the strength of sites currently ranking. High KD = "
            "you'll need a strong site with lots of backlinks to compete. Low KD = even a new site "
            "can potentially rank with good content."
        ),
        "example": (
            "'Email marketing': KD 80. You won't rank without a year of work and strong backlinks. "
            "'Email marketing for dog trainers': KD 15. A well-written article on a fresh site has a "
            "real shot."
        ),
        "why": (
            "Targeting high-KD keywords on a new site is a waste of months. Start with lower-KD "
            "long-tail keywords and build authority. Graduate to harder keywords as your site earns "
            "trust (backlinks, time in index, topical depth). KD is how you know which keywords are "
            "in your reach."
        ),
        "related": ["keyword", "search-volume", "domain-rating"],
    },
    "serp": {
        "term": "SERP (Search Engine Results Page)",
        "topic": "SEO",
        "def": "The page Google shows after a search. Your target for ranking.",
        "explain": (
            "The SERP is what Google returns for a query: 10 organic results, plus ads, plus features "
            "(featured snippet, people also ask, knowledge panel, images, video, maps). Modern SERPs "
            "are packed with features that steal clicks from traditional results. Understanding the "
            "SERP for YOUR target keyword tells you what ranking really means (position 1 might still "
            "be below a featured snippet or ad pack)."
        ),
        "example": (
            "Search 'best CRM 2026': SERP shows ads at top, then a featured snippet (someone's "
            "bullet list), then People Also Ask box, then 10 organic results. Even ranking #1 might "
            "mean you're third on the page after ads and the featured snippet. That changes the math."
        ),
        "why": (
            "Before writing content for a keyword, look at the current SERP. What's ranking? What "
            "format? What angle? Your content has to be equal or better to have a chance. Don't write "
            "blind."
        ),
        "related": ["ranking", "featured-snippet", "keyword"],
    },
    "ranking": {
        "term": "Ranking",
        "topic": "SEO",
        "def": "Your position in Google's organic search results for a given keyword.",
        "explain": (
            "You either rank or you don't. Ranking position determines click-through: #1 gets "
            "~30% of clicks, #2 gets ~15%, #3 gets ~10%, and it falls off fast. Page 2 basically "
            "doesn't exist; fewer than 1% of searchers go there. Your ranking for a keyword is "
            "what determines whether SEO delivers traffic."
        ),
        "example": (
            "You rank #8 for 'project management software' (high volume). Traffic from that keyword: "
            "~2% CTR × 20,000 searches = 400 clicks. Move to #3 and it's more like 10% × 20,000 = "
            "2,000 clicks. Same keyword, 5x the traffic, from position alone."
        ),
        "why": (
            "Ranking is the goal. Track weekly. Know your top-ranking keywords and their trends. A "
            "drop from position 3 to 8 overnight is an emergency, not a 'we'll look into it' ticket."
        ),
        "related": ["serp", "keyword", "backlink"],
    },
    "backlink": {
        "term": "Backlink",
        "topic": "SEO",
        "def": "A link from another website to yours. Google treats it as a vote of confidence.",
        "explain": (
            "Backlinks remain one of the strongest ranking factors. Each backlink is a signal that "
            "someone else found your content valuable enough to link to. Quality matters more than "
            "quantity: one link from the New York Times is worth thousands from low-quality sites. "
            "Google's algorithm specifically weighs link quality, topical relevance, and the anchor text."
        ),
        "example": (
            "A marketing blog links to your article on email deliverability with the anchor text "
            "'great guide on deliverability.' Google sees: (1) a relevant site (2) endorsing your "
            "content (3) with a topical anchor. Your authority for deliverability-related keywords "
            "goes up."
        ),
        "why": (
            "Quality content alone rarely ranks in competitive niches; you need backlinks too. "
            "Building them (via outreach, digital PR, guest posts, being linkworthy) is half the job "
            "of SEO. Without a backlink strategy, you're leaving rankings on the table."
        ),
        "related": ["domain-rating", "ranking", "seo"],
    },
    "domain-rating": {
        "term": "Domain Rating (DR)",
        "topic": "SEO",
        "def": "A 0-100 score of a site's backlink authority. Higher = stronger in Google's eyes.",
        "explain": (
            "DR (Ahrefs) and DA (Moz) and equivalents are tools' estimates of a site's overall "
            "backlink strength. Not a Google metric, but a useful proxy. DR 0-20 = new or weak site. "
            "DR 40-60 = established. DR 70+ = authoritative. DR 90+ = NYT, Wikipedia, major publishers. "
            "Your DR determines how hard keywords you can realistically compete for."
        ),
        "example": (
            "Your site: DR 25. You're going to lose to sites at DR 60+ on competitive keywords unless "
            "your content is dramatically better. Focus on long-tail keywords where the top-ranking "
            "sites are DR 20-30 too. Climb from there."
        ),
        "why": (
            "DR is how you read the competitive landscape. Before writing content for a keyword, "
            "check the DR of sites currently ranking. If they're all 60+ and you're 25, pick a "
            "different keyword."
        ),
        "related": ["backlink", "keyword-difficulty", "ranking"],
    },
    "on-page-seo": {
        "term": "On-Page SEO",
        "topic": "SEO",
        "def": "The SEO factors you control on the page itself: title, headings, content, internal links.",
        "explain": (
            "On-page SEO is everything you can change in the HTML of a page: the title tag, meta "
            "description, headings (H1, H2, H3), body content, image alt text, internal links to other "
            "pages. These signal to Google what the page is about and how it should be understood. "
            "Good on-page = the basics most SEO is built on."
        ),
        "example": (
            "Page on 'email marketing benchmarks': H1 is 'Email Marketing Benchmarks 2026', title "
            "tag includes the phrase, H2s break it down (open rate, CTR, unsubscribe rate), images "
            "have descriptive alt text, and you internally link to your other email marketing articles. "
            "Solid on-page signals."
        ),
        "why": (
            "On-page is the cheapest part of SEO, you don't need external action, just editing. "
            "Most sites have significant on-page improvements available that would lift rankings "
            "by themselves. Audit yearly; fix weekly."
        ),
        "related": ["technical-seo", "keyword", "meta-description"],
    },
    "meta-description": {
        "term": "Meta Description",
        "topic": "SEO",
        "def": "The summary text Google shows below your page title in search results.",
        "explain": (
            "The meta description is a short HTML tag (<code>&lt;meta name=\"description\"&gt;</code>) "
            "that tells Google what the page is about. Google may or may not show it verbatim, but "
            "it often does. A good meta description is 150-160 characters, describes the page value, "
            "and includes the target keyword. It doesn't directly affect ranking, but it heavily "
            "affects click-through rate."
        ),
        "example": (
            "Bad: 'Page about email marketing.' Good: 'Discover the email marketing benchmarks for "
            "2026: open rates, CTRs, and conversion rates from 1M+ real sends. Free data.' The "
            "second one earns the click, even if it doesn't rank higher."
        ),
        "why": (
            "You spent months ranking on page 1. The meta description is whether anyone actually "
            "clicks. Treat it as ad copy for organic. Rewrite weak ones; test variants; improve "
            "CTR as a direct lift to traffic."
        ),
        "related": ["on-page-seo", "ctr", "serp"],
    },
    "schema": {
        "term": "Schema (Structured Data)",
        "topic": "SEO",
        "def": "Extra code on your page that tells Google exactly what type of content it is.",
        "explain": (
            "Schema markup (usually JSON-LD) tags your page so Google knows: this is an article, "
            "this is a product, this is a recipe, this is a review. Schema can unlock rich results: "
            "star ratings in search, recipe cards with cooking time, FAQ dropdowns right in the SERP. "
            "Doesn't directly boost rankings, but dramatically improves click-through when it earns a "
            "rich result."
        ),
        "example": (
            "Your recipe page has recipe schema with prep time, cook time, ratings. Google shows it "
            "with a photo, 4.5 stars, '45 min' visible in the SERP. Your CTR triples compared to a "
            "plain text result. Same ranking; much more traffic."
        ),
        "why": (
            "Schema is underused. Most sites don't implement it and leave rich results on the table. "
            "For any content type that can earn a rich result (articles, products, recipes, events, "
            "FAQs), add the schema. The effort is small; the SERP real estate boost is real."
        ),
        "related": ["on-page-seo", "serp", "featured-snippet"],
    },
    "featured-snippet": {
        "term": "Featured Snippet",
        "topic": "SEO",
        "def": "The answer box Google shows at the very top of some SERPs. 'Position zero.'",
        "explain": (
            "Featured snippets are short extracts (paragraph, list, or table) Google pulls from a page "
            "to directly answer a query. They appear above the regular #1 result, in a big box, and "
            "steal a lot of clicks from traditional rankings. Formatting content well (clear answer "
            "in the opening, lists where appropriate, tables for comparisons) can earn the snippet."
        ),
        "example": (
            "Search 'how long to cook salmon'. The featured snippet says: '4-6 minutes per side for "
            "medium, 8-10 minutes in a 400°F oven.' Pulled from someone's recipe page. That page gets "
            "huge CTR even without the #1 organic rank."
        ),
        "why": (
            "Featured snippets are some of the highest-CTR SERP real estate available. Structuring "
            "content to compete for them (clear question-and-answer formatting, lists, definition-"
            "style openers) is a high-leverage SEO practice."
        ),
        "related": ["serp", "schema", "on-page-seo"],
    },
    "technical-seo": {
        "term": "Technical SEO",
        "topic": "SEO",
        "def": "The under-the-hood SEO work: site speed, crawlability, structured data, architecture.",
        "explain": (
            "Technical SEO is the stuff your users don't see: can Google crawl your site efficiently? "
            "Do pages load fast on mobile? Are URLs clean? Is the sitemap up to date? Are you handling "
            "duplicate content correctly? It's the plumbing. When technical is solid, everything else "
            "works better. When technical is broken, content and backlinks can't compensate."
        ),
        "example": (
            "Audit reveals: 40% of pages have Core Web Vitals failures, sitemap is missing 200 new "
            "pages, and canonical tags are misconfigured causing duplicate-content issues. Fix those "
            "and ranking improves across the whole site, without changing the content itself."
        ),
        "why": (
            "Most sites have significant technical issues that silently cost them rankings. A "
            "technical audit every 6-12 months pays for itself. Site speed especially: slow sites "
            "don't rank well, full stop."
        ),
        "related": ["on-page-seo", "seo"],
    },
    "content-cluster": {
        "term": "Content Cluster (Topic Cluster)",
        "topic": "SEO",
        "def": "A group of related content pieces that together establish topical authority.",
        "explain": (
            "A content cluster is a pillar page (broad overview, targeting a big keyword) plus many "
            "related sub-pages (specific long-tail keywords within the topic) all interlinked. This "
            "pattern tells Google: 'we know this topic deeply, not just one page of it.' Clusters "
            "rank better than isolated articles, especially on competitive topics."
        ),
        "example": (
            "Pillar: 'The Complete Guide to Email Marketing' (broad, high-volume keyword). Sub-pages: "
            "'Email open rate benchmarks', 'Email subject line psychology', 'Email automation flows', "
            "'Email deliverability checklist'. All linked to each other and to the pillar. Google sees "
            "a topical authority."
        ),
        "why": (
            "Writing 30 pages on one topic works better than writing 30 pages on 30 random topics. "
            "Clusters compound. Pick a topic your business cares about, build a cluster over 6-12 "
            "months, and you own the category in search."
        ),
        "related": ["keyword", "on-page-seo", "seo"],
    },
    "local-seo": {
        "term": "Local SEO",
        "topic": "SEO",
        "def": "SEO focused on ranking for searches with local intent ('near me', city names).",
        "explain": (
            "Local SEO gets you found by people looking for a business in their area. It's different "
            "from regular SEO: it emphasizes Google Business Profile (your listing in Maps), reviews, "
            "local citations (directory listings with consistent name/address/phone), and location "
            "pages on your site. Critical for any business with a physical location."
        ),
        "example": (
            "Dentist in Austin wants to rank for 'dentist in Austin' and 'emergency dentist near me'. "
            "They claim their Google Business Profile, collect 50+ 5-star reviews, build listings on "
            "Yelp/Foursquare/etc, and publish location-specific content. They show up in the Map Pack "
            "(top 3 map results on local searches), which drives the bulk of foot traffic."
        ),
        "why": (
            "For local businesses, local SEO is more valuable than general SEO. The map pack at the "
            "top of local searches gets most clicks. Your Google Business Profile is arguably more "
            "important than your website for discovery."
        ),
        "related": ["google-business-profile", "seo", "ranking"],
    },
    "google-business-profile": {
        "term": "Google Business Profile",
        "topic": "SEO",
        "def": "Your free listing in Google Search and Maps. The most important asset for local businesses.",
        "explain": (
            "Google Business Profile (formerly Google My Business) is the listing that shows up for "
            "local searches: name, address, phone, hours, reviews, photos, posts. It's entirely free. "
            "You claim it, verify ownership, keep it updated. For brick-and-mortar businesses, a "
            "well-optimized GBP often drives more customers than the website does."
        ),
        "example": (
            "Search '[your city] plumber'. The top three results are map listings (the 'map pack'). "
            "Those three businesses get maybe 60% of all clicks. Ranking in the map pack comes from: "
            "proximity, review quality/volume, categorization, and profile completeness. GBP "
            "optimization is how you compete."
        ),
        "why": (
            "If you have a local business and haven't optimized your GBP, you're leaving most local "
            "customer discovery on the table. It's free. The payoff is immediate. Start here."
        ),
        "related": ["local-seo", "serp"],
    },
}

# -----------------------------------------------------------------------------
# Template + writer. Same as _rewrite_glossary_ai.py.
# -----------------------------------------------------------------------------
PAGE_TEMPLATE_BLOCK = """<a href="index.html" style="color:#4a00e0; text-decoration: none; font-size: 14px;">← Glossary</a>
<span class="gloss-topic" style="margin-top: 24px;">{topic}</span>
<h1 class="gloss-term">{term}</h1>
<p class="gloss-def">{def_}</p>

<h3 class="gloss-section-head">Explained simply.</h3>
<p class="gloss-explain">{explain}</p>

<h3 class="gloss-section-head">An example.</h3>
<div class="gloss-example">{example}</div>

<h3 class="gloss-section-head">Why it matters.</h3>
<p class="gloss-why">{why}</p>

<div class="gloss-related"><h4>Related terms</h4>{related_links}</div>
"""

EXTRA_CSS = """
.gloss-section-head { font-size: 13px; text-transform: uppercase; letter-spacing: 0.12em; color: #4a00e0; font-weight: 800; margin: 32px 0 8px 0; }
.gloss-explain, .gloss-why { font-size: 16px; line-height: 1.75; color: #2a2a30; margin: 0 0 8px 0; }
.gloss-example { font-size: 15px; line-height: 1.7; color: #3f3f46; background: #f7f5ff; border-left: 3px solid #4a00e0; padding: 14px 18px; border-radius: 6px; margin: 0 0 8px 0; white-space: pre-line; }
"""


def build_related_links(related):
    return "".join(f'<a href="{r}.html">{r.replace("-", " ").title()}</a>' for r in related)


rewritten = 0
missing = []
for slug, data in TERMS.items():
    path = GLOSSARY / f"{slug}.html"
    if not path.exists():
        missing.append(slug)
        continue

    text = path.read_text(encoding="utf-8")

    new_block = PAGE_TEMPLATE_BLOCK.format(
        topic=data["topic"],
        term=data["term"],
        def_=data["def"],
        explain=data["explain"],
        example=data["example"],
        why=data["why"],
        related_links=build_related_links(data["related"]),
    )

    pattern = re.compile(
        r'<a href="index\.html"[^>]*>← Glossary</a>.*?</div><footer',
        re.DOTALL,
    )
    replacement = new_block + '</div><footer'
    text, n = pattern.subn(replacement, text, count=1)
    if n == 0:
        print(f"WARN: could not find block in {slug}")
        continue

    if ".gloss-section-head" not in text and "</style>" in text:
        text = text.replace("</style>", EXTRA_CSS + "\n</style>", 1)

    path.write_text(text, encoding="utf-8")
    rewritten += 1

print(f"Rewrote {rewritten} non-AI glossary entries.")
if missing:
    print(f"Missing files (not found in /glossary): {missing}")
