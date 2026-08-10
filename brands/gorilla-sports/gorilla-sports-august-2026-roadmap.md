# Gorilla Sports CRO Research Brief

**Data Sources:** manifest, Meta, Google Ads, PageSpeed JSON, context, site, live fetch, competitors

Gorilla Sports has strong offer match from ads to landing pages, but weak decision support at the first product choice. Meta Ad 1 promotes discounted home gym and bench equipment. Meta Ad 2 promotes complete home gym packages. Both land on the same "Kuntosalipaketit" collection page, which shows discounts up to -55%, product ratings, red sale prices, compare-at prices, savings labels, filters, sorting, and black "Hinta voimassa vain 7 päivää" strips. It does not show a package chooser, comparison guide, or trust strip near the first decision. Source: Meta, site, Google Ads, competitors.

The same issue appears on the Parallel Bars page. Meta Ad 3 promises small-space training, durable frame, beginner-to-advanced use, and chest, shoulder, and core outcomes. Fold 1 shows four product cards with -47% to -72% discounts, ratings, prices, and urgency strips, but it does not turn those claims into visible comparison criteria. Source: Meta, site.

Trust proof exists, but it is not consistently placed where shoppers decide. The homepage shows 4.3 rating, 7000+ reviews, 100,000+ customers, 30-day return, a Finnish claim, and AA credit rating. The PDP shows 55 reviews for "Saadettava kasipainosarja 30 kg." The cart shows secure payments, 30-day return, and 2-year warranty. Collection landing decisions rely mostly on card-level ratings and sale mechanics. Source: site, live fetch.

The PDP and cart already have strong commerce signals. The risk is density and missed framing. The "Säädettävä käsipainosarja 30 kg" PDP shows 45.95 EUR sale price versus 109.95 EUR compare-at price, a sticky add-to-cart, 55 reviews, and a 75.85 EUR bundle. The cart drawer shows the product, quantity, checkout CTA, and trust panel, but no upsell, cross-sell, bundle reminder, or free-shipping threshold. Source: site.

Speed is a real constraint on paid entry pages. Mobile Lighthouse collected on 2026-08-10 shows homepage performance 55/100 with LCP 5.4s and TBT 630ms. The collection page shows performance 61/100 with LCP 4.3s and TBT 740ms. No desktop PageSpeed, AOV, sessions, CVR, device split, or revenue data was collected, so revenue math remains directional: unknown sessions/mo x conservative lift x unknown AOV = unknown EUR. Source: PageSpeed JSON, site.

## Slot 1: Gym Package Finder Above Product Grid

**Type:** A/B test (1 variation vs. control)
**Page:** Kuntosalipaketit collection page (exact ad landing URL not provided)
**Revenue potential:** unknown sessions/mo x 3-6% CR lift x unknown AOV = unknown EUR.

**Hypothesis:** If we add a goal, space, level, budget, and equipment finder above the grid, more paid visitors will reach a relevant gym package because the current page forces Ad 1 and Ad 2 shoppers to self-compare complete setups from a dense grid.

**Data:** Meta Ad 1 promotes discounted home gym and bench equipment, Meta Ad 2 promotes complete gym packages, and both use the same "Kuntosalipaketit" page. The page shows intro copy, carousel, filters, sorting, and a product grid, but no selector for goal, space, level, budget, or equipment need. Source: Meta, site, Google Ads, competitors.

**V1:** On mobile, place a compact finder directly under the intro and above the carousel or first grid decision, using five tap choices: goal, available space, training level, budget, and equipment type. On desktop, use the same choices as a horizontal guided panel above the grid. Keep the existing carousel, filters, sorting, sale badges, ratings, prices, savings labels, and urgency strips unchanged.

## Slot 2: Parallel Bars Claim Match Tiles

**Type:** A/B test (1 variation vs. control)
**Page:** Parallel Bars landing page (exact ad landing URL not provided)
**Revenue potential:** unknown sessions/mo x 2-4% CR lift x unknown AOV = unknown EUR.

