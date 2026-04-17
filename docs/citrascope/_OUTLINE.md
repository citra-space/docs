# CitraScope Documentation Outline

> **This is a planning document, not published content.**
> Jekyll ignores files prefixed with `_`. This outline tracks what the CitraScope
> docs section should cover. Check off sections as they get written. Delete this
> file when coverage is complete.

---

## Published pages

- [x] `index.md` — Landing page (overview, features, tasking flow, adapters, contributing, security)
- [x] `Installation.md` — Python install, uv, pip, extras
- [x] `RaspberryPi.md` — Standalone Pi image page (flash, first boot, WiFi, GPS, troubleshooting)
- [x] `Dashboard.md` — Web Dashboard parent page
- [x] `Monitoring.md` — Monitoring tab walkthrough (status bar, telescope, optics, tasks, log panel, safety alerts, operational controls)
- [x] `Configuration.md` — Configuration tab walkthrough (API, hardware, autofocus, calibration, observation, processing, time & location, robotic operations, advanced)
- [x] `Analysis.md` — Analysis tab walkthrough (summary cards, processor timing, filters, task list, Auto-Tune, reprocessing)
- [x] `Adapters.md` — Hardware Adapters parent page (overview, capability comparison table)
- [x] `Operating.md` — Full-session walkthrough (prep → align → focus → run a task → review)
- [x] `DirectHardware.md` — Direct Hardware adapter guide
- [x] `NINA.md` — N.I.N.A. adapter guide
- [x] `KStars.md` — KStars / Ekos adapter guide
- [x] `INDI.md` — Direct INDI adapter guide

---

## Outstanding work

### 1. Quick Start Guide — NEW (`QuickStart.md`, nav_order: 06)

- [ ] First launch (`citrascope` or `python -m citrascope`)
- [ ] Opening the web UI (default port 24872)
- [ ] Setup walkthrough (API endpoint, token, telescope ID, adapter selection)
- [ ] Verifying the connection (status bar indicators)
- [ ] What happens automatically once configured (polling, imaging, processing, upload)

### ~~2. Installation UPDATE — Raspberry Pi section~~ DONE

- [x] Add Raspberry Pi image section to `Installation.md` (citrascope-pi)
  - [x] What the Pi image includes (systemd autostart, WiFi provisioning via Comitup, GPS/chrony)
  - [x] Flashing the SD card and first-boot WiFi setup
  - [x] Accessing the UI at `http://citrascope-<mission>.local`
  - [x] Pi image versioning vs CitraScope application version

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

### 5. KStars / INDI review — minor

- [ ] Review `KStars.md` for completeness against current features
- [ ] Review `INDI.md` for completeness against current features

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
| Development & Architecture | Developer-focused; covered in citrascope repo's CLAUDE.md |

---

## Writing guidelines

### Audience and voice

- **Reader**: Telescope operators using CitraScope in the field. They know astrophotography and their hardware — they are not developers and do not read the CitraScope source code.
- **Voice**: Direct and task-oriented. Second person ("To configure X, go to..."). Present tense. Short sentences.
- **Include**: Features visible in the UI, settings and what they do, step-by-step workflows, observable behavior, troubleshooting for things an operator can actually see or change.
- **Exclude**: Internal class names, code architecture, algorithm details, refactors, and anything that only matters to a developer. If a code change doesn't affect what an operator sees or does, it doesn't belong in the docs.
- **Test**: "Would an operator care about this?" If the answer is no, leave it out or reframe it as operator-visible behavior.

### Format

- Short pages, tables for settings, callouts for warnings
- Dark screenshots where possible (operators use this at night)
- Front matter pattern: `title`, `parent: CitraScope`, `nav_order`, optional `has_children`
- For nested sections, use `grand_parent: CitraScope` on third-level pages
- Test locally: `cd docs && bundle exec jekyll serve`
