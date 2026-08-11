# Sava Amsterdam CRO Research Audit

## Data Sources Used

- User-provided collection manifest: `brands/sava-amsterdam/manifest.md`
- Meta Ads and Landing Pages: `raw/meta-ads.md`
- Meta Ads visual summary: `raw/meta-ads-visual-summary.md`
- Google Ads Transparency notes: `raw/google-ads.md`
- Google Ads visual summary: `raw/google-ads-visual-summary.md`
- Current Site visual summary: `raw/site-visual-summary.md`
- PageSpeed / Core Web Vitals: `raw/pagespeed.md`, `raw/homepage-pagespeed-sava.json`, `raw/collections-pagespeed-sava.json`
- Reviews and UGC: `raw/reviews.md`, `raw/reviews-1.txt`, `raw/reviews-2.txt`, `raw/reviews-3.txt`
- Non-data context: `raw/context.md`
- Live page fetches on August 11, 2026: `https://sava-amsterdam.com`, `/en-us/products/cross-chain`, `/en-us/products/cross-bracelet`, `/en-us/collections/best-sellers`
- Self-researched competitor sources on August 11, 2026: CRAFTD London, JAXXON, Miansai via Ounass, and editorial competitor lists from Vogue, Glamour, and GQ search results

## Source Findings

### Meta Ads & Landing Pages

Meta ads are highly offer-led. All three visible creatives use the same core promise: "BUY 1 GET 1 FREE," free worldwide shipping, "Tag us #iamsava," and "Over 180.000 members." The visual system is consistent across ads: close-up men's jewelry lifestyle/video previews, with Ad 1 focused on a silver cross chain, Ad 2 on a wrist/bracelet shot, and Ad 3 on a cross necklace against a blue-sky lifestyle scene.

Message match is strongest on the transactional offer. Ad 1 lands on `https://sava-amsterdam.com/en-us/products/cross-chain`; the collected first fold shows "CROSS CHAIN | SILVER," 4.9 rating, 1321 reviews, a black sale countdown banner, "BUY 1 GET 1 FREE," same-day dispatch copy, and the primary "ADD TO CART" CTA. Live page metadata fetched August 11, 2026 confirms the Cross Chain is positioned as a waterproof, premium surgical-grade 316L stainless steel necklace with USD $59 product price.

Ad 2 lands on `https://sava-amsterdam.com/en-us/products/cross-bracelet`; the first fold shows "CROSS BRACELET | SILVER," 4.9 rating, 1033 reviews, "SUMMER SALE: BUY 1 GET 1 FREE," countdown, and "ADD TO CART." Live metadata fetched August 11, 2026 confirms waterproof 316L stainless steel positioning and USD $59 price.

Ad 3 lands on the best-sellers collection page, not a PDP. The collected first fold shows a full-width "SUMMER SALE" lifestyle hero, "BUY 1 GET 1 FREE," "+ FREE US SHIPPING," "+ LIFETIME GUARANTEE," press logos, and the start of the product grid. Live metadata fetched August 11, 2026 describes the collection as fashion jewelry for men, Amsterdam based, made to last, SAVA Only, with free worldwide shipping.

The main gap is that the social proof hook in the ads is not fully paid off above the landing-page fold. Ads mention "#iamsava" and "Over 180.000 members"; the PDPs show review counts and lower-page UGC, while the collection page shows press logos and product-card ratings, but the exact community proof is not visible in the collected landing page folds. A sticky CTA is not visible in the collected desktop screenshots for PDP or collection landings.

### Google Ads

Google Ads data is screenshot-based only. Visible placements include text/search-style cards, shopping/product cards, and a sitelink-style unit. Headlines include "Sava Amsterdam," "Sava Amsterdam - Made To Last A Lifetime," and product-specific titles such as "CROSS CHAIN | Silver | Mens..." and "SAVA ONE | Silver | Mens Jewelry..."

Google messaging leans more durable and trust-led than Meta. Visible copy mentions timeless silver and gold jewelry for men, free worldwide shipping, lifetime warranty, trusted by 180,000+ customers, and 60-day returns. This overlaps with the homepage and PDP trust bars, but differs from Meta's heavier "BUY 1 GET 1 FREE" framing. Shopping cards show isolated product images on pale backgrounds, but several visible cards show "[Price]" instead of numeric pricing, which weakens comparison shopping clarity if that reflects the live ad state.

### Reviews & UGC

Three user-provided review batches were collected on August 11, 2026 and preserved verbatim in `raw/reviews-1.txt`, `raw/reviews-2.txt`, and `raw/reviews-3.txt`.

#### What Customers Love

- Reviewers repeatedly describe wearing Sava jewelry every day in showers, gyms, beaches, swimming pools, water parks, and saunas without tarnishing, discoloration, scratching, or loss of shine.
- Reviewers praise the jewelry's understated design, polished finish, comfort, packaging, and the way it looks in person.
- Customer service is repeatedly described as fast, courteous, and helpful, including free replacements for broken or stolen items and positive lifetime-warranty support.

