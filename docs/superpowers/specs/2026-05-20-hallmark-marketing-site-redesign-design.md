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

## Growth and discoverability goals

The redesign must improve not just visual quality, but search and answer-surface performance.

This includes:
- classic SEO for core commercial and informational queries
- AEO readiness for answer engines and AI-assisted search experiences
- social/link preview quality through stronger preview imagery and metadata

The site should be easy to understand as:
- a Shopify checkout merchandising app
- a Shopify Plus gifting and upsell tool
- a tool ecommerce agencies can recommend and install for merchants

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
- improve topical clarity for search engines and answer engines
- strengthen social preview quality for links shared in Slack, X, LinkedIn, and search results

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
- use search-facing phrasing where it improves clarity, especially around Shopify Plus, checkout gifts, upsells, checkout merchandising, and agency/operator workflows

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

### Messaging discipline

Messaging should follow product-positioning rules that support both conversion and discoverability:
- use natural operator and agency language instead of generic SaaS jargon
- describe the product against the status quo, not abstract category language
- keep page-level language consistent enough that users and search engines can summarize the product the same way
- prioritize concrete workflow phrasing over vague claims like “streamline” or “optimize”

## Page families

### 1. Homepage family

Homepage uses a `Marquee Hero` to `Long Document` hybrid.

Intent:
- top of page makes the install case quickly
- rest of page reads like a structured operational brief
- argument is built through capability framing, checkout control, proof, pricing, FAQ, and install CTA
- page must clearly answer what the app is, who it is for, and why it is better than doing checkout merchandising manually or with narrower tools

Visual behavior:
- fewer equal-weight card grids
- more alternation between dense text arguments and product evidence
- stronger hierarchy between primary and secondary proof

### 2. Content/blog family

Blog uses a `Long Document` family.

Intent:
- feel like field notes for agencies and operators
- prioritize reading over marketing theatrics
- capture mid-funnel search intent around gifting, checkout upsells, Shopify Plus checkout customization, trust messaging, and related operator workflows

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

## SEO and AEO requirements

The redesign must treat SEO and answer-engine readiness as part of the product surface.

### SEO requirements

- Every page must have a unique title tag and meta description aligned to page intent.
- Canonical URLs must remain explicit and correct.
- Heading structure must be disciplined: one clear H1, then semantic H2/H3 hierarchy.
- Core pages must target distinct search intent instead of overlapping heavily.
- Internal linking should reinforce page relationships between homepage, pricing, FAQ, blog guides, and install surfaces.
- Images must use meaningful alt text tied to product capability or page context.
- Existing structured data should be reviewed and expanded where appropriate instead of left as a minimal stub.

### AEO requirements

- Key pages should answer high-intent questions directly in short, extractable language.
- FAQ content should be written to work for both humans and answer systems.
- Body copy should contain concise definition-style and comparison-ready passages where relevant.
- The homepage should clearly state the category, audience, and primary jobs-to-be-done in plain language.
- Blog pages should include scannable summaries, strong subheads, and direct answers near the top of the article where useful.
- The site should avoid vague positioning language that makes it hard for answer systems to summarize what the product does.

### Structured data requirements

At minimum, the redesign plan should account for:
- Organization schema
- SoftwareApplication schema
- Article schema on blog posts
- FAQPage schema where FAQ sections remain appropriate
- Breadcrumb-style structure only if it matches actual page architecture

### Search-surface content requirements

The redesign should explicitly support:
- ecommerce agency discovery
- Shopify Plus operator discovery
- branded product discovery
- informational blog discovery
- install-intent queries that compare manual checkout merchandising against app-supported workflows

## Social preview and image-preview requirements

The redesign must include a deliberate preview-image system, not an incidental screenshot choice.

### Requirements

- Homepage needs a stronger Open Graph / Twitter preview image aligned to the new design system.
- Blog pages need consistent article-preview imagery or a defined preview-image treatment.
- Preview images should be legible at small sizes and support product recognition quickly.
- Preview imagery should avoid cluttered full-page screenshots as the only solution.
- The preview system should be reusable across future marketing pages.

### Preview-image direction

Preview images should feel like:
- product-credible
- typographically strong
- visually consistent with the site system
- optimized for social cards and search previews rather than full desktop layouts

Possible pattern:
- short claim
- product crop or UI fragment
- disciplined accent usage
- strong brand identifier

### Deliverable expectation

The implementation plan should include:
- shared preview-image art direction
- asset requirements for homepage and blog previews
- metadata wiring for Open Graph and Twitter cards

## Implementation approach

This is a non-destructive redesign.

Implementation model:
1. create `design.md` as the locked system definition
2. create `tokens.css` as the portable shared token layer
3. define SEO/AEO and preview-image system requirements inside the shared site system
4. refit `style.css` to the new system
5. simplify `site.js` where needed to match the new motion stance
6. redesign Phase 1 pages against the locked system
7. roll the system into Phase 2 pages

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
- SEO/AEO content rules
- preview-image direction

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
- search-surface readability and scannability conventions

### `site.js`

Only keep what supports:
- restrained reveal behavior
- interaction state handling
- utility page affordances

Any decorative motion that conflicts with the new system should be removed or reduced.

### Page metadata and preview assets

Each page should be reviewed for:
- title tag
- meta description
- canonical
- Open Graph fields
- Twitter card fields
- preview image path
- relevant structured data

## Verification requirements

The redesign is only complete when it passes all of the following:
- no horizontal scroll
- install CTA remains primary on homepage and key secondary pages
- desktop and mobile are checked on homepage, one blog page, and one utility page
- motion-off experience still feels complete
- no page drifts back into old pastel-glass language
- typography and spacing remain consistent across page families
- metadata is page-specific and not duplicated blindly
- homepage and blog previews render credibly as social cards
- answer-ready sections are present where they materially help discoverability

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

### Risk: redesign improves visuals but weakens search clarity

Mitigation:
- make category and audience language explicit in the system
- keep page intent distinct across homepage, blog, and secondary pages
- include SEO/AEO review in the implementation plan rather than treating it as post-launch cleanup

### Risk: preview images remain generic screenshots

Mitigation:
- define preview-image art direction before implementation
- treat OG/Twitter imagery as shared system output, not per-page improvisation

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
1. shared tokens, messaging rules, and visual shell
2. SEO/AEO and preview-image system
3. homepage redesign
4. blog/content family redesign
5. utility page redesign
6. Phase 2 legacy-page rollout
