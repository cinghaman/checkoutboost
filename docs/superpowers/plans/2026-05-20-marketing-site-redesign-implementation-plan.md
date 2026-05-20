# Marketing Site Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign the Smart Checkout Widgets marketing site into a technical-editorial system that increases install clarity while making the site SEO/AEO ready and improving social preview imagery.

**Architecture:** Introduce a locked site system in `design.md` plus shared tokens in `tokens.css`, then refit the existing static HTML pages to that system in place. Keep the current route/file structure, reduce decorative motion, separate page families visually, and wire consistent metadata, schema, internal linking, and preview-image assets across homepage, blog, utility, and legacy marketing pages.

**Tech Stack:** Static HTML, CSS, vanilla JS, JSON-LD structured data, local screenshot verification with Playwright, local HTTP server for browser QA

---

## File Structure

### Shared system files

- Create: `design.md`
- Create: `tokens.css`
- Modify: `style.css`
- Modify: `site.js`

Responsibilities:
- `design.md` locks the genre, page families, token system, CTA voice, messaging rules, SEO/AEO rules, and preview-image direction.
- `tokens.css` defines the shared named tokens consumed by every page.
- `style.css` becomes the shared technical-editorial skin across all page families.
- `site.js` keeps only restrained motion and behavior that still helps orientation and interaction.

### Homepage family

- Modify: `index.html`

Responsibilities:
- establish the new install-first homepage structure
- make category/audience/value explicit in extractable language
- own the strongest metadata, schema, and homepage preview asset

### Content/blog family

- Modify: `blog/index.html`
- Modify: `blog/automatic-shopify-checkout-gifts.html`
- Modify: `blog/customer-choice-free-gift-shopify-checkout.html`
- Modify: `blog/shopify-checkout-gift-strategy-aov.html`

Responsibilities:
- shift articles to a stronger long-document reading experience
- separate blog-hub intent from article intent
- add article-specific metadata, summaries, and schema

### Utility pages

- Modify: `videos.html`
- Modify: `privacy.html`

Responsibilities:
- apply the shared system without marketing-page theatrics
- clean up metadata quality and page structure

### Legacy secondary marketing pages

- Modify: `tech-partners.html`
- Modify: `cro-techniques.html`
- Modify: `microsoft-pixel-tracking-shopify-plus.html`
- Modify: `api-intgreation.html`

Responsibilities:
- bring old pages onto the shared system
- fix inconsistent metadata and old-style visual drift

### Preview-image assets

- Create: `images/og-home-technical-editorial.svg`
- Create: `images/og-blog-index-technical-editorial.svg`
- Create: `images/og-article-gifts.svg`
- Create: `images/og-article-customer-choice.svg`
- Create: `images/og-article-aov-strategy.svg`
- Create: `images/og-videos.svg`
- Create: `images/og-privacy.svg`

Responsibilities:
- provide reusable social-card assets aligned to the new system
- stop relying on generic product screenshots as the only preview mechanism

---

### Task 1: Lock the shared system in `design.md` and `tokens.css`

**Files:**
- Create: `design.md`
- Create: `tokens.css`
- Test: `index.html`

- [ ] **Step 1: Write the shared design system document**

Add `design.md` with the locked system sections below:

```md
# Design — Smart Checkout Widgets

## Genre
modern-minimal with a technical-editorial overlay

## Macrostructure family
- Marketing pages: Marquee Hero -> Long Document hybrid
- Content pages: Long Document
- Utility pages: Flat document utility

## Theme
- --color-paper
- --color-paper-2
- --color-ink
- --color-ink-2
- --color-rule
- --color-accent
- --color-focus

## Typography
- Display: sharp editorial sans/serif pairing chosen during implementation
- Body: neutral readable text face
- Mono: compact UI/supporting face if needed

## Motion
- reveal pattern: restrained fade/slide only
- reduced motion: opacity-only, <= 150ms

## CTA voice
- Primary CTA: install-oriented filled button
- Secondary CTA: proof/education button

## SEO/AEO rules
- one clear H1 per page
- unique title/description/canonical
- direct category/audience language
- FAQ and article passages written for extraction

## Preview-image direction
- short claim
- cropped UI fragment
- strong brand identifier
- restrained accent usage
```

