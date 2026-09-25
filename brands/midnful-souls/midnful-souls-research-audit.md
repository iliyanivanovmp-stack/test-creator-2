# Mindful Souls CRO Research Audit

## Data Sources Used

- Meta Ads & Landing Pages (raw/meta-ads-visual-summary.md, 3 ad creatives + landing pages)
- Google Ads Transparency Center (raw/google-ads-visual-summary.md)
- PageSpeed / Core Web Vitals (raw/pagespeed.md, Lighthouse mobile reports for homepage and PDP)
- Current Site Screenshots (raw/site-visual-summary.md: homepage, collection, cart drawer)
- Live homepage fetch (mindfulsouls.com, 2026-09-01)
- Live PDP fetch (mindfulsouls.com/products/magical-energy-talisman, 2026-09-01)
- Competitor research (self-researched via WebSearch, 2026-09-01)

Not collected in this pass: Reviews & UGC (sent separately per user, pending), dedicated PDP screenshots, competitor data from client, inspiration sites, email campaigns, non-data context.

## Source Findings

### Meta Ads & Landing Pages

Three active ad-to-landing-page pairs were reviewed.

**Ad 1 (subscription box, static image):** Strong message match. The ad promises "$25.99 first box" and "free bonus inside." The landing page hero repeats the $25.99 price and the free 18-piece aroma oils gift exactly. The only mismatch is trust framing: the ad claims "trusted by over a million people," while the landing page shows "13,000 reviews," a different and unverified metric with no visible link between the two claims.

**Ad 2 (subscription box, video, 35% off):** Direct contradiction between ad and landing page. The ad headline states "Code applied automatically. No code. No fuss." The landing page displays a dashed callout box reading "Use code at checkout & get your 1st Box for only $25.99! [MYBOX35]," which requires the shopper to manually copy and apply a code. This is a bait-and-switch on the ad's central promise. The landing page's primary CTA button also shows the full price ($39.97, ADD TO CART), not the discounted $25.99, so the advertised savings are not reflected in the main buy button, only in a secondary text callout below it.

