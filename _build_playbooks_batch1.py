#!/usr/bin/env python3
"""Build playbooks batch 1: Real Estate, Mortgage, Financial Advisor, Personal Trainer, Coach."""
from _build_playbook import build_playbook
from _playbook_content_factory import generate_modules, std_landing
from _playbook_middle_modules import middle_modules


def build(slug_dir, profession, short, tagline, spec_overrides):
    """Wrapper to build a playbook from its spec."""
    spec = {
        'profession': profession,
        'short': short,
        'audience_description': spec_overrides.get('audience_description', f'clients in your market'),
        'typical_client': spec_overrides.get('typical_client', 'your ideal client'),
        'legal_concerns': spec_overrides.get('legal_concerns', 'licensing board, state regulations'),
        'revenue_model': spec_overrides.get('revenue_model', 'fee or commission'),
        'common_channels': spec_overrides.get('common_channels', ['Facebook', 'Instagram', 'LinkedIn']),
        'primary_asset_types': spec_overrides.get('primary_asset_types', ['emails', 'social posts', 'blog posts']),
        'compliance_notes': spec_overrides.get('compliance_notes', ['State licensing rules', 'Consumer protection laws']),
    }
    spec.update(spec_overrides)

    # Build middle modules (4-13) from spec
    mid = middle_modules(spec)
    spec['custom_modules'] = mid

    # Generate all 15 modules
    modules = generate_modules(spec)

    # Build the playbook
    landing = std_landing(profession, short, tagline)
    build_playbook(slug_dir, profession, tagline, modules, landing)


# ============================================================
# REAL ESTATE
# ============================================================
build(
    slug_dir="real-estate",
    profession="The Real Estate Agent's Claude Playbook",
    short="real estate",
    tagline="For real estate agents who want to build their own marketing: listing copy, neighborhood guides, buyer + seller content, referrals, reviews. 15 modules, 60+ prompts.",
    spec_overrides={
        'audience_description': 'buyers and sellers in your market',
        'typical_client': 'homeowners selling, first-time buyers, move-up buyers, investors',
        'legal_concerns': 'state real estate commission rules, Fair Housing Act, RESPA, NAR Code of Ethics',
        'compliance_notes': [
            'Fair Housing language (no protected-class steering)',
            'MLS/IDX rules in your area',
            'State license disclosure required on all marketing',
            'Broker/agent disclosure',
            'No guaranteeing sale price or timeline',
        ],
        'email_example': "A homeowner whose listing expired 90 days ago without selling, in a neighborhood with strong recent comps.",
        'social_topic_examples': [
            "A specific neighborhood tour",
            "The one inspection fix most buyers don't know about",
            "Why the \"Zillow Zestimate\" is usually wrong for your block",
            "What a $XK price adjustment actually costs in mortgage terms",
            "The hidden closing cost most buyers miss",
        ],
        'blog_topic_examples': [
            '"Homes for sale in [neighborhood]" with market-specific detail',
            '"How much does a home inspection cost in [city]"',
            '"Best neighborhoods in [city] for families with school-age kids"',
            '"Buying vs renting in [city] in 2026: the actual math"',
            '"How long does it take to sell a home in [zip code]"',
        ],
        'video_topic_examples': [
            "3-minute neighborhood walk-through",
            "Pre-listing: 5 things to fix before you list",
            "Open-house walk-through",
            "Client testimonial (anonymized)",
            "Market update 60-second video",
        ],
        'direct_mail_use': 'farming a neighborhood or targeting homeowners with equity',
        'referral_triggers': [
            'Just after closing - client is happiest',
            'One-year home anniversary (trigger for "how do you like it?")',
            'Client refers a friend who also closes - thank both',
            'After a successful price adjustment or over-ask outcome',
        ],
        'review_platforms': ['Google Business Profile', 'Zillow', 'Realtor.com', 'Facebook', 'Yelp'],
        'newsletter_topic_examples': [
            'January - real estate market resolutions / your year in review',
            'March - spring selling prep (when to list)',
            'June - mid-year market update',
            'September - fall buying season + school-year moves',
            'November - tax considerations for sellers',
        ],
        'ad_platforms': [
            'Facebook/Instagram - broad top-of-funnel local targeting',
            'Google Search - high-intent queries ("homes for sale [zip]")',
            'YouTube - neighborhood content + pre-roll',
            'Zillow Premier Agent - if the cost math works for your market',
        ],
        'client_ed_docs': [
            'First-time buyer guide (process, timeline, costs)',
            'Seller pre-listing checklist',
            'Closing day walkthrough',
            'Neighborhood one-pagers (top 5 in your market)',
            'Post-close "first year of ownership" guide',
        ],
        'primary_asset_types': ['listing descriptions', 'neighborhood guides', 'market updates', 'buyer/seller emails'],
    },
)


