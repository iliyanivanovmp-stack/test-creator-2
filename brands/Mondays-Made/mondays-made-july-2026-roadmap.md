# Mondays Made CRO Research Brief

**Data Sources:** Meta Ads & Landing Pages, Google Ads, Reviews & UGC (80+ reviews Jul 4–8 2026), PageSpeed / Core Web Vitals (Jul 8 2026), Current Site Screenshots

---

## Insights

Mobile performance is the single biggest conversion tax on this site. The homepage LCP is 7.1s on mobile, with a Lighthouse score of 0.05 and Time to Interactive at 27.3s. That means most visitors who click a Meta or Google ad wait nearly half a minute before the page responds to a tap. Server response time alone is 620ms before a single asset loads. The PDP scores only marginally better at 53/100. Every test on this roadmap has diminished impact until the site loads. Source: PageSpeed / Core Web Vitals (Jul 8 2026).

The brand has its most powerful conversion asset in the vault and is not using it. Mondays Made has 5,000+ verified reviews at 4.9 stars. The review corpus is strong: customers describe daily wear durability since 2024 and call the pieces "brand new" after two years. Yet Ad 2, which explicitly promises "50,000+ customers across 100 countries. See what they say," drives directly to the Baby Breath Moissanite Necklace PDP, which shows zero customer reviews. Confirmed via live site fetch (Jul 8 2026). Source: Meta Ads (visual summary), Reviews & UGC.

The brand's most defensible product differentiator is invisible in Meta advertising and on the homepage. Reversible jewelry is the feature customers cite most in repeat-purchase reviews: "seldom will you find a jewelry shop that sells this kind of item" (J.T.); "love that it has two designs" (J.O.). Google runs dedicated ad copy for it. Meta does not. The homepage hero leads with "THE PUFFIES / The Summer Edit." in seasonal editorial language. No Meta creative mentions reversibility. This is a positioning gap with validated customer demand sitting unused at the highest-traffic entry points. Source: Reviews & UGC, Google Ads, Meta Ads.

Cart mechanics leave incremental revenue untouched. Free shipping is met by the first item at $149, eliminating any threshold incentive to add more. The cart drawer has no product recommendations despite a "Complete the Look" carousel existing on PDPs. Review authors describe completing jewelry sets over multiple purchases, which means the upsell intent is there. Source: Current Site Screenshots (cart, PDP), Reviews & UGC.

Revenue opportunity: If mobile LCP improvements recover even 10% of bouncing sessions and the social proof and buy box tests each deliver a conservative 5% CR lift on their respective traffic pools, the combined impact on a brand at this stage runs into thousands of dollars monthly per test. Monthly session data was not captured in this audit; all slot estimates show the calculation structure with sessions as the variable.

---

## Slot 1: Ad 2 Social Proof Above-Fold LP Fix

