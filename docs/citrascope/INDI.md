---
title: Working with INDI
nav_order: 30
parent: CitraScope
---

# INDI

## What is INDI

[INDI](https://indilib.org/) (Instrument Neutral Distributed Interface) is a protocol for controlling astronomical instrumentation. It provides a distributed, device-independent control protocol for astronomical equipment that operates over TCP/IP networks. INDI is the underlying technology that powers many observatory control applications, including KStars/Ekos.

## Why Use INDI with CitraScope

Direct INDI integration provides the most flexible and powerful hardware control option:

- **Linux Native** - Designed specifically for Linux observatory automation
- **Device Independent** - Standardized protocol works with hundreds of devices
- **Distributed Architecture** - Control equipment over network from anywhere
- **Multiple Clients** - Multiple applications can control same hardware simultaneously
- **Lightweight** - Minimal overhead compared to full GUI applications
- **Extensible** - Easy to add new drivers for custom or uncommon hardware
- **Active Development** - Regular updates and broad community support
- **Professional Grade** - Used in research observatories worldwide

## Prerequisites

Before integrating INDI with CitraScope, ensure you have:

- **Linux operating system** (Ubuntu, Debian, Fedora, or similar)
- **INDI Library 2.0.0 or later** installed
- **INDI drivers** for your specific hardware
- Your telescope hardware connected and accessible
- Network connectivity if running INDI server remotely
- **Root or sudo access** for initial setup and driver installation

## Installation

### Install INDI Library and Drivers
INDI is for advanced users and as such, we assume you come bearing an INDI environment.

### Install CitraScope with INDI Support

CitraScope requires the optional INDI dependencies:

```bash
pip install citrascope[indi]
```

This installs the `pyindi-client` library needed for INDI communication.

## Configuration

### In CitraScope Web Interface

1. **Navigate to Hardware Configuration**
   - Open CitraScope web interface (default: `http://localhost:24872`)
   - Go to **Hardware Settings**

2. **Select INDI Adapter**
   - Choose **INDI** from the hardware adapter dropdown

   The following settings are available:

   | Setting | Default | Required/Optional | Description |
   |---------|---------|-------------------|-------------|
   | **INDI Server Host** | `localhost` | Required | INDI server hostname or IP address |
   | **INDI Server Port** | `7624` (1-65535) | Required | INDI server port |
   | **Telescope Device Name** | (auto-detect) | Optional | Name of the telescope device. Leave empty to auto-detect the first available telescope. |
   | **Camera Device Name** | (auto-detect) | Optional | Name of the camera device. Leave empty to auto-detect the first available camera. |

3. **Configure Device Mapping**
   - Specify the INDI device names for your equipment:
     - Telescope/Mount device name
     - Camera device name

5. **Save Configuration**
   - Save settings and check if connections turn green

## Supported Features

The INDI adapter supports comprehensive hardware control:

- ✅ **Mount/Telescope Control** - Slew, sync, track, park/unpark, abort
- ✅ **Camera Control** - Exposure, gain, offset, binning, frame types

## Limitations

### Known Limitations

- **Linux Only** - INDI libraries only work on Linux systems (use KStars adapter for macOS/Windows)
- **Driver Availability** - Not all hardware has INDI drivers; check [INDI driver list](https://indilib.org/devices.html)

### Platform Considerations

- Requires `pyindi-client` which only compiles on Linux
- For development on macOS/Windows, use the provided Dev Container

## Troubleshooting

### Connection Issues

**Problem**: CitraScope cannot connect to INDI server

**Solutions**:
- Verify INDI server is running: `ps aux | grep indiserver`
- Check server is listening: `netstat -tlnp | grep 7624`
- Ensure **INDI Server Host** and **INDI Server Port** are correct in CitraScope settings
- Test with indi_getprop: `indi_getprop -h localhost -p 7624`
- Check firewall allows connections on INDI port
- Review INDI server logs for errors

### Device Connection Problems

**Problem**: INDI devices won't connect

**Solutions**:
- Check device is powered on and connected via USB/serial
- Verify user is in `dialout` group: `groups $USER`
- Check device permissions: `ls -l /dev/ttyUSB*`
- Review USB device detection: `dmesg | tail`
- Try different USB ports or cables
- Restart INDI server with correct driver
- Check driver compatibility with your hardware version

### Device Name Problems

**Problem**: CitraScope can't find specified devices

**Solutions**:
- List available devices: `indi_getprop | grep DEVICE`
- Verify exact device names (case-sensitive)
- Update **Telescope Device Name** and **Camera Device Name** in CitraScope settings
- Leave device names empty to use auto-detection
- Ensure devices are connected in INDI before CitraScope connects
- Check for typos in device name configuration

### Performance Issues

### Image Capture Problems

**Problem**: Images aren't captured or are corrupted

**Solutions**:
- Verify camera is connected and cooled
- Check available disk space on INDI server
- Test manual capture with indi_eval or KStars
- Review camera driver logs
- Ensure proper USB power supply
- Check camera-specific settings (gain, offset, format)
- Verify FITS file integrity