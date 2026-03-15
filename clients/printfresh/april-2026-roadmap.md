# April 2026 Testing Roadmap

**Data Sources:** Shopify Analytics, Heatmaps, Customer Surveys, Meta Ads, Site Search, Reviews & UGC, Page Speed, Previous A/B Tests, Competitor Research, Inspiration Sites, Content Calendar, Intelligems Analytics, Current Site Screenshots

---

## Insights

Printfresh's conversion rate has dropped from 1.61% to 1.04% over the last 30 days. The prior period included a warehouse sale that drove 274K sessions of deal-seeking traffic. Now that traffic has normalized, the site is converting full-price visitors at its true baseline. Intelligems confirms the trend: weekly CVR declined from 1.13% to 0.88% through February as discount-driven sessions faded. The store's real challenge is clear: converting customers who are paying full price.

The PDP is the place to solve this. Price remains the #1 purchase objection (55% of survey respondents), yet reviews tell the opposite story: customers who buy describe Eco Satin as "amazing," say they "go to bed feeling like a queen," and come back for multiple sets. The gap between pre-purchase skepticism and post-purchase love is the single biggest conversion opportunity. But on the current PDP, the information that would bridge this gap is hidden. The product description, fabric details, and care instructions all live inside collapsed accordions that most visitors never open. On mobile (79% of traffic), a visitor must scroll past 8+ gallery images, title, price, sizing callout, color swatch, social proof, size selector, CTA, trust icons, and gift wrapping before reaching the first accordion. The PDP is cluttered, with competing visual elements and excessive vertical distance between the gallery and the buy action. PF18 (PDP cleanup/simplification) already won historically, proving that layout improvements on this page convert.

The PDP also underserves cross-sell. "Recently Viewed" and "You May Also Like" sections exist below the fold, but there is no curated "style it with" or "complete the look" experience. With a median order value of $174 sitting $21 below the free shipping threshold ($195), even a small increase in units per order would push more customers over the threshold and lift AOV simultaneously.

Beyond the PDP, April presents two distinct opportunities. Mother's Day (May 11) is the next major gifting moment. April's content calendar leads with "Mother's Day Focus" and "Giftableness," yet the site has no dedicated gifting experience. Reviews mention gifting 94 times in 30 days. The top Bagheera ad sells "the silky-soft gift they'll love unwrapping," but its landing page has no gifting context. April is the ramp.

The other opportunity is product discovery. Printfresh has a high SKU count across dozens of prints, multiple fabrics, and several silhouettes. Site search data shows 41,458 searches in 30 days, dominated by print names (cat+cats = 1,469, dachshund = 577, horse = 547). New visitors (52.75% of traffic) have no efficient way to navigate from "I want fun pajamas" to the right product. The brand is already building persona-based print categories in email marketing ("Co-Sleeping Furry Friend," "Snacks in Bed," "Sound Machine On"). A quiz that translates this personality-to-print matching into a shoppable on-site experience would reduce decision paralysis and give paid traffic a high-intent landing destination.

---

## Slot 1: PDP Cleanup + Product Information Architecture

**Type:** A/B test (4 variations vs. control)
**Page:** PDP, starting with top products by revenue: Courtly Check Bagheera Soho Set (~$150K/mo), Bagheera Eco Satin Robe (~$118K/mo), Macrame Mischief Wildest Dreams Set (~$36.6K/mo). Applies to all Eco Satin PDPs via fabric metafield. Expand to Knits PDPs after launch if results are positive.
**Revenue potential:** ~100K combined monthly sessions on Eco Satin PDPs x 0.3% ATC lift x $193 AOV = ~$57,900/mo

**Hypothesis:** If we clean up the PDP's visual hierarchy and surface product information that is currently hidden in collapsed accordions, add-to-cart rate will increase because the current PDP is cluttered and overwhelming, key purchase-decision content (fabric details, product story, fit information) is buried below the fold in collapsed accordions, and PDP cleanup/simplification has won historically (PF18).

