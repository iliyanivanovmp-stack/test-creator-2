# April 2026 Testing Roadmap

**Data Sources:** Shopify Analytics, GA4, Customer Segmentation Survey, Site Search, Reviews & UGC, Winning Tests Library, Current Site Screenshots

---

## Slot 1: PDP Gallery Layout Overhaul (All PDPs)

**Type:** A/B test (1 variation vs. control)
**Page:** All product detail pages sitewide. Primary measurement on the top 5 by revenue: One and Done Kit (/products/one-and-done-easy-well-pump-install), 2HP Eco-Steady Booster, 1HP Submersible 07RPS10, 1HP Eco-Steady Booster, 5HP Submersible 230RPS50.
**Revenue potential:** ~15,000 PDP sessions/mo x 0.3% ATC lift x $651 AOV = ~$29,295/mo

**Hypothesis:** If we restructure the product gallery layout from a multi-row thumbnail grid to a vertical thumbnail strip with main-image navigation arrows, add-to-cart rate will increase across all PDPs because the current layout creates an unusable wall of tiny thumbnails on complex products (20-30+ images) and offers no sequential browsing on desktop.

**Data:** The session-to-ATC drop-off is 98.34%, the biggest leak in the funnel (Source: Shopify Analytics, Feb 1 - Mar 3, 2026). The gallery is the first thing visitors interact with on every PDP, and the current layout scales poorly: the 1HP Eco-Steady Booster has 30+ images in a 4+ row thumbnail grid, the One and Done Kit has 20+ images in 3 rows (Source: Site Screenshots). On desktop, the only way to navigate images is clicking individual thumbnails. There are no next/previous arrows on the main image. The "Click to expand" overlay button adds visual clutter. On mobile, there's no image counter, so users on a 30-image product don't know there's more content to explore. The gallery optimization case study produced +$15,824/mo by improving how product images are presented, with "more human context = better performance" as the key finding (Source: Winning Tests Library). 65% of traffic is mobile (Source: Shopify Analytics).

**V1: Vertical thumbnail strip + navigation arrows**

Desktop: Replace the multi-row horizontal thumbnail grid below the main image with a single-column vertical thumbnail strip to the left of the main image. Up/down scroll arrows appear at the top and bottom of the strip when thumbnails exceed the visible area (5-6 visible). Add left/right navigation arrows on the main image for sequential browsing. Remove the "Click to expand" overlay button. Zoom still activates on click of the image itself (existing lightbox/expanded view, just no overlay button). The main image expands to fill the width freed by removing the thumbnail grid below it. Buy box stays in its current position to the right.

Mobile: Add left/right navigation arrows on the main image (in addition to existing swipe). Add an image counter badge ("1 / 20") in the bottom-right corner of the main image. Remove the "Tap to zoom" overlay button. Zoom still activates on tap. Thumbnail strip below remains unchanged (horizontal scroll with arrows).

**Brief:** Design: Desktop vertical thumbnail strip, 80px wide, positioned to the left of the main image. Thumbnails are square, ~70px, with 4px gap. Active thumbnail gets a 2px border in brand orange. Up/down arrow buttons at top and bottom of strip, visible only when thumbnails exceed viewable area. Main image left/right arrows: semi-transparent white circles with chevrons, vertically centered on the image, 40px diameter, visible on hover. Mobile arrows: same style, 32px, always visible. Image counter badge: dark semi-transparent pill ("1 / 20") in bottom-right, 12px white text. Dev: This is a Shopify product gallery component replacement. Build as a new section/snippet that replaces the existing gallery on all PDP templates. Vertical strip reads from the same product image array. Scroll behavior on the thumbnail strip: smooth scroll, advancing one thumbnail at a time per arrow click. Main image arrows cycle through the same image array sequentially. Zoom behavior: clicking/tapping the main image opens the existing expanded view. The "Click to expand" / "Tap to zoom" overlay button is removed but the functionality remains on image click/tap.

**Sequencing note:** March Test #3 (submersible pump gallery image content) changes what's inside the gallery (text overlay on the first image). This test changes the gallery container and navigation. If Test #3 is still running when April launches, they can coexist since they modify different layers (content vs. layout). If Test #3 has a winner, apply the winning image content to the control for this test.
