# March 2026 Testing Roadmap

**Data Sources:** Trustpilot Reviews, Site Testimonials, Competitor Research, Winning Tests Library, Site Screenshots (desktop + mobile). Shopify Analytics provided directional context only (new theme live for ~1 week).

## Insights

Performance Golf is transitioning from a Checkout Champ-powered direct response setup to a modern Shopify storefront. The old system was profitable because of one thing: long-form video upsells in the post-purchase flow. A customer buys a club, sees a video, and minutes in, a related product offer appears. That post-purchase mechanism is where the margin lives. Without it, the new Shopify store cannot match the economics of the old setup. Rebuilding this flow as a custom Shopify app is the first priority.

The second priority is trust. Across 35+ recent Trustpilot reviews, the same complaint repeats: customers buy a club and discover unwanted subscription charges on their card weeks later. "SCAM-SCAM-SCAM," wrote one buyer who explicitly declined a free trial but was enrolled anyway. "Tricking elderly people into committing to a monthly fee," wrote another. Six separate 1-star reviews in the last 30 days cite the same issue: unexpected billing, difficulty canceling, aggressive upselling after purchase.

This matters because Performance Golf's core audience is senior golfers aged 50-70+. This demographic is especially sensitive to trust signals. They need to feel safe before they buy. Right now, the cart drawer, the last touchpoint before checkout, offers zero reassurance: no guarantee mention, no social proof, no savings callout. Just a product, a price, and a checkout button surrounded by empty space.

The irony is that Performance Golf holds the strongest guarantee in the competitive set: 365 days, no questions asked. Competitors max out at 60 days (BombTech, Vertical Groove, Square Strike) or 30 days (Lag Shot). PG also has 800K+ clubs sold, 1M+ subscribers, and 3,700+ reviews on the 357 alone at a 4.8 average. These are powerful trust signals. They're completely absent from the cart drawer.

This is a new theme, which means we have a rare opportunity. We can build the profitability layer (post-purchase upsells) and the trust layer (cart drawer optimization) from the start. As traffic data accumulates over the next 4-6 weeks, we'll layer in additional tests targeting the homepage, collection page, and product pages.

---

## Slots 1 & 2: Post-Purchase Video Upsell App

**Type:** Custom Shopify app development (2 slots)

**Why this is the #1 priority:** Performance Golf's old ecommerce setup ran on Checkout Champ, a direct response platform built around post-purchase upsell flows. The profit model depended on long-form video upsells: after a customer completes a purchase, they see a video. At a specific timestamp, a product offer appears as an overlay. This is where the margin came from. The new Shopify store needs to replicate this mechanism to be profitable. Without it, the economics don't work.

**What we're building:** A custom Shopify app that integrates into the post-purchase page (the thank-you/order confirmation flow). The app plays a video and, at configured timestamps, displays a product upsell overlay. The customer can accept the offer (added to their existing order without re-entering payment) or dismiss it and continue watching. This mirrors the Checkout Champ flow that drove profitability on the old platform.

**Key requirements:**
- Video player embedded in the Shopify post-purchase page
- Timed product overlays that appear at specific points in the video
- One-click upsell acceptance (charges the existing payment method, no re-entry)
- Configurable: different videos and offers per product purchased
- Tracking: acceptance rate, revenue per upsell, video completion rate

**Success metrics:** Post-purchase upsell acceptance rate, incremental revenue per order, and comparison against the old Checkout Champ upsell performance once baseline data is available.

---

## Slot 3: Cart Drawer Trust + Savings

**Type:** A/B test (1 or 2 variations vs. control)
**Page:** Cart drawer (site-wide, appears on all pages)
**Revenue potential:** We've seen great results by adding savings visibility + trust signals to a cart drawer and adding upsells. The cart drawer is the last touchpoint before checkout for every buyer who uses the Shopify store. Even small lifts here compound across all products.