**Hypothesis:** If we turn Ad 3 claims into visible comparison tiles before the product cards, more shoppers will understand which parallel bars fit their use case because Fold 1 currently shows discounts and prices without the ad's small-space, durability, beginner, advanced, chest, shoulder, or core decision cues.

**Data:** Meta Ad 3 promotes small-space parallel-bar training for chest, shoulders, core, beginners, and advanced users. The landing page shows four cards with -47% to -72% discounts, ratings, prices, and education below the grid, but Fold 1 does not turn those claims into comparison criteria. Source: Meta, site.

**V1:** On mobile, add a two-row claim tile strip under the title and above filters with labels for small spaces, durable frame, beginner friendly, advanced training, chest, shoulders, and core. On desktop, show the same tiles in one compact row above the four-card grid. Keep the existing filters, sorting, product cards, discounts, ratings, prices, and urgency strips unchanged.

## Slot 3: Collection Trust Strip Near First Decision

**Type:** A/B test (1 variation vs. control)
**Page:** Collection landing pages (exact ad landing URLs not provided)
**Revenue potential:** unknown sessions/mo x 2-4% CR lift x unknown AOV = unknown EUR.

**Hypothesis:** If we move existing page-level proof near the first grid decision, more shoppers will trust the collection before comparing products because the current landing pages show product-card ratings but not the homepage, PDP, or cart proof near the choice point.

**Data:** The homepage shows 4.3 rating, 7000+ reviews, 100,000+ customers, 30-day return, Finnish claim, and AA credit rating. PDP and cart proof also exist, but collection landing decisions do not show page-level proof near the first grid decision. Source: Meta, site, live store fetch.

**V1:** On mobile, add a slim trust strip directly above the product grid using only existing proof: 4.3 rating, 7000+ reviews, 100,000+ customers, 30-day return, Finnish claim, and AA credit rating. On desktop, place the same proof strip above the grid and below filters or sorting. Keep product-card ratings, prices, sale badges, savings labels, and urgency strips unchanged.

## Slot 4: Product Card Decision Hierarchy

**Type:** A/B test (1 variation vs. control)
**Page:** Collection product grids (exact ad landing URLs not provided)
**Revenue potential:** unknown sessions/mo x 2-5% CR lift x unknown AOV = unknown EUR.

**Hypothesis:** If we simplify the product-card hierarchy around rating, product title, price, savings, and one clear next action, more shoppers will compare products faster because current cards make discounts, savings labels, urgency strips, and promotional buttons louder than product differences.

**Data:** The shared landing examples include -49%, -43%, -51%, and -55% discounts. The Parallel Bars page includes -47% to -72% discounts. Collection cards stack discount badges, sale prices, compare-at prices, savings labels, ratings, urgency strips, and savings-style buttons. Source: Meta, site.

**V1:** On mobile, keep the product image, title, rating, sale price, compare-at price, and one savings label, then place the black "Hinta voimassa vain 7 päivää" strip below the price block instead of competing with the card's first scan. On desktop, apply the same hierarchy across the grid so each card has a consistent image, title, rating, price, savings, urgency, and action order. Keep the same products, discounts, ratings, prices, and buttons.