**Data:** Over 55% of post-purchase survey respondents cite price as what almost stopped them, yet reviews describe Eco Satin as "amazing," "so soft," "you go to bed feeling like a queen" (Source: Surveys, 214 responses, Feb 6 - Mar 8, 2026; Reviews). Heatmap data shows strong engagement with product images, price, size selector, and ATC button, but the Description, Details, and Shipping & Returns accordions sit deep below the trust icons and gift wrapping section, where most visitors do not scroll (Source: Heatmaps). All three accordions are collapsed by default, hiding fabric origin, care instructions, sizing details, and the product story. On mobile (79% of traffic), the vertical distance between the gallery and the first accordion is excessive: 8+ swipeable images, title, price, star rating, Shop Pay installments, sizing callout, color swatch, social proof ("In 514 Carts"), size selector, CTA button, trust icon row, and gift wrapping + "Send a Hint" all precede the accordions (Source: Device Split, Site Screenshots). PF18 (PDP cleanup/simplification) won historically (Source: Previous Tests). "Eco satin" was searched 672 times in 30 days, indicating active demand for fabric information (Source: Site Search). Lake Pajamas features a full-width fabric story hero on every PDP; Desmond & Dempsey leads with print stories (Source: Inspiration).

**V1: PDP Design Cleanup**
Tighten the visual hierarchy and reduce clutter in the buy box area. Specific changes: (1) Consolidate the trust icon row into a more compact format: replace the three large stacked icon+label blocks (Free Shipping, Easy Returns, Guarantee to Quality) with a single-line inline format or smaller icon pills, cutting vertical space by ~50%. (2) Reduce spacing between buy box elements on mobile. The current layout has generous padding between each section (price, social proof, size selector, CTA, trust icons, gift wrapping). Tightening this brings the CTA higher. (3) Restyle the gift wrapping + "Send a Hint" row: currently two disjointed elements (checkbox on the left, underlined link on the right). Combine into a single, cohesive gift options bar. (4) On desktop, tighten the right column so the ATC button and trust elements are visible without scrolling alongside the first product image. (5) Improve the gallery dot indicators on mobile for better scannability (current small dots are hard to distinguish across 8+ images). The goal: reduce vertical distance between gallery and CTA on mobile by 15-20%, and make the buy box feel clean and intentional rather than stacked and cluttered.
**Brief:** Design: full PDP audit with mobile-first layout tightening. Reference the current screenshots for specific spacing issues. No new components, just refinement. Dev: CSS and minor template changes. Measure: scroll depth to ATC, ATC rate, time on PDP.

**V2: V1 + Description Accordion Open by Default**
All V1 cleanup changes, plus the Description accordion is expanded by default on page load. Details and Shipping & Returns remain collapsed. This surfaces the product story, fabric description, and key selling points without requiring any user interaction. The Description typically contains fabric composition, print story, and product features. This is the simplest way to test whether making this content visible (rather than hidden) affects conversion.
**Brief:** Design: no additional design work beyond V1. Verify the open accordion state looks clean with existing content lengths across different products. Dev: change default state of Description accordion from collapsed to expanded. Straightforward JS/Liquid change.

**V3: V1 + Product Description Below the Price**
All V1 cleanup changes, plus extract the core product description from the Description accordion and place it as visible body text between the price/star rating line and the color selector. The extracted text should be 2-3 sentences covering: what the product is (silhouette + fabric), the print story, and one key feature (e.g., "Machine washable. Thermoregulating. Sustainably sourced."). The Description accordion can remain below with the full content, or be removed if the extracted text covers all key points. This tests whether surfacing the story at the moment of price shock changes the frame.
**Brief:** Design: style the extracted description as body text within the buy box flow. Font size slightly smaller than the product title, matching brand typography. Mobile: full-width text block between price line and color selector. Desktop: same column, same placement. Dev: pull from the product description metafield, or use a dedicated "short description" metafield if available.