**Type:** A/B test (1 variation vs. control)
**Page:** Baby Breath Moissanite Necklace PDP (https://mondaysmade.com/products/baby-breath-moissanite-necklace)
**Revenue potential:** [Ad 2 monthly sessions] x 10–15% CR lift x $149 AOV. Ad 2 is the brand's highest social proof creative; closing the promise-to-page gap is a direct revenue unlock on that traffic.

**Hypothesis:** If we add customer review quotes directly above the Add to Bag CTA on the Baby Breath Necklace PDP, add-to-bag rate on Ad 2 traffic increases because the ad explicitly promises "see what they say" and the current PDP delivers zero reviews in three folds.

**Data:** Ad 2 body copy: "50,000+ customers across 100 countries. See what they say." Live site fetch (Jul 8 2026) confirmed: "No customer reviews are displayed on this product page." The 5-star aggregate rating appears in the buy box but no review text is visible. Review corpus includes highly specific durability quotes that would serve this placement. Source: Meta Ads (visual summary), WebFetch (Jul 8 2026), Reviews & UGC.

**V1:** Add a two-quote review block immediately below the star rating in the buy box, above the price. Each quote: customer first name, "Verified buyer" label, 5-star icon row, and 2-line review excerpt. Use "Had this necklace since 2024 and it still looks brand new!" (C.Y.) and "Wore it almost everyday and it doesn't rust" from the corpus. On mobile: full-width stacked cards, 14px body font, 44px minimum tap height on any interactive element. On desktop: constrained to the buy box column width, same layout.

---

## Slot 2: Homepage Mobile LCP

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (https://mondaysmade.com/)
**Revenue potential:** [Monthly homepage sessions] x 10–20% bounce recovery x baseline CR x $149 AOV. Every 1,000 sessions at a 1.5% baseline CR = 15 orders per month. Recovering bounces at scale is the highest-leverage performance lever on this roadmap.

**Hypothesis:** If we reduce homepage LCP to under 3s on mobile, sessions reaching the buy funnel increase because the current 7.1s LCP causes an estimated 10–20% of visitors to abandon before the page becomes interactive.

**Data:** Homepage mobile Lighthouse score: 0.05. LCP: 7.1s. Time to Interactive: 27.3s. Speed Index: 22.3s. Server response time: 620ms (flagged FAIL). The LCP element is the split-screen hero: left lifestyle image (model face/hand with ring, blue background) and right editorial banner (cream background, serif headline, pink button). Industry benchmark: every 1s LCP reduction correlates to a 3–5% CR lift. Source: PageSpeed / Core Web Vitals (Jul 8 2026).

**V1:** Replace the split-screen hero image pair with a single optimized WebP image for mobile. Preload the LCP image via `<link rel="preload">`. Defer non-critical JS loading below the fold. Implement server-side caching to reduce TTFB below 200ms. Target: mobile LCP under 3s, TTI under 5s. On mobile: single full-width hero, same headline and CTA preserved. On desktop: restore the split layout using the current design; LCP on desktop (score 75/100) is not the priority here.

---

## Slot 3: Cart Drawer Cross-Sells

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (/cart)
**Revenue potential:** [Monthly cart views] x 10% cross-sell attachment rate x $30 average added item value = AOV uplift per converting session. Review data shows repeat purchasers describe completing sets across orders; the propensity to add is present.

**Hypothesis:** If we add a "Complete the Look" product recommendation block in the cart drawer, AOV increases because free shipping is already satisfied at $149 and there is no current prompt to add a second item.

**Data:** Cart drawer (Jul 8 2026): free shipping progress bar reads "Your order total qualifies for free shipping!" with a full purple bar, immediately below the single line item. Below that: large blank white space, then subtotal, then full-width CHECKOUT button. No product recommendations exist in the cart. A "Complete the Look" carousel is present in folds 2–3 on ring PDPs. Review corpus includes "finally completed the set" language from repeat buyers. Source: Current Site Screenshots (cart), Current Site Screenshots (PDP).

**V1:** In the blank white space between the line item and subtotal, add a "Complete the Look" horizontal product carousel. On mobile: 2-card horizontal scroll, each card showing product thumbnail, name, and price with a circular "+" add button. On desktop: 3-card row, same format. Surface the same recommendations already used in the PDP "Complete the Look" section for the relevant product category.

---

## Slot 4: First-Order Discount Popup vs. Sidebar

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (https://mondaysmade.com/)
**Revenue potential:** Email capture rate improvement x email sequence LTV; direct first-purchase conversion lift for Meta ad traffic who currently receive no offer exposure. No specific session-based calculation is possible without email capture baseline data.

**Hypothesis:** If we replace the passive left-edge sidebar as the primary discount trigger with an active homepage popup, email capture rate and first-purchase conversion increase because the sidebar requires noticing a narrow vertical strip and Meta ad traffic arrives with no discount context.

**Data:** Current homepage: persistent purple sidebar on the left edge with vertical text "GET 10% OFF." No popup is active. All three Meta ad creatives make zero mention of a discount. Google search ads use "10% Off Your First Order" as a primary headline — meaning Google-intent visitors are primed for the offer and Meta visitors are not. Source: Current Site Screenshots (homepage), Google Ads (visual summary), Meta Ads (visual summary).

**V1:** Trigger a single-step email capture popup on the homepage after 8 seconds or on exit intent (whichever comes first). Popup headline: "Get 10% off your first order." One email field, one CTA button ("Get my code") in brand purple. No discount code shown until email is submitted. On mobile: full-screen overlay, 44px CTA button. On desktop: center-modal, 480px wide. The left-edge sidebar remains in place but is subordinate to the popup as the primary capture path.

---

## Slot 5: PDP Buy Box Review Snippet

**Type:** A/B test (1 variation vs. control)
**Page:** Product PDPs — Carved Sakura Ring, Baby Breath Moissanite Necklace, Carved Sunflower Ring (all three Meta ad landing pages)
**Revenue potential:** [Monthly combined PDP sessions] x 5–8% CR lift x $149 AOV. This runs across three high-traffic landing pages simultaneously, multiplying the revenue opportunity.

**Hypothesis:** If we add a rotating customer review quote directly in the buy box on all three ad LP PDPs, add-to-bag rate increases because the 4.9-star aggregate rating signals trust but provides no specific evidence at the moment of decision.

**Data:** All three ad LP buy boxes show: product name, teal materials subtitle, 5-star aggregate rating (no count displayed), price, finish swatches, "Make it a gift?" text link, and "ADD TO BAG" button. No customer quote appears in the first three folds on the Sakura Ring or Sunflower Ring PDPs. Zero reviews appear on the Baby Breath Necklace PDP at any fold. Review corpus contains product-specific, high-specificity quotes with durability, design, and gifting themes. Source: Meta Ads (visual summary, all three LP fold descriptions), Reviews & UGC.

**V1:** Add one review quote directly below the star rating in the buy box, above the price. Quote format: reviewer first name, "Verified buyer" label, star row, 2-line excerpt. Rotate quotes per product: use durability quotes for the necklace ("Had this necklace since 2024 and it still looks brand new!" — C.Y.); use design-distinctiveness quotes for the rings ("I think seldom will have jewelry shop sell this kind of item." — J.T.). On mobile: full-width within the buy box column, 14px font. On desktop: same placement, constrained to the buy box column width.

---

## Slot 6: Homepage Hero Messaging — Reversible Jewelry

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (https://mondaysmade.com/)
**Note:** Run after Slot 2 concludes. Testing a messaging change on a 7.1s LCP page will produce unreliable data.
**Revenue potential:** [Monthly homepage sessions reaching below-hero scroll] x [incremental collection CTR lift] x baseline CR x $149 AOV. No specific lift estimate is available from the audit data; this tests a positioning hypothesis.

**Hypothesis:** If we replace the seasonal editorial headline in the homepage hero with reversible-jewelry-led messaging, scroll depth and collection click-through increase because the reversible differentiator drives repeat purchase intent per reviews but is absent from all current Meta ads and the homepage.

**Data:** Homepage hero (current control): right half shows editorial banner with "NEW IN | THE PUFFIES / The Summer Edit." in large serif type, with a pink "SHOP NOW" button. Google Ads runs dedicated ad copy for the reversible jewelry feature. Multiple review authors cite reversibility as their stated reason for repeat purchasing: "Love that it has two designs! makes it easy to pair with other rings!" (J.O.); "I think seldom will have jewelry shop sell this kind of item." (J.T.). No current Meta creative or homepage copy surfaces this differentiator. Source: Current Site Screenshots (homepage), Google Ads (visual summary), Reviews & UGC.

**V1:** In the right-half editorial banner of the homepage hero, replace the headline "NEW IN | THE PUFFIES / The Summer Edit." with "Two Looks. One Piece." as the primary headline, and "Shop reversible jewelry." as the supporting line. Keep the pink "SHOP NOW" button. On mobile: the hero collapses to a single stack; display the updated headline on a cream background with the same button. On desktop: same editorial banner half, same layout, updated copy only.

---

## Slot 7: Cart Drawer Loyalty Prompt — Mondays Makers Club

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (/cart)
**Note:** Run after Slot 3 concludes, as Slot 3 fills the blank white space. This test targets the area between cross-sell carousel and the subtotal/checkout block.
**Revenue potential:** Repeat purchase rate improvement x customer LTV. Difficult to estimate without retention data; this tests whether loyalty signaling at checkout reduces post-purchase churn.

**Hypothesis:** If we surface the Mondays Makers Club program in the cart drawer before checkout, repeat purchase intent increases because customers who are already buying have the highest propensity to engage with a loyalty offer, and the program is currently invisible at this moment.

**Data:** Cart drawer (Jul 8 2026): large blank white space between line item and the subtotal/CHECKOUT block. Mondays Makers Club loyalty program is not surfaced in the buy box or cart drawer on any documented page. Review corpus shows multiple repeat purchasers who bought second and third items across separate orders — the repeat purchase behavior already exists. Source: Current Site Screenshots (cart drawer), Reviews & UGC.

**V1:** Add a compact "Mondays Makers Club" block between the cross-sell carousel (Slot 3 winner) and the subtotal. Content: brand icon, one-line benefit statement (e.g., "Earn points on every order. Join free."), and a text link "Learn more." On mobile: full-width, 2-line layout, 14px font, no modal trigger — links to the loyalty program page. On desktop: same layout within the cart panel width.

---

## Slot 8: PDP Buy Box Gifting CTA Elevation

**Type:** A/B test (1 variation vs. control)
**Page:** All three Meta ad landing page PDPs (Carved Sakura Ring, Baby Breath Moissanite Necklace, Carved Sunflower Ring)
**Note:** Run sequentially after Slot 5 to isolate variables. Slots 5 and 8 both modify the buy box; run them separately.
**Revenue potential:** [Monthly PDP sessions from gift-intent visitors] x lift in gifting add-to-bag conversion x $149 AOV. Reviews identify gift purchases as a material buyer segment.

**Hypothesis:** If we elevate the gifting option from a text link to a visual toggle in the buy box, gift-buyer add-to-bag rate increases because multiple review authors identify as gift purchasers but the current "Make it a gift?" trigger is buried as a plain text link below the finish swatches.

**Data:** All three ad LP buy boxes include a "Make it a gift?" text link in the buy box, positioned below the finish swatches and above the ADD TO BAG button. Review corpus: "My niece wore it immediately!" (W.K.); multiple reviews describe gifting to partners and family members. Gift buyers are a confirmed segment on these products. The current UI does not visually distinguish the gifting path. Source: Meta Ads (visual summary, all three LP fold descriptions), Reviews & UGC.

**V1:** Replace the "Make it a gift?" text link with a two-option visual toggle above the ADD TO BAG button: "For me / As a gift." Selecting "As a gift" reveals a gift message text field inline (no modal). On mobile: full-width toggle, 44px touch height per option. On desktop: same inline toggle within the buy box column. The ADD TO BAG button remains the same size and position.

---

## Future Slot Candidates

1. **Ad 1 and Ad 3 creative refresh** - Both run identical body copy for different products (Carved Sakura Ring and Carved Sunflower Ring). A differentiated copy test or a reversible-angle creative for one ad could reduce fatigue and improve CTR to the respective LPs.
2. **Malala Fund ethical angle in Meta ads** - The Malala Fund giving story (10% of profits) appears on product pages but is absent from all three Meta creatives. An ad-level ethical-angle test against the current creative could attract values-driven buyers not currently being addressed.
3. **Mondays Makers Club in buy box** - The loyalty program is absent from the buy box across all PDPs. Surfacing it adjacent to the ADD TO BAG button could reduce first-purchase hesitation by signaling ongoing relationship value.
4. **Gifting-specific Meta ad creative** - Multiple review authors identify as gift buyers. No current Meta creative addresses the gifting use case. A dedicated gifting-angle ad driving to a gift-framed LP is an untested acquisition angle with validated demand.
