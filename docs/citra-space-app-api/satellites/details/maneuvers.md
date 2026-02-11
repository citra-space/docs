---
title: Maneuvers
nav_order: 12
parent: Details and Tools
grand_parent: Satellites
---

# Maneuvers

The Maneuvers tab displays detected orbital maneuvers performed by the satellite.

## Understanding Maneuvers

Orbital maneuvers are deliberate changes to a satellite's orbit, typically performed using onboard thrusters. Maneuvers are detected by analyzing changes in orbital elements over time and identifying discontinuities that cannot be explained by natural orbital evolution.

## Maneuvers Table

The table displays all detected maneuvers with the following information:

| Column | Description |
|--------|-------------|
| **Event Time** | When the maneuver was detected to have occurred |
| **Status** | Verification status of the maneuver detection |
| **Magnitude** | Total velocity change (delta-v) in meters per second |
| **Radial** | Velocity change toward/away from Earth's center |
| **In-Track** | Velocity change along the direction of travel |
| **Cross-Track** | Velocity change perpendicular to the orbital plane |
| **Detected** | When the maneuver was identified by the system |

## Maneuver Status

Each maneuver has a verification status:

| Status | Description |
|--------|-------------|
| **Verified** | Maneuver has been confirmed through multiple data sources or analyst review |
| **Unverified** | Maneuver has been detected but not yet confirmed |
| **Rejected** | Detection was determined to be a false positive |

## Status Filter

Use the status dropdown to filter the table:

- **All** - Show all detected maneuvers
- **Verified** - Show only confirmed maneuvers
- **Unverified** - Show maneuvers pending verification
- **Rejected** - Show rejected detections

## Understanding Maneuver Components

### Magnitude

The total magnitude represents the overall velocity change (delta-v) required for the maneuver. Larger values indicate more significant orbital changes.

### Radial Component

Radial maneuvers change the orbit's shape (eccentricity) and altitude:

- **Positive radial** - Thrust away from Earth
- **Negative radial** - Thrust toward Earth

### In-Track Component

In-track maneuvers are the most common type and primarily affect orbital period and phase:

- **Positive in-track (prograde)** - Raises the orbit
- **Negative in-track (retrograde)** - Lowers the orbit

### Cross-Track Component

Cross-track maneuvers change the orbital plane:

- Used for inclination changes
- Used for RAAN adjustments
- Generally the most expensive in terms of fuel

## Use Cases

Maneuver detection supports:

- **Operational awareness** - Understanding when and how satellites change their orbits
- **Pattern analysis** - Identifying station-keeping schedules or operational patterns
- **Collision avoidance** - Recognizing when satellites maneuver in response to conjunction warnings
- **Tracking maintenance** - Knowing when orbital elements need updating after a maneuver

## Limitations

- Detection relies on sufficient observation data before and after the maneuver
- Small maneuvers may not be detectable if they fall within normal tracking uncertainty
- Timing precision depends on observation cadence around the event
