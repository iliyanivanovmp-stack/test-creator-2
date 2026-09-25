# Instant Hydration CRO Research Brief

**Data Sources:** Meta Ads and Landing Pages, Google Ads Transparency, PageSpeed / Core Web Vitals, Current Site Screenshots, Reviews & UGC, Social & Community Research, Competitor research (self-researched), Non-Data Context

Subscription enrollment is the single most evidence-backed problem in this account. Two 1-star reviews describe being converted to a subscription without authorization ("Cannot Cancel," "SCAM... $99 charge"), and the Social & Community Trustpilot summary independently flags the same pattern (Source: Reviews & UGC, Social & Community Research). The PDP screenshot shows why: flavor and delivery frequency are chosen in one step, with subscribe-vs-one-time never made explicit, and a locked incentive list (sampler, shipping, water bottle) that only unlocks after that choice.

On-page priority does not match the trust-signal architecture. Energy+ owns the homepage hero and the audited PDP, confirmed by TikTok and LinkedIn evidence as a genuine strategic pivot, yet that PDP carries zero star rating or review count across all three folds captured, despite the homepage's "2M+ Orders | 100M+ Servings" badge sitting one click away (Source: Site Screenshots).

Mobile performance is in the "poor" range on both pages the funnel depends on. Homepage scores 48/100 with a 31.8-second Time to Interactive and 1,410ms Total Blocking Time; the Energy+ PDP scores 47/100 with a 34.1-second Time to Interactive and 1,840ms Total Blocking Time (Source: PageSpeed, 2026-09-09). Both pages render but resist tap interaction for over half a minute, directly ahead of a purchase flow that requires manual flavor and quantity selection.

Two of three Meta ad campaigns break message match after the click. The Target retail ad ("RUN don't walk to Target") lands on a page with a generic "Find in Store" link and no Target-specific content. The ICEE and Luigi's collab ads match on hero imagery, but the buy box title and "Select from 14 Flavors" CTA never name the collab, leaving a visitor to guess which of 14 generic options matches the ad they clicked (Source: Meta Ads visual summary, live WebFetch).

Sessions, AOV, and ad-spend figures were not collected for this account, so no dollar-based revenue estimate can be shown for the combined opportunity. Every lift below is a conservative percentage range pending real traffic data.

## Slot 1: Default-select a flavor on the Energy+ PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Energy+ PDP (https://instanthydration.com/products/energy-electrolyte-drink-mix)
**Revenue potential:** 3-5% CR lift x sessions/mo (not collected) x $27.50-$49.50 AOV = pending session data.

**Hypothesis:** If we pre-select a flavor and quantity by default so the primary CTA is enabled on page load, more visitors complete a purchase because the disabled "SELECT A FLAVOR" CTA currently forces an extra manual step before any purchase path is available.

**Data:** The buy box shows two flavor tiles (Sour Green Apple, Tropical Crush) each starting at a quantity of 0, with no default selection. The primary CTA stays disabled and reads "SELECT A FLAVOR" until a flavor and quantity are chosen, and the locked incentive list below (sampler, free shipping, water bottle) stays inert until then. Source: Site Screenshots (PDP fold 1).

**V1:** Default-select the first-listed flavor (Sour Green Apple) at quantity 1, with the Subscribe & Save option pre-selected over One-Time Purchase (KB: resources/kb/pdp-structure.md). The primary CTA reads "ADD TO CART" and is enabled on page load, and the incentive list shows as unlocked immediately. Mobile: buy box stacks below the product image carousel with the same defaults. Desktop: buy box sits beside the images with the same defaults; layout otherwise unchanged.

## Slot 2: Add a review and star-rating trust signal to the Energy+ PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Energy+ PDP (https://instanthydration.com/products/energy-electrolyte-drink-mix)
**Revenue potential:** 2-4% CR lift x sessions/mo (not collected) x $27.50-$49.50 AOV = pending session data.

**Hypothesis:** If we add a star rating and review count near the product title, more visitors complete a purchase because the PDP currently shows zero social proof despite the homepage's "2M+ Orders | 100M+ Servings" badge sitting one click away.

