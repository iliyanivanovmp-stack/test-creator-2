# BetterWild CRO Research Brief

**Data Sources:** Meta Ads (3 active ads, Jun 9-10, 2026), PageSpeed / Core Web Vitals (mobile), Amazon Reviews (34 reviews, Jun-Jul 2026), Site Screenshots (homepage, collection, PDP, cart drawer)

---

## Insights

BetterWild runs three concurrent Meta ads on Facebook, Instagram, Messenger, and Threads -- a founder "big secret" reveal, an influencer PSA, and a rescue dog story -- all landing on a single URL: betterwild.com/pages/lf. That LP opens with "ALLERGY RELIEF THAT FIXES THE ROOT CAUSE, NOT JUST THE SYMPTOMS." No element on the page references the founder (Cody), the "big secret," the PSA framing, or the rescue dog story. The largest gap is Ad 3 (Founder): the ad promises "BetterWild Founder Exposes Big Secret" with first-person framing, and the LP has no founder, no secret, and no Cody. Source: Meta Ads, Site Screenshots.

The same LP has a 13.7s mobile LCP and 38.3s TTI (PageSpeed score 41/100, mobile). Every Meta ad click competes against a page that is not interactive for 38 seconds on mobile. Total Blocking Time is 690ms, indicating heavy third-party script load (likely Meta Pixel, review widgets, analytics). This is not a test -- it is a prerequisite fix. Every LP test in this roadmap is degraded until LCP is below 2.5s.

Amazon reviews (34 reviews, Jun-Jul 2026) are 29/34 five-star. The dominant purchase driver is "works when nothing else did." Customers describe BetterWild as a last resort after vets and OTC supplements failed: "We have tried many things from the vet and over the counter... Things were not working." (Shannon) "Nothing seemed to even improve his itchy and redness a little until we found Betterwild!" (Hailey womack) "This is the first time she's back to her regular self." (Daniel) Before/after coat and skin recovery -- including documented bald spot regrowth -- is a recurring theme across multiple reviewers. Source: Amazon Reviews.

Negative reviews concentrate on price and, to a lesser degree, taste rejection. "You have got to be kidding me! $45.00 for this tiny sample size!" (JohnsonFamily) BetterWild's subscribe price runs approximately $1.00/chew vs. $0.37/chew for PetHonesty and $0.48/chew for Zesty Paws -- 2-3x the per-chew cost of major competitors. The 30-day money-back guarantee exists on the PDP but disappears in the cart and is absent from the Amazon listing. The price objection is loudest in the cart and on Amazon, the two places where risk reversal is completely absent. Source: Amazon Reviews, Site Screenshots, Competitor Research.

**Immediate flag:** A live fetch of betterwild.com/pages/lf on Jul 24, 2026 returned the LP's ATC widget as "Sold out." If live visitors see a sold-out state, this is a revenue block that must be resolved before any LP tests run. Verify on mobile in incognito immediately.

Revenue opportunity estimate: at approximately 30,000 LP sessions/mo and $59.98 AOV, a 10% CR lift on the LP alone = approximately $18,000/mo in additional revenue, with the message match and price anchor tests offering the highest near-term leverage.

---

## Slot 1: LP Speed Fix

**Type:** Immediate Fix
**Page:** Ads Landing Page (betterwild.com/pages/lf)

**What's broken:** The LP receiving 100% of paid Meta ad traffic has a 13.7s LCP and 38.3s TTI on mobile (PageSpeed score 41/100). FCP is 4.7s. TBT is 690ms. The page is not interactive for over 38 seconds after first request. A visitor who clicked a 15-second Meta ad waits 38 seconds on a partially-loaded page. This blocks meaningful signal from every other LP test in this roadmap. Source: PageSpeed (LP row: LCP 13.7s, TTI 38.3s, Performance 41/100).

**Fix required:**
- Preload and correctly size the fold 1 hero image (two dogs outdoors, full-width section, right-of-center positioning) so the browser identifies it as the LCP element and renders it first
- Defer non-critical third-party scripts (Meta Pixel, analytics, review widgets) to load after the page becomes interactive
- Target LCP < 2.5s and TTI < 5s before running any A/B tests on this page

