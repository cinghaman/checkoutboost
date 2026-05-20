#!/usr/bin/env python3
"""Add Thank You / Order Status blog post and patch indexes."""

from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("shell", ROOT / "scripts/blog-article-shell.py")
shell = importlib.util.module_from_spec(spec)
spec.loader.exec_module(shell)

DATE = "May 20, 2026"
SLUG = "shopify-thank-you-order-status-widgets.html"

POST = {
    "slug": SLUG,
    "title": "Thank You and Order Status Widgets for Shopify | Smart Checkout Widgets",
    "description": "Use Thank You and Order Status page widgets to extend checkout campaigns — what to show after purchase, Plus vs all stores, and how to avoid duplicate offers.",
    "eyebrow": "thank you & order status",
    "h1": "Thank You and Order Status widgets: what to show after the sale",
    "secondary_label": "Checkout extensibility guide",
    "secondary_href": "/blog/shopify-plus-checkout-extensibility-guide.html",
    "body": """
        <p>Checkout is where revenue is decided. Thank You and Order Status pages are where you reinforce the decision — and earn the next one. Treat them as part of the same merchandising system, not an afterthought buried in email flows.</p>
        <h2>Why post-purchase surfaces still matter</h2>
        <p>Shoppers who just paid are in a high-trust moment. They are looking for confirmation, tracking, and what happens next. A clear Thank You page reduces support tickets. A useful Order Status page keeps them in your ecosystem instead of refreshing carrier sites.</p>
        <p>That is also when second-purchase intent is warm: replenishment reminders, referral prompts, or a single product recommendation can work — if the message matches what they already bought.</p>
        <h2>Plus checkout UI vs content on every store</h2>
        <p>Shopify Plus merchants can customize checkout UI with extensions — gifts, upsells, trust blocks, and payment tweaks at the step before payment.</p>
        <p>Thank You and Order Status pages are different: <strong>content-based widgets</strong> on those surfaces are available on all Shopify stores, not only Plus. Full checkout UI customization still requires Plus; post-purchase content is how non-Plus brands (and Plus brands between campaigns) stay on-brand after the order.</p>
        <p>Plan accordingly: run high-stakes offers in checkout on Plus; use Thank You / Order Status for reinforcement, education, and lightweight upsells that do not compete with the pay step.</p>
        <h2>What to put on Thank You vs Order Status</h2>
        <ul>
          <li><strong>Thank You page</strong> — Confirm the gift or discount they earned, set delivery expectations, invite account creation or SMS tracking, and one secondary CTA (referral, review, or complementary product).</li>
          <li><strong>Order Status page</strong> — Shipping updates, support links, reorder shortcuts, and campaign banners that stay valid while the order is open (not expired promo codes).</li>
        </ul>
        <p>Avoid repeating the same upsell block they already declined in checkout. Post-purchase content should add information or a different angle — not nag.</p>
        <h2>Five layouts that work without clutter</h2>
        <ol>
          <li><strong>Reward recap</strong> — "Your free gift ships with this order" with a thumbnail of the SKU they unlocked.</li>
          <li><strong>Policy accordion</strong> — Returns, duties, or subscription terms in collapsible sections so the hero stays calm.</li>
          <li><strong>Trust strip</strong> — Payment and security icons plus one line on support contact hours.</li>
          <li><strong>Single recommendation</strong> — One add-on or refill tied to the line items in the confirmation, not a full catalog grid.</li>
          <li><strong>Lifecycle banner</strong> — Loyalty program, B2B portal, or wholesale application for the segments you cannot merchandise in consumer checkout.</li>
        </ol>
        <h2>Connect Thank You content to checkout campaigns</h2>
        <p>When checkout runs a threshold gift or automatic discount, the Thank You page should explain <em>why</em> the line item appears — same copy tone, same rules. Shoppers who understand the promotion are less likely to cancel or dispute.</p>
        <p>If you use checkout upsells, reserve Order Status for replenishment or cross-sell after fulfillment starts. Sequencing beats showing every offer on every surface.</p>
        <h2>How Smart Checkout Widgets fits</h2>
        <p>Smart Checkout Widgets supports merchandising in checkout on Shopify Plus — gifting, upsells, BOGO, trust content, and payment customization — and extends to Thank You and Order Status pages for content widgets across stores. One app keeps offer logic and visual language aligned from pay button to tracking page.</p>
        <p>Start with one block on Thank You (reward recap or trust strip), measure support volume and repeat purchase rate for two weeks, then add Order Status content if the first test stays readable on mobile.</p>
        <h2>Related guides</h2>
        <ul>
          <li><a href="/blog/shopify-plus-checkout-extensibility-guide.html">Shopify Plus checkout extensibility overview</a></li>
          <li><a href="/blog/shopify-checkout-upsells.html">Checkout upsells without breaking the final step</a></li>
          <li><a href="/blog/shopify-checkout-gift-strategy-aov.html">Gift strategy for higher AOV</a></li>
        </ul>
""",
}

