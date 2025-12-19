---
title: CitraScope
nav_order: 7.5
---

# CitraScope

Citrascope is a software package designed to work alongside telescope hardware control systems to automate the collection of images of objects on orbit. A telescope operator can opt-in their telescope to being tasked automatically by Citra Space Domain Awareness (SDA) or other Citra users. The operator can monitor automated telescope tasking through the CitraScope hardware tasking dashboard. 

![CitraScope Screenshot](/img/citrascope_screenshot.png)


It's built to run alongside popular astrophotography programs like N.I.N.A. and KStars through APIs offered by those programs.

## Features

CitraScope provides a comprehensive solution for automated telescope tasking:

- **Web-based Configuration** - Configure your hardware and connect to the Citra.space API through an intuitive web interface
- **API Integration** - Seamlessly connects to Citra.space's API and registers your telescope as an available resource for the community
- **Hardware Control** - Directly interfaces with your configured telescope and camera hardware through industry-standard protocols
- **Task Automation** - Acts as an autonomous daemon that receives, executes, and reports on photography tasks without manual intervention

## Tasking

CitraScope continuously polls the Citra.space API for assigned observation tasks. When a task is received, the software:

1. Validates the task parameters against your hardware capabilities
2. Coordinates with your telescope control software to slew to the target
3. Configures camera settings and captures the requested images
4. Processes and uploads the observation data back to Citra.space
5. Reports task completion status and any relevant metadata

Telescope operators maintain full control over when their hardware is available for tasking and can monitor all automated activities through the web dashboard.

## Hardware Adapters

CitraScope provides a suite of telescope hardware adapters to control common astrophotography software stacks:

- **[N.I.N.A.](NINA.html)** (Nighttime Imaging 'N' Astronomy) - Windows-based advanced sequencing platform
- **[KStars](KStars.html)** - Cross-platform planetarium and telescope control software
- **[INDI](INDI.html)** - Instrument Neutral Distributed Interface for Linux-based observatory control

Each adapter leverages the native APIs provided by these platforms to ensure reliable, low-latency hardware control.

## Open Source and Contributing

CitraScope is open source software maintained on [GitHub](https://github.com/citra-space/citrascope). We welcome contributions from the community, whether you're fixing bugs, adding new hardware adapters, or improving documentation.

To get started with development:
- Review our [GitHub repository](https://github.com/citra-space/citrascope) for the latest source code
- Check the open issues for areas where you can contribute
- Follow our development setup guide in the repository README
- Submit pull requests with your improvements

The project uses modern Python development practices including pre-commit hooks, pytest for testing, and automated CI/CD pipelines.

// ...existing code...

## Security and Privacy

CitraScope is designed with transparency and data minimization in mind:

- **Open Source** - All source code is publicly available on GitHub, allowing you to audit exactly what the software does
- **Minimal Data Collection** - CitraScope only transmits data necessary for telescope tasking: observation parameters, image data, and task completion status
- **Local Control** - Your telescope credentials and hardware configuration remain on your local system and are never sent to Citra.space
- **Operator Autonomy** - You retain full control over when your telescope is available for tasking and can disable automated operations at any time
- **No Telemetry** - CitraScope does not collect analytics, usage statistics, or any telemetry data beyond what's required for task execution

All communication with the Citra.space API occurs over encrypted HTTPS connections. Your observation data is only used to fulfill tasking requests and contribute to the space domain awareness mission.

If you have security concerns or discover a vulnerability, please report it through our [GitHub security advisories](https://github.com/citra-space/citrascope/security/advisories).
