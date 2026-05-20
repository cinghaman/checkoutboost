#!/usr/bin/env python3
"""Apply JSON-LD, full OG/Twitter meta, FAQ blocks, sitemap, and AI files."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import seo  # noqa: E402

BLOG_DIR = ROOT / "blog"
LASTMOD = "2026-05-20"
OG_BASE = seo.SITE + "/images/og"

OG_IMAGES = {
    "default": (OG_BASE + "/default.webp", "Smart Checkout Widgets — Shopify Plus checkout gifts and upsells"),
    "automatic-shopify-checkout-gifts.html": (
        OG_BASE + "/automatic-gifts.webp",
        "Guide: automatic gifts in Shopify checkout",
    ),
    "customer-choice-free-gift-shopify-checkout.html": (
        OG_BASE + "/customer-choice-gifts.webp",
        "Guide: customer-choice free gifts at Shopify checkout",
    ),
    "shopify-checkout-gift-strategy-aov.html": (
        OG_BASE + "/gift-strategy-aov.webp",
        "Guide: checkout gift strategy for higher AOV",
    ),
    "shopify-checkout-upsells.html": (
        OG_BASE + "/checkout-upsells.webp",
        "Guide: Shopify checkout upsells",
    ),
    "shopify-checkout-bogo-automatic-discounts.html": (
        OG_BASE + "/bogo-discounts.webp",
        "Guide: BOGO and automatic discounts in Shopify checkout",
    ),
    "shopify-checkout-trust-badges-payment.html": (
        OG_BASE + "/trust-payments.webp",
        "Guide: trust badges and payment customization at checkout",
    ),
    "shopify-plus-checkout-extensibility-guide.html": (
        OG_BASE + "/checkout-extensibility.webp",
        "Guide: Shopify Plus checkout extensibility",
    ),
    "shopify-thank-you-order-status-widgets.html": (
        OG_BASE + "/thank-you-order-status.webp",
        "Guide: Thank You and Order Status widgets",
    ),
    "compare/shopify-checkout-gift-apps.html": (
        OG_BASE + "/compare.webp",
        "Compare Shopify checkout gift and merchandising apps",
    ),
}

COMPARE_FAQS = [
    {
        "q": "What is the best Shopify checkout gift app?",
        "a": "The best fit depends on whether you need only a fixed gift or a full checkout stack (gifts, upsells, trust, payment tweaks). Compare features on the Shopify App Store and test on a development store before launch.",
    },
    {
        "q": "Do checkout gift apps require Shopify Plus?",
        "a": "Native checkout UI extensions for gifts and upsells typically require Shopify Plus. Thank You and Order Status content widgets may be available on all plans — verify on each app listing.",
    },
    {
        "q": "How is Smart Checkout Widgets priced?",
        "a": "Starter is free to install on the Shopify App Store with order limits; Growth and Advanced are paid tiers with trials. See pricing.md and the public listing for current numbers.",
    },
]

# slug -> headline (for schema), faqs
ARTICLE_META = {
    "automatic-shopify-checkout-gifts.html": {
        "headline": "How to launch automatic gifts in Shopify checkout",
        "faqs": [
            {
                "q": "What are automatic gifts in Shopify checkout?",
                "a": "Automatic gifts apply a free reward when cart rules are met at checkout, without requiring the customer to enter a coupon code.",
            },
            {
                "q": "Do automatic checkout gifts require Shopify Plus?",
                "a": "Checkout UI for gifts typically requires Shopify Plus checkout extensibility. Confirm requirements on the Smart Checkout Widgets Shopify App Store listing for your store type.",
            },
        ],
    },
    "customer-choice-free-gift-shopify-checkout.html": {
        "headline": "Why customer-choice free gifts outperform fixed offers",
        "faqs": [
            {
                "q": "What is a customer-choice free gift at checkout?",
                "a": "The shopper picks one reward from a merchant-defined set of gift SKUs when eligibility rules are met, instead of receiving a single fixed item.",
            },
            {
                "q": "When should merchants use customer-choice gifts?",
                "a": "Use them when you have multiple low-cost gift SKUs and want higher perceived value without increasing discount depth on every order.",
            },
        ],
    },
    "shopify-checkout-gift-strategy-aov.html": {
        "headline": "A practical Shopify checkout gift strategy for higher AOV",
        "faqs": [
            {
                "q": "How do checkout gifts increase average order value?",
                "a": "Threshold gifts motivate shoppers to add items to reach a reward. Pairing gifts with a single upsell can grow basket size while keeping the pay step focused.",
            },
            {
                "q": "Should gifts and upsells run together in checkout?",
                "a": "Yes, when sequenced clearly: show the earned gift first, then one relevant upsell. Avoid competing offers in the same viewport on mobile.",
            },
        ],
    },
    "shopify-checkout-upsells.html": {
        "headline": "How to add Shopify checkout upsells without breaking the final step",
        "faqs": [
            {
                "q": "Can you add upsells inside Shopify checkout?",
                "a": "Shopify Plus merchants can present upsells via checkout UI extensions so offers appear before payment, not only on post-purchase pages.",
            },
            {
                "q": "How many upsells should checkout show?",
                "a": "Lead with one primary recommendation tied to cart contents. Multiple competing upsells often increase abandonment.",
            },
        ],
    },
    "shopify-checkout-bogo-automatic-discounts.html": {
        "headline": "BOGO and automatic discounts in Shopify checkout (without coupon chaos)",
        "faqs": [
            {
                "q": "What is the difference between BOGO and threshold gifts in checkout?",
                "a": "BOGO ties rewards to product pairs or buy-X-get-Y rules. Threshold gifts apply when order value or collection rules are met, often with a single free item.",
            },
            {
                "q": "Why avoid coupon codes for checkout promotions?",
                "a": "Codes add friction, increase support tickets, and pull shoppers out of checkout. Automatic rules apply promotions where the order completes.",
            },
        ],
    },
    "shopify-checkout-trust-badges-payment.html": {
        "headline": "Trust badges and payment customization at Shopify checkout",
        "faqs": [
            {
                "q": "What is payment customization at Shopify checkout?",
                "a": "Merchants on Shopify Plus can hide, rename, or reorder payment methods at the final step to reduce confusion and last-step hesitation.",
            },
            {
                "q": "Do trust badges improve checkout conversion?",
                "a": "Specific, policy-backed trust content (returns, security icons, shipping notes) can reduce hesitation when kept short and accurate — not generic badge walls.",
            },
        ],
    },
    "shopify-plus-checkout-extensibility-guide.html": {
        "headline": "Shopify Plus checkout extensibility: what merchandising teams need to know",
        "faqs": [
            {
                "q": "What is Shopify Plus checkout extensibility?",
                "a": "It allows approved apps to add UI and logic inside checkout and related surfaces using checkout UI extensions and Shopify Functions, without editing checkout.liquid.",
            },
            {
                "q": "What is the difference between checkout UI extensions and Shopify Functions?",
                "a": "UI extensions control what shoppers see. Functions control backend logic such as discounts, validations, and payment customization.",
            },
        ],
    },
    "shopify-thank-you-order-status-widgets.html": {
        "headline": "Thank You and Order Status widgets: what to show after the sale",
        "faqs": [
            {
                "q": "Are Thank You page widgets available on all Shopify stores?",
                "a": "Content-based widgets on Thank You and Order Status pages are available on all Shopify stores. Full checkout UI customization requires Shopify Plus.",
            },
            {
                "q": "What should not be repeated on Thank You after checkout?",
                "a": "Avoid showing the same upsell the shopper already declined in checkout. Use Thank You for confirmation, policy clarity, and a different secondary CTA.",
            },
        ],
    },
}

BLOG_INDEX_ARTICLES = [
    {"url": seo.SITE + "/blog/automatic-shopify-checkout-gifts.html", "name": "Automatic gifts in Shopify checkout"},
    {"url": seo.SITE + "/blog/customer-choice-free-gift-shopify-checkout.html", "name": "Customer-choice free gifts"},
    {"url": seo.SITE + "/blog/shopify-checkout-gift-strategy-aov.html", "name": "Checkout gift strategy for AOV"},
    {"url": seo.SITE + "/blog/shopify-checkout-upsells.html", "name": "Checkout upsells"},
    {"url": seo.SITE + "/blog/shopify-checkout-bogo-automatic-discounts.html", "name": "BOGO and automatic discounts"},
    {"url": seo.SITE + "/blog/shopify-checkout-trust-badges-payment.html", "name": "Trust badges and payment customization"},
    {"url": seo.SITE + "/blog/shopify-plus-checkout-extensibility-guide.html", "name": "Checkout extensibility guide"},
    {"url": seo.SITE + "/blog/shopify-thank-you-order-status-widgets.html", "name": "Thank You and Order Status widgets"},
]

STATIC_PAGES = [
    ("index.html", "Smart Checkout Widgets | Shopify Plus Checkout Gifts and Upsells",
     "Smart Checkout Widgets helps Shopify Plus merchants increase AOV with automatic gifts, customer-choice rewards, upsells, trust badges, and checkout merchandising.",
     seo.SITE + "/", "website", "homepage"),
    ("blog/index.html", "Smart Checkout Widgets Blog | Shopify Checkout Gifts and AOV Guides",
     "Read Smart Checkout Widgets articles on Shopify checkout gifts, automatic gifting, customer-choice free gifts, upsells, BOGO, trust content, and checkout extensibility.",
     seo.SITE + "/blog/", "website", "blog_index"),
    ("videos.html", "Smart Checkout Widgets Videos | Shopify Checkout Demos",
     "Watch demo videos for Smart Checkout Widgets — automatic gifts, customer-choice rewards, and checkout merchandising on Shopify Plus.",
     seo.SITE + "/videos.html", "website", "page"),
    ("privacy.html", "Privacy Policy | Smart Checkout Widgets",
     "Privacy policy for Smart Checkout Widgets and Thought Bulb.",
     seo.SITE + "/privacy.html", "website", "page"),
    ("cro-techniques.html", "CRO Techniques for Shopify Checkout | Smart Checkout Widgets",
     "Conversion techniques for Shopify checkout merchandising, gifts, and upsells.",
     seo.SITE + "/cro-techniques.html", "website", "page"),
    ("microsoft-pixel-tracking-shopify-plus.html", "Microsoft Pixel Tracking on Shopify Plus | Smart Checkout Widgets",
     "Notes on Microsoft pixel tracking for Shopify Plus checkout and post-purchase surfaces.",
     seo.SITE + "/microsoft-pixel-tracking-shopify-plus.html", "website", "page"),
    ("api-intgreation.html", "API Integration | Smart Checkout Widgets",
     "API integration overview for Smart Checkout Widgets partners.",
     seo.SITE + "/api-intgreation.html", "website", "page"),
    ("tech-partners.html", "Technology Partners | Smart Checkout Widgets",
     "Technology partners working with Smart Checkout Widgets.",
     seo.SITE + "/tech-partners.html", "website", "page"),
    ("compare/shopify-checkout-gift-apps.html",
     "Shopify Checkout Gift Apps Compared (2026) | Smart Checkout Widgets",
     "Compare Shopify checkout gift and merchandising apps by feature — automatic gifts, customer choice, upsells, Plus requirements, and pricing.",
     seo.SITE + "/compare/shopify-checkout-gift-apps.html",
     "website",
     "compare/shopify-checkout-gift-apps.html"),
]


def strip_old_social_and_schema(html: str) -> str:
    html = re.sub(r"\n?\s*<script type=\"application/ld\+json\">.*?</script>", "", html, flags=re.DOTALL)
    html = re.sub(
        r"(<link rel=\"canonical\" href=\"[^\"]+\">)\s*"
        r"(?:(?:<meta property=\"og:[^\"]*\"[^>]*>|"
        r"<meta property=\"article:[^\"]*\"[^>]*>|"
        r"<meta name=\"twitter:[^\"]*\"[^>]*>)\s*)+",
        r"\1\n",
        html,
    )
    html = re.sub(
        r"\n\s*<link rel=\"alternate\" type=\"text/(?:plain|markdown)\"[^>]*>\s*",
        "\n",
        html,
    )
    return html


def inject_after_canonical(html: str, block: str) -> str:
    m = re.search(r'(<link rel="canonical" href="[^"]+">)', html)
    if not m:
        raise ValueError("canonical link not found")
    pos = m.end()
    return html[:pos] + "\n" + block + html[pos:]


def inject_before_stylesheet(html: str, block: str) -> str:
    m = re.search(r'(\s*<link rel="stylesheet" href="/style.css">)', html)
    if m:
        return html[: m.start()] + "\n" + block + "\n" + html[m.start() :]
    m = re.search(r"</head>", html)
    return html[: m.start()] + "\n" + block + "\n" + html[m.start() :]


def patch_static(
    path: Path,
    title: str,
    desc: str,
    canonical: str,
    og_type: str,
    kind: str,
    og_key: str = "default",
) -> None:
    html = path.read_text(encoding="utf-8")
    html = strip_old_social_and_schema(html)
    img, alt = OG_IMAGES.get(og_key, OG_IMAGES["default"])
    social = seo.social_meta(
        title=title, description=desc, canonical=canonical, og_type=og_type, image=img, image_alt=alt
    )
    extra = ""
    if kind == "homepage":
        extra = "\n" + seo.homepage_graph()
        extra += '\n  <link rel="alternate" type="text/plain" href="/llms.txt" title="LLM site context">'
        extra += '\n  <link rel="alternate" type="text/markdown" href="/pricing.md" title="Structured pricing">'
    elif kind == "blog_index":
        extra = "\n" + seo.blog_index_schema(BLOG_INDEX_ARTICLES)
        extra += '\n  <link rel="alternate" type="text/plain" href="/llms.txt" title="LLM site context">'
    elif kind == "compare/shopify-checkout-gift-apps.html":
        extra = "\n" + seo.web_page_schema(
            name="Shopify checkout gift apps compared",
            description=desc,
            url=canonical,
        )
        extra += "\n" + seo.faq_schema(COMPARE_FAQS)
    else:
        extra = "\n" + seo.web_page_schema(name=title.split("|")[0].strip(), description=desc, url=canonical)
    html = inject_after_canonical(html, social)
    html = inject_before_stylesheet(html, extra)
    path.write_text(html, encoding="utf-8")
    print("Patched", path.relative_to(ROOT))


def patch_article(path: Path) -> None:
    slug = path.name
    meta = ARTICLE_META.get(slug, {"headline": path.stem.replace("-", " "), "faqs": []})
    html = path.read_text(encoding="utf-8")

    title_m = re.search(r"<title>([^<]+)</title>", html)
    desc_m = re.search(r'<meta name="description" content="([^"]+)"', html)
    h1_m = re.search(r"<h1>([^<]+)</h1>", html)
    if not (title_m and desc_m):
        print("SKIP (missing title/desc)", slug)
        return

    title = title_m.group(1).strip()
    desc = desc_m.group(1).strip()
    headline = (h1_m.group(1).strip() if h1_m else meta["headline"])
    canonical = seo.SITE + "/blog/" + slug

    html = strip_old_social_and_schema(html)
    img, alt = OG_IMAGES.get(slug, OG_IMAGES["default"])
    social = seo.social_meta(
        title=title, description=desc, canonical=canonical, og_type="article", image=img, image_alt=alt
    )
    schemas = seo.article_schema(headline=headline, description=desc, url=canonical, image=img)
    faqs = meta.get("faqs", [])
    if faqs:
        schemas += "\n" + seo.faq_schema(faqs)

    html = inject_after_canonical(html, social)
    html = inject_before_stylesheet(html, schemas)

    faq_html = seo.faq_section_html(faqs)
    if faq_html and 'class="post-faq"' not in html:
        html = html.replace(
            '        <div class="section-cta">',
            faq_html + "\n        <div class=\"section-cta\">",
            1,
        )

    path.write_text(html, encoding="utf-8")
    print("Patched article", slug)


def write_sitemap() -> None:
    urls = [
        seo.SITE + "/",
        seo.SITE + "/blog/",
        seo.SITE + "/videos.html",
        seo.SITE + "/privacy.html",
        seo.SITE + "/cro-techniques.html",
        seo.SITE + "/microsoft-pixel-tracking-shopify-plus.html",
        seo.SITE + "/api-intgreation.html",
        seo.SITE + "/tech-partners.html",
        seo.SITE + "/compare/shopify-checkout-gift-apps.html",
    ]
    for slug in ARTICLE_META:
        urls.append(seo.SITE + "/blog/" + slug)

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for u in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{u}</loc>")
        lines.append(f"    <lastmod>{LASTMOD}</lastmod>")
        lines.append("  </url>")
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Wrote sitemap.xml (%d URLs)" % len(urls))


def write_robots() -> None:
    text = """# https://smartcheckoutwidgets.com/robots.txt
User-agent: *
Allow: /

# AI search & citation crawlers (allow for discoverability)
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: https://smartcheckoutwidgets.com/sitemap.xml

# Machine-readable context for AI agents
# https://smartcheckoutwidgets.com/llms.txt
# https://smartcheckoutwidgets.com/pricing.md
"""
    (ROOT / "robots.txt").write_text(text, encoding="utf-8")
    print("Wrote robots.txt")


def main() -> None:
    for rel, title, desc, canonical, og_type, kind in STATIC_PAGES:
        patch_static(ROOT / rel, title, desc, canonical, og_type, kind)

    for path in sorted(BLOG_DIR.glob("*.html")):
        if path.name == "index.html":
            continue
        patch_article(path)

    write_sitemap()
    write_robots()
    print("Done.")


if __name__ == "__main__":
    main()
