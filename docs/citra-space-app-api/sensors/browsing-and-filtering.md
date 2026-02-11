---
title: Browsing and Filtering
nav_order: 1
parent: Sensors
---

# Browsing and Filtering

The Sensors page displays a unified list of all sensors (telescopes and antennas) available to you. Use this page to browse, create, and manage your observation equipment.

## Understanding the Sensors List

Sensors represent the individual pieces of observation equipment deployed at your ground stations. The sensors list provides a central view of all equipment regardless of which ground station it belongs to, making it easy to assess your overall observation capabilities.

## Quick Search

The search bar at the top of the sensors list filters sensors as you type, making it easy to locate a specific instrument.

## Columns

The sensors list displays the following columns:

| Column | Description |
|--------|-------------|
| **Name** | Sensor name with a telescope or antenna icon indicating the type (click to navigate to the detail page) |
| **Type** | Sensor type — Telescope or Antenna |
| **Status** | Current connection status displayed as a color-coded chip (Online or Offline) |
| **Last Connection** | Timestamp of the most recent connection, or "Never" if the sensor has not connected |
| **Actions** | Edit and delete buttons (visible only to the sensor owner) |

## Creating a Sensor

To create a new sensor:

1. Select the `Add Sensor` button in the toolbar
2. Choose the sensor type (Telescope or Antenna) in the side panel
3. Fill in the configuration fields for the selected type
4. Save the new sensor

{: .note }
> The available form fields depend on the sensor type selected. See [Telescopes](telescopes/) for telescope configuration fields or [Antennas](antennas/) for antenna configuration fields.

## Editing a Sensor

Select the edit button in the Actions column to open the configuration form pre-filled with the sensor's current values. Make your changes and save.

{: .important }
> Edit and delete actions are only available for sensors that you own.

## Deleting a Sensor

Select the delete button in the Actions column to remove a sensor. A confirmation dialog will appear before the sensor is permanently deleted.

## Navigating to Details

Click a sensor name in the list to open its detail page, where you can view technical specifications, manage tasking schedules, and work with observation data. See [Telescopes](telescopes/) or [Antennas](antennas/) for more information on each detail page.
