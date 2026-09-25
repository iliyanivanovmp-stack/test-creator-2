# Hears CRO Research Brief

**Data Sources:** Google Ads Transparency, PageSpeed/Core Web Vitals, Current Site Screenshots + live WebFetch verification, Social & Community Research (last30days-ecom), Reviews & UGC, Competitor research (self-researched)

Two independent third-party sources contradict the site's own trust claim. Hears' homepage and PDP repeat "Rated 4.9/5 by 200,000+ customers" in the hero and buy box, but Trustpilot shows a 3.5 TrustScore on 1,284 reviews and Amazon shows 3.8/5 on 232 ratings for the Hears One Ear Plugs listing — Source: Social & Community Research (last30days-ecom, 2026-09-13). This gap sits directly on the two highest-traffic conversion surfaces on the site.

Both key pages paint fast but take dramatically longer to become usable. Lighthouse (2026-09-13) shows LCP of 1.7s (homepage) and 2.4s (PDP), both good, but Total Blocking Time of 8,590ms on the homepage and 17,600ms on the PDP, pushing Time to Interactive to 65.6s and 85.9s — Source: PageSpeed/Core Web Vitals. The floating "Ask a question" AI-chat widget, UGC video carousels, and embedded review modules appear on every screenshot fold and are the likely contributors.

Google Ads segment traffic by use case (sleep, moto, festival, concert) with headlines like "Earplugs for Sleep - Blocks snoring" and "Best Earplugs for Motobike Rides" — Source: Google Ads Transparency. Live WebFetch (2026-09-13) confirms 100% of that traffic lands on one Pacha-festival hero regardless of ad intent, and the ad-stated offers ("45% Off," "Buy 2 & Get 10% Off") don't match the live sitewide offer ("BUY 2, GET 1 FREE"). Separately, live WebFetch resolved an open question from data collection: the PDP's true default variant is "Brass Blue," not the "Pacha Edition 2.0" shown in the original screenshot captures, which reflected a search click-through state, not the default landing state.

Monthly sessions and AOV were not collected for Hears, so no revenue opportunity estimate can be shown without inventing numbers. Every slot below uses the conservative lift ranges the audit supports and states the calculation as "revenue unknown" rather than guessing sessions.

---

## Slot 1: Fix Ad-to-Homepage Message Mismatch

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (hears.com)
**Revenue potential:** Sessions/mo unknown x 0.5-1% CR lift x $43-46 AOV = revenue unknown (sessions/mo not collected).

**Hypothesis:** If we swap the homepage hero headline, subhead, and CTA to match the visitor's incoming Google Ads use case (sleep, moto, festival, concert), add-to-cart rate will rise because visitors will see language that matches what they clicked, instead of a festival image with no connection to their intent.

**Data:** Google Ads Transparency shows 7+ distinct use-case headlines ("Earplugs for Sleep - Blocks snoring," "Best Earplugs for Motobike Rides," etc.), but live WebFetch confirms the homepage hero has zero dynamic variation and shows only "The most iconic earplug is back for the 2026 season" with CTA "SHOP PACHA EDITION" for every visitor, regardless of ad clicked. Source: Google Ads visual summary; live homepage WebFetch (2026-09-13).

**V1:** Keep the existing Pacha hero background image and layout unchanged. Swap only the headline, subhead, and CTA copy based on the incoming ad's use-case parameter (sleep, moto, festival, concert), falling back to the current Pacha copy for organic/direct traffic and any use case without a matched variant. Example: a "sleep" click sees headline "Block snoring, sleep through the night" with CTA "SHOP SLEEP EARPLUGS" instead of "SHOP PACHA EDITION." Mobile and desktop: same copy swap logic, no layout change on either.

---

## Slot 2: Fix Catastrophic Total Blocking Time on Homepage and PDP

**Type:** Immediate Fix
**Page:** Homepage and PDP (hears.com)

**Issue:** Both pages paint fast (LCP 1.7s homepage, 2.4s PDP) but take 65.6s (homepage) and 85.9s (PDP) to become interactive. Total Blocking Time is 8,590ms on the homepage and 17,600ms on the PDP, 14-29x over the 600ms "poor" threshold. This is a functional defect, not a hypothesis to test: at this level, buttons, swatch selectors, and carousels lag or fail to respond regardless of what content sits on the page.

