#!/usr/bin/env python3
"""Email Marketing expertise - 35 pages."""
from _build_expertise import build_expertise_section


SIDEBAR = [
    ("Foundations", [
        ("index", "Overview"),
        ("foundations/why-email", "Why email still wins"),
        ("foundations/list-vs-channel", "Owned list vs rented audience"),
        ("foundations/kpis", "Email marketing KPIs"),
    ]),
    ("List Building", [
        ("list/signup-forms", "Signup forms"),
        ("list/lead-magnets", "Lead magnets"),
        ("list/exit-intent", "Exit-intent popups"),
        ("list/content-upgrades", "Content upgrades"),
        ("list/list-quality", "List quality"),
    ]),
    ("Deliverability", [
        ("deliverability/authentication", "SPF, DKIM, DMARC"),
        ("deliverability/sender-reputation", "Sender reputation"),
        ("deliverability/list-hygiene", "List hygiene"),
        ("deliverability/spam-triggers", "Spam triggers"),
        ("deliverability/monitoring", "Monitoring placement"),
    ]),
    ("Automations", [
        ("automations/welcome-series", "Welcome series"),
        ("automations/abandoned-cart", "Abandoned cart"),
        ("automations/win-back", "Win-back"),
        ("automations/post-purchase", "Post-purchase"),
        ("automations/behavioral", "Behavioral triggers"),
    ]),
    ("Broadcasts", [
        ("broadcasts/cadence", "Broadcast cadence"),
        ("broadcasts/subject-lines", "Subject lines"),
        ("broadcasts/content-types", "Content types"),
        ("broadcasts/segmentation", "Segmentation"),
    ]),
    ("Commerce Email", [
        ("commerce/abandoned-browse", "Abandoned browse"),
        ("commerce/product-launches", "Product launches"),
        ("commerce/vip-loyalty", "VIP + loyalty"),
    ]),
    ("SaaS Email", [
        ("saas/onboarding", "Onboarding sequences"),
        ("saas/feature-education", "Feature education"),
        ("saas/trial-nudges", "Trial nudges"),
        ("saas/churn-prevention", "Churn prevention"),
    ]),
    ("Testing + Analytics", [
        ("testing/ab-tests", "Email A/B tests"),
        ("testing/benchmarks", "Benchmarks"),
        ("testing/cohort-analysis", "Cohort analysis"),
    ]),
    ("Tools", [
        ("tools/klaviyo", "Klaviyo"),
        ("tools/convertkit", "ConvertKit"),
        ("tools/mailchimp", "Mailchimp"),
        ("tools/tool-fit", "Picking a tool"),
    ]),
]


def q(title, desc, intro, sections):
    html = f'<p class="lede">{intro}</p>'
    for h, body in sections:
        html += f'<h2>{h}</h2>'
        if isinstance(body, list):
            html += '<ul>' + ''.join(f'<li>{i}</li>' for i in body) + '</ul>'
        else:
            html += f'<p>{body}</p>'
    return {'title': title, 'description': desc, 'body': html, 'reading_time': 3}


