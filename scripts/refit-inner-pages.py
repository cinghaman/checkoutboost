#!/usr/bin/env python3
"""One-off: refit inner HTML pages to shared Hallmark chrome."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import seo  # noqa: E402

FONTS = """  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700&family=Geist+Mono:wght@400;500;600&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/style.css">"""

GTAG = """  <script async src="https://www.googletagmanager.com/gtag/js?id=G-T9GSXKCN10"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-T9GSXKCN10');
  </script>"""

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

CRISP = """  <script type="text/javascript">
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


def page(title, description, canonical, body_main, og_type="website", extra_head=""):
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
{seo.social_meta(title=title, description=description, canonical=canonical, og_type=og_type)}
{seo.web_page_schema(name=title.split("|")[0].strip(), description=description, url=canonical)}
{FONTS}
{extra_head}
</head>
<body class="page-inner">
{NAV}
{body_main}
{FOOTER}
  <script src="/site.js"></script>
{CRISP}
</body>
</html>
"""


def inner_cta(primary="Install on Shopify", primary_href="https://apps.shopify.com/smart-checkout-widgets", secondary=None, secondary_href="/blog/"):
    sec = ""
    if secondary:
        sec = f'<a class="btn btn-secondary" href="{secondary_href}">{secondary}</a>'
    return f"""    <section class="inner-cta">
      <div class="container">
        <div class="inner-cta__panel">
          <h2>Ready to upgrade your checkout?</h2>
          <p>Install Smart Checkout Widgets on Shopify Plus and launch gifting, upsells, and merchandising in checkout.</p>
          <div class="section-cta" style="justify-content: center; border: 0; padding-top: 0; margin-top: 0;">
            <a class="btn btn-primary" href="{primary_href}" target="_blank" rel="noopener noreferrer">{primary}</a>
            {sec}
          </div>
        </div>
      </div>
    </section>"""


# --- Blog index ---
blog_index_body = f"""  <main id="main-content">
    <section class="page-hero">
      <div class="page-hero-copy">
        <span class="eyebrow">◇ blog</span>
        <h1>Guides for checkout gifting and <em style="font-family: var(--font-italic); font-style: italic; font-weight: 400; color: var(--color-accent);">AOV</em>.</h1>
        <p>Practical articles on automatic gifts, customer-choice rewards, and checkout strategies for Shopify Plus merchants.</p>
      </div>
    </section>
    <section class="page-layout">
      <div class="post-grid">
        <article class="post-card">
          <p class="blog-meta">Automatic gifting</p>
          <h3><a href="/blog/automatic-shopify-checkout-gifts.html">How to launch automatic gifts in Shopify checkout</a></h3>
          <p>Why automatic gifting simplifies setup and creates cleaner reward campaigns.</p>
          <a class="text-link" href="/blog/automatic-shopify-checkout-gifts.html">Read article →</a>
        </article>
        <article class="post-card">
          <p class="blog-meta">Customer choice</p>
          <h3><a href="/blog/customer-choice-free-gift-shopify-checkout.html">Why customer-choice free gifts outperform fixed offers</a></h3>
          <p>Letting shoppers pick a reward can increase perceived value at checkout.</p>
          <a class="text-link" href="/blog/customer-choice-free-gift-shopify-checkout.html">Read article →</a>
        </article>
        <article class="post-card">
          <p class="blog-meta">Checkout AOV</p>
          <h3><a href="/blog/shopify-checkout-gift-strategy-aov.html">A practical Shopify checkout gift strategy for higher AOV</a></h3>
          <p>Connect gifts, upsells, and trust signals into one checkout system.</p>
          <a class="text-link" href="/blog/shopify-checkout-gift-strategy-aov.html">Read article →</a>
        </article>
      </div>
    </section>
{inner_cta()}
  </main>"""

(ROOT / "blog/index.html").write_text(
    page(
        "Smart Checkout Widgets Blog | Shopify Checkout Gifts and AOV Guides",
        "Read Smart Checkout Widgets articles on Shopify checkout gifts, automatic gifting, customer-choice free gifts, upsells, and checkout AOV strategy.",
        "https://smartcheckoutwidgets.com/blog/",
        blog_index_body,
    ),
    encoding="utf-8",
)

