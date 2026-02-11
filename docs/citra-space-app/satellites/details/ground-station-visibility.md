---
title: Ground Station Visibility
nav_order: 7
parent: Details and Tools
grand_parent: Satellites
---

# Ground Station Visibility

The Visibility tab provides a tool to calculate when and where the satellite will be visible from ground stations around the world.

## Understanding Visibility

Satellite visibility (also called "access") refers to the time windows when a satellite passes above a ground station's horizon with sufficient elevation for observation. This tool helps operators plan observation schedules by identifying upcoming visibility windows.

{: .note }
> The Visibility tab is disabled for satellites that have decayed, as position predictions are no longer possible.

## Calculating Visibility

To calculate ground station visibility:

1. Navigate to the satellite's Visibility tab
2. Configure the calculation parameters
3. Select `SOLVE` to run the calculation

### Calculation Parameters

#### Time Range

| Field | Description |
|-------|-------------|
| **Start** | Beginning of the search window (UTC) |
| **Stop** | End of the search window (UTC) |

#### Constraints

| Field | Description |
|-------|-------------|
| **Minimum Duration** | Minimum pass duration to include in results (seconds) |
| **Minimum Elevation** | Minimum elevation angle above horizon (degrees) |

Higher minimum elevation values filter out low-horizon passes that may have poor signal quality or atmospheric interference.

#### Ground Station Filter

Select which ground stations to include in the calculation:

- **All Ground Stations** - Calculate visibility for all registered ground stations
- **Specific Ground Stations** - Select one or more ground stations from the list

### Running the Calculation

Select `SOLVE` to calculate visibility windows. The calculation may take a few seconds depending on the time range and number of ground stations.

Select `RESET` to clear parameters and results.

## Visibility Results

Results are displayed in an interactive format showing:

### Results Table

| Column | Description |
|--------|-------------|
| **Ground Station** | The ground station with visibility |
| **AOS (Acquisition of Signal)** | When the satellite rises above minimum elevation |
| **LOS (Loss of Signal)** | When the satellite drops below minimum elevation |
| **Duration** | Total pass duration |
| **Max Elevation** | Peak elevation angle during the pass |

### Sky Plot

For individual passes, a sky plot shows the satellite's path across the sky as seen from the ground station:

- **Azimuth** - Compass direction (0° = North, 90° = East, 180° = South, 270° = West)
- **Elevation** - Angle above the horizon (0° = horizon, 90° = directly overhead)
- **Pass trajectory** - The path the satellite follows during the visibility window

## Use Cases

Ground station visibility calculations support:

- **Observation planning** - Identifying when to point sensors at the satellite
- **Pass selection** - Choosing high-elevation passes for better observation conditions
- **Multi-site coordination** - Planning handoffs between ground stations for continuous coverage
- **Tasking optimization** - Selecting the best ground stations for collection requests
