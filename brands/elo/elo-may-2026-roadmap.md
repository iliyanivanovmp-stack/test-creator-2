# ELO CRO Research Brief

**Data Sources:** Meta Ads, Reviews & UGC, Page Speed, Competitor Research, Site Screenshots

---

## Insights

ELO's Vagabond is well-liked by the buyers who get what they expected. The problem is that too many buyers don't know what to expect. Amazon reviews from the past year show a recurring pattern: customers add to cart, purchase, then discover their primary game doesn't work. COD Mobile, Wuthering Waves, and several Hoyoverse titles are all confirmed incompatible by verified reviewers. The controller isn't the failure — the buying experience is. Buyers are making a $99.99 decision without the information they need.

Three separate data sources point to the same gap. Reviews surface game compatibility as the top return driver. The PDP puts compatibility details inside collapsed accordions that require deliberate user action to open. And when ELO's own retargeting ad sends warm traffic back to the page with a 15% discount offer (code ELO15, live since April 25, 2026), that page shows no trace of the discount. The ad makes a promise. The landing page doesn't keep it.

The cart drawer is a third opportunity sitting unused. Today it shows one product, a quantity selector, and a checkout button. The Ascend Pro Thumbsticks ($19.99) are the natural impulse add-on — compatible, affordable, and praised in reviews for their stick feel. ELO is leaving every cart that touches checkout without a single upsell offer.

The PDP — the page that receives all paid ad traffic — has a 7.9-second LCP from real mobile users (PageSpeed Insights field data, May 4, 2026). That's nearly double the 4-second "poor" threshold. Every mobile visitor waits close to 8 seconds for the page to load. At $99.99 AOV, with active multi-platform paid campaigns running, fixing the conversion environment on this page is the highest-leverage move.

Conservative estimate: 4,000 monthly sessions to the Vagabond PDP. A 1% conversion rate lift at $99.99 AOV = $4,000 in incremental monthly revenue. The three tests below target three distinct failure points across the funnel.

---

## Slot 1: Game Compatibility Surfaced in the Buy Box