- [ ] **Step 2: Create the portable token file**

Add `tokens.css` with the initial token surface:

```css
:root {
  --color-paper: oklch(97% 0.012 85);
  --color-paper-2: oklch(94% 0.01 85);
  --color-ink: oklch(23% 0.03 255);
  --color-ink-2: oklch(42% 0.02 250);
  --color-rule: oklch(88% 0.01 90);
  --color-accent: oklch(70% 0.16 145);
  --color-accent-ink: oklch(18% 0.02 145);
  --color-focus: oklch(63% 0.16 145);

  --font-display: "Satoshi", "Plus Jakarta Sans", sans-serif;
  --font-body: "Source Sans Pro", "Plus Jakarta Sans", sans-serif;
  --font-ui: "Aktiv Grotesk", "Plus Jakarta Sans", sans-serif;

  --space-3xs: 0.25rem;
  --space-2xs: 0.5rem;
  --space-xs: 0.75rem;
  --space-sm: 1rem;
  --space-md: 1.5rem;
  --space-lg: 2rem;
  --space-xl: 3rem;
  --space-2xl: 4.5rem;
  --space-3xl: 7rem;

  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-md: 1rem;
  --text-lg: 1.25rem;
  --text-xl: 1.75rem;
  --text-2xl: 2.5rem;
  --text-display: clamp(3rem, 7vw, 6rem);
  --text-display-s: clamp(2.4rem, 5vw, 4.5rem);

  --radius-card: 1.25rem;
  --radius-pill: 999px;
  --radius-input: 0.875rem;

  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  --dur-short: 180ms;
  --dur-med: 260ms;
}
```

- [ ] **Step 3: Wire the token file into the homepage first**

Update the `<head>` order in `index.html` to load tokens before `style.css`:

```html
<link rel="stylesheet" href="/tokens.css">
<link rel="stylesheet" href="/style.css">
```

- [ ] **Step 4: Verify the token file is referenced**

Run: `rg -n "tokens.css|style.css" index.html`

Expected: one `tokens.css` line before one `style.css` line

- [ ] **Step 5: Commit**

```bash
git add design.md tokens.css index.html
git commit -m "feat: add locked design system and shared tokens"
```

### Task 2: Rebuild the shared shell and motion system

**Files:**
- Modify: `style.css`
- Modify: `site.js`
- Test: `index.html`

- [ ] **Step 1: Replace the root design language in `style.css`**

At the top of `style.css`, swap hard-coded palette values for token consumption and add the Hallmark stamp:

```css
/* Hallmark · genre: modern-minimal · macrostructure: site-system-shell · design-system: design.md · designed-as-app */

html,
body {
  overflow-x: clip;
}

body {
  background: linear-gradient(180deg, var(--color-paper) 0%, var(--color-paper-2) 100%);
  color: var(--color-ink);
  font-family: var(--font-body);
  line-height: 1.65;
}

h1,
h2,
h3,
.brand-title {
  color: var(--color-ink);
  font-family: var(--font-display);
}
```

- [ ] **Step 2: Refactor shared shell classes away from pastel-glass styling**

Replace the header/surface styling with quieter technical-editorial surfaces:

```css
.site-header {
  background: color-mix(in oklab, var(--color-paper) 92%, transparent);
  border-bottom: 1px solid var(--color-rule);
  position: sticky;
  top: 0;
}

.nav-shell-glass,
.page-panel,
.post-card,
.pricing-card,
.metric-card,
.premium-card,
.faq-item,
.footer-shell {
  background: color-mix(in oklab, var(--color-paper) 96%, var(--color-ink) 4%);
  border: 1px solid var(--color-rule);
  box-shadow: none;
}

.btn-primary {
  background: var(--color-accent);
  color: var(--color-accent-ink);
}
```

