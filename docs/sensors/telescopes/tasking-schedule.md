---
title: Tasking Schedule
nav_order: 1
parent: Telescopes
grand_parent: Sensors
---

# Tasking Schedule

The Tasking Schedule section on the telescope detail page displays all observation tasks assigned to this telescope. As a telescope owner, this is where you schedule tasks, upload observation results, and manage the task lifecycle.

## Understanding the Tasking Schedule

Tasks are observation assignments created from collection requests. Each task represents a scheduled window for the telescope to observe a specific satellite. The telescope detail page is the sensor-owner's operational view — where you take action on tasks assigned to your equipment.

{: .note }
> The [satellite-level tasking schedule](../../satellites/details/tasking-schedule.md) shows tasks aggregated across all sensors for a given satellite. The telescope-level view here shows tasks assigned specifically to this telescope and provides owner actions for fulfilling them.

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
| **Type** | Observation type (Optical) |
| **Status** | Current task status |
| **Filter** | Optical filter assigned for the observation |
| **Requested By** | User who created the original collection request |
| **Satellite Name** | The satellite to be observed |
| **Actions** | Available actions based on task status and your role |

## Task Status

Tasks progress through the following statuses:

| Status | Description |
|--------|-------------|
| **Pending** | Task is waiting to be scheduled by the telescope owner |
| **Scheduled** | Task has been confirmed and is awaiting execution |
| **Succeeded** | Task was completed successfully with results available |
| **Failed** | Task could not be completed |
| **Canceled** | Task was canceled before completion |

## Owner Actions

As the telescope owner, you can perform the following actions on tasks:

### Schedule a Task

For tasks in Pending status, select the schedule action to confirm the task. This moves the task to Scheduled status, indicating that the telescope will perform the observation during the specified window.

### Upload Results

For tasks in Scheduled status, select the upload action to submit observation data. The upload accepts FITS files with the following extensions: `.fits`, `.fit`, `.fts`.

1. Select the upload action on a scheduled task
2. Choose the FITS file from your local system
3. Submit the upload

The task moves to Succeeded status once the upload is processed successfully.

### Cancel a Task

For tasks in Pending or Scheduled status, the telescope owner or the original requester can cancel the task. Select the cancel action and confirm in the dialog.

### View Results

For tasks in Succeeded status, select `VIEW RESULTS` to open the image results panel. This displays the captured observation with options to view in the FITS viewer or download data.

## Use Cases

The telescope tasking schedule supports:

- **Task fulfillment** — Reviewing and scheduling pending observation requests
- **Data delivery** — Uploading FITS files for completed observations
- **Schedule management** — Monitoring upcoming and historical tasks to plan telescope operations
