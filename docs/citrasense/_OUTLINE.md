# CitraSense Documentation Outline

> **This is a planning document, not published content.**
> Jekyll ignores files prefixed with `_`. This outline tracks what the CitraSense
> docs section should cover. Check off sections as they get written. Delete this
> file when coverage is complete.

---

## Published pages

- [x] `index.md` — Landing page (overview, features, tasking flow, adapters, contributing, security)
- [x] `GettingStarted.md` — Quick start, Python install, uv, pip, extras, next steps
- [x] `RaspberryPi.md` — Standalone Pi image page (flash, first boot, WiFi, GPS, troubleshooting)
- [x] `Monitoring.md` — Monitoring tab walkthrough (status bar, telescope, optics, tasks, log panel, safety alerts, operational controls). Peer of Configuration/Analysis; the former `Dashboard.md` parent page was flattened away.
- [x] `Configuration.md` — Configuration tab walkthrough (API, hardware, autofocus, calibration, observation, processing, time & location, robotic operations, edge NATS, advanced)
- [x] `Analysis.md` — Analysis tab walkthrough (summary cards, processor timing, filters, task list, Auto-Tune, reprocessing)
- [x] `Adapters.md` — Hardware Adapters parent page (overview, capability comparison table)
- [x] `TelescopeSensor.md` — Telescope sensor detail page (mount controls, one-button field setup, optics card, autofocus, pointing model, robotic session, active/scheduled tasks)
- [x] `Operating.md` — Full-session walkthrough (prep → align → focus → run a task → review)
- [x] `DirectHardware.md` — Direct Hardware adapter guide
- [x] `NINA.md` — N.I.N.A. adapter guide

> The KStars/Ekos and INDI adapters were removed from CitraSense (#518, 2026-07-20).
> Their doc pages (`KStars.md`, `INDI.md`) were deleted and all cross-references
> scrubbed. CitraSense now ships two real-hardware adapters (Direct, N.I.N.A.) plus
> the Dummy test adapter.

---

## Outstanding work

### 1. Quick Start Guide — NEW (`QuickStart.md`, nav_order: 06)

- [ ] First launch (`citrasense` or `python -m citrasense`)
- [ ] Opening the web UI (default port 24872)
- [ ] Setup walkthrough (API endpoint, token, telescope ID, adapter selection)
- [ ] Verifying the connection (status bar indicators)
- [ ] What happens automatically once configured (polling, imaging, processing, upload)

### ~~2. Installation UPDATE — Raspberry Pi section~~ DONE

- [x] Add Raspberry Pi image section to `Installation.md` (citrasense-pi)
  - [x] What the Pi image includes (systemd autostart, WiFi provisioning via Comitup, GPS/chrony)
  - [x] Flashing the SD card and first-boot WiFi setup
  - [x] Accessing the UI at `http://citrasense-<mission>.local`
  - [x] Pi image versioning vs CitraSense application version

### 3. Troubleshooting — NEW (`Troubleshooting.md`, nav_order: 50)

- [ ] Log file locations and how to find them
- [ ] Common issues:
  - [ ] Can't connect to Citra API (bad token, wrong endpoint, SSL errors)
  - [ ] Hardware adapter won't connect (per-adapter common failures)
  - [ ] Tasks not appearing (wrong telescope ID, automated scheduling disabled)
  - [ ] Plate solving failures (too few stars, wrong FOV estimate, poor pointing)
  - [ ] Upload failures (network issues, 404 on duplicate task)
  - [ ] Time health warnings (NTP drift, GPS not connected, chrony misconfigured)
- [ ] Debug aids:
  - [ ] `keep_processing_output` — retains intermediate pipeline files
  - [ ] `keep_images` — retains raw FITS files after upload
  - [ ] `reprocess` CLI tool — replay a debug directory through the pipeline

### 4. Processing Pipeline — NEW (`Pipeline.md`, nav_order: 25, single page)

- [ ] Overview: what happens after an image is captured (imaging → processing → upload queues)
- [ ] Calibration processor: applying bias/dark/flat masters
- [ ] Plate Solver: astrometry.net, WCS fitting, solve quality metrics, common failure causes
- [ ] Source Extractor: detecting stars and satellites via SExtractor
- [ ] Photometry Calibrator: APASS cross-matching, zero-point calculation, local catalog option
- [ ] Satellite Matcher: TLE propagation, source-to-prediction matching, elset cache
- [ ] Annotated Image: overlay JPEG generation

### 5. ~~KStars / INDI review~~ REMOVED

Both adapters were removed from CitraSense (#518). Pages deleted; nothing to review.

### 6. Multi-sensor & non-telescope sensors — NEW

CitraSense supports multiple sensors per ground station. The operator-visible
surface area for non-telescope sensors is not yet documented.

- [ ] **Sensors overview page** (`Sensors.md`, nav_order: 6, `has_children: true`) — what a "sensor" is, the modalities CitraSense ships (telescope, all-sky, staring camera), how to add / remove one, and how each gets its own task queue.
- [ ] **All-sky camera** (`Allsky.md`, child of Sensors) — purpose, hardware (RPi HQ, USB), streaming controls, frame storage.
- [ ] **Staring camera** (`StaringCamera.md`, child of Sensors) — link to the `target_acquired` daemon, ping log, operating window, what gets uploaded. (Detection-backend choice — on-device optical pipeline vs `target_acquired` — is partially covered in Configuration.md until this page exists.)

### 7. Ground-station switching — NEW

- [ ] How to register a new ground station from current GPS
- [ ] What happens when you switch sites (hardware disconnect/reconnect, in-flight task drop)
- [ ] When to use it (rover deployments, swapping hosts between sites)
- [ ] Could fit as a section in `Sensors.md` or a short top-level `GroundStation.md` page.

---

## Sections removed from outline (already covered)

These were in the original outline but are now fully documented in existing pages:

| Original section | Covered by |
|---|---|
| Landing page update (Direct adapter, Pi link, pipeline) | `index.md` already has all items |
| Calibration (capturing frames, managing masters) | Configuration.md Calibration tab |
| Autofocus & Alignment | Configuration.md Autofocus tab + Monitoring.md Optics/Telescope cards |
| Safety & Operational Controls | Monitoring.md (abort, operator stop, cable wrap, safety alerts, mode switches) + Configuration.md Time & Location |
| Configuration Reference | Configuration.md serves as the setting-by-setting reference |
| Observation Modes (auto/static/tracking) | Configuration.md Observation tab covers the dropdown and per-mode guidance |
| Development & Architecture | Developer-focused; covered in citrasense repo's CLAUDE.md |

---

## Writing guidelines

### Audience and voice

- **Reader**: Telescope operators using CitraSense in the field. They know astrophotography and their hardware — they are not developers and do not read the CitraSense source code.
- **Voice**: Direct and task-oriented. Second person ("To configure X, go to..."). Present tense. Short sentences.
- **Include**: Features visible in the UI, settings and what they do, step-by-step workflows, observable behavior, troubleshooting for things an operator can actually see or change.
- **Exclude**: Internal class names, code architecture, algorithm details, refactors, and anything that only matters to a developer. If a code change doesn't affect what an operator sees or does, it doesn't belong in the docs.
- **Test**: "Would an operator care about this?" If the answer is no, leave it out or reframe it as operator-visible behavior.

### Format

- Short pages, tables for settings, callouts for warnings
- Dark screenshots where possible (operators use this at night)
- Front matter pattern: `title`, `parent: CitraSense`, `nav_order`, optional `has_children`
- For nested sections, use `grand_parent: CitraSense` on third-level pages
- Test locally: `cd docs && bundle exec jekyll serve`
