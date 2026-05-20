#!/usr/bin/env python3
"""Generate a blog article HTML page matching site chrome."""

import sys
from pathlib import Path
from typing import List, Dict, Optional

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import seo  # noqa: E402

GTAG = """  <script async src="https://www.googletagmanager.com/gtag/js?id=G-T9GSXKCN10"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-T9GSXKCN10');
  </script>"""

FONTS = """  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700&family=Geist+Mono:wght@400;500;600&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/style.css">"""

NAV = """  <a class="skip-link" href="#main-content">Skip to content</a>
  <nav class="nav" aria-label="Primary">
    <a href="https://smartcheckoutwidgets.com/" class="nav__brand" aria-label="Smart Checkout Widgets home">
      <img src="/images/logo-mark.svg" alt="" width="22" height="22">
      Smart Checkout
    </a>
    <div class="nav__links">
      <a class="nav__link" href="/#workbench">Product</a>
      <a class="nav__link" href="/#features">Features</a>
      <a class="nav__link" href="/#pricing">Pricing</a>
      <a class="nav__link" href="/blog/">Blog</a>
      <a class="nav__link" href="/videos.html">Videos</a>
    </div>
    <a class="nav__cta" href="https://apps.shopify.com/smart-checkout-widgets" target="_blank" rel="noopener noreferrer">Install free</a>
  </nav>"""

FOOTER = """  <footer class="footer">
    <div class="container">
      <p class="footer__statement">
        Smart Checkout Widgets is gifting and merchandising for teams who'd rather <em>convert</em> than patch coupons.
      </p>
      <div class="footer__row">
        <div class="footer__col">
          <h5>Product</h5>
          <ul>
            <li><a href="/#workbench">Console</a></li>
            <li><a href="/#features">Features</a></li>
            <li><a href="/#pricing">Pricing</a></li>
            <li><a href="/blog/">Guides</a></li>
          </ul>
        </div>
        <div class="footer__col">
          <h5>Resources</h5>
          <ul>
            <li><a href="/blog/">Blog</a></li>
            <li><a href="/videos.html">Videos</a></li>
            <li><a href="/privacy.html">Privacy</a></li>
            <li><a href="https://apps.shopify.com/smart-checkout-widgets" target="_blank" rel="noopener noreferrer">Shopify listing</a></li>
          </ul>
        </div>
        <div class="footer__col">
          <h5>Company</h5>
          <ul>
            <li><a href="https://thoughtbulb.dev" target="_blank" rel="noopener noreferrer">Thought Bulb</a></li>
            <li><a href="mailto:admin@thoughtbulb.dev">Support</a></li>
          </ul>
        </div>
        <div class="footer__col">
          <h5>Legal</h5>
          <ul>
            <li><a href="/privacy.html">Privacy policy</a></li>
          </ul>
        </div>
      </div>
      <div class="footer__legal">
        <span class="wordmark">Smart Checkout Widgets</span>
        <span>© 2026 Thought Bulb · Built for Shopify Plus checkout</span>
      </div>
    </div>
  </footer>"""

CRISP = """  <script src="/site.js"></script>
  <script type="text/javascript">
    window.$crisp = [];
    window.CRISP_WEBSITE_ID = "c6ce9585-187d-471e-a0ba-150354e2d6e8";
    (function () {
      var d = document;
      var s = d.createElement("script");
      s.src = "https://client.crisp.chat/l.js";
      s.async = 1;
      d.getElementsByTagName("head")[0].appendChild(s);
    })();
  </script>"""


def render(
    *,
    slug: str,
    title: str,
    description: str,
    eyebrow: str,
    h1: str,
    date: str,
    body_html: str,
    secondary_label: Optional[str] = None,
    secondary_href: str = "/blog/",
    faqs: Optional[List[Dict[str, str]]] = None,
) -> str:
    canonical = f"https://smartcheckoutwidgets.com/blog/{slug}"
    sec = ""
    if secondary_label:
        sec = f'<a class="btn btn-secondary" href="{secondary_href}">{secondary_label}</a>'
    social = seo.social_meta(
        title=title, description=description, canonical=canonical, og_type="article"
    )
    schemas = seo.article_schema(headline=h1, description=description, url=canonical)
    faq_block = ""
    if faqs:
        schemas += "\n" + seo.faq_schema(faqs)
        faq_block = seo.faq_section_html(faqs)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{GTAG}
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="index,follow">
  <link rel="canonical" href="{canonical}">
{social}
{schemas}
{FONTS}
</head>
<body class="page-inner">
{NAV}
  <main id="main-content">
    <section class="post-hero">
      <div class="post-hero-copy">
        <span class="eyebrow">◇ {eyebrow}</span>
        <h1>{h1}</h1>
        <div class="meta-row">
          <span>Updated {date}</span>
          <span>Smart Checkout Widgets</span>
          <span><a href="/blog/" style="color: inherit;">All articles</a></span>
        </div>
      </div>
    </section>
    <section class="post-layout">
      <article class="post-content">
{body_html}
{faq_block}
        <div class="section-cta">
          <a class="btn btn-primary" href="https://apps.shopify.com/smart-checkout-widgets" target="_blank" rel="noopener noreferrer">Install on Shopify</a>
          {sec}
          <a class="btn btn-secondary" href="/">Back to homepage</a>
        </div>
      </article>
    </section>
    <section class="inner-cta">
      <div class="container">
        <div class="inner-cta__panel">
          <h2>Ready to upgrade your checkout?</h2>
          <p>Install Smart Checkout Widgets on Shopify Plus and launch gifting, upsells, and merchandising in checkout.</p>
          <div class="section-cta" style="justify-content: center; border: 0; padding-top: 0; margin-top: 0;">
            <a class="btn btn-primary" href="https://apps.shopify.com/smart-checkout-widgets" target="_blank" rel="noopener noreferrer">Install on Shopify</a>
            <a class="btn btn-secondary" href="/blog/">More articles</a>
          </div>
        </div>
      </div>
    </section>
  </main>
{FOOTER}
{CRISP}
</body>
</html>
"""


if __name__ == "__main__":
    out = Path(sys.argv[1])
    out.write_text(render(**eval(sys.argv[2])), encoding="utf-8")
