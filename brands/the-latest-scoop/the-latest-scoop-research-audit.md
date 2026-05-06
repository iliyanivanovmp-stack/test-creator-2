# The Latest Scoop CRO Research Audit

## Brand Overview
Canadian lifestyle retailer founded 2004. 13 physical locations across Vancouver, Calgary, Victoria, and Toronto. Sells women's fashion, home decor, accessories, beauty, and gifts. Operates a "new drops weekly" model. Free shipping in Canada on orders over $200 CAD.

---

## Meta Ads

Analyzed 3 recent Meta ads out of many active campaigns. Only 1 ad was available for review; the Meta Ad Library did not surface a landing page URL for it.

**Ad 1:** Store opening announcement for the new Chinook Centre location (Calgary). Started running April 8, 2026. Creative: two-panel carousel showing the storefront and interior with text "The Latest Scoop at Chinook Centre" and "Yes, we're open." Event details: April 11, 12 PM - 3 PM with complimentary matcha and flowers.

**Key observations:**
- Brand/event focused, not direct response ecommerce
- No CTA to the online store
- No product featured, no price, no offer
- Only 1 ad available for analysis

---

## Google Ads Transparency

Multiple Google ad formats active: search, display, and shopping.

**Search ad copy themes:**
- "The Latest Scoop elevated outerwear pieces are perfect for the changing seasons ahead."
- "You Can Set the Tone This Fall with Head-to-Toe Neutrals for a Clean and Modern Look."
- "Shop New Styles for this Fall. Comfort at home and in class."
- "The Latest Scoop - Shop Fresh New Arrivals" (with sitelinks: Dresses, Skirts, Locations, Denim)

**Display ad copy:**
- "Shop Fresh New Arrivals - We Offer Apparel, Stationary, Accessories, Giftware, Home Decor and More."
- "We Are a Lifestyle Concept Store Full of Pretty Things for You and Your Home."
- "Fade Into Fall - The Latest Scoop elevated outerwear pieces are perfect for the changing seasons ahead."
- "Dresses Available - Our Purpose Is to Inspire You to Embrace Your Individuality through Genuine Interactions."

**Shopping ad:** East Side High Rise Loose Crush jean featured with price.

**Key observations:**
- Fall-dated copy running in late April 2026: "Fade Into Fall," "Head-to-Toe Neutrals for this Fall," "outerwear for the changing seasons ahead." Direct message match gap with the current spring site.
- Brand purpose copy is vague: "Inspire You to Embrace Your Individuality through Genuine Interactions" communicates nothing about the product or offer.
- Multiple near-identical search ad copies running simultaneously. No visible variation testing.
- The one conversion-focused search ad (with sitelinks for Dresses, Skirts, Locations, Denim) is the strongest format in the set.
- No shipping offer, no price anchoring, no urgency in any ad copy.

---

## Reviews & UGC

Reviews sourced from Facebook. All provided reviews were negative recommendations.

**Reviewer 1 (Facebook):**
"Quality and pricing for their clothes is totally off. There are no refunds just store credit. Store credit in their case means literally just in the local store. They will not let you use the store credit online. Had to contact customer service and ask for them to transfer the credit to a gift card. Total useless step and waste of time. Their shipping times are off, they take extremely long to prepare the order and the tracking number..."

**Reviewer 2 (Facebook):**
"Worst store in Calgary. Terrible customer service. They do not offer refunds for their overpriced low quality clothing, nor do they properly bring this ridiculous policy to their customer's attention. Zero stars."

**Reviewer 3 (Facebook):**
"Don't shop here. I ordered items for a vacation and they mailed me the wrong items. Clearly someone doesn't know how to do their job. The items were ticketed incorrectly and the person shipping them clearly didn't double check. After a day of trying to get ahold of someone, I was told they have system errors. For this inconvenience I was offered 10% off. The customer service is nonexistent."

**User-provided context:** "Insulting return policy that highlights how The Latest Scoop feels about their customers. Also store is non-inclusive with sizing."

