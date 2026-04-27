# April 2026 Testing Roadmap

**Data Sources:** Shopify Analytics, Fairing Surveys, Meta Ads (top performers), Google Ads Transparency, Amazon Reviews, Reddit Reviews, On-Site Reviews, Current Site Screenshots (Homepage, PDP, Cart Drawer)

## Insights

Doich Foods has a revenue problem hiding inside an AOV problem. The store converts at 2.31% on 177K sessions/mo, generating $115K in total sales with a $19.88 AOV. For a product with packs ranging from $24 to $45, that AOV tells us most customers are buying singles or small quantities. The root cause is visible in the data: on mobile (90.8% of traffic), the PDP defaults to Single ($7.99). The homepage flavor carousel also anchors to $7.99. Customers arrive through ads promising "Buy 3, Get 1 Free" and land on a page pre-selecting a single jar.

Subscription is almost nonexistent. Recharge generates $2K/mo, under 2% of online revenue. The subscription toggle is buried below the fold on the PDP, offering only 10% off. Meanwhile, the bundle deals already offer 25-37% implied discounts. There's no compelling reason to subscribe when the one-time bundle is cheaper per unit than the subscription single.

Reviews and Reddit paint a polarized picture. Customers who expect "cookie dough" are disappointed. Customers who frame Doich as a "protein snack" or "guilt-free treat" become repeat buyers. One Reddit commenter captured it perfectly: if you go in expecting a healthy snack, it's amazing; if you compare it to Nestle, you'll be let down. The PDP doesn't set this expectation. Trust is thin at the decision point: the cart drawer has zero trust signals, the PDP claims "thousands of 5-star reviews" but shows no review widget, and customers on Reddit actively check for scam indicators before buying.

Revenue opportunity: the PDP receives 106,779 sessions/mo. If we shift the default from Single ($7.99) to 4 Pack ($23.99) and increase the effective AOV from $19.88 to even $24, that's a $4.12 lift per order across ~4,100 monthly orders = **$16,892/mo in incremental revenue**. That's the conservative case. A stronger offer structure pushing toward the 6-pack could double that.

---

## Slot 1: PDP Offer Structure (Remove Single, Bundle-First Default)

**Type:** A/B test (2 variations vs. control)
**Page:** PDP (/products/doich-snacking-dough, 106,779 sessions/mo). All traffic from Meta ads lands here.
**Revenue potential:** 106,779 sessions x conservative 0.15% CR lift x $25 AOV = ~$4,000/mo. But the real lever is AOV: shifting from $19.88 to $24+ across 4,100 orders = $16,892+/mo.

**Hypothesis:** If we remove the Single option and default to the 4 Pack as the entry point, AOV will increase because customers can no longer anchor to $7.99, and the "Buy 3, Get 1 Free" message from ads will finally match the default selection on the page.

**Data:** AOV is $19.88 on a product where packs range from $24 to $45, meaning most customers buy singles or small quantities (Source: Shopify Analytics). The PDP defaults to Single ($7.99) on mobile, which represents 90.8% of traffic (Source: PDP Screenshots, Shopify Analytics). Every Meta ad leads with "Buy 3, Get 1 Free" but customers land on a page pre-selecting Single (Source: Meta Ads). The homepage flavor carousel also anchors to $7.99 per flavor (Source: Homepage Screenshots). Dr. Squatch saw a 54% revenue-per-purchaser increase by defaulting to 2-packs instead of singles (Source: SplitBase).

**V1: Remove Single option entirely.** The size selector shows only three tiles: 4 Pack (pre-selected, "Buy 3, Get 1 Free" in green text), 6 Pack ("Most Popular" badge, "Buy 4, Get 2 Free"), 8 Pack ("Best Value" badge, "Buy 5, Get 3 Free"). The quantity selector is removed. The 4 Pack becomes the default at $23.99, with ~~$31.96~~ struck-through to show the per-unit savings. On mobile, the three tiles stack in a 2x2 grid with the 4 Pack occupying the first position. On desktop, they display as a horizontal row. The flavor selector remains unchanged. The sticky bottom bar on mobile shows the 4 Pack price by default.

**V2: Remove Single option and add a subscription-only toggle.** Same layout as V1 (4 Pack, 6 Pack, 8 Pack only), but below the size selector, add a toggle: "One-time purchase" (default) vs. "Subscribe & Save 15%." When subscription is selected, all three pack prices update to show the subscription discount. The subscription option shows "Ships every 30 days. Skip or cancel anytime." in small text below the toggle. The 15% discount (vs. current 10%) makes subscription more competitive with bundle savings. On mobile, the toggle sits between the size selector and the ATC button. On desktop, it sits in the same position. No other changes to the page.

---

## Slot 2: PDP Offer Structure (Subscription-Only, No One-Time Purchase)

**Type:** A/B test (2 variations vs. control)
**Page:** PDP (/products/doich-snacking-dough, 106,779 sessions/mo)
**Revenue potential:** Subscription LTV is the real metric here. If even 20% of the 4,100 monthly orders convert to subscription at $21.59/mo (4-pack sub price), that's 820 recurring subscribers generating $17,703/mo in predictable revenue vs. the current $2K/mo from subscriptions.

