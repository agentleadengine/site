#!/usr/bin/env python3
"""Build playbooks batch 3: Marketing Agency, Ecom founder, SaaS founder, Podcaster, Author."""
from _build_playbook import build_playbook
from _playbook_content_factory import generate_modules, std_landing
from _playbook_middle_modules import middle_modules


def build(slug_dir, profession, short, tagline, spec_overrides):
    spec = {
        'profession': profession, 'short': short,
        'audience_description': spec_overrides.get('audience_description', 'clients'),
        'typical_client': spec_overrides.get('typical_client', 'your ideal client'),
        'legal_concerns': spec_overrides.get('legal_concerns', 'your industry rules'),
        'revenue_model': spec_overrides.get('revenue_model', 'fee'),
        'common_channels': spec_overrides.get('common_channels', ['Facebook', 'LinkedIn']),
        'primary_asset_types': spec_overrides.get('primary_asset_types', ['emails', 'posts']),
        'compliance_notes': spec_overrides.get('compliance_notes', ['Industry rules']),
    }
    spec.update(spec_overrides)
    spec['custom_modules'] = middle_modules(spec)
    modules = generate_modules(spec)
    landing = std_landing(profession, short, tagline)
    build_playbook(slug_dir, profession, tagline, modules, landing)


# ============================================================
# MARKETING AGENCY
# ============================================================
build(
    slug_dir="agency",
    profession="The Marketing Agency Claude Playbook",
    short="agency",
    tagline="For agency founders and account teams: prospecting, case studies, thought leadership, proposal templates, retention content. 15 modules, 60+ prompts.",
    spec_overrides={
        'audience_description': 'B2B decision-makers who hire agencies',
        'typical_client': 'marketing directors, VPs of marketing, founders at $5M-$100M companies',
        'legal_concerns': 'FTC endorsement rules, client confidentiality in case studies, MSA and IP considerations',
        'compliance_notes': [
            'FTC rules on testimonials and typicality of results',
            'Client confidentiality in case studies (permission required)',
            'Performance claims need substantiation',
            'IP and work ownership clauses in your MSA',
            'Subcontracting disclosures where relevant',
        ],
        'email_example': "A VP of Marketing at a Series B SaaS company whose current agency retainer is coming up for renewal.",
        'social_topic_examples': [
            "The specific mistake most in-house teams make with paid search",
            "A teardown of a competitor's onboarding flow (with permission)",
            "Why \"we do everything\" agencies always lose",
            "Something you just learned running 10 campaigns",
            "Anonymized client outcome + what drove it",
        ],
        'blog_topic_examples': [
            '"B2B marketing agency vs in-house: when each makes sense"',
            '"[Specific service] agency in [city]: what to look for"',
            '"How to evaluate a marketing agency proposal"',
            '"Why agency retainers fail in year two"',
            '"Case study: [anonymized client outcome]"',
        ],
        'video_topic_examples': [
            "Teardown videos (site, ads, funnel with permission)",
            "Weekly POV on something in your industry",
            "Behind-the-scenes of an agency workflow",
            "Client-story video (anonymized)",
            "Quick take on a platform update",
        ],
        'direct_mail_use': 'high-ticket enterprise prospecting with "shock and awe" packages',
        'referral_triggers': [
            "Case study published with client's permission",
            "Successful campaign launch",
            "Client's peer asks about working with you",
            "Annual review that went well",
        ],
        'review_platforms': ['Clutch', 'Google Business Profile', 'G2', 'LinkedIn recommendations', 'DesignRush'],
        'newsletter_topic_examples': [
            'Monthly - one specific win or insight from current campaigns',
            'Seasonal market shifts and implications',
            'Platform change reactions (algo updates, etc.)',
            'Tactical breakdowns of trending strategies',
        ],
        'ad_platforms': [
            'LinkedIn - high-intent B2B decision-maker targeting',
            'Google Search - high-intent keywords for agency services',
            'Podcast host-read sponsorships',
            'Industry publication placements',
        ],
        'client_ed_docs': [
            'Agency engagement model + MSA summary',
            'Onboarding + kickoff packet',
            'Quarterly reporting template',
            'Scope-of-work library',
            'Case study library (anonymized)',
        ],
        'primary_asset_types': ['prospecting emails', 'case studies', 'thought leadership content', 'proposals'],
    },
)