**Recurring themes:**
- Return policy perceived as store credit only, and store credit locked to physical locations
- Quality-to-price mismatch ("overpriced low quality")
- Slow shipping and order preparation
- Fulfillment errors (wrong items shipped)
- Unreachable customer service; inadequate compensation for errors (10% off for a completely wrong order)
- Sizing non-inclusivity (size range 24-31 denim, no extended sizing)

**Important note on return policy:** The published online return policy at thelatestscoop.ca states that regular-priced items are refundable to the original payment method within 14 days of ship date, with a $5 return label fee. The disconnect between reviewer experience ("no refunds, store credit only") and the published policy suggests either: in-store purchase policies differ from online, staff communication is inconsistent, or a previous policy created lasting negative perception. The bigger problem is that the policy is hidden in a tab on the PDP and never proactively surfaced in the buy flow.

---

## Page Speed / Core Web Vitals

Report date: April 22, 2026. Mobile scores only (provided).

### Homepage (thelatestscoop.ca)
| Metric | Score |
|--------|-------|
| Performance | 41 / 100 (Fail) |
| Core Web Vitals | Failed |
| Largest Contentful Paint (LCP) | 72.6s |
| First Contentful Paint (FCP) | 12.2s |
| Total Blocking Time | 550ms |
| Speed Index | 24.8s |
| Cumulative Layout Shift | 0 |
| Accessibility | 89 |
| Best Practices | 73 |
| SEO | 92 |

### PDP (Tiger High Rise Dad Jean - Dark Blue)
| Metric | Score |
|--------|-------|
| Performance | 30 / 100 (Fail) |
| Core Web Vitals | Failed |
| Largest Contentful Paint (LCP) | 48.8s |
| First Contentful Paint (FCP) | 11.9s |
| Total Blocking Time | 1,280ms |
| Speed Index | 28.2s |
| Cumulative Layout Shift | 0 |
| Accessibility | 97 |
| Best Practices | 73 |
| SEO | 100 |

**Key observations:**
- Both pages fail Core Web Vitals on mobile. The LCP scores are catastrophic: 72.6s on homepage and 48.8s on PDP. An LCP over 4s is considered poor; these are 12-18x worse than the acceptable threshold.
- PDP Total Blocking Time of 1,280ms is especially damaging. This is the page where purchase decisions are made.
- Page speed is a systemic issue, not page-specific. Top audit flags include: inefficient cache policies, unminimized JavaScript (~4 savings), render-blocking requests, legacy JavaScript, duplicate JavaScript, image delivery issues, and more than 4 concurrent connections.
- CLS of 0 on both pages is the one consistently green metric.

---

## Competitor Insights

Direct Canadian competitors in the curated women's fashion boutique space:

**Aritzia:** Canada's dominant multi-brand women's fashion retailer. Strong online experience, consistent on-figure photography across all product cards, prominent review counts on PDPs, clear free shipping thresholds, and well-optimized collection pages with filter/sort functionality. Positioned slightly more premium and trend-forward than The Latest Scoop.

**Oak & Fort:** Minimalist Canadian women's brand. Known for timeless neutral aesthetics and high-quality fabrics. Similar aesthetic positioning to The Latest Scoop. More consistent brand voice. Competitive price points.

**Dynamite:** Mass Canadian women's fashion. Affordable, trend-driven. Broad size range (XS-XL). Strong social proof on PDPs.

**Key competitive gaps for The Latest Scoop:**
- Competitors display review counts and ratings on both collection grids and PDPs. The Latest Scoop shows none.
- Competitor collection pages use consistent on-figure photography. The Latest Scoop mixes ghost mannequins, model shots, lifestyle images, and badly cropped torso shots in the same grid.
- No visible unique value proposition differentiating The Latest Scoop from Aritzia or Oak & Fort beyond "curated selection."

---

## Site Screenshots