**Data:** No star rating or review count appears anywhere across the three PDP folds captured. The homepage carries a prominent "2M+ Orders | 100M+ Servings" trust badge in its hero, one click from this PDP. Source: Site Screenshots (PDP vs. Homepage).

**V1:** Add a trust badge directly under the product title, above the fold, reusing the homepage's sourced "2M+ Orders | 100M+ Servings" copy since no PDP-specific review count exists in the audit (KB: resources/kb/pdp-structure.md, social proof placed beside images before the title). Mobile: badge sits directly under the title, above the value prop. Desktop: same placement, same copy.

## Slot 3: Fix the Target-ad landing page message match

**Type:** A/B test (1 variation vs. control)
**Page:** Meta Ad 2 landing page, Target retail campaign
**Revenue potential:** Reduces post-click bounce on this ad specifically; ad-level session and spend data not collected, so a dollar figure cannot be shown.

**Hypothesis:** If we add Target-specific in-store availability content to the ad 2 landing page, click-through visitors convert at a higher rate because the page currently breaks the promise made in the ad.

**Data:** Ad 2's entire premise is in-store availability ("RUN don't walk to Target"). Live WebFetch of the landing page it sends traffic to confirms only a generic "Find in Store" link, with no Target-specific text, store locator prompt, or in-store framing anywhere in the page copy. Source: Meta Ads visual summary, live WebFetch.

**V1:** Add a Target-branded strip directly below the hero: "Now Available at Target" with the Target logo and a "Find a Store Near You" button wired to a store locator. Mobile: banner sits full-width directly below the hero image, above the buy box. Desktop: banner spans the hero width in the same position; buy box and rest of page unchanged.

## Slot 4: Carry collab branding into the buy box and CTA