**Hypothesis:** If we make subscription the only purchase option (removing one-time), subscription sign-ups will increase dramatically because the current 1.8% subscription rate suggests the option is invisible, not unwanted. However, this is a high-risk test: research shows one-time CTAs outperform subscription CTAs by 47% on first purchase (Source: Shoplift data). This test validates whether Doich's audience will accept subscription-only or if it kills conversion.

**Data:** Subscription revenue is $2K/mo, under 2% of online sales, despite a subscription option existing on the PDP (Source: Shopify Analytics). The subscription toggle is buried below the fold, offering only 10% off. This is less than the implied bundle discount of 25% on the 4-pack (Source: PDP Screenshots). 17.41% returning customer rate suggests the product has repeat-purchase potential, but customers aren't discovering or choosing subscription (Source: Shopify Analytics). The cart drawer shows subscription as a text line ("30 day subscription with 10% discount") with no benefit selling (Source: Cart Screenshots). Research shows making subscription benefits more visible drove +18% subscription RPV without removing one-time purchase (Source: Shoplift).

**V1: Subscription-only, keep Single option and quantity selector.** The current one-time/subscription toggle is replaced with a single "Subscribe & Save" framing. All pack sizes remain (Single, 4 Pack, 6 Pack, 8 Pack) with the quantity selector intact. Prices show subscription pricing only with 15% off each tier: Single $6.79/mo, 4 Pack $20.39/mo, 6 Pack $28.89/mo, 8 Pack $38.24/mo. Below each price: "Ships every 30 days." Above the ATC button: "Skip, swap flavors, or cancel anytime. No commitment." The ATC button text changes to "SUBSCRIBE NOW." On mobile, everything stays in the same position. On desktop, the subscription benefits text sits below the price. This variation tests whether keeping the Single + quantity selector in a subscription-only context still increases subscription uptake.

**V2: Subscription-only, remove Single option and quantity selector (maximum commitment).** Same as V1 but the Single option and quantity selector are both removed. Only 4 Pack, 6 Pack, and 8 Pack remain, all subscription-only. 4 Pack is pre-selected at $20.39/mo. This combines the bundle-first approach from Slot 1 with subscription-only. The "Skip, swap flavors, or cancel anytime. No commitment." messaging appears more prominently: directly below the size selector in a light green background box to reduce commitment anxiety. ATC button says "START MY SUBSCRIPTION." On mobile, the green reassurance box spans full width between the size tiles and the ATC button. On desktop, same layout.

**Sequencing note:** Slot 1 and Slot 2 both modify the PDP offer structure. They must run sequentially, not simultaneously. Run Slot 1 first (2 weeks minimum), analyze results, then run Slot 2. If Slot 1 V1 (remove Single, bundle-first) wins decisively, Slot 2 becomes even more interesting because it layers subscription onto the winning structure.

---

## Slot 3: PDP Trust & Value Framing (UI Improvements)

**Type:** A/B test (2 variations vs. control)
**Page:** PDP (/products/doich-snacking-dough, 106,779 sessions/mo)
**Revenue potential:** 106,779 sessions x 0.3% CR lift x $19.88 AOV = ~$6,370/mo. Trust signal improvements typically drive 5-15% relative CR lifts on pages with existing trust deficits.

**Hypothesis:** If we add trust signals and reframe the value proposition above the fold, conversion rate will increase because customers currently see a generic product title, a price, and no social proof or value context before deciding.

**Data:** Customers explicitly call the purchase decision risky. Survey: "Still don't see a picture of the nutrition label... That's sketchy" (Source: Surveys). Reddit: multiple users check Reddit for scam indicators before buying (Source: Reddit). Amazon: missing best-by dates, unclear baking instructions, misleading serving counts (Source: Amazon Reviews). The PDP says "Thousands of verified 5-star reviews" but shows no actual review widget, star rating, or review count in fold 1 (Source: PDP Screenshots). The cart drawer has zero trust signals (Source: Cart Screenshots). Checkout-to-purchase drop-off is 59% (Source: Shopify Analytics). Research shows reviews on product pages increase sales by up to 18%, and food brands face a higher first-purchase barrier since customers can't taste the product (Source: CRO research).

**V1: Add trust bar + review count above the fold.** Three changes, stacked. (1) Replace "Thousands of verified 5-star reviews." with a specific, clickable review count: "★★★★★ 5,240+ Reviews" in bold, linking to the reviews section below. Specific numbers outperform vague claims. (2) Below the trust badges (Low Sugar, No Artificial Junk, etc.), add a single-line guarantee bar: "60-Day Satisfaction Guarantee. Not your thing? Full refund." in a light gray background strip spanning full width. (3) Add a "What's Inside" expandable section directly below the product description showing the nutrition label image and ingredients list, addressing the "sketchy" nutrition complaint. On mobile, the review count sits where the current "Thousands of verified 5-star reviews" text is. The guarantee bar sits below the trust badges. The "What's Inside" accordion sits below "SPOON IT, BAKE IT, LIVE A LITTLE." On desktop, same vertical order.

