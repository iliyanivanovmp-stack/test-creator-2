# SVibe CRO Research Brief

**Data Sources:** Meta Ads and Landing Pages, Google Ads Transparency, Reviews and UGC, PageSpeed / Core Web Vitals, Current Site Screenshots, Social and Community Research, Competitor Analysis (self-researched)

Paid acquisition has a message-match problem that gets worse the further a shopper travels from Ad 1. Ad 1 (Snail Curve) matches its landing page cleanly, but Ad 2 (Snail Jovi Arc) drops the ad's "hands-free internal pleasure" framing for a "Longer Erections"/couples-ring angle, and Ad 3 (Snail Jovi) links to an entirely different emotional landing page template ("Reconnect. Without the awkward conversation") that carries none of the ad's product claims and shows a different price ($69) than the related Jovi Arc PDP context ($89). Source: Meta Ads visual summary. Google Ads repeats a "2 years warranty, 30 days return policy" line and "$10 off sign up" / "Save up to $30" offers on nearly every unit, and neither is honored on any of the three Meta-linked landing pages reviewed. Source: Google Ads visual summary.

Mobile performance is a hard blocker sitting under all of this. The homepage (10.2s LCP) and the Snail Curve PDP (13.5s LCP) both score 61/100 on mobile PageSpeed, 4-5x over Google's 2.5s "good" threshold. Source: PageSpeed JSON, fetched 2026-09-23. The PDP is the direct landing page for Ad 1 and the pricing-context page referenced by Ad 2, meaning paid traffic is landing on the two slowest pages on the site.

Reviews surface a specific claims-accuracy conflict: the live PDP's "Whisper quiet" trust badge is directly contradicted by a verified reviewer, "Not whisper quiet, but not distracting" (Shanna Church, 8/23/2026). Cleaning difficulty and lubricant necessity are recurring unprompted complaints that never appear pre-purchase. Source: Reviews. Off-site sentiment (Trustpilot: 3.8/113 reviews as of 2026-09-22) runs cooler than the on-site 4.8/2,847, directional and not corroborated by first-party evidence, but worth watching. Source: Social and Community Research.

Monthly sessions and store-wide AOV were not collected, so none of the estimates below convert to a dollar figure. Priority instead follows evidence strength and position in the funnel: the Ad 3 message-match failure and the mobile LCP issues sit directly on top of live paid spend, so they lead the roadmap regardless of an unquantified lift.

## Slot 1: Fix Ad 3 (Snail Jovi) Landing Page Message Match

**Type:** A/B test (1 variation vs. control)
**Page:** Landing Page (Ad 3, svibe.com)
**Revenue potential:** Not quantifiable, Ad 3 session and conversion data was not collected. Directional priority: this is the largest message-match gap of the three active Meta creatives reviewed.

**Hypothesis:** If the Ad 3 landing page carries the product name, feature claims, and current price consistent with the ad creative, add-to-cart rate from Ad 3 traffic will increase because shoppers currently land on a page with no matching product claims to the ad they clicked.

**Data:** Ad 3's video promises "two motors, a remote" and names the product "Snail Jovi," but the linked landing page uses an unrelated "Reconnect. Without the awkward conversation" template built around relationship pain points, with no motor/remote feature claims anywhere in the three captured folds. The only product reference is a sticky bottom bar showing "Snail Jovi $69 $89." Source: Meta Ads visual summary (Ad 3).

**V1:** Add a product-led block directly under the existing "Reconnect" hero: product name "Snail Jovi," a short feature line repeating the ad's "two motors, remote control" claim, and the current price ($69, list $129 per live pricing). Keep the "Sound familiar?" pain-point section below this new block, and keep the sticky bottom bar unchanged. Mobile: product image stacks above the feature line and CTA. Desktop: image left, feature line and CTA right. (KB: resources/kb/pdp-structure.md, ad-to-page congruency principle)

## Slot 2: Compress PDP Mobile LCP Below 4 Seconds

**Type:** Immediate Fix
**Page:** Product Detail Page, Snail Curve, svibe.com/products/female-vibrator-curve-svibe