path = ROOT / "blog" / POST["slug"]
path.write_text(
    shell.render(
        slug=POST["slug"],
        title=POST["title"],
        description=POST["description"],
        eyebrow=POST["eyebrow"],
        h1=POST["h1"],
        date=DATE,
        body_html=POST["body"].strip(),
        secondary_label=POST["secondary_label"],
        secondary_href=POST["secondary_href"],
    ),
    encoding="utf-8",
)
print("Wrote", path.name)

card = f"""
        <article class="post-card">
          <p class="blog-meta">Thank You &amp; Order Status</p>
          <h3><a href="/blog/{SLUG}">Thank You and Order Status widgets: what to show after the sale</a></h3>
          <p>Use Thank You and Order Status page widgets to extend checkout campaigns — what to show after purchase, Plus vs all stores, and how to avoid duplicate offers.</p>
          <a class="text-link" href="/blog/{SLUG}">Read article →</a>
        </article>"""

index_path = ROOT / "blog/index.html"
index = index_path.read_text(encoding="utf-8")
marker = "      </div>\n    </section>\n    <section class=\"inner-cta\">"
if SLUG not in index and marker in index:
    index = index.replace(marker, f"{card}\n      </div>\n    </section>\n    <section class=\"inner-cta\">")
    index = index.replace(
        "Practical guides on gifting, upsells, BOGO, trust content, payment customization, and Shopify Plus checkout extensibility.",
        "Practical guides on gifting, upsells, BOGO, trust content, checkout extensibility, and Thank You / Order Status widgets.",
    )
    index_path.write_text(index, encoding="utf-8")
    print("Updated blog/index.html")

home_path = ROOT / "index.html"
home = home_path.read_text(encoding="utf-8")
home_card = f"""
          <article class="blog-card">
            <p class="blog-card__meta">Thank You &amp; Order Status</p>
            <h3><a href="/blog/{SLUG}">Thank You and Order Status widgets: what to show after the sale</a></h3>
            <p>Extend checkout campaigns on Thank You and Order Status pages — without repeating the same upsell.</p>
            <a class="blog-card__link" href="/blog/{SLUG}">Read article →</a>
          </article>"""
marker_home = "        </div>\n      </div>\n    </section>\n\n    <section class=\"cta\">"
if SLUG not in home and marker_home in home:
    home = home.replace(marker_home, f"{home_card}\n        </div>\n      </div>\n    </section>\n\n    <section class=\"cta\">")
    home = home.replace(
        "Guides on upsells, BOGO, trust content, checkout extensibility, and gift strategy for Shopify Plus.",
        "Guides on upsells, BOGO, trust content, extensibility, Thank You / Order Status widgets, and gift strategy.",
    )
    home_path.write_text(home, encoding="utf-8")
    print("Updated index.html blog strip")

ext_path = ROOT / "blog/shopify-plus-checkout-extensibility-guide.html"
ext = ext_path.read_text(encoding="utf-8")
link_line = '          <li><a href="/blog/shopify-thank-you-order-status-widgets.html">Thank You and Order Status widgets</a></li>'
if link_line not in ext:
    ext = ext.replace(
        '          <li><a href="/blog/shopify-checkout-gift-strategy-aov.html">Gift strategy for higher AOV</a></li>\n        </ul>',
        '          <li><a href="/blog/shopify-checkout-gift-strategy-aov.html">Gift strategy for higher AOV</a></li>\n'
        + link_line
        + "\n        </ul>",
    )
    ext_path.write_text(ext, encoding="utf-8")
    print("Updated extensibility guide cross-link")

print("Done.")
