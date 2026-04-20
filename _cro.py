#!/usr/bin/env python3
"""CRO expertise - 35 pages."""
from _build_expertise import build_expertise_section


SIDEBAR = [
    ("Foundations", [
        ("index", "Overview"),
        ("foundations/what-is-cro", "What is CRO?"),
        ("foundations/when-to-do-cro", "When to do CRO"),
        ("foundations/scope-and-strategy", "Scope and strategy"),
    ]),
    ("Research", [
        ("research/analytics-audit", "Analytics audit"),
        ("research/heatmaps-recordings", "Heatmaps + recordings"),
        ("research/user-interviews", "User interviews"),
        ("research/surveys", "On-site surveys"),
        ("research/usability-testing", "Usability testing"),
    ]),
    ("Frameworks", [
        ("frameworks/lift", "LIFT model"),
        ("frameworks/ice", "ICE scoring"),
        ("frameworks/pxl", "PXL prioritization"),
        ("frameworks/fogg-behavior", "Fogg Behavior Model"),
    ]),
    ("Landing Pages", [
        ("pages/above-the-fold", "Above the fold"),
        ("pages/headlines-copy", "Headlines + copy"),
        ("pages/social-proof", "Social proof"),
        ("pages/forms", "Form design"),
        ("pages/ctas", "CTA design"),
        ("pages/page-speed", "Page speed"),
    ]),
    ("Checkout + Conversion", [
        ("conversion/checkout-optimization", "Checkout optimization"),
        ("conversion/cart-abandonment", "Cart abandonment"),
        ("conversion/trust-signals", "Trust signals"),
        ("conversion/friction-audit", "Friction audit"),
    ]),
    ("Testing", [
        ("testing/ab-testing-setup", "A/B testing setup"),
        ("testing/sample-size", "Sample size"),
        ("testing/significance", "Significance"),
        ("testing/what-to-test", "What to test"),
        ("testing/velocity", "Testing velocity"),
    ]),
    ("Analytics", [
        ("analytics/funnels", "Funnel analysis"),
        ("analytics/segments", "Segment analysis"),
        ("analytics/attribution", "Attribution gotchas"),
    ]),
    ("Tools", [
        ("tools/google-optimize-alternatives", "Google Optimize alternatives"),
        ("tools/vwo", "VWO"),
        ("tools/optimizely", "Optimizely"),
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
    "index": {'title': 'Conversion Rate Optimization', 'description': 'A 35-page reference on CRO: research, frameworks, landing pages, checkout, testing, analytics.',
              'body': """<p class="lede">Conversion Rate Optimization is the practice of improving what percentage of visitors take a desired action. Small lifts compound: a 20% increase in conversion doubles revenue from the same traffic.</p>
<div class="cards" style="margin-top:32px;">
<a href="foundations/what-is-cro.html" class="card"><h3>Foundations</h3><p>What CRO is, when to do it, scoping.</p></a>
<a href="research/analytics-audit.html" class="card"><h3>Research</h3><p>Data, heatmaps, interviews, surveys, usability.</p></a>
<a href="frameworks/lift.html" class="card"><h3>Frameworks</h3><p>LIFT, ICE, PXL, Fogg.</p></a>
<a href="pages/above-the-fold.html" class="card"><h3>Landing Pages</h3><p>Above-the-fold, copy, social proof, forms, CTAs.</p></a>
<a href="conversion/checkout-optimization.html" class="card"><h3>Checkout + Conversion</h3><p>Checkout, cart abandonment, trust, friction.</p></a>
<a href="testing/ab-testing-setup.html" class="card"><h3>Testing</h3><p>Setup, sample size, significance, velocity.</p></a>
<a href="analytics/funnels.html" class="card"><h3>Analytics</h3><p>Funnels, segments, attribution.</p></a>
<a href="tools/google-optimize-alternatives.html" class="card"><h3>Tools</h3><p>VWO, Optimizely, and alternatives.</p></a>
</div>""", 'reading_time': 3},

    "foundations/what-is-cro": q("What is CRO?",
        "CRO is the systematic practice of improving conversion rates through research and experimentation.",
        "CRO (Conversion Rate Optimization) is the discipline of improving the percentage of visitors who take a desired action. It combines qualitative research with quantitative testing.",
        [("The CRO loop", ["Research: find the problems", "Hypothesize: what to change", "Test: A/B the change", "Measure: did it move the metric?", "Learn and iterate"]),
         ("What counts as conversion", ["Purchase", "Signup", "Demo booking", "Add-to-cart", "Email capture"]),
         ("The compound effect", "Small lifts compound. 5% lift every quarter → 22% annual, 85% over 3 years."),
         ("Not just for e-commerce", "SaaS signup conversion, B2B lead form completion, content site subscription - all benefit from CRO.")]),

    "foundations/when-to-do-cro": q("When to do CRO",
        "CRO requires traffic. Here's the minimum scale where it's worth the effort.",
        "CRO experiments require statistical significance - meaning enough visitors to detect differences. Below a certain scale, it's too slow to be worth doing.",
        [("Minimum traffic", "10K unique visitors/month per tested page, roughly. Lower scale = longer tests = less learning."),
         ("When to prioritize", ["High traffic, low conversion (CRO wins big)", "High-spend paid ads (every conversion matters)", "Stable product (testing isn't chasing a moving target)"]),
         ("When to delay", ["Pre-product-market-fit (fix the product first)", "Very low traffic", "Radical site redesign planned anyway"])]),

    "foundations/scope-and-strategy": q("CRO scope and strategy",
        "What to test, where to focus, what to skip.",
        "CRO isn't button-color testing. It's strategic. Focus on highest-impact pages and flows.",
        [("Prioritization", ["Pages with highest traffic × lowest conversion", "Revenue-per-visit impact potential", "Strategic importance"]),
         ("Don't test", ["Small traffic pages (no significance)", "Ideological preferences ('I like green buttons')", "Things your data says are already working"]),
         ("Strategic vs tactical", ["Strategic: rebuild pricing page, re-architect onboarding", "Tactical: A/B headlines, CTA copy, images", "Both matter; strategic changes drive bigger lifts"])]),

    # RESEARCH (5)
    "research/analytics-audit": q("Analytics audit",
        "Before testing, understand where users drop. An analytics audit finds the bottlenecks.",
        "CRO starts with data. Before testing, look at funnels: where do users enter, where do they drop, where do they convert?",
        [("What to look at", ["Top entry pages", "Page-by-page bounce rates", "Funnel drop-offs", "Conversion rates by segment (new vs returning, mobile vs desktop, channel)", "Search terms if on-site search"]),
         ("Tools", ["Google Analytics 4", "Mixpanel / Amplitude for product analytics", "Custom dashboards (Looker, etc.)"]),
         ("Output", "Ranked list of pages and flows with highest leverage - where a conversion improvement moves the needle most.")]),

    "research/heatmaps-recordings": q("Heatmaps + session recordings",
        "Heatmaps show where users click. Session recordings show what they do. Both reveal issues data alone misses.",
        "Heatmaps and recordings show behavior qualitatively. Where quantitative data says 'users drop here,' recordings show why.",
        [("Heatmap insights", ["Do users see the CTA? (fold test)", "Are they clicking non-clickable elements?", "Are they scrolling?", "Where attention goes"]),
         ("Recording insights", ["Rage clicks (frustration)", "Dead clicks", "Form abandonment mid-field", "Navigation confusion"]),
         ("Tools", ["Hotjar, Microsoft Clarity (free), Fullstory, Mouseflow"]),
         ("Time investment", "Watch 15-30 recordings per feature. Patterns emerge fast.")]),

    "research/user-interviews": q("User interviews",
        "Talking to users reveals what data can't. Especially the 'why' behind behaviors.",
        "User interviews ask people why they did what they did. Priceless qualitative input.",
        [("Who to interview", ["New customers (what convinced you?)", "Non-converters (what stopped you?)", "Long-term users (what keeps you?)"]),
         ("Question patterns", ["Walk me through your signup process", "What made you hesitate?", "What almost made you not complete?", "What else were you considering?"]),
         ("Volume", "5-10 interviews per segment. Patterns emerge at 5-7 for most topics."),
         ("Output", "Qualitative insights that generate hypotheses for testing.")]),

    "research/surveys": q("On-site surveys",
        "Quick on-site surveys catch users in context. Used well, high signal.",
        "Surveys running on your site capture users' minds while they're actively interacting. Different from post-hoc interviews.",
        [("Question types", ["Single question exit survey: 'What stopped you from completing?'", "Rating + follow-up: 'How useful was this page?' (1-5) + why", "NPS: recommend likelihood"]),
         ("When to show", ["Exit intent", "After action (post-purchase)", "After scrolling 50%+ (engaged users)"]),
         ("Tools", ["Hotjar, Qualaroo, Typeform, Intercom, in-product surveys"]),
         ("Avoid", "Long surveys. Users bail.")]),

    "research/usability-testing": q("Usability testing",
        "Watch real users try to use your site. Reveals friction invisible to you.",
        "Usability testing has users attempt tasks on your site, narrating thoughts. Uncovers confusion, friction, mental-model mismatches.",
        [("Method", "Give user a specific task ('find a product for X and buy it'), have them narrate, observe and note."),
         ("Sample size", "5 users reveals 80% of usability issues (Nielsen research)."),
         ("Tools", ["UserTesting, Usertesting.com, Maze, Userlytics - moderated or unmoderated"]),
         ("ROI", "Few hours of testing often reveals glaring issues you'd never catch yourself.")]),

    # FRAMEWORKS (4)
    "frameworks/lift": q("LIFT model",
        "Six elements that affect conversion: Value, Relevance, Clarity, Distraction, Urgency, Anxiety.",
        "LIFT is a framework for auditing pages. Every conversion page has six forces. Good design maximizes Value, Relevance, Clarity, Urgency while minimizing Distraction and Anxiety.",
        [("Value", "Is the promise clear and compelling?"),
         ("Relevance", "Does the page match what the visitor expected (from ad or link)?"),
         ("Clarity", "Is it instantly clear what you're offering and what to do?"),
         ("Distraction", "Is there anything pulling attention away from the conversion?"),
         ("Urgency", "Is there a reason to act now?"),
         ("Anxiety", "What fears or doubts might block completion? Trust signals, guarantees.")]),

    "frameworks/ice": q("ICE scoring",
        "Impact × Confidence × Ease. A lightweight prioritization framework.",
        "ICE ranks experiment ideas by three factors, each 1-10. Product is the score.",
        [("Impact", "How big if it works?"),
         ("Confidence", "How sure are you it'll work?"),
         ("Ease", "How fast can you ship and test?"),
         ("Output", "Rank backlog by ICE score. Run top-scored first."),
         ("Critique", "Subjective scoring. Use for relative ordering, not absolute decisions.")]),

    "frameworks/pxl": q("PXL prioritization",
        "A more structured framework than ICE, built for CRO.",
        "PXL (from CXL) scores ideas on evidence, impact, and effort with more structure than ICE. Harder to manipulate.",
        [("Evidence", "What data supports this test? (user research, analytics, prior tests, expert opinion)"),
         ("Impact", "Above/below fold? Key page? Revenue-adjacent?"),
         ("Ease", "How much engineering and design time?"),
         ("Output", "Similar to ICE but with explicit weights for evidence quality.")]),

    "frameworks/fogg-behavior": q("Fogg Behavior Model",
        "B = MAT: Behavior requires Motivation, Ability, and Trigger.",
        "BJ Fogg's behavior model: for a user to act (B), they need Motivation (why), Ability (easy enough), and Trigger (prompt in the moment).",
        [("Motivation", "Does the user want to do this?"),
         ("Ability", "Is it easy enough? (reducing friction moves more users than motivating them)"),
         ("Trigger", "Is there a clear prompt at the moment of opportunity?"),
         ("CRO implication", "Most conversion failures are Ability problems (friction), not Motivation problems."),
         ("Action", "Audit your conversion flow for each element. Usually Ability (friction) is the biggest lever.")]),

    # LANDING PAGES (6)
    "pages/above-the-fold": q("Above the fold",
        "The first screen decides whether users stay. Here's what must be there.",
        "Above-the-fold is what users see without scrolling. They spend ~5 seconds deciding whether to stay.",
        [("Must include", ["Clear headline stating what you do/offer", "Sub-headline with supporting benefit", "Primary CTA button (visible)", "Hero visual (photo, video, or relevant image)", "Trust signal (logo, review, badge)"]),
         ("Don't include", ["Multiple competing CTAs", "Overwhelming text", "Slow-loading hero video", "Generic stock photo"]),
         ("Mobile first", "60-80% of traffic is mobile. Verify on mobile first."),
         ("5-second test", "Show someone your page for 5 seconds, close it, ask what you do. If they can't answer, rewrite.")]),

    "pages/headlines-copy": q("Headlines + copy",
        "The words on your page matter more than the design. Here's what works.",
        "Good copy on a mediocre page beats great design with mediocre copy. Headlines especially carry most of the conversion weight.",
        [("Headline principles", ["State the benefit or outcome", "Specific over generic", "Under 12 words", "First-time visitor clarity test"]),
         ("Body copy", ["Skim-able structure (headings, bullets)", "Benefits before features", "Specific proof points", "Conversational tone"]),
         ("Common mistakes", ["Generic value props ('boost productivity')", "Feature-first pitches", "Walls of text", "Jargon without translation"])]),

    "pages/social-proof": q("Social proof",
        "Social proof reduces buyer anxiety. Here's how to use it effectively.",
        "People trust what other people did. Social proof is credibility by association.",
        [("Types", ["Testimonials (named, with photo/title)", "Case studies", "Logos of recognized customers", "Usage stats ('40,000+ users')", "Reviews / ratings", "Media mentions"]),
         ("Placement", ["Near CTA for final push", "At objection points", "On pricing page for confidence"]),
         ("Avoid", ["Fake-looking testimonials", "Generic quotes", "Cherry-picked stats without context", "Too many (clutters)"])]),

    "pages/forms": q("Form design",
        "Every form field drops conversion. Design minimizes friction.",
        "Form design is a CRO discipline on its own. Every field, label, validation affects completion rate.",
        [("Principles", ["Ask only what you need", "One field per line (not cramped)", "Inline validation", "Clear error messages", "Progress indicator for multi-step"]),
         ("Field count", "Each added field drops conversion 5-15%. Email-only is the baseline."),
         ("Multi-step vs single", "For 5+ fields, multi-step usually converts better. Shorter perceived commitment at each step."),
         ("Mobile", "Use appropriate input types (email, tel, number) to trigger right keyboard.")]),

    "pages/ctas": q("CTA design",
        "The call-to-action button is the conversion moment. Design matters.",
        "CTA = call to action. The button (or link) where users commit. Design, copy, placement all affect click rate.",
        [("Button design", ["High-contrast color", "Large enough to tap on mobile", "Clear, readable text", "One primary CTA per section"]),
         ("Button copy", ["Action-oriented ('Get my plan')", "Specific over generic ('Start free trial' vs 'Submit')", "Benefit-laden where possible"]),
         ("Placement", ["Above fold (primary)", "After value content (consideration)", "Sticky footer on long pages (sticky mobile)"]),
         ("Testing", "Button copy can swing conversion 5-30%. One of the highest-leverage tests.")]),

    "pages/page-speed": q("Page speed",
        "Every second of load time drops conversion. Speed is a conversion lever.",
        "Slow pages convert poorly. Every 1-second delay in load time can drop conversion 5-10%.",
        [("Targets", ["Under 3 seconds load time", "Under 1.5s First Contentful Paint", "Under 2.5s Largest Contentful Paint", "Core Web Vitals green"]),
         ("Common bottlenecks", ["Uncompressed images", "Too many JS/CSS files", "Slow server response", "Third-party scripts"]),
         ("Tools", ["PageSpeed Insights (free)", "GTmetrix", "WebPageTest"]),
         ("Quick wins", ["Compress images", "Lazy load below-fold content", "Remove unused scripts", "CDN"])]),

    # CHECKOUT + CONVERSION (4)
    "conversion/checkout-optimization": q("Checkout optimization",
        "For e-commerce, checkout is where money is made or lost. Here's what to fix.",
        "Checkout is the highest-value CRO surface in e-commerce. Every friction point leaks revenue.",
        [("Best practices", ["Guest checkout option", "Minimal required fields", "Multiple payment methods", "Visible shipping costs early", "Clear pricing breakdown", "Trust signals (SSL, badges)", "Progress indicator"]),
         ("Common issues", ["Surprise shipping cost at end (top cart abandonment reason)", "Mandatory account creation", "Too many form fields", "No express checkout (Apple Pay, Shop Pay)"]),
         ("Checkout length", "3 steps is common. Long single-page or longer multi-step both work - test.")]),

    "conversion/cart-abandonment": q("Cart abandonment",
        "60-80% of carts are abandoned. Recovery is huge revenue opportunity.",
        "Cart abandonment happens mostly due to checkout friction, surprise costs, or distraction. Some is recoverable via email; more is preventable.",
        [("Prevention in checkout", ["Show shipping cost before checkout", "Offer guest checkout", "Reduce form fields", "Multiple payment options"]),
         ("Recovery via email", "Sequence of 3 emails over 48-72 hours. Recovers 10-30% of abandoned carts."),
         ("Recovery via retargeting ads", "Supplement email; reach users who didn't share email."),
         ("SMS abandonment", "Higher open rates than email. Works well for cart abandonment specifically.")]),

    "conversion/trust-signals": q("Trust signals",
        "Anxiety is a conversion killer. Trust signals reduce it.",
        "Users considering a purchase or signup have doubts. Trust signals systematically address them.",
        [("Types", ["Payment security (SSL badge, Norton, McAfee)", "Money-back guarantee", "Customer testimonials", "Industry certifications", "Privacy guarantee", "Company legitimacy (about page, physical address)"]),
         ("Placement", ["Near forms/checkout", "On pricing page", "Above fold (subtle)", "Dedicated trust/security page"]),
         ("Avoid", ["Cluttering with too many badges", "Dated-looking badges", "Obvious stock-photo testimonials"])]),

    "conversion/friction-audit": q("Friction audit",
        "Every friction point drops conversion. Audit systematically.",
        "Friction is anything that slows or discourages user action. Audit your flow by walking through as a first-time user.",
        [("Common friction points", ["Requiring account before value", "Credit card required for free trial", "Long forms", "Confusing navigation", "Unclear pricing", "Forced upsells"]),
         ("The user test", "Give someone unfamiliar your URL. Watch them try to sign up or buy. Every hesitation is friction."),
         ("Prioritize by", ["Frequency (affects all users)", "Severity (makes them leave entirely)", "Fix cost (easy wins first)"])]),

    # TESTING (5)
    "testing/ab-testing-setup": q("A/B testing setup",
        "Proper A/B test setup: clear hypothesis, single variable, sufficient sample.",
        "A/B testing splits traffic between control (A) and variant (B), measures outcomes, picks winner.",
        [("Prerequisites", ["Clear hypothesis", "Single variable changed", "Minimum sample size calculated", "Primary metric defined"]),
         ("Setup", ["50/50 traffic split", "Random assignment", "Both variants tracked identically", "Run until statistical significance"]),
         ("Post-launch", "Don't peek early - wait for statistical significance before declaring winner.")]),

    "testing/sample-size": q("Sample size",
        "Tests need enough data for statistical significance. Below that, you're looking at noise.",
        "Sample size depends on baseline conversion, effect size you want to detect, and confidence level.",
        [("Calculators", ["VWO, Optimizely have built-in calculators", "Evan Miller's A/B testing calculator", "Excel-based calculators"]),
         ("Rule of thumb", "2-5% baseline conversion rate with 10% expected lift needs 10,000+ visitors per variant."),
         ("Low traffic reality", "Sub-significant tests just mean 'we don't know.' Don't ship losers as winners.")]),

    "testing/significance": q("Statistical significance",
        "95% confidence is the standard. Below that, your result is likely noise.",
        "Statistical significance tells you the difference between variants is unlikely to be random. 95% confidence (p-value 0.05) is standard.",
        [("P-value", "Probability the result is random. Lower is better."),
         ("Common mistakes", ["Stopping early (p-hacking)", "Ignoring base rates", "Running many tests without correction", "Interpreting non-significance as 'no effect'"]),
         ("Practical threshold", "95% confidence + minimum sample size. Lower confidence on low-stakes, higher on high-stakes.")]),

    "testing/what-to-test": q("What to test",
        "Prioritize tests by potential impact × ease. Here's the priority order.",
        "Not all tests move the needle equally. Prioritize for impact.",
        [("High-impact tests", ["Headlines", "Hero images", "CTA copy", "Pricing structure", "Form length", "Page structure (radical changes)"]),
         ("Lower-impact", ["Button color", "Microcopy", "Font choices", "Minor visual tweaks"]),
         ("Skip", ["Things with tiny traffic", "Changes you can't measure", "A/B tests driven by opinion not data"])]),

    "testing/velocity": q("Testing velocity",
        "Shipping more tests = more learning. Velocity compounds over quarters.",
        "Velocity is tests per week or per quarter. Higher velocity = more learning, faster improvement.",
        [("Velocity by maturity", ["Early: 1-2 tests/month", "Growing: 3-5 tests/month", "Mature: 2-3 tests/week"]),
         ("Building velocity", ["Documented test queue", "Templated test design", "Dedicated CRO infrastructure", "Regular planning cadence"]),
         ("Quality still matters", "Bad tests at high velocity is waste. Balance speed and rigor.")]),

    # ANALYTICS (3)
    "analytics/funnels": q("Funnel analysis",
        "Funnel analysis identifies the biggest conversion leak.",
        "A funnel is a sequence of steps. Funnel analysis shows drop-off at each step. The biggest leak is your biggest opportunity.",
        [("Building a funnel", "Map the steps: visit → view product → add cart → checkout → purchase. Measure at each."),
         ("Interpretation", ["Largest % drop = biggest opportunity", "Compare segments (new vs returning, mobile vs desktop)", "Track over time for trends"]),
         ("Actions", "Fix the biggest leak first. Moves the needle more than any other single CRO work.")]),

    "analytics/segments": q("Segment analysis",
        "Aggregate numbers hide truth. Segment analysis reveals specific problems.",
        "Blended conversion rate is an average. Segment by user attributes and you see which segments convert well, poorly, or not at all.",
        [("Segments to analyze", ["New vs returning", "Device (mobile, desktop, tablet)", "Traffic source (paid, organic, email, direct)", "Browser", "Geographic", "Landing page"]),
         ("Insights", "Often one segment has 5-10x conversion of another. Prioritize by segment size × conversion gap."),
         ("Action", "Optimize worst-performing segment first if it's high-traffic. Or double down on best-performing for scale.")]),

    "analytics/attribution": q("Attribution gotchas",
        "Attribution in CRO is tricky. Here's what to watch for.",
        "Attribution tells you which marketing touch drove a conversion. Multiple models exist; none are perfect.",
        [("Models", ["Last-click (simple, biased to bottom of funnel)", "First-click (biased to top)", "Linear (equal weight)", "Data-driven (algorithmic)"]),
         ("CRO-specific concerns", ["Same-user multi-touch: which page gets credit?", "Cross-device: hard to attribute", "Delayed conversions: attribute to session or first-touch?"]),
         ("Pragmatic", "Use platform attribution for directional signal, test for specific optimization, holdouts for truth.")]),

    # TOOLS (3)
    "tools/google-optimize-alternatives": q("Google Optimize alternatives",
        "Google Optimize sunset in 2023. Here's what to use instead.",
        "Google Optimize was the free A/B testing tool. Shut down in September 2023. Here's where to go.",
        [("VWO", "Full-featured CRO platform. Testing, heatmaps, surveys. Most popular alternative."),
         ("Optimizely", "Enterprise-tier. Expensive but deep features."),
         ("GA4 Experiments", "Google's partial replacement. Limited vs Optimize."),
         ("Convert.com, AB Tasty", "Mid-tier alternatives."),
         ("Statsig, Split, LaunchDarkly", "Engineering-heavy feature flag + experimentation tools.")]),

    "tools/vwo": q("VWO",
        "A popular full-stack CRO platform.",
        "VWO offers A/B testing, heatmaps, session recordings, surveys, and more - integrated in one platform.",
        [("Strengths", ["All-in-one (testing + analytics + research)", "Visual editor for non-devs", "Good analytics", "Reasonable pricing"]),
         ("Weaknesses", ["Enterprise tier gets expensive", "UI can be overwhelming"])]),

    "tools/optimizely": q("Optimizely",
        "Enterprise A/B testing platform.",
        "Optimizely is the enterprise CRO platform. Deep features, large companies, premium pricing.",
        [("Strengths", ["Feature breadth", "Performance at scale", "Feature flags + experimentation in one"]),
         ("Weaknesses", ["Expensive", "Overkill for most sites", "Requires significant setup"])])
}


if __name__ == "__main__":
    build_expertise_section("cro", "Conversion Rate Optimization", SIDEBAR, PAGES)