**V4: V1 + Fit & Silhouette Info in Image Gallery**
All V1 cleanup changes, plus add a translucent info overlay on one gallery image (e.g., the lifestyle or flat-lay image) showing the product's fit and silhouette details in a scannable format. On mobile, this appears as a pill or bar at the bottom of a gallery slide (similar position to the existing "Play Video" pill, either replacing it on a different slide or positioned on the flat-lay image). Content example: "Relaxed fit / Button-front top / Elastic waist / Ankle length." On desktop, the overlay appears on hover or as a persistent label on the flat-lay image. This addresses sizing and fit anxiety at the point of highest engagement (the gallery, where heatmap data shows the hottest clicks) rather than burying it in the accordions.
**Brief:** Design: translucent overlay or pill element that does not obscure the product image. Use existing product attribute data (silhouette, fit type, length). Reference the "Play Video" pill styling for consistency. Dev: conditionally render based on available product metafields for fit type and silhouette. If metafields are not populated for a product, hide the overlay. Coordinate with "Play Video" placement so they do not conflict (different gallery slides).

**Sequencing note:** PF23 (trust badges below CTA) and PF24 (fit & size) will conclude before April tests launch. If either wins, incorporate the winning elements into the control for this test. V1's trust icon redesign should account for PF23's results. This test targets the buy box zone (above the accordions). Slot 4 (upsells) targets the zone below the accordions, so both tests can run simultaneously on the same products without conflict.

---

## Slot 2: Mother's Day Gifting Experience