PAGES = {
    "index": {'title': 'Email Marketing', 'description': 'A 35-page reference on modern email marketing: deliverability, automations, broadcasts, commerce, SaaS, testing.',
              'body': """<p class="lede">Email is the highest-ROI marketing channel still. Not because it's new or exciting, but because it's owned — your list is your asset, independent of platform algorithms. This section: how to build, send, and optimize email that actually gets opened, read, and converts.</p>

<div class="cards" style="margin-top:32px;">
<a href="foundations/why-email.html" class="card"><h3>Foundations</h3><p>Why email, owned vs rented, KPIs.</p></a>
<a href="list/signup-forms.html" class="card"><h3>List Building</h3><p>Forms, lead magnets, list quality.</p></a>
<a href="deliverability/authentication.html" class="card"><h3>Deliverability</h3><p>DNS, reputation, hygiene, monitoring.</p></a>
<a href="automations/welcome-series.html" class="card"><h3>Automations</h3><p>Welcome, abandoned cart, win-back, post-purchase.</p></a>
<a href="broadcasts/cadence.html" class="card"><h3>Broadcasts</h3><p>Cadence, subject lines, segmentation.</p></a>
<a href="commerce/abandoned-browse.html" class="card"><h3>Commerce Email</h3><p>DTC-specific flows.</p></a>
<a href="saas/onboarding.html" class="card"><h3>SaaS Email</h3><p>Onboarding, feature ed, churn prevention.</p></a>
<a href="testing/ab-tests.html" class="card"><h3>Testing</h3><p>A/B tests, benchmarks, cohort analysis.</p></a>
<a href="tools/klaviyo.html" class="card"><h3>Tools</h3><p>Klaviyo, ConvertKit, Mailchimp, picking.</p></a>
</div>""", 'reading_time': 3},

    "foundations/why-email": q("Why email still wins",
        "Email is the highest-ROI marketing channel. Here's why, three decades in.",
        "Email has been declared dead every year since 1998. Every year it produces more revenue per dollar than any other marketing channel. The reasons are structural.",
        [("You own it", "Your email list is an owned asset. Platform algorithms can't throttle it. You decide what to send and when."),
         ("Intent of opening", "Inbox is a personal space. Users who open have some level of intent."),
         ("Measurable", "Opens, clicks, conversions — all trackable."),
         ("High ROI", "Average: $36-42 in revenue per $1 spent, depending on industry and report."),
         ("Compounds", "List grows over time; each subscriber is durable until they unsubscribe.")]),

    "foundations/list-vs-channel": q("Owned list vs rented audience",
        "Social followers are rented. Email subscribers are owned. The difference compounds.",
        "Every social follower is rented from the platform. Algorithms change, accounts get suspended, reach degrades. Email subscribers are yours.",
        [("Rented audience", ["Instagram, TikTok, LinkedIn followers", "Subject to algorithm changes", "Platform can suspend your account", "Reach is a small % of followers"]),
         ("Owned audience", ["Your email list", "You choose who to contact and when", "100% of active subscribers can receive your email", "Portable across platforms"]),
         ("The implication", "Use social to grow audiences, but convert them to email. Social is acquisition; email is the moat.")]),

    "foundations/kpis": q("Email marketing KPIs",
        "Open rate, click rate, conversion rate, list growth, deliverability. The metrics that matter.",
        "Email has a dozen possible metrics. Focus on the ones that map to business outcomes.",
        [("Core KPIs", ["Open rate (20-40% broadcast, 40-60% transactional)", "Click-through rate (1-5% broadcast, 10%+ highly-targeted)", "Conversion rate (varies wildly)", "Unsubscribe rate (<0.5%)", "Spam complaints (<0.1%)", "List growth rate"]),
         ("Revenue KPIs", ["Revenue per email sent (RPES)", "Revenue per subscriber per month", "List LTV"]),
         ("Post-iOS 15 open rates", "Apple's Mail Privacy Protection pre-loads images, inflating opens by 20-40%. Open rates are less reliable than they were; click rate is truer.")]),

    # LIST BUILDING (5)
    "list/signup-forms": q("Signup forms",
        "Where and how you ask for emails determines your list growth rate.",
        "The signup form is your list-building infrastructure. Placement, timing, and offer determine conversion.",
        [("Forms that work", ["Inline in content (after value delivered)", "Exit-intent popups", "Slide-ins after scroll %", "Dedicated landing pages for lead magnets", "Footer (last resort)"]),
         ("Forms that don't", ["Immediate popup on landing", "Sidebar noisy sign-up", "Forms with 8 fields", "Generic 'subscribe to newsletter'"]),
         ("The offer", "Specific value: '7-day email series on X' beats 'subscribe to newsletter'."),
         ("Fields", "Email only is the highest converter. Adding name drops conversion 5-10%. More fields, more drop.")]),

    "list/lead-magnets": q("Lead magnets",
        "A lead magnet is a free resource in exchange for email. Done right, the highest-converting signup.",
        "Lead magnets trade specific value for email subscription. Good ones convert 20-50% on landing pages.",
        [("Formats", ["Cheat sheets", "Templates", "Email course", "Free chapter / guide", "Calculator / tool", "Video training"]),
         ("Quality bar", "Good lead magnet is useful enough that someone would pay for it. Doing less destroys trust."),
         ("Specificity wins", "'Content marketing guide' underperforms '7-email cold email sequence that booked me 40 calls'."),
         ("Delivery", ["Welcome email with the magnet", "Set expectations for what else they'll receive", "Immediate value, not an intro"])]),

    "list/exit-intent": q("Exit-intent popups",
        "Exit-intent popups trigger when users are about to leave. Controversial, effective when done well.",
        "Exit-intent detects when the mouse moves to close the tab. Popup appears with an offer. Bothersome if over-used; valuable on specific pages.",
        [("When to use", ["On blog content (useful for signup)", "On product pages with abandonment", "On landing pages as a last-attempt"]),
         ("When not", ["Immediately on landing (annoying)", "On every page visit (fatiguing)", "On mobile (often poor UX)"]),
         ("Offer", "Should match the page content. Content page → related lead magnet. Product page → discount or reminder.")]),

    "list/content-upgrades": q("Content upgrades",
        "A content upgrade is a lead magnet specific to one blog post. The highest-converting signup format.",
        "Content upgrades offer a resource specific to the post the user just read. Contextual relevance drives 5-20x signup vs generic popup.",
        [("Examples", ["Blog post on keyword research + upgrade: 'keyword template'", "Post on email copy + upgrade: '10 tested subject lines'"]),
         ("Implementation", ["Inline in the post", "Modal triggered by click", "Dedicated section near the CTA"]),
         ("Investment", "Each upgrade takes effort. Prioritize top-traffic posts.")]),

    "list/list-quality": q("List quality",
        "A small high-quality list beats a huge low-quality one. Here's how to maintain quality.",
        "List quality matters more than list size. 10,000 engaged subscribers will outperform 100,000 disengaged ones.",
        [("Signs of quality", ["High open rates (35%+)", "Click rates above 3%", "Low unsubscribe rate", "Low spam complaints"]),
         ("Building quality", ["Don't buy lists", "No deceptive signup offers", "Immediately deliver value", "Segment to send relevant content"]),
         ("Maintaining", ["Regular list cleaning (remove unengaged 6+ months)", "Win-back campaigns before suppression", "Consistent value in every send"])]),

    # DELIVERABILITY (5)
    "deliverability/authentication": q("SPF, DKIM, DMARC",
        "Three DNS records that authenticate your email. Without them, deliverability suffers.",
        "Authentication records tell receiving servers your email is actually from you. Required for deliverability in 2026.",
        [("SPF", "Lists authorized IPs that can send from your domain. TXT record."),
         ("DKIM", "Cryptographic signature on every email. Proves the message wasn't modified."),
         ("DMARC", "Policy telling receivers what to do with unauthenticated mail. Also provides reporting."),
         ("All three", "Gmail and Yahoo require all three for senders of 5000+ emails/day as of 2024. No exceptions.")]),

    "deliverability/sender-reputation": q("Sender reputation",
        "Your domain and IP build reputation over time. Here's how to protect it.",
        "Every sending domain and IP has a reputation score with each email provider. Higher = better inbox placement. Built and lost over time.",
        [("Signals that help", ["Low bounce rate", "High engagement", "Low complaints", "Consistent volume", "Good content"]),
         ("Signals that hurt", ["Spike in volume", "High bounce from bad addresses", "Complaint rates above 0.1%", "Sending to unengaged addresses"]),
         ("Monitoring", ["Google Postmaster Tools (Gmail)", "Microsoft SNDS (Outlook)", "Sender Score (general)"])]),

    "deliverability/list-hygiene": q("List hygiene",
        "Send to engaged subscribers. Remove the rest. Your deliverability depends on it.",
        "Sending to unengaged or invalid addresses hurts deliverability. List hygiene is ongoing maintenance.",
        [("Regular tasks", ["Remove hard bounces immediately", "Remove soft bounces after 3-5 attempts", "Suppress unengaged (90+ days no open) or win-back first", "Clean inactive subscribers quarterly"]),
         ("Verification", "Before sending to new lists or after long gaps, verify addresses with ZeroBounce, NeverBounce, etc."),
         ("The tradeoff", "Removing subscribers feels like losing. It isn't. Engaged smaller list outperforms disengaged larger.")]),

    "deliverability/spam-triggers": q("Spam triggers",
        "Certain words, patterns, and structures trigger spam filters. Here's what to avoid.",
        "Spam filters look for patterns in content, structure, and sending behavior. Avoiding triggers improves inbox placement.",
        [("Content triggers", ["ALL CAPS", "Excessive exclamation!!!", "Words: FREE, ACT NOW, GUARANTEED", "Too many links", "Large images with little text"]),
         ("Structure triggers", ["Image-only email", "Shortened URLs", "Weird formatting", "Missing plain-text version"]),
         ("Sending triggers", ["Volume spikes", "Sending too fast to unengaged", "Purchased lists"]),
         ("Test before sending", "Send to Mail-tester.com, get score. Aim for 9+/10.")]),

    "deliverability/monitoring": q("Monitoring placement",
        "Inbox placement isn't automatic. Monitor where your emails actually land.",
        "Your email tool reports 'delivered' — but delivered could mean inbox or spam folder. Monitor actual placement.",
        [("Tools", ["Google Postmaster Tools", "Glock Apps inbox placement tests", "Seed addresses (inbox accounts you check manually)"]),
         ("Signals to watch", ["Inbox placement rate", "Gmail spam folder rate", "Junk folder at Outlook"]),
         ("Actions", ["Placement below 90%? Fix before scaling", "Sudden drop? Investigate recent sends", "Quarterly audit"])]),

    # AUTOMATIONS (5)
    "automations/welcome-series": q("Welcome series",
        "The first emails a new subscriber receives. Critical for first impressions and early conversion.",
        "Welcome series runs when someone joins your list. Typically 3-7 emails over 7-14 days. Highest-opened emails you'll send.",
        [("Structure", ["Email 1 (immediate): deliver promise + intro", "Email 2 (day 2): your story / why you", "Email 3 (day 4): core value content", "Email 4 (day 6): case study or social proof", "Email 5 (day 10): specific CTA / offer", "Email 6 (day 14): hand-off to regular cadence"]),
         ("Conversion opportunity", "New subscribers are warmest. Welcome series should include a soft CTA to your main offer."),
         ("From me personally", "Welcome emails should feel personal, not newsletter-templated.")]),

    "automations/abandoned-cart": q("Abandoned cart",
        "For e-commerce, abandoned cart emails recover 10-30% of lost revenue.",
        "When a shopper adds items to cart and leaves without buying, automated emails nudge them back. The highest-ROI email automation for DTC.",
        [("Typical sequence", ["Email 1 (1-2 hours later): 'You forgot something' + items", "Email 2 (24 hours): Social proof / reviews", "Email 3 (48-72 hours): Urgency / limited offer"]),
         ("Conversion", "10-30% of abandoned carts recover. $$$."),
         ("SMS vs email", "SMS has higher open rates but lower per-message revenue. Use together for max lift."),
         ("Don't over-discount", "Training customers to abandon for a discount. Use sparingly.")]),

    "automations/win-back": q("Win-back",
        "Re-engaging inactive subscribers before they're gone for good.",
        "Inactive subscribers (60-180 days no engagement) get a win-back campaign. Either re-engage or suppress.",
        [("Typical sequence", ["Email 1: 'We miss you' + value reminder", "Email 2: specific offer or incentive", "Email 3: 'Last email' — explicit choice to stay"]),
         ("Measurement", "% re-engage within 14 days. Those who don't get suppressed to protect deliverability."),
         ("Don't over-invest", "Most win-back attempts fail. That's fine. Cleaning the list is the other goal.")]),

    "automations/post-purchase": q("Post-purchase",
        "What you send after a purchase determines retention and next purchase.",
        "Post-purchase automations drive retention, repeat purchase, reviews, referrals. Often neglected.",
        [("Typical flow", ["Email 1 (immediate): Order confirmation", "Email 2 (on ship): tracking", "Email 3 (on delivery): 'Here's how to use it'", "Email 4 (7-14 days): How's it going?", "Email 5 (30 days): Review request", "Email 6 (60+ days): 'You might like...'"]),
         ("Educational content", "Guides for using the product increase satisfaction and reduce returns."),
         ("Review requests", "Timing matters. Ask after they've had enough time to experience the product.")]),

    "automations/behavioral": q("Behavioral triggers",
        "Emails triggered by specific user actions. Highest relevance, highest conversion.",
        "Behavioral triggers fire based on what users do (or don't do): viewed page X, used feature Y, hit usage limit Z. Most relevant email possible.",
        [("Examples", ["Viewed product 3 times, didn't buy", "Used feature for first time", "Hit plan limit", "Missed usage for 14 days"]),
         ("Setup", "Requires event tracking. Klaviyo, Customer.io, Braze support this well."),
         ("Relevance", "Behavioral triggers have 3-10x the conversion of broadcast emails. Worth the setup.")]),

    # BROADCASTS (4)
    "broadcasts/cadence": q("Broadcast cadence",
        "How often to send broadcasts. Too rare and you're forgotten. Too often and you annoy.",
        "Cadence varies by industry and audience. Generally: 1-3 broadcasts per week for content businesses, 1-2 for B2B, 2-5 for DTC.",
        [("DTC", "Weekly or more. 2-5/week for active brands is normal."),
         ("B2B SaaS", "Monthly newsletter + occasional product update. Don't overdo."),
         ("Newsletter", "Weekly or biweekly. Your subscribers signed up for regular content."),
         ("Testing", "Gradually increase frequency and watch unsubscribe/spam rate.")]),

    "broadcasts/subject-lines": q("Email subject lines",
        "The subject line determines whether anyone opens. Single highest lever on open rate.",
        "Subject lines are your email's hook. Short, specific, personal wins.",
        [("Patterns that work", ["Question", "Specific number / detail", "Curiosity gap", "Direct value promise", "Personal / conversational"]),
         ("Anti-patterns", ["All caps", "Multiple exclamations", "Marketing buzzwords ('Don't miss!')", "Clickbait without payoff"]),
         ("Length", "30-50 chars optimal. Mobile cuts off at ~30-40."),
         ("A/B test", "Always test 2 variants. Small changes can swing open rate 5-20%.")]),

    "broadcasts/content-types": q("Content types for broadcasts",
        "The types of broadcast emails that drive opens and clicks.",
        "Not every email needs to be a 'newsletter'. Mix formats to keep engagement high.",
        [("Formats", ["Personal letter-style", "Curated links / roundup", "Single-topic deep dive", "Product / offer announcement", "Case study / story", "Q&A"]),
         ("Mix ratio", "8:1 value : promotion. Mostly value, occasional ask."),
         ("Plain text vs HTML", "Plain text often outperforms for personal-feeling broadcasts. HTML for DTC product showcases.")]),

    "broadcasts/segmentation": q("Segmentation",
        "Sending relevant emails to relevant subscribers improves every metric.",
        "Segmentation splits your list by attributes or behavior so you send different content to different people. Relevance drives engagement.",
        [("Common segments", ["By signup source", "By engagement level", "By past purchase", "By geographic", "By product category interest"]),
         ("Behavioral segments", "Users who clicked X topic, bought Y product, visited Z page — more relevant than demographic segments."),
         ("Start simple", "3-5 segments is enough. Don't build 20 and get lost in management.")]),

    # COMMERCE (3)
    "commerce/abandoned-browse": q("Abandoned browse",
        "Emails triggered by viewing products without purchasing.",
        "Browse abandonment emails catch shoppers who viewed a product but didn't add to cart. Lower-intent than cart abandonment but bigger volume.",
        [("Sequence", ["Email 1 (12-24 hrs): product reminder + similar items", "Email 2 (3-5 days): social proof / reviews", "Email 3 (7 days): final reminder or stop"]),
         ("Conversion", "Lower than cart abandonment (shoppers had lower intent). Still 5-15% lift."),
         ("Don't spam", "Once or twice per product view cycle. Otherwise users unsubscribe.")]),

    "commerce/product-launches": q("Product launches",
        "Email drives a huge % of launch-day revenue for DTC. Here's the sequence.",
        "Product launches via email typically drive 30-50% of first-week revenue. Sequence matters.",
        [("Pre-launch", ["Teasers 14-30 days out", "Waitlist signup", "Behind-the-scenes content"]),
         ("Launch day", ["Morning announcement", "Afternoon follow-up (most opens happen later)"]),
         ("Post-launch", ["Social proof emails (reviews come in)", "Restock / last-chance emails", "Post-mortem offer (if not selling through)"])]),

    "commerce/vip-loyalty": q("VIP + loyalty email",
        "Top customers are worth 5-10x more than average. Email programs exclusive to them.",
        "Top 10% of customers often drive 40-60% of revenue. VIP email programs keep them loyal.",
        [("Tactics", ["Early access to new products", "Exclusive discounts", "VIP-only newsletter content", "Birthday/anniversary sends"]),
         ("Segmentation", "Define VIP: top 10% by LTV, or past 12-month revenue above $X."),
         ("Frequency", "More than regular broadcast cadence. They want to hear from you.")]),

    # SAAS (4)
    "saas/onboarding": q("SaaS onboarding emails",
        "The email sequence for new SaaS users drives activation and retention.",
        "SaaS onboarding emails supplement in-app onboarding. They bring users back and drive feature adoption.",
        [("Triggers", ["Day 1: welcome + getting started", "Day 3: if not activated — help", "Day 7: feature education", "Day 14: case study / social proof", "Day 21: upgrade nudge (if freemium/trial)"]),
         ("Tone", "Helpful, not salesy. New users want help."),
         ("Personalize", "Different emails for users who activated vs didn't.")]),

    "saas/feature-education": q("Feature education emails",
        "Most SaaS users use 20% of features. Emails that introduce new ones drive retention.",
        "Users who adopt more features retain better. Feature education emails nudge adoption.",
        [("Approach", ["Trigger when user hits related scenario", "Show specific value, not feature description", "Include how-to or quick demo"]),
         ("Not", ["Marketing-speak about features", "Long lists of everything your product does", "Pushy upgrade nudges disguised as education"])]),

    "saas/trial-nudges": q("Trial nudges",
        "Trial users are the highest-value prospects. Emails during trial drive conversion.",
        "During a free trial, every email should move users toward activation and conversion.",
        [("Sequence", ["Day 1: welcome + setup assistance", "Day 3: if not activated, offer help", "Day 7: value demonstration / case study", "Day 10: specific CTA to convert", "Day 14 (trial end): final conversion push"]),
         ("Conversion-focused", "Every email has a clear next step toward paid conversion."),
         ("Offer options", ["Extend trial (high-intent holdouts)", "Discount code (last resort)", "Demo with human (enterprise-leaning)"])]),

    "saas/churn-prevention": q("Churn prevention emails",
        "Emails to users showing churn signals, to prevent cancellation.",
        "Users don't just churn — they show signals first: decreased usage, failed logins, support tickets. Email reaches out before cancel.",
        [("Triggers", ["Haven't logged in 14 days", "Feature usage dropped 50%+", "Downgrade or cancel attempt"]),
         ("Tactics", ["'We noticed you haven't been back' outreach", "Offer help / demo", "Case study of success", "Specific save offer for downgraders"]),
         ("Measurement", "% of at-risk users retained.")]),

    # TESTING (3)
    "testing/ab-tests": q("Email A/B tests",
        "Standard practice for optimizing email. Subject lines, send time, content.",
        "A/B testing in email is easy: split list, send variant A to half, variant B to other half, measure.",
        [("What to test", ["Subject lines (highest leverage)", "From name", "Send time", "Email copy (length, tone)", "CTA"]),
         ("Sample size", "Most email tools build in sample-size calculators. Rule of thumb: test needs 500+ recipients per variant for meaningful data."),
         ("Single variable", "One test, one variable. Don't change multiple things at once.")]),

    "testing/benchmarks": q("Email benchmarks",
        "Industry benchmarks for email metrics. How do you compare?",
        "Benchmarks vary by industry. Compare to your vertical, not generic averages.",
        [("Open rate", ["E-commerce broadcast: 20-30%", "B2B SaaS: 25-35%", "Newsletters (engaged niche): 40-60%", "Transactional: 50-80%"]),
         ("Click rate", ["Broadcast: 1-3%", "Targeted automations: 5-15%", "Highly-segmented behavioral: 10-20%+"]),
         ("Unsubscribe rate", "Should be under 0.5% per send. Above that signals list or content problems.")]),

    "testing/cohort-analysis": q("Email cohort analysis",
        "Cohort analysis for email: engagement by signup cohort over time.",
        "Are newer subscribers as engaged as older ones? Cohort analysis reveals list-health trends.",
        [("Signals", ["Declining engagement in new cohorts: acquisition quality dropping", "Older cohorts more engaged: you're retaining the right users", "All cohorts decaying the same: content problem"]),
         ("Action", "Adjust acquisition sources or content based on cohort differences.")]),

    # TOOLS (4)
    "tools/klaviyo": q("Klaviyo",
        "The dominant email + SMS platform for DTC. Deep Shopify integration, segmentation, automation.",
        "Klaviyo is the gold standard for DTC email marketing. Tight Shopify integration, sophisticated segmentation, strong deliverability.",
        [("Strengths", ["Best-in-class DTC e-commerce features", "Product-behavior segmentation", "Flows + campaigns in one platform", "SMS + email unified"]),
         ("Weaknesses", ["Expensive at scale", "Overkill for non-e-commerce use cases", "Learning curve"]),
         ("Best for", "Serious DTC brands. Not for blogs, newsletters, or B2B.")]),

    "tools/convertkit": q("ConvertKit (now Kit)",
        "Email marketing for creators, bloggers, course creators. Tag-based, simple.",
        "ConvertKit rebranded as Kit. Focused on creator-economy: newsletter publishers, course creators, bloggers, podcasters.",
        [("Strengths", ["Clean UI for non-technical users", "Tag-based subscriber management", "Strong deliverability", "Free tier up to 10K subscribers"]),
         ("Weaknesses", ["Basic e-commerce features", "Not for complex B2B automation"]),
         ("Best for", "Creators building email audiences.")]),

    "tools/mailchimp": q("Mailchimp",
        "The original email platform. Broadly capable, not best-in-class at anything.",
        "Mailchimp was the dominant email tool for small businesses. Still has the biggest user base. Has gotten more expensive and more cluttered.",
        [("Strengths", ["Recognizable brand", "Broad integrations", "Free tier (with limits)"]),
         ("Weaknesses", ["Deliverability reputation has slipped", "Pricier than alternatives at scale", "Overcomplicated UI"]),
         ("Best for", "Very small businesses, simple newsletters. Migrate to specialist tools as you grow.")]),

    "tools/tool-fit": q("Picking an email tool",
        "The right tool depends on use case. Here's how to pick.",
        "Each email tool is strong for specific use cases. Mismatch = frustration + cost.",
        [("Decision tree", ["DTC e-commerce with Shopify: Klaviyo", "Newsletter / creator: ConvertKit or Beehiiv", "B2B SaaS with product events: Customer.io or Braze", "Broad small biz: Mailchimp or MailerLite", "Enterprise marketing: Marketo, HubSpot, Iterable"]),
         ("Migration is annoying but possible", "Don't panic-pick. Plan for one migration over the business lifecycle."),
         ("Avoid", "Using 'the one I already have' when it doesn't fit your use case.")]),
}


if __name__ == "__main__":
    build_expertise_section("email-marketing", "Email Marketing", SIDEBAR, PAGES)
