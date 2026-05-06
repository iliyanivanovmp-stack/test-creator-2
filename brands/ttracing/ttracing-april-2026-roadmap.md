# TTRacing Australia CRO Research Brief

**Data Sources:** Meta Ads (3 ads), Google Ads Transparency, Reviews & UGC, Page Speed / Core Web Vitals, Competitor Research, Site Screenshots (Easter Bundle LP, Surge X PDP, TACTO LP, Cart Drawer)

---

## Insights

TTRacing's biggest problem is not product quality. Reviews consistently praise build quality, comfort, and aesthetics across chairs and desks. The problem is conversion friction at every stage of their paid funnel, starting with a site that barely loads on mobile.

Their primary traffic destination - the Easter bundle deals page - scores 25 on mobile PageSpeed with a 20.3-second Largest Contentful Paint. The industry benchmark is under 2.5 seconds. Most mobile visitors bounce before a single product appears. Every test recommended below is operating at a fraction of its potential until this is resolved. This must be raised with TTRacing as a pre-test prerequisite.

Of the 3 Meta ads analyzed (from a larger active campaign portfolio), 2 of 3 have direct friction issues. One sends buyers who clicked on the Swift X 2020 Ant-Man Edition at A$339 to the Surge X at A$399 - a different product at a higher price, with no mention of the Ant-Man edition on the landing page. Another drops paid traffic into an editorial campaign page with no price and no add-to-cart visible in the first three folds. Google Search ads still reference "Comfort for work and gaming in 2025" and display promo codes that expired in October 2025 - both running in April 2026.

The bundle deals landing page - where the brand focuses its paid spend - presents 7 competing bundles in a flat grid with no hierarchy, no recommendation, and no social proof. There are no star ratings, no customer quotes, and no "best seller" signal anywhere on the page. Reviews show TTRacing has strong product satisfaction. None of that sentiment reaches the page where purchase decisions are made.

Size and fit is the single biggest post-purchase complaint from Australian customers. Multiple reviewers - including people under 170cm - found their chair too small after delivery. Secretlab, the brand recommended in every Australian gaming chair roundup, solves this before purchase with a three-size system and a published height and weight guide. TTRacing has no equivalent visible on any gaming chair PDP. This is a conversion gap and a competitive gap simultaneously.

---

## Before Testing: Two Client Actions

These are quick fixes that require no A/B test. Recommend TTRacing act on both before any test launches.

1. **Fix Ad 1 message mismatch:** The Ant-Man Edition ad (running since November 2025) sends buyers to the Surge X PDP. Update the ad link to the correct Swift X 2020 product page, or update the ad copy to match.
2. **Fix stale Google copy:** Remove "2025" from search ad headlines. Remove the October 2025 promo code sitelink. These are live trust-damaging errors, not test candidates.

---

## Slot 1: Social Proof on the Bundle Landing Page