### Homepage (top 3 folds)
- **Fold 1:** Announcement bar rotates: "SIGN UP FOR EMAIL TO WIN $1000," "13 LOCATIONS ACROSS CANADA," "NEW DROPS WEEKLY." Hero is a three-panel image of spring/summer clothing with large "new drops" text overlay. No CTA button on the hero. No value proposition text.
- **Fold 2:** Product grid begins. Mix of ghost mannequin and model photography visible together. Products include a plaid halter top, white jeans (J Brand), a blue cardigan, navy denim dress. No prices visible in fold 1. Prices appear in fold 2-3.
- **Fold 3:** "OUR LATEST DROP" heading. 6 products shown in carousel format: Double-Breasted Trench Jacket ($168 CAD), One Shoulder Striped Long Sleeve Sweater ($88 CAD), Essential White Blouse ($98 CAD), Black Draped Top ($98 CAD), Desert Pleat Skirt Light Khaki ($98 CAD), PU No Collar Jacket Coffee ($145 CAD). Heart/wishlist icons but no add-to-cart buttons on collection grid.

**Key issues:**
- No CTA on the hero (no button, no directional link)
- No trust signals in first 3 folds (no reviews, no social proof, no guarantee)
- Announcement bar burns all 3 slots on brand/marketing messages, none address purchase objections (shipping cost, returns, fit)
- Ghost mannequin and model photography mixed throughout
- Free shipping threshold ($200 CAD) not visible in first 3 folds

### Best Sellers Collection Page (top 3 folds)
- 5-column desktop grid
- Visible products: Boatneck Top ($116), Pleaser High Rise Wide Ankle Twilight ($165), Keeper Low Rise Straight Heartbeat ($185), BNA Soft Curve Laurel Green ($120), Button Down Cap Sleeve Shirt Off White ($80), Spaghetti Bra Cup Mesh Velvet Burn Out Midi Dress ($144), Logan High Rise Dad Jean ($165), Belted Utility Shacket Beige ($179), One Side Metal Triming Halter Dress ($148), Wide Leg Cargo Pants Olive/Green ($135)
- Sort By and Filter options present (top right)
- Grid layout toggle (3 options)

**Key issues:**
- Photography wildly inconsistent: on-figure model shots, ghost mannequins, lifestyle shots, and badly cropped torso photos (no heads) mixed in the same grid
- Zero review stars or review counts on any product card
- No size availability indicator on the grid
- No quick-add to cart
- Free shipping threshold ($200 CAD) only appears occasionally in rotating announcement bar

### PDP - Logan High Rise Dad Jean ($165 CAD)
- Brand label: "HIDDEN JEANS"
- Product name: Logan High Rise Dad Jean
- Price: $165.00 CAD
- Shop Pay: 4 interest-free installments from $14.89/mo
- Color swatch present but appears broken (white square shown for "Dark Blue")
- Size buttons: 24, 25, 26, 27, 28, 29, 30, 31
- CTA: "ADD TO BAG - $165.00" (black button)
- Urgency: "Only 2 left - order now!" in red
- Trust signals in buy box: "Free shipping on orders $200" and "Secure checkout with ApplePay and Shop"
- Tabs: Details, Shipping & Returns (return policy hidden behind tab click)
- Product description tone: casual/influencer ("Hey there, fashion lover! These babies feature...")
- First hero image: Ghost mannequin (jeans only, no model, no styling context)
- Second image: Model wearing the jeans with a black top (full body visible)
- Third image: Torso-only close-up of model in the jeans (no head)
- Zero customer reviews visible anywhere on the page
- No size guide link in buy box
- No "You May Also Like" or cross-sell visible in the first 3 folds

**Key issues:**
- Ghost mannequin is the first image seen. The more compelling model photo is second.
- No reviews at the point of purchase for a $165 item
- Return policy hidden behind a tab rather than surfaced in the buy box
- No size guide link despite denim sizing being a primary conversion obstacle
- Copy tone ("Hey there, fashion lover!") inconsistent with the premium price point and the clean, minimalist brand aesthetic

