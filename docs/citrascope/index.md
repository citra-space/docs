---
title: CitraScope
nav_order: 4
has_children: true
---

# CitraScope

CitraScope automates satellite imaging for the [Citra Space](https://citra.space) network. It runs as a daemon on your telescope computer, polls for observation tasks, controls your hardware, processes captured images, and uploads results — all unattended.

![CitraScope monitoring dashboard showing telescope status, task pipeline, and scheduled observations](img/monitoring-overview.png)

## How It Works

1. CitraScope polls the Citra Space API for assigned tasks
2. Slews the telescope to the target and captures images
3. Runs each image through the processing pipeline (calibration, plate solving, source extraction, photometry, satellite matching, annotated image)
4. Uploads results to Citra Space

You control availability through the [web dashboard](Monitoring.html) — enable or disable scheduling, pause processing, or halt everything with the abort button.

## Features

- **Web dashboard** — [Monitor](Monitoring.html) telescope status, task pipeline, and scheduled observations in real time. [Configure](Configuration.html) every setting from your browser. [Analyze](Analysis.html) past sessions to tune detection settings and reprocess stored images. Dark theme throughout to preserve night vision, and the layout adapts to phones and tablets for field use.
- **[Hardware Adapters](Adapters.html)** — Control your telescope, camera, filter wheel, and focuser through [Direct Hardware](DirectHardware.html) (recommended), [N.I.N.A.](NINA.html), [KStars](KStars.html), or [INDI](INDI.html).
- **Processing Pipeline** — Six-stage image pipeline: calibration, plate solving, source extraction, photometry, satellite matching, and annotated image generation.
- **Robotic Operations** — Automatic dusk-to-dawn sessions with start-of-night autofocus, pointing calibration, and self-tasking when the server queue is empty.
- **[Raspberry Pi](RaspberryPi.html)** — Flash an SD card, power on, connect to WiFi from your phone, and the dashboard is live. Pre-built image for headless field deployments.

## Getting Started

Install CitraScope, launch it, and open the web dashboard:

```bash
uv tool install citrascope
citrascope
```

The dashboard opens at [http://localhost:24872](http://localhost:24872). From there, connect to the Citra Space API and select your hardware adapter. See [Getting Started](GettingStarted.html) for details, or read [Operating CitraScope](Operating.html) for a walkthrough of a full session.

## Open Source

CitraScope is open source on [GitHub](https://github.com/citra-space/citrascope). Contributions are welcome — check the open issues or submit a pull request.

All source code is publicly auditable. CitraScope only transmits data needed for tasking (observation parameters, images, task status). Credentials and configuration stay local. No telemetry or analytics. All API traffic is HTTPS.

Report security concerns through [GitHub security advisories](https://github.com/citra-space/citrascope/security/advisories).