**V2: V1 changes + expectation-setting copy.** Everything from V1, plus one additional change. Replace the current product description ("Meet THE official snacking dough...") with copy that sets the right expectation: "Not cookie dough. Better. A spoonable protein snack with 3x more protein, low sugar, and zero junk. Scoop it straight from the jar, toss it in your bag, or bake it into cookies. 6oz per jar, 8 scoops of guilt-free snacking." This directly addresses the expectation mismatch from reviews. On mobile and desktop, this replaces the existing description in the same position. No other layout changes beyond what V1 already includes.

**Sequencing note:** This test modifies the PDP content area but NOT the offer structure (size selector, pricing, subscription toggle). It can run simultaneously with Slot 1 or Slot 2 only if the changes don't overlap in the same page section. Safest approach: run this after Slot 1 completes, but before or alongside Slot 2 since Slot 2 modifies the buy box while this test modifies the content/trust areas above it.

---

## Slot 4: Cart Drawer Conversion Support

**Type:** A/B test (2 variations vs. control)
**Page:** Cart drawer (sitewide, triggered on all ATC clicks across 177,136 sessions/mo)
**Revenue potential:** 9,965 users reach checkout monthly but only 4,096 purchase (59% drop-off). If cart drawer improvements recover even 5% of abandoned checkouts: 293 additional orders x $19.88 = ~$5,825/mo.

**Hypothesis:** If we add trust signals and a free shipping progress bar to the cart drawer, checkout completion rate will increase because the current cart drawer does nothing to build confidence or incentivize higher spend at the last owned touchpoint before checkout.

**Data:** 59% of users who reach checkout don't complete the purchase (Source: Shopify Analytics). The cart drawer has zero trust signals: no guarantee, no reviews, no satisfaction promise (Source: Cart Screenshots). Free shipping threshold is $45 but the cart shows no progress toward it. A 4-pack at $21.59 is $23.41 away from free shipping with no visual indication (Source: Cart Screenshots). The "Earn Rewards" widget overlaps the checkout button on mobile (Source: Cart Screenshots, Mobile). Case study data shows stacking trust signals above checkout buttons drove +$32,605/mo for another brand (Source: CRO ebook).

**V1: Trust bar + free shipping progress bar.** Two changes. (1) Add a free shipping progress bar at the top of the cart drawer. Shows current cart total vs. $45 threshold with a visual fill bar. Text: "You're $X.XX away from FREE shipping!" When threshold is met: "You've unlocked FREE shipping!" in green. (2) Below the CHECK OUT button, add a single line: "★★★★★ 5,240+ Happy Customers | Satisfaction Guaranteed" in small gray text. On mobile, the progress bar sits at the very top of the cart drawer (above the product line item). The trust line sits directly below the CHECK OUT button. The "Earn Rewards" widget should be hidden or repositioned when the cart drawer is open to prevent overlap with the checkout button. On desktop, same layout.

**V2: V1 + bundle upsell prompt.** Everything from V1, plus one additional element. If the customer has added a Single or 4 Pack, show a contextual upsell bar between the product line item and the subtotal: "Upgrade to 6 Pack and save $X.XX per jar + get FREE shipping." The upsell includes a one-tap "Upgrade" button that swaps the cart item to the 6 Pack of the same flavor. If the customer already has a 6 Pack or 8 Pack, this element doesn't appear. On mobile, the upsell bar spans full width with the "Upgrade" button on the right. On desktop, same horizontal layout. The upsell bar uses a light yellow background to distinguish it from the rest of the cart.

**Sequencing note:** The cart drawer is a separate component from the PDP. This test can run simultaneously with any PDP test (Slots 1, 2, or 3) without conflict.

---

## Future Slot Candidates

These didn't fit into this month but are queued based on the data:

1. **Homepage hero test.** The homepage gets 25,451 sessions/mo and currently anchors visitors to $7.99 in the flavor carousel. Test replacing the carousel with a bundle-first hero that drives directly to the 4-pack or 6-pack PDP selection.

2. **Google Ads landing page.** Google search drives $15,500/mo in sales but all ads land on the homepage rather than the PDP. Test a dedicated landing page matching Google ad messaging ("Cookie Dough, Reimagined") with a direct path to purchase.

3. **Post-purchase subscription upsell.** Instead of pushing subscription at first purchase (high friction), test a post-purchase offer: "Love it? Subscribe and save 15% on your next order." This lets customers try before committing and could be more effective than subscription-first given the product polarization.

4. **PDP social proof section.** Replace the 3 static testimonials with a filterable review widget showing real reviews by flavor, rating, and use case ("snacking," "baking," "kids"). Address the "thousands of reviews" claim with actual visible reviews.

5. **Free shipping threshold test.** The current $45 threshold is awkward: the most popular 6-pack is $33.99 (misses by $11), the 8-pack is $44.99 (misses by $0.01). Test lowering to $35 or $40, or test adding a small add-on product (single jar, $7.99) as a shipping threshold upsell.

6. **"Earn Rewards" widget repositioning.** The floating widget overlaps critical conversion elements on mobile (price, checkout button). Test hiding it on PDP and cart pages, or repositioning it to a non-overlapping location.
