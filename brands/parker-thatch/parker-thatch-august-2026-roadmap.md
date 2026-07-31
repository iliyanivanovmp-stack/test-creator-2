# Parker Thatch CRO Research Brief

**Data Sources:** Meta Ads (visual summary + landing page URLs + live fetches), PageSpeed / Core Web Vitals (July 31 2026), Site Screenshots (homepage, collection, PDP, cart drawer), Live site fetch (parkerthatch.com)

## Insights

Parker Thatch loses the promise of every active Meta ad at the landing page. All 3 active ads drop their primary hook on the PDP. XL Mimi loses both "BACK IN STOCK" and its Women's Wear Daily credential. Jane loses both "NEW ARRIVAL" and "As seen on Reese Witherspoon." Cross Your Heart Sling loses "NEW ARRIVAL." Source: Meta Ads and live PDP fetches.

The site then asks for a $598 to $728 purchase with little reassurance near the ADD TO CART button. The tested PDPs show only 4 to 15 reviews per product. They do not reinforce free shipping, summarize the 14-day return window, or surface a material or craftsmanship callout in the buy box. Source: Site Screenshots and live PDP fetches.

Mobile performance blocks the funnel before persuasion starts. On July 31, 2026, homepage LCP was 18.5 seconds, TBT was 2,160ms, and TTI was 34.2 seconds. PDP LCP was 9.7 seconds and TTI was 35.7 seconds. CLS was 0 on both pages, which isolates load weight and blocking work as the problem. Source: PageSpeed / Core Web Vitals.

The same friction continues across the journey. The homepage first fold has no headline or CTA. The collection grid has no star ratings and hides QUICK ADD behind desktop hover. The cart leaves a large empty area above checkout even though relevant $48 to $228 accessories already appear in PDP cross-sells. Source: Site Screenshots.

A portfolio-level revenue estimate is not defensible because monthly sessions and baseline conversion rates were not collected. The six test calculations below use the seed's conservative traffic and lift estimates. They should be replaced with analytics data before launch.

## Slot 1: Restore Mobile Page Usability

