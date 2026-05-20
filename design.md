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

- Primary: ecommerce agencies
- Secondary: Shopify Plus operators

## Product framing

The site should be easy to summarize as:

- a Shopify Plus checkout merchandising app
- a Shopify checkout gifts and upsells tool
- a tool agencies can recommend and install for merchants
