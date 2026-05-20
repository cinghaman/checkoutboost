#!/usr/bin/env python3
"""Generate four new blog posts and patch blog index + homepage strip."""

from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("shell", ROOT / "scripts/blog-article-shell.py")
shell = importlib.util.module_from_spec(spec)
spec.loader.exec_module(shell)

DATE = "May 20, 2026"

POSTS = [
    {
        "slug": "shopify-checkout-upsells.html",
        "title": "Shopify Checkout Upsells That Feel Native (Not Pushy) | Smart Checkout Widgets",
        "description": "How to add checkout upsells on Shopify Plus without cluttering the final step — timing, relevance, and pairing upsells with gift offers.",
        "eyebrow": "checkout upsells",
        "h1": "How to add Shopify checkout upsells without breaking the final step",
        "secondary_label": "Gift strategy guide",
        "secondary_href": "/blog/shopify-checkout-gift-strategy-aov.html",
        "body": """
        <p>Upsells fail when they feel bolted on. On Shopify Plus, you can present add-ons inside checkout — but only if the offer is relevant to what is already in the cart.</p>
        <h2>Why post-purchase upsells are often too late</h2>
        <p>Post-purchase flows can work, but they ask for a second decision after the shopper already committed. Checkout upsells catch intent while the customer is still evaluating the order total.</p>
        <p>The goal is not to add another banner. It is to suggest one logical add-on: a refill, bundle, warranty, or accessory that fits the items already selected.</p>
        <h2>Three rules for checkout upsells that convert</h2>
        <ul>
          <li><strong>One primary offer.</strong> Multiple competing upsells create decision fatigue. Lead with a single recommendation tied to cart contents or order value.</li>
          <li><strong>Match the gift logic.</strong> If you run a free-gift threshold, show the upsell after the reward is visible. The customer already feels they are winning — the add-on should extend that momentum, not fight it.</li>
          <li><strong>Keep copy short.</strong> Checkout is not a product page. State the benefit in one line and let price do the rest.</li>
        </ul>
        <h2>Common setups merchants use</h2>
        <p>Brands on Shopify Plus often combine:</p>
        <ul>
          <li>Threshold-based free gifts for motivation</li>
          <li>A single upsell for basket expansion</li>
          <li>Trust content (payment icons, policies, reassurance) to protect completion rate</li>
        </ul>
        <p>That stack treats checkout as a small merchandising system — not a pile of unrelated widgets.</p>
        <h2>How Smart Checkout Widgets handles upsells</h2>
        <p>Smart Checkout Widgets lets you configure upsells alongside gifting, banners, and trust elements in the same checkout extension. You can test offer placement without rebuilding your theme or juggling separate apps for each block.</p>
        <p>Start on the free install plan if you want to validate placement and copy before scaling order volume on a paid tier.</p>
        <h2>What to measure</h2>
        <p>Track upsell attach rate, checkout completion rate, and average order value together. A higher attach rate means nothing if completion drops. The winning setup increases AOV while keeping abandonment flat.</p>
        <p>Run one change per week: offer, threshold, or placement. Checkout optimization is iterative — not a single hero widget.</p>
""",
    },
    {
        "slug": "shopify-checkout-bogo-automatic-discounts.html",
        "title": "BOGO and Automatic Discounts in Shopify Checkout | Smart Checkout Widgets",
        "description": "Run BOGO and automatic discount campaigns in Shopify checkout without coupon codes — rules, stacking, and gift offers explained for merchants.",
        "eyebrow": "BOGO & discounts",
        "h1": "BOGO and automatic discounts in Shopify checkout (without coupon chaos)",
        "secondary_label": "Automatic gifting guide",
        "secondary_href": "/blog/automatic-shopify-checkout-gifts.html",
        "body": """
        <p>Coupon codes train customers to leave checkout and hunt for deals. Automatic discounts and BOGO-style rewards apply the promotion where the order actually completes — inside checkout.</p>
        <h2>The problem with code-based campaigns</h2>
        <p>When shoppers must copy a code, three things break: attribution gets messy, support tickets spike ("my code didn't work"), and completion rate drops while people open a new tab.</p>
        <p>Automatic rules tie the promotion to cart conditions — order value, products, or customer eligibility — so the reward shows up without extra steps.</p>
        <h2>BOGO vs threshold gifts: pick the right mechanic</h2>
        <ul>
          <li><strong>BOGO / buy-X-get-Y</strong> works when the catalog has natural pairs — socks with shoes, refills with devices, samples with full sizes.</li>
          <li><strong>Threshold gifts</strong> work when you want a simple "spend $X, choose a reward" campaign without restructuring SKU logic.</li>
          <li><strong>Customer-choice gifts</strong> add perceived value when you have multiple low-cost gift SKUs and want the shopper to pick one.</li>
        </ul>
        <p>Many merchants rotate mechanics by season: BOGO during product launches, threshold gifts during holidays.</p>
        <h2>Stacking discounts and gifts carefully</h2>
        <p>Stacking is powerful and easy to get wrong. Before you combine automatic discounts with free gifts, define:</p>
        <ul>
          <li>Which promotion applies first in your business logic</li>
          <li>Whether the gift counts toward margin targets</li>
          <li>What support will say when a wholesale or VIP customer asks for an exception</li>
        </ul>
        <p>Smart Checkout Widgets is built around automatic discount and gifting flows in checkout. Document your rules in the admin so finance and support share the same definition of "eligible order."</p>
        <h2>Where checkout extensibility helps</h2>
        <p>Shopify Plus checkout extensions let apps render offers natively instead of hacking the thank-you page or email flows. Shoppers see the discount or gift before they pay, which is when it affects conversion.</p>
        <h2>Launch checklist</h2>
        <ol>
          <li>Pick one promotion mechanic for the first test.</li>
          <li>Set a clear eligibility rule (product, collection, or cart minimum).</li>
          <li>Preview the experience on mobile — most checkout traffic is phone-first.</li>
          <li>Monitor completion rate for two weeks before adding a second promotion layer.</li>
        </ol>
""",
    },
    {
        "slug": "shopify-checkout-trust-badges-payment.html",
        "title": "Trust Badges and Payment Customization at Shopify Checkout | Smart Checkout Widgets",
        "description": "Reduce last-step hesitation with payment method customization, trust badges, and clear checkout content on Shopify Plus.",
        "eyebrow": "trust & payments",
        "h1": "Trust badges and payment customization at Shopify checkout",
        "secondary_label": "Customer-choice gifts",
        "secondary_href": "/blog/customer-choice-free-gift-shopify-checkout.html",
        "body": """
        <p>Gifts and upsells increase motivation. Trust content protects the sale. If shoppers hesitate at payment, no promotion mechanic will recover the order.</p>
        <h2>What creates last-step hesitation</h2>
        <p>Customers often abandon when they see an unfamiliar payment method, too many options, or no signal that the store is legitimate. The fix is not more pop-ups — it is clearer checkout content.</p>
        <h2>Payment customization: hide, rename, reorder</h2>
        <p>Shopify Plus merchants can tailor how payment methods appear at the final step:</p>
        <ul>
          <li><strong>Hide</strong> methods that do not fit the order type (e.g., invoice options on small consumer carts).</li>
          <li><strong>Rename</strong> labels shoppers find confusing — "Shop Pay" vs generic wallet names, for example.</li>
          <li><strong>Reorder</strong> methods to surface your preferred option first in your primary markets.</li>
        </ul>
        <p>Cleaner payment lists reduce cognitive load. Fewer visible choices often beat "show everything."</p>
        <h2>Trust badges and icons that actually help</h2>
        <p>Effective trust content is specific:</p>
        <ul>
          <li>Return window in plain language</li>
          <li>Secure checkout / payment provider icons shoppers recognize</li>
          <li>Shipping or duty notes for cross-border orders</li>
        </ul>
        <p>Avoid badge walls with ten generic seals. Pick three proofs that match your store's real policies.</p>
        <h2>Banners and accordions for campaign context</h2>
        <p>Short banners can explain why a gift appeared or why a discount applied — that transparency builds trust. Accordions work well for longer policy text without pushing the pay button below the fold on mobile.</p>
        <h2>Balance trust content with promotions</h2>
        <p>Checkout should read in this order: what I am buying → what I earn (gift/discount) → optional add-on → why it is safe to pay. Smart Checkout Widgets supports that sequence with gifting, upsells, banners, payment icons, and payment customization in one extension.</p>
        <h2>Quick audit before your next campaign</h2>
        <ol>
          <li>Open checkout on a phone and count taps to pay.</li>
          <li>List every payment method a first-time buyer sees.</li>
          <li>Remove trust claims you cannot substantiate in policy pages.</li>
          <li>Run a test order in each market you ship to.</li>
        </ol>
""",
    },
    {
        "slug": "shopify-plus-checkout-extensibility-guide.html",
        "title": "Shopify Plus Checkout Extensibility: A Merchant Guide | Smart Checkout Widgets",
        "description": "What Shopify Plus checkout extensibility means for merchandising teams — UI extensions, Functions, and where gifting and upsells fit.",
        "eyebrow": "checkout extensibility",
        "h1": "Shopify Plus checkout extensibility: what merchandising teams need to know",
        "secondary_label": "All blog guides",
        "secondary_href": "/blog/",
        "body": """
        <p>Checkout used to be the one place themes could not reach. Shopify Plus checkout extensibility changed that — merchants can now add UI and logic at the step where revenue is decided.</p>
        <h2>Checkout extensibility in plain language</h2>
        <p>Extensibility means approved apps can render blocks inside checkout and thank-you / order status surfaces. You customize the experience without editing checkout.liquid or breaking Shopify's compliance boundaries.</p>
        <h2>UI extensions vs Shopify Functions</h2>
        <ul>
          <li><strong>Checkout UI extensions</strong> control what shoppers see: gifts, upsells, banners, custom fields, accordions.</li>
          <li><strong>Shopify Functions</strong> control backend logic: discounts, payment customization, delivery rules, and validations.</li>
        </ul>
        <p>Merchandising teams care most about UI extensions. Operations and finance should be in the room when Functions change pricing or payment behavior.</p>
        <h2>What you can merchandise in checkout now</h2>
        <p>Common Plus use cases we see:</p>
        <ul>
          <li>Automatic gifts and customer-choice rewards</li>
          <li>Checkout upsells tied to cart contents</li>
          <li>Trust badges, payment icons, and campaign banners</li>
          <li>Custom fields for B2B or compliance notes</li>
          <li>Content on Thank You and Order Status pages (available on all stores for content widgets; Plus for full checkout UI)</li>
        </ul>
        <p>Some features in apps are Plus-only for checkout UI; always confirm on the app listing before you plan a launch around a specific block.</p>
        <h2>Who should own checkout experiments</h2>
        <p>Treat checkout like a product surface with a small RACI:</p>
        <ul>
          <li><strong>Growth / retention</strong> owns offer logic and copy</li>
          <li><strong>Operations</strong> owns inventory for gift SKUs</li>
          <li><strong>Finance</strong> signs off on margin impact</li>
          <li><strong>Support</strong> documents what customers see when a promotion fails</li>
        </ul>
        <h2>Getting started without a six-month project</h2>
        <ol>
          <li>Install a checkout extensibility app on a development or duplicate store.</li>
          <li>Ship one offer — a single threshold gift or one upsell.</li>
          <li>Measure completion rate and AOV for two weeks.</li>
          <li>Add trust content or payment tweaks only after baseline is stable.</li>
        </ol>
        <p>Smart Checkout Widgets bundles gifting, discounts, upsells, and trust content so you are not stitching five single-purpose apps together.</p>
        <h2>Related guides</h2>
        <p>Go deeper on specific tactics:</p>
        <ul>
          <li><a href="/blog/automatic-shopify-checkout-gifts.html">Automatic gifts in checkout</a></li>
          <li><a href="/blog/customer-choice-free-gift-shopify-checkout.html">Customer-choice free gifts</a></li>
          <li><a href="/blog/shopify-checkout-gift-strategy-aov.html">Gift strategy for higher AOV</a></li>
        </ul>
""",
    },
]

