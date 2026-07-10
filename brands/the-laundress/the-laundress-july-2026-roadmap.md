# The Laundress CRO Research Brief

**Data Sources:** Meta Ads & Landing Pages, Google Ads, Reviews & UGC (Amazon), PageSpeed / Core Web Vitals (homepage + PDP), Site Screenshots, Non-Data Context, Competitor research (self-researched, July 8 2026)

---

## Insights

The Laundress's single biggest CRO problem is not a site element -- it's a channel gap. The Signature Detergent Classic is the brand's best-selling product: 4.5 stars, 929 reviews, "Best Seller" badge, gallon variant available. Google Shopping surfaces it prominently, with pricing and star extensions. Zero Meta ad traffic goes to its PDP. All three active Meta ads route to weaker destinations -- a delicate wash PDP, a mesh bag bundle with 3.9 stars and no subscription option, and a Black Crow brand awareness storefront with no add-to-cart button. The brand's strongest conversion asset exists on Google but is invisible on Meta. (Source: Meta Ads & Landing Pages, Google Ads)

Of the three active ads, Ad 2 is an active conversion leak. Its creative leads with luxury detergent positioning -- "Elegant, perfumer-crafted fragrances / Luxury detergent with a gentle, effective formula / Designed by textile scientists" -- but the landing page is the Mesh Bag Bundle: $22, 3.9 stars, 166 reviews, no subscription. This mismatch has been live since June 11, 2026. Ad 3 is similarly broken: it sends "Shop Now" clicks to a Black Crow brand storefront page with no purchase path. (Source: Meta Ads & Landing Pages, Site Screenshots)

Scent is both the primary purchase driver and the primary churn trigger. Customers describe the fragrance as "expensive hotel towels," "boutique hotel fresh," and "makes me feel rich" -- these are the words that close sales. The most common 2-3 star complaint across Amazon reviews is that fragrance disappears after drying, reported across Classic, Isle, Marine, and Signature variants. The PDP sets high expectations with an expanded Fragrance Notes section (Top/Heart/Base ingredient lists) and description copy emphasizing "Clean and airy Classic fragrance." Nothing on the PDP addresses what the scent smells like on dry fabric, provides usage guidance, or cross-sells the Fabric Conditioner as a scent extender. The Fabric Conditioner Classic (4.6 stars, $26) appears in a "Pairs Well With" section but without framing. (Source: Reviews & UGC)

The PDP compounds every paid channel problem. On mobile, FCP is 3.6 seconds, LCP is 6.7 seconds, and TTI is 21.1 seconds. A Meta ad click on mobile means: nearly 4 seconds before content appears, nearly 7 seconds until the main image loads, then a scroll required to reach the add-to-cart button -- because the Fragrance Notes section appears above the size selector and purchase options in the buy box. The cart adds further friction: a $70 free shipping threshold, a $44 gap on a single $26 item, one visible cross-sell (Fabric Spray, $19 -- still $25 short of threshold), and no Gallon upsell anywhere in the drawer. The Gallon ($82) is the only single item that unlocks free shipping and saves 21% per load. It is in the collection grid but not surfaced at cart. (Source: PageSpeed / Core Web Vitals, Site Screenshots)

Revenue opportunity: if 3% of single-unit cart sessions upgrade to the Gallon, AOV moves from $26 to $82 -- a 3.15x lift on that segment. The buy-button-above-fold and ad message match fixes compound on top of that. The most straightforward path to more revenue here is: fix the ads that are actively sending traffic to conversion dead ends, route Meta to the best-reviewed product, unblock the buy button on mobile, and give the cart a single upsell that works.

---

## Slot 1: Immediate Fix -- Ad 2 Destination Redirect

**Type:** Immediate Fix

**What's broken:** Meta Ad 2 (active since June 11, 2026) uses luxury detergent messaging but routes to the Mesh Bag Bundle PDP: $22, 3.9 stars, 166 reviews, no subscription option. The copy promises a product the landing page does not deliver.

**Fix:** Redirect Ad 2's destination URL to the Signature Detergent Classic PDP (thelaundress.com/products/signature-detergent-32-fl-oz). No creative change needed -- the current copy already fits the Signature Detergent positioning.

---

## Slot 2: Immediate Fix -- Ad 3 Destination Redirect

**Type:** Immediate Fix

**What's broken:** Meta Ad 3 routes "Shop Now" clicks to a Black Crow brand awareness storefront with no add-to-cart path. Every click is non-convertible by design.

**Fix:** Redirect Ad 3 to the Stain Solution PDP (4.7 stars, $20), which provides an immediate conversion path. Alternatively, route to the Signature Detergent PDP if creative messaging permits.

---

## Slot 3: Signature Detergent Meta Ad Launch

**Type:** A/B test (1 variation vs. control)
**Page:** Signature Detergent PDP (thelaundress.com/products/signature-detergent-32-fl-oz)
**Revenue potential:** New traffic surface; even a 1.5% CR on a cold Meta audience landing on the 929-review PDP vs. 0 current Meta sessions to this page represents a net-new revenue channel at any traffic volume.