# ============================================================
# ECOM FOUNDER
# ============================================================
build(
    slug_dir="ecommerce",
    profession="The E-commerce Founder's Claude Playbook",
    short="ecommerce",
    tagline="For DTC founders and e-commerce operators: email flows, product launches, retention, UGC, influencer outreach, retention content. 15 modules, 60+ prompts.",
    spec_overrides={
        'audience_description': 'consumers in your brand\'s category',
        'typical_client': 'first-time visitors, cart abandoners, one-time buyers, VIPs, email subscribers',
        'legal_concerns': 'FTC endorsement rules, state privacy (CCPA, CPRA), email marketing (CAN-SPAM), product safety claims',
        'compliance_notes': [
            'FTC: clear #ad / #sponsored for paid influencers',
            'CAN-SPAM: unsubscribe, sender info',
            'CCPA/CPRA (if California visitors): privacy policy, data rights',
            'Product safety claims must be substantiated',
            'Country-of-origin claims',
            'Charitable donation claims must be accurate',
        ],
        'email_example': "A cart abandoner who added a high-consideration item ($100+) and didn't purchase within 24 hours.",
        'social_topic_examples': [
            "How you make / source the product (factory or farm footage)",
            "Customer UGC (with permission)",
            "Behind-the-scenes of a launch",
            "Founder story / why you started the brand",
            "Myth-busting in your category",
        ],
        'blog_topic_examples': [
            '"Best [category] for [specific use case]"',
            '"[Your brand] vs [competitor]: an honest comparison"',
            '"How to choose the right [product]"',
            '"[Product category] ingredients guide"',
            '"The story of [flagship product]"',
        ],
        'video_topic_examples': [
            "Product hero video",
            "UGC-style unboxing",
            "Founder story (90 seconds)",
            "How-to-use videos for your products",
            "Customer transformation / review",
        ],
        'direct_mail_use': 'unique insert cards for orders, or postcards to previous customers for re-engagement',
        'referral_triggers': [
            "Successful purchase after a long consideration",
            "Repeat purchase (order #2, #3)",
            "Customer posts UGC",
            "VIP customer milestone (spending threshold)",
        ],
        'review_platforms': ['Trustpilot', 'Google', 'Amazon (if applicable)', 'Your own product pages', 'Yotpo / Stamped'],
        'newsletter_topic_examples': [
            'New collection launches',
            'Behind-the-scenes content',
            'Founder updates and brand milestones',
            'Seasonal campaigns (gift guides, anniversary)',
            'Customer spotlights',
        ],
        'ad_platforms': [
            'Meta (Facebook + Instagram) - core DTC channel',
            'TikTok Ads',
            'Google Shopping + Performance Max',
            'YouTube Shorts',
            'Email (owned) and SMS for retention',
        ],
        'client_ed_docs': [
            'Welcome flow for new subscribers',
            'Post-purchase education (how to use / care for product)',
            'FAQ addressing top 5 pre-purchase questions',
            'Size/fit/selection guides',
            'Gift guide (seasonal)',
        ],
        'primary_asset_types': ['email flows', 'product launch campaigns', 'UGC and influencer content'],
    },
)


