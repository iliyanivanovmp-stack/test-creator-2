# Panafrica CRO Research Brief

**Data Sources:** Meta Ads & Landing Pages, Google Ads Transparency, Reviews & UGC, PageSpeed/Core Web Vitals, Current Site Screenshots, Competitor Analysis (self-researched)

## Insights

Panafrica's homepage is the site's single biggest liability. Mobile LCP is 16.6 seconds and Time to Interactive is 23.4 seconds (Lighthouse, simulated throttling, September 2026) — more than 6x Google's "poor" threshold. Most mobile visitors abandon before the page becomes usable, and the ones who wait have to scroll three full screens before seeing a product, a price, or a single trust signal — Source: pagespeed.md, site-visual-summary.md.

Paid traffic is running three uncoordinated offers at once. Meta's floating "-10€" bubble appears on every ad-linked landing page, but only Ad 3's copy states it ("-10€ sur votre première commande"). Ad 1's landing page instead surfaces an unrelated WhatsApp Club banner (15€ off). Google Ads separately promotes "jusqu'à -40%... jusqu'au 28 juillet" — a promo already past its own stated end date, still serving live. A visitor who sees more than one channel gets three different numbers — Source: meta-ads-visual-summary.md, google-ads-visual-summary.md.

Ninety-plus customer reviews of the Sahara model converge on comfort and color originality as what customers love ("confort incroyable," "j'adore l'agencement des couleurs"). The single most repeated complaint, raised independently by dozens of reviewers over more than a year of orders, is that the shoes run large: "le modèle taille grand ! Prendre une taille en moins," "sans doute 2 tailles en dessous." This persists despite an existing sizing note on the PDP — the guidance isn't cutting through at the point of decision — Source: reviews.md.

Site data also shows two live inconsistencies worth fixing before they're tested: an AOV-driving cross-sell block that renders on ad-traffic Arusha PDPs but not on the standard-traffic Sahara-Safran PDP using the same template, and several Google Ads Transparency Center tiles currently serving broken creative (unfilled `<Prix>`, `<Rating (Reviews)>` placeholders, one raw "500. That's an error." tile) — Source: site-visual-summary.md, google-ads-visual-summary.md.

No monthly session or AOV figures were provided for Panafrica, so none of the slots below carry a dollar estimate. Every opportunity is sized by evidence strength and fixability instead.

---

## Slot 1: Fix homepage Largest Contentful Paint

**Type:** Immediate Fix

**What's broken:** The homepage hero (a two-panel collage-style lifestyle image, "NOUVELLE COLLECTION" headline, single "DÉCOUVRIR" CTA) takes 16.6 seconds to render its largest element on mobile, with a Time to Interactive of 23.4 seconds. Performance score is 0.49. Source: pagespeed.md (Lighthouse, homepage, mobile, simulated throttling).

**Why this is the priority:** LCP this severe is well past the range where most mobile visitors abandon before they can interact with the page at all. Every other homepage fix in this roadmap is wasted if visitors never wait long enough to see it.

**What we're fixing:** Diagnose and resolve the render-blocking cost behind the 16.6s LCP and 23.4s TTI, starting with hero image weight/format and any third-party or render-blocking scripts loading before first paint. Note: PDP shares a near-identical ~23s TTI despite a much lower 4.2s LCP, suggesting a shared render-blocking or third-party script cost worth checking during this fix rather than treating the homepage in isolation.

