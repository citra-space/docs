---
title: RF Captures
nav_order: 2
parent: Antennas
grand_parent: Sensors
---

# RF Captures

The RF Captures section on the antenna detail page displays all radio frequency capture data collected by this antenna. As an antenna owner, this is where you manage your captured signal data.

## Understanding RF Captures

RF captures are recordings of radio signals transmitted by or reflected from satellites during scheduled observation tasks. This antenna-level view shows captures from this specific instrument, whereas the [satellite-level RF captures page](../../satellites/details/rf-captures.md) shows captures aggregated from all antennas that have observed a given satellite.

## RF Captures Grid

The captures are displayed in a searchable grid showing all RF data collected by this antenna. Use the search bar to filter captures by name or other attributes.

## Uploading RF Captures

RF capture data can be uploaded directly from this section or through the tasking schedule when fulfilling a scheduled task.

Upload requirements:

- **File format** — `.json` files only
- **Maximum size** — 20 MB per file
- **Antenna validation** — The capture data must reference this antenna's ID

To upload a new capture:

1. Select the upload action
2. Choose the JSON file from your local system
3. Submit the upload

{: .note }
> RF captures are typically uploaded through the [Tasking Schedule](tasking-schedule.md) when fulfilling a scheduled task. Direct uploads from this section follow the same file requirements.

## Use Cases

Antenna RF captures support:

- **Signal analysis** — Reviewing collected RF data for signal characterization
- **Data management** — Organizing and maintaining the antenna's capture archive
- **Cross-referencing** — Comparing captures with satellite-level aggregated data on the [satellite RF captures page](../../satellites/details/rf-captures.md)
