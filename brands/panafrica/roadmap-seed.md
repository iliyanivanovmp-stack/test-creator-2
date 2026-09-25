# Panafrica Roadmap Seed

**Store:** https://panafrica-store.com
**AOV:** unknown (product prices observed range €79–€159, most products €125–€149)
**Monthly sessions:** unknown
**Data sources:** Meta Ads & Landing Pages, Google Ads Transparency, Reviews & UGC, PageSpeed/Core Web Vitals, Current Site Screenshots, Competitor Analysis (self-researched)

## Key Insights

Panafrica's homepage is the site's biggest single liability: mobile LCP is 16.6s and Time to Interactive is 23.4s (Lighthouse, simulated throttling) — more than 6x Google's "poor" threshold — and the hero itself is pure lifestyle storytelling with no product, price, or trust signal until fold 3. A first-time visitor has to both wait through a catastrophically slow load and scroll three screens before seeing what's for sale or why to trust the brand.

Paid traffic is running three different, uncoordinated offers. Meta's floating "-10€" bubble appears on every ad-linked landing page regardless of which ad drove the click, but only Ad 3's copy ("-10€ sur votre première commande") actually states it — Ads 1 and 2 make no discount claim at all, and Ad 1's landing page instead surfaces an unrelated WhatsApp Club banner (15€ off). Google Ads runs a separate, dated "-40% until July 28" promo that has passed its own stated end date, plus "Retours gratuits" — neither offer matches what Meta shows. Several currently-active Google Ads Transparency Center tiles also render broken, unfilled dynamic-variable placeholders (`<Prix>`, `<Rating (Reviews)>`) or a raw "500. That's an error." creative.

Ninety-plus customer reviews (Sahara model, spanning over a year of orders) converge overwhelmingly on comfort and color/design originality as what customers love ("confort incroyable," "j'adore l'agencement des couleurs"). The single most repeated complaint, independently raised by dozens of separate reviewers, is that the shoes run large: "le modèle taille grand ! Prendre une taille en moins," "Taillent grand," "sans doute 2 tailles en dessous." This persists despite an existing sizing note on the PDP, meaning current sizing guidance isn't cutting through at the point of decision.

## Top Test Opportunities

### 1. Fix homepage Largest Contentful Paint
**What's broken:** The homepage hero is a two-panel collage-style lifestyle image (torn-photo/polaroid aesthetic) with headline "NOUVELLE COLLECTION" over "Découvrez les nouveautés de la rentrée" and a single "DÉCOUVRIR" CTA button. This hero takes 16.6 seconds to render its largest element on mobile (Lighthouse, simulated throttling), against a Time to Interactive of 23.4 seconds — the worst performance figures collected anywhere on the site.
**Evidence:** pagespeed.md (Lighthouse JSON, homepage)
**Key data:** LCP 16.6s, TTI 23.4s, Performance score 0.49, FCP 5.6s, Speed Index 8.2s
**Est. lift:** sessions/mo not provided — cannot calculate $. Directionally high: LCP this severe is well past the range where most mobile visitors abandon before interacting.

### 2. Add a shop-now path to homepage fold 1
**What's broken:** Homepage fold 1 shows only the lifestyle hero collage and "DÉCOUVRIR" CTA — no product name, price, or trust signal. Fold 2 repeats brand messaging ("BASKETS MADE IN AFRICA") with a name-only product row (no prices). Priced products with buyable cards don't appear until fold 3, three full screens down. No star rating or review count appears anywhere in folds 1-3.
**Evidence:** site-visual-summary.md (homepage), live WebFetch of panafrica-store.com
**Key data:** Zero trust signals across 3 homepage folds; pricing absent until fold 3
**Est. lift:** sessions/mo not provided — cannot calculate $.

