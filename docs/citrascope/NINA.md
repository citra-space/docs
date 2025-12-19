---
title: Working with N.I.N.A.
nav_order: 10
parent: CitraScope
---

# N.I.N.A.

## What is NINA

[N.I.N.A.](https://nighttime-imaging.eu/) (Nighttime Imaging 'N' Astronomy) is a free, open-source Windows application designed for astrophotography. It provides advanced sequencing capabilities, equipment control, and image capture automation. NINA supports a wide range of cameras, mounts, filter wheels, focusers, and other observatory equipment through ASCOM and native drivers.

## Why Use NINA with CitraScope

NINA's robust API and sequencing engine make it an excellent platform for automated telescope tasking. You'll choose NINA if your telescope control stack in Windows-based.

## Prerequisites

### Note: Presently only Planewave telescopes supported, more scopes coming soon.

Before integrating NINA with CitraScope, ensure you have:

- **Windows 10 or Windows 11** (64-bit recommended)
- **NINA 3.2 or later** installed ([download here](https://nighttime-imaging.eu/download/))
- **NINA Advanced API plugin** enabled
- **JOKO Orbitals plugin** enabled
- **Planewave tools** enabled 
- Your telescope hardware already configured and working in NINA
- Network connectivity between the NINA system and CitraScope

## Installation

### Enable NINA Advanced API

1. Open NINA
2. Navigate to **Options → Plugins**
3. Find and enable the **Advanced API** plugin
4. Configure the API to listen on a specific port (default: 1888)
5. Restart NINA to activate the plugin

### Install CitraScope

If you haven't already installed CitraScope, follow the [Installation Guide](Installation.html).

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
   - These will be used as defaults for CitraScope tasks

### In CitraScope Web Interface

1. **Navigate to the Hardware Configuration Page**
   - Open CitraScope web interface (default: `http://localhost:24872`)
   - Go to **Hardware Settings**

2. **Select NINA Adapter**
   - Choose **NINA** from the hardware adapter dropdown
   - Enter the NINA system's hostname or IP address
   - Enter the API port (default: 1888)

3. **Save Configuration**
   - Save your settings and Citrascope will try to connect to your hardware.

## Supported Features

The NINA adapter supports the following capabilities:

- ✅ **Mount Control** - Slew to coordinates, track, park/unpark
- ✅ **Camera Control** - Exposure control, gain, offset, binning
- ✅ **Image Capture** - Single and multiple exposures
- ✅ **Filter Wheel** - Automatic filter selection
- ✅ **Cooling Control** - Camera temperature management
- ✅ **Sequence Execution** - Custom NINA sequences triggered by tasks
- ✅ **Plate Solving** - Position verification and sync
- ⚠️ **Autofocus** - Supported but requires proper configuration in NINA
- ⚠️ **Guiding** - Integration depends on your guiding setup

## Limitations

### Known Limitations

- **Windows Only** - NINA is Windows-specific; Linux/Mac users should use INDI or KStars
- **API Dependency** - Requires the Advanced API plugin to be installed and running
- **Network Access** - Both NINA and CitraScope must be network accessible to each other

### Performance Considerations

- NINA should be running continuously for CitraScope to execute tasks
- Large image files may take time to upload depending on network bandwidth
- Ensure your system has adequate resources for both NINA and CitraScope

## Troubleshooting

### Connection Issues

**Problem**: CitraScope cannot connect to NINA

**Solutions**:
- Verify NINA is running and the Advanced API plugin is enabled
- Check that the hostname/IP and port are correct in CitraScope settings
- Ensure Windows Firewall allows connections on the API port
- Test connectivity with `telnet <hostname> <port>` from the CitraScope system
- Restart both NINA and CitraScope

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
- Check available disk space on both NINA and CitraScope systems
- Ensure the camera is properly cooled and stabilized
- Review exposure settings for the task
- Check network bandwidth for upload issues
