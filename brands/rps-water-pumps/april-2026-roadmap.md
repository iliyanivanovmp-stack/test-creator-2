# April 2026 Testing Roadmap

**Data Sources:** Shopify Analytics, GA4, Heatmaps (Microsoft Clarity), Customer Segmentation Survey, Site Search, Meta Ads, Reviews & UGC, Email Campaigns, Winning Tests Library, Current Site Screenshots, Client Communication

---

## Insights

RPS Water Pumps generates $320K/mo on 62,805 sessions with a $726 AOV (Feb 12 - Mar 14, 2026). The business is growing: gross sales up 15.6% and AOV up 11.5% month over month. But the conversion rate is stuck at 0.51%, and the add-to-cart rate at 1.66%. For every 100 visitors, 98 leave without putting anything in their cart. This is the structural problem. Traffic and product quality are not the issue. The site experience is.

The data points to where RPS wins and where the site fails to show it. Service is the #1 purchase decision driver at 4.3/5, above price at 4.0/5 (Customer Survey, n=101). The email campaigns feature BBB accreditation, a 4-step Customer Success Team (Intro Call, Sizing Specialist, Packing Agent, On-Call Engineer), and a 100% Water Assurance Guarantee. None of these appear on the website. Meanwhile, new reviews continue to document extreme DIY savings: one customer quoted $25,000-$30,000 for professional installation and completed the job himself for $3,200 (Rick Wallace, March 2026). "Support has been amazing. Don't change!" writes a 3-year repeat customer (Mark Hull, Feb 2026). The strongest conversion assets live in email inboxes and review databases, not on the pages where purchase decisions happen.

Heatmap data reveals exactly where visitors struggle. On mobile (64% of traffic), the hamburger menu is the #2 most-tapped element (298 taps, 5.14%), but it opens to a text-only list with no images or guided entry points. On desktop, search is the #1 clicked element (185 clicks, 6.81%), suggesting visitors can't find what they need through browsing alone. The homepage loses 40% of mobile visitors by the time they scroll past the hero, and 50% are gone by fold 2. The add-to-cart popup is empty: no trust signals, no upsells, no shipping info, no order total on the checkout button.

Four tests, four distinct funnel stages. Homepage restructure (landing), gallery layout (PDP), cart drawer (checkout intent), and navigation (sitewide discovery). Conservative estimates put the combined opportunity at $100K+/mo in incremental revenue: ~8,000 homepage sessions x 0.4% ATC lift x $726 AOV = $23,232/mo on homepage alone. These tests also serve as validation for the upcoming theme rebuild. Every winner becomes a design decision backed by data, not opinion.

---

## Slot 1: Homepage Hero + Fold 2 Restructure

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (/)
**Revenue potential:** ~8,000 homepage sessions/mo x 0.4% ATC lift x $726 AOV = ~$23,232/mo

**Hypothesis:** If we replace the promotion-first homepage hero with a value-proposition-first hero that leads with DIY savings and social proof, and replace the discount-stacking category grid with a need-based guided selector and trust bar, the homepage add-to-cart rate will increase because the current layout buries RPS's strongest competitive advantages (expert support, $2K-$30K in savings vs. professional install) and provides zero navigation help for an audience with moderate knowledge (3.1/5) that overwhelmingly arrives via search (61%).

**Data:** The homepage is the #1 revenue page: $70K+ revenue, 22.84% of all key events, 1m 30s avg engagement on 8,081 sessions (Source: GA4, Feb 12 - Mar 13, 2026). The sitewide session-to-ATC rate is 1.66%, with 98.34% drop-off (Source: Shopify Analytics, Feb 12 - Mar 14, 2026). Heatmap scroll data shows the hero-to-fold-2 transition is the biggest exit point: on mobile, 40% of visitors leave by 15% scroll (right below the hero) and 50% are gone by 20% scroll. On desktop, 15% drop at the hero transition and 37% by fold 2 (Source: Heatmaps, Microsoft Clarity, last 30 days). The current hero is a full-width sale banner ("DIY YOUR WELL SALE / 50% OFF Pump Kits") with no value proposition, no social proof, and no differentiation. Fold 2 is four category tiles each leading with a discount percentage. Every element above the fold is price/promo (Source: Site Screenshots).