# --- Videos ---
videos_body = f"""  <main id="main-content">
    <section class="page-hero">
      <div class="page-hero-copy">
        <span class="eyebrow">◇ videos</span>
        <h1>Product walkthroughs and gifting demos.</h1>
        <p>Use this page for embeds, setup tutorials, and checkout gifting demos that push merchants toward the Shopify app listing.</p>
      </div>
    </section>
    <section class="page-layout">
      <div class="video-grid">
        <article class="video-card">
          <p class="blog-meta">Suggested video</p>
          <h3>Automatic gifting walkthrough</h3>
          <p>Show how a gift is configured, triggered, and presented at checkout.</p>
        </article>
        <article class="video-card">
          <p class="blog-meta">Suggested video</p>
          <h3>Customer-choice gift setup</h3>
          <p>Show how merchants add multiple gifts and let the customer select one reward.</p>
        </article>
        <article class="video-card">
          <p class="blog-meta">Suggested video</p>
          <h3>Checkout AOV stack</h3>
          <p>Explain how gifts, upsells, and trust elements work together in one strategy.</p>
        </article>
      </div>
      <div class="page-panel">
        <h2>Direct merchants toward action</h2>
        <p>Every video should link to the Shopify app listing or a feature-specific blog post so the page stays useful for discovery and conversion.</p>
        <div class="section-cta">
          <a class="btn btn-primary" href="https://apps.shopify.com/smart-checkout-widgets" target="_blank" rel="noopener noreferrer">Open Shopify app</a>
          <a class="btn btn-secondary" href="/blog/">Browse blog</a>
        </div>
      </div>
    </section>
{inner_cta(secondary="Browse blog")}
  </main>"""

(ROOT / "videos.html").write_text(
    page(
        "Smart Checkout Widgets Videos | Shopify Checkout Gift Demos",
        "Watch Smart Checkout Widgets videos and product walkthroughs for Shopify checkout gifts, upsells, and merchant setup.",
        "https://smartcheckoutwidgets.com/videos.html",
        videos_body,
    ),
    encoding="utf-8",
)


def article_page(title, desc, canonical, eyebrow, h1, content_html, cta_secondary=None, cta_secondary_href="/blog/"):
    sec_btn = ""
    if cta_secondary:
        sec_btn = f'<a class="btn btn-secondary" href="{cta_secondary_href}">{cta_secondary}</a>'
    body = f"""  <main id="main-content">
    <section class="post-hero">
      <div class="post-hero-copy">
        <span class="eyebrow">◇ {eyebrow}</span>
        <h1>{h1}</h1>
        <div class="meta-row">
          <span>Smart Checkout Widgets</span>
          <span><a href="/blog/" style="color: inherit;">All articles</a></span>
        </div>
      </div>
    </section>
    <section class="post-layout">
      <article class="post-content">
{content_html}
        <div class="section-cta">
          <a class="btn btn-primary" href="https://apps.shopify.com/smart-checkout-widgets" target="_blank" rel="noopener noreferrer">Install on Shopify</a>
          {sec_btn}
          <a class="btn btn-secondary" href="/">Back to homepage</a>
        </div>
      </article>
    </section>
{inner_cta(secondary="More articles", secondary_href="/blog/")}
  </main>"""
    return page(title, desc, canonical, body, og_type="article")