# ============================================================
# MORTGAGE BROKER
# ============================================================
build(
    slug_dir="mortgage",
    profession="The Mortgage Broker's Claude Playbook",
    short="mortgage",
    tagline="For mortgage brokers and loan officers: buyer education, real estate agent relationships, rate updates, referral systems. 15 modules, 60+ prompts.",
    spec_overrides={
        'audience_description': 'homebuyers and homeowners refinancing',
        'typical_client': 'first-time buyers, move-up buyers, refinance candidates, investors',
        'legal_concerns': 'CFPB rules, RESPA, TILA, state licensing (NMLS), fair lending',
        'compliance_notes': [
            'NMLS number required on all marketing',
            'No guaranteed rates or approvals',
            'RESPA Section 8 (no kickbacks for referrals)',
            'TRID disclosure requirements',
            'Fair lending (no discriminatory targeting)',
            'Equal Housing Opportunity language',
        ],
        'email_example': "A real estate agent whose buyers are losing deals due to slow pre-approval from their current lender.",
        'social_topic_examples': [
            "What a 0.5% rate change actually means in monthly payment",
            "The one document most buyers forget to gather for pre-approval",
            "Why your FICO score varies across bureaus",
            "FHA vs conventional for a first-time buyer in [your market]",
            "Rate lock timing: when it makes sense, when it doesn't",
        ],
        'blog_topic_examples': [
            '"Mortgage rates in [city] this week" (update weekly)',
            '"FHA vs conventional loan for first-time buyer in [state]"',
            '"How much house can I afford with a $X income"',
            '"Refinance break-even calculator walkthrough"',
            '"Self-employed borrower mortgage: what you need"',
        ],
        'video_topic_examples': [
            "60-second weekly rate update",
            "Pre-approval vs pre-qualification explained",
            "Closing cost breakdown",
            "Rate lock: when and why",
            "Self-employed mortgage documentation",
        ],
        'direct_mail_use': 'refinance opportunity targeting homeowners when rates drop',
        'referral_triggers': [
            'Just after closing - thank buyer + their agent',
            'Agent sends you a deal - thank them, send lead back later',
            'Rate drop that makes refi make sense for past client',
            'Loan anniversary',
        ],
        'review_platforms': ['Google Business Profile', 'Zillow', 'Facebook', 'Yelp', 'NMLS Consumer Access'],
        'newsletter_topic_examples': [
            'January - rate outlook for the year',
            'Spring - buying season preparation',
            'Summer - equity / refi opportunities',
            'Fall - market-shift implications',
            'Year-end - tax deductibility and mortgage interest',
        ],
        'ad_platforms': [
            'Facebook - local homeowner targeting for refi',
            'Google Search - high-intent ("mortgage rates [city]", "refinance calculator")',
            'YouTube - explainer content',
            'LinkedIn - agent partnership building',
        ],
        'client_ed_docs': [
            'Pre-approval document checklist',
            'Loan process timeline (application to close)',
            'Rate lock explainer',
            'Refinance break-even calculator',
            '"First-time buyer" onboarding packet',
        ],
        'primary_asset_types': ['rate update emails', 'agent-partnership content', 'buyer-education guides'],
    },
)