- [ ] **Step 3: Simplify motion and remove decorative hero effects**

Reduce `site.js` to essential behavior:

```js
function initReveal() {
  var revealEls = document.querySelectorAll(".reveal");

  if (prefersReduced || typeof gsap === "undefined" || typeof ScrollTrigger === "undefined") {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
    return;
  }

  gsap.registerPlugin(ScrollTrigger);

  revealEls.forEach(function (el) {
    gsap.to(el, {
      opacity: 1,
      y: 0,
      duration: 0.45,
      ease: "power2.out",
      scrollTrigger: { trigger: el, start: "top 90%" }
    });
  });
}

function initHeroCanvas() {
  return;
}
```

- [ ] **Step 4: Verify JS syntax and CSS references**

Run:
- `node --check site.js`
- `rg -n "var\\(--color-|var\\(--font-" style.css | sed -n '1,20p'`

Expected:
- no output from `node --check`
- multiple token references printed from `style.css`

- [ ] **Step 5: Commit**

```bash
git add style.css site.js
git commit -m "feat: rebuild shared shell and reduce decorative motion"
```

### Task 3: Redesign the homepage and wire core SEO/AEO surfaces

**Files:**
- Modify: `index.html`
- Test: `index.html`

- [ ] **Step 1: Replace the homepage hero and section rhythm**

Restructure `index.html` so the first viewport states the product clearly:

```html
<section class="hero hero-brief">
  <div class="shell hero-brief-grid">
    <div class="hero-brief-copy">
      <p class="eyebrow">For ecommerce agencies and Shopify Plus teams</p>
      <h1>Checkout merchandising for Shopify Plus installs, not just experiments.</h1>
      <p class="hero-text">Smart Checkout Widgets helps agencies and operators launch checkout gifts, upsells, trust content, and payment messaging without stitching together brittle workflows.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="https://apps.shopify.com/smart-checkout-widgets">Install on Shopify</a>
        <a class="btn btn-secondary" href="#proof">See operator proof</a>
      </div>
    </div>
    <figure class="hero-proof-figure">
      <img src="/images/screen2.webp" alt="Smart Checkout Widgets customer-choice gift selection in Shopify checkout">
      <figcaption>Automatic gifts, customer choice, upsells, and trust content in one checkout surface.</figcaption>
    </figure>
  </div>
</section>
```

- [ ] **Step 2: Add answer-engine-friendly summary and FAQ framing**

Insert a concise summary block before the major sections:

```html
<section class="section section-summary" aria-labelledby="summary-title">
  <div class="shell summary-grid">
    <h2 id="summary-title">What Smart Checkout Widgets does</h2>
    <p>Smart Checkout Widgets is a Shopify Plus app for checkout gifting, checkout upsells, trust messaging, payment-method presentation, and checkout merchandising.</p>
    <p>It is built for teams that want more checkout control without relying on manual campaign stitching or multiple narrow tools.</p>
  </div>
</section>
```

- [ ] **Step 3: Update metadata, OG image, and schema**

Replace the existing homepage metadata block with page-intent-specific values:

```html
<title>Smart Checkout Widgets | Shopify Plus Checkout Merchandising App</title>
<meta name="description" content="Install a Shopify Plus app for checkout gifts, checkout upsells, trust messaging, and checkout merchandising built for ecommerce agencies and operators.">
<meta property="og:title" content="Shopify Plus checkout merchandising for agencies and operators">
<meta property="og:description" content="Checkout gifts, upsells, trust messaging, and payment control in one Shopify Plus app.">
<meta property="og:image" content="https://smartcheckoutwidgets.com/images/og-home-technical-editorial.svg">
<meta name="twitter:image" content="https://smartcheckoutwidgets.com/images/og-home-technical-editorial.svg">
```

