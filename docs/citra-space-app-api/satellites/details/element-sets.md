---
title: Element Sets
nav_order: 10
parent: Details and Tools
grand_parent: Satellites
---

# Element Sets

The Element Sets section on the Orbital Analysis tab displays a grid of all orbital element sets (elsets) associated with the satellite.

## Understanding Element Sets

An element set (elset) is a collection of orbital parameters that describe a satellite's orbit at a specific point in time (the epoch). Element sets are used to predict satellite positions for ground track visualization, visibility calculations, and observation planning.

## Element Sets Grid

The grid displays elsets in a searchable, sortable table:

| Column | Description |
|--------|-------------|
| **Epoch** | The reference time for the orbital elements |
| **Type** | Propagation type (e.g., SGP4 with Kozai mean motion, SGP4-XP with Brouwer mean motion) |
| **Source** | The data provider or user who created the elset |
| **Review Status** | Approval status (Approved, Pending, Rejected) |
| **Semi-Major Axis** | Orbit size in kilometers |
| **Eccentricity** | Orbit shape (0 = circular, approaching 1 = highly elliptical) |
| **Inclination** | Orbit tilt in degrees |
| **RAAN** | Right Ascension of Ascending Node in degrees |
| **Arg of Perigee** | Argument of perigee in degrees |
| **Mean Anomaly** | Position along the orbit in degrees |
| **Actions** | Available actions for the elset |

## Elset Types

| Type | Description |
|------|-------------|
| **SGP4 with Kozai mean motion** | Standard SGP4 propagation using Kozai mean elements, typically from Space-Track GP data |
| **SGP4 with Brouwer mean motion** | SGP4 propagation using Brouwer mean elements |
| **SGP4-XP with Brouwer mean motion** | Extended Precision SGP4 propagation using Brouwer mean elements |

## Selecting an Element Set

Click on any row to select that elset:

- The selected elset is highlighted in the grid
- The Observation Residuals chart updates to display residuals for the selected elset
- The Orbital Elements History charts highlight the selected elset's data point

{: .note }
> Selecting an elset is useful for examining how well it fits the observation data in the residuals chart.

## Viewing Residuals

When observation data is available, selecting an elset shows residual indicators:

- **Green checkmark** - Elset has residuals data available
- Clicking an elset with residuals scrolls the Observation Residuals section into view

## Rejecting Element Sets

Authenticated users can reject element sets that they have access to:

1. Select an elset from the grid
2. Select the reject action (trash icon)
3. Confirm the rejection in the dialog

Rejected elsets:
- Are marked with "Rejected" status
- Are excluded from approved satellite data
- Remain visible for historical reference (Government+ users can filter to view them)

## Creating New Element Sets

To create a new element set:

1. Configure the observation time range in the Observation Residuals section
2. Select `CREATE ELSET` to open the Element Set Creation Wizard
3. Follow the wizard steps to fit orbital elements to the observation data
4. Submit the new elset for review

The newly created elset will appear in the grid after successful creation.

## Related Sections

- [Observation Residuals](observation-residuals) - Evaluate elset accuracy against observations
- [Orbital Elements History](orbital-elements) - Visualize orbital parameter evolution over time
