---
name: screenshots
description: >-
  Capture CitraSense UI screenshots for documentation using Playwright.
  Use when taking screenshots of the web dashboard, config tabs, monitoring
  page, or any CitraSense UI element for the docs site — including annotated
  shots with red-outline highlights on specific controls.
---

# CitraSense UI Screenshots

Capture dark-themed screenshots of the CitraSense web UI via Playwright. The
thin `scripts/screenshots/capture.py` CLI handles single shots (including
annotated ones); multi-shot series use dedicated scripts — template lives at
`scripts/screenshots/capture_operating_highlights.py`.

## Prerequisites

### 1. Install Playwright

From the docs repo root, use the local venv (create it if it doesn't exist):

```bash
cd /path/to/docs
python3 -m venv .venv          # only needed once
.venv/bin/pip install -r requirements.txt
.venv/bin/playwright install chromium
```

Always invoke scripts with `.venv/bin/python3` (not bare `python3`):

```bash
.venv/bin/python3 scripts/screenshots/capture.py ...
```

### 2. Verify CitraSense is running

```bash
curl -s http://localhost:24872/api/status | python3 -m json.tool
```

JSON back with status fields = daemon is up and the UI is ready.

### 3. Put CitraSense in dummy mode (for documentation screenshots)

Dummy mode gives a fully functional dashboard with simulated hardware and
tasks — realistic UI state without needing a real telescope. Configure it
through the web UI:

1. Open `http://localhost:24872/#config`
2. Click the **Advanced** tab in the config sidenav
3. Enable **Use Dummy API** (so tasks and uploads are simulated)
4. Switch to the **Hardware** tab
5. Select **Dummy** from the hardware adapter dropdown
6. Click **Save**

Verify:

```bash
curl -s http://localhost:24872/api/config | python3 -c \
  "import sys,json; c=json.load(sys.stdin); print('dummy_api:', c.get('use_dummy_api'), 'adapter:', c.get('hardware_adapter'))"
```

## capture.py — CLI options

The tool handles all Playwright boilerplate: launch browser, set viewport,
navigate, wait, click, hide, highlight, screenshot, close.

| Flag | Purpose |
|------|---------|
| `--url` | Page URL (e.g., `http://localhost:24872/#config`) |
| `--selector` | CSS selector of the element to screenshot |
| `--output` | Output PNG path (e.g., `docs/citrasense/img/config-api.png`) |
| `--wait-for` | Wait for this selector to be visible before acting |
| `--click` | Click a selector before capture (repeatable) |
| `--hide` | Hide elements matching this CSS selector before capture (repeatable) |
| `--highlight` | Add a red outline to elements matching this selector before capture (repeatable). Every match gets highlighted — scope the selector if you only want one. |
| `--pad` | Padding in px around the captured element. Default 0; auto-set to 24 when `--highlight` is used so the outline/shadow aren't clipped. |
| `--viewport` | Viewport size as WIDTHxHEIGHT (default: `1280x800`) |
| `--timeout` | Timeout in ms (default: `10000`) |

Playwright `:has()` and `:has-text()` pseudo-selectors work in every selector
flag (`--selector`, `--click`, `--highlight`) — they're resolved by Playwright's
Locator engine, not the DOM. The `--hide` flag uses `querySelectorAll` and
does *not* support them; use stable CSS (ids, classes) for hides.

## CitraSense navigation

### Main sections (URL hash)

- **Monitoring**: `http://localhost:24872/#monitoring`
- **Config**: `http://localhost:24872/#config`
- **Analysis**: `http://localhost:24872/#analysis`

Monitoring is the default when no hash is present.

### Config sub-tabs (click sidenav pills)

```
--click "a.nav-link:has-text('API')"
--click "a.nav-link:has-text('Hardware')"
--click "a.nav-link:has-text('Observation')"
--click "a.nav-link:has-text('Processing')"
--click "a.nav-link:has-text('Autofocus')"
--click "a.nav-link:has-text('Advanced')"
```

All config tab panes use Alpine's `x-show` (stay in DOM when hidden), so
switching tabs is just a click away from being screenshottable.

**Advanced tab gotcha**: use `.config-sidenav a:has-text('Advanced')` to avoid
a strict-mode collision with the "Advanced Settings" link inside the API tab's
warning alert.

### Log panel

Bootstrap accordion at the bottom of every page.

- Expand: `--click "#logAccordionHeader"`
- Screenshot target: `#logContainer`

### Modals

The setup wizard modal (`#setupWizard`) appears on first launch when the daemon
isn't configured. With dummy mode already configured, trigger it via JavaScript
— that's an inline Playwright script, not a `capture.py` call:

```python
page.evaluate("new bootstrap.Modal(document.getElementById('setupWizard')).show()")
page.locator("#setupWizard .modal-dialog").screenshot(path="...")
```

## Hiding sticky / fixed UI elements

CitraSense has two viewport-fixed elements that float over tall screenshots:

- **Log panel**: `#logAccordion` — `position: fixed; bottom: 0`
- **Save button bar**: `.config-save-bar` — `position: sticky; bottom: ...` on config pages

Always hide both when screenshotting config tabs or any element taller than the
viewport. Also hide the toast container so transient notifications don't leak
into shots:

```bash
--hide "#logAccordion" --hide ".config-save-bar" --hide "#toastContainer"
```

## Selector catalog

### Stable IDs (prefer these)

| Element | Selector |
|---------|----------|
| Status bar | `#globalStatusBar` |
| Log accordion | `#logAccordion` |
| Log content (expanded) | `#logContainer` |
| Setup wizard modal | `#setupWizard .modal-dialog` |
| Monitoring section root | `#monitoringSection` |
| Config section root | `#configSection` |

### Config pane anchors

Each config tab has at least one stable-id input you can wait on. Screenshot
the whole pane with `--selector "#configSection"` and use the anchor as
`--wait-for`:

| Config tab | Anchor element ID |
|-----------|-------------------|
| API | `#apiEndpoint` |
| Hardware | `#hardwareAdapterSelect` |
| Observation | `#observation_mode` |
| Processing | `#processors_enabled` |
| Autofocus | `#autofocus_target_preset` |
| Time & Location | `#time_offset_pause_ms` |
| Robotic Operations | `#sessionSunThreshold` |
| Advanced | `#logLevel` |

### Monitoring cards (no stable IDs — match on heading text)

| Card | Selector |
|------|----------|
| Telescope | `.card:has(.card-header:has-text("Telescope"))` |
| Optics | `.card:has(.card-header:has-text("Optics"))` |
| Active Tasks | `.card:has(.card-header:has-text("Active Tasks"))` |
| Scheduled Tasks | `.card:has(.card-header:has-text("Scheduled Tasks"))` |
| Robotic Session | `.card:has(.card-header:has-text("Robotic Session"))` |

## Common recipes

### Status bar

```bash
.venv/bin/python3 scripts/screenshots/capture.py \
  --url "http://localhost:24872/#monitoring" \
  --selector "#globalStatusBar" \
  --output "docs/citrasense/img/status-bar.png" \
  --wait-for "#globalStatusBar"
```

### Monitoring card

```bash
.venv/bin/python3 scripts/screenshots/capture.py \
  --url "http://localhost:24872/#monitoring" \
  --selector ".card:has(.card-header:has-text('Telescope'))" \
  --output "docs/citrasense/img/monitoring-telescope.png" \
  --wait-for "#monitoringSection" \
  --hide "#logAccordion" --hide "#toastContainer" \
  --viewport 1280x800
```

### Config sub-tab

```bash
.venv/bin/python3 scripts/screenshots/capture.py \
  --url "http://localhost:24872/#config" \
  --selector "#configSection" \
  --output "docs/citrasense/img/config-hardware.png" \
  --wait-for "#hardwareAdapterSelect" \
  --click "a.nav-link:has-text('Hardware')" \
  --hide "#logAccordion" --hide ".config-save-bar" --hide "#toastContainer" \
  --viewport 1280x900
```

### Log panel (expanded)

```bash
.venv/bin/python3 scripts/screenshots/capture.py \
  --url "http://localhost:24872/#monitoring" \
  --selector "#logContainer" \
  --output "docs/citrasense/img/log-panel.png" \
  --wait-for "#globalStatusBar" \
  --click "#logAccordionHeader"
```

### Full-page overview

Use a wider viewport and screenshot the whole section container:

```bash
--selector "#monitoringSection" --viewport 1440x900
```

### Annotated highlight (single shot)

Draw a red outline + glow around a specific control inside a wider crop. Great
for paragraph-scoped screenshots ("press *this* button") in walkthrough guides.
`--highlight` accepts Playwright `:has-text()` selectors.

```bash
.venv/bin/python3 scripts/screenshots/capture.py \
  --url "http://localhost:24872/#monitoring" \
  --selector ".card:has(.card-header:has-text('Telescope'))" \
  --highlight "button:has-text('Align Now')" \
  --output "docs/citrasense/img/operating-align-now-highlight.png" \
  --wait-for "#globalStatusBar" \
  --hide "#logAccordion"
```

Padding defaults to 24px when `--highlight` is used (covers the 3px outline +
3px offset + 14px shadow blur). Override with `--pad` if the highlight is still
clipped or you want more breathing room.

### Annotated highlight series (multiple shots)

When you need several highlighted shots from the same page state — e.g., a
walkthrough guide with one highlight per step — write a dedicated script
instead of calling the CLI N times. The pattern:

  * Inject the highlight CSS once
  * For each shot: add the class, capture with padded clip, strip the class
  * Supports compound framing (highlight *inside* element A, crop to element B)
    and multiple highlights in one frame

Canonical template: **`scripts/screenshots/capture_operating_highlights.py`**
— copy it, swap the selector list and output filenames, then run:

```bash
.venv/bin/python3 scripts/screenshots/capture_my_series.py
```

## Output conventions

- **Directory**: `docs/citrasense/img/`
- **Naming**: `{section}-{element}.png`
  - `monitoring-telescope.png`, `monitoring-optics.png`, `monitoring-active-tasks.png`
  - `config-api.png`, `config-hardware.png`
  - `status-bar.png`, `setup-wizard.png`, `log-panel.png`
  - Annotated highlights: `{guide}-{element}-highlight.png` (e.g., `operating-align-now-highlight.png`)
- **Theme**: always dark — the UI has no light mode
- **Viewport**: `1280x800` for desktop, `1280x900` for tall config panes, `390x844` for mobile, `1440x900` for full-section overviews
