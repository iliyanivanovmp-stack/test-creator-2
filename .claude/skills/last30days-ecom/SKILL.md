---
name: last30days-ecom
description: Ecom-scoped social, review, and web research for a CRO brand — runs only the last30days sources that matter for ecommerce, and skips any source with no signal for that specific brand
---

You are running a scoped fork of the `last30days` research skill (github.com/mvanhorn/last30days-skill), limited to the sources that actually produce useful findings for ecommerce CRO work. This is not the full last30days tool — it drops the sources that only matter for tech/news/finance research and adds a precheck step so a source is never queried unless it has a plausible signal for this specific brand.

Run this before or independently of `/cro-collect`. Its output feeds `/cro-audit` as one more raw source. It does not replace Reviews & UGC collection in `/cro-collect` — it supplements first-party reviews with what people say about the brand elsewhere.

---

## Scope

**Kept (10):** Web search, Reddit, X, YouTube, TikTok, Instagram Reels, Pinterest, Trustpilot, Amazon, local corpus (files already collected in `brands/[brand-name]/raw/`).

**Dropped:** Hacker News, GitHub, Polymarket, StockTwits, arXiv, Techmeme, Digg, LinkedIn, Threads, Bluesky, TruthSocial, Xiaohongshu, Telegram, DripStack, Perplexity, jobs/hiring-signals. None of these produce ecom-brand-relevant signal — they returned empty or off-topic results on the Lanx test run and cost tokens to process anyway.

**Why the precheck matters:** on the Lanx run, Reddit came back with 5 items but none were actually about the brand — one was an auto-removed post, the rest were unrelated shoe threads that only matched on keyword. The one source that actually mattered was web search, which surfaced Trustpilot rating and review themes indirectly. Querying every kept source on every brand wastes the same way — a source with zero real presence for this brand still costs a full pass and still gets read at synthesis time. The precheck in Step 2 exists so only sources with a plausible signal get queried.

---

## Data Integrity

- Findings from this skill are third-party/community research, not first-party data. Label the output file that way — see Step 4.
- Never invent engagement numbers (upvotes, likes, follower counts). If the engine is unavailable and you are running Fallback Mode (Step 3B), report findings as prose with cited URLs only — no fabricated counts.
- If a precheck is ambiguous, run the source rather than guess it away. Skipping is only for a clear absence of presence.
- Record every skip with a one-line reason. A silent skip looks identical to "nothing found" later and destroys the audit trail.
- Do not analyze or form CRO test ideas here. Save findings only — `/cro-audit` does the synthesis.

---

## Step 1: Brand Input

Say in chat: "For social & community research, send me:
- Brand name
- Store URL
- Known handles, if any (X, Instagram, TikTok, Pinterest) — skip any you don't know
- Do they sell on Amazon? (yes / no / unsure)"

Wait for reply. Normalize brand name: lowercase, replace spaces with hyphens, remove special characters — same convention as `/cro-collect`. Use as `[brand-name]` throughout.

If `brands/[brand-name]/` doesn't exist yet, create it (this skill can run before `/cro-collect`).

---

## Step 2: Precheck Each Source

Web search and local corpus always run — never precheck those. For the other 8, run one cheap check per source before committing to a full research pass. Use WebSearch for every check below.

| Source | Precheck | Skip when |
|---|---|---|
| Reddit | `site:reddit.com "[brand name]"` | Zero results are actually about the brand or its product category — not just a coincidental word match |
| X | `site:x.com "[brand name]"`, or check a given handle | No account found, or the account has no recent posts |
| YouTube | `"[brand name]" review OR unboxing site:youtube.com` | Stay lenient — category-level reviews count even with no branded channel. Skip only on zero hits |
| TikTok | `"[brand name]" site:tiktok.com`, or check a given handle | No account, or account is dormant |
| Instagram | `"[brand name]" site:instagram.com`, or check a given handle | Same as TikTok |
| Pinterest | `"[brand name]" site:pinterest.com` | Nothing found |
| Trustpilot | `"[brand name]" trustpilot` | No profile exists at all. This was the highest-value source on the Lanx run — bias toward keeping it unless clearly absent |
| Amazon | `"[brand name]" site:amazon.com`, or use the Step 1 answer directly | Brand confirms no Amazon presence, or search shows none |

