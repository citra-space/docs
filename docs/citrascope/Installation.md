---
title: Installation
nav_order: 05
parent: CitraScope
---

# Installation

## System Requirements

CitraScope requires **Python 3.10, 3.11, or 3.12** to run properly.

## Install uv

We recommend [uv](https://docs.astral.sh/uv/) to install and manage CitraScope. It handles Python versions, virtual environments, and dependencies in a single tool.

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Installing CitraScope

```bash
uv tool install citrascope
```

### Optional Dependencies

If you're using Linux-based telescope control with INDI, install the additional INDI support:

```bash
uv tool install citrascope --with citrascope[indi]
```

## Running CitraScope

Once installed, CitraScope provides a command-line tool to start the daemon:

```bash
citrascope
```

By default, this starts the web interface on `http://localhost:24872` where you can configure your hardware and manage telescope tasking.

### Customizing the Web Interface Port

```bash
citrascope --web-port 8080
```

### Available Commands

```bash
citrascope --help
```

Once the daemon is running, navigate to the web interface in your browser to complete the setup process and connect your telescope hardware.

## Alternative: pip

If you prefer pip, CitraScope installs the standard way:

```bash
pip install citrascope
```
