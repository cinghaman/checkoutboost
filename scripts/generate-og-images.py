#!/usr/bin/env python3
"""Generate branded 1200×675 OG preview images per article (Pastel / Hallmark palette)."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "images" / "og"
W, H = 1200, 675

# Approximate OKLCH Pastel tokens → sRGB
BG = (247, 248, 252)
INK = (26, 29, 46)
INK_MUTED = (82, 88, 110)
ACCENT = (91, 78, 232)
ACCENT_SOFT = (168, 162, 245)
TINT = (236, 234, 252)
COMPANION = (168, 220, 140)

SPECS = {
    "default": {
        "eyebrow": "Smart Checkout Widgets",
        "lines": ["Shopify Plus checkout", "gifts, upsells & merchandising"],
        "accent": ACCENT,
    },
    "automatic-gifts": {
        "eyebrow": "Automatic gifting",
        "lines": ["Launch automatic gifts", "in Shopify checkout"],
        "accent": ACCENT,
    },
    "customer-choice-gifts": {
        "eyebrow": "Customer choice",
        "lines": ["Why shopper-picked gifts", "beat fixed checkout offers"],
        "accent": COMPANION,
    },
    "gift-strategy-aov": {
        "eyebrow": "Checkout AOV",
        "lines": ["Gift strategy for", "higher average order value"],
        "accent": ACCENT,
    },
    "checkout-upsells": {
        "eyebrow": "Checkout upsells",
        "lines": ["Native upsells without", "breaking the final step"],
        "accent": ACCENT,
    },
    "bogo-discounts": {
        "eyebrow": "BOGO & discounts",
        "lines": ["Automatic discounts", "without coupon chaos"],
        "accent": COMPANION,
    },
    "trust-payments": {
        "eyebrow": "Trust & payments",
        "lines": ["Trust badges & payment", "customization at checkout"],
        "accent": ACCENT,
    },
    "checkout-extensibility": {
        "eyebrow": "Shopify Plus",
        "lines": ["Checkout extensibility", "for merchandising teams"],
        "accent": ACCENT,
    },
    "thank-you-order-status": {
        "eyebrow": "Post-purchase",
        "lines": ["Thank You & Order Status", "widgets that convert"],
        "accent": COMPANION,
    },
    "compare": {
        "eyebrow": "Comparison",
        "lines": ["Shopify checkout gift", "apps compared (2026)"],
        "accent": ACCENT,
    },
}

SLUG_TO_OG = {
    "automatic-shopify-checkout-gifts.html": "automatic-gifts",
    "customer-choice-free-gift-shopify-checkout.html": "customer-choice-gifts",
    "shopify-checkout-gift-strategy-aov.html": "gift-strategy-aov",
    "shopify-checkout-upsells.html": "checkout-upsells",
    "shopify-checkout-bogo-automatic-discounts.html": "bogo-discounts",
    "shopify-checkout-trust-badges-payment.html": "trust-payments",
    "shopify-plus-checkout-extensibility-guide.html": "checkout-extensibility",
    "shopify-thank-you-order-status-widgets.html": "thank-you-order-status",
}


def load_fonts():
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    bold = regular = None
    for path in candidates:
        p = Path(path)
        if p.exists():
            if "Bold" in path and bold is None:
                bold = ImageFont.truetype(str(p), 56)
            elif "Bold" not in path and regular is None:
                regular = ImageFont.truetype(str(p), 28)
    if bold is None:
        bold = ImageFont.load_default()
    if regular is None:
        regular = ImageFont.load_default()
    return bold, regular


def draw_card(draw, accent):
    draw.rounded_rectangle((72, 120, W - 72, H - 96), radius=28, fill=(255, 255, 255), outline=TINT, width=2)
    draw.rounded_rectangle((72, 120, 220, H - 96), radius=28, fill=accent)
    draw.ellipse((108, 168, 184, 244), fill=(255, 255, 255))


def render(spec_key: str, out_name: str) -> Path:
    spec = SPECS[spec_key]
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    bold, regular = load_fonts()
    accent = spec["accent"]

    draw.rounded_rectangle((0, 0, W, 8), radius=0, fill=accent)
    draw_card(draw, accent)

    draw.text((248, 168), spec["eyebrow"].upper(), fill=accent, font=regular)
    y = 220
    for line in spec["lines"]:
        draw.text((248, y), line, fill=INK, font=bold)
        y += 72

    draw.text((248, H - 148), "smartcheckoutwidgets.com", fill=INK_MUTED, font=regular)
    draw.text((248, H - 112), "Guides for Shopify Plus checkout", fill=INK_MUTED, font=regular)

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"{out_name}.webp"
    img.save(path, "WEBP", quality=88, method=6)
    print("Wrote", path.relative_to(ROOT))
    return path


def main():
    for key in SPECS:
        render(key, key)
    print("Done. Wire paths in scripts/apply-ai-seo.py OG_IMAGES map.")


if __name__ == "__main__":
    main()
