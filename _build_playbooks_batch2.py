#!/usr/bin/env python3
"""Build playbooks batch 2: Dentist, Chiropractor, Attorney, CPA, Restaurant."""
from _build_playbook import build_playbook
from _playbook_content_factory import generate_modules, std_landing
from _playbook_middle_modules import middle_modules


def build(slug_dir, profession, short, tagline, spec_overrides):
    spec = {
        'profession': profession, 'short': short,
        'audience_description': spec_overrides.get('audience_description', 'clients'),
        'typical_client': spec_overrides.get('typical_client', 'your ideal client'),
        'legal_concerns': spec_overrides.get('legal_concerns', 'licensing board'),
        'revenue_model': spec_overrides.get('revenue_model', 'fee'),
        'common_channels': spec_overrides.get('common_channels', ['Facebook', 'Instagram']),
        'primary_asset_types': spec_overrides.get('primary_asset_types', ['emails', 'posts']),
        'compliance_notes': spec_overrides.get('compliance_notes', ['Industry rules']),
    }
    spec.update(spec_overrides)
    spec['custom_modules'] = middle_modules(spec)
    modules = generate_modules(spec)
    landing = std_landing(profession, short, tagline)
    build_playbook(slug_dir, profession, tagline, modules, landing)


# ============================================================
# DENTIST
# ============================================================
build(
    slug_dir="dentist",
    profession="The Dental Practice Claude Playbook",
    short="dental",
    tagline="For dentists, orthodontists, and practice owners: new-patient acquisition, educational content, referral building, review management. 15 modules, 60+ prompts.",
    spec_overrides={
        'audience_description': 'patients seeking dental care in your community',
        'typical_client': 'families with kids, adults 30-60, seniors, cosmetic-dentistry prospects',
        'legal_concerns': 'HIPAA, state dental board, ADA advertising guidelines, FTC health claims',
        'compliance_notes': [
            'HIPAA: never show PHI or identifiable patient info',
            'State dental board advertising rules',
            'No superlatives like "best dentist" unless substantiated',
            'Before/after photos need patient consent',
            'No guaranteed outcome claims',
            'Fee advertising rules vary by state',
            'ADA principles of ethics',
        ],
        'email_example': "A prospect who called asking about invisible braces pricing but hasn't scheduled a consult.",
        'social_topic_examples': [
            "The one thing most people brush wrong",
            "What a teeth cleaning actually includes",
            "Why patients skip cleanings (and why they shouldn't)",
            "Invisible braces vs traditional: who each is for",
            "Pediatric first dental visit: what to expect",
        ],
        'blog_topic_examples': [
            '"Dentist in [city]: how to choose the right practice"',
            '"Cost of invisible braces in [city]: what to expect"',
            '"Emergency dentist in [city]: what counts as emergency"',
            '"Cosmetic dentistry in [city]: whitening vs veneers vs bonding"',
            '"When should my child first see a dentist"',
        ],
        'video_topic_examples': [
            "Practice tour (30-60s)",
            "'Meet Dr. [Name]' intro",
            "Common procedure demo (patient-friendly)",
            "FAQ shorts",
            "Before/after reveals with consent",
        ],
        'direct_mail_use': 'welcoming new residents in your ZIP codes to the practice',
        'referral_triggers': [
            'After a successful completed case (implant, ortho, cosmetic)',
            'Family member comes in for the first time (refer another family)',
            'Patient compliments the hygienist or staff',
            'Successful emergency care that saved a tooth',
        ],
        'review_platforms': ['Google Business Profile', 'Yelp', 'Healthgrades', 'Zocdoc', 'Facebook'],
        'newsletter_topic_examples': [
            'January — dental resolutions (cleanings scheduled ahead)',
            'Spring — back-to-school sports mouthguards',
            'Summer — cosmetic dentistry before weddings/events',
            'October — dental benefits use-it-or-lose-it',
            'December — flex spending account dental use',
        ],
        'ad_platforms': [
            'Google Search — high-intent ("dentist near me", "emergency dentist")',
            'Facebook — local family targeting',
            'Instagram — cosmetic dentistry before/after',
            'Nextdoor — hyper-local neighborhood visibility',
        ],
        'client_ed_docs': [
            'New patient welcome packet',
            'Pre-procedure instructions (common procedures)',
            'Post-procedure care instructions',
            'Dental benefits guide (how to use your insurance)',
            'Pediatric first visit guide',
        ],
        'primary_asset_types': ['new-patient emails', 'procedure education', 'before/after content'],
    },
)


