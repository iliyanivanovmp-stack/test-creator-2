# Ashley Stewart CRO Research Brief

**Data Sources:** Meta Ads, Google Ads, Reviews & UGC, Page Speed, Competitor Research, Site Screenshots

---

## Insights

Ashley Stewart has a genuine asset problem hiding inside a traffic problem. The brand gets ~600K monthly visits (SimilarWeb, March 2026), 72% of which arrive directly, and those visitors spend over 5 minutes browsing an average of 7 pages per session. Engagement is not the issue. The issue is that the purchase path is leaking at every stage.

The clearest leak: Ashley Stewart is spending heavily on Google Ads to drive product-specific traffic, then landing those visitors on a mismatched homepage. An eyeliner ad and a face gems ad (both running since November 2025, still active) both land on a homepage showing dresses at $24.99+. That homepage variant URL loads with a 10.4-second Speed Index and a Performance score of 30/100 on mobile. The brand's only ad with a dedicated landing page is Bridal, which performs better because the product, copy, and landing page all match. The fix is already in the playbook. It just hasn't been applied across the account.

The cart compounds the problem. "Enter your promo code at checkout" appears in pink text inside the cart, actively pushing buyers out of the purchase flow to search for discount codes. The primary checkout button includes a pre-opted-in SavedBy package protection fee, with opt-out as the secondary action. There are no reviews, no trust signals, and no free shipping threshold visible in the cart. Industry average cart abandonment is 77% in 2025. Ashley Stewart's cart is set up to beat that number.

Reviews are the third signal. Ashley Stewart holds 4.4 to 4.5 star ratings cited across multiple Google Ads creatives, representing thousands of reviews. None of that social proof appears on collection page product tiles, in the cart, or in the homepage's first three folds. Meanwhile, the most recent reviews (2025-2026) cite quality decline, return policy friction (double shipping charge on returns), and delivery failures with third-party carrier Veho. The brand is sitting on real social equity from loyal customers who love the intimates, the in-store experience, and the sale pricing. That equity is not being deployed where it would move purchases.

If Ashley Stewart improved cart conversion by 2 percentage points across an estimated 48,000 monthly cart sessions at a $45 average order value, that is $43,200 in additional monthly revenue with zero additional ad spend. That math gets more compelling when you add a landing page that stops wasting paid clicks.

---

## Slot 1: Cart - Remove the Promo Code Leak

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (mobile and desktop): ashleystewart.com (cart)
**Revenue potential:** ~600K sessions/mo x estimated 8% ATC rate = ~48,000 cart sessions/mo x conservative 2% CR lift x $45 AOV = ~$43,200/mo. Actual numbers depend on internal ATC rate and AOV data.

**Hypothesis:** If we remove the promo code link from the cart view and replace it with a social proof and free shipping threshold element, more visitors will complete checkout because we eliminate the most common cart abandonment trigger (leaving to hunt for codes) and reduce purchase anxiety.

**Data:** The cart currently shows "Enter your promo code at checkout" in pink hyperlink text, visible to every buyer before they hit checkout (Source: Site Screenshots). This link actively signals that a discount code might exist, prompting buyers to pause and search for one. Industry data shows visible promo code fields are a leading cause of cart abandonment (Bizrate Insights/Digital Commerce 360, Oct 2023). Ashley Stewart holds 4.4 to 4.5 star ratings across thousands of reviews cited in its own Google Ads, but none of this social proof appears in the cart (Source: Google Ads, Site Screenshots). The CRO Ebook cites cart as the single highest-impact test area and specifically recommends adding social proof and removing distractions (Source: CRO Ebook). The SavedBy package protection fee ($0.97) is pre-opted-in, making the primary checkout CTA read "CHECKOUT+ • $10.97" rather than the item total, which creates confusion at the most critical moment. Reviews show return policy anxiety is a pre-purchase concern: customers explicitly cite the double shipping charge ($10 return label + $9.95 shipping fee) as a reason they hesitate to order online (Source: Reviews).

**V1:** The variation makes four changes to the cart drawer.

First, remove the "Enter your promo code at checkout" pink link from the cart view entirely. Move promo code entry to the checkout page (standard practice), where it is available but not surfaced as a temptation to leave.

Second, change the SavedBy opt-in logic so it is off by default. The primary checkout CTA reads "CHECKOUT • [item total]" with no added fee. SavedBy becomes an opt-in via a checkbox below the order summary ("Add Package Protection for $0.97"), not a pre-selected surcharge.