**Ad 3 (Magnetic Energy Talisman, video):** Ad copy names specific materials ("obsidian, copper coil, and natural minerals"). The landing page (which is also this product's PDP) does not repeat these material details in the three folds captured, though the live fetch of the full page confirms product-detail and FAQ content exists further down. Trust signals on this landing page are visibly thinner than the subscription-box pages: one customer review card and a Trustpilot "Excellent" badge, versus the subscription pages' review counts, star ratings, and multi-icon trust strips.

### Google Ads

Google Ads Transparency Center shows a much broader campaign than Meta: individual jewelry and crystal SKUs (rings, phone cases, necklaces, water bottles, pendulums, incense) alongside the subscription box, across five regional sub-entities (US, EU, AU, Canada, BV). None of the three Meta creatives collected represent this individual-product catalog at all, meaning Google traffic is likely landing on pages and offers with no Meta-side creative precedent to compare against.

Discount code proliferation is the standout issue: Google Ads show LABOR35, SPRING35, an unlabeled "35% Off First Subscription Box," and a separate "50% OFF + FREE GIFT" banner creative, none of which match the Meta ad codes (Ad 1's no-code $25.99, Ad 2's MYBOX35). A shopper who sees a Google ad and a Meta ad in the same week would encounter at least four different discount mechanics for what appears to be the same core offer.

The Google star-rating snippet shows "3.9 ★★★★ (966)," notably lower and much smaller in sample size than the 4.9/12k-13k figures shown on Meta landing pages and the homepage.

### Reviews & UGC

Not collected in this pass. User indicated reviews would be sent separately. See Missing Data.

### PageSpeed / Core Web Vitals

Mobile Lighthouse reports fetched 2026-09-01.

**Homepage** (mindfulsouls.com/): Performance 0.63, Accessibility 0.92, Best Practices 0.58, SEO 0.92. LCP 4.2s, CLS 0, TBT 360ms, Speed Index 7.8s, TTI 24.5s, FCP 3.4s. Moderate performance; LCP and TTI exceed Google's "good" thresholds (LCP should be under 2.5s), but layout is stable (CLS 0).

**PDP / Ad 3 Landing Page** (magical-energy-talisman): Performance 0.13, a critical score. LCP 13.3s, CLS 0.897, TBT 730ms, Speed Index 37.3s, TTI 48.3s, FCP 7.7s. A CLS of 0.897 is severe (Google's "poor" threshold starts at 0.25); this page is also the direct landing destination for Meta Ad 3's traffic, meaning paid traffic is being sent to the single worst-performing page measured. TTI of 48.3s means the page is effectively non-interactive for most mobile visitors during the load window.

### Competitor Analysis

No competitor data was provided by the client. Researched independently via WebSearch, 2026-09-01.

| Competitor | Positioning | Price (first/entry box) | Notable weakness vs. Mindful Souls |
|---|---|---|---|
| Goddess Provisions | Self-care/spiritual subscription box, crystals + aromatherapy + beauty | $55.00/mo | Higher entry price, no equivalent low-cost trial hook |
| Magickal Earth | Crystal box supplemented with astrology/tarot content | Not listed in search results | Narrower catalog, no individual-SKU e-commerce arm |
| TheraBox | Therapist-curated wellness box, broad mainstream positioning | Not listed in search results | Less crystal/spiritual-specific, competes more on general wellness credibility |

Mindful Souls' $25.99-$39.97 entry price point undercuts Goddess Provisions' $55 stated price, which is a defensible acquisition-offer advantage worth protecting rather than diluting with the inconsistent code stack found in Google/Meta ads above.

Sources: [The 2 Best Crystal Subscription Boxes in 2026](https://www.mysubscriptionaddiction.com/best-crystal-subscriptions/1000), [The 7 Best Crystal Subscription Boxes For 2026](https://mindfulnessbox.com/crystal-subscription-boxes/)

### Emails

Not collected. No files present in raw/, not listed in manifest sources.

### Inspiration Sites

Not collected. No files present in raw/, not listed in manifest sources.

### Non-Data Context

Not collected. No context.md present.

### Current Site Screenshots

**Homepage:** Hero is a Labor Day sale banner (code LABOR35) with a $140-value box visual and a "4.9 (12k+ reviews)" rating. Below the hero, a trust-icon strip repeats free delivery, "2M+ Boxes Delivered," cancel anytime, and 30-day money-back guarantee. A "Trusted by 500k+ Happy Customers" line appears under the category tiles, and a press-logo strip (6 outlets) follows. The discount code LABOR35 is repeated three times within the first fold alone (announcement bar, headline, subhead), which is redundant but not necessarily harmful. The live fetch confirms the same offer structure and adds that the site also claims "100% natural and lab-certified" crystals, a specific quality claim not visible in the screenshot set.

The recurring friction across this fold and the collection page (below) is inconsistent trust numbers presented with equal visual weight: "12k+ reviews" (homepage hero) is a different metric from "500k+ Happy Customers" (homepage, fold 3) and "2M+ Boxes Delivered" (trust strip), and none of these reconcile cleanly with the "13,000 reviews" cited on Meta landing pages or the "3k+ Trustpilot reviews / 11,388 happy customers" cited on the collection page. No single figure is repeated consistently across all four surfaces (homepage, collection, Meta LPs, Google ad snippet).

**Collection page:** Fold 1 opens with a "BEST SELLERS" banner, three featured product thumbnails, and a Trustpilot badge ("Excellent," "3k+ reviews," "4.9/5 by 11,388 happy customers"). A 4-column product grid follows with sort control and product count ("60 products"). Fold 2 reveals pricing: compare-at strikethrough pricing with percentage-off badges (e.g., Magnetic Energy Talisman $39.97 vs $59.97, -33%, 886 reviews) is used consistently on sale items. Individual product review counts vary from 12 to 886, all displayed with identical 5-star iconography regardless of sample size, so a product with 12 reviews reads with the same visual authority as one with 886.

**PDP:** No dedicated PDP screenshots were captured. Layout must be inferred from Ad 3's landing page folds (which is this same product's PDP) plus the live fetch. The live fetch shows the PDP as a one-time-purchase page (not subscription) with a "Buy 1 Get 1 50% OFF" bundle option, a "BUY NOW" CTA, 886 reviews at 4.8/5 (this figure matches the collection-page review count for this SKU, but is higher than the 4.9/5 figures used elsewhere on the site, and differs from the "no review count visible" observation in the three folds actually screenshotted). This is the same page carrying the 0.13 Performance / 0.897 CLS Lighthouse score above, so any buy-box or trust-signal improvements here are undermined by the page's load stability until the performance issue is addressed.

**Cart (drawer):** Right-side slide-out with a free-shipping/free-gift progress bar, quantity stepper, and a "You May Also Like" cross-sell carousel with inline add-to-cart buttons. The only trust or assurance copy visible in the drawer is "Have a discount code? Add it at checkout." No guarantee badge, no returns copy, and no shipping-time reassurance beyond a per-item "Delivery within 4-7 Days" line, a gap relative to the guarantee and trust-icon strips shown prominently on the homepage and Meta landing pages.

## Cross-Source Themes

1. **Trust-metric inconsistency across every surface.** Homepage (12k+ reviews / 500k+ customers / 2M+ boxes), Meta LPs (13,000 reviews), collection page (3k+ Trustpilot / 11,388 customers), Google ad snippet (3.9/966), and the live PDP fetch (886 reviews, 4.8/5) never agree. Evidence: meta-ads-visual-summary.md, site-visual-summary.md, google-ads-visual-summary.md, live PDP fetch. This is the single most evidence-backed issue, touching four independent sources.
2. **Discount code and offer fragmentation.** At least five distinct discount mechanics are live simultaneously (LABOR35, SPRING35, MYBOX35, an unlabeled 35% code, a 50% OFF banner), and Ad 2 explicitly promises "no code" while its landing page requires one. Evidence: meta-ads-visual-summary.md, google-ads-visual-summary.md, site-visual-summary.md.
3. **PDP performance is a severe, isolated outlier.** Performance 0.13, LCP 13.3s, CLS 0.897, TTI 48.3s on the exact page Meta Ad 3 sends traffic to, versus a moderate 0.63 Performance score on the homepage. Evidence: raw/pagespeed.md.

## Top Test Opportunities

**Fix PDP Core Web Vitals on paid-traffic landing pages** — The Magnetic Energy Talisman PDP (Ad 3's landing destination) scores 0.13 Performance with 13.3s LCP and 0.897 CLS, meaning most mobile ad clicks land on a page that is barely usable during load. Evidence: raw/pagespeed.md, meta-ads-visual-summary.md. Est. lift: performance fixes on ad-landing pages commonly recover 5-10% conversion on affected traffic; exact sessions/mo and AOV not provided, so dollar estimate withheld pending traffic data.

**Make Ad 2's advertised discount automatic, or change the ad copy** — Ad 2 says "Code applied automatically. No code. No fuss," but the landing page requires manually entering MYBOX35 in a dashed callout box, and the main CTA button shows full price ($39.97) rather than the discounted $25.99. Evidence: meta-ads-visual-summary.md (Ad 2, LP Fold 1). Est. lift: message-match fixes on paid landing pages typically recover meaningful lost conversion from bounced, misled clicks; sessions/mo and AOV not provided.

**Unify the trust-metric displayed across homepage, collection, and Meta landing pages** — Four different numbers (12k+ reviews, 500k+ customers, 2M+ boxes, 13,000 reviews, 3k+ Trustpilot/11,388 customers) currently appear across surfaces with equal visual weight. Evidence: site-visual-summary.md (homepage, collection), meta-ads-visual-summary.md (all 3 LPs). Est. lift: not calculable without a controlled test baseline; flag as high-priority given four-source evidence strength.

**Consolidate the discount code stack** — LABOR35, SPRING35, MYBOX35, an unlabeled 35% code, and a 50% OFF banner are simultaneously live across Google and Meta, with no single consistent offer. Evidence: google-ads-visual-summary.md, meta-ads-visual-summary.md, site-visual-summary.md (LABOR35 on homepage). Est. lift: not calculable without conversion-by-source data; recommend as a strategic/ops fix as much as a CRO test.

**Add trust and guarantee copy to the cart drawer** — The cart drawer's only reassurance line is "Have a discount code? Add it at checkout." No guarantee badge, no returns copy, despite the homepage and Meta LPs prominently featuring a 30-day money-back guarantee elsewhere. Evidence: site-visual-summary.md (Cart Drawer). Est. lift: cart-stage guarantee reinforcement commonly lifts checkout-initiation rate by low single digits; sessions/mo and AOV not provided.

**Strengthen trust signals on the talisman/PDP-style landing pages** — Ad 3's landing page shows one review card and a Trustpilot badge only, versus the subscription pages' review counts, star ratings, and 4-icon trust strips. Evidence: meta-ads-visual-summary.md (Ad 3 folds 1-3, contrasted with Ad 1/Ad 2 folds). Est. lift: not calculable without page-level conversion data; flag as second-priority behind the CWV fix on the same page.

**Reconcile Google Ads' broad product catalog with a matching landing experience** — Google Ads promote individual jewelry/crystal SKUs (rings, water bottles, pendulums, incense) with no equivalent creative or landing-page precedent in the Meta set collected. Evidence: google-ads-visual-summary.md. Est. lift: not calculable from data collected; recommend as a message-match audit item for a future data pass focused on Google-specific landing pages.

**Standardize review-count display logic on the collection page so low-sample products don't borrow high-sample visual authority** — Products with 12 reviews and 886 reviews use identical 5-star iconography and sizing. Evidence: site-visual-summary.md (Collection Fold 2). Est. lift: not calculable without A/B baseline; lower priority, single-source evidence.

**Reconcile the Google star-rating snippet with on-site figures** — Google's ad snippet shows 3.9/966, well below the 4.9/12k-13k figures shown elsewhere. Evidence: google-ads-visual-summary.md. Est. lift: not calculable; this may reflect a stale or unmanaged Google Business/Merchant listing rather than a page-level test opportunity, worth a client conversation before scoping as a CRO test.

**Repeat the subscription-box guarantee/trust strip closer to the CTA on Ad 3's PDP** — The talisman PDP's captured folds show no guarantee copy or shipping-threshold badge near its "SHOP NOW" CTA, unlike the subscription LPs' sticky bottom bar with trust cues attached directly to the CTA. Evidence: meta-ads-visual-summary.md (Ad 3, "LP trust signals" note). Est. lift: not calculable without conversion data; narrower case of the broader trust-signal opportunity above, kept separate here because it is CTA-adjacent specifically rather than page-wide.

## Unused but Valuable Findings

- The live PDP fetch surfaces a "Buy 1 Get 1 50% OFF" bundle option not visible in the three screenshotted folds, suggesting the buy box has more upsell structure further down the page than the collected screenshots show; worth a dedicated PDP screenshot pass.
- Mindful Souls' $25.99-$39.97 entry price undercuts stated competitor Goddess Provisions' $55 entry price, a positioning advantage that should be protected rather than eroded by the current code fragmentation.

## Missing Data

- MISSING_DATA: pdp_screenshots — no dedicated PDP layout screenshots were captured. Ad 3's landing page folds and a live text-only fetch stand in for PDP visual data, but buy-box structure, pricing display, and trust-signal placement beyond what those sources show cannot be independently verified.
- Reviews & UGC — intentionally excluded from this collection pass per user instruction; to be sent separately. No "What Customers Love / Frustrates" section could be written without this data.
