# Poupette St Barth CRO Research Audit

## Data Sources Used

- Meta Ads and landing pages (3 ad creatives; landing page folds for Ad 2 only)
- Google Ads Transparency Center (2 screenshots)
- PageSpeed / Core Web Vitals (raw Lighthouse JSON, mobile, homepage and PDP)
- Current site screenshots (homepage, collection, PDP, cart) plus a live WebFetch of the homepage
- Skipped this run: Reviews & UGC, Social & Community Research, Competitor Insights, Inspiration Sites, Email Campaigns, Non-Data Context

## Source Findings

### Meta Ads & Landing Pages

Three ads are live on Facebook and Instagram since Aug 31, 2026, all funded by PSBC LIMITED. All three lead with "Shop now" and craft/best-seller angles:

- **Ad 1:** "Every piece made by hand. The Saint Barth print you will live in all summer." Handmade/limited-run framing. No landing page screenshots collected — message match cannot be assessed.
- **Ad 2:** "Bring a little Saint Barth wherever you are. Effortless prints, effortless days." General resort-wear framing with no named product. The landing page collected for this ad is a site search results page for "sasha" (22 results), not a dedicated product or collection page. Search UI (breadcrumb, filter panel, sort dropdown, "22 results found") is the first thing a visitor sees — nothing in the fold reinforces the ad's headline or caption. No trust signals (reviews, ratings, guarantees) appear across any of the three landing page folds captured.
- **Ad 3:** "The Sasha: our best-selling Saint Barth essential. You will see why." Names the exact product shown in Ad 2's landing page search results, but no landing page was collected for Ad 3 itself — the mismatch between which ad names "Sasha" and which ad's landing page shows Sasha search results could not be verified end to end.

**Gap:** Landing pages for Ad 1 and Ad 3 were not collected, so message match is unconfirmed for 2 of 3 live ads.

### Google Ads

Google Ads Transparency Center (advertiser "PSBC LIMITED, Verified") shows roughly 20 ad units: Shopping/product ads, text search ads with sitelinks, responsive display ads, one Local/Maps ad (4.4 stars, 7 reviews, Southampton), and image-led display ads.

Headline themes center on "Iconic Prints, Timeless Cuts," seasonal pushes ("High Summer 26," "Spring 26 Collection"), and a kids' clothing line not present in the Meta creatives reviewed. Offers include "Free worldwide shipping," "Easy Returns," and "10% off your First Order" (Girls Clothing ad) — consistent with the site's announcement bar.

**Gap vs. Meta:** None of the Meta ads' handmade/craft or best-seller framing ("Every piece made by hand," "The Sasha: our best-selling...") appears anywhere in the Google Ads copy reviewed. The two channels are running fully separate messaging with no shared hero angle.

### Reviews & UGC

Not collected — explicitly skipped by the client this run. No review or UGC data available for this audit.

### PageSpeed / Core Web Vitals

Mobile Lighthouse lab data, collected 2026-09-09 (desktop not collected):

| Metric | Homepage | PDP |
|---|---|---|
| Performance score | 64/100 | 62/100 |
| LCP | 13.7s (score 0) | 18.1s (score 0) |
| CLS | 0.002 (score 1) | 0 (score 1) |
| Time to Interactive | 17.1s (score 0.04) | 23.3s (score 0.01) |
| Total Blocking Time | 230ms (score 0.86) | 180ms (score 0.92) |
| Speed Index | 5.5s (score 0.54) | 8.8s (score 0.16) |
| First Contentful Paint | 2.1s (score 0.8) | 2.1s (score 0.8) |

Layout shift is not an issue on either page (CLS near zero). The problem is load and interactivity time: LCP fails Google's "good" threshold (2.5s) by roughly 5.5x on the homepage and 7x on the PDP, and Time to Interactive exceeds 17s on both pages. The PDP is the more severe of the two, with an 18.1s LCP and a Speed Index nearly double the homepage's.

**Gap:** This is lab data from a single mobile run, not field/CrUX data. No desktop scores were collected. Real-world visitor experience (especially on slower connections or older devices) is likely worse than these lab numbers suggest.

### Competitor Analysis

Not collected — no `raw/competitors.md` provided and self-research was not run for this brand this cycle. This section is a gap in the current audit.

### Emails

Not collected — no email screenshots or `raw/emails.md` provided.

### Inspiration Sites

Not collected — no inspiration screenshots or `raw/inspiration.md` provided.

### Non-Data Context