Third, add a single high-impact customer review directly above the checkout CTA. One review with star rating, first name, and 1-2 sentence quote. Pull from the intimates category where reviews are strongest: "The panties are exquisite because there is no sagging anywhereeeeeeee. The bra really makes the clothes I wear look so much better." Rotate from top-rated verified reviews.

Fourth, add a free shipping progress bar below the subtotal. Example: "You're $15 away from free shipping." Set at whatever threshold Ashley Stewart currently uses or is willing to test. If no free shipping threshold exists, test introducing one at $65 (in line with Lane Bryant's $75 for Rewards members and industry benchmarks).

On mobile: The four changes apply identically. The review block stacks above the checkout CTA. The free shipping bar appears directly below the subtotal line. The SavedBy checkbox is visible without scrolling on most modern phones.

On desktop: Same layout changes. The review block sits in a single row above the CTA. The SavedBy checkbox is inline with a brief explanation.

The credit card "Learn More" widget stays in place for this test to isolate the impact of the four changes above. It can be addressed in a future slot.

---

## Slot 2: Ad Landing Pages - Dedicated Page for Non-Bridal Product Ads

**Type:** A/B test (1 variation vs. control)
**Page:** Paid ad landing page. Control: ashleystewart.com/?variant=[product_id] (current homepage variant URL). Variation: new dedicated landing page per ad campaign. Test by duplicating the ad set in Meta and/or Google and pointing one set to the variation, one to the control.
**Revenue potential:** Paid search represents 39.14% of Ashley Stewart's search traffic (SimilarWeb, March 2026). Combined with Meta paid campaigns, paid traffic to the homepage is a significant portion of total sessions. Dedicated landing pages in apparel have been shown to convert 2-5x higher than generic homepages. Even a 20% improvement in paid traffic conversion rate is a material reduction in cost per acquisition given the brand's heavy Google Ads investment.

**Hypothesis:** If we send product-specific paid ad traffic to a dedicated landing page that matches the ad's product, offer, and messaging, conversion rate from paid traffic will increase because the visitor lands on what they clicked for instead of a generic homepage that does not feature the advertised product.

**Data:** Two of three Meta ads analyzed (eyeliner and face gems, both running since November 2025) send traffic to the homepage, which shows dresses at $24.99+ and has no featured placement for the advertised products (Source: Meta Ads, Site Screenshots). The landing page variant URL used by these ads scores 30/100 on mobile performance with a Speed Index of 10.4 seconds and a network payload of 6,512 KB, which is 2.5x larger than the standard homepage and 3x worse on main thread blocking (TBT 6,140ms vs. 1,940ms) (Source: Page Speed). Google Shopping and display ads also show product-specific creatives (face gems, Ariana Grande fragrance, individual clothing items) that almost certainly face the same landing page mismatch (Source: Google Ads). The Bridal ad is the only campaign with a dedicated landing page, and it is the only ad with clear message match between creative, copy, and destination (Source: Meta Ads, Site Screenshots). The CRO Ebook states: "If paid advertising is a major source of new customers for your brand, then Landing Pages are your number one priority for split tests" (Source: CRO Ebook).

**V1:** Build one dedicated landing page template and apply it to the eyeliner and face gems ad campaigns as the starting test. The same template can then be replicated across other product-specific campaigns.

The landing page structure:

Above the fold: Announcement bar matching the ad offer (or removed if no specific offer). Hero image pulled directly from the ad creative, showing the specific product. Headline mirrors the ad headline (e.g., "Plus Size 2-In-1 Magnetic Liquid Eyeliner"). Sub-headline adds a benefit or proof point ("Precision application, all-day hold"). Single CTA: "Shop Now" linking directly to the product or its category page, not the homepage.

Fold 2: Three product benefit bullets. Product image carousel showing the item in use or styled. Price displayed clearly with any active discount.

Fold 3: 2-3 customer reviews specific to the product or accessory category. Star rating. Return/shipping policy summary in one line (e.g., "30-day returns. Free shipping on orders over $65.").

No navigation menu on this page, or navigation collapsed to logo-only. Removing nav prevents visitors from wandering to dresses when the ad brought them for accessories. This is standard for paid landing pages and is what the Bridal page currently does (it retains full nav, which is a future optimization).

On mobile: Single-column layout. Hero image full-width. Benefit bullets in a stacked list. Reviews as cards that scroll horizontally. CTA sticky at the bottom of the screen (fixed position).

On desktop: Two-column layout above the fold: product image left, headline/CTA/bullets right. Reviews in a horizontal row below. Return/shipping line in footer of the page content.

Loading performance: Do not use the variant URL parameter (?variant=44831756451884) as the destination URL. The variant URL increases payload to 6,512 KB and TBT to 6,140ms. The dedicated landing page, built as a clean Shopify page without that parameter, will load significantly faster and is likely to improve Quality Score in Google Ads, reducing cost per click.

---

## Slot 3: Collection Page - Add Star Ratings to Product Tiles

**Type:** A/B test (1 variation vs. control)
**Page:** Collection pages sitewide, starting with the highest-traffic collection (Clothing, Dresses, or whichever has the most sessions per internal analytics). ashleystewart.com/collections/clothing and related.
**Revenue potential:** Visitors browse an average of 7.17 pages per session and stay 5m 15s (SimilarWeb, March 2026), indicating high collection page engagement. A 7% conversion rate lift on collection pages from adding star ratings (documented for a UK fast-fashion brand, 2024) on an estimated 200K collection page sessions/mo at a conservative 1.5% baseline CR and $45 AOV = approximately $9,450/mo. The actual lift depends on current collection page CR from internal data.

**Hypothesis:** If we surface average star ratings and review counts on product tiles in collection pages, add-to-cart rate will increase because shoppers can identify high-rated products without visiting individual PDPs, reducing the friction of evaluating trust mid-browse.

**Data:** No star ratings appear on product tiles across the collection pages visible in screenshots (Source: Site Screenshots). Ashley Stewart holds 4.4 to 4.5 star ratings across 9,575 to 13,388 reviews, as shown in its own Google Ads (Source: Google Ads). This social proof exists but is not deployed in the purchase path. Torrid, Ashley Stewart's largest direct competitor by traffic (~7.3M monthly visits vs. Ashley Stewart's ~600K), surfaces ratings on product tiles (Source: Competitor Research). Lane Bryant provides category-level fit guides and ratings on its collection pages (Source: Competitor Research). Displaying customer ratings alongside product images lifted conversion by 7% for a UK fast-fashion brand (industry data, 2024). Visitors who browse 7+ pages per session (as Ashley Stewart visitors do) are actively comparing products: ratings give them a decision-making shortcut that reduces browse time and increases add-to-cart confidence (Source: CRO Community Research). The CRO Ebook recommends ordering product tiles by Revenue Per Session as a "stupidly simple way to optimize Collections Pages" (Source: CRO Ebook). This test pairs naturally with that approach.

