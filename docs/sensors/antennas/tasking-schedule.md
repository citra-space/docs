---
title: Tasking Schedule
nav_order: 1
parent: Antennas
grand_parent: Sensors
---

# Tasking Schedule

The Tasking Schedule section on the antenna detail page displays all observation tasks assigned to this antenna. As an antenna owner, this is where you schedule tasks, upload RF capture results, and manage the task lifecycle.

## Understanding the Tasking Schedule

Tasks are observation assignments created from collection requests. Each task represents a scheduled window for the antenna to collect radio frequency data from a specific satellite. The antenna detail page is the sensor-owner's operational view — where you take action on tasks assigned to your equipment.

{: .note }
> The [satellite-level tasking schedule](../../satellites/details/tasking-schedule.md) shows tasks aggregated across all sensors for a given satellite. The antenna-level view here shows tasks assigned specifically to this antenna and provides owner actions for fulfilling them.

## Viewing Tasks

Tasks are displayed in two tabs:

### Upcoming Tab

Shows tasks with end times in the future. Sorted by task start time (earliest first).

### Historical Tab

Shows tasks with end times in the past. Sorted by task start time (most recent first).

## Tasking Schedule Grid

| Column | Description |
|--------|-------------|
| **Satellite** | The satellite to be observed |
| **Task Start** | When the observation window begins |
| **Task Stop** | When the observation window ends |
| **Type** | Observation type (TDOA) |
| **Status** | Current task status |
| **Requested By** | User who created the original collection request |
| **Ground Station** | The ground station where this antenna is located |
| **Actions** | Available actions based on task status and your role |

## Task Status

Tasks progress through the following statuses:

| Status | Description |
|--------|-------------|
| **Pending** | Task is waiting to be scheduled by the antenna owner |
| **Scheduled** | Task has been confirmed and is awaiting execution |
| **Succeeded** | Task was completed successfully with results available |
| **Failed** | Task could not be completed |
| **Canceled** | Task was canceled before completion |

## Owner Actions

As the antenna owner, you can perform the following actions on tasks:

### Schedule a Task

For tasks in Pending status, select the schedule action to confirm the task. This moves the task to Scheduled status, indicating that the antenna will collect data during the specified window.

### Upload Results

For tasks in Scheduled status, select the upload action to submit RF capture data. The upload accepts `.json` files with a maximum size of 20 MB.

1. Select the upload action on a scheduled task
2. Choose the JSON file from your local system
3. Submit the upload

The task moves to Succeeded status once the upload is processed successfully.

### Cancel a Task

For tasks in Pending or Scheduled status, the antenna owner or the original requester can cancel the task. Select the cancel action and confirm in the dialog.

### View Results

For tasks in Succeeded status, select `VIEW RESULTS` to open the RF capture results panel. This displays the collected signal data for review.

## Use Cases

The antenna tasking schedule supports:

- **Task fulfillment** — Reviewing and scheduling pending RF observation requests
- **Data delivery** — Uploading JSON capture files for completed observations
- **Schedule management** — Monitoring upcoming and historical tasks to plan antenna operations
