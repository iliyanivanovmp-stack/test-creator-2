# BottleBuzz CRO Research Brief

**Data Sources:** Meta Ads, Google Ads Transparency, Reviews & UGC, Page Speed / Core Web Vitals, Competitor Research, Site Screenshots

---

## Insights

BottleBuzz is selling $100 to $4,499 bottles with a buy box that has no trust signals. The direct competitor, Wooden Cork, is selling the same Blanton's Original for $20 more and leading the buy box with "Authenticity Guaranteed," "In stock, ready to ship," and 592 reviews. BottleBuzz has 2,607 verified reviews and the lower price - but none of that is visible where the purchase decision happens.

The trust gap is not hypothetical. Trustpilot and BBB reviews document authenticity concerns, wrong bottles shipped, and refusals to refund. At least one customer contacted Buffalo Trace Distillery directly; Buffalo Trace reportedly confirmed they do not distribute to BottleBuzz. Any skeptical buyer can find that review in 30 seconds. Yet the PDP shows no star rating, no review count, no authenticity badge, and no shipping promise near the Add to Cart button.

Compounding this: the three Meta ads analyzed (a sample of many active campaigns) all land on collection pages that carry none of the ad's messaging forward. Ad 2 promises delivery "in less than a week." The Blanton's collection page says "Shipping calculated at checkout." Ad 3 runs a Pappy Van Winkle creative that links to the Blanton's collection, a different brand. Meanwhile, the active EASTER 10% discount is visible sitewide but appears in none of the ad copy - an unused hook at the point of highest intent.

The PDP is also the worst-performing page on the site by interactivity: 1,630ms of total blocking time on mobile before a visitor can tap "Add to Cart." That is 1.6 seconds of a frozen page on the highest-intent destination receiving paid traffic. Every second of delay reduces mobile conversions by approximately 7% (Google, 2024).

Revenue opportunity: These three issues target the full funnel from ad click to purchase. Without internal session data, the math is directional - but at BottleBuzz's price points ($100-$1,200 average order), even a 1% absolute CR improvement across PDP traffic, combined with the Meta ad efficiency gain from fixing message match, represents tens of thousands in monthly incremental revenue. The scale of the opportunity grows directly with ad spend.

---

## Slot 1: PDP Buy Box - Trust and Urgency Layer