#### What Frustrates Customers

- Several reviews describe shipping or dispatch taking longer than promised. Examples include paid next-day shipping taking four days to ship, an order purchased July 22 still being unsent July 31 because an item was out of stock, and one delivery taking three weeks.
- Product complaints include jewelry feeling cheap or low quality, a bracelet clasp repeatedly coming undone and causing the bracelet to be lost, a lobster claw clasp being difficult to operate, a loose bracelet fit, a pendant feeling too feminine, and the Sava tag moving toward the front during activity.
- One reviewer reported a necklace breaking after a few days, while also praising the free replacement and customer service response.

#### Client-Actionable Insights

- Use the waterproof and daily-wear experiences as concrete proof for the existing durability promise.
- Audit the gap between same-day or next-day delivery language and fulfillment reality before amplifying urgency around dispatch.
- Review bracelet clasp security, self-fastening ease, and fit guidance alongside the isolated perceived-quality complaints.

### PageSpeed / Core Web Vitals

The provided mobile Lighthouse exports were fetched on August 11, 2026. The homepage scored 55 for performance, with 3.5 s FCP, 11.4 s LCP, 9.2 s Speed Index, 240 ms Total Blocking Time, 0 CLS, and 20.0 s Time to Interactive. The report estimated 262 KiB of unused JavaScript savings.

The Best Sellers collection scored 56 for mobile performance, with 3.6 s FCP, 8.2 s LCP, 6.5 s Speed Index, 300 ms Total Blocking Time, 0 CLS, and 18.8 s Time to Interactive. The report estimated 244 KiB of unused JavaScript savings. No desktop PageSpeed export or INP value was included in the provided files.

### Competitor Analysis

No user-provided `raw/competitors.md` file was present; competitor inputs were skipped in the manifest. The following direct-competitor comparison is self-researched on August 11, 2026.

| Brand | Positioning / Price Evidence | Key Features | Weaknesses / Openings for Sava |
|---|---|---|---|
| Sava Amsterdam | Collected PDP and live metadata show Cross Chain and Cross Bracelet at USD $59, with BOGO offer, free shipping, waterproof 316L stainless steel, lifetime warranty, 60-day returns, 4.9 ratings, and 180,000+ customer/community claim. | Strong promo economics, clear men's jewelry positioning, press logos, product ratings, Trustpilot strip, lifetime guarantee, waterproof/durable messaging. | Value story is fragmented across offer, warranty, UGC, press, and durability blocks; no visible above-fold sticky CTA; collection hero does not show a visible primary button in collected fold 1. |
| CRAFTD London | Search result for CRAFTD London on August 11, 2026 shows men's chains, pendants, bracelets, and rings, $69-89 CRAFTD pricing versus $20-40 fast fashion and $600+ fine jewelry, plus lifetime guarantee. | Direct value ladder explains why CRAFTD exists: cheap jewelry tarnishes, premium brands overcharge, every piece covered for life, water/heat/sweat-proof materials. | Sava has comparable price and warranty claims but does not show an equally compact value-ladder comparison in collected Sava folds. |
| JAXXON | JAXXON men's pendants page fetched August 11, 2026 shows filters for gold, silver, sale, cross, tag, engravable, iced, saint, and stone, with build-your-chain-and-pendant offers from $144-$149 and pendant education copy. | Strong category browsing, many pendant styles, visible filter taxonomy, "built to last" materials language, cross-specific products. | Sava collection screenshots did not show filters or sorting in the collected folds; Sava can compete by making material, fit, and offer comparison easier in-grid. |
| Miansai | Ounass Miansai men's necklaces page fetched August 11, 2026 shows 7 necklaces priced AED 675-900, with a brand story around understated, hand-refined raw materials and modern minimalism. | More premium/editorial brand frame, sterling silver and gold vermeil options, sustainability/material story. | Sava is materially more accessible at USD $59 before BOGO effects, but collected pages do not translate that price gap into a premium-versus-accessible comparison. |

### Emails

No `raw/emails.md` file or email screenshots were present, and Email Campaigns was skipped in the manifest. Subject lines, lifecycle CTAs, discount sequencing, and email-to-site message match cannot be audited from the collected dataset.

### Inspiration Sites

No `raw/inspiration.md` file or inspiration screenshots were present, and Inspiration Sites was skipped in the manifest. No inspiration UX patterns were used.

### Non-Data Context

The client context confirms Sava Amsterdam, `Sava-amsterdam.com`, 8 slots, 1 variation per test, and no specific areas of focus. The context also clarifies screenshot mapping: Ad 3's landing page is the collection page, and Ad 1's landing page is the PDP. This means the collection and PDP audits rely on ad-landing screenshots rather than separate native collection/PDP captures.

