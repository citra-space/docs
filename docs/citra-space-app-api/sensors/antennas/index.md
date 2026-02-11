---
title: Antennas
nav_order: 2
parent: Sensors
has_children: true
---

# Antennas

The antenna detail page displays the full configuration, tasking schedule, and RF captures for a specific antenna. This is the primary management interface for antenna owners.

## Understanding Antennas

Antennas are radio frequency sensors used for signal reception and transmission during satellite passes. Each antenna has configurable parameters that define its frequency range, pointing capabilities, and scheduling behavior. Antenna owners manage their instruments from this page, while other users can view antenna specifications and request observations through collection requests.

## Antenna Detail Page

The antenna detail page is organized into several sections:

- **Configuration** — Technical specifications and scheduling settings
- **Tasking Schedule** — Upcoming and historical observation tasks assigned to this antenna
- **RF Captures** — Radio frequency capture data collected by this antenna

## Antenna Configuration

The antenna configuration form contains the following fields:

| Field | Description |
|-------|-------------|
| **Name** | A descriptive name for the antenna (required) |
| **Ground Station** | The ground station where this antenna is deployed (optional) |
| **Min Frequency** | Minimum receivable frequency in Hertz (minimum 0) |
| **Max Frequency** | Maximum receivable frequency in Hertz (minimum 0) |
| **Min Elevation** | Minimum elevation angle for observations in degrees (0–90) |
| **Max Slew Rate** | Maximum speed the antenna can reposition in degrees per second (minimum 0) |
| **Home Azimuth** | Resting azimuth position in degrees (0–359.99) |
| **Home Elevation** | Resting elevation position in degrees (0–90) |
| **Half Power Beam Width** | Beam width at half power in degrees (minimum 0) |
| **Automated Scheduling** | Toggle to enable or disable automated task scheduling for this antenna |

{: .note }
> Min Frequency and Max Frequency define the antenna's receivable frequency range. Ensure these values accurately reflect your equipment's capabilities for proper task matching.

## Navigating to an Antenna

You can reach an antenna detail page from:

- **Sensors list** — Click the antenna name on the [Browsing and Filtering](../browsing-and-filtering) page
- **Ground station detail** — Click an antenna name in the [Sensors section](../../ground-stations/details/sensors) of a ground station

## Use Cases

Antenna configuration supports:

- **Capability definition** — Specifying the frequency range and elevation constraints for task matching
- **Scheduling optimization** — Setting slew rates and home positions to optimize task scheduling
- **Equipment inventory** — Maintaining accurate records of antenna specifications for observation planning
