# Essentia CRO Research Brief

**Data Sources:** Meta Ads and Landing Pages, Google Ads Transparency Center, PageSpeed/Core Web Vitals, Current Site Screenshots, Competitor research (self-researched, Aug 5 2026)

Mobile speed is the dominant issue and it sits directly upstream of the drop-off you flagged. PDP LCP is 33.8 seconds with Time to Interactive at 42.6 seconds, both scoring 0/100. Homepage LCP is 11.8 seconds with TTI at 37.1 seconds. Both pages carry 1.4-1.5MB of unused JavaScript. A shopper who adds to cart on a page this slow is fighting the site the entire way to checkout. Source: PageSpeed/Core Web Vitals.

Trust content exists but sits in the wrong place. Star ratings show well above the PDP buy box, but the 120-night trial and 20-year warranty are collapsed inside accordions below Add to Cart. The cart page, the step closest to your flagged drop-off, has zero trust signals of any kind. Avocado Green (365-night trial, 25-year warranty) and Naturepedic (25-year warranty) both beat Essentia's terms, and a comparison-shopping visitor who doesn't expand the accordion never sees that Essentia is even in the conversation. Source: Current Site Screenshots, competitor research.

Promotion messaging breaks down at every touchpoint except cart. The sitewide 20% off banner appears on-site but in none of the three Meta ad creatives and none of the Google ad copy reviewed. Collection cards ($1,699-$3,599) and the PDP show full price only, no strikethrough, despite the live sale. The discount only shows up once a shopper reaches cart, where it's itemized correctly ("Discount Applied -$719.80"). Google's own ad set adds to the confusion with two different discount figures, 30% and 22%, neither matching the 20% shown on-site. Source: Meta Ads and Landing Pages, Google Ads Transparency Center, Current Site Screenshots.

One landing page also sends the wrong product: Meta Ad 1 names the "Grateful Bed Eight" mattress but links to the "Grateful Bed Jr" kids' mattress page. Anyone clicking with adult-mattress intent lands on the wrong product entirely. Source: Meta Ads and Landing Pages.

No monthly sessions or AOV figures were provided for this project, so dollar-sized revenue potential isn't available. Every test below carries a conservative CR lift estimate; ask the client for sessions/mo and AOV to convert these into dollar projections.

---

## Slot 1: PDP Mobile Page-Speed Remediation

**Type:** Immediate Fix
**Page:** Product Detail Page (Stratami)

**Why this is urgent:** PDP mobile LCP is 33.8 seconds and Time to Interactive is 42.6 seconds, both scoring 0/100. This is the page where add-to-cart happens, and a checkout flow inheriting this JS weight is a strong candidate for the purchase-completion drop-off flagged for this project.

**What's broken:** Initial mobile load pulls in a large image gallery, three buy-box dropdowns, an Affirm widget, and a Consumer Reports video simultaneously. Unused JavaScript totals ~1.4MB against 6.4MB total page weight, with 20.6 seconds of main-thread work.

**Fix:** Defer non-critical scripts (Affirm widget, video embed) until after the buy box renders. Lazy-load gallery images below the first product photo. Audit and remove unused JS bundles.

---

## Slot 2: Homepage Mobile Page-Speed Remediation

**Type:** Immediate Fix
**Page:** Homepage

**Why this is urgent:** Homepage mobile LCP is 11.8 seconds and TTI is 37.1 seconds, scoring 0/100. This is the entry point for most paid traffic from both Meta and Google.

**What's broken:** Full-bleed video hero loads above a horizontally-scrolling product carousel. Unused JavaScript totals ~1.5MB against 11.2MB total page weight, the heaviest page measured.

**Fix:** Replace autoplay video hero with a compressed static image plus lazy-loaded video, or defer video load until after LCP. Audit and remove unused JS bundles.

---

## Slot 3: Surface the Sitewide Discount on Collection and PDP Pricing

**Type:** A/B test (1 variation vs. control)
**Page:** Collection page and Product Detail Page
**Revenue potential:** Sessions/mo and AOV were not provided by the client. Conservative estimate: 2-4% CR lift once sized against those figures.

**Hypothesis:** If we show the 20% discount as strikethrough pricing on collection cards and the PDP, add-to-cart rate will increase because shoppers currently see full price everywhere except cart and may not register the sale is active before deciding to buy.

**Data:** Collection cards (Venti $1,699, Grateful Eight $1,999, Tatami $2,999, Stratami $3,599) and the PDP show "Starting at $X" with no compare-at price, despite the active "REST & RECHARGE SALE 20% OFF" banner. Cart shows the discount applied correctly ("Discount Applied -$719.80" on the $3,599 item), so the mechanic works, it's just invisible until checkout. Source: Current Site Screenshots.

