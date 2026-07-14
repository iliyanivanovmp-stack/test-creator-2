# Flo Mattress CRO Research Brief

**Data Sources:** manifest; Meta and Google ads; 89 Amazon reviews dated June 22, 2024-July 5, 2026; July 14, 2026 mobile Lighthouse; site screenshots; live homepage; official Wakefit, SleepyCat, and The Sleep Company pages

## Insights

All three Meta ads collected July 14, 2026 and all brand traffic land on one generic homepage. The hero leads with discount, refund, and ₹9-per-night framing, but it drops the celebrity, 95% five-star, doctor, orthopedic, cooling, latex, and vacuum-packed proof that earned the click. Source: Meta and Google ads, manifest, site screenshots, live homepage.

Choice confidence is the next constraint. Visitors must translate five mattress options without a concise comparison, while collected reviews report outcomes ranging from “excellent back support” to “made my back pain worse.” Source: 89 Amazon reviews dated June 22, 2024-July 5, 2026, site screenshots.

The buying path is also slow and dense. July 14, 2026 mobile Lighthouse scored the homepage 48 and the Ergo PDP 49, with 6.5 s and 7.4 s LCP. On the PDP, the Add to Cart button first appears in Fold 2 after price, delivery, EMI, color, size, units, dimensions, thickness, and quantity controls. Source: July 14, 2026 mobile Lighthouse, site screenshots.

The strongest sequence is to preserve paid-message intent, make the five-product choice easier, then shorten the PDP and cart path. Monthly revenue impact cannot be calculated: unknown sessions/mo x unknown baseline CR x unknown AOV.