**Type:** A/B test (4 variations vs. control)
**Page:** Collection page (to be confirmed with client based on where Mother's Day paid traffic will be directed). Default candidate: /collections/bagheera (52,050 sessions/mo, primary gifting ad destination) or a new dedicated gifting collection.
**Revenue potential:** 52,050 sessions/mo (Bagheera baseline) x 0.3% CR lift x $193 AOV = ~$30,137/mo. Sitewide elements in V3/V4 would expand reach beyond the collection page.

**Hypothesis:** If we add gifting context, a Mother's Day shipping cutoff countdown, and curated gift navigation to the pages where Mother's Day traffic lands, conversion rate will increase because the brand's gifting ads promise a gifting experience ("the silky-soft gift they'll love unwrapping") that the site does not deliver, and April is the peak ramp to Mother's Day (May 11).

**Data:** /collections/bagheera drove 52,050 sessions in the last 30 days, with significant traffic from the Bagheera Meta ad running since Dec 4, 2025 (Source: Shopify Analytics, Meta Ads). The ad copy promises "the silky-soft gift they'll love unwrapping" but the landing page is an undifferentiated product grid with no gifting context (Source: Meta Ads, Site Screenshots). Reviews mention gifts or gifting 94 times in 30 days (Source: Reviews). April content calendar theme: "Mother's Day Focus" and "Giftableness" (Source: Content Calendar). Mother's Day is May 11. 53.3% of orders don't qualify for free shipping (median order $174 vs. $195 threshold), and "having to pay for shipping on a $150 product" is a survey objection (Source: Intelligems, Surveys). Gift wrapping exists on PDP as a checkbox below the trust icons but is not featured or visual (Source: Site Screenshots). The client has specifically requested more landing page tests (Source: Non-Data Context).

**V1: Mother's Day Shipping Cutoff Banner + Collection Hero**
Add a slim, sitewide banner below the announcement bar with a Mother's Day shipping cutoff countdown: "Order by [date] for guaranteed Mother's Day delivery." On the collection page, replace the generic header with a gifting-themed hero: headline ("The Gift They'll Actually Wear"), one-line subtext about Eco Satin, and one lifestyle image. Products remain immediately below. The hero should be compact enough on mobile that the first product row is visible on the first scroll.
**Brief:** Design: slim countdown banner (sitewide, dismissible) + compact collection hero (collection page only). Dev: banner is time-gated, displays from launch through the shipping cutoff date (date TBD based on fulfillment timelines). Collection hero: inject above the product grid. CMS-editable so copy can be updated without dev work.

**V2: V1 + Curated "Top Gifts for Mom" Section**
All V1 elements, plus a curated row of 3-4 best-selling products below the hero, styled as gift recommendations. Each card shows product image, name, price, star rating, and a "Gift Wrap Available" tag. This gives gift buyers a shortcut instead of scrolling an undifferentiated grid.
**Brief:** Design: curated product row with gifting labels. Dev: manually curated product IDs, editable via metafield or CMS. Row appears between hero and filter bar, separate from the main product grid.

**V3: V2 + Enhanced Gift Wrapping on PDP**
All V2 elements, plus redesign the gift wrapping section on PDPs linked from this collection. Replace the current checkbox ("Add Gift Wrapping") and "Send a Hint" link with a more visible, expandable gift wrapping module: gift wrap preview image, personalized gift message option, and pricing. Position it more prominently, above the trust icons rather than below them. This closes the loop: the collection page sells the gift, and the PDP makes it easy to send it as one.
**Brief:** Design: expanded gift wrapping module with visual preview, replacing the current checkbox row. Dev: applies to PDPs reached from the gifting collection (or all PDPs if simpler to implement globally). Track: gift wrapping add rate, AOV impact.

**V4: V3 + Price-Tier Gift Guide**
All V3 elements, plus replace the curated "Top Gifts" row with a price-tier gift guide: "Under $100" (eye masks, shorts, single pieces), "Under $200" (PJ sets, nightgowns), "Luxury $200+" (robes, bundles). Each tier is a clickable tile showing 2-3 products. This addresses the core gifting question ("what should I spend?") by giving gift buyers pre-sorted price options.
**Brief:** Design: 3-tile price tier layout, stacked on mobile, inline on desktop. Dev: each tile links to a filtered view of the collection by price range or to a curated product set. CMS-editable product selections per tier.

**Sequencing note:** This test should launch early April to capture the full Mother's Day gifting ramp. The exact collection page and shipping cutoff date need confirmation from the client. After Mother's Day, the countdown banner auto-hides and the remaining gifting elements continue running as a general gifting experience.

---

## Slot 3: Print Persona Quiz

**Type:** A/B test (quiz page vs. control destination)
**Page:** Standalone quiz page (custom build), linked from homepage, navigation, email, and paid ads. Control: visitors sent to /collections/pajamas or homepage (depending on traffic source).
**Revenue potential:** If 10% of homepage sessions (8,770/mo) + paid ad traffic enter the quiz, and quiz completers convert at 2x the site average (2.08% vs. 1.04%): ~8,770 x 2.08% x $193 AOV = ~$35,200/mo. Conservative estimate; quiz traffic from email and ads would expand reach.

**Hypothesis:** If we create a personality-to-print quiz that matches visitors to curated product selections based on their lifestyle and sleep personality, conversion rate among quiz completers will be significantly higher than the site average because the high SKU count creates decision paralysis for new visitors (52.75% of traffic), print-based navigation is the #1 organic discovery method (41K site searches), and the brand is actively building persona-based print categories in their marketing.

**Data:** Site search logged 41,458 searches in 30 days, dominated by print names: cat+cats = 1,469, dachshund = 577, horse = 547, bagheera = 733, peckish pastries = 349, sweet bee = 314 (Source: Site Search). New visitors make up 52.75% of traffic and show lower conversion intent: "uncertainty about the company... dipping my toes in the water," "1st time shopper. Let's see how it goes" (Source: Surveys, Shopify Analytics). The brand's email marketing already maps prints to lifestyle personas: "Co-Sleeping Furry Friend" (animal prints), "Snacks in Bed" (food prints), "Sound Machine On" (nature prints), "A Cup of Chamomile" (floral prints), "Fiction or Non-Fiction" (book prints) (Source: Email, March 13, 2026). Print portals on /collections/pajamas validate that print-based navigation works, but are limited to one collection page (Source: Site Screenshots). Collection page structural changes tend to lose (PF02, PF09), but a standalone quiz bypasses collection page limitations entirely (Source: Previous Tests). The client is investing in "personas" around prints for marketing; the quiz bridges that brand investment with on-site conversion (Source: Client Meeting).

**Quiz structure (all variations):**
3-5 lifestyle questions (not product questions) determine the visitor's "sleep personality." Example flow:
1. "What's your ideal way to unwind?" (Reading / Cooking / Nature walk / Playing with pets / A fancy cocktail)
2. "Your dream vacation?" (Parisian cafe / Tropical jungle / English countryside / Tokyo food tour / Safari)
3. "Pick a Saturday morning vibe" (Farmers market / Dog park / Brunch with friends / Solo coffee and a book / Sleep in, obviously)

Each answer maps to a print persona. At the end, the visitor sees their result ("You're a Co-Sleeping Furry Friend!") with a curated selection of products in matching prints. Results page is shoppable: product cards with quick-add, and a "Shop All [Persona] Prints" CTA linking to the relevant collection.

**V1: Basic Quiz with Shoppable Results**
Quiz flow as described. Results page shows persona name, a short personality description, and 6-8 products in the matching print(s). Standard product cards with image, name, price, and quick-add. "Retake Quiz" option and "Shop All [Print]" link.
**Brief:** Design: mobile-first quiz UI. One question per screen, progress bar, large tappable answer tiles with lifestyle imagery. Results page: persona hero image + product grid. Dev: custom build on Shopify (standalone page template). Product results populated by print tag/metafield mapping. Track: quiz starts, question drop-off by step, completions, completion rate, result-to-PDP clicks, result-to-ATC, purchase attribution (quiz completers vs. control cohort).

**V2: V1 + Fabric Recommendation Layer**
Same quiz flow, but the results page adds a fabric recommendation on top of the print match. After revealing the persona, a secondary module says: "Based on your vibe, we'd recommend starting with Eco Satin" (or Organic Cotton, or Knits) with a one-line fabric description. Products in the results grid are filtered to the recommended fabric first, with a toggle to see other fabrics.
**Brief:** Design: fabric recommendation module between persona hero and product grid. Dev: map quiz answers to both print persona and fabric preference. Logic can be simple: "luxury/indulgent" answers map to Eco Satin, "cozy/casual" to Knits, "breathable/practical" to Organic Cotton.

**V3: V2 + Social Sharing and Email Capture**
All V2 elements, plus the results page includes: (1) a shareable results card ("I'm a Co-Sleeping Furry Friend! Find your Printfresh match") with social share buttons, and (2) an email capture: "Save your results and get [X]% off your first order" (discount TBD with client). This turns the quiz into both a conversion and an acquisition tool.
**Brief:** Design: shareable card with persona illustration, social share buttons (Instagram Story, iMessage, email). Email capture with results summary. Dev: social share generates a dynamic OG image per persona. Email capture integrates with Klaviyo. Discount code auto-applies on redirect to cart.

**V4: V3 + Homepage Quiz Entry Point**
All V3 elements, plus add a quiz entry module on the homepage below the hero (or replacing one of the "Live On The Bright Side" category tiles): "What's Your Sleep Personality?" with a lifestyle image and "Take the Quiz" CTA. This tests whether featuring the quiz on the highest-traffic page drives meaningful quiz engagement.
**Brief:** Design: homepage module matching existing tile aesthetic. Dev: link to standalone quiz page. The homepage module itself can be A/B tested against the current tile it replaces. Track: homepage quiz click-through rate, quiz start rate from homepage vs. other entry points.

**Sequencing note:** The quiz is the most ambitious test in this roadmap. V1 is the MVP and should be scoped first. V2-V4 layer on complexity and can launch as subsequent iterations if build timeline requires phasing. The quiz works as a destination for paid ads and email (the "What's Your Sleep Hack?" email is a natural entry point). For measurement, compare quiz completers vs. a matched cohort sent to /collections/pajamas.

---

## Slot 4: PDP Product Upsells

**Type:** A/B test (3 variations vs. control)
**Page:** PDP, same product scope as Slot 1 (top Eco Satin PDPs by revenue). Placement: below the accordions, repositioning or replacing the existing "Recently Viewed" and "You May Also Like" sections.
**Revenue potential:** ~100K combined monthly sessions x $5 AOV lift from upsell additions x 3% upsell take rate = ~$15,000/mo incremental revenue. Additional upside: if upsell additions push more orders over the $195 free shipping threshold, conversion gains compound.

**Hypothesis:** If we replace the generic "Recently Viewed" and "You May Also Like" sections with curated, contextual product recommendations, average order value will increase because the median order value ($174) sits $21 below the free shipping threshold ($195), customers already navigate by print (41K site searches), and the current below-fold PDP experience offers no curated cross-sell.

**Data:** AOV is $193 but median order value is $174, $21 below the $195 free shipping threshold (Source: Intelligems). 53.3% of orders don't qualify for free shipping (Source: Intelligems). Average units per order is 1.76, down 2.6% (Source: Intelligems). Print-name searches dominate site search (41K total), showing customers want to explore products within the same print (Source: Site Search). The PDP currently has "Recently Viewed" and "You May Also Like" sections below the fold, but neither is curated or contextual to the product being viewed (Source: Site Screenshots). Repeat purchase behavior is strong: "I have this set in several patterns" (Source: Reviews). Desmond & Dempsey uses a "Shop the Print" section on PDP showing all products in the same print (Source: Inspiration). LoveShackFancy uses a "Style It With" section below the accordions with complementary cross-category products and quick-add functionality (Source: Inspiration).

**V1: "Style It With" - Curated Complementary Products**
Replace the existing "Recently Viewed" section position with a "Style It With" section showing 3-4 curated complementary products from the same print. If viewing a PJ set, show the matching robe, eye mask, shorts, or slippers. Each card: product image, name, price, star rating, quick-add button. Horizontal scroll on mobile, inline row on desktop. "You May Also Like" can remain below or be removed.
**Brief:** Design: product row with "Style It With" heading, matching existing card styles. Reference LoveShackFancy's implementation for layout. Dev: populate from products sharing the same print tag/metafield but different product types (exclude current product's type). If the print has fewer than 2 complementary products, fall back to "You May Also Like" logic. Track: upsell clicks, upsell ATC rate, AOV change, units per order, free shipping qualification rate.