### Current Site Screenshots

Homepage: The collected homepage uses a full-width lifestyle hero with models wearing jewelry. The top black trust/benefit bar says "FREE US SHIPPING," "LIFETIME GUARANTEE," and "60-DAY RISK FREE RETURNS." Navigation shows Home, Shop, Best Sellers, Brand, and Contact. The hero includes star rating, "4.9/5 BY 180,000+ CUSTOMERS," headline "SUMMER SALE IS NOW LIVE," bullets for buy 1 get 1 free, lifetime guarantee, and free US shipping, plus a "Shop Now" CTA. Below the hero, the site moves into a benefit line, four-column product grids with watches and jewelry, sale labels, ratings, compare-at prices, and red sale prices. A Trustpilot strip appears only lower in fold 3.

Collection page: The best-sellers collection is represented by Ad 3's landing screenshots. Fold 1 includes a large sale/lifestyle hero, benefit bullets, press-logo strip, and the beginning of a four-column product grid. Folds 2 and 3 show dense product cards with imagery, badges, star ratings, review counts, product names, compare-at pricing, and red sale pricing. Filter controls and sorting UI are not visible in the collected folds. The collection hero has sale-focused text and product cards below, but no visible primary button label in fold 1.

PDP: The Cross Chain PDP is represented by Ad 1's landing screenshots. Fold 1 places a large product image gallery on the left and buy box on the right. The buy box includes rating, title, price, material swatches, BOGO offer, dispatch timer, "ADD TO CART," stock/shipping row, payment icons, sale explanation block, benefit icons, and collapsible details/care/returns sections. Price is shown as $59.00 with $69.00 struck through and a "SAVE $10.00" badge. Fold 2 contains "AS SEEN ON YOU," press logos, and "YOU MAY ALSO LIKE"; fold 3 contains related product cards, Trustpilot reviews, and a "WATERPROOF & DURABLE" content block. No sticky Add to Cart or frequently-bought-together module is visible.

Cart: The collected cart is a drawer. The header reads "YOUR CART" with a close icon. A yellow bar says "BUY 1 GET 1 FREE," followed by "CONGRATULATIONS! YOU GOT A FREE ITEM!" and a progress-style black bar. The cart contains two Cross Chain | Silver line items. The primary CTA is "CHECKOUT SECURELY" with a lock icon. A "YOU MAY LIKE" carousel includes product recommendations with plus icons. Total is $59.00 USD with $138.00 USD struck through, and shipping is free. Trustpilot appears below the checkout CTA, but guarantee or returns copy is not visible in the cart screenshot.

## Cross-Source Themes

1. Offer clarity has the strongest evidence and highest funnel impact. Meta ads, landing pages, homepage, collection, PDP, and cart all repeat BOGO/free-shipping/sale messaging, but each area expresses it differently: ads say "BUY 1 GET 1 FREE," homepage says "SUMMER SALE IS NOW LIVE," PDP uses a BOGO module and dispatch timer, collection uses sale hero bullets, and cart confirms the free item after add. This affects ad-to-cart continuity and revenue because every paid visitor is being sold through the offer.
2. Trust proof exists but is vertically scattered. Google Ads, homepage, PDP, collection, and cart all include trust points such as 180,000+ customers, 4.9 ratings, product review counts, press logos, Trustpilot, lifetime warranty, free shipping, and 60-day returns; however, high-value proof is often lower on the page or split across different components. This matters most on paid landing PDPs and the collection first fold.
3. Product-choice confidence is underdeveloped relative to the catalog. Product cards show ratings, badges, names, and sale prices, while PDPs show material swatches and benefit icons; however, collection filters/sorting are not visible, per-unit BOGO value is not visible, and no bundle/frequently-bought-together module appears in the PDP screenshots. This affects collection browsing, product selection, and AOV.
4. Fulfillment promises create a documented expectation gap. The PDP shows same-day dispatch, while collected reviews include paid next-day shipping taking four days to ship, an order purchased July 22 still being unsent July 31 because an item was out of stock, and one delivery taking three weeks. Positive reviews also report fast delivery, so the issue is inconsistency rather than universally slow shipping.

## Top Test Opportunities

**BOGO Value Builder in PDP Buy Box** - The PDP buy box shows price, material swatches, BOGO offer, dispatch timer, and add-to-cart as separate elements, so the user has to mentally connect the $59 price to receiving two items and the $138 struck-through cart value. Evidence: Meta ads, Ad 1 PDP screenshots, Ad 2 PDP screenshots, cart screenshot, live PDP metadata. Est. lift: 3% CR lift x unknown sessions/mo x unknown AOV = revenue sizing unavailable.

