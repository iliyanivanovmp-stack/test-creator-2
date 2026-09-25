# Poupette St Barth CRO Research Brief

**Data Sources:** Meta Ads and Landing Pages, Google Ads Transparency, PageSpeed / Core Web Vitals, Current Site Screenshots

No trust signal is visible above the fold anywhere in the funnel. Not on the homepage's three folds, not on Ad 2's landing page, not on the collection page, not on the PDP buy box. The only trust-adjacent elements found sit in the footer ("Free shipping," "Secured payment," "Simple returns") or buried in PDP/cart copy, both below where a visitor decides to convert. This pattern repeats across 5 of the 6 collected sources, making it the strongest evidence chain in this audit.

Mobile Core Web Vitals fail Google's "good" thresholds on both pages tested. Homepage LCP is 13.7s and Time to Interactive is 17.1s (Sep 2026 mobile Lighthouse); PDP is worse, at 18.1s LCP and 23.3s Time to Interactive. Both pages score under 0.1 on the LCP metric specifically. CLS is not an issue on either page, the problem is load and interactivity speed. Since both Meta and Google are actively running ads that drive mobile clicks, this speed gap sits directly in the paid traffic path.

Ad-to-landing-page message match is confirmed broken for one live ad and unverifiable for two others. Ad 2 promises general "Saint Barth, everywhere" resort-wear messaging with no named product, then lands visitors on a raw site-search results page for "sasha," breadcrumb, filter panel, and "22 results found" heading, with nothing echoing the ad's headline or caption. This is a confirmed, screenshotted mismatch, not an inferred one.

---

## Slot 1: Add Review Rating to the PDP Buy Box

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (poupettestbarth.com/products/[product])
**Revenue potential:** Not sizeable this cycle, sessions, AOV, and baseline conversion rate were not collected for Poupette St Barth. Flagged high-confidence, unsized in the research audit given the evidence spans 5 of 6 collected sources.

**Hypothesis:** If we add a review star-rating and count badge next to the product title, add-to-cart rate improves because visitors currently see zero trust signals before reaching the price and CTA.

**Data:** The PDP buy box shows product title, colorway, price (€330,00, "Taxes incluses"), a bulleted feature list, then the "AJOUTER AU PANIER" button, with zero review or rating elements found across all 3 captured folds. Source: site-visual-summary.md PDP, all 3 folds.