**V2: "More in This Style" - Same Silhouette, Different Prints**
Same position as V1, but show 3-4 products of the same silhouette in different prints and colorways. If viewing the Rittenhouse Set in Champagne & Caviar, show the Rittenhouse Set in other available prints. This helps customers who like the fit but want to explore print options. Each card: product image, print name, price, star rating, quick-add.
**Brief:** Design: same component structure as V1, different heading. Dev: populate from products sharing the same product type/silhouette tag but different print tags. Prioritize in-stock colorways and newer prints.

**V3: "Recently Viewed" - Redesigned and Repositioned**
Keep the "Recently Viewed" concept but redesign it with the same card styling as V1/V2 (matching product cards with quick-add buttons), and move it to the same prominent position below the accordions. The current implementation uses a generic carousel without quick-add. This tests whether a better-designed version of personalized browsing history outperforms curated editorial recommendations (V1, V2).
**Brief:** Design: same card component as V1/V2, populated with recently viewed products. Dev: use existing recently viewed cookie/session data. Add quick-add to each card. If the visitor has no browsing history (new visitor), fall back to "Best Sellers" or hide the section.

**Sequencing note:** This test targets the zone below the accordions. Slot 1 targets the buy box zone above the accordions. Both can run simultaneously on the same PDPs without conflict.

