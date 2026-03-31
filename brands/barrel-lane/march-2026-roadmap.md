# March 2026 Testing Roadmap

**Data Sources:** Competitor Research, Customer Voice Research, Site Audit, Meta Ads

---

## Test #1: PDP Social Proof & Tasting Notes

**Page:** PDP

**Hypothesis:** If we add customer reviews and detailed tasting notes to product pages, ATC rate will increase because premium spirit buyers need trust signals and flavour guidance to justify $120+ purchases, and every major AU competitor already provides this.

**Data:** All 5 competitors display reviews + tasting profiles on PDP (Source: Competitor Research). "Is it worth $120?" is the #1 objection; tasting guidance and social proof are the top purchase drivers in craft spirits (Source: Customer Voice Research).

**V1:** Add to each PDP: star rating + review count below product title, 3-5 customer reviews above the fold, visual tasting notes section (flavour profile, nose/palate/finish, food pairings), and an "Australian Made, Small Batch" trust badge near ATC. Mobile: reviews stack vertically below the product image, tasting notes section collapses into an expandable accordion, trust badge sits directly above the ATC button full-width. Desktop: reviews display in a two-column grid beside the product image, tasting notes section (flavour wheel or simple list) sits below the product description, trust badge inline next to ATC.
**Brief:** Design: review display component (mobile: single-column stack, desktop: two-column grid), tasting notes visual (flavour wheel or simple list, collapsible on mobile), trust badge. Dev: integrate Shopify review app (e.g. Judge.me), add tasting notes metafield to product template, badge placement near ATC. Can use existing review app or embed manually. No conflicts with other tests.

---

## Test #2: Homepage Hero Message Match

**Page:** Homepage ([https://barrel-lane.com.au/](https://barrel-lane.com.au/))

**Hypothesis:** If we move the value proposition from the announcement bar into the homepage hero, conversion rate will increase because the ads lead with specific value hooks but the hero is a generic brand statement, forcing the announcement bar to do the selling in the weakest position on the page.

**Data:** All 5 active ads lead to the homepage (Source: Meta Ads). Ads lead with concrete hooks: "Box valued at $269," "$110 Welcome Pack With Your First Box," "Exclusive Whisky. Delivered to You," and "Free Delivery, Cancel Anytime" (Source: Meta Ads). The homepage hero shows "Exceptional Australian Whisky, Crafted for Discovery, Delivered with Care," a generic tagline with no price anchoring and no value proposition (Source: Site Audit). The welcome pack offer exists on the page but is confined to the announcement bar ("Join now and receive two Glencairn glasses and a 200ml whisky on us"), which undersells the $110 value with no dollar figure and sits in a format most users scroll past (Source: Site Audit). The first CTA ("Join the Experience") requires scrolling past the hero on both mobile and desktop (Source: Site Audit).

**V1:** Replace the homepage hero headline with a value-led message that matches the ad hooks. Headline: "Australia's Best Small-Batch Whisky. Delivered to Your Door." Subhead: "Box valued at $269. Free starter pack with your first delivery: two Glencairn glasses + a bonus 200ml whisky ($110 value). Free delivery. Cancel anytime." CTA: "Join Now." The announcement bar stays unchanged. Mobile: hero image above, headline + subhead + CTA stacked below. Desktop: text overlay on the left, hero image on the right. Remaining homepage sections stay unchanged.
**Brief:** Design: new hero layout with headline, value subhead, and CTA (mobile: stacked, desktop: two-column split with text left, image right). Dev: replace the existing hero section. Static content, no dynamic elements. No conflicts with other tests. Sequencing: if Test #1 adds reviews to the PDP, this test can run simultaneously since they target different pages.