### 3. Unify the discount offer across Meta, Google, and on-site
**What's broken:** A floating "-10€" bubble sits in the bottom-right corner on every Arusha PDP and in the cart drawer, regardless of entry point. Only Ad 3's copy states this offer explicitly ("-10€ sur votre première commande"); Ads 1 and 2 make no discount claim in-copy, and Ad 1's LP top banner instead promotes an unrelated WhatsApp Club 15€ discount. Google Ads separately promotes "jusqu'à -40% sur une sélection de paires, jusqu'au 28 juillet" — a promo past its own stated date, still serving live.
**Evidence:** meta-ads-visual-summary.md (Ads 1, 2, 3), google-ads-visual-summary.md
**Key data:** 3 distinct offers live simultaneously (-10€ bubble, WhatsApp 15€, Google -40% expired); message match is a documented top-5 landing-page CRO lever
**Est. lift:** sessions/mo not provided — cannot calculate $.

### 4. Fix broken Google Ads creative variants
**What's broken:** Multiple currently-active tiles in the Google Ads Transparency Center grid show unfilled dynamic template variables instead of real values — `<Prix>`, `<Rating (Reviews)>`, `<Category>`, `<distance>` — and one tile shows a raw "500. That's an error. There was an error. Please try again later." creative in place of an ad.
**Evidence:** google-ads-visual-summary.md
**Key data:** At least 4 distinct broken/placeholder tiles observed in a 25+ tile grid
**Est. lift:** sessions/mo not provided — cannot calculate $. Low-effort, high-confidence media hygiene fix.

### 5. Add prominent sizing reassurance at the PDP size selector
**What's broken:** The PDP size selector (36-46 range, with unavailable sizes greyed out) sits below the product title and above the two-tier CTA stack. A Femme/Homme sizing conversion note exists but is not prominent at the point of size selection. Across 90+ reviews, the "runs large" complaint is repeated independently by dozens of customers over more than a year of orders, despite this existing copy.
**Evidence:** reviews.md (recurring across dozens of reviewers, e.g. "prendre une taille en moins," "2 tailles en dessous"), site-visual-summary.md (PDP sizing note)
**Key data:** Sizing is the single most repeated complaint theme in the entire review set
**Est. lift:** sessions/mo not provided — cannot calculate $.

### 6. Standardize the cross-sell block across all PDPs
**What's broken:** On ad-traffic Arusha PDPs, a "Nos recommandations" cross-sell block (e.g., "Accra" shoe at 85€, "Sac Kariba congrès" tote at 20€) renders directly below the delivery-estimate copy, right after the CTA stack. The standard-traffic Sahara-Safran PDP, same template, does not show this block in the equivalent fold.
**Evidence:** meta-ads-visual-summary.md (Ad 2/3 landing pages), site-visual-summary.md (Sahara-Safran PDP, fold 2: "No 'Nos recommandations' cross-sell block visible")
**Key data:** Same PDP template, inconsistent cross-sell rendering between ad-traffic and organic PDPs
**Est. lift:** sessions/mo not provided — cannot calculate $.

### 7. Add trust signal to homepage and collection page
**What's broken:** The 5-star / review-count block sits directly under the product title on every PDP, above the buy box — the highest-priority position on that page. The homepage (3 folds reviewed) and collection page (product grid, cards showing only image/name/price) show no star rating or review count anywhere.
**Evidence:** site-visual-summary.md (homepage: "no review count, star rating... visible"; collection: "no star rating on cards")
**Key data:** Trust signal present on 1 of 3 core page types reviewed
**Est. lift:** sessions/mo not provided — cannot calculate $.

### 8. Resolve collection-grid quick-add inconsistency
**What's broken:** One product card mid-grid on the collection page (collections-f3.png) shows a full size run (36-43, 44-47) and an "Add to cart" button rendered directly in the grid card. Every other card on the same grid shows only product image, name, and price with no inline purchase controls.
**Evidence:** site-visual-summary.md (collection page, flagged as an unresolved layout question in the manifest)
**Key data:** 1 of roughly 12+ visible collection cards shows this behavior; unclear if intentional feature, hover-state artifact, or bug
**Est. lift:** sessions/mo not provided — cannot calculate $.

## Unused Findings

- Live WebFetch (2026-09-02) of all three Arusha PDPs shows a "Coming soon" indicator alongside active stock/size-selector controls — a possible availability-messaging bug that postdates the collected screenshots and needs client confirmation before treating as a live issue.
- Homepage and PDP share a near-identical ~23s Time to Interactive despite very different LCP, suggesting a shared render-blocking/third-party script cost worth a dedicated technical audit beyond image optimization.