**V1:** Add strikethrough original price plus discounted price next to it on every collection card and on the PDP price display, matching the discount already applied at cart. Desktop and mobile both show the same two-price format directly under the product name; no other layout change.

---

## Slot 4: Add Trust Signals to the Cart Page

**Type:** A/B test (1 variation vs. control)
**Page:** Cart
**Revenue potential:** Sessions/mo and AOV were not provided by the client. Conservative estimate: 2-4% CR lift on cart-to-checkout rate once sized against those figures.

**Hypothesis:** If we add trial, warranty, and shipping reassurance directly above the Checkout button, cart-to-checkout rate will increase because the cart currently has zero trust signals at the exact step closest to the flagged drop-off.

**Data:** The cart shows only a line item, thumbnail, quantity stepper, discount line, and a static "Checkout" button. No guarantee, returns policy, or warranty mention appears anywhere on the page. Source: Current Site Screenshots.

**V1:** Add a static trust bar directly above the Checkout button with three items: "120-Night Sleep Trial," "20-Year Warranty," and "Free Shipping." Same bar on mobile and desktop, positioned so it's visible without scrolling past the Checkout button.

---

## Slot 5: Surface Trial and Warranty Terms Near Add to Cart on PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page
**Revenue potential:** Sessions/mo and AOV were not provided by the client. Conservative estimate: 2-3% CR lift on PDP add-to-cart rate once sized against those figures.

**Hypothesis:** If we move the 120-night trial and 20-year warranty out of collapsed accordions and into a visible badge row below Add to Cart, add-to-cart rate will increase because comparison-shopping visitors currently have to tap to expand these terms while competitors' longer terms are visible without any interaction.

**Data:** Star rating (4.5, 36 reviews) sits above the buy box in good proximity to the CTA, but trial and warranty terms sit in collapsed accordions below Add to Cart. Avocado Green offers a 365-night trial and 25-year warranty; Naturepedic offers a 25-year warranty, both stronger than Essentia's terms on paper. Source: Current Site Screenshots, competitor research.

**V1:** Add a badge row directly below the Add to Cart button showing "120-Night Trial" and "20-Year Warranty" as visible text, no accordion or tap required. Same placement and copy on mobile and desktop. Accordion content stays as-is for shoppers who want more detail.

---

## Slot 6: Fix Ad 1 Product Mismatch

**Type:** Immediate Fix
**Page:** Meta Ad 1 landing page

**Why this is urgent:** This is a wrong-product landing experience for every click with adult-mattress intent, and it's the top of the funnel this audit was scoped around.

**What's broken:** Meta Ad 1 names the "Grateful Bed Eight" mattress and claims "top marks from leading independent reviewers." The linked landing page shows the "Grateful Bed Jr" kids' mattress instead, which also carries only 5 reviews, undercutting the ad's own claim.

**Fix:** Confirm with the client whether Ad 1 should point to the Grateful Bed Eight product page, then correct the link. Verify the destination page's review count supports the ad's "top marks" claim before reactivating.

---

## Slot 7: Emphasize the EMF Foam Protection Upsell on PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page
**Revenue potential:** Sessions/mo and AOV were not provided by the client. Conservative estimate: 3-5% AOV lift on completed orders once sized against those figures.

**Hypothesis:** If we visually highlight the EMF Foam Protection Upgrade option instead of leaving it as an unmarked dropdown defaulted to "No EMF Foam Protection," AOV will increase because shoppers currently have no visual cue that this upgrade exists before checking out.

**Data:** The PDP buy box has three dropdowns (Size, Height, EMF Foam Protection Upgrade) with no visual hierarchy between them. EMF Protection defaults to "No EMF Foam Protection" with no highlight, badge, or recommendation. Source: Current Site Screenshots.

**V1:** Add a highlighted border and a short "Recommended" label to the EMF Foam Protection option within the existing dropdown, no new module or page addition. Same treatment on mobile and desktop, sitting inline with the current buy box layout.

---

## Future Slot Candidates

1. **Route the Affirm financing ad (Ad 3) to a transactional page** - Ad 3 promotes 0% APR financing but links to an informational Affirm explainer page with no Add to Cart CTA across all three captured folds, leaving financing-motivated clicks with no path to buy.
2. **Reconcile the discount percentage across ad channels and site** - Google Ads reference both "up to 30%" and "up to 22%" savings, and Meta Ad 2 separately claims "30% on average" via HSA/FSA, none of which match the on-site 20% sale.
3. **Move certification and trust badges above the fold on homepage** - Certification badges (GOLS, GOTS, Well Living Lab, ISO) and the founder story don't appear until homepage fold 3, despite Google Ads leading with certification messaging that sends visitors looking for this exact proof.
