# Gorilla Sports CRO Research Audit

## Data Sources Used

- User-provided collection manifest: `brands/gorilla-sports/manifest.md`
- Meta ads and landing-page notes: `raw/meta-ads.md`
- Meta ads visual summary: `raw/meta-ads-visual-summary.md`
- Google Ads visual summary: `raw/google-ads-visual-summary.md`
- PageSpeed markdown: `raw/pagespeed.md`
- PageSpeed JSON: `raw/gorillasports-homepage-pagespeed.json`, collected 2026-08-10T13:54:49.598Z
- PageSpeed JSON: `raw/gorillasports-collections-pagespeed.json`, collected 2026-08-10T13:56:03.301Z
- Non-data context: `raw/context.md`
- Site visual summary: `raw/site-visual-summary.md`
- Live store text fetch: https://gorillasports.fi/, fetched during audit on 2026-08-10
- Self-researched competitor sources, researched 2026-08-10: Fitnesstukku home gym page, XXL multigym benches category, Gymstick home gyms page, GFitness homepage, Treenikauppa Trustpilot page

## Source Findings

### Meta Ads & Landing Pages

Ad 1 promotes discounted home gym and bench equipment with carousel cards, "ALF jopa yli -40%" sale messaging, "Shop Now" buttons, and 2-year warranty copy. Its shared landing page is a "Kuntosalipaketit" collection-style page with an intro paragraph, popular-products carousel, filters, sorting, a five-column product grid, discount badges, red sale prices, compare-at prices, savings labels, star ratings, and black limited-time strips reading "Hinta voimassa vain 7 päivää." The message match is directionally strong: the ad promises home gym equipment and discounts, and the page shows gym-package products with visible discounts.

Ad 2 uses a video angle around building a dream home gym with complete gym packages for home or workspace. It lands on the same "Kuntosalipaketit" page as Ad 1, so the category/title match is strong. The gap is decision support: no page-level CTA, package selector, "best for" guide, shipping/returns block, or review aggregate is visible near the first product decision. Product-card savings buttons are present, but the page appears to rely on browsing rather than helping shoppers choose a complete package.

Ad 3 promotes push-up and parallel-bar home training, small-space suitability, durable frame, beginner-to-advanced use, and bodyweight development. The landing page is a "Parallel Bars" category with four product cards, discounts from -47% to -72%, star ratings, sale pricing, and product education below the grid. Message match is strong on product category. The friction is that the strongest ad claims, including small-space fit, durability, exercise outcomes, and beginner suitability, are not visible as product-card decision criteria in Fold 1.

Across Meta, offer and category match are solid, but the landing pages make shoppers compare products without much structured buying help. The same product-grid mechanic is used for complete gym packages and parallel bars, even though those categories imply different purchase questions.

### Google Ads

Google Ads screenshots show broad category coverage: weight plates, functional training, wall-mounted pull-up bars, gym mats, kettlebells, weight benches, adjustable weights, push-up bars, barbell sets, step boards, ankle straps, jump ropes, and leg weights. Copy repeatedly positions Gorilla Sports as a Finnish online store with quality products for home or gym. Some ads mention discounts such as "jopa -40%" and "Alennukset jopa -40% katso."

Google is broader and more search-discovery oriented than Meta. Meta ads are product/offer-led with richer creative and explicit "Shop Now" CTAs; Google ads are more text-forward, category-led, and repetitive. The shared opportunity is to make category landing pages translate broad demand into guided product selection, because both channels push shoppers into catalog/category experiences.

### Reviews & UGC

`raw/reviews.md` was not present. The manifest states reviews were skipped because there are no reviews for this brand as a selected source.

#### What Customers Love

- No collected customer-review dataset exists for Gorilla Sports in this collection.

#### What Frustrates Customers

- No collected customer-review dataset exists for Gorilla Sports in this collection.

#### Client-Actionable Insights

- The skipped review source means the client should not base product, operations, or support fixes on this audit alone.
- The site itself displays trust/review proof in screenshots: homepage trust strip shows 4.3 rating, 7000+ reviews, 100,000+ satisfied customers, 30-day return right, Finnish strength-related claim, and AA credit rating; PDP Fold 1 shows 55 product reviews for "Säädettävä käsipainosarja 30 kg."

### PageSpeed / Core Web Vitals

