# Poupette St Barth Roadmap Seed

**Store:** https://www.poupettestbarth.com
**AOV:** unknown
**Monthly sessions:** unknown
**Data sources:** Meta Ads and Landing Pages, Google Ads Transparency, PageSpeed / Core Web Vitals, Current Site Screenshots

## Key Insights

No trust signal (review count, star rating, or guarantee badge) is visible above the fold anywhere in the funnel: not on the homepage's three folds, not on Ad 2's landing page (a search-results page for "sasha," all three folds), not on the collection page, not on the PDP buy box, and not in the cart. The only trust-adjacent elements found sit in the footer ("Free shipping," "Secured payment," "Simple returns") or buried in PDP/cart copy ("Livraison internationale offerte," FAQ return questions) — all below where a visitor decides to convert. This pattern repeats across 5 of the 6 collected sources, making it the strongest evidence chain in this audit.

Mobile Core Web Vitals fail Google's "good" thresholds on both pages tested. Homepage LCP is 13.7s and Time to Interactive is 17.1s; PDP is worse, at 18.1s LCP and 23.3s Time to Interactive. Both pages score under 0.1 on the LCP metric specifically. CLS is not an issue (near zero on both pages) — the problem is load and interactivity speed, not layout shift. Since both Meta and Google are actively running ads that drive mobile clicks, this speed gap sits directly in the paid traffic path.

Ad-to-landing-page message match is confirmed broken for one live ad and unverifiable for two others. Ad 2 promises general "Saint Barth, everywhere" resort-wear messaging with no named product, then lands visitors on a raw site-search results page for "sasha" — breadcrumb, filter panel, and "22 results found" heading, with nothing echoing the ad's headline or caption. Ad 1 ("handmade, limited runs") and Ad 3 ("The Sasha: our best-seller") have no landing page screenshots collected, so it's unknown whether the same mismatch exists there too. Separately, Google Ads and Meta Ads run on entirely different messaging themes ("Iconic Prints, Timeless Cuts" and seasonal collection pushes on Google vs. handmade/craft and best-seller framing on Meta), with zero copy overlap between the two channels.

## Top Test Opportunities

### 1. Add trust signals to the PDP buy box
**What's broken:** The PDP right column shows product title, colorway, price (€330,00 with "Taxes incluses"), a bulleted feature list, then a full-width black "AJOUTER AU PANIER" button. Nowhere in this buy box, or anywhere else on the page's three captured folds, is there a review count, star rating, or guarantee badge. The only trust-adjacent lines are "Livraison internationale offerte" (below the Add to Cart button) and FAQ accordion questions about returns, both positioned well below the purchase decision point.
**Evidence:** site-visual-summary.md PDP, all 3 folds
**Key data:** Zero review/rating elements found across all 3 PDP folds
**Est. lift:** unknown (no baseline conversion or session data provided)

### 2. Fix Ad 2's landing page to match its ad promise
**What's broken:** Ad 2's video creative headline reads "Bring a little Saint Barth wherever you are. Effortless prints, effortless days," with a caption of "St Barth, everywhere." Clicking through lands the visitor on a page whose first fold is a breadcrumb reading "Home / Search: 22 results found for 'sasha'," a "SEARCH" page heading, a pre-filled search box showing "sasha," a left-side filter panel (Gender, Product Type, Size, Material, Color), and a product grid beginning below the fold. No hero image, headline, or copy on the landing page echoes the ad's "everywhere / effortless" framing — it reads as a raw internal search results page, not a designed landing page.
**Evidence:** meta-ads-visual-summary.md Ad 2, ad-creative-2.png, ad2-landing-f1/f2/f3.png
**Key data:** Landing page shows "22 results found for 'sasha'" with no ad-echoing copy
**Est. lift:** unknown (no ad spend or CVR data provided)

### 3. Reduce PDP load time
**What's broken:** The PDP (tested on the "ROBE LONGUE KORA - Pink Padang" product page) loads slowly enough on mobile that Lighthouse records a 0 score on Largest Contentful Paint. The page is structured with a thumbnail strip and primary product photo on the left and buy box on the right — heavy imagery likely contributes to the delay, though this wasn't isolated in the lab report.
**Evidence:** pdp-pagespeed.json (mobile Lighthouse, 2026-09-09)
**Key data:** LCP 18.1s, Time to Interactive 23.3s, Performance score 62/100, Speed Index 8.8s
**Est. lift:** unknown (no sessions/AOV data provided)

### 4. Reduce homepage load time
**What's broken:** The homepage hero is a full-bleed video/image of a model in a printed dress with centered headline text "THE SEASON'S ESSENTIALS" and a "SHOP" link. This heavy hero media is the likely driver of load delay, though not isolated in the lab report.
**Evidence:** homepage-pagespeed.json (mobile Lighthouse, 2026-09-09)
**Key data:** LCP 13.7s, Time to Interactive 17.1s, Performance score 64/100, Speed Index 5.5s
**Est. lift:** unknown (no sessions/AOV data provided)

### 5. Confirm Ad 1 and Ad 3 landing pages match their ad promise
**What's broken:** Ad 1's creative promises handmade, limited-run craftsmanship; Ad 3's creative names "The Sasha" as the brand's best-seller. Neither ad's landing page was captured, so — given Ad 2's confirmed mismatch above — it's unknown whether these two ads send traffic to pages that reinforce or undercut their specific promises.
**Evidence:** meta-ads-visual-summary.md (Ad 1 and Ad 3 landing page fields marked "Not collected")
**Key data:** 2 of 3 live Meta ads have no landing page data
**Est. lift:** unknown — data collection gap, not yet a confirmed opportunity

### 6. Add sale/compare pricing clarity to the collection page
**What's broken:** The collection page (titled "NEW COLLECTION," 103 products) shows every product tile with a single straight price (e.g., "€390,00") — no compare-at/strikethrough pricing, no sale badges, across all three folds captured, despite the site running a site-wide 10% first-order offer in its announcement bar.
**Evidence:** site-visual-summary.md Collection Page, "Price display" note
**Key data:** 0 of the tiles across 3 folds show compare-at pricing or sale badges
**Est. lift:** unknown — needs confirmation of current promo status before sizing

### 7. Make the PDP Add to Cart button sticky
**What's broken:** "AJOUTER AU PANIER" is a full-width black button positioned below the product description and size guide on fold 2. By fold 3, as the visitor scrolls into the shipping/returns accordions and FAQ, the button has scrolled entirely out of view with no sticky/fixed replacement.
**Evidence:** site-visual-summary.md PDP, "CTA behavior" note
**Key data:** CTA absent from fold 3 of 3 captured PDP folds
**Est. lift:** unknown (no baseline conversion or session data provided)

### 8. Add product/offer specificity to the homepage hero
**What's broken:** Fold 1 of the homepage shows a full-bleed lifestyle image, the generic headline "THE SEASON'S ESSENTIALS," and a single unstyled "SHOP" link with no featured product, price, or time-bound call to action — despite an active 10% first-order discount already running in the announcement bar directly above it.
**Evidence:** site-visual-summary.md Homepage Fold 1, live homepage WebFetch
**Key data:** Hero contains 0 product-specific or offer-specific elements
**Est. lift:** unknown (no baseline conversion or session data provided)

## Unused Findings

- The PDP was captured in French (poupettestbarth.com/fr) while homepage and collection were captured in English; the PDP experience for English-primary traffic has not been directly reviewed in this audit.
- Google Ads Transparency shows a kids' Girls Clothing line and offer ("10% off your First Order") not represented anywhere in the Meta creatives collected — worth checking as a separate underexplored funnel.
