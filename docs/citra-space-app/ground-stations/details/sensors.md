---
title: Sensors
nav_order: 2
parent: Details and Tools
grand_parent: Ground Stations
---

# Sensors

The Sensors section on the ground station detail page allows you to manage the observation equipment deployed at the station. Sensors represent the telescopes and antennas used for satellite tracking and data collection.

## Understanding Sensors

Ground stations typically host one or more sensors, each with specific capabilities for observing satellites. Citra Space supports two sensor types:

- **Telescope** - Optical instrument for visual or imaging observations of satellites
- **Antenna** - Radio frequency equipment for signal reception and transmission

Registering sensors at a ground station provides a complete picture of the station's observation capabilities.

## Viewing Sensors

The sensors grid lists all sensors configured at the ground station. Each entry shows the sensor's name, type, and relevant technical parameters.

## Adding a Sensor

To add a new sensor:

1. Select the `Add Sensor` button
2. Choose the sensor type (Telescope or Antenna)
3. Fill in the sensor details in the form
4. Save the new sensor

{: .note }
> The available form fields vary depending on the sensor type selected. See [Telescopes](../../sensors/telescopes/) for the full list of telescope configuration fields or [Antennas](../../sensors/antennas/) for antenna configuration fields.

## Editing a Sensor

To edit an existing sensor:

1. Select the edit button on the sensor you want to modify
2. Update the sensor details in the form
3. Save your changes

## Deleting a Sensor

To delete a sensor:

1. Select the delete button on the sensor you want to remove
2. Confirm the deletion in the confirmation dialog

{: .important }
> Deleting a sensor is permanent and cannot be undone.

## Use Cases

Sensor management supports:

- **Equipment inventory** - Maintaining an accurate record of observation hardware at each site
- **Capability assessment** - Understanding what types of observations each station can perform
- **Observation planning** - Matching sensor capabilities to satellite tracking requirements