Only mobile Lighthouse JSON files were collected; no desktop PageSpeed report was present. The JSON reports had no `loadingExperience` or `originLoadingExperience`, so field Core Web Vitals were unavailable. Lab data is still usable for prioritization.

| Page | Collection time | Device | Performance | FCP | LCP | TBT | CLS | INP |
|---|---:|---|---:|---:|---:|---:|---:|---|
| Homepage, https://gorillasports.fi/ | 2026-08-10T13:54:49.598Z | mobile | 55/100 | 2.2s | 5.4s | 630ms | 0 | not available |
| Collection, https://gorillasports.fi/collections/kuntosalilaitteet | 2026-08-10T13:56:03.301Z | mobile | 61/100 | 2.5s | 4.3s | 740ms | 0 | not available |

The conversion risk is slow above-the-fold rendering on traffic-heavy entry pages. The homepage mobile LCP of 5.4s and collection mobile LCP of 4.3s both exceed the 2.5s "good" threshold. TBT is also heavy at 630ms on homepage and 740ms on collection, which can delay interaction with navigation, search, filters, product cards, and add-to-cart controls. CLS is 0 in the reports, so layout shift is not the observed issue.

### Competitor Analysis

No user-provided `raw/competitors.md` file was present. Competitors below are self-researched during audit on 2026-08-10.

| Brand/source | Evidence found | Price/assortment signal | Key features | Weakness vs. Gorilla Sports opportunity |
|---|---|---|---|---|
| Fitnesstukku | Self-researched home gym page showed 7 homegym products, "Etsi yli 15 000 tuotteen joukosta," free shipping over 49 EUR, free returns, and 14-day cancellation. | Visible homegym examples include resistance bands from 4.90 EUR to a 30 kg weight vest at 211.90 EUR sale price. | Massive catalog, clear "Osta" card CTAs, filters, price guarantee/help links. | Homegym page is accessory-heavy; Gorilla can differentiate complete setups and package guidance rather than only breadth. |
| XXL Finland | Self-researched multigym benches category showed 3 articles, price range 79.99-199 EUR, TITAN LIFE brand, store availability filters, fast delivery, free return/exchange, and bonus points. | Bench/multigym category spans 79.99-199 EUR. | Big-box trust, store availability, low prices, membership/bonus points. | Narrow category depth in observed page; Gorilla can win on deeper specialist range and comparison help. |
| Gymstick | Self-researched home gyms page showed 6 home gym machine products and company contact in Lahti. | Home gym machines page showed six products including HG2.0, HG3.0, HG4.0, PRO20.0, leg press add-on, and PRO20.0 with leg press. | Finnish equipment brand, manufacturer credibility, clear product line progression. | Product-line credibility is strong; Gorilla needs clearer "which setup fits my goal/space/budget" comparison on collections. |
| GFitness | Self-researched homepage positions the store as a wide assortment fitness goods store with categories for commercial fitness equipment, home gym, used equipment, CrossFit, functional training, and service offerings. | Public page did not expose comparable product prices in the fetched text. | Commercial/pro services, used equipment, warehouse/store presence in Lahti. | Stronger B2B/service posture; Gorilla can stay focused on consumer home gym convenience and fast buying. |
| Treenikauppa | Trustpilot page showed 4.8 rating from 509 reviews, 417 reviews in the last 12 months, and company copy claiming a large selection of exercise bikes, treadmills, weight plates, dumbbells, and more. | Pricing not fetched from product pages in this audit. | Strong third-party review proof and Finnish contact details. | Gorilla screenshots show internal review/trust proof, but external review proof was not collected; trust reinforcement near decisions matters. |

### Emails

Email campaigns were skipped in the manifest. No `raw/emails.md` or email screenshots were present. Email message match, subject-line strategy, post-click flow, and lifecycle conversion gaps cannot be assessed from the collected data.

### Inspiration Sites

Inspiration sites were skipped in the manifest. No `raw/inspiration.md` or inspiration screenshots were present. The audit does not use external inspiration patterns beyond direct competitor research.

### Non-Data Context

The brand is Finnish, the store URL is https://gorillasports.fi/, and the output should remain in English even though the collected website UI is Finnish. The roadmap has 8 test slots. Ad 1 and Ad 2 use the same landing page, and the user believes that page is also the collection page. Reviews were intentionally skipped because there are no reviews for this brand as a selected source.

### Current Site Screenshots