articles = {
    "blog/automatic-shopify-checkout-gifts.html": (
        "How to Launch Automatic Gifts in Shopify Checkout | Smart Checkout Widgets",
        "Learn how automatic gifts in Shopify checkout reduce friction, simplify merchant setup, and create stronger promotional campaigns.",
        "https://smartcheckoutwidgets.com/blog/automatic-shopify-checkout-gifts.html",
        "automatic gifting",
        "How to launch automatic gifts in Shopify checkout",
        """        <p>Automatic gifting matters because it removes the weakest part of many promotional campaigns: manual setup that relies too heavily on discount-code mechanics and merchant workarounds.</p>
        <h2>Why merchants want automatic gifts</h2>
        <p>Most merchants are not looking for another complicated rule engine. They want a reliable way to reward customers at checkout, protect perceived value, and launch promotions without creating extra support work for their team.</p>
        <ul>
          <li>Automatic gifts reduce friction for the shopper because the offer feels native to checkout.</li>
          <li>They reduce setup overhead for the merchant because the campaign logic is cleaner.</li>
          <li>They make gift promotions easier to test across seasonal campaigns and threshold-based offers.</li>
        </ul>
        <h2>What to emphasize on your site</h2>
        <p>If this feature is new, the homepage should explain the practical outcome first. Lead with faster setup, cleaner gift delivery, and a stronger checkout experience.</p>
        <h2>How Smart Checkout Widgets fits</h2>
        <p>Smart Checkout Widgets gives merchants a way to combine gifting with other checkout conversion layers like upsells, trust badges, and custom content. The highest-performing campaigns usually combine reward logic with persuasive merchandising.</p>""",
    ),
    "blog/customer-choice-free-gift-shopify-checkout.html": (
        "Why Customer-Choice Free Gifts Work Better in Shopify Checkout | Smart Checkout Widgets",
        "Learn why allowing customers to pick their own free gift in Shopify checkout can increase perceived value and improve gifting campaigns.",
        "https://smartcheckoutwidgets.com/blog/customer-choice-free-gift-shopify-checkout.html",
        "customer choice",
        "Why customer-choice free gifts outperform fixed offers",
        """        <p>When every shopper receives the same free gift, the reward can feel generic. Customer-choice gifting lets the promotion adapt to different preferences without adding coupon friction.</p>
        <h2>Why choice increases perceived value</h2>
        <p>Selection signals generosity. The customer still receives a free item, but the experience feels more personal and more fair.</p>
        <ul>
          <li>Shoppers pick the variant that fits them best.</li>
          <li>Merchants can offer multiple gift SKUs without running separate campaigns.</li>
          <li>Checkout stays native — no code entry or theme hacks.</li>
        </ul>
        <h2>When to use it</h2>
        <p>Customer-choice works well for brands with multiple low-cost gift options, seasonal bundles, or sample programs where relevance matters more than a single default SKU.</p>
        <h2>How Smart Checkout Widgets supports it</h2>
        <p>Configure multiple gift items, tie them to threshold or discount logic, and present the picker inside Shopify Plus checkout with the rest of your merchandising stack.</p>""",
    ),
    "blog/shopify-checkout-gift-strategy-aov.html": (
        "A Practical Shopify Checkout Gift Strategy for Higher AOV | Smart Checkout Widgets",
        "Connect free gifts, upsells, and trust signals into one checkout system that supports stronger average order value.",
        "https://smartcheckoutwidgets.com/blog/shopify-checkout-gift-strategy-aov.html",
        "AOV strategy",
        "A practical Shopify checkout gift strategy for higher AOV",
        """        <p>Many checkout experiments underperform because they are treated as isolated widgets. A stronger approach coordinates reward, persuasion, and clarity.</p>
        <h2>Start with the reward</h2>
        <p>A free gift can push the customer over the line when the reward is timely and relevant. Automatic gifting and customer-choice gifting both improve delivery, but the reward is only one layer.</p>
        <h2>Add a value-expansion layer</h2>
        <p>Upsells and recommended products extend the order instead of only discounting it. When checkout includes a gift plus a relevant add-on, the offer can increase perceived generosity while supporting order growth.</p>
        <h2>Reassure before the click</h2>
        <p>Trust badges, custom banners, payment icons, and consent messaging reduce hesitation. AOV strategies work better when the customer feels safe moving forward.</p>
        <ul>
          <li>Gift logic increases motivation.</li>
          <li>Upsells increase basket size.</li>
          <li>Trust elements protect conversion quality.</li>
        </ul>
        <h2>Position the full system</h2>
        <p>Smart Checkout Widgets is stronger when presented as one system for gifting and checkout merchandising — more differentiated than a flat list of widgets.</p>""",
        "Watch videos",
        "/videos.html",
    ),
}

