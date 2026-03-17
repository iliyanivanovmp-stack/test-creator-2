# April 2026 Testing Roadmap

**Data Sources:** Meta Ads (top 3 best-performing), Reviews & UGC (glove liners + socks), Page Speed / Core Web Vitals, Competitor Research, Current Site Screenshots (homepage, PDP, cart drawer, navigation, collection page)

## Insights

Weston has a trust problem hiding behind strong products. Across 800+ reviews, customers are overwhelmingly positive: glove liners hold a perfect 5.0/5 from 625 reviews, socks sit at 4.9/5 from 176. People write paragraphs about how these gloves changed their daily lives. But the site undercuts that goodwill at every turn.

The most striking finding: the warranty claim changes on every page. The announcement bar says 3 years. The collection page says 1 year. The glove liners PDP says 2 years. When a customer spending $149.95 sees three different warranty terms in one session, they question everything else on the page. Meanwhile, "Free shipping" appears in the trust bar, but the cart drawer reveals a ~$200 threshold. The review count fluctuates between 6,000 and 8,000 depending on the page. These are small details that compound into doubt.

The homepage is the second issue. Two of three top-performing Meta ads land here, and all visitors see is "UP TO 50% OFF on all items / OUR BIGGEST SALE YET!" with an "ENDS: TODAY" button. No product story. No customer proof above the fold. No mention of why these products matter. Reviews tell a different story: at least six glove liner buyers mention Raynaud's disease by name. Customers describe using these gloves on Kilimanjaro, at European Christmas markets, during 12-hour outdoor work shifts in below-freezing weather, and while managing horses. None of that appears on the homepage. The press logos (Good Housekeeping, People, Outdoor Life, Men's Health) are buried below the fold. Only one review is shown despite 8,000+ total.

The third issue is ad-to-page alignment. Ad #3 is a Black Friday ad that has been running since January. It offers 20% off with code CYBER20, but the homepage promotes 50% off. Only one of three ads (Ad #2) lands on the correct product page. The rest dump glove-interested shoppers onto a generic homepage. This is wasted ad spend.

Conservative estimate of the opportunity: if Weston's homepage receives 25,000 sessions/month from Meta ads (conservative for a brand running 3 active campaigns across Facebook, Instagram, Messenger, and Threads) with a 2% conversion rate and $130 AOV, a 15% relative CR lift from better message match and storytelling would add ~$9,750/month in incremental revenue. That's from one page.

---

## Slot 1: Homepage Hero - Problem-Led Storytelling vs. Discount-Only

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (https://www.westonstore.com/)
**Revenue potential:** ~25,000 sessions/mo (est.) x 0.3% CR lift (from ~2.0% to ~2.3%) x $130 AOV = ~$9,750/mo. Sessions estimated based on 3 active Meta ads running across 5 platforms for 2-4 months. CR and AOV estimated from industry benchmarks (no Shopify Analytics data available).

**Hypothesis:** If we replace the discount-only hero with problem-solution storytelling that mirrors the language customers use in reviews, more visitors will engage with the page and convert, because the current hero ("50% OFF on all items") gives no reason to believe these products are different from cheaper competitors.

**Data:** Two of three top-performing Meta ads land on the homepage (Source: Meta Ad Library). The hero is pure discount messaging with no product story, customer proof, or differentiation above the fold (Source: Site Screenshots). Reviews reveal specific, compelling purchase triggers: Raynaud's relief, Kilimanjaro expeditions, hunting in below-zero weather, European Christmas markets. None appear on the homepage (Source: Reviews). Press logos (Good Housekeeping, People, Outdoor Life, Men's Health) are buried below the fold, and only 1 of 8,000+ reviews is shown (Source: Site Screenshots). Competitor homepages from Savior Heat and ORORO similarly lead with discounts, meaning a story-led approach would differentiate Weston (Source: Competitor Research).

