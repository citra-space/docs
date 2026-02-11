---
title: Tasking Schedule
nav_order: 6
parent: Details and Tools
grand_parent: Satellites
---

# Tasking Schedule

The Tasking Schedule section on the Tasking tab displays all observation tasks scheduled for the satellite across all sensors.

## Understanding the Tasking Schedule

Tasks are specific observation assignments created from collection requests. Each task represents a scheduled window for a sensor to observe the satellite. Tasks can be fulfilled manually through the UI or automated using the Citra API.

## Viewing Tasks

Tasks are displayed in two tabs:

### Upcoming Tab

Shows tasks with end times in the future. Sorted by task start time (earliest first).

### Historical Tab

Shows tasks with end times in the past. Sorted by task start time (most recent first).

## Tasking Schedule Grid

| Column | Description |
|--------|-------------|
| **Task Start** | When the observation window begins |
| **Task Stop** | When the observation window ends |
| **Type** | Observation type (Optical or TDOA) |
| **Status** | Current task status |
| **Filter** | Optical filter assigned (for telescope tasks) |
| **Requested By** | User who created the original collection request |
| **Ground Station** | The ground station assigned to the task |
| **Sensor** | The telescope or antenna assigned to perform the observation |
| **Actions** | Available actions based on task status |

## Task Status

Tasks progress through the following statuses:

| Status | Description |
|--------|-------------|
| **Pending** | Task is waiting to be scheduled |
| **Scheduled** | Task has been assigned to a sensor and is awaiting execution |
| **Succeeded** | Task was completed successfully with results available |
| **Failed** | Task could not be completed |
| **Canceled** | Task was canceled before completion |

## Task Actions

### Cancel Task

For tasks in Pending or Scheduled status, the task creator can cancel the task by selecting the cancel icon. A confirmation dialog will appear before the task is canceled.

{: .note }
> Only the user who created the original collection request can cancel pending or scheduled tasks.

### View Results

For tasks with Succeeded status, select `VIEW RESULTS` to open the results panel:

- **Telescope tasks** - Opens the image results panel showing captured observations, with options to view images in the FITS viewer or download data
- **Antenna tasks** - Opens the RF capture results panel showing collected signal data

## Decayed Satellites

For satellites that have decayed (re-entered Earth's atmosphere):

- No new tasks can be created
- The decay date is displayed when viewing an empty upcoming tasks list
- Historical tasks remain available for review
