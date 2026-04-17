# CLAUDE.md — Agent Guide for Citra Space Docs

## What is this repo?

Public documentation for the Citra Space platform, built with **Jekyll** and the **Just the Docs** theme. Hosted on GitHub Pages.

The Jekyll source lives in `docs/` (not the repo root). The repo root has `scripts/` for tooling and this file.

## Quick start

```bash
cd docs
bundle install
bundle exec jekyll serve
```

Site runs at `http://127.0.0.1:4000`. Auto-regenerates on file changes.

## Repo structure

```
docs/                          # Jekyll source root
├── _config.yml                # Site config, theme, color scheme, version
├── _includes/head_custom.html # Injected into <head> — scrollspy JS lives here
├── _sass/custom/custom.scss   # Theme overrides — sticky TOC, wider sidebar
├── citrascope/                # CitraScope product docs
│   ├── _OUTLINE.md            # Planning doc (not published, _ prefix)
│   └── img/                   # Screenshots for CitraScope pages
├── citra-space-app-api/       # Web app / API docs
├── guides-and-tutorials/      # How-to guides
└── index.md                   # Landing page
scripts/
└── screenshots/
    ├── capture.py                         # CLI: single-shot Playwright screenshots (+ annotated highlights)
    └── capture_operating_highlights.py    # Template: multi-shot annotated-highlight series
```

## Writing conventions

- **Audience**: Telescope operators in the field. Not developers.
- **Voice**: Direct, second person, present tense. Short sentences.
- **Include**: UI-visible features, settings, workflows, troubleshooting.
- **Exclude**: Internal class names, code architecture, algorithm details.
- **Test**: "Would an operator care about this?" If no, leave it out.

### Page format

- Front matter: `title`, `parent`, `nav_order`, optional `has_children`, `grand_parent`
- Tables for settings, callouts for warnings (`{: .note }`, `{: .warning }`)
- Dark screenshots only (night-vision UI)
- Files prefixed with `_` are ignored by Jekyll (use for planning docs)

### Long pages with TOC

For comprehensive pages (like Monitoring, Configuration), use a single long page with an auto-generated TOC:

```markdown
# Page Title
{: .no_toc }

Intro text.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

---

## First Section
```

On wide screens (80rem+), the TOC floats as a sticky sidebar on the right via CSS Grid (`custom.scss`). The scrollspy in `head_custom.html` highlights the active heading. On smaller screens, the TOC stays inline as a collapsible `<details>` block. The `scrollIntoView` call is gated behind a media query to avoid hijacking scroll on small viewports.

## Screenshots

Use the Playwright capture tool. See the `screenshots` skill (`.cursor/skills/screenshots/SKILL.md`) for full usage — prerequisites, dummy-mode setup, selector catalog, and all recipes including annotated highlights.

### Single shot (CLI)

```bash
cd /path/to/docs
.venv/bin/python3 scripts/screenshots/capture.py \
  --url "http://localhost:24872/#config" \
  --selector "#configSection" \
  --output "docs/citrascope/img/config-hardware.png" \
  --click "a:has-text('Hardware')" \
  --hide "#logAccordion" --hide ".config-save-bar" --hide "#toastContainer" \
  --viewport 1280x900
```

### Annotated highlight (red outline on a specific control)

Add `--highlight SELECTOR` for paragraph-scoped "press *this* button" shots.
`--pad` auto-defaults to 24px when `--highlight` is used so the outline and
shadow stay in frame.

```bash
.venv/bin/python3 scripts/screenshots/capture.py \
  --url "http://localhost:24872/#monitoring" \
  --selector ".card:has(.card-header:has-text('Telescope'))" \
  --highlight "button:has-text('Align Now')" \
  --output "docs/citrascope/img/operating-align-now-highlight.png" \
  --wait-for "#globalStatusBar" \
  --hide "#logAccordion"
```

For *multiple* highlighted shots from the same page state (e.g., a walkthrough
guide with one highlight per step), copy and adapt
`scripts/screenshots/capture_operating_highlights.py` — the canonical series
template. Run series scripts with `.venv/bin/python3`.

### Key points

- Always `--hide` sticky/fixed overlays on tall screenshots (log panel, save bar, toasts)
- Store images in `docs/citrascope/img/`, named `{page}-{section}.png`; annotated highlights end in `-highlight.png`
- CitraScope runs at `http://localhost:24872`; Playwright runs out of the local venv (`.venv/bin/python3`). One-time setup is in the skill doc's Prerequisites section.

## Custom theme additions

### Sticky right-side TOC (`custom.scss`)

At 80rem+ viewport, pages with a `#markdown-toc` element get a CSS Grid layout: content in column 1, TOC in column 2. The TOC is `position: sticky` with `max-height: calc(100vh - 4rem)` and its own scroll overflow.

The CSS uses `:has()` selectors scoped to pages that actually contain a TOC, so pages without one are unaffected.

### Scrollspy (`head_custom.html`)

Vanilla JS using scroll events + `requestAnimationFrame`. Walks all `#markdown-toc` links, finds the furthest heading above `scrollY + 120px`, and adds `.toc-active` to the matching TOC link. `scrollIntoView({ block: 'nearest' })` keeps the active link visible in the sidebar — but only on wide screens (`min-width: 80rem` media query) to avoid scroll-fighting on mobile where the TOC is inline.

### Wider sidebar

The Just the Docs sidebar is widened from 16rem to 19rem at 50rem+ viewports to accommodate the deeper nav tree.

## Planning

`docs/citrascope/_OUTLINE.md` tracks what CitraScope doc pages need to be written. Checked items are done. Use it to decide what to work on next.

## Cache busting

`_config.yml` has a `version` field. Increment it when CSS/JS changes need to bypass browser cache. It's injected via `head_custom.html` as a CSS custom property.
