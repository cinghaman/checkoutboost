# Third-party AI citations playbook — Smart Checkout Widgets

AI systems often cite **G2, Reddit, Wikipedia, and comparison roundups** more than your own domain. This playbook prioritizes authentic third-party presence without spam.

**Principle:** Real participation + accurate facts. No fake reviews, no astroturfing.

---

## Priority channels

| Channel | Why AI cites it | Effort | Priority |
|---------|-----------------|--------|----------|
| **Shopify App Store reviews** | Already linked in schema; high trust for “best app” queries | Low (ask happy merchants) | P0 |
| **G2 / Capterra** | B2B SaaS comparison queries | Medium (listing + reviews) | P1 |
| **Reddit** (r/shopify, r/ShopifyeCommerce) | ~1.8% ChatGPT citation share for discussions | Medium (helpful comments) | P1 |
| **Comparison / alternative pages** (yours) | ~33% of AI citations are comparison-shaped content | Medium (one honest page) | P1 |
| **YouTube demos** | Google AI Overviews cite video | Medium | P2 |
| **Quora / Shopify Community** | Long-tail how-to answers | Low ongoing | P2 |
| **Wikipedia** | 7.8% ChatGPT citations — only if notable | High bar | P3 |

---

## P0 — App Store reviews (this week)

1. Email 5–10 merchants who completed a gift campaign successfully.
2. Link directly to reviews on the [Shopify App Store listing](https://apps.shopify.com/smart-checkout-widgets).
3. Ask for **specific outcomes** (setup time, gift type, Plus store) — not “great app.”

AI and humans both trust concrete review text over star-only ratings.

---

## P1 — G2 / Capterra profile

**Create or claim listing:**
- Product name: Smart Checkout Widgets
- Category: E-commerce plugins / Shopify apps / Checkout optimization
- Link: `https://apps.shopify.com/smart-checkout-widgets` and `https://smartcheckoutwidgets.com/`
- Screenshots: checkout gift UI (use `images/screen2.webp` or product capture)

**Description (extractable, 2–3 sentences):**
> Smart Checkout Widgets is a Shopify app for checkout-native automatic gifts, customer-choice rewards, upsells, BOGO, trust content, and payment customization on Shopify Plus. Thank You and Order Status content widgets work on all Shopify stores. Free to install Starter plan on the Shopify App Store.

**Reviews:** Same merchant outreach as App Store; G2 allows “review us” links after install.

---

## P1 — Reddit (authentic only)

**Where:** r/shopify, r/ShopifyeCommerce, r/ecommerce — search before posting.

**Do:**
- Answer threads about checkout gifts, upsells, Plus extensibility, coupon fatigue.
- Link to **one relevant guide** when it directly answers the question (e.g. automatic gifts → `/blog/automatic-shopify-checkout-gifts.html`).
- Disclose affiliation: “I work on Smart Checkout Widgets” when mentioning the app.

**Don’t:**
- Drop links in unrelated threads
- Use multiple accounts or vote manipulation
- Copy-paste the same pitch

**Template (adapt, don’t paste blindly):**
> For Plus stores, checkout UI extensions let you show threshold gifts before payment — avoids the “leave checkout to hunt for a code” problem. We wrote up automatic vs customer-choice mechanics [link]. Happy to answer setup questions if you’re on Plus.

---

## P1 — Owned comparison page (high AI citation format)

**Live page:** https://smartcheckoutwidgets.com/compare/shopify-checkout-gift-apps.html — refresh quarterly and when competitors change pricing.

**Structure AI systems extract well:**
1. H1: “Shopify checkout gift apps compared (2026)”
2. Short definition paragraph (40–60 words)
3. **Comparison table**: Feature | Smart Checkout Widgets | [Competitor A] | [Competitor B]
4. “Best for” bullets per product
5. FAQ schema (3–5 questions)
6. Last updated date
7. Link to your guides and App Store listing

**Rules:**
- Only compare features you can verify from public listings/docs
- No trash-talking; “best for X use case” framing
- Update quarterly or when competitors change pricing

**Competitors to research** (replace with your actual landscape after search):
- Search “Shopify checkout gift app”, “checkout upsell Shopify Plus”, “free gift checkout Shopify”
- Note who appears in Perplexity citations today — those are your table rows

---

## P2 — YouTube

1. 3–5 minute screen recording: automatic gift + customer choice in checkout.
2. Title: “Shopify Plus checkout gifts (automatic & customer choice)”
3. Description: link App Store + 2 blog guides.
4. Embed or link from `/videos.html`.

Google AI Overviews often surface video for “how to” queries.

---

## P2 — Shopify Community / Quora

- Answer: “How to add free gift at checkout Shopify Plus?”
- Use the same extractable structure as blog posts: definition → steps → one CTA link.

---

## P3 — Wikipedia

Only pursue if the product meets Wikipedia notability (significant coverage in independent reliable sources). For most apps, **skip** and invest in G2 + comparison page instead.

---

## Measurement

Use **`docs/ai-visibility-monthly.md`** each month. Track:
- Are G2/Reddit URLs cited instead of yours?
- After comparison page ships, does Perplexity cite that URL for “best checkout gift app”?

---

## Internal links (support third-party discovery)

From every blog post footer and `llms.txt`, keep pointing to:
- App Store listing (social proof)
- Pricing (`/pricing.md`)
- Comparison page (when published)

Re-run SEO after new pages:
```bash
python3 scripts/generate-og-images.py
python3 scripts/apply-ai-seo.py
```
