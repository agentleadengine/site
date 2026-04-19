# samuelochoa.com — Personal Brand Site

Single-page personal site positioning you as an **AI researcher & entrepreneur**. Matches Agent Lead Engine's purple accent colors for visual consistency.

## What's in here

- `index.html` — the entire site (HTML + CSS inline, no build step)
- `README.md` — this file

## To preview locally

Open `index.html` in any browser. Done.

## To add your photo

1. Drop a square image in this folder named `profile.jpg` (ideally 400×400 or 800×800 px).
2. Open `index.html`, find the comment `<!-- <img src="profile.jpg" alt="Samuel Ochoa"> -->` (around line ~230).
3. Delete the `<!--` and `-->` so the `<img>` tag is active.
4. Save. The purple-gradient circle with "SO" initials will be replaced with your headshot, still circular-cropped.

## To deploy

Easiest free options:

- **Netlify Drop** → drag-and-drop this folder at netlify.com/drop, done in 30 seconds.
- **Vercel** → `vercel` CLI or drag-and-drop in the dashboard.
- **GitHub Pages** → push to a repo named `samuelochoa.com`, enable Pages in settings.
- **Cloudflare Pages** → similar to Vercel, free tier generous.

Then point your `samuelochoa.com` domain at the host.

## What the site says (intentionally, not accidentally)

- Positions you as AI researcher + serial founder (no specific companies named, per your ask)
- Highlights three pillars of work: applied AI products & agents, LLM integration, AI advisory
- Lists credentials: Farmingdale Business '19, 3.9 GPA
- Single LinkedIn CTA for contact (no email exposed)
- Schema.org Person markup + Open Graph for good previews when someone shares the URL
- SEO title + meta description optimized for "Samuel Ochoa AI"

## Things you might want to add later

- Short blog / essays section (credibility multiplier)
- Speaking / podcast appearances list
- Case studies for advisory work (anonymized if needed)
- Downloadable CV
- An email address if you want a second contact option
- Link to X / GitHub if you become active on either

## To edit the copy

The whole page is plain HTML. Search for the text you want to change, edit, save. No frameworks, no npm install. Nothing to break.