**Hypothesis:** If we create a dedicated Meta ad routing to the Signature Detergent PDP, conversion rate from Meta will increase because the brand's highest-social-proof product is currently invisible on its largest paid social channel.

**Data:** Signature Detergent: 4.5 stars, 929 reviews, "Best Seller" badge. Current Meta ad destinations: Delicate Wash PDP (4.7 stars, $30), Mesh Bag Bundle (3.9 stars, 166 reviews, $22). Google Shopping actively features the Signature Detergent with price and rating. Meta has no ad sending traffic to this page. (Source: Meta Ads & Landing Pages, Google Ads, Site Screenshots)

**V1:** New Meta ad creative and copy built around the Signature Detergent Classic. Ad copy leads with the social proof signal ("929 five-star reviews") and the scent trigger ("the fragrance of a boutique hotel, built for everyday laundry"). Destination URL: Signature Detergent Classic PDP. On mobile: ad card shows product bottle, headline leads with review count. On desktop: same creative, same destination. Control: existing Meta ad set with current three destinations. This is a new ad launch, not a site change -- measure by CTR, LP CR, and ROAS against the existing ad set.

---

## Slot 4: Buy Button Above Fold -- Signature Detergent PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Signature Detergent PDP (thelaundress.com/products/signature-detergent-32-fl-oz)
**Revenue potential:** Mobile LCP is 6.7s (score 0.08, failing) and TTI is 21.1s (score 0.01). The PDP is already a slow load -- requiring an additional scroll to reach add-to-cart multiplies that friction. A 5% CR lift on this PDP represents the highest per-session upside of any on-site change. (Source: PageSpeed / Core Web Vitals)

**Hypothesis:** If we move the Fragrance Notes section below the add-to-cart button, more mobile users will see and click add-to-cart because the buy box is currently pushed below fold 1 by the Fragrance Notes block.

**Data:** Buy box stack order on control: Best Seller badge, product name, rating (4.5 / 929 reviews), Fragrance Notes expanded (Top: Fresh, Aldehydic, Citrus, Marine / Heart: Lavender, Rose, Jasmine, Lily of the Valley, Ylang-ylang / Base: Musk, Oakmoss, Patchouli, Sandalwood, Cedarwood), size selector, purchase options, add-to-cart. The Fragrance Notes block is tall enough to push the add-to-cart below fold 1 on mobile. Mobile TTI: 21.1s -- users wait over 21 seconds before the page is interactive. (Source: Site Screenshots, PageSpeed / Core Web Vitals)

**V1:** Collapse the Fragrance Notes block into a tap-to-expand accordion that defaults closed. New buy box stack order: Best Seller badge, product name, rating, size selector (32 fl oz / Gallon), purchase options (One-time $26 / Auto-replenishment), add-to-cart button, then Fragrance Notes accordion below. On mobile: add-to-cart button is visible above fold 1. On desktop: same reorder -- button rises above the fold without scrolling. No copy changes.

---

## Slot 5: Scent Expectation Section -- Signature Detergent PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Signature Detergent PDP (thelaundress.com/products/signature-detergent-32-fl-oz)
**Revenue potential:** Scent longevity is the primary driver of 2-3 star reviews across all reviewed SKUs. Reducing negative review velocity and increasing Fabric Conditioner attach rate (4.6 stars, $26 cross-sell) are both measurable within 90 days. A 10% lift in Fabric Conditioner attach on Signature Detergent sessions adds $2.60 to AOV on attaching orders.

**Hypothesis:** If we add a "Scent Experience" section below the add-to-cart button that sets dry-fabric scent expectations and cross-sells the Fabric Conditioner as a scent extender, the rate of 2-3 star scent-complaint reviews will decrease and Fabric Conditioner attach rate will increase.

**Data:** Scent longevity complaint is the most common 2-3 star driver across collected Amazon reviews -- reported across Isle, Classic, Marine, and Signature variants. PDP currently has an expanded Fragrance Notes section (Top/Heart/Base) that sets high scent expectations with no post-dry calibration. PDP description copy: "Clean and airy Classic fragrance with notes of lily of the valley, sweet musk and sandalwood." Fabric Conditioner Classic (4.6 stars, $26) appears in a "Pairs Well With" section but is not framed as a scent extender anywhere on the PDP. (Source: Reviews & UGC, Site Screenshots)

**V1:** Add a "Scent Experience" content block below the add-to-cart button and above "Pairs Well With." Block content: one-line expectation setter ("Scent is vibrant while washing, subtle on dry fabric -- use slightly more for a stronger result"), one cross-sell tile for Fabric Conditioner Classic ($26, 4.6 stars) with the label "Extend the scent," and a single customer quote from reviews ("Makes me feel rich just doing laundry"). On mobile: block renders as a single-column stack -- expectation text, then cross-sell tile, then quote. On desktop: same content, two-column layout with the cross-sell tile floated right. No changes above the add-to-cart button.

---

