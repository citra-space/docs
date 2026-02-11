---
title: Telescopes
nav_order: 3
parent: Sensors
has_children: true
---

# Telescopes

The telescope detail page displays the full configuration, tasking schedule, and image uploads for a specific telescope. This is the primary management interface for telescope owners.

## Understanding Telescopes

Telescopes are optical sensors used for visual and imaging observations of satellites. Each telescope has configurable parameters that define its physical capabilities and scheduling behavior. Telescope owners manage their instruments from this page, while other users can view telescope specifications and request observations through collection requests.

## Telescope Detail Page

The telescope detail page is organized into several sections:

- **Configuration** — Technical specifications and scheduling settings
- **Tasking Schedule** — Upcoming and historical observation tasks assigned to this telescope
- **Image Uploads** — Observation images captured by this telescope

## Telescope Configuration

The telescope configuration form contains core operational fields and optional optics specifications.

### Core Fields

| Field | Description |
|-------|-------------|
| **Name** | A descriptive name for the telescope (required) |
| **Ground Station** | The ground station where this telescope is deployed (optional) |
| **Angular Noise** | Measurement noise in arcseconds (minimum 0) |
| **Max Magnitude** | The faintest object the telescope can detect |
| **Min Elevation** | Minimum elevation angle for observations in degrees (0–90) |
| **Max Slew Rate** | Maximum speed the telescope can reposition in degrees per second (minimum 0) |
| **Home Azimuth** | Resting azimuth position in degrees (0–359.99) |
| **Home Elevation** | Resting elevation position in degrees (0–90) |
| **Automated Scheduling** | Toggle to enable or disable automated task scheduling for this telescope |

### Optics Specifications

These optional fields describe the telescope's optical system and are used for field-of-view calculations:

| Field | Description |
|-------|-------------|
| **Horizontal Pixel Count** | Number of pixels along the horizontal axis of the image sensor |
| **Vertical Pixel Count** | Number of pixels along the vertical axis of the image sensor |
| **Pixel Size** | Size of each pixel in micrometers (μm) |
| **Focal Length** | Focal length of the optical system in millimeters (mm) |
| **Focal Ratio** | The f-number of the optical system |
| **Image Circle Diameter** | Diameter of the usable image circle in millimeters (mm) |
| **Field of View** | Computed from pixel count, pixel size, and focal length — displayed as a read-only value |

{: .note }
> Field of View is automatically calculated when pixel count, pixel size, and focal length are provided. It cannot be edited directly.

## Navigating to a Telescope

You can reach a telescope detail page from:

- **Sensors list** — Click the telescope name on the [Browsing and Filtering](../browsing-and-filtering.md) page
- **Ground station detail** — Click a telescope name in the [Sensors section](../../ground-stations/details/sensors.md) of a ground station

## Use Cases

Telescope configuration supports:

- **Capability definition** — Specifying what the telescope can observe based on magnitude limits and elevation constraints
- **Scheduling optimization** — Setting slew rates and home positions to optimize task scheduling
- **Image calibration** — Providing optics specifications for accurate field-of-view and astrometric processing