---

## Additional Slot Candidates

Ideas with strong data support that the client can choose from as additional or replacement tests:

### 5. Sizing Guide/Quiz Effectiveness Test (PDP)

Test the impact of the existing size guide and fit recommendation tool. Survey feedback: "The feature asking what size you normally wear isn't very helpful when I could look at the measurement chart instead" (Source: Surveys). Sizing uncertainty is the #3 purchase objection at ~7% of respondents. Variations: (a) remove the fit quiz, show only garment measurements near the size selector, (b) remove the size guide, keep only the fit quiz, (c) both visible, (d) replace both with a simplified measurement table inline near the size selector. PF24 (fit & size) results will inform direction.

### 6. Product Description Copy Angles (PDP)

Continue the product description copy test currently running on Bagheera products, but on higher-traffic products for faster statistical significance. Test 4 angles: (a) customer-voice descriptions with review quotes woven in, (b) fabric-and-craft-focused descriptions emphasizing origin and materials, (c) occasion-based descriptions ("Date night, lazy Sunday, girls' trip"), (d) print-story-focused descriptions explaining the artist's inspiration. The product description copy case study generated +$50,945/mo using customer-voice descriptions (Source: Winning Tests Library).

### 7. PDP Gift Wrapping Enhancement

Can be tested as part of Slot 2 V3, or independently if the Mother's Day slot goes in a different direction. Redesign the PDP gift wrapping experience: replace the checkbox + "Send a Hint" with a visual gift wrapping module (preview image, personalized message, pricing). Could pair with a Mother's Day shipping cutoff countdown on the PDP itself.

