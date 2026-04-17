---
title: Installation
nav_order: 5
parent: CitraScope
---

# Installation

{: .note }
Looking for the Raspberry Pi image? See the [Raspberry Pi](RaspberryPi.html) page — flash an SD card and power on, no manual install needed.

## Requirements

Python **3.10, 3.11, or 3.12**.

## Install with uv (recommended)

[uv](https://docs.astral.sh/uv/) handles Python versions, virtual environments, and dependencies in a single tool.

Install CitraScope:

```bash
uv tool install citrascope
```

## Hardware extras

Some devices need additional Python libraries. Install everything at once, or only what you need:

```bash
uv tool install citrascope --with citrascope[all-hardware]
```

See [Direct Hardware](DirectHardware.html) for the per-device extras and the full list of supported hardware.

## Install with pip

```bash
pip install citrascope
```

## Run

```bash
citrascope
```

The web dashboard opens at [http://localhost:24872](http://localhost:24872). From there, connect to the Citra Space API and select your hardware adapter.

To use a different port:

```bash
citrascope --web-port 8080
```
