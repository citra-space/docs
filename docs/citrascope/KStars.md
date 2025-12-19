---
title: Working with KStars
nav_order: 20
parent: CitraScope
---

# KStars

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
- Network connectivity between the KStars system and CitraScope
- **Astrometry.net** or similar plate solving configured (recommended)

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

Follow the [Installation Guide](Installation.html) if you haven't already installed CitraScope.

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
   - Enter the D-Bus session details (typically auto-detected on local systems)

3. **Configure Connection Settings**
   - Specify the equipment to use  (typically auto-detected on local systems)

4. **Save Configuration**
   - Save settings once connection, and check to see that all the hardware reports as connected.

## Limitations

### Known Limitations

- **D-Bus Dependency** - Requires D-Bus for local communication, must run on telescope computer

### Performance Considerations

- KStars should remain running with Ekos active for CitraScope tasks
- Plate solving requires appropriate index files for your imaging scale
- Large FITS files may take time to transfer over network
- Ensure adequate system resources for both KStars and CitraScope

## Troubleshooting

### Connection Issues

**Problem**: CitraScope cannot connect to KStars

**Solutions**:
- Verify KStars is running with Ekos started
- Check that D-Bus is accessible (for local) or Web Manager is enabled (for remote)
- Ensure hostname/IP address is correct in CitraScope settings
- Check firewall settings allow D-Bus or Web Manager port
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

