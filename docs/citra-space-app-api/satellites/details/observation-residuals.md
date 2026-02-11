---
title: Observation Residuals
nav_order: 8
parent: Details and Tools
grand_parent: Satellites
---

# Observation Residuals

The Observation Residuals section on the Orbital Analysis tab displays the difference between predicted and observed satellite positions, helping analysts evaluate orbital element quality.

## Understanding Residuals

Residuals measure the difference between where orbital elements predict a satellite should be and where it was actually observed by telescopes. Small, consistent residuals indicate accurate orbital predictions, while large or growing residuals suggest the orbital elements may be stale or inaccurate.

### Residual Components

The chart displays multiple error components:

| Component | Description |
|-----------|-------------|
| **Total Error** | The 3D distance between predicted and observed positions |
| **Radial** | Error in the direction toward/away from Earth's center |
| **In-Track** | Error along the satellite's direction of travel |
| **Cross-Track** | Error perpendicular to the orbital plane |

### Key Insights

- **Small consistent residuals** - Orbital elements are accurate and predictions are reliable
- **Sudden jumps in residuals** - May indicate an orbital maneuver occurred
- **Growing residuals over time** - Suggests orbital elements are becoming stale and need updating
- **Large in-track errors** - Often indicate timing or drag modeling issues
- **Large cross-track errors** - May indicate perturbation modeling issues

## Observation Time Range

Configure the time range for residual analysis:

### Date Pickers

| Field | Description |
|-------|-------------|
| **Start (UTC)** | Beginning of the observation window |
| **End (UTC)** | End of the observation window |

### Quick Select Buttons

| Button | Description |
|--------|-------------|
| **First Available** | Set start to the earliest observation in the database |
| **Last Available** | Set end to the most recent observation |
| **Last 5 Days** | Quick preset for recent data |
| **10** | Last 10 days |
| **15** | Last 15 days |

### Pin Time Range

Enable `Pin time range` to prevent the observation window from automatically adjusting when selecting different element sets. This is useful when comparing multiple elsets against the same observation period.

## Status Filter

{: .note }
> The status filter is available to Government tier users and above.

For Government+ users, a status filter allows viewing residuals calculated against observations with different review statuses:

- **Approved** - Only approved observations (default for all users)
- **Pending** - Observations awaiting review
- **Rejected** - Observations that were rejected

Standard users only see approved observations in the residuals chart.

## Residuals Chart

The interactive chart displays residuals over time:

- **X-axis** - Observation time
- **Y-axis** - Residual magnitude (kilometers)
- **Data points** - Individual observations with residual values
- **Selected elset marker** - Vertical line indicating the selected element set epoch

Hover over data points to see detailed residual values.

## Element Set Selection

Residuals are calculated against a specific element set. The currently selected elset is highlighted in the chart and in the Element Sets grid below.

To select a different elset:
- Click on an elset in the Element Sets grid
- Click on an elset marker in the Orbital Elements History charts

## Creating New Element Sets

Select `CREATE ELSET` to open the Element Set Creation Wizard, which guides you through the process of fitting new orbital elements to the observation data in the current time range.

## Rejecting Element Sets

Authenticated users can reject element sets that they have access to:

1. Select an elset from the grid
2. Select `REJECT ELSET`
3. Confirm the rejection in the dialog

Rejected elsets are marked with a "Rejected" status and excluded from approved satellite data.

{: .note }
> Government tier users and above can view and filter by rejected and pending elsets. Standard users only see approved elsets.