Not collected — no `raw/context.md` provided. No call notes, strategic priorities, or known objections on record for this engagement.

### Social & Community Research

Skipped explicitly at the client's request this run. Per manifest, this is flagged as a real gap, not backfilled.

### Current Site Screenshots

**Homepage:** Full-bleed hero video/image with headline "THE SEASON'S ESSENTIALS" and a single "SHOP" link — no product, price, or offer specificity in the hero itself. Announcement bar promotes 10% off first order plus free shipping; a "Get 10% Off" popup tab is fixed at the bottom-left throughout. No review count, star rating, guarantee copy, or "as seen in" badges appear in any of the three folds captured. A live fetch of the homepage confirms the footer carries three trust badges ("Free shipping," "Secured payment," "Simple returns") — these sit below the fold captured in the screenshots and are not visible to a visitor without scrolling to the footer.

**Collection page:** 103 products with a "Filter" button, sort dropdown, and straight single pricing throughout — no compare-at/strikethrough pricing or sale badges on any tile across three folds, even though the collection is titled "NEW COLLECTION." "Quick Purchase" overlay buttons appear on some tiles but not others, with no visible pattern for which products get it.

**PDP (French locale — captured on poupettestbarth.com/fr, while homepage/collection were captured in English):** Single purchase option only, single price (€330,00), no subscription or bundle option. No review count or star rating anywhere on the page, including in or near the buy box — the only trust-adjacent elements are a free-international-shipping line and FAQ return-policy questions further down the page. The "AJOUTER AU PANIER" (Add to Cart) button is a static block-width button that scrolls out of view by fold 3, not sticky. A "RECOMMANDATIONS POUR VOUS" (recommendations) section begins at the bottom of fold 3 but its content was not captured.

**Cart:** Filename (cart-drawer.png) suggests an overlay drawer, but the screenshot shows a full mobile cart page instead — the actual UI pattern (drawer vs. page) is unconfirmed. Single line item shown, full-width static checkout button, no upsell, cross-sell, bundle, or free-shipping progress bar anywhere in the capture. No trust badge or guarantee copy in the cart itself.

## Cross-Source Themes

1. **No trust signals visible above the fold, anywhere in the funnel.** Homepage folds 1-3, the Ad 2 landing page (all 3 folds), the collection page, the PDP, and the cart all lack review counts, star ratings, or guarantee badges in the visible captures. The only trust signals found (footer badges, FAQ return copy) require scrolling past the point most visitors will convert or bounce. This spans 5 of the 6 collected sources (homepage, Meta LP, collection, PDP, cart) — the strongest evidence pattern in this audit.
2. **Site performance is failing Core Web Vitals on mobile, worse on the PDP than the homepage.** LCP scores of 13.7s (home) and 18.1s (PDP) are 5-7x the "good" threshold, with Time to Interactive over 17s on both pages. This directly threatens paid traffic ROI, since both Meta and Google ads are actively driving mobile clicks into this experience.
3. **Ad-to-landing-page message match is broken for at least one live ad and unverifiable for two others.** Ad 2 promises general "everywhere" resort-wear messaging but lands on a raw search-results page for "sasha," with no landing page collected for Ad 1 or Ad 3 to confirm or rule out the same problem.

## Top Test Opportunities

**Add trust signals to the PDP buy box** — No review count, star rating, or guarantee copy appears anywhere on the PDP, including next to the €330,00 price and Add to Cart button, which raises purchase-decision friction on the highest-intent page in the funnel. Evidence: PDP screenshots (all 3 folds), homepage screenshots. Est. lift: unknown (no baseline conversion or session data provided) — flag as high-confidence, unsized.

**Fix Ad 2's landing page to match its ad promise** — Ad 2 promotes broad "Saint Barth, everywhere" resort-wear messaging but sends clicks to a raw site-search results page for "sasha" with no supporting copy, image, or headline that echoes the ad; this is the single highest-friction point in the paid funnel given it's a confirmed, screenshotted mismatch (not inferred). Evidence: meta-ads-visual-summary.md Ad 2, ad-creative-2.png, ad2-landing-f1/f2/f3.png. Est. lift: unknown (no ad spend or CVR data provided) — flag as high-confidence, unsized.

**Reduce PDP load time** — PDP Lighthouse mobile score is 18.1s LCP and 23.3s Time to Interactive, both far outside Google's "good" range, on the page paid traffic is most likely to land on for product-specific ads (e.g., Ad 3's "Sasha" ad). Evidence: pdp-pagespeed.json. Est. lift: unknown (no sessions/AOV data provided) — flag as high-confidence, unsized.

