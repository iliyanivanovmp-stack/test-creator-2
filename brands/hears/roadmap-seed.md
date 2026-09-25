# Hears Roadmap Seed

**Store:** hears.com
**AOV:** unknown (not provided in any collected source)
**Monthly sessions:** unknown (not provided in any collected source)
**Data sources:** Google Ads Transparency, PageSpeed/Core Web Vitals, Current Site Screenshots + live WebFetch verification, Social & Community Research (last30days-ecom), Reviews & UGC, Competitor research (self-researched)

## Key Insights

Two independent third-party sources contradict the site's own trust claim. Hears' homepage and PDP repeat "Rated 4.9/5 by 200,000+ customers" in the hero and buy box, but Trustpilot shows a 3.5 TrustScore on 1,284 reviews (most recent reviewers "somewhat happy," not uniformly positive) and Amazon shows 3.8/5 on 232 ratings for the Hears One Ear Plugs listing. This gap sits directly on the highest-traffic conversion surfaces.

Both key pages paint fast but take dramatically longer to become usable. Lighthouse (2026-09-13) shows LCP of 1.7s (homepage) and 2.4s (PDP) — both good — but Total Blocking Time of 8,590ms on the homepage and 17,600ms on the PDP, pushing Time to Interactive to 65.6s and 85.9s respectively. The floating "Ask a question" AI-chat widget, UGC video carousels, and embedded review modules appear on every screenshot fold and are the likely contributors, though the JSON doesn't name specific scripts.

Google Ads segment traffic by use case — sleep, moto, festival, concert — with headlines like "Earplugs for Sleep - Blocks snoring" and "Best Earplugs for Motobike Rides." Live WebFetch (2026-09-13) confirms 100% of that traffic lands on one Pacha-festival-themed hero ("The most iconic earplug is back for the 2026 season," a beach/cocktail image) regardless of ad intent, and ad-stated offers ("45% Off," "Buy 2 & Get 10% Off") don't match the live sitewide offer ("BUY 2, GET 1 FREE"). Separately, live WebFetch resolved an open question from collection: the PDP's true default variant is "Brass Blue," not the "Pacha Edition 2.0" shown in the original screenshot captures — those captures reflected a search click-through state (`?_psq=pacha` in the URL), not the default landing state.

## Top Test Opportunities

### 1. Fix ad-to-homepage message mismatch for non-Pacha traffic
**What's broken:** The homepage hero is a full-bleed lifestyle photo (woman on a beach with a cocktail) with a "HEARS × PACHA" co-branded logo overlay, headline "The most iconic earplug is back for the 2026 season," subhead "Don't get caught on the island without protection," and CTA "SHOP PACHA EDITION." This single hero serves every visitor regardless of which Google Ad they clicked — sleep, moto, festival, or concert. A visitor from "Earplugs for Sleep - Blocks snoring" sees a festival/party visual with no sleep messaging until scrolling to Fold 2's "Explore more Hears moments" tiles.
**Evidence:** Google Ads visual summary (headline segmentation), live homepage WebFetch (2026-09-13).
**Key data:** 7+ distinct use-case ad headlines identified; homepage hero has zero dynamic variation.
**Est. lift:** 0.5-1% CR lift x unknown sessions/mo x unknown AOV = revenue unknown.

### 2. Reduce Total Blocking Time on PDP and homepage
**What's broken:** Both pages carry a floating "Ask a question" AI-chat pill button (bottom of hero, repeats on PDP and collection), a horizontally-scrollable UGC video carousel ("Loved by 200,000+ happy customers," 4+ video thumbnails) on the PDP, and embedded review/rating widgets — all visible across every captured fold. Lighthouse shows these pages are visually ready in 1.7-2.4s but not reliably interactive until 65.6-85.9s.
**Evidence:** PageSpeed JSON (homepage + PDP, fetched 2026-09-13), site screenshots.
**Key data:** TBT 8,590ms (homepage) / 17,600ms (PDP); Performance scores 0.59 / 0.55; industry "poor" threshold for TBT is >600ms — these pages are 14-29x over that line.
**Est. lift:** 0.5-1.5% CR lift x unknown sessions/mo x unknown AOV = revenue unknown.

