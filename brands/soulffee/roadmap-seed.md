# Soulffee Roadmap Seed

**Store:** https://www.soulffee.com/
**AOV:** $32.00 (single 30-serving unit; 60-serving available at higher price)
**Monthly sessions:** Unknown (no analytics access)
**Data sources:** PageSpeed (mobile, Jul 8 2026), site screenshots (homepage 4 folds, PDP 3 folds, cart mobile), live site fetch (homepage + PDP)

## Key Insights

Single-SKU brand (Mushroom Orzo) with a direct homepage-to-PDP funnel and no collection page. The biggest commercial gap is subscription default: the PDP pre-selects one-time purchase ($32.00) over Subscribe & Save ($25.92, 19% off), meaning the highest-LTV action is presented as the opt-in option rather than the default. For a brand whose whole proposition is a daily ritual, OTP as default is a structural revenue leak.

Mobile performance is critically broken. Homepage LCP is 10.3 seconds (score 0/1); PDP LCP is 14.9 seconds (score 0/1). TTI on the PDP is 17.5 seconds — the page is unresponsive for nearly 18 seconds on mobile. At these load times a significant portion of paid and organic mobile traffic bounces before the hero loads. CLS is clean on both pages (0 and 0.013), so layout shift is not the issue — the bottleneck is image and resource loading.

Three CTA dead zones exist across the funnel: (1) the homepage hero CTA "TRY NOW" is below the viewport on load, requiring a scroll before users can act; (2) the homepage comparison table (fold 4, the deepest content) ends with no CTA; (3) the cart has zero upsell or AOV mechanics — no 60-serving upgrade, no bundle, no cross-sell, and the announcement bar ("Save Up to 38% Today") promises a discount that has no corresponding mechanism in cart. Social proof is thin: 38 reviews at 4.8 stars exist but are not visible within the first 3 PDP folds, and the homepage shows "4.8+ stars" with no review count.

## Top Test Opportunities

### 1. Subscribe & Save Default Selection
**What's broken:** On the PDP buy box (fold 1, right column), there are two radio buttons stacked vertically. The bottom radio — "One Time Purchase $32.00" — is pre-selected with a filled circle indicator. Above it sits "Subscribe & Save SAVE 19% $25.92 ~~$32.00~~" which is unselected (empty circle). Both options are displayed in similar visual weight with no badge, highlight, or "most popular" label distinguishing the subscription. A user landing on the PDP sees OTP as the active default and must actively switch to subscribe. No explanation of subscription terms is visible without expanding the "Subscription Perks +" accordion below the buy box.
**Evidence:** PDP-f1 screenshot, live PDP fetch
**Key data:** Subscription saves 19% ($25.92 vs $32.00). Subscription perks include free cancellation, free North American shipping, 30-day guarantee, early access. 38 reviews at 4.8 stars confirm product satisfaction — the conversion barrier is commitment, not product quality.
**Est. lift:** Converting 15-25% of current OTP buyers to subscription; LTV multiplier depends on churn rate but any subscription shift is the highest-value test available on a single-SKU store.

### 2. Hero CTA Above the Fold
**What's broken:** On the homepage (fold 1), the hero spans the full viewport with a left-aligned headline ("Calm Mind, Clear Focus, No Jitters"), subtext (3 lines), and a star rating row. The "TRY NOW →" CTA button — a white pill button — is cut off at the bottom of fold 1 and only becomes fully visible in fold 2. On most mobile viewports, the button is not visible without scrolling. The vertical sticky tab ("LIMITED SOULFFEE - UP TO 45% OFF") on the right edge and the announcement bar ("FREE shipping on all orders!") consume additional vertical space, pushing the CTA further down.
**Evidence:** homepage-f1.png, homepage-f2.png
**Key data:** CTA appears at the bottom of fold 1 and is only fully visible in fold 2. No above-fold action is available on load.
**Est. lift:** 5-10% increase in homepage-to-PDP CTR; standard above-fold CTA test with consistent validation across e-commerce.

### 3. 60-Serving Upgrade Prompt in Cart
**What's broken:** The mobile cart page shows a single line item: "Mushroom Orzo, 30 servings, qty 2, $32.00 each, $64.00 subtotal." Below the line item is a shipping estimate collapsible and a "CONGRATS YOU'VE UNLOCKED FREE SHIPPING!" bar with a full dark green progress bar. After that: order note textarea, subtotal, tax note. No upsell widget, product recommendation, or upgrade prompt exists anywhere in the cart. The 60-serving variant is available on the PDP (shown as the alternate size in the size selector row) but is never surfaced in the cart flow.
**Evidence:** cart-drawer screenshot, PDP-f1 screenshot (60-serving variant confirmed)
**Key data:** Free shipping already unlocked at $64 — progress bar mechanic has no further lever. 60-serving upgrade is a natural 2x AOV increase for a returning buyer.
**Est. lift:** 10-15% of cart visitors accept upgrade; at $32 → ~$54 upgrade (60-serving estimated), that's ~$22 AOV lift per converted session.

### 4. Comparison Table CTA (Homepage)
**What's broken:** Fold 4 of the homepage is the final visible content: a two-column comparison table (Soulffee vs. Mushroom Coffee) with 6 attribute rows and checkmarks. Soulffee wins 5 of 6 rows. Below the last table row, the page ends — no CTA, no trust signal, no section break. The sticky nav is visible at the top and the sticky side tab is on the right, but no conversion action is presented at the natural end of the homepage reading flow.
**Evidence:** homepage-f4.png
**Key data:** The comparison table is the deepest homepage section; scroll-depth cohorts at this point are high-intent. A CTA immediately below the table closes the loop for users who read the full page.
**Est. lift:** 3-7% increase in homepage CVR from high-scroll-depth visitors.

### 5. Reviews Block Near Buy Box
**What's broken:** The PDP buy box (fold 1, right column) shows a star rating line: "★★★★★ 38 reviews" as a clickable link. Below the buy box: product description, size selector, purchase toggle, and "TRY IT NOW" button. The reviews section is not captured in any of the 3 PDP folds — it exists on the page but is positioned far below the buy box, requiring significant scrolling to reach. No review snippet or quote is visible near the purchase decision point. The "Why Soulffee?" accordion (open by default) contains 5 brand-authored bullet points but no customer voice.
**Evidence:** PDP-f1, PDP-f2, PDP-f3 screenshots (no review block visible in any); live fetch confirms 38 reviews exist with samples ("Smooth and rich, without the bitterness"; "Gentle on my stomach")
**Key data:** 4.8/5 average, 38 reviews. Top review themes: taste, smooth energy, stomach-friendly.
**Est. lift:** 4-8% PDP CVR improvement from surfacing 2-3 top reviews within or directly below the buy box.

## Unused Findings

- Product naming inconsistency: URL slug `/products/soulffee` vs. in-page title "Mushroom Orzo" — may suppress branded search click-through and creates a trust gap at the URL level.
- "Save Up to 38% Today" in cart announcement bar references a discount with no cart-level mechanism — broken promise that erodes trust at the final conversion step.
- Homepage star rating shows "4.8+ stars" with no review count — adding the count (e.g., "4.8 stars, 38 reviews") converts a vague claim into a verifiable signal.
- Performance: LCP 14.9s on PDP and 10.3s on homepage both score 0/1 — a dev sprint to optimize hero images and defer non-critical JS could unlock meaningful baseline CVR gains before any test runs.