**Issue:** The Snail Curve PDP, the direct landing page for Ad 1 and the pricing-context page for Ad 2, takes 13.5 seconds to reach Largest Contentful Paint on mobile against Google's 2.5s "good" threshold, with a performance score of 61/100. The page's hero product image and 6-thumbnail strip are the likely LCP element given the page's heavy visual weight.

**Evidence:** raw/pagespeed.md (svibe-pdp-pagespeed.json, fetched 2026-09-23), Site Screenshots (confirms this PDP as the Ad 1 landing page).

**Fix:** Audit and compress the hero image and thumbnail strip (format, dimensions, lazy-load below-fold assets) to bring mobile LCP under 2.5s. Paid traffic is currently landing on the slowest page on the site.

## Slot 3: Compress Homepage Mobile LCP Below 4 Seconds

**Type:** Immediate Fix
**Page:** Homepage, svibe.com

**Issue:** The homepage hero, a full-width purple background image with a layered text block ("Different Feels Better" headline, star row, "SHOP NOW" button), loads its largest content in 10.2 seconds on mobile, over 4x Google's 2.5s threshold, with a performance score of 61/100.

**Evidence:** raw/pagespeed.md (svibe-homepage-pagespeed.json, fetched 2026-09-23), Site Screenshots (homepage fold 1).

**Fix:** Compress and prioritize the hero background image in the critical rendering path to bring mobile LCP under 2.5s.

## Slot 4: Surface Warranty and Returns Claim in the PDP Buy Box and Cart Drawer

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (Snail Curve) and Cart (drawer), svibe.com
**Revenue potential:** Not quantifiable, sessions/mo not collected. Directional priority: this claim is repeated across nearly every Google ad but is invisible at the two moments closest to purchase.

**Hypothesis:** If "2 Year Warranty" and "30 Day Returns" are added to the visible Curve PDP buy box and the cart drawer, add-to-cart and cart-to-checkout rates will increase because shoppers currently only see this claim in Google ad copy and a collapsed accordion, not at the moments they decide to buy.

**Data:** "2 Year Warranty" and "30 days return policy" repeat in nearly every Google text ad and appear as a headline buy-box badge on the Snail Jovi Arc PDP, but on the Snail Curve PDP the same information sits only inside a collapsed "Warranty" accordion below the fold. The cart drawer shows a free-shipping banner, a gift countdown timer, and two AOV checkboxes, but no warranty or returns copy at all. Source: Google Ads visual summary, Site Screenshots (PDP buy box + cart drawer).

**V1:** Add "2 Year Warranty · 30 Day Returns" as a fifth badge in the existing Curve PDP trust-badge row (alongside "Never loses contact / 600+ combinations / Whisper quiet / 100% Body Safe," without altering their wording), and add the same line above the "SECURE CHECKOUT" button in the cart drawer. Mobile: badge wraps to a second line under price on the PDP; single line above the CTA in the drawer. Desktop: same placement, inline with existing badge icons. No other buy-box or cart elements change.

## Slot 5: Reconcile the "Whisper Quiet" PDP Badge Against Reviewer Feedback

**Type:** Immediate Fix
**Page:** Product Detail Page, Snail Curve, svibe.com

**Issue:** The Snail Curve PDP's trust-badge row states "Whisper quiet," directly under the star rating. A verified on-site reviewer states: "Not whisper quiet, but not distracting" (Shanna Church, 8/23/2026), a direct contradiction of the specific claim in that badge.

**Evidence:** Reviews (raw/reviews.md), Site Screenshots (PDP fold 1, trust badge row).

**Fix:** Verify the noise claim against current production units before continuing to lead with it. If the "whisper quiet" standard can't be confirmed, replace the badge copy with an accurate, still-favorable claim rather than removing the badge outright.

## Slot 6: Surface Cleaning and Lubricant Requirements Pre-Purchase

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page, Snail Curve, svibe.com
**Revenue potential:** Not quantifiable, sessions/mo and return-rate data not collected. Directional priority: reduces post-purchase complaint and return risk on the flagship SKU.

