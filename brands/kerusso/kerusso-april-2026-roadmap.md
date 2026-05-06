# Kerusso CRO Research Brief

**Data Sources:** Meta Ads (3 of many active ads), Google Ads Transparency, Reviews & UGC (Trustpilot), Page Speed / Core Web Vitals, Competitor Insights, Site Screenshots (Homepage, BOGO Landing Page, PDP, Best Sellers Collection, Cart Drawer)

---

## Insights

Kerusso's biggest conversion problem is not messaging or design. It is page speed. Two of three active Meta ads (started Feb 20 and Feb 27, 2026) send paid traffic directly to a landing page with a 7/100 mobile score and a 30.8-second LCP. Most mobile users abandon before the offer ever renders.

The brand has strong fundamentals: 4.3/5 stars across 1,585 Trustpilot reviews, a 37-year history, and a hero product (the condiment parody series) with genuine social virality. Customers independently use the same word to describe these shirts: "conversation starters." That is the exact narrative Kerusso uses in every active Meta ad. The message is right. The infrastructure is failing it.

Two friction patterns compound the speed problem. The "Get 15% off" popup fires on page load across every page - PDPs, collection pages, and the BOGO landing page - right when visitors are in buying mode. Immediate popups are the number one cause of mobile bounces per analysis of 1 billion popup displays (Wisepops, 2024). And the cart shows a $54.01 gap to the $79 free shipping threshold with no actionable path to close it. Multiple Trustpilot reviews across 2019-2025 cite shipping cost as a deterrent. A customer completing the BOGO offer (2 shirts = $49.98) still does not qualify for free shipping.

Opportunity estimate (conservative, paid traffic only): the BOGO landing page alone, improved from an estimated 0.5% to 2% mobile CR on 20,000 paid sessions per month, adds approximately $15,000/month from traffic already being paid for. That math does not include cart or PDP improvements.

The three tests below target the three largest friction points in sequence: get users to see the offer, give them a reason to spend more, and stop interrupting them while they are deciding to buy.

---

## Slot 1: BOGO Landing Page - Performance Optimization

**Type:** A/B test (1 variation vs. control)
**Page:** /pages/buy-2-get-1-free
**Revenue potential:** 20,000 sessions/mo (estimated paid traffic, not confirmed without GA) x 1.5% conservative mobile CR lift (est. current 0.5% due to 30.8s LCP, target 2.0%) x $49.98 avg BOGO order = ~$15,000/mo

**Hypothesis:** If we deliver a performance-optimized version of the BOGO landing page, mobile conversion will increase because the current 30.8s LCP causes most visitors to abandon before the offer renders.

**Data:** The BOGO page scores 7/100 on mobile PageSpeed Insights (captured Apr 10, 2026), with an LCP of 30.8s - 12x above Google's 2.5s "Good" threshold. The page carries 7,642 KB total weight with 1,772 KB in available image savings and 1,016 KB of unused JavaScript. Two of three active Meta ads (Library IDs 1393660378754994 and 1982430028973776, running since Feb 2026) send paid traffic directly to this page. (Source: Meta Ads, Page Speed)

**V1:** A performance-optimized version of the BOGO landing page. Changes: lazy-load all product images below the initial viewport; preload only the hero banner image and the 3-step progress indicator above the fold; convert all product images to WebP format; defer the bundle builder JavaScript until after the first user interaction; remove unused CSS and JavaScript dependencies flagged in PageSpeed (1,016 KB JS savings, 1,772 KB image savings). The page layout, copy, offer mechanics (3-step progress bar, "Your Bundle" right-panel sidebar), and product grid remain identical to the control.

On mobile: the hero banner ("BUY 2, GET 1 FREE"), the 3-step progress indicator, and the first row of 4 product cards load in the initial render. All remaining product grid rows load progressively as the user scrolls. The "Your Bundle" sidebar stacks below the product grid (standard mobile behavior).

On desktop: the split-panel layout (product grid left, "Your Bundle" sidebar right) is preserved. All below-fold images are lazy-loaded. The sidebar loads immediately as it is in the initial viewport on desktop.

---

## Slot 2: Cart Drawer - One-Click Upsell to Bridge the Free Shipping Gap

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (site-wide)
**Revenue potential:** 10,000 cart sessions/mo (estimated, not confirmed without GA) x 10% one-click upsell take rate x $24.99 avg upsell item = ~$25,000/mo in additional AOV. RIPT Apparel, a comparable graphic t-shirt brand, saw 7.9% AOV increase from a similar free shipping progress mechanic. Baymard Institute: 80% of online shoppers will meet a minimum purchase threshold to avoid shipping costs.

**Hypothesis:** If we replace the static free shipping progress bar in the cart with a contextual one-click upsell showing the specific item needed to reach free shipping, AOV will increase because customers currently see a $54 gap with no actionable path to close it.