Add a clearer `SoftwareApplication` schema description:

```json
{
  "@type": "SoftwareApplication",
  "name": "Smart Checkout Widgets",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Shopify Plus",
  "description": "A Shopify Plus checkout merchandising app for gifts, upsells, trust messaging, and payment presentation."
}
```

- [ ] **Step 4: Verify homepage metadata and section targets**

Run:
- `rg -n "<title>|meta name=\"description\"|og:image|SoftwareApplication" index.html`
- `python3 -m http.server 4173`

Expected:
- metadata lines print with the new terms
- local server starts on port 4173

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "feat: redesign homepage with install-first SEO structure"
```

### Task 4: Rebuild blog hub and article pages for long-document search intent

**Files:**
- Modify: `blog/index.html`
- Modify: `blog/automatic-shopify-checkout-gifts.html`
- Modify: `blog/customer-choice-free-gift-shopify-checkout.html`
- Modify: `blog/shopify-checkout-gift-strategy-aov.html`
- Test: `blog/index.html`

- [ ] **Step 1: Redesign the blog index around operator search intent**

Replace the blog index hero with a tighter archive intro:

```html
<section class="page-hero page-hero-journal">
  <div class="shell page-hero-copy">
    <p class="eyebrow">Journal</p>
    <h1>Checkout gifting and Shopify Plus field notes.</h1>
    <p>Practical guidance for ecommerce agencies and Shopify Plus operators working on gifts, upsells, trust messaging, and conversion clarity.</p>
  </div>
</section>
```

- [ ] **Step 2: Add article-intent summary blocks near the top of each article**

For each blog article, insert a compact “in this article” summary after the hero:

```html
<section class="shell article-summary">
  <p>This guide explains when to use automatic checkout gifts, what they change operationally, and how to connect them to Shopify Plus merchandising goals.</p>
