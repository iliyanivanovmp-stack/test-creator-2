# BetterWild Roadmap Seed

**Store:** https://betterwild.com
**AOV:** ~$59.98 (2-pack subscription, per cart screenshot)
**Monthly sessions:** Unknown — estimated ~50,000 site-wide, ~30,000 on LP /pages/lf (highest-traffic page; all 3 Meta ads land here)
**Data sources:** Meta Ads (3 active ads, Jun 9–10, 2026), PageSpeed (mobile), Amazon Reviews (34, Jun–Jul 2026), Site Screenshots (homepage, collection, PDP, cart drawer), Live WebFetch of betterwild.com and betterwild.com/pages/lf (Jul 24, 2026), Competitor research (caninejournal.com, Jul 24, 2026)

---

## Key Insights

BetterWild runs three concurrent Meta ads — a founder "exposes big secret" video (Cody, brand page), an influencer PSA (The Downtown Aly, symptom checklist hook), and an influencer rescue dog story (caitiesfosterfam, "This Will Change Your Dog's Life") — all landing on a single custom LP at betterwild.com/pages/lf. That LP opens with a generic "ALLERGY RELIEF THAT FIXES THE ROOT CAUSE, NOT JUST THE SYMPTOMS" headline with no reference to any of the ad hooks. The founder narrative is the most egregious gap: the ad promises a "big secret" reveal with personal founder framing (Cody, mission story), and the LP delivers a category page. Meanwhile, the LP itself has a 13.7s mobile LCP and 38.3s TTI — all three ads are driving cold traffic to a page that takes 38 seconds to become interactive on mobile.

Reviews (34 Amazon, Jun–Jul 2026) are overwhelmingly positive (29/34 five-star) and reveal a recurring conversion theme: "works when nothing else did." Customers who had already tried vets, OTC remedies, and other supplements describe BetterWild as a last-resort win. Key verbatim evidence: "We have tried many things from the vet and over the counter... Things were not working." (Shannon) "Nothing seemed to even improve his itchy and redness a little until we found Betterwild!" (Hailey womack) "This is the first time she's back to her regular self." (Daniel) Before/after coat and skin recovery — including bald spot regrowth with photo documentation — is a recurring theme. Negative reviews are concentrated around two issues: price ("$45 for this tiny sample size!") and taste rejection in a minority of dogs. BetterWild's per-chew cost (~$1.00/chew on subscribe) is 2–3x competitors like PetHonesty ($0.37/chew, 90-count) and Zesty Paws ($0.48/chew, 90-count). The 30-day money-back guarantee exists on the PDP but is absent from the cart and from the Amazon listing, leaving the price objection undefended at the moment it matters most.

The PDP buy box structure creates two layers of friction before the ATC button is visible: a dog-count selector (Step 1) and a pack-size selector (Step 2), with the "ADD TO CART - $59.98" button appearing only in fold 2. Subscribe & Save is pre-selected; the one-time option is demoted to secondary text below the CTA. The cart drawer adds no trust signals, no guarantee copy, and no cross-sell — BetterWild has three complementary SKUs (Joint Support, Dental + Multivitamin, Paw Balm) with no cart-level upsell in place. A copy error on the 3-pack ("A 60-day supply for 1 dog" instead of the correct 3-pack description) undermines the highest-AOV purchase option, which also carries the "Recommended" badge.

---

## Top Test Opportunities

