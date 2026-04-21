---
title: Direct Hardware
nav_order: 1
parent: Hardware Adapters
grand_parent: CitraSense
---

# Direct Hardware
{: .no_toc }

## What is Direct Hardware

The Direct Hardware adapter lets CitraSense control your telescope devices end-to-end — no intermediary software like N.I.N.A. or KStars is needed. CitraSense communicates directly with your cameras, mounts, focusers, and filter wheels over USB or serial.

This is the recommended adapter for Linux, macOS, and Raspberry Pi deployments.

## Why Use Direct Hardware

- **Simplest deployment** — no additional software to install, configure, or keep running
- **Full CitraSense integration** — autofocus, alignment, pointing model calibration, camera preview, and calibration frame capture are all built in
- **Composable** — connect only the devices you have. A camera alone works fine; add a mount, focuser, or filter wheel as your setup grows.
- **Headless-friendly** — ideal for unattended Raspberry Pi deployments via [citrascope-pi](https://github.com/citra-space/citrascope-pi)

## Supported Devices

### Cameras

| Device | Install Extra | Notes |
|--------|--------------|-------|
| **Moravian Instruments** (Gx/Cx series) | *(none)* | Includes integrated filter wheel support |
| **USB Camera** (via OpenCV) | `uv tool install citrasense --with citrasense[usb-camera]` | Guide cameras, planetary cameras, webcams |
| **Raspberry Pi HQ Camera** (IMX477) | `uv tool install citrasense --with citrasense[rpi]` | For Pi-based deployments |
| **Ximea Hyperspectral** (MQ series) | Install `ximea-api` from the [Ximea SDK](https://www.ximea.com/support/wiki/apis/Python) | Specialized hyperspectral imaging |

### Mounts

| Device | Install Extra | Notes |
|--------|--------------|-------|
| **ZWO AM3 / AM5 / AM7** | `uv tool install citrasense --with citrasense[zwo-mount]` | USB serial or WiFi TCP connection |

{: .note }
> You can run CitraSense without a mount for static camera setups. Leave the mount type empty in configuration.

### Focusers

| Device | Install Extra | Notes |
|--------|--------------|-------|
| **ZWO EAF** (Electronic Automatic Focuser) | *(none)* | Enables autofocus when paired with a camera |

### Filter Wheels

| Device | Install Extra | Notes |
|--------|--------------|-------|
| **Moravian Instruments** (External) | *(none)* | Standalone external filter wheel |
| **Integrated camera wheel** | *(none)* | Automatically detected from Moravian cameras — leave filter wheel type empty |

## Configuration

### In CitraSense Web Interface

1. Open the CitraSense web interface (default: `http://localhost:24872`)
2. Go to the **Config** tab and click **Hardware** in the sidenav
3. Select **Direct Hardware** from the hardware adapter dropdown

The settings form updates dynamically based on your device selections:

| Setting | Required | Description |
|---------|----------|-------------|
| **Camera Type** | Yes | Select your camera from the dropdown. Available options depend on which device libraries are installed. |
| **Mount Type** | No | Select your mount, or leave empty for a static (no-mount) setup. |
| **Filter Wheel Type** | No | Select a standalone filter wheel, or leave empty to auto-detect an integrated wheel from the camera. |
| **Focuser Type** | No | Select your focuser, or leave empty if you don't have one. |

After selecting a device type, additional device-specific settings appear (e.g., serial port, connection parameters, gain defaults). These vary by device.

4. Click **Save Configuration**. CitraSense will connect to each selected device and report status in the dashboard.

### Install Extras

Some devices require additional Python libraries — the **Install Extra** column in the tables above shows the command for each one. Install before selecting the device, then restart CitraSense.

To install everything at once:

```bash
uv tool install citrasense --with citrasense[all-hardware]
```

## Features

The Direct Hardware adapter provides the most complete feature set of any adapter:

- ✅ **Mount control** — slew, track, custom tracking rates, home
- ✅ **Camera control** — exposure, gain, image capture, live preview
- ✅ **Filter wheel** — automatic filter selection and renaming
- ✅ **Focuser control** — move to position, abort
- ✅ **Autofocus** — V-curve autofocus when both camera and focuser are connected
- ✅ **Plate solving** — position verification and sync
- ✅ **Alignment** — plate-solve-based mount model calibration
- ✅ **Pointing model** — multi-point calibration for improved pointing accuracy
- ✅ **Calibration frames** — bias, dark, and flat frame capture from the UI
- ✅ **Camera preview** — live JPEG preview in the monitoring tab
- ✅ **Mount limits** — altitude limits and cable wrap tracking with auto-unwind
- ✅ **Custom tracking rates** — for satellite tracking (when mount supports it)

{: .important }
> Autofocus, filter wheel, and focuser features require the corresponding device to be connected. If you only have a camera and mount, those features simply won't appear in the UI.

## When to Choose Direct vs an Intermediary Adapter

**Choose Direct Hardware when:**
- You're building a new setup and don't already use N.I.N.A. or KStars
- You want the simplest possible deployment (especially on a Pi)
- You need pointing model calibration or V-curve autofocus
- Your devices are in the supported list above

**Choose N.I.N.A. instead when:**
- You run Windows with a Planewave mount
- You already have a working N.I.N.A. equipment profile
- You need park/unpark or safety monitor integration

**Choose KStars or INDI when:**
- You already have a working KStars/Ekos or INDI setup with devices not supported by Direct Hardware

## Troubleshooting

### Device Not Appearing in Dropdown

**Problem**: A device type doesn't appear in the configuration dropdown.

**Solutions**:
- Install the required extras: `uv tool install citrasense --with citrasense[zwo-mount]` (or whichever extra)
- Restart CitraSense after installing new packages
- Check that the device is physically connected (USB, serial)

### Connection Fails

**Problem**: CitraSense reports a device as disconnected after saving configuration.

**Solutions**:
- Check USB connections and cables
- On Linux, verify your user is in the `dialout` group for serial devices: `groups $USER`
- Check device permissions: `ls -l /dev/ttyUSB*` or `ls -l /dev/ttyACM*`
- For ZWO AM mounts over WiFi, verify the mount's IP address and that port 11880 is reachable
- Review the CitraSense log for detailed error messages (Monitoring tab → expand the log panel)

### Autofocus Not Available

**Problem**: The autofocus option doesn't appear.

**Solution**: Autofocus requires both a **camera** and a **focuser** to be selected and connected. If either is missing, autofocus is disabled.
