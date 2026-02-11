---
title: Find Satellite Passes
nav_order: 1
parent: Details and Tools
grand_parent: Ground Stations
---

# Find Satellite Passes

The Calculate Access section on the ground station detail page determines when satellites will be visible from the station's location. This tool computes pass windows based on orbital elements, geographic position, and observation constraints.

## Understanding Satellite Passes

A satellite pass (also called an "access window") is the period during which a satellite is above the local horizon with sufficient elevation for observation from a ground station. Each pass begins at Acquisition of Signal (AOS) when the satellite rises above the minimum elevation threshold, and ends at Loss of Signal (LOS) when it drops below that threshold.

Pass characteristics depend on the satellite's orbit, the ground station's geographic position, and the constraints you define.

## Calculation Parameters

### Time Range

| Field | Description |
|-------|-------------|
| **Start** | Beginning of the search window (UTC) |
| **Stop** | End of the search window (UTC) |

### Constraints

| Field | Description |
|-------|-------------|
| **Minimum Elevation** | Minimum elevation angle above the horizon in degrees. Higher values filter out low-horizon passes that may have poor signal quality or atmospheric interference |
| **Minimum Duration** | Minimum pass duration in seconds. Filters out brief passes that may not provide enough time for observation |

### Satellite Selection

Select one or more satellites to include in the access calculation. You can search by name or NORAD ID to find specific objects.

## Running the Calculation

1. Configure the time range, constraints, and satellite selection
2. Select `SOLVE` to run the calculation
3. Wait for the computation to complete (a progress indicator is displayed during processing)

{: .note }
> Calculation time depends on the length of the time range and the number of satellites selected. Longer time ranges and more satellites will take longer to compute.

## Results

The results table displays all computed pass windows:

| Column | Description |
|--------|-------------|
| **Satellite** | Name of the satellite |
| **AOS** | Acquisition of Signal - when the satellite rises above minimum elevation (UTC) |
| **LOS** | Loss of Signal - when the satellite drops below minimum elevation (UTC) |
| **Duration** | Total pass duration |
| **Max Elevation** | Peak elevation angle during the pass in degrees |

## Reset

Select `RESET` to clear all parameters and results, returning the form to its default state.

## Use Cases

Satellite pass calculation supports:

- **Observation scheduling** - Identifying upcoming windows to point sensors at a satellite
- **Pass selection** - Choosing high-elevation passes for better observation conditions
- **Collection planning** - Determining optimal times for data collection from specific satellites
- **Multi-satellite monitoring** - Planning observation schedules across multiple objects
