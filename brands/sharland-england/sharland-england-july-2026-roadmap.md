# Sharland England CRO Research Brief

**Data Sources:** Meta Ads visual summary (3 ads + 3 landing pages), Google Ads visual summary, Trustpilot reviews (2022–2025), PageSpeed / Core Web Vitals (tested 2026-07-13), Site visual summary (homepage, collection, PDP, cart), live site fetch, competitor web research

---

## Insights

Trust signals are structurally misallocated across the site. The Hadley Tray PDP, the brand's top-performing page by design, carries 23 five-star reviews positioned directly below price, a named designer (Louise Roe), and a four-icon trust row. Every other page is empty. The homepage shows press logos from Vogue, AD, The New York Times, and The Telegraph, but no star rating, no customer quote, and no shipping promise. Collection pages show GBP prices on a four-column grid with no review counts on cards. Sharland England has earned real trust signals (4.7 Trustpilot, premium press, named service agents cited years after purchase) and withholds them at the pages where most paid traffic arrives first.

Page performance is eliminating a large portion of paid traffic before the first product interaction. Mobile LCP on the homepage (27.3s) and the Hadley Tray PDP (29.0s), tested 2026-07-13, is catastrophically outside Google's 2.5s threshold. At these scores, visitors arriving from all three active Meta campaigns bounce before the page resolves. Every test in this roadmap runs in the context of a site that is losing a significant fraction of mobile visitors before any element is seen. Performance remediation is not in scope for A/B testing but should run in parallel.

US expansion is the current growth priority but the execution has a direct conversion gap. Ad 3 targets US visitors with "FASTER SHIPPING. NO TARIFFS" and lands them on a US collection page showing GBP prices throughout: £185, £395, £1,075. The "No Tariffs" claim in the ad does not appear on the landing page; the headline resets to "No delays: shipped from our US warehouse" only. Trustpilot reviews confirm US shipping is already working well ("amazed at the speed the Hadley tray arrived" (Source: Reviews, Nov 2023); "Fast shipping!" (Source: Reviews, Jul 2024)), but US visitors see no USD prices, no tariff reassurance, and no shipping timeline on arrival. This is active paid budget converting against unnecessary friction.

Ads 1 and 3 both land on collection pages where a newsletter popup fires on page load with no delay, no scroll trigger, and no exit intent. The popup covers one product slot in the top row of the four-column grid before the user has clicked or scrolled. The same 10% off offer already appears in the top announcement bar above the popup. Two of three active Meta campaigns send traffic directly into this friction. Meanwhile, Ad 2 lands on the Hadley Tray PDP, where no popup fires and conversion signals are strong: this PDP is the cleanest page on the site. The performance gap between the PDP experience and the collection page experience is the most actionable conversion gap in the funnel.

Revenue potential cannot be modelled without session and baseline CR data. Tests are sequenced by evidence strength and expected impact, with the highest-traffic and highest-AOV opportunities prioritised.

---

## Slot 1: Collection Page Popup: Switch to Exit-Intent Trigger

**Type:** A/B test (1 variation vs. control)
**Page:** Outdoor Collection / US Collection (sharland-england.com/collections/outdoor, /collections/us)
**Revenue potential:** Collection page sessions/mo (unknown) x 8–15% conservative CR lift x ~£300 blended AOV = revenue scales directly with paid traffic volume to Ads 1 and 3.

**Hypothesis:** If we change the newsletter popup trigger from on-load to exit-intent, more visitors will reach the product grid before being interrupted, increasing collection-to-cart conversion because the popup currently blocks the first product slot before the user has shown any interest.

**Data:** The popup fires immediately on page load on both the Outdoor Collection (Ad 1 LP) and the US Collection (Ad 3 LP), covering approximately one full product card in the top row of the four-column grid. The 10% discount offer in the popup duplicates the top announcement bar already visible on arrival. Two of three active Meta campaigns land directly on collection pages, making this the first conversion barrier for the majority of paid traffic. Source: meta-ads-visual-summary.md (Ad 1 LP fold 1, Ad 3 LP fold 1), site-visual-summary.md (collection fold 1).

**V1:** Replace the on-load popup trigger with an exit-intent trigger (fires when cursor moves toward the browser address bar on desktop, or after a configured back-gesture signal on mobile). The popup content, offer (10% off), and design remain unchanged. On mobile, the trigger fires after 60 seconds of inactivity or on scroll-back-to-top behavior. On desktop, the trigger fires on upward cursor movement toward the navigation bar. The popup does not appear until the visitor has had the opportunity to browse at least one full row of the product grid.

---

