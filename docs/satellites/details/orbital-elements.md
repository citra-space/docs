---
title: Orbital Elements History
nav_order: 9
parent: Details and Tools
grand_parent: Satellites
---

# Orbital Elements History

The Orbital Elements History section on the Orbital Analysis tab displays charts showing how the satellite's orbital parameters evolve over time.

## Understanding Orbital Elements

Orbital elements (also called Keplerian elements) are parameters that define a satellite's orbit. Tracking how these elements change over time reveals important information about the satellite's behavior, including natural orbital evolution, atmospheric drag effects, and deliberate maneuvers.

## Time Range Selection

Select the time range for the orbital element charts:

| Option | Description |
|--------|-------------|
| **7 Days** | Recent week of data |
| **30 Days** | Last month (default) |
| **90 Days** | Last quarter |

## Filters

### Status Filter

{: .note }
> The status filter is available to Government tier users and above. Standard users only see approved element sets.

Filter element sets by review status:

- **Approved** - Only approved elsets (default for all users)
- **Pending** - Elsets awaiting review (Government+ only)
- **Rejected** - Rejected elsets (Government+ only)

### Type Filter

Filter element sets by source type:

- **GP** - General Perturbations (TLE-based)
- **External** - From external data providers
- **Analyst** - Created by analysts in the platform

The type filter intelligently defaults based on available data for the satellite.

## Charts

### Orbital Period and Altitude

This combined chart shows two related orbital parameters:

**Orbital Period** (left axis)
- Time for the satellite to complete one orbit
- Measured in minutes
- Decreasing period indicates the orbit is lowering (often due to drag)

**Perigee and Apogee Altitude** (right axis)
- Perigee: Lowest point in the orbit
- Apogee: Highest point in the orbit
- Measured in kilometers above Earth's surface

### Semi-Major Axis

The semi-major axis represents the orbit's size:

- Measured in kilometers
- Half the longest diameter of the elliptical orbit
- A decreasing semi-major axis indicates orbital decay due to atmospheric drag
- Sudden changes may indicate maneuvers

### Inclination

The orbital inclination is the tilt of the orbit relative to Earth's equator:

- Measured in degrees (0° = equatorial, 90° = polar)
- Typically very stable for most satellites
- Small drifts occur due to gravitational perturbations from the Sun and Moon
- Sudden changes may indicate plane-change maneuvers

### Right Ascension of Ascending Node (RAAN)

RAAN describes the orientation of the orbit in space:

- Measured in degrees (0° to 360°)
- Indicates where the satellite crosses the equator going northbound
- Naturally drifts due to Earth's oblateness (J2 effect)
- Drift rate depends on orbit altitude and inclination

## Interacting with Charts

### Hover Information

Hover over any data point to see:

- Elset epoch (date/time)
- Exact element value
- Source information
- Review status

### Elset Selection

Click on any data point to select that element set:

- The selected elset is highlighted across all charts
- The Observation Residuals chart updates to show residuals for the selected elset
- The Element Sets grid scrolls to show the selected elset

### Zoom and Pan

- **Zoom**: Use mouse wheel or pinch gestures
- **Pan**: Click and drag on the chart
- **Reset**: Double-click to reset the view

## Key Insights

| Pattern | Possible Interpretation |
|---------|------------------------|
| Gradual altitude decrease | Atmospheric drag causing orbital decay |
| Sudden altitude change | Orbital maneuver (boost or de-orbit) |
| RAAN precessing steadily | Normal J2 precession effect |
| Inclination jump | Plane-change maneuver |
| Consistent elset quality | Stable, well-tracked satellite |
| Scattered data points | Possible tracking issues or analyst-generated fits |