for path, data in articles.items():
    if len(data) == 8:
        title, desc, canonical, eyebrow, h1, content, sec, sec_href = data
        html = article_page(title, desc, canonical, eyebrow, h1, content, sec, sec_href)
    else:
        title, desc, canonical, eyebrow, h1, content = data
        html = article_page(title, desc, canonical, eyebrow, h1, content)
    (ROOT / path).write_text(html, encoding="utf-8")

# --- Privacy: extract article from existing file ---
privacy_src = (ROOT / "privacy.html").read_text(encoding="utf-8")
start = privacy_src.find('<article class="page-panel">')
end = privacy_src.find("</article>", start)
privacy_article = privacy_src[start : end + len("</article>")] if start != -1 else "<article class=\"page-panel\"><p>Privacy policy content unavailable.</p></article>"

privacy_body = f"""  <main id="main-content">
    <section class="page-hero">
      <div class="page-hero-copy">
        <span class="eyebrow">◇ legal</span>
        <h1>Privacy Policy</h1>
        <p>How Smart Checkout Widgets collects, uses, and protects your information.</p>
      </div>
    </section>
    <section class="page-layout">
      {privacy_article.replace('class="page-panel"', 'class="page-panel post-content"', 1)}
    </section>
  </main>"""

(ROOT / "privacy.html").write_text(
    page(
        "Privacy Policy | Smart Checkout Widgets",
        "Privacy Policy for Smart Checkout Widgets and smartcheckoutwidgets.com.",
        "https://smartcheckoutwidgets.com/privacy.html",
        privacy_body,
    ),
    encoding="utf-8",
)

# --- CRO guide (simplified from legacy) ---
cro_content = """        <p>In competitive e-commerce, conversion rate optimization turns browsers into buyers. These ten strategies focus on checkout-adjacent wins merchants can implement with clearer merchandising and less friction.</p>
        <h2>1. Optimize product pages</h2>
        <ul><li>Use high-quality visuals and video where possible.</li><li>Write descriptions that address pain points and benefits plainly.</li></ul>
        <h2>2. Streamline checkout</h2>
        <ul><li>Minimize form fields and show progress.</li><li>Offer multiple payment options shoppers expect.</li></ul>
        <h2>3. Leverage social proof</h2>
        <ul><li>Display authentic reviews and trust badges at the final step.</li></ul>
        <h2>4. Personalize where it helps</h2>
        <ul><li>Recommend relevant add-ons based on cart contents, not generic blocks.</li></ul>
        <h2>5. Mobile optimization</h2>
        <ul><li>Large tap targets, fast loads, and readable type on small screens.</li></ul>
        <h2>6. Use urgency carefully</h2>
        <ul><li>Stock indicators and time-bound offers should be truthful.</li></ul>
        <h2>7. A/B test one change at a time</h2>
        <ul><li>Measure checkout widgets, gift thresholds, and upsell placement with real traffic.</li></ul>
        <h2>8. Offer fast support</h2>
        <ul><li>Answer pre-purchase questions before abandonment.</li></ul>
        <h2>9. Transparent pricing</h2>
        <ul><li>Show shipping and return policies early — surprises kill conversion.</li></ul>
        <h2>10. Retarget thoughtfully</h2>
        <ul><li>Abandoned-cart flows should reinforce the same offer logic shown in checkout.</li></ul>
        <h2>Bottom line</h2>
        <p>CRO is ongoing. Combine gifting, upsells, and trust content in checkout with measurement — not one-off hacks.</p>"""