for post in POSTS:
    path = ROOT / "blog" / post["slug"]
    path.write_text(
        shell.render(
            slug=post["slug"],
            title=post["title"],
            description=post["description"],
            eyebrow=post["eyebrow"],
            h1=post["h1"],
            date=DATE,
            body_html=post["body"].strip(),
            secondary_label=post.get("secondary_label"),
            secondary_href=post.get("secondary_href", "/blog/"),
        ),
        encoding="utf-8",
    )
    print("Wrote", path.name)

# Patch blog index — append cards before closing post-grid
index_path = ROOT / "blog/index.html"
index = index_path.read_text(encoding="utf-8")
new_cards = ""
for post in POSTS:
    slug = post["slug"]
    link = f"/blog/{slug}"
    meta = post["eyebrow"].title()
    title_short = post["h1"] if len(post["h1"]) < 72 else post["title"].split("|")[0].strip()
    desc = post["description"][:120] + ("…" if len(post["description"]) > 120 else "")
    new_cards += f"""
        <article class="post-card">
          <p class="blog-meta">{meta}</p>
          <h3><a href="{link}">{title_short}</a></h3>
          <p>{desc}</p>
          <a class="text-link" href="{link}">Read article →</a>
        </article>"""

marker = "      </div>\n    </section>\n    <section class=\"inner-cta\">"
if marker in index and new_cards.strip() not in index:
    index = index.replace(marker, f"{new_cards}\n      </div>\n    </section>\n    <section class=\"inner-cta\">")
    index_path.write_text(index, encoding="utf-8")
    print("Updated blog/index.html")

# Homepage blog strip — add two newest as extra cards (keep existing 3)
home_path = ROOT / "index.html"
home = home_path.read_text(encoding="utf-8")
extra = ""
for post in POSTS[:2]:
    slug = post["slug"]
    link = f"/blog/{slug}"
    meta = post["eyebrow"].title()
    title_short = post["h1"][:60] + ("…" if len(post["h1"]) > 60 else "")
    desc = post["description"][:100] + "…"
    extra += f"""
          <article class="blog-card">
            <p class="blog-card__meta">{meta}</p>
            <h3><a href="{link}">{title_short}</a></h3>
            <p>{desc}</p>
            <a class="blog-card__link" href="{link}">Read article →</a>
          </article>"""

marker_home = "        </div>\n      </div>\n    </section>\n\n    <section class=\"cta\">"
if marker_home in home and "shopify-checkout-upsells.html" not in home:
    home = home.replace(marker_home, f"{extra}\n        </div>\n      </div>\n    </section>\n\n    <section class=\"cta\">")
    home_path.write_text(home, encoding="utf-8")
    print("Updated index.html blog strip")

print("Done.")