**Type:** A/B test (1 variation vs. control)
**Page:** Vagabond PDP (https://eloesports.com/products/elo-vagabond-mobile-gaming-controller)
**Revenue potential:** 4,000 sessions/mo x 1% conservative CR lift x $99.99 AOV = $4,000/mo (session count is an estimate based on active multi-platform paid campaigns; actual impact scales with real traffic volume)

**Hypothesis:** If we move game compatibility information out of the collapsed accordion and into an always-visible module above the fold, conversion rate will increase and return rate will decrease, because buyers can confirm their specific use case before purchasing instead of discovering incompatibility post-purchase.

**Data:** Amazon reviews from verified purchasers repeatedly cite discovering their primary game is incompatible only after purchase: "I have no complaint about the controller itself...I realized it doesn't support my game even though a cheaper controller does." COD Mobile, Wuthering Waves, and Battle Prime are all named as non-functional. On the current PDP, compatibility is addressed via a collapsed "COMPATIBILITY" accordion in fold 2 and a 12-question FAQ section further down the page. Neither appears in the first fold where the purchase decision forms. (Source: Reviews, Site Screenshots) The CRO ebook notes that FAQs moved higher on paid-traffic landing pages produce measurable revenue lifts, because visitors carry an unspoken checklist of questions and answering them faster reduces exit. (Source: CRO Ebook, Ch. 7)

**V1:** Add a "Works With Your Games?" module to the Vagabond PDP, placed immediately below the four trust badges (30-Day Return, 2-Year Warranty, 24/7 Support, Built for Winners) and above any additional content. The module has a dark card background matching the site's aesthetic.

The header reads: "Officially Supported Platforms & Games." Below the header, two columns display platform and game tiles with clear visual indicators. Left column lists confirmed-compatible platforms: Xbox Cloud Gaming, PlayStation Remote Play, NVIDIA GeForce NOW, Steam Link, Xbox Console Streaming, plus the top compatible mobile games (Fortnite Mobile, Minecraft, Genshin Impact — only titles that are genuinely confirmed compatible). Right column is not present in V1; this is a single-column list with bold platform names and 2-3 representative games per platform. At the bottom of the module, a single line in smaller text reads: "Not all mobile games support external controllers. Check your game's settings for controller support before purchasing." A text link labeled "Full compatibility list" anchors to the existing FAQ section below.

On mobile: the module renders as a full-width card below the trust badge grid, above the fold break. The platform list stacks vertically. Each platform is a single line with a checkmark icon and the platform name in bold. The "Full compatibility list" link appears below. The module is not collapsible — it is always visible on load.

On desktop: the module appears in the right-column buy box area, below the trust badge grid, full width of the buy box column. Same content, same layout. The "Full compatibility list" link is present.

Do not remove the existing COMPATIBILITY accordion. This variation adds the new module; the accordion remains for users who want the deeper technical spec.

---

## Slot 2: Cart Drawer — Ascend Thumbstick Upsell

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (sitewide — fires for all orders containing the Vagabond)
**Revenue potential:** 4,000 PDP sessions/mo x 15% estimated ATC rate = 600 cart views/mo x 8% upsell acceptance x $16.99 (Ascend at 15% off) = $815/mo AOV lift. Cart sessions are estimated; acceptance rate is based on industry benchmarks for relevant in-cart upsells. (Source: Shopify Upsell Conversion Benchmarks 2026)

**Hypothesis:** If we add a one-click Ascend Pro Thumbstick upsell in the cart drawer at a 15% discount, average order value will increase without impacting conversion rate, because the Ascend is a low-cost, directly compatible accessory that complements the Vagabond purchase and costs less than 20% of the cart total.

**Data:** The current cart drawer shows the Vagabond line item, a quantity adjuster, a $99.99 subtotal, and a checkout button. The space between the product and the button is entirely blank — no upsells, no accessories, no cross-sells of any kind. (Source: Site Screenshots) The Ascend Pro Thumbsticks ($19.99) are sold on the site and are explicitly designed as a Vagabond companion product. Reviews praise the controller's stick feel as a purchase driver; premium replacement thumbsticks are the natural complement for users who want to customize further. At $19.99, the Ascend is 20% of the Vagabond's cart value — within the ideal upsell range (under 25-30% of cart). (Source: CRO Ebook Ch. 10, CRO Community Research) The CRO ebook states that the best pre-purchase cart upsells are discounted, relevant, one-click, and priced well below the main item — all of which apply here.

**V1:** Add an upsell block to the cart drawer, positioned in the blank space between the Vagabond line item and the "Subtotal" line. The block sits above the subtotal, above the "Shipping calculated at checkout" line, and above the checkout button.

The block contains: a compact product card with the Ascend Pro Thumbsticks image (small thumbnail, left-aligned), the product name "ASCEND Pro Thumbsticks," a strikethrough price of $19.99 crossed out, the discounted price $16.99 in white bold text, a short descriptor line "Drift-proof upgrade for your Vagabond," and a full-width "Add to Order" button in the brand's purple color. Clicking "Add to Order" adds the Ascend to the cart in one tap with no page redirect or drawer close. The cart total and subtotal update instantly. The upsell block collapses after the item is added and is replaced by the Ascend line item in the cart.

On mobile: the full upsell block renders vertically between the Vagabond item and the subtotal. The product image is 48px wide, left-aligned. Text and button stack beneath it. The "Add to Order" button is full-width of the drawer.

On desktop: same layout and positioning within the drawer sidebar. The block does not reflow or change structure relative to mobile.

If the cart contains multiple items (not only the Vagabond), the upsell block still renders unless the Ascend is already in the cart. Implement logic to suppress the block if Ascend is already added.

---

## Slot 3: Retargeting Landing Page — ELO15 Discount Confirmed

**Type:** A/B test (1 variation vs. control)
**Page:** Vagabond PDP — served to retargeting traffic via UTM parameter on the ELO15 ad (https://eloesports.com/products/elo-vagabond-mobile-gaming-controller)
**Revenue potential:** Conservative estimate of 500 retargeting sessions/mo (warm, high-intent traffic from the ELO15 retargeting ad active since April 25, 2026) x 3% conservative CR lift x $84.99 (after 15% discount) = $1,275/mo. Retargeting traffic is a subset of total PDP traffic; lift should be measured on this segment specifically.

**Hypothesis:** If visitors arriving from the ELO15 retargeting ad see an immediate, persistent on-page confirmation of the 15% discount, conversion rate for this segment will increase, because the promise made in the ad is fulfilled on landing rather than requiring the visitor to remember and manually apply a code at checkout.

**Data:** Ad 3 (Library ID: 967616809062103, active since April 25, 2026) is a retargeting ad that explicitly offers 15% off with the code ELO15. The ad headline reads "Finish What You Started." The Vagabond PDP, which is the landing page for this ad, shows no reference to the ELO15 offer, no banner, no price modification, and no visual confirmation that the discount is available. The visitor must recall the code from memory, find the discount field at checkout, and apply it manually. Research shows that any discount used to generate a click must be confirmed on the landing page: "If you're using a discount to stop the scroll, that discount needs to be on the landing page too." (Source: CRO Community Research, Replo Blog) Limited-time offers surfaced on landing pages lift conversion rates by 20-30%. (Source: CRO Community Research)

**V1:** For visitors arriving via the ELO15 retargeting UTM, serve a modified version of the Vagabond PDP with two changes:

**Change 1 — Discount banner:** A dismissible full-width banner appears directly below the purple announcement bar (30-Day Return | 2-Year Warranty | 24/7 Support). The banner reads: "Your 15% off is ready. Use code ELO15 at checkout." followed by a "Copy Code" button that copies ELO15 to clipboard on click. The banner background is a distinct purple tone (slightly lighter than the nav bar) with white text. A dismiss (X) button is visible on the right. The banner persists across scroll and does not push page content down — it overlays below the top nav area.

On mobile: the banner appears below the sticky announcement bar, above the hero image. It is dismissible. The "Copy Code" button is tappable and copies the code to clipboard with a brief "Copied!" confirmation state. The banner does not shift the page layout — it slides down from below the nav as the page loads.

On desktop: same position, same behavior. The banner spans full page width.

**Change 2 — Buy box price treatment:** In the buy box, below the star rating and above the compatibility badges, add a single line: "Save 15% with code ELO15." The line is in the brand's purple text, small font (14px), directly under the $99.99 price. No strikethrough price is shown (since the discount applies at checkout, not on the page). This reinforces the offer at the exact moment the visitor is looking at the price.

On mobile: the "Save 15% with code ELO15" line sits directly below the $99.99 price figure, above the compatibility badges row. Same font, same purple color.

On desktop: same position in the right-column buy box. No layout change otherwise.

Do not change the hero, product images, trust badges, or any other page elements in this variation.

---

## Future Slot Candidates

- **Homepage hero — phone-in-controller hero image:** The current homepage hero shows the Vagabond without a phone inserted. Replacing with an in-use shot (controller gripping a phone mid-game) would make the product immediately legible to first-time visitors and mirror the ad creative context. Multiple reviews cite immediate visual connection as a purchase driver.
- **PDP — "Works with phone cases" callout in the buy box:** The top purchase driver from reviews is case compatibility, yet this differentiator is not visible in the fold-1 buy box. A small icon or line in the buy box ("Works with your phone case") could reduce a common pre-purchase objection without requiring a new section.
- **Page speed remediation:** The Vagabond PDP has a 7.9s real-user LCP on mobile. Reducing page weight (8.7MB) and eliminating render-blocking resources would lift performance and create a better baseline for all CRO tests. This is a dev project, not an A/B test, but it is foundational.
- **Bundle offer on PDP:** No bundle or multi-product offer is visible on the Vagabond PDP in the buy box. A "Complete Setup" bundle (Vagabond + Ascend + Link cable at a combined discount) would increase AOV and compete more directly with GameSir G8 Plus at the $99 price point by reframing the offer.
