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

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then install CitraScope:

```bash
uv tool install citrascope
```

## Optional extras

Install additional hardware support as needed:

```bash
uv tool install citrascope --with citrascope[indi]          # INDI telescope control (Linux)
uv tool install citrascope --with citrascope[zwo-mount]     # ZWO AM3/AM5/AM7 mounts
uv tool install citrascope --with citrascope[usb-camera]    # USB/webcam capture via OpenCV
uv tool install citrascope --with citrascope[all-hardware]  # Everything
```

See [Direct Hardware](DirectHardware.html) for the full list of supported devices and their extras.

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