### Cart Drawer
- Free shipping progress bar: "You're $35.00 away from free shipping!"
- Product image shown in cart: ghost mannequin photo (not the model photo)
- Line item: Logan High Rise Dad Jean, Color: Dark Blue, Size: 24, Qty: 1, $165.00
- Quantity selector (minus/plus)
- Delete button
- Large empty white space below the line item (no cross-sell, no upsell, no recommendations)
- Discount code field + Apply button (prominent)
- Shipping: "Spend $35.00 for free shipping" (repeated messaging from bar above)
- Total: $165.00 CAD
- Checkout button (black, full-width)
- "Continue Shopping!" link (coral/orange text)

**Key issues:**
- Zero cross-sell or upsell content in the large empty space below the line item
- A $165 cart is $35 short of free shipping, yet there's no product recommendation to close that gap
- Discount code field is prominently placed, increasing coupon-seeking abandonment risk (customers leave to search for codes, don't return)
- Ghost mannequin image persists into cart, missing an opportunity to reinforce purchase confidence with the model shot

---

## CRO Ebook Reference ("Billion Dollar Websites" by Dylan Ander)

**Buy Box (Chapter 6):** Five optimization tactics for buy boxes: make price obvious, make the offer unique (bundles), use social proof (reviews), urgency signals, and frictionless payment options (installments). The Latest Scoop has price, urgency, and Shop Pay installments but is missing reviews and the return policy is buried.

**AOV - Upsells (Chapter 9 & 10):** Cart is the highest-leverage upsell placement in ecommerce. "Cross-selling tactics become four times more efficient if you show the customer the related product in their shopping cart, just before they proceed to checkout." The Latest Scoop has a completely empty cart with no cross-sell. One-click upsells in the cart are described as "free money."

**Product Page Testing (Chapter 15):** "Start with your highest-impact products, i.e., the ones that drive the most revenue. Small performance improvements on these pages could make a huge difference." Also: "Navigation changes and landing page improvements are highest priority." The Latest Scoop homepage has no navigational CTA in the hero despite significant paid traffic arriving there.

---

## Cross-Source Analysis

### Converging Themes

**1. Trust deficit at the point of purchase**
Reviews: customers feel deceived by the return policy and question quality-to-price ratio. Site screenshots: zero reviews on PDPs, return policy hidden in a tab, copy tone inconsistent with premium pricing. Google Ads: brand purpose copy ("Inspire You to Embrace Your Individuality") says nothing about product quality or value. All three sources point to a brand that isn't doing enough to build purchase confidence where it counts.

**2. Missed AOV in the cart**
Site screenshots: cart is completely empty below the line item. The $165 Logan jean cart is $35 short of free shipping, yet no product recommendations are shown to close the gap. CRO ebook (Chapter 9/10): pre-purchase cart upsells are described as "free money." Industry data: cart cross-sells lift AOV 10-30%. Nothing here is difficult to solve - the space is just empty.

**3. Photography inconsistency undermining product confidence**
Collection page: ghost mannequins, model shots, lifestyle images, and headless torso crops all in the same grid. PDP: ghost mannequin is the hero image for jeans, with the model photo hidden as the second image. Cart: ghost mannequin image persists. Reviewers: quality complaints may be amplified by inability to visualize how garments actually look and fit on a body.

**4. Page speed is a conversion emergency**
Mobile LCP of 72.6s (homepage) and 48.8s (PDP) is catastrophic. Industry data: mobile pages with LCP over 4s are considered poor. Pages this slow lose visitors before the content even loads. This precedes every other conversion problem on the site.

**5. Message match gap in paid media**
Google Ads running fall messaging ("Fade Into Fall," "outerwear for the changing seasons ahead") in late April 2026. Homepage is promoting spring "new drops." Visitors coming from Google Ads arrive with a fall/outerwear context and land on a spring drop homepage - a direct message mismatch.
