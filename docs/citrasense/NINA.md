---
title: N.I.N.A.
nav_order: 2
parent: Hardware Adapters
grand_parent: CitraSense
---

# N.I.N.A.
{: .no_toc }

## What is NINA

[N.I.N.A.](https://nighttime-imaging.eu/) (Nighttime Imaging 'N' Astronomy) is a free, open-source Windows application designed for astrophotography. It provides advanced sequencing capabilities, equipment control, and image capture automation. NINA supports a wide range of cameras, mounts, filter wheels, focusers, and other observatory equipment through ASCOM and native drivers.

## Why Use NINA with CitraSense

NINA's robust API and sequencing engine make it an excellent platform for automated telescope tasking. You'll choose NINA if your telescope control stack in Windows-based.

## Prerequisites

### Note: Presently only Planewave telescopes supported, more scopes coming soon.

Before integrating NINA with CitraSense, ensure you have:

- **Windows 10 or Windows 11** (64-bit recommended)
- **NINA 3.2 or later** installed ([download here](https://nighttime-imaging.eu/download/))
- **NINA Advanced API plugin** enabled
- **JOKO Orbitals plugin** enabled
- **Planewave tools** enabled 
- Your telescope hardware already configured and working in NINA
- Network connectivity between the NINA system and CitraSense

## Installation

### Enable NINA Advanced API

1. Open NINA
2. Navigate to **Options → Plugins**
3. Find and enable the **Advanced API** plugin
4. Configure the API to listen on a specific port (default: 1888)
5. Restart NINA to activate the plugin

### Install CitraSense

If you haven't already installed CitraSense, follow the [Getting Started](GettingStarted.html) guide.

## Configuration

### In NINA

1. **Enable the Advanced API Plugin**
   - Go to **Options → Plugins → Advanced API**
   - Check **Enable Advanced API**
   - Set the port (default: 1888)
   - Note the hostname/IP address of your NINA system

2. **Configure Your Equipment Profile**
   - Ensure all your hardware is properly configured in NINA
   - Test that you can successfully slew your mount and capture images
   - Verify plate solving is working if you plan to use it

3. **Set Up Your Camera Settings**
   - Configure camera gain, offset, and other imaging parameters
   - These will be used as defaults for CitraSense tasks

### In CitraSense Web Interface

1. **Navigate to the Hardware Configuration Page**
   - Open CitraSense web interface (default: `http://localhost:24872`)
   - Go to **Hardware Settings**

2. **Select NINA Adapter**
   - Choose **NINA** from the hardware adapter dropdown

   The following settings are available:

   | Setting | Default | Required/Optional | Description |
   |---------|---------|-------------------|-------------|
   | **N.I.N.A. API URL** | `http://nina:1888/v2/api` | Required | Base URL for the NINA Advanced HTTP API. Must start with `http://` or `https://`. |
   | **Bypass Autofocus** | `False` | Optional | Skip autofocus routine when initializing. When enabled, CitraSense will use cached focus positions if available. |

3. **Save Configuration**
   - Save your settings and Citrasense will try to connect to your hardware.

## Supported Features

The NINA adapter supports the following capabilities:

- ✅ **Mount Control** - Slew to coordinates, track, park/unpark
- ✅ **Camera Control** - Exposure control, gain, offset, binning
- ✅ **Image Capture** - Single and multiple exposures
- ✅ **Filter Wheel** - Automatic filter selection with automatic focus offset on filter change
- ✅ **Focuser Control** - Move, abort, and status via NINA Advanced API; manual controls work in the CitraSense web UI
- ✅ **Cooling Control** - Camera temperature management
- ✅ **Sequence Execution** - Custom NINA sequences triggered by tasks
- ✅ **Plate Solving** - Position verification and sync
- ✅ **Autofocus** - Full autofocus support via NINA; triggered by CitraSense's autofocus scheduler
- ⚠️ **Guiding** - Integration depends on your guiding setup

## Limitations

### Known Limitations

- **Windows Only** - NINA is Windows-specific; Linux/Mac users should use INDI or KStars
- **API Dependency** - Requires the Advanced API plugin to be installed and running
- **Network Access** - Both NINA and CitraSense must be network accessible to each other
- **Focuser move events** - NINA does not emit a WebSocket event when a focuser move completes; CitraSense polls the focuser position until the move finishes
- **Guiding** - PHD2/NINA guiding state is not currently surfaced in the CitraSense web UI

### Performance Considerations

- NINA should be running continuously for CitraSense to execute tasks
- Large image files may take time to upload depending on network bandwidth
- Ensure your system has adequate resources for both NINA and CitraSense

## Troubleshooting

### Connection Issues

**Problem**: CitraSense cannot connect to NINA

**Solutions**:
- Verify NINA is running and the Advanced API plugin is enabled
- Check that the **N.I.N.A. API URL** is correct in CitraSense settings
- Ensure Windows Firewall allows connections on the API port
- Test connectivity with `telnet <hostname> <port>` from the CitraSense system
- Restart both NINA and CitraSense

### API Errors

**Problem**: API commands fail or return errors

**Solutions**:
- Check the NINA log files for detailed error messages
- Verify all equipment is properly connected and powered on in NINA
- Ensure equipment profiles are correctly configured
- Update NINA and the Advanced API plugin to the latest versions

### Image Capture Problems

**Problem**: Images aren't captured or uploaded correctly

**Solutions**:
- Verify camera settings in NINA (gain, offset, cooling)
- Check available disk space on both NINA and CitraSense systems
- Ensure the camera is properly cooled and stabilized
- Review exposure settings for the task
- Check network bandwidth for upload issues
