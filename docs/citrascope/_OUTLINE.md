# CitraScope Documentation Outline

> **This is a planning document, not published content.**
> Jekyll ignores files prefixed with `_`. This outline tracks what the CitraScope
> docs section should cover. Check off sections as they get written. Delete this
> file when coverage is complete.

---

## Current pages

- [x] `index.md` — Landing page (overview, features, tasking flow, adapters, contributing, security)
- [x] `Installation.md` — Python install, pyenv, venv, PyPI, extras
- [x] `NINA.md` — N.I.N.A. adapter guide
- [x] `KStars.md` — KStars / Ekos adapter guide
- [x] `INDI.md` — Direct INDI adapter guide

---

## Proposed additions and updates

### 1. Landing page (`index.md`) — UPDATE

- [ ] Add Direct Hardware adapter to the adapter list (lead with it — it's the primary path)
- [ ] Reorder adapter list: Direct → N.I.N.A. → KStars → INDI
- [ ] Link to citrascope-pi for Raspberry Pi deployments
- [ ] Mention processing pipeline (plate solving, photometry, satellite matching) in features

### 2. Installation (`Installation.md`) — UPDATE

- [ ] Add Raspberry Pi image section (citrascope-pi)
  - What the Pi image includes (systemd autostart, WiFi provisioning via Comitup, GPS/chrony, INDI packages)
  - Flashing the SD card and first-boot WiFi setup
  - Accessing the UI at `http://citrascope-<mission>.local`
  - Pi image versioning vs CitraScope application version

### 3. Quick Start Guide — NEW (`QuickStart.md`, nav_order: 06)

- [ ] First launch (`citrascope` or `python -m citrascope`)
- [ ] CLI options (`--web-port`)
- [ ] Opening the web UI (default port 24872)
- [ ] Setup wizard walkthrough (API endpoint, token, telescope ID, adapter selection)
- [ ] Verifying the connection (status bar indicators)
- [ ] What happens automatically once configured (polling, imaging, processing, upload)

### 4. Web Dashboard — NEW (`Dashboard.md`, nav_order: 07, has_children: true)

#### 4a. Status Bar (`Dashboard-StatusBar.md`, parent: Web Dashboard)

- [ ] Safety monitor indicator
- [ ] WebSocket connection state
- [ ] Telescope and camera connection
- [ ] Task pipeline counts (imaging → processing → upload)
- [ ] Time health indicator

#### 4b. Monitoring Tab (`Dashboard-Monitoring.md`, parent: Web Dashboard)

- [ ] Telescope position and state
- [ ] Camera status and live preview
- [ ] Focus position and manual controls
- [ ] Filter wheel position and controls
- [ ] Active and queued tasks by pipeline stage
- [ ] Real-time log viewer (WebSocket streaming)
- [ ] Operational controls: pause/resume polling, emergency stop, operator stop

#### 4c. Configuration Tab (`Dashboard-Config.md`, parent: Web Dashboard)

- [ ] Citra API settings (endpoint, token, telescope ID, dummy mode)
- [ ] Hardware adapter selection and dynamic adapter-specific settings
- [ ] Observation settings (mode, exposure, frame count)
- [ ] Processor toggles
- [ ] Calibration settings
- [ ] Autofocus scheduling and target presets
- [ ] Alignment settings
- [ ] Time and GPS configuration
- [ ] Advanced settings (logging, retention, retry behavior)

### 5. Hardware Adapters — NEW parent page (`Adapters.md`, nav_order: 09, has_children: true)

> Move existing adapter pages under this parent. Update their `parent:` front
> matter from `CitraScope` to the new parent title.

- [ ] Overview of the adapter pattern and how adapters are selected
- [ ] Adapter capability comparison table (mount, camera, filter wheel, focuser, guiding, calibration, alignment)

#### 5a. Direct Hardware — NEW (`DirectHardware.md`, parent: Hardware Adapters, nav_order: 1)

> Lead adapter — CitraScope's native hardware control, no intermediary software needed.

- [ ] What "Direct" means (CitraScope controls devices without an intermediary program)
- [ ] Supported devices:
  - ZWO ASI cameras
  - Moravian cameras
  - Ximea cameras
  - USB webcams
  - ZWO EAF focuser
  - ZWO AM5 mount
- [ ] Per-device setup notes and prerequisites
- [ ] When to choose Direct vs an intermediary adapter

#### 5b. N.I.N.A. (`NINA.md`) — EXISTING, move under parent (nav_order: 2)

- [ ] Review for completeness against current features

#### 5c. KStars / Ekos (`KStars.md`) — EXISTING, move under parent (nav_order: 3)

- [ ] Review for completeness against current features

#### 5d. INDI (`INDI.md`) — EXISTING, move under parent (nav_order: 4)

- [ ] Review for completeness against current features

### 6. Citra API Connection — NEW (`CitraAPI.md`, nav_order: 15)

- [ ] What the Citra API is and what data flows through it
- [ ] Setting the API endpoint (production vs development vs custom URL)
- [ ] Personal access tokens (where to generate on the platform, how to enter in CitraScope)
- [ ] Telescope ID (how to find it on Citra Space)
- [ ] Dummy API mode (offline operation for testing without a live backend)
- [ ] Filter sync: how CitraScope and the Citra API keep filter libraries aligned
- [ ] Automated scheduling toggle (how to enable/disable server-side task assignment)

### 7. Observation Modes — NEW (`ObservationModes.md`, nav_order: 20, has_children: true)

#### 7a. Auto Mode (`ObservationModes-Auto.md`, parent: Observation Modes)

- [ ] How the system decides between static and tracking per-task
- [ ] When to use auto (recommended default for most operators)

#### 7b. Static Mode (`ObservationModes-Static.md`, parent: Observation Modes)

- [ ] Use case (GEO satellites, survey, deep-sky targets)
- [ ] Slew → optional plate solve after slew → burst capture flow
- [ ] `num_exposures` and `exposure_seconds` settings
- [ ] How plate_solve_after_slew improves pointing accuracy

#### 7c. Tracking Mode (`ObservationModes-Tracking.md`, parent: Observation Modes)

- [ ] Use case (LEO satellites with apparent motion)
- [ ] Lead position calculation and custom tracking rates
- [ ] Single-frame capture with motion compensation
- [ ] Filter selection for tracking observations

### 8. Processing Pipeline — NEW (`Pipeline.md`, nav_order: 25, has_children: true)

- [ ] Overview: what happens after an image is captured
- [ ] Three-queue architecture (imaging → processing → upload)
- [ ] How to toggle processors on/off in settings
- [ ] `skip_upload` mode (process locally but don't send results to API)

#### 8a. Calibration Processor (`Pipeline-Calibration.md`, parent: Processing Pipeline)

- [ ] Applying bias, dark, and flat frame masters to raw images
- [ ] How masters are selected and matched
- [ ] Relationship to the calibration capture UI (see section 9)

#### 8b. Plate Solver (`Pipeline-PlateSolver.md`, parent: Processing Pipeline)

- [ ] What it does (astrometric solution, WCS fitting to image)
- [ ] Tetra3 / pixelemon solving engine
- [ ] Source extraction (SEP) bundled into this step
- [ ] When solving fails and what affects success (star count, FOV, pointing accuracy)

#### 8c. Photometry Calibrator (`Pipeline-Photometry.md`, parent: Processing Pipeline)

- [ ] APASS catalog cross-matching for photometric calibration
- [ ] Zero-point calculation
- [ ] Local APASS catalog option (`use_local_apass_catalog` for offline/air-gapped setups)

#### 8d. Satellite Matcher (`Pipeline-SatelliteMatcher.md`, parent: Processing Pipeline)

- [ ] TLE propagation to predict satellite positions at exposure time
- [ ] Associating detected sources with predicted positions
- [ ] Elset cache and `elset_refresh_interval_hours` setting

#### 8e. Annotated Image (`Pipeline-AnnotatedImage.md`, parent: Processing Pipeline)

- [ ] What it generates (overlay JPEG with sources, matches, and WCS grid)
- [ ] Where to view annotated images (task preview in the UI)

### 9. Calibration — NEW (`Calibration.md`, nav_order: 30)

- [ ] Why calibration matters for photometric accuracy
- [ ] Capturing bias frames from the UI
- [ ] Capturing dark frames from the UI
- [ ] Capturing flat frames (twilight helper endpoint in the UI)
- [ ] `calibration_frame_count` and `flat_frame_count` settings
- [ ] Managing calibration suites (view, download, delete masters)

### 10. Autofocus & Alignment — NEW (`AutofocusAlignment.md`, nav_order: 35)

#### 10a. Autofocus

- [ ] Scheduled autofocus (enable, set interval in minutes)
- [ ] Target presets (current position, named bright stars, custom RA/Dec)
- [ ] Manual trigger from the monitoring tab
- [ ] How autofocus coordinates with the imaging queue (waits for idle)

#### 10b. Alignment

- [ ] What alignment does (plate solve to sync mount model)
- [ ] Align-on-startup behavior
- [ ] `alignment_exposure_seconds` setting
- [ ] Manual alignment trigger from the UI

### 11. Safety & Operational Controls — NEW (`Safety.md`, nav_order: 40)

- [ ] Emergency stop (what it does, how to trigger, how to clear)
- [ ] Operator stop
- [ ] Task polling pause/resume
- [ ] Mount homing
- [ ] Cable wrap / mount limits and unwind
- [ ] Time health monitoring and the pause threshold
- [ ] GPS location updates

### 12. Configuration Reference — NEW (`ConfigReference.md`, nav_order: 45)

- [ ] Complete table of every `CitraScopeSettings` field (name, type, default, description)
- [ ] Config file location per platform (macOS, Linux, Windows via platformdirs)
- [ ] How settings are persisted (JSON file, `update_and_save` merge behavior)
- [ ] Adapter-specific settings storage (nested dict keyed by adapter name, survives adapter switching)
- [ ] CLI-only settings (`--web-port`)

### 13. Troubleshooting — NEW (`Troubleshooting.md`, nav_order: 50)

- [ ] Log file locations and how to find them (`GET /api/config` returns paths)
- [ ] WebSocket log streaming in the monitoring tab
- [ ] Common issues:
  - [ ] Can't connect to Citra API (bad token, wrong endpoint, SSL errors)
  - [ ] Hardware adapter won't connect (per-adapter common failures)
  - [ ] Tasks not appearing (wrong telescope ID, automated scheduling disabled, API response issues)
  - [ ] Plate solving failures (too few stars, wrong FOV estimate, poor pointing)
  - [ ] Upload failures (network issues, 404 on duplicate task, file size)
  - [ ] Time health warnings (NTP drift, GPS not connected, chrony misconfigured)
  - [ ] Task retry behavior and backoff (max retries, delay escalation)
- [ ] Debug aids:
  - [ ] `keep_processing_output` — retains intermediate pipeline files for post-mortem
  - [ ] `keep_images` — retains raw FITS files after upload
  - [ ] `reprocess` CLI tool (`python -m citrascope.reprocess`) — replay a debug directory through the pipeline

### 14. Development & Architecture — NEW, OPTIONAL (`Development.md`, nav_order: 55)

> Lower priority. Useful for power users, contributors, and developers — not required for operators.

- [ ] Dummy adapter (simulates hardware for testing and development)
- [ ] Dummy API mode (offline operation without a live Citra backend)
- [ ] `reprocess` CLI tool (`python -m citrascope.reprocess`) — replay a debug directory through the pipeline
- [ ] Daemon lifecycle (startup → connect → poll → image → process → upload → repeat)
- [ ] Thread model (main loop, queue worker threads, web server daemon thread)
- [ ] Component diagram (daemon → task manager → queues → adapter + processors → API client)
- [ ] Pointer to `CLAUDE.md` in the citrascope repo for full developer reference

---

## Writing guidelines

- Follow the existing docs style: short pages, tables for settings, callouts for warnings
- Dark screenshots where possible (operators use this at night)
- Front matter pattern: `title`, `parent: CitraScope`, `nav_order`, optional `has_children`
- For nested sections, use `grand_parent: CitraScope` on third-level pages
- Test locally: `cd docs && bundle exec jekyll serve`