---

## Slot 2: Message Match -- Founder LP Variant

**Type:** A/B test (1 variation vs. control)
**Page:** Ads Landing Page (betterwild.com/pages/lf)
**Revenue potential:** ~10,000 Ad 3 sessions/mo x 20% CR lift x $59.98 AOV = ~$12,000/mo

**Hypothesis:** If we serve Ad 3 traffic a landing page that continues the founder "big secret" narrative, conversion rate for that segment will increase because visitors receive the reveal they were promised instead of an unrelated category headline.

**Data:** Ad 3 (running since Jun 9-10, 2026) opens with "BetterWild Founder Exposes Big Secret" and first-person framing from Cody. The LP fold 1 headline is "ALLERGY RELIEF THAT FIXES THE ROOT CAUSE, NOT JUST THE SYMPTOMS" -- no founder, no secret, no Cody. This is a complete message break: the ad creates a curiosity gap the LP never closes. Source: Meta Ads, Site Screenshots.

**V1:** Route Ad 3 traffic via UTM parameter or separate URL to a founder-specific LP variant. In fold 1, replace the headline ("ALLERGY RELIEF THAT FIXES THE ROOT CAUSE, NOT JUST THE SYMPTOMS") with a founder-voiced headline that continues the "big secret" hook from the ad. Replace the one-line subhead ("Support your dog's immunity and ease allergies -- naturally. A blend of clinically validated ingredients!") with a sentence that frames Cody's origin story and leads into the product reveal. Replace the hero image (two dogs outdoors, right-of-center) with a founder image or founder-adjacent visual. Keep the star rating bar, "100,000+ Happy Dogs," and pink "SHOP NOW" button unchanged. On mobile: headline, subhead, and CTA stack vertically; founder image appears below the CTA stack or as a background element. On desktop: two-column layout with founder image on the right, matching the current LP column structure.

---

## Slot 3: LP Fold 1 -- Price Anchor + Guarantee

**Type:** A/B test (1 variation vs. control)
**Page:** Ads Landing Page (betterwild.com/pages/lf)
**Revenue potential:** 30,000 LP sessions/mo x 8% CR lift x $59.98 AOV = ~$14,400/mo

**Hypothesis:** If we add price context and a guarantee signal directly below the fold 1 CTA, conversion rate will increase because visitors have the cost and risk information they need to act before entering the funnel.

**Data:** LP fold 1 shows a pink "SHOP NOW" button with no price and no guarantee copy visible. The announcement bar above the nav states "Subscribe today and get free US shipping on every subscription order!" -- a benefit statement, not a risk reversal. Amazon reviewers cite price as friction: "You have got to be kidding me! $45.00 for this tiny sample size!" (JohnsonFamily, Jun-Jul 2026). The 30-day money-back guarantee exists on the PDP but does not appear on the LP in fold 1 or fold 2. Source: Site Screenshots, Amazon Reviews.

**V1:** Add a single line of trust copy directly below the pink "SHOP NOW" button in fold 1: "From $1/day + 30-Day Money-Back Guarantee." No other fold 1 elements change. On mobile: trust line sits flush below the CTA button at full width, centered. On desktop: trust line centered below the CTA, matching the button's visual hierarchy.

---

## Slot 4: PDP Sticky ATC

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page -- Allergy Relief (betterwild.com/products/allergy-relief or equivalent PDP URL)
**Revenue potential:** 20,000 PDP sessions/mo x 6% CR lift x $59.98 AOV = ~$7,200/mo

**Hypothesis:** If we add a sticky ATC bar that persists while the buy box is out of view, add-to-cart rate will increase because the CTA remains accessible throughout the two-step configuration process.