### 8. Homepage Second Fold: Press Bar + Featured Collection

Redesign the section below the hero. Add a press/social proof bar (Vogue, Oprah, TODAY, etc. if applicable) and test the featured products/collection layout. Heatmap data shows strong engagement through the hero and category tiles, with drop-off at the testimonial section (Source: Heatmaps). PF04 "What to Expect" module won +3.47% RPV on homepage (Source: Previous Tests). Homepage storytelling module case study: +$130,251/mo (Source: Winning Tests Library). 87,697 sessions/mo (Source: Shopify Analytics).

### 9. Cart Drawer Value Reinforcement

Cart drawer tests have won 3/3 historically. Once PF16 (shipping price) and PF22 (shipping threshold) results are in, test adding: (a) "You save $X" on discounted items, (b) fabric micro-badges per item, (c) trust signals in the drawer. Median order value ($174) is $21 below the free shipping threshold; cart-level nudges could push more orders over.

---

## Open Questions for Client

**Mother's Day traffic destination:** Where will paid Mother's Day traffic be directed? This determines the primary test page for Slot 2. Candidates: existing Bagheera collection, a new gifting collection, or a dedicated landing page.

**Mother's Day shipping cutoff date:** What is the last order date for guaranteed Mother's Day delivery? This sets the countdown timer in Slot 2 V1.

**Quiz persona alignment:** The print persona quiz (Slot 3) should align with the persona framework the marketing team is building. Can we coordinate persona names, imagery, and print-to-persona mappings with the marketing team?

**Quiz imagery and assets:** Does the team have lifestyle imagery for each persona category? The quiz UI relies on visual answer tiles and persona result images.

**Content calendar testing:** April has several major launches (Knits Apr 2, National Pajama Day promo Apr 16, Foggy Dog collab Apr 16, Mother's Day Catalog Apr 13). Are any of these candidates for dedicated landing pages or launch-day experiments?

**Client-actionable items from data (not A/B tests):**
These came from surveys and reviews and may warrant investigation or fixes outside the testing roadmap:

- **Wildest Dreams sizing audit:** Some sets have reportedly been updated to true-to-size, but older reviews still say "runs big." If the fit has changed, the "sizing down is recommended" copy on those product pages may now be incorrect and causing wrong-size orders. Worth auditing which SKUs have been updated.
- **Discount code flow:** 5% of survey respondents reported broken or missing discount codes ("$20 off did not work," "Didn't receive discount code after signing up"). Worth checking the signup-to-code delivery flow.
- **Intermittent checkout bug:** A customer reported "checkout button failed to load on mobile and desktop." Worth checking with dev if there are known intermittent issues.
- **Search config fix:** "mckenzie" + "mckenzie childs" = 58 zero-result searches in the last 30 days. These customers are looking for the MacKenzie-Childs collection (43,454 sessions, 2 of the top 3 ads). Adding synonym mappings to site search would fix this immediately.
- **Monogram UX on pocketed items:** "Sewn pockets with monogram" mentioned twice in surveys. The monogram placement on pocketed items may not be clear in the customization flow.
- **Separate pieces demand:** Multiple customers want to buy tops or bottoms individually, not as sets. Could be a product strategy consideration.