**Data:** PageSpeed/Core Web Vitals JSON (homepage + PDP, fetched 2026-09-13): Performance scores 0.59 (homepage) / 0.55 (PDP). The floating "Ask a question" AI-chat pill, UGC video carousels, and embedded review widgets appear on every captured fold on both pages and are the likely script-weight contributors, though the JSON does not name specific scripts.

**Fix:** Audit and defer or lazy-load the third-party scripts behind the chat widget, video carousels, and review modules so they load after first interaction rather than blocking it. Re-run Lighthouse on homepage and PDP after each script change to confirm TBT drops below the 600ms threshold before moving to the next script.

---

## Slot 3: Reconcile the Rating Discrepancy Between Site and Third-Party Platforms

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage and PDP (hears.com)
**Revenue potential:** Sessions/mo unknown x 0.5-1% CR lift x $43-46 AOV = revenue unknown (sessions/mo not collected).

**Hypothesis:** If we replace the ambiguous "Rated 4.9/5 by 200,000+ customers" claim with a specific, sourced rating line, conversion rate will improve because shoppers who cross-check Amazon or Trustpilot before buying will see a claim the site can stand behind instead of a number that contradicts what they find elsewhere.

**Data:** The PDP buy box shows "★★★★★ 4,736 Reviews" directly under the product title, and both homepage and PDP repeat "Rated 4.9/5 by 200,000+ customers." Trustpilot shows a 3.5 TrustScore on 1,284 reviews and Amazon shows 3.8/5 on 232 ratings for the Hears listing, corroborated across two independent platforms. Source: last30days-ecom (Trustpilot + Amazon); live PDP/homepage WebFetch (2026-09-13).

**V1:** Replace "Rated 4.9/5 by 200,000+ customers" in the hero and PDP buy box with "4.9/5 based on 4,736 verified on-site reviews," tied to the on-site review count already shown in the PDP buy box. No claim about off-site platforms is added or removed, this only makes the existing on-site number the visible source of the rating instead of an unattributed customer count. Mobile and desktop: same copy change, no layout change on either.

---

## Slot 4: Correct the Swatch-Availability Contradiction on PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (hears.com)
**Revenue potential:** Sessions/mo unknown x 0.3-0.5% CR lift x $43-46 AOV = revenue unknown (sessions/mo not collected).

**Hypothesis:** If we make the stock-status message change when a shopper selects an unavailable color swatch, add-to-cart rate will improve because shoppers will no longer read "In stock ready to ship" next to a swatch that carries a diagonal strike-through for that exact color.

**Data:** The "Color: Pacha Edition 2.0" swatch row has 9 swatches, 1 with a diagonal strike-through indicating that color is unavailable, positioned directly beside a green-dot "In stock ready to ship" status line with no text distinguishing "this color is out" from "the product is in stock." Source: site-visual-summary.md, PDP Fold 1.

**V1:** Keep the swatch row and strike-through indicator unchanged. When a shopper selects the struck-through swatch, replace the green "In stock ready to ship" line with "This color is currently unavailable. Other colors in stock." The green in-stock message returns automatically when an available swatch is selected. Mobile and desktop: identical logic, no layout change on either.

---

## Slot 5: Surface a Lower-Cost Path to the Free-Shipping Threshold in Cart

**Type:** A/B test (1 variation vs. control)
**Page:** Cart (hears.com)
**Revenue potential:** Sessions/mo unknown x 0.3-0.8% AOV lift x $50 avg cart = revenue unknown (sessions/mo not collected).

**Hypothesis:** If we add a $9-12 accessory item to the cart drawer's cross-sell carousel alongside the existing $43 core-product cross-sell, AOV will rise because shoppers who are $38 short of the $50 free-shipping threshold will have a lower-friction way to close that specific gap instead of only seeing an add-on that overshoots it by $5.