# ============================================================
# SAAS FOUNDER
# ============================================================
build(
    slug_dir="saas",
    profession="The SaaS Founder's Claude Playbook",
    short="SaaS",
    tagline="For B2B SaaS founders in seed through Series B: content, community, outbound, onboarding emails, churn prevention. 15 modules, 60+ prompts.",
    spec_overrides={
        'audience_description': 'B2B prospects in your ICP and existing users',
        'typical_client': 'heads of department or IC power users at your ICP company size',
        'legal_concerns': 'SaaS contract terms, DPA/privacy, B2B email regulations, FTC on performance claims',
        'compliance_notes': [
            'Clear data processing and privacy policies (DPA, GDPR if EU users)',
            'CAN-SPAM compliance for marketing emails',
            'Claims about ROI must be substantiated',
            'Testimonial disclosures (typicality)',
            'Terms of service must match what marketing promises',
            'HIPAA / SOC 2 claims must be backed by actual certifications',
        ],
        'email_example': "A power user at a target company who signed up for a free trial but hasn't upgraded in 21 days.",
        'social_topic_examples': [
            "A specific customer outcome (with permission)",
            "A technical insight your engineering team shared",
            "The one metric most [role] get wrong",
            "Changelog / product update short-form",
            "Founder learnings (honest, specific)",
        ],
        'blog_topic_examples': [
            '"[Your category] vs [alt category]: when each wins"',
            '"How to [specific outcome with your tool]"',
            '"[Your tool] integration with [common tool]"',
            '"State of [your category] in 2026"',
            '"Pricing [your category]: a buyer\'s guide"',
        ],
        'video_topic_examples': [
            "Product walkthrough (60-90s)",
            "Feature release announcement",
            "Customer interview (anonymized or permissioned)",
            "Founder update / changelog",
            "Category education",
        ],
        'direct_mail_use': 'targeted enterprise outreach with "shock and awe" packages for named accounts',
        'referral_triggers': [
            "Customer hits their desired outcome",
            "Expansion or upgrade",
            "Customer praises you in community or social",
            "Long-tenure customer milestone",
        ],
        'review_platforms': ['G2', 'Capterra', 'TrustRadius', 'Product Hunt', 'GetApp'],
        'newsletter_topic_examples': [
            'Monthly product changelog + behind-the-scenes',
            'Customer spotlights',
            'State-of-category analyses',
            'Founder essays',
            'Release notes for power users',
        ],
        'ad_platforms': [
            'LinkedIn - job title + company targeting',
            'Google Search - high-intent category keywords',
            'Reddit + niche community ads',
            'Podcast host-read',
            'Sponsorships of target-audience newsletters',
        ],
        'client_ed_docs': [
            'Onboarding email series (7-14 days)',
            'Quick-start guide',
            'Common workflows / template library',
            'Integrations documentation',
            'Upgrade / expansion path',
        ],
        'primary_asset_types': ['onboarding emails', 'product launches', 'category content', 'customer stories'],
    },
)


# ============================================================
# PODCASTER / CREATOR
# ============================================================
build(
    slug_dir="podcaster",
    profession="The Podcaster + Creator Claude Playbook",
    short="podcasting",
    tagline="For podcasters, YouTubers, and newsletter creators: show notes, social, audience growth, sponsor outreach, email newsletters. 15 modules, 60+ prompts.",
    spec_overrides={
        'audience_description': 'your audience and new listeners in your niche',
        'typical_client': 'listeners, viewers, newsletter subscribers, potential sponsors',
        'legal_concerns': 'FTC disclosure rules for sponsored content, copyright and music licensing, platform TOS',
        'compliance_notes': [
            'FTC: clear #ad / #sponsored for paid integrations',
            'Music licensing (you need rights to every track used)',
            'Copyright for clips and quotes',
            'Platform TOS (YouTube, Spotify, Apple)',
            'Privacy policy for email subscribers',
            'Testimonial rules if using listener testimonials',
        ],
        'email_example': "A podcast listener who's listened to 15+ episodes but hasn't subscribed to the newsletter.",
        'social_topic_examples': [
            "A specific insight from a recent interview",
            "Behind-the-scenes of an episode",
            "Controversial take you're willing to defend",
            "Listener question answered in depth",
            "Guest story or quote (with attribution)",
        ],
        'blog_topic_examples': [
            'Full episode show-notes pages (each episode = one blog)',
            '"Best [topic] podcasts to listen to in 2026"',
            '"Lessons from [X episodes / Y guests]"',
            '"[Topic] guide" pieces that can be repeated-promoted across episodes',
            'Seasonal "best of" roundups',
        ],
        'video_topic_examples': [
            "Clip from episode (60-90s)",
            "Behind-the-scenes shorts",
            "Standalone YouTube essay",
            "Q&A with audience",
            "Sponsor integration (when appropriate)",
        ],
        'direct_mail_use': 'unusual outreach to potential guests or sponsors',
        'referral_triggers': [
            "Listener shares an episode organically",
            "Guest refers another potential guest",
            "Subscriber forwards newsletter",
            "Someone mentions you in media",
        ],
        'review_platforms': ['Apple Podcasts', 'Spotify', 'Podchaser', 'YouTube comments'],
        'newsletter_topic_examples': [
            'Weekly episode recap + links',
            'Guest spotlight and why they matter',
            'Listener questions answered',
            'Behind-the-scenes of production',
            'Curated content from around your space',
        ],
        'ad_platforms': [
            'Other podcasts (cross-promotion)',
            'YouTube Ads pre-roll',
            'Meta - lookalike of current subscribers',
            'Newsletter sponsorship swaps',
        ],
        'client_ed_docs': [
            'Guest prep sheet (what to expect, agenda)',
            'Sponsor media kit',
            'Audience stats one-pager',
            'Pitch template for potential guests',
            'Production process overview for new team members',
        ],
        'primary_asset_types': ['show notes', 'newsletter content', 'guest/sponsor outreach', 'clips and promos'],
    },
)


