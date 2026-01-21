import json
import random

OUTPUT_FILE = "data\marketing_bot\marketing_conversations.jsonl"

# -------------------------
# CORE QUESTION BANKS
# -------------------------

saas_questions = [
    "How do I increase free trial conversions?",
    "How can I reduce churn for my SaaS product?",
    "What onboarding emails should a SaaS company send?",
    "How do I price my SaaS product?",
    "How can I improve product adoption?"
]

ecommerce_questions = [
    "How do I reduce cart abandonment?",
    "What makes a good product description?",
    "How can I increase average order value?",
    "How do I run successful holiday promotions?",
    "What email flows should an ecommerce store have?"
]

local_business_questions = [
    "How can I get more local customers?",
    "How do I improve Google My Business visibility?",
    "What’s the best way to collect customer reviews?",
    "How do I market a local service business?",
    "How can I increase repeat customers?"
]

# -------------------------
# ANSWER TEMPLATES
# -------------------------

saas_answers = [
    "Focus on a frictionless onboarding experience, guide users to their first win quickly, and use behavioral emails to re-engage inactive users. Clear value communication during the trial is critical.",
    "Reduce churn by improving onboarding, monitoring usage metrics, proactively reaching out to at-risk users, and continuously communicating product value.",
    "A SaaS onboarding sequence should include a welcome email, setup guidance, feature highlights, use cases, and social proof.",
    "SaaS pricing should be based on value, target customer size, and willingness to pay. Consider tiered plans with clear upgrade paths.",
    "Improve adoption by simplifying UX, providing in-app guidance, and reinforcing key use cases through email and tutorials."
]

ecommerce_answers = [
    "Reduce cart abandonment by adding trust badges, simplifying checkout, offering free shipping thresholds, and sending abandoned cart emails.",
    "Good product descriptions focus on benefits, address objections, include social proof, and clearly explain how the product improves the customer’s life.",
    "Increase AOV with bundles, upsells, cross-sells, and free shipping thresholds.",
    "Holiday promotions work best when planned early, clearly communicated, and supported by urgency and limited-time offers.",
    "Key ecommerce email flows include welcome, abandoned cart, post-purchase, win-back, and promotional campaigns."
]

local_business_answers = [
    "Local businesses should focus on local SEO, Google reviews, referral programs, and consistent social media engagement.",
    "Improve Google My Business visibility by optimizing your profile, posting updates, collecting reviews, and responding to customers.",
    "Collect reviews by asking at the right time, making it easy, and following up via email or SMS.",
    "Market a local service business using local ads, partnerships, referrals, and community engagement.",
    "Increase repeat customers through loyalty programs, follow-up messages, and excellent service."
]

# -------------------------
# MULTI-TURN SALES FLOWS
# -------------------------

sales_conversations = [
    [
        ("user", "I’m interested in your software, but it seems expensive."),
        ("assistant", "That’s a common concern. Most customers find that the time and cost savings quickly outweigh the price."),
        ("user", "How long does it usually take to see results?"),
        ("assistant", "Many customers see measurable improvements within the first 30 days, especially when following our onboarding process.")
    ],
    [
        ("user", "I’m not sure this is right for my business."),
        ("assistant", "That’s understandable. Can you share what type of business you run?"),
        ("user", "I run a small ecommerce store."),
        ("assistant", "In that case, our solution is designed specifically to help stores like yours increase conversions and automate marketing.")
    ],
    [
        ("user", "What makes this better than competitors?"),
        ("assistant", "Our platform focuses on simplicity, faster implementation, and personalized support, which many competitors lack.")
    ]
]

# -------------------------
# GENERATION LOGIC
# -------------------------

def single_turn_conversation(q, a):
    return {
        "messages": [
            {"role": "user", "content": q},
            {"role": "assistant", "content": a}
        ]
    }

def multi_turn_conversation(flow):
    return {
        "messages": [
            {"role": role, "content": text} for role, text in flow
        ]
    }

conversations = []

# Generate single-turn niche conversations
for _ in range(400):
    q = random.choice(saas_questions)
    a = random.choice(saas_answers)
    conversations.append(single_turn_conversation(q, a))

for _ in range(400):
    q = random.choice(ecommerce_questions)
    a = random.choice(ecommerce_answers)
    conversations.append(single_turn_conversation(q, a))

for _ in range(400):
    q = random.choice(local_business_questions)
    a = random.choice(local_business_answers)
    conversations.append(single_turn_conversation(q, a))

# Generate multi-turn sales conversations
for _ in range(200):
    conversations.append(multi_turn_conversation(random.choice(sales_conversations)))

# Shuffle for better training distribution
random.shuffle(conversations)

# -------------------------
# WRITE FILE
# -------------------------

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for conv in conversations:
        f.write(json.dumps(conv, ensure_ascii=False) + "\n")

print(f"Generated {len(conversations)} conversations → {OUTPUT_FILE}")