# ============================================================
# FINANCIAL ADVISOR
# ============================================================
build(
    slug_dir="financial-advisor",
    profession="The Financial Advisor's Claude Playbook",
    short="financial advisor",
    tagline="For RIAs, fee-only planners, and wealth advisors: prospecting, newsletter content, client education, compliance-aware copy. 15 modules, 60+ prompts.",
    spec_overrides={
        'audience_description': 'prospects considering wealth management and financial planning',
        'typical_client': 'pre-retirees, recently-retired, business owners, high earners 45-65',
        'legal_concerns': 'SEC/FINRA rules, state securities regulators, Investment Advisers Act, Marketing Rule',
        'compliance_notes': [
            'SEC Marketing Rule (testimonials, endorsements, performance)',
            'FINRA rules for broker-dealer reps (Rule 2210)',
            'No performance guarantees or past-performance extrapolation',
            'Required disclaimers on performance data',
            'Net-of-fees requirements for investment content',
            'Form ADV references where applicable',
            'State-specific advertising rules',
        ],
        'email_example': "A business owner age 55-65 who just sold their business and is sitting on a large liquidity event.",
        'social_topic_examples': [
            "The real difference between a fiduciary and a suitability standard",
            "Why Roth conversions can be a tax mistake in certain years",
            "What a 1% fee actually costs over 30 years",
            "The one retirement expense most people underestimate",
            "Sequence-of-returns risk explained without jargon",
        ],
        'blog_topic_examples': [
            '"Should I roll over my 401k to an IRA?"',
            '"How much do I need to retire at 60 in [state]"',
            '"Backdoor Roth conversion step-by-step"',
            '"Fee-only vs fee-based vs commission advisors explained"',
            '"Tax-loss harvesting: when it actually helps"',
        ],
        'video_topic_examples': [
            "60-second market update",
            "Explaining a financial concept (sequence risk, Roth conversion, etc.)",
            "Client Q&A format videos",
            "Market-event reaction video",
            "Retirement scenarios walk-through",
        ],
        'direct_mail_use': 'targeted outreach to high-income or high-net-worth prospects',
        'referral_triggers': [
            'After a successful tax season / year-end planning',
            'Client referred by CPA or estate attorney - thank and reciprocate',
            'After a client milestone (retirement, liquidity event)',
            'Annual review meeting that went well',
        ],
        'review_platforms': ['Google Business Profile', 'LinkedIn recommendations', 'SmartAsset', 'NAPFA listing'],
        'newsletter_topic_examples': [
            'January - year-end tax wrap, new-year planning items',
            'April - tax deadline-driven actions',
            'June - mid-year check-in',
            'October - open enrollment, end-of-year moves',
            'December - gifting + charitable planning',
        ],
        'ad_platforms': [
            'Google Search - high-intent ("fee-only advisor [city]", "fiduciary financial planner")',
            'LinkedIn - higher-income targeting, business owners',
            'Facebook - retiree/pre-retiree lookalikes',
            'Podcast host-read sponsorships (financial shows)',
        ],
        'client_ed_docs': [
            'Onboarding packet (what to expect, documents needed)',
            'Annual review agenda template',
            'Financial plan summary (reader-friendly)',
            'Beneficiary designation checklist',
            'Tax-loss harvesting year-end checklist',
        ],
        'primary_asset_types': ['newsletter content', 'educational videos', 'blog posts', 'client reports'],
    },
)


# ============================================================
# PERSONAL TRAINER
# ============================================================
build(
    slug_dir="personal-trainer",
    profession="The Personal Trainer's Claude Playbook",
    short="fitness",
    tagline="For personal trainers, online coaches, and gym owners: social content, nutrition education, client retention, program launches. 15 modules, 60+ prompts.",
    spec_overrides={
        'audience_description': 'people pursuing fat loss, strength, or general fitness goals',
        'typical_client': 'adults 25-55 who want visible results, busy professionals, postpartum moms, returning-to-fitness clients',
        'legal_concerns': 'FTC guidelines on health claims, testimonial disclosures, liability waivers, insurance requirements',
        'compliance_notes': [
            'No "guaranteed results" language',
            'FTC disclosure for before/after photos (typical results)',
            'No medical claims outside your scope',
            'Testimonial disclosures (paid, received products, etc.)',
            'Local business licensing',
        ],
        'email_example': "A prospect who downloaded your free workout PDF but didn't book a consultation yet.",
        'social_topic_examples': [
            "The one exercise most people do wrong",
            "Why cardio alone won't give you abs",
            "Realistic timeline: fat loss over 12 weeks",
            "Client transformation (with their permission + disclosures)",
            "Common myth: busting high-protein dangers",
        ],
        'blog_topic_examples': [
            '"Personal trainer in [city]: what to expect from a first session"',
            '"How much does a personal trainer cost in [city]"',
            '"In-person vs online personal training: what\'s right for you"',
            '"Beginner workout plan for [age-group] in [city]"',
            '"Nutrition for fat loss: the simple truth"',
        ],
        'video_topic_examples': [
            "30-second exercise demo with form cues",
            "'What I ate today' for fat loss",
            "Client transformation story (anonymized)",
            "Gym tour (if you have a facility)",
            "Myth-busting short",
        ],
        'direct_mail_use': 'targeting new movers or postpartum demographics in specific ZIP codes',
        'referral_triggers': [
            "Client hits a big milestone (weight loss, PR, fits into old clothes)",
            "Client completes a full program successfully",
            "Client's friend asks what they're doing differently",
            "Client takes before/after photos (and consents to share)",
        ],
        'review_platforms': ['Google Business Profile', 'Yelp', 'Facebook', 'Trustpilot', 'Instagram tagged posts'],
        'newsletter_topic_examples': [
            'January - goals without resolutions',
            'March - spring cleanup (habits, not dieting)',
            'Summer - travel + fitness maintenance',
            'September - back-to-routine',
            'December - holiday-season strategy (not restriction)',
        ],
        'ad_platforms': [
            'Instagram/Facebook - visual-first, transformation content',
            'Google Search - high-intent local ("personal trainer [city]")',
            'YouTube - tutorials and case studies',
            'TikTok - if you\'re comfortable on camera',
        ],
        'client_ed_docs': [
            'Onboarding packet (what to bring, expectations)',
            'Starter nutrition guide',
            'Home workout alternatives (for travel)',
            '30-60-90 day check-in template',
            'Movement library (common exercises with form cues)',
        ],
        'primary_asset_types': ['program launch emails', 'transformation content', 'nutrition + workout guides'],
    },
)