Homepage: Fold 1 is a black/red gym-photography hero with header offer bar, black navigation, logo, phone-ordering text, search field, account icon, cart icon, headline "Sinun kotisi. Sinun salisi.", exercise copy, and a large red CTA-style block for "Taljalaitteet jopa -50%." The trust strip below the hero shows 4.3 rating with 7000+ reviews, 100,000+ satisfied customers, 30-day return right, Finnish strength-related claim, and AA credit rating. Fold 2 and Fold 3 are product-carousel and category-grid heavy, with sale badges and red prices. The main homepage friction is that the trust proof sits below a promotional hero, while the hero CTA is category-specific and does not immediately explain why that category is the best next action for a home-gym shopper.

Collection page: No separate canonical `collection-f1.png`, `collection-f2.png`, or `collection-f3.png` screenshots were present. The shared Ad 1/2 landing screenshots show a "Kuntosalipaketit" collection-style page with intro copy, popular-products carousel, filters, sorting, and a product grid. Product cards display discount badges, star ratings, red sale prices, compare-at prices, savings labels, and black "Hinta voimassa vain 7 päivää" urgency strips. The friction is that the grid has many strong commerce signals but little category-level guidance: no package comparison, no "best for small spaces/beginners/heavy lifters" treatment, no setup-size calculator, and no sticky path to narrow products.

PDP: The product page for "Säädettävä käsipainosarja 30 kg" uses a left image gallery and right buy box. Fold 1 shows rating and 55 reviews, brand Gyronetics, title, bullets, red discount badge, 45.95 EUR sale price, 109.95 EUR compare-at price, red savings label, black "Lisää ostoskoriin" button, payment/invoice box, stock/delivery copy, limited-time offer box, and trust bullets. Fold 2 shows a frequently-bought-together block with three checked items, total 75.85 EUR, and a black add-to-cart button; a sticky bottom add-to-cart bar is visible. Fold 3 shows feature imagery, descriptive copy, feature list, accordions, phone-ordering panel, WhatsApp panel, and sticky add-to-cart. The PDP has strong price/trust mechanics; the main risks are buy-box density and a preselected bundle mechanic that may need clearer benefit framing.

Cart: The cart drawer opens from the right over a dimmed page. It shows "Ostoskori," item count 1, close icon, product thumbnail, product name, price, compare-at price, savings label, quantity stepper, remove icon, fixed black "Siirry kassalle" checkout button, and trust panel for secure payments, 30-day return right, and 2-year warranty. No upsell, cross-sell, bundle reminder, or free-shipping threshold mechanic is visible in the cart drawer screenshot.

## Cross-Source Themes

1. Guided category selection is the highest-evidence theme. Meta Ads, Google Ads, ad landing pages, site screenshots, and competitor research all point to shoppers entering broad catalog/category pages. Revenue potential is high because these are paid-entry and collection-browsing moments; funnel importance is high because they precede product selection.
2. Trust and urgency are present but inconsistently placed. Homepage, PDP, collection cards, cart, and competitor research show that reviews, returns, delivery, warranty, savings, and limited-time pricing matter. Revenue potential is medium-high because the proof exists, but it is not always close to the first decision point on landing pages.
3. Mobile speed is a conversion constraint. PageSpeed JSON shows mobile LCP of 5.4s on homepage and 4.3s on collection, with TBT of 630ms and 740ms. Revenue potential is high if paid mobile traffic is meaningful, but fixability depends on development resources.

## Top Test Opportunities

**Gym Package Finder Above Product Grid** — The "Kuntosalipaketit" landing page starts with intro copy, carousel, filters, sorting, and a dense product grid, so paid visitors from gym-package ads must self-compare complete setups without a clear goal/space/budget path. Evidence: Meta ads visual summary, site visual summary, Google Ads visual summary, competitor research. Est. lift: 3-6% CR x unknown sessions/mo x unknown AOV = unknown EUR.

**Ad Claim Match Tiles on Parallel Bars Landing Page** — Ad 3 promises small-space training, chest/shoulder/core outcomes, durable frame, and beginner-to-advanced suitability, but Fold 1 shows standard product cards without turning those claims into visible comparison criteria. Evidence: Meta ads visual summary, site visual summary. Est. lift: 2-4% CR x unknown sessions/mo x unknown AOV = unknown EUR.

