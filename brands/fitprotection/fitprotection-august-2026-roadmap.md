# FIT Protection CRO Research Brief

**Data Sources:** Meta ads visual summary, Google ads visual summary, PageSpeed Lighthouse exports (July 2026), Judge.me reviews (537 published, 4.17/5 average), site visual summary (homepage, collection, PDP, cart), live site fetch (July 27, 2026)

---

## Insights

All three active Meta ads land on the same homepage, but the homepage hero does not reflect any of the three ad frames. Ad 1 and Ad 2 lead with RV glass protection ("Your machine deserves better than a tarp," "Exact Fit For Your RV"). Ad 3 frames the problem as rock chip damage ("NEVER LET A $2 ROCK RUIN YOUR TRIP," Jeep visual). The homepage hero reads "NEVER LOSE ANOTHER COVER" -- a cover retention frame -- with a UTV image and a configurator defaulting to UTV. Every paid visitor hits this mismatch on arrival. Source: Meta ads visual summary, site visual summary.

The configurator compounds the problem for RV buyers. Two of three active ads carry RV destination labels, but the configurator's first dropdown pre-selects "UTV." An RV buyer must manually correct the vehicle type before they can find their product -- one extra required step before purchase intent can convert. The configurator is the only primary CTA on the homepage. Source: Meta ads visual summary, site visual summary.

Trust is delayed. Fold 1 below the hero shows four LOXX industrial credential tiles (100-year fastening heritage, military-aerospace-marine trust, 300+ lb per fastener, exclusive North American LOXX partner). The 537+ verified reviews with a 4.17/5 Judge.me badge appear at fold 2 -- a full scroll below the primary conversion area. For a first-time visitor with no LOXX brand context, customer proof outperforms industrial heritage credentials. Source: Site visual summary, reviews (July 2026).

Customer support perception is the most visible conversion suppressor in the review dataset. Three of the lowest-rated reviews cite the identical gap: no phone number, no named contact, unanswered emails. Bob (1-star, Forest River Nobo): "There is no physical address or phone number. There isn't even a name of a contact person." Rhonda Ishmael (1-star, Forest River Impression): "I have not received a response from the email." With 537 public reviews at 4.17/5 and three 1-star reviews anchored to this single issue, the support problem is visible at scale in Google Shopping and review feeds. Source: Judge.me reviews (July 2026), live site fetch.

PDP performance is critically slow. Lighthouse exports from July 2026 show a 51/100 performance score, 8.7s LCP, and 23.9s TTI on the product page hosting the ATC button. The homepage is also slow (68/100, 4.4s LCP) but the PDP is worse by every metric. Every Google Shopping click, organic product URL visit, and product-level retargeting impression lands on a page that is non-interactive for nearly 24 seconds on mobile. Per Google benchmarks, each 1-second LCP improvement delivers 2-4% CR lift. At 3.5x the "good" LCP threshold, this is a conversion floor issue before any UX optimization matters.

One AOV lever sits unused. Three accessories are confirmed live on the site -- vinyl cleaner ($25), removable magnets ($39), extended warranty ($39) -- but none appear in the cart drawer or on the PDP beyond the All-LOXX upgrade. The free shipping bar shows "UNLOCKED" at full green from the first item added at $364, providing zero incremental incentive for add-ons. Source: Site visual summary (cart section), live site fetch (July 2026).

---

## Slot 1: Homepage Hero Headline -- Rock Chip vs. Cover Loss Frame

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (fitprotection.com)
**Revenue potential:** Monthly sessions unknown (analytics access needed). Conservative est.: 5% relative CR lift on paid traffic. Revenue impact available once session data is confirmed.

**Hypothesis:** If we replace the "NEVER LOSE ANOTHER COVER" hero headline with a rock chip prevention frame, paid visitors from Ad 3 will convert at a higher rate because the headline reflects the buyer fear the ad activated.

**Data:** Ad 3 is active across Facebook, Instagram, Messenger, WhatsApp, and Threads as of July 24, 2026, using the headline "NEVER LET A $2 ROCK RUIN YOUR TRIP" with a Jeep visual. The homepage hero shows "NEVER LOSE ANOTHER COVER" -- a different problem frame -- with a UTV image. Every visitor arriving from Ad 3 lands on a headline addressing a different problem than the one they clicked on. Source: Meta ads visual summary, site visual summary.

**V1:** Replace the hero headline "NEVER LOSE ANOTHER COVER" with "ONE ROCK. ONE COVER. ZERO CRACKED WINDSHIELDS." Subtext unchanged: "Exact Fit To Your Glass. No Drilling, No Straps. Off in 15 seconds." Product image and layout stay as control. On mobile, headline stacks above subtext in the same left-aligned white-on-dark layout. On desktop, headline sits left-aligned alongside the product image in the same fold-1 position as control.

---

## Slot 2: RV Configurator Default -- Category Match for RV Ad Traffic

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (fitprotection.com)
**Revenue potential:** Monthly sessions unknown. Conservative est.: 8% configurator start rate lift on RV ad traffic. Revenue impact available once session data is confirmed.

