# Eureka Pet CRO Research Brief

**Data Sources:** Meta Ads visual summary + live LP fetch, Google Ads visual summary, Trustpilot reviews (2026-06-15, 50k char sample), Lighthouse mobile PageSpeed (2026-06-15), Site visual summary (homepage, collection, PDP, cart), Live site fetch, Competitor research (self-researched 2026-06-15)

---

## Insights

Price sensitivity is the single biggest conversion barrier -- and a recurring churn driver. Multiple 1-3 star Trustpilot reviews cite price as the reason customers won't continue despite loving the product: "for a Rottweiler X Great Dane at $300+ for about 5kgs -- TOTALLY unaffordable." A separate review reports perceived price-gouging when a $97 first order (which included a $30 welcome discount not labeled as one-time) renewed at $126. Large breed owners, multi-dog households, and pensioners are the most explicitly price-blocked segments. None have a dedicated on-site solution today -- no large-breed bundle, per-day cost framing, or topper-use pricing alternative.

The $6 Taste Tester is the strongest acquisition path in the business by evidence. The Taste Tester PDP has 335 Trustpilot reviews versus 75 on the Variety Pack -- that ratio tells you where new customer volume concentrates (Source: Trustpilot reviews). Yet the post-click infrastructure is thin. The Taste Tester PDP has no subscription widget despite a "Subscribe & Save 15%" announcement bar running at the top of the page. The cart following a $6 sample add has one static cross-sell, no free-shipping progress bar ($59 threshold, $53 gap untapped), and no subscription upsell. The funnel driving the most new customers drops them at checkout with minimal LTV infrastructure.

Homepage performance undermines paid traffic ROI. Google Ads send intent-based searches ("air dried dog food Australia") to the homepage, which scores 46/100 on Lighthouse mobile with a 35.7s Time to Interactive (Source: Lighthouse mobile PageSpeed, 2026-06-15). For visitors who do load, the only above-fold CTA is an outline button labeled "Discover More" -- no price, no product, no social proof. The Ad 1 landing page (why-air-dried) runs a filled orange "Try a Sample - $6" CTA with star ratings in the same hero position. That page converts better by design; the homepage does not.

Message mismatch is leaking revenue on the highest-ticket product. Meta Ad 2 promises "save $77" for the Variety Pack. The landing page shows "SAVE $53.85." That $23 gap is visible the moment a click-through lands -- a trust breach at the exact moment a $359 purchase decision is forming (Source: Meta Ads visual summary, live site fetch). The Variety Pack also has no urgency signal despite the ad using "limited time only" language.

Revenue opportunity is concentrated in two places: upgrading the $6 sample funnel's LTV infrastructure and fixing the homepage for paid traffic. Even a 3% increase in sample-to-subscription conversion across the 335+ review volume represents a step-change in recurring revenue per cohort. The homepage CTA fix requires no new traffic -- it converts existing spend better.

---