**Data:** The cart drawer shows "You're $38 away from free shipping" ($50 threshold) directly above a cross-sell carousel whose only visible item is the full-price core product ($43), which overshoots the $38 gap. Source: cart screenshot description, site-visual-summary.md.

**V1:** Keep the free-shipping progress bar and existing $43 cross-sell item unchanged. Add a $9-12 accessory item (e.g. cleaning kit or carry pouch tier) to the same cross-sell carousel, positioned first, so shoppers seeing "$38 away" have an item close to that specific dollar gap next to the existing option. Mobile and desktop: same carousel order on both.

---

## Slot 6: Align PDP Default Variant With Paid-Traffic Intent

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (hears.com)
**Revenue potential:** Sessions/mo unknown x 0.3-0.6% CR lift x $43-46 AOV = revenue unknown (sessions/mo not collected).

**Hypothesis:** If paid and search traffic lands on the confirmed default "Brass Blue" variant instead of being routed to "Pacha Edition 2.0" via URL parameters, add-to-cart rate will improve because shoppers will arrive on a fully-stocked variant instead of one with a partial-OOS swatch (see Slot 4).

**Data:** Live WebFetch (2026-09-13) confirms "Brass Blue" is the PDP's true default variant, but collection-page and search click-throughs push shoppers to "Pacha Edition 2.0" via a `?variant=...&_psq=pacha` query string. Source: manifest open question resolved via live WebFetch; collection and PDP screenshots.

**V1:** Change the collection-page and search-result links that currently carry the `?variant=...&_psq=pacha` parameter so they land on the PDP's default "Brass Blue" variant instead. The PDP itself is unchanged; only the entry variant for this traffic changes. Mobile and desktop: same link change on both.

---

## Slot 7: Move Trust Badges Higher on the PDP Buy Box

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (hears.com)
**Revenue potential:** Sessions/mo unknown x 0.3-0.5% CR lift x $43-46 AOV = revenue unknown (sessions/mo not collected).

**Hypothesis:** If we move the "100-day money back guarantee" and "2 Year Warranty" badges from below the Add to Cart button and cart-drawer-only to directly above the buy box, add-to-cart rate will improve because shoppers will see risk-removal copy at the same point they weigh the rating discrepancy (Slot 3), not after they've already decided.

**Data:** The "100-day money back guarantee" checkmark line currently sits below the black "ADD TO CART" button, and the "2 Year Warranty" / "100-Day Free Returns" badges only appear in the cart drawer, not on the PDP itself. Source: PDP and cart screenshot descriptions, site-visual-summary.md.

**V1:** Move the "100-day money back guarantee," "2 Year Warranty," and "100-Day Free Returns" badges from their current positions (below CTA, cart-only) to a single row directly above the price/rating block at the top of the PDP buy box. No copy changes, same badge icons and text. Mobile and desktop: same row placement, stacked to fit width on mobile if needed.

---

## Slot 8: Fix Unloaded Placeholder Images on the Collection Page

**Type:** Immediate Fix
**Page:** Collection page (hears.com)

**Issue:** The Hears Sleep grid, Accessories grid, and Merch grid (collection page Folds 2-3) render as gray placeholder blocks with faded or missing product photography in the captured screenshots. This sits directly in the browse-to-PDP path for any visitor not going straight to the hero bestseller.

**Data:** Site-visual-summary.md, Collection Fold 2-3. 3 of 3 lower-fold product grids affected in the captured state. Not re-verified live in this pass, WebFetch returns text only, not rendered images.

**Fix:** Manually re-check the collection page live on both mobile and desktop to confirm whether this is a persistent bug or a lazy-load timing artifact at capture time. If persistent, fix the image loading for the Sleep, Accessories, and Merch grids so product photography renders on page load without requiring a scroll-triggered re-render.

---

## Future Slot Candidates

1. **Clarify the "GET A FREE SET OF HEARS" collapsed side-tab CTA** - A vertical tab on the homepage's left edge promises a free set but stays collapsed and unexplained across all three homepage screenshot folds, with no expanded state captured. The mechanic (referral, giveaway, contest) is unclear, which may be under-leveraging it as an acquisition or list-growth CTA. Source: site-visual-summary.md, Homepage Layout notes.
