#!/usr/bin/env python3
"""Shared SEO / AI-extractable head fragments for smartcheckoutwidgets.com."""

import json
from typing import Any, Dict, List, Optional

SITE = "https://smartcheckoutwidgets.com"
ORG_NAME = "Smart Checkout Widgets"
ORG_URL = SITE + "/"
LOGO = SITE + "/images/smart_widget_icon_for_shopify.jpg"
PREVIEW_IMAGE = SITE + "/images/screen2.webp"
PREVIEW_WIDTH = "1200"
PREVIEW_HEIGHT = "675"
PREVIEW_ALT = "Smart Checkout Widgets gift and upsell experience in Shopify checkout"
PUBLISHER = {
    "@type": "Organization",
    "name": ORG_NAME,
    "url": ORG_URL,
    "logo": {"@type": "ImageObject", "url": LOGO},
}


def _esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("<", "&lt;")
    )


def social_meta(
    *,
    title: str,
    description: str,
    canonical: str,
    og_type: str = "website",
    image: str = PREVIEW_IMAGE,
    image_alt: str = PREVIEW_ALT,
) -> str:
    t, d, c = _esc(title), _esc(description), _esc(canonical)
    img, alt = _esc(image), _esc(image_alt)
    article_times = ""
    if og_type == "article":
        article_times = """
  <meta property="article:published_time" content="2026-05-20">
  <meta property="article:modified_time" content="2026-05-20">"""
    return f"""  <meta property="og:title" content="{t}">
  <meta property="og:description" content="{d}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:url" content="{c}">
  <meta property="og:site_name" content="{_esc(ORG_NAME)}">
  <meta property="og:locale" content="en_US">
  <meta property="og:image" content="{img}">
  <meta property="og:image:secure_url" content="{img}">
  <meta property="og:image:width" content="{PREVIEW_WIDTH}">
  <meta property="og:image:height" content="{PREVIEW_HEIGHT}">
  <meta property="og:image:alt" content="{alt}">{article_times}
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{t}">
  <meta name="twitter:description" content="{d}">
  <meta name="twitter:image" content="{img}">
  <meta name="twitter:image:alt" content="{alt}">
"""


def json_ld_script(data: Any) -> str:
    return (
        '  <script type="application/ld+json">\n'
        + json.dumps(data, indent=2, ensure_ascii=False)
        + "\n  </script>"
    )


def article_schema(
    *,
    headline: str,
    description: str,
    url: str,
    image: str = PREVIEW_IMAGE,
    date_published: str = "2026-05-20",
    date_modified: str = "2026-05-20",
) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": headline,
        "description": description,
        "url": url,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "image": [image],
        "datePublished": date_published,
        "dateModified": date_modified,
        "author": PUBLISHER,
        "publisher": PUBLISHER,
        "inLanguage": "en-US",
        "isPartOf": {
            "@type": "Blog",
            "name": ORG_NAME + " Blog",
            "url": SITE + "/blog/",
        },
    }
    return json_ld_script(data)


def faq_schema(questions: List[Dict[str, str]]) -> str:
    if not questions:
        return ""
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q["q"],
                "acceptedAnswer": {"@type": "Answer", "text": q["a"]},
            }
            for q in questions
        ],
    }
    return json_ld_script(data)


def faq_section_html(questions: List[Dict[str, str]]) -> str:
    if not questions:
        return ""
    items = "\n".join(
        f"""          <details class="faq-item">
            <summary>{_esc(q["q"])}</summary>
            <p>{_esc(q["a"])}</p>
          </details>"""
        for q in questions
    )
    return f"""
        <section class="post-faq" aria-labelledby="faq-heading">
          <h2 id="faq-heading">Frequently asked questions</h2>
          <div class="faq-list">
{items}
          </div>
        </section>"""


def blog_index_schema(articles: List[Dict[str, str]]) -> str:
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "CollectionPage",
                "name": ORG_NAME + " Blog",
                "url": SITE + "/blog/",
                "description": "Guides on Shopify checkout gifts, upsells, BOGO, trust content, and checkout extensibility.",
                "publisher": PUBLISHER,
            },
            {
                "@type": "ItemList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": i + 1,
                        "url": a["url"],
                        "name": a["name"],
                    }
                    for i, a in enumerate(articles)
                ],
            },
        ],
    }
    return json_ld_script(data)


def homepage_graph() -> str:
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Organization",
                "@id": ORG_URL + "#organization",
                "name": ORG_NAME,
                "url": ORG_URL,
                "logo": LOGO,
                "sameAs": [
                    "https://apps.shopify.com/smart-checkout-widgets",
                ],
            },
            {
                "@type": "WebSite",
                "@id": ORG_URL + "#website",
                "url": ORG_URL,
                "name": ORG_NAME,
                "publisher": {"@id": ORG_URL + "#organization"},
            },
            {
                "@type": "SoftwareApplication",
                "name": ORG_NAME,
                "applicationCategory": "BusinessApplication",
                "operatingSystem": "Shopify",
                "url": ORG_URL,
                "image": PREVIEW_IMAGE,
                "description": "Shopify Plus app for automatic gifts, customer-choice rewards, checkout upsells, trust badges, and checkout merchandising.",
                "offers": {
                    "@type": "Offer",
                    "price": "0",
                    "priceCurrency": "USD",
                    "description": "Free to install Starter plan on the Shopify App Store",
                    "url": "https://apps.shopify.com/smart-checkout-widgets",
                },
            },
        ],
    }
    return json_ld_script(data)


def web_page_schema(*, name: str, description: str, url: str) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": name,
        "description": description,
        "url": url,
        "isPartOf": {"@type": "WebSite", "name": ORG_NAME, "url": ORG_URL},
        "publisher": PUBLISHER,
    }
    return json_ld_script(data)