**Data:** The buy box requires two steps before the ATC button is visible: a dog-count selector (Step 1: HOW MANY DOGS ARE YOU TREATING?, three radio options, 1 dog pre-selected) and a pack-size selector (Step 2: SELECT YOUR SUPPLY). The "ADD TO CART - $59.98" button appears at the bottom of fold 2, after approximately 800px of scroll on mobile. No sticky CTA exists on mobile or desktop. Source: Site Screenshots (PDP folds 1-2, CTA behavior notes).

**V1:** Add a sticky ATC bar that becomes visible when the product title scrolls above the viewport. The bar shows the product name and price matching the currently selected option (default: pre-selected pack at $59.98, updating dynamically when the visitor changes their selection in Steps 1 or 2). CTA button text: "ADD TO CART - $59.98" in white text on pink background, matching the existing in-page CTA button style. On mobile: bar is pinned to the bottom of the screen, full-width. On desktop: bar is pinned below the navigation header, full-width.

---

## Slot 5: PDP -- One-Time Purchase Default for New Visitors

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page -- Allergy Relief (betterwild.com/products/allergy-relief or equivalent PDP URL)
**Revenue potential:** 12,000 new visitor PDP sessions/mo x 7% CR lift x $39.99 OTP price = ~$3,360/mo

**Hypothesis:** If we default the buy box to one-time purchase for new visitors, conversion rate for that segment will increase because removing the subscription commitment lowers the barrier for first-time buyers who want to trial before committing.

**Data:** Subscribe & Save is pre-selected as the default purchase path in the buy box. The one-time option appears as secondary text below the pink ATC button: "Or buy once at $79.98 (no discount, $5 Shipping)." Chris P's review states "the change has been clear enough so far that I'll keep ordering on subscription" -- implying he did not start on subscription. The 33% price premium for OTP ($79.98 vs. $59.98 for the 2-pack) compounds hesitation for first-time buyers evaluating a product they have not yet tried. Source: Site Screenshots (PDP buy box detail), Amazon Reviews.

**V1:** For new visitors (no purchase history cookie or equivalent signal), set the buy box default to one-time purchase. The one-time purchase option is shown first and prominently in the buy box. Subscribe & Save is presented below it with a label: "Subscribe after your first order and save on future orders -- includes free US shipping." The pink "ADD TO CART" button reflects the one-time price. On mobile: option order reverses -- one-time shown above, subscribe below. On desktop: same buy box layout with option order reversed for new visitor segment only. Returning visitors (confirmed purchasers) continue to see the subscribe-first layout.

---

## Slot 6: Cart -- Guarantee + Trust Strip

**Type:** A/B test (1 variation vs. control)
**Page:** Cart Drawer (betterwild.com)
**Revenue potential:** 10,000 cart sessions/mo x 5% cart-to-checkout lift x $59.98 AOV = ~$3,000/mo

**Hypothesis:** If we add a guarantee strip above the checkout CTA in the cart drawer, cart-to-checkout rate will increase because the risk reversal visible on the PDP carries through to the moment of decision.

**Data:** The cart drawer shows no trust signals. The 30-day money-back guarantee and free shipping copy that appear on the PDP directly below the ATC button do not carry through to the cart. Kathy C's review: "no returns on this product which the price is expensive!!" Source: Site Screenshots (cart drawer section), Amazon Reviews.

**V1:** Add a one-line trust strip directly above the pink CHECKOUT button in the cart drawer: "30-Day Money-Back Guarantee · Free US Shipping." Display as a centered text line or minimal icon strip using existing brand colors. No other cart elements change. On mobile: strip sits flush above the CHECKOUT button, full-width. On desktop: same position within the cart drawer.

---

## Slot 7: Cart -- Cross-Sell

**Type:** A/B test (1 variation vs. control)
**Page:** Cart Drawer (betterwild.com)
**Revenue potential:** 10,000 cart sessions/mo x 12% cross-sell attach rate x $29.99 incremental item = ~$36,000/mo incremental revenue

**Hypothesis:** If we add a single recommended-product card to the cart drawer, AOV will increase because Allergy Relief customers are not currently exposed to complementary SKUs at the highest-intent moment in the funnel.