</section>
```

- [ ] **Step 3: Upgrade blog metadata and add `Article` schema**

For each article, use page-specific metadata and insert schema:

```html
<meta property="og:image" content="https://smartcheckoutwidgets.com/images/og-article-gifts.svg">
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to launch automatic gifts in Shopify checkout",
  "author": { "@type": "Organization", "name": "Smart Checkout Widgets" },
  "publisher": { "@type": "Organization", "name": "Smart Checkout Widgets" }
}
</script>
```

- [ ] **Step 4: Verify article uniqueness**

Run:
- `rg -n "<title>|meta name=\"description\"|@type\": \"Article\"|og:image" blog/*.html`

Expected:
- each blog page returns its own metadata and one `Article` schema block

- [ ] **Step 5: Commit**

```bash
git add blog/index.html blog/automatic-shopify-checkout-gifts.html blog/customer-choice-free-gift-shopify-checkout.html blog/shopify-checkout-gift-strategy-aov.html
git commit -m "feat: redesign blog pages for search and long-document reading"
```

### Task 5: Redesign utility and older marketing pages onto the shared system

**Files:**
- Modify: `videos.html`
- Modify: `privacy.html`
- Modify: `tech-partners.html`
- Modify: `cro-techniques.html`
- Modify: `microsoft-pixel-tracking-shopify-plus.html`
- Modify: `api-intgreation.html`
- Test: `privacy.html`

- [ ] **Step 1: Normalize utility-page shell and metadata**

For `videos.html` and `privacy.html`, ensure the same shared header/footer and metadata pattern:

```html
<meta property="og:image" content="https://smartcheckoutwidgets.com/images/og-videos.svg">
<meta property="og:image" content="https://smartcheckoutwidgets.com/images/og-privacy.svg">
<main id="main-content">
```

Also remove stale `keywords` meta usage from `privacy.html`.

- [ ] **Step 2: Strip old secondary pages of legacy visual drift**

In each legacy page:
- load `/tokens.css` before `/style.css`
- swap any legacy header/footer blocks to the shared shell
- rewrite hero/top sections into page-family-appropriate intros

Use a shared intro pattern:

```html
<section class="page-hero">
  <div class="shell page-hero-copy">
    <p class="eyebrow">Guide</p>
    <h1>...</h1>
    <p>...</p>
  </div>
</section>
```

- [ ] **Step 3: Verify metadata cleanup on utility pages**

Run:
- `rg -n "meta name=\"keywords\"|tokens.css|og:image|twitter:image" privacy.html videos.html tech-partners.html cro-techniques.html microsoft-pixel-tracking-shopify-plus.html api-intgreation.html`

Expected:
- no `keywords` line in `privacy.html`
- each page prints `tokens.css`
- each page has preview-image metadata

- [ ] **Step 4: Visually smoke-test one utility page and one legacy page**

Run:
- `python3 -m http.server 4173`
- `env npm_config_cache=/tmp/npmcache PLAYWRIGHT_BROWSERS_PATH=/tmp/pw npx --yes playwright screenshot --device="Desktop Chrome" http://127.0.0.1:4173/privacy.html /tmp/privacy-check.png`

Expected:
- local server starts
- screenshot writes to `/tmp/privacy-check.png`

- [ ] **Step 5: Commit**

```bash
git add videos.html privacy.html tech-partners.html cro-techniques.html microsoft-pixel-tracking-shopify-plus.html api-intgreation.html
git commit -m "feat: roll shared system into utility and legacy marketing pages"
```

### Task 6: Create the social preview-image system

**Files:**
- Create: `images/og-home-technical-editorial.svg`
- Create: `images/og-blog-index-technical-editorial.svg`
- Create: `images/og-article-gifts.svg`
- Create: `images/og-article-customer-choice.svg`
- Create: `images/og-article-aov-strategy.svg`
- Create: `images/og-videos.svg`
- Create: `images/og-privacy.svg`
- Test: `index.html`

- [ ] **Step 1: Create the shared SVG art-direction frame**

Use one SVG structure for all preview assets:

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <rect width="1200" height="630" fill="oklch(97% 0.012 85)"/>
  <rect x="56" y="56" width="1088" height="518" rx="28" fill="oklch(94% 0.01 85)" stroke="oklch(88% 0.01 90)"/>
  <text x="96" y="170" fill="oklch(23% 0.03 255)" font-size="28" font-family="Arial, sans-serif">SMART CHECKOUT WIDGETS</text>
  <text x="96" y="280" fill="oklch(23% 0.03 255)" font-size="72" font-family="Arial, sans-serif">Shopify Plus checkout merchandising</text>
  <text x="96" y="356" fill="oklch(42% 0.02 250)" font-size="32" font-family="Arial, sans-serif">Gifts, upsells, trust messaging, and payment control.</text>
  <rect x="96" y="440" width="300" height="72" rx="999" fill="oklch(70% 0.16 145)"/>
  <text x="150" y="486" fill="oklch(18% 0.02 145)" font-size="28" font-family="Arial, sans-serif">Install on Shopify</text>
</svg>
```

- [ ] **Step 2: Write page-specific variants**

Change only the headline/subline and, where needed, add a product crop reference or different supporting copy:

```svg
<!-- og-article-gifts.svg -->
<text x="96" y="280" ...>How to launch automatic gifts in Shopify checkout</text>
<text x="96" y="356" ...>A practical guide for agencies and Shopify Plus operators.</text>
```

- [ ] **Step 3: Verify all preview assets are referenced**

Run:
- `rg -n "og-home-technical-editorial|og-blog-index-technical-editorial|og-article-|og-videos|og-privacy" index.html blog/*.html videos.html privacy.html`

Expected:
- each page prints the expected preview-image asset path

- [ ] **Step 4: Open one OG asset locally to confirm it renders**

Run:
- `python3 -m http.server 4173`
- `curl -I http://127.0.0.1:4173/images/og-home-technical-editorial.svg`

Expected:
- HTTP/1.0 200 OK

- [ ] **Step 5: Commit**

```bash
git add images/og-home-technical-editorial.svg images/og-blog-index-technical-editorial.svg images/og-article-gifts.svg images/og-article-customer-choice.svg images/og-article-aov-strategy.svg images/og-videos.svg images/og-privacy.svg index.html blog/*.html videos.html privacy.html
git commit -m "feat: add reusable social preview image system"
```

### Task 7: Final verification, schema checks, and polish cleanup

**Files:**
- Modify: `index.html`
- Modify: `blog/*.html`
- Modify: `videos.html`
- Modify: `privacy.html`
- Modify: `style.css`
- Modify: `site.js`
- Test: all Phase 1 pages

- [ ] **Step 1: Run metadata and schema grep checks**

Run:
- `rg -n "<title>|meta name=\"description\"|canonical|og:image|twitter:image|application/ld\\+json" index.html blog/*.html videos.html privacy.html`

Expected:
- every Phase 1 page returns all six categories

- [ ] **Step 2: Run local multi-page HTTP checks**

Run:

```bash
python3 -m http.server 4173
for u in / /blog/ /blog/automatic-shopify-checkout-gifts.html /blog/customer-choice-free-gift-shopify-checkout.html /blog/shopify-checkout-gift-strategy-aov.html /videos.html /privacy.html; do
  printf '%s ' "$u"
  curl -s -o /dev/null -w '%{http_code}\n' "http://127.0.0.1:4173$u"
done
```

Expected:
- each URL prints `200`

- [ ] **Step 3: Run desktop and mobile screenshot smoke tests**

Run:

```bash
env npm_config_cache=/tmp/npmcache PLAYWRIGHT_BROWSERS_PATH=/tmp/pw npx --yes playwright screenshot --device="Desktop Chrome" --wait-for-timeout 2000 http://127.0.0.1:4173 /tmp/home-final.png
env npm_config_cache=/tmp/npmcache PLAYWRIGHT_BROWSERS_PATH=/tmp/pw npx --yes playwright screenshot -b chromium --viewport-size "390,844" --wait-for-timeout 2000 http://127.0.0.1:4173 /tmp/home-mobile-final.png
```

Expected:
- both screenshot files are written without runtime errors

- [ ] **Step 4: Remove any stale old-style patterns discovered during QA**

Clean up any remaining instances of:

```text
rgba(255, 216, 239
backdrop-filter: blur(18px)
box-shadow: 0 30px 80px
```

Run:
- `rg -n "255, 216, 239|backdrop-filter: blur\\(18px\\)|0 30px 80px" style.css index.html blog/*.html videos.html privacy.html`

Expected:
- no matches, or only intentional matches explicitly retained

- [ ] **Step 5: Commit**

```bash
git add style.css site.js index.html blog/*.html videos.html privacy.html
git commit -m "chore: complete redesign QA and metadata verification"
```

---

## Self-Review

### Spec coverage

- Shared system and page families: Task 1, Task 2
- Homepage redesign: Task 3
- Blog/content redesign: Task 4
- Utility and legacy pages: Task 5
- SEO/AEO and metadata discipline: Task 3, Task 4, Task 5, Task 7
- Preview-image system: Task 6
- QA across desktop/mobile and motion-off posture: Task 2, Task 5, Task 7

No spec sections are currently uncovered.

### Placeholder scan

- No `TODO`, `TBD`, or “implement later” placeholders remain.
- Each task names exact files and concrete commands.
- Each code-changing step includes explicit snippets to apply.

### Type consistency

- Shared file names are used consistently: `design.md`, `tokens.css`, `style.css`, `site.js`
- Preview asset naming is consistent across tasks and metadata checks
- Page-family names are stable across the plan