**Community Proof Match Above Fold** - Meta ads promise "#iamsava" and "Over 180.000 members," but the collected PDP and collection first folds do not show that exact community proof near the first CTA, creating an ad-to-page proof gap. Evidence: Meta ads visual summary, PDP screenshots, collection screenshots, homepage screenshot. Est. lift: 2% CR lift x unknown sessions/mo x unknown AOV = revenue sizing unavailable.

**Sticky Add-to-Cart for Paid Landing Pages** - Product-page landings show only the initial buy-box "ADD TO CART" and no sticky CTA in collected desktop screenshots, so returning to purchase after UGC, press, related products, or Trustpilot requires scrolling back. Evidence: Meta landing screenshots, PDP visual summary, site visual summary. Est. lift: 2.5% CR lift x unknown sessions/mo x unknown AOV = revenue sizing unavailable.

**Collection Hero CTA and Shop Path Clarifier** - The best-sellers landing page fold 1 has sale bullets and product cards beginning below the press strip, but no visible primary button label in the collected fold, weakening the next action for Ad 3 traffic. Evidence: Ad 3 landing screenshots, collection visual summary, Meta ads. Est. lift: 2% CR lift x unknown sessions/mo x unknown AOV = revenue sizing unavailable.

**Collection Card Offer Math** - Collection cards show compare-at prices and red sale prices, but the collected cards do not show per-unit BOGO value or "second item free" mechanics, so users may evaluate products as single-item discounts instead of bundle value. Evidence: collection visual summary, homepage product grid summary, cart screenshot. Est. lift: 2% CR lift x unknown sessions/mo x unknown AOV = revenue sizing unavailable.

**Trust Stack in Cart Drawer** - Cart contains BOGO confirmation, checkout CTA, free shipping, and Trustpilot, but guarantee and 60-day risk-free returns are not visible in the collected cart drawer screenshot, leaving the final pre-checkout step underusing sitewide risk reversal. Evidence: cart screenshot summary, homepage trust bar, Google Ads visual summary. Est. lift: 1.5% CR lift x unknown sessions/mo x unknown AOV = revenue sizing unavailable.

**PDP Durability Proof Near Material Swatches** - Live PDP metadata and lower-page sections emphasize waterproof 316L steel, but the first-fold buy box shows benefits as icons below the CTA area and details lower down, so material proof may be less salient when users choose silver/gold swatches. Evidence: live PDP metadata, PDP visual summary, Google Ads visual summary, competitor analysis. Est. lift: 1.5% CR lift x unknown sessions/mo x unknown AOV = revenue sizing unavailable.

**Related-Product Bundle Module Before Generic Grid** - PDP fold 2 moves into "AS SEEN ON YOU," press logos, and "YOU MAY ALSO LIKE" product cards, but no frequently-bought-together or curated bundle is visible, despite BOGO making a second-item decision central to conversion. Evidence: PDP visual summary, cart BOGO state, Meta offer. Est. lift: 2% CR lift x unknown sessions/mo x unknown AOV = revenue sizing unavailable.

**Search-Ad Landing Message Alignment** - Google Ads emphasize lifetime warranty, 60-day returns, trusted by 180,000+ customers, and "Made To Last A Lifetime," while PDP first folds lead heavily with sale mechanics; a variant could make durability/warranty proof more prominent for Google landing traffic. Evidence: Google Ads visual summary, PDP visual summary, homepage trust bar, live PDP metadata. Est. lift: 1.5% CR lift x unknown sessions/mo x unknown AOV = revenue sizing unavailable.

**Best-Sellers Filter/Sort Visibility** - The collection screenshots show dense four-column product grids but no visible filter or sort controls in the collected folds, forcing paid collection traffic to browse manually across necklaces, bracelets, watches, new, and bestseller items. Evidence: collection visual summary, JAXXON competitor page showing pendant filters, homepage product grid summary. Est. lift: 1.5% CR lift x unknown sessions/mo x unknown AOV = revenue sizing unavailable.

## Unused but Valuable Findings

- Google Shopping cards in the collected screenshot show "[Price]" in several visible cards; if this reflects live ad feed output, paid search merchandising may be losing comparison-shopping clarity before users arrive on-site.
- The homepage Trustpilot strip appears lower in fold 3, while the hero uses an owned 4.9/5 by 180,000+ claim; a future homepage trust test could compare press/review proof sequencing.

## Missing Data

- The provided PageSpeed exports cover mobile only, and neither export includes an INP value. Desktop performance and INP remain unavailable.
- Competitor Insights was skipped and no user-provided `raw/competitors.md` exists; competitor analysis relies on self-research dated August 11, 2026.
- Inspiration Sites was skipped and `raw/inspiration.md` is missing; no external UX pattern set was available.
- Email Campaigns was skipped and no email screenshots or `raw/emails.md` exist; lifecycle message match and retention/recovery opportunities cannot be audited.
