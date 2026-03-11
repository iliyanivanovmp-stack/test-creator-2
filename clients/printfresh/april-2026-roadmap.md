# April 2026 Testing Roadmap

**Data Sources:** Shopify Analytics, Heatmaps, Customer Surveys, Meta Ads, Site Search, Reviews & UGC, Page Speed, Previous A/B Tests, Competitor Research, Inspiration Sites, Content Calendar, Intelligems Analytics, Current Site Screenshots

---

## Insights

Printfresh's conversion rate has dropped from 1.61% to 1.04% over the last 30 days. That sounds alarming, but the context matters: the prior period included a warehouse sale that drove 274K sessions of deal-seeking traffic. Now that traffic has normalized, the site is converting full-price visitors at its true baseline. Intelligems confirms the trend: weekly CVR declined from 1.13% to 0.88% through February as discount-driven sessions faded. The store's real challenge is clear: converting customers who are paying full price.

The data tells us exactly where to focus. Price remains the #1 purchase objection. Over 55% of survey respondents cite it. "The price good gravy." "I would not have purchased without a sale/discount." Yet reviews tell the opposite story. Customers who buy describe Eco Satin as "amazing," say they "go to bed feeling like a queen," and come back for multiple sets. The gap between pre-purchase skepticism and post-purchase love is the single biggest conversion opportunity on this site. The problem isn't the price. It's that nothing on the page justifies it before checkout. The fabric and value information that would bridge this gap lives in the Description accordion (collapsed by default) and in reviews that sit deep on the PDP, well below the fold.

Reviews also surface a sizing inconsistency problem that compounds the price objection. Different silhouettes in the same fabric fit differently: "if you are used to the Wildest Dream sets, the bottoms do not fit the same way." Some Wildest Dreams sets have reportedly been updated to true-to-size, but older reviews still say "runs big," which may now be misleading customers into sizing down incorrectly. Combined with final sale policies and $145-$228 price points, every wrong-size order becomes a lost customer. There are also signals worth flagging to the client: demand for selling set pieces individually ("hoping to buy just the pants"), a potentially broken discount code flow (5% of survey respondents), intermittent checkout bugs ("checkout button failed to load on mobile and desktop"), and a fit quiz that customers find unhelpful compared to raw measurements.

This is compounded by the Knits launch on April 2. A new fabric category (Luna Jersey) is arriving with no fabric story infrastructure. The "Eco Satin sounds sus" skepticism that shows up in surveys could repeat with a new, unfamiliar fabric name. Building a fabric education module now serves both Eco Satin and Knits.

Gifting is the other underserved opportunity. April's content calendar leads with "Mother's Day Focus" and "Giftableness," yet the site has no dedicated gifting experience. Reviews mention gifting 94 times in the last 30 days. The top-performing Bagheera ad sells "the silky-soft gift they'll love unwrapping," but its landing page is a massive undifferentiated product grid with no gifting context. With Mother's Day on May 11, April is the ramp.

The math: the homepage alone drives 87,697 sessions per month at an RPV of $2.32. A 5% RPV lift (conservative, given PF04 achieved +3.47%) would generate an additional $10,172/mo from one page. Across the top 4 landing pages (280K combined sessions), even a 3% RPV lift at current AOV ($193) would add $38,800/mo in revenue.

---

## Slot 1: PDP Fabric Story Module

**Type:** A/B test (4 variations vs. control)
**Page:** PDP, Eco Satin products, starting with top 3 by revenue: Courtly Check Bagheera Soho Set, Bagheera Eco Satin Robe, Macrame Mischief Wildest Dreams Set. Applies to all Eco Satin PDPs via fabric metafield. Expand to Knits PDPs after launch if results are positive.
**Revenue potential:** ~100K combined monthly sessions on Eco Satin PDPs x 0.3% ATC lift x $193 AOV = ~$57,900/mo

**Hypothesis:** If we surface fabric education and customer-voice value proof between the buy box and the collapsed accordions, add-to-cart rate will increase because price is the #1 objection (55% of survey respondents) but post-purchase reviews prove customers love the product once they have it.