## Slot 5: Homepage Hero Path Split By Goal

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (https://gorillasports.fi/)
**Revenue potential:** unknown sessions/mo x 1-3% CR lift x unknown AOV = unknown EUR.

**Hypothesis:** If the homepage hero offers goal-based paths instead of one category-specific promotion, more shoppers will find the right category because Google Ads demand spans many equipment types while Fold 1 currently pushes "Taljalaitteet jopa -50%."

**Data:** Homepage Fold 1 uses black/red gym photography, headline "Sinun kotisi. Sinun salisi.", and one red "Taljalaitteet jopa -50%" block. Google Ads mention weights, pull-up bars, mats, kettlebells, benches, adjustable weights, push-up bars, barbell sets, step boards, ankle straps, jump ropes, and leg weights. Source: site, Google Ads, live store fetch.

**V1:** On mobile, keep the existing hero image, headline, and header structure, but replace the single red category block with three stacked goal paths: build a home gym, train strength, and add accessories. On desktop, show the same three paths side by side in the hero area. Keep the existing homepage trust strip below the hero unchanged.

## Slot 6: Cart Drawer Add-On Module

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (sitewide cart)
**Revenue potential:** unknown cart sessions/mo x 3-8% AOV lift x unknown AOV = unknown EUR.

**Hypothesis:** If we add a relevant add-on module inside the cart drawer, AOV should increase without disrupting checkout because the current drawer captures purchase intent but shows no upsell, cross-sell, bundle reminder, or free-shipping threshold.

**Data:** The cart drawer shows product details, quantity controls, remove icon, fixed black "Siirry kassalle" button, and trust panel for secure payments, 30-day return, and 2-year warranty. No upsell, cross-sell, bundle reminder, or free-shipping threshold is visible. Source: site.

**V1:** On mobile, add one compact add-on module between the cart item and fixed checkout button, with one product recommendation area and a small add button. On desktop, place the same module in the drawer below the cart item and above the trust panel. Keep the fixed "Siirry kassalle" button, product details, quantity stepper, remove icon, and trust panel unchanged.

## Slot 7: PDP Bundle Explanation

**Type:** A/B test (1 variation vs. control)
**Page:** Säädettävä käsipainosarja 30 kg PDP (exact PDP URL not provided)
**Revenue potential:** unknown PDP sessions/mo x 2-5% PDP add-to-cart lift x unknown AOV = unknown EUR.

**Hypothesis:** If we explain why each checked add-on belongs in the bundle and clarify that the shopper can adjust options, more shoppers will add the 75.85 EUR bundle because the current bundle shows items and total price without explaining the workout role of each add-on.

**Data:** The PDP Fold 2 frequently-bought-together block shows three checked bundle items, a 75.85 EUR total, black add-to-cart, and an option dropdown. The base product is 45.95 EUR versus 109.95 EUR compare-at price. Source: site.

**V1:** On mobile, keep the three checked bundle items, total price, option dropdown, and black add-to-cart, then add one short benefit line under each checked item explaining how it completes the workout. On desktop, use the same benefit lines inside the existing Fold 2 bundle block. Keep the default checked state and pricing unchanged.

## Slot 8: Buy Box Proof Compression

**Type:** A/B test (1 variation vs. control)
**Page:** Säädettävä käsipainosarja 30 kg PDP (exact PDP URL not provided)
**Revenue potential:** unknown PDP sessions/mo x 1-3% PDP CR lift x unknown AOV = unknown EUR.

**Hypothesis:** If we compress proof and payment details into a cleaner buy-box sequence, more shoppers will reach add-to-cart because the current PDP Fold 1 stacks many trust, price, offer, delivery, and payment elements into one dense purchase area.

**Data:** PDP Fold 1 shows rating, 55 reviews, brand, title, bullets, discount badge, 45.95 EUR sale price, 109.95 EUR compare-at price, savings label, add-to-cart, payment/invoice box, stock/delivery copy, limited-time offer box, and trust bullets. One purchase option is visible, and a sticky add-to-cart appears lower. Source: site.

**V1:** On mobile, keep rating, 55 reviews, title, sale price, compare-at price, savings label, and black add-to-cart visible in the primary buy box, then compress payment, stock/delivery, limited-time offer, and trust bullets into two expandable rows below the CTA. On desktop, keep the same sequence in the right buy box with the expandable rows below the CTA. Keep the product imagery, sticky add-to-cart, price values, review count, and purchase option unchanged.

## Future Slot Candidates

1. **Mobile LCP optimization for paid entry pages** - Mobile Lighthouse collected on 2026-08-10 shows homepage LCP 5.4s and collection LCP 4.3s, so this should move up once a development slot is available.
2. **Collection filter shortcut chips** - Collection landing pages show filters and sorting, but no shortcut chips for small spaces, complete sets, beginners, heavy lifting, budget, or highest rated.
3. **Search landing-page routing audit** - Google Ads cover many categories, so category-specific landing coverage should be audited beyond the three Meta landing screenshots.
4. **External trust proof validation** - Treenikauppa's public Trustpilot profile showed strong third-party review volume, while Gorilla Sports review sources were skipped in this collection.