## Slot 1: Campaign-Matched Homepage Hero

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (https://www.flomattress.com/)
**Revenue potential:** Unknown sessions/mo x +4% relative CR x unknown AOV = unquantified monthly revenue.

**Hypothesis:** If we match the homepage hero to each paid campaign's documented promise and proof, conversion rate will increase because visitors will immediately recognize the message that earned their click.

**Data:** All three Meta ads collected July 14, 2026 use one homepage URL, while 18 Google ad cards collected July 14, 2026 add orthopedic and doctor angles. The captured hero omits the ads' celebrity, 95% five-star, doctor, latex, cooling, and vacuum-packed proof. Source: Meta and Google ads, manifest, site screenshots.

**V1:** Keep the current hero layout, discount, refund message, ₹9-per-night line, and orange CTA. Change only the hero headline and one adjacent proof line to match the incoming campaign: celebrity and 95% five-star proof for the celebrity creative, offer and trial proof for the discount creative, spine-support and cooling proof for the orthopedic creative, and orthopedic and doctor framing for matching Google traffic. On mobile, place the matched headline and proof above the CTA without increasing the hero beyond one screen. On desktop, place them in the existing text block beside the bedroom image.

## Slot 2: Five-Mattress Decision Cards

**Type:** A/B test (1 variation vs. control)
**Page:** Collection page (URL not captured)
**Revenue potential:** Unknown sessions/mo x +3% relative CR x unknown AOV = unquantified monthly revenue.

**Hypothesis:** If we add consistent decision criteria to all five mattress cards, collection-to-PDP progression will increase because visitors can compare suitability without opening every product.

**Data:** The collection screenshots captured July 14, 2026 present five products across two folds with imagery, one-line copy, starting price, discount, and CTA, but no firmness, material, sleeper fit, cooling, rating, or comparison. Review outcomes conflict on firmness and back-pain relief. Source: site screenshots, 89 Amazon reviews dated June 22, 2024-July 5, 2026.

**V1:** Keep the existing two-column card grid, imagery, price, discount, and Shop Now CTA. Add a compact row to every card for firmness, material, sleeper fit, and cooling, using only the product positioning already documented on the site. On mobile, stack the four labels beneath the one-line description and above price. On desktop, align the labels in the same order and position on all five cards so shoppers can scan across the grid.

## Slot 3: Faster Mobile Critical Path

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage and Ergo PDP (https://www.flomattress.com/; PDP URL not captured)
**Revenue potential:** Unknown sessions/mo x +3% relative CR x unknown AOV = unquantified monthly revenue.

**Hypothesis:** If we reduce non-critical image and script weight on the homepage and Ergo PDP, conversion rate will increase because mobile visitors can see and use the buying experience sooner.

**Data:** July 14, 2026 mobile Lighthouse scored the homepage 48 and the Ergo PDP 49, with LCP of 6.5 s and 7.4 s and payloads of 4,591 KiB and 5,798 KiB. The homepage exposed 399 KiB of image-delivery savings, two wasteful animated GIFs, and duplicated marketing scripts, while the PDP exposed 930 KiB of unused JavaScript. Source: July 14, 2026 mobile Lighthouse.

**V1:** Keep the visible page content and layout unchanged. Replace the homepage animated GIFs with optimized static or click-to-play assets and defer documented non-critical or duplicated marketing scripts until after the primary content becomes interactive. Apply the same script deferral to the Ergo PDP. On mobile, prioritize the hero and buy-box assets before below-fold media. On desktop, preserve the same visual treatment while loading below-fold media and non-critical scripts after the critical path.

## Slot 4: Persistent PDP Purchase Bar

**Type:** A/B test (1 variation vs. control)
**Page:** Ergo PDP (URL not captured)
**Revenue potential:** Unknown sessions/mo x +2% relative CR x unknown AOV = unquantified monthly revenue.

**Hypothesis:** If we keep the selected configuration, price, and Add to Cart action available while shoppers review the PDP, add-to-cart rate will increase because the purchase action no longer depends on returning to Fold 2.

**Data:** In the July 14, 2026 site screenshots, the desktop buy box places price, timer, delivery, EMI, help, color, size, units, dimensions, thickness, and quantity before Add to Cart, which first appears in Fold 2. The captured configuration is ₹6,392.85, and no mobile sticky state was collected. Source: site screenshots.

**V1:** Keep the existing buy box and configuration controls. Add a persistent bar only after the original Add to Cart button leaves the viewport, showing the selected mattress configuration, current price, and Add to Cart action. On mobile, use a bottom bar with a one-line configuration summary and full-width CTA. On desktop, use a compact bottom bar aligned to the content width. Hide the bar whenever the original CTA is visible.

## Slot 5: PDP Suitability Guide

**Type:** A/B test (1 variation vs. control)
**Page:** Ergo PDP (URL not captured)
**Revenue potential:** Unknown sessions/mo x +2% relative CR x unknown AOV = unquantified monthly revenue.

**Hypothesis:** If we place a compact firmness and sleeper-suitability guide beside the Ergo and Ortho choice, add-to-cart rate will increase because shoppers can calibrate support expectations before selecting a mattress.

**Data:** In the July 14, 2026 site screenshots, Ergo is preselected beside an Ortho switch and 21,984 reviews, but no visual maps sleep position, body needs, firmness, and expected outcome. Collected reviews dated June 22, 2024-July 5, 2026 range from “significant relief from the back pain issue” to “made my back pain worse.” Source: site screenshots, 89 Amazon reviews dated June 22, 2024-July 5, 2026.

**V1:** Keep the existing Ergo and harder Ortho switch. Add one compact guide directly beneath it that maps each choice to documented firmness and sleeper suitability without promising pain relief. On mobile, show the guide as two stacked, tap-friendly rows before the review count. On desktop, show two aligned columns beneath the switch so the visitor can compare Ergo and Ortho without leaving the buy box.

## Slot 6: Progressive Size Configuration

**Type:** A/B test (1 variation vs. control)
**Page:** Ergo PDP (URL not captured)
**Revenue potential:** Unknown sessions/mo x +2% relative CR x unknown AOV = unquantified monthly revenue.

**Hypothesis:** If we reveal size controls in a clear sequence, add-to-cart rate will increase because shoppers face fewer simultaneous configuration decisions.

**Data:** In the July 14, 2026 site screenshots, color, standard or custom mode, units, dimensions, thickness, quantity, and measurement help form one long sequence before purchase. One Amazon review from the June 22, 2024-July 5, 2026 sample reported a size issue, and the site supports custom sizing. Source: site screenshots, 89 Amazon reviews dated June 22, 2024-July 5, 2026.

**V1:** Keep every current option and default selection, but group the controls into two steps: choose standard or custom size first, then reveal only the relevant units, dimensions, thickness, and measurement help. Leave color and quantity in their current order. On mobile, use stacked sections with the second section hidden until the first choice is made. On desktop, use the same progressive sequence within the existing right-hand buy box.

## Slot 7: One-Click Compatible Protector

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (sitewide)
**Revenue potential:** Unknown checkouts/mo x +4% relative checkout AOV x unknown AOV = unquantified monthly revenue.

**Hypothesis:** If we pre-match the recommended protector to the mattress configuration and make it a one-click add-on, checkout AOV will increase because shoppers no longer need to resolve compatibility before purchase.

**Data:** The cart drawer already knows the mattress dimensions, thickness, color, and size, but the protector recommendation requires another size choice without visibly confirming compatibility. Source: site screenshots.

**V1:** Keep the current protector recommendation and price. Replace its size selector with the compatible size derived from the mattress already in the cart, show that matched size in the recommendation, and use one Add button. On mobile, keep the matched size and Add action on one compact row. On desktop, show the same compatibility line and action inside the existing cart-drawer recommendation.

## Slot 8: De-Emphasized Promo Code

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (sitewide)
**Revenue potential:** Unknown checkouts/mo x +1% relative checkout CR x unknown AOV = unquantified monthly revenue.

**Hypothesis:** If we collapse the promo-code field behind a secondary link, checkout progression will increase because shoppers can focus on the displayed savings and checkout action instead of searching for another code.

**Data:** The open promo field appears before recommendations and checkout despite displayed savings. No free-shipping threshold is shown, while the drawer already reassures shoppers about delivery, trial, and EMI. Source: site screenshots.

**V1:** Keep promo-code functionality unchanged, but replace the open field with a secondary “Have a promo code?” link below the displayed savings. Reveal the same field only after the link is selected. On mobile, use a single text link below the savings line and above the recommendation. On desktop, place the collapsed link in the same cart-summary region without competing visually with Checkout.

## Future Slot Candidates

1. **Above-the-Fold Mattress Finder** - Replace the generic hero CTA path with a guided choice across the five documented mattress options once a dev/project slot is available.
2. **Add-All Frequently Bought Together Bundle** - Turn the two pillows and protector from three separate PDP decisions into one bundle action to test a +5% relative PDP AOV opportunity.
