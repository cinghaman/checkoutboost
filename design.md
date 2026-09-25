# Design — Smart Checkout Widgets

A locked design system for the Smart Checkout Widgets marketing site. Every page redesign reads this file before emitting code. Do not regenerate per page. Extend or amend the system here when the site needs to grow.

## Genre

Modern-minimal with a technical-editorial overlay.

## Macrostructure family

- Marketing pages: Marquee Hero -> Long Document hybrid
- Content pages: Long Document
- Utility pages: Flat document utility

## Theme

- `--color-paper`
- `--color-paper-2`
- `--color-ink`
- `--color-ink-2`
- `--color-rule`
- `--color-accent`
- `--color-accent-ink`
- `--color-focus`

The palette should read as warm near-white paper, deep navy-charcoal ink, and a disciplined install-green accent. Neutral surfaces should feel operational and quiet, not glossy.

## Typography

- Display: Satoshi, 700 weight, normal style
- Body: Source Sans Pro, 400 weight
- UI support: Aktiv Grotesk, 600 weight
- Display tracking: -0.04em
- Type scale anchor: `--text-display` = `clamp(3rem, 7vw, 6rem)`

## Motion

- Reveal pattern: restrained fade/slide only
- Reduced-motion fallback: opacity-only, <= 150ms
- Decorative floating effects: not allowed

## Microinteractions stance

- Silent success over celebratory feedback
- Instant focus ring
- Hover feedback only where it strengthens clarity
- Motion should support orientation and interaction only

## CTA voice

- Primary CTA: install-oriented filled button using the accent
- Secondary CTA: proof or education oriented

## SEO/AEO rules

- One clear H1 per page
- Unique title, description, canonical, OG, and Twitter metadata per page
- Direct category and audience language near the top of the page
- FAQ and article passages written in short, extractable language
- Articles should include summary framing near the top

## Preview-image direction

- Short claim
- Cropped UI fragment or product cue
- Strong brand identifier
- Restrained accent usage
- Built for social cards and search previews rather than full desktop screenshots

## Audience

- Primary: Shopify merchants on any plan (Basic, Shopify, Advanced, Plus) who install apps themselves
- Secondary: ecommerce agencies and Shopify Plus operators

Changed 2026-09-25. Most installs are non-Plus stores, and they were leaving within
minutes because every page sold a Plus-only app. Agencies install for Plus stores, but
only a store admin can leave an App Store review, so the self-serve merchant is the one
the site must win.

## Product framing

The site should be easy to summarize as:

- a Shopify checkout customizer that works on every plan
- payment and shipping method rules (hide Cash on Delivery, rename shipping rates) and Thank You / Order Status page blocks, on any plan
- checkout gifts, upsells and custom fields on Shopify Plus

Lead with what works on every plan. Name Plus only where Shopify actually requires it,
and tag features with the plans they work on rather than warning about Plus.