## Slot 2: US Landing Page: USD Pricing for US Visitors

**Type:** A/B test (1 variation vs. control)
**Page:** US Collection (sharland-england.com/collections/us)
**Revenue potential:** US-targeted sessions/mo (unknown) x 10–20% conservative CR lift x ~£200 blended accessories AOV = applies to all traffic driven by Ad 3.

**Hypothesis:** If US visitors see prices in USD rather than GBP, collection-to-cart conversion on the US landing page will increase because GBP pricing creates a comprehension gap for US visitors who clicked an ad promising "FASTER SHIPPING. NO TARIFFS."

**Data:** Ad 3 runs US-targeted creative with "FASTER SHIPPING. NO TARIFFS." The US Collection landing page shows GBP-denominated prices throughout: Hadley Tray Berry £185, Fraises Des Bois Tablecloth £395, Emerson Outdoor Dining Chair Set of 2 £1,075. No currency selector appears in the nav or anywhere on the page. The "No Tariffs" claim from the ad creative is not restated on the landing page; it resets to "No delays: shipped from our US warehouse" only. Trustpilot reviews from US customers confirm willingness to pay and positive shipping experience, but also document pre-purchase logistics anxiety. Source: meta-ads-visual-summary.md (Ad 3 creative, LP folds 1–3), manifest.md open questions, reviews.md.

**V1:** Enable Shopify Markets geolocation-based currency display for US visitors. When a visitor arrives on the US Collection page from a US IP address, all prices display in USD at the current exchange rate. On mobile and desktop, price display changes from "£185.00" to "$[USD equivalent]" across all product cards in the four-column grid. A one-line currency note ("Prices shown in USD. Switch currency.") appears below the page header for transparency. No other page elements change.

---

## Slot 3: Hadley Tray PDP: Shipping Timeline in Buy Box

**Type:** A/B test (1 variation vs. control)
**Page:** Hadley Tray PDP (sharland-england.com/products/hadley-tray)
**Revenue potential:** PDP sessions/mo (unknown) x 5–10% conservative CR lift x £185 AOV = highest-priority PDP on the site per manifest.

**Hypothesis:** If we add an explicit shipping timeline and returns window directly in the buy box, add-to-cart rate will increase because US customers have documented pre-purchase shipping anxiety that the current buy box does not address.

**Data:** The Hadley Tray buy box shows: product name, £185.00 price, 23 five-star reviews, colour selector, quantity input, ADD TO CART button, and a "Ships Globally" icon in the row below the button. No shipping timeline or cost appears in the buy box. The Shipping & Returns accordion is collapsed by default and requires a deliberate click to open. At least three Trustpilot reviews from US customers explicitly mention pre-purchase concern about international shipping, resolved only after receiving the order: "we were concerned about the logistics of shipping to our address; that wasn't necessary" (Source: Reviews). The US warehouse is now active and capable of supporting a faster US shipping promise. Source: site-visual-summary.md (PDP buy box), meta-ads-visual-summary.md (Ad 2 LP), reviews.md.

**V1:** Add one line of text directly below the ADD TO CART button: "UK: 3–5 business days | US: 3–5 days from our US warehouse | Free returns within 30 days." On mobile, this line wraps below the full-width ADD TO CART button. On desktop, it sits in the right-column buy box below the button, above the icon trust row. The Shipping & Returns accordion remains available for full policy details. No other buy box elements change.

---

## Slot 4: Cart: Shipping Estimate + Returns Promise

**Type:** A/B test (1 variation vs. control)
**Page:** Cart (sharland-england.com/cart)
**Revenue potential:** Cart sessions/mo (unknown) x 5–8% reduction in abandonment x ~£370 average observed cart value (2x Hadley Tray) = applies at the highest-intent moment on the site.

**Hypothesis:** If we replace "Shipping calculated at checkout" with a shipping cost estimate or free-shipping threshold, and add a visible returns promise, cart abandonment will decrease because unknown shipping cost is a documented cart-exit trigger and the cart currently provides less trust copy than the PDP.

**Data:** The cart shows item, quantity, subtotal, and "Tax included. Shipping calculated at checkout." No shipping estimate, no free-shipping threshold, and no returns promise appear anywhere in the cart. The only CTA is "CHECK OUT" followed by Shop Pay, PayPal, and Google Pay. Industry data (Baymard Institute) identifies unexpected shipping costs as the number one cause of cart abandonment, cited by 48% of abandoners. A one-star Trustpilot review from Dec 2025 names a returns process communication failure as the sole complaint; the site provides no returns visibility before checkout. Source: site-visual-summary.md (cart), reviews.md (Claire Custance, Dec 2025).