**Data:** The cart drawer (screenshot, Apr 10, 2026) shows "You're $54.01 away from Free Shipping!" on a $24.99 cart. A visual progress bar and truck icon are present, but no product recommendation tied to the gap is visible above the fold. The existing "Recommended For You" section appears partially below the checkout button, but its content was cut off in the screenshot. Multiple Trustpilot reviews across 2021-2025 cite shipping cost as a deterrent, including one customer who stated "won't be ordering again" due to shipping charges (Elizabeth, Jan 2021). 39% of shoppers abandon carts due to extra costs including shipping (Baymard Institute). (Source: Reviews, Site Screenshots, CRO Community Research)

**V1:** In the cart drawer, directly below the free shipping progress bar and above any existing recommendations, add a one-click upsell module. The module headline reads: "Add 1 more shirt to unlock free shipping." The module displays the top-selling condiment series shirt (Catch Up with Jesus, $24.99) with: a product thumbnail, the product name, price, a size selector defaulting to the size already in the cart (or M if cart is empty), and a single "Add to Cart" button. Clicking the button adds the item to the cart instantly and updates the progress bar and cart total without a page reload or drawer close. If the cart already contains 2 or more items (BOGO completed), the module updates dynamically to show the remaining gap and a new recommended item. The checkout button, trust badges (Trusted Seller, Shopify Secure, SSL), cart item controls, and header copy remain unchanged.

On mobile: the module stacks vertically below the progress bar. It is visible without scrolling if the cart contains one item. The "Add to Cart" button is full-width and within thumb reach.

On desktop: the module appears in the same position in the cart drawer panel, same layout as mobile but with slightly wider spacing to match the drawer's desktop width.

---

## Slot 3: PDP - Exit-Intent Popup vs. Immediate Fire

**Type:** A/B test (1 variation vs. control)
**Page:** All product detail pages
**Revenue potential:** 50,000 PDP sessions/mo (estimated across top products, not confirmed without GA) x 0.5% conservative ATC rate improvement x $24.99 avg order = ~$6,250/mo, plus additional recovery of abandoning visitors via exit-intent conversion (exit-intent popups recover an estimated 15% of abandoning visitors per Wisepops 2024).

**Hypothesis:** If we switch the "Get 15% off" popup from immediate page-load trigger to exit-intent trigger, ATC rate will increase because the current popup disrupts visitors in active buying mode, while exit-intent timing captures abandoners at the moment they are most likely to respond.

**Data:** The "Get 15% off" popup fires on page load on all PDPs, visible in site screenshots captured Apr 10, 2026. It is also visible on the BOGO landing page and on collection pages. One reviewer explicitly called out "being asked several times if I want to add another shirt to my order" as a checkout friction point. Immediate popups are the #1 cause of mobile bounces per Wisepops analysis of 1 billion popup displays (2024-2025). Exit-intent popups convert at 3.94%; 92% of top-performing popups display after 4+ seconds while the lowest performers show between 0-4 seconds. Exit-intent can recover 15% of abandoning visitors in ecommerce settings. (Source: Reviews, Site Screenshots, CRO Community Research)

**V1:** Change the "Get 15% off" popup trigger from immediate page load to exit intent. The popup content, design, discount amount (15% off), and email capture field are identical to the control.

On desktop: the popup fires when the cursor moves toward the browser's URL bar or tab area (standard exit-intent detection). It does not fire during normal page interaction (scrolling, hovering over images, selecting sizes).

On mobile: the popup fires when the user scrolls back up past 10% of the page after having scrolled down at least 30% (reliable mobile exit signal). It does not fire on first load or while the user is actively scrolling down.

On both devices: the popup fires a maximum of once per session. It does not fire if the user has already interacted with the popup in the session, added a product to cart, or opened the cart drawer. Users who are actively engaging with the size selector or product images do not see the popup.

---

## Future Slot Candidates

1. **Homepage hero - message match with active ads.** The homepage hero (Apr 10, 2026) promotes the golf collection while Meta ads push the BOGO condiment offer. Testing a hero featuring the condiment series + BOGO offer would align paid and organic traffic into the same conversion path.

2. **Best Sellers collection - add star ratings to product cards.** Product cards on the Best Sellers page show no star ratings. Every visible product has 4.0-4.4/5 ratings with 100+ reviews per product. Adding ratings to product cards is a standard social proof test with low implementation cost.

3. **PDP buy box - featured review quote.** Each PDP has 100+ reviews but no featured quote in the buy box. Pulling the top "conversation starter" review into the buy box above the ATC button would reinforce the core purchase motivation at the moment of decision.

4. **Free shipping threshold reduction.** At $79, the threshold is $29 above the BOGO minimum order ($49.98) and $54 above a single item ($24.99). Testing a reduced threshold ($50 or $60) would align the threshold with realistic purchase patterns and remove the most common shipping cost complaint.