**V1:** Add a star rating display (average stars + review count) to every product tile in the collection page grid.

Placement: Below the product name, above the price. Example layout per tile: [Product Name] / [4.5 ★ (127)] / [$69.50 $29.99] / [50% Off].

Show rating only for products with 5 or more reviews. For products with fewer than 5 reviews, show nothing in that slot rather than a thin-sample score.

Style: Use the brand's existing pink/teal color palette. Star icons in the brand's pink (#C35C8E or nearest match). Review count in gray text to avoid visual noise.

On mobile: The rating line stacks below the product name in the same tile layout. Given mobile tiles display at approximately 50% screen width in 2-column view, the star rating should be small (12px) to avoid overcrowding. Test both 2-column and 3-column mobile grid layouts to confirm readability.

On desktop: The tile has more horizontal space. Display stars inline with the review count. No change to tile width or grid structure.

Do not add product badges or other changes in this variation. This test isolates the impact of ratings only. Bestseller badges, "New" labels, and tile reordering by RPS are separate follow-on tests.

---

## Future Slot Candidates

- **Homepage hero simplification:** The current homepage has three competing promotions (rotating announcement bar, hero banner, 50% off full-width banner) in the first two folds, plus an immediate popup. Test a single-message hero with one CTA and one offer.
- **Return policy confidence on PDP:** Reviews show the double shipping charge on returns ($10 label + $9.95 fee) is a purchase barrier. Test a one-line return policy callout near the add-to-cart button on PDP: "Easy 30-day returns. Free return label included." This would require a policy change to enable the copy. Coordinate with the client before writing the variation.
- **PDP sizing guidance:** Multiple reviews cite sizing inconsistency across styles. A fit note on individual PDPs ("This style runs 1 size small. We recommend sizing up.") has been shown to reduce returns 21% and improve checkout completion 10% (Immerss, 2025).
- **Intimates category page:** Ashley Stewart's most-loved product category (per reviews) with dedicated Google and Meta ad spend (lingerie ad copy is the strongest in the account). Test a dedicated intimates landing page with social proof and fit guide integration.
- **Bridal landing page optimization:** The Bridal ad has the best message match of the campaigns analyzed. The announcement bar ("40% Off New Arrivals") interrupts the premium bridal experience. Test removing the announcement bar from the bridal page for paid traffic sessions.
