# Panafrica CRO Research Audit

## Data Sources Used

- Meta Ads & Landing Pages (3 ads, screenshots + visual summary + live WebFetch of all 3 LP URLs)
- Google Ads Transparency Center (screenshots + visual summary)
- Reviews & UGC (raw text, 90+ reviews, Sahara model)
- PageSpeed / Core Web Vitals (Lighthouse JSON, homepage + PDP)
- Current Site Screenshots (homepage, collection, PDP, cart) + live WebFetch of homepage
- Competitor Analysis (self-researched via WebSearch, no user-provided data)

## Source Findings

### Meta Ads & Landing Pages

All three ads route to Arusha-line PDPs at the same 149€ price point, same 5-star/100-review trust block, same two-tier CTA stack ("Acheter en 1-clic" black / "Ajouter au panier" yellow), and the same fold-3 "OPTIMISTE ET ENGAGÉ" brand block — these are templated PDPs, not distinct campaign landing pages.

Message match is inconsistent across the three ads:
- **Ad 1** ("Votre coloris préféré ?") makes no discount claim in the ad copy, but its LP shows a yellow top banner promoting a WhatsApp Club (15€ off) that the ad never mentions, plus a floating "-10€" bubble the ad also never mentions.
- **Ad 2** (same copy as Ad 1) lands on a page with a *different* top banner (3x installment payment), again unrelated to the ad's own copy.
- **Ad 3** is the only ad that states an offer in-copy: "-10€ sur votre première commande" + "Livraison et retours offerts." Its LP shows the same floating "-10€" bubble as the other two ads, but the bubble carries no code or "first order" condition, so it's not confirmed whether the discount shown actually enforces the first-order restriction the ad promises.

Net effect: the floating "-10€" bubble is site-wide and channel-agnostic, but only 1 of 3 ads sets that expectation in its copy. Visitors from Ads 1 and 2 encounter an unadvertised discount (a mild positive surprise, but inconsistent messaging discipline); the ad account is not using the offer as a differentiator where it could.

Live WebFetch of the three LP URLs (2026-09-02) shows review counts and stock/availability status that no longer match the screenshots (e.g., Arusha Soleil now shows a "Coming soon" indicator alongside stock-available messaging, and review counts of 6-13 vs. the 100-review figure shown in the collected screenshots). This is noted as a data-timing gap, not a screenshot error — the site has changed between screenshot capture and this audit.

### Google Ads

Google Ads messaging leads with "ethical," "vegan," "eco-responsible," and "unique wax design" — none of the three Meta ads use this angle; Meta leads with color/style and (for Ad 3) a "-10€ first order" discount. The two channels are running fundamentally different value propositions to prospects.

Offer mismatch: Google Ads' primary offer is "jusqu'à -40% sur une sélection de paires, jusqu'au 28 juillet" (a dated promo, past its stated end date, still serving) plus "Retours gratuits." Meta's offer is the -10€ floating bubble. No shared, consistent sitewide offer exists across paid channels.

Technical issue: several live Google Ads Transparency Center tiles render unfilled dynamic template variables (`<Prix>`, `<Rating (Reviews)>`, `<Category>`, `<distance>`) and one raw "500. That's an error." tile — these appear to be currently active ad variants serving broken creative.

No 5-star/review trust signal appears in any Google ad creative, unlike the consistent 5-star/100-review block on every Meta-driven landing page.

### Reviews & UGC

90+ reviews reviewed (Sahara model, published Dec 2024–Jun 2026).

#### What Customers Love

- Comfort, repeated overwhelmingly across nearly every review ("très confortables," "confort incroyable," "confort absolu")
- Design/color originality ("j'adore l'agencement des couleurs," "couleurs magnifiques et harmonieuses," "modèle très original")
- Perceived quality/finish ("belle fabrication," "finitions impeccables," "très bonne qualité")
- Several reviewers cite the brand's African/ethical identity as part of the appeal ("le petit côté africain," "belles baskets qui donnent bonne conscience")

#### What Frustrates Customers

