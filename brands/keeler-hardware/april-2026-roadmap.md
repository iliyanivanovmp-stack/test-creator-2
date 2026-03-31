# April 2026 Testing Roadmap

**Data Sources:** Meta Ads, Reviews & UGC, Page Speed / Core Web Vitals, Competitor Research, Non-Data Context, Site Screenshots

---

## Insights

The biggest problem in the data is not on the product pages — it's at the two ends of the funnel where you're already spending money. At the top, paid ads are qualifying traffic by intent (security buyers, interior designers, trade professionals) then sending them to pages that ignore that intent entirely. At the bottom, the cart drawer has no checkout button, takes 5+ seconds to load, and shows no shipping threshold. Every buyer passes through it.

Three data sources point to the same gap on the PDP. The top-reviewed feature across dozens of product reviews is "keyed alike." It doesn't appear in the buy box — it's buried in the description tab below the fold. Meanwhile, bulk pricing exists at 10, 20, and 30-unit breakpoints, but buyers have to discover it themselves. There are no quantity shortcuts, no prompts, no nudge. The trade buyer — the highest-value repeat customer — is being asked to do the work.

The reviews tell a clear story about who shops here: rental property managers responding to compliance legislation, builders buying in bulk, interior designers sourcing for projects. The site was built for a general consumer. The gap between who's actually buying and how the site speaks to them is where the conversion opportunity lives.

Assume a conservative AOV of $80 and a 0.5% lift in checkout initiation rate from cart drawer improvements. At 10,000 monthly cart-opener sessions, that's 50 additional checkout initiations. At a 60% checkout-to-order rate, that's 30 additional orders, or $2,400/month. The actual number is likely higher — we don't have session data because Shopify Analytics was not available for this audit. Priority order reflects funnel position and data confidence, not traffic estimates.

---

## Slot 1: Cart Drawer — Checkout Access + Shipping Threshold Bar

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (sitewide) — keelerhardware.com.au
**Revenue potential:** Without session data, we can't calculate precisely. The cart drawer is the last touchpoint before checkout. Adding a direct checkout path and shipping nudge are among the highest-leverage, lowest-risk cart interventions documented in ecommerce CRO. Flag to pull cart drawer sessions from Shopify Analytics before this test launches.

**Hypothesis:** If we add a "Proceed to Checkout" button to the cart drawer and show a free shipping progress bar, checkout initiation rate will increase because visitors currently have no direct path to checkout from the drawer and receive no reminder that they're close to the $99 free shipping threshold.

**Data:** The cart drawer CTA reads "VIEW CART" only — clicking it opens the full cart page before checkout is accessible. There is no "Proceed to Checkout" option in the drawer. (Source: Cart Drawer Screenshot) The drawer also shows a large blank space where the Upnova upsell app loads — confirmed as a 5,020ms render-blocking script that delays drawer content rendering. (Source: Page Speed Audit) The free shipping threshold is $99 and is called out in the announcement bar, but there is no progress indicator inside the drawer to remind buyers how close they are. (Source: Homepage Screenshot, Cart Drawer Screenshot) The upsell recommendation currently includes the same product already in the cart, further undermining the upsell section's utility. (Source: Cart Drawer Screenshot)

