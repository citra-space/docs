---
title: KStars
nav_order: 3
parent: Hardware Adapters
grand_parent: CitraScope
---

# KStars
{: .no_toc }

## What is KStars

[KStars](https://edu.kde.org/kstars/) is a powerful, free desktop planetarium application for Linux, macOS, and Windows. Beyond its planetarium capabilities, KStars includes Ekos, a complete astrophotography suite that provides observatory control, image capture, guiding, focusing, and alignment capabilities.

## Why Use KStars with CitraScope

KStars/Ekos provides a professional-grade observatory control platform with excellent automation capabilities:
- **Cross-Platform** - Runs on Linux, macOS, and Windows
- **INDI Integration** - Native support for hundreds of astronomical devices
- **Free and Open Source** - Active development and community support

## Prerequisites

Before integrating KStars with CitraScope, ensure you have:

- **KStars 3.6.0 or later** installed ([download here](https://edu.kde.org/kstars/))
- **Ekos configured** with your telescope hardware
- **INDI server** running with your equipment profile
- Your telescope hardware already configured and working in Ekos
- CitraScope running on the **same machine** as KStars (the adapter uses local D-Bus)

## Installation

### Install KStars/Ekos

**Linux (Ubuntu/Debian)**:
```bash
sudo apt-add-repository ppa:mutlaqja/ppa
sudo apt-get update
sudo apt-get install kstars-bleeding indi-full
```

**macOS**:
1. **Install D-Bus with brew** (required for CitraScope integration):
  ```bash
  brew install dbus
  brew services start dbus
  ```

2. **Download and Install KStars**:
  - Visit the [KStars website](https://edu.kde.org/kstars/)

**Windows**: Not currently tested or supported on windows.

### Install CitraScope

Follow the [Getting Started](GettingStarted.html) guide if you haven't already installed CitraScope.

## Configuration

### In KStars/Ekos

1. **Configure Your Equipment Profile**
   - Open Ekos: **Tools → Ekos**
   - Create or select your equipment profile
   - Add your mount, camera, focuser, filter wheel, etc.
   - Test that all equipment connects properly

2. **Set Up Plate Solving**
   - Go to **Ekos → Align** module
   - Configure your plate solver (Astrometry.net recommended)
   - Test plate solving with a captured image

3. **Configure Camera Settings**
   - Set default gain, offset, and cooling targets
   - Configure image format (FITS recommended)
   - Set your capture directory

### In CitraScope Web Interface

1. **Navigate to Hardware Configuration**
   - Open CitraScope web interface (default: `http://localhost:24872`)
   - Go to **Hardware Settings**

2. **Select KStars Adapter**
   - Choose **KStars** from the hardware adapter dropdown

   The following settings are available:

   | Setting | Default | Description |
   |---------|---------|-------------|
   | **D-Bus Service Name** | `org.kde.kstars` | D-Bus service name for KStars. Only change if running a custom KStars instance. |
   | **Camera/CCD Device Name** | `CCD Simulator` | Name of the camera device in your Ekos profile. Check Ekos logs on connect for available devices. |
   | **Filter Wheel Device Name** | *(empty)* | Name of the filter wheel device. Leave empty if you have no filter wheel. |
   | **Optical Train Name** | `Primary` | Name of the optical train in your Ekos profile. Check Ekos logs on connect for available trains. |
   | **Exposure Time (seconds)** | `1.0` | Exposure duration in seconds for each frame (0.001–300). |
   | **Frame Count** | `1` | Number of frames to capture per observation (1–100). |
   | **Binning X** | `1` | Horizontal pixel binning (1–4). |
   | **Binning Y** | `1` | Vertical pixel binning (1–4). |
   | **Image Format** | `Mono` | Camera image format. Options: `Mono`, `RGGB`, `RGB`. |

3. **Save Configuration**
   - Save your settings. CitraScope will connect to KStars via D-Bus and report hardware status in the dashboard.

## Supported Features

The KStars adapter supports the following capabilities:

- ✅ **Mount Control** - Slew to coordinates, position readout
- ✅ **Camera Control** - Exposure, binning, image format
- ✅ **Image Capture** - Single and multiple exposures via Ekos Scheduler
- ✅ **Filter Wheel** - Automatic filter selection and discovery
- ✅ **Plate Solving** - Position verification via Ekos Align module

## Limitations

### Known Limitations

- **Local D-Bus Only** - The adapter communicates via session D-Bus. CitraScope must run on the same machine as KStars.
- **No Autofocus** - Autofocus is not currently supported through this adapter.
- **No Focuser Control** - Direct focuser movement is not available. Use KStars/Ekos to manage focus.
- **No Disconnect** - CitraScope cannot programmatically disconnect from KStars. Close KStars manually when done.
- **Windows Not Supported** - D-Bus is not natively available on Windows.

### Performance Considerations

- KStars should remain running with Ekos active for CitraScope tasks
- Plate solving requires appropriate index files for your imaging scale
- Ensure adequate system resources for both KStars and CitraScope

## Troubleshooting

### Connection Issues

**Problem**: CitraScope cannot connect to KStars

**Solutions**:
- Verify KStars is running with Ekos started
- Check that D-Bus is accessible: run `dbus-send --session --print-reply --dest=org.kde.kstars /KStars org.freedesktop.DBus.Peer.Ping` to test
- Ensure **D-Bus Service Name** is correct in CitraScope settings (typically `org.kde.kstars`)
- On macOS, confirm D-Bus is running: `brew services list | grep dbus`
- Restart both KStars and CitraScope
- Review KStars logs: **Help → Debug → View Logs**

### Equipment Profile Issues

**Problem**: Equipment profile fails to load or connect

**Solutions**:
- Verify profile is correctly configured in Ekos
- Test manual connection in Ekos first
- Check all equipment is powered on and connected
- Review INDI driver compatibility and versions
- Update INDI libraries to latest version
- Check equipment permissions (especially on Linux: serial port access)