Service is the #1 purchase decision driver at 4.3/5, above price at 4.0/5 (Source: Customer Survey, n=101). RPS has 531+ reviews at 4.86/5 with customer service as the dominant theme, and named reps called out repeatedly (Source: Reviews & UGC). New reviews document savings of $3,200 vs. a $25,000-$30,000 professional quote (Rick Wallace, March 2026) and $2K vs. $6K-$9K (earlier review). The email campaigns reveal trust assets invisible on the site: BBB A+ accreditation, a 4-step Customer Success Team, 100% Water Assurance Guarantee, and Google/Facebook star ratings (Source: Email Campaigns, March 2026). Aqua Science displays BBB accreditation and 3,100+ reviews prominently, while RPS's higher-rated reviews are invisible on the homepage (Source: Competitor Research).

Heatmap click data confirms navigation engagement: search is the #1 desktop click (185 clicks, 6.81%), and on mobile, "Shop Well Pump Kits" is #1 (303 taps) with the hamburger menu at #2 (298 taps) (Source: Heatmaps). Site search shows 192+ combined searches for submersible well pump variants in the last 30 days (Source: Site Search, Feb 12 - Mar 14, 2026). The Winning Tests Library supports every element: homepage banner copy clarity (+$19,441/mo), need-based product finder (+$17,813/mo), collection page hero with reviews (+$114,870/mo), social proof near purchase elements (+$6,635/mo).

**V1: Value-prop hero + trust bar + need-based category selector**

Fold 1 (Hero): Replace the full-width sale banner with a value-proposition hero. Left side (text): headline "Replace Your Well Pump Yourself. Save Thousands." Subheadline: "Complete DIY kits with everything you need. Free sizing help from our water pump engineers." Below the subheadline: "4.86 stars from 531 reviews" with stars rendered visually in brand orange. Below the star rating: a customer quote in italics, rotated from a set of 3 on each page load: (1) "Quotes ran from $25K-$30K. I did it myself for $3,200." (2) "As a 65 year old woman, my daughter and I installed this pump ourselves." (3) "Support has been amazing. Don't change!" Each quote attributed with first name and state. Two CTAs side by side: primary "Shop Pump Kits" (filled brand orange button) and secondary "Get Free Sizing Help" (outlined button, links to the well pump sizing calculator). Right side (image): keep the existing lifestyle installation photo or similar real-customer installation imagery. The current sale offer ("50% OFF Pump Kits" or whatever the active promo is) moves to a smaller banner bar directly below the hero, not inside it. The promo is still visible, but the hero leads with value, not price.

Trust bar (between hero and fold 2): A horizontal strip with four items evenly spaced, each with a small icon: (1) "Engineer Phone Support" with phone icon and (855) 560-5670, (2) "531 Five-Star Reviews" with star icon, (3) "BBB Accredited, A+ Rating" with BBB icon, (4) "Free Shipping on Pump Kits" with shipping icon. On mobile, this wraps to two rows of two items. This replaces the current abrupt jump from hero to category tiles.

Fold 2 (Need-based category selector): Replace the four discount-percentage category tiles with a need-based selector. Section heading: "What Do You Need?" Tiles framed around the customer's problem, not the product category. Tile 1: "Replacing a Well Pump?" with a well pump lifestyle image, links to /collections/residential-water-pumps. Tile 2: "Fixing Low Water Pressure?" with a booster pump image, links to /collections/booster-pumps. Tile 3: "Need Parts for an Install?" with parts/fittings image, links to /collections/all-pump-install-parts. Tile 4: "Treating a Pond or Fountain?" with pond image, links to /collections/ponds-and-fountains. Each tile shows the problem headline, one-line description (e.g., "Complete kits from $499. Everything you need in one box."), and a "Shop Now" link. No discount percentages on the tiles. Desktop: 4-column grid. Mobile: 2x2 grid. Active promotions can appear as small "Sale" badges on tiles, but the copy leads with the need.