(ROOT / "cro-techniques.html").write_text(
    page(
        "10 CRO Strategies for E-Commerce Checkout | Smart Checkout Widgets",
        "Conversion rate optimization strategies for e-commerce checkout, gifting, and merchandising.",
        "https://smartcheckoutwidgets.com/cro-techniques.html",
        f"""  <main id="main-content">
    <section class="page-hero">
      <div class="page-hero-copy">
        <span class="eyebrow">◇ guide</span>
        <h1>10 CRO strategies that convert browsers into buyers</h1>
        <p>Practical conversion tactics with emphasis on checkout clarity, trust, and reward mechanics.</p>
      </div>
    </section>
    <section class="post-layout"><article class="post-content">
{cro_content}
        <div class="section-cta">
          <a class="btn btn-primary" href="https://apps.shopify.com/smart-checkout-widgets" target="_blank" rel="noopener noreferrer">Install on Shopify</a>
          <a class="btn btn-secondary" href="/blog/shopify-checkout-gift-strategy-aov.html">AOV strategy guide</a>
        </div>
      </article></section>
{inner_cta()}
  </main>""",
    ),
    encoding="utf-8",
)

# --- Microsoft pixel guide ---
ms_content = """        <p>Track purchase conversions in Microsoft Ads with an event-based goal tied to Shopify checkout completion.</p>
        <h2>Why event-based goals</h2>
        <p>URL-only goals miss inline actions. Event-based goals capture purchases when the checkout completed event fires.</p>
        <h2>Create the conversion goal</h2>
        <ol>
          <li>In Microsoft Ads, go to <strong>Tools → Conversion Goals</strong>.</li>
          <li>Click <strong>Create conversion goal</strong>.</li>
          <li>Select <strong>Website</strong>, then <strong>Purchase</strong>, then <strong>Event</strong>.</li>
        </ol>
        <p>If events are unavailable in your account, try a destination URL goal containing <code>processing?completed=true</code> as a fallback.</p>
        <h2>Tagging</h2>
        <ul><li><strong>Action:</strong> Purchase</li><li><strong>Category:</strong> Checkout</li></ul>
        <h2>Add the pixel in Shopify</h2>
        <ol>
          <li>Shopify admin → <strong>Settings → Customer events → Add custom pixel</strong>.</li>
          <li>Paste the UET snippet and replace the tracking ID placeholder.</li>
          <li>Subscribe to <code>checkout_completed</code> and push the purchase event with order value and currency.</li>
        </ol>
        <pre><code>(function(w,d,t,r,u){
  var f,n,i;
  w[u]=w[u]||[];
  f=function(){
    var o={ti:"YOUR_UET_ID", enableAutoSpaTracking: true};
    o.q=w[u];w[u]=new UET(o);w[u].push("pageLoad")
  },
  n=d.createElement(t);n.src=r;n.async=1;
  n.onload=n.onreadystatechange=function(){
    var s=this.readyState;
    s&&s!=="loaded"&&s!=="complete"||(f(),n.onload=n.onreadystatechange=null)
  },
  i=d.getElementsByTagName(t)[0];
  i.parentNode.insertBefore(n,i)
})(window,document,"script","//bat.bing.com/bat.js","uetq");

analytics.subscribe('checkout_completed', (event) => {
  window.uetq = window.uetq || [];
  window.uetq.push('event', 'purchase', {
    event_category: "checkout",
    revenue_value: event.data.checkout.totalPrice.amount,
    currency: event.data.checkout.currencyCode
  });
});</code></pre>
        <h2>Test the setup</h2>
        <ol>
          <li>Complete a test order on your store.</li>
          <li>Confirm the conversion appears in Microsoft Ads.</li>
          <li>Inspect network requests to verify the pixel fires on checkout completion.</li>
        </ol>"""

(ROOT / "microsoft-pixel-tracking-shopify-plus.html").write_text(
    page(
        "Microsoft Pixel Tracking for Shopify Plus | Smart Checkout Widgets",
        "Set up Microsoft Ads event-based conversion tracking on Shopify Plus checkout.",
        "https://smartcheckoutwidgets.com/microsoft-pixel-tracking-shopify-plus.html",
        f"""  <main id="main-content">
    <section class="page-hero">
      <div class="page-hero-copy">
        <span class="eyebrow">◇ integration</span>
        <h1>Microsoft pixel tracking for Shopify Plus</h1>
        <p>Event-based conversion goals for purchase tracking in Microsoft Ads.</p>
      </div>
    </section>
    <section class="post-layout"><article class="post-content">
{ms_content}
        <div class="section-cta">
          <a class="btn btn-primary" href="https://apps.shopify.com/smart-checkout-widgets" target="_blank" rel="noopener noreferrer">Install on Shopify</a>
        </div>
      </article></section>
  </main>""",
    ),
    encoding="utf-8",
)