### 3. Reconcile the rating discrepancy between site and third-party platforms
**What's broken:** The PDP buy box displays "★★★★★ 4,736 Reviews" directly under the product title, and both homepage and PDP repeat "Rated 4.9/5 by 200,000+ customers." A shopper who cross-checks Amazon (3.8/5, 232 ratings) or Trustpilot (3.5 TrustScore, 1,284 reviews) before buying encounters a materially different picture with no visible reconciliation on-site.
**Evidence:** last30days-ecom (Trustpilot + Amazon, corroborated across two independent platforms), live PDP/homepage WebFetch.
**Key data:** Site claim 4.9/5 (200,000+) vs. Trustpilot 3.5 (1,284 reviews) vs. Amazon 3.8 (232 ratings).
**Est. lift:** 0.5-1% CR lift x unknown sessions/mo x unknown AOV = revenue unknown.

### 4. Correct the swatch-availability contradiction on PDP
**What's broken:** In the "Color: Pacha Edition 2.0" swatch row (9 swatches under the noise-reduction selector), one swatch carries a diagonal strike-through indicating that color is unavailable, positioned directly beside a green-dot "In stock ready to ship" status line with no text distinguishing "this specific color is out" from "the product is in stock."
**Evidence:** site-visual-summary.md, PDP Fold 1.
**Key data:** 9 swatches in the Pacha row, 1 struck through; stock badge is a single undifferentiated state.
**Est. lift:** 0.3-0.5% CR lift x unknown sessions/mo x unknown AOV = revenue unknown.

### 5. Surface a lower-cost path to the free-shipping threshold in the cart drawer
**What's broken:** The cart drawer shows a progress bar ("You're $38 away from free shipping," $50 threshold) directly above a horizontally-scrollable "Exclusive offers to pair with your order!" carousel whose only visible cross-sell is the full-price core product ($43) — no $9-12 accessory-tier item (matching the gap size) is offered as a lower-friction way to close the $38 gap.
**Evidence:** cart screenshot description, site-visual-summary.md.
**Key data:** $38 gap to free shipping; only cross-sell shown is $43, which overshoots the threshold by $5 rather than closing it precisely.
**Est. lift:** 0.3-0.8% AOV lift x unknown sessions/mo x unknown AOV = revenue unknown.

### 6. Align PDP default variant with paid-traffic intent
**What's broken:** Live WebFetch (2026-09-13) confirms the PDP's true default variant is "Brass Blue," but the collection page and search-driven click-throughs push shoppers toward "Pacha Edition 2.0" — a limited, partially-OOS colorway (see #4) — via URL parameters. This is an internal inconsistency between what merchandising defaults to and what paid/search traffic actually sees on arrival.
**Evidence:** Manifest open question resolved via live WebFetch; collection and PDP screenshots.
**Key data:** Default variant "Brass Blue" (confirmed live) vs. "Pacha Edition 2.0" (shown in original screenshot captures via `?_psq=pacha` query string).
**Est. lift:** 0.3-0.6% CR lift x unknown sessions/mo x unknown AOV = revenue unknown.

### 7. Move trust badges higher on the PDP buy box
**What's broken:** The "100-day money back guarantee" checkmark line currently sits below the black "ADD TO CART" button, and the "2 Year Warranty" / "100-Day Free Returns" badges only appear in the cart drawer — not on the PDP itself, where the rating discrepancy (#3) most needs a counterweight at the point of decision.
**Evidence:** PDP and cart screenshot descriptions, site-visual-summary.md.
**Key data:** Guarantee copy currently below the primary CTA rather than beside the price/rating block above it.
**Est. lift:** 0.3-0.5% CR lift x unknown sessions/mo x unknown AOV = revenue unknown.

### 8. Fix unloaded placeholder images on the collection page
**What's broken:** The Hears Sleep product grid, Accessories grid, and Merch grid (collection page Folds 2-3) render as gray placeholder blocks with faded or missing product photography in the captured screenshots — sitting directly in the browse-to-PDP path for any non-hero, non-bestseller traffic.
**Evidence:** site-visual-summary.md, Collection Fold 2-3. Not re-verified live (WebFetch returns text only) — flag for manual re-check before build.
**Key data:** 3 of 3 lower-fold product grids affected in the captured state.
**Est. lift:** 0.2-0.5% CR lift x unknown sessions/mo x unknown AOV = revenue unknown.

## Unused Findings

- Saint Laurent x Hears fashion collaboration (corroborated on Pinterest and independent editorial) is absent from current site messaging — a positioning opportunity, not a layout test.
- Reviewers repeatedly self-report wanting to size up from 20dB to 25dB after purchase — a post-purchase cross-sell signal, not a PDP/homepage test.
- Third-party resellers (On Web Consulting Ltd, ShopForward B.V., Now-Sale.co) run Google Shopping listings using Hears imagery with offer framing that doesn't match the live site promo — a brand-control issue to route to the client directly.