**Type:** A/B test (1 variation vs. control)
**Page:** Easter bundle deals landing page (https://ttracing.com.au/pages/easter-festive-bundle-deals). This page structure is used for all major sale periods and is the brand's stated primary paid traffic destination.
**Revenue potential:** Traffic data unavailable for this page. Even a conservative 0.5% absolute CR lift on a high-traffic paid landing page at an average bundle AOV of A$350 (lowest bundles start at A$219; desk combos from A$489) represents significant monthly revenue gain. Exact figure requires baseline session volume from the brand.

**Hypothesis:** If we add star ratings and a review count to each bundle card on the deals landing page, purchase confidence will increase because visitors currently see no evidence that the products in these bundles are trusted - and TTRacing's own reviews show strong satisfaction that is invisible at the point of decision.

**Data:** The Easter bundle landing page has no reviews, star ratings, or customer quotes anywhere on it (Source: Site Screenshots). Reviews collected from TTRacing's platform show repeated praise for product quality: "Feels much sturdier than any other gaming chair we have bought," "Great chair for a great price," "Fantastic chair for a great price" - yet none of this sentiment reaches the page driving the most paid traffic (Source: Reviews & UGC). The CRO ebook recommends adding social proof inside the cart and checkout process, and moving FAQ sections higher on paid landing pages - both indicating that trust signals close to the point of purchase are disproportionately impactful. Research across ecommerce A/B tests shows that social proof additions to product and collection pages drive 5-15% CR lifts depending on baseline review volume and placement.

**V1:** Add star ratings and a review count to each bundle card on the Easter deals page. For each bundle, pull the star rating and review count from the primary product in that bundle (the chair or desk being featured). Display these directly below the bundle name, above the savings amount, using the same red star styling visible elsewhere on the site. On mobile, the star rating and review count appear as a single line (e.g., "★★★★★ 61 reviews") between the bundle name and the deal description link. On desktop, same placement - the card layout does not change, only the trust signal row is added. No other elements move. The "Configure Now" CTA, savings text, product thumbnails, and deal images remain identical to control.

---

## Slot 2: Checkout CTA in the Cart Drawer

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (site-wide, all pages)
**Revenue potential:** Traffic data unavailable. Every buyer on the site passes through the cart drawer. At TTRacing's price points (A$219 to A$719+ for individual items, higher for bundles), cart abandonment is expected to be high - the CRO ebook cites 70% average add-to-cart abandonment across ecommerce, with abandonment increasing for higher-priced products. A direct checkout CTA in the drawer removes one full page load from the purchase path. A/B test data from comparable Shopify stores shows adding a sticky "Proceed to Checkout" CTA in the cart drawer improved conversions by 6.8%. One test with express checkout in the cart delivered a 35.8% CR increase.

**Hypothesis:** If we add a direct "Checkout" button to the cart drawer and show an estimated delivery timeframe, cart-to-purchase conversion will improve because visitors currently must click "View Cart," load the full cart page, then click checkout - and they have no visibility into when their order will arrive until after they submit payment.

**Data:** The current cart drawer shows only a "VIEW CART" button with no direct path to checkout (Source: Cart Drawer Screenshot). Shipping cost is deferred: "Shipping fee to be calculated at checkout" - customers do not know what they will pay for shipping until they are already in checkout (Source: Cart Drawer Screenshot). One TTRacing reviewer gave 3 stars on a product they loved because of unexpected delivery delay with no upfront communication: "Timelines should be explained in advance" (Source: Reviews & UGC). Adding delivery transparency earlier in the funnel addresses this directly. The CRO ebook identifies the cart as one of the least optimized areas on most ecommerce sites and recommends removing risk signals (guarantees, safety badges) and surfacing free shipping offers or other incentives to reduce abandonment.

**V1:** Add two changes to the cart drawer. First, add a red "Checkout" button directly below the existing "VIEW CART" button. The "Checkout" button should be styled identically to the "VIEW CART" button (same red fill, same rounded corners, same font weight) and link directly to the Shopify checkout URL. On mobile, both buttons stack vertically: "VIEW CART" on top, "Checkout" below, with 8px gap between them. On desktop, the same stacking layout applies in the cart drawer. Second, in the empty whitespace between the cart line item and the "You may also like" upsell section, add one line of text: "Estimated delivery: 5-7 business days" (or the actual delivery estimate TTRacing uses for AU orders - confirm with client). Style this as small grey text, centered, no icon. This fills the dead space with useful information instead of leaving it blank. No other elements in the cart drawer change.

---

## Slot 3: Size Guide on Gaming Chair PDPs

**Type:** A/B test (1 variation vs. control)
**Page:** Gaming chair PDPs. Priority pages: Surge X (https://ttracing.com.au/products/ttracing-surge-x-gaming-chair), Duo V4 series, Swift X 2020. The Surge X is recommended as the primary test page given its review volume (61 reviews visible on desktop) and position as a top paid ad destination.
**Revenue potential:** Traffic data unavailable. The Surge X PDP is a direct paid ad destination (Ad 1 in the Meta analysis). Gaming chairs at A$399-549 are high-consideration purchases where uncertainty about fit is a known conversion barrier. If size hesitation accounts for even 5-10% of sessions that don't convert, a fit guide that resolves that hesitation has meaningful revenue potential. Exact figure requires session volume from the brand.

**Hypothesis:** If we add a height and weight size guide to the gaming chair PDP, conversion will increase among undecided visitors because the most common post-purchase complaint is that the chair was the wrong size for them - meaning the product itself is fine, but the purchase decision was made without enough information.

**Data:** Multiple Australian reviewers discovered the wrong fit after purchase: "Not suitable for anyone above 170cm," "Back is very short - headrest comes to the bottom of my neck," "I'm 5'7 and the chair is too small for me. I'd have to be sitting hunched to rest my head" (Source: Reviews & UGC). These are post-purchase complaints about a pre-purchase information gap. Secretlab - ranked #1 for gaming chairs in Australia by every roundup reviewed - publishes a three-size system with clear height and weight ranges: S for under 169cm, R for 170-189cm, XL for 181-205cm. TTRacing has no visible equivalent on any gaming chair PDP reviewed (Source: Site Screenshots, Competitor Research). Herman Miller uses a chair selector quiz to match customers before purchase. The absence of this guidance is both a conversion gap (hesitant buyers who don't purchase) and a satisfaction gap (buyers who purchase and regret it). TTRacing's chair lineup spans multiple size ranges (Duo V4 is flagged as small by reviewers; Surge X is described as large) - this information exists but is not surfaced pre-purchase.

**V1:** Add a static size guide table directly below the upholstery selector on the Surge X PDP (and equivalent position on other chair PDPs in the test). The table has three columns: "Your Height," "Your Weight," and "Recommended Chair." Populate it with TTRacing's actual size recommendations for each chair model (confirm with client). Style the table to match the existing PDP - use the same font, same border style as other elements in the buy box area. Title the section "Find Your Fit" in the same weight/size as the "Upholstery" and "Edition" labels above it. On mobile, the table renders as a simple stacked card layout: each row is its own block (height range / weight range / chair name) with a light grey background. On desktop, the full three-column table renders inline within the buy box column. No other elements on the page move. The existing "Comparison Guide - Explore The Differences" link below the upholstery selector remains in place.

---

## Future Slot Candidates

These ideas have strong data support but did not fit the three prioritized slots. Queue for discussion once current tests complete.

**TACTO landing page buy box above the fold:** The TACTO campaign page (paid traffic destination for Ad 2) shows no price and no add-to-cart in the first three folds. The first visible action a paid visitor can take without scrolling is a small "Shop Now" button in the top-right corner. Adding a buy box (price, ATC button, Afterpay line) to the first fold is a high-confidence change for a paid traffic landing page. Test: add a buy box panel overlaid on or immediately below the hero image on fold 1.

**Bundle landing page featured deal hero:** The current Easter deals page presents 7 bundles in a flat grid with no hierarchy. Test: replace the current text hero ("Hop into the Easter Sale") with a full-width featured bundle card - the single highest-value or best-selling deal - with a direct "Configure Now" CTA. The remaining 6 bundles appear below as secondary options. This reduces decision fatigue and gives visitors a clear recommended action.

**Cart drawer shipping threshold bar:** Add a progress bar to the cart drawer showing how close the customer is to free shipping (if TTRacing offers this threshold). Example: "Add A$51 more for free shipping." Research shows shipping threshold bars increase AOV and reduce cart abandonment simultaneously.