# ============================================================
# COACH / CONSULTANT
# ============================================================
build(
    slug_dir="coach",
    profession="The Coach's Claude Playbook",
    short="coaching",
    tagline="For executive coaches, life coaches, and consultants: lead magnets, cohort launches, newsletter content, referral partnerships. 15 modules, 60+ prompts.",
    spec_overrides={
        'audience_description': 'professionals seeking coaching or advisory support',
        'typical_client': 'mid-career professionals, founders, team leaders, career-transition clients',
        'legal_concerns': 'testimonial disclosures, income/outcome claims, ICF ethics standards (if certified)',
        'compliance_notes': [
            'No "guaranteed outcomes" language',
            'FTC rules on testimonials (typical results disclosure)',
            'No income claims unless substantiated',
            'ICF or other body ethics code if you follow one',
            'Contract/coaching agreement basics',
        ],
        'email_example': "A founder or executive who engaged with your content recently but hasn't booked a discovery call.",
        'social_topic_examples': [
            "The one conversation you're avoiding (and what happens when you finally have it)",
            "Why most coaching fails in the first 90 days",
            "A specific client reframe that changed their decision",
            "The question I ask every client in session one",
            "What coaching isn't",
        ],
        'blog_topic_examples': [
            '"How to find the right executive coach"',
            '"What happens in a coaching session"',
            '"Coaching vs therapy vs mentorship"',
            '"Signs you\'re ready for a coach"',
            '"How much does a coach cost and why"',
        ],
        'video_topic_examples': [
            "60-second insight video",
            "Client case study (anonymized + permissioned)",
            "Answering a common client question",
            "Philosophy video (what coaching means to you)",
            "Behind-the-scenes of a coaching session (generic)",
        ],
        'direct_mail_use': 'targeted executive outreach for high-ticket engagements',
        'referral_triggers': [
            "Client completes engagement and achieves their stated goal",
            "Client recommends a peer",
            "Client's results become visible to their network",
            "Milestone moments in the engagement",
        ],
        'review_platforms': ['Google Business Profile', 'LinkedIn recommendations', 'coach.me / provider directories'],
        'newsletter_topic_examples': [
            'January - goal-setting without hype',
            'March - mid-quarter recalibration',
            'June - mid-year audit',
            'September - fall reset',
            'December - year-end reflection without pressure',
        ],
        'ad_platforms': [
            'LinkedIn - executive and business-owner targeting',
            'Google Search - high-intent ("executive coach [city]")',
            'Facebook - warm-audience retargeting',
            'Podcast host-read (executive-focused shows)',
        ],
        'client_ed_docs': [
            'Coaching agreement template',
            'Session prep / debrief one-pager',
            'Values exercise worksheet',
            'Quarterly progress review template',
            '"Preparing for your first session" one-pager',
        ],
        'primary_asset_types': ['newsletter content', 'cohort launch emails', 'intake and progress tools'],
    },
)

print("\n✓ Batch 1 complete: Real Estate, Mortgage, Financial Advisor, Personal Trainer, Coach (5 × 17 = 85 pages)")