**Type:** Immediate Fix
**Page:** Homepage (https://parkerthatch.com/) and Product Detail Pages

**Why this is the priority:** On July 31, 2026, homepage TTI was 34.2 seconds and PDP TTI was 35.7 seconds. Visitors should not wait more than half a minute before the site responds.

**What to fix:** Prioritize the largest visible content, reduce render-blocking JavaScript, and remove unnecessary load work on mobile. Target LCP below 4.0 seconds first, then move toward Google's 2.5-second good threshold.

**Success metrics:**

- Mobile homepage and PDP LCP
- Mobile homepage and PDP TBT
- Mobile homepage and PDP TTI
- Mobile bounce rate and conversion rate after release

## Slot 2: Correct Nylon Product Ad Claims

**Type:** Immediate Fix
**Page:** Meta Ads 2 and 3

**Why this is the priority:** Ads 2 and 3 describe leather products, but both landing pages sell ballistic nylon bags. The factual conflict can break trust before the shopper evaluates the product.

**What to fix:** Replace "Soft Supple Leather" and "Real leather that gets better over time" with product-specific ballistic nylon copy for XL Mimi and Jane. Keep each ad's existing product, urgency, and credential hook unchanged.

**Success metrics:**

- Zero active ads with a material mismatch
- Material claims match the landing PDP for all 3 active ads

## Slot 3: Carry Ad Status Into the PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Pages for XL Mimi, Jane, and Cross Your Heart Sling
**Revenue potential:** 5,000 estimated sessions/month x 0.8 percentage-point CR lift x $698 AOV = $27,920/month.

**Hypothesis:** If we repeat each ad's product-status hook above the PDP title, conversion rate will increase because shoppers will immediately confirm that they reached the product and offer they clicked.

**Data:** All 3 active ads lose their primary status hook on landing. "BACK IN STOCK" is absent from XL Mimi, while "NEW ARRIVAL" is absent from Jane and Cross Your Heart Sling. Source: Meta Ads and live PDP fetches.

**V1:** Add a compact status label directly above the product title: "Back in Stock" on XL Mimi and "New Arrival" on Jane and Cross Your Heart Sling. On mobile, keep the label on one line above the title within the existing buy box. On desktop, use the same position and alignment. Keep the gallery, rating, swatches, price, and ADD TO CART button unchanged.

## Slot 4: Add a Buy Box Trust Line

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Pages
**Revenue potential:** 10,000 estimated sessions/month x 0.5 percentage-point CR lift x $680 AOV = $34,000/month.

**Hypothesis:** If we place shipping and return reassurance beside the purchase action and reduce competition from the secondary link, conversion rate will increase because shoppers can resolve purchase risk without leaving the buy box.

**Data:** The tested PDPs sell products from $598 to $728 with only 4 to 15 reviews per product. Free shipping appears only in the announcement bar, the 14-day return window is inside an accordion, and "DROP A HINT" competes below ADD TO CART. Source: Site Screenshots and live PDP fetches.

**V1:** Add "Free US ground shipping over $500 | 14-day returns on eligible items" directly below ADD TO CART, then restyle "DROP A HINT" as a smaller secondary text link below that line. On mobile, stack the reassurance line and secondary link with clear spacing. On desktop, keep both aligned to the buy box width. Keep the title, rating, swatches, price, and ADD TO CART treatment unchanged.

## Slot 5: Surface Press and Celebrity Proof

**Type:** A/B test (1 variation vs. control)
**Page:** XL Mimi and Jane Product Detail Pages
**Revenue potential:** 8,000 estimated sessions/month x 0.4 percentage-point CR lift x $700 AOV = $22,400/month.

**Hypothesis:** If we surface the documented press or celebrity credential beside the rating, conversion rate will increase because high-intent shoppers will see stronger proof at the decision point.

**Data:** XL Mimi's Meta ad carries a Women's Wear Daily Top 15 Bags 2023 badge, and Jane's ad says "As seen on Reese Witherspoon." Neither credential appears on its PDP. Source: Meta Ads and live PDP fetches.

**V1:** Add a compact credential strip directly below the existing star rating. Show "Women's Wear Daily Top 15 Bags 2023" on XL Mimi and "As seen on Reese Witherspoon" on Jane. On mobile, allow the strip to wrap to two lines without pushing ADD TO CART below the first buy box view. On desktop, keep it on one line within the buy box. Keep the existing rating, product title, gallery, swatches, and purchase controls unchanged.

## Slot 6: Give the Homepage Hero a Shopping Entry

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (https://parkerthatch.com/)
**Revenue potential:** 8,000 estimated sessions/month x 1.0 percentage-point CVR lift x $660 AOV = $52,800/month.

**Hypothesis:** If we add a clear value statement and shopping CTA to the first fold, homepage conversion rate will increase because visitors will understand the brand and have an immediate path to products.

**Data:** The first homepage fold contains two editorial images but no headline, product, price, or CTA. The first "SHOP NEW" link appears at the bottom of fold 2. Source: Site Screenshots and live homepage fetch.

**V1:** Overlay the existing brand line "Luxury meets utility, classic meets cool" and a prominent "Shop New" button on the current hero. On mobile, place the copy and button in a high-contrast block within the first viewport. On desktop, center the copy and button across the two-panel hero without covering the PT lion mark. Keep the existing hero images, announcement bar, navigation, and lower homepage sections unchanged.

## Slot 7: Add a Relevant Cart Accessory

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer
**Revenue potential:** 2,000 estimated cart sessions/month x $5.50 incremental revenue per cart session = $11,000/month.

**Hypothesis:** If we place one relevant accessory offer in the empty cart area, revenue per cart session will increase because shoppers can complete the look without leaving the cart.

**Data:** The cart drawer has a large empty area between the item row and checkout, with no cross-sell or upsell. Relevant straps, charms, and extenders from $48 to $228 already appear in "Complete The Look" and "You May Also Like" sections on PDPs. Source: Site Screenshots.

**V1:** Add one "Complete the Look" accessory card in the empty area above CHECKOUT, using an accessory already associated with the cart product in the PDP cross-sell. Include its image, name, price, and one-click ADD button. On mobile, show one full-width card without hiding CHECKOUT below unnecessary content. On desktop, use the same single-card treatment inside the drawer. Keep the free-shipping message, cart item row, and CHECKOUT button unchanged.

## Slot 8: Make Collection Cards Easier to Buy

**Type:** A/B test (1 variation vs. control)
**Page:** What's New Collection
**Revenue potential:** 6,000 estimated sessions/month x 0.205 percentage-point CVR lift x $650 AOV = $7,995/month.

**Hypothesis:** If we add product ratings and remove the mobile hover dependency from QUICK ADD, collection conversion rate will increase because shoppers can evaluate and add products directly from the grid.

**Data:** Collection cards show product name, price, and color count but no star ratings. QUICK ADD appears only on desktop hover, so it is not available in the default mobile state. Source: Site Screenshots.

**V1:** Add the existing product star rating and review count below each product name, and show QUICK ADD persistently below the card details on mobile. On desktop, add the rating in the same position and retain the current hover QUICK ADD behavior. Keep the three-column desktop grid, mobile card layout, product images, names, prices, and color counts unchanged.

## Future Slot Candidates

1. **Mimi heritage callout** - Test moving the documented 2009 origin story from the description accordion into the buy box after the higher-priority trust tests.
2. **Homepage CTA treatment** - Test changing the fold 2 "SHOP NEW" plain text link into a button if the first-fold hero entry test does not address the same traffic.
3. **Buy box CTA focus** - Test removing "DROP A HINT" after the trust-line test isolates whether the secondary action still dilutes ADD TO CART.
4. **Cart trust reassurance** - Test a concise shipping and returns line above checkout after the accessory offer establishes its effect on revenue per cart session.