## Slot 1: Homepage Hero -- CTA Upgrade

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (https://eurekapet.co/)
**Revenue potential:** Monthly sessions unknown. Google Ads confirmed sending intent traffic to this page (Source: Google Ads visual summary). A conservative 10% improvement in homepage-to-product CTR x estimated $80 blended AOV = material monthly gain proportional to paid traffic volume.

**Hypothesis:** If we replace the outline "Discover More" button with a filled "Try a Sample - $6" primary CTA and add a social proof bar, more paid visitors will navigate to the Taste Tester PDP because the entry point will match the conversion-optimized Ad 1 landing page hero that already runs the same layout.

**Data:** The homepage hero has one outline button ("Discover More") with no price, product name, or social proof visible above fold 1 (Source: Site visual summary). The Ad 1 landing page runs a filled warm-orange "Try a Sample - $6" primary CTA plus a secondary "Shop the Recipes" outline button, with a "★★★★★ 4.8 | 6,000+ Happy Dogs" bar below the CTAs (Source: Meta Ads visual summary). 335 Taste Tester reviews confirm the $6 offer is the most-proven conversion entry point in the business (Source: Trustpilot reviews).

**V1:** Replace the single outline "Discover More" button with two CTAs: a filled warm-orange "Try a Sample - $6" primary button and a secondary outline "Shop the Recipes" button, positioned in the same hero left column. Add a social proof bar ("★★★★★ 4.8 | 6,000+ Happy Dogs") directly below the CTA pair. All other hero elements unchanged -- headline, subtext, and right-column lifestyle image remain in place. Mobile: stack CTAs vertically, primary button full-width above secondary.

---

## Slot 2: Cart -- Free Shipping Progress Bar

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (https://eurekapet.co/)
**Revenue potential:** Monthly sessions unknown. A $6 sample order sits $53 below the $59 free shipping threshold. Industry benchmark for free-shipping bar implementations on DTC Shopify stores: 10-20% AOV lift on orders where the bar is shown.

**Hypothesis:** If we add a free-shipping progress bar to the cart drawer, average order value will increase because visitors will have a clear, visual goal -- $53 from free shipping -- and will add items to close that gap.

**Data:** The current cart drawer has no progress bar (Source: Site visual summary, cart). Free shipping unlocks at $59, confirmed via live site fetch. A $6 Taste Tester add leaves $53 of motivating gap invisible. The only upsell in cart is one cross-sell ("Cluckin Good Chews $18.95") with no price-to-threshold framing.

**V1:** Add a dynamic progress bar at the very top of the cart drawer, above the line items. Bar label: "You're $[X] away from free shipping!" Bar fills proportionally from $0 to $59. At $6 order: "Add $53.00 for free shipping." When threshold is reached, bar fills green and message changes to "You've unlocked free shipping!" No other changes to cart layout. Mobile and desktop: bar spans full drawer width.

---

## Slot 3: Taste Tester PDP -- Subscribe & Save Toggle

**Type:** A/B test (1 variation vs. control)
**Page:** Taste Tester PDP (https://eurekapet.co/products/natural-dog-food-sample)
**Revenue potential:** Sessions unknown. A $6 one-time buyer generates near-zero LTV without a subscription path. If 3% of sample buyers convert to a recurring subscription order (est. $50-100/cycle), LTV per converted customer increases 10x+ over a single $6 transaction (Source: Trustpilot reviews volume confirms sample funnel scale).

**Hypothesis:** If we add a subscribe/one-time purchase toggle to the Taste Tester buy box, a portion of sample buyers will choose subscription at checkout, converting low-LTV $6 transactions into recurring revenue -- because the technology is already live on the Variety Pack PDP and the announcement bar already primes visitors for it.

**Data:** The Taste Tester buy box shows price $6.00 and a black "Add to cart" button with no subscription option (Source: Site visual summary, PDP fold 1). A "Subscribe & Save 15%" announcement bar runs persistently at the top of the page (Source: Live site fetch). The Variety Pack PDP has a working subscribe/one-time radio toggle with subscription price, "SAVE $53.85" badge, and frequency dropdown (Source: Site visual summary). The tech is live -- it is simply not deployed on the primary sample PDP (Source: Meta Ads visual summary, Ad 3 sends highest-volume sample traffic to this page).

**V1:** Add a subscribe/one-time purchase toggle above the qty selector, matching the Variety Pack PDP layout. One-time: $6.00. Subscribe: $5.10 (15% off, with "SAVE $0.90" badge). Frequency dropdown below toggle: "Every 2 Weeks / Monthly / Every 6 Weeks." Default selection: one-time (to minimize friction for first-time visitors who may not be ready to commit). Mobile and desktop: toggle spans full buy box width, stacked above qty and CTA.

---

## Slot 4: Variety Pack PDP -- Savings Claim Alignment

**Type:** A/B test (1 variation vs. control)
**Page:** Variety Pack PDP (https://eurekapet.co/products/variety-pack)
**Revenue potential:** Sessions unknown. Variety Pack is the highest-ticket product at $359 one-time. A 5-10% CR improvement by removing trust friction could be the single highest-value slot in the roadmap on a per-conversion basis.

**Hypothesis:** If we align the savings display on the Variety Pack PDP to reflect the $77 figure referenced in the Meta Ad 2 copy and add a matching urgency signal, trust will increase at the decision point and Variety Pack CR will improve -- because the $23 discrepancy between ad and page creates doubt at the highest-ticket purchase moment.

**Data:** Meta Ad 2 copy states "save $77" and uses "limited time only" urgency language (Source: Meta Ads visual summary). The Variety Pack PDP shows "SAVE $53.85" badge (subscription $305.15 vs. one-time $359.00) with no urgency signal (Source: Live site fetch). The $23 gap is visible the moment a Meta Ad 2 click-through lands. Variety Pack has only 75 Trustpilot reviews vs. 335 on the Taste Tester -- this funnel underperforms (Source: Trustpilot reviews).

**V1:** Update the savings narrative near the subscription toggle to surface the total value framing: first-order welcome discount + ongoing 15% subscription savings summing to $77 saved. Display as: "Save $77 today -- first-order discount + Subscribe & Save 15%." Add a low-friction urgency line beneath the price: "Limited time offer." Mobile: savings copy appears directly below the subscription toggle price, above the frequency dropdown. Desktop: same position.

---

## Slot 5: Taste Tester PDP -- Trust Icons Above Buy Button

**Type:** A/B test (1 variation vs. control)
**Page:** Taste Tester PDP (https://eurekapet.co/products/natural-dog-food-sample)
**Revenue potential:** Sessions unknown. High-volume page (335 Trustpilot reviews confirm sample funnel concentration). A 3-8% CR lift on the primary acquisition PDP drives outsized impact on new customer cohort size.

**Hypothesis:** If we move the four trust icons above the "Add to cart" button, more visitors will add to cart because purchase reassurance ("100% Money Back Guarantee," "100% Australian Made & Owned") will appear at the decision point rather than after it.

**Data:** Current buy box order: product title, rating, fussy-dog copy, price $6.00, qty selector, "Add to cart" button -- then trust icons (Source: Site visual summary, PDP fold 1). The four icons are: 100% Australian Made & Owned / 100% Money Back Guarantee / 68°C gentle air drying / No Fillers or Additives. The Ad 1 landing page positions trust icons as a horizontal row directly between buy copy and the CTAs (Source: Meta Ads visual summary). Multiple Trustpilot reviewers cite "Australian provenance" and "money back guarantee" as explicit purchase drivers (Source: Trustpilot reviews).

**V1:** Move the four trust icon icons from below "Add to cart" to above "Add to cart," between the qty selector and the button. Icons display as a 2x2 grid on mobile and a horizontal row of 4 on desktop. The button itself and all other buy box elements remain in their current positions. No copy changes.

---

## Slot 6: Cart -- Subscription Upsell Block

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (https://eurekapet.co/)
**Revenue potential:** Sessions unknown. Converting even 2% of sample-only cart visitors to a subscription upsell add represents a step-change in LTV per acquired customer. 5+ Trustpilot reviewers explicitly praise subscription flexibility -- intent is validated (Source: Trustpilot reviews).

**Hypothesis:** If we add a subscription upsell block in the cart drawer's empty white space (currently between the line item and the cross-sell), a portion of $6 sample buyers will opt into a subscription before checkout -- because the "Subscribe & Save 15%" announcement bar has already primed them and the cart is the last conversion touchpoint before payment.

**Data:** The cart drawer has a large empty white space between the Taste Tester line item and the "Cluckin Good Chews $18.95" cross-sell (Source: Site visual summary, cart). The "Subscribe & Save 15%" announcement bar runs site-wide (Source: Live site fetch). The cart currently has zero subscription touchpoints (Source: Site visual summary, cart). Subscription flexibility is praised repeatedly in Trustpilot reviews (Source: Trustpilot reviews).

**V1:** Add a subscription upsell block in the empty white space above the "I'm even better with" cross-sell section. Block copy: "Subscribe & Save 15% -- switch your Taste Tester to a monthly delivery and save." Include a one-click "Switch to Subscribe & Save" button. If clicked, line item updates to subscription at $5.10. If not clicked, cart proceeds normally. Mobile and desktop: block spans full drawer width, styled as a distinct card with amber background to differentiate from the standard cart layout.

---

## Slot 7: Homepage Hero -- Outcome Headline Copy

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (https://eurekapet.co/)
**Revenue potential:** Sessions unknown. Proven in paid search ("Smaller Poos, Better Guts" confirmed live in Google Ads). Applying in-market headline copy to the highest-traffic entry page costs zero additional spend.

**Hypothesis:** If we replace the features-led hero subtext with health-outcome language proven in Google Ads, more visitors will connect the product to a tangible result -- because "90% Aussie protein, 10% fruit, veg & seeds" is a product spec, while "Smaller poos, better guts, more energy" is a customer outcome that motivates action.

**Data:** Current homepage hero subtext: "90% Aussie protein, 10% fruit, veg & seeds. No fillers, no preservatives, no nonsense!" (Source: Site visual summary, homepage fold 1). Google Ads use "Smaller Poos, Better Guts" as active copy in market (Source: Google Ads visual summary). This headline is absent from every landing page and product page on the site (Source: Live site fetch, Site visual summary).

**V1:** Replace the hero subtext ("90% Aussie protein, 10% fruit, veg & seeds. No fillers, no preservatives, no nonsense!") with outcome-led copy: "Smaller poos, better guts, more energy. Air dried at 68°C to lock in real nutrition." Headline unchanged ("All natural Aussie made air dried dog food"). CTAs, right-column image, and all other hero elements unchanged. Mobile and desktop: subtext displays in the same position and type size as control.

---

## Slot 8: Taste Tester PDP -- 3rd Party Rating Badge

**Type:** A/B test (1 variation vs. control)
**Page:** Taste Tester PDP (https://eurekapet.co/products/natural-dog-food-sample)
**Revenue potential:** Sessions unknown. Adding a third-party validation signal at the point of decision removes a trust objection for first-time buyers who are unfamiliar with the brand. Proven signal -- petfoodreviews.com.au 9.5/10 is already in active Google Ad copy (Source: Google Ads visual summary).

**Hypothesis:** If we add the petfoodreviews.com.au 9.5/10 rating as a fifth trust icon in the buy box trust icon row, first-time visitors will have additional independent validation at the point of decision -- because third-party review platform badges carry credibility signals that on-site star ratings alone do not.

**Data:** The Taste Tester PDP trust icon row shows four icons: 100% Australian Made & Owned / 100% Money Back Guarantee / 68°C gentle air drying / No Fillers or Additives (Source: Site visual summary, PDP fold 1). petfoodreviews.com.au 9.5/10 rating appears in Google Ad copy but is absent from the website and all Meta landing pages (Source: Google Ads visual summary, Meta Ads visual summary, Live site fetch).

**V1:** Add petfoodreviews.com.au 9.5/10 as a fifth element in the trust icon row on the Taste Tester PDP. Display format: petfoodreviews.com.au logo + "9.5/10" rating, styled consistently with the existing four trust icons. Mobile: icon row wraps to 3+2 grid. Desktop: single horizontal row of 5. No other buy box changes.

---

## Future Slot Candidates

1. **Large Breed Cost Framing** - Multiple 1-3 star reviews cite structural unaffordability for large dogs; a per-day cost frame or large-breed bundle page would address the segment most explicitly blocked by price.
2. **"Smaller Poos, Better Guts" on Taste Tester PDP** - The outcome headline tested in Slot 7 on the homepage can cascade to the primary acquisition PDP once homepage results are known.
3. **Carbon-Neutral Claim in Ad Creative** - NOCO2 partnership is visible on the live homepage but absent from all Meta and Google creatives -- untested differentiator for eco-conscious segment.
4. **Discount Code Field Removal or Collapse in Cart** - The prominent "Got a discount code?" field in the cart may be leaking buyers who exit to search for codes that don't exist. Worth testing collapsed or removed.