**V1:** Replace the line "Tax included. Shipping calculated at checkout." with two lines: (1) a shipping estimate or free-shipping threshold (e.g., "Free shipping on orders over £X" or "UK shipping: £[rate] | US shipping: £[rate]" - use whichever reflects actual policy); (2) "Free returns within [X] days." Both lines appear in the order summary block below the subtotal, above the CHECK OUT button. On mobile, lines stack below the subtotal. On desktop, they sit in the right-column order summary. No other cart elements change.

---

## Slot 5: Collection Cards: Star Ratings + Review Counts

**Type:** A/B test (1 variation vs. control)
**Page:** All collection pages (Shop All, Outdoor Collection, US Collection)
**Revenue potential:** Collection sessions/mo (unknown) x 3–7% conservative CR lift on collection-to-PDP click-through x ~£185 accessories AOV = applies sitewide across all collection browsing traffic.

**Hypothesis:** If we display star ratings and review counts on product cards in the collection grid, collection-to-PDP click-through will increase because the Hadley Tray's 23 five-star reviews are invisible at the browsing stage, leaving visitors at a brand competing at 3–5x lower-end competitors with no social proof.

**Data:** Every product card across all collection pages shows: product image, product name, price, and colour swatches. No star ratings, no review counts. The Hadley Tray has 23 five-star reviews prominently placed on its PDP. Zero of that social proof is visible in the collection grid or the Bestsellers carousel on the homepage. Sharland England's Hadley Tray is priced at £185 vs. £38–54 for a comparable rattan tray from Birdie Fortescue. At a 4.9x price premium, review counts on product cards are the most direct trust lever available at the browsing stage. Source: site-visual-summary.md (collection page, homepage Bestsellers carousel), reviews.md (23 Hadley Tray reviews, 4.7 Trustpilot average 2022–2025).

**V1:** Add star rating display and review count below the price on all product cards that have at least one review. Format: "★★★★★ (23)" or equivalent: five filled stars with review count in parentheses. On mobile, the star/count row appears below the price in each card. On desktop, the same treatment applies to the four-column grid layout. Cards with zero reviews show no star display. No other card elements change.

---

## Slot 6: Homepage: Trustpilot Badge + Customer Quote Near Hero

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (sharland-england.com)
**Revenue potential:** Homepage sessions/mo (unknown) x 2–5% conservative CR lift x ~£200 blended AOV = applies to all non-PDP, non-collection homepage entry traffic.

**Hypothesis:** If we add a Trustpilot rating badge and one customer quote between the hero carousel and the Bestsellers section, homepage-to-collection or homepage-to-PDP conversion will increase because new visitors currently see zero social proof above the scroll fold.

**Data:** The homepage hero (fold 1) is a full-width lifestyle carousel with a "SHOP GARDEN FURNITURE" CTA. Fold 2 opens the Bestsellers product carousel. The press logo bar (Vogue, The Telegraph, WSJ, NYT, House & Garden, AD, Veranda, Interiors) appears at the bottom of fold 2 or top of fold 3, below the natural scroll fold for most visitors. No star rating, no customer quote, no Trustpilot badge appears anywhere on the homepage. US reviewer verbatims are strong and specific: "It completely makes the entire room!" (VCB, US, Nov 2023); "beautiful handwritten note, cant wait to get more" (kris jezak, US, May 2024). Source: site-visual-summary.md (homepage folds 1–3), reviews.md, live site fetch (4.7 Trustpilot referenced in site metadata).

**V1:** Insert a new section between the hero carousel and the Bestsellers carousel. The section contains: (1) a Trustpilot badge showing the 4.7 rating and star display; (2) one customer quote pulled from existing Trustpilot reviews, with reviewer first name and country. Quote selection should be short, specific, and outcome-focused. For example: "It completely makes the entire room!" or "beautifully packed and with a personal note." On mobile, the Trustpilot badge stacks above the quote in a single-column layout. On desktop, the badge and quote appear side by side in a centred strip. The section uses minimal styling consistent with existing page design, no background color block required.

---

## Slot 7: Cart AOV: Free Shipping Threshold Progress Bar

**Type:** A/B test (1 variation vs. control)
**Page:** Cart (sharland-england.com/cart)
**Revenue potential:** Cart sessions/mo with at least one item (unknown) x £40–80 AOV increase = applies to all sessions where a visitor has added to cart.

**Hypothesis:** If we add a free-shipping threshold progress bar to the cart with recommended accessory products to help visitors close the gap, average order value will increase because the cart currently has no active AOV mechanic and £55–£95 accessories are a credible single-item add from a £185 Hadley Tray baseline.

