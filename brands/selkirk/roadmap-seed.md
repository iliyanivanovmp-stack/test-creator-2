# Selkirk Sport Roadmap Seed

**Store:** selkirk.com
**AOV:** unknown
**Monthly sessions:** unknown
**Data sources:** Meta Ads and Landing Pages, Google Ads Transparency, Reviews & UGC, PageSpeed / Core Web Vitals, Non-Data Context, Current Site Screenshots, Social & Community Research (last30days-ecom)

## Key Insights

The homepage's single hero CTA ("Buy Now") routes to a 3-SKU, bags-only collection page with zero paddles — confirmed by both the client's own flag and independent screenshot capture of the collection page. Paddles are Selkirk's core product, but a visitor must scroll past two full homepage folds to reach a paddle-specific entry point. This is the highest-confidence, highest-funnel-position finding in the audit.

Paid traffic shows three message-match failures on Meta. Ad 1 promises "deals" and "markdowns" but its landing page shows full price with no discount shown. Ad 2 shows "$130.00" and a "Shop Now" CTA, but the landing page lists "$100.99" and the buy button is disabled ("Out of stock"). Ad 3 leads with a 5-star testimonial about paddle quality to sell a $7 towel, whose own landing page shows a 2-star "I do not recommend this product" review directly below the fold.

Mobile performance is severely degraded: homepage LCP 12.0s, PDP (Boomstik) LCP 9.9s (Lighthouse mobile, 2026-09-10) — roughly 4-5x Google's 2.5s "good" threshold. Reviews (client-supplied, SLK Neo set) skew beginner/value: "excellent value... made the game much more enjoyable," though one reviewer called the entry tier "low par" material to replace "once these fall apart." Social listening corroborates paddle durability via TikTok and Amazon ratings, and surfaces warranty/exchange friction from two independent sources: Trustpilot claims-process complaints and the official Boomstik PDP's own "Exchanges are unavailable" copy.

No sessions/mo or AOV figures exist in any collected source, so dollar lift estimates below are omitted rather than invented.

## Top Test Opportunities

### 1. Homepage Hero CTA Routes to Bags, Not Paddles
**What's broken:** The homepage hero is a full-width image of three bags, headline "THESE BAGS KNOW BALL / PRO LINE 2.0 BAG SERIES," single "Buy Now" button. It routes to the Pro Line 2.0 Bags collection: exactly 3 SKUs (Tour Backpack $298, Team Backpack $248, Duffle $198) — paddles appear nowhere on it.
**Evidence:** context.md (client-flagged), site-visual-summary (homepage fold 1, collection fold 2)
**Key data:** Collection page confirmed 3 SKUs, all bags, no paddles.

### 2. Out-of-Stock Buy Box Behind "Shop Now" Ad
**What's broken:** Meta Ad 2 (Vanguard Power Air - S2) shows "$130.00" with a "Shop Now" CTA implying live purchase. Its landing page lists "$100.99," and the primary buy button is disabled, reading "Out of stock," with only "Notify me when back in stock" active.
**Evidence:** meta-ads-visual-summary (Ad 2)
**Key data:** Price mismatch $130.00 (ad) vs. $100.99 (LP); CTA disabled on LP.

### 3. "Deals" Ad Copy With No Visible Discount on LP
**What's broken:** Meta Ad 1 (AMPED Pro Air - Epic) headline reads "Deals on select Selkirk paddles... Limited quantities, so don't sleep on it." Its landing page shows the paddle at $100 flat with a "Free Gift With Purchase" badge — no strikethrough price, sale badge, or discount code visible.
**Evidence:** meta-ads-visual-summary (Ad 1)
**Key data:** Full price $100 shown, zero discount indicators.

### 4. Mobile LCP 9.9-12.0s Across Homepage and PDP
**What's broken:** Lighthouse mobile shows homepage LCP 12.0s (TTI 12.6s, Performance 64/100) and Boomstik PDP LCP 9.9s (TTI 13.5s, Performance 63/100). Both pass on CLS (0) but fail badly on load speed.
**Evidence:** pagespeed.md (homepage + PDP, 2026-09-10)
**Key data:** LCP 12.0s (home) / 9.9s (PDP) vs. 2.5s "good" threshold.

### 5. Mismatched Testimonial-to-Product Ad Pairing
**What's broken:** Meta Ad 3 opens with a 5-star testimonial about paddle quality and service to promote a $7 grip towel. The towel's own PDP shows, directly below the fold, a 2-star "Not great" review ("I do not recommend this product") and a 3-star durability complaint, both visible within one scroll from the ad.
**Evidence:** meta-ads-visual-summary (Ad 3)
**Key data:** First visible LP reviews are 2-star and 3-star, against a 5-star ad framing.

### 6. Cart Shipping-Delay Warning With No Offsetting Trust Signal
**What's broken:** The cart drawer opens with a red banner: "Some items in your cart have a shipping delay & will delay your entire order. Please place two separate orders if you would like your other items sooner." No guarantee, returns copy, or trust badge appears elsewhere in the drawer.
**Evidence:** site-visual-summary (cart)
**Key data:** Warning banner is the only trust-relevant copy visible in the drawer.

### 7. "Ships in 2-3 Weeks" Friction on Flagship $333 Paddle
**What's broken:** The Boomstik PDP shows a red "Ships in 2-3 weeks" note directly above the Add to Cart button, on the product receiving the heaviest Google Ads emphasis (Boomstik-focused search/Shopping ads).
**Evidence:** site-visual-summary (PDP), google-ads-visual-summary (Boomstik emphasis)
**Key data:** $333 price point paired with a 2-3 week shipping delay note pre-purchase.

### 8. Individual Quick-Adds Instead of One Bundle CTA
**What's broken:** Both the AMPED Pro Air and Boomstik PDPs show a 4-item "Frequently Bought Together" row (paddle cover, glove, backpack/balls), each with its own "Quick Add" button rather than one combined "Add all to cart" action.
**Evidence:** meta-ads-visual-summary (Ad 1, Ad 2 LP folds), site-visual-summary (PDP fold 3)
**Key data:** 4 separate Quick Add buttons observed per PDP.

## Unused Findings

- No review count or star rating appears anywhere on the homepage, despite PDPs showing 623-2,664 reviews and a 4.7-star aggregate.
- Two independent sources (Trustpilot claims-process complaints, official Boomstik PDP copy "Exchanges are unavailable") point at unresolved warranty/exchange friction not addressed on-site.