## Slot 6: Cart Gallon Upsell -- Free Shipping Unlock

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (thelaundress.com/cart)
**Revenue potential:** Cart threshold gap on a single Signature Detergent ($26): $44. Gallon ($82) is the only single-item that crosses the $70 threshold. Conservative 3% upgrade rate: 3% of single-unit sessions x ($82 - $26) = $1.68 AOV increase per session across the board; for upgrading sessions, AOV moves from $26 to $82 (3.15x). (Source: Site Screenshots)

**Hypothesis:** If we surface a Gallon size upgrade in the cart drawer framed as a cost-per-wash saving and free shipping unlock, a portion of single-unit buyers will upgrade because the Gallon already appears in the collection grid but is never presented at the moment of purchase intent.

**Data:** Cart drawer shows a free shipping progress bar: "Spend $44.00 more and get free shipping" when a single Signature Detergent Classic ($26) is in cart. One cross-sell visible: Classic Fabric Spray ($19) -- brings total to $45, still $25 short of $70 threshold. Gallon: $82, 21% savings badge in collection grid, cost per wash drops from $0.84 (32 fl oz / 31 washes) to approximately $0.63 (Gallon). Gallon is not shown anywhere in the cart. (Source: Site Screenshots)

**V1:** Add a "Save more per load" upsell block in the cart drawer above the checkout button, shown only when the Signature Detergent 32 fl oz is in cart and order total is below $70. Block copy: "Upgrade to the Gallon -- $0.63/wash vs. $0.84/wash, and unlock free shipping." Show side-by-side: 32 fl oz ($26, $0.84/wash) vs. Gallon ($82, $0.63/wash, free shipping unlocked). One-click swap button: "Upgrade to Gallon." On mobile: full-width block, stacked layout. On desktop: same block, inline layout. Control: existing cart drawer with no Gallon mention.

---

## Slot 7: Subscription Default -- Signature Detergent PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Signature Detergent PDP (thelaundress.com/products/signature-detergent-32-fl-oz)
**Revenue potential:** Subscription customers have materially higher LTV than one-time buyers. Subscription on this PDP includes free shipping, which also addresses a primary cart friction point ($70 threshold). Any measurable lift in subscriber rate compounds over the customer lifetime.

**Hypothesis:** If the purchase option defaults to Auto-replenishment instead of One-time delivery, subscription selection rate will increase because new visitors default to whichever option is pre-selected, and subscription already offers the same price plus free shipping.

**Data:** Current PDP purchase option default: One-time delivery ($26). Auto-replenishment option: same $26 price, includes free shipping. Free shipping is a named benefit of subscription but requires the user to actively switch from the pre-selected one-time option. (Source: Site Screenshots, Non-Data Context)

**V1:** Change the default-selected purchase option from "One-time" to "Auto-replenishment." Visual presentation unchanged. The subscription pill is pre-checked on page load. On mobile and desktop: the free shipping benefit label under the subscription option is the only change visible to users who do not interact with the selector. One-time option remains available one tap/click away.

---

## Slot 8: Homepage Hero -- Add CTA and Headline

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (thelaundress.com/)
**Revenue potential:** The hero section is seen by 100% of homepage visitors. A hero with no headline, no CTA, and no price functions as a brand image, not a conversion entry point. Quantifying a CR lift requires traffic data not collected -- but the opportunity cost of a non-converting hero is session-level.

**Hypothesis:** If we add a headline, product name, and "Shop Now" CTA to the homepage hero section, the rate of visitors navigating from homepage to a product page will increase because the current hero image (Signature Detergent bottle) gives visitors no action to take.

**Data:** Homepage hero on control: full-width image of the Signature Detergent bottle on an off-white background. No headline, no CTA button, no price, no rating. Visitors who do not scroll or interact with navigation have no conversion path from the hero section. (Source: Site Screenshots)

**V1:** Overlay the existing hero image with a short headline ("The detergent that makes laundry feel like luxury"), the product name ("Signature Detergent Classic -- 4.5 stars, 929 reviews"), and a primary CTA button ("Shop Now -- from $26"). On mobile: headline and CTA stack vertically, anchored to the bottom third of the hero image. On desktop: text block floated left, hero image occupies the right two-thirds. No changes below the hero section.

---

## Future Slot Candidates

1. **Ad 3 Black Crow Storefront** - Sending paid clicks to a no-purchase brand page; redirect to Stain Solution PDP (4.7 stars, $20) for immediate conversion path. (Addressed as Immediate Fix in Slot 2 -- listed here if a dedicated A/B test of destination URLs is preferred.)
2. **Measuring Cup Cart Cross-Sell** - Amazon reviewers explicitly name missing measuring cup as a purchase friction for a concentrated product; surfacing it as a cart add-on addresses a stated customer need.
3. **Amazon Packaging QA** - Broken cap complaints appear across multiple reviewers; protecting the 4.5-star rating on the best-selling SKU protects Google Shopping click-through rate.
4. **Collection Page Scent Filter** - With multiple scent variants (Classic, Isle, Marine, Delicate), a scent preference filter on the collection page would reduce variant confusion, which drives scent-mismatch returns.