**V1:** Replace the current discount-only hero with a problem-solution hero. Headline: customer-centric copy addressing the core pain point (e.g., "Cold hands shouldn't stop you"). Below the headline, a single-line proof point pulling from real review language (e.g., "Trusted by 8,000+ customers, from Raynaud's sufferers to Kilimanjaro hikers"). Hero image: product in use, showing someone performing a fine-motor task (phone, dog leash) while wearing the gloves. The current offer ("UP TO 50% OFF") moves below the headline as a secondary element, not the lead. Keep the trust bar and Best Sellers section unchanged.
**Brief:** Desktop: split layout. Left side: headline, subline proof point, offer badge, CTA button. Right side: hero lifestyle image. Press logos ("As Seen In") move above the fold, positioned directly below the trust bar as a single horizontal row. Mobile: stack vertically. Headline at top, hero image below, proof point and offer beneath that, CTA button full-width. Press logos remain as a horizontal scrollable row below the trust bar. The Best Sellers section and everything below remain untouched. The "ENDS: TODAY" urgency element is removed in V1 to test whether the story-led approach converts without artificial urgency.

---

## Slot 2: Glove Liners PDP - Customer-Language Bullets + Raynaud's Callout

**Type:** A/B test (1 variation vs. control)
**Page:** Glove Liners PDP (https://www.westonstore.com/products/weston-heated-gloves)
**Revenue potential:** ~12,000 sessions/mo (est.) x 0.4% CR lift (from ~3.0% to ~3.4%) x $149.95 AOV = ~$7,198/mo. Sessions estimated from Ad #2 driving traffic directly to this PDP. PDP CR estimated higher than sitewide average because visitors arrive with product-specific intent.

**Hypothesis:** If we rewrite the above-fold bullet points using the specific language customers use in reviews and add a Raynaud's social proof callout, more visitors will add to cart, because the current feature-led bullets ("Premium heat technology that lasts up to 8 hours") describe specs without connecting to the problems customers actually care about.

**Data:** Six glove liner reviewers explicitly name Raynaud's disease/syndrome as their purchase trigger: Victor T., Steve V., Cameron B., Ron L., Alyssa, and Terri L. (Source: Reviews). Multiple reviewers highlight phone/touch screen compatibility as the key differentiator vs. competitors: "unlike other companies' claims of touch screen compatibility, these truly just work" (David R.) (Source: Reviews). The current PDP bullets are generic and feature-led, mentioning "cold hands" but not Raynaud's specifically (Source: Site Screenshots). An estimated 5-10% of the population has Raynaud's, and no major heated glove competitor has claimed this positioning (Source: Competitor Research).

**V1:** Replace the 4 above-fold bullet points with customer-language equivalents:
- Current: "Premium heat technology that lasts up to 8 hours" → New: "8-hour battery. Thin enough to text, drive, and clip a dog leash"
- Current: "3 heat settings" → New: "3 heat settings: 100°F, 120°F, 130°F. Adjust without removing gloves"
- Current: "Perfect for those with cold hands, poor circulation, and arthritis" → New: "Trusted by Raynaud's and poor-circulation sufferers (see reviews)"
- Current: "Includes Rechargeable batteries" → New: "Rechargeable batteries included. Wear as liners or standalone gloves"

Add a mini review callout card between the trust badges and the accordion sections. Single review quote from a Raynaud's customer (e.g., Steve V.: "I have Reynaud's Syndrome... The Weston gloves are thin to allow for manual dexterity AND they are wonderfully warm"), with a "Read 625 reviews" link.

**Brief:** Desktop: bullet points remain in their current right-column position next to the product image. Same icon style. The review callout card appears as a full-width grey background card below the trust badges row and above "Product Details" accordion. Card contains: 5-star rating, 1-line review quote, reviewer name, "Read 625 reviews" text link. Mobile: bullets remain stacked below the product image in their current position. Review callout card appears at full width below the trust badges, before the accordions. All other PDP elements (battery upsell, ATC button, sticky bar, accordions, "Why Weston" section) remain unchanged.

---

## Slot 3: Cart Drawer - Savings Visibility + Shipping Clarity

**Type:** A/B test (1 variation vs. control)
**Page:** Cart Drawer (site-wide, all pages)
**Revenue potential:** Site-wide impact across all sessions that add to cart. If 15% of ~40,000 monthly sessions (est.) reach the cart (6,000 cart sessions), a 5% relative increase in cart-to-checkout rate at $130 AOV = ~$3,900/mo. Cart-to-checkout rate estimated conservatively.

**Hypothesis:** If we show explicit savings amounts and clarify the free shipping threshold in the cart drawer, more customers will proceed to checkout, because the current drawer creates uncertainty: no savings visibility, contradictory free shipping messaging across the site, and "Discounts, Taxes are calculated at checkout" suggests the final price is unknown.

**Data:** The current cart drawer shows no savings summary despite products being 25-53% off (Source: Site Screenshots). "Free shipping" is claimed in the collection page trust bar, but the cart drawer shows a ~$200 threshold: "You're $120.05 away from Free Shipping!" with a single $79.95 item in cart (Source: Site Screenshots). "Discounts, Taxes are calculated at checkout" text below the checkout button creates price uncertainty (Source: Site Screenshots). Reviewer Linda D. flagged trust concerns about unexpected charges at checkout related to battery auto-adds (Source: Reviews). The warranty claim inconsistency (1-year vs. 2-year vs. 3-year across pages) means trust signals in the cart drawer need to be accurate and consistent (Source: Site Screenshots).

**V1:** Three changes to the cart drawer:
1. Add a line-item savings display. Below each product's price, show the original price struck through and savings in green text (e.g., "You save $159.05"). At the subtotal line, show total savings: "Total savings: $159.05" in green.
2. Rewrite the free shipping progress bar to include the threshold amount explicitly: "Spend $200 for FREE shipping. You're $120.05 away!" (Use the actual threshold. If the threshold is not $200, use the correct number.)
3. Replace "Discounts, Taxes are calculated at checkout" with "Taxes calculated at checkout." Remove the word "Discounts" since the discount is already reflected in the product price, and including it implies a further unknown adjustment.

**Brief:** Desktop and mobile: the cart drawer layout is identical across devices (side drawer). Savings line appears directly below the product price in the same font size, green color (#2d7d46 or similar), prefixed with "You save." Total savings line appears directly above the subtotal in green, left-aligned. Free shipping bar text changes from "You're $X away from Free Shipping!" to "Spend $[threshold] for FREE shipping. You're $X away!" The "Discounts, Taxes are calculated at checkout" text changes to "Taxes calculated at checkout." All other cart drawer elements (battery upsell, cross-sell carousel, trust badges, checkout button) remain unchanged.

---

## Future Slot Candidates

These test ideas emerged from the data but didn't make the April cut. Queued for May or later:

1. **Dedicated Glove Landing Page for Meta Ads:** Build a purpose-built landing page for glove ads instead of sending traffic to the homepage. Combine the best PDP elements (specs, reviews) with landing page storytelling (use cases, press logos, Raynaud's angle). Test via ad-level split against the current homepage destination for Ads #1 and #3.

2. **Collection Page Above-the-Fold Optimization:** The "All Products" collection page has no hero image, no category explanation, and a trust bar that claims "1-Year Warranty" (inconsistent with the rest of the site). Test adding a lifestyle hero image, category navigation pills, and consistent trust signals.

3. **PDP Product Gallery Expansion (Socks):** The heated socks PDP has only 1 product image vs. multiple on the glove liners PDP. Test adding lifestyle and in-use photos to the socks gallery, including images showing the socks inside boots (a top use case from reviews).

4. **Raynaud's Dedicated Landing Page:** Build a condition-specific landing page targeting Raynaud's sufferers. Pull from the 8+ reviews mentioning the condition. Target via Google Search ads ("heated gloves Raynaud's") and Meta interest targeting. This could open an entirely new acquisition channel.

5. **Bundle Page or PDP Bundle Messaging:** The socks PDP already has "Bundle & save" with clear tiered pricing. Test extending this approach to glove liners, or creating a cross-product bundle page (gloves + socks at a combined discount) since reviews show customers often buy both products.
