---
title: Details and Tools
nav_order: 2
parent: Satellites
has_children: true
---

# Satellite Details and Tools

The satellite detail page provides comprehensive information about a specific satellite including orbital data, observation history, tasking capabilities, and analysis tools. Access any satellite's detail page by selecting a satellite from the [Satellites](https://app.citra.space/satellites) list.

## Page Structure

The satellite detail page is organized into seven tabs:

| Tab | Description |
|-----|-------------|
| **Overview** | Satellite summary with ground track map, position data, aliases, and transmissions |
| **Observations** | RF captures and image uploads associated with the satellite |
| **Tasking** | Collection requests and scheduled observation tasks |
| **Visibility** | Calculate when the satellite is visible from ground stations |
| **Orbital Analysis** | Observation residuals, orbital element history, and element sets |
| **Close Approaches** | Find potential conjunctions with other satellites |
| **Maneuvers** | Detected orbital maneuvers and status history |

{: .note }
> Some tabs are disabled for satellites that have decayed (re-entered Earth's atmosphere). The Visibility and Close Approaches tabs require an active satellite with valid orbital elements.

## Overview Tab

The Overview tab is the default view when navigating to a satellite detail page. It displays key satellite information at a glance.

### Ground Track Map

The ground track map shows the satellite's current and predicted orbital path projected onto Earth's surface. The map displays:

- **Ground track line** - The satellite's trajectory over the next orbital period
- **Current position** - Real-time satellite location updated as the satellite moves
- **Orbital direction** - Visual indication of the satellite's direction of travel

### Satellite Summary Card

Overlaid on the ground track map (or displayed above on mobile devices), the satellite summary card provides quick-reference information:

- **Satellite name and type** (Payload, Rocket Body, or Debris)
- **Sensor capabilities** - For reconnaissance satellites: EO (Electro-Optical), IR (Infrared), SAR (Synthetic Aperture Radar), or SIGINT (Signals Intelligence)
- **Orbit regime** - LEO (Low Earth Orbit), MEO (Medium Earth Orbit), GEO (Geostationary), HEO (Highly Elliptical Orbit), etc.
- **Current position** - Real-time latitude, longitude, and altitude
- **Country of origin** - Operating country with flag indicator
- **Launch site** - Where the satellite was launched from
- **Launch date** - When the satellite was launched and time in orbit
- **Orbit data freshness** - How recently the orbital elements were updated

### Elset Source Information

Below the ground track map, source information displays details about the orbital element set (elset) used for the ground track calculation:

- **Elset epoch** - The reference time for the orbital elements
- **Elset type** - The type of element set (e.g., TLE, state vector)
- **Source** - The data provider or user who contributed the elset
- **Review status** - Approval status for the elset (if applicable)

## Status Badge

For satellites that are pending review or have been rejected, a status badge appears in the page header next to the satellite name. This indicates the current review status of the satellite record.

## Satellite Group Management

The satellite group management icon in the page header allows you to add or remove the satellite from your custom satellite groups for organizing and tracking satellites of interest.
