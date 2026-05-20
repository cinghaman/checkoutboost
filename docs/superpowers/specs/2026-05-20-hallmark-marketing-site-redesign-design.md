# Hallmark Marketing Site Redesign

Date: 2026-05-20
Project: Checkoutboost / Smart Checkout Widgets marketing site
Scope: Multi-page marketing-site redesign
Status: Approved for planning

## Goal

Redesign the full marketing site for Smart Checkout Widgets so it feels made for ecommerce agencies first and Shopify Plus operators second, while pushing one primary action: app installs.

This is a visual and structural redesign, not a route or content-system rebuild. The redesign must preserve the current product positioning, route structure, and install intent while replacing the site's current soft-pastel SaaS aesthetic with a more technical-editorial system.

## Audience

### Primary

Ecommerce agencies evaluating Shopify checkout tooling on behalf of clients.

What they care about:
- credible product framing
- operational clarity
- install confidence
- merchant-fit signals
- proof that the app can support real checkout merchandising work

### Secondary

Shopify Plus operators evaluating the app directly for their own stores.

What they care about:
- capability clarity
- ease of setup
- checkout control
- pricing fit
- confidence that the app will improve merchandising and order value

## Primary action

The redesigned site should drive app installs.

Secondary actions may support the install decision, but they should always feed the primary action:
- reading blog proof/education
- viewing product details
- reviewing pricing
- checking compatibility or FAQ

## Tone

Technical editorial.

Interpretation:
- more “operator brief” than “friendly SaaS”
- more “agency teardown deck” than “soft premium startup”
- clearer, sharper, and more commercially credible
- restrained rather than decorative

## Problem statement

The current site has a relatively polished shared shell, but its visual language still leans toward generic premium-SaaS patterns:
- soft pastel gradients
- glassy surfaces
- repeated card rhythms
- decorative motion and floating treatment
- a tone that feels more startup-friendly than operator-serious

This weakens trust for the actual audience. Ecommerce agencies and Shopify Plus operators respond better to a site that feels more decisive, legible, and structurally intentional.

## Redesign outcome

The redesigned site should:
- feel consistent across all marketing pages
- present Smart Checkout Widgets as a serious operational tool
- make install intent more explicit
- use stronger editorial hierarchy and document rhythm
- reduce reliance on decorative glow, glass, and “floating” UI styling
- remain clear and complete with motion reduced or disabled

## Redesign boundaries

This is an in-place redesign.

Preserve:
- route structure
- existing HTML page ownership
- product names
- factual claims already in the UI
- install-first intent
- general information architecture of each page

Replace:
- visual system
- section rhythm
- component voice
- page family structure
- typography hierarchy
- accent behavior
- decorative motion choices

Do not change without explicit approval:
- route trees
- page deletions
- production file removal
- app logic or integrations
- large copy rewrites that alter product positioning

## Page scope

### Phase 1: core redesign

- `index.html`
- `style.css`
- `site.js`
- `blog/index.html`
- `blog/automatic-shopify-checkout-gifts.html`
- `blog/customer-choice-free-gift-shopify-checkout.html`
- `blog/shopify-checkout-gift-strategy-aov.html`
- `videos.html`
- `privacy.html`
- `design.md`
- `tokens.css`

### Phase 2: system rollout to older secondary pages

- `tech-partners.html`
- `cro-techniques.html`
- `microsoft-pixel-tracking-shopify-plus.html`
- `api-intgreation.html`

No deletions are planned.

## Design system

The whole marketing site uses one locked design system. The site should not be redesigned page-by-page with unrelated themes.

### Genre

Modern-minimal with a technical-editorial overlay.

This means:
- modern product clarity
- editorial hierarchy and rhythm
- restrained embellishment
- document-like seriousness
- strong reading flow

### Theme

The new theme should move away from lavender/pastel glow and into a more credible operator-facing palette.

Core direction:
- paper: warm near-white
- ink: deep navy-charcoal
- accent: disciplined install-green
- rules/borders: quiet tinted neutrals

Rules:
- accent usage remains sparse and intentional
- primary install surfaces own the accent
- neutral surfaces should feel calm and operational, not glossy

### Typography

Typography should carry more of the page’s authority.

System direction:
- display face: sharper, more editorial, less rounded
- body face: highly readable and neutral
- labels/kickers: compact technical markers, used with restraint

Writing behavior:
- headlines should read like claims, positions, or operating principles
- avoid generic startup-copy cadence
- avoid excessive eyebrow/section-label repetition

