---
title: Welcome
nav_order: 1
---

<img src="img/citra-space-corporation.svg" alt="Citra Space Corporation Logo" width="300">

# Citra Space Documentation
{: .no_toc }

Welcome to Citra Space! Here you'll find everything you need to get started with the platform — from using the app and API, to setting up hardware, automating observations, and more.

## Quick Links

- [Citra Space App](https://app.citra.space) — Sign in or create an account
- [API Documentation](https://api.citra.space/docs) — Interactive API reference
- [CitraSense](citrasense/) — Open source telescope automation daemon
- [Discord Community](https://discord.gg/STgJQkWe9y) — Support and discussion
- [GitHub Projects](https://github.com/citra-space) — Open source repositories

## Our Mission

_Citra provides modular sensing and software solutions for detecting, tracking, and identifying orbiting objects to ensure safe and sustainable space operations for all._

## What Citra Space Offers

The Citra Space platform provides tools for satellite tracking, orbital analysis, and space domain awareness:

- **Satellite catalog** — Browse and search satellites with orbital element history, element set management, aliases, and transmission data
- **Orbital analysis** — Assess orbit quality through observation residuals, track how orbital elements evolve over time, and fit new element sets to observation data
- **Maneuver detection** — Detect orbital maneuvers through element discontinuity analysis with delta-v decomposition and verification status tracking
- **Close approach screening** — Calculate conjunctions between objects with configurable distance thresholds, time of closest approach, miss distance, and relative velocity
- **Ground station management** — Register ground stations with satellite pass predictions, weather forecasts, sun and moon data for optical planning, and sensor configuration
- **Observation collection** — Schedule optical and RF observations with prioritized collection requests, automated task assignment across sensors, and image and RF capture processing
- **REST API** — Programmatic access to platform features for observation submissions, orbital analysis, and automation

## Getting Started

### Use the App

[Sign up for an account](citra-space-app-api/sign-up) and explore the [Citra Space App/API documentation](citra-space-app-api/) for walkthroughs of satellites, ground stations, sensors, and user settings.

### Use the API

Follow the [API Quickstart Guide](guides-and-tutorials/api-quickstart-guide) to start making API calls, or jump straight to the [interactive API docs](https://api.citra.space/docs).

### Set Up Hardware

- [Add and Manage Telescopes](guides-and-tutorials/add-and-manage-telescopes) — Configure your optical sensors
- [Add and Manage Antennas](guides-and-tutorials/add-and-manage-antennas) — Configure your RF sensors

### Automate with CitraSense

[CitraSense](citrasense/) is open source software that automates telescope observations by connecting your hardware to the Citra Space platform. Once installed, you'll spend most of your time in the [web dashboard](citrasense/Dashboard): [Monitoring](citrasense/Monitoring) for live status, [Analysis](citrasense/Analysis) for post-session review, and [Configuration](citrasense/Configuration) for setup.

Hardware options: [Direct Hardware](citrasense/DirectHardware) (recommended), [N.I.N.A.](citrasense/NINA), [KStars](citrasense/KStars), or [INDI](citrasense/INDI). A pre-built [Raspberry Pi image](citrasense/RaspberryPi) is also available for headless field deployments.

## More Resources

- [KepLemon](keplemon) — Rust-accelerated astrodynamics Python library for satellite propagation, orbit determination, and close approach detection
- [Contribute](contribute) — Help improve our docs, CitraSense, KepLemon, and other open source projects
- [Legal](legal) — Terms of use, privacy policy, and cookie policy

## Support

Join our [Discord community](https://discord.gg/STgJQkWe9y) for help, feedback, and general space discussion. You can also reach us via the contact option in the app.