- **Sizing runs large** — the single most repeated complaint theme. Multiple reviewers explicitly advise sizing down: "le modèle taille grand ! Prendre une taille en moins," "Taillent grand," "sans doute 2 tailles en dessous," "J'aurai dû prendre la taille en dessous."
- **Color accuracy vs. product photos** — at least 2 reviewers note the physical product's colors are paler/duller than site photography: "The vividness of the colours in the photo does not correspond to reality, the colours on the sneakers are pale," "Le jaune est légèrement plus pâle que sur la photo."
- Isolated quality defects: one report of sole detachment ("la semelle est décollée sur 3cm"), one report of strong interior odor, one note on stiff sole, one note on missing arch support.

#### Client-Actionable Insights

- Sizing guidance on the PDP is not correcting the "runs large" pattern strongly enough — despite an existing Femme/Homme sizing note (per site-visual-summary), the complaint is still the top recurring theme across 90+ reviews. This is a product/content fix (clearer, more prominent sizing copy, or a fit-quiz), not a CRO test.
- Product photography color calibration should be reviewed against physical samples, particularly for lighter/pastel colorways — this is a photography/ops fix.
- Isolated QC complaints (sole detachment, odor) are too rare in this sample to indicate a systemic issue but are worth flagging to ops for monitoring.

### PageSpeed / Core Web Vitals

Source: Lighthouse JSON (mobile, simulated throttling), collected 2026-09-02.