**Data:** The cart shows a "You May Also Like" section with two product thumbnails and a "View all" link: a passive cross-sell with no incentive. There is no free-shipping threshold bar, no bundle prompt, and no volume incentive anywhere in the cart. The Hadley Tray at £185 sits within one accessory purchase of any plausible free-shipping threshold (Pinet Plant Pot from £95, Concha Dish from £80, Little Flower £55, all confirmed on the PDP "Pairs well with" carousel). Multiple Trustpilot reviews document multi-item and gift purchase intent. Source: site-visual-summary.md (cart, PDP upsell section), meta-ads-visual-summary.md (Ad 2 LP "Pairs well with" carousel), reviews.md (multi-item order patterns).

**V1:** Add a free-shipping threshold progress bar at the top of the cart, above the item list. The bar shows progress toward a threshold (e.g., "You're £[X] away from free shipping") and fills as cart value increases. Directly below the progress bar, show 2–3 recommended accessory products (drawn from the "Pairs well with" product list) with inline "Add" buttons; a single click adds the item to cart without leaving the page. On mobile, the bar and products stack in a single-column layout above the order summary. On desktop, the same treatment appears in the right-column order summary area or as a horizontal strip above the item list.

---

## Slot 8: Ad 1 Juliette Message Match: Collection Hero Banner

**Type:** A/B test (1 variation vs. control)
**Page:** Outdoor Collection (sharland-england.com/collections/outdoor)
**Revenue potential:** Ad 1 sessions/mo (unknown) x 8–12% conservative CR lift x ~£875–£1,375 AOV (Juliette seating and table range) = highest per-session revenue potential in the roadmap given Juliette furniture price points.

**Hypothesis:** If we add a Juliette-specific hero banner at the top of the Outdoor Collection page matching Ad 1's creative messaging, CR on Ad 1 traffic will increase because visitors who clicked an ad about the Juliette collection currently arrive on a generic outdoor page with no Juliette reference.

**Data:** Meta Ad 1 runs a video with the headline "Inspired by antique pieces, our Juliette collection brings timeless charm to outdoor spaces." The landing page is the general Outdoor Collection. Fold 1 shows a full-width hero with no Juliette branding, then fires the newsletter popup. Juliette pieces (£875–£1,395 seating and tables) are mixed into the four-column product grid alongside Emerson and other outdoor lines with no callout. The emotional hook from the ad ("timeless charm," "antique pieces") does not appear anywhere on the page. Source: meta-ads-visual-summary.md (Ad 1 creative, LP folds 1–3).

**V1:** Add a dedicated Juliette banner section at the top of the Outdoor Collection page, above the product grid and before the newsletter popup would appear. The banner includes: a headline referencing the Juliette collection by name (e.g., "The Juliette Collection" or "Timeless charm for outdoor spaces"); a brief subline (one sentence, 10–15 words) echoing the ad's antique-inspired positioning; and a "Shop Juliette" anchor link that scrolls to or filters the Juliette products in the grid below. On mobile, the banner stacks as a full-width text block above the product grid. On desktop, it appears as a hero strip spanning the full content width. The existing product grid and popup behavior remain unchanged.

---

## Future Slot Candidates

1. **PDP "Pairs Well With": One-Click Add or Bundle** - The cross-sell carousel (Pinet Plant Pot £95, Concha Dish £80, Little Flower £55) on the Hadley Tray PDP requires a separate PDP visit per item; adding inline "Add to cart" buttons or a pre-configured bundle would convert a passive editorial element into an AOV driver at peak purchase intent.

2. **Homepage Hero CTA Specificity** - The hero CTA "SHOP GARDEN FURNITURE" is category-specific on a brand homepage serving ceramics, linens, and accessory visitors; a more generalist CTA or a split hero path would reduce mismatch for non-furniture traffic.

3. **Named Service "Chat With Our Team" CTA** - Multiple Trustpilot reviews cite staff by name (Quinn, Katherine, Celia) years after purchase; a direct chat or callback CTA in the PDP or cart could convert this genuine service differentiator into a pre-purchase conversion path.

4. **Unboxing Experience Buy Box Copy** - At least five reviews specifically mention the personal note from Louise and exceptional packing; a single line in the PDP buy box ("Every order includes a personal note from Louise") would pre-sell the full brand experience before add-to-cart.

5. **Branded Search Gap: Competitive Bidding Review** - A competitor display ad appeared in the Sharland England brand search SERP (Google Ads visual); brand search is partially unprotected, warranting a branded keyword defensive campaign review.