**Hypothesis:** If we add trust signals and savings visibility to the cart drawer, more shoppers who add to cart will complete checkout, because the current cart drawer is bare (no trust signals, no savings callout, no social proof) and Trustpilot reviews reveal that hidden charges and subscription fears are the #1 purchase barrier for this brand's audience.

**Data:** The cart drawer currently contains only: a free shipping bar, a product line item, an "Is this a gift?" accordion, and a checkout button, with large empty white space between the product and subtotal (Source: Site Screenshots, desktop + mobile). Trustpilot reviews show 6+ one-star reviews in the last 30 days citing unwanted subscription charges, hidden fees, and difficulty canceling. Linda HP: "SCAM-SCAM-SCAM." Mike C: "Tricking elderly people into committing to a monthly fee." Rose Saylor had to cancel her credit card (Source: Reviews). Site search confirms this anxiety: "login" is the #1 zero-result query, and "how do i cancel membership?" also appears (Source: Site Search). PG's 365-day guarantee is 6x longer than the competitive average of 60 days, yet it's completely absent from the cart drawer (Source: Competitor Research, Site Screenshots). The last line buyers see before checkout is "Shipping, taxes, and discount codes are calculated at checkout," which introduces uncertainty rather than reducing it (Source: Site Screenshots).

**V1:** Add three elements to the cart drawer: (1) A savings callout line below the product showing "You're saving $50!" (calculated from the compare-at price), (2) A trust signal strip below the product section with three icons in a row: "365-Day Guarantee," "Free Shipping," and "800K+ Clubs Sold," (3) Replace the "Shipping, taxes, and discount codes are calculated at checkout" text with "Free shipping included. 365-day money-back guarantee." Remove the "Is this a gift?" accordion (low-value feature consuming premium space).
**Brief:** Desktop: Savings callout appears in green text directly below the product's price line. Trust signal strip: three small icons with text labels in a horizontal row, centered, placed between the product section and subtotal. Use the same icon style as the PDP trust icons (circular outline icons). The "Is this a gift?" accordion is removed. The reassurance text replaces the existing shipping/tax disclaimer below the CHECK OUT button. Mobile: Identical layout. The trust strip icons scale to fit the narrower drawer width. If they don't fit in one row, stack as 2+1.

**V2:** Everything from V1, plus add a "Golfers Also Bought" upsell section with one complementary product recommendation. For example, if the cart contains the 357, suggest the 359 Super 9-Wood ("Complete your set"). If the cart contains the SF1 Driver, suggest the EZ7 hybrid. Show product image, name, sale price with strikethrough, and an "Add" button. Place this section between the cart item and the trust strip.
**Brief:** Desktop: "Golfers Also Bought" section shows one product card: small product image (left), product name + "Complete your set" tagline + sale price with strikethrough (center), "ADD" button (right). The recommendation logic: 357 suggests 359, SF1 suggests EZ7, ONE Wedge suggests ONE.S Wedge, default suggests 357 (bestseller). Mobile: Same layout but product image shrinks, and the ADD button moves below the product name/price to prevent horizontal cramping. Only show one upsell product to keep the drawer focused.

---

## Future Slot Candidates

The following tests are ready to run in upcoming months once baseline traffic data has accumulated on the new theme:

1. **Homepage Hero:** The homepage currently leads with the ONE.1 Wedge hero. The 357 Super 7-Wood is the flagship product (most reviewed at 3,700+, most advertised, most searched on-site). Swapping the hero to feature the 357 and surfacing trust signals (4.8 rating, 800K clubs sold) above the fold is the next high-impact test.

2. **Collection Page Trust + Navigation:** The Golf Clubs collection page has no reviews on product cards, no hero banner, and no urgency labels. Adding star ratings, a hero banner with trust signals, and "Best Seller" badges is a proven pattern (we've seen this win big in the past).

3. **357 PDP Gallery + Customer Voice:** The product gallery uses standard product shots with no text overlays or human context. Replacing the lead image with a text-overlay action shot and swapping brand-voice benefit bullets for customer-voice outcomes (specific numbers from reviews) would strengthen the top product page.