**Data:** The cart drawer contains one line item, a cause-marketing shelter selector, a subtotal, and the CHECKOUT button. No upsell or cross-sell is present. BetterWild has three complementary products visible on the collection page -- Joint Support, Dental + Multivitamin, and Paw Balm -- each at $29.99. Source: Site Screenshots (cart drawer, collection page folds 1-3). Industry benchmark: DTC supplement cart cross-sell attach rates average 8-15% (Triple Whale 2024 benchmarks).

**V1:** Add a single cross-sell card in the cart drawer, placed between the line item section and the CHECKOUT button. The card displays one recommended product (Joint Support or Dental + Multivitamin) with: product thumbnail image, product name, one-line descriptor, price ($29.99), and an "Add" button. On mobile: card is full-width, displayed as a compact horizontal row -- thumbnail on the left, name, descriptor, price, and add button on the right. On desktop: same compact horizontal layout constrained to the drawer width.

---

## Slot 8: PDP 3-Pack Copy Error

**Type:** Immediate Fix
**Page:** Product Detail Page -- Allergy Relief (betterwild.com/products/allergy-relief or equivalent PDP URL)

**What's broken:** In the buy box Step 2 (SELECT YOUR SUPPLY), the 3-pack option carries a "Recommended" badge and shows a 90-day supply at $89.98. The explanatory copy directly below it reads: "A 60-day supply for 1 dog -- covers two months of consistent daily support at a better per-day value." This is the 2-pack description. A 90-chew pack at 1 chew per day is a 90-day supply for 1 dog. The copy error directly contradicts the "Recommended" badge on the highest-AOV option ($89.98 vs. $59.98 for the 2-pack). Source: Site Screenshots (PDP fold 2, layout anomalies note).

**Fix required:** Update the explanatory text below the 3-pack option to accurately describe it. Suggested: "A 90-day supply for 1 dog -- three months of consistent daily support at the best per-day value." Confirm the 2-pack copy is correctly assigned to its own option and that the copy is not dynamically generated from a shared metafield.

---

## Future Slot Candidates

1. **Before/After Social Proof Module on LP or PDP** - Multiple reviews include vivid before/after descriptions with specific visual evidence (Shannon's sore healing with photos, Louie Hayes and Hailey womack's bald spot regrowth, Phoebe Freitag's French Bulldogs). This UGC is currently surfaced below the fold. A before/after module in fold 1 or 2 of the LP or PDP is a high-impact trust lever with strong data support.

2. **Homepage Trust Cluster Near Primary CTA** - The 3,500+ review count and media logos (GMA, People, Disney+, National Geographic) do not appear until fold 3 of the homepage. Moving a compact trust strip (review count + 2-3 media logos) adjacent to the fold 1 CTA is a low-effort test with meaningful click-through potential on the approximately 50,000 monthly homepage sessions.

3. **Results Timeline Education on PDP** - Reviewers who saw no results "after days" left 1-star reviews and cited the no-return policy as compounding their frustration. No "Week 1 / Week 2 / Week 4 expectations" content exists on the PDP in collected screenshots. A simple timeline module pre-purchase would reduce early subscription churn and defensive 1-star reviews.

4. **Announcement Bar -- Offer vs. Benefit Test** - Both the homepage and LP announcement bar show "Subscribe today and get free US shipping on every subscription order" -- a passive benefit statement with no urgency. Testing a stronger hook or limited-time offer in this surface is a quick-win test requiring minimal dev.

5. **Wolf-Sourced Probiotics in LP Fold 1** - BetterWild's most distinctive scientific angle (wolf gut microbiome origin) appears only in fold 3 of the LP. No direct competitor uses this positioning. Surfacing it in the LP hero or subhead could differentiate BetterWild from the generic "gut + probiotics" category.

6. **Pricing Inconsistency Audit** - Homepage WebFetch shows "From $39.99" for Allergy Relief; the collection page shows "From: $29.99." Likely OTP vs. subscription price displayed inconsistently across page types. Not a test -- a metafield audit and fix to prevent confused price expectations before the PDP.