**Homepage** (https://panafrica-store.com/): Performance score 0.49. LCP **16.6s**, TBT 350ms, FCP 5.6s, Speed Index 8.2s, Time to Interactive **23.4s**. CLS 0 (not a layout-shift problem — a raw load-speed problem).

**PDP** (https://panafrica-store.com/products/sahara-safran): Performance score 0.64. LCP 4.2s, TBT 490ms, FCP 3.2s, Speed Index 5.1s, Time to Interactive **23.3s**. CLS 0.001.

Both pages share a near-identical Time to Interactive figure (~23s) despite very different LCP, suggesting a shared render-blocking or third-party script cost that dominates interactivity regardless of page type. The homepage's 16.6s LCP is more than 5x Google's "poor" threshold (2.5s+) and is the single worst metric collected across the site.

### Competitor Analysis

No user-provided competitor data (raw/competitors.md not present). Self-researched via WebSearch, 2026-09-02.

Panafrica occupies a narrow niche (wax-print, Africa-manufactured, ethical sneakers) with few direct one-to-one competitors found in research. The closest comparable is:

| Brand | Position | Price range | Notable weakness (from public reviews) |
|---|---|---|---|
| **Veja** | Broader "ethical French sneaker" category leader, much larger scale/brand recognition | ~€125–€215 | Stiff break-in period, ankle-rubbing tongue, inconsistent comfort/support cited in multiple reviews |
| **Panafrica** (this brand) | Niche African-wax-print specialist, smaller scale | €79–€159 (site-observed) | Sizing runs large (top review complaint), catastrophic homepage load speed |

Because no direct wax-print-sneaker competitor with comparable positioning surfaced in research, Panafrica is effectively category-defining in its specific niche — its competitive pressure comes more from the broader "ethical/sustainable sneaker" set (Veja being the clearest example) than from a like-for-like rival. This is a data gap: a client-provided competitor list (if one exists) would sharpen this section.

### Emails

Not collected (raw/emails.md not present — skipped per manifest).

### Inspiration Sites

Not collected (raw/inspiration.md not present — skipped per manifest).

### Non-Data Context

Not collected (raw/context.md not present — skipped per manifest).

### Current Site Screenshots

**Homepage:** Fold 1 is pure lifestyle storytelling — a collage-style hero image, "NOUVELLE COLLECTION" headline, and a single "DÉCOUVRIR" CTA with no product, price, or shop-specific path visible. Fold 2 repeats brand messaging ("BASKETS MADE IN AFRICA") with a product name row (no prices). Products with visible prices don't appear until **fold 3** — three screens deep. No trust signal (review count, star rating, guarantee, shipping promise) appears anywhere in folds 1–3. No sticky header or persistent shop CTA exists on the homepage. Live WebFetch confirms this pattern: hero is "A DROP OF SUMMER" motif and brand mission copy, with pricing only surfacing once catalog sections load.

**Collection page:** Flat pricing only on every card (no compare-at/sale badges). One product card mid-grid (collections-f3.png) exposes a full size run and "Add to cart" directly in the grid, while every other card shows only image + name + price — an inconsistent quick-add implementation, not confirmed as intentional. Screenshots were captured in English while homepage/PDP were captured in French — a locale-capture inconsistency, not a site defect (per manifest note).

**PDP:** Trust signal (5-star, review count) sits directly under the product title, above the buy box — the highest-priority placement on the PDP. Two-tier CTA ("Acheter en 1-clic" / "Ajouter au panier") with a sticky bottom bar. Red stock-urgency messaging present ("Plus que 3 produits en stock"). Shipping/returns copy is one fold below the CTA, not adjacent to it. The standard-traffic Sahara-Safran PDP shows **no** "Nos recommandations" cross-sell block in the captured fold, while the ad-traffic Arusha PDPs (same template, different product) **do** show one in the equivalent position — an inconsistency in whether cross-sell renders.

**Cart:** Right-side slide-out drawer. Free-shipping progress bar already shown fully unlocked at this cart's item total. One cross-sell item shown (espadrilles, 35€). Two-tier CTA repeated ("Passer la commande" / "Acheter en 1-clic"). The floating "-10€" bubble is visible here too, consistent with PDP and all three ad LPs.

## Cross-Source Themes

1. **Message/offer inconsistency across every paid and owned surface** — Meta ads, Google Ads, and the on-site floating "-10€" bubble each promise a different (or no) offer, and Google Ads' headline promo is expired. Evidence: Meta Ads visual summary, Google Ads visual summary. This is the highest revenue-relevance theme because it touches 100% of paid traffic entering the funnel.
2. **Homepage has no purchase path or trust signal until 3 screens down, compounded by a 16.6s LCP** — the homepage is simultaneously the slowest page on the site and the one most starved of conversion mechanics in its early folds. Evidence: site-visual-summary, live homepage WebFetch, pagespeed.md.
3. **Sizing confusion is the dominant, repeated customer complaint** — named across dozens of independent reviews spanning a year-plus of orders, despite existing sizing copy on the PDP. Evidence: reviews.md (recurring across many reviewers), site-visual-summary (existing sizing note not resolving it).

## Top Test Opportunities

**Fix homepage Largest Contentful Paint (16.6s → target sub-4s)** — The homepage's hero image/collage loads in 16.6 seconds on mobile (Lighthouse, simulated throttling), more than 6x Google's "poor" threshold. Combined with a 23.4s Time to Interactive, most mobile visitors are likely abandoning before the page is usable. Evidence: pagespeed.md. Est. lift: sessions/mo not provided — cannot calculate $; directionally, LCP this severe typically drives double-digit bounce-rate reduction once resolved, per Google's own CWV research (not brand-specific data, cited as industry context only).

**Add a shop-now CTA and price/trust signal to homepage fold 1** — The homepage hero (both in screenshots and live WebFetch) is pure lifestyle imagery and brand mission copy ("NOUVELLE COLLECTION," "A DROP OF SUMMER") with a single "DÉCOUVRIR" CTA. No product, price, review count, or star rating appears until fold 3. A first-time visitor cannot see what they'd be buying or why to trust the brand without scrolling three full screens. Evidence: site-visual-summary, live homepage WebFetch. Est. lift: sessions/mo not provided — cannot calculate $.

**Unify the sitewide discount offer across Meta, Google, and on-site messaging** — Three different offers are currently live: Meta's floating "-10€" bubble (only stated in Ad 3's copy), Google's expired "-40% until July 28" promo, and a WhatsApp Club 15€ discount referenced only on Ad 1's landing page banner. A visitor comparing ads or channels sees conflicting numbers. Evidence: meta-ads-visual-summary.md, google-ads-visual-summary.md. Est. lift: sessions/mo not provided — cannot calculate $; message-match is a top-5 documented CRO lever for paid landing pages.

**Fix broken dynamic-variable Google Ad tiles** — Multiple currently-active Google Ads Transparency Center tiles render unfilled template placeholders (`<Prix>`, `<Rating (Reviews)>`, `<Category>`, `<distance>`) or a raw "500. That's an error." creative. These are live spend serving broken ads. Evidence: google-ads-visual-summary.md. Est. lift: sessions/mo not provided — cannot calculate $; this is closer to a paid-media hygiene fix than a CRO test, but is high-confidence and low-effort to correct.

**Add sizing reassurance directly at the size selector on PDP** — The single most repeated complaint across 90+ reviews is that shoes "run large," with reviewers independently recommending sizing down by a full size or more. The existing PDP sizing note (per site-visual-summary) is not resolving this at scale. Testing a more prominent fit-callout (e.g., "Runs large — most customers size down" inline at the size selector, not buried in an accordion) could reduce size-related returns and pre-purchase hesitation. Evidence: reviews.md (recurring theme across dozens of reviewers), site-visual-summary. Est. lift: sessions/mo not provided — cannot calculate $.

**Standardize the "Nos recommandations" cross-sell block across all PDPs** — Ad-traffic Arusha PDPs show a cross-sell recommendation directly below delivery info; the standard-traffic Sahara-Safran PDP does not show this block in the same fold. If this is a genuine gap (not just a screenshot-timing difference), standardizing it sitewide is a straightforward AOV lever already proven to render correctly elsewhere on the same template. Evidence: meta-ads-visual-summary.md (Ad 2/3 LPs show cross-sell), site-visual-summary (Sahara-Safran PDP fold 2 does not). Est. lift: sessions/mo not provided — cannot calculate $.

**Move trust signal (5-star/review count) to homepage and collection page** — The 5-star/review-count block appears prominently on every PDP (directly under product title, above the buy box) but is entirely absent from the homepage and collection page. Evidence: site-visual-summary (homepage: "no review count, star rating... visible in any of the three homepage folds"; collection: "no star rating on cards"). Est. lift: sessions/mo not provided — cannot calculate $.

**Resolve or intentionally roll out collection-grid quick-add** — One product card in the collection grid (collections-f3.png) shows a full size run and "Add to cart" directly in the grid; no other card does. This reads as either an unfinished feature or a hover-state capture artifact. If intentional, sitewide quick-add on collection cards is a well-documented friction-reduction lever; if unintentional, it should be fixed as a bug before being treated as a design decision. Evidence: site-visual-summary (Open Question flagged in manifest). Est. lift: sessions/mo not provided — cannot calculate $.

**Add a guarantee/returns trust element adjacent to the PDP buy box** — Shipping and returns copy ("Livraison et Retours offerts dès 100€") currently sits one fold below the CTA stack rather than directly beside it. Reviews show no complaints about returns specifically, but the standard CRO pattern of placing a low-risk reassurance signal immediately next to the primary CTA is untested here. Evidence: site-visual-summary (PDP fold 1/2 trust signal note). Est. lift: sessions/mo not provided — cannot calculate $.

**Investigate and resolve "Coming soon" / stock-status contradiction on Arusha PDPs** — Live WebFetch (2026-09-02) of all three ad-linked Arusha PDPs shows a "Coming soon" indicator displayed simultaneously with in-stock messaging and functioning size selectors. If this is currently live, paid traffic may be landing on pages that appear unavailable for purchase. This was not visible in the collected screenshots (captured earlier), so it may be a state change since collection, not a standing issue — needs client confirmation before being treated as a live bug. Evidence: live WebFetch of arusha-soleil-1, arusha-ivoire, arusha-niagara product pages. Est. lift: sessions/mo not provided — cannot calculate $; if confirmed live, this is a blocking issue, not just a CRO test.

## Unused but Valuable Findings

- Homepage and PDP Time to Interactive are nearly identical (~23s) despite very different LCP, suggesting a shared render-blocking/third-party script cost worth a technical audit beyond image optimization alone.
- Only one Google Ad angle ("vegan") differs meaningfully from the ethical/eco-responsible cluster — worth testing whether a vegan-specific landing experience outperforms the generic ethical messaging, but there isn't enough evidence here to size it as a standalone test.

## Missing Data

- No competitor data was provided by the client (raw/competitors.md absent) — the Competitor Analysis section above relies entirely on self-research and found no direct wax-print-sneaker rival; a client-supplied list would sharpen this.
- Emails, Inspiration Sites, and Non-Data Context were not collected (per manifest, not provided) — no findings possible for these sections.
- Store URL/product URL used for PageSpeed were inferred from the Lighthouse JSON `requestedUrl` field, not explicitly confirmed by the user (per manifest warning).
- No monthly session or AOV figures were provided, so every Est. lift above omits a dollar calculation. All 10 opportunities are sized by evidence strength and fixability only, not revenue projection.