**V1:** Add a live star-rating and review-count badge (pulled from the store's existing review platform, not a static number) directly beneath the product title, above the price. Everything else in the buy box stays in place: colorway selector, feature bullets, "AJOUTER AU PANIER" button. Mobile: badge sits full-width beneath the title, above the price line. Desktop: badge sits inline beneath the title in the right-column buy box, same position relative to price.

---

## Slot 2: Add a Guarantee Badge to the PDP Buy Box

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (poupettestbarth.com/products/[product])
**Revenue potential:** Not sizeable this cycle, sessions, AOV, and baseline conversion rate were not collected for Poupette St Barth. Flagged high-confidence, unsized in the research audit.

**Hypothesis:** If we move the site's existing shipping and returns badges up to sit beside the Add to Cart button, add-to-cart rate improves because those trust signals currently sit below the purchase decision point.

**Data:** The only trust-adjacent copy on the PDP is "Livraison internationale offerte" below the Add to Cart button and FAQ accordion questions about returns, both positioned below the buy box. The site footer already carries "Free shipping," "Secured payment," and "Simple returns" badges, confirmed via live homepage fetch, but they sit below the fold captured in any screenshot. Source: site-visual-summary.md PDP; live homepage WebFetch, footer badges.

**V1:** Reuse the site's existing footer trust badges ("Free shipping," "Secured payment," "Simple returns") as a compact row directly under the "AJOUTER AU PANIER" button, replacing the current single "Livraison internationale offerte" line in that position. No new copy is introduced. Mobile: three badges stack as a single horizontal row with icons, directly under the button. Desktop: same row, same position, directly under the button in the right-column buy box.

---

## Slot 3: Fix Ad 2's Landing Page to Match Its Ad Promise

**Type:** A/B test (1 variation vs. control)
**Page:** Ad 2 landing page (site search results for "sasha")
**Revenue potential:** Not sizeable this cycle, no ad spend or click-through data was collected. Flagged high-confidence, unsized in the research audit, this is the single confirmed, screenshotted funnel mismatch in the data.

**Hypothesis:** If we replace the raw search-results page with a landing view that echoes Ad 2's headline and product focus, click-to-cart rate from Ad 2 traffic improves because the current page shows no message match at all.

**Data:** Ad 2's creative headline reads "Bring a little Saint Barth wherever you are. Effortless prints, effortless days," caption "St Barth, everywhere." The landing page it sends to opens with a breadcrumb reading "Home / Search: 22 results found for 'sasha,'" a "SEARCH" heading, a pre-filled search box showing "sasha," a left-side filter panel (Gender, Product Type, Size, Material, Color), and a product grid beginning below the fold, none of it echoing the ad's headline or caption. Source: meta-ads-visual-summary.md Ad 2; ad-creative-2.png; ad2-landing-f1/f2/f3.png.

**V1:** Above the existing search results and filter panel, add a hero band carrying the ad's headline ("Bring a little Saint Barth wherever you are") and a single hero image, so the page opens with message match before the product grid. The underlying search/filter functionality stays unchanged and remains reachable by scrolling. Mobile: hero band is full-width, single column, positioned above the breadcrumb. Desktop: hero band spans the full content width above the breadcrumb and filter panel.

---

## Slot 4: Reduce PDP Load Time

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (poupettestbarth.com/products/[product])
**Revenue potential:** Not sizeable this cycle, no sessions or AOV data was collected. Flagged high-confidence, unsized in the research audit, this is the more severe of the two speed failures measured.

**Hypothesis:** If we compress and lazy-load PDP imagery and defer non-critical scripts, mobile Largest Contentful Paint and Time to Interactive drop because the current page fails Google's "good" thresholds by 5-7x.

**Data:** Mobile Lighthouse lab data (2026-09-09) on the PDP shows an 18.1s LCP (score 0), 23.3s Time to Interactive, a 62/100 performance score, and an 8.8s Speed Index, against a page structured with a thumbnail strip and primary product photo on the left and the buy box on the right. Source: pdp-pagespeed.json.

**V1:** Compress and serve the primary product image and thumbnail strip at optimized file sizes, lazy-load all below-the-fold imagery (feature sections, recommendations), and defer non-critical JavaScript until after the buy box renders. No visual layout changes. Mobile: primary image and buy box load first; thumbnails and below-fold content lazy-load on scroll. Desktop: same load sequencing, same layout.

---

## Slot 5: Reduce Homepage Load Time

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (poupettestbarth.com)
**Revenue potential:** Not sizeable this cycle, no sessions or AOV data was collected. Flagged high-confidence, unsized in the research audit.

**Hypothesis:** If we compress the hero media and defer non-critical scripts, mobile Largest Contentful Paint and Time to Interactive drop because the homepage is the first impression for all display and awareness traffic and currently fails Google's "good" thresholds by roughly 5.5x.

**Data:** Mobile Lighthouse lab data (2026-09-09) on the homepage shows a 13.7s LCP (score 0), 17.1s Time to Interactive, a 64/100 performance score, and a 5.5s Speed Index, against a full-bleed hero video/image with headline "THE SEASON'S ESSENTIALS" and a "SHOP" link. Source: homepage-pagespeed.json.

**V1:** Replace the full-bleed hero video with a compressed static hero image (or a shorter, compressed video loop) and defer non-critical JavaScript until after the hero renders. No copy or layout changes. Mobile: compressed hero asset loads first, same headline and "SHOP" link position. Desktop: same treatment, same layout.

---

## Slot 6: Add Sale/Compare Pricing to the Collection Page

**Type:** A/B test (1 variation vs. control)
**Page:** Collection page ("NEW COLLECTION")
**Revenue potential:** Not sizeable this cycle, no sessions or AOV data was collected. Flagged directional, unsized in the research audit.

**Hypothesis:** If we add a compare-at price or "10% OFF" badge to collection tiles, click-through to PDP improves because the site already runs a site-wide 10% first-order offer in its announcement bar, but none of that value shows on the product tiles themselves.

**Data:** The collection page ("NEW COLLECTION," 103 products) shows every tile with a single straight price (e.g., "€390,00"), no compare-at or strikethrough pricing, no sale badges, across all 3 captured folds, despite the site running a site-wide 10% first-order offer in its announcement bar. Source: site-visual-summary.md Collection Page, "Price display" note; live homepage WebFetch, announcement bar.

**V1:** Add a small "10% OFF FIRST ORDER" badge to each product tile, positioned above or beside the existing single price, tied to the same offer already live in the site's announcement bar. No compare-at pricing is invented since no confirmed markdown pricing was found in this data. Mobile: badge sits in the top corner of each tile, above the price. Desktop: same badge position, consistent across the grid.

---

## Slot 7: Make the PDP Add to Cart Button Sticky

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (poupettestbarth.com/products/[product])
**Revenue potential:** Not sizeable this cycle, no sessions or baseline conversion data was collected. Flagged high-confidence, unsized in the research audit.

**Hypothesis:** If we make the "AJOUTER AU PANIER" button sticky once a visitor scrolls past the buy box, add-to-cart rate improves because the button currently scrolls out of view by fold 3, right as the visitor is reading shipping and FAQ content.

**Data:** "AJOUTER AU PANIER" is a full-width black button positioned below the product description and size guide on fold 2. By fold 3, as the visitor scrolls into the shipping/returns accordions and FAQ, the button has scrolled entirely out of view with no sticky or fixed replacement. Source: site-visual-summary.md PDP, "CTA behavior" note.

**V1:** Once a visitor scrolls the primary "AJOUTER AU PANIER" button out of view, a slim sticky bar appears fixed to the bottom (mobile) or top (desktop) of the viewport, carrying the product name, price, and an "AJOUTER AU PANIER" button. It disappears again if the visitor scrolls back up to the original button. Mobile: sticky bar fixed to the bottom of the viewport. Desktop: sticky bar fixed to the top of the viewport, below the site header.

---

## Slot 8: Add Product/Offer Specificity to the Homepage Hero

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (poupettestbarth.com)
**Revenue potential:** Not sizeable this cycle, no sessions or baseline conversion data was collected. Flagged directional, unsized in the research audit.

**Hypothesis:** If we add a featured product, price, and the existing first-order offer to the homepage hero, click-through to shop improves because the current hero carries no product, price, or offer specificity despite an active discount already running above it.

**Data:** Fold 1 of the homepage shows a full-bleed lifestyle image, the generic headline "THE SEASON'S ESSENTIALS," and a single unstyled "SHOP" link, with no featured product, price, or time-bound call to action, despite an active 10% first-order discount already running in the announcement bar directly above it. Source: site-visual-summary.md Homepage Fold 1; live homepage WebFetch.

**V1:** Keep the existing full-bleed lifestyle image and "THE SEASON'S ESSENTIALS" headline, and replace the single "SHOP" link with a featured product name, its price, and a line referencing the existing first-order offer already live in the announcement bar (e.g., "10% off your first order"). Mobile: featured product name, price, and offer line stack beneath the headline, above the CTA. Desktop: same three elements sit beneath the headline in the same hero band.

---

## Future Slot Candidates

1. **Confirm Ad 1 and Ad 3 landing pages match their ad promise** - Ad 1 ("handmade, limited runs") and Ad 3 ("The Sasha: our best-seller") have no landing page screenshots collected, so it's unknown whether they carry the same message-match break confirmed on Ad 2.
2. **Align Google Ads and Meta Ads messaging** - Google Ads run "Iconic Prints, Timeless Cuts" and seasonal collection framing while Meta Ads run handmade/craft and best-seller framing, with zero copy overlap between the two channels, a creative/strategy decision rather than a single-page test.
3. **Clarify the cart page UI pattern (drawer vs. full page)** - The captured screenshot filename suggests a cart drawer, but the capture shows a full mobile cart page; the actual live pattern needs confirming before this can be sized as a test.
4. **Review the English-locale PDP experience** - The PDP was captured on the French-language site while homepage and collection were captured in English, so the PDP experience for English-primary traffic has not been directly reviewed in this audit.
5. **Investigate the Girls Clothing line as a separate funnel** - Google Ads Transparency shows a kids' Girls Clothing line and a "10% off your First Order" offer not represented anywhere in the Meta creatives collected.