**V1:** Replace the "VIEW CART" button with two stacked CTAs: a primary "Proceed to Checkout" button (full-width, teal, same styling as current ADD TO CART) and a secondary "View Cart" text link below it. Add a free shipping threshold bar directly above the CTA area: a progress bar showing how far the current cart total is from $99 free shipping, with text like "Add $X more for free shipping." If the cart is already over $99, replace the bar with a green "You've got free shipping!" confirmation line. Remove the duplicate product from the upsell carousel (the same item already in the cart should be excluded from recommendations). Lazy-load the upsell section so it does not block the drawer from rendering — the checkout button and subtotal must appear immediately on drawer open without waiting for the upsell app.
**Brief:** Desktop: Two-button layout below the cart line items. Primary button: "Proceed to Checkout" full-width, teal (#1B6B5A or current brand teal). Secondary: "View Cart" as a plain text link, centred, smaller font, below the primary button. Shipping progress bar: sits between the product list and the CTA buttons. Bar fills proportionally based on cart subtotal vs. $99. Use brand teal fill on grey track. Label: "Free shipping on orders over $99" with dynamic copy showing remaining amount. Green state when threshold is met. Mobile: Same layout, stacked vertically. Drawer opens from right on mobile — ensure buttons are thumb-reachable at bottom of viewport. Upsell section: move below the CTA block or lazy-load after drawer content is painted. Do not let upsell JS delay the render of the checkout button. This is a dev requirement, not just design. Sequencing: this test does not conflict with Slots 2, 3, or 4.

---

## Slot 2: PDP Buy Box — Bulk Quantity Shortcuts + Keyed Alike Callout

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Pages (all products with bulk pricing) — keelerhardware.com.au/products/*
**Revenue potential:** Without session data, we can't calculate precisely. The target is AOV lift: if 10% of single-unit buyers shift to a 10-unit purchase at $35.53 each instead of $37.40, the order value more than triples. Trade buyers are the most likely segment to respond — they already buy in bulk when they know the savings exist.

**Hypothesis:** If we add quantity shortcut buttons to the buy box and surface the "keyed alike" feature as a callout above the fold, average order value will increase and conversion rate will improve because trade buyers can currently see bulk pricing only in the below-fold table and must manually enter quantities with no prompting.

**Data:** The bulk pricing table (Buy 10–19: $35.53, Buy 20–29: $34.60, Buy 30+: $33.66) sits below the ADD TO CART button, below the trust icons. It is visible on the page but there is no mechanism to activate it — the quantity selector defaults to 1 and there are no shortcuts. (Source: PDP Screenshot, Non-Data Context) "Keyed alike" is the most-cited purchase driver across the last 12 months of product reviews: "great due to their features and being keyed alike," "all keyed alike and $10 per door closer cheaper than Bunnings." (Source: Reviews & UGC) The keyed alike callout currently appears in the product description tab as a blue inline sentence — not visible in the buy box or above the fold. (Source: PDP Screenshot) Rental compliance ("new rental standards — all windows now have to be able to be locked") is a documented purchase trigger appearing in reviews, indicating a buyer segment that purchases multiple units for multi-window installations. (Source: Reviews & UGC)

**V1:** Add three quantity preset buttons directly below the existing quantity selector in the buy box: "10+ — $35.53 each," "20+ — $34.60 each," "30+ — $33.66 each." Clicking a preset populates the quantity field with the minimum for that tier (10, 20, or 30). Style the buttons as outlined chips in the same teal brand colour, smaller than the main CTA. Add a "Keyed Alike" badge directly next to the product title or star rating line — a small teal pill label reading "Keyed Alike." Do not remove the existing bulk pricing table below — keep it as reference. This variation adds two changes: quantity shortcuts and the keyed alike badge.
**Brief:** Desktop: Quantity preset chips sit on one row directly below the -/+ quantity field. Each chip: border 1px teal, rounded corners, label format "10+ saves $X" or "10+ — $35.53 ea." Active state (when user's current quantity matches a tier): filled teal background, white text. Keyed Alike badge: small pill (teal fill, white text, rounded), placed inline after the product title or on the same line as the star rating. Approximately 12px font, 4px padding. The badge should be visible without scrolling on both desktop and mobile. Mobile: Preset chips stack or wrap to two rows if they don't fit in one line at mobile widths. Quantity field and chips sit above ADD TO CART. Keyed Alike badge visible in the first fold. Sequencing: this test targets the buy box and does not conflict with Slot 1 (cart drawer) or Slots 3/4. Can run concurrently.

---

## Slot 3: Dedicated Landing Page — Designer and Trade Audience

**Type:** A/B test (1 variation vs. control)
**Page:** /collections/specials-deals (current landing page for Ads 2 and 3) vs. new dedicated landing page
**Revenue potential:** Ads 2 and 3 both drive paid traffic from audiences explicitly qualified as design-oriented buyers and interior designers. Both currently land on a page with 6,009 undifferentiated sale products and no editorial framing. Even a modest CR improvement on paid traffic translates directly to ROAS improvement on Meta spend.

**Hypothesis:** If we send designer and trade audience traffic (Ads 2 and 3) to a dedicated landing page that mirrors their framing — curated ranges, architectural hardware, trade credentials, Aussie-owned positioning — conversion rate from paid social will increase because visitors currently land on a page that does not match the promise or context of the ad they clicked.

**Data:** Ad 2 (running since November 2025) leads with "Every great design deserves the right hardware" and references architectural handles, precision finishes, and modern colourways. Its landing page is a 6,009-product sale collection with no design editorial framing. (Source: Meta Ads, Landing Page Screenshot) Ad 3 (running since September 2023, the longest-running of the three top ads) positions Keeler as "the preferred suppliers of Door and Architectural Hardware for Interior Designers." Its landing page is the same generic specials page. (Source: Meta Ads) Competitor Designer Doorware uses a three-tier collection structure (Design, Project, Residential) segmented by professional use case, with a Selector Tool for specification. Lo & Co Interiors uses lifestyle photography throughout and explicit 30-day returns messaging. Neither of these approaches is reflected on Keeler's specials landing page. (Source: Competitor Research)

**V1:** Create a dedicated landing page at `/pages/architectural-hardware` (or equivalent) that serves as the destination for Ads 2 and 3. The page should include: a hero section with editorial framing matching the ad copy ("The hardware choice for interior designers and architects"), 4–6 curated product categories shown as lifestyle-adjacent tiles (Door Handles, Cabinet Hardware, Window Hardware, Locks, Finishes, Specials), a short trust section (Aussie-Owned, Trade Pricing, In Stock, Fast Delivery), a selection of featured products in current sale, and a "Help Me Choose" CTA linking to the existing product finder. The page is not a generic collection dump — it is a brand context page with a clear path into the catalogue. Update the URL parameter in Ad 2 and Ad 3 to point to this page for the variation group.
**Brief:** Desktop: Full-width hero with headline, short subheadline (2 lines max), and a single CTA button ("Shop the Range"). Below hero: 2-row grid of 3 category tiles each (6 total), product image + category name + link. Below categories: 3-column trust bar (Aussie-Owned and Operated, Trade Pricing Available, Free Delivery Over $99). Below trust bar: "Featured Products" — 4–6 products with lifestyle or install photography preferred, price shown, "See Options" CTA. Bottom: "Not sure where to start? Help Me Choose" with the existing product finder CTA. Mobile: Hero stacks vertically. Category tiles become a 2-column grid. Trust bar stacks to single column. Product grid 2-column. The page is not a Shopify collection — it is a landing page template. Dev to build as a custom page template or use a page builder. No infinite scroll, no 6,000-product filter sidebar. Keep it focused. Sequencing: this page can be live and tested independently of Slots 1 and 2. No shared components.

---

## Slot 4: Homepage Hero — Post-Sale Value Proposition

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage — keelerhardware.com.au
**Revenue potential:** The homepage is the top entry point for direct and branded traffic. The Autumn Sale hero ends 23 March — 3 days from now. Without a replacement, the homepage defaults to its base state. Testing a value-proposition-led hero in April captures traffic arriving without sale context and gives them a clear reason to browse.

**Hypothesis:** If we replace the post-sale hero with a headline-led value proposition (Keeler's positioning as Australia's specialist hardware supplier, with fast delivery and trade pricing), bounce rate on homepage visits will decrease and category click-through will increase because the current sale hero will be gone and the base homepage provides no clear above-fold reason to continue.

**Data:** The current homepage fold 1 is entirely occupied by the Autumn Sale banner (ends 23 March). When the sale ends, that space reverts to the base homepage. The base homepage was not fully visible in the screenshot as the sale banner was active, but the structure below fold 1 includes trust icons, a Featured Products carousel, and category tiles. (Source: Homepage Screenshot) Reviews confirm the core Keeler advantage: faster and cheaper than Bunnings, in stock when others aren't, phone support accessible, specialist knowledge. These messages currently live in the footer and trust icon bar. (Source: Reviews & UGC) Competitor Lo & Co leads with lifestyle hero copy tied to their design positioning. Zanda leads with residential/commercial segmentation immediately. Keeler's homepage post-sale has no equivalent anchor. (Source: Competitor Research)

**V1:** Replace the hero banner with a 50/50 split layout: left side headline and subtext, right side a product lifestyle image (ideally showing a door handle or lock set in a home context — a shot from the Instagram feed or existing brand photography). Headline: "Australia's Specialist Hardware Supplier." Subheadline: "In stock. Ships fast. Cheaper than Bunnings." Two CTAs side by side: "Shop Door Hardware" and "Help Me Choose." On mobile, the image stacks above the text block, then the two CTAs stack full-width below.
**Brief:** Desktop: Two-column layout, 50/50 split at full viewport width. Left column: headline (H1, large — 36–42px), subheadline (body text, 16–18px, 2 lines max), two side-by-side CTA buttons (primary teal "Shop Door Hardware," secondary outlined "Help Me Choose"). Right column: single lifestyle image, full column height, object-fit cover. Image should show product in context (installed on a door, not white-on-white). If no lifestyle photography is available, use one of the category tile images already in use on the homepage. Mobile: Image block first (16:9 or square crop), then headline, subheadline, then two full-width stacked CTA buttons. Announcement bar (free delivery) remains above header. No countdown timer, no sale messaging. Sequencing: this test targets the homepage hero only. The Featured Products carousel, trust icons, and category grid below fold 1 remain unchanged in both control and variation. This test can run concurrently with Slots 1, 2, and 3 — no shared components.

---

## Future Slot Candidates

1. **Collection page — social proof sort:** Surface products with the most reviews at the top of collection pages. Currently, featured sort shows products with 0 reviews first. Test review-count-weighted sort vs. current featured sort.

2. **PDP photography:** Test adding an installation/lifestyle image to high-traffic PDPs. Even one contextual image alongside the existing white-on-white shots. Requires photography coordination with client.

3. **Free shipping threshold lift:** Test raising the free shipping threshold from $99 to $149 with a stronger "you're X away" message throughout the funnel. Cross-reference with margin data (need Intelligems or Shopify Analytics).

4. **Trade account signup flow:** Reviews and ads both indicate a trade buyer segment (builders, interior designers, property managers). A dedicated trade account program with visible pricing tiers could improve retention and AOV for this segment. Requires non-data context from client on current trade pricing setup.

5. **"Keyed Alike" collection page:** Given the purchase driver strength of the keyed alike feature, a dedicated "Shop Keyed Alike" collection (surfaceable via "Shop By" nav) could capture high-intent buyers searching for this specific capability.
