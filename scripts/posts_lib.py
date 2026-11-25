"""Helpers for posts on the wide article template (cover, figures, notes, video)."""
from pathlib import Path
import re
from PIL import Image
from post_from_template import make, ROOT

INSTALL = '<a class="btn btn-primary" href="https://apps.shopify.com/smart-checkout-widgets" target="_blank" rel="noopener noreferrer">Install on Shopify</a>'
def docs(anchor, label): return f'<a class="btn btn-secondary" href="/docs/#{anchor}">{label}</a>'
def size(name): return Image.open(ROOT / 'images/blog' / f'{name}.webp').size
def fig(name, alt, cap):
    w, h = size(name)
    return f'<figure class="post-figure">\n  <img src="/images/blog/{name}.webp" width="{w}" height="{h}" alt="{alt}" loading="lazy" decoding="async">\n  <figcaption>{cap}</figcaption>\n</figure>'
def pair(*figs): return '<div class="post-pair">\n' + '\n'.join(figs) + '\n</div>'
def note(title, *ps): return f'<div class="post-note">\n  <p class="post-note__title">{title}</p>\n' + '\n'.join(f'  <p>{p}</p>' for p in ps) + '\n</div>'
def video(vid, poster, title, cap):
    return f'''<figure class="post-video">
  <div class="post-video__frame">
    <a class="post-video__play" href="https://youtu.be/{vid}" target="_blank" rel="noopener" data-video="{vid}" data-title="{title}" aria-label="Play video: {title}">
      <img src="/images/blog/{poster}.webp" width="1280" height="720" alt="">
      <span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3.5v17l14-8.5z"/></svg></span>
    </a>
  </div>
  <figcaption>{cap}</figcaption>
</figure>'''

# replaced the same day under a new name: images are cached for 30 days
RENAMED = {'shopify-delivery-date-picker', 'shopify-delivery-pickup-dates-florists-bakeries', 'shopify-split-shipping-rate-rules'}
def post(slug, title, desc, og_alt, deck, minutes, cover, cover_alt, body, faqs, ctas):
    out = make(slug, title, desc, 'guide', slug, og_alt, '2026-11-25', 'Published November 25, 2026', body, faqs, ctas)
    s = out.read_text()
    # share image: the template has moved on since post_from_template was written
    s = s.replace('/images/og/hide-cash-on-delivery-shopify-checkout.webp', f'/images/og/{slug}{"-2" if slug in RENAMED else ""}.webp')
    s = s.replace('Checkout payment step with Cash on Delivery hidden by a rule for carts over $500', og_alt)
    s = s.replace('</h1>\n', f'</h1>\n        <p>{deck}</p>\n', 1)
    s = s.replace('<span>Smart Checkout Widgets</span>', f'<span>{minutes} min read</span>', 1)
    w, h = size(cover)
    s = re.sub(r'(      </div>\n)(    </section>\n    <section class="post-layout">)',
        lambda m: m[1] + f'      <figure class="post-cover"><img src="/images/blog/{cover}.webp" width="{w}" height="{h}" alt="{cover_alt}" fetchpriority="high"></figure>\n' + m[2], s, count=1)
    out.write_text(s)