# ============================================================
# AUTHOR / SELF-PUBLISHER
# ============================================================
build(
    slug_dir="author",
    profession="The Author's Claude Playbook",
    short="author",
    tagline="For fiction and nonfiction authors: book launch, list growth, email, podcast tours, social content, ARC outreach. 15 modules, 60+ prompts.",
    spec_overrides={
        'audience_description': 'readers in your genre and existing fans',
        'typical_client': 'readers, newsletter subscribers, ARC readers, reviewers, bookstores',
        'legal_concerns': 'FTC disclosure for promotional reviews, copyright, Amazon TOS for launch strategies',
        'compliance_notes': [
            'Amazon TOS on reviews (no incentivized reviews without disclosure)',
            'FTC rules on review disclosures',
            'Copyright if quoting other works',
            'Trademark if using others\' character names, etc.',
            'Privacy for reader email lists',
        ],
        'email_example': "A newsletter subscriber who grabbed your free prequel story but hasn't purchased your main book yet.",
        'social_topic_examples': [
            "Behind-the-scenes: the specific scene that was hard to write",
            "Research moments (photos, interviews, etc.)",
            "Character inspiration",
            "What you're reading now",
            "Milestone moments (book contract, release dates, reviews)",
        ],
        'blog_topic_examples': [
            '"Behind [book title]: the inspiration story"',
            '"Books like [popular comp title]: my recommendations"',
            'Deep character or worldbuilding posts',
            'Reader letter / AMAs',
            'Writing process essays',
        ],
        'video_topic_examples': [
            "Book reveal / cover reveal",
            "Character intro shorts",
            "Behind-the-scenes writing life",
            "Reading aloud from the book",
            "Author interview content",
        ],
        'direct_mail_use': 'ARC (advance reader copy) outreach to reviewers, bloggers, and bookstagrammers',
        'referral_triggers': [
            "Reader leaves a heartfelt review",
            "ARC reader posts their thoughts",
            "Book club selects your book",
            "Librarian or bookseller recommends",
        ],
        'review_platforms': ['Amazon', 'Goodreads', 'BookBub', 'BookTok / Bookstagram', 'Barnes & Noble'],
        'newsletter_topic_examples': [
            'Release-day content',
            'Behind-the-scenes of next book',
            'Exclusive short stories or deleted scenes',
            'Reading recommendations',
            'Reader spotlights / fan art',
        ],
        'ad_platforms': [
            'Amazon Ads (sponsored products)',
            'BookBub Ads',
            'Facebook Ads for launches',
            'Google Ads on title searches',
            'TikTok / Instagram for genre-aligned content',
        ],
        'client_ed_docs': [
            'Reader starter guide (where to begin reading you)',
            'ARC expectations + review instructions',
            'Book club discussion questions',
            'Series reading order guide',
            'Glossary or companion guide for complex worlds',
        ],
        'primary_asset_types': ['launch emails', 'social content', 'ARC outreach', 'newsletter'],
    },
)

print("\n✓ Batch 3 complete: Agency, E-commerce, SaaS, Podcaster, Author (5 × 17 = 85 pages)")