**Type:** A/B test (1 variation vs. control)
**Page:** PDP - top-selling products (e.g., /products/blantons-original-single-barrel and equivalents across the Pappy/Weller/Blanton's catalog)
**Revenue potential:** Without session data, using a conservative estimate of 20,000 PDP sessions/month at a $125 AOV and a 1% absolute CR lift (supported by industry data showing trust signals average a 32% CR improvement on PDPs), this test is worth $25,000/month in incremental revenue. The actual figure scales directly with traffic volume, and is higher given BottleBuzz's product mix extends to $1,200+ bottles.

**Hypothesis:** If we add an authenticity guarantee, shipping window, and star rating with review count directly into the buy box - and move "Add to cart" above the "Make it a Gift?" and "Custom Engraving" buttons - ATC rate will increase because buyers spending $100-$1,200 need trust assurance at the point of commitment, and the current buy box provides none.

**Data:** Trustpilot and BBB reviews document authenticity concerns (including a customer who contacted Buffalo Trace directly) and wrong bottles shipped - these are the exact doubts a buyer has when hovering over "Add to cart." (Source: Reviews & UGC) Wooden Cork's Blanton's PDP leads the buy box with "Authenticity Guaranteed," "Expertly Packaged," "In stock, ready to ship," and 592 reviews - the same bottle, $20 more expensive, with trust signals where BottleBuzz has none. (Source: Competitor Research) The PDP screenshots confirm no star rating, no review count, no authenticity badge, and no shipping promise are visible anywhere in the buy box. The ATC button is below fold 1 on mobile, behind "Make it a Gift?" and "Custom Engraving" options. (Source: Site Screenshots) The 2,607 Verified Reviews badge visible on the homepage disappears entirely on the product page. (Source: Site Screenshots) Adding trust signals and reviews to PDPs averages 32% CR lift for high-ticket ecommerce products (CRO research, 2025). The ebook confirms the buy box is "The Judge's domain" for high-ticket purchases - analytical buyers need explicit reassurance to approve the spend. (Source: CRO Ebook)

**V1:** Four changes to the buy box, no changes to any other page element.

First: directly below the product title and brand link, add a star rating display and review count. Pull from the existing reviews on the site. The display format is: "4.X stars (2,607 reviews)" as a clickable link that scrolls to the reviews section. On mobile, this sits on a single line between "Blanton's" and the price. On desktop, same placement in the right-side buy box column.

Second: move the "Add to cart" button directly below the quantity selector, removing it from behind the "Make it a Gift?" and "Custom Engraving" buttons. The new buy box order is: star rating / reviews, then price, then quantity selector, then "Add to cart" (black, full-width), then the Shop Pay installments line ($24.99 x 4), then the trust bar (see below), then "Make it a Gift?" and "Custom Engraving" (in their current outlined button format). On mobile, this makes the ATC button visible on fold 1 for most device heights. On desktop, same column order in the right-side panel.

Third: directly below the Shop Pay installments line, add a three-item horizontal trust bar with icon and label for each: a shield icon with "Authenticity Verified," a truck icon with "Ships within 3-5 business days" (verify this window with the BottleBuzz team before launch), and a box icon with "Expert Packaging." On mobile, the three items stack into a 3-column row with small icons and short labels. On desktop, the same row spans the full buy box width. No background color - plain text with icons keeps it clean and non-promotional.

Fourth: replace "Shipping calculated at checkout" with the delivery estimate used in the trust bar ("Ships within 3-5 business days") so the first thing a buyer reads after the price is a commitment, not a calculation.

No changes to product imagery, product description copy, history section, or any element outside the buy box.

---

## Slot 2: Blanton's Ad Landing Page - Message Match for Paid Traffic

**Type:** A/B test (1 variation vs. control)
**Page:** /collections/blantons (control) vs. new dedicated landing page (variation), tested by duplicating the Blanton's Meta ad sets and pointing one set to the new page
**Revenue potential:** Ad 2 and Ad 3 both direct traffic to /collections/blantons. Estimating 10,000 paid sessions/month to the Blanton's collection from Meta at a $120 AOV, a 0.5% absolute CR lift from improved message match delivers $6,000/month in incremental revenue. At higher ad spend, this scales proportionally. The efficiency gain also reduces effective cost-per-acquisition across all Blanton's campaigns.

**Hypothesis:** If we create a dedicated landing page for Blanton's paid traffic that mirrors the ad's promise (immediate access, fast delivery, full collection available), conversion rate from Meta ads will increase because arriving visitors will find the page confirms what the ad said rather than landing on a generic 44-product collection grid.

**Data:** Ad 2 promises "Get immediate access to purchase nearly every bottle of Blanton's ever made, delivered right to your door in less than a week." The Blanton's collection page (/collections/blantons) headline reads "BLANTON'S BOURBON WHISKEY COLLECTION" followed immediately by a product grid - no delivery promise, no availability signal, no urgency. (Source: Meta Ads, Site Screenshots) Ad 3 runs a Pappy Van Winkle creative linking to the Blanton's collection, creating a direct brand mismatch. (Source: Meta Ads) The EASTER 10% discount is visible on all collection pages but appears in no ad copy - an unconverted hook. (Source: Meta Ads, Site Screenshots) The ebook states clearly: if the hero section doesn't continue the conversation the ad started, visitors bounce. The collection page's 44-product grid and "Price" and "Brand" filters are discovery tools, not purchase-intent tools for cold paid traffic. (Source: CRO Ebook) Wooden Cork converts Blanton's traffic with specific trust signals in the buy box; SipWhiskey converts with scarcity framing (sold-out indicators, availability counts). BottleBuzz's collection page uses neither. (Source: Competitor Research)

**V1:** A new dedicated landing page, separate from /collections/blantons, used only as the destination for Blanton's Meta ad traffic. The existing /collections/blantons page remains live for all other traffic (SEO, direct, email). Test is run by duplicating the active Blanton's Meta ad sets: one set continues to /collections/blantons, one set points to the new landing page.

The landing page structure, top to bottom:

Hero section: Headline "The Blanton's Collection. In Stock. Ready to Ship." Subheadline: "Every bottle Blanton's makes, available now. Order today, at your door in less than a week." (This directly mirrors Ad 2's promise.) Below the subheadline, one line showing the EASTER offer: "Use code EASTER for 10% off all regularly priced bottles." On mobile, headline at the top, then subheadline, then offer line, then the CTA button: "Shop the Collection" (scrolls to the product section below). On desktop, this is a full-width hero with the headline, subheadline, and offer on the left and a single featured product image (Blanton's Gold or Full Lineup hero shot) on the right.

Trust bar: Directly below the hero, a horizontal row of three signals: "Authenticity Verified" | "Ships within 3-5 business days" | "2,607+ Verified Reviews." On mobile, three items in a single row with small icons. On desktop, same row centered and full-width.

Featured products: Below the trust bar, a curated grid of 6-8 top Blanton's products (not the full 44). Prioritize: Blanton's Original Single Barrel, Blanton's Gold Label, Blanton's Straight From The Barrel, Blanton's Full Lineup Bundle Set, Blanton's Black Label, and 1-2 accessory bundles (e.g., Blanton's with Glencairn set). Each tile shows the product image, name, sale price with strikethrough original price, and a "Add to Cart" or "Shop Now" button. No filters, no sort - remove the discovery friction that collection pages require. On mobile, 2-column grid. On desktop, 3-column grid.

Below the product grid, a single line: "Looking for the full Blanton's catalog? View all 44 products." (links to /collections/blantons). This prevents the page from feeling artificially limited while keeping the primary focus on the curated selection.

No navigation changes. Announcement bar (EASTER) remains. Footer remains.

---

## Slot 3: Cart Drawer - Cross-Sell to Increase AOV

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer - sitewide
**Revenue potential:** Estimating 5,000 cart sessions/month (conservative for a store at this activity level), with 10% of shoppers adding a cross-sell item at an average of $35 (accessories, cigars, or a lower-priced bottle), this test is worth $17,500/month in incremental AOV. The actual figure scales with cart volume and cross-sell selection.

**Hypothesis:** If we add a curated "Complete Your Order" product row in the cart drawer's empty white space, AOV will increase without materially impacting checkout conversion rate because buyers who have already committed to a $100-$1,200 bottle are the highest-intent visitors on the site, and a relevant complementary product reduces friction compared to going back to browse.

**Data:** The cart drawer screenshot shows a large empty white space - approximately half the drawer height - between the product line and the subtotal. No cross-sell, upsell, or trust element fills this space. (Source: Site Screenshots) The BottleBuzz site navigation includes Cigars, Accessories, and Bundles categories (visible in main nav). These categories exist specifically because bourbon buyers also buy related items - Glencairn glasses, whiskey stones, cigar bundles, decanters. (Source: Site Screenshots) The ebook identifies recommended products in the cart as one of its nine AOV-improvement tactics: "Adding Recommended Products above the CTA creates scroll debt, which adds friction... position them below the subtotal." The ebook also flags that "Customers Also Wanted" phrasing adds social proof and mimesis to cross-sell sections. (Source: CRO Ebook) Wooden Cork's collection page surface bundles with accessories (Blanton's with Glencairn set, cigar bundles) as standard catalog items - indicating buyer appetite for these combinations. (Source: Competitor Research)

**V1:** In the empty white space of the cart drawer, between the product line items and the subtotal/checkout area, add a "Complete Your Bar" horizontal product row. The row shows 3 product tiles, horizontally scrollable on mobile. Each tile contains: a small product image (square, roughly 80x80px), product name (truncated to 2 lines), price, and a circular "+" add button. Tapping "+" adds the product directly to the cart without closing the drawer and refreshes the cart total inline.

Product selection for the row should be algorithmically driven: if the cart contains a bourbon, surface bourbon accessories (Glencairn glasses, whiskey stones, decanter) and/or cigars. If the cart contains a tequila, surface appropriate glassware. If the cart contains a bundle, surface single bottles that pair with it. If no category match is available, default to the 3 highest-margin accessories in the Accessories category. The selection logic should be confirmed with the BottleBuzz team on what's available in their Shopify product catalog under Accessories and Cigars.

On mobile: the "Complete Your Bar" label (small, gray, caps) appears above the row. The 3 tiles scroll horizontally if they overflow. The row sits between the cart line items and the "Add order note" / shipping threshold area visible at the bottom of the drawer. On desktop: same layout, but the 3 tiles display side by side in the full drawer width without horizontal scroll needed.

The existing "Checkout" and "View cart" buttons remain unchanged in position and appearance.

---

## Future Slot Candidates

- **Homepage hero rotation:** The first hero slot (fold 1) shows "Corporate Gifting" to all visitors, including rare bourbon buyers arriving from Pappy and Blanton's Meta ads. Replacing or rotating slot 1 to lead with "Premium Spirits, Delivered" (currently slot 2) for new visitors from paid channels would improve message match sitewide. Test: dynamic hero that shows the rare spirits value prop to paid traffic sessions and the corporate gifting hero to direct/returning traffic.

- **EASTER discount in Meta ad copy:** The active EASTER 10% discount is visible on every page but appears in none of the 3 Meta ads analyzed. Inserting the offer into ad copy (e.g., "Save 10% this Easter - use code EASTER at checkout") is an ad-level test, not a site test, but it directly increases the relevance of every click and reduces the gap between ad expectation and landing page reality.

- **Page speed remediation:** Homepage LCP of 10.1s and PDP TBT of 1,630ms are significant conversion drags, especially for paid mobile traffic. Addressing unused JavaScript (946 KiB on homepage, 1,022 KiB on PDP), image optimization (977 KiB on homepage), and render-blocking requests would directly improve all test results above. This is a dev project, not an A/B test, but it unlocks the full potential of Slots 1 and 2.

- **PDP price advantage callout:** BottleBuzz prices Blanton's Original at $99.95 vs. $119.99 at Wooden Cork and $199.99 at Rare Whiskey Shop. This is a meaningful price advantage that appears nowhere on the PDP or collection pages. A "Best price online - we checked" badge or simple "Lower than retail" callout near the price could convert comparison shoppers who have already visited a competitor.

- **Email capture popup to offer clarification:** A $10 OFF popup appeared during both the homepage and PDP page speed tests. If this popup fires on mobile for paid traffic before the buy box is accessible, it may be interfering with conversion - especially on the PDP where TBT is already 1,630ms. Testing delayed popup timing (trigger after 30 seconds or scroll past the buy box) would reduce friction without eliminating the email capture mechanism.
