# March 2026 Testing Roadmap

**Data Sources:** Shopify Analytics, Customer Surveys, Meta Ads, Customer Support Logs, Reviews & UGC, Core Web Vitals, Previous A/B Tests, Competitor Research

---

## The Problem

Social traffic converts at 2.05%. Search converts at 5.47%. That's a 2.6x gap.

Social drives 666K sessions monthly, 95% on mobile. All Meta ads point to the homepage. No dedicated landing pages. No message match.

Meanwhile, desktop tests keep winning (+41% RPV from Press Logo Bar). Mobile isn't improving.

**The opportunity:** Close the social/mobile gap.

---

## Current Performance (30 Days)

| Metric | Value |
|--------|-------|
| Sessions | 67,433 |
| Conversion Rate | 1.48% |
| Add-to-Cart Rate | 3.24% |

### By Traffic Source

| Source | CR | Notes |
|--------|-----|-------|
| Email | 6.89% | Benchmark |
| Search | 5.47% | Strong |
| Direct | 3.01% | Moderate |
| Social | 2.05% | Problem |

---

## Test #1: Homepage Banner (Welcome Gift Focus)

**Page:** Homepage

**Hypothesis:** If we lead the homepage banner with the $82.50 Welcome Gift, social traffic CR will increase from 2.05% to 3%+ because the welcome gift is the #1 conversion driver but it's buried below the fold.

**Data:** Survey + Reviews confirm welcome gift drives conversions. GS03 Deluxe Box: +17.93% RPV. Ads lead with gift value but homepage doesn't.

**Variation:** Swap the existing homepage banner: hero image of Welcome Gift unboxing, headline "FREE $82.50 Welcome Gift with Your First Box," subhead showing what's included (glasses, garnishes, snacks). Same CTA placement, rest of homepage unchanged.

**Brief:** A/B test within existing theme. Design needs welcome gift unboxing hero (mobile-first). Dev: banner swap + A/B test setup. Lower effort than a new page.

---

## Test #2: Mobile Social Landing Page

**Page:** Landing Page

**Hypothesis:** If we create a dedicated landing page for social traffic, CR will beat the Test 1 winner because a purpose-built page controls the full experience without homepage constraints.

**Data:** Social: 666K sessions at 2.05% CR vs Search at 5.47% (2.6x gap). 95% mobile. "I saw an ad" is #1 visit trigger (Survey). Ads promise "$223 value for $99" but homepage doesn't match.

**Variation:** Dedicated UTM-triggered landing page: hero: Welcome Pack visual, headline "Get $223 of Gin for $99," subhead "Includes FREE $82.50 Welcome Gift," single CTA "Claim Your Welcome Gift." No nav, ad creative style match.

**Brief:** Build with Shopify sections. Run after Test 1 concludes. Design: full landing page mockup (mobile-first). Dev: Shopify sections build + UTM targeting setup.

---

## Test #3: PDP Mobile Optimization

**Page:** PDP

**Hypothesis:** If we optimize the subscription PDP for mobile, mobile ATC rate will increase because GS02 won +21% RPV on desktop but mobile isn't benefiting from those wins.

**Data:** GS02: +21% RPV desktop. Desktop PDP converts 2.7-10.8%, mobile significantly lower. 95% of social traffic is mobile.

**Variation:** Mobile-first PDP: move key value props above fold (welcome gift, $223 value), add sticky ATC button on scroll, condense description into expandable sections, add review highlights near ATC, clearer subscription options layout.

**Brief:** PDP section modifications. Can run alongside homepage tests (different page). Design: mobile PDP layout + sticky ATC + review highlights. Dev: section mods, expandable content, sticky button.