**Hypothesis:** If the configurator's first dropdown defaults to "RV" instead of "UTV," RV buyers arriving from Ads 1 and 2 will start the configurator at a higher rate because they no longer need to manually correct the vehicle type before searching.

**Data:** 2 of 3 active Meta ads (July 24, 2026) carry RV destination labels: Ad 1 ("RV Glass Protection") and Ad 2 ("Exact Fit For Your RV"). All three ads route to the homepage configurator. The configurator's first dropdown pre-selects "UTV." An RV buyer must switch this field before they can search -- a required friction step before intent can convert. Source: Meta ads visual summary, site visual summary.

**V1:** Set the first dropdown in the "Find My Cover in 3 Taps" configurator to default to "RV" instead of "UTV." All other elements unchanged: Brand and Model dropdowns remain empty until selection, and the teal "FIND MY COVER" button stays in its current position. On mobile, the stacked three-dropdown layout stays vertical. On desktop, the horizontal configurator bar remains in its position below the nav. No visual changes to the configurator.

---

## Slot 3: Trust Signal Elevation -- Reviews to Fold 1

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (fitprotection.com)
**Revenue potential:** Monthly sessions unknown. Conservative est.: 3% CR lift on cold paid traffic. Revenue impact available once session data is confirmed.

**Hypothesis:** If we surface the star rating and review count in fold 1 alongside the LOXX credential tiles, first-time visitors will convert at a higher rate because customer validation appears before they scroll.

**Data:** Fold 1 of the homepage shows four LOXX credential stat tiles below the hero: fastening heritage (approx. 100 years), military-aerospace-marine trust, 300+ lb per fastener hold, and exclusive North American LOXX partner status. The 537+ verified reviews block with Judge.me badge appears at fold 2 only. For a visitor with no prior LOXX context, these industrial credentials carry less weight than customer proof. Source: Site visual summary (fold 1 and fold 2 trust placement), reviews (537 reviews, 4.17/5, July 2026).

**V1:** Add a "537+ verified reviews | 4.17/5" strip directly beneath the hero headline in fold 1 -- positioned above the LOXX stat tile row. The strip uses a star icon and Judge.me badge. The four LOXX stat tiles remain unchanged. The fold 2 review block stays in its current position. On mobile, the strip appears as a single centered line beneath the headline and subtext. On desktop, it appears left-aligned in the same column as the headline.

---

## Slot 4: PDP Page Speed Remediation

**Type:** Immediate Fix
**Page:** Product Detail Page (fitprotection.com/products/...)

**What's broken:** The PDP scores 51/100 on Lighthouse (July 2026) with an 8.7s LCP and 23.9s TTI. Total Blocking Time is 580ms. The buy box -- including the sticky "ADD PROTECTION $364" ATC bar and the four-step configuration flow -- is functionally non-interactive for nearly 24 seconds after navigation on mobile. The LCP is 3.5x above Google's 2.5s "good" threshold. Every Google Shopping click, organic product URL visit, and product-level retargeting impression lands on this experience. Source: PageSpeed Lighthouse exports (July 2026).

**Fix:** Audit and defer render-blocking scripts contributing to the 580ms TBT. Identify the LCP element (most likely the main product image) and apply preload configuration and size optimization. Target: PDP LCP under 4s as a first milestone. Per Google benchmarks, each 1-second reduction delivers 2-4% CR lift. No A/B test required -- this is a technical floor issue affecting every product-page visitor.

---

## Slot 5: Support Contact Visibility

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (fitprotection.com/products/...)
**Revenue potential:** Monthly sessions unknown. Conservative est.: 2-5% CR lift on mid-funnel traffic. Revenue impact available once session data is confirmed.

**Hypothesis:** If we add a visible contact option to the PDP trust row, hesitant buyers will convert at a higher rate because they can see a route to a human before committing $364+.

**Data:** The live site shows support limited to info@fitprotection.com with Mon-Fri 8a-5p MST hours. No phone number, chat widget, or named contact is visible in the header, PDP trust row, or footer. The PDP trust row currently reads: "Free ship lower 48 | 1-Year warranty | Rebuild free if it fails." Three separate 1-star reviews cite this identical gap as their only reason for the rating. Bob (1-star, Forest River Nobo): "There is no physical address or phone number. There isn't even a name of a contact person." Rhonda Ishmael (1-star, Forest River Impression): "I have not received a response from the email." Source: Judge.me reviews (July 2026), live site fetch.

**V1:** Add a fourth element to the PDP trust row: a phone number or named contact point (e.g., "Questions? Call or text [number] | Mon-Fri 8a-5p MST"). If a phone number is not available for the variation, use: "Talk to the team -- [email] | Mon-Fri 8a-5p MST." On mobile, the trust row wraps to a second line to accommodate the additional element. On desktop, the fourth element extends the trust row horizontally in the same pill-and-icon style as the existing three items.

---

## Slot 6: Tariff Disclosure -- International Buyer Notice

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (fitprotection.com/products/...)
**Revenue potential:** Monthly sessions unknown. Eliminates known tariff-related post-purchase shock and reduces duty-triggered 1-star reviews from international buyers.