**Data:** Over 55% of post-purchase survey respondents cite price as what almost stopped them, yet reviews describe Eco Satin as "amazing," "so soft," "you go to bed feeling like a queen" (Source: Surveys, 214 responses, Feb 6 - Mar 8, 2026; Reviews). Reviews also show strong repeat purchase behavior ("I have this set in several patterns") and emotional connection ("I'm so thrilled to put on my Printfresh pajamas at night because they make me feel like it's a special occasion"), but this value proof sits deep on the PDP, well below the fold where most visitors never scroll (Source: Reviews, Heatmaps). "Eco satin" was searched 672 times in the last 30 days (Source: Site Search). One survey respondent noted "fabric to wrinkle annoys me at this price point," reinforcing that customers at this price range expect the fabric story to set expectations upfront (Source: Surveys). Lake Pajamas features a full-width "SILKY SMOOTH DREAMMODAL" fabric story hero on every PDP (Source: Inspiration). The homepage storytelling module case study generated +$130,251/mo for a luxury pajama brand by showing craft before price (Source: Winning Tests Library).

**V1:** Add a "Why Eco Satin" section between the trust icons and the Description accordion. One sentence on fabric origin ("Thermoregulating viscose, sourced from sustainably managed forests. Designed in Philadelphia, hand screen-printed by artisans in India.") and an icon row (Machine Washable, Breathable, Sustainable, Size Inclusive XXS-6X). Everything else stays the same. On mobile, the section appears as a full-width block between trust icons and Description. On desktop, it sits in the same column below the buy box.
**Brief:** Design: one module with a fabric origin line and 4 icons with labels. Match existing brand typography. Dev: conditionally render on Eco Satin PDPs by fabric metafield. Place below PF23 trust badges zone and above Description accordion. No overlap with PF23 or PF24 test areas.

**V2:** V1 plus one customer review quote about the fabric, pulled from existing reviews. Example: "The Ecco Satin fabric is so soft and feels really nice against your skin." Attributed with reviewer first name and star rating. On mobile, the quote appears directly below the icon row. On desktop, same placement.
**Brief:** Design: add a mini-testimonial block below icons. Dev: pull highest-rated review containing "fabric" or "soft" or "satin" keyword from Yotpo API for that product. Fallback to a static quote if API unavailable.

**V3:** V2 plus a lifestyle image showing the fabric drape and texture. One image, approximately 50% width on desktop (alongside the text content) and full-width on mobile. Image should show fabric movement, not a posed model shot.
**Brief:** Design: image + text layout, mobile-stacked, desktop side-by-side. Source one lifestyle image from existing asset library per fabric type. Dev: same conditional rendering logic as V1.

**V4:** V3 plus a "Shop More in This Print" row showing 3-4 other products in the same print (robe, nightgown, eye mask, shorts). Horizontal scroll on mobile, inline row on desktop. Each item shows product image, name, price, and quick-add icon. Inspired by Desmond & Dempsey's "Shop the Print" PDP section.
**Brief:** Design: horizontal product row component. Dev: populate from products sharing the same print tag/metafield. This addresses the print discovery problem (41K searches dominated by print names in the last 30 days). If the print has fewer than 3 products, hide the row.

**Sequencing note:** PF23 (trust badges below CTA) and PF24 (fit & size) will conclude before April tests launch. If either wins, incorporate the winning elements into the control for this test. This test targets the zone below trust badges and above the accordions.

---

## Slot 2: Homepage Personalization for New vs. Returning Visitors