**Brief:** Design: Hero layout is 60/40 text-to-image split on desktop, full-stack (image top, text below) on mobile. Headline in bold, 36px desktop / 28px mobile. Star rating rendered as 5 orange stars with "4.86 from 531 reviews" in 16px. Customer quote in 14px italic. CTA buttons 48px height, primary in brand orange (#E8501C or nearest brand value), secondary outlined. Trust bar: light gray or white background, 60px height desktop, icons 24px, text 14px medium weight. Need-based tiles: rounded corners (8px), subtle shadow, problem headline in 20px bold, description in 14px, "Shop Now" as text link in brand orange. Dev: Shopify homepage section replacement. Three sections (hero, trust bar, category selector) replace the current hero banner + category tile grid. Customer quote rotation: simple JS array with random index on page load. Trust bar is static HTML/CSS. Need-based tiles link to existing collection URLs. Promo banner bar below hero should be editable via Shopify's theme customizer so the client can update sale messaging without code changes.

**Sequencing note:** Independent of Slot 2 (PDP gallery). Different pages, can run simultaneously. If March tests surface a winning headline angle or trust element, incorporate before launch. This test is also a theme rebuild prototype: if the value-prop hero and need-based tiles win, they define the homepage direction for the new theme.

---

## Slot 2: PDP Gallery Layout Overhaul (All PDPs)

**Type:** A/B test (1 variation vs. control)
**Page:** All product detail pages sitewide. Primary measurement on the top 5 by revenue: One and Done Kit (/products/one-and-done-easy-well-pump-install), 3HP Eco-Steady Booster (/products/3hp-continuous-pressure-booster-pump), 1HP Submersible 230RPS10, Everything but the Pipe Kit (/products/everything-but-the-pipe-kit-for-easy-install), 5HP Submersible 230RPS50.
**Revenue potential:** ~15,000 PDP sessions/mo x 0.3% ATC lift x $726 AOV = ~$32,670/mo

**Hypothesis:** If we restructure the product gallery from a multi-row thumbnail grid to a vertical thumbnail strip with main-image navigation arrows on desktop, and add navigation arrows with an image counter on mobile, add-to-cart rate will increase because the gallery is the most interacted-with component on PDPs across both devices, yet the current layout fails both: on desktop it creates an unusable wall of tiny thumbnails on complex products (20-30+ images) with no sequential browsing, and on mobile it offers no image counter or navigation arrows on products with 20-30+ images, leaving users swiping blind through the largest engagement driver on the page.

**Data:** The session-to-ATC drop-off is 98.34%, the biggest leak in the funnel (Source: Shopify Analytics, Feb 12 - Mar 14, 2026). The gallery is the most interacted-with component on PDPs across both devices. On mobile, the top 3 tapped elements are all gallery thumbnails: 142 taps (2.97%), 123 taps (2.57%), and 118 taps (2.47%) out of 4,785 total taps on 2,938 page views. On desktop, the same pattern: the top 3 clicked elements are gallery thumbnails at 112 clicks (3.52%), 105 clicks (3.30%), and 100 clicks (3.14%) (Source: Heatmaps, Microsoft Clarity, last 30 days). Visitors are actively trying to browse product images, but the current layout works against them. The 1HP Eco-Steady Booster has 30+ images in a 4+ row thumbnail grid, the One and Done Kit has 20+ images in 3 rows (Source: Site Screenshots). On desktop, there are no next/previous arrows on the main image, so the only way to browse is clicking individual thumbnails. The "Click to expand" overlay button adds visual clutter. On mobile, there is no image counter, so users on a 30-image product have no idea how much content they're missing. 64% of traffic is mobile (Source: Shopify Analytics, Feb 12 - Mar 14, 2026). The client has confirmed this is a priority: "for desktop I definitely want a new format, I just don't know what could work best for mobile" (Source: Client Communication, March 2026). The gallery optimization case study produced +$15,824/mo, with "more human context = better performance" as the key finding (Source: Winning Tests Library).

**V1: Vertical thumbnail strip + navigation arrows**

Desktop: Replace the multi-row horizontal thumbnail grid below the main image with a single-column vertical thumbnail strip to the left of the main image. Up/down scroll arrows appear at the top and bottom of the strip when thumbnails exceed the visible area (5-6 visible). Add left/right navigation arrows on the main image for sequential browsing. Remove the "Click to expand" overlay button. Zoom still activates on click of the image itself (existing lightbox/expanded view, just no overlay button). The main image expands to fill the width freed by removing the thumbnail grid below it. Buy box stays in its current position to the right.

Mobile: Add left/right navigation arrows on the main image only (in addition to existing swipe). Add an image counter badge ("1 / 20") in the bottom-right corner of the main image. Remove the "Tap to zoom" overlay button. Zoom still activates on tap. Thumbnail strip below the main image remains as horizontal swipe with no arrows - users scroll through thumbnails by swiping, and tap any thumbnail to jump to that image in the main viewer.

**Brief:** Design: Desktop vertical thumbnail strip, 80px wide, positioned to the left of the main image. Thumbnails are square, ~70px, with 4px gap. Active thumbnail gets a 2px border in brand orange. Up/down arrow buttons at top and bottom of strip, visible only when thumbnails exceed viewable area. Main image left/right arrows: semi-transparent white circles with chevrons, vertically centered on the image, 40px diameter, visible on hover. Mobile arrows: same style, 32px, always visible. Image counter badge: dark semi-transparent pill ("1 / 20") in bottom-right, 12px white text. Dev: Shopify product gallery component replacement. Build as a new section/snippet that replaces the existing gallery on all PDP templates. Vertical strip reads from the same product image array. Scroll behavior on the thumbnail strip: smooth scroll, one thumbnail per arrow click. Main image arrows cycle through the image array sequentially. Zoom behavior: clicking/tapping the main image opens the existing expanded view. The overlay buttons are removed but the click/tap-to-zoom functionality remains. This test doubles as a prototype for the theme rebuild: if it wins, the new gallery pattern carries directly into the new theme.

---

## Slot 3: Cart Drawer Format Test (Right Slide-Out vs. Top Dropdown)

**Type:** A/B test (1 variation vs. control)
**Page:** Sitewide (triggers on any add-to-cart action). Primary measurement on the top 5 PDPs by revenue: One and Done Kit, 3HP Eco-Steady Booster, 1HP Submersible 230RPS10, Everything but the Pipe Kit, 2HP Eco-Steady Booster.
**Revenue potential:** 1,044 add-to-carts/mo x 3% ATC-to-complete lift x $726 AOV = ~$22,700/mo

**Hypothesis:** If we replace the current half-screen top-down cart dropdown with a standard right-side slide-out cart drawer, the ATC-to-checkout rate will increase because the top dropdown format is unconventional, takes up half the screen without clear focus, and breaks the expected interaction pattern that most e-commerce shoppers are trained on - a right-side drawer that keeps them oriented on the page while showing their cart contents.

**Data:** The current add-to-cart interaction opens a half-screen dropdown from the top, showing the product added, a subtotal, and two buttons: "View cart" and "Checkout" (Source: Site Screenshots, March 2026). Of 62,805 sessions in the last 30 days, 1,044 add to cart (1.66%), but only 560 reach checkout (0.89%) and 321 complete (0.51%) (Source: Shopify Analytics, Feb 12 - Mar 14, 2026). The ATC-to-checkout drop is 46%. The ATC-to-complete drop is 69%. At $726 AOV, these are high-value carts being abandoned.

Cart drawer case studies from the Winning Tests Library: checkout button with price + lock icon produced +$389,565/mo, focused upsell + single trust signal produced +$40,313/mo, trust signals + savings visibility produced +$32,605/mo (Source: Winning Tests Library). Before layering in upsells, trust signals, or threshold promos, this test isolates the format variable first: does a right-side drawer outperform the current top dropdown as a container? If it wins, subsequent tests can layer in conversion elements (upsells, trust signals, price-on-button) on top of the winning format.

**V1: Right-side slide-out cart drawer**

Replace the current top-down dropdown with a right-side slide-out drawer (full viewport height on both desktop and mobile). The drawer contains the same core information as the current dropdown, presented in the standard right-drawer format:

Header: "Your Cart (X items)" with an X close button.

Cart items: Product thumbnail, name, variant, quantity selector, line price. Vertical list format that accommodates multiple items cleanly.

Checkout button: Full-width button at the bottom of the drawer. Text: "Checkout" with the cart subtotal. Below: a "View Cart" text link for users who want the full cart page.

Desktop: Drawer width 420px, slides in from right with a dark overlay on the page behind it. Mobile: Full-width drawer, same slide-in behavior. All elements stack vertically. Dismissible by clicking the overlay, the X button, or pressing Escape.

This is a clean format test. No upsells, no trust signals, no threshold promos. Same information, different container. This establishes the baseline for the drawer format before adding conversion elements in future iterations.

**Brief:** Design: Drawer background white, header 56px with bold text and X icon. Cart items: 80px square thumbnails, product name in 14px, price in 16px bold. Quantity selector: simple +/- buttons. Checkout button: 56px height, brand orange background, white text, full width, sticky at the bottom on mobile. "View Cart" link below in 14px, underlined. Dev: Build as a Shopify section/snippet that replaces the current top-down cart dropdown behavior. The drawer triggers on any add-to-cart event via AJAX (same trigger as the current dropdown). Cart contents read from the same Shopify cart API. The drawer should be dismissible by clicking the overlay, the X button, or pressing Escape. Keep the implementation simple and modular so upsells, trust signals, and other elements can be added in future test iterations without rebuilding the drawer.

**Sequencing note:** This test is independent of Slots 1, 2, and 4. It targets a different stage of the funnel (post-ATC) and does not conflict with homepage, PDP, or navigation changes. Can run simultaneously with all other April tests.

---

## Slot 4: Mobile Navigation + Desktop Mega Menu Overhaul

**Type:** A/B test (1 variation vs. control)
**Page:** Sitewide (header navigation). Primary measurement on homepage, collection pages (/collections/residential-water-pumps, /collections/booster-pumps), and the top 3 PDPs by session volume.
**Revenue potential:** ~40,000 mobile sessions/mo x 0.1% ATC lift x $726 AOV = ~$29,040/mo

**Hypothesis:** If we replace the text-only mobile menu with a visual navigation that includes product images and a prominent sizing quiz CTA, and enhance the desktop mega menu with visual product cards, the sitewide add-to-cart rate will increase because the current navigation offers no visual cues for an audience with moderate product knowledge (3.1/5), forces technical category decisions before showing any products, and buries the sizing tools that address the #1 purchase barrier (not knowing which pump to buy).

**Data:** The mobile hamburger menu is the #2 most-tapped element on the homepage: 298 taps, 5.14% of all interactions in the last 30 days (Source: Heatmaps, Microsoft Clarity). On desktop, the search bar is the #1 clicked element at 185 clicks (6.81%), and the Submersible Well Pumps nav item is #3 at 83 clicks (3.05%) (Source: Heatmaps). Site search totals 2,859 searches in 30 days, dominated by submersible well pump variants (192+ combined) and accessory searches: pressure tank (36), foot valve (58), poly pipe (41), pressure switch (22) (Source: Site Search, Feb 12 - Mar 14, 2026). 47 searches for "one and done" variants suggest visitors can't find the #1 revenue product through navigation alone.

The current mobile menu is text-only: six category names with dropdown chevrons, two calculator buttons, and large empty space below (Source: Site Screenshots). No product images, no bestseller shortcuts, no guided entry point for new visitors. The desktop mega menu for Submersible Well Pumps shows 30+ text links across 4 columns (by voltage, HP, GPM, well depth) with no images. The Booster Pumps mega menu already includes a featured product image (3HP Eco-Steady), confirming the theme supports visual elements (Source: Site Screenshots).

Customer knowledge level is 3.1/5 and familiarity with RPS is 3.7/5 (Source: Customer Survey, n=101). 61% of visitors arrive via search with no prior brand familiarity. The visual mega menu case study produced +$43,544/mo by replacing text links with product thumbnails: "navigation became a browsing tool, not just utility" (Source: Winning Tests Library). The quiz-in-menu case study produced +$101,495/mo by placing a quiz CTA at the top of the mobile menu (Source: Winning Tests Library).

**V1: Visual mobile menu with quiz CTA + desktop mega menu with product cards**

Mobile menu:

Top of menu (new): A prominent card with "Not Sure Which Pump You Need?" headline, subtext "Get sized in 60 seconds," and a "Take the Quiz" CTA button in brand orange. This links to the Well Pump Sizing Calculator. The card has a subtle background color or border to distinguish it from the category list below.

Category list (enhanced): Each top-level category gets a small product thumbnail (48px) to the left of the category name. Submersible Well Pumps: thumbnail of a submersible pump. Booster Pumps: thumbnail of the 3HP Eco-Steady. Fountains & Aeration: thumbnail of a pond aerator. Well Plumbing: thumbnail of the One and Done Kit. Self Install DIY Kit: thumbnail of a kit box/layout. These thumbnails add visual context without requiring the user to tap into a subcategory to understand what's in each section.

Below categories (new): "Bestsellers" section with 2-3 horizontal product cards showing thumbnail, product name, star rating, and "Shop" link. Products: One and Done Kit, 3HP Eco-Steady Booster, 1HP Submersible. These provide direct shortcuts to high-revenue products for returning visitors and reduce the steps to purchase.

Desktop mega menu (enhanced, Submersible Well Pumps only for V1):

Keep the existing 4-column text structure (by voltage, HP, GPM, well depth) but add a 5th column on the right: a featured product card area showing 2 products stacked vertically. Product 1: "Most Popular" badge + One and Done Kit image, name, star rating, "Shop Now" link. Product 2: "Best for Deep Wells" badge + 5HP Submersible image, name, star rating, "Shop Now" link. This mirrors the Booster Pumps mega menu pattern (which already has a featured product) and gives shoppers a direct path to high-revenue products without parsing 30+ text links.

**Brief:** Design: Mobile quiz card: white or light background with brand orange border-left (4px) or subtle shadow, "Not Sure Which Pump You Need?" in 18px bold, subtext in 14px, CTA button 44px height in brand orange. Category thumbnails: 48px square, rounded corners (4px), positioned left of category name with 12px gap. Bestsellers section: heading "Bestsellers" in 16px bold, horizontal scroll on mobile, product cards 120px wide with 60px thumbnail, name in 12px, star rating in 10px. Desktop featured product column: 240px wide, product cards stacked with 16px gap, "Most Popular" / "Best for Deep Wells" badges in small colored pills (brand orange / dark gray), product image 200px wide, name in 14px, star rating rendered as orange stars, "Shop Now" text link. Dev: Mobile menu modifications use the existing Shopify theme drawer component. The quiz card and bestsellers section are new elements injected above and below the existing nav list. Category thumbnails are static images mapped to each nav item (one image per top-level category). Desktop mega menu enhancement adds a new column to the Submersible Well Pumps dropdown only (V1 scope). Featured products are hardcoded handles that can be updated via theme settings. The existing text links and structure remain unchanged. Only additions, no removals. This minimizes dev risk and allows rollback to the exact current state if needed.

**Sequencing note:** This test modifies the sitewide navigation header, which appears on every page including the homepage. It does not conflict with Slot 1 (homepage hero + fold 2) because the navigation is a separate component above the hero. Both can run simultaneously. If the mobile quiz CTA drives significant traffic to the sizing calculator, that data informs whether to add a similar CTA to PDPs or collection pages in future months.

---

## Future Slot Candidates

Tests that emerged from the data but didn't fit into April's 4 slots:

1. **Ponds & Fountains Landing Page Message Match** (carried from March Slot 1 if not yet launched). GA4 still shows 25s engagement and $0 revenue on 1,527 sessions. 2 of 3 top Meta ads drive pond traffic to wrong pages. High urgency if March test hasn't launched.

2. **Blog-to-Product Pathway Optimization.** Pressure tank FAQ blog gets 1,792 sessions and 2m 02s engagement but only 0.95% of key events. Blog readers are highly engaged but have no conversion pathway. A contextual product recommendation module within blog content could capture this traffic.

3. **One and Done Kit PDP Social Proof + Savings Calculator.** The #1 revenue product ($43.9K/mo) has 2m engagement and 10.81% of key events but no social proof near the ATC button, no savings comparison, and reviews buried below the fold. Carried from March Slot 2.

4. **Collection Page Hero + Labels.** Residential Water Pumps collection gets 1,538 sessions and 1m 20s engagement. The winning tests library's collection page optimization produced +$114,870/mo. Adding a hero with value prop, star ratings on product cards, and urgency/use-case labels could significantly improve collection page conversion.

5. **Sitewide Sticky ATC Bar on Mobile.** 64% of traffic is mobile. A sticky bar that appears on scroll with product name, price, and "Add to Cart" button could reduce the friction of scrolling back up on long PDPs (the One and Done Kit PDP is very long).
