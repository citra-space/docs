---
title: CitraScope
nav_order: 4
has_children: true
---

# CitraScope

CitraScope is a software package that automates the collection of images of objects on orbit. A telescope operator can opt-in their telescope to being tasked automatically by Citra Space Domain Awareness (SDA) or other Citra users, and monitor all automated activity through the CitraScope web dashboard.

![CitraScope Screenshot](/img/citrascope_screenshot.png)

CitraScope can control your hardware directly or work alongside popular astrophotography programs like N.I.N.A. and KStars. For dedicated deployments, [citrascope-pi](https://github.com/citra-space/citrascope-pi) provides a pre-built Raspberry Pi image with everything pre-configured.

## Features

CitraScope provides a comprehensive solution for automated telescope tasking:

- **Web-based Configuration** - Configure your hardware and connect to the Citra Space API through an intuitive web interface
- **API Integration** - Seamlessly connects to Citra Space's API and registers your telescope as an available resource for the community
- **Hardware Control** - Interfaces with your telescope, camera, filter wheel, and focuser through multiple adapter options
- **Task Automation** - Acts as an autonomous daemon that receives, executes, and reports on observation tasks without manual intervention
- **Processing Pipeline** - Captured images pass through a six-stage pipeline: calibration, plate solving, source extraction, photometry, satellite matching, and annotated image generation — all before uploading results to Citra Space

## Tasking

CitraScope continuously polls the Citra Space API for assigned observation tasks. When a task is received, the software:

1. Validates the task parameters against your hardware capabilities
2. Slews the telescope to the target coordinates
3. Configures camera settings and captures the requested images
4. Runs each image through the processing pipeline (calibration, plate solving, source extraction, photometry, satellite matching, and annotated image generation)
5. Uploads the processed observation data back to Citra Space

Telescope operators maintain full control over when their hardware is available for tasking and can monitor all automated activities through the web dashboard.

## Hardware Adapters

CitraScope supports two primary hardware adapters:

- **Direct Hardware** - CitraScope's native hardware control with no intermediary software needed. The recommended path for Linux, macOS, and Raspberry Pi deployments. Supports ZWO ASI cameras, Moravian cameras, ZWO AM3/AM5/AM7 mounts, ZWO EAF focusers, and more.
- **[N.I.N.A.](NINA.html)** (Nighttime Imaging 'N' Astronomy) - For Windows setups with Planewave mounts running N.I.N.A.'s Advanced API.

Additional adapters are available for [KStars](KStars.html) (D-Bus) and [INDI](INDI.html) (Linux) environments. See [Hardware Adapters](Adapters.html) for a full comparison.

## Open Source and Contributing

CitraScope is open source software maintained on [GitHub](https://github.com/citra-space/citrascope). We welcome contributions from the community, whether you're fixing bugs, adding new hardware adapters, or improving documentation.

To get started with development:
- Review our [GitHub repository](https://github.com/citra-space/citrascope) for the latest source code
- Check the open issues for areas where you can contribute
- Follow our development setup guide in the repository README
- Submit pull requests with your improvements

The project uses modern Python development practices including pre-commit hooks, pytest for testing, and automated CI/CD pipelines.

## Security and Privacy

CitraScope is designed with transparency and data minimization in mind:

- **Open Source** - All source code is publicly available on GitHub, allowing you to audit exactly what the software does
- **Minimal Data Collection** - CitraScope only transmits data necessary for telescope tasking: observation parameters, image data, and task completion status
- **Local Control** - Your telescope credentials and hardware configuration remain on your local system and are never sent to Citra.space
- **Operator Autonomy** - You retain full control over when your telescope is available for tasking and can disable automated operations at any time
- **No Telemetry** - CitraScope does not collect analytics, usage statistics, or any telemetry data beyond what's required for task execution

All communication with the Citra.space API occurs over encrypted HTTPS connections. Your observation data is only used to fulfill tasking requests and contribute to the space domain awareness mission.

If you have security concerns or discover a vulnerability, please report it through our [GitHub security advisories](https://github.com/citra-space/citrascope/security/advisories).