**Type:** A/B test (4 variations vs. control)
**Page:** Homepage ([https://www.printfresh.com/](https://www.printfresh.com/))
**Revenue potential:** 87,697 sessions/mo x 5% RPV lift x $2.32 baseline RPV = ~$10,172/mo

**Hypothesis:** If we personalize the homepage experience based on visitor type (new vs. returning), revenue per visitor will increase because 47.25% of visitors are returning customers who need "what's new" while 52.75% are new visitors who need brand story and trust before they'll pay $228 for pajamas.

**Data:** Homepage drove 87,697 sessions in the last 30 days (Source: Shopify Analytics). Returning customer rate is 47.25% (Source: Shopify Analytics). PF04 "What to Expect" module won +3.47% RPV on the homepage, proving modular additions work here (Source: Previous Tests). Surveys show new customers need value justification: "uncertainty about the company... dipping my toes in the water," "1st time shopper. Let's see how it goes" (Source: Surveys). The homepage storytelling module case study generated +$130,251/mo by adding a craft/origin story (Source: Winning Tests Library). The client has specifically requested more personalization tests (Source: Non-Data Context).

**V1:** For new visitors only, replace the current hero with a "Why Printfresh" brand story module: one-line headline ("Joyful designs, hand-painted in Philadelphia"), a 10-second autoplay lifestyle video or hero image showing the studio/artisan process, and a press logo bar (Vogue, Oprah, etc. if applicable). Returning visitors see the default homepage. On mobile, the module is full-width with video/image stacked above press logos. On desktop, split layout with video left and copy/logos right.
**Brief:** Design: brand story hero module (mobile-first). Dev: use Intelligems or Shopify customer tag to detect new vs. returning. New visitor = no cookie or first session. Returning = has cookie or has placed an order. Copy needs client approval on brand voice and press logos.

**V2:** V1 plus, for new visitors, add a customer testimonial strip below the hero with 2-3 short review quotes and star ratings. This stacks trust-building elements for first-time visitors. Returning visitors still see the default homepage. On mobile, testimonials appear as a horizontal scroll strip. On desktop, inline row of 3 quotes.
**Brief:** Design: testimonial strip component. Dev: pull top-rated site reviews from Yotpo. Same new visitor targeting as V1.

**V3:** V1 for new visitors, plus a separate treatment for returning visitors: replace the hero with a "New This Month" module showing April launches (Knits, Sleep & Tabletop, Foggy Dog collab) as shoppable tiles. This serves both segments with tailored content. On mobile, tiles stack vertically. On desktop, 3-4 tile grid.
**Brief:** Design: "New This Month" tile grid (mobile-first). Dev: CMS-editable tiles so the team can update launches without dev work. Combine new visitor logic from V1 with returning visitor detection. Two distinct hero experiences.

**V4:** V3 plus, for returning visitors, add a "Picked for You" personalized product row below the "New This Month" module. Products selected based on browsing history or past purchase category (e.g., if they bought Eco Satin, show new Eco Satin prints; if they bought cotton, show cotton). On mobile, horizontal scroll row. On desktop, 4-product inline row.
**Brief:** Design: personalized product row component. Dev: use Shopify customer data or browsing cookies to populate recommendations. Fallback to "Best Sellers" if no browsing data available. This is the most complex variation and may require Intelligems or Nosto integration for recommendation logic.

**Sequencing note:** No homepage tests running. This test can launch at the start of April.

---

## Slot 3: Spring Collection Above-the-Fold Optimization

**Type:** A/B test (4 variations vs. control)
**Page:** Collection page /collections/spring-pajamas-apparel ([https://www.printfresh.com/collections/spring-pajamas-apparel](https://www.printfresh.com/collections/spring-pajamas-apparel))
**Revenue potential:** 69,224 sessions/mo x 0.3% CR lift x $193 AOV = ~$40,082/mo

**Hypothesis:** If we optimize the above-the-fold experience on the spring collection page with a campaign hero and structured entry points, conversion rate will increase because this page grew +256% in the last 30 days, is now the #3 landing page, and currently opens with a generic "Women's Pajamas" header that doesn't match the spring/seasonal intent driving visitors here.

**Data:** /collections/spring-pajamas-apparel drove 69,224 sessions in the last 30 days, up 256% from the prior period (Source: Shopify Analytics). The collection page scrollmap shows most users only see the first 2-3 rows of products (Source: Heatmaps). The current page opens with "Women's Pajamas / Shop Organic Cotton Pajamas & Cute Sleepwear for Women" and print portal tiles (Dreamy Daffodil, Rabbit Wonderland) before the filter bar (Source: Site Screenshots). The collection page hero + reviews + urgency case study generated +$114,870/mo by adding a lifestyle hero, review counts, and scarcity labels (Source: Winning Tests Library). The collection page print portals case study generated +$59,975/mo with print-based navigation (Source: Winning Tests Library). April launches Knits (Apr 2), Sleep & Tabletop (Apr 7), and Apparel (Apr 14), all feeding into this collection.

**V1:** Replace the generic "Women's Pajamas" header with a seasonal campaign hero: "Spring Collection" headline, one-line subtext tied to the April theme, and a lifestyle image. Keep print portal tiles and filter bar below the hero. On mobile, hero is full-width above the print portals. On desktop, hero spans full width with text overlay on the image.
**Brief:** Design: seasonal hero module (mobile-first). Image from spring campaign assets. Dev: replace the H1 header and subtext on this specific collection template. Print portals and filter bar remain unchanged below.

**V2:** V1 plus add fabric type quick-filter chips above the existing filter bar. Chips: "Eco Satin," "Organic Cotton," "Knits" (after Apr 2 launch). Tapping a chip filters the collection to that fabric. This is additive, not a structural change to existing filters. On mobile, horizontal scroll chips. On desktop, inline chip row.
**Brief:** Design: chip component with fabric name labels. Dev: filter chips trigger the existing Fabric filter value. Start with 3 fabric types. If Knits aren't tagged yet, coordinate with the team to tag them before Apr 2. This is distinct from PF25 (grid layout) as it modifies the filter zone, not the product grid.

**V3:** V2 plus add review count and "Selling Fast" labels to the first row of products. Review count appears below product name (e.g., "4.7 ★ 78 Reviews"). "Selling Fast" badge on products with high velocity. Only first row to keep the test targeted. On mobile, badges and counts appear on the 2-column grid cards. On desktop, same placement on 3-column grid cards.
**Brief:** Design: review count and badge styles for product cards. Dev: pull review count from Yotpo. "Selling Fast" logic based on sales velocity threshold (e.g., top 20% by units sold in last 7 days). Apply only to first product row to isolate the variable.

**V4:** V3 plus add a "New: Knits" promotional banner between the second and third product rows. The banner highlights the Luna Jersey launch with a lifestyle image, one-line description ("Our softest fabric yet"), and a "Shop Knits" CTA linking to the Knits collection. On mobile, the banner is full-width between product rows. On desktop, same placement, spanning the full grid width.
**Brief:** Design: mid-grid promotional banner (mobile-first). Dev: inject between product row 2 and 3 on this collection template. CMS-editable so the team can swap to future launches. Time this variation's launch to Apr 2 or after, so the Knits collection exists.

**Sequencing note:** PF25 (3x collection grid) will conclude before April tests launch. If PF25 wins, apply the winning grid layout to this page's control before running this test.

---

## Slot 4: Bagheera Collection Gifting Landing Page

**Type:** A/B test (4 variations vs. control)
**Page:** Collection page /collections/bagheera ([https://www.printfresh.com/collections/bagheera](https://www.printfresh.com/collections/bagheera))
**Revenue potential:** 52,050 sessions/mo x 0.3% CR lift x $193 AOV = ~$30,137/mo

**Hypothesis:** If we add gifting context and curated entry points to the Bagheera collection page, conversion rate on paid traffic will increase because the top Bagheera ad sells it as "the silky-soft gift they'll love unwrapping" but the landing page has no gifting context, no fabric story, and no curation across a massive product grid.

**Data:** /collections/bagheera drove 52,050 sessions in the last 30 days, with significant traffic from the Bagheera Meta ad (one of the top 3 best-performing ads out of hundreds of active campaigns), running since Dec 4, 2025 (Source: Shopify Analytics, Meta Ads). The ad copy promises "the silky-soft gift they'll love unwrapping" and positions the product as "Luxury Loungewear," but the landing page is an undifferentiated grid of dozens of products across multiple Bagheera colorways with no gifting context, no fabric story, and no curation above the fold (Source: Meta Ads, Site Screenshots). Reviews mention gifts or gifting 94 times in the last 30 days (Source: Reviews). April's content calendar theme is "Mother's Day Focus" and "Giftableness" (Source: Content Calendar). "Why Choose Printfresh?" module exists mid-page but is buried below many products (Source: Site Screenshots). The client has specifically requested more landing page tests (Source: Non-Data Context).

**V1:** Add a "Give the Gift of Great Sleep" hero section above the product grid. One lifestyle image (gifting-themed: wrapped box, someone unwrapping pajamas, or pajamas styled as a gift), headline ("The Gift They'll Actually Wear"), one-line subtext about Eco Satin fabric. Products remain immediately below. On mobile, hero is full-width, compact enough to not push products below the first fold. On desktop, split layout with image left and copy right.
**Brief:** Design: gifting hero module (mobile-first). Source gifting-themed lifestyle image from existing assets or request from client. Copy needs client approval. Dev: inject above the product grid on /collections/bagheera template only.

**V2:** V1 plus add a curated "Gift Sets" row below the hero: 3-4 pre-selected best-selling Bagheera products (Soho Set, Robe, Nightgown) styled as "Top Gifts." Each card shows product image, name, price, and star rating. This gives gift-givers a shortcut instead of scrolling a massive grid. On mobile, horizontal scroll row. On desktop, inline 3-4 product row.
**Brief:** Design: curated product row with "Top Gifts" label. Dev: manually curated product IDs (editable via metafield or CMS). This row is separate from the main product grid.

**V3:** V2 plus add a fabric micro-story strip between the curated row and the main product grid. One line about Eco Satin ("Thermoregulating. Machine washable. Sustainably sourced.") with 3 icons. This addresses the message match gap: the ad says "silky-soft" but the page says nothing about the fabric. On mobile, full-width strip. On desktop, same.
**Brief:** Design: fabric strip component (reusable across collection pages). Dev: render between curated row and product grid.

**V4:** V3 plus add a "Mother's Day Gifting" banner at the top of the page (above the hero), with a countdown or date reference ("Mother's Day is May 11. Free gift wrapping included.") and a link to gift wrapping options. This creates urgency and ties the page to the seasonal moment. On mobile, slim banner above hero. On desktop, same.
**Brief:** Design: seasonal banner component (slim, dismissible). Dev: time-gated to display from April 1 through May 11. CMS-editable so the team can update copy without dev work. After Mother's Day, the banner auto-hides and the test continues with V3 elements only.

**Sequencing note:** No sequencing conflicts. PF25 will conclude before April. This page receives consistent paid traffic, making it a stable testing environment.

---

## Future Slot Candidates

Ideas with strong data support that didn't fit into April's 4 slots:

1. **Cart Drawer Value Reinforcement:** The cart already has a free shipping progress bar, but no "You save $X" line on discounted items, no fabric micro-badges per item, and no trust signals. Cart drawer tests win 3/3 historically. Once PF16 (shipping price) and PF22 (shipping threshold) results are in, apply winners to the baseline, then test value reinforcement on top.
2. **PDP "Shop the Print" Cross-Sell:** If Slot 1 V4 wins, expand the "Shop More in This Print" row as a standalone test on all PDPs. D&D does this to great effect. Site search data (41K searches dominated by print names) confirms print-based navigation is the #1 discovery method.
3. **Knits Launch Dedicated Landing Page:** If the Knits launch on April 2 gets significant marketing support, build a dedicated LP with fabric education for Luna Jersey. This prevents the "Eco Satin sounds sus" problem from repeating with a new fabric name.
4. **MacKenzie-Childs Collection Message Match:** March Test #1 concept. The ad sells exclusivity and craftsmanship, the LP is a product grid. Story still buried below products. 43,454 sessions. Defer if the Bagheera LP test (Slot 4) provides learnings that can be applied here.
5. **Mobile Collection Print Navigation:** March Test #3 concept (horizontal print chip row). Print portals now exist on /collections/pajamas, which is a partial implementation. Test a more visual, D&D-style approach on mobile.
6. **Size Guide Accessibility Fix:** Multiple survey respondents can't find the size guide ("had to google search for it," "The feature asking what size you normally wear isn't very helpful"). This may be a UX fix rather than an A/B test. Also: "mckenzie" + "mckenzie childs" returning zero search results is a search config fix, not a test.

---

## Open Questions for Client

**Content calendar testing:** April has several major launches and promos (Knits Launch Apr 2, National Pajama Day promo Apr 16, Foggy Dog collab Apr 16, Mother's Day Catalog Apr 13). Are we planning to test anything around these, such as dedicated landing pages, promo-specific messaging, or launch-day experiments?

**Client-actionable items from data (not A/B tests):**
These came from surveys and reviews and may warrant investigation or fixes outside the testing roadmap:

- **Wildest Dreams sizing audit:** Some sets have reportedly been updated to true-to-size, but older reviews still say "runs big." If the fit has changed, the "sizing down is recommended" copy on those product pages may now be incorrect and causing wrong-size orders. Worth auditing which SKUs have been updated.
- **Discount code flow:** 5% of survey respondents reported broken or missing discount codes ("$20 off did not work," "Didn't receive discount code after signing up"). Worth checking the signup-to-code delivery flow.
- **Intermittent checkout bug:** A customer reported "checkout button failed to load on mobile and desktop." Worth checking with dev if there are known intermittent issues.
- **Search config fix:** "mckenzie" + "mckenzie childs" = 58 zero-result searches in the last 30 days. These customers are looking for the MacKenzie-Childs collection (43,454 sessions, 2 of the top 3 ads). Adding synonym mappings to site search would fix this immediately.
- **Monogram UX on pocketed items:** "Sewn pockets with monogram" mentioned twice in surveys. The monogram placement on pocketed items may not be clear in the customization flow.
- **Separate pieces demand:** Multiple customers want to buy tops or bottoms individually, not as sets. Could be a product strategy consideration.

