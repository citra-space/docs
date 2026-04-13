# CitraScope Screenshot Capture

Capture dark-themed screenshots of the CitraScope web UI for documentation.
Uses Playwright via the thin `capture.py` CLI tool in `scripts/screenshots/`.

## Prerequisites

### 1. Install Playwright

From the docs repo root, use the venv (create it if it doesn't exist):

```bash
cd /path/to/docs
python3 -m venv .venv  # only needed once
.venv/bin/pip install -r requirements.txt
.venv/bin/playwright install chromium
```

When running `capture.py`, always use `.venv/bin/python3` (not bare `python3`)
to ensure the right environment:

```bash
.venv/bin/python3 scripts/screenshots/capture.py ...
```

### 2. Verify CitraScope is running

```bash
curl -s http://localhost:24872/api/status | python3 -m json.tool
```

If it returns JSON with status fields, the daemon is up and the UI is ready.

### 3. Put CitraScope in dummy mode (for documentation screenshots)

Coach the operator to configure dummy mode through the web UI:

1. Open `http://localhost:24872/#config`
2. Click the **Advanced** tab in the config sidenav
3. Enable **Use Dummy API** (so tasks and uploads are simulated)
4. Go to the **Hardware** tab
5. Select **Dummy** from the hardware adapter dropdown
6. Click **Save**

This gives a fully functional dashboard with simulated hardware and tasks — ideal
for screenshots that show realistic UI state without requiring a real telescope.

To verify: `curl -s http://localhost:24872/api/config | python3 -c "import sys,json; c=json.load(sys.stdin); print('dummy_api:', c.get('use_dummy_api'), 'adapter:', c.get('hardware_adapter'))"`

## capture.py Usage

The tool lives at `scripts/screenshots/capture.py`. It handles all Playwright
boilerplate — launch browser, set viewport, navigate, wait, click, screenshot element, close.

```bash
python scripts/screenshots/capture.py \
  --url <URL> \
  --selector <CSS_SELECTOR> \
  --output <OUTPUT_PATH> \
  [--wait-for <SELECTOR>] \
  [--click <SELECTOR>]... \
  [--viewport WIDTHxHEIGHT] \
  [--timeout MS]
```

### Arguments

| Arg | Required | Description |
|-----|----------|-------------|
| `--url` | Yes | Full URL including hash (e.g., `http://localhost:24872/#monitoring`) |
| `--selector` | Yes | CSS selector of the element to screenshot |
| `--output` | Yes | Output PNG path relative to repo root |
| `--wait-for` | No | Wait for this selector to be visible before any actions (use for page-ready checks) |
| `--click` | No | Click this selector before capture. Repeatable for multi-step setup. |
| `--viewport` | No | Viewport as `WIDTHxHEIGHT`. Default: `1280x800` |
| `--timeout` | No | Timeout in ms for waits/clicks. Default: `10000` |

## CitraScope Navigation

### Main sections (URL hash)

- **Monitoring**: `http://localhost:24872/#monitoring`
- **Config**: `http://localhost:24872/#config`

The default section when no hash is present is Monitoring.

### Config sub-tabs (click sidenav pills)

The config section has a left sidenav with pill links. Switch tabs by clicking them:

```
--click "a.nav-link:has-text('Hardware')"
--click "a.nav-link:has-text('Observation')"
--click "a.nav-link:has-text('Processing')"
--click "a.nav-link:has-text('Autofocus')"
--click "a.nav-link:has-text('Advanced')"
--click "a.nav-link:has-text('API')"
```

All config tab panes use `x-show` (stay in DOM when hidden), so switching tabs is
just a click away from being screenshottable.

### Log panel

The log panel is a Bootstrap accordion at the bottom of every page:

- Expand: `--click "#logAccordionHeader"`
- Screenshot target: `#logContainer`

### Modals

The setup wizard modal (`#setupWizard`) appears on first launch when the daemon
is not configured. To capture it with dummy mode already configured, trigger it
via JavaScript — use an inline Playwright script instead of capture.py:

```python
page.evaluate("new bootstrap.Modal(document.getElementById('setupWizard')).show()")
page.locator("#setupWizard .modal-dialog").screenshot(path="...")
```

## Selector Catalog

### Stable IDs (preferred)

| Element | Selector |
|---------|----------|
| Status bar | `#globalStatusBar` |
| Log accordion | `#logAccordion` |
| Log content (expanded) | `#logContainer` |
| Setup wizard modal | `#setupWizard .modal-dialog` |
| Config section root | `#configSection` |

### Config pane anchors (use parent for pane screenshot)

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

To screenshot an entire config tab pane, find the pane's parent `div` — typically
the closest `x-show` container. Or screenshot `#configSection` for the full config
area including sidenav.

### Monitoring cards (no stable IDs — use heading text)

| Card | Selector pattern |
|------|-----------------|
| Telescope | `.card:has(.card-header:has-text("Telescope"))` |
| Optics | `.card:has(.card-header:has-text("Optics"))` |
| Active Tasks | `.card:has(.card-header:has-text("Active Tasks"))` |
| Scheduled Tasks | `.card:has(.card-header:has-text("Scheduled Tasks"))` |
| Robotic Session | `.card:has(.card-header:has-text("Robotic Session"))` |

These use Playwright's `:has-text()` pseudo-selector, which works in `capture.py`
selectors.

## Output Conventions

- **Directory**: `docs/citrascope/img/`
- **Naming**: `{section}-{element}.png`
  - `monitoring-telescope.png`
  - `monitoring-optics.png`
  - `monitoring-active-tasks.png`
  - `config-api.png`
  - `config-hardware.png`
  - `status-bar.png`
  - `setup-wizard.png`
  - `log-panel.png`
- **Theme**: Always dark (the UI has no light mode)
- **Viewport**: `1280x800` for desktop, `390x844` for mobile if needed

## Example Invocations

```bash
# Status bar
python scripts/screenshots/capture.py \
  --url "http://localhost:24872/#monitoring" \
  --selector "#globalStatusBar" \
  --output "docs/citrascope/img/status-bar.png" \
  --wait-for "#globalStatusBar"

# Telescope monitoring card
python scripts/screenshots/capture.py \
  --url "http://localhost:24872/#monitoring" \
  --selector ".card:has(.card-header:has-text('Telescope'))" \
  --output "docs/citrascope/img/monitoring-telescope.png" \
  --wait-for "#globalStatusBar"

# Config hardware tab
python scripts/screenshots/capture.py \
  --url "http://localhost:24872/#config" \
  --selector "#configSection" \
  --output "docs/citrascope/img/config-hardware.png" \
  --wait-for "#hardwareAdapterSelect" \
  --click "a.nav-link:has-text('Hardware')"

# Log panel (expanded)
python scripts/screenshots/capture.py \
  --url "http://localhost:24872/#monitoring" \
  --selector "#logContainer" \
  --output "docs/citrascope/img/log-panel.png" \
  --wait-for "#globalStatusBar" \
  --click "#logAccordionHeader"
```