# ============================================================
# CHIROPRACTOR
# ============================================================
build(
    slug_dir="chiropractor",
    profession="The Chiropractor's Claude Playbook",
    short="chiropractic",
    tagline="For chiropractors: new-patient acquisition, pain education, corporate wellness partnerships, review and referral systems. 15 modules, 60+ prompts.",
    spec_overrides={
        'audience_description': 'patients with pain, injury, or wellness goals',
        'typical_client': 'adults with back/neck pain, athletes, postpartum moms, desk workers, accident recovery',
        'legal_concerns': 'state chiropractic board, HIPAA, FTC health claims, insurance billing rules',
        'compliance_notes': [
            'HIPAA: no PHI or identifiable patient cases without consent',
            'State chiropractic board rules on advertising',
            'FTC: no unsubstantiated claims about cures',
            'No "guaranteed relief" language',
            'Testimonial rules vary by state',
            'Billing transparency requirements',
        ],
        'email_example': "A potential patient who filled out a pain-intake form but hasn't booked their first visit.",
        'social_topic_examples': [
            "The one posture fix that helps most desk workers",
            "Why you should NOT crack your own neck",
            "What a first chiropractic visit actually includes",
            "Chiropractic during pregnancy: what's safe, what's not",
            "Whiplash recovery timeline (evidence-based)",
        ],
        'blog_topic_examples': [
            '"Chiropractor in [city]: what to expect at a first visit"',
            '"Chiropractor vs physical therapist: which for your situation"',
            '"Chiropractic for back pain from desk work"',
            '"Does insurance cover chiropractic in [state]"',
            '"Pediatric chiropractic: safety and evidence"',
        ],
        'video_topic_examples': [
            "30-second posture fix demo",
            "Office tour and Dr. intro",
            "Common adjustment demo (safe, educational)",
            "Anonymized patient progress story",
            "At-home stretch routine",
        ],
        'direct_mail_use': 'targeting new residents, families, or specific injury-prone demographics (office workers, athletes)',
        'referral_triggers': [
            "Patient hits pain-free milestone",
            "Patient refers a coworker or family member",
            "Accident recovery patient completes treatment",
            "Athlete returns to sport after injury",
        ],
        'review_platforms': ['Google Business Profile', 'Yelp', 'Healthgrades', 'Facebook', 'Nextdoor'],
        'newsletter_topic_examples': [
            'January — new year posture and movement goals',
            'Spring — gardening season injury prevention',
            'Summer — travel and back health',
            'Fall — back-to-school kids + sports',
            'December — holiday stress and body',
        ],
        'ad_platforms': [
            'Google Search — high-intent ("chiropractor near me")',
            'Facebook — local targeting + retargeting site visitors',
            'Instagram — demo and education reels',
            'Nextdoor — local reputation',
        ],
        'client_ed_docs': [
            'New patient welcome packet',
            'Insurance and billing guide',
            'Post-adjustment care instructions',
            'At-home stretch library',
            'Pain journal template',
        ],
        'primary_asset_types': ['new patient emails', 'pain education content', 'at-home instructions'],
    },
)


