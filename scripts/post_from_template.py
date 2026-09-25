#!/usr/bin/env python3
"""Build a new article page from an existing one, keeping the site chrome.

Takes blog/hide-cash-on-delivery-shopify-checkout.html as the template and swaps
in title, description, URLs, share image, dates, body, FAQs (HTML and JSON-LD)
and the call-to-action buttons. Used for the September 2026 posts.
"""
import html, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "blog" / "hide-cash-on-delivery-shopify-checkout.html"
OLD_TITLE = "How to hide cash on delivery in Shopify checkout by cart value, country or customer"
OLD_DESC = "Cash on delivery drives refusals and return costs. Here is how to show it only where it makes sense, using payment method rules that run on any Shopify plan."


def make(slug, title, desc, eyebrow, og, og_alt, published, published_label, body, faqs, ctas,
         outdir="blog", kind="BlogPosting"):
    s = TEMPLATE.read_text()
    url = f"https://smartcheckoutwidgets.com/{outdir}/{slug}/"
    s = s.replace(OLD_TITLE, title).replace(OLD_DESC, desc)
    s = s.replace("https://smartcheckoutwidgets.com/blog/hide-cash-on-delivery-shopify-checkout/", url)
    s = s.replace("/images/og/hide-cod.webp", f"/images/og/{og}.webp")
    s = s.replace("Guide: hiding cash on delivery in Shopify checkout", og_alt)
    s = s.replace('"2026-09-09"', f'"{published}"')
    s = s.replace("◇ payment rules", f"◇ {eyebrow}")
    s = s.replace("Published September 9, 2026", published_label)
    if kind != "BlogPosting":
        s = s.replace('"@type": "BlogPosting"', f'"@type": "{kind}"', 1)

    a = s.index('      <article class="post-content">\n') + len('      <article class="post-content">\n')
    b = s.index('        <section class="post-faq"')
    s = s[:a] + body.strip("\n") + "\n\n" + s[b:]

    fa = s.index('          <div class="faq-list">\n') + len('          <div class="faq-list">\n')
    fb = s.index("          </div>\n        </section>", fa)
    s = s[:fa] + "".join(
        f'          <details class="faq-item">\n            <summary>{html.escape(q)}</summary>\n            <p>{ans}</p>\n          </details>\n'
        for q, ans in faqs) + s[fb:]

    ja = s.index('  "mainEntity": [')
    jb = s.index("  ]\n}\n  </script>", ja)
    items = ",\n".join("    " + json.dumps({"@type": "Question", "name": q, "acceptedAnswer": {
        "@type": "Answer", "text": re.sub("<[^>]+>", "", ans)}}, ensure_ascii=False) for q, ans in faqs)
    s = s[:ja] + '  "mainEntity": [\n' + items + "\n" + s[jb:]

    ca = s.index('        <div class="section-cta">')
    cb = s.index("        </div>\n      </article>", ca)
    s = s[:ca] + '        <div class="section-cta">\n' + "".join(f"          {c}\n" for c in ctas) + s[cb:]

    out = ROOT / outdir / f"{slug}.html"
    out.write_text(s)
    return out