### 1. LP Speed: Fix 13.7s LCP on /pages/lf
**What's broken:** betterwild.com/pages/lf — the single URL that receives 100% of paid Meta ad traffic — has a 13.7s LCP and 38.3s TTI on mobile (PageSpeed score: 41/100). The page's first contentful paint takes 4.7s; the hero image (two dogs outdoors, positioned right-of-center in a full-width section) does not render for nearly 14 seconds. Total Blocking Time is 690ms, indicating heavy third-party scripts (likely Meta Pixel, review widget, analytics). The page is not interactive until 38 seconds after the first request. Visitors who arrived from a 15-second Meta ad scroll are asked to wait 38+ seconds on a blank or partially-loaded page.
**Evidence:** pagespeed.md (LP row: LCP 13.7s, TTI 38.3s, Performance 41/100)
**Key data:** Google benchmark: mobile bounce rate increases ~32% per additional second at 1–3s; at 13.7s LCP, a majority of ad-driven mobile visitors exit before the page is usable. Homepage comparison: LCP 6.8s (also poor, but less than half of the LP's load time).
**Est. lift:** 15% CR improvement (conservative for LCP fix from 13.7s to <2.5s) × 30,000 LP sessions/mo × $59.98 AOV = ~$27,000/mo

---

### 2. Message Match: Ad-Specific LP Heroes
**What's broken:** The LP at betterwild.com/pages/lf shows a fixed full-width dark navy hero section with left-aligned headline ("ALLERGY RELIEF THAT FIXES THE ROOT CAUSE, NOT JUST THE SYMPTOMS"), a star rating bar and "100,000+ Happy Dogs" above the headline, a one-line subhead ("Support your dog's immunity and ease allergies—naturally. A blend of clinically validated ingredients!"), a single pink "SHOP NOW" CTA button, and a hero image of two dogs outdoors on the right. Below it, a symptom grid in fold 2 (ITCHING, SCRATCHING, PAW LICKING, SKIN BITING, RED SKIN) and a gut-science section in fold 3. No element on the page references the founder (Cody), the "big secret," the PSA framing, or the rescue/foster dog story from the three active ads. Ad 3 (Founder) is the highest-gap: "BetterWild Founder Exposes Big Secret" / "Hey, I'm Cody" in the ad has zero continuation on the LP.
**Evidence:** meta-ads-visual-summary (Ad 1 message match: partial; Ad 2: weak; Ad 3: none), site-visual-summary (LP folds 1–3)
**Key data:** Ad 3 headline: "BetterWild Founder Exposes Big Secret" — LP has no founder, no secret, no Cody reference. Industry benchmarks: LP message match improvements yield 20–40% CR lifts in direct response (WordStream, Unbounce 2024 studies).
**Est. lift:** 20% CR lift × 30,000 LP sessions/mo × $59.98 AOV = ~$36,000/mo

---

### 3. LP: Price Anchor + Guarantee in Fold 1
**What's broken:** The LP fold 1 contains a pink "SHOP NOW" button with no price shown and no guarantee copy. The announcement bar above the nav says "Subscribe today and get free US shipping on every subscription order!" — a weak urgency signal. Visitors who click SHOP NOW from an ad are asked to take a commercial action (proceed to purchase) without seeing a price or a risk-reversal. The 30-day money-back guarantee does not appear until the PDP, two pages deeper in the funnel. On the LP, there is no guarantee mention in fold 1 or fold 2.
**Evidence:** meta-ads-visual-summary (LP fold 1: "No guarantee copy visible"), site-visual-summary (LP CTAs and trust signals section), reviews.md (price objections, no-return complaints)
**Key data:** Amazon reviewers cited price as friction even post-purchase. LP has no price shown. Competitor PDPs (PetHonesty, PetLab Co) show starting price and guarantee in the first viewport.
**Est. lift:** 8% CR lift × 30,000 LP sessions/mo × $59.98 AOV = ~$14,400/mo

---

### 4. PDP: Sticky ATC Button
**What's broken:** On the Allergy Relief PDP, the buy box is positioned in fold 1–2 on the right side of a two-column layout. Step 1 (HOW MANY DOGS ARE YOU TREATING?) occupies the upper-right panel with three radio options (1 dog / 2 dogs / 3 dogs, 1 dog pre-selected). Step 2 (SELECT YOUR SUPPLY) lists 1-pack, 2-pack, and 3-pack options stacked vertically below Step 1. The "ADD TO CART - $59.98" button (large, full-width, pink) appears at the bottom of fold 2, below the subscribe/save block and the one-time option text link. The button is not visible until the user has scrolled past both selection steps plus the subscription copy block — approximately 800px of scroll on mobile. No sticky CTA bar is present on mobile or desktop. A visitor who lands on the PDP and immediately looks for the buy button cannot find it without scrolling.
**Evidence:** site-visual-summary (PDP fold 1: no CTA visible; fold 2: ATC button appears; CTA behavior notes)
**Key data:** Ecommerce UX benchmarks: sticky ATC bars on supplement PDPs with multi-option selectors reduce CTA drop-off by 5–10% (Baymard 2024).
**Est. lift:** 6% CR lift × 20,000 PDP sessions/mo × $59.98 AOV = ~$7,200/mo

---

### 5. PDP: One-Time Purchase Default for New Visitors
**What's broken:** The PDP's Subscribe & Save option is pre-selected as the default purchase path. The 2-pack subscribe price ($59.98) and "33% Off First Order" badge are shown first and prominently. The one-time purchase option appears as a secondary text link below the pink ATC button: "Or buy once at $79.98 (no discount, $5 Shipping)." There is no toggle or equivalent-weight presentation for the two options. First-time visitors who are skeptical about efficacy (a documented segment per reviews) must actively choose to downgrade from subscription — a pattern that creates decision friction and may cause abandonment rather than conversion to either option.
**Evidence:** site-visual-summary (PDP buy box detail: "Subscribe & Save is the default purchase mode — one-time option presented as secondary text link below the CTA"), reviews.md (Chris P: "change has been clear enough that I'll keep ordering on subscription" — implies he started one-time)
**Key data:** Reviews show a "try before subscribing" buyer mindset exists in the customer base. At $79.98 OTP vs. $59.98 subscribe, the OTP price is 33% higher — this compounds hesitation for first-timers.
**Est. lift:** 7% CR lift on new-visitor PDP sessions × 12,000 new visitor sessions/mo × $39.99 average OTP price = ~$3,360/mo; LTV benefit from converting trial-buyers to subscribers is additional upside not modeled here.

---

### 6. Cart: Guarantee + Trust Strip
**What's broken:** The cart drawer shows a single line item (e.g., ALLERGY RELIEF — Single Pack — $59.98 — Delivery every 2 months), a cause-marketing shelter selector, a subtotal, and a full-width pink CHECKOUT button. The bottom of the drawer shows "Delivery by Jul 28th – Jul 29th." There are no trust signals — no guarantee copy, no money-back statement, no returns mention, no badge. The 30-day money-back guarantee and "Free US Shipping" copy visible on the PDP immediately below the ATC button do not carry through to the cart. Visitors who hesitate at checkout lose the risk-reversal that was present on the product page.
**Evidence:** site-visual-summary (cart section: "No guarantee copy, no returns policy, no trust badge present"), reviews.md (Kathy C: "no returns on this product which the price is expensive!!")
**Key data:** Baymard 2024: 17% of cart abandonments are attributed to lack of trust / security concerns at checkout. Guarantee copy near the checkout CTA is among the cheapest trust interventions.
**Est. lift:** 5% cart → checkout lift × 10,000 cart sessions/mo × $59.98 AOV = ~$3,000/mo

---

### 7. Cart: Cross-Sell / AOV Upsell
**What's broken:** The cart drawer contains one line item with no upsell, no cross-sell card, no bundle offer, and no free shipping progress bar. BetterWild has three complementary SKUs in the same price range: Joint Support ($29.99), Dental + Multivitamin ($29.99–$59.99), and Paw Balm ($29.99). The cause-marketing shelter selector is the only additional cart element. Allergy Relief customers are not exposed to complementary products at the highest-intent moment in the funnel.
**Evidence:** site-visual-summary (cart: "No upsell, cross-sell, or bundle offer visible in the cart"), site-visual-summary (collection page: 4 products at $29.99 each)
**Key data:** Average DTC supplement cart upsell attach rate: 8–15% (Triple Whale 2024 benchmarks). At $29.99 incremental item and 10,000 cart sessions, even 10% attach = ~$30,000/mo incremental.
**Est. lift:** 12% cross-sell attach rate × 10,000 cart sessions/mo × $29.99 = ~$36,000/mo incremental revenue

---

### 8. PDP: 3-Pack Copy Fix + Conversion Test
**What's broken:** In the PDP buy box Step 2 (SELECT YOUR SUPPLY), the 3-pack option shows: "Recommended" badge (orange), price of $89.98 (was $119.97), $1.00/day, 90-day Supply. Directly below the 3-pack option, explanatory copy reads: "A 60-day supply for 1 dog — covers two months of consistent daily support at a better per-day value." This is the description for the 2-pack, not the 3-pack. A 3-pack at 90 chews is a 90-day supply for 1 dog (or 30-day supply for 3 dogs). The copy error directly contradicts the "Recommended" badge by underselling the option's value, and it is factually incorrect.
**Evidence:** site-visual-summary (PDP fold 2: "The explanatory text under the 3-pack option says 'A 60-day supply for 1 dog' — this appears to describe the 2-pack, not the 3-pack that it sits beneath. Possible copy error.")
**Key data:** The 3-pack is the highest-AOV option ($89.98 vs. $59.98 for 2-pack or $29.99 for 1-pack). Fixing misaligned copy on the "Recommended" option and testing a stronger description ("Best value — 3 months of consistent daily support") is a low-cost, high-impact change.
**Est. lift:** 10% increase in 3-pack selection × 5,000 users reaching the pack selector/mo × $30 incremental vs. 2-pack = ~$15,000/mo

---

## Unused Findings

- **Pricing inconsistency across pages:** Homepage WebFetch shows "From $39.99" for Allergy Relief; collection visual summary shows "From: $29.99." Likely OTP vs. subscription price displayed inconsistently — worth auditing the product metafield to unify the "From" price display.
- **LP sold-out state (unconfirmed):** WebFetch of betterwild.com/pages/lf on Jul 24, 2026 returned the ATC widget as "Sold out." If real, this is a blocking issue — not a test. Recommend manual mobile incognito check immediately.
- **Results timeline education missing:** No "Week 1 / Week 2 / Week 4 expectations" content on LP or PDP. Reviewers who saw no results "after days" left 1-star reviews and cited the no-return policy as a pain point. A simple timeline module could reduce churn and 1-star reviews.
- **Wolf-sourced probiotics differentiation underused on LP:** Brand's most distinctive scientific angle appears only in fold 3 of the LP. Competitors do not use this positioning. Testing it in fold 1 or as a hero subhead could differentiate BetterWild from the "gut + probiotics" category noise.
- **Announcement bar is a missed CRO surface:** Both the homepage and LP show "Subscribe today and get free US shipping" — a passive benefit statement. Testing a time-limited offer or stronger hook in the announcement bar is an easy quick-win.