# ============================================================
# ATTORNEY
# ============================================================
build(
    slug_dir="attorney",
    profession="The Attorney's Claude Playbook",
    short="legal",
    tagline="For personal injury, family law, estate planning, and small-firm attorneys: content, intake, referral partnerships, review management. 15 modules, 60+ prompts.",
    spec_overrides={
        'audience_description': 'prospective clients needing legal services',
        'typical_client': 'personal injury claimants, divorce clients, estate planners, small business owners',
        'legal_concerns': 'state bar advertising rules, ABA Model Rules, attorney-client privilege, solicitation restrictions',
        'compliance_notes': [
            'State bar advertising rules (widely different by state)',
            'No guarantees of outcomes',
            'Required disclaimers in many states ("Advertising material", "Not a guarantee of results")',
            'Testimonial rules vary heavily',
            'Solicitation restrictions (no direct solicitation in some scenarios)',
            'Fee advertising rules',
            'Attorney identification requirements',
            'No comparison claims in some jurisdictions',
        ],
        'email_example': "A prospect who filled out your website contact form about a specific case type but didn't schedule a consult.",
        'social_topic_examples': [
            "The one thing most [case-type] clients do wrong in the first 24 hours",
            "What a free consultation actually covers",
            "Why you should NOT talk to the insurance company first",
            "Common mistakes in [practice area] cases",
            "How fees work in [practice area] (plain language)",
        ],
        'blog_topic_examples': [
            '"Personal injury attorney in [city]: what to do after an accident"',
            '"Divorce in [state]: timeline, costs, and process"',
            '"Estate planning basics for [age group] in [state]"',
            '"DUI attorney [city]: what happens after arrest"',
            '"Small business lawyer [city]: when you actually need one"',
        ],
        'video_topic_examples': [
            "Attorney intro video (who you are, who you help)",
            "Common case type explainer (60-90s)",
            "FAQ shorts for your practice area",
            "Courthouse or office tour",
            "Client case walkthrough (anonymized + permissioned)",
        ],
        'direct_mail_use': 'highly targeted outreach to specific demographics (new homeowners for estate, etc.) where allowed',
        'referral_triggers': [
            "Successful case outcome",
            "Client refers family member for same or related matter",
            "Other attorney refers a case outside their practice area",
            "CPA, financial advisor, or real estate agent refers a client",
        ],
        'review_platforms': ['Google Business Profile', 'Avvo', 'Martindale-Hubbell', 'Super Lawyers', 'Facebook', 'Yelp'],
        'newsletter_topic_examples': [
            'January — estate planning updates for new year',
            'April — tax-related legal issues',
            'Summer — travel-related legal concerns (accidents, etc.)',
            'October — year-end estate moves',
            'December — new year legal resolutions',
        ],
        'ad_platforms': [
            'Google Search — very high intent for PI, DUI, family',
            'LocalServices/LSAs — paid-per-lead Google ads',
            'Facebook — very limited for legal due to category restrictions',
            'YouTube — educational content for SEO + retargeting',
        ],
        'client_ed_docs': [
            'New client intake packet',
            'What to bring to your first meeting',
            '"What happens next" for common case types',
            'Fee agreement plain-language summary',
            'Estate planning document checklist',
        ],
        'primary_asset_types': ['intake emails', 'case education content', 'referral partner outreach'],
    },
)


# ============================================================
# CPA
# ============================================================
build(
    slug_dir="cpa",
    profession="The CPA's Claude Playbook",
    short="CPA",
    tagline="For CPAs, bookkeepers, and tax pros: tax-season content, small-business client acquisition, newsletters, referral systems. 15 modules, 60+ prompts.",
    spec_overrides={
        'audience_description': 'small business owners and individuals needing tax and accounting services',
        'typical_client': 'small business owners, self-employed, real estate investors, high-income W-2 earners',
        'legal_concerns': 'state board of accountancy, AICPA ethics, IRS Circular 230, state tax practitioner rules',
        'compliance_notes': [
            'State CPA board advertising rules',
            'AICPA Code of Professional Conduct',
            'IRS Circular 230 requirements for tax practitioners',
            'No specific tax-outcome guarantees',
            'Independence rules (no claims about independence if providing attest)',
            'Client confidentiality (§7216 restrictions on tax return information)',
        ],
        'email_example': "A small business owner who got recommended to you by another client but hasn't booked an initial call.",
        'social_topic_examples': [
            "The one deduction most small business owners miss",
            "When a S-corp actually saves you money (and when it costs you)",
            "Why filing an extension is NOT bad",
            "Quarterly estimated tax math simplified",
            "What actually triggers an IRS audit",
        ],
        'blog_topic_examples': [
            '"Do I need a CPA for my small business in [state]"',
            '"S-corp vs LLC: which for your situation"',
            '"Self-employed tax deductions you\'re probably missing"',
            '"Quarterly estimated taxes: a complete guide"',
            '"Real estate investor tax strategies in [state]"',
        ],
        'video_topic_examples': [
            "Weekly tax tip short",
            "Tax-season prep checklist (seasonal)",
            "Common question explainer (S-corp, deductions, etc.)",
            "Behind-the-scenes: how we work with clients",
            "Year-end tax planning",
        ],
        'direct_mail_use': 'targeted outreach to small business owners or high-income earners in specific ZIPs',
        'referral_triggers': [
            "Successful tax-season completion",
            "Saved the client money vs prior year",
            "Client's attorney or financial advisor introduces someone",
            "Small business owner hits a growth milestone",
        ],
        'review_platforms': ['Google Business Profile', 'Yelp', 'LinkedIn recommendations', 'Facebook'],
        'newsletter_topic_examples': [
            'January — tax season prep and new-year considerations',
            'April — post-filing review and quarterly planning',
            'June — mid-year strategy moves',
            'September — Q4 year-end planning starts',
            'December — last-minute tax moves',
        ],
        'ad_platforms': [
            'Google Search — high-intent tax season',
            'LinkedIn — small business owner targeting',
            'Facebook — local small business',
            'Industry publications (trade press for niches)',
        ],
        'client_ed_docs': [
            'New client onboarding + data request',
            'Tax-season documents checklist',
            '"What we need from you" for common engagements',
            'Tax-planning one-pagers (S-corp, deductions, etc.)',
            'Year-end checklist',
        ],
        'primary_asset_types': ['tax-season content', 'small-business education', 'quarterly check-ins'],
    },
)


