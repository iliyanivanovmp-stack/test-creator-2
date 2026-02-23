# March 2026 Testing Roadmap

**Data Sources:** Shopify Analytics, Post-Purchase Surveys, Site Search, Reviews & UGC, Previous A/B Tests, Winning Tests Library, Competitor Research

---

## Test #1: $1 Promo Landing Page Lead Capture

**Page:** $1 Promo Sign-Up Page (https://www.gardenstreet.com.au/pages/1-aussie-craft-gin-sign-up)

**Hypothesis:** If we add social proof, urgency, and a value preview above the sign-up form, email capture rate will increase because the page currently shows a bare form with no trust signals, no member count, and no preview of what the subscription delivers.

**Data:** 15,694 sessions in the last 30 days, second highest traffic page, zero optimization to date (Source: Shopify Analytics). The page has no social proof despite 6,000+ reviews at 4.9 stars (Source: Reviews). Competitors like Juniper Society and Gintonica use trust elements and community messaging on acquisition pages (Source: Competitor Research). Case studies show community framing with concrete offers increases email capture by 43% (Source: Winning Tests Library). No ads are currently running, so organic social (Facebook 23,400 + Instagram 15,700 sessions in the last 30 days) funnels to this page as the primary acquisition path (Source: Shopify Analytics).

**Variation 1:** Add a "Join 6,000+ gin lovers" social proof bar above the form with aggregate star rating (4.9 stars). Below the hero, add a "What past members received" mini-carousel showing 2-3 past box photos with contents listed. Add a countdown timer to the April 14 launch date. Keep the existing form and "Enter" CTA intact.

**Variation 2:** Replace the static hero with a split layout: left side keeps the $1 bottle visual, right side adds 3 short member testimonials (one about unboxing, one about gin quality, one about the welcome gift). Add "Limited to first 500 bottles" scarcity text below the headline. Simplify the form to email-only above the fold, with first name/phone/DOB expanding on click.

**Brief:** Design: V1 needs a social proof bar component (star rating + member count), 2-3 past box photos for the carousel, and a countdown timer. V2 needs a split hero layout, 3 testimonial cards, and a collapsible form. Dev: inject elements on the existing custom page. Both variations keep the existing form fields and CTA button. No conflicts with running tests.

---

## Test #2: Checkout Subscription Reassurance

**Page:** Checkout (https://www.gardenstreet.com.au/checkouts/)

**Hypothesis:** If we add subscription reassurance content near the recurring subtotal and Pay now button, checkout completion rate will increase because first-time subscribers face commitment anxiety about recurring charges, shipping costs, and flexibility, which the current checkout does not address.

**Data:** 1,790 sessions reached checkout in the last 30 days, 63.5% completed (652 abandoned checkouts at $99 each = ~A$64,500 in lost revenue per month) (Source: Shopify Analytics). Survey respondents reported: "opted for every two months but put as monthly," "free shipping plastered everywhere but $10 fee at checkout for TAS/NT," and "the price" as barriers (Source: Surveys). Multiple reviewers praise the flexibility to pause, skip, or change frequency (Source: Reviews). GS06 proved adding content near the Pay now button works (+9.64% RPV, deployed) (Source: Previous Tests). GS04 proved generic trust banners at the top of checkout lose, so placement and specificity matter (Source: Previous Tests).

**Variation 1:** Add a compact reassurance strip between the recurring subtotal line and the Pay now button: "No lock-in. Skip, pause, or cancel anytime." + "Free shipping on all subscription boxes" as two single lines with small icons. Everything else on the checkout stays unchanged, including the deployed GS06 reviews section below Pay now.

**Variation 2:** Add an enhanced order summary module: small thumbnail of the current month's box + "Includes FREE welcome gift ($82.50 value)" + "No contracts. Change frequency or cancel anytime." above the Pay now button. Sits between the recurring subtotal and Pay now. GS06 reviews remain below.

**Brief:** Design: V1 needs a 2-line reassurance strip with small icons (lock and truck). V2 needs a compact order preview card with box thumbnail and welcome gift callout. Dev: inject between the recurring subtotal and Pay now button on Shopify checkout. Both variations must preserve the deployed GS06 reviews section below Pay now. Sequencing: GS08 (Shipping Price) is approved for dev and targets shipping thresholds sitewide. This test targets checkout-specific reassurance copy, not shipping pricing. If GS08 changes shipping thresholds, confirm the "Free shipping" claim in V1 is accurate before launch.

---

## Test #3: Homepage Below-Hero Section (Mobile)

**Page:** Homepage (https://www.gardenstreet.com.au/)

**Hypothesis:** If we add a visual "How It Works" or member proof section between the hero banner and the buy box on mobile, add-to-cart rate will increase because mobile visitors (86.6% of traffic) currently scroll from the hero image into a text-heavy description with no visual break to reinforce the value proposition.

**Data:** 33,725 sessions to the homepage in the last 30 days, 86.6% on mobile (Source: Shopify Analytics). GS05 is testing the hero banner and trending winner with clearer messaging and CTAs (Source: Previous Tests). GS01 (press logo bar) won +41% RPV on desktop but lost on mobile, meaning mobile needs a different approach to trust-building than desktop (Source: Previous Tests). Case studies show clear, product-first messaging on homepage heroes generates +$19,441/mo (Source: Winning Tests Library). Reviews show "packaging," "unboxing," and "surprise" are the top emotional drivers (Source: Reviews). 92.18% returning customer rate means most traffic is existing subscribers, but the 7.82% new visitors are the conversion target (Source: Shopify Analytics).

**Variation 1:** Add a 3-step visual "How It Works" strip below the hero: "1. Choose your plan (monthly or bi-monthly) → 2. We curate your box ($230+ value for $99) → 3. Delivered to your door with a FREE welcome gift." Each step with a small icon. Compact, one screen height on mobile.

**Variation 2:** Add a "What Members Say" section below the hero: 3 short review quotes in a horizontal scroll carousel (one about unboxing, one about gin quality, one about gifting) + aggregate "4.9 stars from 6,000+ members" badge. Replaces the text description block on mobile only.

**Brief:** Design: V1 needs a 3-step icon strip (plan, curate, deliver) with concise copy. V2 needs a horizontal scroll testimonial carousel with 3 review cards and a star badge. Dev: inject below the hero section on mobile homepage. Desktop can remain unchanged or receive a parallel treatment. Sequencing: run after GS05 (Homepage Banner) concludes and its winner is deployed. GS05 started Jan 12 and should have results by early March.

---

## Test #4: Blog Article Subscription CTA Module

**Page:** Blog articles (https://www.gardenstreet.com.au/blogs/gin-blog/five-easy-summer-cocktails, https://www.gardenstreet.com.au/blogs/gin-blog/february-2026-backwoods-distilling-co-blood-orange-gin)

**Hypothesis:** If we add contextual subscription CTAs within blog articles, blog-to-subscription conversion will increase because blog readers are engaged content consumers with zero conversion path to the subscription from within the article.

**Data:** The summer cocktails blog article gets 1,582 sessions and the February Backwoods Blood Orange Gin article gets 601 sessions in the last 30 days (Source: Shopify Analytics). "Blood orange gin" is the #1 on-site search at 37 searches in the last 30 days, aligning with the featured blog content about the February box (Source: Site Search). Blog readers arrive engaged (they clicked a content link, not a product link) but see no subscription CTA within the article body (Source: Current Site). Reviews show word-of-mouth and discovery drive sign-ups: "Saw this add on fb, thought I would give it a try," "Signed up after tasting one of your gins at a friend's dinner party" (Source: Reviews). Case studies show customer-voice copy with specific claims generates +$50,945/mo (Source: Winning Tests Library).

**Variation 1:** Add a "This gin is in this month's box" banner module at the top of relevant blog articles + an inline "Join the Club" CTA card after the recipe/content section. The CTA card shows: box thumbnail, "$230+ value for $99/month," "Free welcome gift included," and an ATC button. Apply to all blog articles that feature a gin currently or previously in a monthly box.

**Variation 2:** Add a "Featured in our monthly box" sticky footer bar on all blog pages (visible on scroll, dismissible) + an "Inside the Box" preview module at the end of each article showing the current month's box contents with RRP values. The footer bar shows: "Try this gin for $99/month · Free $82.50 Welcome Gift · Join Now."

**Brief:** Design: V1 needs a contextual banner component ("This gin is in this month's box") and an inline CTA card with box thumbnail and value props. V2 needs a sticky footer bar and an end-of-article box preview module. Dev: inject on blog article templates. V1 requires conditional logic to match blog content to current/past box gins. V2 is simpler as it applies universally to all blog articles. No conflicts with running tests.