**Type:** A/B test (1 variation vs. control)
**Page:** Meta Ad 1 (ICEE) and Ad 3 (Luigi's) landing pages
**Revenue potential:** 2-3% CR lift on collab-ad traffic x sessions/mo (not collected) x $27.50-$49.50 AOV = pending ad-level data.

**Hypothesis:** If the buy box title and CTA reference the collab that brought the visitor there, conversion improves because visitors currently cannot tell which of 14 generic flavor options matches the ad they clicked.

**Data:** Both ICEE and Luigi's ad creatives lead entirely with collab branding, and the landing page hero matches. But the buy box product title reads generic "Instant Hydration Electrolyte Powder," and the CTA reads "Select from 14 Flavors" on both, never naming the collab. Source: Meta Ads visual summary, live WebFetch of the ICEE and Luigi's landing pages.

**V1:** Replace the generic buy box title with a collab-specific title ("ICEE x Instant Hydration Electrolyte Powder" or "Luigi's x Instant Hydration Electrolyte Powder" per page), and change the CTA from "Select from 14 Flavors" to "Get the ICEE Flavor" or "Get the Luigi's Flavor," with the matching flavor tile pre-highlighted. Mobile and desktop: same copy and highlight logic; layout unchanged.

## Slot 5: Immediate Fix - Mobile Time to Interactive and Total Blocking Time on Homepage and PDP

**Type:** Immediate Fix (no A/B test; fix directly)
**Page:** Homepage and Energy+ PDP

**Data:** Mobile Lighthouse lab data, collected 2026-09-09: Homepage scores 48/100 (4.4s LCP, 1,410ms TBT, 31.8s Time to Interactive). Energy+ PDP scores 47/100 (4.8s LCP, 1,840ms TBT, 34.1s Time to Interactive). Both sit in Lighthouse's "poor" range; CLS is 0 on both, so layout stability is not the issue. Source: PageSpeed mobile lab data, 2026-09-09.

**Why this is a fix, not a test:** Both pages resist tap interaction for over half a minute on a simulated mobile connection, ahead of a purchase flow that requires manual flavor and quantity selection on the PDP. This drags on every visitor to these two pages regardless of traffic source, so it should be fixed directly rather than split-tested.

## Slot 6: Clarify subscription enrollment at the point of flavor selection

**Type:** A/B test (1 variation vs. control)
**Page:** Energy+ PDP (https://instanthydration.com/products/energy-electrolyte-drink-mix)
**Revenue potential:** Not directly sizeable in CR or dollar terms from available data. Success is measured through a drop in subscription-related complaints and support tickets, since two 1-star reviews and the Trustpilot summary both point to this same selection step as the source of the friction (Source: Reviews & UGC, Social & Community Research).

**Hypothesis:** If we make the subscribe-versus-one-time choice explicit and visible in plain language at the point of flavor selection, subscription-related complaints drop because customers currently describe being enrolled without realizing it during this exact step.

**Data:** Two 1-star reviews describe being converted to a subscription without authorization: "This company is a SCAM... my order signed me up to receive a subscription... $99 charge" and "Cannot Cancel - I did a 1x Purchase and they 'converted' it to a subscription, without my authorization." The Social & Community Trustpilot summary independently corroborates "subscription/support friction" tied to the same "select a flavor to unlock free gifts" mechanic visible on the live PDP screenshot. Source: Reviews & UGC, Social & Community Research.

**V1:** Add an explicit toggle labeled "Subscribe & Save $X" versus "One-Time Purchase $X" above the flavor tiles, each option showing plain-language terms without requiring a click ("charges every X days, cancel anytime from your account"). Mobile: toggle stacks full-width above the flavor tiles. Desktop: toggle sits directly above the flavor and frequency selector, same copy and placement logic.

## Slot 7: Add an AOV mechanism to the cart page

**Type:** A/B test (1 variation vs. control)
**Page:** Cart
**Revenue potential:** 3-5% AOV lift x sessions/mo (not collected) x current AOV = pending session and AOV data.

**Hypothesis:** If we add a free-gift progress bar to the cart, average order value increases because the cart currently has no upsell, cross-sell, or AOV mechanism at the highest-intent point in the funnel.

**Data:** The cart shows a single line item, a large empty white space, then the checkout summary, with no upsell, cross-sell, bundle offer, or free-shipping progress bar anywhere on the page. Source: Site Screenshots (Cart).

**V1:** Add a horizontal progress bar directly under the line item showing the dollar gap to a free-gift threshold, reusing the water bottle incentive already used on the PDP (e.g. "Add $12 more for a free water bottle"), updating live as the cart changes (KB: resources/kb/cro-system.md). Mobile: progress bar sits full-width directly under the line item. Desktop: same placement, directly above the checkout summary.

## Slot 8: Give the core electrolyte line equal homepage visual weight

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage
**Revenue potential:** 2-4% CR lift on non-Energy+ paid traffic x sessions/mo (not collected) x $27.50-$49.50 AOV = pending session data.

**Hypothesis:** If the core 14-flavor line gets hero-level placement equal to Energy+, conversion improves for traffic that lands on the homepage looking for the core line, because that line drives the bulk of the reviews and Google Ads volume reviewed in this audit but is currently a single fold-2 tile competing for attention.

**Data:** The homepage's entire above-the-fold hero (image, headline, primary CTA) is built around Energy+, a newer, not-yet-best-selling product per the collection note. The only path to the core electrolyte line is a secondary fold-2 tile ("Shop Electrolytes / Choose from 14 delicious flavors") of equal visual weight to the Energy+ tile, despite the core line carrying most of the reviews and dominant Google Ads presence. Source: Site Screenshots (Homepage), Non-Data Context, Google Ads visual summary.

**V1:** Split the hero into two equal-weight panels, one for Energy+ and one for the core 14-flavor line, each with its own CTA ("Shop Energy+" and "Shop Electrolytes"), replacing the current single-product hero. Mobile: panels stack vertically. Desktop: panels sit side by side; rest of the homepage unchanged.

## Future Slot Candidates

1. **Align Google Ads spend with on-site priority (Energy+)** - Energy+ owns the homepage hero and PDP, confirmed as a genuine pivot by TikTok and LinkedIn evidence, but the Google Ads set reviewed shows Energy+ as only one minor display unit against the core line's dominant ad presence. A paid-media reallocation, not a site test, and needs spend and CVR data to size.
2. **Close the "50 Day Happiness Guarantee" return-shipping gap** - Ads and site badges market "Try Risk Free for 50 Days," but a 3-star reviewer reports paying return shipping inside that window. A policy fix, not a site test, best tracked through complaint volume.