### Motion

Motion should be minimal and subordinate to clarity.

Rules:
- no decorative floating for its own sake
- no heavy scroll theatrics
- motion should support orientation and interaction only
- reduced-motion mode must still leave the layout complete and credible

### CTA voice

CTAs must stay install-oriented.

Primary CTA:
- explicit install language
- compact, deliberate button shape
- accent-owned

Secondary CTA:
- proof or education oriented
- routes into supporting decision material
- never competes visually with install CTA

## Page families

### 1. Homepage family

Homepage uses a `Marquee Hero` to `Long Document` hybrid.

Intent:
- top of page makes the install case quickly
- rest of page reads like a structured operational brief
- argument is built through capability framing, checkout control, proof, pricing, FAQ, and install CTA

Visual behavior:
- fewer equal-weight card grids
- more alternation between dense text arguments and product evidence
- stronger hierarchy between primary and secondary proof

### 2. Content/blog family

Blog uses a `Long Document` family.

Intent:
- feel like field notes for agencies and operators
- prioritize reading over marketing theatrics

Visual behavior:
- stronger title block
- tighter metadata treatment
- clearer reading width
- quieter chrome
- more serious article hierarchy

### 3. Utility/secondary family

Utility pages include privacy, videos, and older secondary pages.

Intent:
- feel maintained and on-system
- stay flatter and more restrained than homepage

Visual behavior:
- same type, color, and CTA language
- less hero treatment
- simpler sectioning
- typography-first layout when possible

## Shared rules

The following must remain consistent across all page families:
- wordmark treatment
- accent color behavior
- display/body pairing
- CTA shape and install-first language
- section heading rhythm
- border/rule treatment
- spacing scale

The following may vary:
- hero composition by page family
- whether a page uses product imagery
- proof section structure
- content density between homepage and content pages

## Implementation approach

This is a non-destructive redesign.

Implementation model:
1. create `design.md` as the locked system definition
2. create `tokens.css` as the portable shared token layer
3. refit `style.css` to the new system
4. simplify `site.js` where needed to match the new motion stance
5. redesign Phase 1 pages against the locked system
6. roll the system into Phase 2 pages

## File responsibilities

### `design.md`

Source of truth for:
- genre
- page-family structure
- theme tokens
- typography system
- spacing
- motion stance
- CTA voice
- page-level allowances

### `tokens.css`

Portable design tokens:
- color
- font
- spacing
- type scale
- easing
- duration
- radius
- rule tokens

### `style.css`

Shared visual implementation for:
- layout
- typography
- surfaces
- CTAs
- nav/footer
- page-family patterns
- responsive behavior

### `site.js`

Only keep what supports:
- restrained reveal behavior
- interaction state handling
- utility page affordances

Any decorative motion that conflicts with the new system should be removed or reduced.

## Verification requirements

The redesign is only complete when it passes all of the following:
- no horizontal scroll
- install CTA remains primary on homepage and key secondary pages
- desktop and mobile are checked on homepage, one blog page, and one utility page
- motion-off experience still feels complete
- no page drifts back into old pastel-glass language
- typography and spacing remain consistent across page families

Target widths:
- 320 px
- 375 px
- 414 px
- 768 px
- desktop standard widths

## Risks and mitigations

### Risk: visual inconsistency across old pages

Mitigation:
- lock `design.md` before rollout
- treat older pages as Phase 2, not ad hoc one-offs

### Risk: homepage becomes too editorial and weakens install focus

Mitigation:
- keep install CTA dominant
- ensure proof and capability sections support the install action directly

### Risk: redesign preserves too much of the old aesthetic

Mitigation:
- explicitly remove pastel-glow/glass defaults
- shift palette, hierarchy, and section rhythm at the system level first

### Risk: redesign becomes too austere and loses warmth

Mitigation:
- keep paper tone warm rather than cold
- use accent sparingly but confidently
- preserve enough product imagery to keep the site concrete

## Out of scope

The following are not part of this redesign unless requested later:
- app product UI redesign
- analytics changes
- app-store listing rewrite
- major copy strategy rewrite
- route consolidation
- CMS or framework migration

## Recommended next step

Create the locked site system in `design.md`, then write an implementation plan for:
1. shared tokens and visual shell
2. homepage redesign
3. blog/content family redesign
4. utility page redesign
5. Phase 2 legacy-page rollout
