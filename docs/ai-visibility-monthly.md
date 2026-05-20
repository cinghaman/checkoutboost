# Monthly AI visibility check — Smart Checkout Widgets

Run this on the **first week of each month**. Goal: see whether you are cited in AI answers for checkout gifting queries, and which competitors appear instead.

**Time:** ~45 minutes manual, or use Otterly / Peec / ZipTie if you subscribe.

---

## 1. Core queries to test (20)

Copy each query into **Google** (note AI Overview), **ChatGPT** (with browsing on), and **Perplexity**. Record results in the log table below.

| # | Query |
|---|--------|
| 1 | Shopify checkout gifts |
| 2 | automatic free gift Shopify checkout |
| 3 | customer choice gift Shopify checkout |
| 4 | Shopify Plus checkout upsells |
| 5 | checkout extensibility Shopify Plus |
| 6 | BOGO automatic discount Shopify checkout |
| 7 | trust badges Shopify checkout |
| 8 | payment customization Shopify checkout |
| 9 | Thank You page widgets Shopify |
| 10 | Smart Checkout Widgets |
| 11 | best Shopify checkout gift app |
| 12 | Shopify checkout merchandising app |
| 13 | increase AOV Shopify checkout |
| 14 | free gift at checkout Shopify Plus |
| 15 | checkout UI extensions gifting |
| 16 | alternative to coupon codes checkout Shopify |
| 17 | post-purchase upsell vs checkout upsell Shopify |
| 18 | Smart Checkout Widgets review |
| 19 | Shopify app checkout widgets comparison |
| 20 | Thought Bulb Shopify checkout |

**Owned comparison URL to watch:** https://smartcheckoutwidgets.com/compare/shopify-checkout-gift-apps.html

Optional CSV log: copy `docs/ai-visibility-log-template.csv` each month.

---

## 2. Monthly log (copy a new section each month)

### YYYY-MM

| Query | Google AI Overview | ChatGPT cites SCW? | Perplexity cites SCW? | Top competitor cited | URL cited (yours or theirs) |
|-------|:------------------:|:------------------:|:---------------------:|----------------------|----------------------------|
| 1 | | | | | |
| … | | | | | |

**SCW** = Smart Checkout Widgets (your site or App Store listing).

**Pass criteria (directional):**
- Cited on **≥3** priority queries (1–10) on at least one platform
- Your **blog guide** URL cited (not only homepage)
- No incorrect claims (pricing, Plus-only features)

---

## 3. What to do based on results

| Signal | Action |
|--------|--------|
| Not cited on gifting queries | Strengthen hub page + internal links; pitch G2/Reddit (see third-party playbook) |
| Competitor comparison cited, not you | Publish or refresh a comparison page (honest, structured table) |
| Wrong product facts in AI answer | Update `llms.txt`, `pricing.md`, and App Store listing; add FAQ on relevant blog post |
| Only App Store cited, not blog | Add `sameAs` and links from listing; cross-link guides in llms.txt |
| Cited on Perplexity but not Google | Normal — keep E-E-A-T and core SEO; Google follows rankings more |

---

## 4. On-site checks (same day)

- [ ] `https://smartcheckoutwidgets.com/robots.txt` — AI bots still allowed
- [ ] `https://smartcheckoutwidgets.com/sitemap.xml` — all blog URLs present
- [ ] `https://smartcheckoutwidgets.com/llms.txt` — loads, links current
- [ ] Random blog post — `og:image` unique, JSON-LD validates ([Rich Results Test](https://search.google.com/test/rich-results))
- [ ] Re-run after content changes: `python3 scripts/apply-ai-seo.py`

---

## 5. Referral traffic (optional)

In GA4, watch referrals from:
- `chatgpt.com`, `perplexity.ai`, `copilot.microsoft.com`, `gemini.google.com`

Spikes after publishing a comparison page or G2 review often show up here before rank changes.

---

## 6. Files to update when you learn something

| Finding | Update |
|---------|--------|
| New priority query | Add to section 1 + test monthly |
| New competitor always cited | Add to `docs/third-party-ai-citations-playbook.md` |
| New blog post | `scripts/apply-ai-seo.py` + `python3 scripts/generate-og-images.py` |