**Collection Trust Strip Near First Product Decision** — Landing pages show product ratings on cards but no page-level review count, return right, warranty, delivery, or Finnish-store proof near the first grid decision, despite those trust assets being visible on homepage/PDP/cart. Evidence: meta ads visual summary, site visual summary, live store text fetch. Est. lift: 2-4% CR x unknown sessions/mo x unknown AOV = unknown EUR.

**Product Card Decision Hierarchy Test** — Collection cards contain discount badges, sale prices, compare-at prices, savings labels, star ratings, urgency strips, and savings buttons, creating a sale-heavy card where the next action and product differences may be visually secondary. Evidence: meta ads visual summary, site visual summary. Est. lift: 2-5% CR x unknown sessions/mo x unknown AOV = unknown EUR.

**Homepage Hero Path Split by Shopper Goal** — The homepage hero is visually strong but pushes "Taljalaitteet jopa -50%" as the main red CTA-style block, while paid/search demand spans home gyms, benches, bars, weights, mats, and accessories. Evidence: site visual summary, Google Ads visual summary, live store text fetch. Est. lift: 1-3% CR x unknown sessions/mo x unknown AOV = unknown EUR.

**Cart Drawer AOV Add-On Module** — The cart drawer has checkout CTA and trust proof but no visible upsell, cross-sell, bundle reminder, or free-shipping threshold mechanic, leaving AOV expansion unused after add-to-cart intent is confirmed. Evidence: site visual summary. Est. lift: 3-8% AOV or 1-2% CR x unknown sessions/mo x unknown AOV = unknown EUR.

**PDP Bundle Explanation Test** — The PDP frequently-bought-together block shows three checked items and a total price of 75.85 EUR, but the visible summary does not describe why the selected add-ons complete the workout or whether they are optional. Evidence: site visual summary. Est. lift: 2-5% PDP add-to-cart x unknown PDP sessions/mo x unknown AOV = unknown EUR.

**Buy Box Proof Compression Test** — The PDP buy box includes rating, 55 reviews, brand, title, bullets, discount, sale price, compare-at price, savings label, CTA, payment box, stock/delivery, limited-time offer, and trust bullets, which may make the primary purchase decision feel dense on mobile. Evidence: site visual summary. Est. lift: 1-3% PDP CR x unknown PDP sessions/mo x unknown AOV = unknown EUR.

**Mobile LCP Optimization for Paid Entry Pages** — Mobile Lighthouse shows homepage LCP 5.4s and collection LCP 4.3s, so above-the-fold paid-entry pages likely render too slowly before shoppers can compare products or use search/filter. Evidence: PageSpeed JSON collected 2026-08-10, site visual summary. Est. lift: 2-5% mobile CR x unknown mobile sessions/mo x unknown AOV = unknown EUR.

**Collection Filter Shortcut Test** — The collection-style landing pages show filters and sorting, but no visible shortcut chips for common home-gym decisions such as small spaces, complete sets, beginners, heavy lifting, budget, or highest rated. Evidence: meta ads visual summary, Google Ads visual summary, competitor research. Est. lift: 2-4% collection CR x unknown sessions/mo x unknown AOV = unknown EUR.

## Unused but Valuable Findings

- Google Ads are broad enough that search landing-page routing may need category-specific audit coverage beyond the three Meta landing screenshots.
- The homepage trust strip is strong; it could be reused as a modular proof component on collection pages and cart without inventing new claims.
- Treenikauppa's public Trustpilot profile shows much stronger third-party review volume than the Gorilla Sports review source collected here, so external trust proof may be worth separate validation.

## Missing Data

- Exact landing page URLs for Ad 1, Ad 2, and Ad 3 were not provided; this limits live text analysis of each ad destination.
- No separate canonical collection screenshots were present; Ad 1/2 landing screenshots were used as collection-style evidence based on user context.
- `ad3-landing-f3.png` was not present; lower-page analysis for the Ad 3 landing page is incomplete.
- Reviews were skipped and `raw/reviews.md` was not present; customer love/frustration themes cannot be analyzed.
- Competitor insights were skipped and `raw/competitors.md` was not present; competitor analysis relies on self-research only.
- Email campaigns were skipped; lifecycle and email-to-site message match cannot be analyzed.
- Inspiration sites were skipped; no inspiration pattern evidence was available.
- Desktop PageSpeed reports, AOV, monthly sessions, conversion rate, device split, and revenue data were not collected; lift estimates cannot be converted into revenue forecasts.
