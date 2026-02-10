---
title: Close Approaches
nav_order: 11
parent: Details and Tools
grand_parent: Satellites
---

# Close Approaches

The Close Approaches tab provides a tool to calculate potential conjunctions between the satellite and other objects in orbit.

## Understanding Close Approaches

A close approach (or conjunction) occurs when two space objects pass near each other. Monitoring close approaches is critical for:

- **Collision avoidance** - Identifying potential collision risks
- **Situational awareness** - Understanding the satellite's orbital neighborhood
- **Maneuver planning** - Evaluating whether avoidance maneuvers may be needed
- **Tracking analysis** - Studying the behavior of nearby objects

{: .note }
> The Close Approaches tab is disabled for satellites that have decayed, as position predictions are no longer possible.

## Calculating Close Approaches

To calculate close approaches:

1. Navigate to the satellite's Close Approaches tab
2. Configure the calculation parameters
3. Select `CALCULATE` to run the analysis

### Calculation Parameters

| Field | Description |
|-------|-------------|
| **Time Range** | How many hours into the future to search (1-24 hours) |
| **Minimum Distance** | Distance threshold in kilometers (1-100 km) |

Only approaches where the objects come within the minimum distance are included in results.

### Running the Calculation

Select `CALCULATE` to find close approaches. The calculation propagates the orbits of the primary satellite and all cataloged objects to identify potential conjunctions.

## Close Approaches Results

Results are displayed in a table showing all identified conjunctions:

| Column | Description |
|--------|-------------|
| **Time of Closest Approach (TCA)** | When the objects are at minimum distance |
| **Secondary Object** | The other satellite or debris involved |
| **Miss Distance** | Minimum separation distance in kilometers |
| **Relative Velocity** | Closing speed at TCA |

### Interpreting Results

- **Very close approaches** (< 1 km) - Warrant careful attention and may require action
- **Moderate approaches** (1-10 km) - Should be monitored as predictions evolve
- **Distant approaches** (> 10 km) - Generally low concern but useful for awareness

### Secondary Object Details

Click on a secondary object name to navigate to its satellite detail page for more information about the approaching object.

## Limitations

Close approach calculations are based on:

- **Current orbital elements** - Predictions are only as accurate as the available element sets
- **Two-body propagation** - Simplified orbital mechanics (perturbations may affect actual trajectories)
- **Cataloged objects only** - Untracked debris is not included in the analysis

## Use Cases

| Scenario | Application |
|----------|-------------|
| **Active satellite operations** | Monitor for potential collision risks |
| **Debris tracking** | Understand collision probability for debris objects |
| **Constellation management** | Track approaches between constellation members |
| **Research** | Study orbital dynamics and space traffic patterns |