# --- API integration ---
api_content = """        <h2>XML upload endpoint</h2>
        <p>Example <code>curl</code> request to upload XML to the app endpoint:</p>
        <pre><code>curl --location 'https://game-center.fly.dev/api/xmlprocess' \\
  --header 'X-API-KEY: xx-xxxx-xxxxx' \\
  --form 'xml=@"/path/to/mock_game_data.xml"'</code></pre>
        <h2>JavaScript (FormData)</h2>
        <pre><code>const myHeaders = new Headers();
myHeaders.append("X-API-KEY", "xxx-xxx-xxx");

const formdata = new FormData();
formdata.append("xml", fileInput.files[0], "mock_game_data.xml");

const requestOptions = {
  method: "POST",
  headers: myHeaders,
  body: formdata,
  redirect: "follow"
};

fetch("https://game-center.fly.dev/api/xmlprocess", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.error(error));</code></pre>"""

(ROOT / "api-intgreation.html").write_text(
    page(
        "API Integration | Smart Checkout Widgets",
        "API integration examples for Smart Checkout Widgets XML processing endpoint.",
        "https://smartcheckoutwidgets.com/api-intgreation.html",
        f"""  <main id="main-content">
    <section class="page-hero">
      <div class="page-hero-copy">
        <span class="eyebrow">◇ developers</span>
        <h1>API integration</h1>
        <p>Reference examples for uploading XML to the processing endpoint.</p>
      </div>
    </section>
    <section class="post-layout"><article class="post-content">
{api_content}
      </article></section>
  </main>""",
    ),
    encoding="utf-8",
)

# --- Tech partners (simplified; legacy page was tutorial tabs) ---
(ROOT / "tech-partners.html").write_text(
    page(
        "Shopify Ecosystem & Partners | Smart Checkout Widgets",
        "Smart Checkout Widgets works with Shopify Plus checkout extensibility and the Shopify app ecosystem.",
        "https://smartcheckoutwidgets.com/tech-partners.html",
        f"""  <main id="main-content">
    <section class="page-hero">
      <div class="page-hero-copy">
        <span class="eyebrow">◇ ecosystem</span>
        <h1>Built for the Shopify Plus checkout stack</h1>
        <p>Smart Checkout Widgets uses checkout extensibility, Shopify Functions, and native checkout UI — no theme hacks required.</p>
      </div>
    </section>
    <section class="page-layout">
      <div class="post-grid">
        <article class="post-card">
          <p class="blog-meta">Platform</p>
          <h3>Shopify Plus</h3>
          <p>Checkout gifting, upsells, and merchandising inside the Plus checkout experience.</p>
        </article>
        <article class="post-card">
          <p class="blog-meta">Extensibility</p>
          <h3>Checkout UI extensions</h3>
          <p>Widgets render in checkout with the same patterns merchants expect from Plus apps.</p>
        </article>
        <article class="post-card">
          <p class="blog-meta">Developer</p>
          <h3>Thought Bulb</h3>
          <p>Published on the <a href="https://apps.shopify.com/smart-checkout-widgets" target="_blank" rel="noopener noreferrer">Shopify App Store</a> with ongoing support.</p>
        </article>
      </div>
      <div class="page-panel" style="margin-top: var(--space-xl);">
        <h2>Explore the product</h2>
        <p>Watch setup videos, read gifting guides, or install the app to configure your first offer.</p>
        <div class="section-cta">
          <a class="btn btn-primary" href="https://apps.shopify.com/smart-checkout-widgets" target="_blank" rel="noopener noreferrer">Install free</a>
          <a class="btn btn-secondary" href="/videos.html">Videos</a>
          <a class="btn btn-secondary" href="/blog/">Blog</a>
        </div>
      </div>
    </section>
{inner_cta()}
  </main>""",
    ),
    encoding="utf-8",
)

print("Refitted inner pages.")
