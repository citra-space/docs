---
name: screenshots
description: >-
  Capture CitraScope UI screenshots for documentation using Playwright.
  Use when taking screenshots of the web dashboard, config tabs, monitoring
  page, or any CitraScope UI element for the docs site.
---

# CitraScope UI Screenshots

## Tool

`scripts/screenshots/capture.py` — Playwright-based headless screenshot tool.

Requires `PYENV_VERSION=3.12.0` (Playwright is installed in the 3.12 env):

```bash
cd /path/to/docs && PYENV_VERSION=3.12.0 python3 scripts/screenshots/capture.py [options]
```

## Options

| Flag | Purpose |
|------|---------|
| `--url` | Page URL (e.g., `http://localhost:24872/#config`) |
| `--selector` | CSS selector of the element to screenshot |
| `--output` | Output PNG path (e.g., `docs/citrascope/img/config-api.png`) |
| `--wait-for` | Wait for this selector to be visible before acting |
| `--click` | Click a selector before capture (repeatable) |
| `--hide` | Hide elements matching this CSS selector before capture (repeatable) |
| `--viewport` | Viewport size as WIDTHxHEIGHT (default: `1280x800`) |
| `--timeout` | Timeout in ms (default: `10000`) |

## Hiding Sticky/Fixed UI Elements

CitraScope has two viewport-fixed elements that float over tall screenshots:

- **Log panel**: `#logAccordion` — `position: fixed; bottom: 0` accordion bar
- **Save button bar**: `.config-save-bar` — `position: sticky; bottom: ...` on config pages

Always hide both when screenshotting config tabs or any element taller than the viewport:

```bash
--hide "#logAccordion" --hide ".config-save-bar"
```

Also hide the toast container to avoid transient notifications: `--hide "#toastContainer"`

## Common Recipes

### Config sub-tab

```bash
PYENV_VERSION=3.12.0 python3 scripts/screenshots/capture.py \
  --url "http://localhost:24872/#config" \
  --selector "#configSection" \
  --output "docs/citrascope/img/config-TABNAME.png" \
  --wait-for "#configSection" \
  --click "a:has-text('TabLabel')" \
  --hide "#logAccordion" --hide "#toastContainer" --hide ".config-save-bar" \
  --viewport 1280x900
```

For the **Advanced** tab, use `.config-sidenav a:has-text('Advanced')` to avoid
a strict-mode collision with the "Advanced Settings" link inside the API tab's
warning alert.

### Monitoring section

```bash
PYENV_VERSION=3.12.0 python3 scripts/screenshots/capture.py \
  --url "http://localhost:24872/#monitoring" \
  --selector ".card:has(.card-header:has-text('Telescope'))" \
  --output "docs/citrascope/img/monitoring-telescope.png" \
  --wait-for "#monitoringSection" \
  --hide "#logAccordion" --hide "#toastContainer" \
  --viewport 1280x800
```

### Full-page overview

Use a wider viewport and screenshot the whole section container:

```bash
--selector "#monitoringSection" --viewport 1440x900
```

## Output Conventions

- Store images in `docs/citrascope/img/`
- Naming: `{page}-{section}.png` (e.g., `config-hardware.png`, `monitoring-telescope.png`)
- Dark theme only — the UI is always dark