**Reduce homepage load time** — Homepage Lighthouse mobile score is 13.7s LCP and 17.1s Time to Interactive; slower than PDP-adjacent benchmarks and the first impression for all display/awareness traffic. Evidence: homepage-pagespeed.json. Est. lift: unknown (no sessions/AOV data provided) — flag as high-confidence, unsized.

**Confirm Ad 1 and Ad 3 landing pages match their ad promise** — Ad 1 ("handmade, limited runs") and Ad 3 ("The Sasha, our best-seller") have no landing page screenshots collected, so message match is unverified for two of three live Meta ads; given Ad 2 already shows a confirmed mismatch, these are worth checking. Evidence: meta-ads-visual-summary.md (Ad 1, Ad 3 landing page fields marked "not collected"). Est. lift: unknown — data collection gap, not yet a confirmed opportunity.

**Add sale/compare pricing clarity to the collection page** — Collection page shows straight single pricing on all 103 products, even under a "NEW COLLECTION" heading, with no compare-at pricing or sale badges visible on any tile across three folds; unclear if this is intentional (no current promotions) or a missed opportunity to signal value given the site-wide "10% off first order" offer already running. Evidence: site-visual-summary.md Collection Page. Est. lift: unknown — needs confirmation of current promo status before sizing.

**Clarify cart page UI pattern (drawer vs. full page)** — The screenshot filename indicates a cart drawer, but the capture shows a full mobile cart page; if the live site uses a full-page cart rather than a drawer, that's a heavier interruption to the shopping flow than an overlay, and it's currently unconfirmed which pattern is actually live. Evidence: site-visual-summary.md Cart, cart-drawer.png (per Open Questions in manifest). Est. lift: unknown — needs UI pattern confirmation before sizing.

**Align Google Ads and Meta Ads messaging** — Google Ads use "Iconic Prints, Timeless Cuts" and seasonal collection framing, while Meta Ads use handmade/craft and best-seller framing; none of the Meta copy appears in Google Ads, meaning the two channels build no shared brand recall for a visitor exposed to both. Evidence: google-ads-visual-summary.md ("Gaps vs. Meta" section), meta-ads-visual-summary.md. Est. lift: unknown — a messaging/creative decision, not a single-page test; flag as a strategic finding rather than a standard A/B slot.

**Make the PDP Add to Cart button sticky** — "AJOUTER AU PANIER" is a static block-width button positioned below the description and size guide; it scrolls out of view by fold 3, forcing a visitor who has scrolled to read details, sizing, or FAQ content to scroll back up to purchase. Evidence: site-visual-summary.md PDP, "CTA behavior" note. Est. lift: unknown (no baseline conversion or session data provided) — flag as high-confidence, unsized.

**Add product/offer specificity to the homepage hero** — The hero shows a full-bleed lifestyle image with the generic headline "THE SEASON'S ESSENTIALS" and a single unstyled "SHOP" link — no featured product, price, or time-bound offer is visible in the first fold, despite the site running an active 10% first-order discount in the announcement bar above it. Evidence: site-visual-summary.md Homepage Fold 1, live homepage fetch. Est. lift: unknown (no baseline conversion or session data provided) — flag as directional, unsized.

## Unused but Valuable Findings

- The PDP was captured in French (poupettestbarth.com/fr) while homepage and collection were captured in English — if the brand's primary paid traffic lands in English, the PDP experience for that segment has not actually been reviewed in this audit.
- The Google Ads Transparency data shows a kids' clothing line (Girls Clothing ad, "10% off your First Order") that doesn't appear anywhere in the Meta creatives collected — worth checking whether Girls is a separate underexplored funnel.

## Missing Data

- **Reviews & UGC:** Explicitly skipped by the client this run. No customer sentiment data available to corroborate or challenge any finding in this audit.
- **Social & Community Research:** Explicitly skipped by the client this run, despite normally running unconditionally.
- **Meta Ad 1 and Ad 3 landing pages:** Creatives collected, but no landing page screenshots for either, so message match is unverified for 2 of the 3 live ads.
- **PDP locale mismatch:** PDP screenshots are in French while homepage/collection are in English; PDP copy and CTA text noted above are not directly comparable to the English-language pages elsewhere in this audit.
- **Desktop PageSpeed data:** Only mobile Lighthouse data was collected for both homepage and PDP; desktop performance is unknown.
- **Competitor Insights, Inspiration Sites, Email Campaigns, Non-Data Context:** None provided this run.