**Success metrics:**
- Mobile LCP under 4s (target: sub-2.5s to clear Google's "good" threshold)
- Mobile TTI reduced from 23.4s
- Lighthouse performance score above 0.49

---

## Slot 2: Add a shop-now path to homepage fold 1

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (https://panafrica-store.com/)
**Revenue potential:** Sessions/mo not provided — cannot calculate $. Directional: zero purchase path or trust signal across 3 homepage folds is a structural conversion gap independent of traffic volume.

**Hypothesis:** If we add a product, price, and trust signal to homepage fold 1, more visitors will continue to shop because they no longer have to scroll three screens to see what's for sale or why to trust the brand.

**Data:** Fold 1 currently shows only the lifestyle hero collage and a single "DÉCOUVRIR" CTA — no product, price, or trust signal. Fold 2 repeats brand messaging ("BASKETS MADE IN AFRICA") with a name-only product row and no prices. Priced, buyable product cards don't appear until fold 3. No star rating or review count appears anywhere in folds 1-3. Source: site-visual-summary.md, live WebFetch of panafrica-store.com.

**V1:** Keep the existing lifestyle hero image and headline, but add a compact shop-now element within fold 1: one to two featured products with visible price, plus a star rating/review count line near the CTA. Mobile: stack hero image, then a horizontally scrollable product strip with price and rating directly beneath the "DÉCOUVRIR" CTA, no added scroll depth. Desktop: place the same product strip with prices and rating inline within fold 1, beside or below the hero image, so it is visible without scrolling.

---

## Slot 3: Unify the discount offer across Meta, Google, and on-site

**Type:** Immediate Fix

**What's broken:** Three different offers are live at once. Meta's floating "-10€" bubble appears sitewide (PDP, cart) regardless of entry point, but only Ad 3's copy states it in-ad; Ads 1 and 2 make no discount claim, and Ad 1's landing page instead promotes an unrelated WhatsApp Club 15€ discount via its top banner. Google Ads separately runs "jusqu'à -40% sur une sélection de paires, jusqu'au 28 juillet" — a promo already past its own stated end date, still serving live, plus "Retours gratuits." No offer is consistent across channels. Source: meta-ads-visual-summary.md, google-ads-visual-summary.md.

**Why this is the priority:** This touches 100% of paid traffic entering the funnel. Message match between ad and landing page is a documented top-5 landing-page CRO lever, and right now every paid channel is breaking it.

**What we're fixing:** Pick one sitewide offer, state it consistently in every ad's copy, retire the expired Google -40% promo, and remove or reconcile the WhatsApp Club banner so it doesn't compete with the site's primary offer.

**Success metrics:**
- One offer live across Meta ad copy, Google ad copy, and on-site messaging
- Zero expired promos still serving
- Ad-to-landing-page message match confirmed on all three Meta ads

---

## Slot 4: Fix broken Google Ads creative variants

**Type:** Immediate Fix

**What's broken:** Multiple currently-active tiles in the Google Ads Transparency Center grid render unfilled dynamic template variables instead of real values (`<Prix>`, `<Rating (Reviews)>`, `<Category>`, `<distance>`), and one tile shows a raw "500. That's an error. There was an error. Please try again later." creative in place of an ad. At least 4 distinct broken/placeholder tiles were observed in a 25+ tile grid. Source: google-ads-visual-summary.md.

**Why this is the priority:** This is live ad spend serving broken creative to prospects. Low effort, high confidence, and it's actively costing money right now regardless of any other fix on this roadmap.

**What we're fixing:** Audit all active Google Ads variants for unfilled dynamic-variable placeholders and error-state creative, and pause or correct every broken tile.

**Success metrics:**
- Zero live tiles with unfilled template variables
- Zero live tiles serving an error-state creative

---

## Slot 5: Add prominent sizing reassurance at the PDP size selector

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (https://panafrica-store.com/products/sahara-safran)
**Revenue potential:** Sessions/mo not provided — cannot calculate $. Directional: sizing is the single most repeated complaint theme across the entire 90+ review set, spanning over a year of orders.

**Hypothesis:** If we surface a clear "runs large, size down" callout directly at the size selector instead of relying on the existing PDP sizing note, fewer customers will hesitate or buy the wrong size, because the sizing complaint keeps recurring despite that note already existing.

**Data:** The PDP size selector (36-46 range, unavailable sizes greyed out) sits below the product title and above the two-tier CTA stack ("Acheter en 1-clic" / "Ajouter au panier"). A Femme/Homme sizing conversion note exists on the page but is not prominent at the point of size selection. Across 90+ reviews, dozens of independent reviewers report the same issue: "le modèle taille grand ! Prendre une taille en moins," "Taillent grand," "sans doute 2 tailles en dessous," "J'aurai dû prendre la taille en dessous." Source: reviews.md, site-visual-summary.md.

**V1:** Add a short, inline fit callout directly beneath the size selector (not buried in an accordion), e.g. "Ce modèle taille grand — la plupart des clients prennent une taille en dessous." Keep the existing size grid and CTA stack unchanged. Mobile: callout sits directly under the size buttons, above the CTA stack, no accordion or tap-to-expand. Desktop: same placement, inline beneath the size selector within the buy box.

---

## Slot 6: Standardize the cross-sell block across all PDPs

**Type:** Immediate Fix

**What's broken:** On ad-traffic Arusha PDPs, a "Nos recommandations" cross-sell block (e.g., "Accra" shoe at 85€, "Sac Kariba congrès" tote at 20€) renders directly below the delivery-estimate copy, right after the CTA stack. The standard-traffic Sahara-Safran PDP, same template, does not show this block in the equivalent fold. Source: meta-ads-visual-summary.md (Ad 2/3 landing pages), site-visual-summary.md (Sahara-Safran PDP).

**Why this is the priority:** This is a template inconsistency, not a design decision — the block already renders correctly on some PDPs using the identical template. Standardizing it sitewide is a straightforward AOV lever that's already proven to work elsewhere on the same site.

**What we're fixing:** Confirm why the cross-sell block is missing on the Sahara-Safran PDP fold and roll it out consistently across every PDP using this template.

**Success metrics:**
- Cross-sell block present on 100% of PDPs using this template
- No template-level rendering inconsistencies between ad-traffic and organic PDPs

---

## Slot 7: Add trust signal to homepage and collection page

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (https://panafrica-store.com/) and Collection page
**Revenue potential:** Sessions/mo not provided — cannot calculate $. Directional: trust signal is present on only 1 of 3 core page types reviewed.

**Hypothesis:** If we add the star rating/review count block to the homepage and collection page, more visitors will trust the brand earlier in the journey, because that same trust block already sits in the highest-priority position on every PDP (directly under the product title, above the buy box) and is completely absent everywhere else.

**Data:** The 5-star/review-count block appears prominently on every PDP. The homepage (3 folds reviewed) shows no star rating or review count anywhere. The collection page product grid shows only image, name, and price on each card, with no star rating. Source: site-visual-summary.md.

**V1:** Homepage — add a star rating/review count line within fold 1, next to or below the shop-now product strip from Slot 2. Collection page — add a star rating line to each product card, positioned consistently under the price on every card. Mobile: rating shown as a compact star icon plus count on both homepage and collection cards, no added row height on collection cards. Desktop: same placement, sized to match existing card typography.

---

## Slot 8: Resolve collection-grid quick-add inconsistency

**Type:** Immediate Fix

**What's broken:** One product card mid-grid on the collection page shows a full size run (36-43, 44-47) and an "Add to cart" button rendered directly in the grid card. Every other card on the same grid shows only product image, name, and price with no inline purchase controls. It is unclear whether this is a hover-state artifact, a layout bug, or a partially rolled-out quick-add feature. Source: site-visual-summary.md (flagged as an open question during data collection).

**Why this is the priority:** A single inconsistent card in an otherwise uniform grid reads as broken to a shopper, regardless of intent. This needs to be confirmed as either a bug or a feature before it can be treated as a design decision.

**What we're fixing:** Investigate whether the inline size selector and "Add to cart" on this card is an intended hover-state, a partially built feature, or a rendering bug, and either fix it to match the rest of the grid or confirm and finish the rollout consistently across all cards.

**Success metrics:**
- Every card in the collection grid renders identically (same controls, same layout)
- Root cause documented (bug vs. intentional feature) and resolved accordingly

---

## Future Slot Candidates

1. **Add a guarantee/returns trust element adjacent to the PDP buy box** - Shipping and returns copy ("Livraison et Retours offerts dès 100€") currently sits one fold below the CTA stack instead of directly beside it. The standard pattern of placing a low-risk reassurance signal next to the primary CTA is untested here.
2. **Investigate and resolve "Coming soon" / stock-status contradiction on Arusha PDPs** - Live WebFetch (2026-09-02) of all three ad-linked Arusha PDPs shows a "Coming soon" indicator displayed alongside in-stock messaging and functioning size selectors. This was not visible in the collected screenshots, so it needs client confirmation before being treated as a live, blocking issue.
3. **Vegan-specific landing experience for Google Ads** - Google Ads' "vegan" angle differs from the ethical/eco-responsible cluster used elsewhere, but there isn't enough evidence yet to size this as a standalone test.