# ============================================================
# RESTAURANT
# ============================================================
build(
    slug_dir="restaurant",
    profession="The Restaurant Owner's Claude Playbook",
    short="restaurant",
    tagline="For restaurant and local hospitality operators: social, email, Google, delivery platforms, review management, local SEO. 15 modules, 60+ prompts.",
    spec_overrides={
        'audience_description': 'local diners in your service area',
        'typical_client': 'locals, commuters, families, tourists, event diners',
        'legal_concerns': 'health and food safety regulations, alcohol advertising rules, menu labeling, ADA accessibility',
        'compliance_notes': [
            'State alcohol advertising rules if you serve',
            'FDA menu labeling requirements (20+ location chains)',
            'Allergen disclosure',
            'ADA compliance for digital menus',
            'Truth-in-menu laws (no misrepresenting origin, size, etc.)',
            'Delivery platform TOS',
        ],
        'email_example': "A past diner who redeemed a birthday email offer last year but hasn't been back in 6 months.",
        'social_topic_examples': [
            "Behind-the-scenes: preparing [signature dish]",
            "Menu item spotlight with the story",
            "Staff intro post",
            "Sourcing story (local farm, fish market, etc.)",
            "Seasonal menu changes",
        ],
        'blog_topic_examples': [
            '"Best [cuisine type] in [city]"',
            '"[City] date night restaurants"',
            '"Private events at [your restaurant]"',
            '"Our [signature dish]: the story behind it"',
            '"Seasonal menu changes at [your restaurant]"',
        ],
        'video_topic_examples': [
            "Kitchen action shots (quick cuts)",
            "Dish reveal (plated meal shots)",
            "Chef or owner intro",
            "Customer moment (with permission)",
            "Event setup or private dining tour",
        ],
        'direct_mail_use': 'neighborhood EDDM (every-door direct mail) for grand openings, promotions, or seasonal events',
        'referral_triggers': [
            "Successful private event",
            "Great experience that gets a compliment",
            "Regular who brings new people",
            "Review from a local influencer",
        ],
        'review_platforms': ['Google Business Profile', 'Yelp', 'TripAdvisor', 'OpenTable', 'Facebook', 'Resy'],
        'newsletter_topic_examples': [
            'January — new menu, new year',
            'Valentine\'s/Mother\'s Day — event bookings',
            'Summer — patio season, events',
            'Fall — harvest menu',
            'December — holiday hours, gift cards, private events',
        ],
        'ad_platforms': [
            'Meta (Facebook + Instagram) — visual-heavy, local radius targeting',
            'Google Local Service Ads + local search',
            'Yelp Ads if ROI works in your market',
            'Nextdoor — hyper-local',
        ],
        'client_ed_docs': [
            'Private event FAQ and pricing sheet',
            'Allergen menu',
            'Group booking info sheet',
            'Loyalty program overview',
            'Catering menu',
        ],
        'primary_asset_types': ['menu updates', 'event promotion', 'social content', 'review responses'],
    },
)

print("\n✓ Batch 2 complete: Dentist, Chiropractor, Attorney, CPA, Restaurant (5 × 17 = 85 pages)")