**Hypothesis:** If we add a one-line tariff notice on the PDP near the shipping trust signal, overall conversion holds while international buyers make an informed purchase decision -- reducing post-purchase disputes and public 1-star reviews.

**Data:** Taryn Lowe (1-star, Coachmen Freedom Express) paid $183.86 in import tariffs on a $465 order with no advance notice -- noting she could have replaced three windshields for the same price. No tariff or import duty disclosure appears on any product page, cart, or checkout in the live site fetch. The effective tariff rate in this review was 40% of product price. Source: Judge.me reviews (July 2026), live site fetch.

**V1:** Add a single-line notice beneath the shipping trust signal in the PDP buy box: "International orders (outside the USA) may be subject to import duties and taxes charged at delivery." Text appears in a smaller supporting font, consistent with existing buy box body copy. On mobile, displayed inline below "Free ship -- lower 48." On desktop, shown as a footnote beneath the trust row within the buy box.

---

## Slot 7: Cart Accessories Cross-Sell

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (fitprotection.com)
**Revenue potential:** Monthly sessions unknown. At $380 AOV, a 10% accessory attach rate adds $3.90 per order. Total monthly lift available once order volume is confirmed.

**Hypothesis:** If we add a single accessory cross-sell tile below the All-LOXX upgrade block in the cart drawer, a portion of buyers will add a $25-$39 accessory because purchase intent is already confirmed and the cart is open.

**Data:** The cart drawer shows one upsell: the All-LOXX retention upgrade ($409 swap from $364 base). The free shipping progress bar shows "UNLOCKED" at full green from the first item -- always cleared at the $364 base price -- providing zero incremental AOV incentive. Three accessories are confirmed live on the site: vinyl cleaner ($25), removable magnets ($39), extended warranty ($39). None appear in the cart drawer or on the PDP. Source: Site visual summary (cart section), live site fetch (July 2026).

**V1:** Add a single accessory tile directly below the All-LOXX upgrade block in the cart drawer. Feature the extended warranty ($39) as the lead item, with a one-line description: "Add 2-Year Warranty -- $39. Covers fit, hold, and materials." Include a teal single-tap "ADD TO ORDER" button. On mobile (primary cart interaction surface), the tile spans the full cart drawer width. On desktop, the tile matches the All-LOXX block width directly above it.

---

## Slot 8: Homepage Desktop Sticky CTA

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (fitprotection.com)
**Revenue potential:** Monthly sessions unknown. Conservative est.: 2-5% CR lift on desktop homepage traffic. Revenue impact available once desktop traffic share and session data are confirmed.

**Hypothesis:** If we add a sticky "Find My Cover" button to the nav on desktop scroll, users who scroll past the configurator will start the configurator at a higher rate because the primary CTA is accessible at any scroll depth.

**Data:** Desktop screenshots confirm no sticky element is present across any homepage fold. The "Find My Cover in 3 Taps" configurator sits between the nav and the hero and is not visible once the user scrolls into the LOXX education block, product grid, or feature explainer. No floating button, sticky bar, or secondary CTA appears at any scroll depth on desktop. The configurator is the only primary CTA mechanism on the homepage. Source: Site visual summary (CTA behavior notes, all homepage folds).

**V1:** Add a "Find My Cover" button to the right side of the desktop nav bar that becomes visible after the user scrolls past the configurator row. Button style: teal background, white text, matching the existing "FIND MY COVER" CTA in the configurator. On click, smooth-scroll back to the top of the configurator. Mobile behavior: no change -- sticky nav behavior on mobile remains as control. Desktop only.

---

## Future Slot Candidates

1. **Collection Page Price Filter Fix** -- All 22 products appear under "Under $400," including All-LOXX variants at $409. The "$400-$450" bracket returns 0 results. Fix the price filter logic or metafield configuration. Immediate Fix -- near-zero effort, no test needed.

2. **Google Shopping Feed Price Rendering** -- The Google Ads screenshot shows "[Price]" as a literal placeholder in a Shopping listing for a Yamaha Wolverine UTV cover. Affected SKUs may be excluded from Shopping auctions or running without a price. Audit the Merchant Center product feed for price field errors. Immediate Fix.

3. **RV Total-Hold Claim in Hero Subtext** -- Ad 2 leads with "3,000+ LB TOTAL RV HOLD." The homepage stat tiles show "300+ lb per fastener" and "850 lb mag" -- neither surfaces the total-hold figure RV ad traffic just saw. Test adding the total RV hold claim to the hero subtext or trust tiles for RV-tagged sessions.

4. **Email Popup Trigger Timing** -- A $20 off email capture is confirmed live but invisible in all fold screenshots. If it fires before configurator engagement is established, it interrupts the primary CTA flow. Audit trigger timing and test delaying the popup until post-configurator scroll depth.

5. **Blackout / Overnight Privacy Use Case** -- Multiple reviewers independently cite overnight privacy as a primary benefit ("dark inside the camper," sleeping at Cracker Barrel). Not referenced in any current ad or product copy. Test adding "Blocks light for overnight privacy" to PDP benefit copy or as a secondary ad creative angle.