Record each source as PASS or SKIP with a one-line reason. Do this for all 8 before moving to Step 3.

---

## Step 3: Run Research

**3A — Engine available.** Check for an installed last30days engine first:

```bash
find "$HOME/.claude/plugins/cache/last30days-skill" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | sort -V | tail -1
find "$HOME/.claude/skills/last30days" -maxdepth 0 2>/dev/null
```

If either resolves to a path, the engine is installed. Build the source list from every PASS in Step 2 plus `web`. Run:

```bash
python3 "<engine_dir>/scripts/last30days.py" "[brand name] [store URL]" \
  --search <comma-separated passed sources>,web \
  --corpus "brands/[brand-name]/raw" \
  --emit=md \
  --save-dir "brands/[brand-name]/raw" \
  --save-suffix last30days-ecom
```

Run this directly in the shell tool, not inside a single-quoted `-lc` wrapper — an apostrophe in a search string (a brand name, a quoted review) breaks that quoting. Read the resulting `brands/[brand-name]/raw/lanx-...-raw-last30days-ecom.md`-style file (the engine names it from the topic slug) and copy its content into Step 4's output file.

**3B — Engine not installed (Fallback Mode).** Run one WebSearch pass per PASS source using the same `site:` filters as Step 2, but this time read the actual results — pull the specific threads, posts, or review pages, not just confirm existence. WebFetch a page only if a search result needs the actual text (e.g. a Trustpilot review page). For each PASS source, write 2-5 bullet findings with the source URL cited inline. Do not report native engagement metrics (upvotes, likes) in Fallback Mode — you cannot verify them from a WebSearch snippet, and Data Integrity above forbids inventing them.

Tell the user once, plainly, which mode ran: "Fallback Mode: last30days-skill isn't installed, so this ran on WebSearch/WebFetch only, source-checked but not engagement-scored. Full engine run available once mvanhorn/last30days-skill is installed."

---

## Step 4: Write Output

Write `brands/[brand-name]/raw/last30days-ecom.md`:

```markdown
# [Brand Name] — Social & Community Research (last30days-ecom)

> Third-party/community research. Directional only — treat findings as hypotheses until confirmed by first-party reviews or site evidence elsewhere in the audit.

**Mode:** [Engine / Fallback]
**Date:** [research date]

## Sources Run

- [Source]: [one-line reason it passed the precheck]

## Sources Skipped

- [Source]: [one-line reason]

## Findings by Source

### [Source Name]

[Bullets. Verbatim quotes where available, with URL cited inline. Engagement numbers only in Engine mode.]

[Repeat per source run.]

## Cross-Source Signal

[1-2 sentences only if the same theme shows up in 2+ sources. Skip this section if nothing corroborates across sources — do not force a synthesis that isn't there.]
```

---

## Step 5: Update Manifest

If `brands/[brand-name]/manifest.md` exists, add or update:

```markdown
## Social & Community Research (last30days-ecom)

- Mode: [Engine / Fallback]
- Sources run: [list]
- Sources skipped: [list with reasons]
- File: raw/last30days-ecom.md
```

If the manifest doesn't exist yet (this skill ran before `/cro-collect`), skip this step — `/cro-collect` will create the manifest and you can note the file was already collected when it asks about sources.

---

## Final Response

Say only:

```
Social & community research complete. Mode: [Engine / Fallback].

Sources run: [list]
Sources skipped: [list]

File: brands/[brand-name]/raw/last30days-ecom.md

Next step: Run /cro-collect (if not already done) or /cro-audit.
```