**Hypothesis:** If cleaning method and lubricant requirement are added to the PDP, post-purchase complaint and return rate will decrease because both currently appear only as unprompted complaints in reviews, not anywhere in the three captured PDP folds.

**Data:** "the design makes it a bit difficult to clean thoroughly" (Alora Aldrige, 8/25/2026) and "Must use lubricant with this material." (Kearstin, 9/16/2026) are both unprompted, verified reviewer complaints. Neither cleaning method nor lubricant guidance appears in the product description or the three captured folds (How To Use / Specifications / Warranty accordions were collapsed and not visible). Source: Reviews, Site Screenshots (PDP folds 1-3).

**V1:** Add a "Care & Use" line to the existing "The details" 5-feature callout section: "Water-based lubricant recommended. Rinse with mild soap and warm water after each use." Mobile: appended as a 6th card in the existing feature grid. Desktop: same, inline in the feature row. No other PDP sections change.

## Slot 7: Add a Sticky Mobile Add-to-Cart Bar on the PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page, Snail Curve, svibe.com
**Revenue potential:** Not quantifiable, sessions/mo not collected.

**Hypothesis:** If a sticky Add to Cart bar persists as the shopper scrolls past fold 1, add-to-cart rate will increase because the only persistent element currently observed on the page is an unrelated "Mystery Discount + FREE Guide" popup tab, not a purchase CTA.

**Data:** The "ADD TO CART, $149.00" button sits directly under the color swatches in fold 1 only, with no sticky equivalent through fold 2 (UGC video carousel, "Real homes, real views" grid) or fold 3 ("The details," "Curve or Gizi?" comparison). Source: Site Screenshots (PDP folds 1-3, CTA behavior notes).

**V1:** Add a sticky bottom bar showing product thumbnail, name, price ($149.00), and an Add to Cart button, appearing once the shopper scrolls past the fold-1 buy box. Mobile: full-width bar fixed to the bottom. Desktop: same trigger condition, full-width bar anchored at the bottom. The existing "Mystery Discount" popup tab stays unchanged. (KB: resources/kb/pdp-structure.md, sticky bottom bar pattern)

## Slot 8: Disambiguate "Snail Jovi" vs. "Snail Jovi Arc" Naming Site-Wide

**Type:** Immediate Fix
**Page:** Product Detail Pages (Snail Jovi, Snail Jovi Arc) and Meta ad creative, svibe.com

**Issue:** Two distinct products, "Snail Jovi" ($69, list $129, 46% off) and "Snail Jovi Arc" ($89, list $99, 10% off), share a near-identical name differing by one word. This has already produced a visible downstream error: Ad 3 names its product "Snail Jovi" and describes features ("two motors, a remote") that, per Ad 2's landing page, belong to "Snail Jovi Arc" instead.

**Evidence:** Meta Ads visual summary (Ads 2 and 3), Homepage live verification (2026-09-23 pricing).

**Fix:** Rename one product to remove the one-word overlap, and audit all live ad creative and landing pages to confirm each references the correct product name, feature set, and price before the next spend cycle.

## Future Slot Candidates

1. **Add a subscription or bundle option to the PDP buy box** - The Snail Curve PDP offers only a single one-time-purchase path despite the brand selling multiple SKUs (Curve, Gizi, Jovi, Jovi Arc) that lend themselves to a bundle upsell, and despite the homepage/collection pages already leaning on steep percentage-off discounts rather than AOV mechanics. Source: Site Screenshots (PDP buy box, homepage/collection pricing pattern).
2. **Add third-party award badges to individual product cards on the collection grid** - Awards (2024 Awards Winner, HBIZ Europa, Sexual Freedom Awards finalist) exist only inside a separate quiz-block panel, invisible to a shopper scanning the product grid itself. Source: Site Screenshots (collection page fold 2-3).
3. **Source third-party YouTube reviewer clips into the PDP UGC carousel** - Independent YouTube reviewer coverage exists specifically for the Snail Curve, a possible supplement to the PDP's currently brand-only UGC carousel. Source: Social and Community Research (raw/last30days-ecom.md).
